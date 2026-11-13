#!/usr/bin/env python3
"""Reproducible editorial chart, not an image-exact original reproduction."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

def render(data, theme, context):
    """Render a chart from a dataframe, selected theme dictionary and CONTEXT."""
    rows = data.copy()
    label_col = context["category_field"]
    value_col = context["value_field"]
    rows[value_col] = pd.to_numeric(rows[value_col], errors="raise")
    if rows[label_col].duplicated().any() or rows[value_col].isna().any():
        raise ValueError("Duplicate categories or missing numeric values")
    if not rows["provenance"].isin(["reported","derived","digitized_estimate","missing"]).all():
        raise ValueError("Unknown value provenance")
    rows = rows.sort_values(value_col, ascending=context["ascending"]).reset_index(drop=True)
    plt.rcParams.update({"font.family":theme["font"], "font.size":11})
    fig, ax = plt.subplots(figsize=tuple(theme["figsize"]), dpi=200)
    fig.patch.set_facecolor(theme["background"]); ax.set_facecolor(theme["background"])
    for spine in ax.spines.values(): spine.set_visible(False)
    labels = rows[label_col].tolist()
    values = rows[value_col].to_numpy(dtype=float)
    yy = range(len(rows))
    colors = [theme["negative"] if v < 0 else (theme["primary"] if c == context["focus_category"] else theme["secondary"]) for c,v in zip(labels, values)]
    ax.barh(list(yy), values, color=colors, height=context["bar_height"], zorder=3)
    ax.set_yticks(list(yy)); ax.set_yticklabels(labels, fontsize=11, color=theme["text"])
    ax.invert_yaxis()
    ax.set_xlim(*context["x_limits"])
    ax.axvline(0,color=theme["text"],lw=1,alpha=.55,zorder=2)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(context["tick_step"]))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x,pos:f"{x:.0f}{context.get('tick_suffix','')}"))
    ax.xaxis.grid(True,color=theme["grid"],lw=.8,zorder=0)
    ax.tick_params(axis="both",length=0,pad=10,labelcolor=theme["muted"])
    ax.tick_params(axis="y",labelcolor=theme["text"])
    span = context["x_limits"][1]-context["x_limits"][0]
    for y,v in zip(yy,values):
        x=v + (0.015*span if v>=0 else -0.015*span)
        ax.text(x,y,f"{v:+.0f}{context['value_suffix']}" if context["show_plus"] else f"{v:.0f}{context['value_suffix']}",
                ha="left" if v>=0 else "right",va="center",fontweight="bold",fontsize=12,color=theme["text"])
    fig.suptitle(context["title"],x=.075,y=.96,ha="left",fontsize=17,fontweight="bold",color=theme["text"])
    ax.set_title(context["subtitle"],loc="left",pad=24,fontsize=10,color=theme["muted"])
    ax.set_xlabel(context["xlabel"],labelpad=16,fontsize=10,color=theme["muted"])
    fig.text(.075,.045,context["footnote"],fontsize=8.8,color=theme["annotation_color"])
    fig.subplots_adjust(left=.32,right=.93,top=.78,bottom=.23)
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument("--data",default="data.csv");p.add_argument("--config",default="config.json")
    p.add_argument("--theme",choices=["source","neutral"],default="neutral");p.add_argument("--output",required=True)
    a=p.parse_args(); config=json.loads(Path(a.config).read_text(encoding="utf-8"))
    fig=render(pd.read_csv(a.data),config["THEME"][a.theme],config["CONTEXT"])
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
if __name__ == "__main__": main()
