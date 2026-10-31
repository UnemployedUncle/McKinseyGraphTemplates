#!/usr/bin/env python3
"""Recreate a waterfall for illustrative relative cost reductions."""
from pathlib import Path
import argparse, json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,PercentFormatter


def render(data, theme, context):
    data=data.sort_values(context['columns']['order']).reset_index(drop=True)
    vals=data[context['columns']['y']].astype(float).to_numpy()
    labels=data[context['columns']['category']].astype(str).to_list()
    assert len(vals)>=3 and vals[0]>=0 and abs(vals[-1]-(vals[0]+sum(vals[1:-1])))<1e-6, 'Components do not reconcile'
    fig,ax=plt.subplots(figsize=theme['figsize'],facecolor=theme['background'])
    ax.set_facecolor(theme['background']);running=float(vals[0]);bars=[]
    for i,v in enumerate(vals):
        if i==0 or i==len(vals)-1: bottom=0;h=v;col=theme['base_color'] if i==0 else theme['final_color']
        else: bottom=running+v if v<0 else running; h=abs(v);col=theme['reduction_color'];running+=v
        ax.bar(i,h,bottom=bottom,width=theme['bar_width'],color=col)
        bars.append((bottom,h))
        ax.text(i,bottom+h+theme['label_offset'],context['number_format'].format(v),ha='center',va='bottom',fontsize=theme['label_fontsize'],fontweight='bold',color=theme['text_color'])
    ax.set_ylim(*context['ylim']);ax.set_xlim(-0.65,len(labels)-0.35)
    ax.set_xticks(list(range(len(labels))),labels,fontsize=theme['tick_fontsize'])
    ax.yaxis.set_major_locator(MultipleLocator(context['y_tick_step']))
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=100,decimals=0))
    ax.tick_params(axis='x',length=0,pad=theme['tick_pad']);ax.tick_params(axis='y',length=0,labelsize=theme['tick_fontsize'])
    ax.grid(axis='y',color=theme['grid_color'],alpha=.5,linewidth=.65)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():spine.set_visible(False)
    fig.text(*theme['title_pos'],context['title'],fontsize=theme['title_fontsize'],fontweight='bold',color=theme['text_color'])
    fig.text(*theme['subtitle_pos'],context['subtitle'],fontsize=theme['subtitle_fontsize'],color=theme['text_color'])
    fig.text(*theme['source_pos'],context['source_note'],fontsize=theme['source_fontsize'],color=theme['source_color'])
    fig.subplots_adjust(**theme['margins'])
    return fig


def main():
    p=argparse.ArgumentParser();p.add_argument('--theme',choices=['source','neutral'],default='source')
    p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json');p.add_argument('--output',default='output.png')
    a=p.parse_args();folder=Path(__file__).resolve().parent
    cfg=json.loads((folder/a.config).read_text(encoding='utf-8'))
    fig=render(pd.read_csv(folder/a.data),cfg['THEME'][a.theme],cfg['CONTEXT'])
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
if __name__=='__main__':main()
