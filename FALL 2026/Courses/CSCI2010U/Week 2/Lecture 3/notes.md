
# Lecture 3 — Classes and Inheritance

> Sourced from L03_inheritance_1.pdf slides + live lecture transcript (course 202609 - Data Structures - 40241). See [transcript.md](transcript.md) for the full raw walkthrough.

## Outline
1. Classes, objects, and OOP
2. Relationships
3. Inheritance
4. Inheritance in Java

**Note on "Relationships"**: there's no dedicated slide/section for this — it flows directly from "Classes, objects, and OOP" into "Inheritance" in the live lecture. Not a gap, just how the material was actually delivered.

## Course context (from live lecture)
- Everything written in Lectures 1–2 (bubble sort etc.) was **static/procedural** code — top-to-bottom execution, similar to how Python often runs. Tonight is the first time the course introduces actual **objects**.
- Course pacing: Lectures 3–5 continue Java/OOP fundamentals. From **Lecture 6 onward**, the course becomes purely algorithms-focused.
- **Lab 1** does not require tonight's content. **Lab 2 (next week)** is entirely about inheritance/classes — this lecture is the prep for it.
- Labs must be done live in the lab session in front of the TA (not pre-solved and brought in) — the point is demonstrating understanding, not just producing a correct answer. Explaining your own code out loud is one of the best ways to confirm you understand it.
- **Why OOP exists**: the driving idea is **encapsulation** — objects have their own scope/methods/knowledge, and only specific things can see or act on their contents. This is meant to make code more manageable and reduce errors (arguably; instructor personally uses OOP rarely in data science, but for long-running, world-interacting enterprise systems it carries real value — a big reason Java became a major enterprise language).

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
3. **Identity** — what makes an object *unique*, even if it shares the same state/behaviour as another instance. Examples from lecture: many people at a university can share your exact first+last name, so the university needs a separate unique identifier (student ID) to distinguish you — names aren't globally or even locally unique. Similarly, a shipping company gives every package a unique tracking number even if multiple identical packages (same product, same day, same destination — e.g., a bulk order to one address) are shipped together. In Java, object identity is formally specified by `Object.equals()` (and typically paired with overriding `hashCode()`) — covered in a later lecture, beyond scope for now.

**Aside — why Java pushes encapsulation this hard**: Java's design philosophy is to catch as many bugs as possible at **compile time**, before code ships to production. This is why fields get declared `private`, fixed values get declared `final`, and typing is strict. Contrast with Python/R/MATLAB, which are more permissive and let more issues surface only at runtime. Java doesn't *force* you to encapsulate (you technically could make every field `public`), but doing so runs against the language's whole design intent.

### Identifying classes (design heuristic)
When designing OO systems, it can be tricky to know what should be a class vs. a method. Helpful heuristic (Russell Abbott): identify the **nouns** and **verbs** in your problem description.
- **Nouns → classes.** E.g., in a biscuit system: oven, biscuit cutter, baker.
- **Verbs → methods**, belonging to whichever class makes sense. E.g., biscuits are *cut* (cutter), *baked* (oven), *tasted* (baker).

**Class question (in-lecture) — answered live:** Think about a software system for representing a vehicle. What are some possible classes and their methods?
- **Engine**, **Radio** (`turnOn()`, `turnOff()`, `changeFrequency()`), **Wipers** (`on()`, `off()`, `faster()`, `slower()`), **Transmission/gear stick** (`changeUp()`, `changeDown()`), **Wheels**, **Windows**.
- General principle: a good candidate for its own class is something where you'd want **multiple instances**, each with its own state/actions and unique identity (e.g., 4 wheels, several windows) — not just a single miscellaneous property of the car.

## 2. Relationships
*(No dedicated slide content this lecture — likely folded into the Inheritance section below, or touched on verbally. Flag this if the recording later covers something not captured here.)*

## 3. Inheritance

**Definition**: the process by which one object acquires the properties (traits) of another object. We naturally think in *hierarchies* — e.g., a koala is a Marsupial, which is a Mammal, which is an Animal.

### Why hierarchies matter
Without them, every object would need to explicitly define every feature (a Koala eats, sleeps, has a skeleton, blinks, etc. — all spelled out). With a hierarchy, an object only needs to define what makes it *unique within its class* — it inherits the general qualities from its parent.

**The abstraction challenge (emphasized in lecture)**: picking the right level of abstraction at each layer is genuinely hard. At the top of the hierarchy (Animal), you need traits that nearly *everything* below shares — but not every "obvious" animal trait is universal. E.g., worms don't have a skeleton or eyes, but they do eat and sleep. By the time you're near the bottom of the tree (a specific species), the unique traits are much easier to pin down. This is why designing good class hierarchies takes real thought, not just intuition.

**Animal's "big 5" traits** (from lecture): eat, excrete waste, breathe oxygen, move, reproduce.
**Mammal adds**: mammary glands, fur/hair, neocortex — Mammal inherits the "big 5" *plus* these three.
**Important one-directional check**: "mammals have mammary glands" does NOT mean "animals have mammary glands" — a lizard is an animal but not a mammal, and doesn't have them. This is the same one-directional inheritance rule that shows up later with Employee/Manager.

**Koala inheritance chain**: Animal → Mammal → Marsupial → Koala (with siblings like Reptile, Primate, Kangaroo branching off at each level). Marsupial-specific trait: abdominal pouch for carrying young.

**Mid-level abstraction note**: you can point to an actual koala or a specific human, but you can't point to "a mammal" or "a marsupial" — those are abstract categories that only become concrete once you reach an actual instantiable species/class further down the tree.

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
- Fields are `private` — enforces encapsulation, prevents uncontrolled external access. **Why this matters (from lecture)**: Java won't stop you from making fields `public`, but if external code can directly read/write a field, it can do so in unintended ways and potentially corrupt the object's state or crash the program. Routing all access through methods (getters/setters) means the class controls exactly how its data is read and changed — that control *is* encapsulation in practice.
- `this` refers to the current object instance — `this.name = name;` assigns the constructor's parameter value to the field belonging to *this* specific object. Called an **implicit parameter**. Writing `this.` isn't strictly required inside the constructor, but is considered good practice for clarity.
- **Getter/setter naming convention**: `get` = read a value, `set` = write a value — standard OOP naming pattern used throughout.

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

This directionality is the core rule to internalize: **inheritance flows from general (superclass) to specific (subclass), never the other way.** If it were symmetric, there'd be no point having the hierarchy at all.

## Note: live demo was interrupted
The instructor's Java environment crashed mid-demo (JVM/system issue following an OS update earlier that day — "bad CPU to run an executable") and he couldn't actually run the `officeBoss`/`workerBee` code live. Everything above reflects what was shown in code and explained verbally, but wasn't confirmed by a live run. He plans to fix his system and pick this up properly in Lecture 4, which continues into more advanced inheritance concepts, including **polymorphism**.

