# Midterm practice: fill in the blank (L1-L10)

The professor said the exam questions will look like the lab ones, with fill in the blank. Do this closed notes and closed cheat sheet, on paper, timed (40 minutes for the full set). Write answers on paper first. Answers are in `practice answers.md`. Do not open it until you have finished the whole set.

## Bubble sort and Java (L1, L2)
1. Bubble sort compares ________ elements and swaps them if they are out of order.
2. After one pass, the ________ value in the unsorted part is at its final position at the right end.
3. Fill in: `for (int i = A.length - 1; i ____ 0; i--) { for (int j = 0; j ____ i; j++) { if (A[j+1] ____ A[j]) swap(A, j, j+1); } }`
4. An array has 6 elements. Pass 1 makes ____ comparisons, pass 2 makes ____, and the whole sort makes ____ passes.
5. In bubble sort, the variable that stays fixed during a pass is ____, and the one that moves after every comparison is ____.
6. Trace one pass of bubble sort on [6, 2, 5, 1]. Array after the pass: ________.
7. To sort in descending order, change `<` to ________.
8. A swap method needs a ________ variable, otherwise the first assignment overwrites a value that was never saved.
9. A method that sorts an array in place does not need to return it because arrays are ________ types, so the method gets a copy of the ________ to the same array.
10. In the L2 timing experiment, when n grew by 10, the time grew by about ________.

## Objects, inheritance, polymorphism (L3, L4)
11. The three characteristics of an object are ________, ________ and ________.
12. When finding classes in a problem description, nouns become ________ and verbs become ________.
13. A subclass is created with the keyword ________. The test used to check it is the "________" relationship.
14. A private field in a superclass ________ (is / is not) visible in the subclass, so the subclass must call a public ________ method.
15. The annotation placed above a method that redefines a superclass method is ________. To call the superclass's version, write ________.getSalary().
16. Inside `Manager.getSalary()`, the statement `return getSalary() + bonus;` causes a ________ error because the method calls itself forever.
17. In a subclass constructor, the call to `super(...)` must be the ________ statement.
18. Which line compiles? (a) `Employee e = new Manager(1, "x");` (b) `Manager m = new Employee(1, "x");` Answer: ____
19. `Employee[] staff = {employeeObj, managerObj}; staff[1].getSalary()` runs the ________ class's version of getSalary.
20. A reference variable holds the ________ of an object. The object itself is allocated on the ________.
21. Given `Employee workerBee = new Employee(...)`, the call `workerBee.setBonus(5)` fails because ________.

## Packages, abstract classes, interfaces (L5)
22. A package statement must be the ________ statement in the file. Classes with no package statement go in the ________ package.
23. Of these, ________ is imported automatically: java.util, java.lang, java.io.
24. A `protected` member is accessible from a different package only by ________.
25. A member with no modifier is accessible from a subclass in a different package: ________ (Yes / No).
26. An abstract class ________ (can / cannot) be instantiated, a constructor ________ (can / cannot) be abstract, and a subclass must implement all abstract methods or be declared ________.
27. An abstract class ________ (can / cannot) have a static method.
28. Java allows a class to extend only ________ class because of the ________ problem.
29. A class that uses an interface says ________ in its header and must write ________ for every method in it.
30. `compareTo` returns a negative number when the current object is ________ the argument.
31. To use `Arrays.sort()` on an array of Employee objects, Employee must ________ the ________ interface.

## Algorithms and recursion (L6, L7)
32. An algorithm is finite, ________, effective, and sufficiently abstract to be coded in any language.
33. Linear search returns ________ when the value is not found.
34. PerfectSquare v0 is O(____), v1 is O(____), v2 is O(____).
35. Every recursive method needs a ________ case and a ________ case.
36. The recursive case must work on a ________ subproblem.
37. Recursive calls are stored on the ________.
38. A recursive method with no base case ends with a ________ error.
39. `static void mystery(int n){ if(n==0) return; System.out.println(n); mystery(n-1); System.out.println(n); }` Output of `mystery(3)`: ________.
40. Complete: `TOH(n-1, start, ____, ____); move(start, goal); TOH(n-1, ____, goal, ____);`
41. Moves printed by `TOH(2, A, C, B)`, in order: ________.
42. The default choice should be a(n) ________ solution unless the problem is naturally recursive.

## Analysis of algorithms (L8, L9)
43. In running-time analysis, T(n) counts the number of ________.
44. A for loop header is executed ________ time(s) more than its body.
45. Best-case linear search is O(____). Worst-case is O(____).
46. Order from slowest growing to fastest growing: 2^n, n, log n, n^2, 1, n log n, n!  Answer: ________
47. 5n^3 + 40n + 9 is O(____).
48. True or false: 3n + 4 = O(n^2). ________   True or false: n^2 = O(n). ________
49. In the definition f(n) <= c*g(n) for all n >= n0, the constants c and n0 must be ________ (positive / zero allowed).
50. A single loop from 0 to n is O(____). A loop nested inside it over the same range is O(____). A loop that halves its counter each step is O(____).
51. "Worst case" is the type of ________ given to the algorithm. "Big-O" is a ________.

## Arrays and binary search (L10)
52. Reading `A[i]` takes ________ time. An array's length is ________ once it is created.
53. Complete the insertion loop: `for (int i = a.length-1; i > ____; i--) a[i] = ________;  a[idx] = val;`
54. Complete the deletion loop: `for (int i = idx+1; i < a.length; i++) a[____] = a[____];`
55. Worst case for insert and delete is at idx = ____ and costs O(____). Best case is idx = ____ and costs O(____).
56. Binary search requires the array to be ________. Its worst-case complexity is O(____).
57. Binary search base case: if ____ > ____, return NOT_FOUND.
58. Trace binary search for val = 5 in [1, 3, 5, 7, 9, 11, 13]. List low, high, mid for each call: ________.
59. Why is O(log2 n) the worst case? Each comparison either finds the value or ________ the remaining range.

## Mixed: explain in one sentence each
60. Why can't a Manager read Employee's private field `salary` directly?
61. Why does `printUp(3)` print 1 2 3 but `countdown(3)` print 3 2 1 0?
62. Why do we drop constants and lower-order terms in Big-O?
