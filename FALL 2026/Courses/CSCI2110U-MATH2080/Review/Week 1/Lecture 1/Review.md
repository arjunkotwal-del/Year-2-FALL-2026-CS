---
tags: [review, week1, lecture1]
---

# Review — Week 1 / Lecture 1 (Propositional Logic, §1.1)

← [[../../../Week 1/Lecture 1/Notes|Full Notes]] | [[../../../Week 1/Lecture 1/Questions|Questions]] | ← [[../../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] What this is
> A short list of exactly what to re-drill from this lecture — not the full notes again. If any line below feels shaky, jump back to the linked Notes section before moving on.

## What to review

1. **Truth tables for all six connectives** — ¬, ∧, ∨, ⊕, →, ↔. Be able to write any of them from memory, no lookup.
2. **Conditional p → q is false in exactly one case** (T,F). This trips people up more than anything else in this section — redo the "contract" reasoning if it doesn't feel automatic.
3. **Converse / Inverse / Contrapositive** — know all three definitions cold, and remember: only the **contrapositive** is logically equivalent to the original. Converse/inverse are NOT — this is a confirmed instructor trap (flagged again in Lecture 2).
4. **"Only if" translation trap** — "p only if q" → p→q, not q→p. Re-do the roller coaster example if unsure.
5. **Operator precedence order**: ¬, ∧, ∨, →, ↔ (tightest to loosest). Practice fully parenthesizing a formula with all five operators in one expression — this was the topic you said you didn't understand initially, worth a fresh attempt cold before checking your old work.
6. **Truth table bookkeeping** — n variables → 2ⁿ rows, alphabetical columns, i-th variable alternates in blocks of 2ⁿ⁻ⁱ.
7. **Bitwise OR/AND/XOR** by hand on two bit strings.

## Quick self-check
- [x] Can you build the p→q truth table from memory in under 10 seconds? ✅ 2026-09-15
- [x] Given a random p→q sentence, can you produce converse/inverse/contrapositive without writing the definitions down first? ✅ 2026-09-15
- [x] Can you fully parenthesize `¬p ∧ q ∨ r → s` without a calculator/reference? ✅ 2026-09-15 — `((¬p ∧ q) ∨ r) → s`
- [x] Do you know why converse ≠ original (not just that it's true)? ✅ 2026-09-15

If any box is unchecked, redo [[../../../Week 1/Lecture 1/Questions|Questions.md]] Q11, Q15, and the precedence bonus problem before the next test.
