---
tags: [notes, week2, lecture2, predicate-logic, quantifiers]
---

# Lecture 3 — Predicate Logic & Nested Quantifiers (Sections 1.4–1.5)

← [[../Lecture 1/Notes|Week 2 Lecture 1 (Prop. Equivalences)]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]
Textbook: [[../../files/Rosen - Discrete Mathematics and Its Applications (8th ed).pdf]] (§1.4 pages 40–59, §1.5 pages 60–72)

> [!info] Confirmed against the real posted lecture PDF
> Cross-checked against [[../../files/MATH2080_Lecture3_Sections_1p4_1p5_PredLogic_and_NestedQuants.pdf]] (Canvas, Lecture 3, Sept 17). His slide is a fill-in skeleton (like Lecture 1) — this fills in the blanks using the textbook's own examples for the same numbered items.

> [!warning] Why this section matters
> Propositional logic (weeks 1) can't express things like "every non-zero real number has a multiplicative inverse" — you need a variable and a way to say "for all" or "there exists." This is the jump from propositions to **predicates + quantifiers**, and it's the language proofs are written in for the rest of the course.

---

## 1. Predicates

A **predicate** (propositional function) is a statement whose truth depends on a variable — it's neither true nor false until the variable is given a value.

$P(x)$: "$x > 3$" — not a proposition by itself. But $P(4)$ = "4 > 3" = **True**, and $P(2)$ = "2 > 3" = **False**. Plugging in a value turns the predicate into an actual proposition.

Predicates can take multiple variables: $Q(x,y)$: "$x = y + 3$". $Q(1,2)$ = "1 = 2+3" = False. $Q(3,0)$ = "3 = 0+3" = True.

An $n$-variable predicate is called an **n-ary predicate**.

---

## 2. Universal and existential quantifiers

| Symbol | Name | Reads as | True when | False when |
|---|---|---|---|---|
| $\forall x\, P(x)$ | universal | "for all x, P(x)" | P(x) is true for **every** x in the domain | there's at least one **counterexample** |
| $\exists x\, P(x)$ | existential | "there exists x such that P(x)" | P(x) is true for **at least one** x | P(x) is false for every x |

**The domain (universe of discourse) must always be stated** — the same predicate can be true or false depending purely on what domain you're quantifying over.

**Worked example:** $P(x)$: "$x^2 \geq x$"
- Domain = all real numbers: $\forall x\, P(x)$ is **False** — counterexample $x = 0.5$: $0.25 \geq 0.5$ is false.
- Domain = all integers: $\forall x\, P(x)$ is **True** — no integer strictly between 0 and 1 breaks it.

**Counterexamples are your main tool for disproving a ∀ statement** — you only need ONE failing case.

**Quantifiers over finite domains reduce to propositional logic:**
- $\forall x\, P(x)$ with domain $\{x_1,...,x_n\}$ ≡ $P(x_1) \wedge P(x_2) \wedge \cdots \wedge P(x_n)$
- $\exists x\, P(x)$ with domain $\{x_1,...,x_n\}$ ≡ $P(x_1) \vee P(x_2) \vee \cdots \vee P(x_n)$

**Worked example:** $P(x)$: "$x^2 < 10$", domain = positive integers ≤ 4. $\forall x P(x) = P(1)\wedge P(2)\wedge P(3)\wedge P(4)$. Since $P(4)$ = "16 < 10" is False, the whole conjunction is False.

---

## 3. Quantifiers with restricted domains

Shorthand: put the restriction right after the quantifier symbol.

$\forall x<0\,(x^2>0)$ means "for every real $x$ with $x<0$, $x^2>0$" — equivalent to $\forall x(x<0 \to x^2>0)$.

$\exists z>0\,(z^2=2)$ means "there's a positive $z$ with $z^2=2$" — equivalent to $\exists z(z>0 \wedge z^2=2)$.

> [!important] The pattern
> Restricting a **∀** turns into a **→** (conditional) when unpacked. Restricting an **∃** turns into a **∧** (conjunction) when unpacked. Mixing these up is a common error.

---

## 4. Precedence and binding

- **∀ and ∃ bind tighter than any propositional connective.** So $\forall x P(x) \vee Q(x)$ means $(\forall x P(x)) \vee Q(x)$, **not** $\forall x(P(x) \vee Q(x))$.
- A variable is **bound** if a quantifier applies to it, **free** if not. $\exists x(x+y=1)$: x is bound, y is free.
- The **scope** of a quantifier is the part of the formula it applies to. In $\exists x(P(x)\wedge Q(x)) \vee \forall x R(x)$, the ∃'s scope is just $P(x)\wedge Q(x)$; it does not reach into the ∀'s part.

---

## 5. Logical equivalences involving quantifiers

$$\forall x(P(x)\wedge Q(x)) \equiv \forall x P(x) \wedge \forall x Q(x)$$

You **can** distribute ∀ over ∧, and ∃ over ∨. But:

