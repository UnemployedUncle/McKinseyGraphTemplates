#!/usr/bin/env python3
"""Reusable editorial chart renderer; no third-party image assets."""
import argparse
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def render(data, theme, context):
    """Render a reproducible figure from row dictionaries, theme and context."""
    fig, ax = plt.subplots(figsize=tuple(theme.get("figsize", [11, 6.2])))
    fig.patch.set_facecolor(theme["background"])
    ax.set_facecolor(theme["background"])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="both", length=0, colors=theme["muted"], labelsize=10)
    ax.set_title(context["title"], fontsize=17, fontweight="bold", loc="left", color=theme["ink"], pad=25)
    ax.set_xlabel(context["x_label"], color=theme["ink"], labelpad=12)
    ax.grid(axis="y", color=theme["grid"], alpha=0.55, linewidth=0.7)
    ax.set_axisbelow(True)
    kind = context["chart_type"]
    if kind == "industry_scatter":
        ax.set_xlim(*context["x_limits"])
        ax.set_ylim(*context["y_limits"])
        ax.set_ylabel(context["y_label"], color=theme["ink"])
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.yaxis.set_major_locator(MultipleLocator(5))
        ax.plot([0, context["y_limits"][1]], [0, context["y_limits"][1]],
                color=theme["muted"], linestyle="--", linewidth=1.0, alpha=0.75)
        ax.text(2, context["y_limits"][1]-1.7, "Higher churn", color=theme["muted"], fontsize=9)
        ax.text(36, 2, "Lower churn", color=theme["muted"], fontsize=9)
        for row in data:
            x, y = float(row["previous_pct"]), float(row["recent_pct"])
            highlighted = row["sector"] in context.get("highlight", [])
            ax.scatter([x], [y], color=theme["accent"] if highlighted else theme["point"], s=64 if highlighted else 40, zorder=3)
            dx, dy = float(row["label_dx"]), float(row["label_dy"])
            ax.annotate(row["sector"], (x, y), xytext=(dx, dy), textcoords="offset points",
                        fontsize=7.4, color=theme["ink"] if highlighted else theme["muted"], va="center")
        fig.text(0.11, 0.07, context["footnote"], fontsize=8.5, color=theme["muted"])
    elif kind == "milestone_timeline":
        observed = [r for r in data if r["status"] == "observed"]
        positions = list(range(len(data)))
        vals = [float(r["cities"]) for r in data]
        obs_x = positions[:len(observed)]
        fc_x = positions[len(observed)-1:]
        ax.plot(obs_x, vals[:len(observed)], color=theme["point"], lw=3, marker="o", ms=10)
        ax.plot(fc_x, vals[len(observed)-1:], color=theme["accent"], lw=3, linestyle="--", marker="o", ms=10)
        ax.set_xlim(-0.25, len(data)-0.75)
        ax.set_ylim(0, context["y_max"])
        ax.set_xticks(positions, [r["period_label"] for r in data], fontsize=9)
        ax.set_ylabel(context["y_label"], color=theme["ink"])
        ax.yaxis.set_major_locator(MultipleLocator(10))
        for i, row in enumerate(data):
            ax.annotate(f'{float(row["cities"]):g}', (i, vals[i]), xytext=(0, 13), textcoords="offset points",
                        ha="center", fontsize=12, color=theme["accent"] if row["status"]=="forecast" else theme["ink"], fontweight="bold")
        ax.text(2.32, context["y_max"]-5, "Forecast →", color=theme["accent"], fontsize=11, fontweight="bold")
        fig.text(0.11, 0.07, context["footnote"], fontsize=8.5, color=theme["muted"])
    else:
        raise ValueError(f"Unsupported chart_type: {kind}")
    fig.subplots_adjust(left=0.12, right=0.94, bottom=0.22, top=0.81)
    return fig


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data.csv")
    p.add_argument("--config", default="config.json")
    p.add_argument("--theme", choices=("source", "neutral"), default="source")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    with open(args.data, newline="", encoding="utf-8") as f:
        data = list(csv.DictReader(f))
    fig = render(data, cfg["THEME"][args.theme], cfg["CONTEXT"])
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    main()
