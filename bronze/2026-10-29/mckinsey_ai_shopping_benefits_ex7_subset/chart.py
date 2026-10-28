#!/usr/bin/env python3
"""Reusable, provenance-aware consulting comparison chart. No source image is copied."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parent

def read_csv(path: Path) -> list[dict]:
    with path.open(encoding='utf-8-sig', newline='') as f:
        data=list(csv.DictReader(f))
    if not data:
        raise ValueError('Empty input table')
    for row in data:
        if row['provenance'] not in {'reported','derived','digitized_estimate','missing','synthetic'}:
            raise ValueError('Unsupported provenance')
        row['value'] = None if not row['value'] else float(row['value'])
    return data

def render(data: list[dict], theme: dict, context: dict):
    """Render a reusable bar or dumbbell chart from a long-form dataset."""
    kind=context['chart_type']
    fig, ax = plt.subplots(figsize=theme['size'], facecolor=theme['background'])
    ax.set_facecolor(theme['background'])
    fig.subplots_adjust(left=theme['left'],right=theme['right'],bottom=theme['bottom'],top=theme['top'])
    fig.text(theme['left'],theme['title_y'],context['title'],ha='left',va='top',
             color=theme['text'],fontsize=theme['title_size'],weight='bold')
    fig.text(theme['left'],theme['subtitle_y'],context['subtitle'],ha='left',va='top',
             color=theme['muted'],fontsize=theme['subtitle_size'])
    groups=context['category_order']
    y=np.arange(len(groups))
    if kind=='horizontal_bar':
        series=context['series_order'][0]
        rows={(r['category'],r['series']):r for r in data}
        vals=[]
        for g in groups:
            row=rows[(g,series)]
            if row['value'] is None:
                raise ValueError('Missing values cannot be plotted without an explicit policy')
            vals.append(row['value'])
        colors=[theme['highlight'] if g in context['highlight_categories'] else theme['primary'] for g in groups]
        ax.barh(y,vals,height=theme['bar_height'],color=colors,zorder=3)
        for i,v in enumerate(vals):
            ax.text(v+theme['label_offset'],i,context['value_format'].format(v),va='center',ha='left',
                    fontsize=theme['label_size'],color=theme['text'],fontweight='semibold')
        ax.set_xlim(context['axis_min'],context['axis_max'])
    elif kind=='dumbbell':
        rows={(r['category'],r['series']):r for r in data}
        current, ceilings=[],[]
        for g in groups:
            v1=rows[(g,context['series_order'][0])]['value']
            v2=rows[(g,context['series_order'][1])]['value']
            if v1 is None or v2 is None:
                raise ValueError('Missing values cannot be plotted without an explicit policy')
            current.append(v1);ceilings.append(v2)
        for i,(v1,v2) in enumerate(zip(current,ceilings)):
            ax.plot([v1,v2],[i,i],color=theme['connector'],lw=theme['line_width'],zorder=2)
            ax.scatter([v1],[i],color=theme['highlight'],s=theme['dot_size'],zorder=4)
            ax.scatter([v2],[i],facecolor=theme['background'],edgecolor=theme['primary'],
                       linewidth=theme['outline_width'],s=theme['dot_size'],zorder=4)
            ax.text(v1,i-theme['above_offset'],context['value_format'].format(v1),
                    ha='center',va='bottom',color=theme['highlight'],fontsize=theme['label_size'],weight='bold')
            ax.text(v2+theme['label_offset'],i,context['value_format'].format(v2),
                    ha='left',va='center',color=theme['primary'],fontsize=theme['label_size'],weight='bold')
        ax.set_xlim(context['axis_min'],context['axis_max'])
        ax.plot([],[],marker='o',linestyle='None',color=theme['highlight'],label=context['series_labels'][0])
        ax.plot([],[],marker='o',linestyle='None',markerfacecolor=theme['background'],
                markeredgecolor=theme['primary'],label=context['series_labels'][1])
        ax.legend(frameon=False,loc='lower right',bbox_to_anchor=(1,1.01),ncol=2,
                  fontsize=theme['legend_size'],labelcolor=theme['text'])
    else:
        raise ValueError('Unknown chart_type: '+str(kind))
    ax.set_yticks(y,groups,fontsize=theme['category_size'],color=theme['text'])
    ax.invert_yaxis()
    ax.set_xticks(context['ticks'])
    ax.set_xlabel(context['axis_label'],fontsize=theme['label_size'],color=theme['text'])
    ax.tick_params(axis='x',labelsize=theme['tick_size'],colors=theme['muted'],length=0,pad=8)
    ax.tick_params(axis='y',length=0,pad=10)
    ax.xaxis.grid(True,color=theme['grid'],linewidth=0.8,zorder=0)
    for spine in ax.spines.values():spine.set_visible(False)
    fig.text(theme['left'],theme['source_y'],context['source_note'],ha='left',va='bottom',
             fontsize=theme['source_size'],color=theme['muted'])
    return fig

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data',default=str(BASE/'data.csv'))
    p.add_argument('--config',default=str(BASE/'config.json'))
    p.add_argument('--theme',choices=['source','neutral'],default='source')
    p.add_argument('--output',default='output.png')
    a=p.parse_args()
    cfg=json.loads(Path(a.config).read_text(encoding='utf-8'))
    fig=render(read_csv(Path(a.data)),cfg['THEME'][a.theme],cfg['CONTEXT'])
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
if __name__=='__main__':main()
