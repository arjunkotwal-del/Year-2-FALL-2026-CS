# CSCI2000U Midterm — what the professor actually said
*Pulled from the lecture recordings (L02–L10b). Format: lecture + timestamp, so you can jump to the moment.*

**Midterm:** Wed Nov 4 · 40 marks · all MCQ (20 x 1 mark + 10 x 2 marks) · closed book · Respondus LockDown · one double-sided page of notes.

---

## 1. Scope and logistics (official: Canvas announcement "Midterm details", Oct 1)

> [!important] Coverage is **L01–L14**, not just L01–L10b
> "All lecture materials up to week 7, L01-14." That includes **L11 data structures, L12-L13 NumPy/array programming, L14 data science**. The recordings on Canvas only go to L10b/L11, but the exam goes further. In the L07 recording he also said "everything up until the midterm is what will be on the midterm" (L07 00:01:45).

| Item | Detail |
|---|---|
| Date / time | Wed **Nov 4**, **2:10pm**, **1 hour** |
| Place | North campus, **BIT2080** (the regular lecture room) |
| Format | Canvas quiz under "Assignments", Respondus LockDown browser |
| Allowed | Your **laptop**, plus **one page of notes** (US letter, single or double-sided, handwritten or printed, any layout) |
| **Appendix** | A **function reference guide is included with the exam**: UNIX / git / Python functions, each with its name and a brief description; Python functions also show the header (parameters). So you don't need to memorise signatures, you need to know **what things do and when to use them**. |
| Submission | Final once submitted. Due 3:15pm (2 minute grace), then **-25% per minute late**. Submit about 5 minutes early. |
| Prep | Turn laptop Wi-Fi off and on after entering the room (IT request). Fully charge, quit background apps. |

## 2. Best way to practise

> [!tip] Tutorial exercises and worksheets are "just like the exam"
> **L07 00:02:04–00:02:17.** He said the tutorials are "by far the best way to practice", and you get solutions. **TE1–TE6 plus the 5 posted solutions are downloaded** in `files/tutorials/`. Note TE5 (loops, recursion, lambdas, `*args`) and TE6 (lists, tuples, sets, dicts, **NumPy**) go beyond L10b, which fits the real L01–L14 scope.
>
> **Nuance from TE3 Q6 / TE4 Q3:** `git restore --staged <file>` is non-destructive (unstages only), but plain `git restore <file>` **discards your working-directory edits**. TE4 also uses `git revert --no-edit HEAD` (undo by making a new commit), `git show HEAD~1:readme.md`, and `git diff --staged`.

## 3. How he writes questions (the pattern)

He narrates how he thinks about MCQs while teaching. The pattern: **most options are easy to eliminate, and it comes down to an A-or-B decision on one detail.**

| Where | What he said | The trap |
|---|---|---|
| **L04 00:13:09–00:13:23** | `cp -r` is "like a multiple choice question — you're 80% of the way there... does it copy the folder and its contents or just the contents?" | **Trailing slash:** `cp -r adir cdir` copies the folder itself; `cp -r adir/ cdir` copies only the contents |
| **L09 00:25:19–00:25:56** | `print("The dog","ran over",sep="_",end="!")` — "classic multiple choice... it comes down to just A or B" | Know exactly what `sep` and `end` do and that `end="!"` means the **next** print continues on the same line |
| **L02 00:27:08–00:27:31** | Path questions: "you might look at it and go, oh, I see lots of a's and b's, I'll say 50-50" | Don't guess. **Walk the path step by step** from the starting point; a path can fail to resolve at some step |
| **L02 00:32:27–00:32:46** | A long `../` path that "goes nowhere... a full 360. A great quiz example question: where do I end up?" | Relative paths with `..` that cancel out and land you back where you started |
| **L10b 00:12:09–00:12:46** | `"ahahaha".count("aha")` — "this is a tricky one" (sliding window would give 3, but it's 2) | `count` is **non-overlapping**, not a sliding window |

## 4. Explicitly NOT on the exam

| Topic | Quote | Where |
|---|---|---|
| `git log --pretty=format` codes like `%h`, `%an` | "not the sort of thing that I would ever expect you to remember in an exam... just understand that you can format the output" | **L07 00:17:09** |
| Jupyter keyboard shortcuts | "not the sort of question that I'm going to put on an exam. You don't need to memorize keyboard shortcuts" | **L08 00:33:41** |
| SSH keys / setting up GitHub | "You just need to understand Git as a technology, and then the basics of it" (GitHub setup isn't needed for the course) | **L05 00:24:18** |

> [!note] Careful with the SSH one
> He says you don't need to *set up* SSH/GitHub. The L05 slides still cover public vs private keys conceptually, so I kept one easy conceptual question on it in the mocks. Don't spend time on `ssh-keygen` flags.

## 5. Things he flagged as important or worth knowing

- **Terminal vs shell vs command line (L03 ~00:10:00):** he called this "one of those knowledge things" that separates people who understand it from people who don't. Know: terminal (emulator) = the window; **shell = the program that runs commands**; CLI = the style of interface.
- **Restore vs checkout (L07 00:38:58–00:39:37):** `restore` is **non-destructive** (it just unstages); `checkout <file>` **discards your local changes**.
- **Staging snapshots the file at the moment of `git add` (L06 slide 33):** edit after adding and the file is both staged *and* modified. A commit takes the staged version.
- **Strings are immutable (L10 / L10b 00:07:22–00:08:38):** `s[0] = "J"` errors, but `s = "J" + s[1:]` works because you're making a **new** string, not editing the old one.
- **Slicing is [inclusive, exclusive] (L10b 00:04:40–00:05:17).**
- **Parameters vs arguments, `None`, tracebacks, dynamic + strong typing** (all in L09 slides; he said understanding tracebacks "is really important for diagnosing" bugs, L09 00:47:06).

## 6. Class questions from the slides (he asked these live — expect close variants)

| Lecture | Question | Answer |
|---|---|---|
| L03 | Is Zsh a terminal, shell, or emulator? | **Shell** |
| L03 | How do you check which shell you're running? | `echo $0` |
| L03 | How do you list the parent directory? | `ls ..` |
| L03 | What does `ls -RSral` do? | Recursive, sort by size, reverse, all files, long format |
| L03 | What does `chmod 712 *.c *.txt` do? | User rwx, Group x, Other w on all .c/.txt files |
| L05 | File checked out, edited, staged: what state? | **Staged, not committed** |
| L06 | State of a file right after a commit? | **Unmodified** |
| L06 | Create, stage, then edit `a_file.txt`: states? | Original is **staged**, edited version is **modified** |
| L06 | Create `a` (content a), stage, add `b`, unstage: state and content? | **Untracked**, contains `ab` (in a repo that already has commits) |
| L08 | What command inserts a cell below? / what does `.ipynb` mean? | `B` / "Interactive PYthon NoteBook" (but shortcuts are *not* examined) |
| L09 | `print("The dog","ran over",sep="_",end="!")` then `print("foo")` | `The dog_ran over!foo` |
| L10 | `fruit[:] == fruit[0:len(fruit)]` | True |
| L10 | `'banana'[::2]` | `bnn` |
