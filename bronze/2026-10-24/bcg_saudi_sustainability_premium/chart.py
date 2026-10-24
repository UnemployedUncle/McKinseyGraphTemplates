#!/usr/bin/env python3
"""Reusable two-category donut based on reported results; editorial design, not original."""
import argparse,json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

THEME = None
CONTEXT = None

def render(data,theme,context):
    df=data.copy();df['value']=pd.to_numeric(df['value'],errors='coerce')
    order=context['category_order'];val=df.set_index('category')['value'].reindex(order)
    if val.isna().any() or abs(float(val.sum())-100)>1:raise ValueError('Missing/inconsistent 100% share data')
    plt.rcParams['font.family']=theme['font_family'];plt.rcParams['font.size']=theme['font_size']
    fig=plt.figure(figsize=tuple(theme['figsize']),facecolor=theme['background']);ax=fig.add_axes(theme['donut_rect'])
    ax.pie(val.to_numpy(),startangle=theme['start_angle'],counterclock=False,
       colors=[theme['accent'],theme['secondary']],
       wedgeprops={'width':theme['ring_width'],'edgecolor':theme['background'],'linewidth':3})
    ax.text(0,.12,context['label_format'].format(float(val.iloc[0])),ha='center',va='center',fontsize=theme['center_size'],fontweight='bold',color=theme['accent'])
    ax.text(0,-.21,context['center_sublabel'],ha='center',va='center',fontsize=13,color=theme['muted'],linespacing=1.35)
    ax.set(aspect='equal');ax.axis('off')
    fig.text(.065,.92,context['title'],ha='left',fontsize=theme['title_size'],fontweight='bold',color=theme['text'])
    fig.text(.065,.845,context['subtitle'],ha='left',fontsize=theme['font_size'],color=theme['muted'])
    for i,(name,v) in enumerate(zip(order,val)):
        y=theme['label_y_start']-i*theme['label_y_step']
        fig.text(.75,y,context['label_format'].format(v),ha='left',va='center',fontsize=24,fontweight='bold',color=[theme['accent'],theme['text']][i])
        fig.text(.75,y-.068,name,ha='left',va='center',fontsize=10,color=theme['muted'],wrap=True)
    fig.text(.065,.06,context['source'],fontsize=9,color=theme['muted'])
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument('--theme',choices=['source','neutral'],default='source')
    p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json');p.add_argument('--output',default='output.png');a=p.parse_args()
    d=Path(__file__).resolve().parent;config=json.loads((d/a.config).read_text(encoding='utf-8'))
    input_file=Path(a.data);input_file=input_file if input_file.is_absolute() else d/input_file
    df=pd.read_csv(input_file,encoding='utf-8-sig')
    fig=render(df,config['THEME'][a.theme],config['CONTEXT'])
    output_file=Path(a.output);output_file=output_file if output_file.is_absolute() else d/output_file
    fig.savefig(output_file,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
    print(f'CREATED {output_file}')
if __name__=='__main__':main()
