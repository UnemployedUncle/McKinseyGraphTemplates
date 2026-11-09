#!/usr/bin/env python3
"""Two-panel horizontal bar reconstruction from published figure text."""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def render(data,theme,context):
    fig,axes=plt.subplots(2,1,figsize=tuple(theme['figsize']),layout='constrained')
    fig.patch.set_facecolor(theme['background'])
    for ax,panel in zip(axes,context['panels']):
        rows=sorted([r for r in data if r['scenario']==panel],key=lambda r:int(r['rank']))
        vals=[float(r['final_savings_eur'])/1000 for r in rows]
        colors=[theme['focus'] if r['highlight']=='yes' else theme['neutral'] for r in rows]
        bars=ax.barh(range(len(rows)),vals,color=colors,height=.58)
        ax.set_yticks(range(len(rows)),[r['product_label'] for r in rows],fontsize=10)
        ax.invert_yaxis()
        ax.set_xlim(0,max(vals)*1.35)
        for v,bar,r in zip(vals,bars,rows):
            ax.text(v+2,bar.get_y()+bar.get_height()/2,f'€{int(float(r["final_savings_eur"])):,}',ha='left',va='center',color=theme['text'],fontsize=11,weight='bold')
            ax.text(1,bar.get_y()+bar.get_height()/2,f'{r["annual_gross_return_pct"]}% gross · {r["annual_cost_pct"]}% cost',ha='left',va='center',color=theme['onbar'],fontsize=8)
        ax.set_title(context['panel_titles'][panel],loc='left',color=theme['text'],fontsize=12,weight='bold',pad=12)
        ax.set_xlabel(context['x_label'],fontsize=9,color=theme['muted'])
        ax.grid(axis='x',color=theme['grid'],linestyle=':',alpha=.4)
        ax.set_axisbelow(True)
        ax.spines[:].set_visible(False)
        ax.tick_params(axis='both',length=0,colors=theme['text'])
    fig.suptitle(context['title'],fontsize=16,weight='bold',color=theme['text'],x=.01,ha='left')
    fig.text(.01,-.045,context['footnote'],fontsize=8,color=theme['muted'])
    return fig


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json');p.add_argument('--theme',choices=['source','neutral'],default='source');p.add_argument('--output',default='source.png');a=p.parse_args()
    with open(a.data,newline='',encoding='utf-8') as f: data=list(csv.DictReader(f))
    cfg=json.loads(Path(a.config).read_text(encoding='utf-8'))
    fig=render(data,cfg['THEME'][a.theme],cfg['CONTEXT'])
    Path(a.output).parent.mkdir(parents=True,exist_ok=True);fig.savefig(a.output,dpi=200,bbox_inches='tight',facecolor=fig.get_facecolor());plt.close(fig)

if __name__=='__main__':main()
