# generate_ch4_figs.py
# Creates three figures for Chapter 4:
# 1) mean_median_mode.png
# 2) boxplot_quartiles.png
# 3) variance_std_demo.png
#
# Requirements: matplotlib, numpy
# Usage:
#   python3 generate_ch4_figs.py

import numpy as np
import matplotlib.pyplot as plt

# ----- Synthetic dataset (feel free to replace) -----
rng = np.random.default_rng(42)
# mixture for visible skew/mode
data = np.concatenate([rng.normal(50, 8, 350), rng.normal(70, 5, 150)])

# ---------- 1) Histogram with mean / median / mode ----------
def figure_mean_median_mode(path="mean_median_mode.png"):
    plt.figure()
    # histogram
    counts, bins, patches = plt.hist(data, bins=20, edgecolor='black')
    # compute stats
    mean = data.mean()
    median = np.median(data)
    # "mode" via histogram modal bin center
    max_bin_idx = np.argmax(counts)
    mode = 0.5 * (bins[max_bin_idx] + bins[max_bin_idx+1])
    # vertical lines (no explicit colors to keep default theme)
    plt.axvline(mean, linestyle='--', linewidth=2, label=f"Mean = {mean:.2f}")
    plt.axvline(median, linestyle='-', linewidth=2, label=f"Median = {median:.2f}")
    plt.axvline(mode, linestyle=':', linewidth=2, label=f"Mode ≈ {mode:.2f}")
    plt.title("Histogram with Mean, Median, and Mode")
    plt.xlabel("Value"); plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()

# ---------- 2) Boxplot for Quartiles & IQR ----------
def figure_boxplot_quartiles(path="boxplot_quartiles.png"):
    plt.figure()
    bp = plt.boxplot(data, vert=True, showmeans=True)
    plt.title("Boxplot: Quartiles and IQR")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()

# ---------- 3) Variance / Std visualization ----------
def figure_variance_std_demo(path="variance_std_demo.png"):
    # Using a smaller subset for visual clarity
    x = np.arange(1, 31)
    y = np.array([6,7,3,9,10,6,8,4,7,6, 6,5,9,8,7, 5,6,7,5,9, 10,8,6,7,6, 7,5,8,6,7], dtype=float)
    mean = y.mean()

    plt.figure()
    plt.scatter(x, y, s=30, label="Data")
    plt.plot([x.min()-1, x.max()+1], [mean, mean], linestyle='--', linewidth=2, label=f"Mean = {mean:.2f}")
    # vertical deviations from mean
    for xi, yi in zip(x, y):
        plt.plot([xi, xi], [mean, yi], linewidth=1)
    plt.title("Variance & Standard Deviation: Deviations from Mean")
    plt.xlabel("Index"); plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    figure_mean_median_mode("mean_median_mode.png")
    figure_boxplot_quartiles("boxplot_quartiles.png")
    figure_variance_std_demo("variance_std_demo.png")
    print("Saved: mean_median_mode.png, boxplot_quartiles.png, variance_std_demo.png")
