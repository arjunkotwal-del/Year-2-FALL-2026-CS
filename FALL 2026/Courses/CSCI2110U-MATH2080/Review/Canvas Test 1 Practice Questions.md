---
tags: [review, canvas-test-1, practice]
---

# Canvas Test 1 — Practice Questions (Lectures 1-6)

← [[Canvas Test 1 Review]] | ← [[../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] How to use this
> Test-style questions only (MC, T/F, fill-in, matching, multiple answer), since proofs aren't on the online test. Do the whole set on paper first, THEN check the answer key at the bottom. Mark the ones you miss and re-read that topic in [[Canvas Test 1 Review]].

---

## Part A: Propositional logic (Lecture 1)

**1.** Which compound proposition is false ONLY when p is true and q is false?
a) p ∧ q  b) p ∨ q  c) p → q  d) p ↔ q

**2.** The contrapositive of p → q is:
a) q → p  b) ¬p → ¬q  c) ¬q → ¬p  d) ¬(p → q)

**3.** True or False: The converse of a conditional statement is logically equivalent to the original statement.

**4.** "p only if q" translates to:
a) q → p  b) p → q  c) p ↔ q  d) p ∧ q

**5.** Fully parenthesized, ¬p ∧ q ∨ r → s is:
a) ¬(p ∧ q) ∨ (r → s)
b) ((¬p ∧ q) ∨ r) → s
c) ¬p ∧ (q ∨ (r → s))
d) (¬p ∧ (q ∨ r)) → s

**6.** For (p ∨ q) → (p ∧ q), fill in the truth value:
- p = T, q = F: ______
- p = F, q = F: ______

**7.** A truth table for a compound proposition with 4 variables has ______ rows.

**8.** Let x = 1100 and y = 1010. Fill in: x AND y = ______, x OR y = ______, x XOR y = ______.

---

## Part B: Propositional equivalences (Lecture 2)

**9.** ¬(p → q) is logically equivalent to:
a) ¬p ∨ ¬q  b) p ∧ ¬q  c) ¬p ∧ q  d) ¬p → ¬q

**10.** ¬(p ∨ q) is logically equivalent to:
a) ¬p ∨ ¬q  b) ¬p ∧ ¬q  c) p ∧ q  d) ¬p → q

**11.** Select ALL that are tautologies:
a) p ∨ ¬p
b) p ∧ ¬p
c) (p ∧ q) → p
d) p → (p ∧ q)

**12.** p → q is logically equivalent to:
a) p ∨ ¬q  b) ¬p ∨ q  c) ¬p ∧ q  d) q → p

**13.** True or False: (p ∧ q) ∨ T is a tautology (T is the constant "true").

**14.** ¬p ∨ (p ∧ q) simplifies to:
a) ¬p ∨ q  b) p  c) q  d) ¬p ∧ q

**15.** There are ______ different truth tables for compound propositions involving the two variables p and q.

**16.** True or False: (p ∨ ¬q) ∧ (¬p ∨ q) ∧ (¬p ∨ ¬q) is satisfiable.

**17.** True or False: (p → q) → r and p → (q → r) are logically equivalent.

**18.** The absorption law says p ∨ (p ∧ q) is equivalent to:
a) q  b) p  c) p ∧ q  d) T

---

## Part C: Predicates and quantifiers (Lecture 3)

**19.** ¬∀x P(x) is equivalent to:
a) ∀x ¬P(x)  b) ∃x ¬P(x)  c) ¬∃x P(x)  d) ∃x P(x)

**20.** Match each restricted-domain statement with its unpacked form (dropdown):
- ∀x>0 P(x)  →  ______
- ∃x>0 P(x)  →  ______
Options: ∀x(x>0 → P(x)) / ∀x(x>0 ∧ P(x)) / ∃x(x>0 → P(x)) / ∃x(x>0 ∧ P(x))

**21.** Domain = integers. P(x): "x is even." Q(x): "x is odd." Select ALL that are TRUE:
a) ∀x (P(x) ∨ Q(x))
b) ∀x P(x) ∨ ∀x Q(x)
c) ∃x (P(x) ∧ Q(x))
d) ∃x P(x) ∧ ∃x Q(x)

