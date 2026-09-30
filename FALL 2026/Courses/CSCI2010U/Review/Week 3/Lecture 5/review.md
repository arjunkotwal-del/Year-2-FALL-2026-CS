# Review — Week 3, Lecture 5

## What to review
- [ ] **Access modifier truth table** — memorize cold, especially the `protected` vs. no-modifier distinction for "different package, subclass" (Yes vs. No — the one row they differ on).
- [ ] **Abstract class rules** — can't instantiate, can mix concrete/abstract methods, constructors can't be abstract, subclasses must implement all abstract methods or be abstract themselves. Practice Q2 (true/false) in questions.md.
- [ ] **Person/Employee/Intern hierarchy** — reproduce the abstract `Person` class and both subclasses from memory, including why `super(name)` still works even though `Person` is abstract.
- [ ] **The diamond problem** — explain both problems (field ambiguity, method ambiguity) using the Mouse example, and why Java's single-inheritance restriction avoids them entirely.
- [ ] **Interfaces as "roles"** — understand why a class implementing multiple interfaces (unlike extending multiple classes) doesn't create the diamond problem: all interface methods are abstract, so there's no inherited implementation to conflict over.
- [ ] **`Comparable<T>` and `compareTo`** — know the return-value convention (negative/zero/positive) and that a class must both declare `implements` and provide a concrete `compareTo` body.
- [ ] **Write your own interface implementation** — complete Q3 and Q6 (Shape hierarchy + Comparable) without copying the Employee example directly.
- [ ] Generics were introduced only briefly (`Comparable<Employee>`, `ArrayList<String>`) — full coverage is Lecture 13, so don't over-invest time here yet, just recognize the `<>` syntax purpose.
- [ ] **New from transcript**: abstract classes CAN have static methods — explain why this doesn't contradict "can't be instantiated" (static methods belong to the class, not an instance).
- [ ] **New from transcript**: know that `Arrays.sort()`'s output order comes strictly from `compareTo()`, not insertion order — this was directly demonstrated live as a common point of confusion.
- [ ] **New from transcript**: abstract classes only pay off with multiple sibling subclasses sharing structure — a single-branch hierarchy gains nothing from making the superclass abstract.

## Status
Notes updated from live transcript (2026-09-24). Practice questions still open.
