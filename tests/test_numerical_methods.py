"""Every method is checked against NumPy or SciPy, or against an exact answer."""
import numpy as np
import pytest
from scipy import integrate, interpolate, optimize

import numerical_methods as nm

# Final exam problem: f(x) = x^3 + 12x^2 - 100x - 6
f = lambda x: x**3 + 12 * x**2 - 100 * x - 6
df = lambda x: 3 * x**2 + 24 * x - 100

# Midterm 1 problem: a 4x4 system whose first pivot is zero
A_MID = np.array([[0, 2, 5, -1], [2, 1, 3, 0], [-2, -1, 3, 1], [3, 3, -1, 2]], dtype=float)
B_MID = np.array([-3, 3, -2, 5], dtype=float)


# Root finding
@pytest.mark.parametrize("x0", [-8.0, 8.0])
def test_newton_matches_scipy(x0):
    assert nm.newton(f, df, x0).root == pytest.approx(optimize.newton(f, x0, fprime=df))


def test_bisection_and_secant_agree_with_brentq():
    exact = optimize.brentq(f, 0, 10)
    assert nm.bisection(f, 0, 10).root == pytest.approx(exact, abs=1e-9)
    assert nm.secant(f, 5, 6).root == pytest.approx(exact)


def test_newton_converges_faster_than_bisection():
    assert nm.newton(f, df, 8).iterations < nm.bisection(f, 0, 10).iterations


def test_bisection_requires_a_sign_change():
    with pytest.raises(ValueError):
        nm.bisection(f, 20, 30)


# Linear systems
def test_gaussian_elimination_handles_zero_pivot():
    assert np.allclose(nm.gaussian_elimination(A_MID, B_MID), np.linalg.solve(A_MID, B_MID))


def test_lu_factors_rebuild_the_matrix():
    P, L, U = nm.lu_decomposition(A_MID)
    assert np.allclose(P @ A_MID, L @ U)
    assert np.allclose(L, np.tril(L)) and np.allclose(U, np.triu(U))
    assert np.allclose(nm.lu_solve(A_MID, B_MID), np.linalg.solve(A_MID, B_MID))


def test_cholesky_matches_numpy():
    rng = np.random.default_rng(0)
    M = rng.normal(size=(5, 5))
    spd = M @ M.T + 5 * np.eye(5)
    assert np.allclose(nm.cholesky(spd), np.linalg.cholesky(spd))


def test_cholesky_rejects_non_positive_definite():
    with pytest.raises(np.linalg.LinAlgError):
        nm.cholesky(np.array([[1.0, 2.0], [2.0, 1.0]]))


def test_inverse_matches_numpy():
    assert np.allclose(nm.inverse(A_MID), np.linalg.inv(A_MID))


def test_singular_matrix_is_reported():
    with pytest.raises(np.linalg.LinAlgError):
        nm.gaussian_elimination([[1, 2], [2, 4]], [1, 2])


# Interpolation and fitting
def test_lagrange_reproduces_a_cubic_exactly():
    xs = np.array([-1.0, 0.0, 2.0, 3.0])
    t = np.linspace(-1, 3, 50)
    assert np.allclose(nm.lagrange(xs, f(xs), t), f(t))


def test_natural_spline_matches_scipy():
    xs = np.linspace(0, 2 * np.pi, 9)
    t = np.linspace(0, 2 * np.pi, 200)
    ref = interpolate.CubicSpline(xs, np.sin(xs), bc_type="natural")(t)
    assert np.allclose(nm.NaturalCubicSpline(xs, np.sin(xs))(t), ref)


def test_least_squares_matches_polyfit():
    rng = np.random.default_rng(1)
    x = np.linspace(0, 5, 40)
    y = 2 * x**2 - 3 * x + 1 + rng.normal(scale=0.5, size=x.size)
    assert np.allclose(nm.least_squares_poly(x, y, 2), np.polyfit(x, y, 2))


# Integration
def test_trapezoid_course_example():
    # Course example: integral of x^2 from 0 to 1 with 4 subintervals
    assert nm.trapezoid(lambda x: x**2, 0, 1, 4) == pytest.approx(0.34375)


def test_simpson_is_exact_for_cubics():
    exact = integrate.quad(f, 0, 3)[0]
    assert nm.simpson(f, 0, 3, 2) == pytest.approx(exact)


def test_simpson_error_shrinks_faster_than_trapezoid():
    exact = 2.0  # integral of sin(x) from 0 to pi
    trap_err = abs(nm.trapezoid(np.sin, 0, np.pi, 16) - exact)
    simp_err = abs(nm.simpson(np.sin, 0, np.pi, 16) - exact)
    assert simp_err < trap_err / 100
