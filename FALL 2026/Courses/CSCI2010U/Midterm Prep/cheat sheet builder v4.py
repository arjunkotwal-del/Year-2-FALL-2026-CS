import html, sys

def esc(s): return html.escape(s, quote=False)
def H(t): return f'<h2>{esc(t)}</h2>'
def H3(t): return f'<h3>{t}</h3>'
def P(t): return f'<p>{t}</p>'
def C(t): return '<pre>' + esc(t.strip('\n')) + '</pre>'
def L(items): return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def T(rows):
    out = '<table>'
    for k, r in enumerate(rows):
        tag = 'th' if k == 0 else 'td'
        out += '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in r) + '</tr>'
    return out + '</table>'

# =============================================================== SIDE A
A1 = [
H('HOW TO ANSWER'),
L([
 '<b>Print / return?</b> Make a table: one row per pass or call, one column per variable. Run it line by line.',
 '<b>Fill a blank:</b> copy the matching template; check start, stop test, step, names.',
 '<b>Write a method:</b> 1) what to return, 2) variable (count / sum / min), 3) loop or recursion, 4) return AFTER the loop. Test it on the example.',
]),
H('JAVA ESSENTIALS'),
L([
 'Array: index from <b>0</b>; <code>a.length</code> (no brackets); last = <code>a[a.length-1]</code>; <code>a[a.length]</code> crashes. <code>int[] a = new int[5];</code> (all 0) or <code>{5,2,9}</code>. Size is fixed.',
 'String: <code>s.length()</code>, <code>s.charAt(i)</code>, <code>s.substring(1)</code> ("hello" gives "ello"), <code>s.substring(1,3)</code> ("el", end not included), <code>s1.compareTo(s2)</code> (negative = s1 first). Case matters.',
 '<code>n%10</code> = last digit, <code>n/10</code> drops it (5072: 2 and 507). <code>==</code> compares, <code>=</code> assigns. Defaults: int 0, boolean false, object null.',
 'Primitives are passed as a COPY. Arrays and objects pass a reference copy, so a method changes the SAME array (no return needed).',
 '<b>Compile error</b> (javac refuses): missing ;, wrong type, private field used outside its class, <code>new</code> on an abstract class, parent object put in a child variable, abstract method not written, <code>return null</code> in an int method.',
 '<b>Runtime error</b> (crashes while running): ArrayIndexOutOfBounds, StackOverflowError.',
 '<code>i % k == 0</code> means divisible by k. Integer division truncates: 7 / 2 = 3, 7 % 2 = 1.',
 'A <code>static</code> method cannot use instance fields or <code>this</code>; an object needs <code>new</code> before you use it.',
 'Strings are not arrays: <code>s[i]</code> does not compile, use <code>s.charAt(i)</code>. <code>+=</code> works on Strings, not arrays. An int method returns a number (or throws), never null. Out of range: arrays throw ArrayIndexOutOfBounds, the L11 list throws IndexOutOfBounds.',
 '<code>javac F.java</code> makes F.class; <code>java F</code> runs <code>public static void main(String[] args)</code>.',
]),
H('COUNT, MIN, SUM, MULTIPLES (Lab 1)'),
C('''
int count = 0;                // before the loop
for (int i = 0; i < a.length; i++)
  if (a[i] >= target) count++;  // >= : equal counts
return count;                 // after the loop
countAtLeast({25,10,40,25}, 25):
 i=0 25>=25 yes c=1 | i=1 10>=25 no c=1
 i=2 40>=25 yes c=2 | i=3 25>=25 yes c=3 -> 3
count > 4 in {5,2,9,2}: yes,no,yes,no -> 2
int min = a[0];               // not 0
for (int i = 1; i < a.length; i++)
  if (a[i] < min) min = a[i];
int sum = 0;
for (int i = 0; i < a.length; i++) sum += a[i];
for (int i=start; i<=end; i++)    // multiples
  if (i % mult == 0) System.out.println(i);'''),
H('REVERSE'),
C('''
void reverseArray(int[] a){       // in place
  int l = 0, r = a.length-1;
  while (l < r){ int t=a[l]; a[l]=a[r]; a[r]=t;
    l++; r--; } }        // {1,2,3,4} -> 4 3 2 1
String reverse(String s){ String out = "";
  for (int i=s.length()-1; i>=0; i--)
    out += s.charAt(i);
  return out; }          // "abc" -> "cba"'''),
H('ORDER THE STEPS'),
C('''
insert val at idx: check range (return)
  -> i = a.length-1 -> while i>idx: a[i]=a[i-1], i--
  -> a[idx] = val
binary search: low>high return NOT_FOUND -> mid
  -> equal? return mid -> else recurse on a half
TOH: if n==0 return -> TOH(n-1,start,temp,goal)
  -> print start --> goal -> TOH(n-1,temp,goal,start)
bubble: i from last down to 1 -> j from 0 to i-1
  -> if A[j+1] < A[j] swap
delete: check range -> i = idx+1
  -> while i<length: a[i-1]=a[i] -> last = GAP'''),
H('SLIPS TO AVOID (caught in practice)'),
L([
 '<code>i &lt;= a.length</code> crashes; use <code>i &lt; a.length</code>.',
 'Counter starts BEFORE the loop; <code>count++</code> goes INSIDE the <code>if</code>; <code>return</code> goes AFTER the loop.',
 'Bubble sort: <code>i</code> is fixed during a pass, <code>j</code> moves. n elements: i starts at n-1, n-1 passes.',
 'A recursive call returns a VALUE: <code>sumTo(2)</code> is 3, not 2. Each call adds only its own piece (1 per digit, not n).',
 'Text needs quotes and exact case: <code>"Meow"</code>. Strings use <code>compareTo</code>; numbers use <code>Integer.compare</code>.',
]),
]

