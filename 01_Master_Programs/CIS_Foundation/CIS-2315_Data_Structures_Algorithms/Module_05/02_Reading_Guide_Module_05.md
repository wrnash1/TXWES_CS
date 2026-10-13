# Reading Guide: Module 05 — Binary Trees & BSTs

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

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Binary Search Tree Visualizations** — [https://visualgo.net/en/bst](https://visualgo.net/en/bst)
   Animated step-by-step visualization of BST insert, search, delete, and all four traversals. Watch the inorder successor algorithm play out during deletion of a two-child node.

2. **OpenDSA — Binary Trees Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/BinTree.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/BinTree.html)
   Free interactive OER textbook covering binary tree definitions, traversals, and the BST property with embedded exercises and complexity proofs.

3. **NeetCode — Trees Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
   Free video solutions for the most frequently asked tree interview problems including Max Depth, Invert Binary Tree, Level Order Traversal, and Validate BST, each with a visual explanation of the recursive structure.

4. **MIT OCW 6.006 — Binary Search Trees (Lecture 5)** — [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
   MIT lecture notes and video on BST operations, augmented BSTs, and the relationship between BST height and operation complexity. Free with no account required.

5. **LeetCode Explore: Binary Tree** — [https://leetcode.com/explore/learn/card/data-structure-tree/](https://leetcode.com/explore/learn/card/data-structure-tree/)
   Free LeetCode learning card covering tree traversal, recursion patterns, and BST operations with guided examples and practice problems. No premium subscription required.

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
