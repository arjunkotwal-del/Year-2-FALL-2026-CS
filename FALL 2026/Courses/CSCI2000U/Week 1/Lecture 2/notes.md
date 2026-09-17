# Lecture 2 — UNIX and the Filesystem (CSCI2000U)

## Learning outcomes
- History of UNIX and Unix-like systems
- Abstraction of filesystems (tree structure)
- The concept of paths
- UNIX commands to navigate, view, and modify the filesystem

## Quick facts about UNIX
- UNIX dates back to **1969**, still widely used today
- Modern OSes derived from UNIX: **Linux, BSD, Solaris, macOS**
- Philosophy: command-line interface; each tool does *one thing well*; human-readable text interfaces; output of one command chains as input to another (pipelines)

## History timeline
- **1970s**: Created by Ken Thompson & Dennis Ritchie at Bell Labs. Originally written in Assembly, rewritten in **C** (Ritchie invented C in 1972) for v4 — UNIX was the first major OS written in C. `vi` editor (Bill Joy) and regex (Ken Thompson) both emerged from this era. AT&T commercialized UNIX.
- **1980s**: Bill Joy founded Sun Microsystems (SunOS, Solaris). Richard Stallman founded the GNU Project → later the Free Software Foundation. DEC built the first web crawler, AltaVista.
- **1990s**: UNIX lost the GUI/desktop war to Windows. BSD → Apple used it as the core of Mac OS X. Linus Torvalds created **Linux**, a free "Unix-like" OS (behaves like UNIX, not certified as UNIX). Google launched on Linux PCs.
- **2000s**: Internet/WWW era. Linux popular with hackers/power users; GUI desktops (Gnome) matured. Google's data centers ran on Linux. Android (Andy Rubin) built on a modified Linux kernel.
- **2010s**: Android reached ~80% market share, 2.5B+ users → Linux is the most-installed OS in the world. AWS (#1 cloud) and Azure (#2, 50% Linux) run on Linux. Deep learning frameworks (TensorFlow, PyTorch, MXNet) and Docker all support Linux natively.

**Key term — "Unix-like"**: an OS that behaves like UNIX but isn't necessarily certified/derived UNIX (e.g., Linux, BSD variants).

## The UNIX filesystem — abstraction
- The filesystem is **hierarchical** — a tree-like structure of nodes
- It forms **one rooted tree** of directories
- The root of the tree is denoted `/`
- Tree vocabulary:
  - **Leaf nodes** — nodes with no children (files, or empty dirs)
  - **Non-leaf nodes** — nodes that have children (directories)
  - Each node has **metadata**, and at minimum a **name**
  - Names are *usually* unique within their context but uniqueness is not a strict tree requirement

## Paths
- **Path**: a sequence of node labels used to identify one or more nodes in a tree
- A single label (like "A") is not necessarily unique — multiple nodes in a tree could share a label
- **Absolute path**: a sequence of node labels *from the root*, separated by `/`
  - Used to uniquely identify a node in the tree
  - The node an absolute path points to is called the path's **location** — we say the path "resolves" to that location
- (Relative paths — starting from the current location instead of root — come in the next lecture/L03_Shell)

## Why this matters for cloud/data storage
- Modern cloud storage (Google Cloud Bucket storage, Amazon S3) is modeled on the same hierarchical principles as the original UNIX filesystem
