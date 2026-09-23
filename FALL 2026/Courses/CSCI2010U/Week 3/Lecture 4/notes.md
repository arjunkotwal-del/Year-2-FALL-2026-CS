# Lecture 4 — Inheritance and Polymorphism

> Sourced from L04_inheritance_2.pdf (Canvas, course 202609 - Data Structures - 40241). No transcript — built from slides only.

## Outline
1. Overriding methods
2. Subclass constructors
3. Polymorphism

## 1. Overriding Methods

Recap from Lecture 3: `Manager extends Employee`, adding `setBonus()`.

**Goal**: customize `Manager`'s `getSalary()` so it includes the bonus in the returned value, instead of just the base salary inherited from `Employee`.

### Attempt 1 — reach directly into the private field (fails)
```java
@Override
public double getSalary() {
    return salary + bonus; // This should be easy...
}
```
**Error**: `The field Employee.salary is not visible`

**Why**: `salary` is `private` in `Employee`. A `private` member can only be accessed by other members *of that same class*. `Manager` is a different class from `Employee` (even though it's a subclass), so it cannot reach in and read `Employee`'s private field directly. Access has to go through the public method Employee already provides: `getSalary()`.

### Attempt 2 — call `getSalary()` directly (fails differently)
```java
@Override
public double getSalary() {
    return getSalary() + bonus; // Now it should work!
}
```
**Error**: `StackOverflowError`

**Why**: Since `Manager.getSalary()` has overridden `Employee.getSalary()`, calling `getSalary()` from inside `Manager` calls **itself**, not `Employee`'s version. This creates an infinite recursive loop, consuming stack memory until it crashes.

### Attempt 3 — use `super` (works)
```java
@Override
public double getSalary() {
    return super.getSalary() + bonus;
}
```
Output for `officeBoss` (salary 70000, bonus 500): `Salary = $70500`

### The `super` keyword
Has **two meanings** in Java:
1. Access a member of the superclass that's hidden by the subclass (e.g., call the superclass's version of an overridden method).
2. Call the superclass's constructor (see next section).

### `super` vs. `this`
- `this` **is** a reference to an object — it can be assigned to another variable where appropriate.
- `super` is **not** a reference to an object. `super.salary + bonus` (trying to directly reach a private field this way) is illegal — `super` is a special keyword that tells the compiler to invoke the superclass's version of a method, not a way to bypass access modifiers.

## 2. Subclass Constructors

Every non-static class needs a constructor to initialize its objects — subclasses are no exception. But if the superclass initializes `private` fields in its own constructor (as `Employee` does with `salary` and `name`), the subclass **cannot** initialize those fields itself (same access-modifier rule as above). This is where `super`'s second meaning comes in.

```java
public class Manager extends Employee {
    private double bonus;

    // Subclass constructor
    public Manager(double salary, String name) {
        super(salary, name);
        this.bonus = 0;
    }
    ...
}
```
- `super(salary, name);` invokes the `Employee` constructor, which initializes `salary` and `name`.
- **Important rule**: the call to `super()` must be the **first statement** in the subclass's constructor.

## Why bother with inheritance at all?
Two benefits so far:
- Reduces duplicated code.
- Provides a standard interface across the class tree (e.g., we know every class under `Animal` must have a skeleton — from Lecture 3's taxonomy example).

But there's a third, more powerful benefit: **polymorphism**.

## 3. Polymorphism

### Setup
```java
Manager officeBoss = new Manager(95000, "Bill Lumbergh");
officeBoss.setBonus(2750);

// Company employees
Employee initechWorkers[] = new Employee[3];
initechWorkers[0] = officeBoss;
initechWorkers[1] = new Employee(20745, "Peter Gibbons");
initechWorkers[2] = new Employee(25000, "Mario Savio");

// Print salaries
for (Employee e : initechWorkers)
    System.out.println(e.getName() + ":\t$" + e.getSalary());
```
Output:
```
Bill Lumbergh: $97750.0
Peter Gibbons: $20745.0
Mario Savio:   $25000.0
```

### Two interesting things happened
1. **We mixed Managers and Employees in one `Employee[]` array.** This works because "a manager *is an* employee" — the subclass can be stored wherever the superclass type is expected.
2. **Calling `e.getSalary()` in the loop correctly used `Manager.getSalary()` for `officeBoss`** (giving $97750 = 95000 + 2750 bonus), even though the loop variable `e` is declared as type `Employee`. This is the interesting part explained below.

### Theory of polymorphism — object creation, step by step
Object declaration/assignment has **three distinct parts**:
```
Manager officeBoss = new Manager(0, "");
       ①              ③   ②
```
1. **Declare a reference variable** — tells the JVM to allocate space for a reference. A reference variable is **not** an object itself — it holds the information needed to *find* an object in memory (think of it like a signpost: "you can find your manager at address XYZ"). Once declared, a reference variable's **type can never change**.
2. **Create an object** — tells the JVM to allocate memory for the actual object, on the **heap**. The heap allows dynamic allocation/deallocation; all Java objects live there, and unused objects are automatically garbage collected.
3. **Link the reference to the object** — assigns the new object's memory address to the reference variable. Now the "signpost" points to where the real object lives.

Normally, the reference type and object type match (e.g., `Manager officeBoss = new Manager(...)` — both sides are `Manager`).

### The polymorphism trick — reference type ≠ object type
```java
Employee workerBee = new Manager(99000, "Bill Lumbergh");
```
Here the **reference type** (`Employee`) and the **object type** (`Manager`) are **different**. This is legal specifically because the reference type is a **superclass** of the object's actual type.

### Applying the "is a" test to code
Assignment statements in Java are evaluated **right to left**. Apply the "is a" test the same way — right to left:
- `Employee officeBoss = new Manager(...);` → read as "Employee is a Manager"? No — read right-to-left as "**Manager is-a Employee**" → ✅ valid (Manager → Employee, subclass into superclass reference).
- `Manager officeBoss = new Employee(...);` → "**Employee is-a Manager**" → ❌ invalid — an Employee is not necessarily a Manager, so this won't compile.

**Rule**: when you declare a superclass reference variable, any subclass of that supertype can be substituted where the supertype is expected — but not the reverse.

### Polymorphism in method arguments/return types
```java
public class Company {
    public void hireEmployee(Employee e) {
        System.out.println("You're hired for $" + e.getSalary());
    }
}
...
Employee workerBee = new Employee(20000, "Peter");
Manager officeBoss = new Manager(50000, "Bill Lumbergh");
Company initech = new Company();
initech.hireEmployee(workerBee); // works — Employee is-a Employee
initech.hireEmployee(officeBoss); // works — Manager is-a Employee
```
A method parameter typed as the superclass (`Employee`) will accept **any subclass instance** (`Manager`, `Salesperson`, `Custodian`, etc.) — this is what makes polymorphism practical: you can write one method that works across an entire family of related classes.

### Dynamic method dispatch (name-drop only, not covered in depth)
The remaining open question — *how* does Java know to call `Manager.getSalary()` specifically, even though the loop variable/array is typed as `Employee`? The answer is called **dynamic method dispatch**, a key mechanism underlying polymorphism. **Explicitly stated: this course (CSCI2010U) will not cover DMD in depth** — just know that it's the name of the mechanism responsible for this behaviour.
