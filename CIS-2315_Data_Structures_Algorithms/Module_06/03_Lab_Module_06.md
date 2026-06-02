# Lab Activity: Module 06 — AVL Trees & Red-Black Trees

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement AVL rotations (left and right) with height tracking
- **Part 2** — Implement complete AVL insert with all four balance cases
- **Part 3** — Analysis: compare plain BST vs AVL on sorted insertion

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — AVL Node and Rotations

**File:** `lab06_avl.py`

### 1.1 — AVLNode and Height Helpers

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1   # leaf starts at height 1

    def __repr__(self):
        return f'AVLNode({self.key}, h={self.height})'


def height(node):
    """Return height of node; 0 if None."""
    return node.height if node else 0


def get_balance(node):
    """
    Balance factor = height(right) - height(left).
    -1 to +1: balanced. < -1 or > +1: unbalanced.
    """
    return height(node.right) - height(node.left) if node else 0


def update_height(node):
    """Recompute height from children."""
    node.height = 1 + max(height(node.left), height(node.right))
```

---

### 1.2 — Right Rotation (LL Case Fix)

```python
def right_rotate(z):
    """
    Right rotation to fix LL imbalance.
    y becomes new subtree root; z becomes y's right child.
    """
    y = z.left
    T3 = y.right    # y's right subtree moves to z's left

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights bottom-up: z is now below y, update z first
    update_height(z)
    update_height(y)

    return y   # y is the new root
```

Test:

```python
# Build left-heavy chain: 3 → 2 → 1 (manually, no AVL insert yet)
z = AVLNode(3)
z.left = AVLNode(2)
z.left.left = AVLNode(1)
z.height = 3
z.left.height = 2

print(f'Before: root={z.key}, balance={get_balance(z)}')  # balance = -2
new_root = right_rotate(z)
print(f'After: root={new_root.key}')                       # root = 2
print(f'  left={new_root.left.key}')                       # left = 1
print(f'  right={new_root.right.key}')                     # right = 3
print(f'  height={new_root.height}')                       # height = 2
```

**Checkpoint:** After rotation, the new root is `2`, height is `2` (not `3`).

---

### 1.3 — Left Rotation (RR Case Fix)

```python
def left_rotate(z):
    """
    Left rotation to fix RR imbalance.
    y becomes new subtree root; z becomes y's left child.
    """
    y = z.right
    T2 = y.left    # y's left subtree moves to z's right

    y.left = z
    z.right = T2

    update_height(z)
    update_height(y)

    return y
```

Test:

```python
# Build right-heavy chain: 1 → 2 → 3
z = AVLNode(1)
z.right = AVLNode(2)
z.right.right = AVLNode(3)
z.height = 3
z.right.height = 2

new_root = left_rotate(z)
print(f'After left rotation: root={new_root.key}')    # 2
print(f'  left={new_root.left.key}')                  # 1
print(f'  right={new_root.right.key}')                # 3
```

**Checkpoint:** After rotation, new root is `2`, balanced.

---

## Part 2 — Complete AVL Insert

**File:** (continue `lab06_avl.py`)

### 2.1 — avl_insert with All Four Cases

```python
def avl_insert(root, key):
    """
    Insert key into AVL tree rooted at root.
    Returns the root of the new (possibly rotated) subtree.
    Time: O(log n) per insert.
    """
    # Step 1: Standard BST insert
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = avl_insert(root.left, key)
    elif key > root.key:
        root.right = avl_insert(root.right, key)
    else:
        return root   # duplicate key — ignore

    # Step 2: Update height of this node
    update_height(root)

    # Step 3: Get balance factor and apply rotation if needed
    balance = get_balance(root)

    # LL: left-heavy, new key in left child's left subtree
    if balance < -1 and key < root.left.key:
        return right_rotate(root)

    # RR: right-heavy, new key in right child's right subtree
    if balance > 1 and key > root.right.key:
        return left_rotate(root)

    # LR: left-heavy, new key in left child's right subtree
    if balance < -1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL: right-heavy, new key in right child's left subtree
    if balance > 1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root   # already balanced
```

---

### 2.2 — Helper: In-Order Traversal

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


def tree_height(root):
    return height(root)
```

---

### 2.3 — Test: Sorted Insertion

```python
# Insert sorted values — plain BST would create a chain of height 9
root = None
for k in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    root = avl_insert(root, k)

print('Inorder:', inorder(root))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Height:', tree_height(root))
# Should be 4 (log₂(10) ≈ 3.32, rounded up to 4)
# Plain BST would have height 9
```

