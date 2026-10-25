
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Sequence, Tuple, List, Optional, Dict
import hashlib, hmac, math, statistics

EPS = 1e-12

def _vec(x):
    if isinstance(x, (int, float)):
        return (float(x),)
    return tuple(float(v) for v in x)

def _mad(xs):
    if not xs:
        return 1.0
    med = statistics.median(xs)
    mad = statistics.median(abs(x-med) for x in xs)
    return mad if mad > EPS else 1.0

@dataclass
class RobustMetric:
    """
    Diagonal metric learned from TRAINING data only.
    Scale is robust MAD of first differences for each channel.
    """
    scales: Optional[Tuple[float, ...]] = None

    def fit(self, X: Sequence[Sequence[float] | float]):
        V = [_vec(x) for x in X]
        d = len(V[0])
        diffs = [[] for _ in range(d)]
        for i in range(1, len(V)):
            for j in range(d):
                diffs[j].append(V[i][j] - V[i-1][j])
        self.scales = tuple(max(_mad(col), 1e-6) for col in diffs)
        return self

    def distance(self, a, b) -> float:
        a, b = _vec(a), _vec(b)
        if self.scales is None:
            scales = (1.0,) * len(a)
        else:
            scales = self.scales
        return math.sqrt(sum(((x-y)/s)**2 for x,y,s in zip(a,b,scales)))

@dataclass
class OmegaCoreStateV4:
    A_global: float
    A_local: float
    irreversibility: float
    reversal_rate: float
    A_rate: float
    channel_reversal_mean: float
    channel_reversal_max: float
    path_efficiency: float

    def as_tuple(self):
        return (
            self.A_global, self.A_local, self.irreversibility,
            self.reversal_rate, self.A_rate,
            self.channel_reversal_mean, self.channel_reversal_max,
            self.path_efficiency
        )

@dataclass
class OmegaCoreV4:
    window: int = 20
    metric: RobustMetric = field(default_factory=RobustMetric)
    history: List[Tuple[float, ...]] = field(default_factory=list)
    A_global: float = 0.0

    def _channel_reversals(self, loc):
        if len(loc) < 3:
            return [0.0] * len(loc[0])
        d = len(loc[0])
        rates = []
        for j in range(d):
            prev = 0
            rev = 0
            usable = 0
            for i in range(1, len(loc)):
                z = loc[i][j] - loc[i-1][j]
                s = 1 if z > 0 else (-1 if z < 0 else 0)
                if s == 0:
                    continue
                if prev != 0:
                    usable += 1
                    if s != prev:
                        rev += 1
                prev = s
            rates.append(rev / usable if usable else 0.0)
        return rates

    def update(self, x) -> OmegaCoreStateV4:
        x = _vec(x)
        if self.history:
            self.A_global += self.metric.distance(self.history[-1], x)
        self.history.append(x)
        n = len(self.history)
        start = max(0, n - self.window)
        loc = self.history[start:]
        A_local = sum(self.metric.distance(loc[i-1], loc[i]) for i in range(1,len(loc)))
        D = self.metric.distance(loc[0], loc[-1]) if len(loc) >= 2 else 0.0
        I = 0.0 if A_local <= EPS else 1.0 - D/A_local
        I = min(1.0, max(0.0, I))
        eff = 1.0 if A_local <= EPS else min(1.0, max(0.0, D/A_local))
        rates = self._channel_reversals(loc)
        rev_mean = sum(rates)/len(rates) if rates else 0.0
        rev_max = max(rates) if rates else 0.0
        # For scalar data reversal_rate == channel mean.
        reversal_rate = rev_mean
        A_rate = self.A_global / max(1, n-1)
        return OmegaCoreStateV4(
            self.A_global, A_local, I, reversal_rate, A_rate,
            rev_mean, rev_max, eff
        )

@dataclass
class CalibratedProjector:
    """
    Robust operational projection learned on training/reference states.
    Bin widths are k * MAD(feature values).
    Includes hysteresis for stability.
    """
    widths: Optional[Tuple[float, ...]] = None
    k: float = 2.5
    hysteresis: float = 0.35
    last: Optional[Tuple[int, ...]] = None

    def fit(self, states: Sequence[OmegaCoreStateV4]):
        cols = list(zip(*(s.as_tuple() for s in states)))
        widths = []
        for c in cols:
            w = self.k * _mad(list(c))
            widths.append(max(w, 1e-6))
        self.widths = tuple(widths)
        return self

    def project(self, s: OmegaCoreStateV4) -> Tuple[int, ...]:
        vals = s.as_tuple()
        if self.widths is None:
            self.widths = tuple(0.1 for _ in vals)
        raw = tuple(int(round(v/w)) for v,w in zip(vals,self.widths))
        if self.last is None:
            self.last = raw
            return raw
        out = []
        for v,w,r,p in zip(vals,self.widths,raw,self.last):
            center = p*w
            half = (0.5+self.hysteresis)*w
            out.append(p if center-half <= v <= center+half else r)
        self.last = tuple(out)
        return self.last

    def encode(self, s):
        return "|".join(map(str,self.project(s))).encode()

def hkdf_extract(salt, ikm):
    return hmac.new(salt, ikm, hashlib.sha256).digest()

def hkdf_expand(prk, info, length=32):
    out=b""; t=b""; c=1
    while len(out) < length:
        t = hmac.new(prk, t+info+bytes([c]), hashlib.sha256).digest()
        out += t; c += 1
    return out[:length]

def hkdf(ikm, salt, info, length=32):
    return hkdf_expand(hkdf_extract(salt,ikm), info, length)

@dataclass
class OmegaLifeKeyV4:
    """
    Research construction.
    NOT a production cryptographic primitive.

    Security root:
      secret + device_binding
    Context binding:
      robust Omega projection
    Forward evolution:
      previous key + counter + HKDF
    """
    secret: bytes
    device_binding: bytes
    key: bytes
    projector: CalibratedProjector
    counter: int = 0

    def evolve(self, state: OmegaCoreStateV4) -> bytes:
        self.counter += 1
        z = self.projector.encode(state)
        ikm = self.key + self.secret + self.device_binding + z
        self.key = hkdf(
            ikm,
            self.counter.to_bytes(8,"big"),
            b"Omega-Life-Key-v4",
            32
        )
        return self.key

    def authenticate(self, nonce: bytes, payload: bytes=b"") -> bytes:
        msg = b"OLK4|" + self.counter.to_bytes(8,"big") + nonce + payload
        return hmac.new(self.key, msg, hashlib.sha256).digest()

    def verify(self, nonce: bytes, tag: bytes, payload: bytes=b"") -> bool:
        return hmac.compare_digest(self.authenticate(nonce,payload), tag)
