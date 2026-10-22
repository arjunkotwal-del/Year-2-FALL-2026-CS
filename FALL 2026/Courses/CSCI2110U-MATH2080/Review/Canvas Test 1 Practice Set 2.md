---
tags: [review, canvas-test-1, practice]
---

# Canvas Test 1: Practice Set 2 (modeled on the real L/T quizzes)

← [[Canvas Test 1 Practice Questions]] | ← [[Canvas Test 1 Review]]

> [!info] How to use this
> No proofs, just the question types your quizzes used: select-all, find the invalid step, name the rule, pick the counterexample, fill in the blank, card puzzles. Do all 34 on paper first, then check the key at the bottom.

---

## Section 1: Tautologies and equivalences

**1.** Select ALL tautologies (remember precedence: ¬, then ∧, then ∨, then →):
a) p ∧ q → p ∨ q
b) p → p ∧ q
c) p ∨ ¬p ∧ q
d) (p → q) ∨ (q → p)
e) p ∧ ¬p → q

**2.** Select the ONE proposition logically equivalent to ¬(p ∨ ¬q):
a) ¬p ∨ q  b) ¬p ∧ q  c) p ∧ ¬q  d) ¬p ∧ ¬q

**3.** ¬(p ∧ ¬q) is logically equivalent to:
a) ¬p ∧ q  b) p → q  c) q → p  d) ¬p → ¬q

**4.** Consider (p → q) ∧ (¬p → q). Fill in: when q is T the statement is ____; when q is F the statement is ____. So the whole statement is equivalent to ____.

**5.** For (p → q) ∧ (q → r), fill in the truth value:
- p=T, q=T, r=F: ____
- p=F, q=T, r=F: ____
- p=F, q=F, r=F: ____

**6.** True or False: (p ∨ q) ∧ ¬p ∧ ¬q is satisfiable.

---

## Section 2: Quantifiers

**7.** Domain = integers. P(x): "x is even." Q(x): "x is a multiple of 3." Select ALL that are TRUE:
a) ∃x (P(x) ∧ Q(x))
b) ∀x (P(x) ∨ Q(x))
c) ∃x P(x) ∧ ∃x Q(x)
d) ∀x (P(x) → Q(x))
e) ∃x (¬P(x) ∧ ¬Q(x))

**8.** Which is the negation of ∃x ∀y (P(x,y) → Q(y))?
a) ∀x ∃y (P(x,y) ∧ ¬Q(y))
b) ∀x ∃y (¬P(x,y) ∨ Q(y))
c) ∃x ∀y (P(x,y) ∧ ¬Q(y))
d) ∀x ∃y (P(x,y) → ¬Q(y))

**9.** Which is the negation of ∀x ∃y (P(x,y) ∨ ¬Q(x,y))?
a) ∃x ∀y (¬P(x,y) ∧ Q(x,y))
b) ∃x ∀y (¬P(x,y) ∨ Q(x,y))
c) ∀x ∃y (¬P(x,y) ∧ Q(x,y))
d) ∃x ∀y (P(x,y) ∧ ¬Q(x,y))

**10.** Domain = integers. Select ALL that are TRUE:
a) ∀n ∃m (n + m = 0)
b) ∃n ∀m (n + m = 0)
c) ∀n ∃m (m > n)
d) ∃m ∀n (m > n)
e) ∃n ∀m (nm = m)

**11.** Domain = {1, 2, 3}, P(x,y): "x < y". Fill in True or False:
- ∀x ∃y P(x,y): ____
- ∃x ∃y P(x,y): ____
- ∃y ∀x P(x,y): ____

**12.** Which is a valid conclusion from the premises ∀x (P(x) → Q(x)) and ∃x P(x)?
a) ∀x Q(x)  b) ∃x Q(x)  c) ∀x P(x)  d) ∃x ¬Q(x)

**13.** From ∀x (P(x) → Q(x)) and ¬Q(a), where a is a particular element, the valid conclusion is:
a) P(a)  b) ¬P(a)  c) Q(a)  d) ∀x ¬P(x)

---

## Section 3: Rules of inference and invalid steps

