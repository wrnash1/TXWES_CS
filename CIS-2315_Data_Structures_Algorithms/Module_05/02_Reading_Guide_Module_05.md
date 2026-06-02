# Reading Guide: Module 05 — Binary Trees & BSTs

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Binary trees are the most important data structure in technical interviews. They appear in problems ranging from simple traversal to complex structural manipulation, and they form the basis for heaps (Module 07), hash tables (Module 08), and balanced trees (Module 06). The binary search tree adds an ordering property that enables O(log n) average-case search, insert, and delete. This module covers tree structure, all four traversal orders, BST operations, and the key interview problems built from these foundations.

---

## 1. Binary Tree Structure

### TreeNode

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

A binary tree is a reference to the root `TreeNode`. If the root is `None`, the tree is empty.

### Terminology

| Term | Definition |
|---|---|
| Root | The topmost node; has no parent |
| Leaf | A node with no children (`left is None and right is None`) |
| Height | Length of the longest root-to-leaf path; empty tree has height 0 |
| Depth | Distance from the root to a given node; root has depth 0 |
| Subtree | A node together with all its descendants |
| Balanced | A tree where for every node, the absolute height difference between left and right subtrees is at most 1 |
| Complete | Every level is fully filled except possibly the last, which fills left to right |

---

## 2. Tree Traversals

### Inorder — Left, Root, Right

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)
```

For a BST, inorder traversal produces values in sorted ascending order. Time: O(n). Space: O(h) call stack.

### Preorder — Root, Left, Right

```python
def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)
```

Visits root before children. Useful for serializing a tree (saving structure to file), copying a tree.

### Postorder — Left, Right, Root

```python
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]
```

Visits children before parent. Useful for deletion (free children before parent), computing aggregate values bottom-up.

### Level-Order (BFS) — Level by Level

```python
from collections import deque

def level_order(root):
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
```

Uses a queue instead of the call stack. Time: O(n). Space: O(w) where w = maximum width of the tree.

### Level-Order by Levels (LeetCode #102)

```python
def level_order_levels(root):
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

Processes the queue in batches of `level_size` to separate levels.

---

## 3. Binary Search Tree Operations

### BST Property

For every node in a BST: all values in its left subtree are strictly less than the node's value, and all values in its right subtree are strictly greater. This property holds recursively for every subtree.

### Search — O(h)

```python
def search(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    if target < root.value:
        return search(root.left, target)
    return search(root.right, target)
```

At each node, eliminate one subtree. Average case: O(log n) for a balanced BST. Worst case: O(n) for a skewed tree.

### Insert — O(h)

```python
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root
```

The `root.left = insert(root.left, value)` pattern is the standard recursive insert idiom — the function returns the root of the modified subtree.

### Delete — O(h)

Three cases, in order of complexity:

```python
def delete(root, value):
    if root is None:
        return None
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:         # case 1 (leaf) or case 2 (one child)
            return root.right
        if root.right is None:        # case 2 (one child)
            return root.left
        # case 3: two children — replace with inorder successor
        successor = root.right
        while successor.left:
            successor = successor.left
        root.value = successor.value
        root.right = delete(root.right, successor.value)
    return root
```

The inorder successor is the leftmost node of the right subtree — the smallest value greater than the deleted node. Replacing the value and deleting the successor preserves the BST property.

---

## 4. Common Interview Patterns

### Maximum Depth (LeetCode #104)

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

Time: O(n). Space: O(h).

### Invert Binary Tree (LeetCode #226)

```python
def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

Swap left and right at every node. Time: O(n). Space: O(h).

### Validate BST (LeetCode #98)

```python
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.value <= min_val or root.value >= max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.value) and
            is_valid_bst(root.right, root.value, max_val))
```

Pass min/max bounds down the tree. Each node must be within the bounds set by all its ancestors.

### Lowest Common Ancestor of BST (LeetCode #235)

```python
def lowest_common_ancestor(root, p, q):
    if p.value < root.value and q.value < root.value:
        return lowest_common_ancestor(root.left, p, q)
    if p.value > root.value and q.value > root.value:
        return lowest_common_ancestor(root.right, p, q)
    return root   # root is LCA: p and q straddle it (or one equals root)
```

LCA in a BST: if both targets are smaller, go left; if both are larger, go right; otherwise the current node is the LCA.

---

## 5. Complexity Summary

| Operation | Average Case | Worst Case | Notes |
|---|---|---|---|
| Search | O(log n) | O(n) | Worst: skewed tree (sorted insertion) |
| Insert | O(log n) | O(n) | Same condition |
| Delete | O(log n) | O(n) | Three cases; successor search is O(h) |
| Any traversal | O(n) | O(n) | Every node visited once |
| Max depth | O(n) | O(n) | Must visit every node |
| Space (balanced) | O(log n) | O(n) | Call stack depth = tree height |

---

## 6. Interview Exam Tips

1. **Inorder of a BST = sorted sequence** — if an interviewer asks you to produce sorted output from a BST, inorder traversal is the answer. O(n) time, no extra sorting.

2. **Always handle `None` first** — every recursive tree function should begin with `if root is None: return <base_value>`. This handles empty trees and leaf children.

3. **Validate BST with range bounds, not local comparison** — checking only `root.left.value < root.value` is insufficient. A node in the left subtree could violate the upper bound of a grandparent. Pass `min_val` and `max_val` downward.

4. **Return the root in insert/delete** — the recursive insert/delete pattern `root.left = insert(root.left, value)` requires the function to return the root of the modified subtree at every level.

5. **BST worst case is O(n)** — inserting sorted data produces a right-skewed chain. Always mention this when discussing BST complexity.

6. **Level-order uses a queue; all others use the call stack** — this is a fundamental distinction. If asked for "BFS traversal of a tree," use `collections.deque` with `popleft()`.

7. **Inorder successor = leftmost node of right subtree** — memorize this. It appears in BST delete (case 3), LCA problems, and "next greater element in BST" problems.

8. **Tree height = O(log n) balanced, O(n) skewed** — always state both when discussing space complexity.

---

## 7. Study Checklist

- [ ] Watch the Module 05 video lecture by Professor Nash.
- [ ] Implement all four traversals: inorder, preorder, postorder, level-order.
- [ ] Implement BST: insert, search, delete (all three cases).
- [ ] Solve LeetCode #104 (Maximum Depth of Binary Tree).
- [ ] Solve LeetCode #226 (Invert Binary Tree).
- [ ] Solve LeetCode #98 (Validate BST).
- [ ] Solve LeetCode #102 (Binary Tree Level Order Traversal).
- [ ] Complete the Module 05 Lab.
- [ ] Complete the Module 05 Quiz.
