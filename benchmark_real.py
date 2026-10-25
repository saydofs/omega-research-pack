
import json, math, statistics
from pathlib import Path
import numpy as np

from omega_v4 import RobustMetric, OmegaCoreV4, CalibratedProjector

def ridge_fit(X,y,lam):
    X=np.asarray(X,float); y=np.asarray(y,float)
    mu=X.mean(0); sd=X.std(0); sd[sd<1e-9]=1
    Z=(X-mu)/sd
    A=Z.T@Z + lam*np.eye(Z.shape[1])
    b=Z.T@y
    w=np.linalg.solve(A,b)
    bias=y.mean()
    return mu,sd,w,bias

def ridge_pred(model,X):
    mu,sd,w,bias=model
    X=np.asarray(X,float)
    return ((X-mu)/sd)@w+bias

def rmse(y,p):
    y=np.asarray(y); p=np.asarray(p)
    return float(np.sqrt(np.mean((y-p)**2)))

def build_features(series, H=5, W=20):
    x=np.asarray(series,float)
    metric=RobustMetric().fit(x[:max(30,len(x)//2)])
    core=OmegaCoreV4(window=W,metric=metric)
    rows=[]
    for i in range(len(x)-H):
        st=core.update(x[i])
        xi=np.atleast_1d(x[i])
        lags=[]
        for d in [1,2,3,5,10]:
            j=max(0,i-d)
            lags.extend(np.atleast_1d(x[j]).tolist())
        base=list(xi)+lags+[i]
        omega=list(st.as_tuple())
        # predict mean absolute future movement across channels
        y=float(np.mean(np.abs(np.atleast_1d(x[i+H])-xi)))
        rows.append((i,base,omega,y))
    return rows

def temporal_eval(series,H=5,W=20):
    rows=build_features(series,H,W)
    n=len(rows)
    t1=int(.60*n); t2=int(.80*n)
    train=rows[:t1]; val=rows[t1:t2]; test=rows[t2:]
    lams=[.01,.1,1,10,100,1000]
    out={}
    for name,use_omega in [("baseline",False),("baseline_plus_omega",True)]:
        best=None
        for lam in lams:
            X=[r[1]+(r[2] if use_omega else []) for r in train]
            y=[r[3] for r in train]
            m=ridge_fit(X,y,lam)
            pv=ridge_pred(m,[r[1]+(r[2] if use_omega else []) for r in val])
            ev=rmse([r[3] for r in val],pv)
            if best is None or ev<best[0]:
                best=(ev,lam)
        full=rows[:t2]
        X=[r[1]+(r[2] if use_omega else []) for r in full]
        y=[r[3] for r in full]
        m=ridge_fit(X,y,best[1])
        pt=ridge_pred(m,[r[1]+(r[2] if use_omega else []) for r in test])
        out[name]={"rmse":rmse([r[3] for r in test],pt),"lambda":best[1]}
    out["improvement_pct"]=100*(out["baseline"]["rmse"]-out["baseline_plus_omega"]["rmse"])/out["baseline"]["rmse"]
    return out

def load_local_real_datasets():
    datasets={}
    try:
        import statsmodels.api as sm
        co2=sm.datasets.co2.load_pandas().data["co2"].interpolate().dropna().values
        datasets["CO2"]=co2
    except Exception:
        pass
    try:
        import statsmodels.api as sm
        sun=sm.datasets.sunspots.load_pandas().data["SUNACTIVITY"].values
        datasets["Sunspots"]=sun
    except Exception:
        pass
    try:
        import statsmodels.api as sm
        nile=sm.datasets.nile.load_pandas().data["volume"].values
        datasets["Nile"]=nile
    except Exception:
        pass
    try:
        import statsmodels.api as sm
        md=sm.datasets.macrodata.load_pandas().data
        # real multivariate series: inflation, unemployment, real GDP growth proxy
        arr=md[["realgdp","infl","unemp"]].astype(float).values
        arr[:,0]=np.diff(np.r_[arr[0,0],arr[:,0]])
        datasets["Macrodata_multivariate"]=arr
    except Exception:
        pass
    return datasets

if __name__=="__main__":
    ds=load_local_real_datasets()
    result={}
    for name,x in ds.items():
        result[name]={}
        for H in [1,5,10]:
            if len(x)>80+H:
                result[name][str(H)]=temporal_eval(x,H=H,W=20)
    print(json.dumps(result,indent=2))
    Path("results_real_benchmark.json").write_text(json.dumps(result,indent=2))