**14.** Identify (by number) the step that does NOT follow from the previous ones.
Premises: ∃x P(x), ∃x Q(x). Conclusion: ∃x (P(x) ∧ Q(x)).
(1) ∃x P(x)
(2) P(c) for some c
(3) ∃x Q(x)
(4) Q(c)
(5) P(c) ∧ Q(c)
(6) ∃x (P(x) ∧ Q(x))

**15.** Identify (by number) the step that does NOT follow.
(1) ∃x P(x)
(2) P(c) for some c
(3) ∀x P(x)

**16.** Fill in the reason for each step.
Premises: ¬p ∨ q, ¬q, r ∨ p. Conclusion: r.
1. ¬p ∨ q: premise
2. ¬q: premise
3. ¬p: ____ (from 1, 2)
4. r ∨ p: premise
5. r: ____ (from 3, 4)

**17.** Match each argument with its rule (dropdown):
- "I study or I fail. I did not study. So I fail." → ____
- "If I study, I pass. I did not pass. So I did not study." → ____
- "I am home and I am tired. So I am tired." → ____
- "It is sunny. So it is sunny or snowing." → ____
Options: Disjunctive Syllogism / Modus Tollens / Simplification / Addition / Modus Ponens

**18.** Select ALL arguments that are INVALID:
a) p → q, q, therefore p
b) p → q, ¬p, therefore ¬q
c) p → q, ¬q, therefore ¬p
d) p ∨ q, ¬p, therefore q
e) p → q, q → r, therefore p → r

**19.** True or False: Resolution lets you conclude q ∨ r from p ∨ q and ¬p ∨ r.

---

## Section 4: Proof concepts (no actual proofs)

**20.** The statement "|a + b| ≥ |a| + |b|" is false. Pick a counterexample:
a) a = 2, b = 3  b) a = −2, b = −3  c) a = −2, b = 3  d) a = 0, b = 5

**21.** "If a < b, then a² < b²" is false. Pick a counterexample:
a) a = 1, b = 2  b) a = −3, b = 1  c) a = 0, b = 3  d) a = 2, b = 5

**22.** The statement "n² > n for all integers n" is false. Pick a counterexample:
a) n = 2  b) n = −1  c) n = 1  d) n = 3

**23.** The best technique to prove "if 5n + 1 is even, then n is odd" is:
a) direct  b) contraposition  c) contradiction  d) cases

**24.** The best technique to prove "√11 is irrational" is:
a) direct  b) contraposition  c) contradiction  d) cases

**25.** True or False: To prove p → q by contradiction, you assume p is true and q is false.

**26.** Fill in: if m = 2k+1 and n = 2l+1 are odd, then m + n = 2(____), so it is even. And mn = 2(____) + 1, so it is odd.

**27.** The proof that √2^√2 is either rational or irrational (and still gives irrationals x, y with x^y rational) is called a ____ existence proof.
a) constructive  b) non-constructive

**28.** Match each (dropdown):
- Contrapositive of "if x² is even, then x is even" → ____
- Converse of "if x² is even, then x is even" → ____
Options: If x is odd, then x² is odd / If x is even, then x² is even / If x² is odd, then x is even

---

## Section 5: Card puzzles

**29.** Rule: "If a card shows an even number on one side, then the other side is red." You see: 8, 3, red, blue. Which MUST be flipped? Select ALL:
a) 8  b) 3  c) red  d) blue

**30.** Rule: "Every card with a vowel on one side has @ on the other." You see: U, X, @, #. Which MUST be flipped? Select ALL:
a) U  b) X  c) @  d) #

---

## Section 6: Mixed conceptual

**31.** The contrapositive of "If it rains, then the game is cancelled" is:
a) If the game is cancelled, then it rains
b) If it does not rain, then the game is not cancelled
c) If the game is not cancelled, then it does not rain
d) If it rains, then the game is not cancelled

**32.** "p only if q" means:
a) p → q  b) q → p  c) p ↔ q  d) ¬p → q

**33.** In ∃x (x + y = 1), the free variable is ____.

**34.** True or False: ∃x (P(x) ∧ Q(x)) is logically equivalent to ∃x P(x) ∧ ∃x Q(x).

