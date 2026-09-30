# Lecture 5 — Packages, Abstract Classes, and Interfaces

> Sourced from L05_interfaces.pdf slides + live lecture transcript (course 202609 - Data Structures - 40241). See [transcript.md](transcript.md) for the full raw walkthrough.

## Course context (from live lecture)
- **This is the end of the inheritance unit.** Next class (Monday) the course shifts entirely into data structures and algorithms proper — abstract classes and interfaces will be used constantly as building blocks going forward.
- Practical modifier guidance: **`public`/`private` are the two you'll actually use throughout this course.** No modifier (default) is explicitly discouraged — "just not good behaviour," always specify one. `protected` won't come up much here since the course isn't building multi-package software systems — it matters more in real software engineering.
- Instructor's honest note: it's completely normal for abstract classes to click while interfaces still feel "squishy" right after this lecture — the concept solidifies with repeated exposure, and you'll see interfaces constantly from here on (classes extending one abstract class while implementing several interfaces at once).

## Outline
1. Packages and visibility
2. Abstract classes
3. Interfaces

## 1. Packages and Visibility

### Why this layered system exists
Java has mechanisms at many levels to keep programs organized and data safe from accidental access:
| Level | Scope | Purpose |
|---|---|---|
| **Packages** | Large programs/teams | Group related classes together |
| **Classes / visibility** | — | Set visibility of data fields. Abstraction, encapsulation, information hiding |
| **Methods / scope** | Small programs/individuals | Organize processing; variables only exist within a method |
| **Blocks `{}` / scope** | — | Organize processing; local variables scoped within blocks inside methods |

### Packages
A **package** is a related group of classes. Every class belongs to a package — even classes you write without specifying one go into the **default package**. Named packages: `java.lang`, `javax.swing`, etc.

**What packages give you**:
- Guarantees uniqueness of class names — two classes with the same name can coexist if they're in different packages.
- Nested/hierarchical, just like folders on your hard drive.
- Stronger encapsulation — you can expose class members only to other members of the same package.

**Standard library packages**:
| Package | Contains |
|---|---|
| `java.lang` | Core classes: `System`, `Math`, `String` — **automatically imported** everywhere |
| `java.io` | Data input/output |
| `java.util` | General utility classes: `Arrays`, `Random` |
| `java.net` | Networking/internet programming |
| `javax.crypto` | Encrypting/decrypting data |

### Defining a package
```java
package myfirstpkg;
```
Must be the **first statement** in the Java file. Java maps packages to filesystem directories — all `.class` files belonging to `myfirstpkg` must physically live in a directory called `myfirstpkg`. A package can span many classes/files, all sharing the same `package` statement.

```java
package myfirstpkg;

public class TestPkg {
    public static void main(String[] args) {
        System.out.println("** Testing package creation **");
    }
}
```

**Compiling packaged code (from lecture demo)**: `javac -d bin ...` compiles source files into a `bin` folder while **preserving the package hierarchy** as nested directories — e.g., compiling `lecture05/iface/*.java` produces matching `.class` files under `bin/lecture05/iface/`. Once code belongs to a named package, you must reference it by its full path (e.g., `lecture05.iface.Main`) both to compile and to run — this is why packaged code needs longer compile/run commands than a bare default-package class.

**Library analogy**: a Java "library"/API (like the standard library) is made of one or more packages — like a real library organizing books into sections (adult, junior fiction, etc.), and within each section, individual books.

### Visibility — the four access modifier categories
Packages and classes are both encapsulation mechanisms — packages are containers for classes, classes are containers for code/data. `public`/`private` are sufficient for controlling access *within* a class, but packages need finer-grained control across four scenarios:
- Subclasses in the same package
- Non-subclasses in the same package
- Subclasses in a different package
- Classes that are neither subclasses nor in the same package

### The access modifier truth table
| Member access | `public` | `protected` | *(no modifier)* | `private` |
|---|---|---|---|---|
| Same class | Yes | Yes | Yes | Yes |
| Same package, subclass | Yes | Yes | Yes | No |
| Same package, non-subclass | Yes | Yes | Yes | No |
| Different package, subclass | Yes | Yes | **No** | No |
| Different package, non-subclass | Yes | **No** | No | No |

