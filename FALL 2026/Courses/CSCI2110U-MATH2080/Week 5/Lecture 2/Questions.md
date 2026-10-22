---
tags: [practice, week5, lecture2, sequences, summations, cardinality]
---

# Lecture 9: Practice Questions (Sequences, Sums, Cardinality)

← [[Notes]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Honour homework for this lecture (8th edition, from the slide)
> **§2.4:** #1, 3, 5, 9, 19, 25, 29, 31, 33, 35, 36, 39, 45
> **§2.5:** #1, 3, 19
> (7th ed: §2.4 #1, 3, 5, 9, 19, 25, 29, 31, 33, 35, 36, 39, 43; §2.5 #1, 3, 19.) Odd answers are in the back of the textbook.

Do these on paper first, then check the answers at the bottom.

---

## Part A: Quick questions (test style)

**1.** Find a formula for a_n: 5, 8, 11, 14, ...

**2.** Find a formula for a_n: 3, 6, 12, 24, 48, ...

**3.** Find a formula for a_n: 2, 5, 10, 17, 26, ...

**4.** Find a formula for a_n: 19, 13, 7, 1, −5, ...

**5.** Evaluate Σ (k=1 to 4) (2k + 1).

**6.** Evaluate Σ (k=0 to 5) 3·2^k.

**7.** Evaluate Σ (k=1 to 10) k².

**8.** Evaluate Σ (k=1 to 20) k.

**9.** Evaluate Σ (k=3 to 10) k.

**10.** Evaluate Σ (i=1 to 3) Σ (j=1 to 2) i·j.

**11.** With f1 = 1, f2 = 1, f_n = f_(n−1) + f_(n−2), find f7.

**12.** Evaluate Σ (k=1 to 5) (−1)^k.

**13.** Evaluate Σ (k=0 to 9) 5·1^k.

**14.** Select ALL countable sets:
a) ℤ  b) ℚ  c) ℝ  d) the even integers  e) the interval (0, 1)

**15.** The function f(n) = 2n is a bijection from ℤ+ to ____.

**16.** True or False: two sets have the same cardinality if and only if there is a bijection between them.

**17.** Let S = {primes ≤ 10}. Evaluate the sum of p over p ∈ S.

**18.** (Time permitting) Using w_n = w_(n−1) + 2·w_(n−2), w_1 = 1, w_2 = 3, find w_5, the number of ways to build a 2-by-5 wall.

---

## Part B: Written (midterm style)

**P1.** Prove that ℤ+ and the set of positive odd integers have the same cardinality.

**P2.** Prove that the sum of the first n odd positive integers is n². That is, find Σ (k=1 to n) (2k − 1) using the summation identities.

**P3.** Use the geometric sum formula to find Σ (k=0 to n) 3^k, then evaluate it for n = 4 and check by adding directly.

**P4.** Show that ℕ is countable.

---
---

## ANSWERS

### Part A

**1.** Differences are +3 each time. Starting at 5 when n = 1: **a_n = 3n + 2**.

**2.** Ratio 2 each time, first term 3: **a_n = 3·2^(n−1)**.

**3.** 1+1, 4+1, 9+1, 16+1, 25+1: **a_n = n² + 1**.

**4.** Differences are −6: **a_n = 25 − 6n** (n = 1 gives 19).

**5.** 3 + 5 + 7 + 9 = **24**. (Check: 2·(4·5/2) + 4 = 20 + 4 = 24.)

**6.** Geometric with a = 3, r = 2, n = 5: 3·(2⁶ − 1)/(2 − 1) = 3·63 = **189**.

**7.** 10·11·21/6 = 2310/6 = **385**.

**8.** 20·21/2 = **210**.

**9.** Σ (1 to 10) = 55, minus (1 + 2) = 3: **52**.

**10.** Σ_i Σ_j ij = (1+2+3)(1+2) = 6·3 = **18**.

**11.** f1=1, f2=1, f3=2, f4=3, f5=5, f6=8, f7 = **13**.

**12.** −1 + 1 − 1 + 1 − 1 = **−1**.

**13.** r = 1, so the sum is (n+1)·a = 10·5 = **50**. (It's just 5 added ten times.)

**14. a, b, d.** (ℝ and (0,1) are uncountable.)

**15.** The **even positive integers** (n ↦ 2n pairs every positive integer with exactly one even positive integer).

**16. True.**

**17.** 2 + 3 + 5 + 7 = **17**.

**18.** w_3 = 3 + 2·1 = 5, w_4 = 5 + 2·3 = 11, w_5 = 11 + 2·5 = **21**.

### Part B

**P1.** Define f: ℤ+ → {positive odd integers}, f(n) = 2n − 1.
*One-to-one:* if f(a) = f(b), then 2a − 1 = 2b − 1, so a = b.
*Onto:* let m be a positive odd integer. Then m = 2k − 1 for some positive integer k, namely k = (m+1)/2 (an integer since m is odd, and ≥ 1 since m ≥ 1). Then f(k) = m.
So f is a bijection, and the two sets have the same cardinality. ∎

**P2.** Σ (k=1 to n) (2k − 1) = 2·Σk − Σ1 = 2·n(n+1)/2 − n = n(n+1) − n = **n²**. ∎
(Check n = 3: 1 + 3 + 5 = 9 = 3².)

**P3.** Σ (k=0 to n) 3^k is geometric with a = 1, r = 3 (r ≠ 1): (3^(n+1) − 1)/(3 − 1) = **(3^(n+1) − 1)/2**.
For n = 4: (3⁵ − 1)/2 = (243 − 1)/2 = **121**.
Direct check: 1 + 3 + 9 + 27 + 81 = 121. ✓

**P4.** Define f: ℤ+ → ℕ by f(n) = n − 1.
*One-to-one:* n − 1 = m − 1 implies n = m.
*Onto:* for any k ∈ ℕ (k ≥ 0), f(k + 1) = k, and k + 1 ∈ ℤ+.
So f is a bijection, hence ℕ has the same cardinality as ℤ+, so ℕ is countable. ∎

---

## Score yourself
If you missed the sums, redo section 4 of [[Notes]] (the five identities) and practice shifting the bounds. If you missed the cardinality ones, redo the "build a bijection from ℤ+" pattern: write down a formula, then prove one-to-one and onto exactly like in Lecture 8.
