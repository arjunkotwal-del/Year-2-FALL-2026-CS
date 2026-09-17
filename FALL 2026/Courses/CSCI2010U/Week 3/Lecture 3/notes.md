# Lecture 3 — Classes and Inheritance

> Sourced from L03_inheritance_1.pdf (Canvas, course 202609 - Data Structures - 40241). No transcript — built from slides only.

## Outline
1. Classes, objects, and OOP
2. Relationships
3. Inheritance
4. Inheritance in Java

## 1. Classes, Objects, and OOP

- Java is an **Object Oriented Programming (OOP)** language — fluency in Java requires fluency in the OOP paradigm.
- A Java program is made of **objects**, which contain data (**fields**) and code (**methods**).
- The **members** of a class = its fields + its methods.
- **Encapsulation**: some members are `public` (usable by outside code), others are `private` (hidden).

### Classes = blueprints
A **class** is a blueprint/template from which objects are made. Analogy: a panda-shaped biscuit cutter is the *class*; the individual biscuits it stamps out are the *objects*. When you **construct** a biscuit, you've **instantiated** an **instance** of the biscuit class.

### Three characteristics every object has
1. **State** — what the object *has* (its fields/properties). E.g., flavour = 'chocolate', temperature = 20°C.
   - Some state is fixed (`final`), some is dynamic — but all state changes should happen through a method call on the object (otherwise you've broken encapsulation).
2. **Behaviour** — what the object *does* (its methods). E.g., `warmUp()`, `takeABite()`, `putAway()`.
   - All instances of a class share a "family resemblance" via shared behaviours, e.g. `someCookie.getFlavour();`
3. **Identity** — what makes an object *unique*, even if it shares the same state/behaviour as another instance. E.g., a shipping company gives every package a unique tracking number even if two packages have identical dimensions/destination. In Java, object identity is specified by `Object.equals()` (covered in a later lecture).

### Identifying classes (design heuristic)
When designing OO systems, it can be tricky to know what should be a class vs. a method. Helpful heuristic (Russell Abbott): identify the **nouns** and **verbs** in your problem description.
- **Nouns → classes.** E.g., in a biscuit system: oven, biscuit cutter, baker.
- **Verbs → methods**, belonging to whichever class makes sense. E.g., biscuits are *cut* (cutter), *baked* (oven), *tasted* (baker).

**Class question (in-lecture):** Think about a software system for representing a vehicle. What are some possible classes and their methods? *(No answer given in slides — good practice question, see below.)*

## 2. Relationships
*(No dedicated slide content this lecture — likely folded into the Inheritance section below, or touched on verbally. Flag this if the recording later covers something not captured here.)*

## 3. Inheritance

**Definition**: the process by which one object acquires the properties (traits) of another object. We naturally think in *hierarchies* — e.g., a koala is a Marsupial, which is a Mammal, which is an Animal.

### Why hierarchies matter
Without them, every object would need to explicitly define every feature (a Koala eats, sleeps, has a skeleton, blinks, etc. — all spelled out). With a hierarchy, an object only needs to define what makes it *unique within its class* — it inherits the general qualities from its parent.

**Koala inheritance chain**: Animal → Mammal → Marsupial → Koala (with siblings like Reptile, Primate, Kangaroo branching off at each level).

### Superclass / subclass terminology
- If Mammal is a more specific case of Animal: **Mammal is a subclass of Animal**, and **Animal is the superclass of Mammal**.
- A subclass **inherits all attributes** of its superclass.
- **"Superclass" does NOT mean "better than a subclass."** A subclass inherits all the superclass's functionality, but can also **extend** it (add new features) and **override** it (redefine existing behaviour).

### Worked example: bathtub vendor
A vendor stocks 4 kinds of bathtubs (Generic, Whirlpool, Walk-in, Shower-combo). All four share: a `waterLevel` field, a `fill()` method, an `empty()` method.

- **Bad approach**: model all four as separate, unrelated classes, each duplicating the same field/methods. Fragile — a change to one means changing all four.
- **Better approach (inheritance)**:
  1. Pull the common state/behaviour into a new superclass, `Bathtub` (has `waterLevel`, `fill()`, `empty()`).
  2. Link the four specific types as **subclasses** of `Bathtub` using inheritance (arrow points from subclass up to superclass, meaning "inherits from").
  - Read as: "Shower-combo inherits from Bathtub."

## 4. Inheritance in Java

### Worked example: Employee / Manager
Company has 3 employee types: salespeople, managers, custodians. All employees earn a salary. Managers are treated differently — they can also receive a **bonus**.

**Identifying the inheritance relationship**: use the **"is a"** test — if you can say "X is a Y," X is probably a subclass of Y. A manager **"is an"** employee → `Manager` should inherit from `Employee`, adding manager-specific functionality (the bonus) while keeping the general employee behaviour.

**UML diagram** (superclass → subclasses):
```
        Employee (superclass)
        - salary, - name
        + getSalary(), + getName()
             △
    ┌────────┼────────┐
 Manager  Salesperson  Custodian
 (+ setBonus, only Manager has this)
```

### Employee class (superclass)
```java
public class Employee {
    private double salary;
    private String name;

    public Employee(double salary, String name) {
        this.salary = salary;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }
}
```
- Fields are `private` — enforces encapsulation, prevents uncontrolled external access.
- `this` refers to the current object instance — `this.name = name;` assigns the constructor's parameter value to the field belonging to *this* specific object. Called an **implicit parameter**.

### Manager class (subclass) — using `extends`
```java
public class Manager extends Employee {
    private double bonus = 0;

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }
}
```
- `extends` is the Java keyword that creates a subclass relationship.
- `Manager` automatically has `getName()` and `getSalary()` inherited from `Employee` — no need to redefine them.
- `Manager` additionally defines `setBonus()`, which only it has.

### Using it
```java
// Create a new boss, give him a bonus
Manager officeBoss = new Manager(70000, "Bill Lumbergh");
officeBoss.setBonus(500);

// Print the employee's name
System.out.println(officeBoss.getName());
```
Output: `Bill Lumbergh` — a Manager can still call methods of its Employee superclass.

### The "is-a" relationship is one-directional
```java
// Lets try and sneak our regular employee a bonus...
Employee workerBee = new Employee(34000, "Peter Gibbons");
workerBee.setBonus(5000);  // COMPILE ERROR
```
Result: `Exception in thread "main" java.lang.Error: The method setBonus(int) is undefined for the type Employee`

**Why this fails**: subclasses inherit state/behaviour from their superclass, but **the reverse is not true** — a superclass has no knowledge of what its subclasses add.
- "Manager IS-A Employee" makes sense → `Manager extends Employee` ✓
- "Employee IS-A Manager" does **not** make sense → `Employee` should never `extend Manager` ✗

This directionality is the core rule to internalize: **inheritance flows from general (superclass) to specific (subclass), never the other way.**
