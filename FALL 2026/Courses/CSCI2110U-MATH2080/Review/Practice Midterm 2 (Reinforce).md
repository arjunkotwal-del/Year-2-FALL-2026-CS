---
tags: [review, midterm, practice-exam, reinforce]
---

# Practice Midterm 2 (Reinforce what you know)

← [[Midterm Prep Plan]] | ← [[Practice Midterm 1]]

> [!info] What this paper is
> Built from the instructor's Oct 13 announcement: **70 minutes, about 72 marks**, multiple choice, short answers, and long answers. It only uses skills you've already shown you can do (truth tables, De Morgan's and the identities, quantifier truth values and negation, valid arguments, sets, functions, sums, countability). It is for **confidence and speed**, not for finding gaps.
>
> **Left out on purpose** (your weak spots, still on the real exam): formal proofs with rules of inference (EI/UG), translating English to quantifiers, even/odd/rational/absolute-value proofs, proving two quantified expressions equivalent, image/pre-image, counterexamples for non-equivalence. Come back to those after this.

**Rules:** handwrite everything, closed notes, 70 minutes. For Q3 you may use the identity names (the real exam gives a formula sheet).

---

## Q1. Multiple choice [8] (one answer each, 2 marks)

**a)** Which of these is a tautology?
(i) p ∧ ¬p  (ii) p ∨ ¬p  (iii) p → ¬p  (iv) p ∧ q

**b)** The contrapositive of "If it rains, the game is cancelled" is:
(i) If the game is cancelled, it rains.
(ii) If it doesn't rain, the game isn't cancelled.
(iii) If the game isn't cancelled, it doesn't rain.
(iv) It rains and the game isn't cancelled.

**c)** ¬(p → q) is logically equivalent to:
(i) ¬p → ¬q  (ii) p ∧ ¬q  (iii) ¬p ∨ q  (iv) q → p

**d)** The premises are p → q and ¬q. Which conclusion is valid?
(i) p  (ii) ¬p  (iii) q  (iv) no conclusion follows

## Q2. Short answer [8]

**a)** [4] Let p = "it is raining" and q = "I carry an umbrella". Write in symbols:
 (i) I carry an umbrella only if it is raining.
 (ii) It is raining, but I do not carry an umbrella.

**b)** [3] For the conditional p → q, write its converse, inverse and contrapositive.

**c)** [1] Fill in the blank: ¬(p ∨ q) ≡ ______.

## Q3. Long answer: equivalence by identities [12]

Show, using logical identities and naming the law on every line, that

> ¬(p ∨ (¬p ∧ q)) ≡ ¬p ∧ ¬q

## Q4. Short answer: quantifiers [8]

**a)** [4] The domain is the integers. True or false?
 (i) ∀x (x² ≥ 0)
 (ii) ∃x (x² = 3)
 (iii) ∀x ∃y (y < x)
 (iv) ∃y ∀x (y < x)

**b)** [4] Negate each so the ¬ only touches predicates:
 (i) ∀x (P(x) → Q(x))
 (ii) ∃x ∀y (x + y = 0)

## Q5. Sets [14]

**a)** [4] A = {1, 3, 5, 7} and B = {3, 4, 5}. Find A ∪ B, A ∩ B, A − B, and |P(A ∩ B)|.

**b)** [3] True or false? (i) ∅ ⊆ A  (ii) {3} ∈ B  (iii) {3, 4} ⊆ B

**c)** [7] Long answer. Prove, using the definitions of the set operations and logical identities:

> A − (A − B) = A ∩ B

## Q6. Functions [14]

Let f: ℝ → ℝ, f(x) = −2x + 5.

**a)** [4] Prove f is one-to-one.
**b)** [4] Prove f is onto.
**c)** [2] Find f⁻¹.
**d)** [2] With f(x) = x + 3 and g(x) = 2x, compute (f ∘ g)(1) and (g ∘ f)(1).
**e)** [2] True or false: h: ℤ → ℤ, h(n) = 3n is one-to-one but not onto.

## Q7. Sequences and sums [6]

**a)** [2] Find a formula for a_n: 5, 8, 11, 14, ...
**b)** [2] Evaluate Σ (k=1 to 10) (2k + 1).
**c)** [2] Evaluate Σ (k=0 to 4) 3·2ᵏ.

## Q8. Countability [2] (one answer)

Which of these is **uncountable**?
(i) ℤ  (ii) ℚ  (iii) the positive odd integers  (iv) the interval (2, 5)

