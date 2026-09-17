---
tags: [practice, week2, lecture2, predicate-logic, quantifiers]
---

# Lecture 3 — Practice Questions

← [[Notes]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Source — confirmed from Canvas
> Official honour homework, pulled directly from [[../../files/MATH2080_Lecture3_Sections_1p4_1p5_PredLogic_and_NestedQuants.pdf]]: §1.4 #7, 9, 11, 15, 53 and §1.5 #1, 9, 11, 27, 31 (8th ed). Due before next week's tutorials.

---

## Section 1.4 — Predicates and Quantifiers

### Q7 — Translate predicate statements into English
Translate these statements into English, where $C(x)$ is "x is a comedian" and $F(x)$ is "x is funny," and the domain consists of all people.
a) $\forall x(C(x) \rightarrow F(x))$
b) $\forall x(C(x) \wedge F(x))$
c) $\exists x(C(x) \rightarrow F(x))$
d) $\exists x(C(x) \wedge F(x))$

### Q9 — English → predicate logic
Let $P(x)$ be "x can speak Russian" and $Q(x)$ be "x knows the computer language C++." Express each in terms of $P(x)$, $Q(x)$, quantifiers, and logical connectives. Domain = all students at your school.
a) There is a student at your school who can speak Russian and who knows C++.
b) There is a student at your school who can speak Russian but who doesn't know C++.
c) Every student at your school either can speak Russian or knows C++.
d) No student at your school can speak Russian or knows C++.

### Q11 — Evaluate truth values
Let $P(x)$ be "$x = x^2$." If the domain consists of the integers, what are these truth values?
a) $P(0)$  b) $P(1)$  c) $P(2)$  d) $P(-1)$  e) $\exists x\,P(x)$  f) $\forall x\,P(x)$

### Q15 — Determine truth value (domain = all integers)
a) $\forall n(n^2 \geq 0)$
b) $\exists n(n^2 = 2)$
c) $\forall n(n^2 \geq n)$
d) $\exists n(n^2 < 0)$

### Q53 — Show NOT equivalent
Show that $\exists x P(x) \wedge \exists x Q(x)$ and $\exists x(P(x) \wedge Q(x))$ are **not** logically equivalent. (Find specific P, Q, and a domain where one is true and the other false.)

---

## Section 1.5 — Nested Quantifiers

### Q1 — Translate into English
Translate these statements into English, where the domain for each variable consists of all real numbers.
a) $\forall x\,\exists y(x<y)$
b) $\forall x\forall y\big(((x\geq 0)\wedge(y\geq 0)) \rightarrow (xy\geq 0)\big)$
c) $\forall x\forall y\,\exists z(xy=z)$

### Q9 — English → nested quantifiers
Let $L(x,y)$ be "x loves y," domain for both x and y = all people in the world. Express each:
a) Everybody loves Jerry.
b) Everybody loves somebody.
c) There is somebody whom everybody loves.
d) Nobody loves everybody.
e) There is somebody whom Lydia does not love.
f) There is somebody whom no one loves.
g) There is exactly one person whom everybody loves.
h) There are exactly two people whom Lynn loves.
i) Everyone loves himself or herself.
j) There is someone who loves no one besides himself or herself.

### Q11 — English → nested quantifiers
Let $S(x)$ be "x is a student," $F(x)$ be "x is a faculty member," and $A(x,y)$ be "x has asked y a question," domain = all people associated with your school. Express each:
a) Lois has asked Professor Michaels a question.
b) Every student has asked Professor Gross a question.
c) Every faculty member has either asked Professor Miller a question or been asked a question by Professor Miller.
d) Some student has not asked any faculty member a question.
e) There is a faculty member who has never been asked a question by a student.
f) Some student has asked every faculty member a question.
g) There is a faculty member who has asked every other faculty member a question.
h) Some student has never been asked a question by a faculty member.

