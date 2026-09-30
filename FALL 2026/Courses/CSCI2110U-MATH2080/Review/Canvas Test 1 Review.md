---
tags: [review, canvas-test-1]
---

# Canvas Test 1 Review (Oct 3) — Lectures 1-6

← [[../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Confirmed scope
> Canvas confirms Lecture 6 is labeled **"LAST LECTURE COVERED ON CANVAS TEST I."** So this test covers: §1.1 (propositions), §1.3 (equivalences), §1.4-1.5 (predicates/quantifiers), §1.6 (rules of inference), §1.7 (intro to proofs), §1.8 (proof strategy). Lecture 7 (§2.1-2.2, Sets — Oct 1) is NOT covered.

> [!warning] Format for each topic below
> Notes → Solved Example → Practice Question (a variation) → Step-by-step Answer. Cover the solved example with your hand, try the variation cold, THEN check the answer beneath it.

---

## Topic 1 — Conditional statements: converse, inverse, contrapositive

**Notes:** p→q is false only when p=T, q=F. Contrapositive (¬q→¬p) is ALWAYS logically equivalent to p→q. Converse (q→p) and inverse (¬p→¬q) are NOT equivalent to the original — only to each other.

**Solved example:** Write the converse, inverse, and contrapositive of: "If it snows, then school is cancelled."
- Converse: "If school is cancelled, then it snows."
- Inverse: "If it does not snow, then school is not cancelled."
- Contrapositive: "If school is not cancelled, then it does not snow." (equivalent to original)

**Practice question (variation):** Write the converse, inverse, and contrapositive of: "If the triangle is equilateral, then all its angles are equal."

**Answer:**
1. Converse: "If all the triangle's angles are equal, then it is equilateral."
2. Inverse: "If the triangle is not equilateral, then not all its angles are equal."
3. Contrapositive: "If not all the triangle's angles are equal, then the triangle is not equilateral." (this one is guaranteed to match the original's truth value)

---

## Topic 2 — Truth tables and operator precedence

**Notes:** Precedence (tightest first): ¬, ∧, ∨, →, ↔. n variables → 2ⁿ rows.

**Solved example:** Build the truth table for (p∨¬q)→(p∧q).

| p | q | ¬q | p∨¬q | p∧q | result |
|---|---|---|---|---|---|
| T | T | F | T | T | T |
| T | F | T | T | F | F |
| F | T | F | F | F | T |
| F | F | T | T | F | F |

**Practice question (variation):** Build the truth table for (¬p∧q)→(p∨q).

**Answer:**
| p | q | ¬p | ¬p∧q | p∨q | result |
|---|---|---|---|---|---|
| T | T | F | F | T | T |
| T | F | F | F | T | T |
| F | T | T | T | T | T |
| F | F | T | F | F | T |

(This one is a tautology — all T. Antecedent ¬p∧q is only true when p=F,q=T, and in that row p∨q=T too, so the conditional never fails.)

---

## Topic 3 — Propositional equivalences (De Morgan's, tautology proofs)

**Notes:** ¬(p∧q)≡¬p∨¬q, ¬(p∨q)≡¬p∧¬q. p→q≡¬p∨q. Use named laws to chain a proof instead of a truth table.

**Solved example:** Show ¬(p→q) and p∧¬q are equivalent, via equivalences.

¬(p→q) ≡ ¬(¬p∨q) [conditional-disjunction] ≡ ¬(¬p)∧¬q [De Morgan's] ≡ p∧¬q [double negation]

**Practice question (variation):** Show ¬(p↔q) and (p∧¬q)∨(¬p∧q) are equivalent — or just simplify ¬(p∧q)∨(p∧¬q) using named laws.

**Answer (simplifying ¬(p∧q)∨(p∧¬q)):**

¬(p∧q)∨(p∧¬q) ≡ (¬p∨¬q)∨(p∧¬q) [De Morgan's]
≡ ¬q∨(¬p∨(p∧¬q)) [associative/commutative regroup]
≡ ¬q∨((¬p∨p)∧(¬p∨¬q)) [distributive]
≡ ¬q∨(T∧(¬p∨¬q)) [negation law]
≡ ¬q∨(¬p∨¬q) [identity law]
≡ ¬p∨¬q [idempotent — ¬q∨¬q∨¬p collapses]

**Final simplified form: ¬p∨¬q**

---

## Topic 4 — Quantifiers (∀, ∃), restricted domains, negation

**Notes:** ∀xP(x) false needs 1 counterexample. ¬∀xP(x)≡∃x¬P(x), ¬∃xP(x)≡∀x¬P(x). Restricted ∀ unpacks to →; restricted ∃ unpacks to ∧. Cannot distribute ∀ over ∨, or ∃ over ∧.

**Solved example:** Negate "Every student in this class has studied calculus."

∀x C(x) → ¬∀x C(x) ≡ ∃x ¬C(x) = "There is a student who has NOT studied calculus."

**Practice question (variation):** Negate: "There is a student in this class who has taken every course in the department."

**Answer:**
Original: ∃x∀y T(x,y) where T(x,y)="x has taken course y"
Negate: ¬∃x∀y T(x,y) ≡ ∀x¬∀y T(x,y) ≡ ∀x∃y ¬T(x,y)
In English: "For every student, there is some course in the department that they have NOT taken."

---

## Topic 5 — Nested quantifiers, order sensitivity

**Notes:** Same-type quantifiers (∀∀ or ∃∃) can swap order freely. Mixed types (∃∀ vs ∀∃) CANNOT swap — order changes meaning. ∃y∀xP(x,y) → ∀x∃yP(x,y) always holds; the reverse does not.

**Solved example:** Q(x,y): "x+y=0", domain=reals. ∃y∀xQ(x,y) is False (no single y works for every x); ∀x∃yQ(x,y) is True (pick y=-x each time).

**Practice question (variation):** P(x,y): "x is the reciprocal of y" (xy=1), domain = nonzero reals. Determine the truth value of both ∃y∀xP(x,y) and ∀x∃yP(x,y).

**Answer:**
- ∃y∀xP(x,y): "there's ONE y that is the reciprocal of EVERY x" → **False** — no single number is the reciprocal of every nonzero real simultaneously.
- ∀x∃yP(x,y): "for every x, SOME y is its reciprocal" → **True** — pick y=1/x each time, which always exists since x≠0.
This confirms the one-directional rule: the ∃∀ statement being true would force the ∀∃ one true, but not vice versa — here ∃∀ is false while ∀∃ is true, consistent with the rule (no contradiction).

---

## Topic 6 — Rules of inference (propositional)

**Notes:** Modus Ponens (p,p→q∴q), Modus Tollens (¬q,p→q∴¬p), Hypothetical Syllogism (p→q,q→r∴p→r), Disjunctive Syllogism (p∨q,¬p∴q), Addition, Simplification, Conjunction, Resolution.

**Solved example:** Premises: ¬p∧q, r→p, ¬r→s, s→t. Show t follows.
1. ¬p∧q (premise) 2. ¬p (simplification) 3. r→p (premise) 4. ¬r (modus tollens 2,3) 5. ¬r→s (premise) 6. s (modus ponens 4,5) 7. s→t (premise) 8. t (modus ponens 6,7)

**Practice question (variation):** Premises: p∨q, ¬p∨r, ¬r∨s, ¬q. Show s follows.

**Answer:**
1. p∨q (premise)
2. ¬q (premise)
3. p (disjunctive syllogism, 1&2)
4. ¬p∨r (premise)
5. r (disjunctive syllogism, 3&4 — since p is true, ¬p is false, so r must hold)
6. ¬r∨s (premise)
7. s (disjunctive syllogism, 5&6)

---

## Topic 7 — Quantifier rules of inference (Universal/Existential Instantiation/Generalization)

**Notes:** Universal Instantiation: ∀xP(x)∴P(c) any c. Existential Instantiation: ∃xP(x)∴P(c) SOME (unknown) c. Existential Generalization: P(c) for some c∴∃xP(x). Universal Generalization: P(c) for ARBITRARY c∴∀xP(x).

**Solved example:** Premises: "Everyone in NJ lives within 50 miles of the ocean" (∀xL(x)), "Someone in NJ hasn't seen the ocean" (∃x¬S(x)). Show: "someone who lives within 50 miles hasn't seen it" (∃x(L(x)∧¬S(x))).
1. ∃x¬S(x) premise 2. ¬S(c) some c (existential instantiation) 3. ∀xL(x) premise 4. L(c) (universal instantiation, same c) 5. L(c)∧¬S(c) (conjunction) 6. ∃x(L(x)∧¬S(x)) (existential generalization)

**Practice question (variation):** Premises: "Every computer science major has taken discrete math" (∀x(C(x)→D(x))), "Maya is a computer science major" (C(Maya)). Show D(Maya).

**Answer:**
1. ∀x(C(x)→D(x)) premise
2. C(Maya)→D(Maya) (universal instantiation, c=Maya)
3. C(Maya) premise
4. D(Maya) (modus ponens, 2&3)

(This combo — universal instantiation + modus ponens in one shot — is called **Universal Modus Ponens**.)

---

## Topic 8 — Direct proof

**Notes:** Assume hypothesis true, apply definitions, algebra to reach conclusion's definition. Definitions: even n=2k, odd n=2k+1, rational r=p/q (q≠0).

**Solved example:** Prove the product of two rationals is rational.
Let x=a/b, y=c/d (a,b,c,d integers, b,d≠0). xy=(ac)/(bd). ac,bd are integers, bd≠0. So xy is rational. ∎

**Practice question (variation):** Prove that the sum of two even integers is even.

**Answer:**
Let m,n be even integers. By definition, m=2j and n=2k for integers j,k.
m+n = 2j+2k = 2(j+k)
Since j+k is an integer, m+n is 2×(integer), which matches the definition of even.
Therefore, m+n is even. ∎

---

## Topic 9 — Proof by contraposition

**Notes:** Use when hypothesis is hard to use directly but negated conclusion gives something concrete. Prove ¬q→¬p instead of p→q.

**Solved example:** Prove: if m+n is even, then m,n are both even or both odd.
Contrapositive: if NOT(both even or both odd) — i.e. one even, one odd (WLOG m even, n odd) — then m+n is odd.
m=2k, n=2l+1 → m+n=2(k+l)+1, odd. ∎

**Practice question (variation):** Prove: if n² is odd, then n is odd.

**Answer:**
*Proof by contraposition.* Prove the contrapositive: if n is even, then n² is even.
Assume n is even: n=2k for integer k.
n² = (2k)² = 4k² = 2(2k²)
Since 2k² is an integer, n² is 2×(integer) — even, by definition.
This proves the contrapositive, so the original statement holds: if n² is odd, then n is odd. ∎

---

## Topic 10 — Proof by contradiction

**Notes:** Assume the theorem is FALSE, derive something impossible, conclude the assumption was wrong. Classic use: proving irrationality (nothing to build from directly with "not rational").

**Solved example:** Prove √2 is irrational.
Assume √2=a/b (reduced form, no common factors, b≠0). Then 2b²=a² → a² even → a even → a=2c → b²=2c² → b² even → b even. But then a,b share factor 2, contradicting "reduced form." So √2 is irrational. ∎

**Practice question (variation):** Prove that √3 is irrational.

**Answer:**
*Proof by contradiction.* Assume √3 is rational: √3 = a/b, where a,b are integers with no common factors, b≠0.
Squaring: 3 = a²/b² → 3b² = a²
So a² is a multiple of 3, which means a itself must be a multiple of 3 (since 3 is prime — if 3 didn't divide a, it couldn't divide a²). Write a=3c for integer c.
Substituting: 3b² = (3c)² = 9c² → b² = 3c²
So b² is a multiple of 3 → b is a multiple of 3 too.
**Contradiction:** both a and b are multiples of 3, contradicting "no common factors."
Therefore √3 is irrational. ∎

---

## Topic 11 — Biconditional (iff) proofs

**Notes:** Prove p↔q by proving p→q AND q→p separately. Do whichever direction is easier first; switch technique (direct vs contrapositive) per direction as needed.

**Solved example:** Show n²+3 is odd iff n is even.
(⇐, direct) n even → n=2k → n²+3=2(2k²+1)+1, odd. ✓
(⇒, contrapositive) n odd → n=2k+1 → n²+3=2(2k²+2k+2), even → proves contrapositive of (⇒). ✓

**Practice question (variation):** Show that n is odd if and only if n²-1 is even. Wait — try instead: show n is odd if and only if 3n+1 is even.

**Answer:**
**(⇐) n odd → 3n+1 even (direct):** n=2k+1 → 3n+1 = 3(2k+1)+1 = 6k+3+1 = 6k+4 = 2(3k+2). Since 3k+2 is an integer, 3n+1 is even. ✓

**(⇒) 3n+1 even → n odd (contrapositive: n even → 3n+1 odd):** n=2k → 3n+1 = 6k+1 = 2(3k)+1. Since 3k is an integer, 3n+1 is odd. This proves the contrapositive, so (⇒) holds. ✓

Both directions proven → n is odd ⟺ 3n+1 is even. ∎

---

## Topic 12 — Exhaustive proof and proof by cases

**Notes:** Exhaustive: finite/small number of cases, check every single one. Proof by cases: split hypothesis into cases (each an added premise), prove conclusion in each case separately, covering ALL possibilities. WLOG: skip writing a symmetric case twice.

**Solved example:** Prove |ab|=|a||b| for real a,b — 4 cases based on signs:
(i) a≥0,b≥0: ab≥0, so |ab|=ab=|a||b|. (ii) a≥0,b<0: ab≤0, |ab|=-ab=a(-b)=|a||b|. (iii) a<0,b≥0: symmetric to (ii) by WLOG. (iv) a<0,b<0: ab>0, |ab|=ab=(-a)(-b)=|a||b|.

**Practice question (variation):** Prove that for any integer n, n² ≥ n. (Use cases: n=0, n≥1, n≤-1.)

**Answer:**
*Proof by cases.*
**Case n=0:** 0² = 0 ≥ 0. ✓
**Case n≥1:** multiply both sides of n≥1 by the positive number n: n·n ≥ n·1, so n² ≥ n. ✓
**Case n≤-1:** n² ≥ 0 always (squares are nonnegative), and n is negative (n≤-1<0), so n² ≥ 0 > n automatically. ✓
All integers fall into one of these three cases, and n²≥n holds in each → true for all integers n. ∎

---

## Topic 13 — Existence proofs (constructive vs. non-constructive)

**Notes:** Constructive: exhibit a specific example that works. Non-constructive: prove something must exist without pinning down which one.

**Solved example (constructive):** Prove there's a positive integer equal to the sum of the positive integers smaller than it. Answer: 6 = 1+2+3. ∎ (explicit example given)

**Solved example (non-constructive):** Prove there exist irrationals x,y with xʸ rational.
Consider √2^√2. Either it's rational (done: x=y=√2) or it's irrational — if so, let x=√2^√2 (irrational), y=√2: xʸ = (√2^√2)^√2 = √2² = 2, rational. Either way, such x,y exist — but we never determined WHICH case actually holds. ∎

**Practice question (variation, constructive):** Prove there exists a positive integer that is a perfect square and also one more than a perfect square (i.e. find n where n is a perfect square and n-1 is also a perfect square).

**Answer:**
Try small perfect squares: 0,1,4,9,16,25,...
Check n=1: n-1=0=0², and n=1=1². Both are perfect squares (0 counts as a perfect square, 0²=0).
**n=1 works: 1 is a perfect square (1²), and 1-1=0 is also a perfect square (0²).** ∎
(This is a constructive proof — we exhibited the specific value n=1.)

---

## Topic 14 — Uniqueness proofs

**Notes:** Two parts: (1) Existence — show some x satisfies the property; (2) Uniqueness — show any y satisfying the property must equal x.

**Solved example:** Show ∃!y∀x∈ℝ(x+y=x) — the additive identity is unique.
**Existence:** y=0 works, since x+0=x for all real x.
**Uniqueness:** suppose y' also satisfies ∀x(x+y'=x). Plug in x=0: 0+y'=0, so y'=0. Hence y=0 is the only one. ∎

**Practice question (variation):** Show that the multiplicative identity is unique: ∃!y∀x∈ℝ, x≠0 (xy=x).

**Answer:**
**Existence:** y=1 works, since x·1=x for all nonzero real x.
**Uniqueness:** Suppose y' also satisfies xy'=x for all nonzero x. Plug in x=1 (valid since 1≠0): 1·y'=1, so y'=1.
Since any y satisfying the property must equal 1, the multiplicative identity is unique (y=1). ∎

---

## Topic 15 — Backward/forward reasoning (AM-GM style proofs)

**Notes:** Sometimes it's easier to start from what you want to prove and work backward to something obviously true, then present the argument forward for the formal write-up.

**Solved example:** Prove (x+y)/2 > √(xy) for distinct positive reals x,y.
**Backward scratch work:** Want (x+y)/2 > √(xy). This holds iff x+y > 2√(xy) iff x+y-2√(xy) > 0 iff (√x - √y)² > 0 — true since x≠y means √x≠√y, so (√x-√y)² is a nonzero square, always positive.
**Forward formal proof:** Since x≠y, √x≠√y, so (√x-√y)² > 0. Expanding: x - 2√(xy) + y > 0, so x+y > 2√(xy), so (x+y)/2 > √(xy). ∎

**Practice question (variation):** Prove that for any positive real number x, x + 1/x ≥ 2.

**Answer:**
**Backward scratch work:** Want x + 1/x ≥ 2. This holds iff x² + 1 ≥ 2x (multiply both sides by x>0) iff x² - 2x + 1 ≥ 0 iff (x-1)² ≥ 0 — always true, since any real number squared is nonnegative.

**Forward formal proof:** For any real number x, (x-1)² ≥ 0. Expanding: x² - 2x + 1 ≥ 0, so x² + 1 ≥ 2x. Since x is positive, divide both sides by x (inequality direction unchanged since x>0): x + 1/x ≥ 2. ∎

---

## Final pre-test checklist
- [ ] Converse/inverse/contrapositive — instant recall
- [ ] Truth tables for any compound proposition, column by column
- [ ] Chain 3+ named equivalences to simplify or prove a tautology
- [ ] Negate a quantified statement (single and nested) to the point where ¬ touches only predicates
- [ ] Know when ∃∀ ≠ ∀∃ and why
- [ ] All 8 propositional rules of inference + the 4 quantifier rules, by shape
- [ ] Direct proof, contraposition, and contradiction — know when each is the right tool
- [ ] Biconditional: prove both directions, mixing techniques if needed
- [ ] Proof by cases / exhaustive proof / WLOG
- [ ] Constructive vs non-constructive existence proofs
- [ ] Uniqueness proofs: existence + uniqueness, two separate parts
- [ ] Backward reasoning as scratch work, written forward as the final proof
