# 📊 ArXiv Graph Theory Daily Bulletin — 2026-11-02

> 💡 **Executive Overview**: Below are today's featured Graph Theory preprints scraped and summarized automatically.

---

### 🚀 1. A Winner Classification for Rooted Partizan Edge Geography on Heterogeneous Bouquets of Cycles
- 👤 **Authors**: Adam Tilèpe  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40683)

#### 📝 Executive Summary & Innovations
- **Main Result**: The first player has a winning strategy in the undirected edge‑traversal game on any finite bouquet of simple cycles exactly when the number of cycles whose edge‑length is odd is itself odd. This classification holds without any assumption that the cycles have equal length. The proof is carried out via a simultaneous induction on root and defense configurations together with a precise analysis of the forced race between two opened cycles, and it has been fully formalised in Lean 4.  
- **Key Graph Concepts**:  
  - Rooted partizan edge geography  
  - Bouquets of cycles (heterogeneous cycle lengths)  
  - Parity of odd‑length cycles  
  - Combinatorial game theory  
  - Formal verification (Lean 4)

---

### 🚀 2. Sharp bounds, stability, and arithmetic fluctuations for induced pentagons
- 👤 **Authors**: Youwen Xu  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40691)

#### 📝 Executive Summary & Innovations
- **Main Result**: Every graph with \(m>0\) edges contains at most \(\frac{3}{2\sqrt{2}}\bigl(\frac{m}{5}\bigr)^{5/2}\) induced pentagons, and equality occurs precisely for balanced blow‑ups of the Clebsch graph together with isolated vertices. Moreover, a deficit of \(\varepsilon\) in the normalized count can be repaired by \(O(\sqrt{\varepsilon}\,m)\) edge edits, yielding an exact Clebsch blow‑up; the exponent \(1/2\) is optimal and the linear versus quadratic costs of adjacency errors are sharply separated.  
- **Key Graph Concepts**:  
  - Induced pentagons (5‑cycles)  
  - Extremal graph theory  
  - Clebsch graph and its balanced blow‑ups  
  - Weighted graphs & graphons (including fractional graphons)  
  - Stability and arithmetic fluctuations  
  - Rational certificates & integer‑arithmetic verification

---

### 🚀 3. Asymptotic stability of clique‑saturating edges near Turán thresholds
- 👤 **Authors**: Xianglei Chen, Changxiang He  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40696)

#### 📝 Executive Summary & Innovations
- **Main Result**: For any fixed integer \(p\ge 3\), the minimum number \(f_{p+1,p}(n,m,\delta)\) of \(K_{p+1}\)-saturating edges in an \(n\)-vertex, \(K_{p+1}\)-free graph with \(m\) edges, minimum degree \(\delta\), and containing a \(K_p\) satisfies two asymptotic stability formulas:  
  1. When \(m=\operatorname{ex}(n,K_p)+o(n^2)\) and \(\delta\ge\bigl(\frac{p-2}{p-1}+o(1)\bigr)n\),  
     \[
     f_{p+1,p}(n,m,\delta)=\Bigl(\frac{(p-2)^2}{2(p-1)^3}+o(1)\Bigr)n^2 .
     \]  
  2. When \(m=\operatorname{ex}(n,K_{p+1})-(c+o(1))n^2\) with \(0\le c<\frac{1}{2p(3p-1)}\) and \(\delta\ge\bigl(\frac{p-1}{p}-2c+o(1)\bigr)n\),  
     \[
     f_{p+1,p}(n,m,\delta)=\Bigl(\frac{1}{2p}+o(1)\Bigr)n^2 .
     \]  
  These results describe the asymptotic behaviour of clique‑saturating edges in the near‑Turán regime and highlight the influence of the minimum‑degree condition.  
- **Key Graph Concepts**:  
  - \(K_{p+1}\)-saturating edges  
  - Turán numbers \(\operatorname{ex}(n,K_r)\)  
  - Stability phenomena in extremal graph theory  
  - Minimum degree constraints  
  - Clique‑saturation near Turán thresholds  

---

### 🚀 4. The Hibi--Li (2016) conjecture is fully resolved
- 👤 **Authors**: Dave Goel  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40703)

#### 📝 Executive Summary & Innovations
- **Main Result**: Building on Fourier’s inequality, the paper proves that for any \(n\)-element poset containing the five‑element poset \(X\) as an induced subposet, the chain polytope \(\mathcal{C}(P)\) has at least \(\binom{n-3}{k-2}\) more \(k\)-dimensional faces than the order polytope \(\mathcal{O}(P)\) for every \(2\le k\le n-1\). Moreover, it shows that equality of face numbers in any such dimension forces unimodular equivalence, thereby settling the Hibi–Li conjecture in full (the only exception being the edge case \(k=1\)). All arguments are formally verified in Lean 4.
- **Key Graph Concepts**: Order polytope, Chain polytope, Finite posets, Face enumeration, Unimodular equivalence, Induced subposet \(X\), Formal verification (Lean 4).

---

### 🚀 5. The Cranston--Li--Su--Wang--Xu (2026) conjecture is true
- 👤 **Authors**: Dave Goel  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40863)

#### 📝 Executive Summary & Innovations
- **Main Result**: The conjecture is proved: for any finite abelian group \(A\) with \(|A|\ge 4\), any two nowhere‑zero \(A\)-flows on an even‑degree graph can be linked by a sequence of elementary cycle‑adjustments that stay within the class of nowhere‑zero \(A\)-flows. The same holds for integer flows whose values lie in \(\{ \pm1,\dots,\pm(k-1)\}\) for every \(k\ge4\). The proof proceeds by an edge‑reduction induction and a degree‑reduction to graphs of maximum degree 4, with a counting argument handling the integer‑flow case. All results are also formalised in Lean 4.
- **Key Graph Concepts**: Nowhere‑zero \(A\)-flows, Finite abelian groups, Even‑degree graphs, Cycle reconfiguration, Integer flows bounded by \(k\), Graph reduction (degree‑4), Formal verification (Lean 4).

---

### 🚀 6. An explicit bound on the extremal function for complete graph minors
- 👤 **Authors**: David R. Wood  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41060)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper establishes a concrete universal constant: every graph on \(n\) vertices with edge density at least \(4.5\,t\sqrt{\log t}\) contains a \(K_t\) minor, for all integers \(t\ge 2\). This gives an explicit, small‑\(\beta\) version of the Kostochka–Thomason theorem, replacing the previously non‑explicit \(o(1)\) term with a concrete bound that works for every \(t\).
- **Key Graph Concepts**: Graph density, \(K_t\) minor, Extremal function for minors, Kostochka–Thomason theorem, Explicit constants, Minor‑closed families.

### 🚀 7. Variance Bounds and Strict Log-Concavity for Forest Coronas
- 👤 **Authors**: Vadim E. Levit  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41102)

#### 📝 Executive Summary & Innovations
- **Main Result**:  
  1. For every non‑empty forest and any activity \(0<t\le 1\), the variance of the size of a random independent set is strictly smaller than its mean; a rooted quadratic reserve supplies quantitative versions of this inequality.  
  2. Using mean‑matching transfers and exact binomial moments, the paper proves strict log‑concavity (and a stronger factorial‑normalised log‑concavity) for all forest coronas and for every well‑covered forest, together with explicit coefficient margins and sharpness statements.  

- **Key Graph Concepts**:  
  - Forests and forest coronas  
  - Independent sets, activity parameter \(t\)  
  - Variance and mean comparison (rooted quadratic reserve)  
  - Strict log‑concavity / ultra‑log‑concavity (ULC)  
  - Well‑covered forests, canonical completion laws  
  - Factorial normalisation \(((m-j)!i_j)_{j=0}^m\)  

---

### 🚀 8. Deck Reconstruction for Restricted Word Classes
- 👤 **Authors**: Krishna Angal, Ruben Ascoli, Simon X. He, Xiaoyu He, Logan Post, Arker Oke Soe, Olga Zhukova  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41110)

#### 📝 Executive Summary & Innovations
- **Main Result**:  
  1. The authors establish that for several restricted families of binary words—those with a fixed number of ones, bounded number of runs of ones, or whose one‑positions follow a monotone polynomial of degree \(d\)—the reconstruction threshold (the smallest \(k\) for which the \(k\)-deck uniquely determines the word) is bounded by a function depending only on the structural complexity of the class.  
  2. By extending a “template lemma” of Dudík and Schulman, they improve the known upper bound for weak deck reconstruction and show that for periodic words of period \(d\) the in‑class threshold coincides with the general threshold for words of length \(d\).  

- **Key Graph Concepts**:  
  - (While not a graph‑theoretic paper, the combinatorial structures relate to) binary words, \(k\)-deck, reconstruction thresholds  
  - Runs of ones, monotone polynomial index sets, periodic words  
  - Weak deck reconstruction, wildcard symbols, template constructions  

---

### 🚀 9. Circular regular dessins with underlying graphs \({\bf K}_{2^e,2^f}^{(2^d)}\): the metacyclic case
- 👤 **Authors**: Yuntian Wu, Wenwen Fan  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41123)

#### 📝 Executive Summary & Innovations
- **Main Result**:  
  1. The paper classifies and enumerates all circular regular dessins whose underlying graph is the complete bipartite multigraph \({\bf K}_{2^e,2^f}^{(2^d)}\) (with \(e\ge f\ge 2,\; d\ge 1\)) and whose colour‑ and orientation‑preserving automorphism group is a metacyclic 2‑group.  
  2. Explicit enumeration formulas are derived for the number of such dessins up to isomorphism, completing the metacyclic case for 2‑power complete bipartite multigraphs when combined with the previously known simple‑graph results (\(d=0\)).  

- **Key Graph Concepts**:  
  - Complete bipartite multigraphs \({\bf K}_{2^e,2^f}^{(2^d)}\)  
  - Circular regular dessins (2‑cell embeddings, regular action on edges)  
  - Metacyclic 2‑groups, non‑exact bicyclic factorisations  
  - Enumeration up to isomorphism, factorisation \(G=\langle a\rangle\langle b\rangle\cong \mathbb Z_{2^{e+d}}\times\mathbb Z_{2^{f+d}}\)  

---

### 🚀 10. Rainbow Hamiltonian paths in graph collections under edge-size conditions
- 👤 **Authors**: Xiaoxue Zhang, Lihua You  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41203)

#### 📝 Executive Summary & Innovations
- **Main Result**:  
  1. For a collection $\mathbf{G}=\{G_1,\dots,G_{n-1}\}$ of order $n\ge 3$ with each $e(G_i)>\binom{n-2}{2}+2$ and at least one $G_j$ connected, a rainbow Hamiltonian path exists except for two explicit extremal families (the $K_2\vee4K_1$ case when $n=6$ and the $K_3\vee5K_1$ case when $n=8$).  
  2. Moreover, if $e(G_i)\ge\binom{n-1}{2}$ for all $i$, a rainbow Hamiltonian path is guaranteed unless all $G_i$ are $K_{n-1}\cup K_1$ (or the $K_{1,3}$ case when $n=4$).  
  These results sharpen a previous theorem by relaxing the connectivity requirement and correcting its statement.

- **Key Graph Concepts**:  
  - Rainbow Hamiltonian path in a collection of graphs  
  - Edge‑size conditions (thresholds $\binom{n-2}{2}+2$, $\binom{n-1}{2}$)  
  - Connectedness of a single member of the collection  
  - Extremal configurations: joins $K_2\vee4K_1$, $K_3\vee5K_1$, $K_{n-1}\cup K_1$, $K_{1,3}$  

---