A2 = [
H('BUBBLE SORT (L1, L2)'),
C('''
for (int i = A.length-1; i > 0; i--)  // i fixed
  for (int j = 0; j < i; j++)         // j moves
    if (A[j+1] < A[j]) swap(A, j, j+1);
swap: int t=A[j]; A[j]=A[k]; A[k]=t;  // needs temp
descending: use A[j+1] > A[j]
{4,2,3}: i=2: j=0 2<4 swap 2 4 3
              j=1 3<4 swap 2 3 4
         i=1: j=0 3<2? no  2 3 4   (2 passes)
{3,1,2}: i=2: 1 3 2 | 1 2 3 ; i=1: 2<1? no
{5,2,4,1}: 2541 | 2451 | 2415 (5 locked)
  pass2: 2415 | 2145 | pass3: 1245
{8,1,6,4,9}: i=4: j0 swap 1 8 6 4 9, j1 swap
  1 6 8 4 9, j2 swap 1 6 4 8 9, j3 9<8? no
  i=3: j0 no, j1 swap 1 4 6 8 9, j2 no
  i=2: no, no | i=1: no  -> 1 4 6 8 9
  (4+3+2+1 = 10 compares)
{1,2,3} already sorted: 3 compares, 0 swaps
{3,2,1} reversed: 3 compares, 3 swaps -> 1 2 3'''),
T([
 ['n','i starts','passes','pass1 compares','j max'],
 ['4','3','3','3','2'],
 ['5','4','4','4','3'],
 ['6','5','5','5','4'],
]),
P('Total compares = n(n-1)/2. Worst case O(n^2).'),
H('SEARCHING (L6, L10)'),
C('''
linear: for (int i=0; i<A.length; i++)
          if (A[i]==val) return i;
        return -1;      // best O(1), worst O(n)
binary (array SORTED): bs(a,val,low,high)
  if (low > high) return NOT_FOUND;
  int mid = (low+high)/2;
  if (val == a[mid]) return mid;
  else if (val < a[mid])
    return bs(a,val,low,mid-1);
  else return bs(a,val,mid+1,high);
start: bs(a,val,0,a.length-1)    O(log n)
a={1,3,5,7,9,11,13}
find 11: l0 h6 m3=7, go right: l4
         l4 h6 m5=11 found, return 5
find 3 : l0 h6 m3=7, go left: h2
         l0 h2 m1=3 found, return 1
find 5 : m3=7 h2 | m1=3 l2 | l2 h2 m2=5 -> 2
find 4 : m3=7 h2 | m1=3 l2 | m2=5 h1 | low>high
         NOT_FOUND'''),
H('ARRAY INSERT / DELETE (L10)'),
C('''
insert(a,idx,val):
  for (int i=a.length-1; i>idx; i--)
    a[i] = a[i-1];     // shift RIGHT from the end
  a[idx] = val;        // last element falls off
{4,6,8,10} idx=1 val=50:
 4 6 8 8 | 4 6 6 8 | 4 50 6 8   (2 shifts)
delete(a,idx):
  for (int i=idx+1; i<a.length; i++)
    a[i-1] = a[i];     // shift LEFT
  a[a.length-1] = GAP;
{5,6,7,8} idx=1:
 5 7 7 8 | 5 7 8 8 | 5 7 8 GAP  (2 shifts)
worst idx=0 O(n); best idx=last O(1); a[i] O(1)'''),
H('PERFECT SQUARE (L6, L9)'),
C('''
v0: while (i <= n) { if (i*i==n) Yes; i++ }  O(n)
v1: while (i*i <= n)                        O(sqrt n)
v2: double i till i*i>n, then binary search O(log n)
n=10: v0 10 loops No | v1 i=1,2,3 (1,4,9), 16>10
      stop = 3 loops, No
n=20: v0 20 loops    | v1 i=1..4 (16), 25>20
      stop = 4 loops, No
n=16: v1 i=1..4, 16==16 Yes (4 loops)'''),
H('MORE WHOLE METHODS (Canvas style)'),
C('''
boolean isSorted(int[] a){
  for (int i = 1; i < a.length; i++)
    if (a[i-1] > a[i]) return false;   // not >=
  return true; }     // empty / 1 element = true
int countDivisible(int lo, int hi, int k){
  int count = 0;
  for (int i = lo; i <= hi; i++)
    if (i % k == 0) count++;
  return count; }    // (1, 11, 3) = 3
class Roster { private String[] names; private int size;
  public Roster(int capacity){
    names = new String[capacity]; size = 0; }
  public void add(String name){
    if (size == names.length)
      throw new IndexOutOfBoundsException("full");
    names[size] = name; size++; }
  public String get(int index){
    if (index < 0 || index >= size)
      throw new IndexOutOfBoundsException("bad");
    return names[index]; }
  public int size(){ return size; } }'''),
]

