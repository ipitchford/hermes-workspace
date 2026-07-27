# Hyperplane Slices of the Marked-Cubic Map

## A classification and geometric explanation of the three-dimensional Keller counterexample

**Prepared by GPT-5.6 Pro (OpenAI), with research direction from Ian Pitchford**  
**27 July 2026**

## Abstract

Let \(W\) be a two-dimensional complex vector space, put \(V_d=\operatorname{Sym}^d(W^*)\), and consider multiplication of binary forms
\[
m:V_1\times V_2\longrightarrow V_3,\qquad (L,Q)\longmapsto LQ.
\]
For a nonzero functional \(\ell\in V_3^*\), define
\[
H_\ell=\{C\in V_3:\ell(C)=1\},
\qquad
X_\ell=\{(L,Q):\operatorname{Res}(L,Q)=1,\ \ell(LQ)=1\}.
\]
We prove that the restricted multiplication map \(f_\ell:X_\ell\to H_\ell\) is étale for every \(\ell\), and classify exactly when its source is affine three-space. Let \(\Delta\subset\mathbb P(V_3)\) be the twisted cubic of cubes of linear forms. Then
\[
X_\ell\cong\mathbb A^3
\quad\Longleftrightarrow\quad
\mathbb P(\ker\ell)\text{ is tangent but not osculating to }\Delta.
\]
The tangent case is exhibited, without constructing coordinates on \(X_\ell\), as an iterated Zariski-locally-trivial \(\mathbb A^1\)-bundle
\[
X_\ell\longrightarrow X_\ell^*\longrightarrow\mathbb A^1.
\]
The two other \(PGL_2\)-orbits are excluded by their Grothendieck classes: for contact types \(1+1+1\), \(2+1\), and \(3\), respectively,
\[
[X_\ell]=\mathbb L^3-\mathbb L,\qquad \mathbb L^3,\qquad \mathbb L^3-\mathbb L^2.
\]
In the osculating case one has the stronger identification \(X_\ell\cong\mathbb G_m\times\mathbb A^2\). We also give the universal tangent-space proof of étaleness, identify every fiber with the simple roots of the target cubic, describe the discriminant as the nonproperness locus, and reconcile the geometric construction with the announced explicit polynomial map. An exact symbolic verifier accompanies the manuscript.

## 1. Status, scope, and provenance

A concrete polynomial self-map of \(\mathbb C^3\) with nonzero constant Jacobian and a three-point fiber was publicly announced by Levent Alpöge on 19 July 2026 and credited to Fable. During the following days several complementary explanations appeared. Andy Jiang publicized the symmetric-product marked-root construction; Aaron Lou gave a reproducible linear-times-quadratic factorization and resultant derivation; Will Sawin, David Speyer, Daniel Litt, and Jake Levinson developed an iterated-affine-line-bundle explanation; Terence Tao gave an extended elementary digestion; and Bartosz Naskręcki assembled an independent exact audit and structural analysis.

This note does not claim priority for the counterexample or for the ingredients just listed. Its purpose is narrower and organizational: to place all affine hyperplanes avoiding the origin into one \(PGL_2\)-equivariant family, prove a complete three-orbit classification, and isolate the separate mechanisms responsible for local invertibility, global noninjectivity, and the exceptional isomorphism \(X_\ell\cong\mathbb A^3\).

All varieties are over \(\mathbb C\). The coordinate-free arguments extend more widely, but the characteristic-two and characteristic-three variants require separate treatment and are not claimed here.

## 2. The normalized factorization family

Let
\[
V_1=\operatorname{Sym}^1(W^*),\qquad
V_2=\operatorname{Sym}^2(W^*),\qquad
V_3=\operatorname{Sym}^3(W^*).
\]
The multiplication map
\[
m:V_1\times V_2\to V_3,\qquad (L,Q)\mapsto LQ
\]
has a one-dimensional relative scaling symmetry
\[
(L,Q)\longmapsto(\lambda L,\lambda^{-1}Q).
\]
The resultant \(\rho(L,Q)=\operatorname{Res}(L,Q)\) is bihomogeneous of bidegree \((2,1)\):
\[
\rho(\alpha L,\beta Q)=\alpha^2\beta\,\rho(L,Q).
\]
Consequently the relative scaling changes the resultant by
\[
\rho(\lambda L,\lambda^{-1}Q)=\lambda\rho(L,Q).
\]
The equation \(\rho=1\) therefore fixes the scaling uniquely whenever \(L\) and \(Q\) are coprime.

