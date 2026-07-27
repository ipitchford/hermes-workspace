# Hyperplane slices of the marked-cubic map

This directory packages a geometric classification of the affine hyperplane slices behind the July 2026 three-dimensional Keller counterexample.

## Main result

Let

- \(V_d=\operatorname{Sym}^d(\mathbb C^2)^*\),
- \(m:V_1\times V_2\to V_3\), \((L,Q)\mapsto LQ\),
- \(\rho(L,Q)=\operatorname{Res}(L,Q)\), and
- for \(0\ne\ell\in V_3^*\),
  \[
  H_\ell=\{C\in V_3:\ell(C)=1\},\qquad
  X_\ell=\{(L,Q):\rho(L,Q)=1,\ \ell(LQ)=1\}.
  \]

Then the multiplication map \(f_\ell:X_\ell\to H_\ell\) is étale for every \(\ell\). Up to \(PGL_2\), the projective hyperplane \(\mathbb P(\ker\ell)\) meets the twisted cubic in one of three multiplicity patterns:

| contact type | geometry of \(X_\ell\) |
|---|---|
| \(1+1+1\) | \([X_\ell]=\mathbb L^3-\mathbb L\), so \(\chi_c(X_\ell)=0\) and \(X_\ell\not\cong\mathbb A^3\) |
| \(2+1\) | \(X_\ell\cong\mathbb A^3\) |
| \(3\) | \(X_\ell\cong\mathbb G_m\times\mathbb A^2\) |

Consequently,

\[
X_\ell\cong\mathbb A^3
\quad\Longleftrightarrow\quad
\mathbb P(\ker\ell)\text{ is tangent but not osculating to the twisted cubic.}
\]

The tangent case is proved geometrically as an iterated \(\mathbb A^1\)-bundle. The constant-Jacobian identity is explained invariantly by the five-dimensional coefficient–resultant map; no determinant expansion is needed in the main proof.

## Files

- `paper.md` — self-contained public manuscript.
- `paper.tex` — LaTeX source.
- `verify_all.py` — exact SymPy checks for every coordinate identity, inverse map, Jacobian, collision, coefficient–resultant determinant, and projective syzygy used in the manuscript.
- `requirements.txt` — minimal Python dependency.
- `claims.yaml` — machine-readable claim and evidence ledger.
- `CITATION.cff` — citation metadata.
- `.github/workflows/verify-jacobian-slices.yml` — reproducibility workflow.

## Reproduction

```bash
python -m pip install -r research/jacobian-hyperplane-slices/requirements.txt
python research/jacobian-hyperplane-slices/verify_all.py
```

Expected final line:

```text
ALL EXACT CHECKS PASSED
```

## Status and provenance

The explicit counterexample was publicly announced by Levent Alpöge on 19–20 July 2026 and credited to Fable. The marked-root/symmetric-product geometry was publicized immediately afterwards by Andy Jiang and others; Aaron Lou supplied a reproducible factorization–resultant derivation; Will Sawin, David Speyer, Daniel Litt, Jake Levinson, Terence Tao, Bartosz Naskręcki, and several public commenters supplied complementary geometric and computational explanations.

This package does **not** claim priority for the counterexample. Its contribution is to assemble and prove a complete hyperplane-orbit classification, separate the universal étaleness mechanism from the exceptional affine-space mechanism, and provide a single exact reproducibility artifact.

Prepared by GPT-5.6 Pro (OpenAI), with research direction and sustained geometric questioning from Ian Pitchford, 27 July 2026.
