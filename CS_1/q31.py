import numpy as np
import matplotlib.pyplot as plt
import os

# Differentiability conditions
a = 5
b = 3 - a

print("For differentiability:")
print("a =", a)
print("b =", b)
print("Answer =", round(b, 1))

# x values
x1 = np.linspace(-3, 1, 300, endpoint=False)
x2 = np.linspace(1, 3, 300)

# Piecewise function
y1 = a*x1 + b
y2 = x2**3 + x2**2 + 1

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x1, y1, label="ax + b")
plt.plot(x2, y2, label="x^3 + x^2 + 1")

plt.scatter(1, 3, s=50)
plt.axvline(1, linestyle="--")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("GATE 2025 Q31")
plt.grid(True)
plt.legend()

# Save graph
filename = "gate31.png"
plt.savefig(filename, dpi=150, bbox_inches="tight")
plt.close()

# Automatically open the image on Android
os.system("termux-open " + filename)
