#!/usr/bin/env python3
"""Reusable, attribution-aware consulting charts: render(data, theme, context) -> fig."""
import argparse, csv, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter, FixedLocator, FixedFormatter

def render(data, theme, context):
    colors=theme['colors']
    fig, ax=plt.subplots(figsize=theme.get('figsize',[11,6.2]))
    fig.patch.set_facecolor(colors['background']);ax.set_facecolor(colors['background'])
    fig.subplots_adjust(**theme.get('margins',dict(left=.25,right=.94,bottom=.16,top=.80)))
    for spine in ax.spines.values():spine.set_visible(False)
    ax.tick_params(length=0,labelsize=theme.get('tick_fontsize',9),colors=colors['text'],pad=7)
    ax.set_axisbelow(True)
    kind=context['chart_type']
    if kind=='scatter':
        ax.set_xlim(*context.get('xlim',[0,60]));ax.set_ylim(*context.get('ylim',[0,30]))
        ax.set_aspect('auto')
        xb=context.get('x_axis_compression')
        def tx(x):
            if not xb:return x
            return x if x<=xb['start'] else xb['start']+(x-xb['start'])*xb['factor']
        if xb:
            ticks=xb.get('tick_values',[0,10,20,30,40,100])
            ax.xaxis.set_major_locator(FixedLocator([tx(x) for x in ticks]))
            ax.xaxis.set_major_formatter(FixedFormatter([str(x) for x in ticks]))
        else:ax.xaxis.set_major_locator(MultipleLocator(context.get('x_step',10)))
        ax.yaxis.set_major_locator(MultipleLocator(context.get('y_step',5)))
        ax.grid(axis='both',color=colors['grid'],lw=.7)
        xx=[context['xlim'][0],context['xlim'][1]]
        ax.fill_between(xx,[0,0],[min(context['ylim'][1],v) for v in xx],color=colors['increase_zone'],alpha=.22,zorder=0)
        ax.fill_between(xx,[min(context['ylim'][1],v) for v in xx],[context['ylim'][1]]*2,color=colors['decrease_zone'],alpha=.16,zorder=0)
        ax.plot(xx,xx,ls='--',lw=1.3,color=colors['diagonal'],zorder=1)
        for row in data:
            x=tx(float(row['x']));y=float(row['y'])
            ax.scatter(x,y,s=theme.get('marker_size',45),color=colors['dot'],edgecolor='white',linewidth=.65,zorder=3)
            ax.annotate(row['label'],(x,y),xytext=(float(row.get('label_dx') or 5),float(row.get('label_dy') or 5)),
                textcoords='offset points',ha='left',va='bottom',fontsize=theme.get('label_fontsize',7.0),color=colors['text'])
        ax.set_xlabel(context['x_label'],fontsize=11,color=colors['text'],labelpad=15)
        ax.set_ylabel(context['y_label'],fontsize=11,color=colors['text'],labelpad=15)
        ax.text(.04,.94,context['upper_zone_label'],transform=ax.transAxes,color=colors['text'],fontsize=9,va='top')
        ax.text(.96,.08,context['lower_zone_label'],transform=ax.transAxes,color=colors['text'],fontsize=9,ha='right')
    elif kind=='barh':
        rows=sorted(data,key=lambda x:float(x['value']))
        names=[r['label'] for r in rows];values=[float(r['value']) for r in rows]
        highlights=set(context.get('highlights',[]))
        bars=ax.barh(range(len(rows)),values,color=[colors['highlight'] if r['label'] in highlights else colors['bar'] for r in rows],height=.6)
        ax.set_yticks(range(len(rows)),names)
        ax.set_xlim(0,context.get('x_max',max(values)*1.3))
        ax.xaxis.set_major_locator(MultipleLocator(context.get('x_step',2)))
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'{x:.0f}%'))
        ax.grid(axis='x',color=colors['grid'],lw=.8)
        for rect,v in zip(bars,values):
            ax.text(rect.get_width()+.22,rect.get_y()+rect.get_height()/2,f'{v:g}%',ha='left',va='center',fontsize=10,fontweight='bold',color=colors['text'])
        ax.set_xlabel(context['x_label'],fontsize=11,color=colors['text'],labelpad=12)
    else:raise ValueError(f'Unknown chart_type {kind}')
    fig.text(theme.get('title_x',.07),.955,context['title'],ha='left',va='top',fontsize=theme.get('title_size',15),fontweight='bold',color=colors['text'])
    fig.text(theme.get('title_x',.07),.905,context['subtitle'],ha='left',va='top',fontsize=theme.get('subtitle_size',9),color=colors['muted'])
    fig.text(theme.get('title_x',.07),.045,context['footnote'],ha='left',va='bottom',fontsize=theme.get('footnote_size',8),color=colors['muted'])
    return fig

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data',default='data.csv');p.add_argument('--config',default='config.json')
    p.add_argument('--theme',choices=['source','neutral'],default='source');p.add_argument('--output',required=True)
    a=p.parse_args()
    with open(a.data,encoding='utf-8',newline='') as f: data=list(csv.DictReader(f))
    cfg=json.loads(Path(a.config).read_text(encoding='utf-8'))
    fig=render(data,cfg['THEME'][a.theme],cfg['CONTEXT'])
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(a.output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
if __name__=='__main__':main()
