# Mock Midterm 3 — Answer Key
*Don't open this until you've finished the mock.*

**Scoring:** A = 12, B = 8, C = 12, D = 8. Total 40.

## Quick key (MCQ)

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 1 | C | 5 | C | 9 | B | 13 | C |
| 2 | C | 6 | B | 10 | C | 14 | A |
| 3 | A | 7 | B | 11 | C | 15 | B |
| 4 | C | 8 | C | 12 | B | 16 | B |

---

## Explanations (MCQ)

**1. C.** `pwd` = print working directory.

**2. C.** A relative path doesn't start with `/`. `..` means the parent folder.

**3. A.** 6 = rw-, 4 = r--, 0 = ---, so `rw-r-----`.

**4. C.** `git add` stages the file as it is at that moment. The later edit is a separate, unstaged change, so the file is both staged and modified.

**5. C.** `.gitignore` only affects **untracked** files. To untrack a committed file use `git rm --cached` as well.

**6. B.** Indexes 1 and 2 (the end index 3 is excluded): `'el'`.

**7. B.** Python refuses to silently mix types, so it is **strongly** typed. (It is also dynamically typed, but that isn't what the error shows.)

**8. C.** `list.sort()` sorts in place and **returns `None`**, so `y` is `None`. (Verified: `x` becomes `[1, 2, 3]`.)

**9. B.** A set keeps unique values only: `{1, 2, 3}` has length 3.

**10. C.** `*args` collects the extra positional arguments into a **tuple**.

**11. C.** `flatten()` returns a copy. `ravel()`, `reshape()` and `view()` give views.

**12. B.** `with` releases the resource: the file is closed automatically at the end of the block.

**13. C, 24.** `fact(4) = 4 * 3 * 2 * 1`. The base case is `n <= 1`. (Verified.)

**14. A, `1 4 7`.** `range(1, 10, 3)` starts at 1 and steps by 3, stopping before 10. (Verified.)

**15. B, `[ 6 22]`.** `axis=1` gives one result **per row**: 0+1+2+3 = 6 and 4+5+6+7 = 22. (`axis=0` would give `[ 4  6  8 10]`, one per column.) (Verified.)

**16. B.** The key is the negative length, so the longest string sorts first: `['ccc', 'bb', 'a']`. (Verified.)

---

## Section C — Marking guide (3 marks each)

**17.** (1 mark each)
- `git restore --staged a.txt` **unstages** the file: it leaves the staging area.
- It **keeps your edits** in the working copy.
- `git restore a.txt` **discards the working edits completely**; the file returns to the last committed version and the edits can't be recovered.

**18.** (1 mark each)
- (a) **750**: owner rwx = 7, group r-x = 5, others --- = 0.
- Owner can read, write and execute. Group can read and execute but **not write**. Everyone else has **no access**.

**19.** (1 mark each for any three of these)
- A **view** shares the same memory as the original, so changing it **changes the original**.
- A **copy** is independent, so changing it does **not** change the original.
- Operations that return views: slicing, `view()`, `reshape()`, `ravel()`. Operations that return copies: `copy()`, `flatten()`.
- Give 1 mark for a correct pairing of an operation with its behavior, and 1 mark for stating what happens to the original.

**20.** (1 mark each: definition of dynamic, definition of strong, and examples)
- **Dynamically typed:** a variable's type is decided at run time by its value and can change, e.g. `x = 5` then `x = "hi"` is allowed.
- **Strongly typed:** Python won't silently convert between unrelated types, e.g. `"5" + 3` raises a `TypeError`.

---

## Section D — Marking guide (4 marks each)

**21. Model answer**
```python
def average(*args):
    if len(args) == 0:
        return None
    return sum(args) / len(args)

average(2, 4, 9)   # 5.0
average()          # None
```
- 1 mark: correct `def` with `*args`.
- 1 mark: handles the empty case and returns `None`.
- 1 mark: correct mean (`sum(args) / len(args)`).
- 1 mark: states both call results (`5.0` and `None`). (Verified.)

Any equivalent solution is fine (a loop, `if not args`, and so on). Don't deduct for small syntax slips; the prof says concepts matter more.

**22. Model answer**
```
git rm --cached secret.env
echo "secret.env" >> .gitignore
git add .gitignore
git commit -m "stop tracking secret.env"
```
- 1 mark: `git rm --cached secret.env` stops tracking but **keeps the file on disk** (plain `git rm` would delete it).
- 1 mark: adding `secret.env` to `.gitignore` so it is never added again.
- 1 mark: `git add .gitignore` (or committing both changes) so the ignore rule is saved.
- 1 mark: `git commit` to record the change.

Common error: using only `.gitignore`. It does nothing for a file that is already tracked.

---

## Self-diagnosis

| If you missed... | Review |
|---|---|
| 1-3, 18 | L02-L04 paths, `chmod`, permissions |
| 4, 5, 17, 22 | L05-L07 git states, `restore`, `rm --cached`, `.gitignore` |
| 6-8, 20 | L08-L10 Python basics, strings, typing |
| 9, 10, 13, 14, 16, 21 | L11 data structures, TE5 loops, recursion, lambda, `*args` |
| 11, 15, 19 | L12-L13 NumPy: `axis`, views vs copies |
| 12 | L14 files and `with` |

Tell me your score per section and which written answers felt weak, and I'll drill those.
