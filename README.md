# Omega Research Pack v4

**Author:** Mohamed Sayed  
**Affiliation:** Independent Researcher  
**Project:** Omega / The Universe That Never Repeats  
**Related working preprint:**  
*The Universe That Never Repeats: Omega-NR — Exact Physical Non-Repetition, Accumulated Change, and a Testable Quantum-Geometric Extension*  
**DOI:** 10.5281/zenodo.23624320
> **Omega Interlevel Numbers** is maintained as a separate mathematical research extension in [`omega-interlevel-numbers/`](./omega-interlevel-numbers/).
## Overview

Omega Research Pack v4 is a research software prototype implementing and testing operational projections derived from the Omega-NR framework.

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

## Core Operational Quantities

For a state trajectory \(X\):

$$
A_g(n)=\sum_{k=1}^{n} d_G(X_k,X_{k-1})
$$

$$
A_l(n;W)=\sum_{k=n-W+1}^{n} d_G(X_k,X_{k-1})
$$

$$
\mathcal I_\Omega
=
1-
\frac{d_G(X_{n-W},X_n)}{A_l}
$$

with:

$$
0 \le \mathcal I_\Omega \le 1
$$

The multivariate metric is:

$$
d_G(x,y)=\sqrt{(x-y)^T G(x-y)}
$$

where the operational diagonal metric is calibrated from training/reference data only.

## Research Status

This repository is a **research prototype**.

It does **not** claim:

- production cryptographic security,
- independent security audit,
- that Omega history is secret entropy,
- that Omega Core universally improves forecasting,
- physical unclonability without a hardware-bound root of trust.

Important negative controls are retained intentionally.

In particular, if an attacker possesses the same secret, the same device binding, and reproduces the exact operational history, the software-only construction derives the same key.

Strong clone resistance therefore requires a hardware-bound identity such as a secure element, PUF-like root, or equivalent trusted hardware.

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
- `zenodo_metadata.json` — Zenodo deposit and repository metadata

## Citation

Please cite the software record using the Zenodo DOI below.

The conceptual framework is currently represented by the related working preprint:

Mohamed Sayed, *The Universe That Never Repeats: Omega-NR — Exact Physical Non-Repetition, Accumulated Change, and a Testable Quantum-Geometric Extension*, Zenodo, 2026. DOI: 10.5281/zenodo.23624320.

**Software DOI:** 10.5281/zenodo.23637375  
**Concept DOI:** 10.5281/zenodo.23637374

## Open Research Invitation

This project is presented as a starting point rather than a finished theory.

The Omega-NR framework and the accompanying research software are intended as an initial research seed for further investigation, independent testing, criticism, refinement, and development.

Researchers, mathematicians, physicists, engineers, computer scientists, and other interested specialists are warmly invited to examine the framework, challenge its assumptions, improve its mathematical formulation, test its predictions, and explore possible applications.

The purpose of making this work public is to place the original idea and its initial development in the scientific record and to encourage researchers with greater expertise, tools, data, facilities, or resources to develop it further.

The intention is not to claim that the framework is complete or final, but to establish the original research seed clearly enough that others may independently examine, challenge, extend, or improve it.

Researchers who find value in Omega-NR are encouraged to build upon it, test it rigorously, propose alternative formulations, and collaborate on future work.

Appropriate scholarly acknowledgment and citation of the original Omega-NR work and its associated software record are respectfully requested.

## Authorship, Priority, and Attribution

The original conception, formulation, and initial development of the Omega-NR framework are attributed to **Mohamed Sayed**.

The public release of this research is intended to establish a clear and dated scholarly record of the original work and to encourage further independent research.

Publication of the framework and software as an open research project does not constitute a transfer, assignment, abandonment, or waiver of authorship, scholarly priority, attribution, or any other rights that may apply to the original research work.

Researchers who test, criticize, extend, reformulate, or build upon Omega-NR are requested to preserve appropriate scholarly attribution to the original work and associated research records.

## Research and Noncommercial Use

The current development branch of this repository is intended to support noncommercial research, academic study, independent testing, experimentation, validation, criticism, and further scientific development.

Use of the software must comply with the license applicable to the specific version or release being used.

Researchers are encouraged to study, test, reproduce, criticize, and extend the work in accordance with the applicable license and with appropriate scholarly attribution.

## Commercial Use

Commercial use of versions released under a noncommercial license requires a separate written license or authorization from **Mohamed Sayed**.

Commercial use includes, where applicable:

- incorporation into commercial products or services,
- commercial deployment,
- paid implementation or integration,
- resale or redistribution as part of a commercial offering,
- use as part of a revenue-generating service,
- licensing, sublicensing, or commercialization of derivative implementations where restricted by the applicable license.

For commercial licensing or collaboration, contact the author through the public repository or the contact information associated with the published research record.

Nothing in this section retroactively changes rights already granted under an earlier software release.

In particular, **Omega Research Pack v4.0.0 was originally released under the MIT License**, and the rights granted under that release remain governed by the license that accompanied that release.

## Rights Notice

Copyright © 2026 **Mohamed Sayed**.

All rights not expressly granted by the applicable license are reserved.

The theoretical framework, research manuscripts, authorship claims, scholarly priority, and related research materials are distinct from the software license and remain subject to their respective publication terms and applicable rights.

No statement in this repository should be interpreted as a transfer or abandonment of authorship, scholarly priority, attribution, or other rights in the original Omega-NR research work.

## Development Philosophy

Omega-NR is intentionally being developed as an open-ended research program.

Negative results, failed predictions, null findings, and limitations are considered part of the scientific record rather than something to be hidden.

The objective is to determine where Omega-derived path-history quantities add measurable information, where they do not, and whether stronger mathematical or physical formulations can be developed.

Future versions may refine the operational definitions, improve validation methods, introduce new experimental domains, or revise parts of the current implementation while preserving the historical record of earlier versions.

## Versioning and Licensing

This repository uses versioned public releases.

The first public software release is:

**Omega Research Pack v4.0.0**

The corresponding GitHub release is tagged:

`v4.0.0`

Version `v4.0.0` was released under the **MIT License**.

Future versions may be distributed under different licensing terms. Users must refer to the `LICENSE` file and release information associated with the specific version they use.

Published versions should be treated as fixed research records.

Future substantive changes, including licensing changes, should be released as a new version rather than silently changing the historical meaning of an earlier release.

## License

The license applicable to the current development version is provided in the repository's `LICENSE` file.

The historical `v4.0.0` release remains governed by the MIT License under which it was originally published.

## Disclaimer

This code is provided for research, experimentation, and reproducibility.

It must not be used as a drop-in production authentication, security, cryptographic, safety-critical, or industrial control system without independent validation, security review, threat modeling, and implementation hardening.

No guarantee is made that the Omega-NR framework, Omega Core, or Omega Life-Key will provide predictive, cryptographic, physical, commercial, or engineering advantages in any specific application.

The software and research materials are provided for scientific investigation and further evaluation.
