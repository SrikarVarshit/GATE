# EE1030/EE2100 - Matrix Theory : Programming Assignment
# Question 2 : Linear Regression as a Least-Squares Problem
# Roll number: EE26BTECH11XXX

import numpy as np
import matplotlib.pyplot as plt


def gram_schmidt(A):
    m, n = A.shape
    Q = np.zeros((m, n))

    for j in range(n):
        v = A[:, j].copy()
        for i in range(j):
            proj = np.dot(Q[:, i], A[:, j])
            v = v - proj * Q[:, i]
        Q[:, j] = v / np.linalg.norm(v)

    return Q


def back_substitution(R, c):
    n = len(c)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        s = 0.0
        for j in range(i + 1, n):
            s = s + R[i, j] * x[j]
        x[i] = (c[i] - s) / R[i, i]

    return x


# Generate dataset
np.random.seed(7)
n = 40
x = np.random.uniform(0, 10, n)
y = 4 + 2.5 * x + 2 * np.random.randn(n)

# Part (a)
print("Part (a)")
plt.figure(1)
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot of y vs x")

ones_col = np.ones(n)
X = np.column_stack((ones_col, x))
print("Shape of X :", X.shape)
print("Rank of X  :", np.linalg.matrix_rank(X))

# Part (b)
print("\nPart (b)")
XTX = X.T @ X
XTy = X.T @ y
beta = np.linalg.solve(XTX, XTy)
print("(i)  beta_0 =", beta[0], "(true value = 4)")
print("     beta_1 =", beta[1], "(true value = 2.5)")

beta_lstsq = np.linalg.lstsq(X, y, rcond=None)[0]
print("(ii) np.linalg.lstsq =", beta_lstsq)
print("     Same as normal equations :", np.allclose(beta, beta_lstsq))

plt.figure(2)
plt.scatter(x, y, label="Data")
y_line = beta[0] + beta[1] * x
plt.plot(x, y_line, color="red", label="Fitted line")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Least-squares line fit")
plt.legend()

plt.savefig("fit.png", dpi=200, bbox_inches="tight")

# Part (c)
print("\nPart (c)")
y_hat = X @ beta
r = y - y_hat

print("(i)   X^T r =", X.T @ r)
print("      X^T r = 0 :", np.allclose(X.T @ r, 0))
print("      Sum of residuals =", np.sum(r))

P = X @ np.linalg.inv(X.T @ X) @ X.T
print("(ii)  P y = y_hat :", np.allclose(P @ y, y_hat))
print("      P^2 = P     :", np.allclose(P @ P, P))
print("      trace(P)    :", np.trace(P))

y_sq = np.linalg.norm(y) ** 2
yhat_sq = np.linalg.norm(y_hat) ** 2
r_sq = np.linalg.norm(r) ** 2
print("(iii) ||y||^2 =", y_sq)
print("      ||y_hat||^2 =", yhat_sq)
print("      ||r||^2 =", r_sq)
print("      ||y_hat||^2 + ||r||^2 =", yhat_sq + r_sq)
print("      Equal :", np.isclose(y_sq, yhat_sq + r_sq))

# Part (d)
print("\nPart (d)")
Q = gram_schmidt(X)
R = Q.T @ X
print("R =")
print(R)

beta_qr = back_substitution(R, Q.T @ y)
print("beta from QR =", beta_qr)
print("beta from part (b) =", beta)
print("Same beta :", np.allclose(beta_qr, beta))

plt.show()

