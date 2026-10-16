"""Interpolation and curve fitting: Lagrange, natural cubic splines, least squares."""
import numpy as np


def lagrange(x_nodes, y_nodes, x):
    """Evaluate the Lagrange interpolating polynomial through the nodes at x."""
    x_nodes = np.asarray(x_nodes, dtype=float)
    y_nodes = np.asarray(y_nodes, dtype=float)
    x = np.asarray(x, dtype=float)
    total = np.zeros_like(x)
    for j in range(len(x_nodes)):
        basis = np.ones_like(x)
        for m in range(len(x_nodes)):
            if m != j:
                basis *= (x - x_nodes[m]) / (x_nodes[j] - x_nodes[m])
        total += y_nodes[j] * basis
    return total


class NaturalCubicSpline:
    """Piecewise cubic through every node, with zero curvature at both ends.

    Building the spline means solving a tridiagonal system for the second
    derivative M_i at each node; each interval then uses its own cubic.
    """

    def __init__(self, x_nodes, y_nodes):
        x = np.asarray(x_nodes, dtype=float)
        y = np.asarray(y_nodes, dtype=float)
        if np.any(np.diff(x) <= 0):
            raise ValueError("x nodes must be strictly increasing")
        n = len(x)
        h = np.diff(x)
        A = np.zeros((n, n))
        rhs = np.zeros(n)
        A[0, 0] = A[-1, -1] = 1.0
        for i in range(1, n - 1):
            A[i, i - 1] = h[i - 1]
            A[i, i] = 2 * (h[i - 1] + h[i])
            A[i, i + 1] = h[i]
            rhs[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
        from .linear_systems import gaussian_elimination
        self.M = gaussian_elimination(A, rhs)
        self.x, self.y, self.h = x, y, h

    def __call__(self, t):
        t = np.asarray(t, dtype=float)
        i = np.clip(np.searchsorted(self.x, t) - 1, 0, len(self.h) - 1)
        x0, x1 = self.x[i], self.x[i + 1]
        h, M0, M1 = self.h[i], self.M[i], self.M[i + 1]
        y0, y1 = self.y[i], self.y[i + 1]
        return (M0 * (x1 - t) ** 3 / (6 * h) + M1 * (t - x0) ** 3 / (6 * h)
                + (y0 / h - M0 * h / 6) * (x1 - t) + (y1 / h - M1 * h / 6) * (t - x0))


def least_squares_poly(x, y, degree):
    """Fit a polynomial by solving the normal equations (V^T V) c = V^T y.

    Returns coefficients from highest power to lowest, matching np.polyfit.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    V = np.vander(x, degree + 1)
    from .linear_systems import cholesky, forward_substitution, back_substitution
    L = cholesky(V.T @ V)
    return back_substitution(L.T, forward_substitution(L, V.T @ y))