---
---

## ANSWER KEY

**1. a, d, e.**
- a: (p∧q)→(p∨q), whenever p∧q is true, p∨q is too.
- b: fails at p=T, q=F.
- c: parses as p ∨ (¬p ∧ q) ≡ p ∨ q, which is not always true.
- d: if p→q is false then p=T, q=F, and then q→p is true.
- e: the left side p∧¬p is always F, so the conditional is always T.

**2. b.** ¬(p ∨ ¬q) ≡ ¬p ∧ ¬¬q ≡ ¬p ∧ q.

**3. b.** ¬(p ∧ ¬q) ≡ ¬p ∨ q ≡ p → q.

**4.** T; F; **q.** (If q=F: p→q ≡ ¬p and ¬p→q ≡ p, so the AND is ¬p ∧ p = F.)

**5.** F; F; T. (p=T,q=T,r=F: T ∧ F = F. p=F,q=T,r=F: T ∧ F = F. p=F,q=F,r=F: T ∧ T = T.)

**6. False.** Satisfying it needs q true (from p∨q with ¬p) but also ¬q.

**7. a, c, e.**
- a: 6.
- b: x=1 breaks it.
- c: both exist.
- d: x=2 is even but not a multiple of 3.
- e: x=1 is neither.

**8. a.** ¬∃x∀y(P→Q) ≡ ∀x∃y¬(P→Q) ≡ ∀x∃y(P ∧ ¬Q).

**9. a.** ¬∀x∃y(P ∨ ¬Q) ≡ ∃x∀y¬(P ∨ ¬Q) ≡ ∃x∀y(¬P ∧ Q).

**10. a, c, e.**
- a: m=−n.
- b: no single n works.
- c: m=n+1.
- d: no largest integer.
- e: n=1.

**11.** ∀x∃y(x<y): **False** (x=3 has no larger y). ∃x∃y(x<y): **True**. ∃y∀x(x<y): **False** (y=3 fails at x=3).

**12. b.** ∃xP gives P(c), then P(c)→Q(c) gives Q(c), so ∃xQ(x).

**13. b.** Universal modus tollens.

**14. Step 4.** The second existential must introduce a NEW name (d), not reuse c. The same c might not satisfy Q.

**15. Step 3.** Universal generalization needs an arbitrary c, but c here is just some element that happens to satisfy P.

**16.** Step 3: **Disjunctive Syllogism**. Step 5: **Disjunctive Syllogism**.

**17.** Disjunctive Syllogism; Modus Tollens; Simplification; Addition.

**18. a, b.** (a affirms the conclusion, b denies the hypothesis. c is modus tollens, d is disjunctive syllogism, e is hypothetical syllogism.)

**19. True.**

**20. c.** a=−2, b=3: |1| = 1, but |−2| + |3| = 5, and 1 ≥ 5 is false.

**21. b.** a=−3 < b=1, but 9 < 1 is false.

**22. c.** n=1: 1 > 1 is false.

**23. b.** From 5n+1 = 2k you can't isolate n. Contrapositive: n even gives 5(2k)+1 = 10k+1, which is odd.

**24. c.**

**25. True.**

**26.** k+l+1; 2kl+k+l. ((2k+1)+(2l+1) = 2(k+l+1). (2k+1)(2l+1) = 4kl+2k+2l+1 = 2(2kl+k+l)+1.)

**27. b.** non-constructive (you never find out which case is true).

**28.** Contrapositive: **If x is odd, then x² is odd.** Converse: **If x is even, then x² is even.**

**29. a and d.** 8 is even, so check red. Blue is not red, so check it isn't even. 3 and red can't break the rule.

**30. a and d.** U is a vowel, so check @. # is not @, so check it isn't a vowel. X and @ can't break the rule.

**31. c.**

**32. a.**

**33. y.**

**34. False.** Same x vs. possibly different x.

---

## Scoring
- 31-34: ready.
- 26-30: redo the sections you missed.
- Under 26: spend tonight on Sections 2 and 3 (quantifier negation and rules of inference), the places where marks usually go.