A3 = [
H('RECURSION (L7, Lab 4)'),
L([
 'Needs a <b>base case</b> (smallest problem, returns) and a <b>recursive case</b> (calls itself on a SMALLER problem). No base case = StackOverflowError.',
 'Trace: go DOWN (calls wait), then back UP (each returns using the value from below). <code>sumTo(2)</code> means the SUM 1+2 = 3, not the number 2. Countdown n..0 = n+1 calls.',
 'Print BEFORE the call = going down (3,2,1). Print AFTER = coming up (1,2,3).',
]),
C('''
sumTo(n): if (n==0) return 0;
          return n + sumTo(n-1);
 (0)=0 (1)=1+0=1 (2)=2+1=3 (3)=3+3=6  4 calls
twice(n): if (n==0) return 0;
          return 2 + twice(n-1);
 (1)=2 (2)=4 (3)=6   (= 2n)
down(n): if(n==0) return;
  print n; down(n-1);        down(3): 3 2 1
up(n): if(n==0) return;
  up(n-1); print n;          up(3): 1 2 3
test(n): if(n==0) return; print "A"+n;
  test(n-1); print "B"+n;
 test(2): A2 A1 B1 B2   test(3): A3 A2 A1 B1 B2 B3
sumDigits(n): if (n==0) return 0;
  return n%10 + sumDigits(n/10);
 (72) = 2 + (7 + 0) = 9
 iter: while (n>0) { s += n%10; n /= 10; }
countDigits(n): if (n<10) return 1;
  return 1 + countDigits(n/10);
 (472) = 1+(1+1) = 3     each call adds 1, not n
power(b,e): if (e==0) return 1;
  return b * power(b, e-1);
rev(s): if (s.length()<=1) return s;
  return rev(s.substring(1)) + s.charAt(0);
 rev("abc") = rev("bc")+a = (rev("c")+b)+a = "cba"
isPal(t): if (t.length()<=1) return true;
  if (t.charAt(0) != t.charAt(t.length()-1))
    return false;
  return isPal(t.substring(1, t.length()-1));
 "abba": a=a, "bb": b=b, "" true
 "abca": a=a, "bc": b!=c  false (2 calls)
 iter: i=0, j=t.length()-1;
  while (i<j) { if (t.charAt(i)!=t.charAt(j))
    return false; i++; j--; }  return true;
mystery(n): print n; mystery(n-1); print n
 mystery(3): 3 2 1 then 1 2 3 (base prints none)
f(n): if (n<=1) return 1; return f(n-1)+f(n-2);
 f(2)=2 f(3)=3 f(4)=5 ; calls for f(4) = 9
 isPal("level"): l=l, "eve": e=e, "v" true (3 calls)
TOH(n,start,goal,temp): if (n==0) return;
  TOH(n-1,start,temp,goal);
  print start --> goal;
  TOH(n-1,temp,goal,start);   call TOH(n,"A","C","B")
 n=2: A-B A-C B-C
 n=3 (7): A-C A-B C-B A-C B-A B-C A-C
 moves 2^n - 1'''),
H('RAPID-FIRE ANSWERS (Java basics)'),
C('''
Arrays.toString(new int[3])        -> [0, 0, 0]
"Java".length()                    -> 4
"Hello".charAt(1)                  -> 'e'
int[] a={4,8,15}; a[3]             -> ArrayIndexOutOfBounds
int[] a = new int[3];              OK
int a[3];  int[] a = new int[];    do NOT compile
String s="hi"; char c = s[0];      does NOT compile
static int f(){ return null; }     does NOT compile
int x = null;                      does NOT compile
7 / 2 + " " + 7 % 2                -> 3 1
public Student(String name, int id){
  this.name = name; this.id = id; }'''),
H('WRITE A RECURSIVE METHOD IN 4 STEPS'),
C('''
1 base case: smallest input, return directly
2 one piece of work: n%10, first letter, n
3 call yourself on a SMALLER input:
  n/10, n-1, substring(1)
4 combine: return piece + the call
sumDigits: base n==0 gives 0 | piece n%10
  | smaller n/10
palindrome: base length<=1 true | piece compare
  the ends | smaller substring(1, length-1)
A loop's stop condition = the recursive base case'''),
H('LOOPS TO BIG-O'),
C('''
return a[5];                           O(1)
for (i=0;i<n;i++) sum+=a[i];           O(n)
for (...n) x++;  for (...n) y++;       O(n) two loops in a row
for (i=0;i<n;i++) for (j=0;j<n;j++)    O(n^2)
for (i=0;i<n;i++) for (j=0;j<i;j++)    O(n^2) (n(n-1)/2)
while (n > 1) { n = n/2; }             O(log n)
T(n)=6n^2+30n+11                       O(n^2)
for (i=0;i<n;i++) for (j=0;j<5;j++)    O(n) inner is fixed
for (i=1;i<n;i*=2)                     O(log n) doubles
3 nested loops each to n               O(n^3)
for (...n) x++; for (..n)for(..n) y++; n+n^2 = O(n^2)'''),
]

