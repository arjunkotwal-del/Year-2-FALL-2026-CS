---
tags: [review, week3, lecture2]
---

# Review — Week 3 / Lecture 2 (Introduction to Proofs, §1.7 — course Lecture 5)

← [[../../../Week 3/Lecture 2/Notes|Full Notes]] | [[../../../Week 3/Lecture 2/Questions|Questions]] | ← [[../../../CSCI2110U-MATH2080 - Discrete Math]]

> [!warning] This is your highest-priority review section this term
> Your own study guide flags proofs as the #1 risk area. This lecture is where the technique actually starts. Don't just read the examples — redo every one cold, from a blank page, before checking your work.

## What to review

1. **Definitions cold**: even (n=2k), odd (n=2k+1), rational (p/q, q≠0). Every proof in this section plugs into one of these.
2. **Direct proof recipe**: assume hypothesis → apply definition → algebra → recognize target definition in the result.
3. **When to switch to contraposition**: hypothesis is hard to use directly (e.g. "x is irrational"), but the negated conclusion gives something concrete to work with.
4. **The √2 irrational proof by contradiction** — know it well enough to reproduce from memory, including WHY starting with "a,b share no common factors" is the setup that creates the eventual contradiction.
5. **Biconditional proofs**: two separate directions, potentially using different techniques for each (as in the n²+3 odd ⟺ n even example — direct one way, contrapositive the other).
6. **Counterexamples**: one failing case is enough to kill a ∀ conjecture. Don't overthink — try small/simple values first (like n=4 killing the "2ⁿ−1 is always prime" conjecture).

## Quick self-check
- [ ] Can you write out the direct proof that the product of two rationals is rational, unaided?
- [ ] Can you complete the contrapositive proof for "m+n even → m,n same parity" from a blank page?
- [ ] Can you reproduce the √2 irrational proof, explaining every step's purpose (not just reciting it)?
- [ ] Given a random ∀ conjecture, can you quickly test small cases to look for a counterexample before assuming it's true?

If any box is unchecked, redo [[../../../Week 3/Lecture 2/Questions|Questions.md]] extra practice A and C before the next test — these are the two proof techniques (contradiction, biconditional) most likely to reappear on the midterm.

## Cross-lecture note
Proof by contraposition is literally proof by contrapositive equivalence (¬q→¬p ≡ p→q) from Week 1/2 — same fact, now used as an active proof *technique* instead of just an equivalence to verify. If converse/inverse confusion resurfaces here, that's the same recurring trap from Weeks 1-2, now in proof form.
