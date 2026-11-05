import html, sys

def esc(s): return html.escape(s, quote=False)
def H(t): return f'<h2>{esc(t)}</h2>'
def H3(t): return f'<h3>{t}</h3>'
def P(t): return f'<p>{t}</p>'
def C(t): return '<pre>' + esc(t.strip('\n')) + '</pre>'
def L(items): return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def T(rows, cls=''):
    out = f'<table class="{cls}">'
    for k, r in enumerate(rows):
        tag = 'th' if k == 0 else 'td'
        out += '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in r) + '</tr>'
    return out + '</table>'
def K(s): return '<code>' + esc(s) + '</code>'

# =============================================================== SIDE A
A1 = [
H('HOW TO ANSWER'),
L([
 '<b>Print / return?</b> Make a table: one row per pass or call, one column per variable. Run it line by line.',
 '<b>Fill a blank:</b> copy the matching template; check start, stop test, step, names.',
 '<b>Write a method:</b> 1) what to return, 2) a variable (count / sum / min), 3) loop or recursion, 4) return AFTER the loop. Test it on the example.',
]),
H('JAVA ESSENTIALS'),
L([
 'Array: index from <b>0</b>; <code>a.length</code> (no brackets); last = <code>a[a.length-1]</code>; <code>a[a.length]</code> crashes. <code>int[] a = new int[5];</code> (all 0) or <code>{5,2,9}</code>. Size is fixed.',
 'String: <code>s.length()</code>, <code>s.charAt(i)</code>, <code>s.substring(1)</code> ("hello" gives "ello"), <code>s.substring(1,3)</code> ("el", end not included), <code>s1.compareTo(s2)</code> (negative = s1 first). Case matters.',
 '<code>n%10</code> = last digit, <code>n/10</code> drops it (5072: 2 and 507). <code>i % k == 0</code> = divisible by k. 7 / 2 = 3, 7 % 2 = 1. <code>==</code> compares, <code>=</code> assigns.',
 'Defaults: int 0, boolean false, objects null. An int method returns a number (or throws), never null.',
 'Arrays and objects pass a reference copy, so a method changes the SAME array (no return needed). Primitives pass a copy.',
 'A <code>static</code> method cannot use instance fields or <code>this</code>. Strings are not arrays: <code>s[i]</code> fails; <code>+=</code> works on Strings, not arrays.',
 '<code>javac F.java</code> makes F.class; <code>java F</code> runs <code>public static void main(String[] args)</code>.',
]),
H('COUNT, MIN, SUM, MULTIPLES (Lab 1)'),
C('''
int count = 0;                // before loop
for (int i = 0; i < a.length; i++) {
  if (a[i] >= target) {   // equal counts
    count++;
  }
}
return count;                 // after loop
'''),
P('countAtLeast({25,10,40,25}, 25): yes, no, yes, yes = <b>3</b>. Count above 4 in {5,2,9,2}: yes, no, yes, no = <b>2</b>.'),
C('''
int min = a[0];               // not 0
for (int i = 1; i < a.length; i++) {
  if (a[i] < min) {
    min = a[i];
  }
}
int sum = 0;
for (int i = 0; i < a.length; i++) {
  sum += a[i];
}
for (int i = start; i <= end; i++) {
  if (i % mult == 0) {        // multiples
    System.out.println(i);
  }
}
'''),
H('REVERSE'),
C('''
void reverseArray(int[] a) {  // in place
  int l = 0;
  int r = a.length - 1;
  while (l < r) {
    int t = a[l];
    a[l] = a[r];
    a[r] = t;
    l++;
    r--;
  }
}                  // {1,2,3,4} -> 4 3 2 1
String reverse(String s) {
  String out = "";
  for (int i = s.length() - 1; i >= 0; i--) {
    out += s.charAt(i);
  }
  return out;                 // "abc" -> "cba"
}
'''),
H('ORDER THE STEPS'),
C('''
insert: check range -> i = a.length-1
  -> while i > idx: a[i] = a[i-1], i--
  -> a[idx] = val
binary search: low > high return NOT_FOUND
  -> mid -> equal? return mid -> recurse a half
TOH: n == 0 return -> TOH(n-1,start,temp,goal)
  -> print move -> TOH(n-1,temp,goal,start)
delete: check range -> i = idx+1
  -> while i < length: a[i-1] = a[i] -> GAP
'''),
]

