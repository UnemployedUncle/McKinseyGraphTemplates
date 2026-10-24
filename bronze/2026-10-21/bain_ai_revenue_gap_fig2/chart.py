#!/usr/bin/env python3
"""Portable consulting-style chart renderer. Edit config.json and data.csv, not this source."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

HERE = Path(__file__).resolve().parent


def _base_fig(theme, context):
    fig = plt.figure(figsize=theme["figsize"], facecolor=theme["background"])
    plt.rcParams.update({"font.family": theme["font_family"], "font.size": theme["font_size"]})
    return fig


def _header(fig, theme, context):
    if context.get("title"):
        fig.text(theme["left"], theme["title_y"], context["title"], color=theme["ink"],
                 ha="left", va="top", fontsize=theme["title_size"], weight="bold", wrap=True)
    if context.get("subtitle"):
        fig.text(theme["left"], theme["subtitle_y"], context["subtitle"],
                 color=theme["muted"], fontsize=theme["subtitle_size"], va="top", ha="left")
    if context.get("source"):
        fig.text(theme["left"], theme["footer_y"], context["source"],
                 fontsize=theme["footer_size"], color=theme["muted"], va="bottom", ha="left")


def _horizontal_bars(data, theme, context):
    fig = _base_fig(theme, context)
    _header(fig, theme, context)
    ax = fig.add_axes(theme["plot_area"])
    rows = data.reset_index(drop=True)
    ys = range(len(rows))
    colors = [theme["highlight"] if r["category"] in context["highlight_categories"]
              else theme["bar"] for _, r in rows.iterrows()]
    ax.barh(list(ys), rows["value"], color=colors, height=theme["bar_height"])
    ax.set_yticks(list(ys), [context.get("category_labels", {}).get(c, c) for c in rows["category"]])
    ax.invert_yaxis()
    ax.set_xlim(*context["xlim"])
    ax.set_xticks(context["xticks"])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:.0f}{context['value_suffix']}"))
    ax.grid(axis="x", color=theme["grid"], linestyle="-", linewidth=.7)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0, pad=theme["y_label_padding"], colors=theme["ink"], labelsize=theme["category_size"])
    ax.tick_params(axis="x", length=0, pad=7, colors=theme["muted"], labelsize=theme["tick_size"])
    for sp in ax.spines.values(): sp.set_visible(False)
    for i, (_, row) in enumerate(rows.iterrows()):
        value = float(row["value"])
        ax.text(value + context["value_offset"], i, f"{value:g}{context['value_suffix']}",
                ha="left", va="center", fontsize=theme["value_size"], weight="bold",
                color=colors[i], clip_on=False)
    return fig


def _dumbbell(data, theme, context):
    fig = _base_fig(theme, context)
    _header(fig, theme, context)
    ax = fig.add_axes(theme["plot_area"])
    series_names = context["series_order"]
    cats = context["category_order"]
    for i, cat in enumerate(cats):
        subset = data[data.category == cat].set_index("series")
        v0 = float(subset.loc[series_names[0], "value"])
        v1 = float(subset.loc[series_names[1], "value"])
        ax.plot([v0, v1], [i, i], color=theme["connector"], linewidth=theme["connector_width"], zorder=1)
        ax.scatter([v0], [i], s=theme["marker_area"], color=theme["bar"], zorder=3)
        ax.scatter([v1], [i], s=theme["marker_area"], color=theme["highlight"], zorder=3)
        for val, color, sign in ((v0,theme["bar"],+1),(v1,theme["highlight"],-1)):
            offset = context["label_offset"] * sign
            ax.text(val+offset,i+context["value_label_vertical_offset"],f"${val:,.0f}B",color=color,
                    ha="left" if sign>0 else "right", va="bottom",weight="bold",fontsize=theme["value_size"])
        ax.text(max(v0,v1)*context["delta_label_x_factor"],i-context["delta_label_y_offset"],
                f"{(v1/v0-1)*100:.1f}%",color=theme["highlight"],ha="center",fontsize=theme["delta_size"])
    ax.set_yticks(range(len(cats)),cats)
    ax.invert_yaxis()
    ax.set_xlim(*context["xlim"])
    ax.set_xticks(context["xticks"])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x,p: f"${x:,.0f}B"))
    ax.grid(axis="x",color=theme["grid"],linewidth=.7)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y",length=0,pad=12,colors=theme["ink"],labelsize=theme["category_size"])
    ax.tick_params(axis="x",length=0,pad=7,colors=theme["muted"])
    for sp in ax.spines.values():sp.set_visible(False)
    return fig


def _waterfall_gap(data, theme, context):
    """Three stepped pillars with a split innovation requirement. Values come from rows, not literals."""
    fig = _base_fig(theme, context)
    _header(fig, theme, context)
    ax = fig.add_axes(theme["plot_area"])
    xs = theme["bar_positions"]
    group_order = context["group_order"]
    lows = {}
    total = 0.0
    for i, group in enumerate(group_order):
        group_rows = data[data["category"] == group]
        lows[group] = total
        for _, row in group_rows.iterrows():
            val = float(row["value"])
            fill = theme["group_colors"][i]
            ax.bar(xs[i],val,bottom=total,width=theme["bar_width"],
                   color=fill,edgecolor=theme["internal_edge_color"],linewidth=theme["internal_edge_width"])
            if group==context["innovation_group"] and val>=context["min_internal_label_value"]:
                ax.text(xs[i],total+val/2,context["segment_labels"].get(row["series"],row["series"]),
                        fontsize=theme["segment_size"],color=theme["segment_ink"],ha="center",va="center",wrap=True)
            total += val
    ax.set_ylim(*context["ylim"])
    ax.set_xlim(*context["xlim"])
    ax.set_xticks(xs)
    ax.set_xticklabels([str(s).split("\n", 1)[0] for s in context["category_labels"]],fontweight="bold")
    for i, label in enumerate(context["category_labels"]):
        if "\n" in label:
            secondary=label.split("\n",1)[1]
            ax.text(xs[i],context["category_detail_axis_y"],secondary,ha="center",va="top",
                    transform=ax.get_xaxis_transform(),color=theme["ink"],fontsize=theme["category_detail_size"])
    ax.set_yticks(context["yticks"])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y,p:f"${y:g}T"))
    ax.tick_params(axis="x", length=0,pad=10, colors=theme["ink"],labelsize=theme["category_size"])
    ax.tick_params(axis="y", length=0, pad=7, colors=theme["muted"],labelsize=theme["tick_size"])
    for tick in ax.get_xticklabels():tick.set_linespacing(1.35)
    for sp in ax.spines.values():sp.set_visible(False)
    ax.axhline(0, color=theme["ink"], linewidth=.8)
    # The $1.5T capex comparison line and the $6T reference level are part of the sourced display.
    for line in context["reference_lines"]:
        ax.axhline(line["value"],color=theme["grid_dark"],linewidth=1.1,linestyle=(0,(2.5,2.5)),zorder=0)
        ax.text(context["reference_label_x"],line["value"],line["label"],
                color=theme["ink"],ha="left",va="bottom" if line.get("above") else "top",
                fontsize=theme["ref_size"],weight="bold")
    # Anchors derive from cumulative rows and source-defined parameters.
    for i, group in enumerate(group_order[:2]):
        subset=data[data.category==group]
        top=lows[group]+sum(subset.value)
        ax.text(xs[i],top+context["value_label_offset"],context["group_value_labels"][group].replace("$",r"\$"),
                ha="center",va="bottom",fontsize=theme["value_size"],color=theme["ink"])
    innovation_bottom=lows[context["innovation_group"]]
    if context.get("minor_segment_annotation"):
        minor=context["minor_segment_annotation"]
        vals=data[(data.category==context["innovation_group"])&(data.series==minor["series"])].value
        if len(vals):
            ax.text(context["innovation_annotation_x"],innovation_bottom+float(vals.iloc[0])/2,
                    minor["label"],color=theme["ink"],ha="left",va="center",fontsize=theme["segment_size"])
    innovation_total=sum(data[data.category==context["innovation_group"]].value)
    ax.text(context["innovation_annotation_x"],innovation_bottom+innovation_total*.51,
            context["innovation_annotation"],color=theme["highlight"],weight="bold",
            ha="left",va="center",fontsize=theme["annotation_size"])
    return fig


def render(data: pd.DataFrame, theme: dict, context: dict):
    kind = context["chart_type"]
    if kind=="horizontal_bars": return _horizontal_bars(data,theme,context)
    if kind=="dumbbell": return _dumbbell(data,theme,context)
    if kind=="waterfall_gap": return _waterfall_gap(data,theme,context)
    raise ValueError(f"Unsupported chart_type: {kind}")


def main():
    parser=argparse.ArgumentParser(description="Source-inspired, data-accurate chart template")
    parser.add_argument("--theme",choices=["source","neutral"],default="source")
    parser.add_argument("--data",default="data.csv")
    parser.add_argument("--config",default="config.json")
    parser.add_argument("--output",default="output.png")
    a=parser.parse_args()
    data=pd.read_csv(HERE / a.data if not Path(a.data).is_absolute() else a.data)
    with (HERE/a.config if not Path(a.config).is_absolute() else Path(a.config)).open(encoding="utf-8") as f:
        cfg=json.load(f)
    fig=render(data,cfg["THEME"][a.theme],cfg["CONTEXT"])
    out=HERE/a.output if not Path(a.output).is_absolute() else Path(a.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor(),bbox_inches=None)
    plt.close(fig)
    print(f"Wrote: {out}")

if __name__=="__main__":main()
