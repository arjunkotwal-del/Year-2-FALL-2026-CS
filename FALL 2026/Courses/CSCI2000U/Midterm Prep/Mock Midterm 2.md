# CSCI2000U — Mock Midterm 2
**30 questions · 40 marks** (Section A: 20 x 1 mark · Section B: 10 x 2 marks) · all multiple choice

> [!note] Coverage
> **L11–L14** (data structures, NumPy, views vs copies, data science process, CSV files) plus the git/tutorial material from TE3 and TE4. Do **Mock 1** for L02–L10b. The real exam covers L01–L14.

> [!warning] Rules
> Closed book except your one-page notes. **Time yourself: 60 minutes.** Write answers on paper, then check **Mock Midterm 2 - Answer Key.md**. For every miss, write one line on *why* you picked the wrong option.

---

## Section A — 1 mark each

**1.** Which Python built-in data structure is an **immutable** sequence?
- A. list
- B. tuple
- C. dict
- D. set

**2.** Which Python built-in data structure stores **unique, unordered** items?
- A. list
- B. tuple
- C. set
- D. string

**3.** What does `my_list.pop()` do by default?
- A. Removes the first item and returns it
- B. Removes the last item and returns it
- C. Removes the last item without returning it
- D. Removes all items

**4.** Which statement about `sort()` and `sorted()` on a list is correct?
- A. `sorted(my_list)` sorts the list in place; `my_list.sort()` returns a new list
- B. Both sort the list in place
- C. `my_list.sort()` sorts in place; `sorted(my_list)` returns a new sorted list and leaves the original unchanged
- D. Both return a new list and leave the original unchanged

**5.** What happens if you add a dictionary entry using a key that already exists?
- A. A second entry with the same key is created
- B. The new value overwrites the old value
- C. Python raises an error
- D. The new entry is ignored

**6.** Which statement removes the key-value pair with key `'a'` from a dictionary `d`?
- A. `d.remove('a')`
- B. `del d['a']`
- C. `d.pop()`
- D. `d['a'] = None`

**7.** Which dictionary method gives you each key-value pair as a tuple when looping?
- A. `keys()`
- B. `values()`
- C. `items()`
- D. `pairs()`

**8.** What is `set([1, 2, 2, 3, 3, 3])`?
- A. `{1, 2, 2, 3, 3, 3}`
- B. `{1, 2, 3}`
- C. `[1, 2, 3]`
- D. `{3: 3}`

**9.** Which describes the elements of a NumPy array compared to a Python list?
- A. Heterogeneous, stored as scattered pointers
- B. Homogeneous, stored in a contiguous block of memory
- C. Heterogeneous, stored contiguously
- D. Homogeneous, stored as scattered pointers

**10.** Which statement about vectorized (array) operations is true?
- A. They are asymptotically faster than loops (lower Big-O)
- B. They apply an operation to a whole array without an explicit loop, and are still O(n) but often much faster in practice
- C. They only work on one-dimensional arrays
- D. They modify the array's data type

**11.** What does the `shape` attribute of a NumPy array return?
- A. The number of dimensions as an integer
- B. The data type of the elements
- C. A tuple giving the size of each dimension
- D. The total number of elements

**12.** What does `np.zeros((2, 3))` create?
- A. A 2-element array containing the values 2 and 3
- B. A 2x3 array filled with zeros
- C. A 3x2 array filled with zeros
- D. A 1D array of six zeros

**13.** Which NumPy function creates an array of **evenly-spaced floating-point** values between two endpoints?
- A. `arange`
- B. `linspace`
- C. `zeros`
- D. `reshape`

**14.** Which are NumPy's broadcasting rules for compatibility? Comparing shapes from the right, two dimensions are compatible when:
- A. They are equal, or one of them is 1
- B. They are equal, or one of them is 0
- C. They are both even numbers
- D. They differ by exactly 1

**15.** Given `a = np.array([1, 2, 3])` and `b = a.view()`, what happens to `a` after `b[0] = 99`?
- A. Nothing, `a` is unchanged
- B. `a[0]` becomes 99, because `b` is a view of the same data
- C. `a` becomes `[99, 99, 99]`
- D. An error is raised

