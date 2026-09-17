# Lecture 3 — Practice Questions

## Q1. Identifying classes (nouns/verbs heuristic)
The lecture posed this in class without giving an answer. Attempt it yourself: think about a software system for representing a **vehicle**. What are some possible classes, and what methods might each have? Use the nouns-are-classes, verbs-are-methods heuristic from the lecture.

## Q2. "Is-a" test
For each pair, state whether an inheritance relationship makes sense, and if so, which class should `extend` which:
a) `Car` and `Vehicle`
b) `Circle` and `Shape`
c) `Engine` and `Car`
d) `SavingsAccount` and `BankAccount`

(Hint: think about which pairs actually satisfy the "is a" phrasing, vs. pairs that are really a "has a" relationship instead — the lecture didn't cover "has a" explicitly, but it's the natural contrast to think through.)

## Q3. Trace the Employee/Manager example
Given:
```java
Employee e = new Employee(50000, "Alex Kim");
Manager m = new Manager(80000, "Jordan Lee");
m.setBonus(2000);
```
a) What does `e.getSalary()` return?
b) What does `m.getName()` return? (Note: `Manager` never defines `getName()` itself — where does it come from?)
c) Would `e.setBonus(1000);` compile? Why or why not?

## Q4. Write a new subclass
Using the `Employee` superclass from notes.md, write a `Custodian` class that extends `Employee` and adds one new field: `suppliesBudget` (a `double`), with a getter `getSuppliesBudget()` and a setter `setSuppliesBudget(double amount)`. Follow the same pattern as the `Manager` class.

## Q5. Conceptual — why one-directional?
Explain in your own words why `Employee` should never `extend Manager`, even though it would let regular employees call `setBonus()`. What would break, conceptually, about the "is-a" relationship if you did this?

## Q6. Superclass/subclass terminology check
True or false, and correct any false statements:
a) A superclass is "better" or more capable than its subclasses.
b) A subclass can override functionality it inherits from its superclass.
c) A subclass only has access to the fields/methods it defines itself — it does not automatically get its superclass's public methods.
d) `extends` is the Java keyword used to create a subclass relationship.
