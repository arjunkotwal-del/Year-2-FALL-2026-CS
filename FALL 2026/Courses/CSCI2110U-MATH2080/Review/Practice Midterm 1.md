---
tags: [review, midterm, practice-exam]
---

# Practice Midterm 1 (Lectures 1 to 9)

← [[Midterm Prep Plan]] | ← [[../CSCI2110U-MATH2080 - Discrete Math]]

> [!warning] How to use this
> 1. **Handwrite** every answer on paper. The real midterm is on paper (Thu Oct 22, 30%, includes proofs).
> 2. **Closed notes, timer on.** Part 1 = 60 min, Part 2 = 40 min. About 1 minute per mark.
> 3. Mark yourself with the answer key at the bottom, and put every miss in the error log in [[Midterm Prep Plan]].
> 4. The real paper's length and mark split are not confirmed. The instructor posts the topic list around Oct 15, so treat this as a drill and not a prediction.

---

## Textbook problems to do first (8th edition, from the instructor's slides)

These are the "honour homework" exercises. The odd answers are in the back of the book. Exact wording is in the Rosen PDF in `files/`.

| Lecture | Section | Exercises |
|---|---|---|
| L1 | §1.1 | 1, 3, 11, 15, 33, 47 |
| L1 | §1.2 | 35 |
| L2 | §1.3 | 1, 5, 7, 11, 19, 35 |
| L3 | §1.4 | 7, 9, 11, 15, 53 |
| L3 | §1.5 | 1, 9, 11, 27, 31 |
| L4 | §1.6 | 1, 3, 9, 19, 23, 29, 35 |
| L5 | §1.7 | 5, 9, 11, 29, 37, 41 |
| L6 | §1.8 | 1, 5, 25 |
| L7 | §2.1, 2.2 | see the L7 slide |
| L8 | §2.3 | 3, 5, 8 & 9, 10 & 11, 12 & 13, 31, 33, 37, 47, 65, 73 |
| L9 | §2.4 | 1, 3, 5, 9, 19, 25, 29, 31, 33, 35, 36, 39, 45 |
| L9 | §2.5 | 1, 3, 19 |

**Extra §1.6 practice** (same topic as Q5 to Q7 below): #5 (Randy), #13 and #14 (name the rule at each step), #15 and #16 (correct or incorrect), #23 (find the error).

The paper below is my own set of questions in the same style as these.

---

# PART 1: Logic and Proofs (Lectures 1 to 6), about 60 marks, 60 minutes

## Q1. Truth table [4]
Build the truth table for (p → q) ∧ (q → r) → (p → r). Is it a tautology, a contradiction, or a contingency?

## Q2. Simplify with laws [5]
Simplify ¬(p ∨ ¬q) ∨ (¬p ∧ ¬q) to a single short expression. Name the law used at every step.

## Q3. Translate [4]
Let p = "you study" and q = "you pass". Write in symbols:
- a) You study, but you do not pass.
- b) You pass only if you study.
- c) Studying is sufficient for passing.
- d) Write the **negation** of "If you study, then you pass" as an English sentence (no "it is not the case that").

## Q4. Quantifiers [8]
Domain for (a) is the integers.
- a) True or false? (i) ∀n ∃m (n + m = 0) (ii) ∃m ∀n (n + m = 0) (iii) ∀x ∃y (y > x²) (iv) ∃x (x² = 2)
- b) Negate ∀x ∃y (P(x,y) → Q(x,y)) so the ¬ only touches predicates.
- c) With S(x) = "x is a student", T(x) = "x is a professor", A(x,y) = "x has asked y a question", write "Every student has asked some professor a question."

## Q5. Rules of inference, formal proofs [10]
For each, write a table with columns **step, statement, reason**.
- a) [5] Premises: (1) p ∧ t (2) t → (p → q) (3) q → ¬r. Prove ¬r.
- b) [5] Premises: (1) ∀x (P(x) → Q(x)) (2) ∃x P(x). Prove ∃x Q(x).

## Q6. Valid or not? [6]
For each argument, say **valid** or **invalid**, and name the rule or the fallacy.
- a) If the program compiles, the tests run. The tests did not run. Therefore the program did not compile.
- b) If it is a bird, it has wings. This animal has wings. Therefore it is a bird.
- c) The bug is in the parser or in the lexer. The bug is not in the lexer. Therefore the bug is in the parser.

## Q7. Find the error [3]
This "proof" claims ∃x P(x) ∧ ∃x Q(x) implies ∃x (P(x) ∧ Q(x)). What is wrong with it?

| Step | Statement | Reason |
|---|---|---|
| 1 | ∃x P(x) ∧ ∃x Q(x) | Premise |
| 2 | ∃x P(x) | Simplification (1) |
| 3 | P(c) | EI (2) |
| 4 | ∃x Q(x) | Simplification (1) |
| 5 | Q(c) | EI (4) |
| 6 | P(c) ∧ Q(c) | Conjunction (3, 5) |
| 7 | ∃x (P(x) ∧ Q(x)) | EG (6) |

