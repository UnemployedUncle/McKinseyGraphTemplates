from pathlib import Path
import argparse, json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parent

def render(data, theme, context):
    d = data.copy() if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
    t, c = theme, context
    fig, ax = plt.subplots(figsize=c["figsize"])
    fig.patch.set_facecolor(t["background"])
    ax.set_facecolor(t["background"])
    fig.subplots_adjust(**c["margins"])
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0, labelsize=t["tick_size"], colors=t["ink"])
    fig.text(.035,.95,c["title"],fontsize=t["title_size"],weight="bold",color=t["ink"])
    fig.text(.035,.89,c["subtitle"],fontsize=10,color=t["ink"])
    kind=c["kind"]
    if kind=="history":
        d=d.sort_values("year"); x=np.arange(len(d)); y=d.value.to_numpy()
        assert d.year.is_unique and (y>=0).all()
        ax.bar(x,y,width=c["bar_width"],color=[t["colors"][s] for s in d.phase_color])
        ax.set_ylim(0,max(y)*1.23); ax.set_xlim(-.65,len(d)-.35)
        ax.set_yticks([]); ax.spines["bottom"].set_visible(True)
        ax.set_xticks(x,[str(a)+("E" if f=="estimate" else "") if show else "" for a,f,show in zip(d.year,d.status,d.show_year)])
        for i,row in enumerate(d.itertuples()):
            if row.provenance=="reported": ax.text(i,row.value+7,f"{row.value:g}",ha="center",fontsize=9,weight="bold")
            if isinstance(row.phase_label,str) and row.phase_label:
                ax.vlines(i,row.value+20,max(y)*1.2,colors=t["muted"],linestyles=":",linewidth=.8)
                ax.text(i+.12,max(y)*1.2,row.phase_label,ha="left" if i<len(d)-2 else "right",va="top",fontsize=8,weight="bold",color=t["ink"])
        fig.text(.035,.82,c["kpi"],fontsize=16,weight="bold",color=t["colors"]["forecast"])
    elif kind=="grouped":
        groups=list(dict.fromkeys(d.period)); series=list(dict.fromkeys(d.series)); x=np.arange(len(groups))*c["group_spacing"]
        assert not d.duplicated(["period","series"]).any() and d.value.between(0,100).all()
        width=c["bar_width"]
        for j,s in enumerate(series):
            v=d[d.series==s].set_index("period").reindex(groups).value.to_numpy(); assert np.isfinite(v).all()
            bars=ax.bar(x+(j-(len(series)-1)/2)*width,v,width*.94,color=t["colors"][j],label=s)
            ax.bar_label(bars,fmt="%.1f",padding=3,fontsize=11,weight="bold")
        ax.set_xticks(x,groups); ax.set_ylim(0,max(d.value)*1.2); ax.set_yticks(np.arange(0, max(d.value)*1.2,2)); ax.grid(axis="y",color=t["grid"],linewidth=.5); ax.set_axisbelow(True)
        ax.legend(loc=c["legend_loc"],bbox_to_anchor=c["legend_anchor"],ncol=len(series),title=c["legend_title"],frameon=True,fontsize=9,title_fontsize=9)
    elif kind=="profiles":
        avg=d[d.category==c["average_label"]]; d=d[d.category!=c["average_label"]]; cols=c["columns"]
        assert len(avg)==1 and d.category.is_unique and ((d[cols]>=0)&(d[cols]<=100)).all().all()
        assert (d[cols[0]]<=d[cols[1]]).all() and (d[cols[1]]<=d[cols[2]]).all()
        y=np.arange(len(d)); ax.set_xlim(0,100); ax.set_ylim(len(d)-.5,-2.55)
        for i in [-2]+list(y): ax.axhspan(i-.19,i+.19,color=t["band"],zorder=0)
        for tick in range(0,101,10): ax.vlines(tick,-2.5,-1.5,color=t["grid"],lw=.65); ax.vlines(tick,-.5,len(d)-.5,color=t["grid"],lw=.65)
        for j,k in enumerate(cols):
            color=t["colors"][j]; ax.plot(d[k],y,"o-",color=color,ms=7,lw=.9); v=float(avg.iloc[0][k]); ax.plot(v,-2,"o",color=color,ms=7)
            ax.text(v+2,-2,f"{v:g}",va="center",fontsize=10,color=t["ink"])
            ax.text(v,-2.7,c["series_labels"][j],ha="center",va="bottom",fontsize=9,color=t["ink"])
        ax.set_yticks([-2]+list(y),[c["average_label"]]+list(d.category)); ax.set_xticks(range(0,101,20)); ax.spines["bottom"].set_visible(True)
    else: raise ValueError(kind)
    fig.text(.035,.025,c["footnote"],fontsize=8,color=t["muted"],va="bottom",wrap=True)
    return fig

def main():
    p=argparse.ArgumentParser(); p.add_argument("--data",default=str(BASE/"data.csv")); p.add_argument("--config",default=str(BASE/"config.json")); p.add_argument("--theme",choices=["source","neutral"],default="source"); p.add_argument("--output",required=True); p.add_argument("--dpi",type=int,default=200); a=p.parse_args()
    cfg=json.loads(Path(a.config).read_text()); fig=render(pd.read_csv(a.data),cfg["THEME"][a.theme],cfg["CONTEXT"]); fig.savefig(a.output,dpi=a.dpi); plt.close(fig)
if __name__=="__main__": main()
