# 📘 Lecture 2 — UNIX and the Filesystem
*CSCI2000U — Scientific Data Analysis*

---

## 🏆 Learning outcomes
By the end of this lecture you should understand:
- [ ] The history of UNIX and Unix-like systems
- [ ] The abstraction of filesystems
- [ ] The concept of paths
- [ ] UNIX commands to navigate, view, and modify the filesystem

---

## ⚡ Quick facts

> [!important] UNIX in one breath
> - Dates back to **1969** — still widely used today
> - Modern descendants: **Linux, BSD, Solaris, macOS**
> - Philosophy: one CLI, each tool does *one thing well*, human-readable text, pipe output → input

---

## 🕰️ History timeline

```
1970s ── Created at Bell Labs (Ken Thompson & Dennis Ritchie)
      │  Rewritten in C (Ritchie invents C, 1972) — first major OS in C
      │  vi editor (Bill Joy) · regex (Ken Thompson) · AT&T commercializes UNIX
      ▼
1980s ── Bill Joy → Sun Microsystems (SunOS, Solaris)
      │  Richard Stallman founds GNU → later the Free Software Foundation
      │  DEC servers → builds first web crawler, AltaVista
      ▼
1990s ── UNIX loses the GUI war to Windows
      │  BSD → core of Mac OS X
      │  Linus Torvalds creates LINUX ("Unix-like", not certified UNIX)
      │  Google launches on Linux PCs
      ▼
2000s ── Internet/WWW era; Linux popular with hackers/power users
      │  Gnome desktops mature; Android built on modified Linux kernel
      ▼
2010s ── Android hits ~80% market share (2.5B+ users)
      │  → Linux = most-installed OS in the world
      │  AWS (#1 cloud) + Azure (#2, 50% Linux) run on Linux
      │  TensorFlow, PyTorch, MXNet, Docker — all native to Linux
```

> [!info] Key term — "Unix-like"
> An OS that **behaves** like UNIX but isn't necessarily certified/derived UNIX.
> **Example:** Linux, BSD variants.

---

## 🌳 The filesystem — abstraction

> [!important] The filesystem is a tree
> - **Hierarchical** — a tree-like structure of nodes
> - Appears as **one rooted tree** of directories
> - Root of the tree is denoted **`/`**

```
/                       ← root
├── bin
├── dev
├── etc
├── home
│   ├── dan
│   └── lisa
└── usr
```

### Tree vocabulary

| Term | Meaning | Example above |
|---|---|---|
| 🍃 **Leaf node** | No children | `dan`, `lisa`, `bin` |
| 🌲 **Non-leaf node** | Has children | `/`, `home` |
| 🏷️ **Metadata** | Info attached to a node (at least a **name**) | file/dir name |

> [!note] Names aren't always unique
> The same label (e.g. `A`) can appear at multiple locations in a tree — a bare name isn't enough to pin down *one* node.

---

## 🧭 Paths

> [!important] Path
> A sequence of node labels used to identify one or more nodes in a tree.

```
<root>
├── A
│   └── B
│       └── A
│           ├── B
│           └── A
└── B
```
☝️ Three nodes labelled `A`, three labelled `B` — labels alone don't uniquely identify a node.

> [!important] Absolute path
> A sequence of node labels **from the root**, separated by `/`.
> - Uniquely identifies a node
> - The node it points to = the path's **location**
> - We say the path **"resolves"** to that location

```
/home/dan/notes.txt   ← absolute path, resolves to notes.txt inside dan's folder
```

*(Relative paths — starting from your current location instead of root — are covered next lecture, L03 Shell.)*

---

## ☁️ Why this matters for the cloud

> [!example] Modern storage is UNIX's grandchild
> Google Cloud Bucket storage and Amazon S3 are Internet-scale, cloud-based systems — but they're **modeled on the same hierarchical tree principles** as the original 1969 UNIX filesystem.
