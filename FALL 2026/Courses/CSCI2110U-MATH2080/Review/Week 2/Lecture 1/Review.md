---
tags: [review, week2, lecture1]
---

# Review — Week 2 / Lecture 1 (Propositional Equivalences, §1.3 — course Lecture 2)

← [[../../../Week 2/Lecture 1/Notes|Full Notes]] | [[../../../Week 2/Lecture 1/Questions|Questions]] | ← [[../../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] What this is
> A short list of exactly what to re-drill from this lecture. If any line below feels shaky, jump back to the linked Notes section before moving on.

## What to review

1. **Tautology vs. contradiction vs. contingency** — definitions, plus the shortcut: `(anything) ∨ T` or `X ∨ ¬X` inside a formula → automatic tautology. But watch for the trap: confirm any "T" you see is actually the fixed true-constant and not just another variable letter before applying the shortcut (this bit you personally — worth re-testing).
2. **De Morgan's Laws**, both directions, and applying them to negate English sentences (not just symbols) — "p and q" negates to "not p OR not q," never "not p AND not q."
3. **Conditional-disjunction equivalence**: p → q ≡ ¬p ∨ q. This is the bridge move used in almost every algebraic proof involving →.
4. **The full equivalence table** (identity, domination, idempotent, double negation, commutative, associative, distributive, De Morgan's, absorption, negation laws) — not memorized word-for-word, but recognized by shape when it appears mid-proof.
5. **Chaining equivalences to prove a tautology or simplify an expression**, citing one law per line — this is the actual exam skill, more than truth tables once variable count grows.
6. **Contrapositive equivalence**: ¬q→¬p ≡ p→q — confirmed as instructor-emphasized (appears on his slide verbatim, and repeats the converse/inverse trap from Lecture 1).
7. **Satisfiable vs. unsatisfiable** — satisfiable needs just one working assignment; unsatisfiable needs an argument that *every* assignment fails.

## Quick self-check
- [x] Can you state both De Morgan's laws and apply one to a plain English sentence in under 30 seconds? ✅ 2026-09-15
- [x] Can you simplify a 3-4 step expression using named laws, one per line, without a truth table? ✅ 2026-09-15
- [ ] Do you know why `(p∧q)∨T` is a tautology but `(p∧q)∨T` where T is a *variable* (not the constant) is not?
- [ ] Can you prove `(p→q)∧(q→r) → (p→r)` is a tautology via equivalence chain (not truth table)?

If any box is unchecked, redo [[../../../Week 2/Lecture 1/Questions|Questions.md]] Q7, Q19, and the bonus simplification problem before the next test.

## Cross-lecture note
Both Week 1 Lecture 1 and this lecture separately flag the same mistake: **converse/inverse ≠ original conditional, only contrapositive is equivalent.** If this shows up a third time, treat it as a guaranteed test question.
