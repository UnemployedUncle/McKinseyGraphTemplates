"""Reusable matplotlib charts; render(data, theme, context) -> fig."""
import argparse
import json
import math
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def render(data, theme, context):
    kind=context["chart_kind"]
    fig=plt.figure(figsize=tuple(theme.get("figsize",[11,6.2])),facecolor=theme["background"])
    fg=theme["text_color"]
    fig.text(.07,.92,context["title"],fontsize=17,weight="bold",color=fg)
    fig.text(.07,.865,context["subtitle"],fontsize=10,color=theme["muted_color"])
    if kind=="line":
        ax=fig.add_axes([.105,.21,.825,.56])
        ys=data["value_pct"].astype(float).tolist()
        xs=list(range(len(ys)))
        ax.plot(xs,ys,color=theme["accent"],lw=2.7,marker="o",markersize=7)
        ax.set_xlim(-.25,len(xs)-.72)
        maximum=max(10,math.ceil(max(ys)*1.18/10)*10)
        ax.set_ylim(0,maximum)
        ax.set_yticks(range(0,maximum+1,10))
        ax.set_yticklabels([f"{i}%" for i in range(0,maximum+1,10)])
        ax.set_xticks(xs,data["label"])
        for x,y in zip(xs,ys):
            ax.annotate(f"{y:g}%",(x,y),xytext=(0,-20),textcoords="offset points",
                        ha="center",fontsize=11,fontweight="bold",color=fg)
        ax.spines[["top","right","left"]].set_visible(False)
        ax.spines["bottom"].set_color(theme["axis_color"])
        ax.tick_params(axis="both",length=0,pad=8)
        ax.grid(False)
    elif kind=="paired_donut":
        places=[[.08,.24,.36,.53],[.55,.24,.36,.53]]
        colors=[theme["palette"][name] for name in data["category"]]
        for pos,col,title in zip(places,context["comparison_columns"],context["comparison_labels"]):
            ax=fig.add_axes(pos)
            values=data[col].astype(float).tolist()
            wedges,_=ax.pie(values,startangle=90,counterclock=False,colors=colors,
                             wedgeprops={"edgecolor":theme["background"],"linewidth":2.5})
            ax.add_artist(plt.Circle((0,0),.43,color=theme["background"]))
            ax.text(0,0,title,ha="center",va="center",fontsize=12,weight="bold",color=fg)
            for wedge,val in zip(wedges,values):
                angle=math.radians((wedge.theta1+wedge.theta2)/2)
                ax.text(.73*math.cos(angle),.73*math.sin(angle),f"{val:g}%",
                        color=theme["inside_color"],ha="center",va="center",fontsize=10,weight="bold")
            ax.axis("equal")
        legend=fig.add_axes([.12,.19,.78,.09]);legend.axis("off")
        for i,row in data.reset_index(drop=True).iterrows():
            x=.01+i/len(data)
            legend.scatter(x,.5,c=theme["palette"][row["category"]],s=80,marker="s")
            legend.text(x+.02,.5,row["category"],transform=legend.transAxes,
                        fontsize=8.2,va="center",color=fg)
        legend.set_xlim(0,1);legend.set_ylim(0,1)
    elif kind=="treemap":
        ax=fig.add_axes([.13,.19,.74,.60]);ax.set_axis_off()
        v=data["value_pct"].astype(float).tolist()
        if len(v)!=4 or abs(sum(v)-100)>1e-8:raise ValueError("Four shares totaling 100% required")
        upper=sum(v[:2])/100;lower=sum(v[2:])/100
        boxes=[(0,lower,v[0]/sum(v[:2]),upper),
               (v[0]/sum(v[:2]),lower,v[1]/sum(v[:2]),upper),
               (0,0,v[2]/sum(v[2:]),lower),
               (v[2]/sum(v[2:]),0,v[3]/sum(v[2:]),lower)]
        for row,(x,y,w,h) in zip(data.itertuples(index=False),boxes):
            ax.add_patch(Rectangle((x,y),w,h,fc=theme["palette"][row.category],ec=theme["background"],lw=5))
            ax.text(x+w/2,y+h/2+.035,row.category,ha="center",va="center",
                    color=theme["inside_color"],fontsize=11,weight="bold")
            ax.text(x+w/2,y+h/2-.07,f"{row.value_pct:g}%",ha="center",va="center",
                    color=theme["inside_color"],fontsize=18,weight="bold")
        ax.set_xlim(0,1);ax.set_ylim(0,1)
    else:
        raise ValueError(f"Unknown chart kind {kind}")
    fig.text(.07,.095,context["note"],fontsize=8,color=theme["muted_color"])
    fig.text(.07,.055,context["source_label"],fontsize=8,color=theme["muted_color"])
    return fig

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",default="data.csv")
    p.add_argument("--config",default="config.json")
    p.add_argument("--theme",choices=["source","neutral"],default="source")
    p.add_argument("--output",required=True)
    p.add_argument("--dpi",type=int,default=200)
    a=p.parse_args()
    data=pd.read_csv(a.data)
    cfg=json.loads(Path(a.config).read_text(encoding="utf-8"))
    fig=render(data,cfg["THEME"][a.theme],cfg["CONTEXT"])
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=a.dpi,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(str(out))

if __name__=="__main__":main()