### Q27 — Determine truth value (domain = all integers)
a) $\forall n\,\exists m(n^2<m)$
b) $\exists n\,\forall m(n<m^2)$
c) $\forall n\,\exists m(n+m=0)$
d) $\exists n\,\forall m(nm=m)$
e) $\exists n\,\exists m(n^2+m^2=5)$
f) $\exists n\,\exists m(n^2+m^2=6)$
g) $\exists m\,\exists n(n^2+m=4 \wedge n-m=2)$
h) $\exists n\,\exists m(n+m=4 \wedge n-m=2)$
i) $\forall n\,\forall m\,\exists p(p=(m+n)/2)$

### Q31 — Push negation inward (no negation before a quantifier)
Express the negation of each so that all negation symbols immediately precede predicates:
a) $\forall x\,\exists y\,\forall z\,T(x,y,z)$
b) $\forall x\,\exists y\,P(x,y) \vee \forall x\,\exists y\,Q(x,y)$
c) $\forall x\,\exists y\big(P(x,y) \wedge \exists z\,R(x,y,z)\big)$
d) $\forall x\,\exists y\big(P(x,y) \rightarrow Q(x,y)\big)$

---

## Extra from tutoring session
Try translating this one cold (not from the textbook — good synthesis practice):
"There is a student in this class who has taken every course that some other student in this class has also taken."

---

## Answers

> [!warning] Attempt first
> Don't read these until you've written your own answer.

### Section 1.4

**Q7** — translate to English (domain = all people)
a) Every comedian is funny.
b) Everyone is a comedian and is funny (i.e., every person is a funny comedian).
c) There is someone who, if they're a comedian, is funny — trivially true as long as at least one non-comedian exists (vacuously satisfies the conditional). In practice: "There's someone who isn't a comedian, or who is a funny comedian."
d) There is a comedian who is funny (some comedian is funny).

**Q9**
a) $\exists x(P(x)\wedge Q(x))$
b) $\exists x(P(x)\wedge\neg Q(x))$
c) $\forall x(P(x)\vee Q(x))$
d) $\forall x(\neg P(x)\wedge\neg Q(x))$ — equivalently $\neg\exists x(P(x)\vee Q(x))$

**Q11** — P(x): "x = x²", domain = integers
a) $P(0)$: $0=0^2=0$ → **True**
b) $P(1)$: $1=1^2=1$ → **True**
c) $P(2)$: $2=4$? → **False**
d) $P(-1)$: $-1=1$? → **False**
e) $\exists x\,P(x)$ → **True** (x=0 or x=1 work)
f) $\forall x\,P(x)$ → **False** (x=2 is a counterexample)

**Q15** — domain = all integers
a) $\forall n(n^2\geq 0)$ → **True** (squares are always non-negative)
b) $\exists n(n^2=2)$ → **False** (no integer squares to 2)
c) $\forall n(n^2\geq n)$ → **True** ($n^2-n=n(n-1)$ is a product of consecutive integers, always ≥ 0)
d) $\exists n(n^2<0)$ → **False** (squares are never negative)

**Q53** — show not equivalent
Counterexample: domain = integers, $P(x)$: "x is even", $Q(x)$: "x is odd."
$\exists xP(x)\wedge\exists xQ(x)$ is **True** (2 is even, 3 is odd — each existential is separately satisfiable).
$\exists x(P(x)\wedge Q(x))$ is **False** (no single integer is both even and odd).
Different truth values → not equivalent. This is the "same x vs. possibly different x" trap from the Notes.

### Section 1.5

**Q1** — translate to English (domain = reals)
a) Every real number has a (strictly) larger real number.
b) The product of two non-negative real numbers is non-negative.
c) The product of any two real numbers is itself a real number.

