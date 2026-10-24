#!/usr/bin/env python3
"""Config-first, reproducible consulting data chart. Original figure pixels not included."""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def _display(data, t, c):
    kind=c['chart_kind']
    if kind == 'absolute_stacked_columns':
        years=c['period_order']; segments=c['series_order']
        lookup={(str(r['period']),r['series']):r for r in data}
        total={y:float(next(r['total'] for r in data if str(r['period'])==str(y))) for y in years}
        if any(abs(sum(float(lookup[(y,s)]['value']) for s in segments)-100)>0.01 for y in years):
            raise ValueError('Percent shares must sum to 100 within each period')
        fig=plt.figure(figsize=t['figsize'],facecolor=t['background']); ax=fig.add_axes(t['axes_rect'],facecolor=t['background'])
        x=list(range(len(years))); bot=[0.0]*len(years)
        for s in segments:
            percentages=[float(lookup[(y,s)]['value']) for y in years]
            heights=[total[y]*v/100 for y,v in zip(years,percentages)]
            bars=ax.bar(x, heights, bottom=bot,width=t['bar_width'],color=t['palette'][s],edgecolor=t['background'],linewidth=t['bar_edge_width'])
            for i,(h,v) in enumerate(zip(heights,percentages)):
                ax.text(i,bot[i]+h/2,f'{v:g}%',ha='center',va='center',fontsize=t['segment_label_size'],color=t['label_color'][s],weight='bold' if s==c['highlight_series'] else 'normal')
            bot=[p+h for p,h in zip(bot,heights)]
        for i,y in enumerate(years):
            ax.text(i,total[y]+t['total_offset'],f'{total[y]:,.0f}',ha='center',va='bottom',weight='bold',fontsize=t['total_label_size'],color=t['text'])
        ax.set_xticks(x,[f'{y}\npipeline' for y in years],fontsize=t['category_label_size'],color=t['text'])
        ax.set_xlim(-t['x_padding'],len(years)-1+t['x_padding']);ax.set_ylim(0,max(total.values())*t['headroom']);ax.set_yticks([])
        ax.tick_params(axis='x',length=0,pad=t['category_label_pad'])
        for spine in ax.spines.values():spine.set_visible(False)
        handles=[Patch(color=t['palette'][s],label=c['legend_labels'][s]) for s in c['legend_order']]
        fig.legend(handles=handles,ncol=len(handles),loc='lower center',bbox_to_anchor=t['legend_anchor'],frameon=False,fontsize=t['legend_size'])
    elif kind == 'horizontal_comparison':
        ordered=c['category_order']; lookup={r['category']:r for r in data}
        if any(cat not in lookup for cat in ordered):raise ValueError('missing category')
        values=[float(lookup[cat]['value']) for cat in ordered]
        if any(v<0 or v>100 for v in values):raise ValueError('share outside 0..100')
        fig=plt.figure(figsize=t['figsize'],facecolor=t['background']);ax=fig.add_axes(t['axes_rect'],facecolor=t['background'])
        yy=list(range(len(ordered)))
        colors=[t['highlight'] if name==c['highlight_category'] else t['base_color'] for name in ordered]
        ax.barh(yy,values,color=colors,height=t['bar_height'],zorder=3)
        ax.set_yticks(yy,[c['category_labels'].get(s,s) for s in ordered],fontsize=t['category_label_size'])
        ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xticks(c['x_ticks']);ax.set_xlabel(c['xlabel'],labelpad=12,color=t['muted']);ax.grid(axis='x',color=t['grid'],alpha=.9,zorder=0)
        for i,v in enumerate(values):ax.text(v+t['label_offset'],i,('~' if ordered[i] in c.get('approximate_categories',[]) else '')+f'{v:g}%',ha='left',va='center',fontweight='bold',fontsize=t['label_size'],color=t['text'])
        for spine in ax.spines.values():spine.set_visible(False)
        ax.tick_params(axis='x',length=0,colors=t['muted']);ax.tick_params(axis='y',length=0,pad=10,colors=t['text'])
    else:raise ValueError('Unsupported chart kind: '+str(kind))
    fig.text(t['header_x'],t['exhibit_y'],c['exhibit'],fontsize=t['exhibit_size'],weight='bold',color=t['text'],ha='left')
    fig.text(t['header_x'],t['title_y'],c['title'],fontsize=t['title_size'],family=t['title_family'],ha='left',color=t['text'],weight=t['title_weight'])
    fig.text(t['header_x'],t['subtitle_y'],c['subtitle'],fontsize=t['subtitle_size'],ha='left',color=t['text'])
    fig.text(t['header_x'],t['source_y'],c['source'],fontsize=t['source_size'],ha='left',color=t['muted'])
    if c.get('note'):fig.text(t['header_x'],t['note_y'],c['note'],fontsize=t['source_size'],color=t['muted'],ha='left')
    return fig

def render(data, theme, context):
    return _display(data,theme,context)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--theme',choices=['source','neutral'],default='source')
    ap.add_argument('--data',default='data.csv')
    ap.add_argument('--output',default='output.png')
    ap.add_argument('--config',default='config.json')
    opts=ap.parse_args()
    folder=Path(__file__).resolve().parent
    cfg=json.loads((folder/opts.config).read_text(encoding='utf-8'))
    file=Path(opts.data);file=file if file.is_absolute() else folder/file
    with file.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    fig=render(rows,cfg['THEME'][opts.theme],cfg['CONTEXT'])
    out=Path(opts.output);out=out if out.is_absolute() else folder/out
    out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig);print('CREATED',out)
if __name__=='__main__':main()
