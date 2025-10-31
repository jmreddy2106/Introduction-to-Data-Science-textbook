# generate_ch2_figs.py
# Creates three textbook-style diagrams for Chapter 2:
# 1) data_science_components.png
# 2) learning_algorithms.png
# 3) data_science_ecosystem.png

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import matplotlib.lines as mlines

# ---------- Shared style ----------
BG = "#ffffff"
TITLE = "#21364a"
TEXT = "#1f2d3d"
SUBTEXT = "#3e556e"
EDGE = "#2f4b6e"
COLORS = ["#d9e7f7", "#c6dbf2", "#b4cfed", "#a1c3e8", "#8fb7e3", "#7daadb"]

def rounded_box(ax, xy, width, height, face, label, sublabel=None, lw=1.5):
    box = FancyBboxPatch(
        xy, width, height,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=lw, facecolor=face, edgecolor=EDGE
    )
    ax.add_patch(box)
    x, y = xy
    ax.text(x + width/2, y + height*0.62, label,
            ha="center", va="center", fontsize=13, weight="bold", color=TEXT)
    if sublabel:
        ax.text(x + width/2, y + height*0.28, sublabel,
                ha="center", va="center", fontsize=10.5, color=SUBTEXT)

def add_title(ax, text):
    ax.text(0.5, 0.96, text, ha="center", va="center",
            fontsize=14, weight="bold", color=TITLE)

# =====================================================================
# Figure 2.1 — Data Science Components (vertical stacked)
# =====================================================================
def fig_components(path="data_science_components.png"):
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_axis_off()
    add_title(ax, "Data Science Components")

    # Positions (x,y), (w,h)
    x, w, h = 0.18, 0.64, 0.14
    ys = [0.75, 0.56, 0.37, 0.18]
    labels = [
        ("Statistics", "Inference, uncertainty, estimation"),
        ("Machine Learning", "Pattern learning, prediction"),
        ("Computing", "Data systems, algorithms, scalability"),
        ("Data Science", "Integrates stats + ML + computing")
    ]

    # Draw boxes
    for i, (yy, (lab, sub)) in enumerate(zip(ys, labels)):
        rounded_box(ax, (x, yy), w, h, COLORS[i], lab, sub)

    # Plain connectors (no arrows)
    for i in range(len(ys)-1):
        y1 = ys[i] - 0.02
        y2 = ys[i+1] + h + 0.02
        ax.plot([0.5, 0.5], [y1, y2], color=EDGE, linewidth=1.5)

    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor=BG)
    plt.close(fig)

# =====================================================================
# Figure 2.2 — Types of Learning Algorithms (vertical)
# =====================================================================
def fig_learning_algorithms(path="learning_algorithms.png"):
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_axis_off()
    add_title(ax, "Types of Learning Algorithms")

    x, w, h = 0.18, 0.64, 0.18
    ys = [0.68, 0.42, 0.16]
    items = [
        ("Supervised Learning", "Labeled data → predict outputs\nExamples: spam detection, diagnosis"),
        ("Unsupervised Learning", "Unlabeled data → discover structure\nExamples: clustering, anomaly detection"),
        ("Reinforcement Learning", "Trial & reward → optimal policy\nExamples: game AI, robotics")
    ]

    for i, (yy, (lab, sub)) in enumerate(zip(ys, items)):
        rounded_box(ax, (x, yy), w, h, COLORS[i], lab, sub)

    # Plain connectors between boxes
    ax.plot([0.5, 0.5], [ys[0]-0.02, ys[1]+h+0.02], color=EDGE, linewidth=1.5)
    ax.plot([0.5, 0.5], [ys[1]-0.02, ys[2]+h+0.02], color=EDGE, linewidth=1.5)

    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor=BG)
    plt.close(fig)

# =====================================================================
# Figure 2.3 — Data Science Ecosystem (circular)
# =====================================================================
def fig_ecosystem(path="data_science_ecosystem.png"):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_axis_off()
    add_title(ax, "Data Science Ecosystem")

    # Center
    center = (0.5, 0.47)
    c_r = 0.12
    c = Circle(center, c_r, facecolor=COLORS[3], edgecolor=EDGE, linewidth=1.8)
    ax.add_patch(c)
    ax.text(center[0], center[1], "Data\nScience", ha="center", va="center",
            fontsize=13, weight="bold", color=TEXT)

    # Outer nodes (plain lines, no arrows)
    nodes = [
        ("Artificial Intelligence", (0.5, 0.82)),
        ("Data Mining", (0.18, 0.62)),
        ("Big Data Analytics", (0.18, 0.32)),
        ("Cloud Computing", (0.82, 0.62)),
        ("Data Visualization", (0.82, 0.32)),
    ]
    r_w, r_h = 0.28, 0.12

    for i, (lab, (nx, ny)) in enumerate(nodes):
        rounded_box(ax, (nx - r_w/2, ny - r_h/2), r_w, r_h,
                    COLORS[i % len(COLORS)], lab)
        # connector line to center edge point
        ax.plot([center[0], nx], [center[1], ny], color=EDGE, linewidth=1.4)

    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor=BG)
    plt.close(fig)

# ---- Run all ----
if __name__ == "__main__":
    fig_components("data_science_components.png")
    fig_learning_algorithms("learning_algorithms.png")
    fig_ecosystem("data_science_ecosystem.png")
    print("Saved: data_science_components.png, learning_algorithms.png, data_science_ecosystem.png")
