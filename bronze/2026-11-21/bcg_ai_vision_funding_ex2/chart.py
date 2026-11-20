#!/usr/bin/env python3
"""Reusable source/neutral chart renderer. No proprietary font or image assets."""
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
HERE = Path(__file__).resolve().parent

def render(data, theme, context):
    rows = list(data)
    fig = plt.figure(figsize=(11, 6.2), facecolor=theme["background"])
    ink = theme["text"]
    muted = theme["muted"]
    bg = theme["background"]
    fig.text(.055, .91, context["title"], size=16, weight="bold", color=ink, va="top")
    fig.text(.055, .845, context["subtitle"], size=9.5, color=muted, va="top")
    if context["kind"] == "funding_tiles":
        assert len(rows) == 6
        for row_idx, group in enumerate(context["group_order"]):
            group_rows = sorted((r for r in rows if r["group"] == group), key=lambda r: int(r["sequence"]))
            assert len(group_rows) == 3
            y = .67 - row_idx * .35
            color = theme["accent"] if row_idx == 0 else theme["alternate"]
            fig.text(.055,y + .119,context["group_titles"][row_idx],color=ink,size=11,weight="bold")
            for col_idx,r in enumerate(group_rows):
                x = .055 + col_idx*.31
                width,height=.278,.088
                fig.add_artist(Rectangle((x,y),width,height,transform=fig.transFigure,facecolor=bg,edgecolor=color,linewidth=1.2,clip_on=False))
                fill = float(r["value_pct"])/100
                fig.add_artist(Rectangle((x,y),width*fill,height,transform=fig.transFigure,facecolor=color,edgecolor="none",clip_on=False))
                label_x=x+width*fill+.038 if fill<.22 else x+width*fill/2
                label_color=ink if fill<.22 else theme["on_accent"]
                fig.text(label_x,y+height/2,f'{float(r["value_pct"]):g}%',color=label_color,weight="bold",size=15,va="center",ha="center",clip_on=False)
                fig.text(x+width/2,y-.032,r["category"],color=ink,size=8.2,va="top",ha="center")
        fig.text(.055,.105,context["note"],color=muted,size=8.3)
    elif context["kind"] == "displacement_bars":
        order=context["group_order"]
        lookup={r["group"]:r for r in rows}
        vals=[float(lookup[k]["value_pct"]) for k in order]
        ax=fig.add_axes([.21,.23,.70,.53],facecolor=bg)
        yp=list(range(len(order)))
        colors=[theme["accent"] if k in context["highlight_groups"] else theme["neutral"] for k in order]
        bars=ax.barh(yp,vals,height=.56,color=colors,zorder=3)
        for bar,v in zip(bars,vals):
            ax.text(v+1,bar.get_y()+bar.get_height()/2,f"{v:g}%",va="center",color=ink,fontsize=13,weight="bold")
        ax.set_yticks(yp,order,fontsize=11,color=ink)
        ax.set_xlim(0,max(vals)*1.23)
        ax.set_xticks([0,10,20,30,40],labels=["0%","10%","20%","30%","40%"],color=muted)
        ax.tick_params(length=0,axis="both",pad=9)
        ax.invert_yaxis()
        ax.xaxis.grid(True,color=theme["grid"],zorder=0)
        ax.spines[["top","right","left","bottom"]].set_visible(False)
        fig.text(.055,.123,context["note"],color=muted,size=8.4)
    else:
        raise ValueError("Unknown context kind")
    fig.text(.055,.05,context["source_line"],size=7.8,color=muted)
    return fig

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",default=str(HERE/"data.csv"))
    p.add_argument("--config",default=str(HERE/"config.json"))
    p.add_argument("--theme",choices=["source","neutral"],required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    with open(a.data,encoding="utf-8",newline="") as f:
        data=list(csv.DictReader(f))
    config=json.loads(Path(a.config).read_text(encoding="utf-8"))
    fig=render(data,config["THEME"][a.theme],config["CONTEXT"])
    out=Path(a.output)
    out.parent.mkdir(exist_ok=True,parents=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"theme={a.theme} rows={len(data)} output={out} dpi=200")
if __name__=="__main__": main()
