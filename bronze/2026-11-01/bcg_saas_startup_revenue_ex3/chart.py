#!/usr/bin/env python3
"""Recreate an illustrative growth-path line chart with explicit data provenance."""
from pathlib import Path
import argparse, json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def render(data, theme, context):
    fig, ax = plt.subplots(figsize=theme.get("figsize", [9.3, 5.6]), facecolor=theme["background"])
    ax.set_facecolor(theme["background"])
    ordering = context.get("series_order", list(data[context["columns"]["series"]].drop_duplicates()))
    for series in ordering:
        rows = data.loc[data[context["columns"]["series"]] == series].copy()
        rows = rows.sort_values(context["columns"]["x"])
        ax.plot(rows[context["columns"]["x"]], rows[context["columns"]["y"]],
                color=theme["palette"].get(series, theme["highlight"]),
                linewidth=theme["line_width"], marker=theme.get("marker", None),
                solid_capstyle="round", label=series)
        end = rows.iloc[-1]
        ax.annotate(context["end_labels"].get(series, f"{end[context['columns']['x']]} months"),
                    xy=(end[context["columns"]["x"]], end[context["columns"]["y"]]),
                    xytext=(0, theme.get("end_label_offset", 10)), textcoords="offset points",
                    ha="center", color=theme["text_color"], fontsize=theme["label_fontsize"])
    ax.set_xlim(*context["xlim"]); ax.set_ylim(*context["ylim"])
    ax.xaxis.set_major_locator(MultipleLocator(context["x_tick_step"]))
    ax.yaxis.set_major_locator(MultipleLocator(context["y_tick_step"]))
    ax.set_xlabel(context["x_label"], labelpad=theme["labelpad"])
    ax.set_ylabel(context["y_label"], rotation=0, ha="left", labelpad=theme["ylabel_pad"])
    ax.yaxis.set_label_coords(*theme["ylabel_coords"])
    ax.tick_params(axis='both', which='both', length=0, colors=theme["axis_color"], labelsize=theme["tick_fontsize"])
    if theme["show_grid"]: ax.grid(axis="y", color=theme["grid_color"], linewidth=0.6, alpha=0.6)
    for side in ['top','right','left']: ax.spines[side].set_visible(False)
    ax.spines['bottom'].set_color(theme["axis_color"])
    fig.text(*theme["title_pos"], context["title"],fontsize=theme["title_fontsize"],fontweight="bold",color=theme["text_color"])
    fig.text(*theme["subtitle_pos"],context["subtitle"],fontsize=theme["subtitle_fontsize"],color=theme["text_color"])
    ax.legend(loc="upper center",bbox_to_anchor=theme["legend_anchor"],ncol=1,frameon=False,fontsize=theme["legend_fontsize"])
    fig.text(*theme["source_pos"],context["source_note"],fontsize=theme["source_fontsize"],color=theme.get("source_color",theme["text_color"]))
    fig.subplots_adjust(**theme["margins"])
    return fig


def main():
    p=argparse.ArgumentParser();p.add_argument('--theme',choices=['source','neutral'],default='source')
    p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json');p.add_argument('--output',default='output.png')
    a=p.parse_args();folder=Path(__file__).resolve().parent
    cfg=json.loads((folder/a.config).read_text(encoding='utf-8'))
    fig=render(pd.read_csv(folder/a.data),cfg['THEME'][a.theme],cfg['CONTEXT'])
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
if __name__=='__main__':main()
