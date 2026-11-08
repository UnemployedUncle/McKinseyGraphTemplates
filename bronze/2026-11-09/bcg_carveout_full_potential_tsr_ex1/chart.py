#!/usr/bin/env python3
"""Reusable two-series event-aligned indexed line chart; no source image included."""
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

def render(data, theme, context):
    rows=sorted(data,key=lambda x:int(x["order"]))
    x=list(range(len(rows)))
    full=[float(x["full_potential_index"]) for x in rows]
    all_=[float(x["all_carveouts_index"]) for x in rows]
    plt.rcParams.update({"font.size":theme.get("font_size",10),"font.family":"DejaVu Sans"})
    fig,ax=plt.subplots(figsize=tuple(theme["figure_size"]))
    fig.patch.set_facecolor(theme["background"]); ax.set_facecolor(theme["background"])
    ax.plot(x,all_,color=theme["all_color"],marker="o",markersize=4,linewidth=1.8,label=context["all_label"],zorder=2)
    ax.plot(x,full,color=theme["full_color"],marker="o",markersize=4.5,linewidth=2.2,label=context["full_label"],zorder=3)
    for i,v in enumerate(full):
        ax.annotate(f"{v:.1f}",(i,v),xytext=(0,8),textcoords="offset points",ha="center",fontsize=8,color=theme["text_color"],fontweight="bold")
    for i,v in enumerate(all_):
        ax.annotate(f"{v:.1f}",(i,v),xytext=(0,-13),textcoords="offset points",ha="center",fontsize=8,color=theme["text_color"])
    ax.set_xticks(x,[z["period_label"] for z in rows],fontsize=8)
    ax.set_xlim(-.25,len(x)-.3); ax.set_ylim(*context["y_range"])
    ax.set_yticks(context["y_ticks"])
    ax.spines[["top","right"]].set_visible(False)
    ax.spines[["left","bottom"]].set_color(theme["spine_color"])
    ax.tick_params(colors=theme["text_color"])
    ax.axhline(context["baseline_index"],color=theme["baseline_color"],linewidth=.8,linestyle="--",alpha=.7)
    ax.set_ylabel(context["y_label"],fontsize=10,labelpad=10)
    ax.set_title(context["title"],loc="left",fontweight="bold",fontsize=15,pad=25,color=theme["text_color"])
    gap=full[-1]-all_[-1]
    end=len(x)-1
    ax.annotate("",xy=(end+.18,all_[-1]),xytext=(end+.18,full[-1]),arrowprops={"arrowstyle":"|-|","color":theme["text_color"],"lw":1.2})
    ax.text(end+.33,(full[-1]+all_[-1])/2,f"{gap:.1f}\nindex points",va="center",fontsize=9,color=theme["text_color"])
    ax.legend(loc="upper left",frameon=False,ncol=2,bbox_to_anchor=(.18,-.08),fontsize=9)
    fig.text(.12,.01,context["footnote"],fontsize=8,color=theme["note_color"])
    fig.subplots_adjust(left=.12,right=.90,top=.78,bottom=.24)
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument("--data",default="data.csv");p.add_argument("--config",default="config.json");p.add_argument("--theme",choices=["source","neutral"],default="source");p.add_argument("--output",required=True);a=p.parse_args()
    with open(a.data,encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    cfg=json.load(open(a.config,encoding="utf-8"));fig=render(rows,cfg["THEME"][a.theme],cfg["CONTEXT"])
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
if __name__=="__main__":main()
