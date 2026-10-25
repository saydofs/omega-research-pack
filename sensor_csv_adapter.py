
from __future__ import annotations
import argparse, csv, json, math
import numpy as np
from omega_v4 import RobustMetric, OmegaCoreV4

def read_csv(path, columns):
    rows=[]
    with open(path, newline="", encoding="utf-8-sig") as f:
        r=csv.DictReader(f)
        for row in r:
            vals=[]
            ok=True
            for c in columns:
                try:
                    v=float(row[c])
                    if not math.isfinite(v):
                        ok=False; break
                    vals.append(v)
                except Exception:
                    ok=False; break
            if ok:
                rows.append(vals)
    return np.asarray(rows,float)

def extract(path, columns, window=20, train_fraction=.5):
    X=read_csv(path,columns)
    if len(X)<max(50,window+5):
        raise ValueError("Not enough valid rows.")
    cut=max(30,int(len(X)*train_fraction))
    metric=RobustMetric().fit(X[:cut])
    core=OmegaCoreV4(window=window,metric=metric)
    out=[]
    for i,x in enumerate(X):
        s=core.update(x)
        out.append([i,*x.tolist(),*s.as_tuple()])
    names=[
        "index",*columns,
        "A_global","A_local","irreversibility","reversal_rate","A_rate",
        "channel_reversal_mean","channel_reversal_max","path_efficiency"
    ]
    return names,out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--columns",required=True,help="Comma-separated numeric sensor columns")
    ap.add_argument("--window",type=int,default=20)
    ap.add_argument("--output",default="omega_features.csv")
    args=ap.parse_args()
    cols=[c.strip() for c in args.columns.split(",") if c.strip()]
    names,rows=extract(args.csv,cols,args.window)
    with open(args.output,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(names); w.writerows(rows)
    print(json.dumps({"rows":len(rows),"columns":names,"output":args.output},indent=2))

if __name__=="__main__":
    main()
