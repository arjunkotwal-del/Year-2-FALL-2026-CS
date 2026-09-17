---
tags: [practice, week1, lecture2, propositional-equivalences]
---

# Lecture 2 — Practice Questions

← [[Notes]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Source — confirmed from Canvas
> Official honour homework, pulled directly from the posted lecture PDF ([[../../files/MATH2080_Lecture2_Sections_1p3_PropEquivs.pdf]]): §1.3 #1, 5, 7, 11, 19, 35 (8th ed). Due before next week's tutorials.

---

### Q1 — Verify with truth tables
Use truth tables to verify these equivalences:
a) $p \wedge T \equiv p$
b) $p \vee F \equiv p$
c) $p \wedge F \equiv F$
d) $p \vee T \equiv T$
e) $p \vee p \equiv p$
f) $p \wedge p \equiv p$

### Q5 — Distributive law
Use a truth table to verify the distributive law:
$$p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$$

### Q7 — Negate with De Morgan's
Use De Morgan's laws to find the negation of each of these statements:
a) Jan is rich and happy.
b) Carlos will bicycle or run tomorrow.
c) Mei walks or takes the bus to class.
d) Ibrahim is smart and hard working.

### Q11 — Prove tautologies via truth tables
Show that each conditional statement is a tautology, using truth tables:
a) $(p \wedge q) \rightarrow p$
b) $p \rightarrow (p \vee q)$
c) $\neg p \rightarrow (p \rightarrow q)$
d) $(p \wedge q) \rightarrow (p \rightarrow q)$
e) $\neg(p \rightarrow q) \rightarrow p$
f) $\neg(p \rightarrow q) \rightarrow \neg q$

### Q19 — Determine tautology (no truth table shortcut — try equivalences first)
Determine whether $(\neg q \wedge (p \rightarrow q)) \rightarrow \neg p$ is a tautology.

### Q35 — Show NOT equivalent
Show that $(p \rightarrow q) \rightarrow r$ and $p \rightarrow (q \rightarrow r)$ are **not** logically equivalent. (Find one truth assignment where they differ — that's enough to disprove equivalence.)

---

## "Time permitting" bonus exercises (from the lecture slide itself)

1. Determine whether $(\neg p \wedge (p \rightarrow q)) \rightarrow \neg q$ is a tautology.
2. Show that $(p \wedge q) \rightarrow r$ and $(p \rightarrow r) \wedge (q \rightarrow r)$ are **not** logically equivalent.
3. How many different truth tables of compound propositions are there that involve the propositional variables p and q? *(Hint: think about how many rows are in such a table, and how many ways to fill a column of that many T/F entries.)*
4. Determine if this proposition is satisfiable: $(p \vee \neg q) \wedge (\neg p \vee q) \wedge (\neg p \vee \neg q)$
5. Find a compound proposition involving p, q, r that is true exactly when **two** of the three are true (and false otherwise). Hint: form a disjunction of conjunctions.

---

## Extra from tutoring session (not from lecture)
Simplify, showing each law used at each step:
$$\neg(\neg p \vee q) \vee (p \wedge q)$$

---

## Answers

> [!warning] Attempt first
> Don't read these until you've written your own answer.

### Q1 — verify with truth tables
Each holds because the two sides produce identical columns across all rows of p (and q where relevant):
a) $p\wedge T$: p=T→T, p=F→F. Matches p exactly.
b) $p\vee F$: p=T→T, p=F→F. Matches p exactly.
c) $p\wedge F$: always F, regardless of p. Matches constant F.
d) $p\vee T$: always T, regardless of p. Matches constant T.
e) $p\vee p$: p=T→T, p=F→F. Matches p.
f) $p\wedge p$: p=T→T, p=F→F. Matches p.

### Q5 — distributive law
| p | q | r | q∨r | p∧(q∨r) | p∧q | p∧r | (p∧q)∨(p∧r) |
|---|---|---|---|---|---|---|---|
|T|T|T|T|T|T|T|T|
|T|T|F|T|T|T|F|T|
|T|F|T|T|T|F|T|T|
|T|F|F|F|F|F|F|F|
|F|T|T|T|F|F|F|F|
|F|T|F|T|F|F|F|F|
|F|F|T|T|F|F|F|F|
|F|F|F|F|F|F|F|F|

Columns 5 and 8 match in every row → equivalent, confirmed.

### Q7 — negate with De Morgan's
a) Jan is not rich, or Jan is not happy.
b) Carlos will not bicycle tomorrow and will not run tomorrow.
c) Mei does not walk and does not take the bus to class.
d) Ibrahim is not smart, or he is not hard working.

### Q11 — prove tautologies (all six are tautologies — every row is T)
a) $(p\wedge q)\to p$: T,T,T,T
b) $p\to(p\vee q)$: T,T,T,T
c) $\neg p\to(p\to q)$: T,T,T,T
d) $(p\wedge q)\to(p\to q)$: T,T,T,T
e) $\neg(p\to q)\to p$: T,T,T,T
f) $\neg(p\to q)\to\neg q$: T,T,T,T
(rows in order TT, TF, FT, FF — verify any you're unsure of by filling in the table yourself.)

### Q19 — is $(\neg q\wedge(p\to q))\to\neg p$ a tautology?
**Yes.** Truth table (TT,TF,FT,FF): all four rows evaluate to T. (This is exactly the logical form of *modus tollens* — "if p→q and not-q, then not-p" — which is why it comes out true in every case.)

### Q35 — show NOT equivalent
$(p\to q)\to r$ and $p\to(q\to r)$ are **not** equivalent. Counterexample: p=F, q=F, r=F.
- $(p\to q)\to r = (F\to F)\to F = T\to F = \mathbf{F}$
- $p\to(q\to r) = F\to(F\to F) = F\to T = \mathbf{T}$

Different values on the same input → not logically equivalent.

### "Time permitting" bonus exercises
1. $(\neg p\wedge(p\to q))\to\neg q$ — **not a tautology**. Counterexample: p=F, q=T: $\neg p=T$, $p\to q=T$, so antecedent $=T$; $\neg q=F$; $T\to F=\mathbf{F}$.
2. $(p\wedge q)\to r$ vs $(p\to r)\wedge(q\to r)$ — **not equivalent**. Counterexample: p=T, q=F, r=F: LHS $=(T\wedge F)\to F = F\to F = T$; RHS $=(T\to F)\wedge(F\to F)=F\wedge T=F$. Different.
3. **16** different truth tables — a table has $2^2=4$ rows, and each row's output can independently be T or F, giving $2^4=16$ possible output columns.
4. $(p\vee\neg q)\wedge(\neg p\vee q)\wedge(\neg p\vee\neg q)$ is **satisfiable** — try p=F, q=F: all three clauses become T∨T, T∨F, T∨T → all true.
5. True when exactly two of p,q,r are true: $(p\wedge q\wedge\neg r)\vee(p\wedge\neg q\wedge r)\vee(\neg p\wedge q\wedge r)$

### Extra — simplify $\neg(\neg p\vee q)\vee(p\wedge q)$
$$\neg(\neg p\vee q) \equiv \neg(\neg p)\wedge\neg q \equiv p\wedge\neg q \quad\text{(De Morgan's, double negation)}$$
$$\text{So the expression becomes: } (p\wedge\neg q)\vee(p\wedge q)$$
$$\equiv p\wedge(\neg q\vee q) \quad\text{(distributive law)}$$
$$\equiv p\wedge T \equiv p \quad\text{(negation law, identity law)}$$
**Final answer: just $p$.**
