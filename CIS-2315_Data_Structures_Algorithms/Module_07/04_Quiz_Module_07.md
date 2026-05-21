# Quiz: Module 07 – Binary Search Trees (BST)
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the average-case time complexity of searching for a value in a balanced BST with n nodes?
*   A) O(n)
*   B) O(n log n)
*   C) O(log n)
*   D) O(1)
*   **Correct Answer:** C) O(log n)
*   **Distractor Analysis:**
    *   *Why correct:* Each comparison eliminates the entire left or right subtree from consideration. In a balanced BST of height log n, the search path visits at most log n nodes.
    *   A is incorrect: O(n) is the worst case for a degenerate (completely unbalanced) BST, not the average case for a balanced one.
    *   B is incorrect: O(n log n) describes sorting algorithms; it does not describe a single search operation.
    *   D is incorrect: O(1) describes hash table lookup; BST search always requires traversing at least part of the tree.

---

**Question 2**
Which of the following is the most accurate description of the **BST property** (the invariant that makes a binary tree a valid BST)?
*   A) For every node N, the left child's value is less than N's value and the right child's value is greater — this single parent-child check is sufficient to validate the entire tree.
*   B) For every node N, ALL values in N's left subtree are strictly less than N's value, and ALL values in N's right subtree are strictly greater — this invariant must hold recursively throughout the entire tree.
*   C) For every node N, the left and right subtrees have heights that differ by at most 1, ensuring the tree remains balanced and all operations run in O(log n).
*   D) For every node N, the node stores the minimum value of its entire subtree so that range minimum queries can be answered in O(1) by accessing any node directly.
*   **Correct Answer:** B) For every node N, ALL values in N's left subtree are strictly less than N's value, and ALL values in N's right subtree are strictly greater — this invariant must hold recursively throughout the entire tree.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Checking only the immediate parent-child relationship is the classic BST validation trap. A node can satisfy the parent-child check yet violate the invariant if a value in a deep subtree is out of bounds (e.g., a node with value 3 in the right subtree of 5).
    *   *Why B is correct:* The BST property is a global constraint: every ancestor's bounds apply to all nodes in that subtree, not just the immediate child.
    *   *Why C is incorrect:* That describes the AVL tree balance condition, not the fundamental BST ordering property. A valid BST need not be balanced.
    *   *Why D is incorrect:* That describes a segment tree or range minimum query structure, not a BST.

---

**Question 3**
When deleting a node with two children from a BST, what value is typically used to replace the deleted node?
*   A) The value of the deleted node's parent.
*   B) The value of the deleted node's left child.
*   C) The value of the in-order successor — the smallest value in the deleted node's right subtree.
*   D) The value of the root node, and the root is then replaced by its own in-order successor recursively.
*   **Correct Answer:** C) The value of the in-order successor — the smallest value in the deleted node's right subtree.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Replacing with the parent's value would destroy the parent-child relationship and is not a standard BST deletion strategy.
    *   *Why B is incorrect:* The left child is the largest value smaller than the deleted node (the in-order predecessor), which can also be used, but the canonical approach uses the in-order successor (right subtree minimum).
    *   *Why C is correct:* The in-order successor is the leftmost node in the right subtree. Copying its value to the deleted node and then deleting the successor (which has at most one child) preserves the BST property.
    *   *Why D is incorrect:* The root is not involved unless the root itself is being deleted. Replacement cascading to the root would be needlessly complex.

---

**Question 4**
What does inorder traversal of a valid BST always produce?
*   A) Elements in reverse sorted order, from largest to smallest.
*   B) Elements in the order they were inserted into the tree.
*   C) Elements in ascending sorted order, from smallest to largest.
*   D) Elements by level, with the root first and leaves last.
*   **Correct Answer:** C) Elements in ascending sorted order, from smallest to largest.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Reverse sorted order is produced by Right–Root–Left traversal (reverse inorder), not standard inorder.
    *   *Why B is incorrect:* Insertion order is only recovered by preorder traversal of a specific kind of tree; inorder always gives the BST's ordering.
    *   *Why C is correct:* Because the BST property guarantees all left-subtree values are smaller and all right-subtree values are larger, visiting Left–Root–Right visits nodes in ascending order.
    *   *Why D is incorrect:* Level-by-level (BFS) order is produced by level-order (BFS) traversal using a queue, not inorder DFS.

---

**Question 5**
You are implementing `isValidBST` using a recursive helper that passes bounds. What are the correct initial bounds when calling the helper on the root?
*   A) min = 0, max = 0
*   B) min = root.val – 1, max = root.val + 1
*   C) min = –infinity, max = +infinity
*   D) min = leftmost_leaf.val, max = rightmost_leaf.val
*   **Correct Answer:** C) min = –infinity, max = +infinity
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Initializing both bounds to 0 would immediately invalidate any root value that is not between 0 and 0, incorrectly rejecting all trees whose root is not 0.
    *   *Why B is incorrect:* Bounding by root ± 1 would restrict the entire tree to values within one of the root, which is wrong for any non-trivial BST.
    *   *Why C is correct:* The root can hold any value, so initial bounds are unconstrained (–∞, +∞). As recursion descends left, the upper bound tightens to the current node's value; descending right tightens the lower bound. This correctly enforces the BST property across all ancestors.
    *   *Why D is incorrect:* Leaf values are unknown at the start of validation and would produce incorrect bounds even if known.
