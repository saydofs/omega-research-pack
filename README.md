# Omega Research Pack v4

**Author:** Mohamed Sayed  
**Affiliation:** Independent Researcher  
**Project:** Omega / The Universe That Never Repeats  
**Related working preprint:**  
*The Universe That Never Repeats: Omega-NR — Exact Physical Non-Repetition, Accumulated Change, and a Testable Quantum-Geometric Extension*  
**DOI:** 10.5281/zenodo.23624320

## Overview

Omega Research Pack v4 is a research software prototype implementing and testing
operational projections derived from the Omega-NR framework.

The package contains two main experimental tracks:

1. **Omega Core v4**
   - accumulated global path length
   - accumulated local path length
   - Omega irreversibility index
   - reversal-rate statistics
   - path-efficiency quantities
   - multivariate robust metric calibration

2. **Omega Life-Key v4**
   - research prototype for history-bound key evolution
   - robust projection of physical history
   - forward key evolution using HKDF
   - device-binding placeholder
   - simulations for clone divergence, replay, rollback, sensor-history replay,
     drift, and measurement noise

## Core operational quantities

For a state trajectory X:

\[
A_g(n)=\sum_{k=1}^{n} d_G(X_k,X_{k-1})
\]

\[
A_l(n;W)=\sum_{k=n-W+1}^{n} d_G(X_k,X_{k-1})
\]

\[
\mathcal I_\Omega
=
1-
\frac{d_G(X_{n-W},X_n)}{A_l}
\]

with:

$$
0 \le \mathcal I_\Omega \le 1
$$

The multivariate metric is:

$$
d_G(x,y)=\sqrt{(x-y)^T G(x-y)}
$$

where the operational diagonal metric is calibrated from training/reference data only.

## Research status

This repository is a **research prototype**.

It does **not** claim:
- production cryptographic security,
- independent security audit,
- that Omega history is secret entropy,
- that Omega Core universally improves forecasting,
- physical unclonability without a hardware-bound root of trust.

Important negative controls are retained intentionally.

In particular, if an attacker possesses the same secret, the same device binding,
and reproduces the exact operational history, the software-only construction
derives the same key. Strong clone resistance therefore requires a hardware-bound
identity such as a secure element, PUF-like root, or equivalent trusted hardware.

## Reproducibility

Run the mathematical tests:

```bash
python -m unittest test_omega_v4.py -v
```

Run the attack simulation:

```bash
python attack_suite_v4.py
```

Run the available real time-series benchmark:

```bash
python benchmark_real.py
```

For a CSV sensor dataset:

```bash
python sensor_csv_adapter.py your_data.csv --columns temperature,pressure,vibration
```

## Files

- `omega_v4.py` — Omega Core v4 and Omega Life-Key v4 implementation
- `attack_suite_v4.py` — adversarial and robustness simulations
- `benchmark_real.py` — temporal holdout benchmark
- `sensor_csv_adapter.py` — numeric sensor CSV adapter
- `test_omega_v4.py` — invariant/unit tests
- `results_attack_suite.json` — attack-suite outputs
- `results_real_benchmark.json` — benchmark outputs
- `benchmark_summary.csv` — compact benchmark table
- `operating_profiles.json` — tested projection profiles
- `tuning_v4.json` — projection tuning results
- `OMEGA_V4_RESULTS.json` — combined results artifact
- `CITATION.cff` — citation metadata
- `LICENSE` — software license
- `CHANGELOG.md` — version history
- `zenodo_metadata.json` — metadata prepared for repository deposit

## Citation

Please cite the software record using the Zenodo DOI below. The conceptual framework is currently represented by the related working preprint:

Mohamed Sayed, *The Universe That Never Repeats: Omega-NR — Exact Physical Non-Repetition, Accumulated Change, and a Testable Quantum-Geometric Extension*, Zenodo, 2026. DOI: 10.5281/zenodo.23624320.

Software DOI: 10.5281/zenodo.23637375
Concept DOI: 10.5281/zenodo.23637374

## License

MIT License. See `LICENSE`.

## Disclaimer

This code is provided for research and reproducibility. It must not be used as a
drop-in production authentication or cryptographic system without independent
security review, hardware threat modeling, and implementation hardening.
