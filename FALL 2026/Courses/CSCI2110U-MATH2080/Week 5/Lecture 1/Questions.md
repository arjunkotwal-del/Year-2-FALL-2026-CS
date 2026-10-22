---
tags: [practice, week5, lecture1, functions]
---

# Lecture 8: Practice Questions (Functions)

← [[Notes]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Honour homework for this lecture (8th edition, from the slide)
> **§2.3:** #3, 5, 8 & 9, 10 & 11, 12 & 13, 31, 33, 37, 47, 65, 73
> (7th ed: #3, 5, 8 & 9, 10 & 11, 12 & 13, 31, 33, 35, 45, 63, 71.) Odd answers are in the back of the textbook.

Do these on paper first, then check the answers at the bottom.

---

## Part A: Quick questions (test style)

**1.** f: ℝ → ℝ, f(x) = 3x − 7. Is f one-to-one? Is f onto?

**2.** f: ℤ → ℤ, f(n) = 2n. Is f one-to-one? Is f onto?

**3.** f: ℤ → ℤ, f(n) = n². Is f one-to-one? Is f onto?

**4.** Select ALL bijections:
a) f: ℝ → ℝ, f(x) = 5x + 1
b) f: ℝ → ℝ, f(x) = x²
c) f: ℝ → (0, ∞), f(x) = eˣ
d) f: ℤ → ℤ, f(n) = n + 4
e) f: ℤ → ℤ, f(n) = 2n

**5.** f(x) = 2x + 1 and g(x) = x². Compute (g ∘ f)(3) and (f ∘ g)(3).

**6.** Fill in: ⌊−2.5⌋ = ____, ⌈−2.5⌉ = ____, ⌊7⌋ = ____, ⌈7.01⌉ = ____, ⌊⌈2.3⌉⌋ = ____.

**7.** What is the domain of f(x) = √(x − 2) / (x − 5)?

**8.** True or False: a function has an inverse if and only if it is a bijection.

**9.** True or False: if g ∘ f is one-to-one, then f is one-to-one.

**10.** Evaluate 5! + 0!.

**11.** g(x) = ⌊x⌋. Find g⁻¹({2}).

**12.** The range of f: ℝ → ℝ, f(x) = x² is ____ (not ℝ), so f is not ____.

---

## Part B: Written (midterm style)

**P1.** Prove f: ℝ → ℝ, f(x) = 3x + 5 is one-to-one and onto.

**P2.** Let f(x) = (x + 2)/(x − 1) with domain ℝ − {1}. Find f⁻¹ and state its domain.

**P3.** Prove f(x) = (3x + 1)/(x − 2), with domain ℝ − {2}, is one-to-one.

**P4.** Show that f: ℤ → ℤ, f(n) = n² + 1 is neither one-to-one nor onto.

**P5.** Prove: if f: A → B and g: B → C are both one-to-one, then g ∘ f is one-to-one.

---
---

## ANSWERS

### Part A

**1. Both yes.** One-to-one: 3a − 7 = 3b − 7 gives a = b. Onto: for any y, x = (y + 7)/3 gives f(x) = y.

**2. One-to-one: yes. Onto: no.** 2a = 2b gives a = b. But odd numbers are never hit (2n is always even).

**3. Neither.** f(2) = f(−2) = 4, so not one-to-one. Negative numbers (and 2, 3, ...) are never hit, so not onto.

**4. a, c, d.** (b is not one-to-one and not onto. e is one-to-one but not onto, since odd numbers are missed.)

**5.** (g ∘ f)(3) = g(f(3)) = g(7) = **49**. (f ∘ g)(3) = f(g(3)) = f(9) = **19**. Not equal, so order matters.

**6.** ⌊−2.5⌋ = **−3**, ⌈−2.5⌉ = **−2**, ⌊7⌋ = **7**, ⌈7.01⌉ = **8**, ⌊⌈2.3⌉⌋ = ⌊3⌋ = **3**.

**7.** Need x − 2 ≥ 0 and x ≠ 5, so the domain is **[2, ∞) with 5 removed**, i.e. {x ∈ ℝ | x ≥ 2, x ≠ 5}.

**8. True.**

**9. True.** If f(a1) = f(a2), then g(f(a1)) = g(f(a2)), so (g∘f)(a1) = (g∘f)(a2), which forces a1 = a2 because g∘f is one-to-one. (The reverse direction, about g, is the one that can fail.)

**10.** 5! = 120 and 0! = 1, so **121**.

**11.** ⌊x⌋ = 2 exactly when 2 ≤ x < 3, so g⁻¹({2}) = **[2, 3)**.

**12.** The range is **[0, ∞)**, so f is not **onto**.

### Part B

**P1.**
*One-to-one:* Assume f(a) = f(b). Then 3a + 5 = 3b + 5, so 3a = 3b, so a = b.
*Onto:* Let y ∈ ℝ be arbitrary. Take x = (y − 5)/3, which is a real number. Then f(x) = 3·(y−5)/3 + 5 = y.
So f is a bijection. ∎

**P2.** Set y = (x + 2)/(x − 1) and solve for x:
y(x − 1) = x + 2
yx − y = x + 2
yx − x = y + 2
x(y − 1) = y + 2
x = (y + 2)/(y − 1)

So **f⁻¹(y) = (y + 2)/(y − 1)**. y = 1 is impossible (it would need x + 2 = x − 1), so the range of f is ℝ − {1}. Therefore **f⁻¹: ℝ − {1} → ℝ − {1}**.

**P3.** Assume f(a) = f(b), with a, b ≠ 2.
(3a + 1)/(a − 2) = (3b + 1)/(b − 2)
(3a + 1)(b − 2) = (3b + 1)(a − 2)
3ab − 6a + b − 2 = 3ab − 6b + a − 2
−6a + b = −6b + a
7b = 7a, so a = b. ∎

**P4.**
*Not one-to-one:* f(1) = 2 and f(−1) = 2, but 1 ≠ −1.
*Not onto:* 0 has no preimage, because n² + 1 = 0 would need n² = −1, impossible. (Also n² + 1 ≥ 1 for every n.) ∎

**P5.** Assume (g ∘ f)(a1) = (g ∘ f)(a2). That is, g(f(a1)) = g(f(a2)). Since g is one-to-one, f(a1) = f(a2). Since f is one-to-one, a1 = a2. Hence g ∘ f is one-to-one. ∎

---

## Score yourself
If you missed one-to-one/onto questions, redo section 2 of [[Notes]] first. In the written part, the "assume f(a) = f(b), then show a = b" start is what earns the first marks every time.
