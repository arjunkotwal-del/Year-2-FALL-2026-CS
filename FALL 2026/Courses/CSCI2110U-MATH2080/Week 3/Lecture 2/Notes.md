---
tags: [notes, week3, lecture2, proofs]
---

# Lecture 5 — Introduction to Proofs (Section 1.7)

← [[../Lecture 1/Notes|Week 3 Lecture 1 (Rules of Inference)]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]
Textbook: [[../../files/Rosen - Discrete Mathematics and Its Applications (8th ed).pdf]] (Section 1.7, pages 85-95)

> [!info] Confirmed against the real posted lecture PDF
> Cross-checked against [[../../files/MATH2080_Lecture5_Sections_1p7_ProofsIntro.pdf]] (Canvas, Lecture 5, Sept 24). Slide skeleton filled in using the textbook's own numbered examples.

> [!warning] This is the payoff lecture
> Everything since Week 1 — connectives, equivalences, quantifiers, rules of inference — was building toward THIS. This is where you actually learn to write a mathematical proof from scratch. Confirmed by the instructor: proof questions on the midterm/final are usually just "know the definition + apply one technique," not creative leaps.

---

## 1. Terminology

- **Theorem:** a statement shown to be true, important enough to be named. (Weaker versions: *proposition*, *fact*, *result* — rank roughly theorem > proposition > fact/result.)
- **Axiom / Postulate:** a statement assumed true without proof (the starting foundation).
- **Proof:** a valid argument establishing a theorem's truth — built from axioms, hypotheses, previously proven theorems, and rules of inference.
- **Lemma:** a minor theorem used as a stepping stone inside a bigger proof.
- **Corollary:** a theorem that follows quickly/directly from another already-proven theorem.
- **Conjecture:** a statement believed true but not yet proven (or disproven). Becomes a theorem once proven.

---

## 2. Key definitions used throughout this course

- **Even integer:** n is even if there exists an integer k such that n = 2k.
- **Odd integer:** n is odd if there exists an integer k such that n = 2k+1.
- **Rational number:** r is rational if there exist integers p, q (q≠0) such that r = p/q. If no such p,q exist, r is **irrational**.

> [!important] Memorize these cold
> Nearly every proof in this section plugs into one of these three definitions. If you don't have "even = 2k" and "odd = 2k+1" automatic, you can't start any of these proofs.

---

## 3. How theorems are structured

Most theorems are secretly of the form **∀x(P(x) → Q(x))**, even when the "for all" is left implicit. Example: "If x > y, where x and y are positive reals, then x² > y²" really means "For all positive reals x, y: if x>y then x²>y²."

**Handling different conclusion shapes:**
- Conclusion is itself **p → q**: add p to your premises, deduce q.
- Conclusion is a **disjunction p∨q**: add ¬p to your premises and deduce q (or add ¬q and deduce p).
- Conclusion is a **conjunction p∧q**: prove p and prove q *separately*, as two independent mini-proofs.
- Conclusion is a **biconditional p↔q**: prove p→q AND q→p (two directions, usually two separate arguments).

---

## 4. Direct proof

**Method:** assume p is true, use definitions/algebra/previous results, derive that q must also be true.

**Worked example:** Prove that the product of any two rational numbers is a rational number.

*Proof.* Let r and s be rational. By definition, r = a/b and s = c/d for integers a,b,c,d with b≠0, d≠0. Then:

rs = (a/b)(c/d) = (ac)/(bd)

Since a,b,c,d are integers, ac and bd are also integers, and bd≠0 (product of two nonzero numbers). So rs is expressed as an integer over a nonzero integer — by definition, rs is rational. ∎

**Second worked example:** Prove that if n is an odd integer, then n² is odd.

*Proof.* Assume n is odd, so n = 2k+1 for some integer k. Then:

n² = (2k+1)² = 4k² + 4k + 1 = 2(2k²+2k) + 1

Since 2k²+2k is an integer, n² has the form 2(integer)+1 — by definition, n² is odd. ∎

> [!tip] The pattern every direct proof follows
> 1. Write down the definition of your hypothesis (turns "n is odd" into "n = 2k+1").
> 2. Substitute/manipulate algebraically toward what you need to show.
> 3. Recognize the final expression matches the DEFINITION of your target property.

---

## 5. Proof by contraposition

**Method:** relies on p→q ≡ ¬q→¬p (proved way back in Week 2). Assume ¬q, derive ¬p. This is your go-to when a *direct* proof stalls.

**Worked example:** Prove that if m, n are integers such that m+n is even, then m and n are either both even or both odd.

*Proof (by contraposition).* Contrapositive: "if m and n are NOT both even or both odd" (i.e., one is even and the other odd), "then m+n is NOT even" (i.e., m+n is odd).

