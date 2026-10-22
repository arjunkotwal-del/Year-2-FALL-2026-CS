---
tags: [notes, week5, lecture2, sequences, summations, cardinality]
---

# Lecture 9: Sequences, Summations, Cardinality (Sections 2.4-2.5)

← [[../../CSCI2110U-MATH2080 - Discrete Math]] | [[Questions]]
Source: [[../../files/MATH2080_Lecture9_Sections_2p4_2p5_SequencesnSums_and_Cardinality.pdf]] (blank skeleton posted before the lecture, Oct 8)

> [!warning] Built BEFORE the lecture
> This was built from the posted skeleton plus the textbook. After the lecture, compare it against the instructor's `_filled.pdf` and fix anything he did differently.

---

## 1. Sequences

A **sequence** is a function from ℤ+ (or ℕ) to some set. Write a(n) as a_n. The whole sequence is {a_n}.

| Type | Formula | Example |
|---|---|---|
| Harmonic | a_n = 1/n | 1, 1/2, 1/3, ... |
| Arithmetic | a_n = a + n·d (add d each step) | 5, 8, 11, ... |
| Geometric | a_n = a·r^(n−1) (multiply by r each step) | 2, 6, 18, ... |
| Even positive integers | 2n | 2, 4, 6, ... |
| Odd positive integers | 2n − 1 | 1, 3, 5, ... |
| Squares / cubes / powers of 2 | n², n³, 2ⁿ | |
| Alternating | (−1)ⁿ | −1, 1, −1, 1, ... |
| 0,1,0,1... | (1 + (−1)ⁿ)/2 | 0, 1, 0, 1, ... |
| Fibonacci (recursive) | f1 = 1, f2 = 1, f_n = f_(n−1) + f_(n−2) | 1, 1, 2, 3, 5, 8, 13, ... |

## 2. Inferring a formula from terms (Example 2)

**Method:** check the differences (arithmetic?), then the ratios (geometric?), then compare with n!, n², 2ⁿ.

1. **19, 13, 7, 1, −5, −11, −17...** differences are all −6. Arithmetic with d = −6: **a_n = 25 − 6n** (n=1 gives 19 ✓).
2. **2, 6, 18, 54, 162...** ratios are all 3. Geometric: **a_n = 2·3^(n−1)**.
3. **2, 3, 7, 25, 121, 721...** each is one more than a factorial (1!+1, 2!+1, 3!+1, 4!+1, 5!+1, 6!+1): **a_n = n! + 1**.

## 3. Summation notation

Σ from k=m to n of a_k = a_m + a_(m+1) + ... + a_n.
- m = lower index, n = upper index, k = **dummy variable** (the letter doesn't matter: the sum over k equals the sum over i).
- Number of terms = n − m + 1.

## 4. The summation identities (memorize these)

| # | Identity |
|---|---|
| 1 | Σ (k=0 to n) a·r^k = a·(r^(n+1) − 1)/(r − 1) if r ≠ 1. If r = 1 it's (n+1)·a |
| 2 | Σ (k=1 to n) 1 = n |
| 3 | Σ (k=1 to n) k = n(n+1)/2 |
| 4 | Σ (k=1 to n) k² = n(n+1)(2n+1)/6 |
| 5 | Σ (k=1 to n) k³ = [n(n+1)/2]² |

**Splitting a range:** Σ (k=m to n) = Σ (k=1 to n) − Σ (k=1 to m−1).

## 5. Worked examples

**Example 3a: Σ (i=3 to 50) of (2i² − i + 1)/3.**
Pull out 1/3 and split: (1/3)[2·Σi² − Σi + Σ1], all from i=3 to 50.
- Σ (i=1 to 50) i² = 50·51·101/6 = 42925. Subtract i=1,2: 1+4 = 5. So Σ (3..50) i² = 42920.
- Σ (i=1 to 50) i = 1275. Subtract 1+2 = 3. So Σ (3..50) i = 1272.
- Number of terms: 50 − 3 + 1 = 48, so Σ1 = 48.
- (1/3)[2(42920) − 1272 + 48] = (1/3)(84616) = **84616/3** (about 28205.33).

**Example 3b (double sum): Σ (i=0 to 2) Σ (j=0 to 3) (2i + 3j).**
Do the inner sum first, with i fixed: Σ (j=0 to 3)(2i + 3j) = 4·(2i) + 3(0+1+2+3) = 8i + 18.
Then Σ (i=0 to 2)(8i + 18) = 8(0+1+2) + 18·3 = 24 + 54 = **78**.

**Example 4a: Σ over 1 ≤ k ≤ 5 of (3k+1)/2.** This is just k = 1 to 5. (1/2)[3·15 + 5] = (45 + 5)/2 = **25**.
**Example 4b:** S = {primes ≤ 10} = {2, 3, 5, 7}, so Σ over p ∈ S of p = 2+3+5+7 = **17**.
(Example 4c is the determinant formula from linear algebra, a sum over permutations. Just recognize it is a sum over a set. Example 5, the Putnam problem, is a challenge you can skip.)

## 6. Cardinality (Section 2.5)

**Same cardinality:** A and B have the same cardinality iff there is a **bijection** (one-to-one correspondence) from A to B.

**Countable:** finite, OR the same cardinality as ℤ+. Otherwise **uncountable**.

| Set | Countable? |
|---|---|
| ℤ+, ℕ, ℤ | Yes |
| Even integers, odd positive integers | Yes |
| ℚ | Yes |
| ℝ, the interval (0,1) | **No** (uncountable) |

**How to show a set is countable:** build a bijection from ℤ+, ideally with a diagram that lists the elements in order.

- **Even positive integers:** f(n) = 2n.
- **Odd positive integers:** f(n) = 2n − 1.
- **ℕ:** f(n) = n − 1.
- **ℤ (Example 7)** list the integers in the order 0, 1, −1, 2, −2, 3, −3, ... and match them with 1, 2, 3, 4, 5, 6, 7, ... Formula: f(n) = n/2 if n is even, and f(n) = −(n−1)/2 if n is odd. (f(1)=0, f(2)=1, f(3)=−1, f(4)=2, f(5)=−2.)

> [!tip] The strange fact
> ℤ+ is a proper subset of ℤ, yet the two sets have the same size. For infinite sets, "same size" means a bijection exists, not "one contains the other".

## 7. Time-permitting: the 2-by-n wall

Number of ways w_n to build a 2-by-n wall using 1-by-2 and 2-by-2 bricks. Case on how the left end starts:
- one vertical 1-by-2 brick (fills width 1): leaves w_(n−1) ways
- two horizontal 1-by-2 bricks stacked (width 2): leaves w_(n−2)
- one 2-by-2 brick (width 2): leaves w_(n−2)

So **w_n = w_(n−1) + 2·w_(n−2)**, with w_1 = 1 and w_2 = 3. Then w_3 = 5, w_4 = 11, w_5 = 21. This is a **recursively defined sequence**, which is the preview of the recursion unit later.

---

## Summary checklist
- [ ] Spot arithmetic / geometric / factorial patterns and write a formula a_n
- [ ] Know the 5 summation identities cold
- [ ] Evaluate sums with shifted bounds (subtract the front part) and double sums (inner first)
- [ ] State the definition of same cardinality and countable
- [ ] Build a bijection to show ℤ+ ~ evens, odds, ℕ or ℤ
- [ ] Know ℝ is uncountable and ℚ is countable

**Next:** [[Questions]]
