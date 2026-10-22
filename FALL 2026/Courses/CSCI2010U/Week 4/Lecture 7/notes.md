# Lecture 7 — Recursion

> Sourced from L07_recursion.pdf (32 slides, Canvas course 202609 - Data Structures - 40241). No transcript. Sections marked "Supplementary" are my additions for practice and are not on the slides.

## Outline
1. Boxes upon boxes
2. Recursion
3. Towers of Hanoi

## 1. Boxes upon boxes

**Problem**: you have moved into a new flat and are looking for your phone charger. A friend says it is in the large box. That box is packed with more boxes, which contain yet more boxes.

### First approach: iterative, with an explicit pile
```
Algorithm: ChargerSearch_v1(main_box)
1:  pile = main_box.makePile()
2:  while pile != empty
3:      box = pile.takeABox()
4:      for item in box
5:          if item == box
6:              pile.add(box)
7:          else if item == charger
8:              Set charger aside
9:          end
10:     end
11: end
```
You keep the bookkeeping yourself: a pile of boxes still to open, a loop over the pile, and a loop over the contents of each box.

### Second approach: recursive
```
Algorithm: ChargerSearch_v2(box)
1:  for item in box
2:      if item == charger
3:          Set charger aside
4:      else if item == box
5:          ChargerSearch_v2(box)
6:      end
7:  end
```
Line 5 is a **recursive method call**: the method calls itself.

Note on the slide: line 5 as written passes `box`, but the intent is to pass the nested box (the `item`). Passing the same box again would loop forever.

**Why v2 is nicer**: there is no pile. The call stack keeps track of which boxes you are partway through, and you never write that bookkeeping yourself. A box with no nested boxes is the point where the search stops going deeper.

## 2. Recursion

### Definition
> "To understand recursion, one must first understand recursion."

- **Recursion** is the process of defining something in terms of itself.
- Procedurally: a procedure is recursive when one of its steps invokes the procedure itself.
- Slide example, "How to make homemade yogurt": add warmed milk to a small amount of homemade yogurt, incubate, cool and eat. It is defined in terms of itself, and it only works if you already have a starter, which is the basic case.

### When does it end?
Recursion must avoid circularity, which in programming means infinite loops (non-termination).

A **string** is either:
- empty, or
- a character followed by another string.

The definition uses "string" inside itself, yet it is not circular because of the basic, non-recursive case (the empty string).

### Recursively defined objects
A general recursive definition says an object is either:
- a certain **basic object** (the non-recursive case), or
- **formed from simpler objects by certain rules** (the recursive case).

Recursive objects are common data structures. A simple list:
```java
class List {
    int value;
    List next;
}
```
Each `List` holds a value and another `List`. (Lists are covered in L10–12.)

### Recursive methods
A recursive method is a method that calls itself. It must contain two elements:
- **Base case**: a conditional statement, placed as the first statement in the algorithm, that has a `return`. It guarantees the algorithm terminates.
- **Recursive case(s)**: the method calls itself. It must address a **smaller** subproblem, so the recursive calls converge to the base case.

### Countdown
```
Algorithm: Countdown(i)
1:  print i
2:  if i <= 0
3:      return          // Base case
4:  else
5:      Countdown(i-1)  // Recursive case
6:  end
```
Java:
```java
public class Countdown {
    public static void main(String[] args) {
        countdown(3);
    }

    public static void countdown(int i) {
        System.out.println(i);
        if (i <= 0)
            return;              // Base case
        else
            countdown(--i);      // Recursive case
    }
}
```
Output:
```
3
2
1
0
```
`--i` decrements `i` first and then passes the new value, so the call is `countdown(i - 1)`.

### How does it work? The call stack
- Method calls get added to a **stack** (stacks are covered in L14).
- When a method calls another method (or itself), its state is stored, its execution is suspended, and the new method begins.
- When a `return` is reached, that method is removed from the stack and the returned value (if any) goes back to its caller. The caller resumes right after the line that made the call.
- There is some overhead in doing this.

### Solving problems with recursion
1. Begin by writing the **base case**.
2. Think about solving the problem by combining the results of **smaller but similar** subproblems.
3. Do not worry about how the recursive call solves its subproblem. Accept that it will solve it correctly, then use that result to solve the original problem.
4. Do not go down the rabbit hole of analysing the recursive process beyond the recursive call. Focus on the base case and on recombining the results.

## 3. Towers of Hanoi (TOH)

