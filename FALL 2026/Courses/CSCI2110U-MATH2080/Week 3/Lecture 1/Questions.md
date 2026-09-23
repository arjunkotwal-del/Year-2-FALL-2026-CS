---
tags: [practice, week3, lecture1, rules-of-inference]
---

# Lecture 4 — Practice Questions

← [[Notes]] | ← [[../../CSCI2110U-MATH2080 - Discrete Math]]

> [!info] Source — confirmed from Canvas
> Official honour homework, pulled directly from [[../../files/MATH2080_Lecture4_Sections_1p6_RulesOfInference.pdf]]: §1.6 #1, 3, 9, 19, 23, 29, 35 (same numbers in both 7th and 8th editions). Due before next week's tutorials.

---

### Q1 — Find the argument form and check validity
"If Socrates is human, then Socrates is mortal. Socrates is human. ∴ Socrates is mortal." Find the argument form and determine whether it's valid.

### Q3 — Name the rule used
What rule of inference is used in each of these arguments?
a) Alice is a mathematics major. Therefore, Alice is either a mathematics major or a computer science major.
b) Jerry is a mathematics major and a computer science major. Therefore, Jerry is a mathematics major.
c) If it is rainy, then the pool will be closed. It is rainy. Therefore, the pool is closed.
d) If it snows today, the university will close. The university is not closed today. Therefore, it did not snow today.
e) If I go swimming, then I will stay in the sun too long. If I stay in the sun too long, then I will sunburn. Therefore, if I go swimming, then I will sunburn.

### Q9 — Draw the conclusion (multi-step arguments)
For each of these collections of premises, what relevant conclusion(s) can be drawn? Explain the rules of inference used.
a) "If I take the day off, it either rains or snows." "I took Tuesday off or I took Thursday off." "It was sunny on Tuesday." "It did not snow on Thursday."
b) "If I eat spicy foods, then I have strange dreams." "I have strange dreams if there is thunder while I sleep." "I did not have strange dreams."
c) "I am either clever or lucky." "I am not lucky." "If I am lucky, then I will win the lottery."
d) "Every computer science major has a personal computer." "Ralph does not have a personal computer." "Ann has a personal computer."

### Q19 — Determine validity, spot the error if invalid
Determine whether each of these arguments is valid. If an argument is correct, what rule of inference is used? If not, what logical error occurs?
a) If n is a real number such that n > 1, then n² > 1. Suppose n² > 1. Then n > 1.
b) If n is a real number with n > 3, then n² > 9. Suppose n² ≤ 9. Then n ≤ 3.
c) If n is a real number with n > 2, then n² > 4. Suppose n ≤ 2. Then n² ≤ 4.

### Q23 — Identify the error(s)
Identify the error or errors in this argument that supposedly shows that if ∃xP(x)∧∃xQ(x) is true, then ∃x(P(x)∧Q(x)) is true:
1. ∃xP(x) ∧ ∃xQ(x) — Premise
2. ∃xP(x) — Simplification from (1)
3. P(c) — Existential instantiation from (2)
4. ∃xQ(x) — Simplification from (1)
5. Q(c) — Existential instantiation from (4)
6. P(c) ∧ Q(c) — Conjunction from (3) and (5)
7. ∃x(P(x) ∧ Q(x)) — Existential generalization

### Q29 — Prove validity via rules of inference
Use rules of inference to show that if ∀x(P(x)∨Q(x)) and ∀x((¬P(x)∧Q(x))→R(x)) are true, then ∀x(¬R(x)→P(x)) is also true, where the domains of all quantifiers are the same.

### Q35 — The Superman argument
Determine whether this argument, taken from Kalish and Montague, is valid:
"If Superman were able and willing to prevent evil, he would do so. If Superman were unable to prevent evil, he would be impotent; if he were unwilling to prevent evil, he would be malevolent. Superman does not prevent evil. If Superman exists, he is neither impotent nor malevolent. Therefore, Superman does not exist."

---

## Extra practice (not from lecture, from tutoring session)
Write out, step by step with reasons, a proof that the following premises imply the conclusion "It rained on Thursday":
"If I take the day off, it either rains or snows." "I took Tuesday off, or I took Thursday off." "It was sunny on Tuesday." "It did not snow on Thursday."
(This is Q9a above — try it fully worked out before checking [[Notes]] section 3.)
