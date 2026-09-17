# Lecture 2 — Questions / Self-check

1. What year did UNIX originate, and where?
2. What programming language is modern UNIX written in, and who invented that language?
3. Name three modern operating systems descended from UNIX.
4. What does "Unix-like" mean, and give an example.
5. Who created Linux, and in what decade?
6. Describe the UNIX filesystem's overall structure in one sentence.
7. What's the difference between a leaf node and a non-leaf node in the filesystem tree?
8. What is the root of the UNIX filesystem denoted as?
9. Define "path" vs. "absolute path."
10. Why might a single node label NOT be enough to uniquely identify a location in the tree?

## Answers (self-check after review)
1. 1969, at Bell Labs (Ken Thompson & Dennis Ritchie)
2. C — invented by Dennis Ritchie (1972)
3. Any three of: Linux, BSD, Solaris, macOS
4. An OS that behaves like UNIX but isn't necessarily certified UNIX — e.g., Linux
5. Linus Torvalds, in the 1990s
6. It's a single hierarchical (tree-shaped) structure of nodes, rooted at `/`
7. Leaf nodes have no children (e.g., files); non-leaf nodes have children (e.g., directories)
8. `/`
9. A path is any sequence of node labels identifying one or more nodes; an absolute path is a sequence of labels *from the root*, separated by `/`, that resolves to exactly one location
10. Because the same label (e.g., "A") can appear at multiple different nodes/locations in the tree — the label alone doesn't encode position