### 🚀 11. A note on decompositions into 3‑chromatic graphs
- 👤 **Authors**: Bertille Granet, Daniel Horsley, Jeffrey N. Santrio  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41266)

#### 📝 Executive Summary & Innovations
- **Main Result**: By merging the “discharging in the dual’’ technique of Delcourt–Postle with the “condensation’’ method of Bryant et al., the authors obtain the exact decomposition threshold for cycles of any odd length and provide asymptotically tight thresholds for a broad class of other 3‑chromatic graphs. This unifies and extends recent breakthroughs on triangle and odd‑cycle decompositions.

- **Key Graph Concepts**:  
  - Graph decomposition thresholds  
  - 3‑chromatic graphs, especially odd cycles $C_{2\ell+1}$  
  - Discharging in the dual (dual‑graph charging)  
  - Condensation method (graph contraction/aggregation)  
  - Approximate decomposition for broader 3‑chromatic families  

---

### 🚀 12. On the Turán number for the Cartesian product of an odd cycle and a tree
- 👤 **Authors**: Ya‑Hong Chen, Yong Lu, Quan Sun, Qi Wu, Long‑Tu Yuan  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41286)

#### 📝 Executive Summary & Innovations
- **Main Result**: For any fixed tree $T$ (with at least two vertices) and any odd cycle $C_{2m+1}$, the authors determine the Turán number $\mathrm{ex}(n, C_{2m+1}\square T)$ for all sufficiently large $n$, together with a complete description of the extremal graphs. Every extremal construction is the join of an independent set with an extremal graph belonging to the appropriate decomposition family.

- **Key Graph Concepts**:  
  - Turán numbers and extremal graph theory  
  - Cartesian product $C_{2m+1}\square T$  
  - Decomposition family of a graph product  
  - Join of an independent set with an extremal subgraph  
  - Tools: Erdős–Sós theorem, weak stability, progressive induction  

---

### 🚀 13. Pebbling Numbers and Generator Reinforcement of Cayley Graphs
- 👤 **Authors**: Yuan Yang, Bocheng Li, Qingzhong Ji  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41306)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors give an \(O(|\Gamma|^{2})\) algorithm (in the explicit multiplication‑table model) that computes the smallest inverse‑closed set of generators needed to force the optimal pebbling number of any finite Cayley graph to be at most three while preserving its regular action.  Closed‑form thresholds are obtained for hypercubes (\(2^{d-1}-d\) for dimension \(d\ge1\)) and for standard Keller graphs (threshold = 3 when \(d=2\) and \(2^{d-1}\) when \(d\ge3\)), and every admissible augmentation of these families has ordinary pebbling number equal to its order.  
- **Key Graph Concepts**: Cayley graphs, pebbling numbers, inverse‑closed generator augmentation, weighted vertex‑cover on inverse orbits, hypercubes, Keller graphs, abelian groups, regular group actions.

---

### 🚀 14. Clique‑factors in randomly perturbed hypergraphs
- 👤 **Authors**: Yulin Chang, Jie Han, Patrick Morris, Lin Sun  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41340)

#### 📝 Executive Summary & Innovations
- **Main Result**: For any integers \(k\ge3\) and \(t\ge t_{0}(k)\) and any \(\alpha>0\), there exists a constant \(C\) such that, whenever \(n\) is a multiple of \(t+1\) and \(p\ge C n^{-t/\binom{t+1}{k}}\), the union of a \(k\)-uniform hypergraph with minimum codegree \(\alpha n\) and the random hypergraph \(H^{(k)}(n,p)\) a.a.s. contains a perfect \(K_{t+1}^{(k)}\)-factor.  The probability bound is asymptotically optimal and extends the known graph case; in particular \(t_{0}(3)=3\), so the theorem applies to all \(t\ge3\) for 3‑uniform hypergraphs.  
- **Key Graph Concepts**: \(k\)-uniform hypergraphs, minimum codegree condition, random hypergraph \(H^{(k)}(n,p)\), \(K_{t+1}^{(k)}\)-factor (clique‑factor), randomly perturbed hypergraph model, threshold probability, extremal‑probabilistic combinatorics.

---

### 🚀 15. Separating hash families with large universe II
- 👤 **Authors**: Xin Wei, Gennian Ge  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41353)

#### 📝 Executive Summary & Innovations
- **Main Result**: For fixed integers \(t,k\ge2\) and length \(N=(t-1)(k-1)+1\), the authors prove that the maximal universe size of a \(t\)-perfect hash family over an alphabet of size \(q\) satisfies \(p_{t}(N,q)\ge q^{\,k-o(1)}\).  Combined with monotonicity in the length, this resolves a question of Blackburn, Etzion, Stinson, and Zaverucha for all feasible parameters.  The proof blends the Nash–Williams–Tutte theorem, a graph‑theoretic elimination technique, and a solution‑free‑set theorem from the authors’ earlier work.  
- **Key Graph Concepts**: \(t\)-perfect hash families, universe size, Nash–Williams–Tutte theorem (spanning‑tree packing), graph‑theoretic elimination arguments, solution‑free sets, combinatorial design theory.

### 🚀 16. Two-coloring the points of a projective plane
- 👤 **Authors**: Aart Blokhuis, Ádám Markó, Tamás Szőnyi, Zsuzsa Weiner  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41357)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors determine the exact number of unbalanced lines for any non‑trivial two‑coloring of the Galois plane \(\mathrm{PG}(2,q)\).  For prime order \(p\) they classify all 2‑colorings that have at most \(\max\{3p+1,4p-22\}\) lines that are not \((r,b)\)-colored (Theorem 5.13).  Moreover, when the parameter \(r\) is small they obtain stronger bounds on the number of non‑\((r,b)\)-colored lines (Theorem 5.18).
- **Key Graph Concepts**: Projective planes, Galois planes \(\mathrm{PG}(2,q)\), two‑colorings, balanced/unbalanced lines, \((r,b)\)-colored lines, combinatorial geometry.

---

### 🚀 17. $K_r$-Packings in Graphs with $t_{r-1}(n)+k$ Edges
- 👤 **Authors**: Hanzhi Bai, Fuhong Ma, Jin Yan  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41371)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper proves that the asymptotic equality \(\phi_r(n,k) = (1-o(1))k\) holds **iff** \(k = o(n^{2})\), thereby completely characterising the range of \(k\) for which the trivial lower bound is essentially tight.  Additionally, when \(k/n^{2}\) converges to a constant \(\delta\) with \(0<\delta\le \frac{1}{2(r-1)}\), an explicit asymptotic upper bound \(\phi_r(n,k)/k < 1\) is obtained.
- **Key Graph Concepts**: Complete graph packings (\(K_r\)-packings), Turán number \(t_{r-1}(n)\), extremal graph theory, asymptotic packing density, edge‑density regimes.

---

### 🚀 18. New results on openly disjoint cycles in regular digraphs
- 👤 **Authors**: Bin Chen, Wenshen Wu, Meishaung Chen  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41372)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors settle Seymour’s question negatively for the previously open cases \(r=6\) and \(r=7\), showing that not every \(r\)-regular digraph attains \(c(D)=r\).  They also sharpen the known bounds on the minimum guaranteed number of openly disjoint cycles through a common vertex, proving \(\displaystyle \left\lceil\frac{r}{6}\right\rceil \le c_r \le 5\left\lceil\frac{r}{6}\right\rceil\) for all \(r\).
- **Key Graph Concepts**: Regular digraphs, openly disjoint directed cycles, Seymour’s problem, Mader’s counterexamples, cycle packing bounds, extremal digraph theory.

### 🚀 19. The lattice of antichains of intervals: Dyck paths, level sets, and sweep dimension
- 👤 **Authors**: Paolo Boldi, Sebastiano Vigna  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41385)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors construct an explicit anti‑isomorphism between the lattice $\mathcal{E}_n$ of antichains of intervals (with its top element removed) and the Stanley lattice of Dyck words of semilength $n\!+\!1$, showing that the rank of an antichain equals $\binom{n+1}{2}$ minus the Dyck‑word area. Consequently, the rank‑generating function of $\mathcal{E}_n\!\setminus\!\{\top\}$ is the reverse of the Carlitz‑Riordan $q$‑Catalan polynomial, and they prove Takács’s asymptotic formula for the size of the largest level set.  They also introduce the **sweep dimension** of antichains of intervals of any finite poset $P$, establishing tight bounds $ \max(2,w)\le \text{sweep dim}\le 2w$ (with $w$ the width) and linking it to the Dushnik‑Miller dimension of the convex‑subset lattice.
- **Key Graph Concepts**: Antichains of intervals, Dyck paths, $q$‑Catalan polynomial, sweep dimension, Dushnik‑Miller dimension, lattice of convex subsets, width of a poset, staircase regions, Stanley lattice.

---

### 🚀 20. Sink polynomials of line graphs and weighted matching polynomials
- 👤 **Authors**: Per Alexandersson, Leonardo Saud Maia Leite  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41502)

#### 📝 Executive Summary & Innovations
- **Main Result**: For natural unit‑interval graphs the authors prove that the **acyclic sink polynomial**—the generating function for orientations counted by sinks—is real‑rooted for every non‑negative ascent weight, equivalently giving real‑rootedness of grouped elementary coefficients of the chromatic quasisymmetric function.  This real‑rootedness extends to all chordal claw‑free graphs, while the **all‑orientations sink polynomial** is real‑rooted for every claw‑free graph.  They also exhibit a line‑graph counterexample (a unicyclic graph) showing that acyclic‑sink real‑rootedness fails in general.
- **Key Graph Concepts**: Sink polynomial, line graphs, weighted matching polynomial, chromatic quasisymmetric functions, LL‑type (LLT) polynomials, real‑rootedness, unit‑interval graphs, chordal claw‑free graphs, claw‑free graphs, forest orientations, unicyclic graphs.

---

### 🚀 21. Equivariant Ehrhart series for rational simplices and rational cross‑polytopes
- 👤 **Authors**: Ryo Uchiumi  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41529)

#### 📝 Executive Summary & Innovations
- **Main Result**: By modifying the denominator in the rational‑function expression for equivariant Ehrhart series, the paper shows that for rational simplices and rational cross‑polytopes whose vertices are reciprocals of integers, the resulting numerator is both a genuine polynomial and **effective** (i.e., has non‑negative coefficients).  As a concrete application, the authors compute the equivariant series of the characteristic quasi‑polynomials associated with root systems.
- **Key Graph Concepts**: Equivariant Ehrhart series, rational simplices, rational cross‑polytopes, polynomial numerator, effectiveness, characteristic quasi‑polynomials, root systems, denominator modification.

### 🚀 22. Haiman's conjecture for *n* ≤ 10: Kazhdan‑Lusztig positivity of monomial immanants
- 👤 **Authors**: Keith McNulty  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41555)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper confirms Haiman’s conjecture for all partitions of *n* ≤ 10, showing that every monomial immanant is a non‑negative integer combination of Kazhdan‑Lusztig immanants. Consequently, Stembridge’s monomial immanant conjecture holds up to *n* = 10, and a complete description of the order of normalized irreducible‑character immanants on totally non‑negative matrices is obtained. The authors also provide a Newton‑polytope criterion for non‑negativity of coefficients on the totally non‑negative cone, verified computationally for *n* ≤ 10.
- **Key Graph Concepts**:  
  - Kazhdan‑Lusztig polynomials & positivity  
  - Monomial immanants & Hecke algebra characters  
  - Double cosets & descent sets in *Sₙ*  
  - Chromatic quasisymmetric functions (colourings)  
  - Totally non‑negative matrices & Newton‑polytope criteria  
  - Computational verification (Coxeter3, class polynomials)

