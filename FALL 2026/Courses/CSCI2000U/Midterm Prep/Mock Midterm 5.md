# CSCI2000U — Mock Midterm 5 (all MCQ)
**40 marks** · Section A: 20 MCQ x 1 · Section B: 10 MCQ x 2 · **60 minutes**

> [!note] Coverage
> **L01–L14**, with extra weight on the tutorial topics (recursion, lambda, `*args`, git undo, views vs copies). This is the all-MCQ format you first heard about: 20 x 1 mark + 10 x 2 marks.

> [!warning] Rules
> Closed book except your one-page notes. Time yourself: 60 minutes. Write your answers as a list (`1 B, 2 C, ...`) and check **Mock Midterm 5 - Answer Key.md** only at the end. For every miss, write one line on *why* you picked it.

---

## Section A — 1 mark each

**1.** What does `pwd` print?
- A. The permissions of the current folder
- B. The absolute path of the current working directory
- C. The files in the current directory
- D. The name of the current user

**2.** What does `cd -` do?
- A. Goes to your home directory
- B. Goes up one directory
- C. Goes back to the previous directory you were in
- D. Lists the current directory

**3.** What does `rm -r olddir` do?
- A. Removes `olddir` and everything inside it
- B. Renames `olddir`
- C. Removes only the empty directory `olddir`
- D. Copies `olddir` recursively

**4.** `f.txt` already contains text. You run `echo hi > f.txt`. What does `f.txt` contain afterwards?
- A. The old text, then `hi` added at the end
- B. The old text only
- C. Nothing, the command fails
- D. Only `hi`

**5.** What permission string does `chmod 644 notes.txt` give?
- A. `rwxr--r--`
- B. `rw-r--r--`
- C. `rw-rw-rw-`
- D. `r--r--r--`

**6.** In the data science process, which step usually takes the **most** time?
- A. Building the final model
- B. Presenting the results
- C. Data wrangling (cleaning and preparing the data)
- D. Choosing a programming language

**7.** You create a new file `a.txt` and run `git add a.txt`. What state is the file in?
- A. Staged
- B. Untracked
- C. Committed
- D. Ignored

**8.** What does `git restore --staged f.txt` do?
- A. Deletes your edits to `f.txt`
- B. Deletes `f.txt` from the repository
- C. Commits `f.txt`
- D. Unstages `f.txt` and keeps your edits in the working directory

**9.** What does `git rm --cached secret.env` do?
- A. Deletes `secret.env` from disk and from git
- B. Stops tracking `secret.env` but keeps the file on disk
- C. Hides `secret.env` forever
- D. Restores `secret.env` from the last commit

**10.** What does a `.gitignore` file do?
- A. Stops tracked files from changing
- B. Deletes files that match its patterns
- C. Stops git from tracking untracked files that match its patterns
- D. Encrypts the listed files

**11.** What does `git revert HEAD` do?
- A. Deletes the last commit from history
- B. Moves your files back without recording anything
- C. Creates a **new** commit that undoes the changes of the last commit
- D. Unstages everything

**12.** What is `2 ** 3` in Python?
- A. 6
- B. 5
- C. 9
- D. 8

**13.** What is `10 % 3`?
- A. 3
- B. 1
- C. 3.33
- D. 0

**14.** What is `"5" + "5"`?
- A. `10`
- B. A `TypeError`
- C. `'55'`
- D. `'5 5'`

**15.** What is `len({1, 1, 2})`?
- A. 3
- B. 1
- C. 2
- D. An error is raised

**16.** What is `[1, 2, 3][-1]`?
- A. `1`
- B. `[3]`
- C. An `IndexError`
- D. `3`

**17.** `t = (1, 2)` then `t[0] = 5`. What happens?
- A. `t` becomes `(5, 2)`
- B. A `TypeError`, because tuples are immutable
- C. `t` becomes `(5, 5)`
- D. A `KeyError`

**18.** `d = {"a": 1}` then `d["b"]`. What happens?
- A. It returns `None`
- B. It returns `0`
- C. A `KeyError`
- D. It adds `"b"` to `d`

**19.** What is `np.arange(0, 10, 2)`?
- A. `[0 2 4 6 8]`
- B. `[0 2 4 6 8 10]`
- C. `[2 4 6 8 10]`
- D. `[0 1 2 3 4]`

**20.** What does `pd.read_csv("data.csv")` return?
- A. A list of lists
- B. A NumPy array
- C. A dictionary
- D. A DataFrame

---

## Section B — 2 marks each

**21.** What does this print?
```python
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(4))
```
- A. `4`
- B. `24`
- C. `10`
- D. A `RecursionError`

**22.** What does this print?
```python
f = lambda x, y=1: x * 10 + y
print(f(2), f(2, 3))
```
- A. `21 21`
- B. `21 23`
- C. `20 23`
- D. A `TypeError`

**23.** What does this print?
```python
def g(*args):
    return len(args), sum(args)

print(g(1, 2, 3))
```
- A. `3 6`
- B. `[3, 6]`
- C. `6`
- D. `(3, 6)`

**24.** What does this print?
```python
s = "abcdefg"
print(s[1:5], s[::2])
```
- A. `bcde aceg`
- B. `bcdef aceg`
- C. `bcde bdf`
- D. `abcde aceg`

**25.** What does this print?
```python
a = [[1, 2], [3]]
b = a.copy()
b[0].append(9)
b.append([4])
print(len(a), a[0])
```
- A. `3 [1, 2]`
- B. `3 [1, 2, 9]`
- C. `2 [1, 2, 9]`
- D. `2 [1, 2]`

**26.** What does this print?
```python
print({k: v for k, v in zip("abc", range(3)) if v > 0})
```
- A. `{'a': 0, 'b': 1, 'c': 2}`
- B. `{'b', 'c'}`
- C. `[('b', 1), ('c', 2)]`
- D. `{'b': 1, 'c': 2}`

**27.** What does this print?
```python
A = np.arange(6).reshape(2, 3)
print(A + np.array([10, 20, 30]))
```
- A. `[10 21 32]`
- B. `[[10 21 32] [13 24 35]]`
- C. `[[10 11 12] [23 24 25]]`
- D. A `ValueError`, because the shapes differ

**28.** What does this print?
```python
x = np.arange(5)
y = x[1:4]
y[0] = 99
print(x)
```
- A. `[ 0 99  2  3  4]`
- B. `[0 1 2 3 4]`
- C. `[99  1  2  3  4]`
- D. `[ 1 99  3]`

**29.** You edit `a.txt`, run `git add a.txt`, then edit `a.txt` **again** without adding. What does `git status` show?
- A. `a.txt` as staged only, and the second edit is lost
- B. `a.txt` as modified only
- C. `a.txt` under **both** "changes to be committed" and "changes not staged"
- D. `a.txt` as untracked

**30.** The current directory has a file `a.txt` and an **existing** directory `notes/`. You run `mv a.txt notes`. What happens?
- A. `a.txt` is renamed to `notes`
- B. An error is raised
- C. A copy goes into `notes/` and `a.txt` stays
- D. `a.txt` is moved inside `notes/`
