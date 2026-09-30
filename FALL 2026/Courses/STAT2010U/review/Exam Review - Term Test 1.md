---
tags: [review, exam-prep]
test: Term Test 1
date: Thursday Oct 1, 2026, 11:10am–12:30pm
location: SIRC3110
source: instructor's Canvas announcement + live Lecture 5 (Sept 24) commentary on test structure + actual Term Test 1 formula sheet (provided by student, Sept 25)
---

# 🎯 Term Test 1 — Master Exam Review

← [[STAT2010U - Statistics and Probability]]

> [!danger] Logistics — read this first
> - **Scope**: Ch 1 (§1.1–1.4, 1.6) + Ch 2 (§2.1–2.3) = **Lectures 1–6 inclusive** (today's Lecture 5 + tomorrow's Lecture 6 both count)
> - **Format**: 4 questions, short + long answer, **+1 bonus**. **No multiple choice.**
> - **Handwritten, in pencil** — no laptops
> - Printed **double-sided** — check the back of every page
> - Formula sheet + table booklet **provided at the test** (also pre-posted in Canvas under "Term Test/Exam Resources" — go practice with the real one)
> - **80 minutes**, do not show up late
> - **"Therefore" statements**: only required when a question explicitly asks for one — don't waste time writing them for every answer (correction from Lecture 5)

> [!tip] The professor told you exactly what's coming
> She described the 4 long-answer question types directly in Lecture 5. This file is organized around exactly those 4 buckets — treat this as your literal test blueprint, not a guess.

---

## 📄 Confirmed Formula Sheet (the actual one provided at the test)

> [!success] This is the real formula sheet — everything below is authoritative, not reconstructed
> You are NOT given a blank cheat sheet — this exact sheet is provided. Study these forms so you recognize them instantly, don't waste test time re-deriving.

**Distributions:**
| | Mean | Variance |
|---|---|---|
| Discrete | μₓ = Σx·p(x) | σ² = Σ(x−μ)²·p(x) |
| Continuous | μₓ = ∫x·f(x)dx | σ² = ∫(x−μ)²·f(x)dx |
| Continuous median | ∫f(x)dx = 0.5 (integrate from domain start to m) | — |
| Exponential | **μ = 1/λ** ⭐ (not derived in lecture, just use it) | f(x)=λe^(−λx); P(x>c)=e^(−λc) |
| Normal | μₓ = μ | σ² = σ² |
| Standard Normal | z = (x−μ)/σ | f(z) = (1/√2π)e^(−z²/2) |
| Binomial | μ = nπ | σ² = nπ(1−π) |

Binomial pmf: p(x) = [n!/(x!(n−x)!)] · π^x · (1−π)^(n−x) = (n choose x)·π^x·(1−π)^(n−x), x=0,1,...,n

**Raw Data (Univariate):**
- Sample mean: x̄ = (x₁+x₂+...+xₙ)/n
- Sample variance (computational shortcut form): s² = [Σx² − (Σx)²/n] / (n−1) — faster than the "subtract mean from each point" definition, same result
- **IQR = Q3 − Q1**
- **Mild outliers**: below Q1−1.5(IQR) or above Q3+1.5(IQR)
- **Extreme outliers**: below Q1−3(IQR) or above Q3+3(IQR)

> [!warning] Quartile calculation method itself is still not confirmed
> The formula sheet gives you what to *do* with Q1/Q3 (IQR, outlier bounds) but not *how to calculate* Q1/Q3 from raw data — that's still pending Lecture 6 content. Don't assume a method until confirmed.

---

## 🧭 The 4 question types (straight from the professor)

| #   | Topic                                 | What it tests                                                                                             |
| --- | ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 1   | **Probability density functions**     | prove valid density (integrate=1), find the mean, percentiles, median — "anything I've shown you on PDFs" |
| 2   | **Raw dataset → stem-leaf/histogram** | increment, skew direction, sample mean/variance/std dev (by calculator)                                   |
| 3   | **Raw dataset → median/quartiles**    | median, Q1/Q3, likely boxplot-adjacent                                                                    |
| 4   | **Named distributions**               | normal, binomial, exponential — mixed small parts                                                         |
| 🎁  | Bonus                                 | unknown                                                                                                   |

---

## 1️⃣ Probability Density Functions

> [!info] Status
> Fully covered already — see [[Week 1/Notes]] and [[Week 2/Notes]] for the worked examples (uniform, shot-put, exponential, k·x²). This section just consolidates the **question types** she flagged.

