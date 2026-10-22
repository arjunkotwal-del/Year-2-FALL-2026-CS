---
tags: [review, midterm, practice-exam, mock]
---

# Practice Midterm 4 (Final Mock, matches the announcement)

← [[Midterm Prep Plan]] | ← [[Practice Midterm 3 (Mock)]]

> [!info] Format
> Built from the instructor's announcement: **7 questions, 60 marks, 70 minutes**. Multiple choice, short answers, and 4 long answers (equivalence by identities, valid argument, number proof, set proof plus function proof). Handwritten, closed notes, but use the **formula sheet on the Canvas announcement**.
>
> **Short on time?** Do Q4 to Q7 (the long answers). They carry the most marks on the real exam.

---

## Q1. Multiple choice [10] (one answer each, 2 marks)

**a)** The contrapositive of "If it is sunny and I have time, then I go hiking" is:
A. If I do not go hiking, then it is not sunny or I do not have time.
B. If I do not go hiking, then it is not sunny and I do not have time.
C. If I go hiking, then it is sunny and I have time.
D. If it is not sunny or I have no time, then I do not go hiking.

**b)** The domain is ℝ. Which statement is true?
A. ∃x ∀y (x < y)  B. ∀x ∃y (x < y)  C. ∀x ∃y (y² = x)  D. ∃y ∀x (x² ≤ y)

**c)** Which function is one-to-one?
A. f: ℝ → ℝ, f(x) = |x|  B. f: ℤ → ℤ, f(n) = n²  C. f: ℝ → ℝ, f(x) = x³  D. f: ℤ × ℤ → ℤ, f(m, n) = mn

**d)** Let f: ℝ → ℤ, f(x) = ⌊2x⌋. Which statement is true?
A. f([0, 1)) = {0, 1}  B. f⁻¹({1}) = [1, 2)  C. f(x + 1) = f(x) + 1 for every real x  D. f(0.5) = 0

**e)** Which statement holds for all sets A and B?
A. A ∩ B ⊆ A − B  B. A − B ⊆ A ∪ B  C. A ∪ B ⊆ A ∩ B  D. A ⊆ A − B

## Q2. Logic, short answers [10]

**a)** [3] Negate (p ∨ ¬q) → (r ∧ s) so that there is no → and ¬ appears only in front of single variables.
**b)** [2] Write the converse, inverse and contrapositive of "If n is divisible by 4, then n is even."
**c)** [3] True or false? (i) ∀x > 0 ∃y ∈ ℕ (y > 1/x)  (ii) ∃x ∈ ℝ ∀y ∈ ℝ (xy = 0)  (iii) ∃x ∈ ℤ (x² = 2)
**d)** [2] Show that ∀x (P(x) ∨ Q(x)) and ∀x P(x) ∨ ∀x Q(x) are **not** logically equivalent, by giving a counterexample.

## Q3. Functions, sequences, countability, short answers [10]

**a)** [4] Let f: ℝ → ℤ, f(x) = ⌈2x − 3⌉. Find f((0, 2]) and f⁻¹({0}).
**b)** [3] a_n = (n + 1)/(2n). Find a₃, Σ (k=1 to 3) a_k, and Σ (k=1 to 3) (−1)ᵏ a_k.
**c)** [3] Countable or uncountable? (i) 3ℤ  (ii) (0, 1)  (iii) ℤ × ℤ

## Q4. Long answer: equivalence by identities [6]
Prove (p ∧ q) → (r ∨ ¬p) ≡ q → (p → r), naming each law (formula sheet).

## Q5. Long answer: valid argument [8]
Show that the premises
1. ∀x (A(x) → B(x))
2. ∀x (B(x) → ¬C(x))
3. ∃x (A(x) ∧ D(x))

lead to the conclusion ∃x (D(x) ∧ ¬C(x)). Write a numbered derivation, naming the rule and the lines used.

