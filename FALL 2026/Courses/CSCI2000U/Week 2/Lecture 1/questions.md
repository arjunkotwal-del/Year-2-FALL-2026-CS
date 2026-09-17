# Lecture 3 — Questions / Self-check

1. What's the difference between a terminal, a terminal emulator, and a shell?
2. Is Zsh a terminal, a shell, or an emulator?
3. What command tells you which shell program you're currently running, and why does it work?
4. How do you print the present working directory two different ways?
5. What's the difference between `ls` and `ls <path>`?
6. What does `mkdir -p foo/bar/final` do differently from plain `mkdir foo/bar/final`?
7. How do you open the manual page for the `ls` command?
8. What does `echo $USER` print, and why?

## Answers (self-check after review)
1. Terminal = physical hardware (or today, its emulator) that accepts input/displays output; terminal emulator = software that mimics that hardware inside a GUI; shell = the program that actually reads and executes your commands
2. A shell
3. `echo $0` — `$0` refers to the currently running process, which is usually the shell itself (e.g., bash)
4. `pwd`, or `echo $PWD`
5. `ls` lists the current directory; `ls <path>` lists the contents of the directory at that path instead
6. `-p` creates any missing intermediate directories along the path; without it, `mkdir` fails if a parent directory doesn't already exist
7. `man ls`
8. Your username — it expands the `$USER` environment variable set by the shell/OS