**Q9** — L(x,y): "x loves y", domain = all people
a) $\forall x\,L(x,\text{Jerry})$
b) $\forall x\,\exists y\,L(x,y)$
c) $\exists y\,\forall x\,L(x,y)$
d) $\neg\exists x\,\forall y\,L(x,y)$ — equivalently $\forall x\,\exists y\,\neg L(x,y)$
e) $\exists x\,\neg L(\text{Lydia},x)$
f) $\exists y\,\forall x\,\neg L(x,y)$
g) $\exists y\big(\forall x\,L(x,y) \wedge \forall z(\forall x\,L(x,z)\to z=y)\big)$ — there's a y everyone loves, and any z that everyone loves must be that same y
h) $\exists x\exists y\big(x\neq y \wedge L(\text{Lynn},x)\wedge L(\text{Lynn},y) \wedge \forall z(L(\text{Lynn},z)\to(z=x\vee z=y))\big)$
i) $\forall x\,L(x,x)$
j) $\exists x\,\forall y(y\neq x \to \neg L(x,y))$

**Q11** — S(x) student, F(x) faculty, A(x,y) "x asked y a question"
a) $A(\text{Lois}, \text{ProfMichaels})$
b) $\forall x(S(x)\to A(x,\text{ProfGross}))$
c) $\forall x\big(F(x)\to(A(x,\text{ProfMiller})\vee A(\text{ProfMiller},x))\big)$
d) $\exists x\big(S(x)\wedge\forall y(F(y)\to\neg A(x,y))\big)$
e) $\exists x\big(F(x)\wedge\forall y(S(y)\to\neg A(y,x))\big)$
f) $\exists x\big(S(x)\wedge\forall y(F(y)\to A(x,y))\big)$
g) $\exists x\big(F(x)\wedge\forall y((F(y)\wedge y\neq x)\to A(x,y))\big)$
h) $\exists x\big(S(x)\wedge\forall y(F(y)\to\neg A(y,x))\big)$

**Q27** — domain = all integers
a) $\forall n\exists m(n^2<m)$ → **True** ($m=n^2+1$ always works)
b) $\exists n\forall m(n<m^2)$ → **True** (pick n=-1; since $m^2\geq 0 > -1$ always, it works for every m)
c) $\forall n\exists m(n+m=0)$ → **True** ($m=-n$)
d) $\exists n\forall m(nm=m)$ → **True** (n=1 works: $1\cdot m=m$ for all m)
e) $\exists n\exists m(n^2+m^2=5)$ → **True** (n=1, m=2: $1+4=5$)
f) $\exists n\exists m(n^2+m^2=6)$ → **False** (no two perfect squares sum to 6: 0,1,4,9,... — no pair works)
g) $\exists m\exists n(n^2+m=4\wedge n-m=2)$ → **True** (n=2, m=0: $4+0=4$ ✓, $2-0=2$ ✓)
h) $\exists n\exists m(n+m=4\wedge n-m=2)$ → **True** (n=3, m=1)
i) $\forall n\forall m\exists p(p=(m+n)/2)$ → **False** (e.g. n=0, m=1 gives p=0.5, not an integer, and p's domain is also integers)

**Q31** — push negation inward
a) $\forall x\exists y\forall zT(x,y,z) \;\rightsquigarrow\; \exists x\forall y\exists z\,\neg T(x,y,z)$
b) $\forall x\exists yP(x,y)\vee\forall x\exists yQ(x,y) \;\rightsquigarrow\; \big(\exists x\forall y\,\neg P(x,y)\big)\wedge\big(\exists x\forall y\,\neg Q(x,y)\big)$
c) $\forall x\exists y(P(x,y)\wedge\exists zR(x,y,z)) \;\rightsquigarrow\; \exists x\forall y\big(\neg P(x,y)\vee\forall z\,\neg R(x,y,z)\big)$
d) $\forall x\exists y(P(x,y)\to Q(x,y)) \;\rightsquigarrow\; \exists x\forall y\big(P(x,y)\wedge\neg Q(x,y)\big)$ (using $\neg(p\to q)\equiv p\wedge\neg q$ at the last step)

### Extra — tutoring session translation
Let $S(x)$: "x is a student in this class," $T(x,c)$: "x has taken course c." One reasonable translation:
$$\exists x\Big(S(x) \wedge \forall y\forall c\big((S(y)\wedge y\neq x \wedge T(y,c)) \to T(x,c)\big)\Big)$$
(There's a student x such that for every other student y and every course c, if y took c, then x also took c.)
