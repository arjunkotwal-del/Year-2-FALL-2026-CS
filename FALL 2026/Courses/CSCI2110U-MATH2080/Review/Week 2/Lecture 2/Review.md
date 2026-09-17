---
tags: [review, week2, lecture2]
---

# Review — Week 2 / Lecture 2 (Predicate Logic & Nested Quantifiers, §1.4–1.5 — course Lecture 3)

← [[../../../Week 2/Lecture 2/Notes|Full Notes]] | [[../../../Week 2/Lecture 2/Questions|Questions]] | ← [[../../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] What this is
> A short list of exactly what to re-drill from this lecture. If any line below feels shaky, jump back to the linked Notes section before moving on.

## What to review

1. **∀/∃ truth conditions** — know when each is true/false, and that a single counterexample kills a ∀ claim.
2. **Restricted domain unpacking**: ∀-restriction → conditional (→), ∃-restriction → conjunction (∧). This exact asymmetry is also how you translate "every student..." (→) vs "some student..." (∧) when broadening to "all people" as the domain.
3. **De Morgan's for quantifiers**: ¬∀xP(x) ≡ ∃x¬P(x), and ¬∃xP(x) ≡ ∀x¬P(x). Practice on English sentences, not just symbols.
4. **What you CANNOT distribute**: ∀ over ∨, and ∃ over ∧. Know a concrete counterexample for each (this is a classic exam "true or false + justify" question).
5. **Order of nested quantifiers matters when mixed** (∀...∃ vs ∃...∀) but NOT when both are the same type. Be able to explain WHY using the loop analogy, not just recite the rule.
6. **"Exactly one" translation pattern**: existence clause AND a uniqueness clause ruling out all other candidates.
7. **Negating nested quantifiers**: push the negation inward one layer at a time, flipping ∀↔∃ each step, only converting → to ∧¬ as the very last step if needed.

## Quick self-check
- [ ] Can you state, from memory, a domain where ∀x(x²≥x) is false and one where it's true?
- [ ] Given ∃y∀xP(x,y), can you explain in your own words why this forces ∀x∃yP(x,y) but not the reverse?
- [ ] Can you negate `∀x∃y∀zT(x,y,z)` fully, with no negation left of any quantifier, in under a minute?
- [ ] Can you translate "everyone has exactly one best friend" without looking at the notes?

If any box is unchecked, redo [[../../../Week 2/Lecture 2/Questions|Questions.md]] Q9 (parts g-j) and Q31 before the next test.

## Cross-lecture note
This lecture is where the converse/inverse trap from Weeks 1-2 generalizes: mixing up quantifier order (∃∀ vs ∀∃) is the predicate-logic version of the same "direction matters" mistake. If it shows up in a fourth lecture, it's almost certainly a guaranteed exam topic.