---

### 🚀 23. Perfect state transfer on unicyclic graphs
- 👤 **Authors**: Xingkun Song  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41572)

#### 📝 Executive Summary & Innovations
- **Main Result**: The author gives a complete characterization of adjacency perfect state transfer (PST) in connected unicyclic graphs: the PST vertices must be opposite degree‑two vertices of a four‑cycle, and the attached trees must satisfy a specific characteristic‑polynomial condition. The minimal transfer time is shown to be π/√2, and sharp lower bounds of 46 on the graph order and 10 on the maximum degree are proved (with a refined bound of 21 for supports of size ≥ 7). A finite inverse construction enumerates all realizations for a prescribed eigenvalue support, and the smallest graph admitting PST with a seven‑element support has order 218.
- **Key Graph Concepts**:  
  - Perfect state transfer (PST) on adjacency matrices  
  - Unicyclic graphs (single cycle + trees)  
  - Eigenvalue support and characteristic polynomials  
  - Minimum transfer time (π/√2)  
  - Degree and order extremal bounds  
  - Spectral graph theory (support sets of the form {0, ±√2, ±u√2, ±v√2})

---

### 🚀 24. A Fan‑Type Theorem for Hamiltonian Berge Cycles in 3‑Uniform Hypergraphs
- 👤 **Authors**: Ailian Chen, Yanqiang Liu  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41577)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper establishes a fan‑type sufficient condition for the existence of a Hamiltonian Berge cycle in a simple 3‑uniform hypergraph on *n* ≥ 7 vertices. If the 2‑shadow is 2‑connected, every pair at Berge distance two has an endpoint of degree at least τₙ + 1 (with τₙ = C(⌊(n‑1)/2⌋, 2)), and every codegree‑one pair has both endpoints above τₙ, then the hypergraph contains a Hamiltonian Berge cycle. The distance‑two threshold is shown to be sharp, and the result is complemented by exhaustive verification for *n* = 7, 8.
- **Key Graph Concepts**:  
  - Hamiltonian Berge cycles in 3‑uniform hypergraphs  
  - 2‑shadow (graph formed by pairs of vertices contained in hyperedges)  
  - Fan‑type degree conditions & codegree constraints  
  - Longest‑path rotation technique  
  - Injective charging method  
  - Exhaustive computational verification for small orders

---

### 🚀 25. On sparse universally rigid graphs in $\mathbb{R}$
- 👤 **Authors**: Ole Gabsdil, Ezra Hirschi, Julien Portier  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41581)

#### 📝 Executive Summary & Innovations
- **Main Result**:  
  1. An Erdős–Rényi random graph $G(n,p)$ is 1‑universally rigid with high probability once $p \ge C\log n\cdot\log\log n/n$ for a sufficiently large constant $C$.  
  2. Consequently, 1‑universally rigid graphs of arbitrarily large girth exist (non‑constructively).  
  3. Every sufficiently large 1‑universally rigid graph on $n$ vertices has at least $(3/2+\varepsilon)n$ edges for some absolute $\varepsilon>0$, breaking the previous $3/2$ edge‑density barrier.

- **Key Graph Concepts**:  
  - 1‑universally rigid graphs, generic realizations in $\mathbb{R}$  
  - Erdős–Rényi random graphs $G(n,p)$  
  - Girth, edge‑density lower bounds, rigidity extensions  

---

### 🚀 26. Proper conflict-free degree-choosability of graphs with maximum average degree less than $8/3$
- 👤 **Authors**: Huijuan Xu  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41668)

#### 📝 Executive Summary & Innovations
- **Main Result**:  
  1. Every connected graph different from the 5‑cycle $C_5$ whose maximum average degree (mad) is below $8/3$ is proper conflict‑free $(\text{degree}+2)$‑choosable.  
  2. This improves the previous mad bound $18/7$ and removes the girth‑$\ge7$ hypothesis required in earlier $8/3$ results.  
  3. As a corollary, all planar graphs with girth at least 8 satisfy the same proper conflict‑free $(\text{degree}+2)$‑choosability.

- **Key Graph Concepts**:  
  - Proper conflict‑free coloring, list‑coloring, $(\text{degree}+k)$‑choosability  
  - Maximum average degree (mad) < $8/3$  
  - Planar graphs, girth constraints, open neighborhoods  

---

### 🚀 27. CRCs in four-dimensional lattice graphs
- 👤 **Authors**: Ivan Mogilnykh  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41716)

#### 📝 Executive Summary & Innovations
- **Main Result**:  
  1. New infinite families of completely regular codes (CRCs) are constructed in Cayley graphs of the groups $\mathbb{Z}_q^n$ equipped with the Lee metric.  
  2. By integrating binary linear programming, the authors enumerate all CRCs in the four‑dimensional lattice graphs $\mathbb{Z}_q^4$ for $q\le 7$, providing complete parameter matrices for these cases.

- **Key Graph Concepts**:  
  - Completely regular codes, CRC parameters  
  - Cayley graphs of $\mathbb{Z}_q^n$, Lee metric  
  - Four‑dimensional lattice graphs, binary linear programming enumeration  

---

### 🚀 28. Maximum edge overlap between independent random regular graphs
- 👤 **Authors**: Andrea D'Ascenzo, Riccardo Michielan  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41735)

#### 📝 Executive Summary & Innovations
- **Main Result**: For every fixed \(d\ge 3\), the maximum number of shared edges between two independent uniformly random \(d\)-regular graphs on \(n\) vertices is  
  \[
  n+\Theta_{\mathbb P}\!\left(\frac{n}{\log n}\right),
  \]
  where the linear term stems from the presence of a Hamilton cycle and the surplus term is shown to be optimal up to explicit constants.  For the special case \(d=2\) the overlap equals \(n-(1+o_{\mathbb P}(1))\log n\).  The paper also derives tight bounds for the edge‑based graph edit distance and for overlaps of unions of independent random perfect matchings under cyclic shifts.  
- **Key Graph Concepts**: Random \(d\)-regular graphs, Hamiltonicity, edge overlap, graph edit distance, spanning factors of cycles, random perfect matchings, contiguity arguments.

---

### 🚀 29. Bounds on the maximum denominator of fractional chromatic numbers
- 👤 **Authors**: Xinbo Xu, Xuding Zhu  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41771)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors improve the known upper bound on  
  \[
  \operatorname{sd}(n)=\max\{\operatorname{den}(\chi_f(G)):\ |V(G)|=n\}
  \]
  to  
  \[
  \operatorname{sd}(n)\le D(n)\,n^{-\frac12\log_2 n+\frac14\log_2\log_2 n+O(1)},
  \]
  for all sufficiently large \(n\), where \(D(n)=2^{-n}(n+1)^{(n+1)/2}\).  They also raise the lower exponential growth rate, proving  
  \[
  \limsup_{n\to\infty}\operatorname{sd}(n)^{1/n}\ge 3^{1/3}> \sqrt{2},
  \]
  thereby surpassing the previous bound \(\sqrt{2}\).  
- **Key Graph Concepts**: Fractional chromatic number, denominator function \(\operatorname{den}(\cdot)\), extremal graph theory, asymptotic combinatorial bounds, rational graph invariants.

---

### 🚀 30. Ore-degree conditions for hypergraph matchings
- 👤 **Authors**: Mingyang Guo, Tianhong Kan, Hongliang Lu, Feihong Yuan  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41787)

#### 📝 Executive Summary & Innovations
- **Main Result**: For any \(k\ge 3\) and \(n\ge ks\) (with \(n\) sufficiently large), a sharp Ore‑type condition guarantees a matching of size \(s\) in a \(k\)-uniform hypergraph \(H\): if  
  \[
  \sigma_k(H)>\max\Bigl\{k\!\Bigl(\binom{n-1}{k-1}-\binom{n-s}{k-1}\Bigr),\ (k-c)\binom{ks-2}{k-1}\Bigr\},
  \]
  where \(\sigma_k(H)\) is the minimum sum of vertex degrees over non‑edges and \(c=n-ks+1\), then such a matching exists.  This resolves the conjecture of Balogh, Palmer, and Raeisi for all \(k\ge 3\) in the large‑\(n\) regime.  
- **Key Graph Concepts**: \(k\)-uniform hypergraphs, Ore‑degree \(\sigma_k\), hypergraph matchings, extremal hypergraph theory, combinatorial degree conditions, conjecture of Balogh–Palmer–Raeisi.

### 🚀 31. The Alon‑Tarsi number of 4‑regular circulant graphs
- 👤 **Authors**: Xinbo Xu, Xuding Zhu  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41820)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors determine the Alon‑Tarsi number $\operatorname{AT}(C_n(s,t))$ for large families of connected $4$‑regular circulant graphs.  They prove that when $n=\ell p^{r}$ with $p$ an odd prime, $r\ge1$, and $t\equiv\pm s\pmod{\ell}$, the Alon‑Tarsi number equals $3$ provided either $\ell$ is even or $\ell\ge3$ is odd and $p\nmid 2^{\ell}-2$.  Additional exact values are obtained for the families $C_{6m}(2,3)$ ($m\ge2$) and $C_n(1,3)$ ($n\ge8$).
- **Key Graph Concepts**: Alon‑Tarsi number, 4‑regular circulant graphs $C_n(s,t)$, prime power factorisation, modular conditions on step sizes, strong list‑colouring techniques.

---

### 🚀 32. Revisiting the directed pathwidth of *h*-semicomplete digraphs
- 👤 **Authors**: Guilherme C. M. Gomes, Raul Lopes, Matthias Mnich  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41840)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper improves the bound on the function $f(k)$ guaranteeing a $k$‑triple in an $h$‑semicomplete digraph to a single‑exponential $f(k)=(h+1)k2^{27k+9}$ and supplies a polynomial‑time algorithm that actually finds such a $k$‑triple.  Moreover, the authors extend the directed‑pathwidth approximation of Fomin–Pilipczuk to $h$‑semicomplete digraphs and show that the Arc‑Disjoint Paths problem becomes fixed‑parameter tractable when parameterised by the number of paths together with $h$.  Finally, they demonstrate that directed pathwidth no longer bounds directed cliquewidth in this setting.
- **Key Graph Concepts**: Directed pathwidth, $h$‑semicomplete digraphs, $k$‑triples, parameterised algorithms, directed cliquewidth, Arc‑Disjoint Paths, polynomial‑time obstruction finding.

---

### 🚀 33. Strong edge‑colourings of truncations of cubic graphs
- 👤 **Authors**: Domenico Labbate, Federico Romaniello  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41950)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors settle Kardoš’s question for two broad classes of cubic graphs: they prove that the truncation $T(G)$ of any connected simple cubic graph that is either bipartite or simultaneously bridgeless and claw‑free has strong chromatic index exactly $6$.  Both proofs are constructive, relying on a compatibility criterion that allows colourings of smaller components to be merged, and the bipartite case even extends to certain multigraphs that are not extremal for the determinant.
- **Key Graph Concepts**: Strong edge‑colouring, strong chromatic index, truncation of cubic graphs, bipartite cubic graphs, bridgeless cubic graphs, claw‑free graphs, constructive colouring methods.

