#!/usr/bin/env python3
"""Editorial small-multiple endpoint lollipop; does not imply intermediate observations."""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def render(data, theme, context):
    """Render two period panels; data is a list of per-cohort endpoint records."""
    periods = context["periods"]
    fig, axes = plt.subplots(1, len(periods), figsize=tuple(theme["figsize"]), layout="constrained")
    if len(periods)==1: axes=[axes]
    fig.patch.set_facecolor(theme["background"])
    for ax,period in zip(axes,periods):
        rows=sorted([r for r in data if r["period"]==period],key=lambda x: int(x["rank"]))
        ax.set_facecolor(theme["background"])
        y=list(range(len(rows)))
        vals=[float(r["value_index"]) for r in rows]
        maxval=max(vals)
        for i,(r,v) in enumerate(zip(rows,vals)):
            color=theme["focus"] if r["cohort"]==context["focus_cohort"] else theme["neutral"]
            ax.hlines(i,0,v,color=color,lw=5,alpha=.65)
            ax.scatter(v,i,color=color,s=75,zorder=4)
            ax.text(v+maxval*.035,i,f'{v:,.0f}',va='center',fontsize=12,weight='bold',color=theme['text'])
        ax.set_yticks(y,[r["cohort_label"] for r in rows],fontsize=11)
        ax.invert_yaxis()
        ax.set_xlim(0,maxval*1.27);ax.set_ylim(len(rows)-.4,-.6)
        ax.set_xlabel(context["x_label"],fontsize=10,color=theme['muted'])
        ax.set_title(context["panel_titles"][period],loc='left',color=theme['text'],fontsize=13,weight='bold',pad=16)
        ax.grid(axis='x',color=theme['grid'],linestyle=':',alpha=.55)
        ax.spines[:].set_visible(False)
        ax.tick_params(axis='both',length=0,colors=theme['text'])
        for label in ax.get_xticklabels(): label.set_fontsize(9)
    fig.suptitle(context['title'],fontsize=17,weight='bold',color=theme['text'],x=.01,ha='left')
    fig.text(.01,-.045,context['footnote'],fontsize=8,color=theme['muted'])
    return fig


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json');p.add_argument('--theme',choices=['source','neutral'],default='source');p.add_argument('--output',default='source.png');args=p.parse_args()
    with open(args.data,newline='',encoding='utf-8') as f: data=list(csv.DictReader(f))
    cfg=json.loads(Path(args.config).read_text(encoding='utf-8'))
    fig=render(data,cfg['THEME'][args.theme],cfg['CONTEXT'])
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,dpi=200,bbox_inches='tight',facecolor=fig.get_facecolor())
    plt.close(fig)

if __name__=='__main__':main()