> [!warning] What you CANNOT do
> - $\forall x(P(x) \vee Q(x))$ is **NOT** equivalent to $\forall x P(x) \vee \forall x Q(x)$ (you can't split a ∀ across an OR)
> - $\exists x(P(x)\wedge Q(x))$ is **NOT** equivalent to $\exists x P(x) \wedge \exists x Q(x)$ (you can't split an ∃ across an AND)

Why the second one fails: $\exists x P(x) \wedge \exists x Q(x)$ just needs *some* x making P true and *some possibly different* x making Q true. $\exists x(P(x)\wedge Q(x))$ needs the *same* x to satisfy both. These are genuinely different claims.

---

## 6. De Morgan's Laws for quantifiers — negating quantified statements

$$\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$$
$$\neg \exists x\, P(x) \equiv \forall x\, \neg P(x)$$

**Intuition:** "It's not true that everything has property P" means "something lacks property P." "It's not true that something has property P" means "everything lacks property P."

**Worked example:** Negate "Every student in this class has studied calculus."

Let $C(x)$: "x has studied calculus," domain = students in the class. Original: $\forall x\, C(x)$.

Negation: $\neg\forall x\,C(x) \equiv \exists x\,\neg C(x)$ = **"There is a student in this class who has not studied calculus."**

**Second worked example:** Negate "There is an honest politician." Let $H(x)$ = "x is honest." Original: $\exists x\,H(x)$. Negation: $\forall x\,\neg H(x)$ = **"Every politician is dishonest."**

> [!tip] Careful with English ambiguity
> "All Americans do not eat cheeseburgers" is genuinely ambiguous in English — could mean $\forall x\,\neg C(x)$ (no American eats them) or $\neg\forall x\,C(x)$ (not all Americans eat them). Avoid this phrasing; prefer "Some American does not eat cheeseburgers" for the second meaning.

---

## 7. Translating English → predicate logic

**Worked example:** "Every student in this class has studied calculus."

Rewrite: "For every student x in this class, x has studied calculus" → $\forall x\, C(x)$ (domain = students in class).

But if you want the domain to be **all people** instead: "For every person x, if x is a student in this class, then x has studied calculus" → $\forall x(S(x) \rightarrow C(x))$.

> [!important] Universal + conditional, Existential + conjunction
> When the domain is broadened to "all people," a **∀** statement pairs with **→** (as above), while an **∃** statement pairs with **∧**. Example: "Some student has visited Mexico," domain = all people → $\exists x(S(x) \wedge M(x))$, **not** $\exists x(S(x)\to M(x))$ (that version would be trivially true for any non-student, since F→anything is T).

This mirrors the restricted-domain pattern from section 3 — same logic, just spelled out with an explicit predicate instead of shorthand.

---

## 8. Nested quantifiers (Section 1.5)

When one quantifier is inside the scope of another: $\forall x\,\exists y(x+y=0)$.

**Order matters when quantifiers differ (∀ vs ∃)** — but **not** when they're the same type.

- $\forall x\forall y\,P(x,y) \equiv \forall y\forall x\,P(x,y)$ — order of same-type quantifiers can be swapped freely.
- $\exists y\forall x\,Q(x,y)$ vs $\forall x\exists y\,Q(x,y)$ — **NOT the same!**

**Worked example (the classic one):** $Q(x,y)$: "$x+y=0$", domain = all reals.

- $\exists y\,\forall x\,Q(x,y)$ = "There's a single y that works for EVERY x" → **False** (no fixed y satisfies x+y=0 for all x).
- $\forall x\,\exists y\,Q(x,y)$ = "For every x, SOME y works (possibly different y each time)" → **True** (just pick y = −x each time).

> [!important] The rule to memorize
> If $\exists y\,\forall x\,P(x,y)$ is true, then $\forall x\,\exists y\,P(x,y)$ is automatically also true. The reverse does **not** hold. Read left-to-right: whichever variable is quantified **first** ("outermost") is fixed before the next one is chosen — ∃ first means one value has to work for everything after it; ∀ first means each subsequent choice is allowed to depend on it.

**Loop analogy:** think of nested quantifiers as nested loops. $\forall x\exists y$: for each x (outer loop), search for a y that works (inner loop) — y is allowed to change per x. $\exists y\forall x$: pick one y (outer), then check it works for every x (inner) — y is locked in before x varies.

---

## 9. Translating nested quantifiers

**Worked example:** "The sum of two positive integers is always positive."

Rewrite: "For every two integers, if both are positive, then their sum is positive" → $\forall x\forall y((x>0)\wedge(y>0) \rightarrow (x+y>0))$.

**Worked example:** "Everyone has exactly one best friend."

Break it down: "for every person x, there's a y who is x's best friend, AND for every other person z (z≠y), z is NOT x's best friend":

$$\forall x\,\exists y\Big(B(x,y) \wedge \forall z\big((z\neq y)\to \neg B(x,z)\big)\Big)$$

This is the general pattern for "exactly one" — assert existence, then assert uniqueness by ruling out every other candidate.

---

## 10. Negating nested quantifiers

Push the negation inward one quantifier at a time, flipping ∀↔∃ at each step (De Morgan's for quantifiers, applied repeatedly), and flip → to ∧¬ at the very end if needed (using $\neg(p\to q)\equiv p\wedge\neg q$ from §1.3).

**Worked example:** Negate $\forall x\,\exists y(xy=1)$ so no negation precedes a quantifier.

$$\neg\forall x\exists y(xy=1) \equiv \exists x\,\neg\exists y(xy=1) \equiv \exists x\,\forall y\,\neg(xy=1) \equiv \exists x\forall y(xy\neq 1)$$

Each step flips exactly one quantifier — this is mechanical once you know the two De Morgan's-for-quantifiers rules.

---

## Summary checklist
- [ ] Know when ∀ / ∃ statements are true vs. false, and how to find a counterexample to disprove a ∀ claim
- [ ] Know the restricted-domain shorthand and that ∀-restriction unpacks to →, ∃-restriction unpacks to ∧
- [ ] Can state both De Morgan's laws for quantifiers and use them to negate a compound English sentence
- [ ] Understand why $\exists y\forall x$ implies $\forall x\exists y$ but not conversely — and can explain why using the loop analogy
- [ ] Can translate "everyone has exactly one X" style statements using the existence + uniqueness pattern
- [ ] Can negate a nested-quantifier expression one layer at a time, ending with no negation to the left of any quantifier

**Next:** → [[Questions]] (real honour homework, confirmed via Canvas)
