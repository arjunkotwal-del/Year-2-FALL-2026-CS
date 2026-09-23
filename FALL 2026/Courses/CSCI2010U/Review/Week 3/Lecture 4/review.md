# Review — Week 3, Lecture 4

## What to review
- [ ] **The three override attempts** — reproduce from memory why direct field access fails, why calling `getSalary()` recursively fails, and why `super.getSalary()` works. This sequence is a common exam-trace question.
- [ ] **`super` vs `this`** — explain clearly that `super` is not an object reference, unlike `this`. Know why `super.salary` is illegal syntax.
- [ ] **Subclass constructor rule**: `super(...)` must be the first statement. Explain why (superclass private fields can't be touched directly by the subclass).
- [ ] **The three-step object creation model**: declare reference → create object (heap) → link reference to object. Be able to draw the "signpost" diagram from memory.
- [ ] **The "is a" test applied right-to-left to code** — practice Q5 in questions.md until it's automatic: `Employee e = new Manager(...)` compiles, `Manager m = new Employee(...)` does not.
- [ ] **Polymorphism with arrays and method parameters** — trace Q4, and write your own version of the `Company.hireEmployee(Employee e)` pattern (Q6).
- [ ] Know that **dynamic method dispatch** is the name of the mechanism behind polymorphic method calls, but that CSCI2010U explicitly does not cover it in depth — don't over-invest time deriving it, just recognize the term.

## Status
Not yet reviewed.
