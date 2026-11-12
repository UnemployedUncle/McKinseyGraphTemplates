#!/usr/bin/env python3
"""Reproducible consulting chart; only CSV and THEME/CONTEXT settings control appearance."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def render(data: pd.DataFrame, theme: dict, context: dict):
    kind = context['chart_type']
    fs = theme.get('figure_size', [12, 7])
    fig, ax = plt.subplots(figsize=fs)
    bg = theme.get('background', '#FFFFFF')
    fg = theme.get('text', '#24313C')
    accent = theme.get('accent', '#147D67')
    second = theme.get('secondary', '#A8B9B2')
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    for sp in ax.spines.values(): sp.set_visible(False)
    if kind == 'ranked_index':
        val = context['value_col']; lab = context['label_col']
        frame = data.sort_values(val, ascending=False).reset_index(drop=True)
        y = list(range(len(frame)))
        colors = [accent if v in context['highlight_categories'] else second for v in frame[lab]]
        ax.barh(y, frame[val].astype(float), height=.67, color=colors, zorder=2)
        ax.set_yticks(y, frame[lab].tolist(), fontsize=11, color=fg)
        ax.invert_yaxis()
        ax.set_xlim(0, context['max_x'])
        ax.set_xlabel(context['x_label'], fontsize=11, color=fg, labelpad=10)
        ax.xaxis.set_major_locator(MultipleLocator(20))
        ax.grid(axis='x', color=theme['grid'], alpha=.6, zorder=0)
        for yi, v in zip(y, frame[val]):
            ax.text(float(v)+1.3, yi, f'{float(v):g}', va='center', fontsize=11,
                    color=fg, fontweight='bold', clip_on=False)
        fig.subplots_adjust(left=.22,right=.93,top=.80,bottom=.19)
    elif kind == 'import_width_marimekko':
        frame = data.sort_values(context['value_col'], ascending=False).reset_index(drop=True)
        widths = frame[context['width_col']].astype(float).to_numpy()
        total = widths.sum(); xpos = 0.0; mids=[]
        for _,row in frame.iterrows():
            w = float(row[context['width_col']]);
            three = float(row[context['three_col']]); two = float(row[context['two_col']]);
            xleft=xpos+.018*w
            usable=.965*w
            ax.bar(xleft, two, width=usable, align='edge', color=accent, edgecolor=bg, linewidth=.7, zorder=3)
            ax.bar(xleft, three, bottom=two, width=usable, align='edge', color=theme['highlight'], edgecolor=bg, linewidth=.7, zorder=3)
            mids.append(xpos+w*.5); xpos += w
        ax.set_xlim(0,total); ax.set_ylim(0,40)
        ax.set_yticks([0,10,20,30,40],labels=['0','10','20','30','40'])
        ax.set_xticks(mids, frame[context['label_col']].tolist(), rotation=70, ha='right', fontsize=8, color=fg)
        ax.set_ylabel(context['y_label'], fontsize=11,color=fg)
        ax.tick_params(axis='x', length=0, pad=5)
        ax.grid(axis='y', color=theme['grid'],alpha=.6,zorder=0)
        for x,(_,row) in zip(mids,frame.iterrows()):
            if float(row[context['width_col']])>=350:
                ax.text(x,float(row[context['value_col']])+.9,f"{row[context['value_col']]:g}%",
                        ha='center',va='bottom',fontsize=8,color=fg,fontweight='bold')
        ax.bar(0,0,color=accent,label='Exactly two vulnerabilities')
        ax.bar(0,0,color=theme['highlight'],label='All three vulnerabilities')
        ax.legend(frameon=False,loc='upper right',ncol=2,fontsize=9)
        fig.subplots_adjust(left=.09,right=.96,top=.78,bottom=.28)
    else:
        raise ValueError(f'Unsupported chart_type: {kind}')
    fig.text(.055,.966,context['title'],fontsize=17,fontweight='bold',ha='left',va='top',color=fg)
    fig.text(.055,.923,context['subtitle'],fontsize=10.5,ha='left',va='top',color=theme['muted'])
    fig.text(.055,.035,context['footnote'],fontsize=8,ha='left',va='bottom',color=theme['muted'])
    return fig


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',required=True)
    parser.add_argument('--config',required=True)
    parser.add_argument('--theme',choices=['source','neutral'],required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    frame=pd.read_csv(args.data)
    cfg=json.loads(Path(args.config).read_text(encoding='utf-8'))
    fig=render(frame,cfg['THEME'][args.theme],cfg['CONTEXT'])
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)

if __name__ == '__main__': main()
