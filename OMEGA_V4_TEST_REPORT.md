# Omega Research Pack v4 — Test Report

## 1. Mathematical core

The operational multidimensional path metric is:

d_G(x,y) = sqrt((x-y)^T G (x-y))

with a diagonal robust scale matrix learned from training/reference data only.

Omega Core v4 records:
- A_global
- A_local
- irreversibility = 1 - endpoint_distance / A_local
- reversal statistics
- A_global / step
- path efficiency

By construction, for A_local > 0:

0 <= irreversibility <= 1

and accumulated path length A_global is non-decreasing.

## 2. Security interpretation

Omega Life-Key v4 is a research history-binding construction, not production cryptography.

Key evolution binds:
- previous key
- secret
- hardware/device binding placeholder
- robust Omega operational history
- monotone counter

It does not treat Omega history as new entropy.

## 3. Attack-suite results

Noise projection match:
```json
{
  "1e-5": 1.0,
  "1e-4": 0.92,
  "5e-4": 0.5633333333333334,
  "1e-3": 0.25666666666666665
}
```

Drift projection match:
```json
{
  "1e-7": 0.92,
  "1e-6": 0.92,
  "5e-6": 0.9266666666666666
}
```

Clone:
```json
{
  "clone_at": 110,
  "first_key_divergence": 140,
  "diverged": true
}
```

Replay / rollback:
```json
{
  "old_nonce_tag_valid_with_new_nonce": false,
  "old_state_tag_valid_now": false
}
```

Sensor-history replay:
```json
{
  "detected_rate": 0.8888888888888888
}
```

Exact-history negative control:
```json
{
  "same_key_fraction": 1.0
}
```

Different device binding:
```json
{
  "same_key_fraction": 0.0
}
```

## 4. Operating-point trade-off

Two profiles are retained rather than hiding the trade-off.

Stable:
- noise 1e-4 match ~97.7%
- clone detection delay ~45 steps

Fast-detect:
- noise 1e-4 match ~93.3%
- clone detection delay ~10 steps

These values come from the synthetic multivariate stress test in this pack and are not deployment guarantees.

## 5. Real time-series benchmark

```json
{
  "CO2": {
    "1": {
      "baseline": {
        "rmse": 0.3182430702473196,
        "lambda": 100
      },
      "baseline_plus_omega": {
        "rmse": 0.31912519102158543,
        "lambda": 100
      },
      "improvement_pct": -0.2771845977919558
    },
    "5": {
      "baseline": {
        "rmse": 0.70142835181535,
        "lambda": 0.01
      },
      "baseline_plus_omega": {
        "rmse": 0.6281005960613966,
        "lambda": 0.01
      },
      "improvement_pct": 10.454062138232029
    },
    "10": {
      "baseline": {
        "rmse": 1.2066095923983633,
        "lambda": 0.01
      },
      "baseline_plus_omega": {
        "rmse": 1.1190275467873174,
        "lambda": 0.01
      },
      "improvement_pct": 7.258523897274851
    }
  },
  "Sunspots": {
    "1": {
      "baseline": {
        "rmse": 20.384558476641075,
        "lambda": 1
      },
      "baseline_plus_omega": {
        "rmse": 25.864489184632177,
        "lambda": 0.01
      },
      "improvement_pct": -26.882753993767512
    },
    "5": {
      "baseline": {
        "rmse": 40.61294102522693,
        "lambda": 0.01
      },
      "baseline_plus_omega": {
        "rmse": 58.53791582483669,
        "lambda": 0.01
      },
      "improvement_pct": -44.136116092837426
    },
    "10": {
      "baseline": {
        "rmse": 21.191478069225727,
        "lambda": 1000
      },
      "baseline_plus_omega": {
        "rmse": 26.18979416274214,
        "lambda": 0.1
      },
      "improvement_pct": -23.58644393368185
    }
  },
  "Nile": {
    "1": {
      "baseline": {
        "rmse": 127.1229423775241,
        "lambda": 10
      },
      "baseline_plus_omega": {
        "rmse": 123.75405091215639,
        "lambda": 0.1
      },
      "improvement_pct": 2.650105010441723
    },
    "5": {
      "baseline": {
        "rmse": 111.2978110587184,
        "lambda": 100
      },
      "baseline_plus_omega": {
        "rmse": 105.83841436126443,
        "lambda": 10
      },
      "improvement_pct": 4.9052147975971465
    },
    "10": {
      "baseline": {
        "rmse": 90.39189175144449,
        "lambda": 100
      },
      "baseline_plus_omega": {
        "rmse": 89.40306561599446,
        "lambda": 100
      },
      "improvement_pct": 1.0939323387202196
    }
  },
  "Macrodata_multivariate": {
    "1": {
      "baseline": {
        "rmse": 22.050279040041076,
        "lambda": 10
      },
      "baseline_plus_omega": {
        "rmse": 21.357478973916837,
        "lambda": 100
      },
      "improvement_pct": 3.1419106527685376
    },
    "5": {
      "baseline": {
        "rmse": 31.661894062082546,
        "lambda": 10
      },
      "baseline_plus_omega": {
        "rmse": 32.017228462860025,
        "lambda": 1
      },
      "improvement_pct": -1.1222777768150607
    },
    "10": {
      "baseline": {
        "rmse": 27.39841705322477,
        "lambda": 100
      },
      "baseline_plus_omega": {
        "rmse": 27.130820951423615,
        "lambda": 10
      },
      "improvement_pct": 0.9766845335674516
    }
  }
}
```

Interpretation:
- Omega features sometimes improve a temporal holdout and sometimes worsen it.
- Therefore Omega Core is not a universal forecasting feature.
- The benchmark target here is future absolute movement, not the exact same target used in the earlier NASA battery capacity-loss experiment.

## 6. Important negative result

If attacker and legitimate device have:
- the same secret,
- the same device binding,
- the exact same operational history,

then the software-only construction derives the same key.

Therefore strong clone resistance needs a hardware-bound root of trust (e.g. secure element/PUF-like binding) in addition to Omega history.

## 7. External datasets prepared for next validation

The package includes `sensor_csv_adapter.py` for direct ingestion of numeric sensor CSV files.

Recommended next physical datasets:
- UCI Condition Monitoring of Hydraulic Systems
- NASA IMS Bearings
- NASA Li-ion Battery Aging raw channels

## 8. Research status

Current status:
- mathematical prototype: working
- operational feature extractor: working
- attack simulator: working
- real public time-series benchmark: working
- true hardware/PUF experiment: not yet performed
- production cryptographic validation: not claimed