# =============================================================== SIDE B
B1 = [
H('INHERITANCE (L3, L4, Lab 2)'),
L([
 '<code>extends</code>. Test "is a": Manager IS AN Employee, never the reverse. A subclass can add and <b>override</b>.',
 '<code>super(...)</code> must be the FIRST line of the constructor (runs the parent constructor).',
 'Parent <code>private</code> fields are not visible in the child: use the getter.',
 'In an override, <code>super.m()</code> = parent version. Plain <code>m()</code> = itself, forever = <b>StackOverflowError</b> (runtime).',
]),
C('''
class Pet { private String name;
  public Pet(String name){ this.name = name; }
  public String getName(){ return name; }
  public String sound(){ return "..."; } }
class Dog extends Pet { private int tricks;
  public Dog(String name, int tricks){
    super(name);             // first line
    this.tricks = tricks; }
  @Override public String sound(){ return "Woof"; }
  public String describe(){
    return getName() + " knows " + tricks; } }
class Cat extends Pet { private int lives;
  public Cat(String name, int lives){
    super(name); this.lives = lives; }
  @Override public String sound(){ return "Meow"; }
  public String describe(){
    return getName() + " has " + lives; } }
class LoudDog extends Dog {
  public LoudDog(String n, int t){ super(n, t); }
  @Override public String sound(){
    return super.sound() + "!"; } }
Pet[] p = { new Pet("A"), new Dog("B",1),
            new LoudDog("C",2) };
for (Pet x : p) System.out.println(x.sound());
// prints:  ...   Woof   Woof!
new Dog("Rex",3).describe()  gives  Rex knows 3'''),
C('''
class Manager extends Employee {
  private double bonus;
  public Manager(double salary, String name){
    super(salary, name); this.bonus = 0; }
  @Override public double getSalary(){
    return super.getSalary() + bonus; } }
// salary 70000, bonus 500 gives 70500
LimitedCounter(String name, int limit){
  super(name); this.limit = limit; }
@Override public void increment(){
  if (getCount() < limit) super.increment(); }
for (Counter c : counters) c.increment();'''),
H('POLYMORPHISM (L4)'),
L([
 'A parent variable can hold a child object. The version that RUNS is the object\'s own class (dynamic dispatch).',
 'Read right to left with "is a". A parent variable cannot call child-only methods.',
 'Making an object: declare a REFERENCE (an address), create the object with <code>new</code> on the <b>HEAP</b>, link them.',
]),
T([
 ['code','result'],
 ['<code>Pet p = new Dog("B",1);</code>','OK (Dog is a Pet)'],
 ['<code>p.sound()</code>','runs Dog\'s: Woof'],
 ['<code>p.describe()</code>','COMPILE error (Pet has none)'],
 ['<code>Dog d = new Pet("A");</code>','COMPILE error'],
 ['<code>Pet[] arr</code>','holds Pet, Dog, Cat'],
 ['<code>void feed(Pet x)</code>','accepts any Pet child'],
]),
H3('Polymorphism with an array (L4)'),
C('''
Manager boss = new Manager(95000, "Bill");
boss.setBonus(2750);
Employee[] w = { boss, new Employee(20745,"Peter"),
   new Employee(25000,"Mario") };
for (Employee e : w)
  println(e.getName() + ": $" + e.getSalary());
// Bill: $97750.0 (95000+2750) Peter: $20745.0 Mario: $25000.0'''),
H('COMPILE OR RUNTIME?'),
T([
 ['situation','error'],
 ['override calls itself (no <code>super.</code>)','RUNTIME StackOverflowError'],
 ['<code>a[4]</code> on length 4','RUNTIME ArrayIndexOutOfBounds'],
 ['list <code>get</code> with a bad index','RUNTIME IndexOutOfBounds'],
 ['<code>new Shape()</code> (abstract)','COMPILE'],
 ['concrete class missing an abstract method','COMPILE'],
 ['child reads parent\'s private field','COMPILE'],
 ['<code>Dog d = new Pet("A");</code>','COMPILE'],
 ['child-only method on a parent variable','COMPILE'],
 ['<code>return null</code> in an int method','COMPILE'],
]),
]

