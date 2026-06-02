# Lab Activity: Module 05 — Binary Trees & BSTs

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Build a binary tree and implement all four traversals
- **Part 2** — Implement a Binary Search Tree with insert, search, and delete
- **Part 3** — LeetCode interview patterns: max depth, invert, validate BST, level-order

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Binary Tree and Traversals

**File:** `lab05_tree.py`

### 1.1 — TreeNode and Helper

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'TreeNode({self.value})'


def make_tree(values):
    """
    Build a complete binary tree from a list (level-order).
    None values leave that position empty.
    """
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(nodes):
            node.left = nodes[left_idx]
        if right_idx < len(nodes):
            node.right = nodes[right_idx]
    return nodes[0]
```

Build the reference tree:

```python
root = make_tree([4, 2, 6, 1, 3, 5, 7])
#         4
#        / \
#       2   6
#      / \ / \
#     1  3 5  7
```

---

### 1.2 — Inorder, Preorder, Postorder

```python
def inorder(root):
    """Left → Root → Right — O(n)"""
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def preorder(root):
    """Root → Left → Right — O(n)"""
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def postorder(root):
    """Left → Right → Root — O(n)"""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]
```

Test:

```python
root = make_tree([4, 2, 6, 1, 3, 5, 7])
print(inorder(root))    # [1, 2, 3, 4, 5, 6, 7]
print(preorder(root))   # [4, 2, 1, 3, 6, 5, 7]
print(postorder(root))  # [1, 3, 2, 5, 7, 6, 4]
```

**Checkpoint:** All three outputs match exactly. Note that inorder of this BST produces sorted order.

---

### 1.3 — Level-Order (BFS)

```python
from collections import deque

def level_order(root):
    """Level-by-level traversal using a queue — O(n)"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def level_order_levels(root):
    """Return a list of lists, one list per level — O(n)"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

Test:

```python
root = make_tree([4, 2, 6, 1, 3, 5, 7])
print(level_order(root))        # [4, 2, 6, 1, 3, 5, 7]
print(level_order_levels(root)) # [[4], [2, 6], [1, 3, 5, 7]]
```

**Checkpoint:** Level-order flat matches insertion order. Levels output groups nodes correctly by depth.

---

## Part 2 — Binary Search Tree

**File:** `lab05_bst.py`

### 2.1 — BST Insert and Search

```python
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        """Recursive insert — returns root of modified subtree."""
        if root is None:
            return TreeNode(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        return root   # return unchanged root if value already exists

    def search(self, value):
        """Return True if value is in the BST."""
        return self._search(self.root, value)

    def _search(self, root, target):
        if root is None:
            return False
        if root.value == target:
            return True
        if target < root.value:
            return self._search(root.left, target)
        return self._search(root.right, target)

    def inorder(self):
        """Return sorted list of all values."""
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result
```

Test:

```python
bst = BST()
for v in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(v)

print(bst.inorder())       # [2, 3, 4, 5, 6, 7, 8]
print(bst.search(4))       # True
print(bst.search(9))       # False
```

**Checkpoint:** Inorder produces sorted output. Search correctly returns True/False.

---

### 2.2 — BST Delete (Three Cases)

```python
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return None
        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            # Case 1: leaf — return None
            # Case 2: one child — return the child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # Case 3: two children — replace with inorder successor
            successor = root.right
            while successor.left:
                successor = successor.left
            root.value = successor.value
            root.right = self._delete(root.right, successor.value)
        return root
```

Test:

```python
bst = BST()
for v in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(v)

bst.delete(2)    # Case 1: leaf
print(bst.inorder())  # [3, 4, 5, 6, 7, 8]

bst.delete(3)    # Case 2: one child (4)
print(bst.inorder())  # [4, 5, 6, 7, 8]

bst.delete(7)    # Case 3: two children (6 and 8) — successor = 8
print(bst.inorder())  # [4, 5, 6, 8]
```

**Checkpoint:** Each deletion produces the correct remaining sorted sequence.

---

## Part 3 — LeetCode Interview Patterns

**File:** `lab05_patterns.py`

### 3.1 — Maximum Depth (LeetCode #104)