**22.** Domain = real numbers. Select ALL that are TRUE:
a) ∃y ∀x (x + y = x)
b) ∀x ∃y (x + y = 0)
c) ∃y ∀x (x + y = 0)
d) ∃y ∀x (y > x)
e) ∀x ∃y (y > x)

**23.** True or False: ∀x ∃y P(x,y) is logically equivalent to ∃y ∀x P(x,y).

**24.** Which is the negation of ∀x ∃y (P(x,y) ∧ ¬Q(x,y))?
a) ∃x ∀y (¬P(x,y) ∨ Q(x,y))
b) ∀x ∃y (¬P(x,y) ∨ Q(x,y))
c) ∃x ∀y (¬P(x,y) ∧ Q(x,y))
d) ∃x ∀y (P(x,y) ∨ ¬Q(x,y))

**25.** Which is the negation of ∃x ∀y (¬P(x,y) → Q(x,y))?
a) ∀x ∃y (¬P(x,y) ∧ ¬Q(x,y))
b) ∃x ∀y (¬P(x,y) ∧ ¬Q(x,y))
c) ∀x ∃y (P(x,y) ∧ ¬Q(x,y))
d) ∀x ∃y (¬P(x,y) ∨ ¬Q(x,y))

**26.** Let L(x,y) = "x loves y," domain = all people. "There is somebody whom everybody loves" is:
a) ∀x ∃y L(x,y)  b) ∃y ∀x L(x,y)  c) ∃x ∀y L(x,y)  d) ∀y ∃x L(x,y)

**27.** Domain = {1, 2, 3}. P(x): "x² < 5". Fill in: ∀x P(x) is ______ and ∃x P(x) is ______.

**28.** True or False: ∃x (P(x) ∧ Q(x)) is logically equivalent to ∃x P(x) ∧ ∃x Q(x).

**29.** In the formula ∃x (x + y = 1), the free variable is ______.

**30.** Select ALL statements that are logically equivalent to ∀x (P(x) ∧ Q(x)):
a) ∀x P(x) ∧ ∀x Q(x)
b) ∀x P(x) ∨ ∀x Q(x)
c) ∃x (P(x) ∧ Q(x))
d) ¬∃x (¬P(x) ∨ ¬Q(x))

---

## Part D: Rules of inference (Lecture 4)

**31.** Name the rule: "If it rains, the pool closes. It is raining. Therefore, the pool is closed."
a) Modus Ponens  b) Modus Tollens  c) Hypothetical Syllogism  d) Disjunctive Syllogism

**32.** Name the rule: "If it snows, the university closes. The university is not closed. Therefore, it did not snow."
a) Modus Ponens  b) Modus Tollens  c) Addition  d) Simplification

**33.** Name the rule: "Alice is a math major. Therefore, Alice is a math major or a CS major."
a) Simplification  b) Conjunction  c) Addition  d) Resolution

**34.** Name the rule: "If I swim, I stay in the sun. If I stay in the sun, I sunburn. Therefore, if I swim, I sunburn."
a) Modus Ponens  b) Modus Tollens  c) Hypothetical Syllogism  d) Resolution

**35.** Name the rule: "It's either hotter than 100° or the pollution is dangerous. It is not hotter than 100°. Therefore, the pollution is dangerous."
a) Disjunctive Syllogism  b) Modus Ponens  c) Addition  d) Conjunction

**36.** Concluding p from p → q and q is called the fallacy of:
a) denying the hypothesis  b) affirming the conclusion  c) modus tollens  d) begging the question

**37.** Which argument form is VALID?
a) p → q, ¬p, therefore ¬q
b) p → q, q, therefore p
c) p → q, ¬q, therefore ¬p
d) p ∨ q, p, therefore ¬q

**38.** Match each (dropdown):
- ∀x P(x) ∴ P(c) for any c →  ______
- P(c) for some c ∴ ∃x P(x) →  ______
Options: Universal Instantiation / Universal Generalization / Existential Instantiation / Existential Generalization

