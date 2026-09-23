---
tags: [notes, week3, lecture1, rules-of-inference]
---

# Lecture 4 — Rules of Inference (Section 1.6)

← [[../../Week 2/Lecture 2/Notes|Week 2 Lecture 2 (Predicate Logic)]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]
Textbook: [[../../files/Rosen - Discrete Mathematics and Its Applications (8th ed).pdf]] (Section 1.6, pages 76-84)

> [!info] Confirmed against the real posted lecture PDF
> Cross-checked against [[../../files/MATH2080_Lecture4_Sections_1p6_RulesOfInference.pdf]] (Canvas, Lecture 4, Sept 21). Slide skeleton filled in using the textbook's own numbered examples.

> [!warning] Why this section matters
> This is the toolbox you'll actually use to WRITE proofs starting next lecture. Every proof is really just a chain of these rules applied one after another — memorize the shapes, not just the names.

---

## 1. Arguments and validity

An **argument** is a sequence of propositions (**premises**) leading to a final proposition (**conclusion**), written:

```
p1
p2
 ...
pn
─────
∴ q
```

A **valid argument** is one where: IF all premises are true, THEN the conclusion MUST be true. Validity is about the *structure*, not whether the premises happen to be true in real life.

**Example:** "If you have access to the network, then you can change your grade. You have access to the network. ∴ You can change your grade." — valid structure (this is Modus Ponens, below), regardless of whether the premises are actually true in reality.

---

## 2. The 8 core rules of inference (propositional logic)

Each rule is itself a tautology in disguise — that's WHY it's always valid.

| Rule | Form | Name |
|---|---|---|
| 1 | p, p→q ∴ q | **Modus Ponens** |
| 2 | ¬q, p→q ∴ ¬p | **Modus Tollens** |
| 3 | p→q, q→r ∴ p→r | **Hypothetical Syllogism** |
| 4 | p∨q, ¬p ∴ q | **Disjunctive Syllogism** |
| 5 | p ∴ p∨q | **Addition** |
| 6 | p∧q ∴ p | **Simplification** |
| 7 | p, q ∴ p∧q | **Conjunction** |
| 8 | p∨q, ¬p∨r ∴ q∨r | **Resolution** |

**Memory anchors:**
- Modus Ponens = "affirms" (p is true → q follows)
- Modus Tollens = "denies" (q is false → p must be false, via contrapositive logic)
- Hypothetical Syllogism = chaining two conditionals (p→q→r collapses to p→r)
- Disjunctive Syllogism = "process of elimination" (p or q, not p, so it must be q)
- Addition/Simplification/Conjunction are the "obvious" ones — you can always weaken an AND into just one piece, or always OR something extra onto a known truth
- Resolution = the rule automated theorem-provers (like Prolog) are built on

---

## 3. Worked examples — identifying the rule used

**Example (Modus Ponens):** "Linda is an excellent swimmer. If Linda is an excellent swimmer, then she can work as a lifeguard. Therefore, Linda can work as a lifeguard."

Let p = "Linda is an excellent swimmer," q = "she can work as a lifeguard." Premises: p, p→q. Conclusion: q. → **Modus Ponens.**

**Example (multi-step chain):** Show that ¬p∧q, r→p, ¬r→s, s→t imply the conclusion t.

| Step | Statement | Reason |
|---|---|---|
| 1 | ¬p ∧ q | Premise |
| 2 | ¬p | Simplification (1) |
| 3 | r → p | Premise |
| 4 | ¬r | Modus Tollens (2, 3) |
| 5 | ¬r → s | Premise |
| 6 | s | Modus Ponens (4, 5) |
| 7 | s → t | Premise |
| 8 | t | Modus Ponens (6, 7) |

This is the actual FORMAT you'll be expected to write proofs in — a numbered list, each line justified by exactly one rule and citing which earlier line(s) it uses.

**Example (drawing a conclusion from a real scenario):** "If I take the day off, it either rains or snows. I took Tuesday off, or I took Thursday off. It was sunny on Tuesday. It did not snow on Thursday." What can you conclude?

Set up: D_T = "I took Tuesday off," D_Th = "I took Thursday off," and for each day, "rains or snows" applies. "Sunny on Tuesday" means it did NOT rain AND did NOT snow on Tuesday.

| Step | Statement | Reason |
|---|---|---|
| 1 | D_T → (rain_T ∨ snow_T) | Premise |
| 2 | ¬rain_T ∧ ¬snow_T | Premise (sunny Tuesday) |
| 3 | ¬(rain_T ∨ snow_T) | De Morgan's (2) |
| 4 | ¬D_T | Modus Tollens (1, 3) |
| 5 | D_T ∨ D_Th | Premise |
| 6 | D_Th | Disjunctive Syllogism (4, 5) |
| 7 | D_Th → (rain_Th ∨ snow_Th) | Premise |
| 8 | rain_Th ∨ snow_Th | Modus Ponens (6, 7) |
| 9 | ¬snow_Th | Premise |
| 10 | rain_Th | Disjunctive Syllogism (8, 9) |

**Conclusion: it rained on Thursday** (and you took Thursday off, from step 6).

