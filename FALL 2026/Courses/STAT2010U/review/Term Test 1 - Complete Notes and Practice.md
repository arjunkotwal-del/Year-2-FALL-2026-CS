---
tags: [review, exam-prep, notes]
test: Term Test 1 (Oct 1, 2026)
format: "Notes → Solved Example → Variation Question → Step-by-Step Solution, per topic"
---

# 📘 Term Test 1 — Complete Notes & Practice

← [[Exam Review - Term Test 1]]

> [!danger] Test snapshot
> Lectures 1–6 (§1.1–1.4, 1.6, 2.1–2.3). 4 questions + bonus, handwritten, pencil, no MC, 80 min. Formula sheet + tables provided — [[Exam Review - Term Test 1#📄 Confirmed Formula Sheet|see confirmed formula sheet]].

Every topic below follows the same structure: **Notes** (the concept) → **Solved Example** (fully worked, every step shown) → **Variation Question** (you attempt this one on your own first) → **Step-by-Step Solution** (check yourself after).

---

## 1️⃣ Probability Density Functions — Validity & Unknown Constants

### 📝 Notes
A function f(x) is a valid density function only if:
1. **f(x) ≥ 0** everywhere on its domain
2. **∫f(x)dx over the whole domain = 1**

If there's an unknown constant (k, A, c...), solve for it using rule #2: integrate, set equal to 1, solve algebraically.

### ✅ Solved Example
**f(x) = kx² for 0 < x < 3, and 0 elsewhere. Find k.**

Step 1: Check f(x)≥0 — since x>0 and k will be positive, kx² ≥ 0 on this domain. ✓

Step 2: Set the integral equal to 1:
∫₀³ kx² dx = 1
k[x³/3] from 0 to 3 = 1
k(27/3 − 0) = 1
9k = 1
**k = 1/9**

### 🔄 Variation Question
f(x) = k(4−x) for 0 < x < 4, and 0 elsewhere. Find k.

### 🔍 Step-by-Step Solution
∫₀⁴ k(4−x) dx = 1
k[4x − x²/2] from 0 to 4 = 1
k[(16 − 8) − 0] = 1
k(8) = 1
**k = 1/8**

---

## 2️⃣ Mean of a Probability Density Function

### 📝 Notes
**μ = ∫ x·f(x) dx** over the domain. Different from finding a probability — you multiply by x before integrating.
Sanity check: the mean should always fall somewhere *inside* the domain.

### ✅ Solved Example
**Using f(x) = (1/9)x² for 0 < x < 3 from above, find the mean.**

μ = ∫₀³ x·(1/9)x² dx = (1/9)∫₀³ x³ dx
= (1/9)[x⁴/4] from 0 to 3
= (1/9)(81/4 − 0)
= (1/9)(20.25)
= **2.25**

Sanity check: 2.25 falls inside (0,3) ✓

### 🔄 Variation Question
Using f(x) = (1/8)(4−x) for 0 < x < 4 from above, find the mean.

### 🔍 Step-by-Step Solution
μ = ∫₀⁴ x·(1/8)(4−x) dx = (1/8)∫₀⁴ (4x−x²) dx
= (1/8)[2x² − x³/3] from 0 to 4
= (1/8)[(32 − 64/3) − 0]
= (1/8)(32 − 21.333)
= (1/8)(10.667)
= **1.333**

Sanity check: 1.333 falls inside (0,4) ✓ — makes sense it's below the midpoint (2), since this density is higher near x=0 and tapers to 0 at x=4 (left-heavy → pulls the mean lower).

---

## 3️⃣ Median / Percentiles of a PDF

### 📝 Notes
Solve **∫(lower bound to m) f(x) dx = target proportion** for m. Median uses 0.5; a general percentile uses that percentile as a decimal (e.g. 10th percentile = 0.10).

### ✅ Solved Example
**f(x) = 1/15 for 10 < x < 25 (uniform). Find the median.**

∫₁₀^m (1/15) dx = 0.5
(1/15)(m−10) = 0.5
m − 10 = 7.5
**m = 17.5**

### 🔄 Variation Question
f(x) = 2x for 0 < x < 1. Find the 25th percentile (Q1).

### 🔍 Step-by-Step Solution
∫₀^Q1 2x dx = 0.25
[x²] from 0 to Q1 = 0.25
Q1² = 0.25
**Q1 = 0.5**

---

## 4️⃣ Stem-and-Leaf Plots, Skew, Increment

### 📝 Notes
Stem = leading digit(s), leaf = next digit (truncated, not rounded). SU/LU from place value. **Increment = SU/#LCPS** (lines per stem). Skew: long tail direction names the skew (right-skewed = tail extends right, values cluster left).

### ✅ Solved Example
**Data: 41, 45, 52, 58, 59, 63, 65, 67, 68, 71, 73. Build a one-leaf-category-per-stem plot, find the increment, and describe the skew.**

```
Stem | Leaf
 4   | 1 5
 5   | 2 8 9
 6   | 3 5 7 8
 7   | 1 3
```
SU=10, #LCPS=1 → **Increment = 10**

Counts: 2, 3, 4, 2 — builds up gradually (2→3→4) then drops sharply (4→2) → **left-skewed** (gradual buildup on the low end, shorter tail on the high end after the peak).

### 🔄 Variation Question
Data: 12, 15, 18, 61, 65, 68, 71, 74, 78, 79, 82. Build a stem-leaf plot, find increment, describe skew.

### 🔍 Step-by-Step Solution
```
Stem | Leaf
 1   | 2 5 8
 6   | 1 5 8
 7   | 1 4 8 9
 8   | 2
```
SU=10, #LCPS=1 → **Increment = 10**

Counts: 3, 3, 4, 1 — one small cluster low (1,2,5,8), then a gap, then most data clustered high (61-82) with a long thin low-end tail → **right-skewed** (long tail toward the low values, most data clustered on the high/right end).

---

## 5️⃣ Raw Data: Mean, Variance, SD (calculator) + Median

### 📝 Notes
- **x̄** (sample mean), **s** (sample SD), **s²** (sample variance) — via calculator univariate/1-var stat mode. Never do these by hand for anything beyond a tiny dataset.
- **Median — NEVER use your calculator.** Order data. n odd → position (n+1)/2. n even → average of positions n/2 and (n/2)+1.

### ✅ Solved Example
**Data (ordered): 12, 15, 18, 21, 24, 27, 30 (n=7). Find x̄ and the median.**

x̄ = (12+15+18+21+24+27+30)/7 = 147/7 = **21**

Median: n=7 (odd) → position (7+1)/2 = 4th value = **21**

### 🔄 Variation Question
Data (ordered): 5, 9, 14, 20, 26, 33 (n=6). Find x̄ and the median.

### 🔍 Step-by-Step Solution
x̄ = (5+9+14+20+26+33)/6 = 107/6 ≈ **17.83**

Median: n=6 (even) → average of positions 3 and 4 → (14+20)/2 = **17**

---

## 6️⃣ Quartiles, IQR, Boxplots, Outliers

### 📝 Notes
Same median rule, applied twice: order data, split into lower/upper halves (include the median in both halves if n is odd), then **Q1 = median of lower half**, **Q3 = median of upper half**.
**IQR = Q3−Q1**. **Mild outlier**: beyond Q1−1.5(IQR) or Q3+1.5(IQR). **Extreme outlier**: beyond Q1−3(IQR) or Q3+3(IQR).

### ✅ Solved Example
**Ordered data (n=10): 5, 7, 8, 9, 10, 11, 12, 13, 14, 45. Find Q1, Q3, IQR, and classify any outliers.**

n=10 (even) → lower half (first 5): 5,7,8,9,10 → Q1 = median of this (n=5, odd, position 3) = **8**
Upper half (last 5): 11,12,13,14,45 → Q3 = median of this (position 3) = **13**

IQR = 13−8 = **5**

Mild bounds: 8−1.5(5)=0.5, 13+1.5(5)=20.5
Extreme bounds: 8−3(5)=−7, 13+3(5)=28

Check 45: beyond 28 (extreme bound) → **45 is an extreme outlier**

### 🔄 Variation Question
Ordered data (n=11): 3, 6, 7, 9, 11, **13**, 15, 16, 18, 20, 50. Find Q1, Q3, IQR, and classify any outliers.

### 🔍 Step-by-Step Solution
n=11 (odd) → median = position (11+1)/2=6th value = 13. Since n is odd, include this median in BOTH halves:
Lower half: 3,6,7,9,11,13 (n=6) → Q1 = avg of positions 3&4 = (7+9)/2 = **8**
Upper half: 13,15,16,18,20,50 (n=6) → Q3 = avg of positions 3&4 = (16+18)/2 = **17**

IQR = 17−8 = **9**

Mild bounds: 8−1.5(9)=−5.5, 17+1.5(9)=30.5
Extreme bounds: 8−3(9)=−19, 17+3(9)=44

Check 50: beyond 44 (extreme bound) → **50 is an extreme outlier**

---

## 7️⃣ Binomial Distribution

### 📝 Notes
Checklist: **fixed n, independence, constant π** (never announced — you detect it). Formula: **P(x)=(n choose x)π^x(1−π)^(n−x)**. Mean=nπ, Variance=nπ(1−π). Discrete → P(x<k)≠P(x≤k). Table only works for n∈{5,10,15,20,25} + listed π. Complement trick: P(X≥1)=1−P(X=0).

### ✅ Solved Example
**A factory finds 15% of bolts are defective. A sample of 10 bolts is checked. Find P(X=2), and the mean/variance of X.**

Checklist: n=10 (fixed), π=0.15 (constant), independence (assumed) → binomial ✓

P(X=2) = (10 choose 2)(0.15)²(0.85)⁸ = 45 × 0.0225 × 0.2725 ≈ **0.2759**

μ = nπ = 10(0.15) = **1.5**
σ² = nπ(1−π) = 10(0.15)(0.85) = **1.275**

### 🔄 Variation Question
A survey finds 25% of students bike to campus. A sample of 8 students is selected. Find P(X=3), and the mean/variance of X.

### 🔍 Step-by-Step Solution
n=8, π=0.25 → binomial ✓

P(X=3) = (8 choose 3)(0.25)³(0.75)⁵ = 56 × 0.015625 × 0.2373 ≈ **0.2076**

μ = nπ = 8(0.25) = **2**
σ² = nπ(1−π) = 8(0.25)(0.75) = **1.5**

---

## 8️⃣ Exponential Distribution

### 📝 Notes
f(x)=λe^(−λx), x>0. **P(x>c)=e^(−λc)**, **P(x≤c)=1−e^(−λc)**, **mean=1/λ**. Always right-skewed.

### ✅ Solved Example
**Wait times follow an exponential distribution with λ=0.4. Find P(x>3) and the mean.**

P(x>3) = e^(−0.4×3) = e^(−1.2) ≈ **0.301**
Mean = 1/λ = 1/0.4 = **2.5**

### 🔄 Variation Question
Time between failures follows an exponential distribution with a mean of 6 hours. Find P(x<4).

### 🔍 Step-by-Step Solution
mean=6 → λ=1/6≈0.1667

P(x<4) = 1−e^(−0.1667×4) = 1−e^(−0.6667) ≈ 1−0.5134 ≈ **0.4866**

---

## 9️⃣ Normal Distribution

### 📝 Notes
**z = (x−μ)/σ**, then read Table I as left-tail area P(Z≤z). Symmetry: P(Z≤−a)=P(Z≥a). Table I covers both negative and positive z directly — check before using the "1 minus" trick.

### ✅ Solved Example
**X ~ N(μ=60, σ=8). Find P(x<50).**

z = (50−60)/8 = −1.25

Look up Table I directly at z=−1.25 (row −1.2, column .05): **P(Z≤−1.25) ≈ 0.1056**

### 🔄 Variation Question
X ~ N(μ=100, σ=15). Find P(x>115).

### 🔍 Step-by-Step Solution
z = (115−100)/15 = 1.0

P(Z>1.0) = 1 − P(Z≤1.0) = 1 − 0.8413 = **0.1587**

---

## ✅ Final Status Check
All 9 core question types confirmed and drilled. Before test day:
- [ ] Redo every "Variation Question" above cold (cover the solution, time yourself)
- [ ] Confirm your calculator's exact button sequence for x̄/s/s² one more time
- [ ] Review [[Mock Test 1]] and [[Mock Test 2]] under full timed conditions if you haven't already
- [ ] Sleep — this matters more than one more hour of review at this point
