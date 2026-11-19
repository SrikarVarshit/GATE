# EE1030/EE2100 - Matrix Theory : Programming Assignment
# Question 1 : QR Decomposition
# Roll number: EE26BTECH11XXX

import numpy as np


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


A = np.array([[1.0, 1.0, 0.0],
              [1.0, 0.0, 1.0],
              [0.0, 1.0, 1.0]])

# Part (a)
print("Part (a)")
Q = gram_schmidt(A)
print("Q =")
print(Q)

# Part (b)
print("\nPart (b)")
R = Q.T @ A
print("R =")
print(R)

# Part (c)
print("\nPart (c)")
I = np.eye(3)
err_ortho = np.linalg.norm(Q.T @ Q - I)
print("(i)   ||Q^T Q - I|| =", err_ortho)
print("(ii)  QR = A :", np.allclose(Q @ R, A))
print("      ||QR - A|| =", np.linalg.norm(Q @ R - A))
print("(iii) R is upper triangular :", np.allclose(R, np.triu(R)))

Q_np, R_np = np.linalg.qr(A)
print("\nFrom np.linalg.qr(A):")
print("Q_np =")
print(Q_np)
print("R_np =")
print(R_np)
print("Same Q up to signs :", np.allclose(np.abs(Q), np.abs(Q_np)))
print("Same R up to signs :", np.allclose(np.abs(R), np.abs(R_np)))

# Part (d)
print("\nPart (d)")
np.random.seed(0)
B = np.random.randn(5, 3)
b = np.random.randn(5)

Q_b = gram_schmidt(B)
R_b = Q_b.T @ B
print("Shape of Q :", Q_b.shape)
print("Shape of R :", R_b.shape)

P = Q_b @ Q_b.T
p = P @ b
print("P =")
print(P)
print("p =", p)

print("(i)   Q^T Q = I :", np.allclose(Q_b.T @ Q_b, np.eye(3)))
print("      Q Q^T = I :", np.allclose(Q_b @ Q_b.T, np.eye(5)))
print("(ii)  P^2 = P   :", np.allclose(P @ P, P))
print("      P^T = P   :", np.allclose(P.T, P))
print("(iii) B^T (b - p) =", B.T @ (b - p))

# Part (e)
print("\nPart (e)")
d = np.array([1.0, 2.0, 3.0])
c = Q.T @ d
x_qr = back_substitution(R, c)
x_np = np.linalg.solve(A, d)

print("x using QR =", x_qr)
print("x using np.linalg.solve =", x_np)
print("Difference =", x_qr - x_np)

