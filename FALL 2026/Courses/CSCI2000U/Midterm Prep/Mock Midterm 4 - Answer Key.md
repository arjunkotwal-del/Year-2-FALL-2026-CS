# Mock Midterm 4 — Answer Key
*Don't open this until you've finished the mock.*

**Scoring:** A = 12, B = 8, C = 12, D = 8. Total 40.

## Quick key (MCQ)

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 1 | B | 5 | B | 9 | B | 13 | A |
| 2 | C | 6 | B | 10 | B | 14 | B |
| 3 | A | 7 | B | 11 | C | 15 | D |
| 4 | A | 8 | C | 12 | D | 16 | B |

---

## Explanations (MCQ)

**1. B.** `-a` shows all files, including hidden ones (names starting with `.`).

**2. C.** `-p` creates the missing parent directories one by one, and it doesn't complain if they already exist.

**3. A.** `mv` onto a name that doesn't exist is a **rename**. (If `old.txt` were an existing directory, the file would move *inside* it.)

**4. A.** 7 = rwx, 5 = r-x, 5 = r-x, so `rwxr-xr-x`.

**5. B.** The flow is working directory -> **staging area** -> repository.

**6. B.** `git clone` copies a remote repo with its full history. `git init` is the one that turns the current folder into a repo.

**7. B.** `git diff --staged` shows staged vs the last commit. Plain `git diff` is working copy vs staging area.

**8. C.** `//` is floor division: `7 // 2` is 3.

**9. B.** `/` always gives a float: `3 / 2` is `1.5`.

**10. B.** `[-2:]` starts at the second-last character and runs to the end: `'on'`.

**11. C.** `|` is union, and a set keeps unique values only: `{1, 2, 3}`.

**12. D.** `reshape(2, 3)` gives 2 rows and 3 columns: shape `(2, 3)`.

**13. A, `6 12`.** `f(3)` uses the default `y=2` so it gives 6. `f(3, y=4)` gives 12. (Verified.)

**14. B, `bANANa 3`.** `replace("an", "AN")` swaps every `an` for `AN`: `b` `AN` `AN` `a`. `count("a")` counts the three `a`s in the original string. `s` itself is unchanged because strings are immutable. (Verified.)

**15. D, `4 3`.** `b = a` is the **same list**, so `b.append(4)` changes `a` too (length 4). `c = a.copy()` was made before the append and is independent (length 3). (Verified.)

**16. B, `[5 7 9] [2 5]`.** `axis=0` gives one result **per column**: 1+4, 2+5, 3+6. `M[:, 1]` is the second column: `[2 5]`. (`axis=1` would give `[ 6 15]`.) (Verified.)

---

## Section C — Marking guide (3 marks each)

**17.** (1 mark each)
- `cp -r adir cdir` copies the **directory itself** into `cdir`, so `a.txt` ends up at `cdir/adir/a.txt`.
- `cp -r adir/ cdir` (trailing slash) copies the **contents** of `adir` into `cdir`, so `a.txt` ends up at `cdir/a.txt`.
- Mentions that this is the slides' (macOS) behaviour. GNU/Linux tools may treat the trailing slash differently, but the exam follows the slides.

**18.** (1 mark each)
- The three areas: **working directory**, **staging area** (index), **repository** (`.git`).
- `git add` moves changes from the working directory **into the staging area** (a snapshot of the file as it is at that moment).
- `git commit` moves the staged snapshot **into the repository** as a new commit.

**19.** (1 mark each)
- `list.sort()` sorts **in place** and returns `None`, so `y` is `None` while `x` is now sorted.
- Fix 1: `x.sort()` and then use `x`.
- Fix 2: `y = sorted(x)`, which returns a **new** sorted list and leaves `x` unchanged.

**20.** (1 mark each)
- `axis=0` collapses the **rows** and gives **one result per column**: shape `(3,)`.
- `axis=1` collapses the **columns** and gives **one result per row**: shape `(2,)`.
- Gives a correct small example, e.g. `[[0 1 2],[3 4 5]]` gives `[3 5 7]` for `axis=0` and `[3 12]` for `axis=1`.

(Note: the lecture slide wording for `axis=0` is misleading. Use "one per column".)

---

## Section D — Marking guide (4 marks each)

**21. Model answer**
```python
def count_vowels(s):
    n = 0
    for ch in s.lower():
        if ch in "aeiou":
            n += 1
    return n

count_vowels("Data Science")   # 5
```
- 1 mark: correct `def` and a counter starting at 0.
- 1 mark: a loop over the characters.
- 1 mark: a correct vowel test and increment, and `return n` **after** the loop.
- 1 mark: states `5` (the vowels are a, a, i, e, e) and explains that `s.lower()` converts to lowercase so `D` and `S` and any capital vowels are handled. (Verified.)

Common error: putting `return` inside the loop, which stops after the first character.

**22. Model answer**
```python
import csv

scores = [("Ada", 90), ("Lin", 85)]

with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(scores)

with open("scores.csv", "r", newline="") as f:
    for row in csv.reader(f):
        print(row)
```
Output: `['name', 'score']`, `['Ada', '90']`, `['Lin', '85']`.

- 1 mark: `with open(..., "w", newline="")` and a `csv.writer`.
- 1 mark: writes the header row and the data rows.
- 1 mark: reads the file back with `"r"` and `csv.reader` and prints each row.
- 1 mark: numbers come back as **strings** (`'90'`, not `90`), and opening with `"w"` again **erases the existing contents**. (Verified: the file contained `name,score`, `Ada,90`, `Lin,85`.)

---

## Self-diagnosis

| If you missed... | Review |
|---|---|
| 1-4, 17 | L03-L04 shell, `mv`, `cp -r`, permissions |
| 5-7, 18 | L05-L07 git areas, `clone`, `diff --staged` |
| 8-10, 13, 14, 21 | L08-L10 Python basics, strings, functions, loops |
| 11, 15, 19 | L11 sets, aliasing vs copying, `sort` vs `sorted` |
| 12, 16, 20 | L12-L13 NumPy shape, `axis` |
| 22 | L14 files, `csv`, modes |

Tell me your score per section and which written answers felt weak, and I'll drill those.