## Q8. Proofs [22]
State your technique first. Use n = 2k for even, n = 2k + 1 for odd.
- a) [4] **Direct:** If n is odd, then n² + n is even.
- b) [4] **Contraposition:** If 3n + 2 is even, then n is even.
- c) [4] **Contradiction:** The sum of a rational number and an irrational number is irrational.
- d) [4] **Cases:** For every integer n, n² ≥ n.
- e) [6] **Biconditional:** n² + 3 is odd if and only if n is even.

---

# PART 2: Sets, Functions, Sequences (Lectures 7 to 9), about 40 marks, 40 minutes

> [!tip] Don't start Part 2 until you've worked through the L7, L8, L9 notes.

## Q9. Sets [14]
- a) [3] A = {1, 2, 3, 4}, B = {3, 4, 5}. Find A ∪ B, A ∩ B, A − B, B − A, and |P(B)|.
- b) [3] True or false? (i) ∅ ∈ P(A) (ii) {1} ∈ {1, 2} (iii) {1} ⊆ {1, 2}
- c) [2] In a class of 40 students, 25 take CS, 18 take Math, and 8 take both. How many take neither?
- d) [6] **Element proof:** Prove (A ∩ B) ∪ (A − B) = A.

## Q10. Functions [14]
f: ℝ → ℝ, f(x) = 5x − 3.
- a) [3] Prove f is one-to-one.
- b) [3] Prove f is onto.
- c) [3] Find f⁻¹.
- d) [3] With f(x) = 2x + 1 and g(x) = x², compute (g ∘ f)(2) and (f ∘ g)(2).
- e) [2] Show that h: ℤ → ℤ, h(n) = n², is neither one-to-one nor onto.

## Q11. Sequences, sums, cardinality [12]
- a) [2] Find a formula for a_n: 7, 11, 15, 19, ...
- b) [3] Evaluate Σ (k=1 to 20) (3k − 2).
- c) [3] Evaluate Σ (k=0 to 6) 2·3^k.
- d) [4] Prove that the set of negative integers is countable.

---
---

# ANSWER KEY (attempt first, then mark)

## Part 1

**Q1.** Rows (p q r): the whole thing is T in all 8 rows.

| p | q | r | p→q | q→r | (p→q)∧(q→r) | p→r | whole |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | T | F | T | F | F | F | T |
| T | F | T | F | T | F | T | T |
| T | F | F | F | T | F | F | T |
| F | T | T | T | T | T | T | T |
| F | T | F | T | F | F | T | T |
| F | F | T | T | T | T | T | T |
| F | F | F | T | T | T | T | T |

**Tautology** (this is hypothetical syllogism written as a formula). The only rows where the left side is T have p → r true as well.

**Q2.**
¬(p ∨ ¬q) ∨ (¬p ∧ ¬q)
≡ (¬p ∧ ¬¬q) ∨ (¬p ∧ ¬q), De Morgan
≡ (¬p ∧ q) ∨ (¬p ∧ ¬q), double negation
≡ ¬p ∧ (q ∨ ¬q), distributive (factor out ¬p)
≡ ¬p ∧ T, negation law (q ∨ ¬q ≡ T)
≡ **¬p**, identity law

**Q3.** a) p ∧ ¬q  b) q → p ("pass only if study" means passing requires studying, so the "only if" part, p, goes on the right)  c) p → q  d) "You study, and you do not pass." (¬(p → q) ≡ p ∧ ¬q.)

**Q4.**
a) (i) **T** (m = −n). (ii) **F** (no single m works for every n). (iii) **T** (y = x² + 1). (iv) **F**.
b) **∃x ∀y (P(x,y) ∧ ¬Q(x,y))**. Flip each quantifier, then ¬(a → b) ≡ a ∧ ¬b.
c) **∀x (S(x) → ∃y (T(y) ∧ A(x,y)))**. With ∀ use →, with ∃ use ∧.

**Q5.**
a)
| Step | Statement | Reason |
|---|---|---|
| 1 | p ∧ t | Premise |
| 2 | t → (p → q) | Premise |
| 3 | q → ¬r | Premise |
| 4 | p | Simplification (1) |
| 5 | t | Simplification (1) |
| 6 | p → q | Modus ponens (5, 2) |
| 7 | q | Modus ponens (4, 6) |
| 8 | ¬r | Modus ponens (7, 3) |

b)
| Step | Statement | Reason |
|---|---|---|
| 1 | ∀x (P(x) → Q(x)) | Premise |
| 2 | ∃x P(x) | Premise |
| 3 | P(c) | EI (2), c is a new name |
| 4 | P(c) → Q(c) | UI (1) |
| 5 | Q(c) | Modus ponens (3, 4) |
| 6 | ∃x Q(x) | EG (5) |

