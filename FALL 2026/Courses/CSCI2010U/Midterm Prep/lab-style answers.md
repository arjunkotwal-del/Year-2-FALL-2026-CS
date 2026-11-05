# Lab-style answers (open only after attempting)

## Lesson 1
**1.1**
```java
public static int countBelow(int[] a, int limit) {
    int count = 0;
    for (int i = 0; i < a.length; i++) {
        if (a[i] < limit) {
            count++;
        }
    }
    return count;
}
```
**1.2**
```java
public static int maxOf(int[] a) {
    int best = a[0];
    for (int i = 1; i < a.length; i++) {
        if (a[i] > best) best = a[i];
    }
    return best;
}
```
**1.3** `{3, 8, 3, 1}`, counting `>= 3`: after 3 -> 1, after 8 -> 2, after 3 -> 3, after 1 -> 3. Final answer 3.

**1.4** On the last pass `i == a.length`, which is one past the last valid index, so `a[i]` throws `ArrayIndexOutOfBoundsException`. The last valid index is `a.length - 1`, so use `i < a.length`.

**1.5** `javac Foo.java` compiles the source into bytecode, producing `Foo.class`. `java Foo` starts the JVM and runs the `main` method in `Foo.class`.

## Lesson 2
**2.1** `super(balance);`, `this.rate = rate;`, `super.deposit(amount + amount * rate);`

**2.2** `balance` is private in `Account`, so `BonusAccount` can't access it (compile error, "field is not visible"). `deposit(...)` without `super.` calls `BonusAccount.deposit` itself, which calls itself forever, giving a `StackOverflowError`.

**2.3** `110.0` then `115.0`. The plain account gets 10. The bonus account gets 10 + 10 * 0.5 = 15 added to 100.

**2.4** The reference type is `Account` for both, but the object type differs. Java uses each object's own `deposit` (dynamic method dispatch, named in lecture but not explained in depth).

**2.5**
```java
for (Account a : list) a.deposit(5);
```

## Lesson 3
**3.1**
```java
public class Rect extends Shape {
    private double w, h;
    public Rect(double w, double h) { this.w = w; this.h = h; }
    @Override public double area() { return w * h; }
}
```
**3.2**
```java
public class Rect extends Shape implements Comparable<Rect> {
    ...
    @Override public int compareTo(Rect other) {
        return Double.compare(area(), other.area());
    }
}
```
**3.3** `new Shape()` does not compile because `Shape` is abstract and can't be instantiated. `new Circle(2)` compiles because Circle is concrete and a Circle is a Shape, so a Shape reference can hold it.

**3.4** Compile error: `Rect` is not abstract and does not override the abstract method `area()`.

**3.5** `Arrays.sort(rs);`. `Rect` must implement `Comparable<Rect>` with a `compareTo` method.

**3.6**
```java
@Override public int compareTo(Person other) {
    return this.name.compareTo(other.name);   // or getName() if the field is private in a superclass
}
```
It returns a negative number if this name comes before the other.

## Lesson 4
**4.1** a)
```java
static int countDigits(int n) {
    int count = 1;
    while (n >= 10) { n = n / 10; count++; }
    return count;
}
```
b)
```java
static int countDigits(int n) {
    if (n < 10) return 1;            // base case
    return 1 + countDigits(n / 10);  // smaller number
}
```
**4.2**
```java
static int sumTo(int n) {
    if (n == 0) return 0;
    return n + sumTo(n - 1);
}
```
Trace: `sumTo(3)` -> `3 + sumTo(2)` -> `2 + sumTo(1)` -> `1 + sumTo(0)` -> `sumTo(0)` returns 0, then `sumTo(1)` returns 1, `sumTo(2)` returns 3, `sumTo(3)` returns 6.

**4.3**
```java
static int power(int base, int exp) {
    if (exp == 0) return 1;
    return base * power(base, exp - 1);
}
```
`power(2, 4)` = 2*2*2*2*1 = 16.

**4.4**
```java
static boolean allSame(String s) {
    if (s.length() <= 1) return true;
    if (s.charAt(0) != s.charAt(1)) return false;
    return allSame(s.substring(1));
}
```
**4.5** `g(4)` = 2 * g(3) = 2 * 2 * g(2) = ... = 2*2*2*2*g(0) = 16. Calls: g(4), g(3), g(2), g(1), g(0), so 5 calls. Returns unwind: g(0)=1, g(1)=2, g(2)=4, g(3)=8, g(4)=16.

**4.6** The loop `while (n >= 10)` stops when n < 10, and the recursive base case `n < 10` is the same condition, where the answer is 1 digit.

**4.7** `"hello".substring(1)` returns `"ello"`. `"hello".substring(1, 3)` returns `"el"` (start included, end excluded). `"hello".charAt(0)` returns `'h'`.

## Lesson 5
**5.1** a) O(n)  b) O(n^2)  c) O(n^2) (inner loop bounded by the outer loop variable, about n^2/2)  d) O(log n)  e) O(1)  f) O(n) (two separate loops add: n + n = 2n, which drops to O(n)).

**5.2** The header test runs `n + 1` times, the body runs `n` times.

**5.3** O(n^2). For large n the 6n^2 term dominates, and the constant 6 doesn't change how fast the running time grows with n, only a scale factor, so it is dropped.

**5.4** a) True  b) False  c) True  d) False  e) True.

**5.5** Pairs: first element pairs with n-1 others, second with n-2, ... so (n-1) + (n-2) + ... + 1 = n(n-1)/2. That is (n^2 - n)/2, whose leading term is n^2/2. Dropping the constant 1/2 and the lower term -n/2 gives O(n^2), the same as n * n.

**5.6** 100n vs n^2: equal at n = 100. For n < 100, n^2 is smaller (faster). For n > 100, 100n is faster. For large n the linear algorithm is better: 100n is O(n) and n^2 is O(n^2).

**5.7** Best case: value at the first index, O(1). Worst case: value last or missing, O(n). We focus on worst case because it is an upper bound guarantee (the algorithm can never take longer) and because it happens often (e.g. searching for a value that isn't there).

## Mixed
**6.1** `super(name)` is the call in a subclass constructor that runs the superclass constructor to initialise its private state, and must be the first statement. `super.increment()` is a call from inside an overriding method to the superclass's version of that method.

**6.2** A loop keeps going until its condition fails, and a recursive method keeps calling itself until the base case is true. The base case is the same condition as the loop's stopping condition, and each step must move toward it.

**6.3** `Arrays.sort` calls `compareTo` on the elements. A class that implements `Comparable<T>` has to supply `compareTo`, so the sort has a rule for which element comes first.

**6.4** A concrete class can be instantiated, and an object with an unimplemented abstract method would have a method with no body to run. So every abstract method must be implemented before the class can be concrete.
