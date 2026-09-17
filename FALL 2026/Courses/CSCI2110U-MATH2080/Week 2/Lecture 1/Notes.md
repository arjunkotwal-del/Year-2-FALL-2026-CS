---
tags: [notes, week1, lecture2, propositional-equivalences]
---

# Lecture 2 — Propositional Equivalences (Section 1.3)

← [[../../Week 1/Lecture 1/Notes|Lecture 1 Notes]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]
Textbook: [[../../files/Rosen - Discrete Mathematics and Its Applications (8th ed).pdf]] (Section 1.3, pages 26–39)

> [!info] This is Lecture 2 of the course (Sept 14), filed under Week 2
> Cross-checked against [[../../files/MATH2080_Lecture2_Sections_1p3_PropEquivs.pdf]] (posted on Canvas — module "Lecture Notes," Lecture 2, Sept 14). The instructor's own slide skeleton matches this content closely, including his exact "COMMON MISTAKES" callouts below. No live-lecture transcript yet — if you get one, we can patch in any extra wording/examples he added live.

> [!info] What this covers
> Tautology/contradiction/contingency, logical equivalence, De Morgan's Laws, the big table of equivalences, building new equivalences algebraically (instead of truth tables), satisfiability.

---

## 1. Tautology, contradiction, contingency

- **Tautology:** always True, no matter the inputs. Example: $p \vee \neg p$.
- **Contradiction:** always False, no matter the inputs. Example: $p \wedge \neg p$.
- **Contingency:** neither — sometimes T, sometimes F.

This connects directly to what we practiced already: spotting `(anything) ∨ T` or `X ∨ ¬X` patterns lets you declare a tautology without a full table — but you should still be able to build the table to confirm it, which is the ground truth.

---

## 2. Logical equivalence — the formal definition

**Definition:** p and q are **logically equivalent** (written $p \equiv q$) if $p \leftrightarrow q$ is a tautology — equivalently, if their truth tables have identical columns for every row.

> [!important]
> $\equiv$ is NOT a logical connective. $p \equiv q$ is not itself a compound proposition — it's a *statement about* two propositions, meaning "these always match."

**How to check equivalence:** build both truth tables side by side; if the final columns match row-for-row, they're equivalent.

---

## 3. De Morgan's Laws (the headline result of this section)

$$\neg(p \wedge q) \equiv \neg p \vee \neg q$$
$$\neg(p \vee q) \equiv \neg p \wedge \neg q$$

**Memory rule:** negating flips AND↔OR and pushes the negation onto each piece individually.

**Worked example (proved via truth table):** Show $\neg(p \vee q) \equiv \neg p \wedge \neg q$.

| p | q | p∨q | ¬(p∨q) | ¬p | ¬q | ¬p∧¬q |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | T | F | F | T | F |
| F | T | T | F | T | F | F |
| F | F | F | T | T | T | T |

Columns 4 and 7 match exactly → equivalent. Confirmed.

**Applied example:** Negate "Miguel has a cellphone and he has a laptop computer."

Let p = "Miguel has a cellphone," q = "Miguel has a laptop." Statement = $p \wedge q$.
Negation, by De Morgan's: $\neg(p \wedge q) \equiv \neg p \vee \neg q$
→ **"Miguel does not have a cellphone, or he does not have a laptop computer."**

> [!tip] Common mistake to avoid
> The negation of "p and q" is NOT "not p and not q." It's "not p **or** not q." Negating flips the connective — this is exactly the trap the assignment/quiz questions test.

---

## 4. The conditional-disjunction equivalence

$$p \rightarrow q \equiv \neg p \vee q$$

This is huge — it lets you rewrite any conditional as an OR, which is often easier to manipulate algebraically (no separate "implication" rules to memorize once you convert).

**Worked check (truth table):**

| p | q | ¬p | ¬p∨q | p→q |
|---|---|---|---|---|
| T | T | F | T | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

Match → confirmed equivalent.

---

## 5. The master table of equivalences

| Equivalence | Name |
|---|---|
| $p \wedge T \equiv p$, $\quad p \vee F \equiv p$ | Identity laws |
| $p \vee T \equiv T$, $\quad p \wedge F \equiv F$ | Domination laws |
| $p \vee p \equiv p$, $\quad p \wedge p \equiv p$ | Idempotent laws |
| $\neg(\neg p) \equiv p$ | Double negation law |
| $p \vee q \equiv q \vee p$, $\quad p \wedge q \equiv q \wedge p$ | Commutative laws |
| $(p\vee q)\vee r \equiv p\vee(q\vee r)$ (same for ∧) | Associative laws |
| $p\vee(q\wedge r)\equiv(p\vee q)\wedge(p\vee r)$ (and the mirror version) | Distributive laws |
| $\neg(p\wedge q)\equiv \neg p\vee\neg q$, $\quad \neg(p\vee q)\equiv\neg p\wedge\neg q$ | De Morgan's laws |
| $p\vee(p\wedge q)\equiv p$, $\quad p\wedge(p\vee q)\equiv p$ | Absorption laws |
| $p\vee\neg p\equiv T$, $\quad p\wedge\neg p\equiv F$ | Negation laws |

