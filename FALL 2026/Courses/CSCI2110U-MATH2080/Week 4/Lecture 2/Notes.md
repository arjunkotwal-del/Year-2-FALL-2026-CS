---
tags: [notes, week4, lecture2, sets]
---

# Lecture 7: Sets and Set Operations (Sections 2.1-2.2)

← [[../../CSCI2110U-MATH2080 - Discrete Math]] | [[Questions]]
Source: [[../../files/MATH2080_Lecture7_Sections_2p1_2p2_Sets_and_Set_operations_filled.pdf]] (instructor's filled-in version, Oct 1)

> [!info] What the instructor said is NOT tested
> Membership tables (the 0/1 tables for set identities) are marked **NOT TESTED** on his slide. Skip them. Proving identities with logic chains IS fair game.

---

## 1. Basics

- A **set** is an unordered collection of elements. Order and repeats don't matter: {1,3,5,7} = {1,7,3,5}.
- 3 ∈ A means "3 is an element of A". 4 ∉ A means "4 is not an element of A".
- **Standard sets:**
  - ℕ = {0, 1, 2, ...} (**0 IS included in this course**)
  - ℤ = {0, ±1, ±2, ...}
  - ℤ+ = {1, 2, 3, ...}
  - ℚ = rationals, ℝ = reals
  - ∅ = {} = the empty set

## 2. Subsets

**A ⊆ B** iff ∀x (x ∈ A → x ∈ B). A ⊊ B means proper (strict) subset: A ⊆ B but A ≠ B.

**Don't confuse ∈ and ⊆.** With A = {1,3,5,7}:
| Statement | True? | Why |
|---|---|---|
| 3 ∈ A | yes | 3 is an element |
| 3 ⊆ A | nonsense | 3 is not a set |
| {3} ⊆ A | yes | the set {3} has only elements of A |
| {3} ∈ A | no | {3} is not one of A's elements |
| ∅ ⊆ A | yes | "x ∈ ∅ → x ∈ A" has a false hypothesis, so it's vacuously true |

For every set A: ∅ ⊆ A and A ⊆ A.

**Set equality:** A = B iff A ⊆ B and B ⊆ A (prove both directions).

## 3. Cardinality

|A| = number of elements. |{a,b,c}| = 3. |ℤ+| is infinite.

## 4. Set-builder notation

{x ∈ ℕ | x³ ≤ 10} = {0, 1, 2}

Read it as: "the set of x in ℕ **such that** x³ ≤ 10". The part before | says where x lives, the part after is the condition.

**The universe matters:**
- {x ∈ ℝ | x² − 3x ≤ 4} = [−1, 4] (an interval; x²−3x−4 ≤ 0 has roots −1 and 4)
- {x ∈ ℤ | x² − 3x ≤ 4} = {−1, 0, 1, 2, 3, 4}

## 5. Power set

P(A) = the set of ALL subsets of A (including ∅ and A itself). **|P(A)| = 2^|A|.**

- P(∅) = {∅} (1 subset)
- P({a}) = {∅, {a}} (2 subsets)
- P({a,b}) = {∅, {a}, {b}, {a,b}} (4 subsets)
- P(P(∅)) = P({∅}) = {∅, {∅}}
- P(P(P(∅))) = {∅, {∅}, {{∅}}, {∅,{∅}}}

## 6. Cartesian product

A × B = all **ordered pairs** (a, b) with a ∈ A and b ∈ B. **|A × B| = |A|·|B|.**

A = {a,b,c}, B = {−1,1}: A × B = {(a,−1),(a,1),(b,−1),(b,1),(c,−1),(c,1)}, so |A×B| = 3·2 = 6.

Order matters: (a,b) ≠ (b,a) unless a = b.

## 7. Truth set of a predicate

The set of all x in the universe that make P(x) true. ℝ+ is the truth set of P(x): x > 0. Solving x² − 3x = 4 means finding the truth set of that predicate.

---

## 8. Set operations

| Operation | Notation | Meaning | Logic translation |
|---|---|---|---|
| Union | A ∪ B | in A, in B, or both | x ∈ A ∨ x ∈ B |
| Intersection | A ∩ B | in both | x ∈ A ∧ x ∈ B |
| Difference | A − B | in A but not in B | x ∈ A ∧ x ∉ B |
| Complement | Ā (or A^c) | U − A, everything not in A | x ∉ A, i.e. ¬(x ∈ A) |

- A and B are **disjoint** if A ∩ B = ∅ (e.g. evens and odds).
- Examples: A = {1,3,5}, B = {2,3,4}: A ∪ B = {1,2,3,4,5}, A ∩ B = {3}, A − B = {1,5}, B − A = {2,4}.
- ℝ − ℚ = the irrationals. A ∪ ∅ = A. A ∩ ∅ = ∅.

> [!important] The key trick
> Every set statement can be turned into a LOGIC statement about "x ∈ ...". So set identities are proved with the logic rules you already know (De Morgan, distributive, etc.).

**Example:** x ∈ A ∪ (B − C) ≡ x ∈ A ∨ (x ∈ B ∧ x ∉ C)

## 9. Set identities (same names as the logic laws)

| Law | Identity |
|---|---|
| Identity | A ∩ U = A, A ∪ ∅ = A |
| Domination | A ∪ U = U, A ∩ ∅ = ∅ |
| Idempotent | A ∪ A = A, A ∩ A = A |
| Complementation | (Ā)‾ = A |
| Commutative | A ∪ B = B ∪ A, A ∩ B = B ∩ A |
| Associative | A ∪ (B ∪ C) = (A ∪ B) ∪ C (same for ∩) |
| Distributive | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C), A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| De Morgan | complement of (A ∩ B) = Ā ∪ B̄, complement of (A ∪ B) = Ā ∩ B̄ |
| Absorption | A ∪ (A ∩ B) = A, A ∩ (A ∪ B) = A |
| Complement | A ∪ Ā = U, A ∩ Ā = ∅ |

