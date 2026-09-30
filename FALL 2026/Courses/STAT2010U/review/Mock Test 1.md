---
tags: [review, exam-prep, mock-test]
based_on: Term Test 1 structure as described by professor (Lecture 5)
---
  
# 📝 Mock Term Test 1

← [[Exam Review - Term Test 1]]

> [!danger] Test conditions — actually use them
> - Set a timer for **80 minutes**
> - **Handwritten, pencil, no laptop, no calculator app** — use an actual physical calculator like on test day
> - Formula sheet allowed (use your [[Exam Review - Term Test 1#📄 Confirmed Formula Sheet|confirmed formula sheet]]) — but no extra notes
> - Only write a "therefore" statement where explicitly asked
> - Do NOT check answers until you've finished everything or run out of time

---

## Question 1 — Probability Density Function (2 parts)

A continuous random variable X has density function:

f(x) = kx² for 1 < x < 4, and 0 otherwise

**(a)** Find the value of k that makes this a valid density function. [4 marks]

**(b)** Find the mean of X. [4 marks]

**(c)** Find the median of X. [4 marks]

---

## Question 2 — Raw Dataset: Stem-Leaf, Skew, Calculator Stats

The following data represents the number of minutes 16 students spent on a homework assignment:

```
23  31  35  38  41  42  44  45  46  47  48  52  55  58  61  67
```

**(a)** Construct a stem-and-leaf plot using the tens digit as the stem. State the stem unit (SU), leaf unit (LU), and increment. [5 marks]

**(b)** Based on your plot, is the data left-skewed, right-skewed, or symmetric? Justify your answer in one sentence. [2 marks]

**(c)** Using your calculator, find the sample mean (x̄) and sample standard deviation (s). [3 marks]

---

## Question 3 — Raw Dataset: Median, Quartiles, Boxplot

Using the same 16 data values from Question 2 (already ordered above):

**(a)** Find the median. [3 marks]

**(b)** Find Q1 and Q3. [4 marks]

**(c)** Find the IQR. [1 mark]

**(d)** Determine the mild and extreme outlier boundaries. Are there any outliers in this dataset? [4 marks]

---

## Question 4 — Distributions (several parts)

**(a)** A quality control engineer knows that 8% of items produced on an assembly line are defective. She inspects 12 items. Let X = number of defective items found.

State, with justification, what distribution X follows and identify its para  meters. [3 marks]

**(b)** Using your answer from (a), find P(X = 2). [3 marks]

**(c)** Find the mean and variance of X from part (a). [2 marks]

**(d)** The time (in minutes) between customer arrivals at a bank follows an exponential distribution with λ = 0.25. Find the probability that more than 6 minutes pass between arrivals. [3 marks]

**(e)** A machine fills bottles with a mean volume of 500 mL and a standard deviation of 4 mL, normally distributed. Find the probability that a randomly selected bottle contains less than 495 mL. [4 marks]

---

## 🎁 Bonus Question

A density function is given by f(x) = 3x² for 0 < x < 1, and 0 otherwise.

Show that this is a valid density function, and then find P(X > 0.5). [3 bonus marks]

---
---

# 🔑 Answer Key (don't peek until done)

## Question 1
**(a)** ∫₁⁴ kx² dx = 1 → k(x³/3) from 1 to 4 = k(64/3 − 1/3) = k(21) = 1 → **k = 1/21**

**(b)** μ = ∫₁⁴ x·(1/21)x² dx = (1/21)∫₁⁴ x³ dx = (1/21)[x⁴/4] from 1 to 4 = (1/21)(256/4 − 1/4) = (1/21)(63.75) ≈ **3.036**

**(c)** Solve ∫₁^m (1/21)x² dx = 0.5 → (1/21)(m³/3 − 1/3) = 0.5 → m³ − 1 = 31.5 → m³ = 32.5 → **m ≈ 3.19**

## Question 2
**(a)**
```
Stem | Leaf
  2  | 3
  3  | 1 5 8
  4  | 1 2 4 5 6 7 8
  5  | 2 5 8
  6  | 1 7
```
SU=10, LU=1, increment=10 (one leaf category per stem)

**(b)** Counts per stem: 1, 3, 7, 3, 2 (stems 2,3,4,5,6). The peak (stem 4) sits roughly in the middle, with counts building up (1→3→7) and tapering down (7→3→2) on either side at a similar rate → **roughly symmetric**. (When you sketch it, check this yourself — this dataset is close enough to symmetric that either "symmetric" or "slight skew" with correct reasoning should be accepted; the key skill being tested is justifying your read of the shape, not hitting one exact label.)

**(c)** Σx = 23+31+35+38+41+42+44+45+46+47+48+52+55+58+61+67 = 733
x̄ = 733/16 ≈ **45.81**
(Standard deviation: use your calculator's stat mode on this dataset — expect s in the range of roughly 11-12; verify with your own calculator.)

## Question 3
**(a)** n=16 (even) → median = average of 8th and 9th values = (46+47)/2 = **46.5**
   
**(b)** Lower half (first 8): 23,31,35,38,41,42,44,45 → n=8 even → Q1 = avg of 4th&5th = (38+41)/2 = **39.5**
Upper half (last 8): 46,47,48,52,55,58,61,67 → n=8 even → Q3 = avg of 4th&5th = (52+55)/2 = **53.5**

**(c)** IQR = 53.5 − 39.5 = **14**

**(d)** Mild bounds: 39.5−1.5(14)=**18.5** and 53.5+1.5(14)=**74.5**. Extreme bounds: 39.5−3(14)=**−2.5** and 53.5+3(14)=**95.5**. All data (23-67) falls within the mild bounds → **no outliers**.

## Question 4
**(a)** Binomial: fixed n=12, constant π=0.08 (probability of defective), independence assumed (items produced independently). X ~ Binomial(n=12, π=0.08)

**(b)** P(X=2) = (12 choose 2)(0.08)²(0.92)¹⁰ ≈ 66 × 0.0064 × 0.4344 ≈ **0.183**

**(c)** μ = nπ = 12(0.08) = **0.96**; σ² = nπ(1−π) = 12(0.08)(0.92) ≈ **0.883**

**(d)** P(x>6) = e^(−0.25×6) = e^(−1.5) ≈ **0.223**

**(e)** z = (495−500)/4 = −1.25 → P(z<−1.25) = **0.1056** (from Table I)

## Bonus
Valid density: ∫₀¹ 3x² dx = [x³] from 0 to 1 = 1 − 0 = 1 ✅ (and 3x²≥0 on the domain)
P(X>0.5) = ∫₀.₅¹ 3x² dx = [x³] from 0.5 to 1 = 1 − 0.125 = **0.875**
