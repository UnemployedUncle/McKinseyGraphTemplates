"""Reusable chart rendering from CSV and configurable themes."""
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def render(data, theme, context):
    rows = list(data)
    fig = plt.figure(figsize=theme.get('figsize', [11, 6.2]), facecolor=theme['background'])
    ink = theme['text']; muted = theme['muted']; accent = theme['accent']
    fig.text(.055, .947, context['title'], fontsize=15, color=ink, weight='bold', va='top')
    fig.text(.055, .899, context['subtitle'], fontsize=9.5, color=muted, va='top')
    kind = context['chart_kind']
    if kind == 'slope_grid':
        groups = list(dict.fromkeys(r['group'] for r in rows))
        header_y = [.82, .552, .282]
        axis_bottom = [.625, .355, .105]
        for gi, group in enumerate(groups):
            items = [r for r in rows if r['group'] == group]
            fig.text(.055, header_y[gi], group, fontsize=10, weight='bold', color=ink)
            for j, r in enumerate(items):
                ax = fig.add_axes([.055+j*.181, axis_bottom[gi], .155, .12 if gi==2 else .145])
                a, b = float(r['q1_pct']), float(r['q3_pct'])
                color = accent if gi < 2 else theme['secondary']
                ax.plot([0, 1], [a, b], color=color, lw=2.2, zorder=2)
                ax.scatter([0, 1], [a, b], color=color, s=26, zorder=3)
                for x, v in [(0, a), (1, b)]:
                    ax.annotate(f'{v:+g}%', (x, v), xytext=(0, 6), textcoords='offset points',
                                ha='center', fontsize=8, color=ink)
                ax.set_xlim(-.18, 1.18); ax.set_ylim(-24, 15)
                ax.set_xticks([0, 1], ['Q1 2026', 'Q3 2026'], fontsize=6.5)
                ax.set_yticks([-20, 0, 10], ['-20%', '0%', '10%'], fontsize=6.5)
                ax.set_title(r['category'], fontsize=8, color=ink, weight='bold', pad=10)
                ax.axhline(0, color=theme['grid'], lw=.5)
                ax.spines[['top', 'right', 'left']].set_visible(False)
                ax.spines['bottom'].set_color(theme['grid'])
                ax.tick_params(axis='both', length=0, colors=muted)
    elif kind == 'relocation_panels':
        for j, r in enumerate(rows):
            ax = fig.add_axes([.065+j*.315, .24, .27, .49])
            before = float(r['base_mva_usd_bn'])
            loss = float(r['loss_mva_usd_bn'])
            after = before-loss
            vals = [before, after]
            ax.bar([0, 2], vals, width=.55, color=theme['accent'], zorder=3)
            ax.bar([1], [loss], bottom=[after], width=.55, color=theme['loss'], zorder=3)
            for x, y, label in [(0,before,f'{before:,.0f}'), (1,after+loss/2,f'-{loss:,.0f}'), (2,after,f'{after:,.0f}')]:
                ax.annotate(label, (x,y), xytext=(0,6 if x != 1 else 0),
                            textcoords='offset points', ha='center', va='bottom' if x != 1 else 'center',
                            fontsize=9, weight='bold', color=ink)
            pct = loss/before*100
            ax.annotate(f'-{pct:.0f}%', (1, before*1.09), ha='center', fontsize=9,
                        color=theme['loss'], weight='bold')
            ax.set_ylim(0, 3100)
            ax.set_xlim(-.55, 2.55)
            ax.set_xticks([0,1,2], ['Baseline', 'At risk', 'After move'], fontsize=7)
            ax.set_title(r['region'], fontsize=11, weight='bold', color=ink, pad=17)
            ax.set_yticks([0, 1000, 2000, 3000] if j == 0 else [])
            ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:,.0f}'))
            ax.tick_params(axis='both', labelsize=7, length=0, colors=muted)
            ax.spines[['top', 'right', 'left']].set_visible(False)
            ax.spines['bottom'].set_color(theme['grid'])
            jobs_base=int(float(r['jobs_base_m']))
            jobs_loss=int(float(r['jobs_at_risk_m']))
            fig.text(.11+j*.315, .172, f'{jobs_base}m jobs  →  -{jobs_loss}m  →  {jobs_base-jobs_loss}m',
                     fontsize=8.7, color=ink)
    elif kind == 'maturity_stack':
        ax = fig.add_axes([.075, .45, .86, .19])
        start=0
        for r in rows:
            val=float(r['share_pct']); color=theme['palette'][r['stage']]
            ax.barh([0], [val], left=[start], height=.8, color=color, edgecolor='white', lw=2)
            ax.text(start+val/2, 0, f'{val:g}%', ha='center', va='center',
                    fontsize=12 if val > 10 else 10, color='white' if r['stage'] in ('Workflow redesign','Role redesign') else ink, weight='bold')
            start+=val
        ax.set_xlim(0,100); ax.set_yticks([])
        ax.set_xticks([0,20,40,60,80,100], [f'{v}%' for v in [0,20,40,60,80,100]])
        ax.tick_params(axis='x', length=0, colors=muted)
        ax.spines[:].set_visible(False)
        for j,r in enumerate(rows):
            fig.text(.08+(j%2)*.48, .30-(j//2)*.065, f'■  {r["stage"]}: {r["share_pct"]}%',
                     fontsize=10.5, color=ink, weight='bold')
    else:
        raise ValueError(f'Unknown chart_kind: {kind}')
    fig.text(.055, .048, context['note'], fontsize=7.7, color=muted)
    fig.text(.055, .022, context['source_label'], fontsize=7, color=muted)
    return fig


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data', default='data.csv')
    parser.add_argument('--config', default='config.json')
    parser.add_argument('--theme', choices=('source','neutral'), default='source')
    parser.add_argument('--output', required=True)
    parser.add_argument('--dpi', type=int, default=200)
    args=parser.parse_args()
    with open(args.data,encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    cfg=json.loads(Path(args.config).read_text(encoding='utf-8'))
    fig=render(rows,cfg['THEME'][args.theme],cfg['CONTEXT'])
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,dpi=args.dpi,facecolor=fig.get_facecolor())
    plt.close(fig)

if __name__ == '__main__':
    main()
