---
tags: [course]
crn: 40245
term: Fall 2026
credit_hours: 3
---

# CSCI2110U / MATH2080 — Discrete Mathematics

← [[Home]]

## Logistics
- **Lecture:** Mon & Thu 6:40–8:00pm, online (Google Meet — .net account, online section only)
- **Instructor:** Mihai Beligan — SCI3016, ext. 5318, email via Canvas; office hours Mon/Wed/Fri 2–3pm SCI3016 (starts wk of Sept 14)
- **TAs:** Zahra Hashemi (tutorials Tue/Wed), Marian Kowalski — Canvas; office hours TBA (starts wk of Sept 14). Note: tutorials run one week behind lecture material (week 1 tutorial covers week 1's one lecture; from week of Sept 21 onward, tutorials cover the prior week's two lectures).
- **Classes:** Sept 10 – Dec 7, 2026
- **Prereq:** MATH 1020U. Coreq: MATH 1850U or MATH 2050U

## Textbook
*Discrete Mathematics and Its Applications*, Rosen, 8th ed. — Chapters 1, 2, 3, 4, 5, 6, 9, 10. Resources at mhhe.com/rosen.

## Grading
| Component | Weight |
|---|---|
| In-lecture/tutorial pop quizzes | 10% (out of 75% of total possible marks; can bonus past 10/10) |
| Assignments (4, groups of ≤4) | 10% |
| Online Canvas tests (2, Lockdown Browser) — tentative Sat Oct 3 & Sat Nov 21 | 5% + 5% |
| Midterm — Thu Oct 22, in-person, BIT2080 | 30% |
| Final exam — cumulative, in-person | 40% |

