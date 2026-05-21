# Reading Guide: Module 06 – Binary Trees and Tree Traversal
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 06 – Binary Trees and Tree Traversal**! Trees are the most heavily tested non-linear data structure in technical interviews. Problems involving maximum depth, path sums, lowest common ancestor, and level-order traversal appear at every company from Amazon to Meta. The recursive structure of trees makes them a natural testing ground for recursive thinking, and mastering tree traversal patterns unlocks solutions to a large fraction of medium-difficulty interview problems.

This module covers binary tree structure, the four traversal orders (inorder, preorder, postorder, level-order), and recursion patterns for tree problems.

---

### 1. High-Yield Glossary

*   **Binary tree**: A hierarchical data structure where each node has at most two children, referred to as the left child and right child. A node with no children is a leaf. The topmost node is the root.

*   **Height of a tree**: The length of the longest path from the root to any leaf, measured in edges. A tree with a single root node has height 0. An empty tree has height –1 by convention.

*   **Depth of a node**: The number of edges from the root to that node. The root is at depth 0. Height and depth are often confused in interviews — be explicit about which definition you are using.

*   **Inorder traversal (Left–Root–Right)**: Recursively visit the left subtree, then the root, then the right subtree. On a Binary Search Tree, inorder traversal produces elements in sorted order.

*   **Preorder traversal (Root–Left–Right)**: Visit the root first, then recursively traverse left and right subtrees. Used to serialize/copy a tree and in expression tree evaluation.

*   **Postorder traversal (Left–Right–Root)**: Recursively traverse left and right subtrees before visiting the root. Used to delete or free a tree, and to compute subtree properties that depend on both children.

*   **Level-order traversal (BFS)**: Visit all nodes at depth 0, then depth 1, then depth 2, etc., using a queue. Produces the tree level by level. Used for minimum depth, level averages, and right-side view problems.

---

### 2. Certification Exam Tips
*   **Recursive DFS is the default for tree problems:** Most binary tree problems (max depth, path sum, symmetric check, LCA) are solved with a simple DFS recursion that returns a value from each subtree. The pattern: base case (null node returns 0/False/None), then combine left and right results.
*   **Level-order = BFS with a queue:** Any problem asking "for each level" or "minimum depth" uses BFS. Use `collections.deque`; process all nodes at current level before enqueuing the next level's nodes.
*   **Height vs. balanced:** A tree is balanced if every subtree's left and right heights differ by at most 1. LeetCode #110 (Balanced Binary Tree) requires computing height bottom-up and short-circuiting on imbalance.
*   **Serialize/deserialize trees:** LeetCode #297 uses preorder traversal with null markers. If you can serialize (preorder DFS) and deserialize (reconstruct from the string), you deeply understand tree structure.
*   **LCA (Lowest Common Ancestor) pattern:** Post-order DFS — return a node if you find p or q; if both subtrees return non-null, current node is the LCA.
*   **Study Resource:** Use [Visualgo Binary Tree](https://visualgo.net/en/bst) to animate all four traversal orders interactively, which makes the recursive call order concrete and easier to memorize.

---

### Required Readings & Videos
*   **Required Reading:** [Binary Trees – Open Data Structures (Pat Morin), Chapter 6](https://opendatastructures.org/ods-python/6_Binary_Trees.html) — covers tree structure, traversal implementations, and recursive pattern analysis with Python code.
*   **Required Video:** [Trees – NeetCode on YouTube](https://www.youtube.com/watch?v=oSWTXtMglKE) — a 30-minute interview-focused video covering tree structure, all traversal orders, and essential recursive DFS patterns with LeetCode walkthroughs.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a `BinaryTree` class** with recursive `inorder`, `preorder`, `postorder`, and `level_order` methods.
*   **Solve LeetCode #104 (Maximum Depth of Binary Tree)** using recursive DFS.
*   **Solve LeetCode #102 (Binary Tree Level Order Traversal)** using BFS with a deque.
*   **Solve LeetCode #226 (Invert Binary Tree)** to practice the recursive bottom-up DFS pattern.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 6 of Open Data Structures.
- [ ] Watch the NeetCode Trees video.
- [ ] Implement all four traversals recursively and iteratively.
- [ ] Solve LeetCode #104, #102, and #226.
- [ ] Proceed to the Module 06 Quiz.
