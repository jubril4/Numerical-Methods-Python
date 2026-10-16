"""Numerical integration: composite trapezoidal and Simpson's rules."""
import numpy as np


def trapezoid(f, a, b, n):
    """Composite trapezoidal rule with n equal subintervals. Error shrinks like h^2."""
    if n < 1:
        raise ValueError("n must be at least 1")
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1])


def simpson(f, a, b, n):
    """Composite Simpson's 1/3 rule. n must be even. Error shrinks like h^4."""
    if n < 2 or n % 2:
        raise ValueError("n must be an even number of at least 2")
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h / 3 * (y[0] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum() + y[-1])
