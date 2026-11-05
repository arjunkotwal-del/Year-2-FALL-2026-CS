# CSCI2000U — Mock Midterm 3
**40 marks** · Section A: 12 MCQ x 1 · Section B: 4 MCQ x 2 · Section C: 4 short answers x 3 · Section D: 2 long answers x 4

> [!note] Coverage
> **L01–L14** mixed: UNIX paths and permissions, git, Python basics, strings, loops, recursion, lambda, `*args`, data structures, NumPy, files. This mock adds the **written** sections (C and D) because the prof said the real exam has short and long answers as well as MCQ.

> [!warning] Rules
> Closed book except your one page of notes. **Time yourself: 60 minutes** (about 25 for A+B, 35 for C+D). Write short and long answers on paper or in a text file, in your own words. Then check **Mock Midterm 3 - Answer Key.md**. For every miss, write one line on *why*. Syntax matters less than concepts, but spell commands correctly.

---

## Section A — 1 mark each

**1.** Which command prints your current working directory?
- A. `ls`
- B. `cd`
- C. `pwd`
- D. `echo`

**2.** Which is a **relative** path?
- A. `/home/sam/data.txt`
- B. `/data.txt`
- C. `../data/a.txt`
- D. `/`

**3.** What permission string does `chmod 640 f.txt` give?
- A. `rw-r-----`
- B. `rwxr-x---`
- C. `rw-rw----`
- D. `r--r-----`

**4.** You run `git add f.txt`, then edit `f.txt` again, then run `git status`. What does it show?
- A. `f.txt` is only staged
- B. `f.txt` is only modified
- C. `f.txt` is both staged and modified
- D. `f.txt` is untracked

**5.** `config.txt` is already committed. You add `config.txt` to `.gitignore`. What happens?
- A. Git stops tracking it immediately
- B. Git deletes it from disk
- C. Nothing: it stays tracked, because `.gitignore` only affects untracked files
- D. Git raises an error

**6.** What is `"hello"[1:3]`?
- A. `'hel'`
- B. `'el'`
- C. `'ell'`
- D. `'he'`

**7.** `"5" + 3` raises a `TypeError`. This shows Python is:
- A. dynamically typed only
- B. strongly typed
- C. weakly typed
- D. untyped

**8.** What does this print?
```python
x = [3, 1, 2]
y = x.sort()
print(y)
```
- A. `[1, 2, 3]`
- B. `[3, 1, 2]`
- C. `None`
- D. An error is raised

**9.** What is `len({1, 2, 2, 3})`?
- A. 2
- B. 3
- C. 4
- D. An error is raised

**10.** In `def f(*args):`, what is `args` inside the function?
- A. a list
- B. a dictionary
- C. a tuple
- D. a set

**11.** Which NumPy method returns a **copy** of the data?
- A. `ravel()`
- B. `reshape()`
- C. `flatten()`
- D. `view()`

**12.** What does the `with` statement do when you open a file?
- A. Opens the file twice
- B. Closes the file automatically when the block ends
- C. Erases the file's contents
- D. Makes the file read-only

---

## Section B — 2 marks each

**13.** What does this print?
```python
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(4))
```
- A. 10
- B. 12
- C. 24
- D. 1

**14.** What does this print?
```python
for i in range(1, 10, 3):
    print(i, end=" ")
```
- A. `1 4 7`
- B. `1 4 7 10`
- C. `1 2 3`
- D. `3 6 9`

**15.** What does this print?
```python
a = np.arange(8).reshape(2, 4)    # [[0 1 2 3], [4 5 6 7]]
print(a.sum(axis=1))
```
- A. `[ 4  6  8 10]`
- B. `[ 6 22]`
- C. `28`
- D. `[[0 1 2 3] [4 5 6 7]]`

**16.** What does this print?
```python
print(sorted(["bb", "a", "ccc"], key=lambda s: -len(s)))
```
- A. `['a', 'bb', 'ccc']`
- B. `['ccc', 'bb', 'a']`
- C. `['bb', 'a', 'ccc']`
- D. `[3, 2, 1]`

---

## Section C — Short answer, 3 marks each
*Answer in 2–4 sentences or a short list.*

**17.** Explain the difference between `git restore --staged a.txt` and `git restore a.txt`. Say what each does to the staging area and to your edits.

**18.** A file shows `rwxr-x---` in `ls -l`. (a) What is the octal form? (b) State what the owner, the group, and everyone else can do.

**19.** Explain the difference between a **view** and a **copy** of a NumPy array. Give one operation that returns each, and say what happens to the original array when you change an element of the result.

**20.** Explain what **dynamically typed** and **strongly typed** mean in Python. Give a one-line code example of each.

---

## Section D — Long answer, 4 marks each

**21.** Write a Python function `average(*args)` that returns the mean of any number of numbers, and returns `None` if no numbers are given. Then show a call with three numbers and a call with none, and say what each returns.

**22.** `secret.env` was committed to a git repository by mistake. You want git to **stop tracking** it, **keep the file on your disk**, and make sure it is **never added again**. Write the exact commands in order, ending with the commit, and explain in one sentence why each command is needed.