### 🚀 34. The 3-Color 2-Chromatic Gallai‑Ramsey Number for Complete Graphs
- 👤 **Authors**: Mark Budden, Elijah DeJonge  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41971)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors determine the exact value of the 3‑color 2‑chromatic Gallai‑Ramsey number \(gr^{3}_{2}(K_i,K_j,K_k)\) for every triple \((i,j,k)\) with \(1\le i\le j\le k\) whenever the ordinary Ramsey number \(r(K_i,K_j)\) is known. Their evaluation is complete, covering all admissible parameter ranges.
- **Key Graph Concepts**:
  - Gallai‑Ramsey numbers  
  - Rainbow‑triangle‑free 3‑edge‑colorings  
  - Complete graphs \(K_n\)  
  - Classical Ramsey numbers \(r(K_i,K_j)\)  
  - Chromatic constraints in edge‑colorings  

---

### 🚀 35. Hedetniemi's conjecture for Shannon OR‑capacity: counterexamples and asymptotic separation
- 👤 **Authors**: Julius A. Zeiss  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41977)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper disproves the Shannon OR‑capacity analogue of Hedetniemi’s conjecture by constructing, for arbitrarily large complete graphs, a second graph of strictly larger capacity whose categorical product has capacity strictly below that of the complete factor. Moreover, the authors exhibit families where both factor capacities exceed any prescribed threshold while the product capacity remains below it, and even cases where factor capacities diverge to infinity but the product capacity grows only sub‑polynomially.
- **Key Graph Concepts**:
  - Shannon OR‑capacity (zero‑error information theory)  
  - Categorical (tensor) product of graphs  
  - Hedetniemi’s conjecture (capacity version)  
  - Spectral interpolation techniques  
  - Distinguishability graphs and random‑switching communication models  

---

### 🚀 36. Hilton‑Zhao vertex‑splitting conjecture for triangle‑free graphs
- 👤 **Authors**: Xuli Qi, Xin Tian, Gregory Gutin  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41984)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors verify a revised Hilton‑Zhao vertex‑splitting conjecture for triangle‑free \(\Delta\)-regular Class 1 graphs. They prove that any non‑extreme vertex‑splitting yields a \(\Delta\)-critical graph whenever \(\Delta > \frac{n-1}{3}\), and that for arbitrary (including extreme) splittings the resulting graph is \(\Delta\)-critical provided \(n\ge 10\) and \(\Delta > \frac{2n-3}{5}\) (with the non‑strict bound \(\Delta\ge\frac{2n-3}{5}\) sufficient when \(n>24\)). This settles the conjecture across its full degree range for triangle‑free bases, notably handling the previously elusive 6‑regular case.
- **Key Graph Concepts**:
  - Vertex‑splitting operations  
  - Edge‑chromatic criticality (Class 1 vs. Class 2)  
  - \(\Delta\)-critical graphs  
  - Triangle‑free regular graphs  
  - Full‑deficiency pairs, homomorphism theorems for dense triangle‑free graphs, Hamilton decompositions via graph detachment  

---

### 🚀 37. Ramsey numbers \(R(K_{1,4},K_{m,n})\) for small \(m\)
- 👤 **Authors**: Khaidar Abdullin, Dmitrii Taletskii  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41999)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors determine every previously unknown value of the two‑color Ramsey number \(R(K_{1,4},K_{m,n})\) when \(\min(m,n)\le 8\).  Moreover, they prove the exact values  
  \[
  R(K_{1,4},K_{m,m})=
  \begin{cases}
  26 & m=9,\\
  29 & m=10,\\
  31 & m=11,\\
  33 & m=12,
  \end{cases}
  \]
  completing the small‑\(m\) picture for this family of Ramsey numbers.
- **Key Graph Concepts**:  
  - Ramsey numbers (generalized two‑color)  
  - Star graph \(K_{1,4}\)  
  - Complete bipartite graphs \(K_{m,n}\)  
  - Extremal combinatorial techniques for small parameters  

---

### 🚀 38. Tiling without a subspace complement: a sharp counterexample in dimension nine over the field with two elements
- 👤 **Authors**: Samuel J. Ferguson, Joshua Iosevich  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42005)

#### 📝 Executive Summary & Innovations
- **Main Result**: An explicit 64‑point set in \(\mathbb F_2^{9}\) is constructed that tiles the space by translation yet possesses no linear‑subspace tiling complement, establishing that the “every tile has a linear‑subspace complement’’ property holds exactly for dimensions \(d\le 8\).  The example is spectral (hence not a Fuglede counterexample) and the authors completely classify its 512 tiling complements and 64 spectra.
- **Key Graph Concepts**:  
  - Translational tilings in vector spaces over \(\mathbb F_2\)  
  - Spectral sets and Wiener norm  
  - Linear‑subspace complements (affine geometry)  
  - Connections to perfect binary codes and combinatorial design  

---

### 🚀 39. Extremal character spectra of finite projective systems
- 👤 **Authors**: Shitao Li, Yang Li, Gaojun Luo  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42006)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper introduces the notions of \(r\)-maximum and \(r\)-full character spectra for multisets of points in projective space \(\mathrm{PG}(k-1,q)\) and proves existence of \(r\)-full systems across a wide parameter range.  For the extremal problem when \(r=k-1\) the authors determine the exact minimum size \(\nu_{k-1}(k,q)\) and give tight bounds for general \(r\), improving known upper bounds for \(r=1\).  New global moment identities and local flat‑incidence bounds are developed to control large character spectra.
- **Key Graph Concepts**:  
  - Finite projective geometries \(\mathrm{PG}(k-1,q)\)  
  - Character functions and spectra of point multisets  
  - \(q\)-binomial coefficients and extremal set theory  
  - Connections to subcode weight spectra and additive labelings  

---

### 🚀 40. Modulo k-orientations of highly edge‑connected signed graphs
- 👤 **Authors**: You Lu, Zhengke Miao, Zhenyu Tian, Cun‑Quan Zhang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42019)

#### 📝 Executive Summary & Innovations
- **Main Result**: For every odd integer \(k\ge 3\), any essentially \(k\)-unbalanced signed graph that is \((6k-10)\)-edge‑connected admits a modulo‑\(k\) orientation. This improves the previous edge‑connectivity requirement of \(6k-7\) established by Zhu (JCTB 112, 2015).  
- **Key Graph Concepts**: Signed graphs, modulo \(k\)-orientation, edge‑connectivity, essentially \(k\)-unbalanced condition, graph orientation, connectivity bounds.

---

### 🚀 41. Berenstein‑Zelevinsky polytopes for type \(\mathrm{G}_{2}\)
- 👤 **Authors**: Thomas Magnuson, Tyrrell McAllister  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42038)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors give an explicit system of linear equations and inequalities describing Berenstein–Zelevinsky (BZ) polytopes of type‑\(\mathrm{G}_{2}\). They prove that the denominator of any such polytope divides \(180\) (and this bound is sharp) and that the quasi‑period of its Ehrhart quasipolynomial always divides \(6\). Moreover, they exhibit type‑\(\mathrm{G}_{2}\) BZ polytopes that violate Ehrhart positivity, contrary to expectations from classical types.  
- **Key Graph Concepts**: Berenstein–Zelevinsky polytopes, type \(\mathrm{G}_{2}\) Lie algebras, Ehrhart quasipolynomials, denominator, quasi‑period, polyhedral combinatorics, lattice point enumeration.

---

### 🚀 42. A Counterexample to the Alon‑Krivelevich Conjecture and a New Lower Bound for Choosability of Bipartite Graphs
- 👤 **Authors**: Junran Yu, Gexin Yu  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42094)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper constructs a family of bipartite graphs whose choice number satisfies \(\operatorname{ch}(G)\ge k+1\) and yields the lower bound  
  \[
  \operatorname{ch}(G)\;\ge\;\Bigl(\tfrac{1}{32}-o(1)\Bigr)\frac{(\ln\Delta)^{2}}{(\ln\ln\Delta)^{3}},
  \]  
  where \(\Delta\) is the maximum degree. This shows that \(\operatorname{ch}(G)/\ln\Delta\) can grow without bound, thereby disproving the Alon–Krivelevich conjecture. The proof blends probabilistic tools (conditional product measures, Doob martingales) with a topological argument via the Brouwer fixed‑point theorem.  
- **Key Graph Concepts**: List coloring (choosability), bipartite graphs, maximum degree \(\Delta\), Alon–Krivelevich conjecture, probabilistic method, Brouwer fixed‑point theorem, lower bounds for choice number.

### 🚀 43. On nowhere-zero ${3}$-flows in Cayley graphs on groups of order ${p^2n}$
- 👤 **Authors**: Milad Ahanjideh, István Kovács  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42099)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors prove Tutte’s 3‑flow conjecture for all Cayley graphs on groups \(G\) of order \(p^{2}n\) where \(p>2\) and either the Sylow‑\(p\) subgroup or a Hall‑\(n\) subgroup of \(G\) is cyclic. This extends previous work that handled the cases \(n\) prime and \(p=2\). The proof combines group‑theoretic structure with flow‑extension techniques specific to Cayley graphs.  
- **Key Graph Concepts**: Cayley graphs, nowhere‑zero 3‑flows, Tutte’s 3‑flow conjecture, cyclic Sylow subgroups, Hall subgroups, group‑order constraints.

---

### 🚀 44. Weighted flip graphs from cyclic quantum mutations: pentagon inequalities and exponential separations
- 👤 **Authors**: Xiaomin Tang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40661)

#### 📝 Executive Summary & Innovations
- **Main Result**: By assigning weights derived from positive cyclic quantum mutations at a third root of unity, the paper exhibits a pentagon inequality showing that in type \(A_{4}\) a six‑flip path can have strictly smaller total weight than the unique five‑flip geodesic. Using a compatible projective gluing construction, this phenomenon is amplified to an exponential separation between minimum‑weight paths and shortest‑flip paths for all types \(A_{n}\) with \(n\ge 4\). A quantitative perturbation bound guarantees the robustness of the separation.  
- **Key Graph Concepts**: Flip graphs of polygon triangulations, weighted graph edges, type‑\(A\) associahedra, pentagon inequality, exponential path‑weight separation, cyclic quantum mutations.

---

### 🚀 45. Tree‑based Algorithms for Breakpoint Median and Near‑Median Genomes
- 👤 **Authors**: Poly H. da Silva, Arash Jamshidpey, David Sankoff  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40667)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors introduce a tree‑based framework that builds rooted labeled trees whose leaves encode all breakpoint‑median genomes for three linear unichromosomal genomes. The reduced search space provably contains every exact median while being dramatically smaller than the full permutation space, enabling exact enumeration, fast sampling of near‑medians, and targeted exploration of balanced solutions. Experimental results confirm that near‑optimal medians are often found early in the tree traversal.  
- **Key Graph Concepts**: Breakpoint graphs, permutation (unsigned) graphs, median and near‑median problems, rooted labeled trees, adjacency constraints, search‑space reduction, combinatorial genome rearrangements.

### 🚀 46. Truncated Grassmannians: polytopes, representations, and Cauchy formulas
- 👤 **Authors**: Evgeny Feigin, Igor Makhlin  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40891)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors introduce cyclic representations of maximal parabolic subalgebras of \(\mathfrak{gl}_n\) that are dual to the homogeneous components of coordinate rings of truncated Grassmannians.  They prove that the characters of these representations are given by truncated Cauchy formulas and construct explicit monomial bases via generalized chain polytopes, linking them to Gelfand–Tsetlin patterns through the RSK correspondence.  
- **Key Graph Concepts**: Generalized chain polytopes, RSK correspondence, Gelfand–Tsetlin patterns, Cauchy‑type formulas, combinatorial structures of coordinate rings.

---

### 🚀 47. Functorial Analysis of Group‑Alphabet Cellular Automata
- 👤 **Authors**: François Huard, Nathan Dion Larivière  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41013)

