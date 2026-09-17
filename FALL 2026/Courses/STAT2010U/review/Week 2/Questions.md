---
tags: [review, questions]
week: 2
source: Canvas — Suggested Qs for Week 2, Devore-Farnum-Doi Sec 1.3 & 1.4 (solutions in ../../files/hw_week2_solutions.pdf; textbook problem text not posted separately, only solutions)
---

# Week 2 — Questions to Review

## Assigned (Sec 1.3): 19, 21, 23, 25, 27
Continuous density function problems:
- **#19**: uniform density on [4,6] — proportions, median, finding a percentile (x₀) by solving an area equation
- **#21**: triangular density on [0,10] — find height from total-area-1 constraint, compute proportions on each side, symmetric-triangle shortcut for percentiles
- **#23**: exponential density, λ = .00004 — proportions via the **P(x>c) = e^(−λc)** shortcut, finding best/worst 1% cutoffs by inverting that formula with natural logs
- **#25**: density with an unknown constant c multiplying a quadratic — solve ∫f(x)dx=1 for c, then use symmetry to shortcut a 50% proportion question
- **#27**: discrete-looking proportion table (not continuous) — straightforward sums/complements of given proportions

## Assigned (Sec 1.4): 31, 33, 35, 37, 39, 41
Standard & nonstandard normal:
- **#31**: pure z-table lookups — P(z≤a), P(z>a), P(a≤z≤b), symmetric two-tail probabilities, and reading 0.0000 for extreme z (±4+)
- **#33**: reverse lookups — given a proportion, find z* using **linear interpolation** between table rows
- **#35, #37, #39**: nonstandard normal — standardize with z=(x−μ)/σ first, then look up. #39 also does a reverse lookup (given top 5%, find the raw x* value)
- **#41**: **continuity correction** — discrete x approximated by a normal curve, using x±0.5 boundaries before standardizing

## Self-audit prompts
- In #23, where does the shortcut P(x>c) = e^(−λc) actually come from? Try deriving it yourself by integrating λe^(−λx) from c to ∞ — don't just accept the formula.
- In #33/#39, why do you convert "top 15%" into a **left-tail** probability (0.85) before using Table I? What would go wrong if you looked up 0.15 directly?
- In #41, why use 19.5/40.5 instead of 20/40? What's actually being approximated here (a discrete distribution's step function by a smooth normal curve) — draw it out.
- Can you tell, from the density function's formula alone (before any calculation), whether a distribution is symmetric? What did #25 and #21 have in common that let you skip half the work?

## Things I got wrong / unsure about
-
