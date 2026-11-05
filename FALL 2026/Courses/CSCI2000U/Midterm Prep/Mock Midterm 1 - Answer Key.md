# Mock Midterm 1 — Answer Key
*Don't open this until you've finished the mock.*

**Scoring:** Section A is 20 marks (1 each). Section B is 20 marks (2 each). Total 40.

## Quick key

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 7 | B | 13 | D | 19 | B | 25 | B |
| 2 | C | 8 | B | 14 | B | 20 | C | 26 | C |
| 3 | C | 9 | B | 15 | B | 21 | A | 27 | B |
| 4 | C | 10 | B | 16 | A | 22 | B | 28 | A |
| 5 | D | 11 | C | 17 | B | 23 | B | 29 | B |
| 6 | C | 12 | B | 18 | C | 24 | B | 30 | B |

---

## Explanations

### Section A

**1. B.** Bash is a shell. Konsole, xterm, and macOS Terminal are terminal *emulators* (the window). The shell is the program that reads and runs your commands. (L03)

**2. C.** `echo $0` prints the currently running process, which is normally your shell. (L03, class question)

**3. C.** `..` means the parent directory, so `ls ..` lists it. `cd ..` would *move* you there but not list anything. (L03, class question)

**4. C.** 4 = read, 2 = write, 1 = execute; 4 + 2 + 1 = 7. (L03)

**5. D.** The classes are User (u), Group (g), Other (o). There is no "admin" class. (L03)

**6. C.** `rm -r` removes a directory recursively. `rmdir` only removes *empty* directories. (L04)

**7. B.** Git takes snapshots, not deltas. If a file didn't change, it stores a link to the previous identical file. (L05)

**8. B.** modified, staged, committed. (L05)

**9. B.** `clone` downloads a copy of an existing repo; `init` converts a local directory. (L05)

**10. B.** You share the **public** key and keep the private key secret. (L05, public-key cryptography)

**11. C.** 40 hex characters (a 160-bit SHA-1). You can usually refer to a commit by a short unique prefix. (L06)

**12. B.** HEAD is a pointer to the commit you're focused on, normally pointing at the current branch. (L06)

**13. D.** After a commit the file is **unmodified**. (L06, class question)

**14. B.** `restore --staged` unstages the file but leaves your edits alone. It is non-destructive. (L06, L07 00:38:58)

**15. B.** Put `.gitignore` in the root working directory, **not** inside `.git/`. (L07)

**16. A.** `git diff` = working directory vs staging area. `git diff --staged` = staging area vs last commit. (L07)

**17. B.** `git log` lists newest first (reverse order). (L07)

**18. C.** Strings are immutable, so item assignment `s[0] = "J"` raises `TypeError`. A, B build a **new** string and reassign the variable, which is fine. (L10, L10b 00:07:22)

**19. B.** Dynamically typed (type checked at runtime) and strongly typed (type-safety checks exist). Java is static; C is weak. (L09)

**20. C.** Functions without a `return` hand back `None`. (L09)

### Section B

**21. A, `/home/sam/docs/notes`.** Trace it from `/home/sam/docs`:
`..` -> `/home/sam` · `data` -> `/home/sam/data` · `..` -> `/home/sam` · `docs` -> `/home/sam/docs` · `notes` -> `/home/sam/docs/notes`.
This is the "goes nowhere, where do I end up?" style he described (L02 00:32:27). Don't guess, walk each step.

**22. B.** Following the lecture slide: with the trailing slash (`adir/`), `cp -r` copies the **contents** of `adir` into `cdir`, so there's no extra `adir` folder. Existing `ctxt.txt` stays. Without the slash (`cp -r adir cdir`) you'd get `cdir/adir/...`. (L04 slides 5-6, L04 00:13:09)

> [!warning] Real-world caveat (this will bite you if you test it yourself)
> The trailing-slash behaviour on the slides is the **macOS/BSD** `cp`. On **Linux / WSL / Git Bash (GNU `cp`)**, both `cp -r adir cdir` and `cp -r adir/ cdir` give `cdir/adir/...` — the slash makes no difference. I tested this. **For the exam, answer the way the slides do.** If you see different behaviour in your own terminal, that's why.

**23. B, `-rw-r-----`.** 6 = rw-, 4 = r--, 0 = ---. So owner rw, group r, other nothing. (L03)

**24. B.** `git restore --staged` removes it from staging. Because it was never committed, it goes back to **untracked** (not "modified"), and the working-directory content is untouched: `a` and `b`. (L06 slides 46-47)
*Note: this only works in a repo that already has at least one commit — in a brand-new empty repo, git errors with "could not resolve HEAD". The question says "already has commits" for that reason.*

**25. B.** `git add` snapshots the file **as it is at that moment**. Editing afterwards leaves the new change as modified-but-unstaged, and `git commit` only takes what's staged, so only `v1` is committed. (L06 slide 33; I verified it in a real repo)

**26. C, Add readme.** `HEAD` = Add plots, `HEAD~1` = Fix typo, `HEAD~2` = Add readme. Count back from the top, newest first. (L07)

**27. B.** `sep="-"` goes between items: `x-y-z`. `end="!"` replaces the newline, so the next `print` continues on the same line: `x-y-z!end`. (L09 class question; L09 00:25:19)

**28. A, `twr`.** Index: s0 t1 r2 a3 w4 b5 e6 r7 r8 y9. Slice `[1:8:3]` starts at 1, stops before 8, step 3: indices 1, 4, 7 -> `t`, `w`, `r`. (L10)
Distractors: `sae` is `word[0:8:3]`, `rbr` is `word[2:9:3]`, `trawber` is `word[1:8]`.

**29. B, 2.** `count` counts **non-overlapping** matches. `ahahaha`: matches at 0-2 and 4-6 = 2. A sliding window would give 3, but it isn't one. (L10b 00:12:09, he called this "a tricky one")

**30. B.** The first `if` and the second `if` are **independent**. 85 >= 80 prints `A`. Then the second `if x >= 70` is also true, so it prints `B`, and its `else` is skipped. Only `elif` would have stopped after `A`. (L09 slide 6)

---

## Self-diagnosis

| If you missed... | You need to review |
|---|---|
| 1-6, 21-23 | L02-L04 shell, paths, permissions |
| 7-17, 24-26 | L05-L07 git |
| 18-20, 27-30 | L08-L10b Python |

Missed 2+ in a block? Tell me the block and I'll drill it with a fresh set.
