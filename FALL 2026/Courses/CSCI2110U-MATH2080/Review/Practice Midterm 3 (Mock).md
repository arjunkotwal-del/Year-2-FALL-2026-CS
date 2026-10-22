---
tags: [review, midterm, practice-exam, mock]
---

# Practice Midterm 3 (Mock exam, built from the instructor's announcement)

← [[Midterm Prep Plan]] | ← [[Practice Midterm 1]] | ← [[Practice Midterm 2 (Reinforce)]]

> [!info] Format
> Follows the instructor's Oct 17 announcement: multiple choice, short answers, and long answers (equivalence by identities, quantified equivalence, a valid argument with rules of inference, proofs, a set proof, a function proof). **8 questions, 80 marks.** It is a bit longer than the real one (6-7 questions, 70 minutes), so aim for **70 to 80 minutes**, or split it into two sittings.
>
> **Rules:** handwritten, closed notes, but you may use the **formula sheet on the Canvas announcement** (identities and rules of inference). That is what you'll have on the real exam.

---

## Q1. Multiple choice [10] (one answer each, 2 marks)

**a)** The contrapositive of "If I eat and sleep, then I focus" is:
(i) If I focus, then I eat and sleep.
(ii) If I do not focus, then I do not eat or I do not sleep.
(iii) If I do not focus, then I do not eat and I do not sleep.
(iv) If I do not eat or I do not sleep, then I do not focus.

**b)** The negation of (p ∧ q) → r is equivalent to:
(i) (¬p ∨ ¬q) → ¬r  (ii) p ∧ q ∧ ¬r  (iii) ¬(p ∧ q) → r  (iv) (p ∧ q) ∨ ¬r

**c)** Over the integers, the negation of ∀x ∃y (x + y = 0) is:
(i) ∃x ∀y (x + y ≠ 0)  (ii) ∀x ∃y (x + y ≠ 0)  (iii) ∃x ∃y (x + y ≠ 0)  (iv) ∀x ∀y (x + y ≠ 0)

**d)** The premises are p ∨ q and ¬p. Which conclusion is valid?
(i) ¬q  (ii) q  (iii) p  (iv) none follows

**e)** Which of these sets is countable?
(i) ℝ  (ii) (0, 1)  (iii) ℕ × ℕ  (iv) all real numbers between 2 and 3

## Q2. Logic, short answers [10]

**a)** [3] Write the converse, the inverse and the contrapositive of "If x is divisible by 6, then x is even."

**b)** [3] Negate (p ∨ q) → (r ∧ ¬q), so that the ¬ appears only directly in front of variables.

**c)** [4] True or false? (i) ∀x > 0 ∃y ∈ ℕ (y > x)  (ii) ∃x ∈ ℝ ∀y ∈ ℝ (x ≤ y²)  (iii) ∀x ∈ ℝ ∃y ∈ ℝ (xy = 1)  (iv) ∃x ∈ ℤ (x² < x)

## Q3. Sets, functions, sequences, short answers [10]

**a)** [4] True or false?
(i) A − B ⊆ A
(ii) ∅ ⊆ A ∩ B ⊆ A ⊆ A ∪ B
(iii) {1} ∈ {1, 2}
(iv) A − B = B − A for all sets A, B

**b)** [3] f: ℝ → ℤ, f(x) = ⌈x/2⌉. Find f(5), f({1, 2, 3, 4}) and f⁻¹({3}).

**c)** [3] a_n = (n + 1)/(n + 2). Find a₃, Σ (k=1 to 3) a_k, and Σ (k=1 to 3) (−1)ᵏ a_k.

## Q4. Long answer: equivalence by identities [8]

Show that (p ∨ q) → r ≡ (p → r) ∧ (q → r), naming the law at every step.

## Q5. Long answer: quantified equivalence [8]

Prove that ∃x (P(x) ∨ Q(x)) ≡ ∃x P(x) ∨ ∃x Q(x). (Show each side implies the other.)

## Q6. Long answer: valid argument [10]

Use rules of inference to show that the premises
1. ∀x (R(x) → S(x))
2. ∃x (R(x) ∧ T(x))
3. ∀x (S(x) → ¬U(x))

