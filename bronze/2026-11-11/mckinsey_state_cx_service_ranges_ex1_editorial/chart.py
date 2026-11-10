#!/usr/bin/env python3
"""Interval plot for article-reported service satisfaction ranges; editorial, not publisher's original."""
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def render(data,theme,context):
    rows=sorted(data,key=lambda r:int(r["order"]))
    fig,ax=plt.subplots(figsize=theme.get("figsize",[11.0,5.3]),facecolor=theme["background"])
    ax.set_facecolor(theme["background"])
    ys=list(range(len(rows)-1,-1,-1))
    for y,r in zip(ys,rows):
        low=float(r["min_pct"]);high=float(r["max_pct"])
        if low>high:raise ValueError("min_pct exceeds max_pct")
        ax.plot([low,high],[y,y],color=theme["line_color"],linewidth=theme["line_width"],solid_capstyle="round",zorder=2)
        ax.scatter([low,high],[y,y],color=[theme["min_color"],theme["max_color"]],s=theme["marker_size"],zorder=3)
        ax.text(low,y+theme["label_offset"],f"{low:g}%",ha="center",color=theme["text_color"],fontsize=theme["label_size"],weight="bold")
        ax.text(high,y+theme["label_offset"],f"{high:g}%",ha="center",color=theme["text_color"],fontsize=theme["label_size"],weight="bold")
    ax.set_yticks(ys,[r["service"] for r in rows]);ax.set_xlim(*context["xlim"]);ax.set_ylim(-.7,len(rows)-.02)
    ax.set_xlabel(context["x_label"],fontsize=theme["axis_size"],color=theme["text_color"]);ax.tick_params(axis="y",length=0,labelsize=theme["axis_size"],colors=theme["text_color"])
    ax.tick_params(axis="x",labelsize=theme["axis_size"],colors=theme["text_color"]);ax.set_xticks(context["xticks"]);ax.grid(axis="x",color=theme["grid_color"],alpha=.7)
    for spine in ax.spines.values():spine.set_visible(False)
    ax.set_title(context["title"],fontsize=theme["title_size"],weight="bold",loc="left",pad=36,color=theme["title_color"])
    fig.text(.12,.07,context["footer"],fontsize=theme["footnote_size"],color=theme["text_color"])
    fig.subplots_adjust(left=.30,right=.94,top=.79,bottom=.23)
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument("--data",default="data.csv");p.add_argument("--config",default="config.json");p.add_argument("--theme",choices=["source","neutral"],default="source");p.add_argument("--output",default="source.png");args=p.parse_args()
    with open(args.data,encoding="utf-8-sig",newline="") as handle:data=list(csv.DictReader(handle))
    with open(args.config,encoding="utf-8") as handle:cfg=json.load(handle)
    fig=render(data,cfg["THEME"][args.theme],cfg["CONTEXT"])
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,dpi=200,facecolor=fig.get_facecolor(),bbox_inches="tight");plt.close(fig)
if __name__=="__main__":main()
