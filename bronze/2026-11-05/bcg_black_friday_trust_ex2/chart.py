#!/usr/bin/env python3
"""BCG-inspired horizontal ranking; all appearance controlled by config.json."""
import argparse, csv, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def render(data, theme, context):
    """Render full (11-factor) net-trust ranking; return Matplotlib Figure."""
    values=[float(r['value']) for r in data]
    if not data or any(v < -100 or v > 100 for v in values):
        raise ValueError('Net trust score must be between -100 and 100 percentage points')
    if len(set(r['category'] for r in data)) != len(data):
        raise ValueError('Duplicate categories')
    fig,ax=plt.subplots(figsize=theme['figsize'],facecolor=theme['background'])
    fig.subplots_adjust(**theme['margins'])
    ax.set_facecolor(theme['background'])
    positions=list(range(len(data)))
    colors=[theme['colors'][r['group']] for r in data]
    ax.barh(positions,values,height=.67,color=colors,zorder=2)
    ax.invert_yaxis()
    ax.set_yticks(positions,labels=[r['category'] for r in data])
    for label in ax.get_yticklabels():
        label.set_fontsize(theme['label_size']);label.set_color(theme['text'])
    ax.set_xlim(0,max(values)*1.10)
    for i,v in enumerate(values):
        ax.text(v+.65,i,f'{v:g}',fontsize=theme['value_size'],color=theme['text'],weight='bold',va='center',ha='left')
    ax.tick_params(axis='y',length=0,pad=10)
    ax.set_xticks([]);ax.tick_params(axis='x',length=0)
    for spine in ax.spines.values():spine.set_visible(False)
    fig.text(.045,.94,context['title'],ha='left',va='top',fontsize=theme['title_size'],weight='bold',color=theme['text'])
    fig.text(.045,.887,context['subtitle'],ha='left',va='top',fontsize=10.5,color=theme['muted'])
    groups=list(dict.fromkeys(r['group'] for r in data))
    fig.legend(handles=[Patch(facecolor=theme['colors'][g],label=context['group_labels'][g]) for g in groups],
               loc='lower center',bbox_to_anchor=(.64,.062),ncol=3,frameon=False,fontsize=9)
    fig.text(.045,.028,context['footnote'],va='bottom',ha='left',fontsize=7.9,color=theme['muted'])
    return fig

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json')
    p.add_argument('--theme',choices=['source','neutral'],default='source');p.add_argument('--output',required=True)
    a=p.parse_args();cfg=json.loads(Path(a.config).read_text(encoding='utf-8'))
    with open(a.data,encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    fig=render(rows,cfg['THEME'][a.theme],cfg['CONTEXT'])
    output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,dpi=200,facecolor=cfg['THEME'][a.theme]['background']);plt.close(fig)
if __name__=='__main__':main()
