# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 05 — Binary Trees & BSTs

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Draw every tree on the whiteboard/slide before coding. Students who can draw a tree and annotate left/right children understand the structure. Students who cannot will struggle with every traversal.
> - Traversal order is the hardest concept — inorder, preorder, postorder. Use the same tree (1-2-3-4-5) for all three and trace each one. The visual comparison makes the difference.
> - Level-order (BFS) is the most common interview traversal. Use a queue; never mention it without drawing the queue state.
> - BST property: left < root < right. Emphasize that inorder traversal of a valid BST produces a sorted sequence — this is how you validate a BST.
> - BST delete has three cases. Spend extra time on the successor case (node has two children). It is the hardest and most frequently tested.
> - Common mistakes: forgetting to `return` the recursive call result, confusing inorder/preorder, not handling None nodes in recursive calls.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 05 | Binary Trees & BSTs | CIS-2315"]**

"Module 04 gave you the recursive thinking skills you need for this module. Now we apply them to the most important data structure in technical interviews: the binary tree. Trees are everywhere — file systems, compilers, databases, HTML DOM, and virtually every algorithm problem at the medium and hard level on LeetCode. By the end of this module, you will implement binary trees from scratch, traverse them in all four orders, and build a complete binary search tree with search, insert, and delete."

---

## [01:30 – 06:00] Part 1 — Binary Tree Structure

**[SHOW SLIDE: "Binary Tree — Nodes and References"]**

"A binary tree is a data structure where each node has at most two children: a left child and a right child.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

That is the complete node definition. The tree is just a reference to the root node.

**[SHOW DIAGRAM: tree with nodes 4 at root, 2 and 6 as children, 1,3,5,7 as leaves]**

Key terminology:

- **Root** — the topmost node; has no parent
- **Leaf** — a node with no children (`left is None and right is None`)
- **Height** — the length of the longest path from root to a leaf
- **Depth** — the distance from the root to a given node
- **Subtree** — any node together with all its descendants

[PAUSE]

Height and depth matter for complexity analysis. In a balanced binary tree with n nodes, the height is O(log n). In a degenerate tree — where every node has only one child — the height is O(n), which degrades every operation.

[PAUSE]

Let me build the tree `[4, 2, 6, 1, 3, 5, 7]` manually:

```python
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
```

This is the reference tree we will use for every traversal."

---

## [06:00 – 12:00] Part 2 — Tree Traversals

**[SHOW SLIDE: "The Four Traversal Orders"]**

"Traversal means visiting every node in the tree. There are four orders, and each has specific uses.

**[DEMO — Inorder: Left → Root → Right]**

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)
```

For our tree `[4,2,6,1,3,5,7]`: `[1, 2, 3, 4, 5, 6, 7]` — sorted order. This is the key property of a BST.

[PAUSE]

**[DEMO — Preorder: Root → Left → Right]**

```python
def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)
```

Result: `[4, 2, 1, 3, 6, 5, 7]`. Preorder gives you the root first — useful for serializing a tree (saving it to a file and reconstructing it later).

[PAUSE]

**[DEMO — Postorder: Left → Right → Root]**

```python
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]
```

Result: `[1, 3, 2, 5, 7, 6, 4]`. Postorder processes children before parents — useful for deleting a tree or computing directory sizes (process subdirectories before the parent directory).

[PAUSE]

**[DEMO — Level-Order (BFS): Level by Level]**

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

Result: `[4, 2, 6, 1, 3, 5, 7]` — level by level, left to right. Level-order uses a queue (BFS). The other three use recursion (DFS).

[PAUSE]

**Memory aid:** In-Pre-Post refers to where the root is processed — **In**between children, **Pre**vious (before) children, **Post** (after) children."

---

## [12:00 – 16:30] Part 3 — Binary Search Tree

**[SHOW SLIDE: "BST Property"]**

"A Binary Search Tree (BST) is a binary tree with an ordering property: for every node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater.

**[SHOW DIAGRAM: BST with root 5, left subtree 3→(2,4), right subtree 7→(6,8)]**

This property allows O(log n) average-case search, insert, and delete — comparable to binary search on a sorted array, but with O(log n) insert and delete instead of O(n).

[PAUSE]

**[DEMO — BST Search]**

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

At each node, you eliminate half the tree. If the target is less than the current value, it cannot be in the right subtree — ignore it and go left. This is why BST search is O(height).

[PAUSE]

**[DEMO — BST Insert]**

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

The pattern `root.left = insert(root.left, value)` is the standard recursive insert idiom. The function returns the root of the (possibly modified) subtree, which is reassigned to the parent's child pointer."

---

## [16:30 – 20:30] Part 4 — BST Delete and Validate

**[SHOW SLIDE: "BST Delete — Three Cases"]**

"BST delete is the most complex tree operation because there are three cases:

1. **Node is a leaf** — simply remove it (return `None`)
2. **Node has one child** — replace node with its only child
3. **Node has two children** — replace node's value with its inorder successor (the smallest value in the right subtree), then delete the inorder successor

```python
def delete(root, value):
    if root is None:
        return None
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        # Found the node to delete
        if root.left is None:
            return root.right        # Case 1 or 2: no left child
        if root.right is None:
            return root.left         # Case 2: no right child
        # Case 3: two children — find inorder successor
        successor = root.right
        while successor.left:
            successor = successor.left
        root.value = successor.value          # replace value
        root.right = delete(root.right, successor.value)  # delete successor
    return root
```

The inorder successor is the leftmost node in the right subtree — the smallest value greater than the current node.

[PAUSE]

**[DEMO — Validate BST (LeetCode #98)]**

A tree that looks like a BST visually might not be one. The correct validation passes range bounds down:

```python
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.value <= min_val or root.value >= max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.value) and
            is_valid_bst(root.right, root.value, max_val))
```

For every node, we verify it is within the bounds set by all its ancestors. Simply checking `root.left.value < root.value` is not enough — a value in the left subtree could violate an ancestor's upper bound."

---

## [20:30 – 24:00] Part 5 — Height and Complexity

**[SHOW SLIDE: "Tree Height and Complexity"]**

"Maximum depth (height) is one of the most common interview tree problems.

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

Time: O(n) — every node is visited once. Space: O(h) call stack where h = height = O(log n) balanced, O(n) skewed.

[PAUSE]

BST complexity summary:

| Operation | Average | Worst (skewed) |
|---|---|---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Inorder traversal | O(n) | O(n) |

The worst case occurs when the BST degenerates into a linked list — inserting values in sorted order `[1, 2, 3, 4, 5]` creates a right-skewed chain. Module 06 addresses this with self-balancing trees (AVL and Red-Black trees) that guarantee O(log n) for all operations.

The Module 05 lab has you implement all four traversals, BST insert/search/delete, and solve LeetCode problems #104, #226, #98, and #102. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 05 — Binary Trees & BSTs]**

---

## Additional Resources

- [VisuAlgo — Binary Search Tree Visualization](https://visualgo.net/en/bst)
- [NeetCode — Trees Playlist](https://www.youtube.com/watch?v=RBHmipAzBt0)
- [LeetCode #104 — Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [LeetCode #226 — Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [LeetCode #98 — Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [LeetCode #102 — Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