lead to the conclusion ∃x (T(x) ∧ ¬U(x)). Write a table with line, statement and reason (with line numbers).

## Q7. Long answer: proofs [12]

**a)** [6] Prove that 5n + 4 is even if and only if n is even.
**b)** [6] Prove by contradiction: the product of a nonzero rational number and an irrational number is irrational.

## Q8. Long answer: sets and functions [12]

**a)** [6] Prove, using the definitions of the set operations and logical identities: A ∩ (B − C) = (A ∩ B) − C.
**b)** [6] Let f: ℤ × ℤ → ℤ × ℤ, f(m, n) = (m + n, m − n). Prove that f is one-to-one, and show that f is not onto.

---
---

# ANSWER KEY (attempt first)

## Q1 [10]
a) **(ii)**. The contrapositive of (e ∧ s) → f is ¬f → ¬(e ∧ s), and ¬(e ∧ s) ≡ ¬e ∨ ¬s. (iv) is the inverse.
b) **(ii)** p ∧ q ∧ ¬r, since ¬(a → b) ≡ a ∧ ¬b.
c) **(i)**. Flip both quantifiers and negate the inside.
d) **(ii)** q, by disjunctive syllogism.
e) **(iii)** ℕ × ℕ is countable. ℝ, (0,1) and any interval of reals are not.

## Q2 [10]
a) Converse: if x is even, then x is divisible by 6. Inverse: if x is not divisible by 6, then x is not even. Contrapositive: **if x is not even, then x is not divisible by 6.** (Only the contrapositive is equivalent to the original.)
b) ¬((p ∨ q) → (r ∧ ¬q)) ≡ (p ∨ q) ∧ ¬(r ∧ ¬q) ≡ **(p ∨ q) ∧ (¬r ∨ q)**.
c) (i) **T** (take any natural y > x). (ii) **T** (x = 0, since 0 ≤ y² always). (iii) **F** (x = 0 has no y with 0·y = 1). (iv) **F** (x² < x needs 0 < x < 1, no integer).

## Q3 [10]
a) (i) **T** (ii) **T** (iii) **F** (the elements of {1, 2} are 1 and 2) (iv) **F** (for example A = {1}, B = ∅: A − B = {1} but B − A = ∅).
b) f(5) = ⌈2.5⌉ = **3**. f({1,2,3,4}) = {⌈0.5⌉, ⌈1⌉, ⌈1.5⌉, ⌈2⌉} = **{1, 2}**. f⁻¹({3}): ⌈x/2⌉ = 3 ⟺ 2 < x/2 ≤ 3 ⟺ 4 < x ≤ 6, so **(4, 6]**.
c) a₁ = 2/3, a₂ = 3/4, a₃ = **4/5**. Sum = 2/3 + 3/4 + 4/5 = (40 + 45 + 48)/60 = **133/60**. Alternating: −2/3 + 3/4 − 4/5 = (−40 + 45 − 48)/60 = **−43/60**.

## Q4 [8]

| Step | Expression | Law |
|---|---|---|
| 1 | (p ∨ q) → r | Given |
| 2 | ¬(p ∨ q) ∨ r | Conditional identity |
| 3 | (¬p ∧ ¬q) ∨ r | De Morgan's |
| 4 | (¬p ∨ r) ∧ (¬q ∨ r) | Distributive |
| 5 | (p → r) ∧ (q → r) | Conditional identity (twice) ∎ |

## Q5 [8]
(⇒) Suppose ∃x (P(x) ∨ Q(x)). By EI, let c be an element with P(c) ∨ Q(c).
- If P(c): by EG, ∃x P(x), so ∃x P(x) ∨ ∃x Q(x).
- If Q(c): by EG, ∃x Q(x), so ∃x P(x) ∨ ∃x Q(x).
(⇐) Suppose ∃x P(x) ∨ ∃x Q(x).
- If ∃x P(x): by EI let d have P(d). By addition, P(d) ∨ Q(d). By EG, ∃x (P(x) ∨ Q(x)).
- If ∃x Q(x): by EI let e have Q(e). By addition, P(e) ∨ Q(e). By EG, ∃x (P(x) ∨ Q(x)).
Both directions hold, so the two statements are equivalent. ∎