A2 = [
H('BUBBLE SORT (L1, L2)'),
C('''
for (int i = A.length - 1; i > 0; i--) {
  for (int j = 0; j < i; j++) {
    if (A[j + 1] < A[j]) {
      int temp = A[j];        // swap
      A[j] = A[j + 1];
      A[j + 1] = temp;
    }
  }
}
'''),
P('<code>i</code> is FIXED during a pass; <code>j</code> moves. n elements: n-1 passes. Descending: use <code>A[j+1] &gt; A[j]</code>. After pass k the last k are locked. Worst case O(n^2).'),
T([
 ['start','pass 1','pass 2','pass 3','pass 4'],
 ['4 2 3','2 3 4','2 3 4','',''],
 ['3 1 2','1 2 3','1 2 3','',''],
 ['5 2 4 1','2 4 1 5','2 1 4 5','1 2 4 5',''],
 ['8 1 6 4 9','1 6 4 8 9','1 4 6 8 9','1 4 6 8 9','1 4 6 8 9'],
]),
T([
 ['n','i starts','passes','pass 1 compares','j max'],
 ['4','3','3','3','2'],
 ['5','4','4','4','3'],
 ['6','5','5','5','4'],
]),
P('Compares: 4+3+2+1 = 10 for 5 elements, n(n-1)/2. Sorted {1,2,3}: 3 compares, 0 swaps. Reversed {3,2,1}: 3 compares, 3 swaps.'),
H('SEARCHING (L6, L10)'),
C('''
for (int i = 0; i < A.length; i++) {
  if (A[i] == val) {
    return i;
  }
}
return -1;       // best O(1), worst O(n)
'''),
H3('Binary search: array must be SORTED'),
C('''
bs(a, val, low, high):
  if (low > high) return NOT_FOUND;
  int mid = (low + high) / 2;
  if (val == a[mid]) return mid;
  else if (val < a[mid])
    return bs(a, val, low, mid - 1);
  else
    return bs(a, val, mid + 1, high);
// start bs(a, val, 0, a.length - 1)  O(log n)
'''),
P('a = {1,3,5,7,9,11,13}. Each step: low, high, mid = a[mid].'),
T([
 ['find','steps','result'],
 ['11','0,6,3=7 go right; 4,6,5=11','5'],
 ['3','0,6,3=7 go left; 0,2,1=3','1'],
 ['5','0,6,3=7; 0,2,1=3; 2,2,2=5','2'],
 ['4','0,6,3=7; 0,2,1=3; 2,2,2=5, high=1','NOT_FOUND'],
]),
H('ARRAY INSERT / DELETE (L10)'),
C('''
insert(a, idx, val):
  for (int i = a.length - 1; i > idx; i--) {
    a[i] = a[i - 1];          // shift RIGHT
  }
  a[idx] = val;               // last falls off
delete(a, idx):
  for (int i = idx + 1; i < a.length; i++) {
    a[i - 1] = a[i];          // shift LEFT
  }
  a[a.length - 1] = GAP;
'''),
T([
 ['example','steps'],
 ['insert 50 at 1 in 4 6 8 10','4 6 8 8; 4 6 6 8; 4 50 6 8 (2 shifts)'],
 ['delete idx 1 in 5 6 7 8','5 7 7 8; 5 7 8 8; 5 7 8 GAP (2 shifts)'],
]),
P('Worst idx = 0 gives O(n); best idx = last gives O(1); a[i] is O(1).'),
H('PERFECT SQUARE (L6, L9)'),
P('v0 <code>while (i &lt;= n)</code> O(n). v1 <code>while (i*i &lt;= n)</code> O(sqrt n). v2 doubles i, then binary search: O(log n).'),
T([
 ['n','v0 loops','v1 loops','answer'],
 ['10','10','3 (i=1,2,3)','No'],
 ['20','20','4 (i=1..4)','No'],
 ['16','4','4','Yes'],
]),
H('MORE WHOLE METHODS'),
C('''
boolean isSorted(int[] a) {
  for (int i = 1; i < a.length; i++)
    if (a[i - 1] > a[i]) return false;
  return true;    // empty or 1 element: true
}
int countDivisible(int lo, int hi, int k) {
  int count = 0;
  for (int i = lo; i <= hi; i++)
    if (i % k == 0) count++;
  return count;   // (1, 11, 3) = 3
}
'''),
]

