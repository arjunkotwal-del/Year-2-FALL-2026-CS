# Lecture 2 — Java Basics & Implementing Bubble Sort

> Sourced from L02_java_basics.pdf (Canvas). No transcript today — built from slides only.

## Outline
1. Setting up Java
2. Implementing bubble sort in Java
3. Review of Java concepts
4. Analysis of bubble sort

## 1. Setting up Java
- Editor: **VS Code**
- Install: VS Code, Microsoft's OpenJDK, VS Code "Coding Pack for Java" extension
- Run a program: click **Run** above `main`, or press **F5**
- Optional keybinding: `Ctrl-K Ctrl-S` → search "Run java" to set a custom shortcut

## 2. Implementing Bubble Sort in Java

Two components:
- Nested `for` loops (the sorting logic)
- `Swap` — a utility method for exchanging two array elements

### Swap method
```java
/**
 * Swap two array elements
 */
public static void Swap(int[] A, int j, int i) {
    int temp;
    temp = A[j];
    A[j] = A[i];
    A[i] = temp;
}
```
Needs a `temp` variable — without it, the first assignment would overwrite the value before it's saved.

### Bubblesort method
```java
public static void Bubblesort(int[] A) {
    for (int i = A.length - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (A[j+1] < A[j]) {
                Swap(A, j, j+1);
            }
        }
    }
}
```
This is a direct translation of the Lecture 1 pseudocode — same structure, just Java syntax (`for (init; condition; update)` instead of `for i = ... downto ...`).

### Main method (test case)
```java
public static void main(String[] args) {
    int[] data = {4, 3, 5, 2, 1};
    System.out.println("Pre-sort:  " + Arrays.toString(data));
    Bubblesort(data);
    System.out.println("Post-sort: " + Arrays.toString(data));
}
```
Console output:
```
Pre-sort:  [4, 3, 5, 2, 1]
Post-sort: [1, 2, 3, 4, 5]
```

**Why neither `Bubblesort` nor `Swap` returns the array:** Java is pass-by-value, but for reference types (like arrays), the method receives a *copy of the reference* — both `main()` and `Bubblesort()` point to the **same underlying array object** in memory. So changes made inside `Bubblesort` are visible in `main` without needing a return value.

## 3. Review of Java concepts

### Class declaration
```java
public class Bubblesort1 {
    ...
}
```
- `public` — access modifier; optional since all top-level classes are public by default.
- `class` — all Java code must live inside a class (Java's basic unit of encapsulation).
- `Bubblesort1` — the class name **must match the filename** (e.g., `Bubblesort1.java`).

### Main method signature
```java
public static void main(String[] args) {
```
- `public` — must be public since it's called by code outside the class (the JVM calls it when the program starts).
- `static` — lets `main()` be invoked without first creating an object instance.
- `void` — tells the compiler `main()` returns nothing.
- `main` — the entry point of every Java application (case-sensitive, required in every program).
- `String[] args` — array of Strings holding command-line arguments passed when the program runs.

### Types in Java
Two kinds:
- **Primitive types**: integrals (`byte`, `short`, `int`, `long`, `char`), floating point (`float`, `double`), `boolean`.
- **Reference types**: classes (`String`, `ArrayList`, `Scanner`), arrays, and others.

### Passing types into methods (pass-by-value, but...)
- For **primitive types**: the method gets a brand-new **copy** of the variable's value.
- For **reference types**: the method gets a copy of the *reference* (the "address"), but both the caller and the method point to the **same object instance**. Changes to the object's contents are visible everywhere that reference points.
- This is exactly why `Bubblesort(data)` can sort `data` in place without returning anything — `main` and `Bubblesort` share the same array object.

### Arrays and `toString()`
- Arrays are **objects** in Java.
- All objects have a default `toString()` — for arrays this prints an unhelpful low-level representation, e.g. `[I@251a69d7` (this is what `System.out.println("...": + data)` gives you directly).
- `java.util.Arrays` provides `Arrays.toString(data)` — a proper "pretty print" for arrays: `[4, 3, 5, 2, 1]`.
- Must `import java.util.Arrays;` at the top of the file to use it.
- `System.out` — `System` is part of `java.lang` (auto-imported everywhere); `out` is a static field of type `PrintStream`, connected to the console by default.

### For loop — general form
```java
for (initialisation; expression; update) {
    body
}
```
Flow: run `initialisation` once → check `expression` → if true, run `body`, then `update`, then recheck `expression` → repeat until `expression` is false.

### Outer/inner loop roles (bubble sort specifically)
- **Outer loop** (`i`): tracks the number of passes through the array. Counting `i` *down* feels backwards at first, but it's what makes the inner loop's bound (`j < i`) simple and correct.
- **Inner loop** (`j`): does the actual neighbour-element comparisons, up to the limit `i` set by the outer loop.

### Class question (from lecture)
**Q: How could we get Bubblesort to sort in descending order instead?**
→ Flip the comparison: change `if (A[j+1] < A[j])` to `if (A[j+1] > A[j])`.

## 4. Analysis of Bubble Sort

Bubble sort gives the correct answer and runs near-instantly on a small array — but "correct and fast on a small case" isn't the same as "efficient." We care about **time efficiency** as arrays scale up.

### Measuring bubble sort's runtime
```java
public static void main(String[] args) {
    final double NANOSEC2SEC = 1e9;
    Random r = new Random();
    long start, end;
    int[] data = new int[1000];
    // Initialise array with random integers
    for (int i = 0; i < data.length; i++)
        data[i] = r.nextInt();
    // Track system times before and after sort
    start = System.nanoTime();
    Bubblesort(data);
    end = System.nanoTime();
    // Print time taken
    System.out.println("Time taken: " + (end-start)/NANOSEC2SEC + " sec");
}
```

### Timing results
| Array size (n) | Time (sec) |
|---|---|
| 10,000 | 0.12 |
| 100,000 | 13.50 |
| 1,000,000 | 1424.06 |

**Pattern**: each time `n` grows by a factor of 10, the runtime grows by a factor of ~100 (10²). This is a strong hint that bubble sort's time complexity scales with `n²` — formal proof/notation (Big-O) comes in Lecture 8.

**Caveat (important)**: measuring wall-clock runtime like this is system-dependent, doesn't scale as a general comparison method, and is prone to bias (e.g., choice of test cases). This is *why* we need a proper mathematical framework (Big-O notation) rather than just timing code — covered in Lecture 8 (Analysis of Algorithms).

## Coding challenge (try at home, not covered live)
1. Replace the outer `for` loop with a `while` loop that does the same thing.
2. Optimize: track whether a swap occurred during a pass — if no swaps happened, the array is already sorted and you can stop early (don't need to run all `n-1` passes). This is the same optimization idea from Lecture 1's Q6 practice question.
