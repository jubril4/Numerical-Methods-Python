"""From scratch numerical methods, checked against NumPy and SciPy."""
from .roots import bisection, newton, secant, RootResult
from .linear_systems import (forward_substitution, back_substitution, gaussian_elimination,
                             lu_decomposition, lu_solve, cholesky, inverse)
from .interpolation import lagrange, NaturalCubicSpline, least_squares_poly
from .integration import trapezoid, simpson

__all__ = [
    "bisection", "newton", "secant", "RootResult",
    "forward_substitution", "back_substitution", "gaussian_elimination",
    "lu_decomposition", "lu_solve", "cholesky", "inverse",
    "lagrange", "NaturalCubicSpline", "least_squares_poly",
    "trapezoid", "simpson",
]
