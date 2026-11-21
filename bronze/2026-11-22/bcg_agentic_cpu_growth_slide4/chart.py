"""Reusable matplotlib chart: source/neutral themes and data-driven annotations."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np


def render(data, theme, context):
    """Return a chart from CSV records, a presentation theme and business context."""
    fig, ax = plt.subplots(figsize=(11, 6.2))
    fig.patch.set_facecolor(theme.get("background", "white"))
    ax.set_facecolor(theme.get("background", "white"))
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(theme.get("grid", "#CCD3D2"))
    ax.tick_params(axis="both", which="both", length=0, labelcolor=theme["text"])
    ax.grid(axis="y" if context["chart_type"] != "paired_horizontal" else "x",
            color=theme.get("grid", "#E2E6E5"), alpha=0.65, linewidth=0.7)
    ax.set_axisbelow(True)
    kind = context["chart_type"]
    if kind == "profit_bridge":
        positions = np.arange(len(data))
        gross = np.array([float(r["gross_usd_bn"]) for r in data]); loss = np.array([float(r["cancellation_loss_usd_bn"] or 0) for r in data])
        ax.bar(positions, gross, color=theme["gross"], width=.72, zorder=2)
        ax.bar(positions, -loss, color=theme["loss"], width=.72, zorder=2)
        for i, r in enumerate(data):
            if r["net_usd_bn"]:
                val = float(r["net_usd_bn"])
                ax.scatter([i], [val], color=theme["net"], s=67, zorder=4, edgecolor=theme["background"], linewidth=.7)
            if gross[i]:
                ax.text(i, gross[i] + .55, f'{gross[i]:g}', ha="center", va="bottom", fontsize=9.5, color=theme["text"])
            if loss[i]:
                ax.text(i, -loss[i] - .5, f'−{loss[i]:g}', ha="center", va="top", fontsize=9.5, color=theme["loss"])
        ax.axhline(0, color=theme["net"], linewidth=1.2, zorder=3)
        ax.set_xticks(positions, [r["period"] for r in data], fontsize=10)
        ax.set_ylabel(context["axis_label"], fontsize=10, color=theme["text"])
        ax.set_ylim(-8, 28)
        ax.legend(handles=[Patch(color=theme["gross"], label="Gross trading profit"), Patch(color=theme["loss"], label="US cargo cancellation fees"),
                           Line2D([0],[0],marker="o",linestyle="None",markerfacecolor=theme["net"],color=theme["net"],label="Net (where disclosed)")],
                  loc="upper left", frameon=False, ncol=3, fontsize=8.8)
        ax.annotate(context["highlight_note"], xy=(len(data)-1, float(data[-1]["net_usd_bn"])),
                    xytext=(len(data)-1.34, 10.4), color=theme["text"], fontsize=10, fontweight="bold",
                    arrowprops={"arrowstyle":"->", "color":theme["net"], "lw":1.1}, ha="center")
    elif kind == "cpu_stacked":
        positions = np.arange(len(data)); bottom = np.zeros(len(data))
        for col, color, label in [("current_gw", "installed", "Current installed base"),
                                  ("traditional_cpu_growth_gw", "traditional", "Traditional CPU growth"),
                                  ("ai_uplift_gw", "ai", "AI uplift")]:
            vals = np.array([float(r[col]) for r in data]); ax.bar(positions, vals, bottom=bottom, color=theme[color], width=.7, label=label)
            for i,(v,b) in enumerate(zip(vals,bottom)):
                if v >= 2:
                    ax.text(i,b+v/2,f"{v:g}",ha="center",va="center",fontsize=8.7,
                            color="white" if color=="installed" else theme["text"],fontweight="bold")
            bottom += vals
        for i,r in enumerate(data):
            ax.text(i,bottom[i]+.6,f'{float(r["total_gw"]):g}',ha="center",fontsize=10,color=theme["text"],fontweight="bold")
        ax.set_xticks(positions,[r["period"] for r in data]); ax.set_ylabel(context["axis_label"],fontsize=10,color=theme["text"])
        ax.set_ylim(0,max(bottom)*1.23); ax.legend(loc="upper left",ncol=3,frameon=False,fontsize=8.5)
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True, nbins=6))
    elif kind == "paired_horizontal":
        labels=[r["category"] for r in data]; pos=np.arange(len(data)); h=.33
        local=np.array([float(r["aus_nz_pct"]) for r in data]); global_avg=np.array([float(r["global_pct"]) for r in data])
        ax.barh(pos-h/2,local,height=h,color=theme["local"],label="Australia / New Zealand")
        ax.barh(pos+h/2,global_avg,height=h,color=theme["global_color"],label="Global")
        for i,(a,g) in enumerate(zip(local,global_avg)):
            ax.text(a+1,i-h/2,f"{a:g}%",va="center",color=theme["text"],fontsize=9.5)
            ax.text(g+1,i+h/2,f"{g:g}%",va="center",color=theme["text"],fontsize=9.5)
        ax.set_yticks(pos,labels,fontsize=10); ax.invert_yaxis(); ax.set_xlim(0,102)
        ax.set_xlabel(context["axis_label"],fontsize=10,color=theme["text"])
        ax.legend(loc="lower right",ncol=2,frameon=False,fontsize=8.8)
    else:
        raise ValueError("Unsupported chart_type: " + str(kind))
    fig.suptitle(context["title"], x=.075, y=.965, ha="left", fontsize=17, fontweight="bold", color=theme["text"])
    fig.text(.075,.904,context["subtitle"],fontsize=9.5,color=theme["muted"])
    fig.text(.075,.04,context["footnote"],fontsize=8.2,color=theme["muted"])
    fig.subplots_adjust(left=.245 if kind == "paired_horizontal" else .15,right=.94,top=.82,bottom=.18)
    return fig


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--data",default="data.csv")
    parser.add_argument("--config",default="config.json"); parser.add_argument("--theme",choices=["source","neutral"],default="source")
    parser.add_argument("--output",default="source.png"); args=parser.parse_args()
    with open(args.data,encoding="utf-8-sig",newline="") as f: data=list(csv.DictReader(f))
    with open(args.config,encoding="utf-8") as f: config=json.load(f)
    fig=render(data,config["THEME"][args.theme],config["CONTEXT"])
    target=Path(args.output); target.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(target,dpi=200,facecolor=fig.get_facecolor()); plt.close(fig)
    print(f"Rendered {args.theme}: {target}")


if __name__=="__main__":
    main()
