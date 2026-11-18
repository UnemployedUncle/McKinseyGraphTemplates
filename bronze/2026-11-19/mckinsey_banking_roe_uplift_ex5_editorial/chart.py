#!/usr/bin/env python3
"""Reusable quantitative chart; content from CSV, visual design from JSON."""
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent


def render(data, theme, context):
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
    fig, ax = plt.subplots(figsize=(11, 6.2))
    bg, ink, quiet = theme['background'], theme['text'], theme['muted']
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    kind = context['kind']
    if kind == 'comparison_bar':
        rows = list(data)
        values = [float(row['value']) for row in rows]
        xs = list(range(len(rows)))
        bars = ax.bar(xs, values, width=.55,
                      color=[theme['neutral'] if row['status'] == 'weak' else theme['accent'] for row in rows])
        ax.set_ylim(0, max(values) * 1.25)
        ax.set_xlim(-.48, len(rows)-.52)
        ax.set_xticks(xs, [row['label'] for row in rows], color=ink, fontsize=12)
        ax.set_yticks([])
        for bar, value in zip(bars, values):
            ax.text(bar.get_x()+bar.get_width()/2, value+.35, f'{value:g}%',
                    ha='center', va='bottom', fontsize=17, color=ink, fontweight='bold')
        ax.axhline(0, color=quiet, lw=.8)
    elif kind == 'stacked_share':
        rows = list(data)
        left = 0.0
        for row in rows:
            value = float(row['value'])
            color = theme['accent'] if row['status']=='high_dependency' else theme['neutral']
            ax.barh([0], [value], left=left, height=.38, color=color)
            ax.text(left + value/2, 0, f'~{value:g}%', ha='center', va='center',
                    color=theme['on_accent'] if row['status']=='high_dependency' else ink,
                    fontsize=17, fontweight='bold')
            left += value
        ax.set_xlim(0, 100)
        ax.set_ylim(-.46,.56)
        ax.set_yticks([])
        ax.set_xlabel(context['x_label'], color=quiet)
        ax.set_xticks([0,20,40,60,80,100], ['0','20','40','60','80','100%'])
        for row in rows:
            ax.plot([], [], color=theme['accent'] if row['status']=='high_dependency' else theme['neutral'],
                    linewidth=7, label=row['label'])
        ax.legend(loc='upper center', bbox_to_anchor=(.5,1.04), ncol=2,
                  frameon=False, labelcolor=ink, fontsize=10)
    elif kind == 'waterfall':
        rows = list(data)
        baseline = float(rows[0]['value'])
        deltas = [float(row['value']) for row in rows[1:]]
        xs = list(range(len(rows)+1))
        totals = [baseline]
        for delta in deltas:
            totals.append(totals[-1] + delta)
        bar_values = [baseline] + deltas + [totals[-1]]
        bottom = [0] + totals[:-1] + [0]
        colors = [theme['neutral']] + [theme['accent']]*len(deltas) + [theme['final']]
        ax.bar(xs,bar_values,bottom=bottom,width=.55,color=colors)
        for i in range(1,len(totals)):
            ax.plot([i-1+.275,i-.275],[totals[i-1]]*2,color=quiet,lw=1)
        labels = [rows[0]['label']] + [r['label'] for r in rows[1:]] + [context['total_label']]
        ax.set_xticks(xs,labels,fontsize=9,color=ink)
        ax.set_xlim(-.6,len(xs)-.4)
        ax.set_ylim(0,max(totals)*1.24)
        ax.set_ylabel(context['y_label'],color=quiet)
        for i,(v,b) in enumerate(zip(bar_values,bottom)):
            fmt = f'+{v:g}pp' if 0<i<len(xs)-1 else f'{v:g}%'
            ax.text(i,b+v+.3,fmt,ha='center',fontsize=13,color=ink,fontweight='bold')
        ax.grid(axis='y',alpha=.22,color=quiet)
    else:
        raise ValueError(f'Unknown chart kind {kind}')
    if kind != 'stacked_share':
        ax.grid(axis='y',alpha=.10,color=quiet)
    ax.set_axisbelow(True)
    for side in ax.spines.values():
        side.set_visible(False)
    ax.tick_params(length=0, colors=quiet, pad=9)
    ax.set_title(context['title'],loc='left',color=ink,fontsize=15,fontweight='bold',pad=35)
    fig.text(.08,.055,context['footnote'],color=quiet,fontsize=8)
    fig.subplots_adjust(left=.10,right=.94,top=.75,bottom=.20)
    return fig


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',default=str(HERE/'data.csv'))
    parser.add_argument('--config',default=str(HERE/'config.json'))
    parser.add_argument('--theme',choices=['source','neutral'],required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with Path(args.data).open(newline='',encoding='utf-8') as f:
        data=list(csv.DictReader(f))
    cfg=json.loads(Path(args.config).read_text(encoding='utf-8'))
    fig=render(data,cfg['THEME'][args.theme],cfg['CONTEXT'])
    out=Path(args.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f'render theme={args.theme} rows={len(data)} path={out} dpi=200')

if __name__=='__main__':
    main()