### (a) Prove f(x) is a valid density
Two checks, always:
1. **f(x) ≥ 0** on the whole domain
2. **∫ f(x) dx over the full domain = 1**

If a constant is unknown (k, A, c...), this is also how you solve for it — set the integral equal to 1 and solve.

> [!example] Pattern
> f(x) = kx² on [0,2] → ∫₀² kx² dx = 1 → k = 3/8 (see [[Week 2/Notes]] for full steps)

### (b) Find the mean of a PDF ⭐ NEW — explicitly flagged as exam content
> [!danger] Not yet in your notes — this is new
> **Mean of a continuous random variable**: μ = ∫ x·f(x) dx (integrated over the whole domain)
>
> This is different from finding a probability — you're integrating **x times f(x)**, not just f(x) alone.

> [!example] Worked pattern (using the uniform density from Week 1)
> f(x) = 1/15 on [10,25]. Find the mean.
> μ = ∫₁₀²⁵ x·(1/15) dx = (1/15)·[x²/2] from 10 to 25
> = (1/15)·(625/2 − 100/2) = (1/15)·(262.5) = **17.5**
>
> Sanity check: for a uniform distribution, the mean should just be the midpoint of the interval → (10+25)/2 = 17.5 ✅ matches.

### (c) Percentiles / median of a PDF
Already covered — solve ∫(lower bound to m) f(x) dx = target proportion (0.5 for median, 0.10 for 10th percentile, etc.) for the unknown bound. See [[Week 1/Notes]] uniform distribution example.

### ✅ Practice checklist
- [ ] Prove-valid-density questions (solve for unknown constant)
- [ ] Find the mean: μ = ∫x·f(x)dx — **new, drill this specifically**
- [ ] Find a percentile/median by solving an integral = target proportion
- [ ] Exponential-specific shortcuts (P(x>c)=e^(−λc)) — still fair game if she gives an exponential PDF

---

## 2️⃣ Raw Dataset → Stem-Leaf/Histogram, Skew, Mean/SD by Calculator

> [!info] Status — fully confirmed now
> Stem-leaf/histogram/skew: [[Week 1/Notes]]. Sample mean/variance/std dev + calculator method: confirmed from Lecture 5 — see [[Week 3/Notes]] and [[Week 3/Transcript - Lecture 5]].

### What's confirmed
- Stem-and-leaf plot construction (stem/leaf/SU/LU/increment) — [[Week 1/Notes]]
- Histogram construction, class frequency/relative frequency — [[Week 1/Notes]]
- Skew shape identification (left/right/symmetric) — [[Week 1/Notes]]
- **Sample mean x̄** — by calculator (univariate/1-variable mode, enter data, read x̄) — [[Week 3/Notes]]
- **Sample variance s² / std dev s** — by calculator (get `s` or `Sₓ`, square it for s² if no separate button) — [[Week 3/Notes]]

> [!danger] Learn your specific calculator NOW
> Steps differ by brand/model (TI: 2nd→Data→1-variable; Casio/Sharp: cycle Mode). The professor's own advice: look up your exact calculator model on ChatGPT for step-by-step instructions if you don't have the manual. **Do this before test day** — don't learn it cold under time pressure.

### ✅ Practice checklist
- [ ] Build a stem-and-leaf plot from raw data, state SU/LU/increment
- [ ] Identify skew from a plot or histogram
- [ ] **Confirm your own calculator's exact button sequence** for univariate mean/SD — test it on a known small dataset (e.g. 22,2,12,16,18 → mean should be 14)
- [ ] Compute sample mean and std dev by calculator until it's fast — guaranteed test question

---

## 3️⃣ Raw Dataset → Median / Quartiles

> [!info] Status — fully confirmed now
> Median, quartiles, IQR, boxplots, and outliers all confirmed from the actual Lecture 6 PDF (§2.3). See [[Week 3/Lecture 6 - Quartiles and Boxplots]] for full worked examples.

### Median (raw data)
- **Do NOT use your calculator** — every brand handles it differently/unreliably. Always compute by hand.
- Order the data first (on the test, data will already be pre-sorted for you)
- **n odd**: median = value at position (n+1)/2
- **n even**: median = average of values at positions n/2 and (n/2)+1
- Notation: sample median = **x̃** (x-tilde/squiggly), not x-bar

### Quartiles (raw data) — same median rule, applied twice
1. Split ordered data into lower half / upper half (if n odd, include the median in **both** halves)
2. **Q1 = median of the lower half**, **Q3 = median of the upper half** — apply the same odd/even position rule to each half
3. **IQR = Q3 − Q1**