---
---

# ANSWER KEY (attempt first)

## Q1 [8]
a) **(ii)** p ∨ ¬p.
b) **(iii)**. The contrapositive of p → q is ¬q → ¬p.
c) **(ii)** p ∧ ¬q.
d) **(ii)** ¬p, by modus tollens.

## Q2 [8]
a) (i) **q → p** ("only if" puts the condition on the right). (ii) **p ∧ ¬q**.
b) Converse: **q → p**. Inverse: **¬p → ¬q**. Contrapositive: **¬q → ¬p**. (Only the contrapositive is equivalent to p → q.)
c) **¬p ∧ ¬q** (De Morgan's).

## Q3 [12]

| Step | Expression | Law |
|---|---|---|
| 1 | ¬(p ∨ (¬p ∧ q)) | Given |
| 2 | ¬p ∧ ¬(¬p ∧ q) | De Morgan's (outer) |
| 3 | ¬p ∧ (¬¬p ∨ ¬q) | De Morgan's (inner) |
| 4 | ¬p ∧ (p ∨ ¬q) | Double negation |
| 5 | (¬p ∧ p) ∨ (¬p ∧ ¬q) | Distributive |
| 6 | F ∨ (¬p ∧ ¬q) | Negation law (¬p ∧ p ≡ F) |
| 7 | ¬p ∧ ¬q | Identity law (F ∨ A ≡ A) ∎ |

## Q4 [8]
a) (i) **T**. (ii) **F** (no integer squares to 3). (iii) **T** (take y = x − 1). (iv) **F** (there is no smallest integer; also y < y fails).
b) (i) **∃x (P(x) ∧ ¬Q(x))**. (ii) **∀x ∃y (x + y ≠ 0)**.

## Q5 [14]
a) A ∪ B = {1, 3, 4, 5, 7}. A ∩ B = {3, 5}. A − B = {1, 7}. |P(A ∩ B)| = 2² = **4**.
b) (i) **T** (ii) **F** (the elements of B are 3, 4, 5, not the set {3}) (iii) **T**.
c) x ∈ A − (A − B)
⟺ x ∈ A ∧ x ∉ (A − B), definition of difference
⟺ x ∈ A ∧ ¬(x ∈ A ∧ x ∉ B), definition of difference
⟺ x ∈ A ∧ (x ∉ A ∨ x ∈ B), De Morgan's and double negation
⟺ (x ∈ A ∧ x ∉ A) ∨ (x ∈ A ∧ x ∈ B), distributive
⟺ F ∨ (x ∈ A ∧ x ∈ B), negation law
⟺ x ∈ A ∧ x ∈ B, identity law
⟺ x ∈ A ∩ B, definition of intersection. ∎

## Q6 [14]
a) Assume f(a) = f(b). Then −2a + 5 = −2b + 5. Subtract 5: −2a = −2b. Divide by −2: a = b. ∎
b) Let y ∈ ℝ. Solve y = −2x + 5: −2x = y − 5, so x = (5 − y)/2. This x is a real number, so it's in the domain. Check: f((5 − y)/2) = −2·(5 − y)/2 + 5 = −(5 − y) + 5 = y. ∎
c) f⁻¹(y) = **(5 − y)/2**.
d) (f ∘ g)(1) = f(g(1)) = f(2) = **5**. (g ∘ f)(1) = g(f(1)) = g(4) = **8**.
e) **True.** One-to-one: 3a = 3b gives a = b. Not onto: nothing maps to 1 (n would be 1/3, not an integer).

## Q7 [6]
a) Arithmetic, d = 3: **a_n = 3n + 2**.
b) Σ(2k + 1) = 2·Σk + Σ1 = 2·(10·11/2) + 10 = 110 + 10 = **120**.
c) Geometric, a = 3, r = 2, 5 terms: 3(2⁵ − 1)/(2 − 1) = 3·31 = **93**.

## Q8 [2]
**(iv)** the interval (2, 5). Intervals of real numbers are uncountable.

---

## Score yourself
Out of 72. Target 60+ in 70 minutes.
- Lost marks in Q3 or Q5c: redo the identity pattern (De Morgan's, shared part, q ∨ ¬q, identity). It is the same six-step pattern from Q2 of Practice Midterm 1.
- Lost marks in Q6: redo the three templates (assume f(a) = f(b); let y be arbitrary and solve for x; solve y = f(x) for x).
- Put every miss in the error log in [[Midterm Prep Plan]].
