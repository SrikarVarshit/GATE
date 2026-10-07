import os
import numpy as np
import sympy as sp
import matplotlib

# Use headless backend for Termux
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ==========================================
# 1. SOLVING THE SYSTEM (Symbolic Reduction)
# ==========================================
print("=" * 50)
print("STEP 1: SOLVING THE SYSTEM OF EQUATIONS")
print("=" * 50)

# Define symbolic variables
x1, x2, x3 = sp.symbols('x1 x2 x3')
X = sp.Matrix([x1, x2, x3])

# Coefficient matrix from the problem
A = sp.Matrix([
    [1, 1, 1],
    [1, 0, 2]
])

print("\nGiven Coefficient Matrix A:")
sp.pprint(A)

# Compute Reduced Row Echelon Form (RREF)
rref_matrix, pivot_cols = A.rref()
print("\nReduced Row Echelon Form (RREF):")
sp.pprint(rref_matrix)

# Solve Ax = 0 (Null space / Kernel)
nullspace_vectors = A.nullspace()
basis_vector = nullspace_vectors[0]

print("\nNull Space Basis Vector (Direction of the line):")
sp.pprint(basis_vector)

print("\nGeneral Parametric Solution:")
print("x1 = -2 * t")
print("x2 =  1 * t")
print("x3 =  1 * t")
print("Where t (x3) is an arbitrary free parameter (representing a Line).")
print("=" * 50)

# Convert symbolic basis vector to a NumPy directional array
dir_v = np.array([float(basis_vector[0]), 
                  float(basis_vector[1]), 
                  float(basis_vector[2])])

# ==========================================
# 2. PLOTTING THE PLANES AND SOLVED LINE
# ==========================================
# Grid coordinates for planes
grid_span = np.linspace(-6, 6, 30)
X1, X2 = np.meshgrid(grid_span, grid_span)

# Initial Plane 1: x1 + x2 + x3 = 0  ->  x3 = -x1 - x2
X3_plane1 = -X1 - X2

# Initial Plane 2: x1 + 0*x2 + 2*x3 = 0  ->  x3 = -0.5 * x1
X3_plane2 = -0.5 * X1

# Solved Line: x(t) = t * dir_v
t_vals = np.linspace(-4, 4, 100)
line_x1 = dir_v[0] * t_vals
line_x2 = dir_v[1] * t_vals
line_x3 = dir_v[2] * t_vals

# Build 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Render Plane 1 and Plane 2
ax.plot_surface(X1, X2, X3_plane1, alpha=0.45, color='deepskyblue')
ax.plot_surface(X1, X2, X3_plane2, alpha=0.45, color='darkorange')

# Render the solved intersection line
ax.plot(line_x1, line_x2, line_x3, color='red', linewidth=3.5)

# Coordinate labels and plot formatting
ax.set_xlabel(r'$x_1$', fontsize=12, labelpad=10)
ax.set_ylabel(r'$x_2$', fontsize=12, labelpad=10)
ax.set_zlabel(r'$x_3$', fontsize=12, labelpad=10)
ax.set_title("Initial Planes & Solved Line Intersection", fontsize=13)
ax.set_zlim(-6, 6)

# Create custom legend entries
legend_items = [
    Line2D([0], [0], color='deepskyblue', lw=4, label=r'Plane 1: $x_1 + x_2 + x_3 = 0$'),
    Line2D([0], [0], color='darkorange', lw=4, label=r'Plane 2: $x_1 + 2x_3 = 0$'),
    Line2D([0], [0], color='red', lw=3, label=rf'Solved Line: $\vec{{x}} = t \, [{int(dir_v[0])}, {int(dir_v[1])}, {int(dir_v[2])}]^T$')
]
ax.legend(handles=legend_items, loc='upper left')

output_file = "planes_solution.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close(fig)

print(f"\nPlot successfully saved to: {output_file}")
print("Opening the plot in default Android image viewer...")
os.system(f"termux-open {output_file}")

