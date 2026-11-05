# Lab-style code practice (new problems, same skills as Labs 1-5)

Do these on paper, closed notes. Write the code, then check in `lab-style answers.md`. Lesson order matches `Labs/lab map.md`.

## Lesson 1: counting loops over arrays (Lab 1)
**1.1** Complete the method. It returns how many elements are strictly less than `limit`. Example: `{5, 2, 9, 2}` with limit 5 returns 2.
```java
public static int countBelow(int[] a, int limit) {
    ____ count = ____;
    for (int i = ____; i < ____; i++) {
        if (a[i] ____ limit) {
            count____;
        }
    }
    return ____;
}
```
**1.2** Write `public static int maxOf(int[] a)` that returns the largest element. Assume the array has at least one element. Do not sort it.

**1.3** For `{3, 8, 3, 1}` and a method that counts elements `>= 3`, write the value of `count` after each element. Final answer?

**1.4** A student wrote `for (int i = 0; i <= a.length; i++)`. What happens when it runs and why?

**1.5** What do `javac Foo.java` and `java Foo` each do? Which file does each one produce or use?

## Lesson 2: inheritance and polymorphism (Lab 2)
Given:
```java
public class Account {
    private double balance;
    public Account(double balance) { this.balance = balance; }
    public double getBalance() { return balance; }
    public void deposit(double amount) { balance += amount; }
}
```
**2.1** Complete the subclass. A `BonusAccount` adds a bonus of `amount * rate` on every deposit.
```java
public class BonusAccount extends Account {
    private double rate;
    public BonusAccount(double balance, double rate) {
        ____(balance);
        this.rate = ____;
    }
    @Override
    public void deposit(double amount) {
        ____.deposit(amount + amount * rate);
    }
}
```
**2.2** In `BonusAccount.deposit`, why can't you write `balance += amount + amount * rate;`? Why would `deposit(amount + amount * rate);` (no `super.`) be wrong, and what error would you get?

**2.3** Predict the output:
```java
Account[] list = { new Account(100), new BonusAccount(100, 0.5) };
for (Account a : list) a.deposit(10);
for (Account a : list) System.out.println(a.getBalance());
```
**2.4** Why do both accounts print different results when `deposit(10)` is called through the same `Account` reference type?

**2.5** Write one loop that calls `deposit(5)` on every `Account` in an `Account[] list`, with no casts and no `instanceof`.

## Lesson 3: abstract classes and interfaces (Lab 3)
```java
public abstract class Shape {
    public abstract double area();
}
public class Circle extends Shape {
    private double r;
    public Circle(double r) { this.r = r; }
    @Override public double area() { return 3.14 * r * r; }
}
```
**3.1** Write `Rect extends Shape` with fields `w` and `h`, a constructor, and `area()`.

**3.2** Make `Rect` comparable by area, smallest first. Write the class header and the method. Use `Double.compare`.

**3.3** Will `Shape s = new Shape();` compile? Will `Shape s = new Circle(2);` compile? Why?

**3.4** What happens if `Rect` does not implement `area()` and is not declared abstract?

**3.5** Given an array `Rect[] rs` of three Rect objects, which single line sorts them by area? What must be true of `Rect` for that line to work?

**3.6** Employee-style: write `compareTo` that orders people by `name` (a `String`) using `String.compareTo`. What does it return if this name comes before the other?

## Lesson 4: recursion (Lab 4)
**4.1** Write `countDigits(int n)` two ways, for `n >= 0`, where 0 has 1 digit. Examples: 7 returns 1, 4082 returns 4.
a) with a loop, b) recursively.

**4.2** Write `static int sumTo(int n)` recursively, returning 1 + 2 + ... + n, with `sumTo(0)` returning 0. Trace `sumTo(3)` showing each call.

**4.3** Write `static int power(int base, int exp)` recursively for `exp >= 0`. Base case first. Example: `power(2, 4)` returns 16.

**4.4** Write `static boolean allSame(String s)` recursively: true if every character in `s` is the same. The empty string and one-letter strings are true. Use `charAt` and `substring(1)`.

**4.5** Trace and give the result:
```java
static int g(int n) {
    if (n == 0) return 1;
    return 2 * g(n - 1);
}
```
`g(4)` = ? Show every call, and say how many calls were made.

**4.6** For `4.1a` (loop) and `4.1b` (recursion), name the loop stopping condition and the matching base case.

**4.7** What does `"hello".substring(1)` return? What does `"hello".substring(1, 3)` return? What does `"hello".charAt(0)` return?

## Lesson 5: analysis of algorithms (Lab 5 concepts, L8, L9)
**5.1** Give the Big-O of each snippet (n = array length):
a) `for (int i = 0; i < n; i++) sum += a[i];`
b) `for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) count++;`
c) `for (int i = 0; i < n; i++) for (int j = 0; j < i; j++) count++;`
d) `int i = n; while (i > 1) { i = i / 2; }`
e) `return a[0];`
f) `for (int i = 0; i < n; i++) x++;  for (int j = 0; j < n; j++) y++;` (two loops one after the other)

**5.2** A `for (int i = 0; i < n; i++)` loop is run to completion. How many times is the header (the test `i < n`) evaluated? How many times does the body run?

**5.3** `T(n) = 6n^2 + 30n + 11`. What is its Big-O? Which term dominates once n is large, and why do we drop the constant 6?

**5.4** True or false: a) `5n + 20 = O(n)`  b) `n^2 = O(n)`  c) `n = O(n^2)`  d) `2^n = O(n^3)`  e) `n log n = O(n^2)`.

**5.5** Why does comparing every pair of n elements take about n(n-1)/2 comparisons, and what is that in Big-O? Why is the Big-O the same as for n * n comparisons?

**5.6** Two algorithms solve the same problem. One takes 100n steps, the other takes n^2 steps. For which input sizes is n^2 faster? Which is better for large n, and which Big-O does each have?

**5.7** Best case and worst case of linear search, each with its Big-O. Which one do we focus on in this course, and give two reasons.

## Mixed: explain in one or two sentences, as you would to the TA
**6.1** What is the difference between `super(name)` and `super.increment()`?
**6.2** How does a loop's stopping condition relate to a recursive base case?
**6.3** How does implementing `Comparable` give `Arrays.sort` something to compare with?
**6.4** Why must a concrete class implement every abstract method?
