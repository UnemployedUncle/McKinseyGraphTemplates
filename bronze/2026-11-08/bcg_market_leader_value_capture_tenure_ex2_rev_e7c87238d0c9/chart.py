#!/usr/bin/env python3
"""Config-driven consulting chart. Edit only data.csv and config.json to reuse."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter, FuncFormatter


def read_data(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def render(data, theme, context):
    """Return a matplotlib Figure; theme and context are config sections."""
    plt.rcParams.update({"font.family": theme.get("font_family", "DejaVu Sans"), "font.size": theme.get("font_size", 10),
                         "axes.unicode_minus": False})
    fig, ax = plt.subplots(figsize=tuple(theme.get("figsize", [11, 6.6])), facecolor=theme["background"])
    ax.set_facecolor(theme["plot_background"])
    fig.subplots_adjust(**theme.get("margins", {"left": .15, "right": .96, "bottom": .20, "top": .80}))
    kind = context["chart_type"]
    if kind == "quadrant_scatter":
        xk,yk = context["x_field"],context["y_field"]
        points = sorted(data, key=lambda row: row[context["label_field"]])
        for p in points:
            x,y=float(p[xk]),float(p[yk]); err=float(p.get("uncertainty_pp", 0))
            assert 0 <= x <= 100 and 0 <= y <= 100 and err>=0
            ax.scatter(x,y,s=theme["marker_size"],color=theme["highlight"] if p[context["label_field"]] in context.get("highlights", []) else theme["primary"],
                       edgecolor=theme["background"], linewidth=.8, zorder=5)
            # All locations (including point coordinates) are read from input CSV. Only
            # small *label* offsets come from optional display settings.
            dx,dy=context.get("label_offsets",{}).get(p[context["label_field"]], [1.5,1.7])
            ax.annotate(p[context["label_field"]], (x,y),xytext=(dx,dy),textcoords="offset points",fontsize=theme["label_font_size"], color=theme["text"],zorder=6)
        ax.axhline(50,color=theme["grid"],lw=1,ls="--",zorder=0)
        ax.axvline(50,color=theme["grid"],lw=1,ls="--",zorder=0)
        ax.set_xlim(-2,103); ax.set_ylim(-2,103)
        ax.xaxis.set_major_formatter(PercentFormatter(100));ax.yaxis.set_major_formatter(PercentFormatter(100))
        ax.grid(color=theme["grid"],alpha=.40,lw=.7, zorder=-5)
        ax.set_xlabel(context["x_axis"],labelpad=14,fontsize=10,color=theme["text"])
        ax.set_ylabel(context["y_axis"],labelpad=12,fontsize=10,color=theme["text"])
        # Quadrant summary is descriptive, not a claim of causality.
        for x,y,label in [(3,96,"Long tenure / lower capture"),(55,96,"Long tenure / higher capture"),
                          (3,4,"Newer leaders / lower capture"),(55,4,"Newer leaders / higher capture")]:
            ax.text(x,y,label,fontsize=8,color=theme["muted"],alpha=.85,ha="left",va="center", zorder=1)
    elif kind == "diverging_bar":
        rows=list(data)
        names=[p[context["label_field"]] for p in rows]
        vals=[float(p[context["value_field"]]) for p in rows]
        counts=[int(p[context["count_field"]]) for p in rows]
        assert len(names)==len(set(names)) and all(n>0 for n in counts) and sum(counts)==int(context["sample_size"])
        positions=list(range(len(rows)))
        bars=ax.barh(positions,vals,color=[theme["positive"] if v>=0 else theme["negative"] for v in vals],height=.53)
        ax.axvline(0,color=theme["text"],lw=1.3)
        ax.set_yticks(positions,[f"{name}  (n={cnt})" for name,cnt in zip(names,counts)],color=theme["text"])
        ax.invert_yaxis();ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos: f"{x:+.0f}" if x else "0"))
        ax.grid(axis="x",color=theme["grid"],alpha=.6,ls="-")
        ax.set_axisbelow(True)
        for b,v in zip(bars,vals):
            ax.text(v+(0.55 if v>=0 else -.55),b.get_y()+b.get_height()/2,f"{v:+.1f}",ha="left" if v>=0 else "right",va="center",fontweight="bold",color=theme["text"])
        xx=max(abs(min(vals)),abs(max(vals)))*1.3
        ax.set_xlim(-xx,xx);ax.set_xlabel(context["x_axis"],color=theme["text"],labelpad=12)
        ax.tick_params(axis="y",length=0)
    else:
        raise ValueError(f"Unsupported chart_type: {kind}")
    for spine in ax.spines.values():spine.set_visible(False)
    ax.tick_params(axis="both",colors=theme["muted"])
    fig.text(theme.get("title_x",.09),.94,context["title"],fontsize=theme["title_font_size"],fontweight="bold",color=theme["text"],va="top")
    fig.text(theme.get("title_x",.09),.87,context["subtitle"],fontsize=theme["subtitle_font_size"],color=theme["muted"],va="top")
    fig.text(theme.get("title_x",.09),.035,context["footnote"],fontsize=theme["footnote_font_size"],color=theme["muted"],va="bottom",wrap=True)
    return fig


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",default="data.csv")
    p.add_argument("--config",default="config.json")
    p.add_argument("--theme",choices=("source","neutral"),default="source")
    p.add_argument("--output",required=True)
    args=p.parse_args();cfg=json.loads(Path(args.config).read_text(encoding="utf-8"))
    data=read_data(args.data)
    if not data:raise ValueError("data.csv has no rows")
    fig=render(data,cfg["THEME"][args.theme],cfg["CONTEXT"])
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Render success: {out} / {len(data)} rows / dpi=200")

if __name__=="__main__":main()
