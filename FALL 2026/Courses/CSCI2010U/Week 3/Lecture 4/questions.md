# Lecture 4 — Practice Questions

## Q1. Why does each override attempt fail/succeed?
For each version of `Manager.getSalary()` below, state whether it compiles/runs successfully, and if not, explain exactly why (in terms of access modifiers or recursion):
```java
// Version A
return salary + bonus;

// Version B
return getSalary() + bonus;

// Version C
return super.getSalary() + bonus;
```

## Q2. `super` vs `this`
Explain the difference between `super` and `this` in your own words. Is `super` a reference to an object? Why is `return super.salary + bonus;` illegal even though `return super.getSalary() + bonus;` works?

## Q3. Subclass constructor rule
What specific rule governs where `super(...)` must appear in a subclass constructor? What happens (conceptually) if a superclass initializes private fields in its constructor, and the subclass constructor doesn't call `super(...)` at all?

## Q4. Trace the polymorphism example
Given:
```java
Employee a = new Employee(30000, "Alex");
Manager b = new Manager(60000, "Bo");
b.setBonus(1000);
Employee[] team = new Employee[2];
team[0] = a;
team[1] = b;
for (Employee e : team)
    System.out.println(e.getName() + ": " + e.getSalary());
```
a) What gets printed for each line?
b) Is `team[1] = b;` legal? Justify using the "is a" test, read right to left.
c) Would `Manager[] team2 = new Employee[2];` compile? Why or why not?

## Q5. Apply the "is a" test
For each assignment, state whether it compiles, using the right-to-left "is a" reading:
```java
a) Employee e1 = new Manager(1, "X");
b) Manager m1 = new Employee(1, "X");
c) Employee e2 = new Employee(1, "X");
d) Manager m2 = new Manager(1, "X");
```

## Q6. Write a polymorphic method
Using the `Company` class pattern from notes.md, write a method `announceRaise(Employee e, double amount)` that prints `"<name> got a raise to $<newSalary>"` — where `newSalary` is computed by calling `e.getSalary() + amount` (don't worry about actually updating the object's state, just print the calculated value). Then show that this method works correctly when called with both an `Employee` and a `Manager` argument.

## Q7. Conceptual — the three steps of object creation
Explain, in your own words, what each of the three parts of `Manager officeBoss = new Manager(0, "");` actually does:
1. `Manager officeBoss`
2. `new Manager(0, "")`
3. `=`

Why is a reference variable described as a "signpost" rather than the object itself?
