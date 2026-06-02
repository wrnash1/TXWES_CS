# Quiz: Module 05 — Binary Trees & BSTs

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What traversal order produces sorted output when applied to a valid Binary Search Tree?

- A) Preorder (Root → Left → Right)
- B) Postorder (Left → Right → Root)
- C) Inorder (Left → Root → Right)
- D) Level-order (BFS)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Preorder visits the root before its children. On a BST, this produces the root first, then its left subtree values, then its right subtree values — which is not sorted order unless the tree has a specific structure.
- *Why B is incorrect:* Postorder visits both children before the root. On a BST this produces the leaves before internal nodes, which is not sorted order.
- *Why C is correct:* Inorder visits Left → Root → Right. The BST property guarantees that every node in the left subtree has a smaller value than the root, and every node in the right subtree has a larger value. Inorder therefore processes all smaller values first, then the current node, then all larger values — producing ascending sorted order for the entire tree.
- *Why D is incorrect:* Level-order traversal processes nodes level by level from root to leaves. For a BST, this produces the tree structure in insertion order, not sorted order.

---

### Question 2

A BST is built by inserting values in order: `[10, 5, 15, 3, 7]`. What is the height of the resulting tree?

- A) 1
- B) 2
- C) 3
- D) 5

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Height 1 would mean the root has only leaf children — a tree of 3 nodes maximum. With 5 insertions, at least some nodes must be at depth 2.
- *Why B is correct:* Insert 10 (root, height 0). Insert 5 (left child of 10, height 1). Insert 15 (right child of 10, height 1). Insert 3 (left child of 5, height 2). Insert 7 (right child of 5, height 2). The tree has 3 levels: root at depth 0, children at depth 1, grandchildren at depth 2. Height = 2.
- *Why C is incorrect:* Height 3 would require a node at depth 3. The 5 insertions above produce a balanced tree with maximum depth 2 — no node is deeper than depth 2.
- *Why D is incorrect:* Height 5 would occur for a degenerate chain of 5 nodes — what you get from inserting sorted values. Inserting `[10, 5, 15, 3, 7]` produces a balanced tree, not a chain.

---

### Question 3

Which of the following correctly implements BST search?

- A) Scan all nodes using level-order traversal and return `True` if the target is found
- B) At each node, if `target == root.value` return `True`; if `target < root.value` recurse left; else recurse right; return `False` if `root is None`
- C) Sort the tree using inorder traversal, then use binary search on the resulting list
- D) Use a hash map to store all values during an initial traversal, then check membership in O(1)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Level-order traversal visits every node — O(n). BST search exploits the ordering property to eliminate half the tree at each node, achieving O(log n) average case. Using level-order throws away this advantage.
- *Why B is correct:* This is the direct application of the BST property. At each node, the target either matches (return `True`), is in the left subtree (recurse left), or is in the right subtree (recurse right). Base case `root is None` handles missing values. Average case O(log n), worst case O(n).
- *Why C is incorrect:* Producing a sorted list via inorder is O(n), and binary search adds O(log n) on top — but the total is still O(n), no better than scanning. Furthermore, this approach requires O(n) auxiliary space for the output list.
- *Why D is incorrect:* Building a hash map requires a full O(n) traversal and O(n) space. For a single lookup this is slower than the O(log n) BST search. For repeated lookups this might be reasonable, but it is not BST search — it bypasses the tree structure entirely.

---

### Question 4

What is the inorder successor of a node with two children in a BST?

- A) The rightmost node in the left subtree
- B) The leftmost node in the right subtree
- C) The parent node
- D) The node with the next-larger key in the entire tree's sorted array

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The rightmost node in the left subtree is the inorder predecessor — the largest value smaller than the current node. The inorder successor is the smallest value larger than the current node.
- *Why B is correct:* The inorder successor is the smallest value greater than the current node. In a BST, all values greater than the current node are in its right subtree. The smallest of those is the leftmost node of the right subtree — follow `right` once, then go `left` as far as possible. This is used in BST delete (case 3) from the reading guide.
- *Why C is incorrect:* The parent node could be larger or smaller depending on which direction you came from. It is not guaranteed to be the immediate successor in sorted order.
- *Why D is incorrect:* While this definition of "inorder successor" is correct in the abstract, answer B gives the efficient structural way to find it in a BST — which is what the question is testing. Following an inorder traversal to produce a full array is O(n); finding the leftmost right-subtree node is O(h).

---

### Question 5

Why is checking only `root.left.value < root.value` insufficient to validate a BST?

- A) It only handles the left child and ignores the right child
- B) A node in the left subtree could be smaller than its local parent but larger than a grandparent, violating the BST property
- C) Python's comparison operator does not work on `TreeNode` objects
- D) The check is only valid for leaf nodes, not internal nodes

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The issue is not about which child is checked — even checking both children locally is insufficient. The problem is that local checks do not account for inherited constraints from ancestors higher in the tree.
- *Why B is correct:* Consider this tree: root=10, root.right=15, root.right.left=3. Locally, 3 < 15 (valid). But 3 < 10, meaning it should be in 10's left subtree, not its right subtree. The correct validation passes `min_val` and `max_val` bounds downward so every node is checked against all ancestor constraints.
- *Why C is incorrect:* Python comparison works on any values that support `<` and `>`, including integers stored in `TreeNode.value`. The issue is algorithmic, not a language limitation.
- *Why D is incorrect:* The local check `root.left.value < root.value` is actually most correct for internal nodes (where both children exist). The failure case involves deep descendants that violate an ancestor's constraint — which is not a leaf-only phenomenon.

