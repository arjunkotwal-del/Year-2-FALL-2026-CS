---
tags: [review, notes]
week: 1
dates: Sept 8–11, 2026
lectures: "Lecture 1 (Sept 10, §1.1–1.2), Lecture 2 (Sept 11, §1.2–1.3)"
source: Canvas — lec1_complete.pdf, lec2_complete.pdf (in ../../files)
---

# Week 1 Notes

← [[Week 2 - Lectures 3-4]]

## Lecture 1 — §1.1 Populations, Samples, and Processes
- **Statistic**: any numerical summary measure based on data from a sample.
- **Statistics** = the collection, description, and interpretation of data.
- **Population**: set of all measurements/objects of interest in a study.
- **Sample**: a subset of the population.
- **Simple random sample (SRS)**: every member of the population has an equal chance of being chosen. Why use one? More accurate representation of the population → more accurate statistic.
- Data types:
  - **Univariate**: one variable (e.g. battery lifetime)
  - **Bivariate**: two variables (e.g. height & weight per player)
  - **Multivariate**: 3+ variables
  - **Numerical (quantitative)**: continuous (any precision, e.g. length) vs discrete (isolated points, e.g. # of children)
  - **Categorical (qualitative)**: ordinal (natural order, e.g. letter grade) vs non-ordinal (no order, e.g. car brand)
- **Variable**: characteristic of a person/thing assignable a number or category (notation: x, y or x₁, x₂...)

## Lecture 1 → 2 — §1.2 Visual Displays for Univariate Data
- **Frequency distribution**: divide data into class intervals, count observations per class (class frequency fᵢ) and proportion per class (relative frequency fᵢ/n).
- **Class midpoint** = (lower boundary + upper boundary)/2
- **Class width (CW)** = upper class boundary − lower class boundary (usually constant across a histogram)
- Bracket convention: `[50,60)` includes 50, excludes 60 — 60 belongs to the next class.
- **Histogram**: bar height = class (relative) frequency. Class width choice changes the "look" — too few classes = no detail, too many = choppy.
- **Categorical histogram**: bars centered on each category, height = count/frequency.
- Sample shapes: **left-skewed** (long left tail, values cluster right), **right-skewed** (long right tail, values cluster left), **symmetric**, **bell-shaped** (a subset of symmetric — not all symmetric shapes are bell-shaped).
- **Stem-and-leaf plot**: split each value into a stem (leading digit(s)) and leaf (next digit, truncated — not rounded). Stem unit (SU) and leaf unit (LU) come from place value. "Final plot" = leaves sorted ascending within each stem.
  - One-leaf-category-per-stem (LCPS) vs two-leaf-category-per-stem (splits each stem into two ranges, e.g. 40–44 / 45–49).
  - **Increment** = SU / #LCPS (distance from one plotted line to the next).

## Lecture 2 — §1.3 intro: Continuous Distributions
- **Density function f(x)** describes a continuous variable's population/process distribution. Must satisfy:
  1. f(x) ≥ 0 (probabilities can't be negative)
  2. ∫₋∞^∞ f(x) dx = 1 (total area = 1)
  3. P(a ≤ x ≤ b) = ∫ₐᵇ f(x) dx (area under curve between a and b)
- Because it's continuous, **P(a ≤ x ≤ b) = P(a < x < b)** — no area sits above a single point.
- **Uniform distribution**: f(x) = 1/(b−a) for a < x < b, 0 otherwise. Constant-height rectangle.
- Worked in lecture: sea-water cooling temp increase ~ Uniform(10°C, 25°C):
  - f(x) = 1/15 on [10,25]
  - P(x < 20) = ∫₁₀²⁰ (1/15)dx = 10/15 ≈ 0.667
  - P(20 < x < 22) = 2/15 ≈ 0.133
  - P(x ≥ 15) = ∫₁₅²⁵(1/15)dx = 10/15 ≈ 0.667
  - Median: solve ∫₁₀ᵐ(1/15)dx = 0.5 → m = 17.5
  - 10th percentile: solve ∫₁₀ᵃ(1/15)dx = 0.10 → a = 11.5
- Second worked example: shot-put density f(x) = A(4−x²) on (−2,2). Solve for A using ∫f(x)dx=1 → A = 3/32.
  - P(x < −1) ≈ 0.156, P(x > 0.75) ≈ 0.232 (left as take-home exercise in lecture)

## Why this matters
- Mobius Assignment 1 (due Mon Sept 21) covers Lectures 1–4 — this is half of it.
- Term Test 1 (Oct 1) covers Wk1–4.

## Status
- [x] Confirmed lecture content from Canvas (lec1_complete.pdf, lec2_complete.pdf)
- [ ] Rework the shot-put "exercise to try at home" (P(x > 0.75)) by hand
- [ ] Do [[Questions]] for Week 1