For \(0\ne\ell\in V_3^*\), define the affine hyperplane
\[
H_\ell=\{C\in V_3:\ell(C)=1\}\cong\mathbb A^3
\]
and its normalized factorization space
\[
X_\ell=\{(L,Q)\in V_1\times V_2:\rho(L,Q)=1,\ \ell(LQ)=1\}.
\]
We study
\[
f_\ell:X_\ell\to H_\ell,\qquad (L,Q)\mapsto LQ.
\]

## 3. Universal étaleness

The constant-Jacobian phenomenon does not depend on the special hyperplane. It follows from a five-dimensional statement.

### Proposition 3.1

The map
\[
\Phi:V_1\times V_2\longrightarrow V_3\times\mathbb A^1,
\qquad
\Phi(L,Q)=(LQ,\rho(L,Q))
\]
is étale on the open set \(\rho\ne0\).

### Proof

Fix a coprime pair \((L,Q)\). A tangent vector \((\dot L,\dot Q)\) lies in the kernel of the differential of multiplication exactly when
\[
\dot L\,Q+L\,\dot Q=0.
\]
Since \(L\) and \(Q\) are coprime, \(L\mid\dot L\). Both \(L\) and \(\dot L\) have degree one, so \(\dot L=tL\) for some scalar \(t\); substitution gives \(\dot Q=-tQ\). Hence
\[
\ker(dm)_{(L,Q)}=\mathbb C\,(L,-Q),
\]
the infinitesimal relative-scaling direction.

By bidegree \((2,1)\),
\[
d\rho_{(L,Q)}(L,-Q)=(2-1)\rho(L,Q)=\rho(L,Q)\ne0.
\]
Thus the resultant detects exactly the one tangent direction forgotten by multiplication. The differential of \(\Phi\) is injective, and both source and target have dimension five, so it is an isomorphism. ∎

### Corollary 3.2

For every nonzero \(\ell\), the map \(f_\ell:X_\ell\to H_\ell\) is étale.

### Proof

There is a Cartesian square
\[
\begin{array}{ccc}
X_\ell&\longrightarrow&V_1\times V_2\\
\downarrow f_\ell&&\downarrow\Phi\\
H_\ell\times\{1\}&\longrightarrow&V_3\times\mathbb A^1.
\end{array}
\]
Étaleness is preserved by base change. ∎

This is the invariant explanation of the constant Jacobian. The special choice of hyperplane is needed only to make \(X_\ell\) itself affine three-space.

## 4. Two intrinsic models of \(X_\ell\)

### 4.1 Projective complement

Let
\[
\overline X=\mathbb P(V_1)\times\mathbb P(V_2)\cong\mathbb P^1\times\mathbb P^2.
\]
Let \(\mathcal R\) be the resultant divisor and let
\[
\mathcal S_\ell=\{([L],[Q]):\ell(LQ)=0\}.
\]
Then
\[
[\mathcal R]=(2,1),\qquad [\mathcal S_\ell]=(1,1)
\]
in \(\operatorname{Pic}(\overline X)\cong\mathbb Z^2\).

### Lemma 4.1

There is a canonical isomorphism
\[
X_\ell\cong\overline X\setminus(\mathcal R\cup\mathcal S_\ell).
\]

### Proof

Forget the scalar representatives of \((L,Q)\). Conversely, take a projective pair outside the two divisors and choose representatives. Put
\[
r=\rho(L,Q),\qquad h=\ell(LQ).
\]
Both are nonzero. The unique rescaling with resultant and hyperplane value equal to one is
\[
L'=\frac{h}{r}L,\qquad Q'=\frac{r}{h^2}Q.
\]
Indeed, \(\rho(L',Q')=1\) and \(\ell(L'Q')=1\). The formulas are regular on the complement. ∎

