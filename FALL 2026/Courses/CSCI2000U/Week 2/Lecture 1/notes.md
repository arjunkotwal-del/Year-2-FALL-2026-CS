# Lecture 3 — Working with the Shell (CSCI2000U)

## Learning outcomes / outline
1. Unix SHELL
2. Shell basics
3. Listing files and directories
4. Permissions

## Terminal vs. Shell vs. Command line
- **Terminal**: physical hardware you sit at (historically a TeleTYpewriter, TTY). Accepts input, displays output. A terminal that relies on a host computer for processing is a "dumb terminal"/"thin client."
- **Terminal emulator**: software that emulates a text-only terminal inside a GUI window (e.g., Terminal for macOS, Konsole for Linux, xterm for X11). It just displays input/output — it can't run commands itself. In casual speech, "terminal" usually means "terminal emulator."
- **Shell**: a text-only program that actually executes commands, interacts with files, and allows scripting. Examples: Unix shells (`sh`, Bash, Zsh, tcsh); PowerShell (Microsoft, not Unix).
- **Command line interface (CLI)**: refers to the *style* of interface (text-based) — could be Bash, or something else entirely like a Python interpreter.
- **Prompt**: the text to the left of your cursor, e.g. `username@hostname:directory$`. Indicates the shell is ready for input. Customizable (`~/.zshrc`, `~/.bashrc`).
- Data flow: **You → Terminal (emulator) → Shell → UNIX filesystem**

## Shell basics — key commands
| Command | Purpose |
|---|---|
| `pwd` | Print working directory (also available via `$PWD` env var, e.g. `echo $PWD`) |
| `ls` | List contents of current directory. `ls <path>` lists elsewhere |
| `cd <path>` | Change directory. Path can be relative or absolute |
| `mkdir <path>` | Create a directory. `mkdir -p foo/bar/final` creates intermediate dirs as needed (`-p` is a command **option** that changes behaviour) |
| `man <command>` | Open the manual page for a command, e.g. `man ls`, or even `man man` |
| `echo $0` | Prints the currently running process — tells you what shell you're in (likely `bash`) |
| `echo` | Prints its arguments to console; also expands environment variables, e.g. `echo $USER`, `echo $HOME` |

## Key vocabulary
- **Present working directory**: the location the shell currently tracks as "where you are"
- **Environment variable**: a named value the shell/OS exposes (e.g. `$PWD`, `$USER`, `$HOME`, `$0`)
- **Command option/flag**: a modifier like `-p` that changes a command's behavior

## Practice (from lecture's own coding challenge)
1. Write your current directory to the console → `pwd`
2. Create a new subdirectory `foo/bar` → `mkdir -p foo/bar`