### Quartiles (continuous distribution) — same as median, different target
- **Q1**: solve ∫(lower bound to Q1) f(x)dx = **0.25**
- **Q3**: solve ∫(lower bound to Q3) f(x)dx = **0.75**
- (Median was the same setup with target 0.5)

### Boxplots & outliers (confirmed, formula sheet + lecture match)
- Five-number summary: min, Q1, median, Q3, max
- **Mild outlier**: beyond Q1−1.5(IQR) or Q3+1.5(IQR)
- **Extreme outlier**: beyond Q1−3(IQR) or Q3+3(IQR)
- Skew tell: if the median sits closer to Q1 than Q3, that's **right skew** (and vice versa for left skew)

### ✅ Practice checklist
- [ ] Full raw-data quartile problem: order → median → split halves → Q1/Q3 → IQR → outlier bounds → classify outliers
- [ ] Continuous distribution quartile problem (e.g. exponential or a custom f(x)) — solve two integrals (0.25 and 0.75 targets)
- [ ] Standard normal quartiles via reverse Table I lookup (Q1≈−0.675, Q3≈+0.675 by symmetry)

---

## 4️⃣ Named Distributions — Normal, Binomial, Exponential

| Distribution | Status | Where |
|---|---|---|
| **Exponential** | ✅ confirmed, taught | [[Week 2/Notes]], [[Week 2/Transcript - Lecture 3]] |
| **Normal** | ⚠️ reconstructed only, not lecture-verified | [[Week 2/Notes]] (flagged unconfirmed section) |
| **Binomial** | ✅ confirmed, taught | [[Week 3/Notes]], [[Week 3/Transcript - Lecture 5]] |

> [!tip] What you now have solid
> - **Exponential**: P(x>c)=e^(−λc), P(x≤c)=1−e^(−λc), improper integral proof, λ as height parameter
> - **Binomial**: P(x)=(n choose x)π^x(1−π)^(n−x); recognize via fixed-n + independence + constant-π checklist; μ=nπ, σ²=nπ(1−π); table only valid for n∈{5,10,15,20,25} + listed π values; complement trick P(X≥1)=1−P(X=0)
> - **Normal (still needs verification)**: z=(x−μ)/σ, Table I bookkeeping, continuity correction

> [!danger] Binomial's real trap: recognizing it, not calculating it
> Unlike normal/exponential, a binomial question **never announces itself**. Check all 3: fixed n, independence (often implied not stated), constant π. Also watch for questions that give you the *complement* probability (e.g. "probability of losing") when they're actually asking about the opposite outcome — your π must match what the question is actually asking about.

### ✅ Practice checklist
- [ ] Exponential shortcut drills — solid, keep sharp
- [ ] Normal z-score drills — solid from practice, but still verify against real Lecture 4 content if it surfaces
- [ ] Binomial: practice identifying success/failure correctly (the lottery win/lose trap), practice both hand-calculation and table lookup, drill the complement trick for large n

---

## 🎁 Bonus Question
Unknown content — professor didn't preview it. Don't spend prep time guessing; focus on the 4 confirmed question types first.

---

## 📋 Master status board

| Question | Confidence | What's needed |
|---|---|---|
| 1. PDF (valid density, mean, percentile) | 🟢 strong | drill μ=∫x·f(x)dx specifically — least practiced piece |
| 2. Stem-leaf/histogram + calculator mean/SD | 🟢 strong | confirmed — just need to lock in your own calculator's button sequence |
| 3. Median/quartiles | 🟢 strong | fully confirmed (Lecture 6) — practice full boxplot problems end-to-end |
| 4. Normal/Binomial/Exponential | 🟢 strong | exponential + binomial fully confirmed; normal confirmed via formula sheet + Lecture 6 quartile example (z=(x−μ)/σ, Table I) |

**All 4 question types are now confirmed against real lecture content and the actual formula sheet — no more guessed sections.**

## ✅ Immediate next steps
- [ ] Drill μ = ∫x·f(x)dx until automatic (new, high-yield)
- [ ] **Learn your specific calculator's univariate stat mode today** — practice entering data, pulling x̄ and s, on a known dataset (22,2,12,16,18 → mean=14)
- [ ] Drill binomial recognition (fixed n + independence + constant π) and the success/failure reading trap
- [ ] Practice one full raw-data boxplot problem start to finish (order → median → Q1/Q3 → IQR → outlier classification)
- [ ] Practice one continuous-distribution quartile problem (two integrals, targets 0.25 and 0.75)
- [ ] Do a final mixed mock quiz across all 4 question types before test day