### 4.2 Cubics with a marked simple root

A nonzero linear form determines its zero \(p\in\mathbb P^1\). Since \(\rho(L,Q)\ne0\), that point is not a root of \(Q\).

### Lemma 4.2

There is a natural isomorphism
\[
X_\ell\cong
\{(C,p):C\in H_\ell,\ C(p)=0,\ p\text{ is a simple root of }C\}.
\]
Under this isomorphism, \(f_\ell\) forgets the marked root.

### Proof

A normalized pair supplies \((C,p)=(LQ,Z(L))\). Conversely, if \(p\) is a simple root of \(C\), choose any factorization \(C=L_0Q_0\) with \(Z(L_0)=p\). Relative rescaling changes the resultant by one power of the scaling parameter, so there is a unique rescaling for which the resultant is one. ∎

It follows immediately that
\[
\#f_\ell^{-1}(C)=
\begin{cases}
3,&C\text{ has three distinct roots},\\
1,&C\text{ has one double and one simple root},\\
0,&C\text{ has a triple root}.
\end{cases}
\]

## 5. The three hyperplane orbits

Let
\[
\Delta=\{[M^3]:[M]\in\mathbb P(V_1)\}\subset\mathbb P(V_3)
\]
be the twisted cubic, also called the small diagonal in \(\operatorname{Sym}^3(\mathbb P^1)\). The projective hyperplane at infinity associated with \(\ell\) is
\[
H_\ell^\infty=\mathbb P(\ker\ell).
\]
Its intersection with \(\Delta\) is a divisor of degree three on \(\mathbb P^1\). Up to \(PGL_2\), exactly three multiplicity patterns occur:
\[
1+1+1,\qquad 2+1,\qquad 3.
\]
They mean, respectively, transverse, tangent but nonosculating, and osculating contact with the twisted cubic.

