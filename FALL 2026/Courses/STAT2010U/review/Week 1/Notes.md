---
tags: [review, notes]
week: 1
dates: Sept 8–11, 2026
lectures: "Lecture 1 (Sept 10, §1.1–1.2), Lecture 2 (Sept 11, §1.2–1.3)"
source: Canvas — lec1_complete.pdf, lec2_complete.pdf (in ../../files)
---

# 📅 Week 1 — Data, Displays & First Look at Continuous Distributions

← [[Week 2 - Lectures 3-4]] | 🔗 [[Questions]]

> [!tip] The 3-sentence version
> Statistics = using a small **sample** to make inferences about a whole **population**. Once you have data, you describe it visually (histograms, stem-leaf plots) before doing any math on it. A **density function** is the continuous-data version of a histogram — the area under it *is* the probability.

---

## 🧩 Lecture 1 — §1.1 Populations, Samples & Types of Data

### Core vocabulary
| Term | Definition | Example |
|---|---|---|
| **Population** | set of ALL measurements/objects of interest | all adults 19+ in Oshawa |
| **Sample** | a subset of the population | 1000 surveyed voters |
| **Statistic** | a numerical summary from a *sample* | the 60% who said "yes" |
| **SRS** | sample where every member has equal chance of selection | random draw, not "grab the tallest people" |

> [!question] Why SRS specifically?
> A biased sample (e.g. measuring only basketball players for "average height") gives a biased statistic. SRS is the safeguard — it's what lets you trust that sample ≈ population.

### Data family tree

```
                    DATA
                     │
        ┌────────────┴────────────┐
    NUMERICAL                CATEGORICAL
   (quantitative)             (qualitative)
        │                          │
   ┌────┴────┐              ┌──────┴──────┐
CONTINUOUS  DISCRETE      ORDINAL      NON-ORDINAL
(length,    (# kids,     (letter      (car brand,
 weight)     # fish)      grades)      yes/no vote)
```

Also cross-cutting: **univariate** (1 variable) → **bivariate** (2) → **multivariate** (3+).

> [!example] Worked — classify the data
> **(a)** Voters classified Liberal / Reform / NDP / Other → **categorical, non-ordinal** (no natural order between party names)
> **(b)** Tomato plant height → **numerical, continuous**
> **(c)** Paint job rated excellent/good/fair/poor → **categorical, ordinal** (there's a clear rank)

---

## 📊 Lecture 1→2 — §1.2 Visual Displays for Univariate Data

### Frequency tables → histograms
Recipe:
1. Split the range into **class intervals**, e.g. `[50,60)` — square bracket = included, round = excluded
2. Count how many values land in each → **class frequency** fᵢ
3. Divide by n → **class relative frequency** fᵢ/n (these always sum to 1)
4. **Class midpoint** = (lower + upper)/2 → the "typical value" of that bin
5. **Class width (CW)** = upper − lower boundary

> [!example] Worked — 95 grades, 5 classes
> | Class | Frequency | Rel. Freq |
> |---|---|---|
> | [50,60) | 11 | .1158 |
> | [60,70) | 24 | .2526 |
> | [70,80) | 36 | .3789 |
> | [80,90) | 21 | .2211 |
> | [90,100) | 3 | .0316 |
>
> Bar heights = these numbers, bars sit above each class interval on the x-axis.
>
> ⚠️ Too few classes (e.g. one giant `[50,100)` bar) = "horrible display, tells us nothing." Class width choice controls how much detail survives.

### Shape vocabulary (the thing you'll be asked to *identify* constantly)

```
 LEFT-SKEWED          RIGHT-SKEWED           SYMMETRIC            BELL-SHAPED
   long tail            long tail          both sides          (special case
   on the LEFT          on the RIGHT       balance around      of symmetric)
                                            a center
      ▄█                    █▄                 ▄█▄                 ▄███▄
    ▄██                    ██▄               ▄█████▄            ▄███████▄
  ▄████                  ████▄              ▄███████▄         ▄███████████▄
 ██████                ██████               ▄▄▄▄▄▄▄▄▄         ▄▄▄▄▄▄▄▄▄▄▄▄▄
```
> [!warning] Common trap
> "Left-skewed" refers to where the **tail** is, not where the data piles up. Left-skewed data actually clusters on the *right*.

### Stem-and-leaf plot
Splits each number into **stem** (leading digits) | **leaf** (next single digit, truncated not rounded).

> [!example] Worked — SAT scores
> Data: 638, 574, 627, 621, 705, 690, 522, 612, 594, 581, 640, 653, 638, 760, 491
>
> ```
> Stem | Leaf
>   4  | 9
>   5  | 2 7 8 9
>   6  | 1 2 2 3 3 4 5 9
>   7  | 0 6
> ```
> Stem unit SU = 100, leaf unit LU = 10 → `6|3` means ≈ 630 (approximates 638, the 8 is truncated).
> **Increment** = SU ÷ #LCPS (lines-per-stem). Splitting each stem into 2 lines (e.g. 40–44 / 45–49) doubles detail — increment = 100/2 = 50.

---

## 🌊 Lecture 2 — §1.3 (start): Continuous Distributions

A **density function f(x)** is the continuous-world histogram. It must satisfy:

| Rule | Meaning |
|---|---|
| f(x) ≥ 0 | no negative probability |
| total area under curve = 1 | ∫ f(x) dx over all x = 1 |
| P(a ≤ x ≤ b) = area under curve from a to b | proportion of values between a and b |

> [!info] Continuity quirk
> Because x is continuous, **P(a ≤ x ≤ b) = P(a < x < b)** — a single point has zero width, so zero area, so zero probability. Endpoints don't matter here (they will later for discrete variables).

> [!example] Worked — Uniform distribution (cooling water temp)
> Temp increase ~ Uniform(10°C, 25°C) → f(x) = 1/15 on [10,25], flat rectangle.
> - P(x < 20) = ∫₁₀²⁰ (1/15) dx = 10/15 ≈ **0.667**
> - P(20 < x < 22) = 2/15 ≈ **0.133**
> - P(x ≥ 15) = 10/15 ≈ **0.667**
> - Median (50th %ile): solve ∫₁₀ᵐ (1/15) dx = 0.5 → **m = 17.5**
> - 10th percentile: solve ∫₁₀ᵃ (1/15) dx = 0.10 → **a = 11.5**

> [!example] Worked — shot-put example (non-uniform)
> f(x) = A(4 − x²) on (−2, 2). Solve ∫₋₂² A(4−x²) dx = 1 → **A = 3/32**.
> - P(x < −1) ≈ **0.156**
> - P(x > 0.75) ≈ **0.232** ← flagged in lecture as "exercise to try at home" — redo this one yourself, don't just trust the number.

---

## 🎯 Why this matters
- Mobius Assignment 1 (due Mon Sept 21) covers Lectures 1–4 — everything above is directly testable.
- Term Test 1 (Oct 1) covers Wk1–4.

## ✅ Status
- [x] Confirmed lecture content from Canvas (lec1_complete.pdf, lec2_complete.pdf)
- [ ] Redo the shot-put P(x > 0.75) integral by hand, no peeking
- [ ] Work through [[Questions]] for Week 1
