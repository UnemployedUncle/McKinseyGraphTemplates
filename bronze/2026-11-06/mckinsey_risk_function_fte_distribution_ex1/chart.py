#!/usr/bin/env python3
"""Reusable ranked horizontal chart of risk-function capacity shares."""
import csv,json,argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def render(data,theme,context):
    rows=sorted(data,key=lambda d:(-float(d['value']),int(d['order'])))
    values=[float(d['value']) for d in rows];cats=[r['category'] for r in rows]
    fig,ax=plt.subplots(figsize=tuple(theme.get('figsize',[11.5,8.4])))
    fig.patch.set_facecolor(theme['background']);ax.set_facecolor(theme['background'])
    colors=[theme['highlight'] if v>=context['highlight_min'] else theme['neutral_bar'] for v in values]
    bars=ax.barh(range(len(rows)),values,color=colors,height=.62)
    for p,v in zip(bars,values):
        ax.text(v+.45,p.get_y()+p.get_height()/2,f'{v:g}%',va='center',ha='left',fontsize=10,fontweight='bold',color=theme['text'])
    ax.set_yticks(range(len(rows)),cats,fontsize=10,color=theme['text']);ax.invert_yaxis()
    ax.set_xlim(0,max(values)*1.20);ax.set_xticks([0,10,20,30]);ax.set_xticklabels(['0%','10%','20%','30%'])
    ax.tick_params(axis='x',length=0,labelsize=9,colors=theme['subtle']);ax.tick_params(axis='y',length=0,pad=9)
    ax.grid(axis='x',color=theme['grid'],linewidth=.7);ax.set_axisbelow(True)
    for spine in ax.spines.values():spine.set_visible(False)
    ax.set_title(context['title'],loc='left',fontsize=16,fontweight='bold',color=theme['text'],pad=28)
    ax.text(0,1.02,context['subtitle'],transform=ax.transAxes,fontsize=10,color=theme['subtle'])
    fig.text(.06,.024,context['footnote'],fontsize=8,color=theme['subtle'])
    fig.subplots_adjust(left=.32,right=.91,top=.86,bottom=.09)
    return fig

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data',default='data.csv');ap.add_argument('--config',default='config.json');ap.add_argument('--theme',choices=['source','neutral'],default='neutral');ap.add_argument('--output',default='output.png');a=ap.parse_args()
    with open(a.data,encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    cfg=json.loads(Path(a.config).read_text(encoding='utf-8'));fig=render(rows,cfg['THEME'][a.theme],cfg['CONTEXT'])
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
if __name__=='__main__':main()