- A puzzle invented by the French mathematician Édouard Lucas in 1883.
- Three rods (A, B, C) and a set of discs of differing sizes.
- Initially all discs are on one rod, in order of size, smallest on top.
- Goal: move them all from the first rod to the third rod, one disc at a time, **never placing a larger disc on top of a smaller one**.
- The original version had 8 discs. The Tower of Brahma has 64.

### Starting small: n = 3
Generalise to n discs. The cases n = 0, 1, 2 are trivial, so start with n = 3.
1. Move the top n-1 discs (the two smallest) from A to B.
2. Move the largest disc, disc n, from A to C.
3. Move the n-1 discs from B to C.

Steps 1 and 3 each shrink the problem by one disc. Eventually you reach a base case with no discs (n = 0). That is recursion.

### Algorithm
```
Algorithm: TOH(n, start, goal, temp)
1:  if n == 0
2:      return                      // Base case
3:  end
4:  TOH(n-1, start, temp, goal)     // Recursive call: n-1 discs
5:  move(start, goal)               // Move disc
6:  TOH(n-1, temp, goal, start)     // Recursive call: n-1 discs
```
Java:
```java
public static void main(String[] args) {
    TOH(Integer.parseInt(args[0]), "A", "C", "B");
}

public static void TOH(int n, String start, String goal, String temp) {
    if (n == 0)
        return;                                       // Base case
    TOH(n-1, start, temp, goal);                      // Recursive call: n-1 discs
    System.out.println(start + " --> " + goal);       // Move disc
    TOH(n-1, temp, goal, start);                      // Recursive call: n-1 discs
}
```
- Moves are printed to the console, since there are no disc objects.
- Parameter order is `(n, start, goal, temp)`. The initial call is `TOH(n, "A", "C", "B")`.
- In the first recursive call the roles of `goal` and `temp` swap. In the second call, `start` and `temp` swap.

## Recursion vs iteration
- Every problem that can be solved recursively can also be solved iteratively (at worst by representing the call stack explicitly).
- If a problem, solution, or data structure is naturally described recursively, the recursive version is likely simpler and more likely to be correct.
- The default should be an iterative solution unless the problem is naturally cast recursively.
- TOH should be done recursively. Calculating factorials is best done iteratively.

## How to hand-trace a recursive method (Supplementary)
1. Write the first call with its argument values.
2. Every call gets its own **frame** with its own parameter values. Indent each deeper call one level.
3. Execute lines in order. When you reach a recursive call, pause that frame and open a new one for the call.
4. At a base case, `return`. Close that frame and go back to the frame that made the call.
5. The paused frame resumes at the line **after** the recursive call.
6. Write any output (prints, returned values) in the order it happens.

### Worked example A: output after the recursive call (Supplementary)
```java
static void printUp(int i) {
    if (i <= 0)
        return;
    printUp(i - 1);
    System.out.println(i);
}
```
Trace of `printUp(3)`:
```
printUp(3)                        i=3, not base case, call printUp(2)
    printUp(2)                    i=2, not base case, call printUp(1)
        printUp(1)                i=1, not base case, call printUp(0)
            printUp(0)            i=0, base case, return
        back in printUp(1)        prints 1, returns
    back in printUp(2)            prints 2, returns
back in printUp(3)                prints 3, returns
```
Output:
```
1
2
3
```
Countdown prints before the recursive call, so it prints 3, 2, 1, 0 on the way down. `printUp` prints after the call, so it prints on the way back up. Where the print sits relative to the recursive call decides the output order.

### Worked example B: TOH with n = 2 (Supplementary)
Call: `TOH(2, A, C, B)`, meaning n=2, start=A, goal=C, temp=B.
```
TOH(2, A, C, B)
    TOH(1, A, B, C)                    n=1, start=A, goal=B, temp=C
        TOH(0, A, C, B)                base case, return
        move A --> B
        TOH(0, C, B, A)                base case, return
    move A --> C
    TOH(1, B, C, A)                    n=1, start=B, goal=C, temp=A
        TOH(0, B, A, C)                base case, return
        move B --> C
        TOH(0, A, C, B)                base case, return
```
Moves, in order:
```
A --> B
A --> C
B --> C
```
That is the smaller disc to B, the larger disc to C, then the smaller disc onto C. The problem in the at-home challenge (n = 3) follows the same pattern one level deeper. See questions.md.

How the arguments were computed in the first recursive call of `TOH(2, A, C, B)`: the line is `TOH(n-1, start, temp, goal)`, so it becomes `TOH(1, A, B, C)`. The second recursive call in the same frame, `TOH(n-1, temp, goal, start)`, becomes `TOH(1, B, C, A)`.