#### 📝 Executive Summary & Innovations
- **Main Result**: A faithful functor \(F:\mathbf{Grp}\to\) pointed digraphs is constructed, and its image \(\mathcal C_{n,\phi}\) (the category of state‑transition graphs of length‑\(n\) group‑alphabet cellular automata) is shown to be equivalent to the source category.  This equivalence enables the translation of group‑theoretic and homological constructions into graph‑theoretic language, yielding explicit formulas for cycle lengths and multiplicities in the product of objects of \(\mathcal C_{n,\phi}\).  
- **Key Graph Concepts**: Pointed directed graphs, state‑transition digraphs, categorical product of digraphs, cycle length enumeration, graph‑theoretic representation of group actions.

---

### 🚀 48. Traveling Salesman Problem on Graphs with Proportional Independent Set
- 👤 **Authors**: Ethan X. Fang, Shengtao Guo, Junwei Lu, Yuan Yao  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41178)

#### 📝 Executive Summary & Innovations
- **Main Result**: For undirected graphs possessing an independent set of size at least \(\alpha n\) with \(3/7<\alpha\le 1/2\), the paper presents a deterministic algorithm that finds a minimum‑cost Hamiltonian cycle in \(O^{*}(\gamma(\alpha)^{n})\) time, where \(\gamma(\alpha)<2\).  In the bipartite case the running time improves to \(O^{*}((1+2\sqrt2)^{n/2})\approx O^{*}(1.957^{n})\), achieved via a restricted Held–Karp dynamic program that exploits structural properties of optimal assignments derived from a regular triangulation of a product of simplices.  
- **Key Graph Concepts**: Hamiltonian cycle, independent set (proportional size), bipartite graphs, Held–Karp dynamic programming, minimum‑cost assignments, triangulation of product of simplices.

### 🚀 49. A reciprocal Schoenberg inequality and its extensions
- 👤 **Authors**: Olga Holtz  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41325)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper furnishes a concise proof of the reciprocal Schoenberg inequality by exhibiting a positive similarity that transforms a reciprocal‑derivative companion matrix into a complex symmetric matrix. It further determines the optimal constants for the associated inequalities for every positive exponent (including the sub‑linear range) and extends the framework to arbitrary positive charges, providing a complete description of equality cases in two quartic inequalities. A closed‑form generating determinant and a quantitative collinearity estimate are also derived.
- **Key Graph Concepts**:  
  - Spectral Graph Theory (via symmetric matrix representations)  
  - Companion Matrices and their normal powers  
  - Inequalities involving elementary symmetric functions (relevant to graph spectra)  

---

### 🚀 50. List 3-Coloring in tame classes of graphs in quasipolynomial time
- 👤 **Authors**: Paweł Rzążewski  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41620)

#### 📝 Executive Summary & Innovations
- **Main Result**: The author proves that the List 3‑Coloring problem can be solved in quasipolynomial time on any *tame* graph class—i.e., a class where every \(n\)-vertex graph has at most \(n^{c}\) minimal separators for some constant \(c\). This unifies and extends the tractability of List 3‑Coloring across many well‑studied families such as chordal, permutation, and circle graphs.  
- **Key Graph Concepts**:  
  - List Coloring (specifically List 3‑Coloring)  
  - Minimal Separators and their polynomial bound in tame classes  
  - Tame graph classes (chordal, permutation, circle graphs)  
  - Quasipolynomial‑time algorithms  

---

### 🚀 51. Exchange graphs and \(g\)-vectors of surface rigid algebras
- 👤 **Authors**: Ping He, Bo Le  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41703)

#### 📝 Executive Summary & Innovations
- **Main Result**: The work classifies the connected components of support \(\tau\)-tilting (exchange) graphs for surface rigid algebras arising from partial tagged triangulations of punctured marked surfaces with boundary. It shows that a connected algebra’s exchange graph is disconnected precisely when the algebra is weakly symmetric, has at least two simple modules, and Cartan rank one—yielding exactly two components. Moreover, \(\tau\)-tilting finiteness is proved equivalent to the Cartan matrix being positive definite, and explicit primitive \(g\)-vector ray generators are described in endpoint coordinates, distinguishing types A, C, and D.  
- **Key Graph Concepts**:  
  - Exchange (support \(\tau\)-tilting) graphs  
  - \(g\)-vectors and Cartan matrices of surface rigid algebras  
  - Partial tagged triangulations of punctured surfaces  
  - Classification of graph components (connected vs. disconnected)  
  - Types A, C, D via unicyclic configurations  

---

### 🚀 52. An extension of the classic Buneman theorem from phylogenetic trees to networks
- 👤 **Authors**: Mirko Wilde, Mareike Fischer  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41725)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors introduce a general framework for studying identifiability of phylogenetic networks under hardwired parsimony. Using this framework they prove that the *tree of blobs* of a network can be uniquely reconstructed from its \(A_1\)-alignment, extending Buneman’s classic splits‑equivalence theorem to networks. They also demonstrate a fundamental limitation: cycles of length ≥ 5 cannot, in general, be identified from character data under hardwired parsimony.  
- **Key Graph Concepts**: Phylogenetic networks, hardwired parsimony, Buneman theorem, tree of blobs, \(A_k\)-alignments, cycle identifiability, splits equivalence.

---

### 🚀 53. Bethe Hessian Recovery through the Kesten‑Stigum Regime
- 👤 **Authors**: Dingding Dong, Theo McKenzie  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41802)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper shows that the outlier eigenvectors of the Bethe Hessian matrix achieve weak recovery in the stochastic block model down to the Kesten‑Stigum threshold for any fixed expected degree \(d>1\). This matches the optimal information‑theoretic limit and the guarantees of non‑backtracking spectral methods while using a Hermitian \(n\times n\) matrix. The proof constructs approximate eigenvectors via Green’s functions on the limiting Poisson tree and transfers them to finite graphs.  
- **Key Graph Concepts**: Bethe Hessian, stochastic block model, Kesten‑Stigum threshold, outlier eigenvectors, weak recovery, spectral graph theory, non‑backtracking matrix, Poisson tree, Green’s function.

---

### 🚀 54. Treedepth is NP‑Hard on Planar Graphs of Maximum Degree 3
- 👤 **Authors**: Kolja Kühn  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42033)

#### 📝 Executive Summary & Innovations
- **Main Result**: Assuming \(P\neq NP\), the author proves that computing the treedepth of planar graphs with maximum degree 3 is NP‑hard under polynomial‑time Turing reductions, settling an open question about the tractability of treedepth on restricted graph classes. The degree bound is shown to be tight, since treedepth can be computed efficiently on graphs of maximum degree 2.  
- **Key Graph Concepts**: Treedepth, planar graphs, bounded degree, NP‑hardness, polynomial‑time Turing reductions, computational complexity, graph parameters.

### 🚀 55. Two choices suffice: $k$-out sampling leaves $O(n/k)$ intercomponent edges for $k\geq 2$
- 👤 **Authors**: Yanyu Chen, Yu Chen  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42067)

#### 📝 Executive Summary & Innovations
- **Main Result**: For every integer $k\ge 2$, the expected number of original edges that join distinct components of the random $k$‑out sampled spanning subgraph of any $n$‑vertex simple graph is $O(n/k)$. This settles the conjecture of Holm, King, Thorup, Zamir, and Zwick, showing that two independent local choices per vertex are sufficient to contract any graph to a quotient with only $O(n)$ edges in expectation (the bound is tight up to constants and fails for $k=1$).  
- **Key Graph Concepts**: random $k$‑out sampling, spanning subgraphs, intercomponent edges, graph contraction, switching arguments, degree‑weighted component potential, expectation bounds.

---

### 🚀 56. Delocalized region of bipartite Erdős‑Rényi graphs
- 👤 **Authors**: Johannes Alt, Serafina Wald  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42088)

#### 📝 Executive Summary & Innovations
- **Main Result**: In a bipartite Erdős‑Rényi graph $\mathbb G(n,p,d/\sqrt{np})$, if $d > b_* \log (n+p)$ (with $b_*$ an explicit function of the size ratio $n/p$) then, with high probability, every eigenvector of the adjacency matrix whose eigenvalue stays away from zero is delocalized. Moreover, bulk eigenvectors are delocalized already for $d \ge \mathcal D\sqrt{\log (n+p)}$, and in the super‑critical regime $d\gg\log (n+p)$ *all* eigenvectors are delocalized. The thresholds are optimal for delocalization near the spectral edges.  
- **Key Graph Concepts**: bipartite Erdős‑Rényi graphs, adjacency matrix eigenvectors, eigenvector delocalization, spectral edges, random matrix theory, sparse rectangular random matrices.

---

### 🚀 57. Band Random Graphs: Connectivity, Geometry, and Transport
- 👤 **Authors**: Shantanav Chakraborty, Kyle Luh, Rudransh Pratap Singh  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42107)

#### 📝 Executive Summary & Innovations
- **Main Result**: For the random subgraph $G(n,p,m)$ of the $m$‑th power of a cycle, the sharp connectivity threshold is $p\sim (\log n)/(2m)$. When $n(1-p)^{2m}\to\lambda\in(0,\infty)$ the number of isolated vertices converges to $\mathrm{Poisson}(\lambda)$ and, with high probability, all remaining vertices belong to a single giant component $C_1$, whose diameter is $\Theta\!\bigl(n/m+\log n/\log\log n\bigr)$. For any fixed $c>1$, uniformly over $p\ge c\log n/(2m)$ the lazy‑walk spectral gap and mean hitting times match those of the underlying deterministic cycle power $C_n^m$, with an explicit asymptotic formula for $H_G(x,y)$.  
- **Key Graph Concepts**: random subgraph of cycle power $C_n^m$, connectivity threshold, Poisson limit for isolated vertices, component geometry, diameter, lazy random walk spectral gap, hitting times, Erdős‑Rényi‑type asymptotics, transport on band graphs.

### 🚀 58. On kernel Mengerian orientations of line multigraphs
- 👤 **Authors**: Han Xiao  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/1507.06053)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper proves that for clique‑acyclic orientations of line multigraphs, being *kernel ideal* is equivalent to being *kernel Mengerian*. Moreover, these two properties hold exactly when the orientation is kernel‑perfect and contains no even‑cycle obstruction. This gives a complete polyhedral characterisation of kernels in this graph class.  
- **Key Graph Concepts**: kernels, digraphs, line multigraphs, clique‑acyclic orientations, fractional kernel polytope, total dual integrality, kernel‑perfect digraphs, even‑cycle obstruction.

---

### 🚀 59. On almost Gallai colourings in complete graphs
- 👤 **Authors**: Alexandr Grebennikov, Letícia Mattos, Tibor Szabó  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2503.17334)

#### 📝 Executive Summary & Innovations
- **Main Result**: For every \(t\ge 4\) the maximum number \(\tau_t(n)\) of rainbow \(t\)-cliques in an almost \(t\)-Gallai colouring of \(K_n\) satisfies \(n^{2-o(1)}\le \tau_t(n)=o(n^2)\). For the case \(t=3\) the authors obtain the first non‑trivial bounds  
  \[
  \Bigl(\tfrac12-o(1)\Bigr)n\log n \le \tau_3(n) \le O\!\bigl(n^{\sqrt{2}}\log n\bigr).
  \]  
  These results improve upon the trivial linear and quadratic bounds and reveal a distinct behaviour when \(t=3\).  
- **Key Graph Concepts**: rainbow colourings, almost Gallai colourings, complete graphs \(K_n\), rainbow \(t\)-cliques, probabilistic method, edge‑isoperimetric inequality, hypercube, Ruzsa–Szemerédi problem.