**39.** Premises: p ∨ q, ¬p, ¬q ∨ r. Which conclusion follows?
a) ¬r  b) r  c) p  d) nothing follows

**40.** Premises: "Every CS major has a personal computer." "Ralph does not have a personal computer." What follows?
a) Ralph is a CS major  b) Ralph is not a CS major  c) Ralph needs a computer  d) nothing follows

**41.** True or False: An argument is valid if and only if its premises are true in real life.

---

## Part E: Proofs (Lectures 5 and 6)

**42.** Match what you ASSUME at the start (dropdown):
- Proving p → q directly  →  ______
- Proving p → q by contraposition  →  ______
- Proving p ∨ q  →  ______
- Proving p → q by contradiction  →  ______
Options: Assume p / Assume ¬q / Assume ¬p (or ¬q) / Assume p AND ¬q

**43.** Fill in the definitions: An integer n is even if n = ______ for some integer k. An integer n is odd if n = ______ for some integer k.

**44.** The best technique to prove "√7 is irrational" is:
a) direct proof  b) contraposition  c) contradiction  d) cases

**45.** The best technique to prove "if n² is odd, then n is odd" is:
a) direct proof  b) contraposition  c) contradiction  d) exhaustive proof

**46.** True or False: Showing that a statement works for several examples is a valid proof of a "for all" statement.

**47.** True or False: One counterexample is enough to disprove "for all x, P(x)."

**48.** Match each term (dropdown):
- Lemma → ______
- Corollary → ______
- Conjecture → ______
Options: a statement believed true but not yet proven / a minor theorem used to help prove a bigger one / a theorem that follows directly from another theorem

**49.** In the proof that √2 is irrational, we reach a contradiction because we show:
a) a is odd  b) both a and b are even, contradicting "lowest terms"  c) b is negative  d) a² is odd

**50.** True or False: The product of two irrational numbers is always irrational.

**51.** To prove p ↔ q you must prove:
a) p → q only  b) q → p only  c) both p → q and q → p  d) ¬p → ¬q only

**52.** A proof that exhibits one specific example is called ______ (constructive / non-constructive). A proof that shows existence without finding the example is ______.

**53.** A uniqueness proof has two parts: ______ and ______.

**54.** How many perfect cubes are less than 100? ______

**55.** "Without loss of generality (WLOG)" is used to:
a) skip writing a case that is a mirror image of another case
b) assume the theorem is false
c) prove the converse
d) avoid defining variables

**56.** Cards each have a letter on one side and a number on the other. Rule: "If a card has a vowel on one side, then it has an even number on the other." You see: E, K, 4, 7. Which cards MUST be flipped to check the rule? Select ALL:
a) E  b) K  c) 4  d) 7

**57.** To prove x + 1/x ≥ 2 for x > 0, backward scratch work reduces it to: ______ ≥ 0.

**58.** True or False: If a < b < 0, then a² > b².

**59.** True or False: If m is even and n is odd, then m + n is odd.

**60.** To prove the statement "if 3n + 2 is odd, then n is odd," a direct proof gets stuck because you end up with n = (2k−1)/3. The better technique is ______.

---
---

## ANSWER KEY

### Part A
1. **c** (p → q is false only at T,F)
2. **c** (¬q → ¬p)
3. **False** (converse is NOT equivalent; only the contrapositive is)
4. **b** (p only if q means p → q)
5. **b** (¬ binds tightest, then ∧, then ∨, then →)
6. p=T,q=F: **F** (T → F). p=F,q=F: **T** (F → F is true).
7. **16** (2⁴)
8. AND = **1000**, OR = **1110**, XOR = **0110**

### Part B
9. **b** (¬(p→q) ≡ p ∧ ¬q)
10. **b** (De Morgan)
11. **a and c.** (b is a contradiction; d fails at p=T, q=F: T → F is false.)
12. **b** (p → q ≡ ¬p ∨ q)
13. **True** (anything ∨ T is T)
14. **a.** ¬p ∨ (p ∧ q) ≡ (¬p ∨ p) ∧ (¬p ∨ q) ≡ T ∧ (¬p ∨ q) ≡ ¬p ∨ q
15. **16** (4 rows, each can be T or F: 2⁴)
16. **True** (p=F, q=F makes all three clauses true)
17. **False** (counterexample p=F, q=F, r=F: left side is F, right side is T)
18. **b** (absorption: p ∨ (p ∧ q) ≡ p)