---

## 4. Rules of inference for quantified statements

| Rule | Form | Meaning |
|---|---|---|
| **Universal Instantiation** | ∀x P(x) ∴ P(c), any c in domain | If it's true for everyone, it's true for any specific one |
| **Universal Generalization** | P(c) for arbitrary c ∴ ∀x P(x) | If you prove it for a *generic/arbitrary* element, it holds for all |
| **Existential Instantiation** | ∃x P(x) ∴ P(c), for SOME c | If something exists, give it a name and use it — but you don't get to choose what c is |
| **Existential Generalization** | P(c) for some c ∴ ∃x P(x) | If you found ONE example that works, you've proven existence |

> [!warning] Don't confuse instantiation with generalization
> Universal Instantiation goes ∀ → specific (safe, always works). Universal Generalization goes specific → ∀ (only valid if your "specific" c was truly arbitrary/generic, not some particular case you picked because it was convenient).

**Worked example:** "Everyone in New Jersey lives within 50 miles of the ocean." "Someone in New Jersey hasn't seen the ocean." Therefore, "someone who lives within 50 miles of the ocean hasn't seen it."

Let L(x) = "x lives within 50 miles of the ocean," S(x) = "x has seen the ocean," domain = people in NJ.

| Step | Statement | Reason |
|---|---|---|
| 1 | ∃x ¬S(x) | Premise |
| 2 | ¬S(c), for some specific c | Existential Instantiation (1) |
| 3 | ∀x L(x) | Premise |
| 4 | L(c) | Universal Instantiation (3) — works for ANY c, including the one from step 2 |
| 5 | L(c) ∧ ¬S(c) | Conjunction (2, 4) |
| 6 | ∃x(L(x) ∧ ¬S(x)) | Existential Generalization (5) |

**Key trick:** existential instantiation gives you a specific (but unknown) c first — THEN you apply universal instantiation using that *same* c, since "for all" covers it too.

---

## 5. Combining propositional + quantifier rules

Two combos come up so often they get their own names:

**Universal Modus Ponens:** ∀x(P(x)→Q(x)), P(a) for specific a ∴ Q(a)
**Universal Modus Tollens:** ∀x(P(x)→Q(x)), ¬Q(a) for specific a ∴ ¬P(a)

These are literally just Universal Instantiation + Modus Ponens (or Modus Tollens) chained together — used constantly in math without being spelled out explicitly.

---

## 6. Fallacies (assigned reading — Rosen p.79)

Two traps that LOOK like valid rules but aren't:

- **Fallacy of affirming the conclusion:** from p→q and q, concluding p. **INVALID** — q being true doesn't mean p was the only way to get there. (Counterexample: "If you do every problem in this book, you'll learn discrete math. You learned discrete math. ∴ You did every problem" — false, you could've learned it by attending lectures instead.)
- **Fallacy of denying the hypothesis:** from p→q and ¬p, concluding ¬q. **INVALID** — same reasoning, ¬p doesn't rule out q being true some other way.

> [!tip] How to catch these
> Both fallacies are contingencies, not tautologies — build the truth table and you'll find a row where premises are true but the "conclusion" is false. That's the giveaway they're not real rules.

---

## 7. Time-permitting example — the Superman argument (fun, but shows the full toolkit)

"If Superman were able and willing to prevent evil, he would do so. If Superman were unable to prevent evil, he would be impotent; if he were unwilling, he would be malevolent. Superman does not prevent evil. If Superman exists, he is neither impotent nor malevolent. Therefore, Superman does not exist."

Let A = able, W = willing, Pr = prevents evil, I = impotent, M = malevolent, E = exists.

| Step | Statement | Reason |
|---|---|---|
| 1 | (A∧W) → Pr | Premise |
| 2 | ¬Pr | Premise |
| 3 | ¬(A∧W) | Modus Tollens (1, 2) |
| 4 | ¬A ∨ ¬W | De Morgan's (3) |
| 5 | ¬A → I | Premise |
| 6 | ¬W → M | Premise |
| 7 | I ∨ M | (from 4, 5, 6 — case split: whichever of ¬A/¬W holds, its rule fires) |
| 8 | E → (¬I ∧ ¬M) | Premise |
| 9 | ¬(¬I∧¬M) ≡ (I∨M) | already have this from step 7 |
| 10 | ¬E | Modus Tollens (8, 9) |

**Conclusion: Superman does not exist.** A valid (if silly) argument — good demonstration that validity ≠ the premises being realistic.

---

## Summary checklist
- [ ] Can name all 8 propositional rules of inference from their symbolic shape alone
- [ ] Can write a multi-step proof in the "Step / Statement / Reason" table format, citing exactly one rule per line
- [ ] Know the 4 quantifier rules and which direction each goes (specific↔general)
- [ ] Can spot the two fallacies (affirming the conclusion, denying the hypothesis) and explain why each fails
- [ ] Comfortable combining a quantifier rule with a propositional rule in one argument (universal modus ponens/tollens)

**Next:** → [[Questions]] (real honour homework: §1.6 #1, 3, 9, 19, 23, 29, 35)
