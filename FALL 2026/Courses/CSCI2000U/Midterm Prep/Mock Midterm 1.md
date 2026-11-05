# CSCI2000U — Mock Midterm 1
**30 questions · 40 marks** (Section A: 20 x 1 mark · Section B: 10 x 2 marks) · all multiple choice

> [!note] Coverage
> This mock covers **L02–L10b** (shell, git, Python basics, strings). The real midterm covers **L01–L14**, so Mock 2 will cover L11–L14 (data structures, NumPy, data science).

> [!warning] Rules for this to be worth anything
> - Closed book. Use only your one-page cheat sheet. Time yourself: **60 minutes**.
> - Write your answers on paper first, then check against **Mock Midterm 1 - Answer Key.md**.
> - For every miss, write one line on *why* you picked the wrong option. That line is the real study.
> - Section B questions are the ones he wrote like "it comes down to A or B" — slow down and trace them.

---

## Section A — 1 mark each

**1.** Which of the following is a Unix **shell**?
- A. Konsole
- B. Bash
- C. xterm
- D. Terminal (the macOS app)

**2.** Which command shows the shell program you are currently running?
- A. `pwd`
- B. `whoami`
- C. `echo $0`
- D. `man shell`

**3.** Which command lists the contents of the **parent** directory?
- A. `ls .`
- B. `ls ~`
- C. `ls ..`
- D. `cd ..`

**4.** In `chmod` absolute (octal) mode, what does the digit **7** mean?
- A. read only
- B. read and write
- C. read, write, and execute
- D. execute only

**5.** Which of these is **not** one of the three permission classes?
- A. user
- B. group
- C. other
- D. admin

**6.** Which command removes a **non-empty** directory called `foo`?
- A. `rmdir foo`
- B. `rm foo`
- C. `rm -r foo`
- D. `mv foo`

**7.** How does git store the history of a project?
- A. As a list of line-by-line differences (deltas) between versions
- B. As a stream of snapshots
- C. As one backup zip file per day
- D. As only the latest copy of every file

**8.** Which are git's three main file states?
- A. new, old, deleted
- B. modified, staged, committed
- C. local, remote, cloud
- D. tracked, ignored, hidden

**9.** What does `git clone <repo>` do?
- A. Converts the current directory into a new repository
- B. Downloads a copy of an existing repository
- C. Uploads your commits to the remote
- D. Creates a new branch

**10.** To authenticate with GitHub using SSH, which key do you add to your GitHub profile?
- A. The private key
- B. The public key
- C. Both keys
- D. Neither, you use your password

**11.** A full git commit hash is a hexadecimal string of how many characters?
- A. 8
- B. 16
- C. 40
- D. 256

**12.** In git, what is `HEAD`?
- A. The very first commit in the repository
- B. A pointer to the commit you are currently focused on (normally via the current branch)
- C. The staging area
- D. The remote copy of the repository

**13.** What state is a file in right after it has been committed?
- A. untracked
- B. modified
- C. staged
- D. unmodified

**14.** What does `git restore --staged notes.txt` do?
- A. Deletes `notes.txt` from disk
- B. Removes it from the staging area but leaves your edits in the working directory
- C. Discards your edits to `notes.txt`
- D. Creates a new commit containing `notes.txt`

**15.** Where should the `.gitignore` file be placed?
- A. Inside the `.git/` folder
- B. In the root of the working directory
- C. In your home directory only
- D. Inside every commit

**16.** What does plain `git diff` (no options) compare?
- A. The working directory against the staging area
- B. The staging area against the last commit
- C. The last commit against the previous commit
- D. Your local repo against the remote

**17.** In what order does `git log` list commits?
- A. Oldest first
- B. Newest first
- C. Alphabetically by message
- D. By file size

**18.** Given `s = "Hello"`, which line raises an error in Python?
- A. `s = s + "!"`
- B. `s = "J" + s[1:]`
- C. `s[0] = "J"`
- D. `print(s[0])`

**19.** Python is best described as:
- A. statically and weakly typed
- B. dynamically and strongly typed
- C. statically and strongly typed
- D. dynamically and weakly typed

**20.** What does a Python function with **no** `return` statement give back?
- A. `0`
- B. `""` (empty string)
- C. `None`
- D. It raises an error

---

## Section B — 2 marks each

**21.** The directory tree is:
```
/
└── home
    └── sam
        ├── docs
        │   └── notes
        └── data
```
Your present working directory is `/home/sam/docs`. You run:
```
cd ../data/../docs/notes
```
Where are you now?
- A. `/home/sam/docs/notes`
- B. `/home/sam/data`
- C. `/home/sam/docs`
- D. The command fails

**22.** Using the behaviour shown in the lecture slides, the tree is:
```
.
├── adir
│   ├── a.txt
│   └── subdir
│       └── subtxt.txt
└── cdir
    └── ctxt.txt
```
After `cp -r adir/ cdir`, what is inside `cdir`?
- A. Only `ctxt.txt`
- B. `ctxt.txt`, `a.txt`, `subdir/subtxt.txt` (the contents of `adir`, with no extra `adir` folder)
- C. `ctxt.txt` and a new folder `adir` containing `a.txt` and `subdir/`
- D. The command fails because `cdir` already exists

**23.** After `chmod 640 report.txt`, which permission string would `ls -l` show for the file?
- A. `-rw-r--r--`
- B. `-rw-r-----`
- C. `-rwxr-----`
- D. `-rw-rw----`

**24.** In a repo that already has commits, you run these steps in order:
```
echo 'a' > a_file.txt
git add a_file.txt
echo 'b' >> a_file.txt
git restore --staged a_file.txt
```
What state is `a_file.txt` in, and what does it contain?
- A. staged, containing `a`
- B. untracked, containing `a` and `b` (two lines)
- C. modified, containing `a` and `b`
- D. untracked, containing only `a`

**25.** You run:
```
echo 'v1' > new.txt
git add new.txt
echo 'v2' >> new.txt
git commit -m "add new"
```
Which statement is true?
- A. The commit contains both `v1` and `v2`
- B. The commit contains only `v1`; the `v2` line is still an unstaged change
- C. The commit fails because the file changed after `git add`
- D. The commit contains only `v2`

**26.** `git log --oneline` shows (newest first):
```
f4a1c9e Add plots
3b7d2a0 Fix typo
91e5c68 Add readme
0d2f4b1 Initial commit
```
What does `git show --format=oneline HEAD~2` display the commit message of?
- A. Add plots
- B. Fix typo
- C. Add readme
- D. Initial commit

**27.** What is the exact output of this code?
```python
print("x", "y", "z", sep="-", end="!")
print("end")
```
- A. `x-y-z!` on one line, then `end` on the next line
- B. `x-y-z!end`
- C. `x y z!end`
- D. `x-y-z end`

**28.** What does this print?
```python
word = "strawberry"
print(word[1:8:3])
```
- A. `twr`
- B. `sae`
- C. `rbr`
- D. `trawber`

**29.** What does this evaluate to?
```python
"ahahaha".count("aha")
```
- A. 1
- B. 2
- C. 3
- D. 4

**30.** What is printed?
```python
x = 85
if x >= 80:
    print("A")
if x >= 70:
    print("B")
else:
    print("C")
```
- A. `A` only
- B. `A` then `B` (on separate lines)
- C. `B` only
- D. `A`, `B`, and `C`
