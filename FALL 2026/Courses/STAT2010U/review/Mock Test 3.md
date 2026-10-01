---
tags: [review, exam-prep, mock-test]
based_on: Term Test 1 structure — harder variations, Lectures 1-6 scope only
---

# 📝 Mock Term Test 3 (Harder)

← [[Exam Review - Term Test 1]] | [[Mock Test 1]] | [[Mock Test 2]]

> [!danger] Test conditions
> 80 minutes, handwritten, pencil, physical calculator, formula sheet only. This one leans into wording traps and reverse lookups — read every question twice before starting.

---

## Question 1 — Probability Density Function

A continuous random variable X has density function:

f(x) = k·x⁻⁴ for x > 1, and 0 otherwise

**(a)** Find k. [5 marks]

**(b)** Find the value that separates the **lowest 20%** of the distribution from the rest. [4 marks]

**(c)** Find the mean of X. [4 marks]

---

## Question 2 — Raw Dataset: Stem-Leaf (5 leaf categories), Increment, Median, Calculator Stats

Weekly sales figures (in thousands of dollars) for 20 stores:

```
0.31  0.33  0.38  0.39  0.42  0.44  0.45  0.47  0.48  0.49
0.51  0.53  0.55  0.58  0.62  0.64  0.67  0.71  0.78  0.79
```

**(a)** Construct a stem-and-leaf plot using **5 leaf categories per stem**, with leaf unit = tenths digit. [4 marks]

**(b)** Find the increment. [2 marks]

**(c)** Find the median from your plot. [2 marks]

**(d)** Using your calculator, find x̄ and s. [2 marks]

---

## Question 3 — Raw Dataset: Quartiles and Boxplot (odd n)

Ordered data (n=15): 12, 14, 15, 18, 19, 22, 23, **25**, 27, 29, 31, 33, 40, 44, 58

**(a)** Find the median, and explain why it's included in both halves when splitting the data. [3 marks]

**(b)** Find Q1 and Q3. [4 marks]

**(c)** Find the IQR, and determine if there are any mild or extreme outliers. [5 marks]

---

## Question 4 — Distributions (with wording traps)

**(a)** A survey shows that 85% of drivers wear seatbelts. A random sample of 12 drivers is observed. Let X = number who do **NOT** wear a seatbelt.

State the distribution of X and its parameters (careful — read what X is actually counting). Find P(X = 3). [5 marks]

**(b)** A manufacturing process has a failure rate such that the time between failures is exponentially distributed with λ = 0.05 (per hour). Find the probability that more than 30 hours pass without a failure, AND find the mean time between failures. [4 marks]

**(c)** IQ scores are normally distributed with μ=100, σ=15. Find the score that separates the **top 5%** from the rest. [4 marks]

---

## 🎁 Bonus Question

f(x) = 4x³ for 0 < x < 1, and 0 otherwise.

Find the value that separates the smallest 90% from the largest 10%. [3 bonus marks]

---
---

# 🔑 Answer Key

## Question 1
**(a)** ∫₁^∞ kx⁻⁴ dx = 1. Replace ∞ with w, take limit:
k[x⁻³/(−3)] from 1 to w = k(−1/(3w³) + 1/3)
As w→∞: −1/(3w³)→0, so k/3 = 1 → **k = 3**

**(b)** "Lowest 20%" means P(X<c)=0.20 — this is the **20th percentile**.
∫₁^c 3x⁻⁴ dx = 0.20
[−x⁻³] from 1 to c = 0.20
1 − 1/c³ = 0.20 → 1/c³ = 0.80 → c³ = 1.25 → **c ≈ 1.0772**

**(c)** μ = ∫₁^∞ x·3x⁻⁴ dx = ∫₁^∞ 3x⁻³ dx
= lim(w→∞) [3x⁻²/(−2)] from 1 to w = lim [−3/(2w²) + 3/2] = **3/2 = 1.5**

## Question 2
**(a)** All values are 0.xx → stem = 0 always. 5 categories split 0-9 into: (0-1),(2-3),(4-5),(6-7),(8-9)

Leaves (tenths digit) for each value: 3,3,3,3,4,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7

```
Stem | Leaf
 0   | (none, 0-1)
 0   | 3 3 3 3
 0   | 4 4 4 4 4 4
 0   | 5 5 5 5
 0   | 6 6 6 7 7 7
```
Count check: 0+4+6+4+6=20 ✓

**(b)** SU = 1 (LU=0.1, so SU=LU×10=1). #LCPS=5. **INCR = 1/5 = 0.2**

**(c)** n=20 (even) → average of 10th & 11th ordered values. From the original ordered list: 10th=0.49, 11th=0.51 → median = (0.49+0.51)/2 = **0.50**

**(d)** x̄ = sum/20 = 10.54/20 = **0.527**. Find s on your calculator — verify against this mean as a check.

## Question 3
**(a)** n=15 (odd) → median = position (15+1)/2 = 8th value = **25**. It's included in both halves because with an odd count, the middle value can't be cleanly split between two equal halves — the convention is to let both halves share it so each half still has a well-defined median of its own.

**(b)** Lower half (positions 1-8, includes median): 12,14,15,18,19,22,23,25 (n=8, even) → Q1 = avg of 4th&5th = (18+19)/2 = **18.5**
Upper half (positions 8-15, includes median): 25,27,29,31,33,40,44,58 (n=8, even) → Q3 = avg of 4th&5th = (31+33)/2 = **32**

**(c)** IQR = 32−18.5 = **13.5**
Mild bounds: 18.5−1.5(13.5)=−1.75, 32+1.5(13.5)=52.25
Extreme bounds: 18.5−3(13.5)=−22, 32+3(13.5)=72.5
Check 58: beyond mild bound (52.25) but within extreme bound (72.5) → **58 is a mild outlier**. No other values qualify.

## Question 4
**(a)** Careful: X counts drivers who do **NOT** wear a seatbelt — so "success" (what X counts) is NOT wearing a seatbelt, with probability 1−0.85=0.15, not 0.85.
X ~ Binomial(n=12, π=0.15)
P(X=3) = (12 choose 3)(0.15)³(0.85)⁹ = 220 × 0.003375 × 0.2316 ≈ **0.1721**

**(b)** P(x>30) = e^(−0.05×30) = e^(−1.5) ≈ **0.2231**
Mean = 1/λ = 1/0.05 = **20 hours**

**(c)** "Top 5%" means P(X>c)=0.05, equivalently P(X≤c)=0.95 (95th percentile).
z for 0.95 ≈ **1.645** (from Table I reverse lookup)
c = μ + zσ = 100 + 1.645(15) = 100 + 24.675 = **124.675**

## Bonus
∫₀^c 4x³ dx = 0.90
[x⁴] from 0 to c = 0.90 → c⁴ = 0.90 → **c ≈ 0.9740**