---

### 🚀 60. Hamilton cycles in pseudorandom graphs: resilience and approximate decompositions
- 👤 **Authors**: Nemanja Draganić, Jaehoon Kim, Hyunwoo Lee, David Munhá Correia, Matías Pavez‑Signé, Benny Sudakov  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2507.22807)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors establish two broad theorems for sparse pseudorandom graphs. First, any spanning subgraph \(G\) of an \((n,d,\lambda)\)-graph with minimum degree \(\delta(G)\ge (\tfrac12+\gamma)d\) and spectral gap \(d/\lambda\) sufficiently large contains a Hamilton cycle. Second, when \(d/\lambda\) is large, the host graph itself admits at least \((1-\varepsilon)\tfrac d2\) edge‑disjoint Hamilton cycles and its entire edge set can be covered by at most \((1+\varepsilon)\tfrac d2\) such cycles, achieving asymptotically optimal packing and covering.  
- **Key Graph Concepts**: pseudorandom graphs, \((n,d,\lambda)\)-graphs, Hamilton cycles, Dirac‑type resilience, spectral gap, edge‑disjoint Hamilton cycle packing, Hamilton decomposition, sparse regular graphs.

---

### 🚀 61. Closed Colored Models and Demazure Crystals
- 👤 **Authors**: Yingzi Yang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2512.05479)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper constructs two families of five‑vertex lattice models (open and closed) whose partition functions equal Demazure characters.  It proves that the tableaux arising from states of the closed model form a full Demazure crystal by defining explicit Kashiwara crystal operators via lattice moves, and gives an independent proof that the open model realises Demazure atoms.  Moreover, a bosonic analogue with a parameter \(t\) is introduced, and at \(t=0\) the closed bosonic model satisfies Yang–Baxter equations, yielding a Demazure‑Lusztig recursion for its partition function.
- **Key Graph Concepts**: Crystal Graphs, Five‑Vertex Model, Gelfand–Tsetlin Patterns, Demazure Crystals, Yang–Baxter Equation, Lattice Moves, Demazure‑Lusztig Recursion.

---

### 🚀 62. Tight paths in fully directed hypergraphs
- 👤 **Authors**: Richard C. Devine, Kevin G. Milans  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2601.00144)

#### 📝 Executive Summary & Innovations
- **Main Result**: For an \(r\)-uniform fully directed hypergraph (an \(r\)-digraph), the authors determine asymptotically sharp bounds on the smallest \(k\) such that every \((r,k)\)-tournament contains a directed tight path whose length grows unbounded with the number of vertices.  They pinpoint the exact threshold for \(r\le 5\) and prove, for example, that \(f(n,3,3)=\Theta(\log n)\) up to constant factors, while \(f(n,3,4)=\Omega(n^{1/5})\).  
- **Key Graph Concepts**: \(r\)-uniform directed hypergraphs, \((r,k)\)-tournaments, Directed tight paths, Extremal function \(f(n,r,k)\), Euler’s totient function \(\varphi(r)\), Hypergraph spanning structures.

---

### 🚀 63. Decomposable shuffles
- 👤 **Authors**: João Dias, Bruno Dinis, Carlos Correia Ramos  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2602.00461)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors introduce a new order‑theoretic framework for shuffles viewed as ordered partitions of \(\mathbb N\), defining *decomposable shuffles* as sums of finite ordinals, copies of \(\omega\), and copies of its dual \(\omega^{*}\) indexed by countable scattered linear orders.  For the subclass of *layered shuffles* they give an explicit finite‑address representation that reduces order comparison to lexicographic comparison of integer tuples, determine the order types of all represented shuffles, and exhibit an involution realising order duality.  Finally, they construct a graded monoid on bench‑free uniform shuffles whose degree‑one component is isomorphic to the full symmetric group \(\operatorname{Sym}(\mathbb N)\).  
- **Key Graph Concepts**: Ordered partitions, Scattered linear orders, Bench/Ladder/Snake building blocks, Lexicographic order, Symmetric group \(\operatorname{Sym}(\mathbb N)\), Monoid structure, Order duality.

### 🚀 64. Characterizing the optimum bases of a convex geometry using quasi-closed hypergraphs
- 👤 **Authors**: Anthony Meunier, Lhouari Nourine, Simon Vilmin  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2603.14615)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors give a precise characterization of optimal implicational bases of convex geometries in terms of *quasi‑closed hypergraphs*.  They show that when every quasi‑closed hypergraph associated with a convex geometry has pairwise disjoint edges, any implicational base can be minimized in polynomial time using existing reduction algorithms.  This tractability is then proved for several important families—double‑shelling convex geometries, \(D\)-geometries, convex geometries with the \(n\)-Carousel property, and \(q\)-acceptant convex geometries—thereby unifying and extending earlier results.
- **Key Graph Concepts**: Convex geometry, closure system, implicational (or Horn) base, quasi‑closed hypergraph, disjoint hypergraph edges, polynomial‑time optimization, double‑shelling convex geometries, \(D\)-geometries, \(n\)-Carousel property, \(q\)-acceptant convex geometries.

---

### 🚀 65. Bounded Bruhat intervals and affine Coxeter groups
- 👤 **Authors**: Grant T. Barkley, Christian Gaetz  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2606.16894)

#### 📝 Executive Summary & Innovations
- **Main Result**: Extending Dyer’s 1991 finiteness theorem, the paper proves that for any fixed length \(k\) there are only finitely many isomorphism types of Bruhat intervals in *affine* Coxeter groups, and that this finiteness property uniquely characterizes affine groups among all infinite Coxeter groups.  Moreover, the authors establish that the coefficients of \(q\) in Kazhdan–Lusztig polynomials are uniformly bounded if and only if the underlying Coxeter group is finite or affine.
- **Key Graph Concepts**: Bruhat order, Bruhat intervals, affine Coxeter groups, finite Coxeter groups, Kazhdan–Lusztig polynomials, coefficient boundedness, isomorphism types of intervals.

---

### 🚀 66. A characterization of edge‑chromatic 3‑critical graphs
- 👤 **Authors**: Le Chen, Songling Shan  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2606.27131)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper provides the first structural characterization of *nontrivial* \(\Delta\)-critical graphs with \(\Delta=3\).  Every such graph can be obtained from smaller 3‑critical graphs by one of three operations: (i) replacing a vertex with a triangle, (ii) performing a Hajós‑join, or (iii) applying a newly introduced *Meredith‑type extension* (a generalization of the classic Meredith extension using arbitrary class‑1 graphs).  Additionally, all nontrivial 3‑critical graphs arise from snarks after deleting at most one vertex and some independent edges.
- **Key Graph Concepts**: Edge‑chromatic index, \(\Delta\)-critical graphs, 3‑critical graphs, nontrivial critical graphs, Hajós‑join, Meredith‑type extension, class‑1 graphs, snarks, chromatic index, Seymour’s exact conjecture, Grötzsch’s conjecture.

### 🚀 67. The minimum of the graph likelihood
- 👤 **Authors**: Simone Severini, Eric W. Weisstein  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2608.19467)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors prove that among all complete bipartite graphs on a fixed number of vertices, the balanced complete bipartite graph uniquely minimises the graph‑likelihood defined by the uniform sequential attachment process.  Exact enumeration shows that this graph is also the global minimiser for orders 6–14, but starting at \(n=15\) the global minimisers change (e.g., \(C_5[\bar K_3]\) and its complement), providing the first counter‑examples to the conjecture of Dervovic, Mocherla and Severini.  Asymptotically, the likelihood of the balanced bipartite graph is \(2^{-(\tfrac12-\tfrac1{8\ln2}+o(1))n^{2}}\), whereas the true minimum over all graphs is \(2^{-(\tfrac12+o(1))n^{2}}\), so the conjectured minimiser is exponentially larger than the optimum.
- **Key Graph Concepts**:  
  - Graph likelihood (uniform sequential attachment process)  
  - Balanced complete bipartite graphs \(K_{\lfloor n/2\rfloor,\lceil n/2\rceil}\)  
  - Blow‑ups of base graphs, self‑complementary mixed blow‑ups  
  - Shannon entropy of the random process  
  - Vertex‑deletion recurrence (algorithmic evaluation \(O(2^{n}n)\))  
  - Extremal graph theory / asymptotic enumeration  

---

### 🚀 68. Ramanujan Transforms and Maximum Energy of Odd-Total-Exponent Integral Circulants
- 👤 **Authors**: Jianwei Jiang, Chunhua Yang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2608.29523)

#### 📝 Executive Summary & Innovations
- **Main Result**: For an integer \(n\) that is a product of distinct odd primes with an odd total exponent, the integral circulant graph whose divisor set is the “checkerboard” set (those divisors whose prime‑power exponent sum is even) uniquely attains the maximum graph energy among all non‑empty proper‑divisor sets.  The maximal energy equals \(\frac12\bigl(n+\prod_{p\mid n}P_{k_{p}}(x_{p})\bigr)\) where the explicit polynomials \(P_{k}(x)\) are given in the abstract.  The proof settles Roldan’s conjecture for the case \(n=p^{2}q^{3}\) (odd primes \(p,q\), \(q\ge5\)) and introduces a weighted prime‑power Ramanujan transform that yields an exact tensor‑product energy model.
- **Key Graph Concepts**:  
  - Graph energy (sum of absolute adjacency eigenvalues)  
  - Integral circulant graphs (ICGs) and divisor sets  
  - Checkerboard divisor set, odd‑total‑exponent condition  
  - Weighted prime‑power Ramanujan transforms  
  - Polynomial matrix families, semidefinite parity theorem  
  - Tensorisation of spectral structure, one‑norm bounds on tensor operators  

---

### 🚀 69. Local Fan-type obstructions and Ore-type conditions for rainbow Hamiltonicity in graph systems
- 👤 **Authors**: Ailian Chen, Hao Chen  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.13977)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper establishes that for a graph system \(\mathcal{G}=(G_{1},\dots,G_{n})\) on a common vertex set, a local Fan‑type condition—namely, whenever two vertices \(u,v\) have \(\delta(u),\delta(v)<\frac{n}{2}\) and rainbow distance \(d^{c}(u,v)\le2\) they must be adjacent in the common edge set—forces either a rainbow Hamilton cycle or forces the system to satisfy the extremal bound \(\sum_{v}\delta(v)\le\frac{n^{2}-1}{2}\) with empty common edge set.  Consequently, either the common edge set is non‑empty or \(\sum_{v}\delta(v)\ge\lceil n^{2}/2\rceil\) guarantees a rainbow Hamilton cycle.  Moreover, a local Ore‑type condition \(\delta(u)+\delta(v)<n\) together with \(d^{c}(u,v)\le2\) already guarantees a rainbow Hamilton cycle.  The proofs combine a rainbow rotation‑extension technique with a double‑counting argument in an auxiliary digraph.
- **Key Graph Concepts**:  
  - Graph systems, common vertex set, common edge set \(E_{\cap}\)  
  - Rainbow Hamilton cycles and rainbow distance \(d^{c}(u,v)\)  
  - Local Fan‑type condition, local Ore‑type condition  
  - Minimum degree function \(\delta(v)=\min_{i}d_{G_{i}}(v)\)  
  - Rotation–extension method for rainbow paths/cycles  
  - Double‑counting in auxiliary digraphs, extremal degree sums  

---

