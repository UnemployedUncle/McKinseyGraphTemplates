#!/usr/bin/env python3
"""Source-based, reusable scenario interval and two-period slope charts."""
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def render(data, theme, context):
    chart_type = context['chart_type']
    fig, ax = plt.subplots(figsize=tuple(theme.get('figsize', [11, 6.2])))
    fig.patch.set_facecolor(theme['background'])
    ax.set_facecolor(theme['background'])
    ink, muted = theme['foreground'], theme['muted']
    ax.tick_params(axis='both', labelcolor=ink, colors=theme['grid'])
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.text(.06, .93, context['title'], fontsize=17, weight='bold', color=ink)
    fig.text(.06, .875, context['subtitle'], fontsize=10, color=muted)
    if chart_type == 'interval':
        if len(data) != 1:
            raise ValueError('Interval requires exactly one scenario')
        lo, hi = float(data[0]['low']), float(data[0]['high'])
        if not (0 <= lo <= hi <= 100):
            raise ValueError('Invalid percentage range')
        ax.hlines(0, lo, hi, color=theme['accent'], lw=16, capstyle='round', zorder=3)
        ax.plot([lo, hi], [0, 0], 'o', ms=11, color=theme['accent_dark'], zorder=4)
        for v in [lo, hi]:
            ax.text(v, .22, f'{v:g}%', ha='center', fontsize=14, color=ink, weight='bold')
        ax.set_xlim(*context['xlim'])
        ax.set_ylim(-.5, .6)
        ax.set_yticks([])
        ax.set_xticks(context['xticks'])
        ax.set_xlabel(context['xlabel'], color=ink, labelpad=13)
        ax.grid(axis='x', color=theme['grid'], alpha=.75)
        ax.text((lo + hi) / 2, -.25, f'Range width: {hi-lo:g} pp', ha='center', color=muted)
    elif chart_type == 'slope':
        if len(data) != 2:
            raise ValueError('Slope requires two dated rows')
        rows = sorted(data, key=lambda d: d['period'])
        values = [float(row['value']) for row in rows]
        if not all(0 <= v <= 100 for v in values):
            raise ValueError('Shares must be percentages')
        ax.plot([0,1], values, color=theme['accent'], lw=4, marker='o', markersize=13)
        for i, v in enumerate(values):
            ax.annotate(f'{v:g}%', (i,v), (0,15), textcoords='offset points', ha='center', color=ink, fontsize=15, weight='bold')
        ax.set_xlim(-.3,1.3)
        ax.set_ylim(*context['ylim'])
        ax.set_xticks([0,1], [r['period'] for r in rows])
        ax.set_yticks(context['yticks'])
        ax.set_ylabel(context['ylabel'], color=ink)
        ax.grid(axis='y', color=theme['grid'], alpha=.75)
        ax.text(.5, sum(values)/2-10, f'{values[1]-values[0]:+g} pp', ha='center', color=theme['accent_dark'], fontsize=13, weight='bold')
    else:
        raise ValueError('Unsupported chart type')
    fig.text(.06,.075,context['footer'],fontsize=8.4,color=muted)
    fig.subplots_adjust(left=.12,right=.93,top=.79,bottom=.21)
    return fig

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--data', default='data.csv')
    p.add_argument('--config', default='config.json')
    p.add_argument('--theme', default='source', choices=['source','neutral'])
    p.add_argument('--out', required=True)
    args = p.parse_args()
    with open(args.data, newline='', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    cfg = json.loads(Path(args.config).read_text(encoding='utf-8'))
    fig = render(data, cfg['THEME'][args.theme], cfg['CONTEXT'])
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.out, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)
