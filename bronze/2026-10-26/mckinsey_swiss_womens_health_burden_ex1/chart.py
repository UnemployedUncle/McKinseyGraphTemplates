#!/usr/bin/env python3
"""Editable analytical chart: data CSV + THEME and CONTEXT; no source images."""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def render(data, theme, context):
    kind=context["chart_kind"]
    fig=plt.figure(figsize=theme["figsize"],facecolor=theme["background"])
    ax=fig.add_axes(theme["axes_rect"],facecolor=theme["background"])
    plt.rcParams["font.family"]=theme["font"]
    if kind=="vertical_four_bars":
        order=context["category_order"]
        lookup={r["category"]:r for r in data}
        if any(name not in lookup for name in order):raise ValueError("Required category missing")
        values=[float(lookup[name]["value"]) for name in order]
        if not all(0<=v<=100 for v in values):raise ValueError("Percentage out of range")
        xs=list(range(len(order)))
        colors=[theme["palette"].get(name,theme["bar_color"]) for name in order]
        ax.bar(xs,values,width=theme["bar_width"],color=colors,zorder=3)
        for x,v in zip(xs,values):
            ax.text(x,v+theme["value_offset"],f"{v:g}",ha="center",va="bottom",color=theme["text"],fontsize=theme["value_size"],fontweight="bold")
        ax.set_xticks(xs,[context["category_labels"].get(k,k) for k in order],fontsize=theme["tick_size"])
        ax.set_xlim(-theme["x_padding"],len(xs)-1+theme["x_padding"])
        ax.set_ylim(0,theme["y_max"])
        if context.get("show_y",False):ax.set_yticks(context["y_ticks"])
        else:ax.set_yticks([])
        ax.axhline(0,color=theme["baseline"],lw=theme["baseline_width"])
        if context.get("show_ratio_arrow",False):
            # draw highlight as an independent data-coordinate overlay
            arrow=FancyArrowPatch((xs[0],values[0]+theme["arrow_gap"]),(xs[-1],values[-1]+theme["arrow_gap"]),
                 arrowstyle="-|>",mutation_scale=12,linewidth=theme["arrow_width"],
                 color=theme["arrow_color"],connectionstyle="arc3,rad=0",zorder=2)
            ax.add_patch(arrow)
            x=(xs[0]+xs[-1])/2
            y=(values[0]+values[-1])/2+theme["arrow_gap"]
            ax.text(x,y,context["ratio_label"],ha="center",va="center",fontsize=theme["ratio_size"],weight="bold",
                 bbox=dict(boxstyle="circle,pad=0.4",facecolor=theme["ratio_badge"],edgecolor="none"),zorder=4)
    elif kind=="horizontal_share_stack":
        order=context["category_order"]
        lookup={r["category"]:r for r in data}
        if any(n not in lookup for n in order):raise ValueError("Required category missing")
        values=[float(lookup[n]["value"]) for n in order]
        if not all(0<=v<=100 for v in values):raise ValueError("Percentage out of range")
        if abs(sum(values)-100)>context.get("sum_tolerance",0.5):raise ValueError("Shares do not sum to 100")
        left=0.0
        for k,v in zip(order,values):
            ax.barh([0],[v],left=[left],height=theme["bar_width"],color=theme["palette"][k],edgecolor=theme["background"],linewidth=theme["edge_width"])
            if v>=context["min_direct_label"]:
                ax.text(left+v/2,0,f"{v:g}%",ha="center",va="center",fontsize=theme["value_size"],color=theme["label_colors"].get(k,theme["text"]),fontweight="bold")
            left+=v
        ax.set_xlim(0,100);ax.set_ylim(-0.85,0.85)
        ax.set_yticks([]);ax.set_xticks([])
        # legend: human-readable direct mapping, below the horizontal share bar
        import matplotlib.patches as patches
        legend=[patches.Patch(color=theme["palette"][k],label=context["category_labels"].get(k,k)+" ("+f"{lookup[k]['value']}%"+")") for k in order]
        fig.legend(handles=legend,loc="lower center",bbox_to_anchor=theme["legend_anchor"],ncol=2,fontsize=theme["legend_size"],frameon=False)
    else:raise ValueError(f"Unsupported chart_kind {kind}")
    for spine in ax.spines.values():spine.set_visible(False)
    ax.tick_params(axis="both",length=0,pad=theme["tick_pad"],colors=theme["text"])
    fig.text(theme["header_x"],theme["exhibit_y"],context["exhibit"],fontsize=theme["exhibit_size"],color=theme["text"],weight="bold")
    fig.text(theme["header_x"],theme["title_y"],context["title"],fontsize=theme["title_size"],color=theme["text"],family=theme["title_font"],weight=theme["title_weight"],va="top")
    fig.text(theme["header_x"],theme["subtitle_y"],context["subtitle"],fontsize=theme["subtitle_size"],color=theme["muted"],va="top")
    fig.text(theme["header_x"],theme["source_y"],context["source"],fontsize=theme["source_size"],color=theme["muted"])
    if context.get("note"):fig.text(theme["header_x"],theme["note_y"],context["note"],fontsize=theme["note_size"],color=theme["muted"])
    return fig


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--theme",choices=["source","neutral"],default="source")
    p.add_argument("--data",default="data.csv")
    p.add_argument("--output",default="output.png")
    p.add_argument("--config",default="config.json")
    args=p.parse_args()
    folder=Path(__file__).resolve().parent
    cfg=json.loads((folder/args.config).read_text(encoding="utf-8"))
    inpath=Path(args.data);inpath=inpath if inpath.is_absolute() else folder/inpath
    with inpath.open(encoding="utf-8-sig",newline="") as h:data=list(csv.DictReader(h))
    fig=render(data,cfg["THEME"][args.theme],cfg["CONTEXT"])
    out=Path(args.output);out=out if out.is_absolute() else folder/out
    out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(out)
if __name__=="__main__":main()
