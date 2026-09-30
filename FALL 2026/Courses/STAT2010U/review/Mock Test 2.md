---
tags: [review, exam-prep, mock-test]
based_on: Term Test 1 structure (Lectures 1-6 confirmed scope only)
---

# 📝 Mock Term Test 2

← [[Exam Review - Term Test 1]] | [[Mock Test 1]]

> [!danger] Test conditions
> - Timer: **80 minutes**
> - Handwritten, pencil, physical calculator only
> - Use your [[Exam Review - Term Test 1#📄 Confirmed Formula Sheet|confirmed formula sheet]] — nothing else
> - Only write "therefore" statements where explicitly asked
> - No peeking at the answer key until done or time's up

---

## Question 1 — Probability Density Function (improper integral + percentile)

A continuous random variable X has density function:

f(x) = k/x³ for x > 1, and 0 otherwise

**(a)** Find the value of k that makes this a valid density function. [5 marks]

**(b)** Find the value c that separates the smallest 30% of the distribution from the largest 70%. [4 marks]

---

## Question 2 — Raw Dataset: Stem-Leaf, Increment, Median, Calculator Stats, Binomial

The following data represents the lifetimes (in hours) of 22 incandescent lamps from a forced life test (already ordered lowest to highest, as it will be on the real test):

```
702   765   785   905   919   920   923   929   938   948   950
958   970   977   978   1123  1156  1170  1195  1196  1198  1217
```

**(a)** Using your calculator, find the sample mean (x̄) and sample variance (s²). [3 marks]

**(b)** Construct a stem-and-leaf plot with **2 leaf categories per stem**, using the **tens digit** as the leaf unit. [4 marks]

**(c)** Calculate the increment of your plot, and find the median lifetime. [3 marks]

**(d)** If n=27 and π=1/7 for a binomial random variable X, find P(X > 0) using the complement shortcut. [2 marks]

---

## Question 3 — Raw Dataset: Quartiles and Boxplot

Using the same 22 lifetime values from Question 2 (ordered): 702, 765, 785, 905, 919, 920, 923, 929, 938, 948, 950, 958, 970, 977, 978, 1123, 1156, 1170, 1195, 1196, 1198, 1217

**(a)** Find Q1 and Q3. [4 marks]

**(b)** Find the IQR. [1 mark]

**(c)** Determine the mild and extreme outlier boundaries. Are there any outliers? [4 marks]

---

## Question 4 — Distributions (Binomial, Exponential, Normal)

**(a)** A shipping company finds that 12% of packages arrive damaged. A random sample of 15 packages is inspected. Let X = number of damaged packages.

State the distribution of X and its parameters, then find its mean and variance. [3 marks]

**(b)** Using part (a), find P(X = 2). [3 marks]

**(c)** The time between earthquakes in a region follows an exponential distribution with a mean of 8 years. Find the probability the next earthquake occurs within 5 years. [3 marks]

**(d)** Bags of flour are filled with a mean weight of 5.2 kg and standard deviation 0.15 kg, normally distributed. Find the probability a randomly selected bag weighs less than 5.0 kg. [4 marks]

---

## 🎁 Bonus Question

A density function is given by f(x) = 3x² for 0 < x < 1, and 0 otherwise.

Find the value that separates the smallest 40% of the distribution from the largest 60%. [3 bonus marks]

---
---

# 🔑 Answer Key

## Question 1
**(a)** ∫₁^∞ (k/x³) dx = 1 → use the improper integral technique (replace ∞ with w, take limit):
∫₁^w kx⁻³ dx = k[−x⁻²/2] from 1 to w = k(−1/(2w²) + 1/2)
As w→∞: −1/(2w²) → 0, so this becomes k/2 = 1 → **k = 2**

**(b)** Solve ∫₁^c (2/x³) dx = 0.30:
[−x⁻²] from 1 to c = 1 − 1/c² = 0.30 → 1/c² = 0.70 → c² = 1/0.70 ≈ 1.4286 → **c ≈ 1.195**

## Question 2
**(a)** Σx = 21822, n=22, x̄ = 21822/22 ≈ **991.91**
s² ≈ **22171.13** (verify on your own calculator — this is exactly what Q2a is testing)

**(b)**
```
Stem | Leaf (tens digit, leaf unit)
 7   | 0
 7   | 6 8
 9   | 0 1 2 2 2 3 4
 9   | 5 5 7 7 7
 11  | 2
 11  | 5 7 9 9 9
 12  | 1
 12  | (none)
```
(Stem = hundreds/thousands digits combined, e.g. "11" = 1100s; leaf = tens digit; ones digit truncated)

**(c)** SU=100, #LCPS=2 → Increment = 100/2 = **50**
Median: n=22 (even) → average of 11th & 12th ordered values = (950+958)/2 = **954**

**(d)** P(X>0) = 1 − P(X=0) = 1 − (1−1/7)²⁷ = 1 − (6/7)²⁷ ≈ 1 − 0.0156 ≈ **0.9844**

## Question 3
**(a)** Lower half (first 11): 702,765,785,905,919,**920**,923,929,938,948,950 → Q1 = 6th value = **920**
Upper half (last 11): 958,970,977,978,1123,**1156**,1170,1195,1196,1198,1217 → Q3 = 6th value = **1156**

**(b)** IQR = 1156 − 920 = **236**

**(c)** Mild bounds: 920−1.5(236)=**566** and 1156+1.5(236)=**1510**
Extreme bounds: 920−3(236)=**212** and 1156+3(236)=**1864**
All data (702–1217) falls within the mild bounds → **no outliers**

## Question 4
**(a)** X ~ Binomial(n=15, π=0.12) — fixed n, constant π, independence assumed.
μ = nπ = 15(0.12) = **1.8**; σ² = nπ(1−π) = 15(0.12)(0.88) = **1.584**

**(b)** P(X=2) = (15 choose 2)(0.12)²(0.88)¹³ = 105 × 0.0144 × 0.1898 ≈ **0.287**

**(c)** μ=8 → λ=1/8=0.125. P(x<5) = 1−e^(−0.125×5) = 1−e^(−0.625) ≈ 1−0.535 ≈ **0.465**

**(d)** z = (5.0−5.2)/0.15 = −1.333 → P(z<−1.33) = 1−P(z<1.33) = 1−0.9082 = **0.0918**

## Bonus
∫₀^c 3x² dx = 0.40 → c³ = 0.40 → **c ≈ 0.7368**
