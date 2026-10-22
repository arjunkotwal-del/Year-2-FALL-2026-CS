# Lecture 7 — Practice Questions

Do these in order. For every trace, use the frame method from notes.md: one indented line per call, with its parameter values, and mark where each frame pauses and resumes. Attempt each one on paper before pasting your answer here for checking.

## Q1. Trace output before and after the call
```java
static void mystery1(int n) {
    if (n == 0)
        return;
    System.out.println(n);
    mystery1(n - 1);
    System.out.println(n);
}
```
Trace `mystery1(3)` frame by frame. Write the full output, in order, and mark which lines were printed on the way down and which on the way back up.

## Q2. Find the bug
Each method is supposed to terminate. For each one, say what happens when it is called and why, then fix it.
```java
static int sum(int n) {
    return n + sum(n - 1);
}

static void bad(int n) {
    if (n == 0)
        return;
    bad(n + 1);
}
```
Call `sum(3)` and `bad(3)`. Name the specific rule from the lecture that each one breaks. Which exception does Java report?

## Q3. Write a recursive method
Write `static int sum(int n)` that returns 1 + 2 + ... + n, recursively. Start by writing the base case, then the recursive case, as the lecture says. Trace `sum(4)`. Self-check: it should return 10.

## Q4. At-home challenge from the lecture: TOH with n = 3
Using `n = 3`, trace out TOH's method calls, including parameter values, showing when each move happens and when each base case is reached. Start from `TOH(3, A, C, B)` and use the frame layout from Worked example B in notes.md.

Self-check before you paste it: you should find **7 moves** and **8 base-case calls** (n = 0). Then physically move three coins or pieces of paper between three spots following your list of moves and confirm no larger piece ever sits on a smaller one.

## Q5. Base case and recursive case
For each of Countdown, `printUp`, and TOH, state:
a) the base case
b) the recursive case
c) what gets smaller on every recursive call

## Q6. Recursively defined objects
The lecture defines a string as either empty, or a character followed by another string. Using the same style, write a definition of a **list of integers**. Which part is the basic case and which part is the recursive case? Compare it to the `class List { int value; List next; }` slide.

## Q7. Recursion vs iteration
a) The lecture says every recursive solution can be written iteratively. What is the worst-case way of doing that?
b) The lecture says TOH should be recursive but factorial should be iterative. Give the reason for each.
c) What should the default choice be, and when do you switch?

## Q8. Stack behaviour
Describe, in your own words, what happens to the call stack during `countdown(3)`:
a) how many frames exist at the deepest point
b) what happens to each frame when `countdown(0)` returns
c) why `countdown` has no work left to do after its recursive call returns, and how that differs from `printUp`

## Q9. Stretch: exam-style
```java
static int f(int n) {
    if (n <= 1)
        return 1;
    return f(n - 1) + f(n - 2);
}
```
Trace `f(4)` and give the returned value. Count how many calls to `f` are made in total, including `f(4)` itself. This is the kind of call-tree question that connects to Big-O in L8–L9.
