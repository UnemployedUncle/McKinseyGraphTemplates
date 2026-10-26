"""Editable matplotlib recreation: change config.json and data.csv only."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent

def render(data: pd.DataFrame, theme: dict, context: dict):
    plt.rcParams.update({"font.family":theme.get("font_family","DejaVu Sans"),
        "font.size":theme.get("font_size",11),"axes.unicode_minus":False})
    fig,ax=plt.subplots(figsize=tuple(theme.get("figsize",[11,5.5])))
    fig.patch.set_facecolor(theme.get("background","white"))
    ax.set_facecolor(theme.get("background","white"))
    kind=context["chart_type"]
    label_color=theme.get("text_color","#242424")
    ordered=context.get("order") or list(dict.fromkeys(data["category"].tolist()))
    if kind=="stacked_horizontal_bar":
        series=context.get("series_order") or list(dict.fromkeys(data["series"].tolist()))
        xlabels=np.arange(len(ordered))
        offset=np.zeros(len(ordered))
        for s in series:
            vals=[]
            for cat in ordered:
                v=data.loc[(data["category"]==cat)&(data["series"]==s),"value"]
                vals.append(float(v.iloc[0]) if not v.empty else 0)
            ax.barh(xlabels,vals,left=offset,height=theme.get("bar_height",0.50),
              color=theme["series_colors"][s],edgecolor=theme.get("edgecolor","white"),linewidth=1.1,label=s)
            offset+=np.array(vals)
        totals=context.get("reported_totals",{})
        for i,cat in enumerate(ordered):
            label=totals.get(cat)
            if label is None: label=round(float(offset[i]),1)
            ax.text(float(offset[i])+theme.get("label_offset",1.0),i,str(label)+"%",va="center",
                    color=label_color,fontweight="bold",fontsize=theme.get("value_font_size",11))
        ax.set_yticks([])
        for i,cat in enumerate(ordered):
            ax.text(0,i-.32,context.get("display_labels",{}).get(cat,cat),
                    ha="left",va="center",fontsize=theme.get("category_font_size",9.8),color=label_color)
        ax.set_ylim(len(ordered)-.45,-.58)
        ax.set_xlim(0,context.get("x_max",60))
        ax.xaxis.set_visible(context.get("show_x_axis",False))
        ax.legend(loc=theme.get("legend_loc","upper left"),frameon=False,
                  bbox_to_anchor=tuple(theme.get("legend_anchor",[0,1.17])),ncol=len(series),fontsize=theme.get("legend_font_size",10))
    elif kind=="vertical_bar":
        vals=[float(data.loc[data["category"]==cat,"value"].iloc[0]) for cat in ordered]
        colors=[theme.get("highlight_color") if cat in context.get("highlight",[]) else theme.get("default_color") for cat in ordered]
        ax.bar(np.arange(len(ordered)),vals,color=colors,width=theme.get("bar_width",0.58))
        ax.set_xticks(range(len(ordered)),labels=[context.get("display_labels",{}).get(x,x) for x in ordered])
        ax.set_ylim(*context.get("y_lim",[0,max(vals)*1.25]));ax.set_ylabel(context.get("axis_label",""))
        for i,v in enumerate(vals):ax.text(i,v+theme.get("label_offset",.08),f"{v:g}×",ha="center",fontweight="bold",color=label_color)
        if theme.get("show_grid",False):ax.grid(axis="y",alpha=.15);ax.set_axisbelow(True)
    elif kind=="horizontal_bar":
        vals=[float(data.loc[data["category"]==cat,"value"].iloc[0]) for cat in ordered]
        colors=[theme.get("highlight_color") if cat in context.get("highlight",[]) else theme.get("default_color") for cat in ordered]
        ys=np.arange(len(ordered))
        ax.barh(ys,vals,color=colors,height=theme.get("bar_height",0.64))
        ax.set_yticks(ys,labels=ordered);ax.invert_yaxis()
        ax.set_xlim(*context.get("x_lim",[0,max(vals)*1.17]));ax.set_xlabel(context.get("axis_label",""))
        for i,v in enumerate(vals):ax.text(v+theme.get("label_offset",5),i,f"{v:,.1f}",va="center",color=label_color,fontweight="bold")
        if theme.get("show_grid",False):ax.grid(axis="x",alpha=.13);ax.set_axisbelow(True)
    else:raise ValueError(f"Unknown chart_type: {kind}")
    ax.spines[['top','right','left']].set_visible(False)
    if not context.get("show_bottom_spine",False):ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis="both",length=0,colors=label_color,pad=theme.get("tick_pad",7))
    fig.text(theme.get("title_x",.08),theme.get("title_y",.96),context["title"],
             ha="left",va="top",fontweight="bold",color=label_color,fontsize=theme.get("title_font_size",16))
    fig.text(theme.get("title_x",.08),theme.get("subtitle_y",.885),context.get("subtitle",""),
             ha="left",va="top",color=label_color,fontsize=theme.get("subtitle_font_size",10))
    fig.text(theme.get("title_x",.08),theme.get("footnote_y",.035),context.get("footnote",""),
             ha="left",va="bottom",fontsize=theme.get("footnote_font_size",8),color=theme.get("muted_color","#666"))
    margins=theme.get("margins",{"left":.10,"right":.91,"bottom":.19,"top":.73})
    fig.subplots_adjust(**margins)
    return fig

def main():
    p=argparse.ArgumentParser();p.add_argument("--theme",choices=["source","neutral"],default="source")
    p.add_argument("--data",default="data.csv");p.add_argument("--output",default="output.png")
    a=p.parse_args()
    data=pd.read_csv(ROOT/a.data if not Path(a.data).is_absolute() else a.data)
    c=json.loads((ROOT/'config.json').read_text(encoding='utf-8'))
    f=render(data,c['THEME'][a.theme],c['CONTEXT'])
    out=Path(a.output);out=(ROOT/out if not out.is_absolute() else out);out.parent.mkdir(parents=True,exist_ok=True)
    f.savefig(out,dpi=200,facecolor=f.get_facecolor());plt.close(f)
    print(f'Rendered {out}')
if __name__=='__main__': main()
