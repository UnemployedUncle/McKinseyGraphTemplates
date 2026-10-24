#!/usr/bin/env python3
"""Reusable 100% stacked-bars, based on reported source figures (NOT pixel-identical)."""
import argparse,json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.colors import to_rgb

THEME = None
CONTEXT = None

def render(data, theme, context):
    order=context['series_order']; cats=context['category_order']
    df=data.copy()
    df['value']=pd.to_numeric(df['value'], errors='coerce')
    wide=df.pivot_table(index='series', columns='category', values='value',aggfunc='first').reindex(index=order,columns=cats)
    if wide.isna().any().any():
        raise ValueError('Missing numeric category/series combination; will not invent values')
    sums=wide.sum(axis=1)
    if not all(abs(v-100)<=1.0 for v in sums):
        raise ValueError(f'Expected ~100% within rounding, found {sums.to_dict()}')
    plt.rcParams['font.family']=theme['font_family']
    plt.rcParams['font.size']=theme['font_size']
    fig,ax=plt.subplots(figsize=tuple(theme['figsize']))
    fig.patch.set_facecolor(theme['background']);ax.set_facecolor(theme['background'])
    bars=[];bottom=[0.0]*len(order)
    for cat in cats:
        vals=wide[cat].tolist()
        container=ax.barh(order,vals,height=theme['bar_height'],left=bottom, color=theme['palette'][cat],edgecolor=theme['background'],linewidth=2,label=cat)
        for i,(p,val) in enumerate(zip(container.patches,vals)):
            if val>=theme['label_minimum']:
                r,g,b=to_rgb(theme['palette'][cat]); luminance=.2126*r+.7152*g+.0722*b
                color='white' if luminance<.57 else theme['text']
                ax.text(bottom[i]+val/2,i,context['label_format'].format(val),ha='center',va='center',color=color,fontweight='bold' if cat==context['highlight_category'] else 'normal',fontsize=theme['font_size'])
        bottom=[a+b for a,b in zip(bottom,vals)]
    ax.set_xlim(*context['x_limits']);ax.set_xticks(context['x_ticks'])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x,_: f'{x:.0f}%'))
    ax.set_xlabel(context['xlabel'],color=theme['muted'],labelpad=15)
    ax.set_ylabel(context.get('ylabel',''))
    ax.grid(axis='x',color=theme['grid'],lw=.7)
    ax.set_axisbelow(True)
    for spine in ax.spines.values(): spine.set_visible(False)
    ax.tick_params(axis='x',length=0,colors=theme['muted'])
    ax.tick_params(axis='y',length=0,colors=theme['text'],labelsize=14)
    ax.invert_yaxis()
    fig.subplots_adjust(left=theme['left'],right=theme['right'],top=theme['top'],bottom=theme['bottom'])
    fig.text(.08,.94,context['title'],ha='left',fontsize=theme['title_size'],fontweight='bold',color=theme['text'])
    fig.text(.08,.88,context['subtitle'],ha='left',fontsize=theme['font_size'],color=theme['muted'])
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles,labels,loc='lower center',bbox_to_anchor=(.52,.09),ncol=3,frameon=False,fontsize=10)
    fig.text(.08,.028,context['source'],ha='left',fontsize=9,color=theme['muted'])
    return fig

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--theme',choices=['source','neutral'],default='source')
    parser.add_argument('--data',default='data.csv');parser.add_argument('--output',default='output.png')
    parser.add_argument('--config',default='config.json');args=parser.parse_args()
    d=Path(__file__).resolve().parent
    config=json.loads((d/args.config).read_text(encoding='utf-8'))
    src=Path(args.data);src=src if src.is_absolute() else d/src
    data=pd.read_csv(src,encoding='utf-8-sig',dtype={'series':str})
    fig=render(data,config['THEME'][args.theme],config['CONTEXT'])
    dest=Path(args.output);dest=dest if dest.is_absolute() else d/dest
    fig.savefig(dest,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f'CREATED {dest}')
if __name__=='__main__':main()
