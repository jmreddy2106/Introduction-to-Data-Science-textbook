import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([2,3,5,4,7])

plt.figure()
plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot (Bivariate)")
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,1.5],[2,2.2],[3,2.8]])
B = np.array([[1,2.6],[2,3.2],[3,3.8]])

plt.figure()
plt.scatter(A[:,0], A[:,1], label="Group A", marker="o")
plt.scatter(B[:,0], B[:,1], label="Group B", marker="s")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Multiple Scatter (Grouped)")
plt.legend()
plt.grid(True)
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

rng = np.random.default_rng(0)
n = 200
X = pd.DataFrame({
    "feat1": rng.normal(0,1,n),
    "feat2": rng.normal(5,2,n),
    "feat3": rng.normal(-2,0.5,n)
})

axes = scatter_matrix(X, figsize=(8,8), diagonal="hist")
plt.suptitle("Scatter Matrix")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

xy = np.array([[1,3,10],[2,4,30],[3,5,50]], dtype=float)
x, y, s = xy[:,0], xy[:,1], xy[:,2]

alpha, beta = 1000.0, 50.0
sizes = beta + alpha*(s - s.min())/(s.max() - s.min())

plt.figure()
plt.scatter(x, y, s=sizes, alpha=0.6)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bubble Chart (size encodes third variable)")
for xi, yi, si in xy:
    plt.annotate(f"s={int(si)}", (xi, yi), textcoords="offset points", xytext=(5,5))
plt.grid(True)
plt.show()