**Summary of each modifier**:
- **`public`** — accessible by different classes and different packages.
- **`private`** — cannot be accessed outside of the class.
- **`protected`** — accessible outside the package, but only by classes that subclass it.
- **No modifier (default/"package-private")** — accessible to different classes and subclasses *within the current package only*.

## 2. Abstract Classes

### Motivation
As you move up an inheritance tree, classes become more general, or **abstract**. Sometimes you want a superclass that defines the *structure* of an abstraction without providing an implementation for every method — leaving the details to subclasses. **Abstract classes** provide this mechanism.

**Why it's needed (Animal hierarchy example from Lecture 3)**: all animals breathe, so `Animal` should have a `Breath()` method. But animals breathe in different ways — humans have lungs, fish have gills (class discussion confirmed this is exactly why: there's no single implementation of "breathing" covering every animal). There's no single correct implementation of `Breath()` that applies to every subclass. An abstract method solves this: the superclass declares *that* the method must exist, without saying *how*. The method only becomes concrete further down the tree, at whatever level is specific enough to have one true implementation (e.g., "land animal" vs. "aquatic animal").

**Why abstract classes can't be instantiated (the analogy)**: "Animal" is a taxonomic concept, not something that exists in the wild — you can't walk into a store and buy "an animal," only a specific bird or a specific kitten. Same logic for abstract classes: you can never do `new Animal()` or `new Person()` directly. Confirmed live: `Person mrX = new Person("...")` throws a compiler error — **"Cannot instantiate the type Person."**

**What actually blocks instantiation**: purely the literal presence of the `abstract` keyword. Demonstrated live by removing `abstract` from `getPosition()` and giving it a body (e.g., `return null;`) — this instantly turns `Person` into an ordinary concrete class, indistinguishable in principle from `Employee` or `Intern`. There's nothing else structurally special about an abstract class beyond that keyword and having at least one unfinished method.

**When abstract classes are actually worth using**: if your hierarchy is a single branch (only one class extends the would-be abstract superclass), there's no real benefit — you're not saving anything. Abstract classes pay off specifically when there are **multiple sibling subclasses** (e.g., both `Employee` and `Intern` extending `Person`) sharing structure — that's when defining shared behaviour once instead of duplicating it actually matters.

### Rules for working with abstract classes
- Declared with the keyword `abstract`.
- **Cannot be instantiated** — you can never do `new Person()` if `Person` is abstract.
- Can contain **both concrete methods and abstract methods**.
- Abstract methods are declared with the keyword `abstract` (and have no body — just a signature ending in `;`).
- **Constructors cannot be declared abstract.**
- Any subclass of an abstract class must implement **all** abstract methods, **or** be declared abstract itself (deferring the obligation further down the tree).
- Classes that are *not* abstract are called **concrete classes**.

### Worked example — Person / Employee / Intern
Motivation: "Employees are people too." A `Person` superclass makes sense since all people share attributes (name, height, weight, etc.). This also lets the company model **Interns** — people who aren't employees.

**Design**: move `getName()` from `Employee` up to `Person` (concrete — just returns a field). Add a new **abstract** method to `Person`: `getDescription()`/`getPosition()` — each subclass must define its own version describing that person's role.

**UML notation**: *italics* = abstract (both the class name `Person` and the method `getPosition()` are italicized in the diagram, since `Person` is abstract and `getPosition()` has no default implementation).

```
Person (abstract)
- field: name
+ getName()          [concrete]
+ getPosition()       [abstract]
        △
   ┌────┴────┐
Employee    Intern
- field: salary
+ getSalary()
+ getPosition()  [Employee's own implementation]
   △
Manager
+ setBonus()
```

### Code — the abstract `Person` class
```java
public abstract class Person {
    private String name;

    // Constructor
    public Person(String name) {
        this.name = name;
    }

    // Concrete method
    public void printGreeting() {
        System.out.println("Hello, my name is " + name);
    }

    // Abstract method - must be implemented by subclass
    public abstract String getPosition();
}
```