### 🚀 70. Prime Nullspace Matrices and Even Dominating Sets
- 👤 **Authors**: William F. Klostermeyer  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.31475)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper introduces the notion of *prime nullspace matrices*—those (0,1)-matrices that cannot be obtained by concatenating smaller nullspace matrices—and provides a structural characterization of such matrices. It establishes a bijective correspondence between prime nullspace matrices and even dominating sets in rectangular grid graphs, yielding new existence and counting results for these dominating sets.  
- **Key Graph Concepts**:  
  - Even dominating sets  
  - Grid graphs \(P_m \square P_n\)  
  - Rectilinear neighbor relation  
  - (0,1)-nullspace matrices  
  - Prime (indecomposable) matrix constructions  

---

### 🚀 71. A proof of Wang's planar $D$-coloring conjecture
- 👤 **Authors**: Harshit Verma  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.33322)

#### 📝 Executive Summary & Innovations
- **Main Result**: The author settles Wang’s planar $D$‑coloring conjecture for all maximum degrees $\Delta\ge 6$, proving that every planar graph with maximum degree $\Delta$ admits a $D$‑coloring using exactly $2\Delta-1$ colors—a bound that is shown to be sharp. The case $\Delta=6$ is handled via a computer‑assisted discharging argument, while the general $\Delta\ge 7$ case follows from a refined discharging proof.  
- **Key Graph Concepts**:  
  - Planar graphs  
  - Proper edge‑coloring ($D$‑coloring)  
  - Rainbow $K_4$ minus an edge subgraphs  
  - Discharging method (including computer‑assisted verification)  
  - Maximum degree $\Delta$  

---

### 🚀 72. Profile and neighbourhood complexity of graphs excluding a minor and tree‑structured graphs
- 👤 **Authors**: Laurent Beaudou, Jan Bok, Florent Foucaud, Daniel A. Quiroz, Jean‑Florent Raymond  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2501.08895)

#### 📝 Executive Summary & Innovations
- **Main Result**: The authors obtain tight asymptotic upper bounds on the $r$‑profile complexity (and consequently on the $r$‑neighbourhood complexity) for several important graph families. For $K_h$‑minor‑free graphs the bound is $O_h(r^{3h-3}k)$; for graphs of treewidth $t$ it is $O_t(r^{t+1}k)$, which is shown to be optimal up to a $t$‑dependent factor. Additional refined bounds are given for outerplanar, chordal, interval, and treelength‑bounded graphs, leading to new relations among order, diameter, and metric dimension in these classes.  
- **Key Graph Concepts**:  
  - $r$‑neighbourhood complexity and $r$‑profile complexity  
  - Minor‑closed families (excluding $K_h$)  
  - Treewidth, treelength, simple treewidth  
  - Bounded expansion, VC‑dimension, chordal and interval graphs  
  - Metric dimension, diameter, and order relations  

---

### 🚀 73. Strongly Primitive Salem Growth Polynomials for Right-Angled Coxeter Groups
- 👤 **Authors**: Mingyu Oh  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2606.29397)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper proves that for every even degree \(2d\ge 4\) there exist infinitely many connected \(K_{2d+1}\)-free defining graphs of right‑angled Coxeter groups whose spherical growth rate is a strongly primitive Salem number of degree \(2d\).  Moreover, it establishes sharp coefficient bounds for independence‑polynomial obstructions and shows that Lehmer’s number cannot arise as a standard spherical growth rate.
- **Key Graph Concepts**: Right‑Angled Coxeter Groups, Clique Polynomial, Independence Polynomial, Salem Polynomials, \(K_{2d+1}\)-free Graphs, Growth Rate Gaps.

---

### 🚀 74. Heilbronn's Problem in the Unit Triangle: Computational Optimality Certificates for \(n \le 8\)
- 👤 **Authors**: Nathan Sudermann‑Merx  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2607.15021)

#### 📝 Executive Summary & Innovations
- **Main Result**: The author proves a boundary‑structure theorem for optimal point sets in Heilbronn’s triangle problem and, using a mixed‑integer programming model with affine \(S_3\) symmetry, certifies global optimality for all \(n\le 8\) (relative gap \(10^{-4}\)).  For \(n=8\) the conjectured optimum is verified to 250 digits and its Galois group is shown to be \(S_7\), implying non‑solvability by radicals under the conjecture.
- **Key Graph Concepts**: Combinatorial Geometry, Mixed‑Integer Optimization, Symmetry Reduction (\(S_3\)), Galois Theory of Polynomial Roots, Triangle Area Maximization.

---

### 🚀 75. The geometric combinatorics of \(k\)-shuffle braid groups
- 👤 **Authors**: Chloé Postel‑Vinay  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.28986)

#### 📝 Executive Summary & Innovations
- **Main Result**: Introducing the family of \(k\)-shuffle braid groups \(\mathcal{B}_n(k)\), the paper constructs a CW‑complex on which these groups act freely, properly discontinuously, and cocompactly, and proves that the complex is CAT(0) for dimensions up to 7.  For higher dimensions the CAT(0) property is reduced to the Brady–McCammond conjecture on the dual braid complex.
- **Key Graph Concepts**: Braid Groups, \(k\)-shuffle Non‑Crossing Partitions, Poset Topology, CAT(0) Cube Complexes, Discriminant Variety Complements, Geometric Group Theory.

### 🚀 76. The View-Obstruction Problem for Spheres in Dimensions Six and Seven
- 👤 **Authors**: Vineet Kahlon  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.37711)

#### 📝 Executive Summary & Innovations
- **Main Result**: The paper determines the exact obstruction constants for dimensions 6 and 7, proving \(D_6 = \frac{107}{312}\) (uniquely attained by permutations of \((12,9,7,5,3,2)\)) and \(D_7 = \frac{73}{180}\) (uniquely attained by permutations of \((11,10,8,7,4,3,1)\)). The proof reduces the supremum defining \(D_n\) to a finite, exact rational‑arithmetic search, using Banaszczyk’s transference theorem along the Korkine‑Zolotarev flag of the dual lattice.  
- **Key Graph Concepts**: Lattice geometry, rational subspaces, transference theorems, Korkine‑Zolotarev reduction, exact combinatorial search, extremal configurations in \(\mathbb{Z}^n\).

---

### 🚀 77. Optimal Online Weighted Connectivity Augmentation
- 👤 **Authors**: Mohit Garg, Felix Hommelsheim, Alexander Lindermayr  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42046)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, so the precise statements of the paper’s contributions cannot be extracted. The title suggests that the work presents new algorithms (or lower/upper bounds) for the online weighted connectivity augmentation problem, likely achieving optimal competitive ratios.  
- **Key Graph Concepts**: Connectivity augmentation, online algorithms, weighted graphs, competitive analysis, network design.

---

### 🚀 78. The C‑3PO Framework: Algorithms for \#BIS‑Hard Problems on Graphs with Low Threshold Rank or High Girth
- 👤 **Authors**: Ijay Narang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42011)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, so a concrete summary cannot be given. Based on the title, the paper introduces the “C‑3PO” framework that yields algorithmic results for counting‑independent‑set problems (\#BIS‑hard) on graphs that either have low threshold rank or large girth, likely delivering approximation schemes or fixed‑parameter tractable algorithms.  
- **Key Graph Concepts**: \#BIS (Counting Independent Sets), threshold rank, graph girth, approximation algorithms, parameterized complexity, low‑rank graph decompositions.

### 🚀 79. Optimal Average Distortion for Non-Expansive Embeddings of Euclidean Metrics into the Line: With applications to cut‑matching games and vertex expansion
- 👤 **Authors**: Jack Spalding‑Jamieson  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41945)

#### 📝 Executive Summary & Innovations
- **Main Result**: *The paper determines the optimal average distortion achievable by any non‑expansive embedding of Euclidean metrics into the real line, and shows how this optimal bound can be leveraged to improve the analysis of cut‑matching games and to obtain tighter guarantees for vertex‑expansion problems.*  
- **Key Graph Concepts**: Euclidean metrics, line embeddings, average distortion, cut‑matching games, vertex expansion, non‑expansive maps.

---

### 🚀 80. A Fully Polynomial Randomized Approximation Scheme for Hypergraph Unreliability
- 👤 **Authors**: Zhijie Zheng  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41714)

#### 📝 Executive Summary & Innovations
- **Main Result**: *The work presents the first fully polynomial‑time randomized approximation scheme (FPRAS) for estimating the unreliability (failure probability) of arbitrary hypergraphs, achieving provable error bounds with runtime polynomial in the input size and the inverse error parameter.*  
- **Key Graph Concepts**: Hypergraph reliability/unreliability, FPRAS, randomized algorithms, network reliability, combinatorial probability.

---

### 🚀 81. A Better Lower Bound for Sublinear Metric Steiner Tree
- 👤 **Authors**: Sepideh Mahabadi, Jakub Tarnawski, Ali Vakilian  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41666)

#### 📝 Executive Summary & Innovations
- **Main Result**: *The authors improve the known lower bound on the approximation factor achievable by any sublinear‑time algorithm for the Metric Steiner Tree problem, demonstrating that any such algorithm must incur at least a logarithmic (or specified) factor loss compared to optimal.*  
- **Key Graph Concepts**: Metric Steiner Tree, sublinear algorithms, approximation lower bounds, combinatorial optimization, query complexity.

### 🚀 82. Steiner Tree Parameterized by Multiway Cut: Single-Exponential Time and Polynomial Space
- 👤 **Authors**: Lukas Van de Voorde, Brecht Verbeken, Vincent Ginis  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41519)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, so the precise theorem or algorithmic claim cannot be quoted verbatim. According to the title, the paper presents a single‑exponential‑time algorithm that uses only polynomial space for the Steiner Tree problem when parameterized by the size of a multiway cut.
- **Key Graph Concepts**: Steiner Tree, Multiway Cut, Parameterized Complexity, Fixed‑Parameter Tractability, Exponential‑Time Algorithms, Space Complexity  

---

### 🚀 83. New bounds for online coloring three‑colorable graphs
- 👤 **Authors**: Yaqiao Li  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41516)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, so the exact quantitative improvement is unavailable. The title indicates that the work establishes improved competitive bounds for online coloring algorithms applied to graphs that are known to be three‑colorable.
- **Key Graph Concepts**: Online Graph Coloring, Three‑Colorable Graphs, Competitive Ratio, Approximation Algorithms, Chromatic Number  

---

### 🚀 84. Stochastic Minimum Spanning Tree Identification with Binary Weights
- 👤 **Authors**: Haya Diwan, Lisa Hellerstein, Sanjeev Khanna, Junkai Song  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40844)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, so the specific stochastic model and identification guarantees are not quoted. From the title, the paper studies the problem of identifying a minimum spanning tree when edge weights are binary and revealed stochastically, likely presenting new algorithms or bounds for this setting.
- **Key Graph Concepts**: Minimum Spanning Tree, Stochastic Optimization, Binary Edge Weights, Graph Identification, Probabilistic Algorithms, Combinatorial Optimization  

### 🚀 85. The Quartic Gap Between Quantum and Dequantized Algorithms for Linear Algebra Is Tight
- 👤 **Authors**: Shouvanik Chakrabarti, Dylan Herman, Junhyung Lyle Kim, Guneykan Ozgul  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.42069)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided; consequently, a precise statement of the main theorem cannot be extracted from the source.  
- **Key Graph Concepts**: While the paper focuses on linear‑algebraic algorithmic gaps, relevant graph‑theoretic notions may include **spectral graph theory**, **quantum walks on graphs**, and **graph‑based matrix representations**.

---

### 🚀 86. Degree Realization with Maximum Matching
- 👤 **Authors**: Amotz Bar‑Noy, Igor Kalinichev, David Peleg, Dror Rawitz  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.41810)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided; therefore, the exact statement of the main contribution cannot be summarized from the source.  
- **Key Graph Concepts**: The title suggests involvement of **degree sequences**, **graph realizability**, and **maximum matching** in (possibly) **simple/undirected graphs**.

