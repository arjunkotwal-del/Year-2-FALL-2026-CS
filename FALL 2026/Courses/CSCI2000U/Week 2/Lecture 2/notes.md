# Lecture 4 — Files, Version Control, and git (CSCI2000U)

## Learning outcomes / outline
1. Working with files
2. What is version control?
3. Versioning filesystem
4. Branches
5. Types of version control
6. Intro to git

## Working with files — key commands
| Command | Purpose |
|---|---|
| `cp <source> <target>` | Copy a file; target can be a file or directory |
| `cp <source1> <source2> <target>` | Copy multiple files into a target directory |
| `cp -r <source> <target>` | Recursively copy a directory **and itself** into target (creates `target/source/...`) |
| `cp -r <source>/ <target>` | Recursively copy the **contents** of source into target (no extra nested folder) — note the trailing `/` |
| `mv <source> <target>` | Move a file/directory to a target file or directory |
| `mv <old> <new>` | Rename (mv with same directory, new name) |
| `mv <dir_1> <dir_2> <dir_dest>` | Move multiple items into a destination directory |
| `rm <path1> <path2>` | Remove files |
| `rmdir <dir>` | Remove an **empty** directory |
| `rm -r <dir>` | Remove a non-empty directory recursively |
| `tree` | Visualize a directory as a tree (native on Windows/some Linux distros; on macOS install via Homebrew) |

**Trailing-slash trap**: `cp -r adir cdir` copies `adir` itself into `cdir` (→ `cdir/adir/...`). `cp -r adir/ cdir` copies just adir's *contents* into `cdir` (→ `cdir/a.txt`, `cdir/subdir/...`). This is a classic marks-losing mistake — always check for the trailing slash.

## What is version control?
- The practice of tracking and managing changes to code, documents, and other assets — a.k.a. "source control"
- Version control software tracks changes in a database
- Lets a developer "undo" — compare earlier versions, fix mistakes, while minimizing disruption to collaborators

## Versioning filesystem (VFS) concepts
- A **versioning file system** allows a file to exist in several versions at the same time (a form of revision control) — Wikipedia
- Recall: a normal filesystem is a tree of nodes (files/directories); each node has metadata (name, permission, modified date)
- A **versioned filesystem** extends this: instead of one tree, you have a *sequence of filesystem snapshots over time*, `FS(t=1)`, `FS(t=2)`, ... each one a full tree at that point in time
- Usually `FS(i+1)` is just an incremental modification of `FS(i)`, not a totally different tree
- Why we need it: technology is trial and error — versioning lets you reliably recover from mistakes, and lets you look up the modification history of an individual file (e.g., "how many times has `assignment_1.py` been modified?")
- Key terminology introduced: **commit**, **head** (defined more fully in the git lectures to come)

## Versioning vs. backups
| Backups | Versioned filesystem |
|---|---|
| Occur on a timed basis | Occurs when the file actually changes |
| Typically system-wide | On a file-by-file basis |
| Written to separate media | Written to the same disk, usually same directory |

## Coming up
This lecture sets up the concepts (branches, types of VC, git basics) that the next lectures (L05–L07: Gitting Started, Common git, History/Undo) build on directly.
