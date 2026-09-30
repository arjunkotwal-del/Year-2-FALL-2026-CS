---
tags: [review, notes]
week: 3
dates: Sept 21–25, 2026
lectures: "Lecture 5 (Sept 24, §1.6/2.1/2.2) — confirmed from live transcript; Lecture 6 (Sept 25, §2.3) — pending"
source: "Lecture 5: [[Transcript - Lecture 5]] (live class, Sept 24)."
---

# 📅 Week 3 — Binomial Distribution & Calculator-Based Statistics

← [[STAT2010U - Statistics and Probability]] | 🎙️ [[Transcript - Lecture 5]]

> [!tip] The 3-sentence version
> The **binomial distribution** is your third named distribution — the tricky part is *recognizing* it (fixed trials + independence + constant success probability), since the question never announces it like normal/exponential do. The rest of the lecture is pure **calculator + formula mechanics**: mean/median/variance, done three different ways depending on whether you have raw data, a discrete distribution, or a continuous distribution. Notation is everything here — x̄/s/s² (sample) vs μ/σ/σ² (distribution) — mixing them up on the test costs marks even if your math is right.

---

## 🎲 The Binomial Distribution

### Recognizing it — the 3-part checklist
| Check | Meaning |
|---|---|
| **Fixed n** | a set number of trials |
| **Independence** | one trial doesn't affect the next (often *implied*, not stated) |
| **Constant π** | fixed probability of "success" (just a label — not necessarily good) |

> [!warning] The hard part isn't the math
> Normal and exponential questions **tell you** what distribution they are. Binomial never does — you have to reason it out from the setup every time.

### The formula (on your formula sheet — don't memorize, know how to apply)
**P(x) = (n choose x) · π^x · (1−π)^(n−x)**, x = 0,1,...,n

- "n choose x" = combinations, calculator button **nCr** (not nPr — permutations aren't used this course)
- Two parameters: **n** and **π**

> [!danger] Discrete rules apply — inclusive/exclusive matters
> Same as any mass function: P(x≥k) ≠ P(x>k). Always read the wording carefully.

> [!example] Worked — germination
> n=5, π=0.4. P(X=3) = (5 choose 3)(0.4)³(0.6)² ≈ **0.230**
> P(X≤2) = P(0)+P(1)+P(2) ≈ **0.683**
> P(2≤X≤4) inclusive = P(2)+P(3)+P(4) ≈ **0.653**; P(2<X<4) exclusive = just P(3) ≈ **0.230**

### The binomial table — shortcut, with limits
- Only valid for **n = 5, 10, 15, 20, 25** AND specific listed π values — otherwise calculate by hand (no interpolating)
- Gives **individual** probabilities, not cumulative — you still sum entries yourself for a range
- **Complement trick**: P(X≥1) = 1 − P(X=0) — saves adding up many terms when n is large

> [!warning] Success vs. failure — read carefully
> If a question gives you the probability of the outcome you *don't* care about (e.g. "probability of losing = 0.89" but you want P(win)), your π is the **complement**: π = 1 − 0.89 = 0.11. Misreading this flips your entire answer.

---

## 🧮 Mean, Median, Variance — Three Contexts, Three Formula Sets

### Notation (memorize this table — it's an easy way to lose marks)

| | Sample (raw data) | Discrete distribution | Continuous distribution |
|---|---|---|---|
| Mean | **x̄** | **μ** | **μ** |
| Median | **x̃** | — | 50th percentile |
| Variance | **s²** | **σ²** | **σ²** |
| Std. deviation | **s** | **σ** | **σ** |

### Mean

| Context | Formula | Method |
|---|---|---|
| Raw data | x̄ = Σx/n | **calculator**, univariate mode |
| Discrete | μ = Σ[x·P(x)] | by hand, sum |
| Continuous | μ = ∫x·f(x)dx | by hand, integrate |
| Binomial (shortcut) | μ = n·π | plug in, no derivation needed |

> [!example] Worked — continuous mean (the one flagged as new/high-yield)
> f(x)=1/2 on [0,2] → μ = ∫₀² x(1/2)dx = **1** (sanity check: falls inside [0,2] ✅)

### Median

| Context | Method |
|---|---|
| Raw data | **By hand only — never calculator** (unreliable across brands). Order data. n odd → position (n+1)/2. n even → average positions n/2 and (n/2)+1 |
| Continuous | Solve ∫(lower bound to m) f(x)dx = 0.5 for m (same method from Week 1/2) |

> [!example] Worked — odd n
> Ordered data 2,12,16,18,22 (n=5) → position (5+1)/2=3 → median = **16**

> [!example] Worked — even n
> n=8, positions 4 & 5 are 19 and 26 → median = (19+26)/2 = **22.5**

### Variance & Standard Deviation

| Context | Formula | Method |
|---|---|---|
| Raw data | s² = Σ(x−x̄)²/(n−1) | **calculator** (get s, square for s²) |
| Discrete | σ² = Σ[(x−μ)²·P(x)] | by hand, sum |
| Continuous | σ² = ∫(x−μ)²·f(x)dx | by hand, integrate — expand (x−μ)² first |
| Binomial (shortcut) | σ² = n·π·(1−π) | plug in, no derivation needed |

> [!tip] Calculator is mandatory here
> Variance by hand for raw data is painful even with 5 points. **Learn your specific calculator's stat mode before test day** — enter data, find the `s` or `Sₓ` button. If it only gives standard deviation, square it yourself for variance.

> [!danger] Show your work
> Even if your calculator can integrate, you must show full integration steps for any non-MC question — "calculator said so" isn't accepted work. (Term tests have zero multiple choice, so this always applies here.)

---

## 🎯 Why this matters
- Term Test 1 covers **Lectures 1–6** — this lecture's binomial + calculator content is directly one of the 4 confirmed question types (distributions question, plus the raw-data mean/SD question).
- **Correction from earlier notes**: "therefore" statements are only required when the question explicitly asks for one — not every single answer. Don't waste test time on unrequested ones.

## ✅ Status
- [x] Lecture 5 confirmed from live transcript — see [[Transcript - Lecture 5]]
- [ ] Get Lecture 6 (Sept 25, §2.3) content — likely median/quartiles for raw data, per the professor's own preview
- [ ] **Learn your actual calculator's univariate stat mode now** — practice entering data and pulling mean/SD before test day
- [ ] Memorize the notation table (x̄/s/s² vs μ/σ/σ²) — cheap marks, easy to lose
- [ ] Drill binomial "which value is success" trap (lottery win/lose example)
