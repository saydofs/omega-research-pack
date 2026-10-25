
import json, math, copy
from pathlib import Path
from omega_v4 import RobustMetric, OmegaCoreV4, CalibratedProjector, OmegaLifeKeyV4

def sig(n=300, dims=4):
    out=[]
    for i in range(n):
        out.append(tuple(
            1 + 0.01*j - 0.0005*(j+1)*i
            + 0.04*math.sin(i/(5+j))
            + 0.01*math.sin(i/(2.1+j/3))
            for j in range(dims)
        ))
    return out

def perturb(X, amp=1e-4, drift=0.0):
    out=[]
    for i,row in enumerate(X):
        out.append(tuple(v+amp*math.sin((i+1)*(j+1)*1.713)+drift*i for j,v in enumerate(row)))
    return out

def calibrate(X, W=20):
    metric=RobustMetric().fit(X[:100])
    core=OmegaCoreV4(window=W,metric=metric)
    states=[core.update(x) for x in X[:100]]
    proj=CalibratedProjector(k=3.0,hysteresis=.35).fit(states)
    return metric,proj

def projection_match(X,Y):
    metric,p0=calibrate(X)
    p1=copy.deepcopy(p0); p2=copy.deepcopy(p0)
    c1=OmegaCoreV4(metric=metric); c2=OmegaCoreV4(metric=metric)
    m=0
    for a,b in zip(X,Y):
        m += int(p1.project(c1.update(a))==p2.project(c2.update(b)))
    return m/len(X)

def clone_key_divergence():
    X=sig(220); metric,p=calibrate(X)
    cr=OmegaCoreV4(metric=metric); cc=OmegaCoreV4(metric=metric)
    pr=copy.deepcopy(p); pc=copy.deepcopy(p)
    lr=OmegaLifeKeyV4(b"S"*32,b"PUF-A",b"K"*32,pr)
    lc=OmegaLifeKeyV4(b"S"*32,b"PUF-A",b"K"*32,pc)
    cut=110; first=None
    for i,x in enumerate(X):
        xc=x if i<=cut else tuple(v+0.003*math.sin(i/(2+j)) for j,v in enumerate(x))
        kr=lr.evolve(cr.update(x)); kc=lc.evolve(cc.update(xc))
        if i>cut and first is None and kr!=kc: first=i
    return {"clone_at":cut,"first_key_divergence":first,"diverged":first is not None}

def replay_and_rollback():
    X=sig(80); metric,p=calibrate(sig(150))
    core=OmegaCoreV4(metric=metric)
    life=OmegaLifeKeyV4(b"S"*32,b"PUF-A",b"K"*32,copy.deepcopy(p))
    old_tag=None
    for i,x in enumerate(X):
        life.evolve(core.update(x))
        if i==25: old_tag=life.authenticate(b"N1",b"OPEN")
    return {
        "old_nonce_tag_valid_with_new_nonce": life.verify(b"N2",old_tag,b"OPEN"),
        "old_state_tag_valid_now": life.verify(b"N1",old_tag,b"OPEN")
    }

def sensor_replay():
    X=sig(220); metric,p=calibrate(X)
    c1=OmegaCoreV4(metric=metric); c2=OmegaCoreV4(metric=metric)
    p1=copy.deepcopy(p); p2=copy.deepcopy(p)
    cut=120; same=0; total=0
    for i,x in enumerate(X):
        xr=x if i<=cut else X[i-40]
        z1=p1.project(c1.update(x)); z2=p2.project(c2.update(xr))
        if i>cut:
            total+=1; same += int(z1==z2)
    return {"detected_rate":1-same/max(1,total)}

def exact_history_negative_control():
    X=sig(160); metric,p=calibrate(X)
    c1=OmegaCoreV4(metric=metric); c2=OmegaCoreV4(metric=metric)
    l1=OmegaLifeKeyV4(b"S"*32,b"PUF-A",b"K"*32,copy.deepcopy(p))
    l2=OmegaLifeKeyV4(b"S"*32,b"PUF-A",b"K"*32,copy.deepcopy(p))
    same=0
    for x in X:
        same += int(l1.evolve(c1.update(x))==l2.evolve(c2.update(x)))
    return {"same_key_fraction":same/len(X)}

def different_device_binding():
    X=sig(80); metric,p=calibrate(sig(150))
    c1=OmegaCoreV4(metric=metric); c2=OmegaCoreV4(metric=metric)
    l1=OmegaLifeKeyV4(b"S"*32,b"PUF-A",b"K"*32,copy.deepcopy(p))
    l2=OmegaLifeKeyV4(b"S"*32,b"PUF-B",b"K"*32,copy.deepcopy(p))
    same=0
    for x in X:
        same += int(l1.evolve(c1.update(x))==l2.evolve(c2.update(x)))
    return {"same_key_fraction":same/len(X)}

if __name__=="__main__":
    X=sig()
    result={
        "noise_match": {
            "1e-5":projection_match(X,perturb(X,1e-5)),
            "1e-4":projection_match(X,perturb(X,1e-4)),
            "5e-4":projection_match(X,perturb(X,5e-4)),
            "1e-3":projection_match(X,perturb(X,1e-3)),
        },
        "drift_match":{
            "1e-7":projection_match(X,perturb(X,1e-4,1e-7)),
            "1e-6":projection_match(X,perturb(X,1e-4,1e-6)),
            "5e-6":projection_match(X,perturb(X,1e-4,5e-6)),
        },
        "clone":clone_key_divergence(),
        "replay_rollback":replay_and_rollback(),
        "sensor_replay":sensor_replay(),
        "exact_history_negative_control":exact_history_negative_control(),
        "different_device_binding":different_device_binding()
    }
    print(json.dumps(result,indent=2))
    Path("results_attack_suite.json").write_text(json.dumps(result,indent=2))
