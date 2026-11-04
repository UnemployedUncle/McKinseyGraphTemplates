#!/usr/bin/env python3
"""Editable 2035 market model regional scenario stacked-bar view."""
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def render(data,theme,context):
    """Render the reported regional base/upside figures; return Matplotlib Figure."""
    order=context['scenario_order'];regions=context['region_order']
    lookup={(r['scenario'],r['region']):float(r['value_usd_bn']) for r in data}
    if len(lookup)!=len(data) or set(lookup)!={(s,r) for s in order for r in regions}:
        raise ValueError('Expected exactly one observation per scenario-region combination')
    if any(v<0 for v in lookup.values()):raise ValueError('Market size cannot be negative')
    totals=[sum(lookup[(s,r)] for r in regions) for s in order]
    fig,ax=plt.subplots(figsize=theme['figsize'],facecolor=theme['background'])
    fig.subplots_adjust(**theme['margins']);ax.set_facecolor(theme['background'])
    for i,s in enumerate(order):
        bottom=0
        for r in regions:
            v=lookup[(s,r)]
            ax.bar(i,v,bottom=bottom,width=.54,color=theme['colors'][r])
            if v>=20:
                ax.text(i,bottom+v/2,f'{v:g}',ha='center',va='center',color='#FFFFFF' if r in ('United States','China') else '#1B2734',fontweight='bold',fontsize=9)
            bottom+=v
        ax.text(i,bottom+12,f'${bottom:g}B',ha='center',va='bottom',fontsize=14,fontweight='bold',color=theme['text'])
    ax.set_xlim(-.65,len(order)-.35);ax.set_ylim(0,max(totals)*1.17)
    ax.set_xticks(range(len(order)),[context['annotations'][s] for s in order]);
    ax.tick_params(axis='x',length=0,labelsize=theme['label_size'])
    ax.tick_params(axis='y',colors=theme['muted'])
    ax.set_ylabel(context['y_label'],fontsize=10,color=theme['muted']);ax.grid(axis='y',color='#E6EBEF',alpha=.8)
    ax.set_axisbelow(True)
    for side in ('top','right','left'):ax.spines[side].set_visible(False)
    ax.spines['bottom'].set_color('#C7D0D9')
    handles=[Patch(color=theme['colors'][r],label=r) for r in regions]
    fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.51,.105),ncol=4,frameon=False,fontsize=9)
    fig.text(.055,.942,context['title'],ha='left',va='top',fontsize=theme['title_size'],fontweight='bold',color=theme['text'])
    fig.text(.055,.893,context['subtitle'],ha='left',va='top',fontsize=10,color=theme['muted'])
    fig.text(.055,.02,context['footnote'],ha='left',va='bottom',fontsize=8,color=theme['muted'])
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json')
    p.add_argument('--theme',choices=['source','neutral'],default='source');p.add_argument('--output',required=True)
    a=p.parse_args();cfg=json.loads(Path(a.config).read_text(encoding='utf-8'))
    with open(a.data,encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    fig=render(rows,cfg['THEME'][a.theme],cfg['CONTEXT'])
    output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,dpi=200,facecolor=cfg['THEME'][a.theme]['background']);plt.close(fig)
if __name__=='__main__':main()
