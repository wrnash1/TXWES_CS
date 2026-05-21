# Reading Guide: Module 07 – Binary Search Trees (BST)
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 07 – Binary Search Trees (BST)**! A Binary Search Tree is a binary tree with a critical ordering property that makes search, insertion, and deletion efficient. BSTs appear in interview problems on validation, range queries, k-th smallest elements, and tree modification. Understanding when a BST degrades to O(n) — and what self-balancing trees like AVL and Red-Black trees do about it — demonstrates the depth interviewers look for in senior roles.

This module covers the BST property, recursive and iterative operations, tree validation, and the key interview patterns built on BST ordering.

---

### 1. High-Yield Glossary

*   **BST property**: For every node N in a BST, all values in N's left subtree are strictly less than N's value, and all values in N's right subtree are strictly greater. This invariant must hold recursively for the entire tree, not just parent-child pairs.

*   **BST search**: Starting at the root, compare the target to the current node: go left if smaller, right if larger, return the node if equal. Average case O(log n) for balanced trees; O(n) worst case for a degenerate (sorted-input) tree.

*   **BST insertion**: Perform a search to find the insertion point — the null child where the new node should go — then attach it. Maintains the BST property by following the same left-smaller, right-greater logic.

*   **BST deletion**: Three cases: (1) leaf node — remove directly; (2) one child — replace node with its child; (3) two children — replace node's value with its in-order successor (smallest value in right subtree), then delete the successor.

*   **In-order successor**: The node with the smallest value that is still greater than a given node's value. For a node with a right subtree, it is the leftmost node in that right subtree. Used in BST deletion and range query problems.

*   **Degenerate BST**: A BST built by inserting sorted data, which produces a linear chain with no branching. All operations degrade to O(n) — effectively a linked list. Self-balancing trees (AVL, Red-Black) prevent this.

*   **BST validation**: Verifying that a tree satisfies the BST property at every node. A common mistake is only checking the immediate parent-child relationship; the correct approach passes valid min/max bounds down recursively, tightening them at each level.

---

### 2. Certification Exam Tips
*   **Validate BST with bounds, not just parent comparison:** The classic trap: `[5, 4, 6, null, null, 3, 7]` passes a naive parent-check but fails because 3 is in the right subtree of 5. Use `isValid(node, min, max)` with bounds passed recursively.
*   **In-order traversal of BST yields sorted output — use it:** If the problem asks for k-th smallest, rank, or range, inorder traversal gives you elements in sorted order without extra sorting cost.
*   **BST delete is always asked in interviews:** Be ready to write it from scratch. Focus on the two-children case: find in-order successor, copy its value up, delete the successor (which has at most one child).
*   **Know the difference between BST and balanced BST:** An unbalanced BST can degrade to O(n). When guaranteed balance matters, mention AVL or Red-Black trees. Java's `TreeMap`/`TreeSet` are backed by Red-Black trees.
*   **Range query pattern:** "Find all values between lo and hi" — inorder traversal, skip branches where the subtree cannot contain values in range (prune left if node <= lo, prune right if node >= hi).
*   **Study Resource:** The [Visualgo BST](https://visualgo.net/en/bst) tool lets you insert, delete, and search interactively, animating each step of the tree rebalancing and pointer updates.

---

### Required Readings & Videos
*   **Required Reading:** [Binary Search Trees – Open Data Structures (Pat Morin), Chapter 6.2](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbal.html) — covers BST search, insertion, and deletion with full Python implementations and O(log n) average / O(n) worst-case analysis.
*   **Required Video:** [Binary Search Tree – NeetCode on YouTube](https://www.youtube.com/watch?v=s3bOfVIroqg) — a 25-minute interview-focused video covering BST operations, validation, and the k-th smallest / LCA patterns.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a BST class** with recursive `insert`, `search`, `delete`, and `inorder` methods.
*   **Solve LeetCode #98 (Validate Binary Search Tree)** using the recursive min/max bounds approach.
*   **Solve LeetCode #230 (Kth Smallest Element in a BST)** using inorder traversal.
*   **Solve LeetCode #235 (Lowest Common Ancestor of a BST)** exploiting the BST property to avoid full DFS.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 6.2 of Open Data Structures.
- [ ] Watch the NeetCode BST video.
- [ ] Implement insert, search, and delete from scratch.
- [ ] Solve LeetCode #98, #230, and #235.
- [ ] Proceed to the Module 07 Quiz.
