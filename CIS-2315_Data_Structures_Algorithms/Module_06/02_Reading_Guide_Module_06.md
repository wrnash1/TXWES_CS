# Reading Guide: Module 06 — AVL Trees & Red-Black Trees

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2315 &BULL; DATA STRUCTURES & ALGORITHM ANALYSIS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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
