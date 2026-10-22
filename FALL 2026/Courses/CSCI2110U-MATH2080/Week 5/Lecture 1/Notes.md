---
tags: [notes, week5, lecture1, functions]
---

# Lecture 8: Functions (Section 2.3)

← [[../../CSCI2110U-MATH2080 - Discrete Math]] | [[Questions]]
Source: [[../../files/MATH2080_Lecture8_Sections_2p3_Functions.pdf]] (blank skeleton posted before the lecture)

> [!warning] Built BEFORE the lecture (Oct 5)
> This was built from the posted skeleton plus the textbook. After the lecture, when the instructor posts the `_filled.pdf` version, compare it against this file and fix anything he did differently.

---

## 1. Definition and vocabulary

A **function f: A → B** assigns to **every** element of A **exactly one** element of B. Write f(a) = b.

- **Domain** = A (the inputs). **Codomain** = B (the allowed outputs).
- **Range** = the outputs that actually get hit = f(A) = {f(a) | a ∈ A}. The range is a subset of the codomain.
- **Image of a subset:** for S ⊆ A, f(S) = {f(x) | x ∈ S}.

> [!important] "Every" and "exactly one"
> Every input must have an output (no input left out), and no input can have two outputs. A rule where one input gives two outputs is NOT a function.

**Domain of a closed-form function** = all inputs where the formula makes sense:
- 1/(x+4): need x ≠ −4
- ln(y): need y > 0
- arccos(t² − 1): need −1 ≤ t² − 1 ≤ 1, so 0 ≤ t² ≤ 2, so −√2 ≤ t ≤ √2

## 2. One-to-one and onto

| Term | Meaning | Test |
|---|---|---|
| **One-to-one (injective)** | different inputs give different outputs: a1 ≠ a2 ⟹ f(a1) ≠ f(a2) | To prove: assume f(a1) = f(a2), show a1 = a2. To disprove: find two different inputs with the same output |
| **Onto (surjective)** | every element of the codomain is hit: Range(f) = B | To prove: take an arbitrary b in B, solve f(a) = b for a, check a is in the domain. To disprove: find a b that nothing maps to |
| **Bijection** | one-to-one AND onto | needed for an inverse |

**Example 4:** (all use x²)
| Function | One-to-one? | Onto? |
|---|---|---|
| f1: ℝ → ℝ | No: f(2) = f(−2) | No: negatives are never hit |
| f2: ℝ → [0, ∞) | No: f(2) = f(−2) | Yes: every y ≥ 0 equals (√y)² |
| f3: (−∞, 0] → [0, ∞) | Yes: strictly decreasing on (−∞, 0] | Yes |

So f3 is a **bijection**; the domain and codomain choices decide everything.

**Example 5:**
| Function | One-to-one? | Onto? | Why |
|---|---|---|---|
| f1: ℤ → ℤ, f1(n) = n + 1 | Yes | Yes | n+1 = m has the solution n = m−1 |
| f2: ℤ → ℤ, f2(n) = n² − 3 | No: f(1) = f(−1) = −2 | No: −1 would need n² = 2 | |
| f3: ℤ×ℤ → ℤ, f3(m,n) = m + 3n | No: (3,0) and (0,1) both give 3 | Yes: f3(m, 0) = m | |
| f4: ℤ×ℤ → ℤ, f4(m,n) = m² + n² | No: (1,0) and (0,1) both give 1 | No: negatives and 3 aren't hit | |

> [!tip] Quick shortcut
> A real function that is **strictly increasing** or **strictly decreasing** is one-to-one.

## 3. Inverse functions