**16.** Which creates an array that is **independent** of the original (changing it won't change the original)?
- A. `a.view()`
- B. `a[:]`
- C. `a.copy()`
- D. `a.ravel()`

**17.** Which statement about `flatten()` and `ravel()` is correct?
- A. `flatten()` returns a view; `ravel()` returns a copy
- B. Both return views
- C. `flatten()` returns a copy; `ravel()` returns a view
- D. Both return copies

**18.** What does `reshape()` return?
- A. A view of the original data with the new shape; the original array is not modified
- B. Nothing; it changes the original array in place
- C. An independent deep copy
- D. A list

**19.** What is "data wrangling" (or data munging)?
- A. Plotting graphs of a clean dataset
- B. Turning messy data into a clean dataset, often the largest share of a project's time
- C. Fitting a machine-learning model
- D. Presenting results to a non-expert audience

**20.** What does the `with` statement do in `with open("data.csv", "r") as f:`?
- A. Reads the whole file into memory first
- B. Automatically closes the file (releases the resource) when the block ends
- C. Makes the file read-only for other programs permanently
- D. Creates the file if it doesn't exist

---

## Section B — 2 marks each

**21.** What is printed?
```python
fruits = ['apple', 'pear', 'peach', 'banana']
fruits.insert(0, fruits.pop())
print(fruits)
```
- A. `['apple', 'pear', 'peach', 'banana']`
- B. `['banana', 'apple', 'pear', 'peach']`
- C. `['pear', 'peach', 'banana', 'apple']`
- D. `['banana']`

**22.** What is printed?
```python
d = {"x": 1, "y": 2}
d["y"] = 20
d["z"] = 3
del d["x"]
print(list(d.items()))
```
- A. `[('x', 1), ('y', 20), ('z', 3)]`
- B. `[('y', 20), ('z', 3)]`
- C. `[('y', 2), ('z', 3)]`
- D. An error is raised

**23.** Given:
```python
p = np.array([[1], [2], [3]])      # shape (3, 1)
q = np.array([10, 20, 30, 40])     # shape (4,)
```
What is `(p + q).shape`?
- A. `(3, 4)`
- B. `(4,)`
- C. `(3, 1)`
- D. An error is raised because the shapes differ

**24.** What does this print?
```python
U = np.arange(6).reshape(2, 3)     # [[0 1 2], [3 4 5]]
print(U.mean(axis=0))
```
- A. `[1. 4.]`
- B. `[1.5 2.5 3.5]`
- C. `2.5`
- D. `[[0 1 2] [3 4 5]]`

**25.** What is printed?
```python
B = np.arange(6).reshape(2, 3)     # [[0 1 2], [3 4 5]]
row = B[0, :]
row[:] = 9
print(B)
```
- A. `[[9 9 9] [3 4 5]]`
- B. `[[0 1 2] [3 4 5]]`
- C. `[[9 9 9] [9 9 9]]`
- D. `[[9 1 2] [3 4 5]]`

**26.** What is printed?
```python
B = np.arange(6).reshape(2, 3)     # [[0 1 2], [3 4 5]]
C = B.copy()
C[:, 0] = -1
print(B[0, 0], C[0, 0])
```
- A. `-1 -1`
- B. `0 -1`
- C. `0 0`
- D. `-1 0`

**27.** What is printed?
```python
x = np.array([3, -1, 5, 0, -2])
print(x[x > 0])
```
- A. `[True False True False False]`
- B. `[3 5]`
- C. `[3 5 0]`
- D. `[0 -1 -2]`

**28.** In a repo, `README.md` is committed and clean. You run:
```
echo 'oops' >> README.md
git restore README.md
git status
```
What happens?
- A. `README.md` is deleted from the repository
- B. The edit is discarded and `git status` reports a clean working tree
- C. The edit is moved to the staging area
- D. The edit is kept but unstaged

**29.** A repo has three commits (A, B, C = `HEAD`). You run `git revert --no-edit HEAD`. Which is true?
- A. History rewinds, leaving only commits A and B
- B. There are now four commits; the newest one undoes the changes made by C
- C. Nothing changes until you run `git commit`
- D. Commit C is deleted from the log

**30.** `employees.csv` currently contains 100 rows. You run:
```python
with open("employees.csv", "w", newline="") as f:
    pass
```
What does `employees.csv` contain afterwards?
- A. The same 100 rows (nothing was written)
- B. Nothing; opening in `"w"` mode erased the existing contents
- C. The 100 rows plus one blank row
- D. The command fails because the file already exists
