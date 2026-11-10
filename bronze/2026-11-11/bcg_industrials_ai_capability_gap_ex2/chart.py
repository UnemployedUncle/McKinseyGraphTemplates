#!/usr/bin/env python3
"""Five-column capability KPI cards; values and style configured externally."""
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def render(data,theme,context):
    rows=sorted(data,key=lambda r:int(r["order"]))
    fig=plt.figure(figsize=theme.get("figsize",[14.5,6.0]),facecolor=theme["background"])
    ax=fig.add_axes(theme.get("axes_box",[.045,.10,.91,.64]))
    ax.set_xlim(-.03,len(rows)+.03);ax.set_ylim(0,1);ax.axis("off")
    fig.text(.047,.91,context["title"],fontsize=theme["title_size"],color=theme["title_color"],weight="bold")
    fig.text(.047,.83,context["subtitle"],fontsize=theme["subtitle_size"],color=theme["text_color"])
    for i,r in enumerate(rows):
        x=i+.04;w=.91
        if i%2==0:ax.add_patch(Rectangle((x,.03),w,.94,color=theme["stripe_color"],lw=0))
        ax.text(x+w/2,.85,r["gap_display"],ha="center",va="center",fontsize=theme["gap_size"],color=theme["gap_color"],weight="bold")
        ax.plot([x+w/2,x+w/2],[.69,.78],linestyle="--",lw=1,color=theme["line_color"])
        ax.text(x+w/2,.58,f'{float(r["industrial_pct"]):g}%',ha="center",va="center",fontsize=theme["number_size"],weight="bold",color=theme["number_color"])
        ax.text(x+w/2,.46,context["percent_label"],ha="center",fontsize=theme["small_size"],color=theme["text_color"])
        ax.add_patch(Rectangle((x+.03,.08),w-.06,.23,facecolor=theme["callout_background"],edgecolor="none"))
        ax.text(x+w/2,.19,r["capability"],ha="center",va="center",fontsize=theme["label_size"],color=theme["text_color"],weight="bold",wrap=True)
    fig.text(.047,.045,context["footer"],fontsize=theme["footnote_size"],color=theme["text_color"])
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument("--data",default="data.csv");p.add_argument("--config",default="config.json");p.add_argument("--theme",choices=["source","neutral"],default="source");p.add_argument("--output",default="source.png");args=p.parse_args()
    with open(args.data,encoding="utf-8-sig",newline="") as handle:data=list(csv.DictReader(handle))
    with open(args.config,encoding="utf-8") as handle:cfg=json.load(handle)
    fig=render(data,cfg["THEME"][args.theme],cfg["CONTEXT"])
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,dpi=200,facecolor=fig.get_facecolor(),bbox_inches="tight");plt.close(fig)
if __name__=="__main__":main()
