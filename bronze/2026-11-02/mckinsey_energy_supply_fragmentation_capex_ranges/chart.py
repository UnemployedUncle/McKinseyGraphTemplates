#!/usr/bin/env python3
"""Editable, data-driven consulting chart (no external image or private assets)."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def _rows(path):
    with open(path, newline='', encoding='utf-8-sig') as source:
        return list(csv.DictReader(source))


def _float(value):
    if value is None or str(value).strip() == '':
        return None
    return float(value)


def render(data, theme, context):
    """Render one reusable chart; return a Matplotlib Figure."""
    rows = list(data)
    if not rows:
        raise ValueError('data.csv must contain at least one row')
    chart_type = context['chart_type']
    fig, ax = plt.subplots(figsize=tuple(theme['figure_size']))
    fig.patch.set_facecolor(theme['background'])
    ax.set_facecolor(theme['background'])
    color_map = theme.get('palette', {})
    title = context['title']
    fig.text(0.055, 0.965, title, ha='left', va='top',
             fontsize=theme['title_size'], fontweight='bold',
             color=theme['ink'], linespacing=1.13)
    if context.get('subtitle'):
        fig.text(0.055, context.get('subtitle_y', 0.857), context['subtitle'],
                 ha='left', va='top', fontsize=theme['subtitle_size'],
                 color=theme['muted'])
    if chart_type == 'grouped_bar':
        categories = context.get('category_order') or list(dict.fromkeys(row['category'] for row in rows))
        series = context.get('series_order') or list(dict.fromkeys(row['series'] for row in rows))
        width = float(theme['bar_width'])
        count = len(series)
        centers = list(range(len(categories)))
        for si, item in enumerate(series):
            for ci, cat in enumerate(categories):
                chosen = [r for r in rows if r['category'] == cat and r['series'] == item]
                if len(chosen) != 1:
                    raise ValueError(f'Expected one observation for {cat}/{item}')
                val = _float(chosen[0].get('value'))
                if val is None:
                    raise ValueError('Missing reported value cannot be rendered')
                px = ci + (si - (count-1)/2)*width
                ax.bar(px, val, width=width, color=color_map[item],
                       linewidth=theme.get('edge_width', 0))
                ax.text(px, val+float(theme['label_offset']),
                        context['value_format'].format(val),
                        fontsize=theme['label_size'],ha='center',va='bottom',
                        fontweight='bold',color=theme['ink'])
        ax.set_xlim(-0.5, len(categories)-0.5)
        ax.set_ylim(*context['y_limits'])
        ax.set_xticks(centers, categories,fontsize=theme['tick_size'],color=theme['ink'])
        ax.tick_params(axis='x', length=0)
        ax.set_yticks([])
        for side in ('left','right','top'): ax.spines[side].set_visible(False)
        ax.spines['bottom'].set_color(theme['spine'])
        ax.spines['bottom'].set_linewidth(.8)
        legend_handles = [Patch(facecolor=color_map[s],label=s) for s in series]
        ax.legend(handles=legend_handles,ncol=len(series),loc='lower left',
                  bbox_to_anchor=(0,1.005),frameon=False,fontsize=theme['legend_size'],
                  handlelength=1.1,handleheight=.8,handletextpad=.3,columnspacing=.5,
                  borderaxespad=0)
        for ann in context.get('gap_annotations', []):
            idx = categories.index(ann['category'])
            ax.vlines(idx, ymin=ann.get('line_start',30),
                      ymax=ann.get('line_end',80),
                      color=theme['ink'],linestyles=(0,(3,3)),linewidth=1.15)
            ax.text(idx+.025,ann.get('text_y',77),ann['text'],
                    fontsize=theme['annotation_size'],color=theme['ink'],
                    ha='left',va='center')
    elif chart_type == 'horizontal_bar':
        categories = context.get('category_order') or [r['category'] for r in sorted(rows,key=lambda r:-float(r['value']))]
        lookup = {r['category']: r for r in rows}
        if len(lookup) != len(rows): raise ValueError('Duplicate categories')
        bars = []
        for cat in categories:
            if cat not in lookup: raise ValueError(f'Unknown category {cat}')
            val = _float(lookup[cat].get('value'))
            if val is None: raise ValueError('Missing values are not plotted')
            bars.append(val)
        y = list(range(len(categories)))
        colors = [theme.get('highlight',theme['default']) if c in context.get('highlight_categories', [])
                  else theme['default'] for c in categories]
        ax.barh(y,bars,color=colors,height=theme['bar_width'])
        for ypos,v in zip(y,bars):
            ax.text(v + theme['label_offset'], ypos, context['value_format'].format(v),
                    va='center',fontsize=theme['label_size'],color=theme['ink'],fontweight='bold')
        ax.invert_yaxis()
        ax.set_yticks(y,categories,fontsize=theme['tick_size'],color=theme['ink'])
        ax.set_xlim(*context['x_limits']);ax.set_xticks(context['x_ticks'])
        ax.tick_params(axis='x',labelsize=theme['axis_size'],colors=theme['muted'],length=0)
        ax.tick_params(axis='y',length=0,pad=9)
        if theme.get('grid',False): ax.grid(axis='x',alpha=.13,zorder=0)
        ax.set_axisbelow(True)
        for s in ax.spines.values(): s.set_visible(False)
    elif chart_type == 'range_plot':
        categories=context.get('category_order') or [r['category'] for r in rows]
        lookup={r['category']:r for r in rows}
        for i,cat in enumerate(categories):
            r=lookup[cat];lo=_float(r['lower']);hi=_float(r['upper'])
            if lo is None or hi is None or lo>hi: raise ValueError(f'Invalid range for {cat}')
            color=theme['highlight'] if cat in context.get('highlight_categories',[]) else theme['default']
            ax.plot([lo,hi],[i,i],linewidth=theme['line_width'],color=color,solid_capstyle='round')
            ax.scatter([lo,hi],[i,i],s=theme['marker_size'],color=color,edgecolors=theme['background'],linewidths=1.2,zorder=4)
            ax.text(hi+theme['label_offset'],i,context['range_format'].format(lo,hi),
                    va='center',fontsize=theme['label_size'],color=theme['ink'],fontweight='bold')
        ax.invert_yaxis()
        ax.set_ylim(len(categories)-.5+.6, -1.1)
        ax.set_yticks(range(len(categories)),categories,fontsize=theme['tick_size'],color=theme['ink'])
        ax.set_xlim(*context['x_limits']);ax.set_xticks(context['x_ticks'])
        ax.tick_params(axis='x',labelsize=theme['axis_size'],colors=theme['muted'],length=0)
        ax.tick_params(axis='y',length=0,pad=10)
        if theme.get('grid',False): ax.grid(axis='x',alpha=.14)
        ax.set_axisbelow(True)
        for s in ax.spines.values():s.set_visible(False)
    else:
        raise ValueError(f'Unsupported chart_type: {chart_type}')
    fig.subplots_adjust(**theme['margins'])
    if context.get('source_note'):
        fig.text(.055,.04,context['source_note'],fontsize=theme['footnote_size'],
                 color=theme['muted'],va='bottom')
    return fig


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',default='data.csv')
    parser.add_argument('--config',default='config.json')
    parser.add_argument('--theme',choices=['source','neutral'],default='source')
    parser.add_argument('--output',default='output.png')
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    csv_path=Path(args.data)
    if not csv_path.exists():csv_path=root/csv_path
    config_path=Path(args.config)
    if not config_path.exists():config_path=root/config_path
    config=json.loads(config_path.read_text(encoding='utf-8'))
    fig=render(_rows(csv_path),config['THEME'][args.theme],config['CONTEXT'])
    fig.savefig(args.output,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__=='__main__':main()