A3 = [
H('RECURSION (L7, Lab 4)'),
L([
 'Needs a <b>base case</b> (smallest problem, returns) and a <b>recursive case</b> (calls itself on a SMALLER problem). No base case = StackOverflowError.',
 'Trace: go DOWN (calls wait), then back UP using the value from below. <code>sumTo(2)</code> means the SUM 1+2 = 3, not the number 2. Countdown n..0 = n+1 calls.',
 'Print BEFORE the call = going down (3,2,1). Print AFTER = coming up (1,2,3).',
]),
C('''
int sumTo(int n) {
  if (n == 0) return 0;
  return n + sumTo(n - 1);
}            // (0)=0 (1)=1 (2)=3 (3)=6
void down(int n) {      // down(3): 3 2 1
  if (n == 0) return;
  System.out.println(n);
  down(n - 1);
}
void up(int n) {              // up(3): 1 2 3
  if (n == 0) return;
  up(n - 1);
  System.out.println(n);
}
void test(int n) {   // test(2): A2 A1 B1 B2
  if (n == 0) return;
  System.out.println("A" + n);
  test(n - 1);
  System.out.println("B" + n);
}
int sumDigits(int n) {
  if (n == 0) return 0;
  return n % 10 + sumDigits(n / 10);
}            // (72) = 2 + (7 + 0) = 9
int countDigits(int n) {
  if (n < 10) return 1;
  return 1 + countDigits(n / 10);
}            // (472) = 1 + (1 + 1) = 3
'''),
C('''
String rev(String s) {
  if (s.length() <= 1) return s;
  return rev(s.substring(1))
         + s.charAt(0);
}   // "abc": rev("bc") + a
    // = (rev("c") + b) + a = "cba"
boolean isPal(String t) {
  int n = t.length();
  if (n <= 1) return true;
  if (t.charAt(0) != t.charAt(n - 1))
    return false;
  return isPal(t.substring(1, n - 1));
}   // "abba": a=a, "bb": b=b, "" true
    // "abca": a=a, "bc": b!=c false (2 calls)
int f(int n) {
  if (n <= 1) return 1;
  return f(n - 1) + f(n - 2);
}   // f(2)=2 f(3)=3 f(4)=5; 9 calls for f(4)
'''),
C('''
TOH(n, start, goal, temp):
  if (n == 0) return;
  TOH(n - 1, start, temp, goal);
  print start --> goal;
  TOH(n - 1, temp, goal, start);
call TOH(n, "A", "C", "B");  moves = 2^n - 1
n=2: A-B A-C B-C
n=3: A-C A-B C-B A-C B-A B-C A-C
'''),
H('WRITE A RECURSIVE METHOD IN 4 STEPS'),
C('''
1 base case: smallest input, return directly
2 one piece of work: n%10, first letter, n
3 call yourself on a SMALLER input:
  n/10, n-1, substring(1)
4 combine: return piece + the call
A loop stop condition = the base case
'''),
H('LOOPS TO BIG-O'),
T([
 ['code','Big-O'],
 ['<code>return a[5];</code>','O(1)'],
 ['one loop <code>i&lt;n</code>','O(n)'],
 ['two loops one after the other','O(n)'],
 ['loop inside loop, both to n','O(n^2)'],
 ['inner <code>j&lt;i</code> inside <code>i&lt;n</code>','O(n^2)'],
 ['<code>while (n&gt;1) n=n/2;</code>','O(log n)'],
 ['<code>for (i=1;i&lt;n;i*=2)</code>','O(log n)'],
 ['inner loop of 5, outer to n','O(n)'],
 ['3 nested loops to n','O(n^3)'],
]),
H('LAB 5: HOW THE WORK GROWS'),
T([
 ['approach','work','Big-O'],
 ['sum each window of k','(n-k+1) x k adds','O(nk)'],
 ['running sum, add new/drop old','2 ops per step','O(n)'],
 ['check every pair i &lt; j','n(n-1)/2 pairs','O(n^2)'],
 ['sorted: index at each end','1 index moves/step','O(n)'],
]),
P('O(1) space = scalars only. Use <b>long</b> for sums.'),
]

