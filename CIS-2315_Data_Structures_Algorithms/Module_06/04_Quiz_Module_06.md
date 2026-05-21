# Quiz: Module 06 – Binary Trees and Tree Traversal
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
In what order does inorder traversal visit the nodes of a binary tree?
*   A) Root → Left subtree → Right subtree
*   B) Left subtree → Root → Right subtree
*   C) Left subtree → Right subtree → Root
*   D) Root → Right subtree → Left subtree
*   **Correct Answer:** B) Left subtree → Root → Right subtree
*   **Distractor Analysis:**
    *   *Why correct:* "In-order" means the root is visited *in* the middle — after the left subtree and before the right subtree. On a BST, this produces sorted output.
    *   A is incorrect: That is preorder traversal (Root–Left–Right).
    *   C is incorrect: That is postorder traversal (Left–Right–Root).
    *   D is incorrect: That is reverse preorder and does not correspond to a standard traversal.

---

**Question 2**
Which of the following is the most accurate definition of the **height** of a binary tree?
*   A) The total number of nodes in the tree, counting every node from root to all leaves.
*   B) The number of edges on the longest path from the root to any leaf node.
*   C) The number of levels in the tree, counted as the sum of the depths of all leaf nodes divided by the number of leaves.
*   D) The maximum number of children any single node in the tree has, capped at two for a binary tree.
*   **Correct Answer:** B) The number of edges on the longest path from the root to any leaf node.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes the node count (size) of the tree, not its height.
    *   *Why B is correct:* Height measures the longest root-to-leaf path in edge count. A single-node tree has height 0; an empty tree has height –1 by convention.
    *   *Why C is incorrect:* That describes an average depth calculation, not height. Height is a maximum, not an average.
    *   *Why D is incorrect:* That describes the branching factor (max children per node), which is a property of node degree, not tree height.

---

**Question 3**
You need to find the minimum depth of a binary tree (the number of edges from the root to the nearest leaf). Which traversal strategy finds this most efficiently?
*   A) Postorder DFS — it processes leaves before the root, so it finds the minimum naturally.
*   B) Inorder DFS — it visits nodes in sorted order, enabling binary search for the minimum depth.
*   C) Level-order BFS — it visits nodes level by level and returns as soon as the first leaf is found.
*   D) Preorder DFS with memoization — caching subtree results avoids recomputation on shared subtrees.
*   **Correct Answer:** C) Level-order BFS — it visits nodes level by level and returns as soon as the first leaf is found.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Postorder DFS must visit the entire tree before returning; it cannot short-circuit when the first leaf is found.
    *   *Why B is incorrect:* Inorder traversal has no notion of depth level and does not produce nodes in depth order.
    *   *Why C is correct:* BFS explores nodes in increasing depth order. The moment it dequeues a leaf node (no left or right child), that depth is the minimum — it stops immediately without checking deeper levels.
    *   *Why D is incorrect:* Binary trees have no shared subtrees (no DAG structure), so memoization provides no benefit. DFS would still explore the deepest path before returning.

---

**Question 4**
What is the space complexity of a recursive inorder traversal on a balanced binary tree with n nodes?
*   A) O(1) — the traversal reads nodes in-place without extra memory.
*   B) O(n) — every node is stored in an output list during traversal.
*   C) O(log n) — the recursive call stack depth equals the tree height, which is O(log n) for a balanced tree.
*   D) O(n²) — each recursive call copies the subtree before processing it.
*   **Correct Answer:** C) O(log n) — the recursive call stack depth equals the tree height, which is O(log n) for a balanced tree.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Recursion uses the call stack; each active call frame occupies stack space proportional to the current depth.
    *   *Why B is incorrect:* O(n) is the space used if you collect results in a list; the *auxiliary* call stack space for a balanced tree is O(log n), not O(n).
    *   *Why C is correct:* At any point during traversal, the call stack holds at most one frame per level from root to current node. A balanced tree of n nodes has height O(log n), so stack depth is O(log n).
    *   *Why D is incorrect:* Recursive DFS does not copy subtrees; it processes nodes in-place by following pointers. O(n²) space is not a realistic complexity for tree traversal.

---

**Question 5**
Which traversal order is most useful for serializing (encoding) a binary tree so that it can be perfectly reconstructed from the encoded string?
*   A) Inorder traversal with null markers
*   B) Preorder traversal with null markers
*   C) Level-order traversal without null markers
*   D) Postorder traversal without null markers
*   **Correct Answer:** B) Preorder traversal with null markers
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Inorder traversal alone, even with null markers, does not uniquely identify a binary tree — many different tree shapes produce the same inorder sequence with the same nulls unless combined with a second traversal.
    *   *Why B is correct:* Preorder with null markers uniquely encodes every binary tree because the root is always first, so reconstruction is unambiguous: read root, recursively reconstruct left subtree until a null, then right subtree. This is the approach used in LeetCode #297.
    *   *Why C is incorrect:* Omitting null markers means internal null branches are invisible, making reconstruction ambiguous when node values repeat or when the tree is sparse.
    *   *Why D is incorrect:* Postorder without null markers has the same ambiguity problem as C and does not allow unambiguous reconstruction.
