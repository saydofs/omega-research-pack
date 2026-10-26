# Omega Interlevel Numbers

> **A mathematical exploration of numbers as unique hierarchical realizations rather than value-only objects.**

**Omega Interlevel Numbers** is an exploratory mathematical extension of **Omega-NR — The Universe That Never Repeats**.

The project asks a simple but radical question:

> If two numerical realizations display the same conventional value, must they be the same numerical object?

Omega-NR answers **no** at the level of realization identity.

So instead of treating a number only as

\[
N=v,
\]

this project investigates objects of the form

\[
\boxed{
N_\Omega=(V,\mathcal T,\Gamma,\beta,\Lambda)
}
\]

where:

- `V` — visible/surface value,
- `T` — ordered hierarchical structure,
- `Γ` — path/history,
- `β` — unique realization identity,
- `Λ` — local emergence/geometry data.

---

## Why this exists

Ordinary arithmetic is extraordinarily successful at describing **value**.

But many systems also care about:

- how a state was reached,
- how it branched,
- what internal structure exists below the visible state,
- whether two equal outputs have different histories,
- whether reconstruction of a form also reconstructs the original identity.

Omega Interlevel Numbers explores whether those questions can be encoded mathematically inside the number object itself.

---

## Zero and space in the broader Omega hypothesis

Omega-NR does not identify numerical zero with absolute non-existence.

The broader hypothesis treats space itself as material in some form:

\[
\boxed{\text{Space is a form of material existence.}}
\]

This physical/ontological claim is **not proved or developed in this mathematical paper**; it is reserved for separate work. Its immediate consequence here is simply that numerical zero and structural boundaries must not be interpreted as absolute nothingness.

---

## Core principle

Two realized numbers may have equal visible value:

\[
V(N_1)=V(N_2)=5,
\]

while remaining different realizations:

\[
\boxed{N_1\neq N_2.}
\]

A repeated visible `5` is therefore not assumed to recreate the previous `5` identity.

This is the **Omega Numerical Uniqueness Axiom** used by the framework.

---

## What “interlevel” means

A notation such as

```text
555555[777777777[450]82]639
```

is not intended as an exotic decimal expansion.

It represents an ordered hierarchy: numerical content can emerge at deeper levels, return upward, and continue.

The internal content is structurally anchored but not merely “owned” by the previous digit.

---

## Main mathematical objects

### 1. Depth projection

\[
\Pi_k(N)
\]

shows the structure only through depth \(k\).

\[
\Pi_j(\Pi_k(N))=\Pi_{\min(j,k)}(N).
\]

### 2. Depth profile

\[
H_N(z)=\sum_{k\ge0}L_kz^k.
\]

Useful as a coarse description, but not a complete identity fingerprint.

### 3. Exact structural signature

\[
S_\Omega(N)=\{(p_i,v_i,a_i,\ell_i)\}.
\]

For finite ordered hierarchies, this signature is reconstructive.

### 4. Local emergence law

For a node with \(b\) children:

\[
\boxed{c_e=\frac1{b+1}}.
\]

It follows from local conservation plus local symmetry among the \(b\) children and one retained parent-state channel.

### 5. Canonical structural mass

\[
M_\Omega(N)=
\sum_{v\in N}
\prod_{e\in P(v)}c_e.
\]

For full \(b\)-ary infinite branching:

\[
\boxed{M_\Omega=b+1}.
\]

For branching bounded by \(B\):

\[
\boxed{M_\Omega\le B+1}.
\]

So infinite depth does **not** necessarily imply infinite canonical mass.

### 6. Canonical geometry

Each parent interval is divided into \(b+1\) local channels.

A child receives

\[
W_{\text{child}}
=
\frac{W_{\text{parent}}}{b+1}.
\]

The same locally derived law controls influence and geometric contraction.

Along an infinite descent:

\[
W_k\le2^{-k}\to0,
\]

so the nested geometry converges to a unique limiting address.

---

## Omega Path Algebra

Finite structures can be represented by multisets of ordered root-to-leaf paths.

### Addition

\[
A\oplus_\Omega B
\]

is path-multiset union.

It is commutative and associative.

### Multiplication

\[
A\otimes_\Omega B
\]

concatenates every path of \(A\) with every path of \(B\).

It is associative and distributive, but generally:

\[
\boxed{
A\otimes_\Omega B\neq B\otimes_\Omega A.
}
\]

Order matters because path history matters.

### Structural subtraction

If \(B\) is present inside \(C=A\oplus_\Omega B\),

\[
C\ominus_\Omega B=A.
\]

This reconstructs structure, not historical identity.

### Left and right division

Because multiplication is noncommutative, left and right factorization are different.

A longest common prefix corresponds naturally to a shared initial history; a longest common suffix corresponds to a shared terminal history.

---

## Structure can return; identity cannot be replayed

A path can return to the same structural location:

