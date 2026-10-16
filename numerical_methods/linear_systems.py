"""Direct solvers for linear systems Ax = b, written without np.linalg.solve."""
import numpy as np


def forward_substitution(L, b):
    """Solve Ly = b where L is lower triangular."""
    L = np.asarray(L, dtype=float)
    b = np.asarray(b, dtype=float)
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - L[i, :i] @ y[:i]) / L[i, i]
    return y


def back_substitution(U, y):
    """Solve Ux = y where U is upper triangular."""
    U = np.asarray(U, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]
    return x


def gaussian_elimination(A, b):
    """Gaussian elimination with partial pivoting, then back substitution.

    Partial pivoting swaps in the row with the largest pivot, which avoids
    dividing by zero (or by tiny numbers that magnify rounding error).
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    for k in range(n - 1):
        p = k + int(np.argmax(np.abs(A[k:, k])))
        if np.isclose(A[p, k], 0.0):
            raise np.linalg.LinAlgError("matrix is singular")
        if p != k:
            A[[k, p]] = A[[p, k]]
            b[[k, p]] = b[[p, k]]
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
    if np.isclose(A[-1, -1], 0.0):
        raise np.linalg.LinAlgError("matrix is singular")
    return back_substitution(A, b)


def lu_decomposition(A):
    """Factor PA = LU with partial pivoting. Returns P, L, U."""
    A = np.array(A, dtype=float)
    n = A.shape[0]
    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()
    for k in range(n - 1):
        p = k + int(np.argmax(np.abs(U[k:, k])))
        if p != k:
            U[[k, p]] = U[[p, k]]
            P[[k, p]] = P[[p, k]]
            L[[k, p], :k] = L[[p, k], :k]
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
    np.fill_diagonal(L, 1.0)
    return P, L, U


def lu_solve(A, b):
    """Solve Ax = b using PA = LU, so Ly = Pb and then Ux = y."""
    P, L, U = lu_decomposition(A)
    y = forward_substitution(L, P @ np.asarray(b, dtype=float))
    return back_substitution(U, y)


def cholesky(A):
    """Factor a symmetric positive definite matrix as A = L L^T."""
    A = np.asarray(A, dtype=float)
    if not np.allclose(A, A.T):
        raise ValueError("matrix must be symmetric")
    n = A.shape[0]
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            s = A[i, j] - L[i, :j] @ L[j, :j]
            if i == j:
                if s <= 0:
                    raise np.linalg.LinAlgError("matrix is not positive definite")
                L[i, i] = np.sqrt(s)
            else:
                L[i, j] = s / L[j, j]
    return L


def inverse(A):
    """Invert A by solving A x = e_i for each column of the identity."""
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    return np.column_stack([lu_solve(A, np.eye(n)[:, i]) for i in range(n)])
