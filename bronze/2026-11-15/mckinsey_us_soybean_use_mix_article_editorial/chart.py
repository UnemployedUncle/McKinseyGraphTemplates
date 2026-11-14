"""Reusable chart renderer; source data and visual styles are configuration-driven."""
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def render(data, theme, context):
    fig, ax = plt.subplots(figsize=tuple(theme.get('figsize', [11, 6.2])))
    bg = theme.get('background', '#FFFFFF')
    fg = theme.get('text', '#202020')
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    ax.tick_params(colors=fg, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    kind = context['chart_type']
    if kind == 'descending_waterfall':
        rows = sorted(data, key=lambda row: int(row['order']))
        values = [float(row['value_cad']) for row in rows]
        total = sum(values)
        ax.bar(0, total, width=.66, color=theme['total'], zorder=3)
        ax.text(0, total + 12, f'${total:,.0f}', ha='center', fontsize=12, weight='bold', color=fg)
        rem = total
        for i, (row, value) in enumerate(zip(rows, values), start=1):
            rem -= value
            group_color = theme['low'] if row['segment'] == 'low' else theme['high']
            ax.bar(i, value, bottom=rem, width=.66, color=group_color, zorder=3)
            pct = float(row['share_pct'])
            ax.text(i, rem + value + 12, f'${value:,.0f}\n({pct:g}%)', ha='center', va='bottom', fontsize=10, color=fg)
            if i < len(values):
                ax.plot([i+.33, i+.67], [rem, rem], color=theme['guide'], lw=1, ls=':')
        ax.set_xlim(-.7, len(rows)+.65)
        ax.set_ylim(0, total*1.30)
        labels = [context['total_label']] + [row['label'] for row in rows]
        ax.set_xticks(range(len(labels)), labels, fontsize=9)
        ax.set_yticks([])
        ax.axhline(0, color=theme['guide'], lw=.8)
        ax.text(1.5, total*1.19, context['low_note'], ha='center', color=theme['low_text'], fontsize=12, weight='bold')
        ax.text(4, total*1.19, context['high_note'], ha='center', color=theme['high'], fontsize=12, weight='bold')
    elif kind == 'grouped_share':
        periods = list(dict.fromkeys(row['period'] for row in data))
        groups = list(dict.fromkeys(row['category'] for row in data))
        lookup = {(row['period'], row['category']): float(row['value_pct']) for row in data}
        width = .35
        for j, group in enumerate(groups):
            xx = [i + (j-(len(groups)-1)/2)*width for i in range(len(periods))]
            yy = [lookup.get((period, group), 0) for period in periods]
            ax.bar(xx, yy, width=width*.93, color=theme['series'][j], label=group)
            for x, y in zip(xx, yy):
                ax.text(x, y+1.5, f'{y:g}%', ha='center', va='bottom', fontsize=11, color=fg, weight='bold')
        ax.set_ylim(0, max(lookup.values())*1.25)
        ax.set_xticks(range(len(periods)), periods)
        ax.set_ylabel(context['y_label'], color=fg)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:g}%'))
        ax.yaxis.grid(True, color=theme['guide'], alpha=.4, zorder=0)
        ax.legend(frameon=False, ncol=len(groups), loc='upper right')
    else:
        raise ValueError(f'Unknown chart_type: {kind}')
    fig.suptitle(context['title'], x=.06, y=.98, ha='left', fontsize=17, fontweight='bold', color=fg)
    ax.set_title(context['subtitle'], loc='left', fontsize=10, color=theme['muted'], pad=22)
    fig.text(.06, .018, context['footnote'], fontsize=8, color=theme['muted'])
    fig.subplots_adjust(top=.78, bottom=.19, left=.07, right=.97)
    return fig


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--data', default='data.csv')
    p.add_argument('--config', default='config.json')
    p.add_argument('--theme', choices=('source', 'neutral'), default='source')
    p.add_argument('--output', required=True)
    a = p.parse_args()
    data = list(csv.DictReader(Path(a.data).open(encoding='utf-8', newline='')))
    cfg = json.loads(Path(a.config).read_text(encoding='utf-8'))
    fig = render(data, cfg['THEME'][a.theme], cfg['CONTEXT'])
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(a.output, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == '__main__':
    main()