B2 = [
H('ABSTRACT CLASS (L5, Lab 3)'),
C('''
abstract class Shape {
  public abstract double area(); }   // no body
class Square extends Shape { private double s;
  public Square(double s){ this.s = s; }
  @Override public double area(){ return s*s; } }
new Shape()                        ERROR (abstract)
Shape b = new Square(2);           OK
class Triangle extends Shape { }   ERROR: no area()
 fix: write area() OR "abstract class Triangle"'''),
C('''
abstract class Person { private String name;
  public Person(String name){ this.name = name; }
  public String getName(){ return name; }
  public abstract String getPosition(); }
class Employee extends Person { private double salary;
  public Employee(double salary, String name){
    super(name); this.salary = salary; }
  @Override public String getPosition(){
    return "Employee " + getName() + " on salary $" + salary; } }
class Intern extends Person {
  public Intern(String name){ super(name); }
  @Override public String getPosition(){
    return "Intern unpaid"; } }
Person[] staff = { new Employee(20000,"Peter"),
                   new Intern("Tom") };
for (Person p : staff) println(p.getPosition());
 // Employee Peter on salary $20000.0  /  Intern unpaid'''),
L([
 '<b>Cannot instantiate</b> an abstract class, even with a constructor. A constructor can NOT be abstract. Mixes concrete + abstract methods; can have static methods.',
 'A child must write ALL abstract methods or be abstract itself. Non-abstract = <b>concrete</b>.',
 'Use it when siblings share structure: Person (abstract getPosition) with Employee and Intern, each writing its own.',
]),
H('INTERFACE AND compareTo'),
C('''
class Student implements Comparable<Student> {
  private String name;
  public Student(String name){ this.name = name; }
  @Override public int compareTo(Student o){
    return name.compareTo(o.name); } }   // Strings
class Book implements Comparable<Book> {
  private int pages;
  @Override public int compareTo(Book o){
    return Integer.compare(pages, o.pages); } } // numbers
class Employee extends Person
    implements Comparable<Employee> { ... }
Arrays.sort(arr); // Maya,Alex,Priya gives Alex,Maya,Priya'''),
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
H('EXPLAIN WHY'),
L([
 '<b>Equal to target counts:</b> "at least" means &gt;=.',
 '<b>super(name) vs super.increment():</b> the first sets the parent\'s private state (first line only); the second calls the parent version of an overridden method.',
 '<b>new Person() fails:</b> abstract, cannot be instantiated, even with a constructor.',
 '<b>Concrete class writes every abstract method:</b> otherwise an object would have a method with no body.',
 '<b>Comparable and Arrays.sort:</b> sort calls compareTo to decide the order. implements = many roles; extends = one parent.',
 '<b>Loop stop vs base case:</b> both are the condition where work ends, and every step moves toward it.',
 '<b>Why private fields?</b> Only methods can change state, so the class controls how its data is read and changed (encapsulation).',
 '<b>Why no two parents?</b> Diamond: which inherited field or method wins? Interfaces avoid it because every method is abstract.',
 '<b>Palindrome mismatch:</b> one differing outer pair already proves it is not one, so return false at once.',
]),
]

