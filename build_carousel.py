"""
Builds a 3-slide LinkedIn carousel version of the gas-gap/wind/curtailment
chart: one panel per image, sized 4:5 (1080x1350) for full-width mobile
feed display, with larger fonts since each panel now stands alone.

Reuses the data loading and panel-drawing functions from build_chart.py.
Run after build_chart.py (or standalone - it loads its own data).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import build_chart as bc

SLIDE_SIZE = (9, 11.25)  # inches, 4:5 at 120 dpi -> 1080x1350 px
DPI = 120


def save_slide(fig, filename):
    fig.savefig(filename, dpi=DPI, bbox_inches="tight", pad_inches=0.4)
    print(f"Saved {filename}")


def build_slide1(data):
    fig, ax = plt.subplots(figsize=SLIDE_SIZE)
    bc.draw_panel0(ax, data, show_legend=True, show_xlabel=True)
    ax.tick_params(labelbottom=True, labelsize=bc.FS_TICK)
    fig.suptitle(
        "UK electricity generation mix, 2000-2025",
        fontsize=bc.FS_LABEL + 4,
        y=1.08,
        fontweight="bold",
    )
    save_slide(fig, "carousel_1_generation_mix.png")


def build_slide2(data):
    fig, ax = plt.subplots(figsize=SLIDE_SIZE)
    bc.draw_panel1(ax, data)
    fig.suptitle(
        "Growth in unused gas capacity since 2000",
        fontsize=bc.FS_LABEL + 4,
        y=0.98,
        fontweight="bold",
    )
    save_slide(fig, "carousel_2_gas_gap.png")


def build_slide3(data):
    fig, ax = plt.subplots(figsize=SLIDE_SIZE)
    bc.draw_panel2(ax, data, fig=fig, show_colorbar=False)
    fig.suptitle(
        "Offshore wind vs. grid constraint cost, 2017-2025",
        fontsize=bc.FS_LABEL + 4,
        y=0.98,
        fontweight="bold",
    )
    save_slide(fig, "carousel_3_wind_vs_curtailment.png")


def main():
    data = bc.load_data()
    build_slide1(data)
    build_slide2(data)
    build_slide3(data)


if __name__ == "__main__":
    main()