## Q6. Long answer: number proof [6]
Prove that for every integer n, n is even if and only if n² + 4n + 1 is odd. Use only the definitions of even and odd. You may use contraposition.

## Q7. Long answer: sets and functions [10]
**a)** [5] Prove A − (B ∩ C) = (A − B) ∪ (A − C), using the definitions and logical identities.
**b)** [5] Let f: ℝ − {2} → ℝ, f(x) = (x + 3)/(x − 2).
 (i) [3] Prove f is one-to-one.
 (ii) [2] Find f⁻¹ and state its domain.

---
---

# ANSWER KEY (attempt first)

## Q1 [10]
a) **A.** The contrapositive of (s ∧ t) → h is ¬h → ¬(s ∧ t), and ¬(s ∧ t) ≡ ¬s ∨ ¬t.
b) **B.** Given any x, take y = x + 1. (A: nothing is bigger than every x. C: fails for x = −1. D: x² has no upper bound.)
c) **C.** x³ never repeats an output. (|x|: f(1) = f(−1). n²: f(2) = f(−2). mn: f(1,2) = f(2,1).)
d) **A.** For x ∈ [0, 1), 2x ∈ [0, 2), so ⌊2x⌋ ∈ {0, 1}. B is false: ⌊2x⌋ = 1 ⟺ 1 ≤ 2x < 2 ⟺ x ∈ [1/2, 1). C: f(x + 1) = ⌊2x + 2⌋ = f(x) + 2. D: f(0.5) = ⌊1⌋ = 1.
e) **B.** Anything in A − B is in A, so in A ∪ B. (A: counterexample A = {1}, B = {1}. C: A = {1}, B = {2}. D: A = {1}, B = {1}.)

## Q2 [10]
a) ¬((p ∨ ¬q) → (r ∧ s)) ≡ (p ∨ ¬q) ∧ ¬(r ∧ s) ≡ **(p ∨ ¬q) ∧ (¬r ∨ ¬s)**. (¬(a → b) ≡ a ∧ ¬b, then De Morgan's.)
b) Converse: if n is even, then n is divisible by 4. Inverse: if n is not divisible by 4, then n is not even. Contrapositive: **if n is not even, then n is not divisible by 4.**
c) (i) **True** (take a natural number y > 1/x). (ii) **True** (x = 0). (iii) **False** (no integer squares to 2).
d) Domain ℤ, P(x): "x is even", Q(x): "x is odd". ∀x (P(x) ∨ Q(x)) is **true** (every integer is even or odd), but ∀x P(x) ∨ ∀x Q(x) is **false** (not every integer is even, and not every integer is odd). Different truth values, so not equivalent.

## Q3 [10]
a) For x ∈ (0, 2], 2x − 3 ranges over (−3, 1]. The ceilings are −2, −1, 0, 1, so **f((0, 2]) = {−2, −1, 0, 1}**.
f⁻¹({0}): ⌈2x − 3⌉ = 0 ⟺ −1 < 2x − 3 ≤ 0 ⟺ 2 < 2x ≤ 3 ⟺ 1 < x ≤ 3/2, so **(1, 3/2]**.
b) a₁ = 1, a₂ = 3/4, a₃ = 4/6 = **2/3**. Σ = 1 + 3/4 + 2/3 = 12/12 + 9/12 + 8/12 = **29/12**. Alternating: −1 + 3/4 − 2/3 = −12/12 + 9/12 − 8/12 = **−11/12**.
c) (i) **countable** (ii) **uncountable** (iii) **countable**.

## Q4 [6]

| Step | Expression | Law |
|---|---|---|
| 1 | (p ∧ q) → (r ∨ ¬p) | Given |
| 2 | ¬(p ∧ q) ∨ (r ∨ ¬p) | Conditional identity |
| 3 | (¬p ∨ ¬q) ∨ (r ∨ ¬p) | De Morgan's |
| 4 | ¬p ∨ ¬p ∨ ¬q ∨ r | Commutative and associative |
| 5 | ¬p ∨ ¬q ∨ r | Idempotent (¬p ∨ ¬p ≡ ¬p) |
| 6 | ¬q ∨ (¬p ∨ r) | Commutative and associative |
| 7 | ¬q ∨ (p → r) | Conditional identity |
| 8 | q → (p → r) | Conditional identity ∎ |

