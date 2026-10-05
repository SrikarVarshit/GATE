import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess

# Given system:
# x + ky = 1
# kx + y = -1

k = float(input("Enter the value of k: "))

# Matrix form: AX = B
A = np.array([
    [1, k],
    [k, 1]
], dtype=float)

B = np.array([
    [1],
    [-1]
], dtype=float)

# Augmented matrix
AB = np.hstack((A, B))

print("\nCoefficient matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAugmented matrix [A|B]:")
print(AB)

# Determinant and ranks
det_A = np.linalg.det(A)
rank_A = np.linalg.matrix_rank(A)
rank_AB = np.linalg.matrix_rank(AB)

print("\nDeterminant =", det_A)
print("Rank(A) =", rank_A)
print("Rank([A|B]) =", rank_AB)

# Check the nature of solution
if rank_A < rank_AB:
    nature = "NO SOLUTION"

elif rank_A == rank_AB and rank_A < 2:
    nature = "INFINITELY MANY SOLUTIONS"

else:
    nature = "UNIQUE SOLUTION"

print("\nNature of solution:", nature)

# Find solution when unique
if nature == "UNIQUE SOLUTION":

    solution = np.linalg.solve(A, B)

    x = solution[0, 0]
    y = solution[1, 0]

    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")

elif nature == "NO SOLUTION":
    print("The lines are parallel.")

else:
    print("Both equations represent the same line.")


# Plot the equations
x_values = np.linspace(-10, 10, 1000)

plt.figure(figsize=(8, 7))

if abs(k) > 1e-10:
    y1 = (1 - x_values) / k
    plt.plot(x_values, y1, label="x + ky = 1", linewidth=2)
else:
    plt.axvline(x=1, label="x + ky = 1", linewidth=2)

y2 = -1 - k * x_values

plt.plot(x_values, y2, label="kx + y = -1", linewidth=2)

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"System for k = {k}\n{nature}")
plt.grid(True, alpha=0.3)
plt.legend()

# Mark the intersection for a unique solution
if nature == "UNIQUE SOLUTION":
    plt.scatter(
        x, y,
        s=80,
        zorder=5,
        label=f"Solution ({x:.2f}, {y:.2f})"
    )
    plt.legend()

# Save and open the graph
folder = "gate_plots"
os.makedirs(folder, exist_ok=True)

filename = os.path.join(folder, f"k_{k}.png")

plt.savefig(filename, dpi=150, bbox_inches="tight")

print("\nGraph saved at:")
print(os.path.abspath(filename))

try:
    subprocess.run(["termux-open", os.path.abspath(filename)])
except FileNotFoundError:
    print("termux-open not found.")