## Q6 [10]

| Line | Statement | Reason |
|---|---|---|
| 1 | ∀x (R(x) → S(x)) | Premise |
| 2 | ∃x (R(x) ∧ T(x)) | Premise |
| 3 | ∀x (S(x) → ¬U(x)) | Premise |
| 4 | R(c) ∧ T(c) | EI (2), c is a new name |
| 5 | R(c) | Simplification (4) |
| 6 | T(c) | Simplification (4) |
| 7 | R(c) → S(c) | UI (1) |
| 8 | S(c) | Modus ponens (5, 7) |
| 9 | S(c) → ¬U(c) | UI (3) |
| 10 | ¬U(c) | Modus ponens (8, 9) |
| 11 | T(c) ∧ ¬U(c) | Conjunction (6, 10) |
| 12 | ∃x (T(x) ∧ ¬U(x)) | EG (11) ∎ |

## Q7 [12]
**a)** (⇒) Contraposition: if n is odd, then 5n + 4 is odd. Let n = 2k + 1. Then 5n + 4 = 10k + 5 + 4 = 10k + 9 = 2(5k + 4) + 1, which is odd.
(⇐) Direct: let n = 2k. Then 5n + 4 = 10k + 4 = 2(5k + 2), which is even. Both directions hold. ∎

**b)** Let r = a/b be a nonzero rational (a ≠ 0, b ≠ 0) and x irrational. Suppose r·x is rational, say r·x = c/d with d ≠ 0. Then x = (c/d)/(a/b) = bc/(ad), and ad ≠ 0 because a ≠ 0 and d ≠ 0. So x is rational. This contradicts x being irrational. So r·x is irrational. ∎

## Q8 [12]
**a)** x ∈ A ∩ (B − C)
⟺ x ∈ A ∧ (x ∈ B ∧ x ∉ C), definitions of ∩ and −
⟺ (x ∈ A ∧ x ∈ B) ∧ x ∉ C, associative law
⟺ x ∈ A ∩ B ∧ x ∉ C, definition of ∩
⟺ x ∈ (A ∩ B) − C, definition of −. ∎

**b)** *One-to-one:* assume f(m, n) = f(m′, n′). Then m + n = m′ + n′ and m − n = m′ − n′. Adding the equations: 2m = 2m′, so m = m′. Subtracting them: 2n = 2n′, so n = n′. Hence (m, n) = (m′, n′).
*Not onto:* the pair (1, 0) has no preimage. We would need m + n = 1 and m − n = 0, so m = n and 2m = 1, giving m = 1/2, which is not an integer. ∎

---

# Bonus: the instructor's own examples, with answers

