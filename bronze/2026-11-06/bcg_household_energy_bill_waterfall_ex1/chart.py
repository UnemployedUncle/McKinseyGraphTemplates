#!/usr/bin/env python3
"""Configurable household energy bill waterfall; no source graphic assets."""
import argparse,csv,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def render(data,theme,context):
    rows=sorted(data,key=lambda r:int(r['order']))
    comps=[r for r in rows if r['kind']=='baseline_component']
    steps=[r for r in rows if r['kind']!='baseline_component']
    total=sum(float(r['value']) for r in comps)
    if total <= 0: raise ValueError('Positive baseline required')
    fig,ax=plt.subplots(figsize=tuple(theme.get('figsize',[14,7.5])))
    fig.patch.set_facecolor(theme['background']);ax.set_facecolor(theme['background'])
    left=0; y=0
    basecols=theme['baseline_colors']
    for r,color in zip(comps,basecols):
        value=float(r['value']);ax.add_patch(Rectangle((left-.32,y),.64,value,facecolor=color,edgecolor='none'))
        ax.text(left,y+value/2,f'{value:,.0f}',ha='center',va='center',size=9,color=theme['inbar_text'],fontweight='bold')
        y+=value
    ax.text(left,total+95,f'{total:,.0f}',ha='center',color=theme['text'],fontsize=10,fontweight='bold')
    running=total; previous=0
    checkpoint_index=0
    for x,r in enumerate(steps,start=1):
        amount=float(r['value']);kind=r['kind']
        if kind=='saving':
            bottom=running-amount
            ax.plot([previous+.33,x-.33],[running,running],color=theme['connector'],lw=.8,zorder=1)
            ax.add_patch(Rectangle((x-.32,bottom),.64,amount,facecolor=theme['saving_colors'][min(x-1,len(theme['saving_colors'])-1)],edgecolor='none'))
            ax.text(x,bottom+amount/2 if amount>=350 else bottom+amount+80, f'{amount:,.0f}',ha='center',va='center',fontsize=9,color=theme['inbar_text'] if amount>=350 else theme['text'],fontweight='bold')
            running=bottom
        else:
            assert abs(running-amount)<1e-6,'Reported subtotal does not reconcile'
            ax.plot([previous+.33,x-.33],[running,running],color=theme['connector'],lw=.8,zorder=1)
            checkpoint_index+=1
            color=theme['checkpoint_colors']['today' if checkpoint_index==1 else 'future']
            ax.add_patch(Rectangle((x-.32,0),.64,amount,facecolor=color,edgecolor='none'))
            ax.text(x,amount/2,f'{amount:,.0f}\n({(amount/total)*100:.0f}%)',ha='center',va='center',size=10,color='#FFFFFF',fontweight='bold')
            ax.text(x, total+115, f'{(1-amount/total)*100:.0f}% saving',ha='center',fontsize=10,color=theme['text'],fontweight='bold')
            ax.plot([x,x],[total-30,amount+100],color=theme['connector'],lw=.8,alpha=.6)
        previous=x
    labels=[context['first_label']]+[r['category'].replace('|','\n') for r in steps]
    ax.set_xticks(range(len(labels)));ax.set_xticklabels(labels,fontsize=8.5,color=theme['text'])
    ax.set_xlim(-.65,len(labels)-.35);ax.set_ylim(-70,total*1.17)
    ax.set_yticks([]);[sp.set_visible(False) for sp in ax.spines.values()]
    ax.tick_params(axis='x',length=0,pad=12)
    ax.set_title(context['title'],loc='left',color=theme['text'],fontsize=16,fontweight='bold',pad=28)
    ax.text(0,1.015,context['subtitle'],transform=ax.transAxes,fontsize=10,color=theme['text'])
    fig.text(.08,.028,context['footnote'],size=8,color=theme['subtle'])
    fig.subplots_adjust(left=.07,right=.98,top=.83,bottom=.27)
    return fig

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data',default='data.csv');ap.add_argument('--config',default='config.json');ap.add_argument('--theme',choices=['source','neutral'],default='neutral');ap.add_argument('--output',default='output.png');a=ap.parse_args()
    with open(a.data,encoding='utf-8',newline='') as f: data=list(csv.DictReader(f))
    cfg=json.loads(Path(a.config).read_text(encoding='utf-8'));fig=render(data,cfg['THEME'][a.theme],cfg['CONTEXT'])
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
if __name__=='__main__':main()
