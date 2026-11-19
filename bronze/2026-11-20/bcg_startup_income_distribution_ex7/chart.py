#!/usr/bin/env python3
"""Reusable comparison charts; CSV values and JSON settings."""
import csv, json, argparse
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
HERE=Path(__file__).resolve().parent
def render(data, theme, context):
    rows=list(data)
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10})
    bg,ink,muted=theme["background"],theme["text"],theme["muted"]
    fig=plt.figure(figsize=(11,6.2),facecolor=bg)
    fig.text(.075,.90,context["title"],color=ink,fontsize=16,fontweight="bold",va="top")
    fig.text(.075,.833,context["subtitle"],color=muted,fontsize=10,va="top")
    if context["kind"]=="grouped_income_bar":
        ax=fig.add_axes([.10,.25,.84,.50],facecolor=bg)
        places=list(dict.fromkeys(r["city"] for r in rows)); xx=np.arange(len(places)); width=.32
        for gi,group in enumerate(["low","high"]):
            selected=[next(r for r in rows if r["city"]==p and r["group_code"]==group) for p in places]
            vals=[float(r["value_pct"]) for r in selected]
            xpos=xx+(gi-.5)*width
            ax.bar(xpos,vals,width=width*.93,color=theme["accent"] if group=="low" else theme["neutral"],zorder=3)
            for x,v in zip(xpos,vals):
                ax.text(x,v+1.1,f"{v:g}%",ha="center",va="bottom",color=ink,fontweight="bold",fontsize=13)
        ax.set_xticks(xx,places,color=ink,fontsize=12);ax.tick_params(axis="x",length=0,pad=10)
        ax.set_ylim(0,max(float(r["value_pct"]) for r in rows)*1.22)
        ax.set_yticks([0,10,20,30,40],["0%","10%","20%","30%","40%"],color=muted)
        ax.grid(axis="y",color=theme["grid"],alpha=.65);ax.set_axisbelow(True)
        ax.spines[["top","right","left","bottom"]].set_visible(False)
        from matplotlib.patches import Patch
        fig.legend(handles=[Patch(facecolor=theme["accent"],label="Lower-income cohort"),Patch(facecolor=theme["neutral"],label="Top 10%")],loc="center right",bbox_to_anchor=(.93,.782),frameon=False,ncol=2,labelcolor=ink,fontsize=9)
        fig.text(.10,.155,context["note"],color=muted,fontsize=8)
    elif context["kind"]=="productivity_bar_table":
        ax=fig.add_axes([.10,.48,.84,.30],facecolor=bg)
        names=[r["economy"] for r in rows]
        values=[float(r["gdp_per_working_age_eur_thousands"]) for r in rows]
        bars=ax.bar(np.arange(len(rows)),values,color=[theme["accent"] if r["economy"]=="Belgium" else theme["neutral"] for r in rows],width=.62,zorder=3)
        for bar,value in zip(bars,values):
            ax.text(bar.get_x()+bar.get_width()/2,value+1,f"€{value:g}k",ha="center",fontsize=11,fontweight="bold",color=ink)
        ax.set_ylim(0,max(values)*1.24);ax.set_xticks(np.arange(len(rows)),names,fontsize=9,color=ink)
        ax.tick_params(axis="x",length=0,pad=6);ax.set_yticks([])
        ax.spines[["top","right","left","bottom"]].set_visible(False)
        tab=fig.add_axes([.105,.16,.83,.24]);tab.axis("off")
        table_data=[[label]+[f"{float(r[key]):,.0f}{suffix}" for r in rows] for label,key,suffix in [("Employment rate","employment_rate_pct","%"),("GDP per hour","gdp_per_hour_eur","€"),("Hours / worker","hours_per_worker","h")]]
        t=tab.table(cellText=table_data,colLabels=["Metric"]+names,loc="center",cellLoc="center",colLoc="center",colWidths=[.20]+[.16]*len(rows))
        t.auto_set_font_size(False);t.set_fontsize(8.5);t.scale(1,1.35)
        for (ri,ci),cell in t.get_celld().items():
            cell.set_edgecolor(theme["grid"]);cell.set_linewidth(.5)
            cell.set_facecolor(theme["header_bg"] if ri==0 else bg)
            cell.get_text().set_color(ink)
            if ri==0 or ci==0: cell.get_text().set_weight("bold")
        fig.text(.105,.115,context["note"],color=muted,fontsize=7.6)
    else: raise ValueError("Unsupported chart kind")
    fig.text(.075,.055,context["source_line"],fontsize=7.5,color=muted)
    return fig
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",default=str(HERE/"data.csv"))
    p.add_argument("--config",default=str(HERE/"config.json"))
    p.add_argument("--theme",choices=["source","neutral"],required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    with open(a.data,encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    cfg=json.loads(Path(a.config).read_text(encoding="utf-8"))
    fig=render(rows,cfg["THEME"][a.theme],cfg["CONTEXT"])
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=200,facecolor=fig.get_facecolor());plt.close(fig)
    print(f"rows={len(rows)} theme={a.theme} output={out} dpi=200")
if __name__=="__main__": main()