## 10. Proving a set identity (the method)

To show X = Y: pick an **arbitrary x** and show x ∈ X ⟺ x ∈ Y by a chain of logical equivalences. (Or prove X ⊆ Y and Y ⊆ X.)

**Worked example: prove A − (B − C) = (A − B) ∪ (A ∩ C).**

Let x be arbitrary.
| Step | Statement | Reason |
|---|---|---|
| 1 | x ∈ A − (B − C) | start |
| 2 | ≡ x ∈ A ∧ ¬(x ∈ B − C) | definition of − |
| 3 | ≡ x ∈ A ∧ ¬(x ∈ B ∧ x ∉ C) | definition of − |
| 4 | ≡ x ∈ A ∧ (x ∉ B ∨ ¬¬(x ∈ C)) | De Morgan |
| 5 | ≡ x ∈ A ∧ (x ∉ B ∨ x ∈ C) | double negation |
| 6 | ≡ (x ∈ A ∧ x ∉ B) ∨ (x ∈ A ∧ x ∈ C) | distributive |
| 7 | ≡ x ∈ (A − B) ∨ x ∈ (A ∩ C) | definitions of − and ∩ |
| 8 | ≡ x ∈ (A − B) ∪ (A ∩ C) | definition of ∪ |

Since x was arbitrary, the two sets are equal. ∎

**Containment proof pattern (A ⊆ B):** "Let x ∈ A. [reason]. So x ∈ B. Hence A ⊆ B."

## 11. Generalized union and intersection

For i = 1, 2, ...: A_i = {i, i+1, ..., 2i}.
- A_2 = {2,3,4}, A_3 = {3,4,5,6}, A_4 = {4,5,6,7,8}
- ∩ from i=2 to 4 of A_i = A_2 ∩ A_3 ∩ A_4 = **{4}**
- ∪ from i=1 to ∞ of A_i = A_1 ∪ A_2 ∪ ... = **ℤ+**

## 12. Computer representation (bit strings)

With universal set U = {1,...,10}: A = {1,3,5,6} becomes 1010110000, B = {3,6,9} becomes 0010010010. (A 1 in position i means i is in the set.)
- **A ∪ B = bitwise OR:** 1010110010 = {1,3,5,6,9}
- **A ∩ B = bitwise AND:** 0010010000 = {3,6}

## 13. Inclusion-Exclusion

**|A ∪ B| = |A| + |B| − |A ∩ B|** (subtract the overlap so it isn't counted twice).

**Example:** 200 students, 50 take MATH, 140 take CSCI, 24 take both. Students with an exam = 50 + 140 − 24 = 166. At the pub night (no exam): 200 − 166 = **34**.

---

## Summary checklist
- [ ] Know ∈ vs ⊆ and why ∅ ⊆ A is always true
- [ ] Can list the power set of a small set and know |P(A)| = 2^|A|
- [ ] Can write A × B and know |A × B| = |A||B|
- [ ] Can translate a set expression (A − (B ∪ C)) into logic (x ∈ A ∧ x ∉ B ∧ x ∉ C)
- [ ] Can prove a set identity with an arbitrary-x chain of equivalences
- [ ] Can do bit-string union/intersection and inclusion-exclusion word problems

**Next:** [[Questions]]
