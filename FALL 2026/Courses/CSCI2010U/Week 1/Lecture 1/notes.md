# Lecture 1 — Introduction & Bubble Sort

## Course logistics
- Instructor: Dr. Steven R. Livingstone
- Grading: Labs 20% (pass/fail, lowest of 11 dropped) | Midterm 40% | Final 40%
- Labs start Week 2, in person, done in pairs (groups of 3 allowed if odd numbers), can't be completed individually or outside the assigned session
- AI is **banned** on assessments — allowed only as a learning aid (explaining concepts, generating extra practice problems)

## Efficiency — time vs. space
- **Time**: estimated by counting the number of operations required to solve an instance of the problem
- **Space**: amount of memory required to solve the problem instance
- Sorting algorithms split into:
  - Simple/inefficient: Bubble sort, Insertion sort, Selection sort
  - Efficient: Merge sort, Quicksort, Heapsort, Shellsort

## Algorithms as recipes
- An algorithm is a set of instructions for accomplishing a task — an **abstraction** that gives the important steps but omits minor details.
- **Pseudocode**: language for describing algorithm behaviour to humans; ignores software-engineering concerns like error handling.

## Bubble Sort

**Idea**: repeatedly scan the array comparing *adjacent* elements, swapping them if out of order. Each full pass "bubbles" the largest remaining unsorted value to its correct final position at the end of the unsorted region.

**Pseudocode**:
```
Algorithm: Bubblesort(A)
1: for i = A.length-1 downto 1
2:     for j = 0 to i-1
3:         if A[j+1] < A[j]
4:             Swap(A, j, j+1)
5:     end
6: end
```

- Outer loop `i`: counts down from `n-1` to `1`. Tracks how much of the array is still unsorted (shrinks by 1 each pass, since the last element of the previous pass is now locked in).
- Inner loop `j`: walks left-to-right through the unsorted portion (`0` to `i-1`), comparing `A[j]` and `A[j+1]`.
- Swap condition: if `A[j+1] < A[j]`, the pair is out of order for ascending sort → swap.

### Worked trace: `[4, 3, 5, 2, 1]`

**Pass 1** (i=4, j: 0→3):
```
j | Compare      | Swap? | Array after
--|--------------|-------|-------------
0 | 4,3 → 3<4    | yes   | 3 4 5 2 1
1 | 4,5 → 5<4? no| no    | 3 4 5 2 1
2 | 5,2 → 2<5    | yes   | 3 4 2 5 1
3 | 5,1 → 1<5    | yes   | 3 4 2 1 5
```

End of pass 1: `3 4 2 1 5` — `5` locked in.

**Pass 2** (i=3, j: 0→2):
```
j | Compare   | Swap? | Array after
--|-----------|-------|-------------
0 | 3,4 → no  | no    | 3 4 2 1 5
1 | 4,2 → 2<4 | yes   | 3 2 4 1 5
2 | 4,1 → 1<4 | yes   | 3 2 1 4 5
```

End of pass 2: `3 2 1 4 5` — `4` locked in.

**Pass 3** (i=2, j: 0→1):
```
j | Compare   | Swap? | Array after
--|-----------|-------|-------------
0 | 3,2 → 2<3 | yes   | 2 3 1 4 5
1 | 3,1 → 1<3 | yes   | 2 1 3 4 5
```

**Pass 4** (i=1, j: 0→0):
```
j | Compare   | Swap? | Array after
--|-----------|-------|-------------
0 | 2,1 → 1<2 | yes   | 1 2 3 4 5
```

Result: `[1, 2, 3, 4, 5]`. Total passes = n − 1 = 4.

### Key takeaways
- Bubble sort makes at most `n-1` passes.
- After pass `k`, the last `k` elements are guaranteed sorted and don't need to be re-checked.
- It's simple but inefficient — O(n²) comparisons in the worst case (more on Big-O once we hit the analysis lectures).