## Q5 [8]

| Line | Statement | Reason |
|---|---|---|
| 1 | ∀x (A(x) → B(x)) | Premise |
| 2 | ∀x (B(x) → ¬C(x)) | Premise |
| 3 | ∃x (A(x) ∧ D(x)) | Premise |
| 4 | A(c) ∧ D(c) | EI (3), c is a new name |
| 5 | A(c) | Simplification (4) |
| 6 | D(c) | Simplification (4) |
| 7 | A(c) → B(c) | UI (1) |
| 8 | B(c) | Modus ponens (5, 7) |
| 9 | B(c) → ¬C(c) | UI (2) |
| 10 | ¬C(c) | Modus ponens (8, 9) |
| 11 | D(c) ∧ ¬C(c) | Conjunction (6, 10) |
| 12 | ∃x (D(x) ∧ ¬C(x)) | EG (11) ∎ |

## Q6 [6]
(⇒) Suppose n is even, n = 2k. Then n² + 4n + 1 = 4k² + 8k + 1 = 2(2k² + 4k) + 1, which is odd. ✓
(⇐) Contrapositive: if n is odd, then n² + 4n + 1 is even. Let n = 2k + 1.
n² + 4n + 1 = (4k² + 4k + 1) + (8k + 4) + 1 = 4k² + 12k + 6 = 2(2k² + 6k + 3), which is even. ✓
So if n² + 4n + 1 is odd, then n is even. Both directions hold. **Therefore** n is even if and only if n² + 4n + 1 is odd. ∎

## Q7 [10]
**a)** x ∈ A − (B ∩ C)
⟺ x ∈ A ∧ ¬(x ∈ B ∧ x ∈ C), definition of difference and intersection
⟺ x ∈ A ∧ (x ∉ B ∨ x ∉ C), De Morgan's
⟺ (x ∈ A ∧ x ∉ B) ∨ (x ∈ A ∧ x ∉ C), distributive
⟺ x ∈ (A − B) ∨ x ∈ (A − C), definition of difference
⟺ x ∈ (A − B) ∪ (A − C), definition of union. ∎

**b)(i)** Let a, b ∈ ℝ − {2} with f(a) = f(b). Then (a + 3)/(a − 2) = (b + 3)/(b − 2). Cross-multiply (both denominators are nonzero):
(a + 3)(b − 2) = (b + 3)(a − 2)
ab − 2a + 3b − 6 = ab − 2b + 3a − 6
−2a + 3b = −2b + 3a
5b = 5a, so a = b. ∎

**b)(ii)** Set y = (x + 3)/(x − 2): y(x − 2) = x + 3, so yx − 2y = x + 3, so x(y − 1) = 2y + 3, so x = (2y + 3)/(y − 1). So **f⁻¹(y) = (2y + 3)/(y − 1)**. The value y = 1 is impossible (it would need x + 3 = x − 2), so the range of f is ℝ − {1}, and **f⁻¹ has domain ℝ − {1}**.

---

## Score yourself
Out of 60. Target 50 or more.
- Q4, Q7a lost marks: the identity pattern (remove →, De Morgan's, regroup, match the target).
- Q5 lost marks: EI first with a new name, UI with the same c, then the propositional rules, then EG.
- Q6 lost marks: write n = 2k or 2k + 1, **expand (2k + 1)² correctly**, and finish with "2 times an integer".
- Q7b lost marks: "assume f(a) = f(b)", cross-multiply, reach a = b.
- Put every miss in the error log in [[Midterm Prep Plan]].