# =============================================================== SIDE B
EXPL = [
H('EXPLAIN WHY'),
L([
 '<b>Equal to target counts:</b> "at least" means &gt;=.',
 '<b>super(name) vs super.increment():</b> the first sets the parent\'s private state (first line only); the second calls the parent version of an overridden method.',
 '<b>new Person() fails:</b> abstract, cannot be instantiated, even with a constructor.',
 '<b>Comparable and Arrays.sort:</b> sort calls compareTo to decide the order. implements = many roles; extends = one parent.',
 '<b>Loop stop vs base case:</b> both are the condition where work ends, and every step moves toward it.',
 '<b>Why private fields?</b> Only methods can change state, so the class controls how data is read and changed.',
]),
]

B1 = [
H('INHERITANCE (L3, L4, Lab 2)'),
L([
 '<code>extends</code>. Test "is a": Manager IS AN Employee, never the reverse. A subclass can add and <b>override</b>.',
 '<code>super(...)</code> must be the FIRST line of the constructor (runs the parent constructor).',
 'Parent <code>private</code> fields are not visible in the child: use the getter.',
 'In an override, <code>super.m()</code> = parent version. Plain <code>m()</code> = itself, forever = <b>StackOverflowError</b> (runtime).',
]),
C('''
class Pet {
  private String name;
  public Pet(String name) { this.name = name; }
  public String getName() { return name; }
  public String sound() { return "..."; }
}
class Dog extends Pet {
  private int tricks;
  public Dog(String name, int tricks) {
    super(name);              // first line
    this.tricks = tricks;
  }
  @Override
  public String sound() { return "Woof"; }
  public String describe() {
    return getName() + " knows " + tricks;
  }
}
class LoudDog extends Dog {
  public LoudDog(String n, int t) {
    super(n, t);
  }
  @Override
  public String sound() {
    return super.sound() + "!";
  }
}
// Cat: same pattern, sound() returns "Meow"
Pet[] p = { new Pet("A"), new Dog("B", 1),
            new LoudDog("C", 2) };
for (Pet x : p) {
  System.out.println(x.sound());
}         // prints:  ...   Woof   Woof!
'''),
C('''
class LimitedCounter extends Counter {
  // private int limit;
  public LimitedCounter(String name,
      int limit) {
    super(name);
    this.limit = limit;
  }
  @Override
  public void increment() {
    if (getCount() < limit) {
      super.increment();
    }
  }
}
// Manager: super(salary, name); bonus = 0;
// getSalary: super.getSalary() + bonus
'''),
H('POLYMORPHISM (L4)'),
L([
 'A parent variable can hold a child object. The version that RUNS is the object\'s own class.',
 'Read right to left with "is a". A parent variable cannot call child-only methods.',
 'Making an object: declare a REFERENCE (an address), create the object with <code>new</code> on the <b>HEAP</b>, link them.',
]),
T([
 ['code','result'],
 ['<code>Pet p = new Dog("B",1);</code>','OK (Dog is a Pet)'],
 ['<code>p.sound()</code>','runs Dog: Woof'],
 ['<code>p.describe()</code>','COMPILE error'],
 ['<code>Dog d = new Pet("A");</code>','COMPILE error'],
 ['<code>Pet[] arr</code>','holds Pet, Dog, Cat'],
 ['<code>void feed(Pet x)</code>','accepts any Pet child'],
]),

]