### Part C
19. **b**
20. ∀x>0 P(x) → **∀x(x>0 → P(x))**. ∃x>0 P(x) → **∃x(x>0 ∧ P(x))**. (∀ unpacks to →, ∃ unpacks to ∧.)
21. **a and d.** (a: every integer is even or odd. d: an even and an odd integer both exist. b is false: not all integers are even, and not all are odd. c is false: no integer is both.)
22. **a, b, e.** (a: y=0. b: y=−x. e: y=x+1. c is false: no single y works for all x. d is false: no single number is greater than every real.)
23. **False** (∃∀ implies ∀∃, but not the reverse)
24. **a.** ¬∀x∃y(P ∧ ¬Q) ≡ ∃x∀y¬(P ∧ ¬Q) ≡ ∃x∀y(¬P ∨ Q)
25. **a.** ¬∃x∀y(¬P → Q) ≡ ∀x∃y¬(¬P → Q) ≡ ∀x∃y(¬P ∧ ¬Q) (using ¬(a→b) ≡ a ∧ ¬b)
26. **b** (∃y∀x L(x,y): one person, loved by everyone)
27. ∀x P(x): **False** (3² = 9 is not < 5). ∃x P(x): **True** (1² = 1 < 5).
28. **False** (same x vs possibly different x)
29. **y**
30. **a and d.** (a is the allowed distribution of ∀ over ∧. d: ¬∃x(¬P ∨ ¬Q) ≡ ∀x(P ∧ Q) by De Morgan.)

### Part D
31. **a** Modus Ponens
32. **b** Modus Tollens
33. **c** Addition
34. **c** Hypothetical Syllogism
35. **a** Disjunctive Syllogism
36. **b** affirming the conclusion
37. **c** (modus tollens. a is denying the hypothesis, b is affirming the conclusion, d is invalid.)
38. **Universal Instantiation**; **Existential Generalization**
39. **b.** p ∨ q and ¬p give q (disjunctive syllogism). Then ¬q ∨ r and q give r.
40. **b** (universal modus tollens: if he were a CS major he'd have a PC)
41. **False** (validity is about structure: if the premises were true, the conclusion would have to be)

### Part E
42. Direct: **Assume p**. Contraposition: **Assume ¬q**. p ∨ q: **Assume ¬p (or ¬q)**. Contradiction: **Assume p AND ¬q**.
43. even: **2k**. odd: **2k+1**.
44. **c** (contradiction: "irrational" only means "not rational," so assume it IS rational)
45. **b** (contraposition: assume n is even, show n² is even)
46. **False** (examples are not a proof)
47. **True**
48. Lemma → **a minor theorem used to help prove a bigger one**. Corollary → **a theorem that follows directly from another theorem**. Conjecture → **a statement believed true but not yet proven**.
49. **b**
50. **False** (√2 · √2 = 2 is rational)
51. **c**
52. **constructive**; **non-constructive**
53. **existence** and **uniqueness**
54. **4** (1, 8, 27, 64; 5³ = 125 is too big)
55. **a**
56. **a and d.** E: vowel, so check the other side is even. 7: odd, so check the other side is NOT a vowel (contrapositive). K and 4 can never break the rule.
57. **(x − 1)²** (x + 1/x ≥ 2 ⇔ x² + 1 ≥ 2x ⇔ x² − 2x + 1 ≥ 0 ⇔ (x−1)² ≥ 0)
58. **True** (both negative with a further from zero than b, so a² > b²)
59. **True** (2k + (2l+1) = 2(k+l) + 1)
60. **contraposition** (assume n is even, show 3n+2 is even)

---

## Score yourself
- **54-60:** you're ready.
- **45-53:** re-read the topics for what you missed in [[Canvas Test 1 Review]].
- **Under 45:** the weakest part is the one to redo tonight (Parts C and D, quantifier negations and rules of inference, are the usual trouble spots).
