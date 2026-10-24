#!/usr/bin/env python3
"""Editable, deterministic consulting-style chart. No external images or private data."""
from pathlib import Path
import csv, json, argparse
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FuncFormatter

def load_data(csv_path):
    with Path(csv_path).open(encoding="utf-8-sig", newline="") as fh:
        return [dict(row, value=float(row["value"])) for row in csv.DictReader(fh)]

def render(data, theme, context):
    """Return a matplotlib Figure. Layout/text/colors come from configuration."""
    rows = list(data)
    if not rows:
        raise ValueError("No data")
    vals = [float(d[context["value_field"]]) for d in rows]
    labels = [d[context["category_field"]] for d in rows]
    scale = theme.get("font_scale", 1.0)
    mpl.rcParams["font.family"] = theme.get("font", "DejaVu Sans")
    fig, ax = plt.subplots(figsize=tuple(theme["figsize"]), facecolor=theme["background"])
    ax.set_facecolor(theme["background"])
    y = list(range(len(rows)))
    colors = [theme["accent"] if d[context["category_field"]] == context["highlight_category"] else
              (theme["negative"] if vals[i] < 0 else theme["normal"]) for i,d in enumerate(rows)]
    bars = ax.barh(y, vals, height=theme["bar_height"], color=colors, linewidth=0, zorder=3)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(*context["xlim"])
    ax.xaxis.set_major_locator(MultipleLocator(context["tick_step"]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos: context["tick_format"].format(x=x)))
    ax.grid(axis="x", color=theme["grid_color"], linewidth=0.7, zorder=0)
    ax.axvline(0, color=theme["axis_color"], linewidth=theme["zero_line_width"], zorder=4)
    for spine in ax.spines.values(): spine.set_visible(False)
    ax.tick_params(axis="both", length=0, labelsize=theme["tick_size"]*scale, colors=theme["text_color"], pad=7)
    for bar,val in zip(bars,vals):
        sign = 1 if val>=0 else -1
        x = val + sign * context["label_pad"]
        ha = "left" if val>=0 else "right"
        ax.text(x,bar.get_y()+bar.get_height()/2,context["value_format"].format(value=val),
                ha=ha, va="center", fontsize=theme["value_size"]*scale,
                fontweight="bold", color=theme["text_color"])
    fig.subplots_adjust(left=theme["margins"]["left"],right=theme["margins"]["right"],
                        top=theme["margins"]["top"],bottom=theme["margins"]["bottom"])
    fig.text(theme["margins"]["left"],0.96,context["title"],ha="left",va="top",
             fontsize=theme["title_size"]*scale,fontweight="bold",color=theme["text_color"])
    fig.text(theme["margins"]["left"],0.88,context["subtitle"],ha="left",va="top",
             fontsize=theme["subtitle_size"]*scale,color=theme["muted_color"])
    fig.text(theme["margins"]["left"],0.05,context["source_note"],ha="left",va="bottom",
             fontsize=theme["footer_size"]*scale,color=theme["muted_color"])
    return fig

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--theme",choices=["source","neutral"],default="source")
    parser.add_argument("--data",default="data.csv")
    parser.add_argument("--output",default="output.png")
    parser.add_argument("--config",default="config.json")
    ns=parser.parse_args()
    root=Path(__file__).resolve().parent
    def based(p): return p if p.is_absolute() else root/p
    config=json.loads(based(Path(ns.config)).read_text(encoding="utf-8"))
    data=load_data(based(Path(ns.data)))
    fig=render(data,config["THEME"][ns.theme],config["CONTEXT"])
    out=based(Path(ns.output))
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor(),metadata=None if out.suffix==".svg" else {"Software":"Matplotlib"})
    plt.close(fig)
    print(out, out.stat().st_size)

if __name__=="__main__": main()
