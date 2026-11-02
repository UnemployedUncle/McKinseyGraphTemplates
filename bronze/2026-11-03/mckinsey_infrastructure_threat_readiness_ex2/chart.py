#!/usr/bin/env python3
"""Deterministic, configuration-driven chart renderer (no network access)."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def read_data(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError("data.csv contains no records")
    for row in rows:
        row["value"] = float(row["value"])
        if not 0 <= row["value"] <= 100:
            raise ValueError("Percent values must be between 0 and 100")
        if row.get("provenance") not in {"reported", "derived", "digitized_estimate"}:
            raise ValueError("Each plotted value requires provenance")
    return rows


def render(data, theme, context):
    """Render selected chart type with numeric marks drawn strictly from data."""
    if not data:
        raise ValueError("No data")
    fig, ax = plt.subplots(figsize=tuple(theme.get("figsize", [11.2, 6.4])))
    fig.patch.set_facecolor(theme["background"])
    ax.set_facecolor(theme["background"])
    labels = [r["category"] for r in data]
    vals = np.array([float(r["value"]) for r in data])
    colors = [theme["highlight"] if r["category"] in context.get("highlight", []) else theme["secondary"] for r in data]
    kind = context.get("chart_type", "horizontal_bar")
    if kind == "horizontal_bar":
        pos = np.arange(len(data))
        bars = ax.barh(pos, vals, height=theme.get("bar_width", 0.61), color=colors, edgecolor="none")
        ax.set_yticks(pos, labels=labels)
        ax.invert_yaxis()
        ax.set_xlim(0, context.get("axis_max", 110))
        ax.set_xlabel(context.get("axis_label", "Share of respondents (%)"), labelpad=12)
        ax.xaxis.grid(True, alpha=.14, color=theme["grid"])
        ax.set_axisbelow(True)
        ax.tick_params(axis="y", length=0, pad=12, labelsize=11)
        for bar, value in zip(bars, vals):
            ax.text(bar.get_width()+1.5, bar.get_y()+bar.get_height()/2, f"{value:.0f}%", va="center", fontsize=12, fontweight="bold", color=theme["text"])
    elif kind == "vertical_bar":
        pos=np.arange(len(data))
        bars=ax.bar(pos, vals, width=theme.get("bar_width", .56), color=colors, edgecolor="none")
        ax.set_xticks(pos, labels=labels)
        ax.set_ylim(0, context.get("axis_max", 45))
        ax.set_ylabel(context.get("axis_label", "Share (%)"), labelpad=12)
        ax.yaxis.grid(True, alpha=.14, color=theme["grid"])
        ax.set_axisbelow(True)
        ax.tick_params(axis="x", length=0, pad=12, labelsize=11)
        for bar,value in zip(bars, vals):
            ax.text(bar.get_x()+bar.get_width()/2, value+1, f"{value:.0f}%", ha="center", va="bottom", fontsize=17, fontweight="bold", color=theme["text"])
        if len(vals)==2 and context.get("show_difference",False):
            delta=vals[1]-vals[0]
            ax.text(.5, max(vals)+4.5, f"{delta:+.0f} percentage points", ha="center", fontsize=11, color=theme["highlight"], fontweight="bold")
    else:
        raise ValueError("Unsupported chart_type: " + str(kind))
    ax.spines[:].set_visible(False)
    ax.tick_params(colors=theme["text"])
    for label in ax.get_xticklabels()+ax.get_yticklabels():label.set_color(theme["text"])
    ax.title.set_color(theme["text"])
    fig.suptitle(context["title"], fontsize=19, fontweight="bold", x=.07, y=.978, ha="left", color=theme["text"])
    fig.text(.07,.916,context["subtitle"],fontsize=10.5,color=theme["muted"],ha="left")
    fig.text(.07,.055,context["footnote"],fontsize=8.7,color=theme["muted"],ha="left")
    fig.subplots_adjust(left=theme.get("left",.32),right=.91,top=.83,bottom=.18)
    return fig


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",default="data.csv")
    p.add_argument("--config",default="config.json")
    p.add_argument("--theme",choices=["source","neutral"],default="source")
    p.add_argument("--output",default="output.png")
    args=p.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding="utf-8"))
    fig=render(read_data(args.data),cfg["THEME"][args.theme],cfg["CONTEXT"])
    fig.savefig(args.output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(args.output)

if __name__=="__main__":main()