```python
def max_depth(root):
    """
    Return the maximum depth (height) of the binary tree.
    Time: O(n), Space: O(h)
    """
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

Test:

```python
root = make_tree([4, 2, 6, 1, 3, 5, 7])
print(max_depth(root))           # 3

root2 = make_tree([1, 2, None, 3])
print(max_depth(root2))          # 3
```

---

### 3.2 — Invert Binary Tree (LeetCode #226)

```python
def invert_tree(root):
    """
    Mirror the tree: swap left and right subtrees at every node.
    Time: O(n), Space: O(h)
    """
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

Test:

```python
root = make_tree([4, 2, 6, 1, 3, 5, 7])
print(inorder(root))              # [1, 2, 3, 4, 5, 6, 7]
invert_tree(root)
print(inorder(root))              # [7, 6, 5, 4, 3, 2, 1]  — reversed
print(level_order(root))          # [4, 6, 2, 7, 5, 3, 1]
```

---

### 3.3 — Validate BST (LeetCode #98)

```python
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Validate that the tree satisfies the BST property throughout.
    Time: O(n), Space: O(h)
    """
    if root is None:
        return True
    if root.value <= min_val or root.value >= max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.value) and
            is_valid_bst(root.right, root.value, max_val))
```

Test — include a tricky invalid BST:

```python
# Valid BST
root = make_tree([5, 3, 7, 2, 4, 6, 8])
print(is_valid_bst(root))   # True

# Invalid: looks like BST locally but violates ancestor bounds
#      5
#     / \
#    3   7
#         \
#          4   ← 4 < 5, should be in left subtree of 5
invalid = TreeNode(5)
invalid.left = TreeNode(3)
invalid.right = TreeNode(7)
invalid.right.right = TreeNode(4)
print(is_valid_bst(invalid))  # False
```

**Checkpoint:** Valid BST returns True; invalid returns False. Submit to LeetCode #98.

---

### 3.4 — Level Order Traversal (LeetCode #102)

```python
def level_order_lc(root):
    """
    Return list of lists — one list per level of the tree.
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

Test:

```python
root = make_tree([3, 9, 20, None, None, 15, 7])
print(level_order_lc(root))  # [[3], [9, 20], [15, 7]]
```

Submit to LeetCode #102.

---

### 3.5 — Integration Test

```python
if __name__ == '__main__':
    root = make_tree([4, 2, 6, 1, 3, 5, 7])

    assert inorder(root)   == [1, 2, 3, 4, 5, 6, 7]
    assert preorder(root)  == [4, 2, 1, 3, 6, 5, 7]
    assert postorder(root) == [1, 3, 2, 5, 7, 6, 4]
    assert level_order(root) == [4, 2, 6, 1, 3, 5, 7]
    assert max_depth(root) == 3

    bst = BST()
    for v in [5, 3, 7, 2, 4]:
        bst.insert(v)
    assert bst.inorder() == [2, 3, 4, 5, 7]
    assert bst.search(4) == True
    assert bst.search(9) == False
    bst.delete(3)
    assert bst.inorder() == [2, 4, 5, 7]

    assert is_valid_bst(make_tree([5, 3, 7, 2, 4, 6, 8])) == True

    print('All assertions passed.')
```

---

## Deliverables

Submit to Canvas:

1. `lab05_tree.py` — TreeNode, make_tree, all four traversals with test output
2. `lab05_bst.py` — BST class with insert, search, delete, inorder with test output
3. `lab05_patterns.py` — max_depth, invert_tree, is_valid_bst, level_order with test output
4. LeetCode submission screenshots for #104, #226, #98, and #102

---

## Summary

| Concept | Key Point |
|---|---|
| Inorder (L-R-Root) | BST inorder = sorted sequence |
| Preorder (Root-L-R) | Visit root first; useful for serialization |
| Postorder (L-R-Root) | Visit children before parent; useful for deletion |
| Level-order (BFS) | Uses a queue; processes level by level |
| BST property | left < root < right — holds recursively |
| BST insert | `root.left = insert(root.left, value)` — return root at every level |
| BST delete case 3 | Replace with inorder successor (leftmost of right subtree) |
| Validate BST | Pass min/max bounds down — local check is not sufficient |
| Max depth | `1 + max(depth(left), depth(right))` — base case is None → 0 |
