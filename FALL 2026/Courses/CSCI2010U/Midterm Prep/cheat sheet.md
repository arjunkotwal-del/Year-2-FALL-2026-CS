# CSCI2010U Midterm Cheat Sheet (double-sided)

Built only from slides L1-L10. Copy it onto your sheet by hand if you can: writing it is itself revision. Check that handwritten or printed is allowed, and the size limit, before you commit.

# SIDE A: CODE AND ALGORITHMS

## Bubble sort (L1, L2)
```
for i = A.length-1 downto 1        // i is FIXED for the whole pass = number of pairs to check
    for j = 0 to i-1               // j MOVES after every comparison
        if A[j+1] < A[j]  Swap(A, j, j+1)
```
```java
for (int i = A.length-1; i > 0; i--)
  for (int j = 0; j < i; j++)
    if (A[j+1] < A[j]) swap(A, j, j+1);
static void swap(int[] A, int j, int k){ int temp=A[j]; A[j]=A[k]; A[k]=temp; }
```
- n elements: n-1 passes. Pass 1 makes n-1 comparisons, then n-2, ... 1.
- After pass k the last k elements are locked in place.
- Descending order: change `<` to `>`.
- Worst case O(n^2). Timing in L2: n x10 gave time x100 (0.12s, 13.5s, 1424s for 10k, 100k, 1M).
- No return needed: arrays are reference types, so the method gets a copy of the reference to the SAME array.
- `Arrays.toString(a)` needs `import java.util.Arrays;`. Printing an array directly gives `[I@...`.
- for loop: `for (init; condition; update) { body }`.
- main: `public static void main(String[] args)`. public = JVM can call it, static = no object needed, void = returns nothing.
- Primitive types: method gets a copy of the value. Reference types: copy of the reference.

## Linear search (L6)
```
for i = 0 to A.length-1
    if A[i] == val  return i
return -1
```
```java
for (int i = 0; i < A.length; i++) if (A[i] == val) return i;
return -1;
```
Best case: val at A[0], O(1). Worst case: val last or missing, exactly A.length comparisons, O(n).

## Binary search (L10): array must be SORTED
```
Binary_search(A, val, low, high)
 if low > high  return NOT_FOUND
 mid = (low + high)/2
 if val == A[mid]  return mid
 else if val < A[mid]  return Binary_search(A, val, low, mid-1)
 else                  return Binary_search(A, val, mid+1, high)
```
Start call: `binarySearch(a, val, 0, a.length-1)`. One comparison finds it or halves the range. Worst case log2(n) halvings, O(log2 n).

## Array insert / delete (L10), arrays have fixed length, index 0..n-1, access O(1)
```java
insert(a, idx, val):  for (int i = a.length-1; i > idx; i--) a[i] = a[i-1];   a[idx] = val;
delete(a, idx):       for (int i = idx+1; i < a.length; i++) a[i-1] = a[i];   a[a.length-1] = GAP;
```
Worst case idx = 0: O(n). Best case idx = n-1 (last): O(1). Insert shifts RIGHT starting from the end. Delete shifts LEFT starting from idx+1.

## Perfect square (L6, L9)
- v0: `while i <= n`, check i*i == n. O(n).
- v1: `while i*i <= n`. O(sqrt n).
- v2: double i until i*i > n, then binary search between low = i/2 and high = i. O(log2 n).

## Recursion (L7)
- Needs a BASE CASE (first statement, has a return, guarantees termination) and a RECURSIVE CASE (calls itself on a SMALLER subproblem).
- Missing base case or no progress toward it gives StackOverflowError.
- Calls go on the call STACK. A call is suspended when it calls itself, and resumes on the line AFTER the call when the inner call returns.
- Print BEFORE the recursive call gives down order. Print AFTER gives up order.
- `countdown(3)` prints 3 2 1 0. `printUp(3)` (print after call, base n<=0) prints 1 2 3.
- Trace method: one indented line per call with its parameter values, mark each base case, write output in the order it happens.
- Recursion vs iteration: default to iterative unless the problem is naturally recursive. TOH recursive, factorial iterative.
```
TOH(n, start, goal, temp)
  if n == 0 return
  TOH(n-1, start, temp, goal)       // move n-1 to temp
  move(start, goal)                 // print start --> goal
  TOH(n-1, temp, goal, start)       // move n-1 onto goal
```
- Initial call `TOH(n, "A", "C", "B")`.
- n=2 moves: A-B, A-C, B-C.
- n=3 moves (7): A-C, A-B, C-B, A-C, B-A, B-C, A-C. Calls with n=0 (base): 8.
- Moves for n discs: 2^n - 1.

# SIDE B: OOP AND ANALYSIS