- **Contrapositive of "If I study and get rest before the test, I should ace it":** If I should not ace it, then I did not study or I did not get rest.
- **Negate (p ∧ r) → (q ∨ ¬r):** (p ∧ r) ∧ ¬(q ∨ ¬r) ≡ p ∧ r ∧ ¬q ∧ r ≡ **p ∧ r ∧ ¬q**.
- **Show (p ∧ r) → (q ∨ ¬r) ≡ r → (p → q):** ¬(p ∧ r) ∨ q ∨ ¬r ≡ ¬p ∨ ¬r ∨ q ∨ ¬r ≡ ¬p ∨ ¬r ∨ q ≡ ¬r ∨ (¬p ∨ q) ≡ r → (p → q). (De Morgan's, idempotent, rearrange, conditional identity.)
- **∀x > 0 ∃y ∈ ℕ (1/y < x):** True. Given x > 0, choose a natural number y > 1/x. Then 1/y < x.
- **∀x ∃y P(x,y) vs ∃y ∀x P(x,y):** not equivalent. Take P(x,y): "x < y" over ℤ. ∀x ∃y (x < y) is true (y = x + 1), but ∃y ∀x (x < y) is false (nothing is larger than every integer, including itself).
- **∀x (P ∧ Q) ≡ ∀x P ∧ ∀x Q:** (⇒) for any element c, P(c) ∧ Q(c) by UI, so P(c) and Q(c) separately, and c arbitrary gives ∀x P and ∀x Q by UG. (⇐) for arbitrary c, P(c) and Q(c) by UI, so P(c) ∧ Q(c), and UG gives ∀x (P ∧ Q).
- **∀x (P ∨ Q), ∃x ¬Q, ∀x (P → R) ⊢ ∃x R:** EI on ∃x ¬Q gives ¬Q(c). UI: P(c) ∨ Q(c). Disjunctive syllogism: P(c). UI: P(c) → R(c). Modus ponens: R(c). EG: ∃x R(x).
- **|a| < M iff −M < a < M:** (⇒) cases a ≥ 0: a = |a| < M and −M < 0 ≤ a. Case a < 0: −a = |a| < M, so a > −M, and a < 0 < M. (⇐) cases a ≥ 0: |a| = a < M. Case a < 0: |a| = −a < M since a > −M.
- **3n² + 1 odd iff n even:** (⇒) contraposition: n odd, n = 2k + 1, so 3n² + 1 = 3(4k² + 4k + 1) + 1 = 12k² + 12k + 4, which is even. (⇐) n = 2k, 3n² + 1 = 12k² + 1 = 2(6k²) + 1, odd.
- **Sum of two rationals is rational:** a/b + c/d = (ad + bc)/(bd), with bd ≠ 0.
- **(A ∪ B) − (A ∩ B) = (A − B) ∪ (B − A):** x ∈ left ⟺ (x∈A ∨ x∈B) ∧ ¬(x∈A ∧ x∈B) ⟺ (x∈A ∨ x∈B) ∧ (x∉A ∨ x∉B) ⟺ (x∈A ∧ x∉B) ∨ (x∈B ∧ x∉A) (distributive, then simplify with the negation law) ⟺ x ∈ right.
- **ℤ × ℤ → ℤ × ℤ, f(m, n) = (m, m − n):** one-to-one and onto. Given (a, b), take m = a and n = a − b.
- **f(x) = ⌈3x − 5⌉ + 2:** if the question is f applied to the interval (0, 3], then 3x − 5 ranges over (−5, 4], the ceiling takes the values −4, ..., 4, so the image is **{−2, ..., 6}**. And f⁻¹({1}): ⌈3x − 5⌉ = −1 ⟺ −2 < 3x − 5 ≤ −1 ⟺ **1 < x ≤ 4/3**. (The screenshot is small, so check which interval the question uses.)
- **⌈x⌉ − ⌊x⌋:** 0 if x is an integer, 1 otherwise.
- **g ∘ f one-to-one when f, g are:** assume g(f(a)) = g(f(b)); g one-to-one gives f(a) = f(b); f one-to-one gives a = b.
- **f(S ∩ T) ⊆ f(S) ∩ f(T):** let y ∈ f(S ∩ T). Then y = f(x) for some x ∈ S ∩ T. So x ∈ S and x ∈ T, so y ∈ f(S) and y ∈ f(T), so y ∈ f(S) ∩ f(T).
- **a_n = n/(n + 1):** a₅ = 5/6; Σ (k=1 to 3) a_k = 1/2 + 2/3 + 3/4 = 23/12; Σ (−1)ᵏ a_k = −1/2 + 2/3 − 3/4 = −7/12.
- **Countable:** ℚ yes, ℝ no, 2ℤ yes, ℕ × ℕ yes, {x ∈ ℕ | sin(xπ/2) = 1} = {1, 5, 9, ...} yes.

---

## Score yourself
Out of 80. Target 65 or more in 70 to 80 minutes.
- Put every miss in the error log in [[Midterm Prep Plan]], with the reason.
- Q4, Q5, Q6 lost marks: redo the pattern (identity names, EI first, UI with the same c, EG or UG at the end).
- Q7 lost marks: say which technique you chose and why. Your recurring slips are contraposition vs cases, and expanding (2k + 1)².
- Q8 lost marks: "assume f(a) = f(b)" for one-to-one, "let y be arbitrary" for onto, and the element method for sets.