> [!tip] You've already used absorption
> Remember when we simplified $(\neg p \vee q) \vee (\neg p \wedge q)$ down to just $\neg p \vee q$? That was the **absorption law** in action: $p \vee (p \wedge q) \equiv p$ with $p := \neg p$.

**Don't memorize these by rote** — recognize the *shape*. Most exam questions are "apply one law at a time" chains, not "recall the name."

---

## 6. Building new equivalences algebraically (no truth table needed)

This is the actual skill tested — chain known equivalences together, one substitution at a time, citing which law you used at each step. This scales better than truth tables (2ⁿ rows explodes fast — 20 variables = over a million rows).

**Worked example:** Show $\neg(p \rightarrow q)$ and $p \wedge \neg q$ are equivalent — by algebra, not a table.

$$
\begin{aligned}
\neg(p \rightarrow q) &\equiv \neg(\neg p \vee q) &&\text{conditional-disjunction equivalence}\\
&\equiv \neg(\neg p) \wedge \neg q &&\text{De Morgan's law}\\
&\equiv p \wedge \neg q &&\text{double negation law}
\end{aligned}
$$

Each line is justified by exactly one named law — that's the format you should reproduce in your own work.

**Second worked example:** Show $(p \wedge q) \rightarrow (p \vee q)$ is a tautology, by reducing it to T.

$$
\begin{aligned}
(p \wedge q) \rightarrow (p \vee q) &\equiv \neg(p\wedge q) \vee (p \vee q) &&\text{conditional-disjunction}\\
&\equiv (\neg p \vee \neg q) \vee (p \vee q) &&\text{De Morgan's}\\
&\equiv (\neg p \vee p) \vee (\neg q \vee q) &&\text{associative/commutative}\\
&\equiv T \vee T &&\text{negation law (twice)}\\
&\equiv T &&\text{domination law}
\end{aligned}
$$

Since it reduces to the constant T, it's a tautology.

---

## 6b. Contrapositive equivalence (straight from his slides)

$$\neg q \rightarrow \neg p \equiv p \rightarrow q$$

This is the formal version of what we already know: a conditional and its contrapositive always match. His slides prove this by starting from $\neg q \to \neg p$ and reducing it via conditional-disjunction + De Morgan's + double negation until it becomes $p \to q$ — literally the same chain-of-equivalences technique from section 6 above, just applied to prove *this* specific identity. Try it yourself:

$$\neg q \rightarrow \neg p \equiv \neg(\neg q) \vee \neg p \equiv q \vee \neg p \equiv \neg p \vee q \equiv p \rightarrow q$$
(conditional-disjunction, then double negation, then commutativity, then conditional-disjunction again in reverse)

**Preview example on his slide (Example 5)** — this is foreshadowing actual proof technique (coming in §1.7-1.8): given $p \to q$: "If $n^2+2n-1$ is an odd integer, then $n$ is an even integer," you'd prove it by proving the contrapositive $\neg q \to \neg p$ instead: "If $n$ is odd, then $n^2+2n-1$ is even" — often easier to work with directly. We'll build this out properly once proofs start.

## 6c. Common mistakes (instructor's own emphasis — appears verbatim on his slide)

- Thinking an implication and its **converse** are logically equivalent — they're **not**: $p \to q \not\equiv q \to p$
- Thinking an implication and its **inverse** are logically equivalent — they're **not**: $p \to q \not\equiv \neg p \to \neg q$

This is the exact same trap flagged in [[../../Week 1/Lecture 1/Notes|Week 1 Lecture 1]] — he's repeating it because it's genuinely the most common error students make, and it's now confirmed as instructor-emphasized twice.

---

## 7. Satisfiability

A proposition is **satisfiable** if there's *at least one* assignment of truth values that makes it True. It's **unsatisfiable** if it's False under every assignment (i.e. it's a contradiction).

- To prove satisfiable → just exhibit one assignment that works (a "solution").
- To prove unsatisfiable → you need to argue *every* assignment fails (harder — usually by reasoning about the structure, not brute-force checking each row).

This is used heavily in practice (n-queens, Sudoku solvers, circuit design) but at our level it's mostly about the definition and reasoning through small examples.

---

## Summary checklist
- [x] Know the difference: tautology / contradiction / contingency ✅ 2026-09-15
- [x] Can state De Morgan's both directions from memory, and apply them to negate compound English sentences ✅ 2026-09-15
- [x] Know $p \to q \equiv \neg p \vee q$ cold — it's the bridge between implication and OR/AND-based algebra ✅ 2026-09-15
- [x] Can chain 3-5 equivalence laws together to simplify an expression or prove a tautology, citing the law used each step ✅ 2026-09-15
- [x] Understand satisfiable vs. unsatisfiable and how to argue each ✅ 2026-09-15

**Next:** → [[Questions]] (practice set, drawn from §1.3 exercises since no honour homework has been posted for this lecture yet)