B2 = [
H('COMPILE OR RUNTIME?'),
T([
 ['situation','error'],
 ['override calls itself (no <code>super.</code>)','RUNTIME StackOverflow'],
 ['<code>a[4]</code> on length 4','RUNTIME ArrayIndex...'],
 ['<code>new Shape()</code> (abstract)','COMPILE'],
 ['concrete class missing an abstract method','COMPILE'],
 ['child reads parent private field','COMPILE'],
 ['<code>return null</code> in an int method','COMPILE'],
]),
H('ABSTRACT CLASS (L5, Lab 3)'),
C('''
abstract class Shape {
  public abstract double area();  // no body
}
class Square extends Shape {
  private double s;
  public Square(double s) { this.s = s; }
  @Override
  public double area() { return s * s; }
}
new Shape()                // ERROR (abstract)
Shape b = new Square(2);   // OK
class Triangle extends Shape { }  // ERROR
  // fix: write area() OR abstract class
'''),

L([
 '<b>Cannot instantiate</b> an abstract class, even with a constructor. A constructor can NOT be abstract. Mixes concrete + abstract methods; can have static methods.',
 'A child must write ALL abstract methods or be abstract itself. Non-abstract = <b>concrete</b>.',
]),
H('WRITE A WHOLE CLASS (Roster)'),
C('''
class Roster {
  private String[] names;
  private int size;
  public Roster(int capacity) {
    names = new String[capacity];
    size = 0;
  }
  public void add(String name) {
    if (size == names.length)
      throw new IndexOutOfBoundsException();
    names[size] = name;
    size++;
  }
  public String get(int index) {
    if (index < 0 || index >= size)
      throw new IndexOutOfBoundsException();
    return names[index];
  }
  public int size() { return size; }
}
'''),
]

B3 = [
H('INTERFACE AND compareTo'),
C('''
class Student implements Comparable<Student> {
  private String name;
  public Student(String name) {
    this.name = name;
  }
  @Override
  public int compareTo(Student o) {
    return name.compareTo(o.name);
  }
}
// Strings use compareTo; numbers use
// Integer.compare(pages, o.pages)
class Employee extends Person
    implements Comparable<Employee> { ... }
Arrays.sort(arr);
// Maya, Alex, Priya -> Alex, Maya, Priya
'''),
L([
 'Returns <b>negative</b> if this comes first, <b>0</b> if equal, <b>positive</b> if after. <code>Arrays.sort</code> uses it; order does NOT come from insertion order.',
 'Interface = a list of promises (a ROLE); all methods abstract. <code>implements</code> MANY, <code>extends</code> only ONE (diamond problem: two parents, which method?).',
 'Generics <code>&lt;T&gt;</code> restrict the type: <code>ArrayList&lt;String&gt;</code> holds Strings only.',
]),
H('ACCESS AND PACKAGES'),
T([
 ['access','public','protected','none','private'],
 ['same class','Y','Y','Y','Y'],
 ['same pkg, subclass','Y','Y','Y','N'],
 ['same pkg, other','Y','Y','Y','N'],
 ['diff pkg, subclass','Y','Y','N','N'],
 ['diff pkg, other','Y','N','N','N'],
]),
P('Package: first line <code>package x;</code>, class names unique per package, no statement = default package, <code>java.lang</code> (System, Math, String) auto-imported, <code>java.util</code> has Arrays and Random. Course uses mostly public and private.'),
]

