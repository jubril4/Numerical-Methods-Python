"""Root finding: bisection, Newton's method, and the secant method.

Each solver returns a RootResult with the root, the number of iterations,
and the history of estimates so convergence can be compared and plotted.
"""
from dataclasses import dataclass, field
from typing import Callable, List


@dataclass
class RootResult:
    root: float
    iterations: int
    history: List[float] = field(default_factory=list)


def bisection(f: Callable[[float], float], a: float, b: float,
              tol: float = 1e-10, max_iter: int = 200) -> RootResult:
    """Halve a bracketing interval [a, b] until it is smaller than tol."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    history = []
    for i in range(1, max_iter + 1):
        mid = (a + b) / 2
        fm = f(mid)
        history.append(mid)
        if fm == 0 or (b - a) / 2 < tol:
            return RootResult(mid, i, history)
        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    raise RuntimeError("bisection did not converge")


def newton(f: Callable[[float], float], df: Callable[[float], float], x0: float,
           tol: float = 1e-12, max_iter: int = 100) -> RootResult:
    """Follow the tangent line: x_next = x - f(x) / f'(x)."""
    x = x0
    history = [x]
    for i in range(1, max_iter + 1):
        d = df(x)
        if d == 0:
            raise ZeroDivisionError("derivative is zero; choose another starting point")
        x_next = x - f(x) / d
        history.append(x_next)
        if abs(x_next - x) < tol:
            return RootResult(x_next, i, history)
        x = x_next
    raise RuntimeError("Newton's method did not converge")


def secant(f: Callable[[float], float], x0: float, x1: float,
           tol: float = 1e-12, max_iter: int = 100) -> RootResult:
    """Like Newton's method, but estimates the slope from the last two points."""
    history = [x0, x1]
    for i in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        if f1 == f0:
            raise ZeroDivisionError("flat secant line; choose other starting points")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        history.append(x2)
        if abs(x2 - x1) < tol:
            return RootResult(x2, i, history)
        x0, x1 = x1, x2
    raise RuntimeError("secant method did not converge")