### `Employee` subclass
```java
public class Employee extends Person {
    private double salary;

    // Constructor calls abstract superclass constructor
    public Employee(double salary, String name) {
        super(name);
        this.salary = salary;
    }

    // Employee-specific position description
    @Override
    public String getPosition() {
        return "Employee " + getName() + " on salary $" + getSalary();
    }
}
```
Note: even though `Person` is abstract, its constructor still runs normally via `super(name)` — abstract just means you can't do `new Person(...)` directly, not that its constructor is unusable.

### `Intern` subclass
```java
public class Intern extends Person {
    // Constructor calls abstract superclass constructor
    public Intern(String name) {
        super(name);
    }

    // Employee-specific position description
    @Override
    public String getPosition() {
        return "Intern unpaid";
    }
}
```

### Example — polymorphism across the abstract hierarchy
```java
Manager officeBoss = new Manager(50000, "Bill Lumbergh");
officeBoss.setBonus(2750);
Employee workerBee = new Employee(20000, "Peter Gibbons");
Intern proletarian = new Intern("Tom Smykowski");
Person initechStaff[] = {officeBoss, workerBee, proletarian};
for (Person p : initechStaff) {
    System.out.println(p.getPosition());
}
```
Output:
```
Employee Bill Lumbergh on salary $52750.0
Employee Peter Gibbons on salary $20000.0
Intern unpaid
```
This works because `Manager`, `Employee`, and `Intern` all trace back to the common abstract superclass `Person` — the array can hold any mix of them, and calling `getPosition()` correctly dispatches to each object's own implementation (same polymorphism mechanism from Lecture 4).

### Why use abstract classes
- Define a **template** for a group of related subclasses.
- Mix concrete and abstract methods — generalized behaviour lives in the superclass, specific behaviour is deferred to subclasses.
- Guarantees no one can instantiate the abstract class directly — forces you to always work with a concrete, fully-specified subclass.

## 3. Interfaces

### Single inheritance and its limitation
Inheritance is powerful for "passing on" fields/behaviours shared by related entities, and lets you add new behaviour or override existing behaviour in subclasses. But unlike biological inheritance (two parents), **Java only allows single inheritance** — a class can only `extends` **one** superclass. This restriction exists because of the **diamond problem**.

### The diamond problem
Suppose `OpticalMouse` and `WirelessMouse` both inherit from a common superclass `Mouse` (which has a `refreshRate` field and an abstract `track()` method). Both override `track()`. Now suppose you wanted `WirelessOptical` to inherit from **both** `OpticalMouse` and `WirelessMouse` (hence "diamond" — the class diagram literally forms a diamond shape).

Two problems arise:
1. **Field conflict**: `refreshRate` is inherited from `Mouse` by both `OpticalMouse` and `WirelessMouse`, potentially with different values in each. If `WirelessOptical` needs both values, which one does it get?
2. **Method conflict**: which `track()` implementation gets invoked when called on a `WirelessOptical` instance — the one from `OpticalMouse`, or the one from `WirelessMouse`?