---

### Question 6

What is the time complexity of BST search, insert, and delete for a balanced BST with n nodes?

- A) O(1) for all operations
- B) O(log n) average case; O(n) worst case
- C) O(n) for all operations
- D) O(n log n) because the tree must be rebalanced after each operation

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(1) would require a direct index computation, which only arrays support. BST search requires following pointers from the root — at minimum one comparison per level.
- *Why B is correct:* In a balanced BST, each comparison eliminates one subtree, so search, insert, and delete each require at most h comparisons where h = O(log n). Worst case is O(n) when the tree is skewed (inserting sorted values creates a chain where every node has only one child).
- *Why C is incorrect:* O(n) is only the worst case for a skewed tree. A balanced BST has height O(log n), making all three operations O(log n) average case.
- *Why D is incorrect:* A standard BST does not rebalance after operations. O(n log n) rebalancing would describe self-balancing trees (AVL, Red-Black), and even those are O(log n) per operation with at most O(log n) rotations — not O(n log n).

---

### Question 7

Which traversal uses a queue and processes nodes level by level?

- A) Inorder
- B) Preorder
- C) Postorder
- D) Level-order (BFS)

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Inorder (Left → Root → Right) is a depth-first traversal implemented with the call stack (recursive) or an explicit stack (iterative). It processes left subtrees fully before the root.
- *Why B is incorrect:* Preorder (Root → Left → Right) is also depth-first and uses the call stack. It visits the root immediately, then descends into the left subtree.
- *Why C is incorrect:* Postorder (Left → Right → Root) is depth-first and uses the call stack. It processes both subtrees completely before the root.
- *Why D is correct:* Level-order traversal is BFS applied to a tree. It uses a `deque`: enqueue the root, then in each iteration dequeue a node, record its value, and enqueue its children. This ensures all nodes at depth d are processed before any node at depth d+1 — the defining property of level-by-level traversal.

---

### Question 8

What is the worst-case height of a BST containing n nodes?

- A) O(1) — all BSTs have constant height
- B) O(log n) — BSTs are always balanced
- C) O(n) — inserting sorted values creates a skewed chain
- D) O(n²) — each insertion may require rebalancing all previous nodes

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Height O(1) is only possible for trees with at most 2 nodes. A tree of n nodes has height at least O(log n) (balanced) and at most O(n) (skewed).
- *Why B is incorrect:* An unmodified BST makes no guarantee about balance. Inserting `[1, 2, 3, 4, 5]` in order produces a right-skewed chain where every node has only a right child — height n-1 = O(n).
- *Why C is correct:* If values are inserted in sorted ascending order, each new value is larger than all previous values and goes to the rightmost position. The result is a chain (each node has one child only), height O(n). This degrades search/insert/delete from O(log n) to O(n).
- *Why D is incorrect:* A standard BST performs no rebalancing. O(n²) would imply nested rebalancing work, which does not occur. Self-balancing trees (AVL, Red-Black) perform O(log n) rotations per operation — not O(n²).

---

### Question 9

What does the `1 +` in `max_depth` accomplish?

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

- A) It counts the number of edges from root to the deepest leaf
- B) It adds the depth contribution of the current node to the maximum depth of either subtree
- C) It prevents the function from returning 0 on an empty tree
- D) It ensures both left and right subtrees are explored before returning

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This implementation counts nodes, not edges. The depth of a single-node tree is 1 (one node, zero edges). An edge-counting implementation would return 0 for a single-node tree.
- *Why B is correct:* `max_depth(root.left)` returns the maximum depth achievable from the left child. `max_depth(root.right)` does the same for the right child. The current node adds 1 to whichever subtree is deeper. This correctly accumulates the path length from any leaf back to the root.
- *Why C is incorrect:* Returning 0 for `None` (empty subtree) is the base case — it is correct behavior. The `1 +` does not prevent the 0 return; it adds 1 on top of the recursive result at non-`None` nodes.
- *Why D is incorrect:* Both `max_depth(root.left)` and `max_depth(root.right)` are evaluated as arguments to `max()` — Python evaluates both arguments before calling `max`. The `1 +` does not control evaluation order; it modifies the arithmetic result.

---

### Question 10

In the BST delete operation, when the node to be deleted has two children, which value replaces it and why?

- A) The value from the left child, because the left child is always the predecessor
- B) Any random value from the BST, because BST deletion is non-deterministic
- C) The value of the inorder successor (leftmost node of the right subtree), which is the smallest value greater than the deleted node
- D) The value of the root, to maintain the root as the center of the tree

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The left child is the immediate left subtree root, not necessarily the inorder predecessor (the predecessor is the rightmost node of the left subtree). Furthermore, replacing with the left child's value would require handling its children recursively and could disrupt the BST property more than the successor approach.
- *Why B is incorrect:* BST deletion is deterministic. The standard algorithm always uses the inorder successor (or alternatively the inorder predecessor — but the choice is consistent and documented). The BST property must be maintained after deletion.
- *Why C is correct:* The inorder successor is the smallest value greater than the deleted node. Replacing the deleted node's value with the successor's value maintains the BST property: the replaced node is still smaller than all right subtree values (since the successor was the smallest of those) and larger than all left subtree values. The successor is then deleted from the right subtree, which has at most one child (no left child), falling into case 1 or 2.
- *Why D is incorrect:* Replacing with the root's value would require moving the root down and reassigning its children — a much more complex operation that would likely violate the BST property. The inorder successor is chosen specifically because it can slot into the deleted position without disrupting any existing relationships.