## Objects (L3)
- Class = blueprint, object = instance. Object has STATE (fields), BEHAVIOUR (methods), IDENTITY (unique, `equals`).
- Nouns become classes, verbs become methods. Members = fields + methods.
- Encapsulation: private fields, access via public methods. Java catches errors at compile time. `final` = fixed value.
- `this` = the current object. Getter reads, setter writes.
- Subclass inherits from superclass. "is a" test: Manager is an Employee, so `Manager extends Employee`. Never the reverse.
- "Superclass" does not mean better. Subclass can EXTEND (add) and OVERRIDE (redefine).

## Inheritance code (L4)
```java
class Manager extends Employee {
  private double bonus;
  public Manager(double salary, String name){ super(salary, name); this.bonus = 0; }  // super(...) FIRST
  @Override public double getSalary(){ return super.getSalary() + bonus; }
}
```
- private in superclass is NOT visible in subclass. `salary + bonus` gives "field is not visible".
- `getSalary() + bonus` inside the override calls ITSELF, so StackOverflowError. Use `super.getSalary()`.
- `super.salary` is illegal. super is not an object reference, `this` is.
- super has 2 meanings: call a superclass method, call the superclass constructor.

## Polymorphism (L4)
- `Manager boss = new Manager(...)`: declare reference variable, create object on the HEAP, link them.
- Reference type can be a SUPERCLASS of the object type: `Employee e = new Manager(...)` is OK. `Manager m = new Employee(...)` does NOT compile.
- Read assignment right to left: Manager is-a Employee, OK.
- `Employee[] a = {employee, manager}` is OK. Calling `a[i].getSalary()` uses the object's own version (dynamic method dispatch, named only).
- A method with an `Employee` parameter accepts any subclass.
- Superclass reference can't call subclass-only methods (`workerBee.setBonus()` fails).

## Packages, access, abstract, interface (L5)
| | public | protected | none | private |
|---|---|---|---|---|
| same class | Y | Y | Y | Y |
| same pkg subclass | Y | Y | Y | N |
| same pkg non-subclass | Y | Y | Y | N |
| diff pkg subclass | Y | Y | N | N |
| diff pkg non-subclass | Y | N | N | N |
- Package: first statement `package name;`, class names unique per package, nested like folders. java.lang auto-imported (System, Math, String). java.util has Arrays, Random.
- Abstract class: `abstract` keyword, CANNOT be instantiated, can mix concrete and abstract methods, a constructor cannot be abstract, a subclass must implement ALL abstract methods or be abstract. Can have static methods. Concrete = not abstract.
- Java has SINGLE class inheritance (one `extends`) because of the DIAMOND problem: shared field and which method to call.
- Interface = a role, set of requirements, all methods abstract (Java 8 change not covered). Class can implement MANY.
```java
class Employee extends Person implements Comparable<Employee> {
  @Override public int compareTo(Employee e){ return Double.compare(getSalary(), e.getSalary()); }
}
```
- compareTo returns negative if this < other, 0 if equal, positive if this > other. `Arrays.sort` needs Comparable. Sort order comes from compareTo, not insertion order.
- Generics `<Employee>` restrict the type (full topic L13).

## Algorithms and analysis (L6, L8, L9)
- Algorithm: FINITE, DETERMINISTIC (same input same output), EFFECTIVE, IMPLEMENTATION (abstract enough for any language, every step precise). Pseudocode is for humans, language-free. al-Khwarizmi (c. 800 CE), Turing and Church formalised it in the 1930s.
- Efficiency = time (count basic steps) and space (memory). Time matters most.
- T(n) = number of basic steps for input size n. Each line costs a constant c_i. `end` and comments are not counted. A loop header runs ONE MORE time than its body.
- Linear search: T = c1(t+1) + c2*t + c3 + c4. Best t=1, constant. Worst t=n, T = an + b, linear.
- Best = shortest, worst = longest, average not covered. We use WORST case: it is an upper bound guarantee, and it often happens (searching for a missing value).
- Rate of growth ladder, slowest to fastest: 1, log n, sqrt n, n, n log n, n^2, n^3, 2^n, n!
- Drop lower-order terms AND the constant coefficient: 3n^2 + 90n -> O(n^2).
- BIG-O: f(n) = O(g(n)) if there exist positive c and n0 with 0 <= f(n) <= c*g(n) for all n >= n0. g is an UPPER bound. O(g) is a SET of functions. c >= 1, n0 >= 1.
- 3 + 5n^2 + 7n^3 <= 15n^3, so O(n^3). A polynomial is O(its highest power).
- Class challenge answers for 3 + 5n + 18n^2: O(n) FALSE, O(n^2) TRUE, O(n^3) TRUE. 3^n = O(n^3) FALSE. n^3 = O(3^n) TRUE.
- Loop patterns: pre/post work O(1). Single loop 0..n O(n). Nested loops O(n^2). Variable halved or doubled each step O(log2 n). Divide and conquer with linear combine O(n log2 n).
- Big-O is notation. Worst case is the type of input. Big-O can describe best, worst or any case.
