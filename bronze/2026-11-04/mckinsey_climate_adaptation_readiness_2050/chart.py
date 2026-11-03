#!/usr/bin/env python3
"""Reusable source/neutral consulting chart from strictly typed CSV observations."""
import argparse, csv, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


def render(data, theme, context):
    """Return a matplotlib figure using source/neutral theme and business context."""
    plt.rcParams.update({'font.family':'DejaVu Sans','axes.spines.top':False,'axes.spines.right':False})
    fig, ax = plt.subplots(figsize=tuple(theme['figsize']), facecolor=theme['background'])
    ax.set_facecolor(theme['background'])
    fig.subplots_adjust(**theme['margins'])
    if context['chart_type']=='scatter':
        assert len(data)>0
        mapping=theme['colors']
        order=['China_controls','China_no_controls','Other_mixed']
        for g in order:
            rows=[r for r in data if r['group']==g]
            ax.scatter([float(r['extraction_concentration']) for r in rows],
                       [float(r['processing_concentration']) for r in rows],
                       s=theme['marker_size'],color=mapping[g],
                       marker='D' if g=='China_controls' else 'o',zorder=3,label=context['groups'][g])
            if theme.get('show_labels',True):
                for r in rows:
                    x=float(r['extraction_concentration']);y=float(r['processing_concentration'])
                    dx,dy=context.get('offsets',{}).get(r['category'],[5,5])
                    ax.annotate(r['category'],(x,y),xytext=(dx,dy),textcoords='offset points',
                                fontsize=theme['label_size'],color=theme['text'],ha='left' if dx>=0 else 'right',va='center')
        ax.set_xlim(-.03,1.06);ax.set_ylim(-.05,1.05)
        ax.set_xticks([0,.2,.4,.6,.8,1]);ax.set_yticks([0,.5,1]);
        ax.grid(color=theme['grid'],alpha=.6,linewidth=.8)
        ax.set_xlabel(context['x_label'],fontsize=10,color=theme['text'],labelpad=12)
        ax.set_ylabel(context['y_label'],fontsize=10,color=theme['text'],labelpad=12)
        ax.legend(loc='upper center',bbox_to_anchor=(.5,-.23),ncol=3,frameon=False,fontsize=8)
    elif context['chart_type']=='stacked':
        assert len(data)==2
        vals=[float(r['value']) for r in data];total=sum(vals)
        assert 0<total and abs(total-1150)<1e-6
        left=0
        for r,value in zip(data,vals):
            color=theme['colors'][r['category']]
            ax.barh([0],width=value,left=left,height=.42,color=color)
            ax.text(left+value/2,0,f"${value:,.0f}B\n{value/total:.0%}",ha='center',va='center',
                    fontsize=14,color=theme['inside_text'],weight='bold')
            left+=value
        ax.set_xlim(0,total);ax.set_ylim(-.7,.9);ax.axis('off')
        handles=[Patch(facecolor=theme['colors'][r['category']],label=r['label']) for r in data]
        ax.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,-.05),ncol=2,frameon=False,fontsize=9)
        ax.text(total/2,.57,context['subtitle'],ha='center',va='center',fontsize=11,color=theme['text'])
    else:
        raise ValueError('Unknown chart_type')
    fig.suptitle(context['title'],x=theme['title_x'],y=theme['title_y'],ha='left',fontsize=theme['title_size'],fontweight='bold',color=theme['text'])
    fig.text(.075,.035,context['footnote'],fontsize=8,color=theme['muted'],ha='left')
    return fig


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',default='data.csv');parser.add_argument('--config',default='config.json')
    parser.add_argument('--theme',choices=['source','neutral'],default='source');parser.add_argument('--output',required=True)
    args=parser.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding='utf-8'))
    with open(args.data,newline='',encoding='utf-8') as f:data=list(csv.DictReader(f))
    fig=render(data,cfg['THEME'][args.theme],cfg['CONTEXT'])
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,dpi=200,facecolor=cfg['THEME'][args.theme]['background'])
    plt.close(fig)

if __name__=='__main__':main()