**Checkpoint:** Inorder is sorted. Height is 4, not 9.

---

### 2.4 — Test: Trigger Each Rotation Case

```python
# LL case — triggers right rotation
r1 = None
for k in [3, 2, 1]:
    r1 = avl_insert(r1, k)
print('LL root:', r1.key)   # 2

# RR case — triggers left rotation
r2 = None
for k in [1, 2, 3]:
    r2 = avl_insert(r2, k)
print('RR root:', r2.key)   # 2

# LR case — triggers left-right double rotation
r3 = None
for k in [3, 1, 2]:
    r3 = avl_insert(r3, k)
print('LR root:', r3.key)   # 2

# RL case — triggers right-left double rotation
r4 = None
for k in [1, 3, 2]:
    r4 = avl_insert(r4, k)
print('RL root:', r4.key)   # 2
```

**Checkpoint:** All four cases produce root = 2 with height = 2.

---

## Part 3 — Plain BST vs AVL Analysis

**File:** `lab06_analysis.py`

### 3.1 — Plain BST Insert (No Balancing)

```python
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bst_insert(root, key):
    if not root:
        return BSTNode(key)
    if key < root.key:
        root.left = bst_insert(root.left, key)
    elif key > root.key:
        root.right = bst_insert(root.right, key)
    return root

def bst_height(root):
    if not root:
        return 0
    return 1 + max(bst_height(root.left), bst_height(root.right))
```

### 3.2 — Compare Heights on Sorted Input

```python
import sys
sys.setrecursionlimit(10000)

n_values = [10, 100, 500, 1000]

print(f'{"n":>6} | {"BST height":>12} | {"AVL height":>12} | {"log2(n)":>10}')
print('-' * 50)

for n in n_values:
    # Build plain BST with sorted input
    bst_root = None
    for k in range(1, n + 1):
        bst_root = bst_insert(bst_root, k)

    # Build AVL with same sorted input
    avl_root = None
    for k in range(1, n + 1):
        avl_root = avl_insert(avl_root, k)

    import math
    print(f'{n:>6} | {bst_height(bst_root):>12} | {tree_height(avl_root):>12} | {math.log2(n):>10.2f}')
```

Expected output (approximate):

```text
     n |   BST height |   AVL height |    log2(n)
--------------------------------------------------
    10 |            9 |            4 |       3.32
   100 |           99 |            7 |       6.64
   500 |          499 |           10 |       8.97
  1000 |          999 |           10 |       9.97
```

**Checkpoint:** BST height grows linearly with n; AVL height stays at approximately log₂(n).

---

### 3.3 — Red-Black Property Verification Exercise

Answer these questions in comments:

```python
# Q: State all five Red-Black tree properties from memory.
#
# A:
# 1. Every node is red or black.
# 2. The root is black.
# 3. Every NIL leaf is black.
# 4. If a node is red, both children are black (no two consecutive reds).
# 5. Every path from any node to descendant NIL leaves has the same
#    number of black nodes (equal black-height).

# Q: Given this tree, identify which Red-Black property is violated:
#         B(10)
#        /     \
#      R(5)   R(15)
#             /
#           R(12)
#
# A: Property 4 is violated — R(15) has a red child R(12),
#    meaning two consecutive red nodes exist on that path.

# Q: What is the maximum height of a Red-Black tree with black-height bh?
# A: At most 2*bh. The tallest path alternates red-black, giving 2 nodes
#    per black node. Since black-height is bh, max height = 2*bh.
```

**Checkpoint:** All three questions answered correctly in comments.

---

## Deliverables

Submit to Canvas:

1. `lab06_avl.py` — complete AVL implementation with rotation tests and four-case rotation test
2. `lab06_analysis.py` — plain BST vs AVL height comparison table with Red-Black exercise answers

---

## Summary

| Concept | Key Point |
|---|---|
| Balance factor | height(right) - height(left); ±1 balanced, ±2 triggers rotation |
| LL rotation | Right rotation — one step |
| RR rotation | Left rotation — one step |
| LR rotation | Left on child, then right on root — two steps |
| RL rotation | Right on child, then left on root — two steps |
| Height update | Update lower node first (z before y) after rotation |
| AVL guarantee | O(log n) height always; ≤ 2 rotations per insert |
| Red-Black | 5 properties; height ≤ 2 log n; ≤ 3 rotations per insert or delete |
| Production use | Java TreeMap, C++ std::map, Linux scheduler — all Red-Black |