Java sidesteps this entire mess by disallowing multiple class inheritance in the first place. (An alternative like explicitly writing `superOptical.track()` vs `superWireless.track()` to disambiguate is conceivable, but clunky — Java's designers chose not to go that route, inventing interfaces instead.)

### Interfaces as the solution
Java uses **interfaces** (keyword `interface`) to get most of the benefits of multiple inheritance without the diamond problem's complexity. The trick: interfaces sidestep the conflict by making **all methods abstract**\* — so a class that uses an interface must implement all of its methods itself, with no ambiguity about which implementation "wins."

*(\*Note: this changed with Java 8, which introduced default methods in interfaces — but that's explicitly flagged as beyond the scope of CSCI2010U.)*

### Interfaces vs. abstract classes
An **interface is not a class** — it's a **set of requirements**. It defines a **role** that other classes can play, regardless of where they sit in the inheritance tree (or which tree entirely). Example: a `Manager` is a `Person` (inheritance), but might also take on multiple unrelated roles within the company — e.g., "Event Organiser" and "Paramedic." **A Java class can implement multiple interfaces**, which is how a single class can take on many such roles simultaneously — this is the key difference from single-inheritance class hierarchies.

**Real-world example from lecture**: staff at a university might have a primary job title (e.g., working at a service desk) but also independently take on roles like event organizer, CPR-trained paramedic, or graduate supervisor — none of these roles are subclasses of each other or of the primary job; they're separate capabilities layered on top. This is exactly what implementing multiple interfaces models: several unrelated "roles" added to one class, with no diamond-problem risk, because interface methods are only requirements, never competing implementations.

### Defining/using an interface — the `Comparable` example
Motivating problem: the company wants to sort employees by various criteria, using the built-in `Arrays.sort()` method. A requirement of `sort()` is that all objects being sorted must be instances of classes that **implement the `Comparable` interface**.

**The `Comparable` interface's actual source (simplified)**:
```java
public interface Comparable<T> {
    public int compareTo(T o);
}
```
It has a single method, `compareTo`, which takes an object and returns an integer telling you whether the current object is less than, equal to, or greater than the argument object.

**What that integer means is entirely up to you** — that's the whole point of the interface: you decide how two objects of your own class should be compared (by salary, age, tenure, or some complex mixture).

### Implementing an interface — two requirements
To implement an interface, a class must:
1. Declare that it is implementing the given interface.
2. Provide concrete definitions for **all** methods of the interface.

```java
public class Employee extends Person implements Comparable<Employee> {
    @Override
    public int compareTo(Employee e) {
        return Double.compare(getSalary(), e.getSalary());
    }
    ...
}
```
- `Double.compare(a, b)` returns negative if `a < b`, `0` if equal, positive if `a > b` — following the same convention `compareTo` is expected to follow.
- Note a class can both `extends` a superclass **and** `implements` an interface (or multiple interfaces) at the same time — this is exactly the "many roles" mechanism mentioned above.

### Generics (brief aside — full topic in Lecture 13)
`Comparable<Employee>` uses **generics**: the `<...>` (informally called "the diamond" — different concept from the diamond *problem*) restricts the type of data a class/interface/method can hold or operate on. E.g., `ArrayList<String> names = new ArrayList<String>();` restricts that list to only ever hold `String` objects. Here, `Comparable<Employee>` tells the compiler this class only ever compares against other `Employee` objects, so it can safely rely on `Employee` having a `getSalary()` method.

### Putting it together — sorting employees
```java
Manager officeBoss = new Manager(50000, "Bill Lumbergh");
officeBoss.setBonus(2750);
Employee workerBee1 = new Employee(20000, "Peter Gibbons");
Employee workerBee2 = new Employee(48000, "Mario Savio");
Person initechStaff[] = {officeBoss, workerBee1, workerBee2};
// Sort our array
Arrays.sort(initechStaff);
for (Person p : initechStaff) {
    System.out.println(p.getPosition());
}
```
Output (sorted ascending by salary, since `compareTo` was implemented that way):
```
Employee Peter Gibbons on salary $20000.0
Employee Mario Savio on salary $48000.0
Employee Bill Lumbergh on salary $52750.0
```
`Arrays.sort()` works here because `Employee` (and by inheritance, `Manager`) implements `Comparable`, giving `sort()` a defined way to order the objects.

**Important — sort order comes from `compareTo`, not insertion order**: this was directly demonstrated live. Printing the array *before* calling `Arrays.sort()` shows objects in whatever order they were inserted; printing *after* always shows them ordered by salary (ascending), regardless of insertion order. This confirms `compareTo()`, not the order you added elements, is what determines the sorted result.

## Class Q&A: Can an abstract class have a static method?
**Yes.** Demonstrated live by adding a `public static` method directly inside the abstract `Person` class. This works because static methods belong to the **class itself**, not to any particular instance — so the "you can't instantiate this" restriction on abstract classes is irrelevant to them. You can call a static method on an abstract class without ever creating an object of it.
