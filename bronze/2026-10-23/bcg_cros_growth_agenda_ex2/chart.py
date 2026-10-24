#!/usr/bin/env python3
"""Reusable consulting chart template. Edit data.csv and config.json, then re-render."""
import argparse,csv,json,textwrap
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

BASE = Path(__file__).resolve().parent

def render(data, theme, context):
    """Render data-driven chart; all contextual/stylistic knobs live in config.json."""
    by_category={str(r['category']):r for r in data}
    order=[c for c in context.get('order',list(by_category)) if c in by_category]
    order+= [c for c in by_category if c not in order]
    if not order: raise ValueError('No valid rows.')
    rows=[by_category[x] for x in order]
    values=[float(row['value']) for row in rows]
    if not all(0<=v<=100 for v in values): raise ValueError('Expected percentage values within 0-100')
    plt.rcParams['font.family']=theme['font']
    fig=plt.figure(figsize=tuple(theme['figsize']),facecolor=theme['background'])
    ax=fig.add_axes([theme['left'],theme['bottom'],theme['right']-theme['left'],theme['top']-theme['bottom']])
    ax.set_facecolor(theme['background'])
    pos=list(range(len(rows)))
    focus=set(context.get('highlight_categories',[]))
    kind=context.get('chart_type','horizontal_bars')
    if kind=='horizontal_bars':
        for i,(r,v) in enumerate(zip(rows,values)):
            color=theme['highlight'] if r['category'] in focus else theme['primary']
            ax.barh(i,v,height=theme.get('bar_height',0.55),color=color,edgecolor='none',zorder=3)
    elif kind=='lollipop':
        for i,(r,v) in enumerate(zip(rows,values)):
            color=theme['highlight'] if r['category'] in focus else theme['primary']
            ax.plot([0,v],[i,i],color=color,lw=theme.get('line_width',3),zorder=3,solid_capstyle='round')
            ax.plot(v,i,'o',color=color,markersize=theme.get('marker_size',13),zorder=4)
    else: raise ValueError(f'Unsupported chart type: {kind}')
    xhi=float(context['xlim'][1]); xlo=float(context['xlim'][0]); width=xhi-xlo
    for i,v in enumerate(values):
        ax.text(min(v+width*0.02,xhi+width*0.04),i,context.get('value_format','{:.0f}%').format(v),ha='left',va='center',fontsize=theme['label_size'],fontweight='bold',color=theme['text'],clip_on=False)
    ax.set_xlim(xlo,xhi)
    ax.set_yticks(pos,[str(r['category']) for r in rows],fontsize=theme['label_size']-1)
    ax.invert_yaxis()
    ax.set_ylim(len(rows)-0.45,-0.55)
    ax.set_xticks(context.get('xticks',list(range(0,101,20))))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x,_:f'{x:.0f}%'))
    ax.tick_params(axis='x',length=0,pad=8,labelsize=theme['tick_size'],colors=theme['muted'])
    ax.tick_params(axis='y',length=0,pad=12,colors=theme['text'])
    ax.grid(axis='x',color=theme['grid'],lw=0.9,zorder=0)
    for sp in ax.spines.values():sp.set_visible(False)
    ax.set_xlabel(context['xlabel'],fontsize=theme['tick_size']+1,color=theme['muted'],labelpad=13)
    # Figure-coordinate labels keep titles independent of the input data and font size.
    fig.text(theme['left'],0.945,textwrap.fill(context['title'],width=context.get('title_wrap',43),break_long_words=False),ha='left',va='top',fontsize=theme['title_size'],fontweight='bold',color=theme['text'],linespacing=1.25)
    fig.text(theme['left'],0.824,context['subtitle'],ha='left',va='top',fontsize=theme['subtitle_size'],color=theme['muted'])
    fig.text(theme['left'],0.105,context['footnote'],ha='left',va='top',fontsize=theme['source_size'],color=theme['muted'])
    fig.text(theme['left'],0.072,context['source'],ha='left',va='top',fontsize=theme['source_size'],color=theme['muted'])
    return fig

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data',default=str(BASE/'data.csv'))
    p.add_argument('--config',default=str(BASE/'config.json'))
    p.add_argument('--theme',choices=['source','neutral'],default='source')
    p.add_argument('--output',default=str(BASE/'output.png'))
    args=p.parse_args()
    config=json.loads(Path(args.config).read_text(encoding='utf-8'))
    with Path(args.data).open(newline='',encoding='utf-8-sig') as f:
        data=list(csv.DictReader(f))
    fig=render(data,config['THEME'][args.theme],config['CONTEXT'])
    path=Path(args.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(path,dpi=200,facecolor=config['THEME'][args.theme]['background'])
    plt.close(fig)
    print(json.dumps({'output':str(path),'theme':args.theme,'rows':len(data)}))
if __name__=='__main__':main()
