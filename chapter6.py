import seaborn as sns
import matplotlib.pyplot as plt

data = [2, 3, 3, 4, 5, 6, 7, 8, 8, 9]

sns.histplot(data, bins=10, kde=False, color='skyblue', edgecolor='black')
plt.title("Histogram of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

## Histogram
data = [10, 12, 14, 16, 18, 20, 22]

sns.boxplot(x=data, color='lightgreen')
plt.title("Box Plot: Quartile Visualization")
plt.xlabel("Values")
plt.show()


# Generate and save a KDE plot image for the provided data and bandwidths
import math
import numpy as np
import matplotlib.pyplot as plt

def phi(u):
    return (1/math.sqrt(2*math.pi))*math.exp(-0.5*u*u)

def kde_gaussian(x_data, x_eval, h):
    n = len(x_data)
    s = 0.0
    for xi in x_data:
        u = (x_eval - xi)/h
        s += phi(u)
    return s/(n*h)

# Provided data
data = [4,5,6,7,8]

# Create a smooth grid and compute KDE for h=1.0
xs = np.linspace(3, 9, 400)
h = 1.0
ys = np.array([kde_gaussian(data, x, h) for x in xs])

# Plot (single chart) and save
plt.figure()
plt.plot(xs, ys, label="KDE (h=1.0)")
plt.scatter(data, [0]*len(data), marker="x", label="Data points")
plt.title("Gaussian KDE for data [4,5,6,7,8] (h=1.0)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)

out_path = "kde_plot_h1.png"
plt.savefig(out_path, dpi=300, bbox_inches="tight")
plt.close()

