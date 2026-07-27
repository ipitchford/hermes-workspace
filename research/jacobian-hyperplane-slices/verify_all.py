#!/usr/bin/env python3
"""Exact verification for the marked-cubic hyperplane-slice package.

All calculations are over QQ.  No floating-point arithmetic is used.
Run with:
    python verify_all.py
"""

from __future__ import annotations

import sys
import sympy as sp

R = sp.Rational


def check_zero(expr: sp.Expr, label: str) -> None:
    value = sp.factor(sp.expand(expr))
    if value != 0:
        raise AssertionError(f"{label} failed; residual = {value}")
    print(f"PASS  {label}")


def check_equal(lhs: sp.Expr, rhs: sp.Expr, label: str) -> None:
    check_zero(lhs - rhs, label)


def main() -> None:
    print(f"SymPy {sp.__version__}")
    print("Exact domain: QQ")

    # ------------------------------------------------------------------
    # 1. The tangent slice X and its polynomial A^3 chart.
    # ------------------------------------------------------------------
    a, b, c, d, e, y, z = sp.symbols("a b c d e y z")

    relation_res = a**2 * e - a * b * d + c * b**2 - 1
    relation_hyp = a * d + b * c - 1

    b_f = 1 + a * y
    c_f = 1 - R(3, 2) * a * y + a**2 * z
    d_f = R(1, 2) * y - a * z + R(3, 2) * a * y**2 - a**2 * y * z
    e_f = -2 * z + 4 * y**2 - 4 * a * y * z + 3 * a * y**3 - 2 * a**2 * y**2 * z

    forward = {b: b_f, c: c_f, d: d_f, e: e_f}

    check_zero(relation_res.subs(forward), "forward chart satisfies resultant=1")
    check_zero(relation_hyp.subs(forward), "forward chart satisfies fixed coefficient=1")

    y_i = 2 * b * d - a * e
    z_i = 2 * d**2 + c * e + 6 * b * d**2 + 3 * b * c * e - R(9, 2) * e
    z_structural = 2 * y_i * d + c * y_i**2 - R(1, 2) * e

    check_equal(y_i.subs(forward), y, "inverse y after forward chart")
    check_equal(z_i.subs(forward), z, "inverse z after forward chart")

    # Check that the compact and structural inverse formulas agree in O(X).
    gb = sp.groebner(
        [relation_res, relation_hyp], e, d, c, b, a, order="lex", domain=sp.QQ
    )

    def check_mod_ideal(expr: sp.Expr, label: str) -> None:
        _, remainder = gb.reduce(sp.expand(expr))
        check_zero(remainder, label)

    check_mod_ideal(z_i - z_structural, "two polynomial formulas for z agree on X")

    backward = {
        b: 1 + a * y_i,
        c: 1 - R(3, 2) * a * y_i + a**2 * z_i,
        d: R(1, 2) * y_i - a * z_i + R(3, 2) * a * y_i**2 - a**2 * y_i * z_i,
        e: -2 * z_i
        + 4 * y_i**2
        - 4 * a * y_i * z_i
        + 3 * a * y_i**3
        - 2 * a**2 * y_i**2 * z_i,
    }

    check_mod_ideal(backward[b] - b, "backward chart recovers b")
    check_mod_ideal(backward[c] - c, "backward chart recovers c")
    check_mod_ideal(backward[d] - d, "backward chart recovers d")
    check_mod_ideal(backward[e] - e, "backward chart recovers e")

    # ------------------------------------------------------------------
    # 2. Multiplication map G and its Jacobian.
    # ------------------------------------------------------------------
    G1 = sp.expand(a * c_f)
    G2 = sp.expand(a * e_f + b_f * d_f)
    G3 = sp.expand(b_f * e_f)

    expected_G1 = a - R(3, 2) * a**2 * y + a**3 * z
    expected_G2 = (
        R(1, 2) * y
        - 3 * a * z
        + 6 * a * y**2
        - 6 * a**2 * y * z
        + R(9, 2) * a**2 * y**3
        - 3 * a**3 * y**2 * z
    )
    expected_G3 = (
        -2 * z
        + 4 * y**2
        - 6 * a * y * z
        + 7 * a * y**3
        - 6 * a**2 * y**2 * z
        + 3 * a**2 * y**4
        - 2 * a**3 * y**3 * z
    )

    check_equal(G1, expected_G1, "expanded G1")
    check_equal(G2, expected_G2, "expanded G2")
    check_equal(G3, expected_G3, "expanded G3")

    jac_G = sp.factor(sp.Matrix([G1, G2, G3]).jacobian([a, y, z]).det())
    check_equal(jac_G, -1, "det(DG)=-1")

    # ------------------------------------------------------------------
    # 3. Left-right equivalence with the announced map.
    # ------------------------------------------------------------------
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    F1 = (1 + x1 * x2) ** 3 * x3 + x2**2 * (1 + x1 * x2) * (4 + 3 * x1 * x2)
    F2 = x2 + 3 * x1 * (1 + x1 * x2) ** 2 * x3 + 3 * x1 * x2**2 * (4 + 3 * x1 * x2)
    F3 = 2 * x1 - 3 * x1**2 * x2 - x1**3 * x3

    source_linear = {a: x1, y: x2, z: -R(1, 2) * x3}
    G_after_A = [sp.expand(expr.subs(source_linear)) for expr in (G1, G2, G3)]
    B_after_GA = [G_after_A[2], 2 * G_after_A[1], 2 * G_after_A[0]]

    check_equal(B_after_GA[0], F1, "announced F1 = (B o G o A)_1")
    check_equal(B_after_GA[1], F2, "announced F2 = (B o G o A)_2")
    check_equal(B_after_GA[2], F3, "announced F3 = (B o G o A)_3")

    jac_F = sp.factor(sp.Matrix([F1, F2, F3]).jacobian([x1, x2, x3]).det())
    check_equal(jac_F, -2, "det(DF)=-2")

    collision_points = [
        {x1: 0, x2: 0, x3: -R(1, 4)},
        {x1: 1, x2: -R(3, 2), x3: R(13, 2)},
        {x1: -1, x2: R(3, 2), x3: R(13, 2)},
    ]
    collision_target = (-R(1, 4), 0, 0)
    for index, point in enumerate(collision_points, start=1):
        image = tuple(sp.simplify(expr.subs(point)) for expr in (F1, F2, F3))
        if image != collision_target:
            raise AssertionError(f"collision point {index} maps to {image}, not {collision_target}")
        print(f"PASS  collision point {index}")

    # ------------------------------------------------------------------
    # 4. Five-dimensional coefficient-resultant determinant.
    # ------------------------------------------------------------------
    xx, beta, gamma, delta, eps = sp.symbols("xx beta gamma delta eps")
    cc3 = xx * gamma
    cc2 = xx * delta + beta * gamma
    cc1 = xx * eps + beta * delta
    cc0 = beta * eps
    rho = xx**2 * eps - xx * beta * delta + beta**2 * gamma

    jac_master = sp.factor(
        sp.Matrix([cc3, cc2, cc1, cc0, rho])
        .jacobian([xx, beta, gamma, delta, eps])
        .det()
    )
    check_equal(jac_master, -rho**2, "five-dimensional determinant = -rho^2")

    # The Schur-complement constraint block.
    constraint_block = sp.Matrix(
        [
            [sp.diff(cc2, delta), sp.diff(cc2, eps)],
            [sp.diff(rho, delta), sp.diff(rho, eps)],
        ]
    )
    check_equal(constraint_block.det(), xx**3, "constraint block determinant = x^3")

    # ------------------------------------------------------------------
    # 5. Projective moving-conic syzygy.
    # ------------------------------------------------------------------
    aa, bb, qc, qd, qe = sp.symbols("aa bb qc qd qe")
    hyperplane_line = bb * qc + aa * qd
    resultant_line = bb**2 * qc - aa * bb * qd + aa**2 * qe
    sigma = {qc: aa**2, qd: -aa * bb, qe: -2 * bb**2}

    h1 = hyperplane_line
    h2 = -2 * bb * qd + aa * qe

    check_zero(hyperplane_line.subs(sigma), "moving conic lies on hyperplane line")
    check_zero(resultant_line.subs(sigma), "moving conic lies on resultant line")
    check_zero(h2.subs(sigma), "second quotient coordinate vanishes on moving conic")
    check_equal(resultant_line, bb * h1 + aa * h2, "R = b h1 + a h2")

    quotient_matrix = sp.Matrix([[bb, aa, 0], [0, -2 * bb, aa]])
    conic_vector = sp.Matrix([aa**2, -aa * bb, -2 * bb**2])
    matrix_product = quotient_matrix * conic_vector
    check_zero(matrix_product[0], "exact-sequence row 1 kills conic section")
    check_zero(matrix_product[1], "exact-sequence row 2 kills conic section")

    # The 2x2 minors are (-2 b^2, a b, a^2), with no common projective zero.
    minors = [
        quotient_matrix[:, [0, 1]].det(),
        quotient_matrix[:, [0, 2]].det(),
        quotient_matrix[:, [1, 2]].det(),
    ]
    expected_minors = [-2 * bb**2, aa * bb, aa**2]
    for i, (minor, expected) in enumerate(zip(minors, expected_minors), start=1):
        check_equal(minor, expected, f"quotient matrix minor {i}")

    # ------------------------------------------------------------------
    # 6. Target cubic discriminant.
    # ------------------------------------------------------------------
    t, u3, u1, u0 = sp.symbols("t u3 u1 u0")
    cubic = u3 * t**3 + t**2 + u1 * t + u0
    disc = sp.factor(sp.discriminant(cubic, t))
    expected_disc = u1**2 - 4 * u3 * u1**3 - 4 * u0 - 27 * u3**2 * u0**2 + 18 * u3 * u1 * u0
    check_equal(disc, expected_disc, "target cubic discriminant")

    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - command-line failure path
        print(f"FAIL: {exc}", file=sys.stderr)
        raise
