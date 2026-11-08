#!/usr/bin/env python3
"""Reusable rank-ordered non-exclusive response-count chart."""
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

def render(data,theme,context):
    rows=sorted(data,key=lambda r:(-int(r["company_count"]),r["move"]))
    counts=[int(r["company_count"]) for r in rows]
    denom=int(rows[0]["denominator"])
    if len(set(int(r["denominator"]) for r in rows))!=1:raise ValueError("Inconsistent denominators")
    if any(v<0 or v>denom for v in counts):raise ValueError("Count outside denominator")
    labels=[r["move"] for r in rows]
    fig,ax=plt.subplots(figsize=tuple(theme["figure_size"]));fig.patch.set_facecolor(theme["background"]);ax.set_facecolor(theme["background"])
    y=list(range(len(rows)))
    colors=[theme["low_color"] if v<=context["low_threshold"] else theme["main_color"] for v in counts]
    ax.barh(y,counts,color=colors,height=.63)
    ax.set_yticks(y,labels,fontsize=11);ax.invert_yaxis()
    ax.set_xlim(0,denom+2);ax.set_xticks([0,5,10,15,20]);ax.set_xlabel(context["x_label"])
    ax.spines[["top","right","left"]].set_visible(False)
    ax.spines["bottom"].set_color(theme["spine_color"])
    ax.tick_params(axis="y",length=0,pad=10,colors=theme["text_color"])
    ax.tick_params(axis="x",colors=theme["text_color"])
    ax.grid(axis="x",alpha=.12);ax.set_axisbelow(True)
    for i,v in enumerate(counts):ax.text(v+.35,i,f"{v}/{denom}",va="center",fontsize=10,fontweight="bold",color=theme["text_color"])
    ax.set_title(context["title"],loc="left",fontsize=15,fontweight="bold",pad=27,color=theme["text_color"])
    fig.text(.14,.045,context["footnote"],fontsize=8,color=theme["note_color"])
    fig.subplots_adjust(left=.38,right=.91,top=.83,bottom=.19)
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument("--data",default="data.csv");p.add_argument("--config",default="config.json");p.add_argument("--theme",choices=["source","neutral"],default="source");p.add_argument("--output",required=True);a=p.parse_args()
    with open(a.data,encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
    cfg=json.load(open(a.config,encoding="utf-8"));fig=render(rows,cfg["THEME"][a.theme],cfg["CONTEXT"])
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
if __name__=="__main__":main()
