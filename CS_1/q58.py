
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

# PDF constant
C = 1 / 21

# Generate x values
x = np.linspace(0, 5, 500)

# Calculate the CDF
F = np.zeros_like(x)

for i in range(len(x)):
    if x[i] < 1:
        F[i] = 0
    elif x[i] <= 4:
        F[i] = C * (x[i]**3 - 1) / 3
    else:
        F[i] = 1

# Plot the CDF
plt.plot(x, F, label="CDF F(x)")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Cumulative Distribution Function")
plt.grid(True)
plt.legend()

# Save the graph
filename = os.path.expanduser("~/cdf.png")
plt.savefig(filename, dpi=150, bbox_inches="tight")
plt.close()

print("CDF graph saved to:", filename)

# Automatically open the image in Termux
subprocess.run(["termux-open", filename])

