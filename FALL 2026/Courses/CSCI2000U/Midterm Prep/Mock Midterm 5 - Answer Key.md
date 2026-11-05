# Mock Midterm 5 — Answer Key
*Don't open this until you've finished the mock.*

**Scoring:** Section A = 20 (1 each), Section B = 20 (2 each). Total 40.

## Quick key

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 7 | A | 13 | B | 19 | A | 25 | C |
| 2 | C | 8 | D | 14 | C | 20 | D | 26 | D |
| 3 | A | 9 | B | 15 | C | 21 | C | 27 | B |
| 4 | D | 10 | C | 16 | D | 22 | B | 28 | A |
| 5 | B | 11 | C | 17 | B | 23 | D | 29 | C |
| 6 | C | 12 | D | 18 | C | 24 | A | 30 | D |

---

## Section A explanations

**1. B.** `pwd` = print working directory, as an absolute path.

**2. C.** `cd -` jumps back to the previous directory. (`cd ~` is home, `cd ..` is up one.)

**3. A.** `-r` is recursive, so the directory and all its contents are removed. Plain `rm` can't remove a directory.

**4. D.** `>` **overwrites**; `>>` appends. The file now holds only `hi`.

**5. B.** 6 = rw-, 4 = r--, 4 = r--, so `rw-r--r--`.

**6. C.** Data wrangling takes the largest share of time (the slides say well over 80%).

**7. A.** `git add` on a new file moves it from untracked to **staged**.

**8. D.** `git restore --staged f` unstages but keeps your edits. `git restore f` (without `--staged`) is the one that discards edits.

**9. B.** `--cached` means "only the git side". The file is untracked but stays on disk. Pair it with a `.gitignore` entry.

**10. C.** `.gitignore` only affects **untracked** files. Files already tracked stay tracked until you `git rm --cached` them.

**11. C.** `git revert` adds a **new** commit that undoes an old one. The log grows, history is not erased.

**12. D.** `**` is exponent: 2 to the power 3 = 8.

**13. B.** `%` is the remainder: 10 = 3 x 3 + 1.

**14. C.** `+` on two strings concatenates: `'55'`.

**15. C.** A set keeps unique values: `{1, 2}` has length 2.

**16. D.** Index `-1` is the last item: `3` (not `[3]`).

**17. B.** Tuples are immutable, so item assignment raises a `TypeError`.

**18. C.** Looking up a missing key with `[]` raises `KeyError`. (`d.get("b")` would return `None`.)

**19. A.** `arange(start, stop, step)` stops **before** `stop`: `[0 2 4 6 8]`.

**20. D.** `pd.read_csv` returns a pandas **DataFrame**.

---

## Section B explanations

**21. C, `10`.** `total(4)` = 4 + 3 + 2 + 1 + 0 = 10. The base case `n == 0` stops the recursion. (Verified.)

**22. B, `21 23`.** `f(2)` uses the default `y=1`: 2x10+1 = 21. `f(2, 3)` = 20+3 = 23. (Verified.)

**23. D, `(3, 6)`.** `*args` is a **tuple** `(1, 2, 3)`. Returning two values returns a tuple, which prints as `(3, 6)`. (Verified.)

**24. A, `bcde aceg`.** `s[1:5]` is indexes 1 to 4 (stops **before** 5): `bcde`. `s[::2]` takes every second character from the start: `aceg`. (Verified.)

**25. C, `2 [1, 2, 9]`.** `copy()` is a **shallow** copy, so the inner list is shared: `b[0].append(9)` changes `a[0]` too. But `b.append([4])` only changes `b`, so `len(a)` is still 2. (Verified.)

**26. D, `{'b': 1, 'c': 2}`.** `zip` pairs `a-0, b-1, c-2`; the condition `v > 0` drops `a`. Curly braces with `k: v` make a dict. (Verified.)

**27. B.** Broadcasting: shapes `(2,3)` and `(3,)` compare from the right (3 vs 3, equal), so the row `[10 20 30]` is added to **each row**: `[[10 21 32] [13 24 35]]`. (Verified.)

**28. A, `[ 0 99  2  3  4]`.** A slice is a **view**, so writing through `y` changes `x`. (Verified.)

**29. C.** `git add` stages a **snapshot** of the file at that moment. The later edit is only in the working directory, so the file is "staged **and** modified".

**30. D.** `mv` onto an **existing directory** moves the file inside it (`notes/a.txt`). It only renames when the destination does not exist.

---

## Self-diagnosis

| If you missed... | Review |
|---|---|
| 1-5, 30 | L02-L04 UNIX commands, `>` vs `>>`, `mv`, permissions |
| 7-11, 29 | L05-L07 and TE3/TE4: git areas, `restore`, `rm --cached`, `.gitignore`, `revert` |
| 12-19, 24 | L08-L11 Python basics, strings, tuples, dicts, sets |
| 21-23, 26 | TE5: recursion, lambda, `*args`, comprehensions |
| 25 | L11 aliasing vs shallow copy |
| 19, 27, 28 | L12-L13 NumPy: `arange`, broadcasting, views |
| 6, 20 | L14 data science process, pandas |

Tell me your score for A and B (and the numbers you missed) and I'll drill those topics.
