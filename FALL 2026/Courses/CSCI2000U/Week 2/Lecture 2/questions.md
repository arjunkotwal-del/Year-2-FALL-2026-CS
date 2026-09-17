# Lecture 4 — Questions / Self-check

1. What's the difference between `cp -r adir cdir` and `cp -r adir/ cdir`?
2. How do you rename a file using `mv`?
3. What's the difference between `rmdir` and `rm -r`?
4. Define "version control" in one sentence.
5. What is a versioning filesystem, per the lecture's definition?
6. Why isn't a versioned filesystem the same thing as a periodic backup? Give two differences.
7. Why do we need versioning at all — what problem does it solve?
8. In `FS(t=1)`, `FS(t=2)`, ..., what's usually true about the relationship between `FS(i)` and `FS(i+1)`?

## Answers (self-check after review)
1. `cp -r adir cdir` copies the `adir` folder itself into `cdir` (result: `cdir/adir/...`); `cp -r adir/ cdir` copies only the contents of `adir` into `cdir` (result: `cdir/a.txt`, `cdir/subdir/...`, no extra nesting)
2. `mv oldname.ext newname.ext` (moving to the same location under a new name counts as a rename)
3. `rmdir` only removes a directory if it's already empty; `rm -r` removes a directory and everything inside it recursively
4. The practice of tracking and managing changes to code, documents, and other assets over time (a.k.a. source control)
5. Any filesystem that allows a computer file to exist in several versions at the same time — a form of revision control
6. Backups happen on a timed schedule and are usually system-wide, written to separate media; versioning happens whenever a file actually changes, on a per-file basis, written to the same disk/directory
7. Technology is trial and error — versioning gives a reliable way to recover from mistakes and to review a file's modification history
8. `FS(i+1)` is usually just an incremental modification of `FS(i)`, not an unrelated/completely different tree
