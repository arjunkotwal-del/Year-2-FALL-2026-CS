# Practice answers (open only after finishing the set)

Mark yourself, then copy every miss into `error log.md` with the reasoning in your own words.

## Bubble sort and Java
1. adjacent (neighbouring)
2. largest
3. `i > 0`, `j < i`, `A[j+1] < A[j]`
4. 5, 4, 5 passes
5. i is fixed during a pass, j moves
6. [6,2,5,1]: 2 6 5 1, then 2 5 6 1, then 2 5 1 6. Array after the pass: [2, 5, 1, 6]
7. `>`
8. temp (temporary)
9. reference, reference
10. 100 (about x100)

## Objects, inheritance, polymorphism
11. state, behaviour, identity
12. classes, methods
13. extends, "is a"
14. is not, getter (public getSalary())
15. @Override, super
16. StackOverflowError
17. first
18. (a)
19. Manager's (the object's own class)
20. address (reference / location), heap
21. Employee has no setBonus method, only Manager does (a superclass does not know what subclasses add)

## Packages, abstract classes, interfaces
22. first, default
23. java.lang
24. subclasses
25. No
26. cannot, cannot, abstract
27. can
28. one (a single), diamond
29. implements, a concrete definition (implementation)
30. less than
31. implement, Comparable

## Algorithms and recursion
32. deterministic
33. -1
34. O(n), O(sqrt n), O(log2 n)
35. base, recursive
36. smaller
37. stack
38. StackOverflowError (stack overflow)
39. 3 2 1 1 2 3 (3, 2, 1 on the way down; base case at n = 0 prints nothing; then 1, 2, 3 on the way up)
40. `TOH(n-1, start, temp, goal); move(start, goal); TOH(n-1, temp, goal, start);`
41. A --> B, A --> C, B --> C
42. iterative

## Analysis of algorithms
43. basic steps
44. one (1) more
45. O(1), O(n)
46. 1, log n, n, n log n, n^2, 2^n, n!
47. O(n^3)
48. True. False.
49. positive
50. O(n), O(n^2), O(log2 n)
51. input, mathematical notation

## Arrays and binary search
52. constant, O(1), fixed
53. idx, a[i-1]
54. i-1, i
55. 0, n, n-1 (the last position), 1. (O(n) worst, O(1) best)
56. sorted (increasing order), log2 n
57. low, high
58. Call 1: low=0, high=6, mid=3, A[3]=7, 5<7 so high=2. Call 2: low=0, high=2, mid=1, A[1]=3, 5>3 so low=2. Call 3: low=2, high=2, mid=2, A[2]=5, found, return 2.
59. cuts (halves) the remaining range

## Explain in one sentence
60. private means only members of the same class can access it, and Manager is a different class from Employee, so it must go through the public method.
61. printUp prints after its recursive call so it prints on the way back up the stack, while countdown prints before its recursive call so it prints on the way down.
62. Only the rate of growth matters for large n, and the leading term dominates the rest while constant factors don't change how fast the running time grows.
