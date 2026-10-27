#!/usr/bin/env python3
"""Reproducible consulting chart: replace data.csv and THEME/CONTEXT in config.json."""
from pathlib import Path
import argparse, csv, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

HERE = Path(__file__).resolve().parent

def load_data(path):
    with Path(path).open(newline='', encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    for row in rows:
        row['value']=float(row['value']) if row['value'].strip() else float('nan')
    return rows

def render(data, theme, context):
    """Return matplotlib Figure. Accept rows from load_data()."""
    fig=plt.figure(figsize=theme['size'], facecolor=theme['background'])
    ax=fig.add_axes([theme['plot_left'],theme['plot_bottom'],theme['plot_right']-theme['plot_left'],theme['plot_top']-theme['plot_bottom']])
    ax.set_facecolor(theme['background'])
    kind=context['chart_type']; ink=theme['ink']
    ax.tick_params(axis='both',colors=ink,labelsize=theme['font_size'],length=0,pad=8)
    ax.spines[:].set_visible(False)
    if kind=='stacked_column':
        order=context['series_order']; values={r['category']:r['value'] for r in data}
        if set(order)!=set(values): raise ValueError('series_order does not match data')
        total=sum(values.values()); bottom=0
        if total<=0: raise ValueError('Nonpositive total')
        ax.set_ylim(0,100); ax.set_xlim(-0.58,0.58)
        for name in order:
            # Reported percentages are rounded and total 101%; normalize only DRAWN heights.
            shown=float(values[name]); height=shown/total*100
            ax.bar(0,height,width=0.89,bottom=bottom,color=theme['colors'][name],edgecolor=theme['line_color'],linewidth=1.1)
            label=(f'{name} {shown:g}%' if height<10 else f'{name}\n{shown:g}%')
            ax.text(0,bottom+height/2,label,color=theme.get('label_colors',{}).get(name,theme['label_color']),ha='center',va='center',fontsize=theme['font_size'],fontweight='bold')
            bottom+=height
        ax.set_yticks(context['ticks'],[f'{int(t)}%' for t in context['ticks']]);ax.set_xticks([])
        ax.text(0,103,context['total_label'],ha='center',va='center',fontweight='bold',fontsize=13,color=ink)
        ax.set_ylim(0,106)
        ax.axhline(0,color=ink,linewidth=0.85)
    elif kind=='horizontal_bar':
        order=context['order']; values={r['category']:r['value'] for r in data}
        if set(order)!=set(values): raise ValueError('order mismatch')
        ys=np.arange(len(order)); colors=[theme['colors']['highlight'] if name in context['highlight'] else theme['colors']['default'] for name in order]
        bars=ax.barh(ys,[values[k] for k in order],color=colors,height=theme['bar_height'])
        ax.set_yticks(ys,order);ax.invert_yaxis(); ax.set_xlim(*context['xlim'])
        ax.set_xticks(context['ticks'],[f'{int(x)}%' for x in context['ticks']]);ax.set_xlabel(context['x_label'],color=ink,labelpad=12)
        ax.xaxis.grid(True,color=theme['grid'],alpha=0.7);ax.set_axisbelow(True)
        for i,v in enumerate([values[k] for k in order]):
            ax.text(v+theme['label_offset'],i,f'≈{v:.0f}%',va='center',ha='left',fontweight='bold',fontsize=12,color=ink)
    elif kind=='range':
        pairs={r['series']:r['value'] for r in data}
        lo,hi=pairs['lower_reduction'],pairs['upper_reduction']
        if not 0<=lo<=hi<=100: raise ValueError('Range endpoints invalid')
        c=theme['colors'];ax.set_xlim(*context['xlim']);ax.set_ylim(-0.6,0.6)
        ax.hlines(0,lo,hi,lw=theme['line_width'],color=c['range'],zorder=2)
        ax.scatter([lo,hi],[0,0],s=theme['marker_size']**2,c=[c['start'],c['end']],zorder=3,edgecolors='white',linewidth=1.4)
        for val,label in zip((lo,hi),context['range_labels']):ax.text(val,0.24,label,ha='center',fontsize=16,color=ink,fontweight='bold')
        ax.set_xticks(context['ticks'],[f'{int(x)}%' for x in context['ticks']]);ax.set_yticks([])
        ax.xaxis.grid(True,color=theme['grid']);ax.set_axisbelow(True);ax.set_xlabel(context['x_label'],color=ink,labelpad=12)
    else:raise ValueError(f'Unsupported chart_type={kind}')
    fig.text(theme['title_x'],theme['title_y'],context['title'],ha='left',va='top',fontsize=theme['title_size'],fontweight='bold',color=ink)
    fig.text(theme['title_x'],theme['title_y']-0.092,context['subtitle'],ha='left',va='top',fontsize=10,color=ink)
    fig.text(theme['title_x'],0.045,context['source_note'],ha='left',va='bottom',fontsize=8,color=ink,alpha=.8)
    return fig

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data',default='data.csv');ap.add_argument('--config',default='config.json');ap.add_argument('--theme',default='source',choices=['source','neutral']);ap.add_argument('--output',default='output.png')
    args=ap.parse_args()
    inp=lambda p:Path(p) if Path(p).is_absolute() else HERE/p
    conf=json.loads(inp(args.config).read_text(encoding='utf-8'))
    f=render(load_data(inp(args.data)),conf['THEME'][args.theme],conf['CONTEXT'])
    dest=Path(args.output)
    if not dest.is_absolute():dest=HERE/dest
    dest.parent.mkdir(parents=True,exist_ok=True);f.savefig(dest,dpi=200,facecolor=f.get_facecolor());plt.close(f)
    print(dest)
if __name__=='__main__': main()
