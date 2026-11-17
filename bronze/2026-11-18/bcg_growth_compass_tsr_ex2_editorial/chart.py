#!/usr/bin/env python3
"""Self-contained, reusable consulting exhibit from source data and display settings."""
from __future__ import annotations
import csv
import json
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent

def render(data, theme, context):
    fig, ax = plt.subplots(figsize=(11, 6.2))
    fig.set_facecolor(theme['background'])
    ax.set_facecolor(theme['background'])
    ink, quiet, accent = theme['text'], theme['muted'], theme['accent']
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
    kind = context['kind']
    if kind == 'paired_dots':
        ordered = list(data)
        ys = list(range(len(ordered)))[::-1]
        for row, y in zip(ordered, ys):
            v = float(row['value_pct'])
            if row.get('benchmark_pct', '').strip():
                benchmark = float(row['benchmark_pct'])
                ax.plot([benchmark, v], [y, y], color=quiet, lw=3, zorder=2, alpha=.55)
                ax.scatter([benchmark], [y], color=theme['benchmark'], s=130, zorder=3)
                ax.annotate(f'{benchmark:g}%', (benchmark, y), xytext=(0,-18), textcoords='offset points', ha='center', fontsize=10, color=quiet)
            ax.scatter([v], [y], color=accent, s=220, zorder=4)
            ax.annotate(f'{v:g}%', (v, y), xytext=(0,12), textcoords='offset points', ha='center', fontsize=11, fontweight='bold', color=ink)
        ax.set_yticks(ys, [row['company'] for row in ordered], color=ink)
        ax.set_xlim(0, max(float(r['value_pct']) for r in ordered)*1.21)
        ax.set_ylim(-.55, len(ordered)-.35)
        ax.set_xlabel(context['x_label'], color=quiet, labelpad=12)
        ax.legend(handles=[Line2D([0],[0],marker='o',ls='',color=accent,label='Company TSR'),
                           Line2D([0],[0],marker='o',ls='',color=theme['benchmark'],label='Industry median')],
                  loc='lower right',frameon=False,labelcolor=ink,fontsize=9)
        ax.text(.99, .97, 'Aurobindo: peer median not disclosed', transform=ax.transAxes, ha='right',va='top',color=quiet,fontsize=8)
    elif kind == 'status_bar':
        rows = list(data)
        xs=range(len(rows))
        vals=[float(row['value_gbp_billion']) for row in rows]
        cols=[theme['benchmark'] if row['status']=='observed' else accent for row in rows]
        bars=ax.bar(xs, vals, color=cols, width=.47, zorder=3)
        for bar,row,value in zip(bars,rows,vals):
            if row['status']=='forecast':
                bar.set_hatch('//')
                bar.set_edgecolor(theme['text'])
                bar.set_linewidth(.8)
            ax.text(bar.get_x()+bar.get_width()/2,value+.22,f'£{value:.1f}bn',ha='center',va='bottom',color=ink,fontsize=14,fontweight='bold')
            ax.text(bar.get_x()+bar.get_width()/2,.15,row['status'].upper(),ha='center',va='bottom',color=theme['background'] if row['status']=='forecast' else ink,fontsize=8,fontweight='medium')
        ax.set_xticks(list(xs),[row['time_label'] for row in rows],color=ink)
        ax.set_ylim(0,max(vals)*1.26)
        ax.set_ylabel(context['y_label'],color=quiet,labelpad=10)
        diff=vals[1]-vals[0]
        ax.text(.5,.92,f'+£{diff:.1f}bn potential increase',transform=ax.transAxes,ha='center',fontsize=12,fontweight='bold',color=accent)
    else:
        raise ValueError(f'Unknown chart kind: {kind}')
    ax.grid(axis='x' if kind=='paired_dots' else 'y',color=theme['grid'],linewidth=.7,alpha=.75,zorder=0)
    for s in ax.spines.values():s.set_visible(False)
    ax.tick_params(axis='both',length=0,colors=quiet,pad=9)
    ax.set_title(context['title'],loc='left',color=ink,fontweight='bold',fontsize=16,pad=33)
    fig.text(.1,.055,context['footnote'],color=quiet,fontsize=7.8,ha='left')
    fig.subplots_adjust(left=.22,right=.93,top=.76,bottom=.18)
    return fig

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--theme',choices=['source','neutral'],required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    cfg=json.loads((HERE/'config.json').read_text(encoding='utf-8'))
    with (HERE/'data.csv').open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    fig=render(rows,cfg['THEME'][args.theme],cfg['CONTEXT'])
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f'Rendered {out} at 200dpi, theme={args.theme}, rows={len(rows)}')
if __name__=='__main__':main()