- Assignments: group work (auto-assigned groups of 3-4, reset each assignment except you keep your own group for the last one if you want). If a groupmate isn't contributing, contact instructor by the deadline stated in the assignment preamble to get them kicked out — they then submit solo work with a **20% penalty**. Everyone submits one copy, do the work individually first, then compare and merge.
- Pop quizzes: in-lecture (short, ~2 marks, 1 question) + tutorial quizzes (longer, ~4-5 questions, 8-10 marks). Tutorial quizzes open Monday–Friday each week (not just during tutorial), one attempt only, so don't waste it — go to tutorial and resolve confusion first.
- **Quiz bonus mechanic:** total quiz marks across the term (e.g. 80) are scaled against **75% of the total**, not 100%. Example: 80 total marks available → denominator used is 60 (75% of 80). Score 55/80 → counted as 55/60. Score 80/80 → still 80/60, i.e. bonus above 100% on this component. Component is worth 10% of final grade overall.
- Missed Canvas test → weight rolls into final exam. Missed midterm → needs SAS/paperwork, deferred to final exam (don't rely on this — final is cumulative and historically harder to do well on than the midterm).
- **Confirmed 2026-09-17: in-lecture quizzes DO count** toward the grade. The Canvas gradebook weight table shows a "Quizzes L" category at 0% (separate from "Quizzes T" at 10%) — that 0% is an unused/placeholder category, not the real policy, since lecture quizzes are graded in practice.
- **Confirmed 2026-09-17: the written syllabus body is the authoritative source**, not the Canvas gradebook weight table. Gradebook table (Midterm 25%, Canvas Tests 20%) does not reflect actual weighting — go with the syllabus: **Midterm 30%, Canvas Tests 5%+5%=10%, Assignments 10%, Quizzes 10%, Final 40%.**

## Topic outline
1. Propositional logic
2. Predicate logic; rules of inference
3. Proofs
4. Set theory; functions
5. Sequences/sums; cardinality; growth of functions
6. Divisibility/modular arithmetic; integer reps; primes & GCD
7. Induction
8. Recursion; basic counting; permutations/combinations
9. Binomial theorem; generalized permutations/combinations
10. Discrete probability
11. Relations
12. Elementary graph theory

## Study resources
- TrevTutor — recommended for the Propositional Logic series
- Interactive HTML learning tool built by Claude, gated topic progression

## Key dates
- Online Canvas Test 1: Sat Oct 3
- Midterm: Thu Oct 22 (in-lecture, BIT2080)
- Online Canvas Test 2: Sat Nov 21

## Canvas modules (as posted)
- **Lecture Notes** module: Lecture 1 (Sept 10) — Propositional Logic §1.1, PDF posted. Rest not yet uploaded as of this scrape.

## Notes

### 2026-09-10 — Tutoring session log (Week 1 / Lecture 1)
- Covered: propositions, six connectives, truth tables, conditional statement traps (p→q false only in T,F case), converse/inverse/contrapositive (contrapositive is the only one equivalent to the original — matters later for proof techniques), translating English→logic ("only if" traps), operator precedence (¬, ∧, ∨, →, ↔ in that order), bitwise OR/AND/XOR.
- Created: [[Week 1/Lecture 1/Notes]] (filled-in lecture content, since the posted PDF is a blank slide skeleton) and [[Week 1/Lecture 1/Questions]] (Week 1 honour homework, transcribed in full: §1.1 #1,3,11,15,33,47; §1.2 #35). Plain-text copies (Notes.txt, Questions.txt) also saved in the same folder for sharing.
- Textbook (Rosen 8th ed.) added to vault: [[files/Rosen - Discrete Mathematics and Its Applications (8th ed).pdf]].
- In progress: operator precedence practice — parenthesizing `p ∨ q ∧ ¬r ↔ p ∧ r` step by step.

### 2026-09-14 — Lecture 2 (Propositional Equivalences, §1.3) — filed under Week 2/Lecture 1
- Confirmed via Canvas: real course PDF is `MATH2080_Lecture2_Sections_1p3_PropEquivs.pdf`, saved to [[files/MATH2080_Lecture2_Sections_1p3_PropEquivs.pdf]]. Real honour homework: §1.3 #1, 5, 7, 11, 19, 35 (8th ed).
- Built [[Week 2/Lecture 1/Notes]] and [[Week 2/Lecture 1/Questions]] — covers tautology/contradiction, De Morgan's, the full equivalence-law table, chaining equivalences algebraically, contrapositive equivalence, satisfiability.
- Practiced live: tautology-spotting shortcuts (`X ∨ T`, `X ∨ ¬X`), De Morgan negation of compound English sentences, simplifying `¬(¬p∨q)∨(p∧q)` down to `¬p∨q` via De Morgan's + double negation + absorption.
- Note on organization: lecture numbering is continuous across the course (Lecture 1, 2, 3...) but filed by calendar week here — Lecture 2 (Sept 14, Monday) is the first lecture of Week 2, hence `Week 2/Lecture 1/`.

### 2026-09-17 — Lecture 3 (Predicate Logic & Nested Quantifiers, §1.4–1.5) — filed under Week 2/Lecture 2
- Confirmed via Canvas: real course PDF is `MATH2080_Lecture3_Sections_1p4_1p5_PredLogic_and_NestedQuants.pdf`, saved to [[files/MATH2080_Lecture3_Sections_1p4_1p5_PredLogic_and_NestedQuants.pdf]]. Real honour homework: §1.4 #7, 9, 11, 15, 53 and §1.5 #1, 9, 11, 27, 31 (8th ed).
- Built [[Week 2/Lecture 2/Notes]] and [[Week 2/Lecture 2/Questions]] — covers predicates, universal/existential quantifiers, restricted domains, precedence/binding, quantifier equivalences (what distributes and what doesn't), De Morgan's for quantifiers, translating English with nested quantifiers, order-of-quantifiers (∃∀ vs ∀∃), and negating nested quantifiers.
- Added [[Review/Week 2/Lecture 2/Review]].
- Recurring pattern flagged again: order/direction sensitivity (converse≠original in Weeks 1-2, now ∃∀≠∀∃ here) — treat as a near-certain exam topic given it's been emphasized three times running.

### 2026-09-17 — Live Lecture 3 transcript (confirms/extends notes above)
- Added [[Week 2/Lecture 2/Transcript]] with the raw transcript.
- Confirms Notes.md is accurate — all definitions, the rational/irrational counterexample, and the De Morgan-for-quantifiers mechanics match what he actually taught live.
- **New content not in the PDF alone:** the reciprocal example (∀x≠0 ∃y(xy=1)) for explaining why ∃∀ vs ∀∃ order matters — y=1/x depends on which x you picked, so it can't come first; the "exactly two people Lynn loves" full derivation, built up in 3 attempts (existence → distinctness → uniqueness clause ruling out all other Z); the non-negative-product translation example as a closing example for the section.
- **IMPORTANT: he released a live in-lecture quiz on negating `∃x∀y(P(x,y)∧¬Q(x,y))`, then killed/invalidated it mid-lecture** after a student flagged his answer key had an error (he'd mistakenly counted a triple negation as a double negation). He said he'll re-ask the same type of question on the **tutorial quiz** instead — so this exact question type is very likely to reappear in tutorial, worth practicing the corrected version.
- Separately, this transcript **confirms the correct method** for the practice exam question you got 0/2 on (negating `∀x∃y(¬P(x,y)→Q(x,y))`): convert the implication to `¬(¬P)∨Q ≡ P∨Q` first via double negation, THEN negate the whole quantified statement → `∃x∀y(¬P(x,y)∧¬Q(x,y))`. Matches what we worked out together — good confirmation the approach was right.

### 2026-09-21 — Week 3 (Lectures 4 & 5: Rules of Inference §1.6, Intro to Proofs §1.7)
- Confirmed via Canvas: both already posted ahead of schedule. Files saved: [[files/MATH2080_Lecture4_Sections_1p6_RulesOfInference.pdf]] and [[files/MATH2080_Lecture5_Sections_1p7_ProofsIntro.pdf]].
- Real honour homework confirmed: §1.6 #1, 3, 9, 19, 23, 29, 35 (same both editions); §1.7 8th ed #5, 9, 11, 29, 37, 41 (7th ed #5, 9, 11, 27, 35, 39).
- Built [[Week 3/Lecture 1/Notes]] + [[Week 3/Lecture 1/Questions]] (Rules of Inference: the 8 propositional rules, quantifier rules, fallacies, multi-step proof format) and [[Week 3/Lecture 2/Notes]] + [[Week 3/Lecture 2/Questions]] (Intro to Proofs: direct proof, contraposition, contradiction, biconditional proofs, counterexamples — the actual proof-writing techniques used for the rest of the course).
- Added [[Review/Week 3/Lecture 1/Review]] and [[Review/Week 3/Lecture 2/Review]] — Lecture 5 (proofs) flagged as **highest priority review** this term, directly matching the study guide's stated highest-risk area.
- Cross-lecture note: proof by contraposition in Lecture 5 is literally the contrapositive-equivalence fact from Weeks 1-2, now applied as an active proof technique rather than just an equivalence check — good continuity to point out if it helps it stick.

### 2026-09-24 — Live Lecture 5 transcript (confirms/extends notes above)
- Added [[Week 3/Lecture 2/Transcript]] with the raw transcript.
- **Canvas Test 1 scope confirmed live** (Oct 3): covers up to and including the Monday Sept 28 lecture (Lecture 6), but explicitly NOT the Thursday Oct 1 lecture (Lecture 7) — there's a buffer lecture excluded right before the test. Update study plan to prioritize material through Lecture 6.
- Confirmed live: √2-irrational proof needs the "reduced fraction" assumption stated explicitly up front — without it there's nothing to contradict at the end. Added this as a warning in [[Week 3/Lecture 2/Notes]].
- New technique notes added to Notes.md from the live lecture: **WLOG** (skip writing symmetric proof cases twice), **use different letters for independent unknowns** (m=2k, n=2l+1, not both using k — avoids accidentally proving only the "consecutive integers" special case), and the **simple→complex strategy rule** (always easier to reason from n toward n² than backward — this is why several proofs switch to contraposition).
- For biconditional proofs: confirmed you can (and should) do whichever direction is easier first — no requirement to go ⇒ before ⇐.

### 2026-09-10 — Live Lecture 1 transcript notes (confirms/extends tutoring notes above)
- Instructor confirmed **contrapositive is the important one** to internalize (converse/inverse mainly matter as common-mistake traps, e.g. "differentiable ⟹ continuous" vs the false converse "continuous ⟹ differentiable").
- Instructor's mental model for p→q: think of it as a **contract** — "if you pay $1000, I rent the apartment." Only broken when you pay (p=T) and don't get the apartment (q=F). Matches the "promise" framing already in [[Week 1/Lecture 1/Notes]].
- De Morgan's laws are coming in **Lecture 2** — foreshadowed today via the negation of "Bob goes to the party AND John does not" → "Bob does not go OR John does."
- Exams/tests: mostly proof-based on midterm/final (introductory-level, not many steps beyond a definition or major theorem); Canvas tests are MC/fill-in-blank/short, no real proofs there. Assignments are harder/longer since you get a week.
- Confirmed truth-table bookkeeping method matches notes: n variables → 2ⁿ rows, first variable column splits in half (T block then F block), each subsequent variable halves again.
- Lecture recordings are NOT posted publicly (instructor records only for dispute purposes) — so live attendance or these notes are the only record.
