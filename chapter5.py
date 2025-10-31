import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=50, scale=10, size=100)
sorted_data = np.sort(data)
p = (np.arange(1, len(data)+1) - 0.5) / len(data)

plt.figure(figsize=(6, 4))
plt.plot(p, sorted_data, marker='o', linestyle='-')
plt.xlabel('Cumulative Probability (Quantiles)')
plt.ylabel('Data Values')
plt.title('Quantile Plot of Normally Distributed Data')
plt.grid(True)

plt.tight_layout()
plt.savefig("quantile_plot.png", dpi=300)  # <-- valid extension here
plt.show()


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Given sample data
data = np.array([5, 6, 7, 8, 9])

# Q–Q Plot for given data
fig = plt.figure()
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q–Q Plot: Sample Data [5,6,7,8,9]")

# Save the figure
output_path = "qq_plot_sample_data.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()
plt.close()