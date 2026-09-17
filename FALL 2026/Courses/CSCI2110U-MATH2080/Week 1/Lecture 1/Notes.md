---
tags: [notes, week1, lecture1, propositional-logic]
---

# Lecture 1 — Propositional Logic (Section 1.1)

← [[CSCI2110U-MATH2080 - Discrete Math]] | Slide source: [[../../files/MATH2080_Lecture1_Sections_1p1_PropLogic.pdf]] | Textbook: [[../../files/Rosen - Discrete Mathematics and Its Applications (8th ed).pdf]] (Section 1.1, pages 1–17)

> [!info] What this covers
> Propositions, connectives, truth tables, conditionals (converse/inverse/contrapositive), translating English → logic, bit operations.

---

## 1. What is a proposition?

**Definition:** A *declarative sentence* that is either true or false — not both, not neither.

✅ Propositions: "Toronto is in Canada" (T), "2 + 2 = 5" (F)
❌ Not propositions: "What time is it?" (question), "x + 1 = 2" (depends on x — not fixed true/false until x is given)

We encode them with lowercase letters: `p, q, r, s, ...`
True/False encoded as `T`/`F` or `1`/`0`.

---

## 2. The six connectives

| Name | Symbol | Read as |
|---|---|---|
| Negation | ¬p | "not p" |
| Conjunction | p ∧ q | "p and q" |
| Disjunction | p ∨ q | "p or q" (inclusive) |
| Exclusive or | p ⊕ q | "p xor q" |
| Conditional | p → q | "if p then q" |
| Biconditional | p ↔ q | "p if and only if q" |

**Example set-up** (used throughout): p = "I just won the lottery," q = "I am buying everyone a pony."

- ¬p: "I did not just win the lottery."
- p ∧ q: "I just won the lottery and I am buying everyone a pony."
- p ∨ q: "I just won the lottery or I am buying everyone a pony" (or both — inclusive or).
- p ⊕ q: "Exactly one of: I won the lottery / I'm buying everyone a pony" — not both.

---

## 3. Truth tables for the connectives

**Negation:**

| p | ¬p |
|---|---|
| T | F |
| F | T |

**Conjunction / Disjunction / XOR:**

| p | q | p∧q | p∨q | p⊕q |
|---|---|---|---|---|
| T | T | T | T | F |
| T | F | F | T | T |
| F | T | F | T | T |
| F | F | F | F | F |

**Conditional p → q** — the one everyone gets wrong:

| p | q | p → q |
|---|---|---|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

> [!tip] Why is F → anything true?
> A conditional is a *promise*: "if p, then q." The promise is only **broken** when p happens and q doesn't. If p never happens (p is F), the promise was never tested — so it's vacuously true. "If Juan has a smartphone, then 2+3=5" is TRUE if Juan has no smartphone, no matter how false "2+3=5" is.

**Biconditional p ↔ q** — true exactly when p and q match:

| p | q | p ↔ q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

---

## 4. Conditional statements — converse, inverse, contrapositive

Given `p → q`:

| Name | Formula | Relation to original |
|---|---|---|
| **Converse** | q → p | swap p and q |
| **Inverse** | ¬p → ¬q | negate both, keep order |
| **Contrapositive** | ¬q → ¬p | swap AND negate |

> [!important] The one fact you must memorize
> `p → q` and its **contrapositive** `¬q → ¬p` are **logically equivalent** — always the same truth value. The converse and inverse are equivalent *to each other*, but **not** to the original. Assuming converse = original is one of the most common logic errors (and shows up constantly in proofs later this course, e.g. contrapositive proofs in [[Section 1.7-1.8]]).

**Worked example:** "The home team wins whenever it is raining."

Rewrite first: "If it is raining, then the home team wins." → p = raining, q = home team wins. So `p → q`.

- **Contrapositive** (¬q → ¬p): "If the home team does not win, then it is not raining." ✅ equivalent to original
- **Converse** (q → p): "If the home team wins, then it is raining." ⚠️ not equivalent
- **Inverse** (¬p → ¬q): "If it is not raining, then the home team does not win." ⚠️ not equivalent

---

## 5. Translating English → logic

**Key phrases for `p → q`:** "if p, then q," "q whenever p," "q if p," "p is sufficient for q," "q is necessary for p," "p only if q."

> [!warning] "Only if" is the trap
> "p only if q" translates to `p → q`, **not** `q → p`. Say it slowly: "You can graduate only if you pass the exam" means passing is *required* (necessary) for graduating — graduating (p) forces passing (q) to be true. So p → q.

**Worked example:** "You cannot ride the roller coaster if you are under 4 feet tall unless you are older than 16 years old."

- q = "You can ride the roller coaster," r = "You are under 4 feet tall," s = "You are older than 16"
- "Unless" ≈ "if not" — so "you cannot ride *unless* s" means: if ¬s, then you cannot ride, given the height condition.
- Formula: `(r ∧ ¬s) → ¬q`

---

## 6. Truth tables of compound propositions

**Bookkeeping rule:** n variables → 2ⁿ rows. Alphabetical column order. Column for variable *i* (1-indexed) alternates blocks of 2ⁿ⁻ⁱ T's then F's.
- 3 variables (p,q,r) → 8 rows: p is TTTTFFFF, q is TTFFTTFF, r is TFTFTFTF.

**Worked example:** Build the truth table for `(p ∨ ¬q) → (p ∧ q)`

| p | q | ¬q | p∨¬q | p∧q | (p∨¬q)→(p∧q) |
|---|---|---|---|---|---|
| T | T | F | T | T | T |
| T | F | T | T | F | **F** |
| F | T | F | F | F | T |
| F | F | T | T | F | **F** |

Build it column by column, left to right — never try to jump straight to the final column.

---

## 7. Operator precedence

When parentheses are dropped, apply in this order:

1. ¬ (negation) — highest
2. ∧ (and)
3. ∨ (or)
4. → (conditional)
5. ↔ (biconditional) — lowest

So `p → q ∨ r` means `p → (q ∨ r)`, and `¬p ∧ q` means `(¬p) ∧ q`.

> [!tip] Exam habit
> Even though precedence rules exist, **use parentheses anyway** when writing your own formulas — it removes all ambiguity and costs you nothing.

---

## 8. Bit strings and bit operations

A **bit string** is a sequence of 0s/1s (1 = true, 0 = false). Apply connectives bit-by-bit (same length required): OR (∨), AND (∧), XOR (⊕).

**Worked example:** x = 0110 1011, y = 1110 0001 *(illustrative — see [[Questions#Q47|Q47]] for the actual homework pairs)*

```
  0110 1011
  1110 0001
  ---------
  1110 1011   OR   (1 if either bit is 1)
  0110 0001   AND  (1 only if both bits are 1)
  1000 1010   XOR  (1 only if bits differ)
```

---

## Summary checklist
- [x] Can build a truth table from scratch for any connective, unaided ✅ 2026-09-15
- [x] Know p → q is false in exactly one case (T,F) ✅ 2026-09-15
- [x] Can produce converse/inverse/contrapositive without looking it up, and know only contrapositive is equivalent ✅ 2026-09-15
- [x] Comfortable translating "only if," "unless," "sufficient," "necessary" into formulas ✅ 2026-09-15
- [x] Can do bitwise OR/AND/XOR by hand ✅ 2026-09-15

**Next:** → [[Questions]] (Week 1 honour homework)
