# Diagrams

## 1. Universal coefficient–resultant map and its slices

```mermaid
flowchart TB
  A["V₁ × V₂<br/>(linear form, quadratic form)"]
  B["V₃ × A¹<br/>(product cubic, resultant)"]
  X["X_ℓ = {Res=1, ℓ(LQ)=1}"]
  H["H_ℓ × {1}<br/>H_ℓ ≅ A³"]

  A -->|"Φ(L,Q)=(LQ,Res(L,Q))<br/>étale on Res≠0"| B
  X --> A
  X -->|"f_ℓ: forget the marked simple root"| H
  H --> B
```

The lower square is Cartesian. Universal étaleness of \(\Phi\) therefore implies étaleness of every hyperplane slice \(f_\ell\).

## 2. The three hyperplane orbits

```mermaid
flowchart TB
  E["Projective hyperplane P(ker ℓ)<br/>cuts the twisted cubic in degree 3"]
  T1["1+1+1<br/>transverse"]
  T2["2+1<br/>tangent, nonosculating"]
  T3["3<br/>osculating"]
  O1["[X_ℓ]=L³−L<br/>χc=0<br/>not A³"]
  O2["X_ℓ ≅ A³<br/>unique successful orbit"]
  O3["X_ℓ ≅ Gₘ×A²<br/>nonconstant unit"]

  E --> T1 --> O1
  E --> T2 --> O2
  E --> T3 --> O3
```

## 3. Tangent geometry

```mermaid
flowchart TB
  X["X_ℓ<br/>marked root p and quadratic divisor D"]
  XS["X*<br/>p and a line Λ through s(p)"]
  A1["A¹<br/>residual point q on the auxiliary conic"]

  X -->|"fiber Λ \ {s(p)} ≅ A¹"| XS
  XS -->|"fiber P¹ \ {−2q} ≅ A¹"| A1
```

The auxiliary conic is
\[
s(p)=\{p,-2p\}\subset\operatorname{Sym}^2(\mathbb P^1)\cong\mathbb P^2.
\]
Both affine-line bundles are trivial because their bases are affine spaces. Hence \(X_\ell\cong\mathbb A^3\).

## 4. Covering behavior

```mermaid
flowchart TB
  C3["cubic with 3 distinct roots"] --> F3["3 marked-simple-root preimages"]
  C2["double root + simple root"] --> F1["1 preimage<br/>two sheets escape to infinity"]
  C1["triple root"] --> F0["0 preimages<br/>omitted locus"]
```

The discriminant is the nonproperness locus. There is no ramification on the source: the map is étale everywhere.