**Q6.** a) **Valid**, modus tollens. b) **Invalid**, affirming the conclusion (other animals have wings). c) **Valid**, disjunctive syllogism.

**Q7.** Step 5 reuses the name c. The EI at step 5 needs a **new** name, say d, giving Q(d). Then you only get P(c) ∧ Q(d), and you can't combine them into one x. In fact the conclusion doesn't follow: some x can be P and a different x can be Q.

**Q8.**
a) **Direct.** Let n = 2k + 1. Then n² + n = (4k² + 4k + 1) + (2k + 1) = 4k² + 6k + 2 = 2(2k² + 3k + 1), which is even. ∎

b) **Contraposition.** Contrapositive: if n is odd, then 3n + 2 is odd. Let n = 2k + 1. Then 3n + 2 = 6k + 3 + 2 = 6k + 5 = 2(3k + 2) + 1, which is odd. ∎

c) **Contradiction.** Let r be rational and x irrational. Suppose r + x is rational, say r + x = s. Then x = s − r, which is a difference of two rationals, so x is rational. This contradicts x being irrational. So r + x is irrational. ∎

d) **Cases.** Case 1: n ≥ 1. Then n² = n·n ≥ n·1 = n. Case 2: n ≤ 0. Then n² ≥ 0 ≥ n. The two cases cover every integer. ∎

e) **Biconditional.**
(⇒) Claim: if n² + 3 is odd, then n is even. Use contraposition: if n is odd, then n² + 3 is even. Let n = 2k + 1. Then n² + 3 = 4k² + 4k + 1 + 3 = 4k² + 4k + 4 = 2(2k² + 2k + 2), which is even. ✓
(⇐) Claim: if n is even, then n² + 3 is odd. Let n = 2k. Then n² + 3 = 4k² + 3 = 2(2k² + 1) + 1, which is odd. ✓
Both directions are proved, so the biconditional holds. ∎

## Part 2

**Q9.**
a) A ∪ B = {1,2,3,4,5}. A ∩ B = {3,4}. A − B = {1,2}. B − A = {5}. |P(B)| = 2³ = 8.
b) (i) **True** (∅ is a subset of every set). (ii) **False** (the elements of {1,2} are 1 and 2). (iii) **True**.
c) Take CS or Math = 25 + 18 − 8 = 35. Neither = 40 − 35 = **5**.
d) x ∈ (A ∩ B) ∪ (A − B)
⟺ (x ∈ A ∧ x ∈ B) ∨ (x ∈ A ∧ x ∉ B), definitions
⟺ x ∈ A ∧ (x ∈ B ∨ x ∉ B), factor out x ∈ A
⟺ x ∈ A ∧ T
⟺ x ∈ A. ∎

**Q10.**
a) Assume f(a) = f(b). Then 5a − 3 = 5b − 3, so 5a = 5b, so a = b. ∎
b) Let y ∈ ℝ. Take x = (y + 3)/5. Then f(x) = 5·(y + 3)/5 − 3 = y. ∎
c) y = 5x − 3, so x = (y + 3)/5. **f⁻¹(y) = (y + 3)/5.** (f is a bijection, so the inverse exists.)
d) (g ∘ f)(2) = g(f(2)) = g(5) = **25**. (f ∘ g)(2) = f(g(2)) = f(4) = **9**.
e) Not one-to-one: h(2) = h(−2) = 4 but 2 ≠ −2. Not onto: nothing maps to 2, since n² = 2 has no integer solution. ∎

**Q11.**
a) Arithmetic with d = 4: **a_n = 4n + 3** (n = 1 gives 7).
b) Σ(3k − 2) = 3·Σk − 2·20 = 3·(20·21/2) − 40 = 3·210 − 40 = **590**.
c) Geometric, a = 2, r = 3, 7 terms: 2·(3⁷ − 1)/(3 − 1) = 2·(2186)/2 = **2186**.
d) Define f: ℤ⁺ → {negative integers}, f(n) = −n.
One-to-one: f(a) = f(b) gives −a = −b, so a = b.
Onto: for any negative integer m, −m is a positive integer and f(−m) = m.
So f is a bijection and the negative integers are countable. ∎

---

## Score yourself
Part 1 (62 marks) and Part 2 (40 marks).
- Missed Q1 to Q3: redo [[../Week 1/Lecture 1/Notes]] and [[../Week 2/Lecture 1/Notes]].
- Missed Q4 or Q7: quantifier rules, especially "EI needs a new name".
- Missed Q8: look at which technique you chose. That's your recurring weak spot.
- Missed Part 2: redo the matching notes in `Week 4/Lecture 2`, `Week 5/Lecture 1`, `Week 5/Lecture 2`.
