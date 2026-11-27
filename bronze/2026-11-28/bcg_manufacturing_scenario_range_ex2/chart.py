import argparse
import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

BASE = Path(__file__).resolve().parent
CFG = json.loads((BASE / 'config.json').read_text())
THEME, CONTEXT = CFG['THEME'], CFG['CONTEXT']

def render(data, theme, context):
    if isinstance(theme, str):
        theme = THEME[theme]
    fig, ax = plt.subplots(figsize=context['figsize'])
    fig.subplots_adjust(**context['margins'])
    fig.patch.set_facecolor(theme['background'])
    ax.set_facecolor(theme['background'])
    if context['kind'] == 'ranked_bar':
        d = data.sort_values('order')
        y = range(len(d))
        ax.barh(y, d.value, height=context['bar_width'], color=theme['colors'][0])
        ax.set_yticks(list(y), d.category, fontsize=11)
        ax.invert_yaxis()
        ax.set_xlim(0, max(d.value)*1.13)
        for i,v in enumerate(d.value):
            ax.text(v+max(d.value)*.007, i, f'{v:g}%', va='center', fontsize=11)
        ax.set_xticks([])
        ax.spines['left'].set_visible(True)
        ax.spines['left'].set_color(theme['axis'])
    else:
        d = data.sort_values('order').reset_index(drop=True)
        if (d.high < d.low).any():
            raise ValueError('high below low')
        x = range(len(d))
        w=context['bar_width']
        ax.bar(x, d.high-d.low, bottom=d.low, width=w, color=theme['colors'][:len(d)])
        span = max(d.high)-min(d.low)
        ax.axhline(context['baseline'], color=theme['axis'], ls='--', lw=.8)
        ax.text(len(d)-.52, context['baseline']+span*.035, f"2025 baseline = {context['baseline']:,}", ha='right', fontsize=10)
        for i,r in d.iterrows():
            ax.text(i,r.high+span*.035,f'{r.high_label}: {r.high:,.0f}',ha='center',va='bottom',fontsize=10)
            ax.text(i,r.low-span*.035,f'{r.low_label}: {r.low:,.0f}',ha='center',va='top',fontsize=10)
            ax.text(i,-.18,f'{r.reported_delta:,.0f}',transform=ax.get_xaxis_transform(),ha='center',va='center',color='white',fontsize=11,fontweight='bold',bbox={'boxstyle':'round,pad=.25','facecolor':theme['colors'][i],'edgecolor':'none'})
        ax.set_xticks(list(x),d.category,fontsize=11)
        ax.set_ylim(*context['ylim'])
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v,p:f'{v:,.0f}'))
        ax.text(-.02,-.18,'Range ($bn)',transform=ax.transAxes,ha='right',va='center',fontsize=10)
        ax.spines['left'].set_visible(True)
        ax.spines['left'].set_color(theme['axis'])
    for s in ['top','right','bottom']:
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0,colors=theme['text'])
    fig.text(.04,.94,context['title'],fontsize=17,fontweight='bold',color=theme['text'],va='top')
    fig.text(.04,.865,context['subtitle'],fontsize=11,color=theme['text'],va='top')
    fig.text(.04,.045,context['note'],fontsize=8,color=theme['text'],va='bottom',wrap=True)
    return fig

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data',type=Path,default=BASE/'data.csv')
    p.add_argument('--config',type=Path,default=BASE/'config.json')
    p.add_argument('--theme',choices=['source','neutral'],default='source')
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--dpi',type=int,default=200)
    a=p.parse_args(); cfg=json.loads(a.config.read_text())
    fig=render(pd.read_csv(a.data),cfg['THEME'][a.theme],cfg['CONTEXT'])
    a.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(a.output,dpi=a.dpi); plt.close(fig)
if __name__=='__main__': main()