Rescaling \(\ell\) does not change the isomorphism class of the slice. If \(\ell'=\lambda\ell\), then
\[
(L,Q)\longmapsto(\lambda L,\lambda^{-2}Q)
\]
identifies \(X_\ell\) with \(X_{\ell'}\). The \(SL_2\)-equivariance of multiplication and the invariance of the resultant then show that \(X_\ell\) depends only on the contact type.

## 6. Tangent but nonosculating: an iterated \(\mathbb A^1\)-bundle

Assume
\[
H_\ell^\infty\cap\Delta=2\infty+0.
\]
Choose the affine coordinate on \(\mathbb P^1\setminus\{\infty\}\) for which this is the normal form. The hyperplane condition on a finite unordered triple is
\[
p+q+r=0.
\]
Write \(\operatorname{Sym}^2(\mathbb P^1)\cong\mathbb P^2\), and for fixed \(p\in\mathbb P^1\) define two lines:
\[
R_p=\{\{q,r\}:p\in\{q,r\}\},
\qquad
S_p=\{\{q,r\}:p+q+r=0\}.
\]
The first is the fiber of the ramification divisor; it is tangent to the discriminant conic \(\{\{q,q\}\}\) at \(\{p,p\}\). The second is the fiber of \(\mathcal S_\ell\).

For finite \(p\), the two lines meet at
\[
s(p)=\{p,-2p\}.
\]
At \(p=\infty\), the two lines coincide with the line at infinity and \(s(\infty)=\{\infty,\infty\}\). The map
\[
s:\mathbb P^1\to\operatorname{Sym}^2(\mathbb P^1),\qquad p\mapsto\{p,-2p\}
\]
is a smooth conic; denote its image by \(C_s\).

Define
\[
X_\ell^*=\{(p,\Lambda):s(p)\in\Lambda,\ \Lambda\ne R_p,S_p\},
\]
where \(\Lambda\) is a line in \(\operatorname{Sym}^2(\mathbb P^1)\).

### Lemma 6.1

The map
\[
\pi:X_\ell\to X_\ell^*,\qquad
(p,D)\mapsto(p,\overline{s(p)D})
\]
is a Zariski-locally-trivial \(\mathbb A^1\)-bundle.

### Proof

The point \(s(p)\) lies in the deleted locus \(R_p\cup S_p\), so \(D\ne s(p)\) and the joining line is defined. For fixed \((p,\Lambda)\), the point \(D\) may be any point of \(\Lambda\setminus\{s(p)\}\cong\mathbb A^1\). Globally this is the complement of a section in the corresponding \(\mathbb P^1\)-bundle. ∎

Every line through \(s(p)\) meets the conic \(C_s\) in a residual point \(s(q)\), allowing equality \(q=p\) for a tangent line. This defines
\[
\rho:X_\ell^*\to C_s\setminus\{s(\infty)\}\cong\mathbb A^1,
\qquad (p,\Lambda)\mapsto q.
\]
The exclusions have a simple meaning:

- \(S_p\) is the line through \(s(p)\) and \(s(\infty)\), so \(\Lambda\ne S_p\) is exactly \(q\ne\infty\).
- \(R_p\) meets \(C_s\) at \(s(p)\) and \(s(-p/2)\), so \(\Lambda\ne R_p\) is exactly \(p\ne-2q\).

Consequently
\[
X_\ell^*\cong\{(p,q)\in\mathbb P^1\times\mathbb A^1:p\ne-2q\}.
\]

### Lemma 6.2

The map \(\rho:X_\ell^*\to\mathbb A^1\) is a Zariski-locally-trivial \(\mathbb A^1\)-bundle, and \(X_\ell^*\cong\mathbb A^2\).

### Proof

For fixed \(q\), the fiber is \(\mathbb P^1\setminus\{-2q\}\cong\mathbb A^1\). It is the complement of the graph of the section \(q\mapsto-2q\) in the trivial \(\mathbb P^1\)-bundle over \(\mathbb A^1\). Hence it is an \(\mathbb A^1\)-bundle. Every \(\mathbb A^1\)-bundle over affine space is trivial: its linear part lies in \(\operatorname{Pic}(\mathbb A^1)=0\), and its translational torsor lies in \(H^1(\mathbb A^1,\mathcal O)=0\). Thus \(X_\ell^*\cong\mathbb A^2\). ∎

Applying the same argument to \(\pi:X_\ell\to X_\ell^*\cong\mathbb A^2\) yields the central result.

### Theorem 6.3

If \(H_\ell^\infty\) is tangent but not osculating to \(\Delta\), then
\[
X_\ell\cong\mathbb A^3.
\]

### A vector-bundle form of the same geometry

Write the linear factor as \([a:b]\) and the quadratic coefficients as \([c:d:e]\). The two boundary lines in the fiber \(\mathbb P^2\) are
\[
bc+ad=0,
\qquad
b^2c-abd+a^2e=0.
\]
Their moving intersection has closure
\[
\sigma([a:b])=[a^2:-ab:-2b^2],
\]
a nondegenerate conic. Projection away from this section is governed by the exact sequence
\[
0\longrightarrow\mathcal O(-2)
\xrightarrow{(a^2,-ab,-2b^2)^T}
\mathcal O^3
\xrightarrow{\left(\begin{smallmatrix}b&a&0\\0&-2b&a\end{smallmatrix}\right)}
\mathcal O(1)^2
\longrightarrow0.
\]
Thus the quotient projective-line bundle is \(\mathbb P(\mathcal O(1)^2)\cong\mathbb P^1\times\mathbb P^1\). The two boundary divisors descend to a constant section and a degree-one graph. Removing them gives the second \(\mathbb A^1\)-bundle above. This is the \(SL_2\)-equivariant explanation for the elementary syzygy used in coordinate derivations.

## 7. The two other orbits and a complete classification

Let \(\mathbb L=[\mathbb A^1]\) in the Grothendieck ring \(K_0(\operatorname{Var}_{\mathbb C})\). Use the marked-root projection
\[
\eta:X_\ell\to\mathbb P^1,\qquad(C,p)\mapsto p.
\]
For fixed \(p\), the conditions \(C(p)=0\) and \(\ell(C)=1\) usually form an affine plane. The cubics for which \(p\) is a multiple root form an affine line inside it. Hence the usual fiber is
\[
\mathbb A^2\setminus\mathbb A^1\cong\mathbb A^1\times\mathbb G_m,
\qquad [\text{fiber}]=\mathbb L^2-\mathbb L.
\]

The exceptional behavior is controlled by the tangent developable of the dual twisted cubic. Let \(e_p(C)=C(p)\), and let \(K_p\subset V_3\) be the subspace of cubics vanishing to order at least two at \(p\). Then
\[
K_p^\perp=\operatorname{span}(e_p,de_p)
\]
is the tangent line to the dual twisted cubic at \([e_p]\).

- If \([\ell]\) lies on no tangent line, every fiber is the usual \(\mathbb A^2\setminus\mathbb A^1\).
- If \([\ell]\) lies on a tangent line but not on the dual twisted cubic, there is one exceptional fiber \(\mathbb A^2\): the multiple-root affine line is absent.
- If \([\ell]=[e_p]\), the affine-plane equations are inconsistent at that \(p\), so the exceptional fiber is empty.

These are exactly the contact types \(1+1+1\), \(2+1\), and \(3\). Stratifying the base gives
\[
[X_\ell]=
\begin{cases}
(\mathbb L+1)(\mathbb L^2-\mathbb L)=\mathbb L^3-\mathbb L,&1+1+1,\\[2mm]
\mathbb L(\mathbb L^2-\mathbb L)+\mathbb L^2=\mathbb L^3,&2+1,\\[2mm]
\mathbb L(\mathbb L^2-\mathbb L)=\mathbb L^3-\mathbb L^2,&3.
\end{cases}
\]
Applying compactly supported Euler characteristic, which sends \(\mathbb L\) to one, gives
\[
\chi_c(X_\ell)=0,1,0
\]
in the three cases. Since \(\chi_c(\mathbb A^3)=1\), the transverse and osculating cases cannot be affine three-space.

The osculating case can be identified explicitly. Choose the normal form in which \(\ell(C)\) is the leading coefficient. If
\[
L=aT+bS,\qquad Q=cT^2+dTS+eS^2,
\]
then \(\ell(LQ)=ac=1\), so \(a\in\mathbb G_m\), \(c=a^{-1}\), and the resultant equation solves uniquely for \(e\). The free coordinates are \((a,b,d)\), giving
\[
X_\ell\cong\mathbb G_m\times\mathbb A^2.
\]

We have proved the promised classification.

### Theorem 7.1 — Hyperplane-slice classification

For every nonzero \(\ell\in V_3^*\),
\[
X_\ell\cong\mathbb A^3
\quad\Longleftrightarrow\quad
H_\ell^\infty\text{ is tangent but not osculating to }\Delta.
\]
Equivalently, the successful projective hyperplanes form the tangent developable of the dual twisted cubic with the twisted cubic itself removed.

## 8. Geometry of the étale map

By Lemma 4.2, the fiber of \(f_\ell\) over a cubic is its set of simple roots. Therefore:

1. The generic degree is three.
2. The image is the complement in \(H_\ell\) of the triple-root locus.
3. Over the discriminant complement, \(f_\ell\) is a finite étale three-sheeted covering in both the algebraic and usual complex topologies.
4. At a generic discriminant point, the cubic has one double and one simple root; the simple-root sheet remains, while the two markings of the coalescing roots escape to infinity under resultant normalization.
5. At a triple-root cubic, no marking is simple and the fiber is empty.

Thus there is no finite branch locus: the map is étale everywhere on its source. The failure is nonproperness. Its asymptotic or nonproperness set is exactly the discriminant hypersurface in \(H_\ell\).

For a target cubic \(C(t)\) and a chosen simple root \(\zeta\), the normalized factorization is especially transparent:
\[
L(t)=\frac{t-\zeta}{C'(\zeta)},
\qquad
Q(t)=C'(\zeta)\frac{C(t)}{t-\zeta}.
\]
Hence the leading coefficient of the normalized linear factor is \(1/C'(\zeta)\). When \(\zeta\) approaches a repeated root, \(C'(\zeta)\to0\), and the corresponding source point escapes to infinity.

## 9. Explicit affine coordinates and the announced map

Take the tangent normal form
\[
X=\{(a,b,c,d,e)\in\mathbb A^5:
 a^2e-abd+cb^2=1,\ ad+bc=1\}.
\]
The geometric theorem already gives \(X\cong\mathbb A^3\). A constructive polynomial isomorphism is
\[
\begin{aligned}
b&=1+ay,\\
c&=1-\frac32ay+a^2z,\\
d&=\frac12y-az+\frac32ay^2-a^2yz,\\
e&=-2z+4y^2-4ayz+3ay^3-2a^2y^2z.
\end{aligned}
\]
A polynomial inverse is
\[
y=2bd-ae,
\]
\[
z=2d^2+ce+6bd^2+3bce-\frac92e.
\]
Equivalently, after defining \(y=2bd-ae\), one may use the structurally simpler identity
\[
z=2yd+cy^2-\frac12e.
\]

Multiplication gives
\[
(aT+bS)(cT^2+dTS+eS^2)
=acT^3+(ad+bc)T^2S+(ae+bd)TS^2+beS^3.
\]
Dropping the fixed coefficient \(ad+bc=1\) yields
\[
G(a,y,z)=(ac,ae+bd,be),
\]
that is,
\[
\begin{aligned}
G_1={}&a-\frac32a^2y+a^3z,\\
G_2={}&\frac12y-3az+6ay^2-6a^2yz+\frac92a^2y^3-3a^3y^2z,\\
G_3={}&-2z+4y^2-6ayz+7ay^3-6a^2y^2z+3a^2y^4-2a^3y^3z.
\end{aligned}
\]
The exact verifier confirms
\[
\det DG=-1.
\]

Let
\[
A(x,y,z)=\left(x,y,-\frac z2\right),
\qquad
B(u_1,u_2,u_3)=(u_3,2u_2,2u_1).
\]
Then the publicly announced map
\[
\begin{aligned}
F_1={}&(1+xy)^3z+y^2(1+xy)(4+3xy),\\
F_2={}&y+3x(1+xy)^2z+3xy^2(4+3xy),\\
F_3={}&2x-3x^2y-x^3z
\end{aligned}
\]
satisfies
\[
F=B\circ G\circ A.
\]
Therefore
\[
\det DF=(-4)(-1)\left(-\frac12\right)=-2.
\]
The three-point collision is
\[
F(0,0,-1/4)=F(1,-3/2,13/2)=F(-1,3/2,13/2)=(-1/4,0,0).
\]

## 10. The five-dimensional determinant identity

In coordinates
\[
L=xT+\beta S,\qquad Q=\gamma T^2+\delta TS+\varepsilon S^2,
\]
put
\[
\begin{aligned}
c_3&=x\gamma,\\
c_2&=x\delta+\beta\gamma,\\
c_1&=x\varepsilon+\beta\delta,\\
c_0&=\beta\varepsilon,\\
\rho&=x^2\varepsilon-x\beta\delta+\beta^2\gamma.
\end{aligned}
\]
Direct expansion gives
\[
\det\frac{\partial(c_3,c_2,c_1,c_0,\rho)}
{\partial(x,\beta,\gamma,\delta,\varepsilon)}=-\rho^2.
\]
This coordinate identity is the determinant shadow of Proposition 3.1. Restricting to \(c_2=\rho=1\) and eliminating \(\delta,\varepsilon\) divides by the triangular constraint-block determinant \(x^3\); the affine chart contributes the compensating factor \(x^3\). The expanded constant Jacobian is therefore bookkeeping for two transverse normalizations, not a chance cancellation.

## 11. Why the cubic case is exceptional

There is a degree-\(n\) marked-root map
\[
\pi_n:\mathbb P^1\times\mathbb P^{n-1}\to\mathbb P^n.
\]
Let \(R_n\) be its ramification divisor and let \(S_n\) be the pullback of an irreducible target hyperplane. Their classes are
\[
[R_n]=(n-1,1),\qquad [S_n]=(1,1)
\]
in \(\operatorname{Pic}(\mathbb P^1\times\mathbb P^{n-1})\cong\mathbb Z^2\). For the complement
\[
U_n=(\mathbb P^1\times\mathbb P^{n-1})\setminus(R_n\cup S_n),
\]
the divisor localization sequence gives
\[
\operatorname{Cl}(U_n)\cong
\mathbb Z^2/\langle(n-1,1),(1,1)\rangle
\cong\mathbb Z/(n-2)\mathbb Z.
\]
Thus this natural compactified source cannot be affine \(n\)-space for \(n\ge4\). The determinant of the two boundary classes is one only at \(n=3\). This class-group calculation gives a clean invariant form of the low-degree exceptionalism.

## 12. Conclusion

The construction separates into three independent facts:

- **Universal local geometry:** multiplication plus the resultant is étale wherever the factors are coprime.
- **Universal global multiplicity:** forgetting a marked simple root is generically three-to-one.
- **Exceptional affine geometry:** only a tangent nonosculating hyperplane turns the normalized source into affine three-space.

The last fact is no longer an unexplained polynomial coincidence. Tangency forces two moving boundary lines in each projective plane to meet on an auxiliary conic; projection from that conic section produces two successive affine-line bundles. The other two hyperplane orbits retain detectable topological or unit-group obstructions. In this sense the counterexample is the unique successful member, up to symmetry and scale, of the most natural affine-hyperplane family associated with linear-times-quadratic factorization of a binary cubic.

## Appendix A. Reproducibility contract

The accompanying script `verify_all.py` performs exact rational-arithmetic checks of:

1. the forward polynomial parametrization of \(X\);
2. both compositions of the forward and inverse maps;
3. the expanded map \(G\) and \(\det DG=-1\);
4. left-right linear equivalence with the announced map and \(\det DF=-2\);
5. the advertised three-point collision;
6. the five-dimensional identity \(\det D(c_3,c_2,c_1,c_0,\rho)=-\rho^2\);
7. the projective conic section, syzygies, and relation \(R=bh_1+ah_2\);
8. the discriminant formula for the target cubic.

No floating-point arithmetic is used.

## References

### Primary public sources on the 2026 counterexample

Alpöge, L. (2026, July 19). *Announcement of an explicit counterexample to the Jacobian conjecture* [Social media post]. X. https://x.com/__alpoge__/status/2079028340955197566

Jiang, A. (2026, July 20). *Projective symmetric-product description of the counterexample* [Social media post]. X. https://x.com/davikrehalt/status/2079175065695035442

Levinson, J. (2026, July 22). *Claude’s counterexample to the Jacobian conjecture*. https://levjake.wordpress.com/wp-content/uploads/2026/07/jacobian-claude-counterexample-writeup.pdf

Litt, D. (2026, July 21). *Affine-line-bundle explanation of the marked-cubic source* [Social media post]. X. https://x.com/littmath/status/2079353531430289734

Lou, A. (2026, July 20). *Deriving an explicit polynomial counterexample to the Jacobian conjecture: A reproducible cubic-factor and resultant construction*. https://aaronlou.com/jacobian_counterexample_derivation.pdf

Naskręcki, B. (2026, July 21). *Exact audit and structural analysis: A three-dimensional Keller counterexample*. https://nasqret.github.io/jacobian-counterexample/book/index.html

Speyer, D. (2026, July 20–21). *The new counterexample to the Jacobian conjecture*. Secret Blogging Seminar. https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/

Tao, T. (2026, July 21). *A digestion of the Jacobian conjecture counterexample*. What’s New. https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/

### Affine-bundle lemma

Speyer, D. E. (2024). *Richardson varieties, projected Richardson varieties and positroid varieties* (Lemma 3.5). arXiv. https://arxiv.org/abs/2303.04831

## Contribution and AI disclosure

Ian Pitchford supplied the research direction and the sequence of questions that isolated the group action, projective compactification, hyperplane orbit problem, and invariant classification target. GPT-5.6 Pro synthesized the proofs, wrote the manuscript and verifier, and performed the exact symbolic audit. Public mathematical ingredients and provenance are credited above. This document is a post-announcement synthesis and classification, not a historical reconstruction of how the original example was discovered.
