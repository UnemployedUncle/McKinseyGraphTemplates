import argparse,csv,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Patch
from matplotlib.ticker import PercentFormatter


def render(data, theme, context):
    groups=context['groups']; series=context['series']; colors=theme['colors']
    lookup={(r['group'],r['series']):float(r['value']) for r in data}
    assert len(lookup)==len(data)==len(groups)*len(series)
    a=np.array([[lookup[g,s] for s in series] for g in groups]); assert np.isfinite(a).all() and (a>=0).all()
    fig,ax=plt.subplots(figsize=context['figsize']); fig.patch.set_facecolor('white')
    fig.subplots_adjust(**context['margins']); fig.text(.055,.945,context['title'],fontsize=18,weight='bold',color=theme['ink'],va='top')
    fig.text(.055,.88,context['subtitle'],fontsize=11,weight='medium',color=theme['ink'],va='top')
    kind=context['kind']; x=np.arange(len(groups)); ax.spines[['top','right','left']].set_visible(False)
    ax.tick_params(axis='both',length=0,labelsize=10); ax.set_axisbelow(True)
    if kind=='grouped':
        w=context['bar_width']; ax.set_ylim(0,context['ymax']); ax.set_xticks(x,groups); ax.set_yticks(np.arange(0,context['ymax']+1,20)); ax.grid(axis='y',alpha=.15)
        for j,s in enumerate(series):
            pos=x+(j-(len(series)-1)/2)*w; ax.bar(pos,a[:,j],w,color=colors[j],label=s)
            for p,v in zip(pos,a[:,j]): ax.text(p,v+2,f'{v:g}',ha='center',fontsize=10,weight='bold')
        for i,row in enumerate(a):
            for j,ref,offset in [(2,0,16),(2,1,8)]:
                y=max(row[ref],row[j])+offset; p=x[i]+(ref-1)*w; q=x[i]+(j-1)*w
                ax.plot([p,p,q,q],[y-2,y,y,y-2],color=theme['muted'],lw=.8,ls='--'); ax.text((p+q)/2,y+1,f'−{round((1-row[j]/row[ref])*100)}% vs '+context['short_series'][ref],ha='center',fontsize=8)
        ax.legend(loc='upper center',bbox_to_anchor=(.5,-.12),ncol=3,frameon=False,fontsize=9)
    elif kind=='stacked':
        assert np.all(np.abs(a.sum(axis=1)-100)<=2)
        z=a/a.sum(axis=1)[:,None]*100; bottom=np.zeros(len(groups)); ax.set_ylim(0,100); ax.set_xlim(-.5,len(groups)-.5); ax.set_xticks(x,groups); ax.set_yticks(np.arange(0,101,20)); ax.yaxis.set_major_formatter(PercentFormatter(100)); ax.grid(axis='y',alpha=.15)
        for j,s in enumerate(series):
            ax.bar(x,z[:,j],context['bar_width'],bottom=bottom,color=colors[j],edgecolor='white',linewidth=.7)
            for i,g in enumerate(groups):
                r=next(r for r in data if r['group']==g and r['series']==s)
                if r['provenance']=='reported' and a[i,j]>=context['label_min']:
                    ax.text(x[i],bottom[i]+z[i,j]/2,f'{a[i,j]:g}%',ha='center',va='center',color=theme['label_colors'][j],fontsize=11,weight='bold')
            bottom+=z[:,j]
        order=[i for col in range(context['legend_cols']) for i in range(col,len(series),context['legend_cols'])]
        fig.legend([Patch(facecolor=colors[i]) for i in order],[series[i] for i in order],loc='upper left',bbox_to_anchor=(.05,.83),ncol=context['legend_cols'],frameon=False,fontsize=9)
    elif kind=='ribbon':
        assert np.allclose(a.sum(axis=1),100) and len(groups)==2
        w=context['bar_width']; left,right=0,1; t=np.linspace(0,1,301); f=t*t*(3-2*t); xx=left+w/2+(right-left-w)*t
        low=np.c_[np.zeros(2),np.cumsum(a,axis=1)[:,:-1]]; high=np.cumsum(a,axis=1)
        for j,s in enumerate(series):
            lo=low[0,j]+(low[1,j]-low[0,j])*f; hi=high[0,j]+(high[1,j]-high[0,j])*f
            ax.fill_between(xx,lo,hi,color=colors[j],alpha=theme['ribbon_alpha'],linewidth=0)
            for i,p in enumerate([left,right]):
                ax.add_patch(Rectangle((p-w/2,low[i,j]),w,a[i,j],facecolor=colors[j],edgecolor='white',linewidth=.7)); ax.text(p,low[i,j]+a[i,j]/2,f'{a[i,j]:g}',ha='center',va='center',fontsize=12,color=theme['label_colors'][j])
            ax.text(right+w/2+.025,low[1,j]+a[1,j]/2,s,va='center',fontsize=10)
        ax.set_xlim(-.15,1.75); ax.set_ylim(0,100); ax.set_xticks([0,1],groups,fontweight='bold'); ax.set_yticks([]); ax.spines['bottom'].set_visible(False)
    else: raise ValueError(kind)
    fig.text(.055,.035,context['note'],fontsize=9,color=theme['muted'],va='bottom',wrap=True)
    return fig


def main():
    p=argparse.ArgumentParser(); base=Path(__file__).resolve().parent
    p.add_argument('--data',type=Path,default=base/'data.csv'); p.add_argument('--config',type=Path,default=base/'config.json'); p.add_argument('--theme',choices=['source','neutral'],default='source'); p.add_argument('--output',type=Path,required=True); p.add_argument('--dpi',type=int,default=200); args=p.parse_args()
    cfg=json.loads(args.config.read_text()); data=list(csv.DictReader(args.data.open())); fig=render(data,cfg['THEME'][args.theme],cfg['CONTEXT']); args.output.parent.mkdir(parents=True,exist_ok=True); fig.savefig(args.output,dpi=args.dpi); plt.close(fig)

if __name__=='__main__': main()
