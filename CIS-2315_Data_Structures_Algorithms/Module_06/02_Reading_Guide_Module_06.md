# Reading Guide: Module 06 — AVL Trees & Red-Black Trees

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

A plain BST has O(log n) average-case operations but degrades to O(n) when insertions create a skewed tree. Self-balancing trees eliminate this worst case by automatically maintaining O(log n) height after every mutation. This module covers two families: AVL trees (strict balance via rotation) and Red-Black trees (relaxed color-based balance). Both guarantee O(log n) for search, insert, and delete in all cases.

---

## 1. The Balance Problem

Inserting sorted values into a BST produces a chain — height O(n), making every operation O(n). The fix is to detect and correct imbalance after every insert or delete.

**Balance factor** of a node = height(right subtree) - height(left subtree).

- -1, 0, +1: balanced
- -2 or +2: unbalanced — a rotation is required

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # leaf starts at height 1

def height(node):
    return node.height if node else 0

def get_balance(node):
    return height(node.right) - height(node.left) if node else 0
```

---

## 2. AVL Rotations

Four cases, identified by the direction of the imbalance:

### LL — Right Rotation

Left-heavy node (balance = -2), inserted into left child's left subtree.

```python
def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y
```

### RR — Left Rotation

Right-heavy node (balance = +2), inserted into right child's right subtree.

```python
def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y
```

### LR — Double Rotation (Left then Right)

Left-heavy node (balance = -2), inserted into left child's right subtree. Fix: left rotate the left child, then right rotate the root.

```python
# Applied in avl_insert when: balance < -1 and key > root.left.key
root.left = left_rotate(root.left)
return right_rotate(root)
```

### RL — Double Rotation (Right then Left)

Right-heavy node (balance = +2), inserted into right child's left subtree. Fix: right rotate the right child, then left rotate the root.

```python
# Applied in avl_insert when: balance > 1 and key < root.right.key
root.right = right_rotate(root.right)
return left_rotate(root)
```

**Memory aid:** The case name (LL, LR, RL, RR) describes the path to the imbalance. Single-rotation cases (LL, RR) use one rotation in the opposite direction. Double-rotation cases (LR, RL) use two rotations.

---

## 3. Complete AVL Insert

```python
def avl_insert(root, key):
    # Step 1: Standard BST insert
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = avl_insert(root.left, key)
    elif key > root.key:
        root.right = avl_insert(root.right, key)
    else:
        return root  # duplicate

    # Step 2: Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Step 3: Balance and rotate
    balance = get_balance(root)

    if balance < -1 and key < root.left.key:       # LL
        return right_rotate(root)
    if balance > 1 and key > root.right.key:        # RR
        return left_rotate(root)
    if balance < -1 and key > root.left.key:        # LR
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance > 1 and key < root.right.key:        # RL
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
```

Rotations per insert: at most 2 (one for LR or RL). After a rotation, the subtree height decreases by 1, restoring the balance of all ancestor nodes without further action.

---

## 4. Red-Black Trees

### The Five Properties

1. Every node is **red** or **black**.
2. The **root** is always black.
3. Every **NIL leaf** (sentinel node at the end of every chain) is black.
4. If a node is **red**, both its children are black. (No two consecutive red nodes on any path.)
5. Every path from any node to its descendant NIL leaves contains the same number of **black nodes** (the node's black-height).

### Why This Guarantees O(log n) Height

- Property 5: all root-to-NIL paths have the same black-height bh.
- Property 4: no path can have two consecutive red nodes.
- Therefore the longest possible path (alternating red and black) is at most 2× the shortest path (all black).
- Since the tree has at least 2^bh - 1 nodes, bh = O(log n), so height ≤ 2·bh = O(log n).

### Violations

**Property 2 violation:** Root is red — fix by recoloring root to black.

**Property 4 violation:** Red node has a red child — fix by recoloring and/or rotation (uncle recolor or rotate-recolor depending on uncle's color).

**Property 5 violation:** Paths to NIL have unequal black-heights — fix by rotation and recoloring.

---

## 5. AVL vs Red-Black Comparison

| Property | AVL Tree | Red-Black Tree |
|---|---|---|
| Balance condition | Balance factor at most ±1 everywhere | Equal black-heights; no consecutive reds |
| Height guarantee | Strictly O(log n) — height ≤ 1.44 log n | O(log n) — height ≤ 2 log n |
| Rotations per insert | At most 2 | At most 2 |
| Rotations per delete | O(log n) | At most 3 |
| Lookup speed | Slightly faster (shorter tree) | Slightly slower (taller tree) |
| Insert/delete speed | Slightly slower (more rebalancing) | Slightly faster (fewer rotations on delete) |
| Used in | Database indexes (read-heavy) | Java `TreeMap`, C++ `std::map`, Linux kernel |

**Rule of thumb:** When mutations are frequent, prefer Red-Black. When reads dominate, AVL may be preferred.

---

## 6. Complexity Summary

| Operation | Plain BST (worst) | AVL (worst) | Red-Black (worst) |
|---|---|---|---|
| Search | O(n) | O(log n) | O(log n) |
| Insert | O(n) | O(log n) | O(log n) |
| Delete | O(n) | O(log n) | O(log n) |
| Space | O(n) | O(n) | O(n) |

---

## 7. Interview Exam Tips

1. **Know all four rotation cases by name** — LL, RR (single rotations), LR, RL (double rotations). Interviewers ask "what rotation fires when you insert X into this tree?"

2. **Balance factor sign convention** — define it consistently: `height(right) - height(left)`. Positive means right-heavy, negative means left-heavy.

3. **Update heights bottom-up** — in every rotation, update the lower node's height before the upper node's height. Skipping this produces incorrect balance factors.

4. **Red-Black properties 4 and 5 are the testable ones** — property 4 (no consecutive reds) and property 5 (equal black-height) are the most frequently tested in quizzes and interviews.

5. **AVL insert fires at most 2 rotations; delete may fire O(log n)** — this is why Red-Black is preferred for write-heavy workloads.

6. **Python's `sortedcontainers.SortedList` is O(log n) sorted** — it is implemented with a list-of-sorted-lists approach, not a pure AVL/RB tree, but provides the same complexity guarantee and is the practical Python tool for sorted sets.

7. **`bisect` module for sorted arrays** — Python's `bisect.insort` provides O(log n) search + O(n) insert in a sorted list. For O(log n) insert, use `sortedcontainers`.

8. **Height invariant after rotation** — after any rotation, the new subtree root has the same height as the old subtree root had before the offending insertion. This is why only a constant number of rotations propagates up.

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — AVL Tree Visualizations** — [https://visualgo.net/en/bst](https://visualgo.net/en/bst)
   Interactive step-by-step visualization of AVL insertions and the triggered rotations. Select "AVL" mode in VisuAlgo to see the balance factor update and rotation animation after each insert.

2. **OpenDSA — AVL Trees Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/AVL.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/AVL.html)
   Free interactive textbook covering AVL balance factors, all four rotation cases, and height analysis with embedded exercises and diagrams.

3. **MIT OCW 6.046J — Balanced BSTs (Lecture Notes)** — [https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)
   MIT lecture notes covering Red-Black tree properties, insertion cases, and the formal proof that Red-Black height is O(log n). Free with no account required.

4. **Abdul Bari — AVL Tree Rotations (YouTube)** — [https://www.youtube.com/watch?v=jDM6_TnYIqE](https://www.youtube.com/watch?v=jDM6_TnYIqE)
   Clear diagram-based walkthrough of all four AVL rotation cases (LL, RR, LR, RL) with worked examples. One of the clearest free explanations available.

5. **Python `sortedcontainers` Documentation** — [https://grantjenks.com/docs/sortedcontainers/](https://grantjenks.com/docs/sortedcontainers/)
   Free documentation for Python's `SortedList`, `SortedDict`, and `SortedSet` — the practical Python equivalents of AVL/Red-Black trees for interview use. Covers time complexity guarantees and usage examples.

---

## 8. Study Checklist

- [ ] Watch the Module 06 video lecture by Professor Nash.
- [ ] Implement `right_rotate` and `left_rotate` for AVL.
- [ ] Implement `avl_insert` with all four rotation cases.
- [ ] Test AVL insert on sorted input `[1, 2, 3, 4, 5]` — verify height stays at 3.
- [ ] State all five Red-Black properties from memory.
- [ ] Identify which Red-Black property is violated in a given example tree.
- [ ] Complete the Module 06 Lab.
- [ ] Complete the Module 06 Quiz.