Assume, without loss of generality, m is even and n is odd: m=2j, n=2k+1 for integers j,k. Then:

m+n = 2j + 2k + 1 = 2(j+k) + 1

This is odd by definition. We've proven the contrapositive, so the original statement is true. ∎

> [!tip] When to reach for contraposition instead of direct
> If your hypothesis is something *hard to use directly* (like "x is irrational" — hard to build FROM), but the negated conclusion gives you something concrete to work WITH (like "x is even" — easy to plug in as n=2k), switch to contraposition.

---

## 6. Proof by contradiction

**Method:** assume the theorem is FALSE (i.e. assume ¬p where p is what you want to prove), derive something impossible (a contradiction, like r∧¬r for some r), conclude your assumption was wrong, so p must be true.

**Worked example (the classic one):** Prove that √2 is irrational.

*Proof (by contradiction).* Suppose, for contradiction, that √2 IS rational. Then √2 = a/b for integers a,b with no common factors (fraction in lowest terms), b≠0.

Squaring both sides: 2 = a²/b², so a² = 2b².

This means a² is even. (A fact worth knowing: if a² is even, then a itself must be even — provable separately.) So a = 2c for some integer c. Substituting:

(2c)² = 2b² → 4c² = 2b² → b² = 2c²

So b² is even too, meaning b is even.

**Contradiction:** we assumed a and b share NO common factors, but we've just shown both a and b are even — meaning they share a factor of 2. Contradiction. So our assumption (√2 is rational) must be false — √2 is irrational. ∎

> [!tip] This exact proof template generalizes
> The same structure proves √3, cube-root-of-2, and in general √n is irrational whenever n isn't a perfect square.

---

## 7. Proof of biconditionals (equivalences)

To prove p ↔ q, prove **both directions**: p→q AND q→p, usually as two separate mini-proofs.

**Worked example:** Show that n² + 3 is odd if and only if n is even.

**(⇒) direction:** Assume n is even, so n=2k. Then n²+3 = 4k²+3 = 2(2k²+1)+1 — odd, by definition. ✓

**(⇐) direction — proved via contrapositive:** Instead of assuming n²+3 is odd directly, prove the contrapositive "if n is odd, then n²+3 is even." Assume n=2k+1. Then n²+3 = (2k+1)²+3 = 4k²+4k+1+3 = 4k²+4k+4 = 2(2k²+2k+2) — even, by definition. This proves the contrapositive, so the original (⇐) direction holds. ✓

Both directions proven → the biconditional is established. ∎

---

## 8. Counterexamples — disproving a conjecture

To disprove a **∀x P(x)** claim, you only need ONE x where P(x) fails.

**Worked example:** Conjecture: "If n is a natural number greater than 1, then 2ⁿ−1 is a prime number."

**Counterexample:** n=4. 2⁴−1 = 15 = 3×5 — not prime. The conjecture is **false**.

(Sanity check that it "looks true" for small n first: n=2 gives 3 (prime), n=3 gives 7 (prime) — this is why it's tempting to believe, and exactly why you need to actually check further before trusting a pattern.)

---

## 9. Vacuous and trivial proofs (quick mentions)

- **Vacuous proof:** if you can show the hypothesis p is simply FALSE, then p→q is automatically true (F→anything=T) — no work needed on q at all.
- **Trivial proof:** if you can show the conclusion q is simply TRUE regardless of p, then p→q is automatically true.

Both are legitimate proof techniques, just often used for edge cases (like proving a statement holds for n=0 when the "interesting" hypothesis doesn't even apply there).

---

## 10. Common mistakes in proofs (assigned reading — Rosen p.93)

- **Dividing by zero disguised in algebra** — e.g. the classic fake proof that 1=2 hides a division by (a−b) when a=b, i.e. dividing by 0.
- **Fallacy of affirming the conclusion / denying the hypothesis** — same traps from Lecture 4, now showing up inside "proofs."
- **Begging the question / circular reasoning** — using the statement you're trying to prove (or something equivalent to it) as a step in your own proof, without justification.

---

## Summary checklist
- [ ] Know the definitions of even, odd, rational (and irrational) cold — can produce them instantly
- [ ] Can write a direct proof: assume hypothesis, substitute definition, algebra to target definition
- [ ] Know when to switch to contraposition (hypothesis hard to use directly, negated conclusion easier to work with)
- [ ] Can execute the √2-is-irrational proof by contradiction from memory, including WHY the "no common factors" setup matters
- [ ] Can prove a biconditional by proving both directions separately
- [ ] Can disprove a false ∀ claim with a single counterexample

**Next:** → [[Questions]] (real honour homework: §1.7 #5, 9, 11, 29, 37, 41)
