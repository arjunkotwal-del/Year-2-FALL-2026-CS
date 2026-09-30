---
tags: [review, notes]
week: 3
lecture: 6
date: Sept 25, 2026
source: Canvas lec6_complete.pdf (§2.3, "More Detailed Summary Quantities")
---

# 📅 Lecture 6 — Quartiles, IQR, Boxplots & Outliers

← [[Notes]] | [[../Exam Review - Term Test 1]]

> [!tip] The 3-sentence version
> Quartiles cut ordered data into four equal chunks — Q1 is the "median of the lower half," Q3 is the "median of the upper half," found using the exact same odd/even position rule as an ordinary median, just applied recursively to each half. For continuous distributions, Q1 and Q3 are found the same way the median was (solve an integral equal to a target proportion — 0.25 and 0.75 instead of 0.5). Boxplots package the five-number summary (min, Q1, median, Q3, max) into one picture, and IQR-based rules (1.5×IQR mild, 3×IQR extreme) flag outliers.

---

## 📏 Quartiles for Raw Data

**Definition**: Order the data. Split into a lower half and an upper half.
- If **n is odd**, include the median in *both* halves.
- If **n is even**, split cleanly (no shared value).

Then:
- **Q1 = median of the lower half**
- **Q3 = median of the upper half**
- **IQR = Q3 − Q1**

> [!tip] Same median rule, just applied twice
> Finding Q1/Q3 is literally "find the median" — just run the odd/even median rule on each half instead of the whole dataset.

> [!example] Worked — n=11 (odd)
> Ordered: 4.4, 16.4, 22.2, 30, 33.1, **36.6**, 40.4, 66.7, 73.7, 81.5, 109.9
>
> Median (n=11, odd): position (11+1)/2 = 6th → **36.6**
>
> Lower half (includes the median, n=6): 4.4, 16.4, 22.2, 30, 33.1, 36.6
> Upper half (includes the median, n=6): 36.6, 40.4, 66.7, 73.7, 81.5, 109.9
>
> Each half has n=6 (even) → Q1/Q3 = average of the 3rd and 4th values within that half:
> **Q1** = (22.2+30)/2 = **26.1**
> **Q3** = (66.7+73.7)/2 = **70.2**
> **IQR** = 70.2 − 26.1 = **44.1**

> [!example] Worked — n=30 (even)
> Median = average of 15th & 16th values = (196+197)/2 = **196.5**
>
> Lower sample = first 15 values (n=15, odd) → Q1 = (15+1)/2 = 8th value of that half = **191**
> Upper sample = last 15 values (n=15, odd) → Q3 = 8th value of that half = **204**
> **IQR** = 204 − 191 = **13**

---

## 🌊 Quartiles for Continuous Distributions

Same logic as finding a median (∫f(x)dx = 0.5), just with different target proportions:

- **Q1**: solve ∫(lower bound to Q1) f(x) dx = **0.25**
- **Q3**: solve ∫(lower bound to Q3) f(x) dx = **0.75**
- Equivalently, using upper-tail integrals: ∫(Q1 to ∞) f(x)dx = 0.75, ∫(Q3 to ∞) f(x)dx = 0.25

> [!info] Why 25%/75%?
> Quartiles cut the distribution into quarters: 25% below Q1, 25% between Q1 and median, 25% between median and Q3, 25% above Q3.

> [!example] Worked — Exponential, λ=0.1 (arrival times)
> f(x) = 0.1e^(−0.1x)
>
> **Median**: solve −e^(−0.1m) + 1 = 0.5 → e^(−0.1m) = 0.5 → m = ln(2)/0.1 ≈ **6.93**
> **Q3**: solve −e^(−0.1Q3) + 1 = 0.75 → e^(−0.1Q3) = 0.25 → Q3 = ln(4)/0.1 ≈ **13.86**
> **Q1**: solve −e^(−0.1Q1) + 1 = 0.25 → e^(−0.1Q1) = 0.75 → Q1 = ln(1/0.75)/0.1 ≈ **2.88**
>
> **Expected value (mean)** = 1/λ = 1/0.1 = **10 min** (confirms formula sheet: exponential mean = 1/λ)
>
> Note: Q3 is farther from the median than Q1 is — because the exponential distribution is **right-skewed**.

> [!example] Worked — Standard Normal
> Symmetric about μ=0, so:
> **Median = μ = 0**
> **Q1**: solve P(Z ≤ Q1) = 0.25 → reverse-lookup Table I → **Q1 ≈ −0.675**
> **Q3**: by symmetry, **Q3 = +0.675**
> **IQR** = 0.675 − (−0.675) = **1.35**

---

## 📦 Boxplots & Outliers

**Five-number summary**: smallest value, Q1, median, Q3, largest value — this is what a boxplot displays.

**Purpose**: visualize where data clusters and spot outliers (same goal as a histogram/stem-leaf, different picture).

### Outlier rules (from formula sheet)
| Type | Rule |
|---|---|
| **Mild outlier** | beyond Q1 − 1.5(IQR) or Q3 + 1.5(IQR) |
| **Extreme outlier** | beyond Q1 − 3(IQR) or Q3 + 3(IQR) |

```
extreme    mild                              mild    extreme
  *         *    ┌─────┬─────┐                *        *
  |         |    │ Q1  │ Q3  │                |        |
──┴─────────┴────┴──┬──┴─────┴────────────────┴────────┴──→
Q1−3IQR  Q1−1.5IQR  Q1  x̃   Q3        Q3+1.5IQR    Q3+3IQR
```

> [!example] Worked — n=30 dataset (continuing from above)
> Q1=191, Q3=204, IQR=13
> Mild bounds: 191−1.5(13)=**171.5** and 204+1.5(13)=**223.5**
> Extreme bounds: 191−3(13)=**152** and 204+3(13)=**243**
>
> Checking the actual data (146...247):
> - **Mild outliers**: 165, 171, 232 (each beyond the mild bound but not the extreme bound)
> - **Extreme outliers**: 146, 247 (beyond the extreme bound)
>
> Shape note: median (196.5) sits slightly closer to Q1 (191) than to Q3 (204) → **slight right skew** (more data gathered on the left, tapering off to the right).

---

## 🎯 Why this matters
- This is **exactly** Term Test 1's Question 3 ("raw dataset → median/quartiles") — now fully confirmed, no more guessing.
- Also closes a piece of Question 4 (normal distribution) — standard normal quartiles via reverse Table I lookup.

## ✅ Status
- [x] Quartile method for raw data (odd/even, recursive median rule) — confirmed
- [x] Quartile method for continuous distributions (∫=0.25, ∫=0.75) — confirmed
- [x] Boxplot five-number summary + outlier rules — confirmed
- [ ] Practice a full boxplot sketch from raw data start to finish (order → median → Q1/Q3 → IQR → outlier bounds → classify outliers → sketch)
- [ ] Drill: which is farther from the median for a right-skewed distribution, Q1 or Q3? (Q3 — memorize this pattern, it signals skew direction)
