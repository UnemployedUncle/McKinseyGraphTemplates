#!/usr/bin/env python3
"""BCG-style annual policy-interventions stacked columns; editable via CSV + JSON."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def render(data, theme, context):
    mapping = context.get("column_mapping", {"category":"category","series":"series","value":"value"})
    category, series, value = [mapping[k] for k in ("category","series","value")]
    frame = data.copy()
    frame[category] = frame[category].astype(str)
    ordered = context.get("year_order") or list(dict.fromkeys(frame[category]))
    parts = context.get("series_order", ["Advanced economies", "Other economies"])
    pivot = frame.pivot_table(index=category, columns=series, values=value, aggfunc="first").reindex(ordered)
    if pivot[parts + [context["total_series"]]].isna().any().any():
        raise ValueError("Missing components/annual totals: source data cannot be rendered")
    values = [pivot[p].to_numpy(float) for p in parts]
    totals = pivot[context["total_series"]].to_numpy(float)
    if not np.allclose(np.sum(values, axis=0), totals, atol=1.0):
        raise ValueError("Stack segments do not sum to reported totals")
    x = np.arange(len(ordered))
    plt.rcParams["font.family"] = theme["font"]
    fig, ax = plt.subplots(figsize=theme["figsize"])
    fig.patch.set_facecolor(theme["background"]); ax.set_facecolor(theme["background"])
    colors = [theme["primary"], theme["secondary"]]
    bottom=np.zeros(len(ordered))
    for p, h, color in zip(parts,values,colors):
        ax.bar(x,h,bottom=bottom,color=color,width=theme["bar_width"],label=p,edgecolor="none")
        bottom += h
    for xi,total in zip(x, totals):
        ax.annotate(f"{total:,.0f}",(xi,total),ha="center",va="bottom",fontsize=theme["label_fontsize"],color=theme["text"],weight="bold",xytext=(0,4),textcoords="offset points")
    ax.set_xticks(x,ordered)
    ax.tick_params(axis='both',labelsize=9,length=0,colors=theme['text'])
    ax.set_ylim(context['axis_min'],context['axis_max'])
    ax.set_yticks(np.arange(context['axis_min'],context['axis_max']+1,context['axis_step']))
    ax.set_yticklabels([f'{i:,.0f}' for i in ax.get_yticks()])
    ax.spines[['top','right','left']].set_visible(False)
    ax.spines['bottom'].set_color(theme['grid']);ax.yaxis.grid(False)
    for a in context.get('annotations',[]):
        ix=ordered.index(str(a['category']))
        ax.annotate(a['text'],xy=(ix,totals[ix]+80),xytext=(ix,a['at_y']),ha='center',va='bottom',fontsize=8,color=theme['text'],arrowprops={'arrowstyle':'-|>','color':theme['annotation_color'],'lw':theme['line_width']})
    fig.suptitle(context['title'],x=theme['margins']['left'],y=.975,ha='left',fontsize=theme['title_fontsize'],weight='bold',color=theme['text'])
    fig.text(theme['margins']['left'],theme.get('subtitle_y',.84),context['subtitle'],ha='left',fontsize=10,color=theme['text'])
    ax.set_ylabel(context['y_label'],labelpad=11,color=theme['text'])
    handles, labels = ax.get_legend_handles_labels()
    legend_order = context.get('legend_order', parts)
    legend_map = dict(zip(labels, handles))
    fig.legend([legend_map[name] for name in legend_order], legend_order, loc='lower center',
               bbox_to_anchor=(0.5,.095),ncol=2,frameon=False,
               fontsize=theme.get('legend_fontsize',8))
    fig.text(theme['margins']['left'],.04,context['source_note'],fontsize=7,color=theme['text'])
    fig.subplots_adjust(**theme['margins'])
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument('--theme',choices=['source','neutral'],default='source');p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json');p.add_argument('--output',default='output.png');a=p.parse_args()
    base=Path(__file__).resolve().parent
    config=json.loads((base/a.config).read_text(encoding='utf-8'))
    fig=render(pd.read_csv(base/a.data),config['THEME'][a.theme],config['CONTEXT'])
    output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(output.resolve())
if __name__=='__main__':main()
