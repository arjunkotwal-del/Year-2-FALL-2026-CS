---
tags: [review, notes]
week: 2
dates: Sept 14–18, 2026
lectures: "Lecture 3 (Sept 17, §1.3) — confirmed from live transcript; Lecture 4 (Sept 18, §1.4) — still unconfirmed"
source: "Lecture 3: [[Transcript - Lecture 3]] (live class, Sept 17). Lecture 4: reconstructed from hw_week2_solutions.pdf + topic outline — NOT yet verified against the actual lecture."
---
 v  
# 📅 Week 2 — Exponential Distribution, Discrete Mass Functions & the Normal Distribution

← [[Week 2 - Lectures 3-4]] | 🔗 [[Questions]] | 🎙️ [[Transcript - Lecture 3]]

> [!tip] The 3-sentence version
> Lecture 3 gives you the **exponential distribution** (waiting-time problems) with a shortcut formula you should never have to integrate for again, then flips to **discrete mass functions**, where — unlike continuous — strict vs. non-strict inequalities actually change your answer. Lecture 4 (not yet verified) is expected to cover the **normal distribution** and z-scores. The throughline all week: "does a single point carry probability weight?" — no for continuous, yes for discrete.

---

## 🌊 Lecture 3 — §1.3 cont'd: Exponential Distribution + Intro to Discrete

> [!info] Source note
> This section is confirmed directly from the live lecture transcript — see [[Transcript - Lecture 3]] for the full worked dialogue if anything below is unclear.

### Closing out general continuous PDFs
- If you already found one shaded region (say, a "less than" proportion), the opposite region is just **1 − that answer** — because total area under any density curve = 1. Re-integrating from scratch is allowed but wastes time (no marks lost either way).
- Always end application answers with a plain-English **"therefore" statement** — required on tests.
- Inequality wording (tested explicitly, marks lost for wrong sign):

| Phrase | Inequality |
|---|---|
| **at least** k | x ≥ k |
| **at most** k | x ≤ k |
| **less than** k | x < k |
| **greater than** k | x > k |

> [!warning] Continuous-only fact
> For a continuous distribution, **P(x < k) = P(x ≤ k)** — a single point has zero width, so zero area, so it never changes the answer. This flips once discrete distributions start (see below) — don't carry this assumption forward.

### The Exponential Distribution
The second named continuous distribution this course covers (Normal is the other, still incoming). Classic **average waiting-time** model.

```
   f(x)
    │╲
  λ │ ╲
    │  ╲___
    │      ╲______
    │             ╲___________
    └──────────────────────────── x
    0
```
Always right-skewed, starts at height λ, decays toward (never touching) 0.

- **f(x) = λe^(−λx)**, x > 0
- **λ ("lambda")** is a **parameter** — a constant controlling the graph's shape. For exponential specifically, λ sets the **starting height**. (Every named distribution has parameters — Normal's are μ and σ, covered next lecture.)
- Regardless of λ, **total area is always 1** (valid density).
- Domain runs to +∞ → a "greater than" proportion is an **improper integral**.

> [!example] Proving the shortcut (improper integral, done properly)
> Want P(x > c) = ∫꜀^∞ λe^(−λx) dx.
> **Don't plug ∞ directly into a bound — that's "bad math."** Instead:
> 1. Replace the upper bound with a variable w, take the limit as w→∞
> 2. Integrate: λe^(−λx) integrates to −e^(−λx) (the λ cancels against −λ, the derivative of the exponent)
> 3. Sub bounds (w then c), *then* take the limit
> 4. As w→∞: e^(−λw) → 0 (exponential decay). The c-term has no w, stays constant.
> 5. Double negative flips sign → **final answer: e^(−λc)**

> [!tip] Formula-sheet shortcuts — use these, don't re-derive every time (confirmed against actual Term Test 1 formula sheet)
> - **P(x > c) = e^(−λc)**
> - **P(x ≤ c) = 1 − e^(−λc)**
> - **P(a < x < b) = e^(−λa) − e^(−λb)** (bigger "greater-than" region minus the excess)
> - **Mean: μ = 1/λ** ⭐ confirmed from formula sheet, not derived in lecture — just apply it
>
> On tests, the professor will **always explicitly say** "exponential distribution" in the question — you're never expected to detect it. Generic PDFs (not named) must still be integrated directly — no shortcut available.

> [!example] Worked — exponential mean
> λ = 0.5 → μ = 1/0.5 = **2**

