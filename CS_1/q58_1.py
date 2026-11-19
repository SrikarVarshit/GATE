
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

# Generate one million random numbers
N =500

# Generate random numbers U between 0 and 1
# No fixed seed, so samples change between runs
U = np.random.uniform(0, 1, N)

# Inverse CDF: generate X values between 1 and 4
X = (1 + 63 * U) ** (1/3)

print("Total random numbers generated:", N)
print("First 10 random numbers:")
print(X[:10])

# Theoretical CDF
x = np.linspace(0, 5, 1000)
F = np.where(
    x < 1, 0,
    np.where(x <= 4, (x**3 - 1) / 63, 1)
)

# Sort generated samples
X_sorted = np.sort(X)

# Empirical CDF
empirical_cdf = np.arange(1, N + 1) / N

# Plot both CDFs
plt.figure(figsize=(10, 6))

plt.plot(
    x, F,
    label="Theoretical CDF",
    linewidth=2
)

# Plot a subset of points for faster rendering
step = 100
plt.plot(
    X_sorted[::step],
    empirical_cdf[::step],
    ".",
    markersize=2,
    label="Empirical CDF (1 million samples)"
)

plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("CDF Using One Million Random Samples")
plt.xlim(0, 5)
plt.ylim(-0.05, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()

filename = "cdf_random_plot.png"
plt.savefig(filename, dpi=180)
plt.close()

print("Plot saved as:", filename)

# Open automatically in Termux
if "TERMUX_VERSION" in os.environ:
    subprocess.run(["termux-open", filename])
else:
    print("Run this script in Termux to open the image automatically.")