B3 = [
H('ALGORITHMS AND BIG-O (L6 to L9)'),
L([
 '<b>Algorithm</b> = finite, deterministic (same input, same output), effective, implementable in any language. Pseudocode is for humans. <b>Time</b> = count steps; <b>space</b> = memory; time matters most.',
 '<b>T(n)</b> = steps for input size n. Each line costs a constant; <code>end</code> and comments not counted. A loop header runs ONE MORE time than its body.',
 'Linear search: best (first spot) O(1), worst (missing) <code>an+b</code> = O(n). We use <b>worst case</b>: an upper-bound guarantee that happens often. Average case not covered.',
 'Big-O is a notation. Worst case is a type of input. Big-O can describe either.',
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
linear search lines: 1 for: c1(t+1) | 2 if: c2*t
  3 return i: c3 | 6 return -1: c4   (t = body runs)
best t=1: 2*c1 + c2 + c3 = constant = O(1)
worst t=n: c1(n+1) + c2*n + c4
  = (c1+c2)n + c1 + c4 = O(n)
perfect square v0 worst: about 4n steps (1 multiply,
  2 compares, 1 add per pass) = O(n)
3n+5 = O(n): 3n+5 <= 8n for n>=1  (c=8, n0=1)
n^2+n = O(n^2): n^2+n <= 2n^2 for n>=1  (c=2, n0=1)
3+5n^2+7n^3 <= 3n^3+5n^3+7n^3 = 15n^3  (c=15)'''),
H('LISTS (L11)'),
L([
 '<b>Ordered</b> = each element has a position (not sorted by value). Head = start, tail = end.',
 'Interface says WHAT (add, addLast, get, isEmpty, size, toString); the implementation says HOW (ArrList uses an array).',
 '<code>size</code> = stored now, <code>maxSize</code> = capacity. A bad index throws <b>IndexOutOfBoundsException</b> (unchecked, runtime). The slide checks <code>index &gt; size</code>; the correct test is <code>index &gt;= size</code>.',
 'add at head = like array INSERT (shift right), O(n). addLast on a full list = shift left, O(n).',
]),
C('''
ArrList(){ this(DEFAULT_SIZE); }      // DEFAULT 10
ArrList(int capacity){ maxSize = capacity;
  size = 0; listArray = (T[]) new Object[capacity]; }
get(i): if (i<0 || i>=size)
  throw new IndexOutOfBoundsException("..");
  return listArray[i];
add(e,i) shift RIGHT (from the end):
  for (int k = size<maxSize ? size : maxSize-1;
       k > i; k--) listArray[k] = listArray[k-1];
  listArray[i] = e;  if (size<maxSize) size++;
addLast(e) when FULL, shift LEFT:
  for (int k = 1; k < listArray.length; k++)
    listArray[k-1] = listArray[k];'''),
H('QUICK FACTS (past quiz)'),
L([
 'Default int = <b>0</b>. <code>"Hello".length()</code> = <b>5</b>. <code>int[] arr = new int[5];</code> Last = <code>arr[arr.length-1]</code>.',
 'Out of bounds = <b>ArrayIndexOutOfBoundsException</b>. Arrays fixed size. Java ArrayList remove last = O(1).',
 'Constructor: <code>public Person(String name, int age){ this.name = name; this.age = age; }</code>',
 'Printing an array directly gives garbage like [I@251a69d7; use <code>Arrays.toString(a)</code> (needs <code>import java.util.Arrays;</code>). <code>public static void main(String[] args)</code>.',
 'Binary search needs a SORTED array. A method that sorts an array needs no return: arrays pass a reference.',
 'Compile with <code>javac F.java</code>, run with <code>java F</code>. A Java <code>for</code> runs init once, then test, body, step.',
 'Terms: class = blueprint, object = instance; object has state (fields), behaviour (methods), identity. Encapsulation = private fields + public methods. Nouns = classes, verbs = methods.',
]),
]

FS = float(sys.argv[2]) if len(sys.argv) > 2 else 7.0
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
pre { font-family: Consolas, "Courier New", monospace; font-size: __PRE__pt; line-height: 1.1; margin: 1px 0 2px; padding: 1px 2px;
      background: #f2f2f2; border: 0.4px solid #bbb; white-space: pre-wrap; word-break: break-word; }
code { font-family: Consolas, "Courier New", monospace; font-size: __CODE__pt; background: #eee; padding: 0 1px; }
table { border-collapse: collapse; margin: 1px 0 2px; width: 100%; }
td, th { border: 0.4px solid #666; padding: 0 2px; font-size: __TD__pt; text-align: center; }
th { background: #d9d9d9; }
'''
CSS = (CSS.replace('__FS__', str(FS)).replace('__H2__', str(round(FS + 0.6, 2)))
          .replace('__PRE__', str(round(FS - 0.7, 2))).replace('__CODE__', str(round(FS - 0.4, 2)))
          .replace('__TD__', str(round(FS - 0.3, 2))))

def page(title, cols):
    inner = ''.join('<div class="col">' + ''.join(c) + '</div>' for c in cols)
    return f'<div class="page"><div class="title">{title}</div><div class="cols">{inner}</div></div>'

doc = ('<!doctype html><html><head><meta charset="utf-8"><title>CSCI2010U Midterm Cheat Sheet</title><style>'
       + CSS + '</style></head><body>'
       + page('CSCI2010U MIDTERM - SIDE A: CODE YOU CAN WRITE, TRACES, RECURSION, SEARCHING', [A1, A2, A3])
       + page('CSCI2010U MIDTERM - SIDE B: OOP, INTERFACES, BIG-O, LISTS, EXPLAIN WHY', [B1, B2, B3])
       + '</body></html>')
out = sys.argv[1]
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc))
