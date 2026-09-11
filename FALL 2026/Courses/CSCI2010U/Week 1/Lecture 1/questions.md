# Lecture 1 — Practice Questions

## Q1. Trace by hand
Trace bubble sort on `[8, 1, 6, 4, 9]`. Show every comparison and swap, pass by pass, in a table (like the worked example in notes.md). State how many passes it takes and which elements get "locked in" after each pass.

## Q2. Trace by hand (already-sorted input)
Trace bubble sort on `[1, 2, 3, 4, 5]`. What do you notice about the number of swaps? Does the pseudocode as written still run all `n-1` passes even though no swaps happen? (Hint: look closely at the loop structure — is there an early-exit condition?)

## Q3. Worst case
Construct a 5-element array that forces the *maximum* possible number of swaps for bubble sort. Justify why it's the worst case.

## Q4. Conceptual
Explain in your own words why the inner loop only needs to go up to `i-1` (not all the way to `A.length-1`) on every pass.

## Q5. Implementation (attempt independently, no AI)
Write the Java method signature and body for:
```java
public static void bubbleSort(int[] A) {
    // your implementation here
}
```
Translate the pseudocode directly — get the loop bounds right first, then worry about style.

## Q6. Stretch
The pseudocode always runs the full `n-1` outer passes even if the array becomes sorted early. Modify your Java implementation to add an optimization: stop early if a full pass makes zero swaps. What's the best-case behavior now for an already-sorted array?