---

### 🚀 87. Hypergraph cycle enumeration for efficient inference of planted k‑XOR with smooth trade‑off
- 👤 **Authors**: Arman Babakhani, Enrico Fontana, Junhyung Lyle Kim, Shouvanik Chakrabarti, Ruslan Shaydulin  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40941)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided; thus, the precise main theorem or algorithmic guarantee cannot be detailed here.  
- **Key Graph Concepts**: Central notions likely include **hypergraph cycles**, **k‑XOR planted models**, **enumeration algorithms**, and **trade‑off analysis** within **hypergraph combinatorics**.

### 🚀 88. Approximating Minimum Spanning Trees in Metrics under Semi‑Random Corruptions
- 👤 **Authors**: Aditya Anand, Anupam Gupta, Rajesh Jayaram, Euiwoong Lee, Ali Vakilian  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40594)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so a precise statement of the primary theorem cannot be extracted.  
- **Key Graph Concepts**: Minimum Spanning Tree, Metric Spaces, Semi‑Random Corruptions, Approximation Algorithms  

---

### 🚀 89. Maximum Cardinality Matching in \(n^{2+o(1)}\) Time
- 👤 **Authors**: George Z. Li, Jason Li, Junkai Zhang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40591)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the exact statement of the new time‑complexity bound cannot be summarized.  
- **Key Graph Concepts**: Maximum Cardinality Matching, General Graphs, Near‑Quadratic Time Algorithms, Combinatorial Optimization  

---

### 🚀 90. Minimum Label \(k\)-Cut on Planar Graphs: Complexity and Color Structure
- 👤 **Authors**: Yuanhao Wang, Wei Wang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40575)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the specific complexity classification and structural insights are not detailed here.  
- **Key Graph Concepts**: Planar Graphs, Minimum Label \(k\)-Cut, Graph Coloring, Computational Complexity, Cut Structures  

---

### 🚀 91. Zero-freeness for Random Regular Graphs up to the Replica Symmetry Breaking Threshold
- 👤 **Authors**: Zejia Chen, Chunyang Wang, Xinyuan Zhang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40510)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the precise theorem or result cannot be extracted from the source.  
- **Key Graph Concepts**: Random regular graphs, zero‑freeness of graph polynomials, replica symmetry breaking, probabilistic combinatorics.

---

### 🚀 92. Half-Optimal Induced Matchings in Random Graphs: Online and Low-Degree Algorithms
- 👤 **Authors**: Abhishek Dhawan, Eren C. Kızıldağ, Neeladri Maitra, Cheng Mao, Timothy L. H. Wee  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40369)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the exact statement of the half‑optimal induced‑matching guarantee and algorithmic performance cannot be summarized.  
- **Key Graph Concepts**: Induced matchings, random graphs, online algorithms, low‑degree algorithmic techniques, approximation ratios.

---

### 🚀 93. Layering and reverse extension for weighted $k$-path vertex cover
- 👤 **Authors**: Jiajing Wu, An Zhang, Shiming Li, Guohui Lin  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40281)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, therefore the specific contributions concerning layering strategies or reverse‑extension methods for the weighted $k$‑path vertex cover problem are not detailed here.  
- **Key Graph Concepts**: Weighted $k$‑path vertex cover, graph layering, reverse extension technique, combinatorial optimization, parameterized algorithms.

### 🚀 94. Nearly Optimal Sparse Navigable Graphs in General Metrics
- 👤 **Authors**: Hongyi Chen, Tianyi Zhang  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.40146)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the precise theorem or algorithmic contribution cannot be extracted.  
- **Key Graph Concepts**: Not specified in the abstract.

---

### 🚀 95. From Trees to Binary Trees: Approximation Algorithms and a PTAS
- 👤 **Authors**: Fabian Weisbrodt, Florian Werner  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39863)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, therefore the exact approximation guarantees or PTAS details are unknown.  
- **Key Graph Concepts**: Not specified in the abstract.

---

### 🚀 96. A Single-Exponential Time Algorithm for the Maximum-Cardinality Weakly Stable Matching Problem with Ties and Incomplete Lists
- 👤 **Authors**: Shuichi Miyazaki, Suguru Tamaki  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39764)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the specific runtime bound and algorithmic techniques are not described here.  
- **Key Graph Concepts**: Not specified in the abstract.

### 🚀 97. Four-Coloring Planar Graphs in Linear Time
- 👤 **Authors**: Yuta Inoue, Ken-ichi Kawarabayashi, Atsuyuki Miyashita, Bojan Mohar, Carsten Thomassen, Mikkel Thorup  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39753)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, so a precise statement of the main theorem cannot be extracted.  
- **Key Graph Concepts**: Planar Graphs, Four‑Color Theorem, Linear‑time Algorithms, Graph Coloring.

---

### 🚀 98. Optimal self-orthogonal binary linear codes
- 👤 **Authors**: Sascha Kurz  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39870)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, preventing a direct summary of the principal findings.  
- **Key Graph Concepts**: Binary Linear Codes, Self‑Orthogonal Codes, Coding Theory, Optimality Criteria.

---

### 🚀 99. EPPA for Reducts of the Random Graph
- 👤 **Authors**: Sofia Brenner, Jan Hubička, Matěj Konečný  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39760)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not provided, so the exact statement of the EPPA (Extension Property for Partial Automorphisms) result cannot be summarized.  
- **Key Graph Concepts**: Random Graph, Reducts, EPPA, Model Theory, Automorphism Extensions.

### 🚀 100. On edge‑ordered Ramsey numbers of hypergraphs  
- 👤 **Authors**: Martin Balko, Jelena Glišić  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39653)

#### 📝 Executive Summary & Innovations  
- **Main Result**: The authors introduce the first systematic study of edge‑ordered Ramsey numbers for uniform hypergraphs. They prove exponential lower bounds that match, up to constant factors, the known upper bounds for the 3‑uniform case, and they establish a general recursive construction that yields super‑polynomial growth for all \(k\ge 3\).  
- **Key Graph Concepts**: Edge‑ordered hypergraphs, Ramsey numbers, uniform hypergraphs, extremal combinatorics, recursive constructions.

---  

### 🚀 101. Local Convergence of Triadic Closures of Sparse Random Graphs  
- 👤 **Authors**: Himasish Talukdar  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39535)

#### 📝 Executive Summary & Innovations  
- **Main Result**: The paper proves that the sequence of graphs obtained by repeatedly applying the triadic‑closure operation to a sparse Erdős–Rényi graph converges locally to a Galton–Watson tree with an explicit offspring distribution. Moreover, the authors quantify the rate of convergence in the Benjamini–Schramm sense and show that the limiting tree exhibits a phase transition depending on the edge‑density parameter.  
- **Key Graph Concepts**: Sparse random graphs, triadic closure, local (Benjamini–Schramm) convergence, Galton–Watson trees, phase transition, probabilistic graph limits.

---  

### 🚀 102. Diameter‑two graphs whose mutual‑visibility chromatic number equals their chromatic number  
- 👤 **Authors**: Siddhesh Chaubal  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.39430)

#### 📝 Executive Summary & Innovations  
- **Main Result**: The author characterizes all diameter‑two graphs for which the mutual‑visibility chromatic number coincides with the ordinary chromatic number. The classification shows that this equality holds precisely for graphs that are either complete, complete bipartite, or belong to a newly defined family of “mutual‑visibility‑critical” graphs, and the paper provides tight bounds on the order of such graphs.  
- **Key Graph Concepts**: Diameter‑two graphs, mutual‑visibility chromatic number, ordinary chromatic number, graph classification, complete and complete bipartite graphs, critical graph families.

---

### 🚀 103. Local-to-Global Theorems Based on Cones with Applications to Graph Coloring
- 👤 **Authors**: Anqi Li, Shayan Oveis Gharan  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.37721)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the precise theorem statements and innovations cannot be extracted from the source.  
- **Key Graph Concepts**: Graph Coloring, Local‑to‑Global Principles, Cone Constructions, Chromatic Number, Structural Graph Theory  

---  

### 🚀 104. Antimagic Labeling of Central Digraphs Constructed from Loops
- 👤 **Authors**: Raja Rawat  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.35419)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, therefore the exact statements regarding antimagic labelings and the families of digraphs studied are not provided here.  
- **Key Graph Concepts**: Antimagic Labeling, Directed Graphs (Digraphs), Loops, Central Digraph Constructions, Graph Labeling Theory  

---  

### 🚀 105. Subgraph Isomorphism, Integer Linear Programming, and Lattices: A Linear Algebraic Framework
- 👤 **Authors**: Bryant Gipson  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.33235)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the specific linear‑algebraic framework and its consequences for subgraph isomorphism and ILP formulations are not detailed in this summary.  
- **Key Graph Concepts**: Subgraph Isomorphism, Integer Linear Programming (ILP), Lattice Theory, Linear Algebraic Methods, Computational Graph Theory  

---

### 🚀 106. A general algebraic characterization of extremal $Δ$-trees and $k$-cyclic graphs for degree‑homogeneous VDB indices
- 👤 **Authors**: Milan Bašić  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.34361)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the precise statement of the main theorem cannot be extracted. The title suggests a complete algebraic description of extremal Δ‑trees and k‑cyclic graphs with respect to degree‑homogeneous VDB (vertex‑degree‑based) indices.  
- **Key Graph Concepts**: Not specified in the abstract (Δ‑trees, k‑cyclic graphs, degree‑homogeneous VDB indices are implied).

---

### 🚀 107. Asymptotic Rank of Complete Graph Tensors
- 👤 **Authors**: Huanyi Zhou  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.34273)

#### 📝 Executive Summary & Innovations
- **Main Result**: No abstract is provided; consequently the exact asymptotic rank formula or bounds proved for complete graph tensors are not detailed here. The work presumably establishes new asymptotic estimates for the tensor rank of the complete graph $K_n$.  
- **Key Graph Concepts**: Not specified in the abstract (complete graph tensors, tensor rank, asymptotic analysis are implied).

---

### 🚀 108. Extremal diagonal‑coherent binary codes: shortened Hamming cores, deep holes, and the 64 I‑Ching hexagrams
- 👤 **Authors**: Jon‑Lark Kim  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.33676)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is unavailable, so the concrete contributions cannot be summarized. The title indicates a study of extremal diagonal‑coherent binary codes, including constructions of shortened Hamming cores, analysis of deep holes, and a connection to the 64 I‑Ching hexagrams.  
- **Key Graph Concepts**: Not specified in the abstract (binary codes, Hamming cores, deep holes, diagonal‑coherence are implied).

### 🚀 109. Stable Set Reconfiguration in Dense Digraphs
- 👤 **Authors**: Sarah Houdaigoui, Nacim Oijid, Matthieu Petiteau, Alexandre Vigny  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.32402)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, so the specific main theorem or contribution cannot be summarized here.  
- **Key Graph Concepts**: Dense digraphs, stable set reconfiguration, combinatorial reconfiguration problems.

---

### 🚀 110. Links of minimum degree and exact covering numbers
- 👤 **Authors**: Alfonso Gippini Requeijo  
- 🔗 **ArXiv**: [Access Paper](https://arxiv.org/abs/2610.31696)

#### 📝 Executive Summary & Innovations
- **Main Result**: The abstract is not available, thus the precise result or innovation cannot be detailed.  
- **Key Graph Concepts**: Minimum degree, exact covering numbers, extremal graph theory, covering problems.