f has an inverse **only if f is a bijection**. Then f⁻¹(b) = a exactly when f(a) = b. (Don't confuse f⁻¹ with 1/f.)

**Example 6: f(x) = 4x/(x − 3), domain ℝ − {3}.**

**(1) Prove f is one-to-one.** Assume f(a) = f(b):

4a/(a−3) = 4b/(b−3)
4a(b−3) = 4b(a−3)
4ab − 12a = 4ab − 12b
−12a = −12b, so a = b. ∎

**(2) Find f⁻¹.** Set y = 4x/(x−3) and solve for x:

y(x − 3) = 4x
yx − 3y = 4x
yx − 4x = 3y
x(y − 4) = 3y
**x = 3y/(y − 4)**

So f⁻¹(y) = 3y/(y − 4). **The range:** y can't be 4, since 4x/(x−3) = 4 would force 4x = 4x − 12, which is impossible. So the range is ℝ − {4}, and **f⁻¹: ℝ − {4} → ℝ − {3}.**

**Recipe for finding an inverse:** write y = f(x), solve for x in terms of y, then rename. Always state the new domain (= the old range).

## 4. Composition

(g ∘ f)(a) = g(f(a)). **Apply f FIRST, then g.** Requires f: A → B and g: B → C.

- Order matters: g ∘ f is usually not f ∘ g. Example: f(x) = 2x+1, g(x) = x². (g∘f)(3) = g(7) = 49 but (f∘g)(3) = f(9) = 19.
- **Identity function** i_A(x) = x.
- f ∘ f⁻¹ = i_B and f⁻¹ ∘ f = i_A.

## 5. Graph of a function

G(f) = {(a, f(a)) | a ∈ A}, a subset of A × B (links back to Cartesian products from Lecture 7).

## 6. Important functions

- **Floor ⌊x⌋** = the greatest integer ≤ x. ⌊3.7⌋ = 3, ⌊−3.2⌋ = **−4** (not −3), ⌊5⌋ = 5.
- **Ceiling ⌈x⌉** = the least integer ≥ x. ⌈3.2⌉ = 4, ⌈−3.7⌉ = **−3**, ⌈5⌉ = 5.
- **Factorial** n! = n(n−1)...2·1, with 0! = 1. (5! = 120.)

> [!warning] Negative numbers
> Floor of a negative decimal goes DOWN (more negative). ⌊−2.5⌋ = −3, ⌈−2.5⌉ = −2.

## 7. "Time permitting" examples worked out

**(1)** S = {−1, 0, 2, 4, 7}.
- f(x) = 2x + 1: f(S) = **{−1, 1, 5, 9, 15}**
- f(x) = ⌈x/5⌉: ⌈−0.2⌉ = 0, ⌈0⌉ = 0, ⌈0.4⌉ = 1, ⌈0.8⌉ = 1, ⌈1.4⌉ = 2. So f(S) = **{0, 1, 2}**

**(2a)** If g and f∘g are one-to-one, is f one-to-one? **No.** Counterexample: A = {1}, B = {1, 2}, C = {1}, g(1) = 1, f(1) = f(2) = 1. Then g and f∘g are one-to-one but f is not.

**(2b)** If g and f∘g are onto, is f onto? **Yes.** f∘g being onto means every c in C equals f(g(a)) for some a, and g(a) ∈ B. So every c is hit by f, so f is onto.

**(3)** f(S ∩ T) ⊆ f(S) ∩ f(T) can be proper. Take f(x) = x², S = {−1}, T = {1}. Then S ∩ T = ∅, so f(S ∩ T) = ∅. But f(S) ∩ f(T) = {1} ∩ {1} = {1}.

**(4)** g(x) = ⌊x⌋.
- g⁻¹({−1, 0, 1}) = all x with ⌊x⌋ ∈ {−1, 0, 1} = **[−1, 2)**
- g⁻¹({x | 0 < x < 1}) = **∅**, because ⌊x⌋ is an integer and no integer lies strictly between 0 and 1.

---

## Summary checklist
- [ ] Define function, domain, codomain, range, and tell range from codomain
- [ ] Prove one-to-one (assume f(a)=f(b)) and disprove with a collision
- [ ] Prove onto (solve f(a)=b) and disprove by finding an unhit value
- [ ] Find an inverse and its domain (swap and solve, state the range)
- [ ] Compute g ∘ f in the right order
- [ ] Evaluate floor, ceiling (careful with negatives) and factorial

**Next:** [[Questions]]
