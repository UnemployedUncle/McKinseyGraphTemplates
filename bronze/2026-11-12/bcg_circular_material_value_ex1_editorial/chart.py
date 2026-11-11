#!/usr/bin/env python3
"""Configurable matplotlib editorial comparison based only on published data."""
import argparse, csv, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def read_rows(path):
    with open(path,encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def render(data, theme, context):
    fig=plt.figure(figsize=tuple(theme.get("figure_size",[11,6.2])),facecolor=theme["background"])
    kind=context["chart_type"]
    if kind=="stock_flow_dual":
        groups=[("stock",[.08,.23,.35,.51]),("annual_flow",[.55,.23,.37,.51])]
        for j,(group,rect) in enumerate(groups):
            rows=[row for row in data if row["group"]==group]
            if not rows: raise ValueError("Missing observations: "+group)
            vals=[float(r["value"]) for r in rows]
            ax=fig.add_axes(rect)
            bars=ax.barh(range(len(vals)),vals,height=.52, color=[theme["accent"] if i==0 else theme["secondary"] for i in range(len(vals))])
            ax.set_xlim(0,max(vals)*1.35);ax.invert_yaxis();ax.set_yticks([])
            ax.set_title(context["panel_titles"][j],loc="left",fontsize=12,fontweight="bold",pad=15)
            ax.set_xlabel(context["panel_axis_labels"][j])
            for i,(bar,row,v) in enumerate(zip(bars,rows,vals)):
                marker=">" if row["qualifier"]=="lower_bound" else "≈"
                ax.text(max(vals)*.025,bar.get_y()+bar.get_height()/2,row["metric"],va="center",fontsize=8.4,color=theme["background"] if i==0 else theme["text"])
                ax.text(v+max(vals)*.03,bar.get_y()+bar.get_height()/2,f"{marker}€{v:g}B",va="center",fontsize=11,color=theme["text"])
            ax.grid(axis="x",alpha=.13);ax.set_axisbelow(True)
            ax.spines[['right','top','left']].set_visible(False);ax.tick_params(axis="y",length=0)
    elif kind=="horizontal_oversupply":
        rows=sorted(data,key=lambda r:float(r["value"]))
        vals=[float(r["value"]) for r in rows]
        ax=fig.add_axes([.29,.25,.62,.51])
        bars=ax.barh(range(len(vals)),vals,height=.52,color=[theme["secondary"],theme["accent"]])
        ax.set_yticks(range(len(vals)),[r["metric"] for r in rows]);ax.set_xlim(0,max(vals)*1.23)
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"{x:g}%"));ax.set_xlabel(context["axis_label"])
        for bar,v in zip(bars,vals):ax.text(v+max(vals)*.026,bar.get_y()+bar.get_height()/2,f"+{v:g}%",va="center",fontsize=13,fontweight="bold",color=theme["text"])
        ax.grid(axis="x",alpha=.13);ax.set_axisbelow(True)
        ax.spines[['right','top','left']].set_visible(False);ax.tick_params(axis="y",length=0)
    else:raise ValueError("Unsupported chart type")
    fig.suptitle(context["title"],x=.07,y=.96,ha="left",fontsize=17,fontweight="bold",color=theme["text"])
    fig.text(.07,.88,context["subtitle"],fontsize=10,color=theme["text"])
    fig.text(.07,.07,context["footnote"],fontsize=8.2,color=theme["footnote"])
    return fig

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--data",default="data.csv");p.add_argument("--config",default="config.json")
    p.add_argument("--theme",choices=["source","neutral"],default="source")
    p.add_argument("--output",default="source.png")
    a=p.parse_args();cfg=json.loads(Path(a.config).read_text(encoding="utf-8"))
    fig=render(read_rows(a.data),cfg["THEME"][a.theme],cfg["CONTEXT"])
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
    print(out)
