"""Run every method on course problems, print the results, and save the plots in docs/images."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import numerical_methods as nm

OUT = Path(__file__).parent / "docs" / "images"
OUT.mkdir(parents=True, exist_ok=True)

f = lambda x: x**3 + 12 * x**2 - 100 * x - 6
df = lambda x: 3 * x**2 + 24 * x - 100

# 1. Root finding: compare convergence on the final exam polynomial
print("Root finding, f(x) = x^3 + 12x^2 - 100x - 6, root near x = 5.71")
runs = {
    "Bisection [0, 10]": nm.bisection(f, 0, 10),
    "Newton (x0 = 8)": nm.newton(f, df, 8),
    "Secant (x0 = 5, x1 = 6)": nm.secant(f, 5, 6),
}
true_root = runs["Newton (x0 = 8)"].root
for name, r in runs.items():
    print(f"  {name:<26} root = {r.root:.10f}   iterations = {r.iterations}")

fig, ax = plt.subplots(figsize=(7, 4))
for name, r in runs.items():
    err = np.abs(np.array(r.history) - true_root)
    err = np.where(err == 0, 1e-16, err)
    ax.semilogy(range(len(err)), err, marker="o", ms=3, label=name)
ax.set(xlabel="Iteration", ylabel="Error |x - root|", title="Convergence of root finding methods")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "root_convergence.png", dpi=150)

# 2. Linear systems: midterm problem with a zero first pivot
A = np.array([[0, 2, 5, -1], [2, 1, 3, 0], [-2, -1, 3, 1], [3, 3, -1, 2]], dtype=float)
b = np.array([-3, 3, -2, 5], dtype=float)
x = nm.gaussian_elimination(A, b)
print("\nLinear system (midterm 1), solved by Gaussian elimination with partial pivoting")
print("  x =", np.round(x, 6), "  max residual =", f"{np.max(np.abs(A @ x - b)):.1e}")

# 3. Interpolation: Lagrange vs natural cubic spline on Runge's function
runge = lambda t: 1 / (1 + 25 * t**2)
nodes = np.linspace(-1, 1, 11)
t = np.linspace(-1, 1, 400)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(t, runge(t), "k", lw=2, label="True function 1/(1 + 25x^2)")
ax.plot(t, nm.lagrange(nodes, runge(nodes), t), "--", label="Lagrange polynomial (degree 10)")
ax.plot(t, nm.NaturalCubicSpline(nodes, runge(nodes))(t), label="Natural cubic spline")
ax.plot(nodes, runge(nodes), "o", color="black", ms=4, label="11 equally spaced nodes")
ax.set(ylim=(-0.5, 2.0), xlabel="x", ylabel="y", title="High degree polynomials oscillate; splines do not")
ax.grid(alpha=0.3)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(OUT / "runge_interpolation.png", dpi=150)
lag_err = np.max(np.abs(nm.lagrange(nodes, runge(nodes), t) - runge(t)))
spl_err = np.max(np.abs(nm.NaturalCubicSpline(nodes, runge(nodes))(t) - runge(t)))
print(f"\nInterpolation of Runge's function, max error: Lagrange {lag_err:.3f}, spline {spl_err:.3f}")

# 4. Integration: error vs number of subintervals
print("\nIntegral of sin(x) from 0 to pi (exact value 2)")
ns = [2, 4, 8, 16, 32, 64, 128]
trap = [abs(nm.trapezoid(np.sin, 0, np.pi, n) - 2) for n in ns]
simp = [abs(nm.simpson(np.sin, 0, np.pi, n) - 2) for n in ns]
for n, et, es in zip(ns, trap, simp):
    print(f"  n = {n:>3}   trapezoid error = {et:.2e}   Simpson error = {es:.2e}")
fig, ax = plt.subplots(figsize=(7, 4))
ax.loglog(ns, trap, "o-", label="Trapezoidal rule (error ~ h^2)")
ax.loglog(ns, simp, "s-", label="Simpson's rule (error ~ h^4)")
ax.set(xlabel="Number of subintervals n", ylabel="Absolute error", title="Integration error as the grid is refined")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "integration_error.png", dpi=150)

print(f"\nPlots saved to {OUT}")
