---
tags: [review, notes]
week: 2
dates: Sept 14–18, 2026
lectures: "Lecture 3 (Sept 17, §1.3), Lecture 4 (Sept 18, §1.4)"
source: Canvas — lecture complete PDFs not accessible (permissions); content inferred from hw_week2_solutions.pdf (Sec 1.3 & 1.4 problems) + course topic outline
---

# Week 2 Notes

← [[Week 2 - Lectures 3-4]]

> ⚠️ Canvas denied direct access to the Lecture 3/4 "complete PDF" files (permissions error — only skeletal PDFs and homework are downloadable so far). The notes below are reconstructed from the homework solutions (which show worked problems for §1.3–1.4) and the course topic outline, **not the lecture PDFs themselves**. Fill in gaps once you can grab the actual completed lecture PDFs from Canvas.

## Lecture 3 — §1.3 cont'd: More Continuous Distributions
Building on Lecture 2's uniform distribution, more density function shapes appear here:
- **Triangular density**: e.g. f(x) piecewise-linear, peaking in the middle (like f(x) = .4 − .04x type functions in HW). Area = area of a triangle = ½(base)(height).
- **Exponential density**: f(x) = λe^(−λx) for x > 0. Key shortcut proven in HW: **P(x > c) = e^(−λc)** for any exponential — memorize this, it saves you from re-integrating every time.
- General technique across all of these: set up ∫f(x)dx = 1 to solve for an unknown constant, then integrate over sub-intervals to get proportions/probabilities — same method as Lecture 2's uniform example.
- Median / percentile problems: set the definite integral equal to the target proportion (e.g. 0.5 for median, 0.10 for 10th percentile) and solve for the boundary.

## Lecture 4 — §1.4: The Normal Distribution
- **Standard normal (z) distribution**: mean 0, standard deviation 1. Probabilities read off **Table I** (z-table) as left-tail areas: Proportion(z ≤ z₀).
- Common manipulations (from HW):
  - P(z > a) = 1 − P(z ≤ a)
  - P(a ≤ z ≤ b) = P(z ≤ b) − P(z ≤ a)
  - Symmetry: P(z ≤ −a) = P(z ≥ a), and P(z ≤ −a or z ≥ a) = 2·P(z ≤ −a)
  - Finding a z-value from a given tail proportion = reverse table lookup (find the z whose table value matches), using **linear interpolation** when the exact probability isn't in the table.
- **Nonstandard (general) normal**: x ~ N(μ, σ). Convert to standard normal via
  **z = (x − μ) / σ**
  then read off Table I as usual. This is the single most important formula from this week.
- **Continuity correction** (discrete x approximated by a normal curve): when x is a *discrete* variable being approximated by a continuous normal, shift boundaries by 0.5 before standardizing — e.g. P(20 ≤ x ≤ 40) → use z-bounds from 19.5 and 40.5, not 20 and 40.

## Why this matters
- Mobius Assignment 1 (due Mon Sept 21) covers Lectures 1–4 — z-scores and normal distribution problems will be on it.
- Term Test 1 (Oct 1) covers Wk1–4 including normal distributions.

## Status
- [ ] Get the actual Lecture 3/4 completed PDFs from Canvas to verify/replace this reconstruction
- [ ] Practice z-table lookups both directions (probability → z, and z → probability)
- [ ] Do [[Questions]] for Week 2