B4 = [
H('ALGORITHMS AND BIG-O (L6 to L9)'),
L([
 '<b>Algorithm</b> = finite, deterministic (same input, same output), effective, implementable in any language. Pseudocode is for humans. <b>Time</b> = count steps; <b>space</b> = memory; time matters most.',
 '<b>T(n)</b> = steps for input size n. Each line costs a constant; <code>end</code> and comments not counted. A loop header runs ONE MORE time than its body.',
 'Linear search: best (first spot) O(1), worst (missing) <code>an+b</code> = O(n). We use <b>worst case</b>: an upper-bound guarantee that happens often.',
 'Ladder, slow to fast: <b>1, log n, sqrt n, n, n log n, n^2, n^3, 2^n, n!</b>',
 '<b>Definition:</b> f(n) = O(g(n)) if there are positive c and n0 with 0 &lt;= f(n) &lt;= c*g(n) for all n &gt;= n0. g is an UPPER bound; O(g) is a SET.',
 '<b>Drop constants and small terms:</b> 4n^2+20n+9 = O(n^2); 3+5n^2+7n^3 &lt;= 15n^3 so O(n^3).',
 '<b>True/False rule:</b> simplify, then LEFT = O(RIGHT) is true if left is the same or EARLIER on the ladder.',
]),
T([
 ['claim','answer'],
 ['5n+20 = O(n)','T'],
 ['n^2 = O(n)','F'],
 ['n = O(n^3)','T'],
 ['2^n = O(n^3)','F'],
 ['3n+4 = O(n^2)','T'],
 ['n log n = O(n^2)','T'],
 ['3^n = O(n^3)','F'],
 ['n^3 = O(3^n)','T'],
 ['3+5n+18n^2 = O(n) / O(n^2)','F / T'],
]),
H('T(n) AND BIG-O, WORKED'),
C('''
linear search: line 1 for: c1(t+1)
  line 2 if: c2*t | line 3 return i: c3
  line 6 return -1: c4     (t = body runs)
best t=1: 2*c1 + c2 + c3 = constant = O(1)
worst t=n: c1(n+1) + c2*n + c4
  = (c1+c2)n + c1 + c4 = O(n)
3n+5 = O(n): 3n+5 <= 8n for n>=1 (c=8, n0=1)
n^2+n = O(n^2): <= 2n^2 for n>=1 (c=2)
3+5n^2+7n^3 <= 3n^3+5n^3+7n^3 = 15n^3
'''),
H('LISTS (L11)'),
L([
 '<b>Ordered</b> = each element has a position (not sorted by value). Head = start, tail = end.',
 'Interface says WHAT (add, addLast, get, isEmpty, size, toString); the implementation says HOW (ArrList uses an array).',
 '<code>size</code> = stored now, <code>maxSize</code> = capacity. A bad index throws <b>IndexOutOfBoundsException</b> (unchecked, runtime). The slide checks <code>index &gt; size</code>; the correct test is <code>index &gt;= size</code>.',
]),
C('''
ArrList() { this(DEFAULT_SIZE); }  // 10
ArrList(int capacity) {
  maxSize = capacity;
  size = 0;
  listArray = (T[]) new Object[capacity];
}
get(i): if (i < 0 || i >= size)
    throw new IndexOutOfBoundsException();
  return listArray[i];
add(e, i): shift RIGHT from the end
  for (k = last; k > i; k--)
    listArray[k] = listArray[k - 1];
  listArray[i] = e;
  if (size < maxSize) size++;
addLast(e) when FULL: shift LEFT
  for (k = 1; k < listArray.length; k++)
    listArray[k - 1] = listArray[k];
'''),
P('add at head = array INSERT (shift right), O(n). addLast on a full list = shift left, O(n).'),
H('QUICK FACTS'),
T([
 ['expression','result'],
 ['<code>Arrays.toString(new int[3])</code>','[0, 0, 0]'],
 ['<code>"Hello".charAt(1)</code>','\'e\''],
 ['<code>a[3]</code> on {4,8,15}','ArrayIndexOutOfBounds'],
 ['<code>int a[3];</code> or <code>new int[]</code>','does NOT compile'],
 ['<code>char c = s[0];</code> (String s)','does NOT compile'],
 ['<code>static int f(){return null;}</code>','does NOT compile'],
 ['<code>7 / 2 + " " + 7 % 2</code>','3 1'],
]),
L([
 'Constructor: <code>public Person(String name, int age) { this.name = name; this.age = age; }</code>',
 'Terms: object = state (fields) + behaviour (methods) + identity. Encapsulation = private fields + public methods.',
]),
]

