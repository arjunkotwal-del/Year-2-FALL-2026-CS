---
tags: [practice, week1, lecture1, propositional-logic]
---

# Lecture 1 — Practice Questions

← [[Notes]] | ← [[CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Source
> Honour homework from [[../../files/MATH2080_Lecture1_Sections_1p1_PropLogic.pdf]], due before tutorials. Full text pulled from [[../../files/Rosen - Discrete Mathematics and Its Applications (8th ed).pdf]] (8th edition numbering — 7th ed. numbers noted at bottom).

> [!tip] How to use this
> Attempt every part yourself, in writing, before checking anything. Don't just eyeball truth tables in your head — write out the rows. This is the highest-risk skill area this term.

---

## Section 1.1 — Propositional Logic

### Q1 — Is it a proposition?
Which of these sentences are propositions? What are the truth values of those that are propositions?
a) Boston is the capital of Massachusetts.
b) Miami is the capital of Florida.
c) 2 + 3 = 5.
d) 5 + 7 = 10.
e) x + 2 = 11.
f) Answer this question.

### Q3 — Negations
What is the negation of each of these propositions?
a) Linda is younger than Sanjay.
b) Mei makes more money than Isabella.
c) Moshe is taller than Monica.
d) Abby is richer than Ricardo.

### Q11 — Formula → English
Let p = "Swimming at the New Jersey shore is allowed" and q = "Sharks have been spotted near the shore." Express each as an English sentence.
a) ¬p
b) p ∧ q
c) ¬p ∨ q
d) p → ¬q
e) ¬q → p
f) ¬p → ¬q
g) p ↔ ¬q
h) ¬p ∧ (p ∨ ¬q)

### Q15 — English → formula
Let p = "You drive over 65 miles per hour," q = "You get a speeding ticket." Write each as a formula (using connectives and negations).
a) You do not drive over 65 miles per hour.
b) You drive over 65 miles per hour, but you do not get a speeding ticket.
c) You will get a speeding ticket if you drive over 65 miles per hour.
d) If you do not drive over 65 miles per hour, then you will not get a speeding ticket.
e) Driving over 65 miles per hour is sufficient for getting a speeding ticket.
f) You get a speeding ticket, but you do not drive over 65 miles per hour.
g) Whenever you get a speeding ticket, you are driving over 65 miles per hour.

### Q33 — Truth tables
Construct a truth table for each:
a) p ∧ ¬p
b) p ∨ ¬p
c) (p ∨ ¬q) → q
d) (p ∨ q) → (p ∧ q)
e) (p → q) ↔ (¬q → ¬p)
f) (p → q) → (q → p)

### Q47 — Bitwise operations
Find the bitwise OR, AND, and XOR of each pair:
a) 101 1110, 010 0001
b) 1111 0000, 1010 1010
c) 00 0111 0001, 10 0100 1000
d) 11 1111 1111, 00 0000 0000

---

## Section 1.2 — Applications

### Q35 — Knights, knaves, and spies
On an island there are three kinds of people: **knights** (always tell the truth), **knaves** (always lie), and **spies** (can do either). You meet three people A, B, C — you know one is a knight, one a knave, one a spy, but not which is which. Determine, if possible, who is the knave, knight, and spy — or state that there's no unique solution.

> A says "I am not the spy," B says "I am not the spy," C says "I am not the spy."

---

## 7th edition cross-reference
If you're checking against an older solutions manual: §1.1 #1, 3, 9, 11, 31, 43 and §1.2 #31 correspond to this set (numbering shifts slightly between editions — content is the same).

---

## Answers

> [!warning] Attempt first
> Don't read these until you've written your own answer. Checking cold answers against a solution key with no attempt teaches you nothing.

### Q1
a) Proposition, **True** (Boston is the capital of Massachusetts).
b) Proposition, **False** (Tallahassee, not Miami, is Florida's capital).
c) Proposition, **True** ($2+3=5$).
d) Proposition, **False** ($5+7=12 \neq 10$).
e) **Not** a proposition — truth depends on the value of x.
f) **Not** a proposition — it's an imperative/question, not a declarative sentence.

### Q3
a) Linda is not younger than Sanjay.
b) Mei does not make more money than Isabella.
c) Moshe is not taller than Monica.
d) Abby is not richer than Ricardo.

### Q11
a) Swimming at the New Jersey shore is not allowed.
b) Swimming at the New Jersey shore is allowed and sharks have been spotted near the shore.
c) Swimming at the New Jersey shore is not allowed, or sharks have been spotted near the shore.
d) If swimming at the New Jersey shore is allowed, then sharks have not been spotted near the shore.
e) If sharks have not been spotted near the shore, then swimming at the New Jersey shore is allowed.
f) If swimming at the New Jersey shore is not allowed, then sharks have not been spotted near the shore.
g) Swimming at the New Jersey shore is allowed if and only if sharks have not been spotted near the shore.
h) Swimming is not allowed, and either swimming is allowed or sharks have not been spotted (this combination is actually only satisfiable when swimming isn't allowed and sharks haven't been spotted, since the first clause forces ¬p).

### Q15 (p: drive over 65, q: get a speeding ticket)
a) $\neg p$
b) $p \wedge \neg q$
c) $p \rightarrow q$
d) $\neg p \rightarrow \neg q$
e) $p \rightarrow q$
f) $q \wedge \neg p$
g) $q \rightarrow p$

### Q33 — truth tables (rows in order TT, TF, FT, FF)
a) $p \wedge \neg p$: **F, F, F, F** — contradiction.
b) $p \vee \neg p$: **T, T, T, T** — tautology.
c) $(p \vee \neg q) \rightarrow q$: **T, F, T, F**.
d) $(p \vee q) \rightarrow (p \wedge q)$: **T, F, F, T**.
e) $(p \rightarrow q) \leftrightarrow (\neg q \rightarrow \neg p)$: **T, T, T, T** — tautology (a conditional and its contrapositive always match).
f) $(p \rightarrow q) \rightarrow (q \rightarrow p)$: **T, T, F, T** — contingency.

### Q47 — bitwise operations
a) x = 1011110, y = 0100001
   OR = 1111111, AND = 0000000, XOR = 1111111
b) x = 1111 0000, y = 1010 1010
   OR = 1111 1010, AND = 1010 0000, XOR = 0101 1010
c) x = 00 0111 0001, y = 10 0100 1000
   OR = 10 0111 1001, AND = 00 0100 0000, XOR = 10 0011 1001
d) x = 11 1111 1111, y = 00 0000 0000
   OR = 11 1111 1111, AND = 00 0000 0000, XOR = 11 1111 1111

### Q35 (§1.2 — knights, knaves, spies)
**There is no valid assignment — the puzzle is unsolvable.**

Reasoning: the statement "I am not the spy" is true for everyone *except* whoever the actual spy is. Now consider whoever holds the **knave** role: a knave always lies, so their statement must be false. But "I am not the spy" is false only for the actual spy — and the knave, by definition, is a different person from the spy. So the knave's statement is actually **true** (since the knave genuinely isn't the spy), which contradicts the requirement that knaves always lie. This contradiction arises no matter which of A, B, C you assign as the knave — so no consistent assignment of knight/knave/spy exists for these three statements.

