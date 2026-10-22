---
tags: [practice, week4, lecture2, sets]
---

# Lecture 7: Practice Questions (Sets)

← [[Notes]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Honour homework for this lecture (8th edition, from the slide)
> **§2.1:** #1, 9, 11, 13, 19, 21, 25, 33, 37, 47
> **§2.2:** #3, 7, 15, 21, 27, 29, 33, 53, 57, 59, 61
> (7th ed: §2.1 #1, 7, 9, 11, 17, 19, 23, 31, 35, 43; §2.2 #3, 7, 15, 19, 25, 27, 31, 47, 51, 53, 55.) Odd-numbered answers are in the back of the textbook. Skip any membership-table problems.

Do these on paper first, then check the answers at the bottom.

---

## Part A: Quick questions (test style)

**1.** With A = {1, 3, 5, 7}, select ALL true statements:
a) 3 ∈ A  b) {3} ⊆ A  c) 3 ⊆ A  d) ∅ ⊆ A  e) {3} ∈ A

**2.** Fill in: |P({a,b,c})| = ____. If |A| = 3 and |B| = 2 then |A × B| = ____. |P(∅)| = ____.

**3.** List the elements of {x ∈ ℤ | x² − 3x ≤ 4}.

**4.** Write x ∈ A − (B ∪ C) as a logical statement with no set operations.

**5.** True or False: {∅} = ∅.

**6.** List all elements of P({1, 2}).

**7.** If |A| = 12, |B| = 20 and |A ∩ B| = 5, then |A ∪ B| = ____.

**8.** U = {1,...,8}, A = {1, 2, 5}, B = {2, 5, 8}. Write A and B as bit strings, then give A ∩ B and A ∪ B as bit strings and as sets.

**9.** Of 80 students, 45 take CS, 30 take Math and 12 take both. How many take neither?

**10.** Select ALL that are true for every pair of sets A, B:
a) A ∩ B ⊆ A  b) A ⊆ A ∪ B  c) A − B = B − A  d) A ∪ ∅ = A  e) A ∩ Ā = U

**11.** The complement of (A ∪ B) equals:
a) Ā ∪ B̄  b) Ā ∩ B̄  c) A ∩ B  d) Ā − B̄

**12.** For A = {1, 2} and B = {x, y}, list A × B. Is A × B = B × A?

---

## Part B: Set proofs (midterm style, write them out)

**P1.** Prove A − (B ∪ C) = (A − B) ∩ (A − C) using a chain of logical equivalences.

**P2.** Prove A ∩ (A ∪ B) = A.

**P3.** Prove that if A ⊆ B, then A ∩ C ⊆ B ∩ C.

**P4.** Prove that A ⊆ B if and only if A ∪ B = B.

---
---

## ANSWERS

### Part A

**1. a, b, d.** (3 ⊆ A is nonsense, 3 is not a set. {3} ∈ A is false, {3} isn't an element of A. ∅ ⊆ A is true for every set.)

**2.** 8 (2³). 6 (3·2). 1 (P(∅) = {∅}, one element).

**3.** x² − 3x − 4 ≤ 0 ⟺ (x − 4)(x + 1) ≤ 0 ⟺ −1 ≤ x ≤ 4. Integers: **{−1, 0, 1, 2, 3, 4}**.

**4.** x ∈ A ∧ ¬(x ∈ B ∨ x ∈ C) ≡ **x ∈ A ∧ x ∉ B ∧ x ∉ C** (De Morgan).

**5. False.** {∅} has one element (the empty set), and ∅ has zero elements.

**6.** **{∅, {1}, {2}, {1, 2}}**

**7.** 12 + 20 − 5 = **27**

**8.** A = 11001000, B = 01001001. A ∩ B (bitwise AND) = 01001000 = **{2, 5}**. A ∪ B (bitwise OR) = 11001001 = **{1, 2, 5, 8}**.

**9.** |CS ∪ Math| = 45 + 30 − 12 = 63. Neither = 80 − 63 = **17**.

**10. a, b, d.** (c is false: A − B and B − A are usually different. e is false: A ∩ Ā = ∅, not U.)

**11. b.** De Morgan: complement of (A ∪ B) = Ā ∩ B̄.

**12.** A × B = **{(1,x), (1,y), (2,x), (2,y)}**. A × B ≠ B × A, because (1,x) is in A × B but is not in B × A (order matters).

### Part B

**P1.** Let x be arbitrary.

x ∈ A − (B ∪ C)
≡ x ∈ A ∧ ¬(x ∈ B ∪ C) [definition of −]
≡ x ∈ A ∧ ¬(x ∈ B ∨ x ∈ C) [definition of ∪]
≡ x ∈ A ∧ (x ∉ B ∧ x ∉ C) [De Morgan]
≡ (x ∈ A ∧ x ∉ B) ∧ (x ∈ A ∧ x ∉ C) [idempotent: duplicate "x ∈ A", then regroup]
≡ x ∈ (A − B) ∧ x ∈ (A − C) [definition of −]
≡ x ∈ (A − B) ∩ (A − C) [definition of ∩]

Since x was arbitrary, the sets are equal. ∎

**P2.** Let x be arbitrary.

x ∈ A ∩ (A ∪ B)
≡ x ∈ A ∧ (x ∈ A ∨ x ∈ B) [definitions of ∩ and ∪]
≡ x ∈ A [absorption law: p ∧ (p ∨ q) ≡ p]

So A ∩ (A ∪ B) = A. ∎

**P3.** Assume A ⊆ B. Let x ∈ A ∩ C. Then x ∈ A and x ∈ C. Since A ⊆ B and x ∈ A, we get x ∈ B. So x ∈ B and x ∈ C, which means x ∈ B ∩ C. Therefore A ∩ C ⊆ B ∩ C. ∎

**P4.** An "if and only if" needs both directions.

**(⇒)** Assume A ⊆ B. We show A ∪ B = B by two containments.
- B ⊆ A ∪ B always holds.
- Let x ∈ A ∪ B. Then x ∈ A or x ∈ B. If x ∈ A, then x ∈ B because A ⊆ B. If x ∈ B, we're done. Either way x ∈ B, so A ∪ B ⊆ B.
So A ∪ B = B.

**(⇐)** Assume A ∪ B = B. Let x ∈ A. Then x ∈ A ∪ B (by definition of union), and A ∪ B = B, so x ∈ B. Therefore A ⊆ B. ∎

---

## Score yourself
Part A: 1 point each (question 2 is 3). Anything you miss, re-read that section of [[Notes]]. For Part B, check you (a) started from an arbitrary x or an arbitrary element, (b) justified every step with a named law, and (c) finished with a concluding sentence.