FS = float(sys.argv[2]) if len(sys.argv) > 2 else 7.0
PREF = float(sys.argv[3]) if len(sys.argv) > 3 else 6.4
CSS = '''
@page { size: Letter; margin: 0.3in; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; }
body { font-family: Arial, Helvetica, sans-serif; font-size: __FS__pt; line-height: 1.12; color: #000;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 7.9in; height: 10.36in; display: flex; flex-direction: column; overflow: hidden; page-break-after: always; }
.page:last-child { page-break-after: auto; }
.title { font-size: 8pt; font-weight: bold; text-align: center; background: #1f3864; color: #fff; padding: 1px 0; margin-bottom: 2px; flex: none; }
.cols { display: flex; gap: 0.1in; flex: 1; min-height: 0; }
.col { flex: 1 1 0; min-width: 0; overflow: hidden; border-right: 0.5px solid #aaa; padding-right: 0.04in; }
.col:last-child { border-right: none; padding-right: 0; }
h2 { font-size: __H2__pt; margin: 3px 0 1px; padding: 0 2px; background: #cfe2f3; border-left: 2px solid #1f3864; }
h3 { font-size: __FS__pt; margin: 2px 0 0; color: #7f1d1d; text-decoration: underline; }
p { margin: 1px 0 2px; }
ul { margin: 1px 0 2px 8px; padding: 0; }
li { margin: 0 0 1px 0; }
pre { font-family: Consolas, "Courier New", monospace; font-size: __PRE__pt; line-height: 1.13; margin: 1px 0 3px; padding: 2px 3px;
      background: #f6f6f6; border: 0.4px solid #bbb; border-left: 2px solid #1f3864; white-space: pre; overflow: hidden; }
code { font-family: Consolas, "Courier New", monospace; font-size: __CODE__pt; background: #eee; padding: 0 1px; }
table { border-collapse: collapse; margin: 1px 0 3px; width: 100%; }
td, th { border: 0.4px solid #666; padding: 0 2px; font-size: __TD__pt; text-align: center; }
th { background: #d9d9d9; }
'''
CSS = (CSS.replace('__FS__', str(FS)).replace('__H2__', str(round(FS + 0.6, 2)))
          .replace('__PRE__', str(PREF)).replace('__CODE__', str(round(FS - 0.4, 2)))
          .replace('__TD__', str(round(FS - 0.3, 2))))

def page(title, cols):
    inner = ''.join('<div class="col">' + ''.join(c) + '</div>' for c in cols)
    return f'<div class="page"><div class="title">{title}</div><div class="cols">{inner}</div></div>'

doc = ('<!doctype html><html><head><meta charset="utf-8"><title>CSCI2010U Midterm Cheat Sheet</title><style>'
       + CSS + '</style></head><body>'
       + page('CSCI2010U MIDTERM - SIDE A: CODE YOU CAN WRITE, TRACES, RECURSION, SEARCHING', [A1, A2, A3])
       + page('CSCI2010U MIDTERM - SIDE B: OOP, INTERFACES, BIG-O, LISTS, EXPLAIN WHY', [B1 + EXPL, B2 + B3, B4])
       + '</body></html>')
open(sys.argv[1], 'w', encoding='utf-8').write(doc)
print('wrote', sys.argv[1], len(doc))
