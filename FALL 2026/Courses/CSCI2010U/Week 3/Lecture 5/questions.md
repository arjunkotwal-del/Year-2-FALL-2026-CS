# Lecture 5 — Practice Questions

## Q1. Access modifier truth table
Without looking at notes.md, fill in this table from memory (Yes/No):
| Member access | public | protected | no modifier | private |
|---|---|---|---|---|
| Same class | | | | |
| Same package, subclass | | | | |
| Same package, non-subclass | | | | |
| Different package, subclass | | | | |
| Different package, non-subclass | | | | |

Then explain in one sentence each why `protected` and default (no modifier) differ specifically for the "different package, subclass" row.

## Q2. Abstract class rules — true or false
a) An abstract class can have a constructor.
b) You can create `new Person()` if `Person` is declared abstract.
c) An abstract class must have at least one abstract method.
d) A subclass of an abstract class must implement every abstract method, unless it is itself declared abstract.
e) A constructor can be declared abstract.

## Q3. Design your own abstract hierarchy
Design an abstract class `Shape` with:
- A concrete method `describe()` that prints something generic.
- An abstract method `getArea()`.
Then write two concrete subclasses, `Circle` and `Rectangle`, each implementing `getArea()` correctly (Circle needs a `radius` field, Rectangle needs `width`/`height`).

## Q4. The diamond problem
Explain, in your own words, the two specific problems that arise if Java allowed a class to extend two superclasses that share a common ancestor (use the Mouse/OpticalMouse/WirelessMouse/WirelessOptical example). Why does restricting Java to single inheritance avoid this?

## Q5. Interface vs abstract class
List two differences between an interface and an abstract class, based on what's covered in Lecture 5. Specifically: can a class implement multiple interfaces? Can a class extend multiple abstract classes? Why does the "role" framing (Event Organiser, Paramedic) make more sense for interfaces than for inheritance?

## Q6. Implement Comparable
Given the `Shape` class from Q3, make it implement `Comparable<Shape>`, comparing shapes by their area (smallest to largest). Write the full `compareTo` method using `Double.compare()`.

## Q7b. Static methods in abstract classes (answered live in lecture — confirm you understand why)
The lecture confirmed abstract classes CAN have static methods. Explain in your own words why this doesn't contradict the "abstract classes can't be instantiated" rule — what's different about how static methods are invoked compared to instance methods?

## Q7. Trace the sorting example
Given:
```java
Employee a = new Employee(45000, "A");
Employee b = new Employee(30000, "B");
Employee c = new Employee(60000, "C");
Person[] staff = {a, b, c};
Arrays.sort(staff);
for (Person p : staff) System.out.println(p.getName());
```
Assuming `Employee` implements `Comparable<Employee>` comparing by salary ascending, what gets printed, in order? Why does this compile even though the array is typed `Person[]`, not `Employee[]`?
