#!/usr/bin/env python3
"""Configurable mirrored allocation-intentions butterfly with 2 business panels."""
import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def render(data,theme,context):
    mapping=context.get('column_mapping',{'category':'category','series':'series','value':'value'})
    category,series,value=[mapping[k] for k in ('category','series','value')]
    source=data.copy();source[category]=source[category].astype(str)
    fig,axes=plt.subplots(len(context['panel_order']),1,figsize=theme['figsize'])
    fig.patch.set_facecolor(theme['background']); plt.rcParams['font.family']=theme['font']
    for ax,panel in zip(np.atleast_1d(axes),context['panel_order']):
        labels=context['categories'][panel]
        d=source.pivot_table(index=category,columns=series,values=value,aggfunc='first').reindex(labels)
        dec=d[context['decrease_series']].to_numpy(float); inc=d[context['increase_series']].to_numpy(float)
        if np.isnan(dec).any() or np.isnan(inc).any() or (np.r_[dec,inc] < 0).any() or (np.r_[dec,inc] > 100).any():
            raise ValueError('Invalid respondent percentages or missing categories')
        y=np.arange(len(labels)); ax.set_facecolor(theme['background'])
        ax.barh(y,-dec,height=theme['bar_height'],color=theme['decrease'],label=context['legend_labels']['Decrease'])
        ax.barh(y,inc,height=theme['bar_height'],color=theme['increase'],label=context['legend_labels']['Increase'])
        ax.axvline(0,color=theme['text'],lw=.9)
        ax.set_yticks(y,labels);ax.invert_yaxis();ax.set_xlim(context['axis_min'],context['axis_max'])
        ax.tick_params(axis='y',labelsize=9.2,length=0,pad=10,labelcolor=theme['text'])
        ax.tick_params(axis='x',labelsize=9,length=0,labelcolor=theme['text'])
        for k,(a,b) in enumerate(zip(dec,inc)):
            ax.text(-a-1.0,k,f'{a:.0f}%',ha='right',va='center',fontsize=theme['label_fontsize'],color=theme['text'])
            ax.text(b+1.0,k,f'{b:.0f}%',ha='left',va='center',fontsize=theme['label_fontsize'],color=theme['text'])
        ax.set_xticks(np.arange(context['axis_min']//10*10,context['axis_max']+1,context['axis_step']))
        ax.set_xticklabels([f'{abs(int(v))}%' for v in ax.get_xticks()])
        ax.spines[:].set_visible(False)
        ax.set_title(context['panel_labels'].get(panel,panel),fontsize=12,weight='bold',color=theme['text'],loc='left',pad=12)
        ax.set_axisbelow(True);ax.grid(axis='x',alpha=.42,color=theme['grid'])
    fig.subplots_adjust(**theme['margins'],hspace=theme['panel_spacing'])
    fig.suptitle(context['title'],x=theme['margins']['left'],y=.985,ha='left',fontsize=theme['title_fontsize'],weight='bold',color=theme['text'])
    fig.text(theme['margins']['left'],.918,context['subtitle'],ha='left',fontsize=10,color=theme['text'])
    fig.legend(*axes[-1].get_legend_handles_labels(),loc='lower center',bbox_to_anchor=(0.55,.068),ncol=2,frameon=False,fontsize=9)
    fig.text(theme['margins']['left'],.025,context['source_note'],fontsize=7,color=theme['text'])
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument('--theme',choices=['source','neutral'],default='source');p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json');p.add_argument('--output',default='output.png');a=p.parse_args()
    base=Path(__file__).resolve().parent;cfg=json.loads((base/a.config).read_text(encoding='utf-8'))
    fig=render(pd.read_csv(base/a.data),cfg['THEME'][a.theme],cfg['CONTEXT'])
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,dpi=200,facecolor=fig.get_facecolor());plt.close(fig);print(out.resolve())
if __name__=='__main__':main()
