# Mock Midterm 2 — Answer Key
*Don't open this until you've finished the mock.*

**Scoring:** Section A is 20 marks (1 each). Section B is 20 marks (2 each). Total 40.

## Quick key

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 7 | C | 13 | B | 19 | B | 25 | A |
| 2 | C | 8 | B | 14 | A | 20 | B | 26 | B |
| 3 | B | 9 | B | 15 | B | 21 | B | 27 | B |
| 4 | C | 10 | B | 16 | C | 22 | B | 28 | B |
| 5 | B | 11 | C | 17 | C | 23 | A | 29 | B |
| 6 | B | 12 | B | 18 | A | 24 | B | 30 | B |

---

## Explanations

### Section A

**1. B.** Tuples are immutable lists (static arrays). Lists are mutable. (L11)

**2. C.** A set is an unordered collection of **unique** objects. (L11)

**3. B.** `pop()` removes the **tail** (last item) and hands the value back. You can pass an index to pop a different position. (L11)

**4. C.** `sort()` modifies the list **in place**. `sorted()` returns a **new** list and leaves the original alone. (L11 slides 22-23)

**5. B.** Keys must be unique. A repeated key hashes to the same location, so the new value **overwrites** the old one (verified: `{'a':1,'b':2,'a':3}` gives `{'a': 3, 'b': 2}`). (L11 slide 35)

**6. B.** `del d['a']` removes the pair. `pop()` with no key is a list method, and `remove` is not a dict method. (L11 slide 37)

**7. C.** `items()` yields `(key, value)` tuples. `keys()` and `values()` give only one half. (L11 slide 38)

**8. B.** `set()` wrapped around an object returns only the unique values: `{1, 2, 3}`. (L11 slide 44; TE6 2a)

**9. B.** Arrays are **homogeneous** and stored in a **contiguous** block of memory. Lists are heterogeneous pointers to scattered objects. This is one reason NumPy is faster. (L12 slide 9)

**10. B.** Vectorized operations avoid explicit loops, but they are **not** asymptotically faster: adding 5 to 100 elements is still O(n) either way. They're often orders of magnitude faster in practice because they run in C on contiguous memory. (L12 slides 4, 8)

**11. C.** `shape` is a **tuple** of dimension sizes (e.g. `(2, 3)`). `ndim` is the integer number of dimensions. (L12 slide 18)

**12. B.** The first argument is a tuple giving the shape, so `(2, 3)` is 2 rows by 3 columns of zeros. (L12 slide 21)

**13. B.** `linspace` gives evenly spaced floats. `arange` gives integer-style ranges by a step. (L12 slides 22-23)

**14. A.** Compare shapes from the **right**; dimensions are compatible if equal or one of them is 1 (the 1 is stretched). (L12 slide 29, L13 slide 9)

**15. B.** A view "sees" the same data rather than owning a copy, so changing one changes the other. Both point to the same place in memory. (L13 slides 18-21; slide 35 answer)

**16. C.** `copy()` makes an independent (deep) copy. `view()`, plain slicing, and `ravel()` all give views. (L13 slides 18-25)

**17. C.** `flatten()` returns a **copy**; `ravel()` returns a **view** (when possible). (L13 slides 31-32; I verified `np.shares_memory`: flatten False, ravel True)

**18. A.** `reshape()` returns a **view** with the new shape and does not modify the original. `resize()` is the one that changes the array in place. (L13 slides 28-30)

**19. B.** Data wrangling/munging is turning messy data into a clean dataset, and it can be over 80% of a project's time. (L14 slide 10)

**20. B.** The `with` statement acquires the resource and **closes it automatically** when the block ends. (L14 slide 27)

### Section B

**21. B, `['banana', 'apple', 'pear', 'peach']`.** Work inside out: `fruits.pop()` removes and returns `'banana'`. Then `insert(0, 'banana')` puts it at the head. This is the class challenge from L11. (L11 slide 49)

**22. B.** `d["y"] = 20` overwrites `y`. `d["z"] = 3` adds a new key. `del d["x"]` removes `x`. Left: `y` and `z`. (L11)

**23. A, `(3, 4)`.** Compare right to left: `(3,1)` vs `(4,)` -> last dims 1 and 4 (one is 1, stretched to 4); then 3 vs (missing, treated as 1) -> 3. Result `(3, 4)`. This is TE6 5c. (L12 slides 28-30; TE6)

**24. B, `[1.5 2.5 3.5]`.** `axis=0` collapses the **rows**, giving one result **per column**: columns are (0,3), (1,4), (2,5), with means 1.5, 2.5, 3.5. (`axis=1` would give `[1. 4.]`, one result per row.)

> [!warning] The slide wording is misleading here
> L12 slide 34 says axis=0 "takes the mean across all the row values". Ignore that phrasing and use the rule that works: **`axis=0` gives one value per column; `axis=1` gives one value per row.** TE6 5b agrees: `U.mean(axis=0)` is "column-wise means".

**25. A.** `B[0, :]` is a slice, and **slices are views**. Setting `row[:] = 9` changes `B` itself: `[[9 9 9] [3 4 5]]`. (L13 slide 23; TE6 4c)

**26. B, `0 -1`.** `copy()` is independent, so `C[:,0] = -1` changes `C` only. `B[0,0]` is still 0. (L13 slide 25; TE6 4d)

**27. B, `[3 5]`.** `x > 0` builds a boolean mask `[True False True False False]` (that's option A, the mask itself). Indexing with the mask picks only the `True` positions. (TE6 5a)

**28. B.** `git restore <file>` (without `--staged`) **discards working-directory edits**, so the file returns to the committed version and the tree is clean. Careful: this is the destructive form, unlike `restore --staged`. (TE3 6, TE4 3b; I verified in a real repo)

**29. B.** `git revert` creates a **new commit** that undoes an earlier one. It does not rewrite history, so the log goes from 3 commits to 4 (verified: the new commit is titled `Revert "C"`). `--no-edit` just skips the message editor. (TE4 3c)

**30. B.** Opening in `"w"` mode **deletes all existing data** in the file, even if you write nothing. (I verified: a 19-byte file became 0 bytes.) Use `"a"` to append. (L14 slide 28)

---

## Self-diagnosis

| If you missed... | You need to review |
|---|---|
| 1-8, 21, 22 | L11 lists, tuples, dicts, sets |
| 9-18, 23-27 | L12-L13 NumPy (attributes, broadcasting, axis, views vs copies) |
| 19, 20, 30 | L14 data science process, files |
| 28, 29 | git undo (TE3, TE4) |

Tell me your score per block and I'll teach and drill the weakest one.
