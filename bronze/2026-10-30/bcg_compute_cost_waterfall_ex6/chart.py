#!/usr/bin/env python3
"""Editable consulting chart types; source/neutral themes are in config.json."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib.patches import Patch

HERE = Path(__file__).resolve().parent

def read_data(path):
    with open(path, newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))
    for row in rows:
        row["value"] = float(row["value"]) if row.get("value") else None
    return rows

def render(data, theme, context):
    """Return a Matplotlib figure from CSV rows, a theme and a chart context."""
    settings = theme
    plt.rcParams.update({"font.family": settings.get("font", "DejaVu Sans"),
                         "font.size": settings.get("font_size", 11),
                         "axes.unicode_minus": False})
    fig = plt.figure(figsize=tuple(settings.get("figsize", [11, 5.7])),
                     facecolor=settings.get("background", "white"))
    box = context.get("plot_area", [0.11, 0.15, 0.82, 0.65])
    ax = fig.add_axes(box)
    ax.set_facecolor(settings.get("background", "white"))
    kind = context["chart_type"]
    by_cat = {x["category"]: x for x in data if x["value"] is not None}
    if kind == "waterfall":
        categories = context["category_order"]
        cumulative = 0.0
        bar_width = settings.get("bar_width", 0.56)
        colors = settings["palette"]
        for i, category in enumerate(categories):
            row = by_cat[category]
            total = row["series"] == "total"
            height = row["value"]
            bottom = 0.0 if total else cumulative
            ax.bar(i, height, bottom=bottom, width=bar_width,
                   color=colors.get(category, settings["accent"]), linewidth=0)
            label = context.get("value_format", "{value:.1f}").format(value=height)
            if category in context.get("inside_labels", []):
                ax.text(i, bottom + height * 0.52, label, ha="center", va="center",
                        color="white", fontweight="bold", fontsize=settings.get("label_size", 11))
            else:
                ax.text(i, bottom + height + settings.get("label_offset", .7), label,
                        ha="center", va="bottom", fontweight="bold", fontsize=settings.get("label_size", 11))
            if not total:
                cumulative += height
                if i < len(categories) - 2:
                    ax.plot([i + bar_width / 2, i + 1 - bar_width / 2],
                            [cumulative, cumulative], color=settings.get("connector", "#777777"),
                            linestyle=settings.get("connector_style", "--"), linewidth=.8)
        ax.set_xticks(range(len(categories)), [context.get("category_labels", {}).get(x, x) for x in categories])
        ax.set_ylim(*context.get("ylim", [0, 54]))
        ax.set_xlim(-.5, len(categories) - .5)
        ax.yaxis.set_visible(False)
        ax.tick_params(axis="x", length=0, labelsize=settings.get("tick_size", 10), pad=6)
        for spine in ax.spines.values(): spine.set_visible(False)
    elif kind == "stacked_100":
        categories = context["category_order"]
        series = context["series_order"]
        bar_width = settings.get("bar_width", .76)
        for idx, cat in enumerate(categories):
            bottom = 0
            rows = {r["series"]:r for r in data if r["category"]==cat}
            for serie in series:
                amount = rows[serie]["value"]
                if amount is None: continue
                ax.bar(idx, amount, width=bar_width, bottom=bottom,
                       color=settings["palette"][serie], edgecolor=settings.get("edge", "white"),
                       linewidth=settings.get("edge_width", 1))
                ax.text(idx, bottom + amount / 2, context.get("value_format", "{value:.0f}%").format(value=amount),
                        ha="center", va="center", color=settings.get("inside_text", "white"),
                        fontsize=settings.get("label_size", 11))
                bottom += amount
            if abs(bottom - 100) > .2:
                raise ValueError(f"Stacked percentage does not total 100 for {cat}: {bottom}")
        ax.set_xticks(range(len(categories)),
                      [context.get("category_labels", {}).get(x,x) for x in categories])
        ax.set_xlim(-.5, len(categories)-.5)
        ax.set_ylim(*context.get("ylim", [0, 100]))
        ax.yaxis.set_visible(False)
        ax.tick_params(axis="x", length=0, labelsize=settings.get("tick_size", 12))
        for side in ["top", "right", "left"]: ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_linewidth(.7)
        ax.spines["bottom"].set_color("#555555")
        handles = [Patch(facecolor=settings["palette"][serie],
                         label=context.get("series_labels", {}).get(serie,serie)) for serie in series]
        ax.legend(handles=handles, loc="lower left", bbox_to_anchor=tuple(context.get("legend_anchor",[0.0,1.04])),
                  ncol=len(series), frameon=False, handlelength=.95, handletextpad=.3,
                  columnspacing=1.0, fontsize=settings.get("legend_size", 10))
    elif kind == "horizontal_bar":
        categories = context["category_order"]
        y = list(range(len(categories)))
        vals = [by_cat[c]["value"] for c in categories]
        colors = [settings["accent"] if c in context.get("highlights", []) else settings.get("muted", "#AAB7C1") for c in categories]
        ax.barh(y, vals, color=colors, height=settings.get("bar_width",.56))
        ax.set_yticks(y, [context.get("category_labels",{}).get(c,c) for c in categories])
        ax.invert_yaxis()
        ax.set_xlim(*context.get("xlim",[0,100]))
        ax.tick_params(axis="y",length=0,pad=10)
        ax.set_xlabel(context.get("x_label", ""),fontsize=settings.get("tick_size",11),labelpad=8)
        if settings.get("show_grid",True):
            ax.grid(axis="x", color=settings.get("grid_color","#E3E9EE"),linewidth=.7)
            ax.set_axisbelow(True)
        for i, value in zip(y, vals):
            ax.text(value + context.get("label_offset",1.5),i,
                    context.get("value_format","{value:.0f}%").format(value=value),
                    va="center",ha="left",fontweight="bold",fontsize=settings.get("label_size",11))
        for side in ["top","right","left"]:ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color("#A0A0A0")
    else:
        raise ValueError(f"Unsupported chart_type: {kind}")
    title_y = context.get("title_y",.945)
    fig.text(context.get("title_x",.075),title_y,context["title"].replace("$", r"\$"),
             fontsize=settings.get("title_size",18),fontweight=settings.get("title_weight","normal"),
             color=settings.get("text_color","#1E2625"),va="top")
    subtitle = context.get("subtitle","")
    if subtitle:
        fig.text(context.get("title_x",.075),context.get("subtitle_y",.875),subtitle.replace("$", r"\$"),
                 fontsize=settings.get("subtitle_size",10),color=settings.get("text_color","#1E2625"),va="top")
    source = context.get("source","")
    if source:
        fig.text(context.get("title_x",.075),context.get("source_y",.045),source,
                 color=settings.get("source_color","#666666"),fontsize=settings.get("source_size",8),va="bottom")
    return fig

def main():
    parser = argparse.ArgumentParser(description="Editable quantitative chart")
    parser.add_argument("--data",default="data.csv")
    parser.add_argument("--config",default="config.json")
    parser.add_argument("--theme",choices=["source","neutral"],default="source")
    parser.add_argument("--output",default="output.png")
    args=parser.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding="utf-8"))
    fig=render(read_data(args.data),cfg["THEME"][args.theme],cfg["CONTEXT"])
    fig.savefig(args.output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
if __name__ == "__main__":main()
