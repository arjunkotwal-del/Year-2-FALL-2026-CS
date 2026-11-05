# CSCI2000U — Mock Midterm 4
**40 marks** · Section A: 12 MCQ x 1 · Section B: 4 MCQ x 2 · Section C: 4 short answers x 3 · Section D: 2 long answers x 4

> [!note] Coverage
> **L01–L14** again, but with different angles from Mock 3: string methods, default arguments, aliasing, `axis`, `cp -r`, the three git areas, file I/O with `csv`. Same format as the real exam: MCQ plus short and long written answers.

> [!warning] Rules
> Closed book except your one-page notes. **Time yourself: 60 minutes** (about 25 for A+B, 35 for C+D). Write C and D in your own words, then check **Mock Midterm 4 - Answer Key.md**. For every miss, write one line on *why*. Concepts matter more than syntax, but spell commands correctly.

---

## Section A — 1 mark each

**1.** What does `ls -a` do?
- A. Lists files sorted by size
- B. Lists all files, including hidden ones that start with a dot
- C. Lists files in a long format
- D. Lists only directories

**2.** What does `mkdir -p a/b/c` do when none of `a`, `b`, `c` exist?
- A. Fails because `a` does not exist
- B. Creates only `c`
- C. Creates `a`, then `a/b`, then `a/b/c`
- D. Creates a file called `c`

**3.** `old.txt` does not exist. You run `mv report.txt old.txt`. What happens?
- A. `report.txt` is renamed to `old.txt`
- B. A copy called `old.txt` is made and `report.txt` is kept
- C. `report.txt` is deleted
- D. An error is raised

**4.** What permission string does `chmod 755 run.sh` give?
- A. `rwxr-xr-x`
- B. `rw-r--r--`
- C. `rwxrwxrwx`
- D. `r-xr-xr-x`

**5.** In git, which area sits **between** the working directory and the repository?
- A. The remote
- B. The staging area
- C. The stash
- D. The `.gitignore`

**6.** What does `git clone <url>` do?
- A. Turns the current folder into a repository
- B. Copies a remote repository, with its history, to your machine
- C. Saves the staged files as a commit
- D. Deletes the remote repository

**7.** What does `git diff --staged` compare?
- A. Working copy vs staging area
- B. Staging area vs the last commit
- C. Two branches
- D. The remote vs your local repository

**8.** What is `7 // 2` in Python?
- A. 3.5
- B. 4
- C. 3
- D. 1

**9.** What is `type(3 / 2)`?
- A. `int`
- B. `float`
- C. `str`
- D. `bool`

**10.** What is `"python"[-2:]`?
- A. `'py'`
- B. `'on'`
- C. `'n'`
- D. `'thon'`

**11.** What is `{1, 2} | {2, 3}`?
- A. `{2}`
- B. `{1, 2, 2, 3}`
- C. `{1, 2, 3}`
- D. `{1, 3}`

**12.** What is `np.arange(6).reshape(2, 3).shape`?
- A. `6`
- B. `(3, 2)`
- C. `(6,)`
- D. `(2, 3)`

---

## Section B — 2 marks each

**13.** What does this print?
```python
def f(x, y=2):
    return x * y

print(f(3), f(3, y=4))
```
- A. `6 12`
- B. `6 6`
- C. `3 3`
- D. An error is raised

**14.** What does this print?
```python
s = "banana"
print(s.replace("an", "AN"), s.count("a"))
```
- A. `banana 3`
- B. `bANANa 3`
- C. `bANANa 2`
- D. `ANANAN 3`

**15.** What does this print?
```python
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print(len(a), len(c))
```
- A. `3 3`
- B. `4 4`
- C. `3 4`
- D. `4 3`

**16.** What does this print?
```python
M = np.array([[1, 2, 3], [4, 5, 6]])
print(M.sum(axis=0), M[:, 1])
```
- A. `[ 6 15] [2 5]`
- B. `[5 7 9] [2 5]`
- C. `[5 7 9] [4 5 6]`
- D. `21 [2 5]`

---

## Section C — Short answer, 3 marks each
*Answer in 2–4 sentences or a short list.*

**17.** `cdir` already exists and `adir` contains `a.txt`. Explain the difference between `cp -r adir cdir` and `cp -r adir/ cdir` (using the course slides' behaviour). Say where `a.txt` ends up in each case.

**18.** Name the **three areas** in git and say what `git add` and `git commit` each do to move your work between them.

**19.** A student writes `y = x.sort()` and finds that `y` is `None`. Explain why, and show two ways to get a sorted list back.

**20.** Explain what `axis=0` and `axis=1` mean when you call `.sum()` on a 2x3 NumPy array. Give the shape of each result.

---

## Section D — Long answer, 4 marks each

**21.** Write a Python function `count_vowels(s)` that uses a loop to return the number of vowels (`a e i o u`, upper or lower case) in the string `s`. Then say what `count_vowels("Data Science")` returns, and why your function handles the capital `D` and `S`.

**22.** Given `scores = [("Ada", 90), ("Lin", 85)]`, write Python code that (a) writes a CSV file `scores.csv` with a header row `name,score` followed by the two rows, and (b) reads the file back and prints each row. Then answer: what type are the numbers when you read them back, and what would happen to the file if you opened it with `"w"` again?