\[
N_0\to N_1\to N_2\to N_1\to N_0.
\]

But Omega realization identity treats the revisits as new events:

\[
N_1^{(1)}\neq N_1^{(2)}.
\]

This yields the central statement:

> **Structure may be reconstructed; identity cannot be replayed.**

---

## Difference from fractions or ordinary decimals

A fraction such as

\[
\frac57
\]

represents a value.

Omega Interlevel Numbers are intended to carry:

\[
\boxed{
\text{value}
+
\text{hierarchy}
+
\text{path}
+
\text{geometry}
+
\text{identity}
+
\text{history}.
}
\]

The framework survives a key conceptual test: same-surface structures can produce different structural responses because their internal organizations differ.

That does **not yet** prove that this is a fundamentally new number system. It shows that the internal hierarchy can be operationally relevant rather than decorative metadata.

---

## Current status

This repository is a **preliminary research framework**, not a completed mathematical theory.

The current model has:

- formal definitions,
- finite reconstructive signatures,
- infinite path projections,
- a first-difference metric,
- a local emergence law,
- finite-mass results,
- a canonical geometric encoding,
- a noncommutative path algebra,
- computational stress tests,
- explicit limitations and rejected branches.

It does **not** yet claim:

- a new established branch of mathematics,
- complete novelty relative to all prior mathematics,
- a physical proof of Omega-NR,
- a unique or final geometry,
- proven practical superiority over existing representations.

---

## Research philosophy

This project is designed to be challenged.

If you find a limitation, counterexample, incomplete definition, or stronger formulation, constructive mathematical development is welcome.

Where possible, please accompany criticism with one of:

- a counterexample,
- a corrected definition,
- a stronger proof,
- an alternative model,
- a reproducible experiment.

The goal is not to protect the framework from criticism. The goal is to discover whether the underlying idea can survive rigorous mathematics.

---

## Repository map

```text
MANUSCRIPT.md
README.md
LICENSE_CODE.md
RIGHTS_AND_LICENSING.md
NOTICE.md
CONTRIBUTING.md
CITATION.cff
CHANGELOG.md
RESEARCH_STATUS.md
figures/
experiments/
```

---

## Relationship to Omega-NR

Original Omega-NR preprint:

**Mohamed Sayed — The Universe That Never Repeats: Omega-NR — Exact Physical Non-Repetition, Accumulated Change, and a Testable Quantum-Geometric Extension**

- Version DOI: `10.5281/zenodo.23624320`
- Concept DOI: `10.5281/zenodo.23624319`

---

## Citation

Until this extension receives its own DOI, cite the repository/package version and the author:

> Mohamed Sayed (2026). *Omega Interlevel Numbers: Hierarchical Numerical Identity, Path Algebra, and Canonical Geometry*. Exploratory research framework.

See `CITATION.cff`.

---

## License and rights

The project intentionally separates software licensing from manuscript rights.

- **Code and executable research scripts:** PolyForm Noncommercial 1.0.0.
- **Research manuscript, original explanatory text, and original figures:** Copyright © 2026 Mohamed Sayed. All rights reserved, subject to normal scholarly quotation, citation, and applicable legal exceptions.
- **Commercial use:** requires separate written permission/license from the copyright holder.

See `RIGHTS_AND_LICENSING.md` and `LICENSE_CODE.md`.

---

## Final note

This project begins from a deliberately simple idea:

> **The same visible numerical value need not mean the same numerical realization.**

Everything else — hierarchy, depth, path algebra, geometry, and history — is an attempt to determine what mathematics follows if that idea is taken seriously.

---

## Possible fields of use

Possible research/application domains include:

- hierarchical mathematics and structured number systems;
- history-dependent and non-Markovian systems;
- engineering and material-state histories;
- provenance and audit trails;
- identity-aware computation;
- integrity and cybersecurity research;
- hierarchical databases and knowledge representation;
- compression/generative representations;
- geometric visualization of structured information;
- industrial and scientific process traceability;
- AI/agent state-history representation;
- physics-inspired hierarchical state models.

These are **candidate fields for investigation**, not claims of proven superiority or validated commercial performance.

---

## Development and official-project policy

This project welcomes independent criticism, counterexamples, proofs, experiments, alternative formulations, and extensions.

However:

- a **substantive modification** proposed for adoption into the **official Omega framework** should be supported by proof, counterexample, formal derivation, reproducible computation, or other documented evidence;
- inclusion of such a modification in an official Omega release requires explicit project approval;
- independent extensions should be described as independent unless officially approved;
- commercial or revenue-generating use of covered software is not granted by the noncommercial code license and requires a separate written agreement;
- commercial reuse of copyrighted manuscript/figure material beyond applicable legal exceptions also requires permission.

This policy protects official-project provenance while leaving scientific criticism and independent mathematical research open.

See `RIGHTS_AND_LICENSING.md` and `CONTRIBUTING.md`.

