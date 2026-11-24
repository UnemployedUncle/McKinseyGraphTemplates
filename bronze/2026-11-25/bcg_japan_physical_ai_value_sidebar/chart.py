import argparse, csv, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def render(data, theme, context):
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': theme['font_size']})
    fig = plt.figure(figsize=context['figsize'], facecolor='white')
    fig.text(*context['layout']['title_xy'],context['title'],fontsize=theme['title_size'],weight='bold',va='top',color=theme['ink'])
    if context['kind']=='ranked_pairs':
        groups=list(dict.fromkeys(r['group'] for r in data))
        axes=fig.subplots(1,len(groups),squeeze=False)[0]
        fig.subplots_adjust(**context['layout']['subplots'])
        fig.legend(handles=[Patch(color=theme['colors'][i],label=v) for i,v in enumerate(context['series_labels'])],loc='upper left',bbox_to_anchor=context['layout']['legend_xy'],ncol=2,frameon=False)
        xmax=max(float(r[k]) for r in data for k in ('value_a','value_b'))*1.30
        for panel,(ax,group) in enumerate(zip(axes,groups)):
            rows=sorted((r for r in data if r['group']==group),key=lambda r:int(r['rank']))
            ax.set_title(group,weight='bold',pad=10)
            for y,r in enumerate(rows):
                if panel==0: ax.text(-xmax*.25,y+.1,r['rank'],ha='center',va='center',color=theme['colors'][0],fontsize=theme['title_size'],clip_on=False)
                ax.text(0,y-.35,r['category'],weight='bold',va='bottom',fontsize=theme['font_size']-1)
                for i,k in enumerate(('value_a','value_b')):
                    v=float(r[k]); pos=y+i*.22
                    ax.barh(pos,v,height=.20,color=theme['colors'][i]); ax.text(v+.45,pos,f'{v:g}%',va='center',fontsize=theme['font_size']-1)
            ax.set_xlim(0,xmax); ax.set_ylim(len(rows)-.45,-.65); ax.axis('off')
            if panel < len(groups)-1: ax.axvline(xmax*1.07,color='#dddddd',lw=.8,clip_on=False)
    elif context['kind']=='scenario_stack':
        ax=fig.add_axes(context['layout']['axes_rect']); ax.axis('off')
        rows=data; vals=[float(r['cost_savings'])+float(r['new_value']) for r in rows]
        ymax=max(vals)*1.25; ax.set_ylim(0,ymax); ax.set_xlim(-.48,len(rows)-.45)
        for i,(r,total) in enumerate(zip(rows,vals)):
            a,b=float(r['cost_savings']),float(r['new_value']); w=.65
            ax.bar(i,a,width=w,color=theme['colors'][0]); ax.bar(i,b,bottom=a,width=w,color=theme['colors'][1]);
            ax.text(i,a/2,f'{a:g}',ha='center',va='center',color='white',weight='bold',fontsize=theme['font_size']-1)
            ax.text(i if b/ymax>.04 else i+w*.34,a+b/2,f'{b:g}',ha='center',va='center',color=theme['ink'],weight='bold',fontsize=theme['font_size']-2 if b/ymax<=.04 else theme['font_size']-1,bbox=dict(fc=theme['colors'][1],ec='none',pad=.5) if b/ymax<=.04 else None)
            ax.text(i,total+ymax*.025,f'{total:g}',ha='center',va='bottom',weight='bold')
            ax.text(i+w*.34,total+ymax*.07,f"{float(r['gdp_pct']):.1f}%",ha='center',va='bottom',bbox=dict(boxstyle='round,pad=.25',fc=theme['accent'],ec='none'),weight='bold',fontsize=theme['font_size']-1)
            ax.text(i,-ymax*.05,r['category'],ha='center',va='top',weight='bold',clip_on=False)
            ax.text(i,-ymax*.12,r['description'].replace('|','\n'),ha='center',va='top',fontsize=theme['font_size']-1,clip_on=False)
        fig.text(.04,.85,context['unit'],weight='bold',color=theme['ink'])
        fig.legend(handles=[Patch(color=theme['accent'],label=context['gdp_label']),Patch(color=theme['colors'][1],label=context['series_labels'][1]),Patch(color=theme['colors'][0],label=context['series_labels'][0])],loc='upper left',bbox_to_anchor=context['layout']['legend_xy'],frameon=False,fontsize=theme['font_size']-1)
    elif context['kind']=='timeline_stack':
        ax=fig.add_axes(context['layout']['axes_rect']); rows=data; vals=[float(r['build_months'])+float(r['ramp_months']) for r in rows]; ymax=max(vals)*1.2
        ax.set_ylim(0,ymax); ax.set_xlim(-.55,len(rows)-.45); ax.axis('off'); ax.axhline(0,color='#666666',lw=.7)
        for i,(r,total) in enumerate(zip(rows,vals)):
            a,b=float(r['build_months']),float(r['ramp_months']); ax.bar(i,a,width=.48,color=theme['colors'][0]); ax.bar(i,b,bottom=a,width=.48,color=theme['colors'][1],edgecolor='white',linewidth=.5)
            ax.text(i,a/2,f'{a:g}',ha='center',va='center',color='white'); ax.text(i,a+b/2,f'{b:g}',ha='center',va='center',color=theme['ink']); ax.text(i,total+ymax*.025,f'{total:g}',ha='center',va='bottom',weight='bold')
            ax.text(i,-ymax*.035,r['category'].replace('|','\n'),ha='center',va='top',clip_on=False); ax.text(i,-ymax*.25,r['case_count'],ha='center',va='center',clip_on=False)
            if r['row_type']=='aggregate' and i>0: ax.axvline(i-.5,color='#aaaaaa',ls=':',lw=1,ymin=-.2,clip_on=False)
        ax.text(-.58,float(rows[0]['build_months'])/2,context['series_labels'][0],ha='right',va='center',fontsize=theme['font_size']-1,clip_on=False)
        ax.text(-.58,float(rows[0]['build_months'])+float(rows[0]['ramp_months'])/2,context['series_labels'][1].replace('|','\n'),ha='right',va='center',fontsize=theme['font_size']-1,clip_on=False)
        fig.text(.025,.88,context['unit'],weight='bold'); fig.text(.025,.285,context['count_label'],weight='bold',fontsize=theme['font_size']-1)
        for y in (.31,.26): fig.add_artist(plt.Line2D([.025,.975],[y,y],transform=fig.transFigure,color='#999999',lw=.7))
        aggregate=next(r for r in rows if r['row_type']=='aggregate'); keys=('payback_months','roi_3y_x','case_count')
        for i,(key,label) in enumerate(zip(keys,context['kpi_labels'])):
            x=.025+i*.33; fig.text(x,.205,label,fontsize=theme['font_size']-1,va='center'); fig.text(x+.15,.205,context['kpi_formats'][i].format(float(aggregate[key])),weight='bold',fontsize=theme['title_size'],va='center')
            if i<2: fig.add_artist(plt.Line2D([x+.31,x+.31],[.17,.24],transform=fig.transFigure,color='#777777',lw=.7))
    else: raise ValueError('unknown kind')
    fig.text(*context['layout']['note_xy'],context['note'],fontsize=theme['font_size']-2,va='bottom',color=theme['ink'],linespacing=1.35)
    return fig

def main():
    p=argparse.ArgumentParser(); root=Path(__file__).parent
    p.add_argument('--data',type=Path,default=root/'data.csv'); p.add_argument('--config',type=Path,default=root/'config.json'); p.add_argument('--theme',choices=['source','neutral'],default='source'); p.add_argument('--output',type=Path,required=True); p.add_argument('--dpi',type=int,default=200)
    a=p.parse_args(); c=json.loads(a.config.read_text()); data=list(csv.DictReader(a.data.open())); fig=render(data,c['THEME'][a.theme],c['CONTEXT']); a.output.parent.mkdir(parents=True,exist_ok=True); fig.savefig(a.output,dpi=a.dpi); plt.close(fig)
if __name__=='__main__': main()