> [!example] Worked — response time, λ = 0.2
> - **At least 10 sec**: P(x≥10) = e^(−0.2×10) = e^(−2) ≈ **0.1353** → "≈14% of response times are at least 10 seconds"
> - **Less than 5 sec**: P(x<5) = 1 − e^(−0.2×5) = 1 − e^(−1) ≈ **0.6321** → "≈63% are less than 5 seconds"
> - **At most 5 sec**: identical to "less than 5" for a continuous distribution → **0.6321** (see warning above)
> - **Between 5 and 10 sec**: P(x>5) − P(x>10) = e^(−0.2×5) − e^(−0.2×10) ≈ **0.2325**
>   - "Between" without "inclusive/exclusive" doesn't matter here — continuous distributions don't care about endpoints.

### Finding an unknown constant k in a density
Same recipe every time: **integrate over the whole domain, set equal to 1, solve.**

> [!example] Worked — pop quiz question
> f(x) = kx² on [0,2], 0 elsewhere. Find k.
> ∫₀² kx² dx = 1 → kx³/3 from 0 to 2 → k(8/3) = 1 → **k = 0.375**

---

## 🎲 Lecture 3 (cont'd): Discrete Distributions — Mass Functions

- Keyword: **"mass function"** (continuous = "density function"). Also check what the random variable X can actually be — decimals allowed → continuous; integer counts only (accidents, sheep, etc.) → discrete.
- Two validity properties (parallel to continuous, but **no calculus**):
  1. No negative probabilities
  2. **Σ P(x) = 1** (sum instead of integral)

> [!danger] The big contrast to memorize
> For discrete/mass functions, **P(x < k) ≠ P(x ≤ k)** — the opposite of continuous! A single value now carries real probability weight (isolated points on a number line, not a smooth curve).

### Worked example — traffic accidents (mass function table)

| x (accidents) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| P(x) | 0.10 | 0.20 | 0.45 | 0.15 | ? | ? |

- **At most 3** (x ≤ 3): P(0)+P(1)+P(2)+P(3) = .10+.20+.45+.15 = **0.90**
- **Fewer than 3** (x < 3): P(0)+P(1)+P(2) = .10+.20+.45 = **0.75** ← different from "at most 3"! (Would've been identical if this were continuous.)
- **At least 4** (x ≥ 4): individual P(4), P(5) unknown — instead use **1 − P(x≤3) = 1 − 0.90 = 0.10** (can't split the 0.10 between x=4 and x=5 without more info)
- **Between 1 and 3**: *must* specify inclusive/exclusive for discrete (unlike continuous, where it never mattered)
  - Inclusive: P(1)+P(2)+P(3) = .20+.45+.15 = **0.80**
  - Exclusive (strictly between): just P(2) = **0.45**

### Quick-reference: continuous vs discrete

| | Continuous (density) | Discrete (mass) |
|---|---|---|
| Validity check | ∫f(x)dx = 1 | Σ P(x) = 1 |
| P(x<k) vs P(x≤k) | same | **different** |
| "Between a,b" inclusive/exclusive | doesn't matter | **must specify** |
| Keyword | "probability density function" | "mass function" |

---

## 🔔 Lecture 4 — §1.4: The Normal Distribution *(⚠️ not yet verified against the actual lecture)*

> [!warning] Unconfirmed section
> Canvas hasn't given access to the Lecture 4 completed PDF and no transcript exists for it yet. Everything below is reconstructed from homework solutions (§1.4) + the course outline. Treat it as a preview, not ground truth — swap in the real lecture content once you have it (a transcript like [[Transcript - Lecture 3]] would settle it fast).

- **Standard normal (z)**: mean 0, sd 1. Table I gives left-tail area P(z ≤ a).
- **Nonstandard normal**: x ~ N(μ,σ) → standardize via **z = (x − μ) / σ**, then read Table I.
- z-table bookkeeping: P(z>a)=1−P(z≤a); P(a≤z≤b)=P(z≤b)−P(z≤a); symmetry P(z≤−a)=P(z≥a); reverse lookups need interpolation.
- **Continuity correction**: discrete x approximated by a normal curve → shift bounds by ±0.5 before standardizing (e.g. P(20≤x≤40) uses z-bounds from 19.5 and 40.5).

Full detail in the earlier draft of these notes — kept as a placeholder pending confirmation.

---

## 🎯 Why this matters
- Mobius Assignment 1 (due Mon Sept 21) covers Lectures 1–4 — exponential shortcuts, mass function inequalities, and (probably) z-scores all testable.
- Term Test 1 (Oct 1) covers Wk1–4.

## ✅ Status
- [x] Lecture 3 confirmed from live transcript — see [[Transcript - Lecture 3]]
- [ ] Get Lecture 4 content confirmed (PDF or transcript) — normal distribution section is still a reconstruction
- [ ] Drill the exponential shortcut formulas until automatic: P(x>c)=e^(−λc), P(x≤c)=1−e^(−λc)
- [ ] Practice discrete "at most/fewer than/at least/between" problems — the < vs ≤ distinction is the #1 place to lose marks this week
- [ ] Work through [[Questions]] for Week 2
