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

---

### Question 11

**Each question is worth 5 points.**

Which traversal order produces a sorted sequence when applied to a valid binary search tree?

- A) Preorder (Root → Left → Right)
- B) Postorder (Left → Right → Root)
- C) Inorder (Left → Root → Right)
- D) Level-order (breadth-first)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Preorder visits the root before its children. In a BST, this produces the root first, then all left subtree values, then right — not sorted order. For example, BST with root 5, left 3, right 7 produces preorder [5, 3, 7], not sorted.
- *Why B is incorrect:* Postorder visits both children before the root. This produces all left subtree values, then right subtree values, then the root — the root comes last, which is not sorted order.
- *Why C is correct:* Inorder visits the left subtree (all values smaller than root), then the root, then the right subtree (all values larger). Because BST property holds recursively, this produces a globally sorted sequence. This is why inorder is used for BST-related problems requiring sorted output.
- *Why D is incorrect:* Level-order visits nodes top-down, left-to-right within each level. For a BST, this does not produce sorted order — nodes at the same level can have arbitrary values relative to each other.

---

### Question 12

What is the height of a perfectly balanced binary tree with 15 nodes?

- A) 3
- B) 4
- C) 5
- D) 7

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A perfectly balanced binary tree of height 3 has 2⁰ + 2¹ + 2² + 2³ − 1... actually a tree of height h (where height = number of edges from root to leaf) has 2^(h+1) − 1 nodes. Height 3: 2⁴ − 1 = 15 nodes. So height 3 is actually correct for 15 nodes when height counts edges.
- *Why B is correct:* This depends on the height convention. If height = number of levels (counting the root as level 1), then 15 nodes in a perfect binary tree occupy levels 1 through 4 (1 + 2 + 4 + 8 = 15 nodes). Height = 4. If height counts edges (root at height 0), height = 3. The most common interview convention counts levels: height = ⌊log₂(15)⌋ + 1 = 4 levels, so height = 4 (using 1-based level count).
- *Why C is incorrect:* 5 levels would require 2⁵ − 1 = 31 nodes for a perfect binary tree, not 15.
- *Why D is incorrect:* 7 would be the height if you confused n with height. The relationship is n = 2^(h+1) − 1, so h = log₂(n+1) − 1 = log₂(16) − 1 = 4 − 1 = 3 (edge convention) or 4 (level convention).

---

### Question 13

A BST is constructed by inserting elements in this order: 5, 3, 7, 1, 4. What does the inorder traversal produce?

- A) `[5, 3, 7, 1, 4]`
- B) `[1, 3, 4, 5, 7]`
- C) `[1, 4, 3, 7, 5]`
- D) `[5, 7, 3, 4, 1]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `[5, 3, 7, 1, 4]` is the insertion order, which is also the preorder traversal of this particular tree (Root, Left subtree preorder, Right subtree preorder).
- *Why B is correct:* Inorder traversal of a BST always produces a sorted sequence. Regardless of insertion order, the BST property guarantees left < root < right at every node. The five values {5, 3, 7, 1, 4} sorted in ascending order are [1, 3, 4, 5, 7].
- *Why C is incorrect:* `[1, 4, 3, 7, 5]` is not sorted and does not correspond to any standard traversal of this BST.
- *Why D is incorrect:* `[5, 7, 3, 4, 1]` visits the root first, then the right subtree, then the left — this is neither a standard traversal nor the sorted output of inorder.

---

### Question 14

Which statement correctly describes the difference between a binary tree and a binary search tree?

- A) A binary tree has at most 2 children per node; a BST has at most 3
- B) A BST requires that for every node, left subtree values are less than the node and right subtree values are greater, enabling O(log n) search in a balanced BST
- C) A binary tree stores only integers; a BST can store any comparable type
- D) A BST always has the same number of nodes on both sides of the root

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both binary trees and BSTs have at most 2 children per node — that is the definition of "binary" in both cases.
- *Why B is correct:* A binary tree is any tree with at most 2 children per node, with no constraint on value ordering. A BST adds the ordering invariant: all values in the left subtree are less than the current node's value, and all values in the right subtree are greater. This invariant enables binary search — at each node, compare the target with the current value and recurse to only one subtree. In a balanced BST, this achieves O(log n) search.
- *Why C is incorrect:* Both binary trees and BSTs can store any comparable data type. The distinction is about structural ordering invariants, not data types.
- *Why D is incorrect:* This describes a perfectly balanced tree, which is a special case of a BST. An ordinary BST makes no guarantee about equal distribution — inserting sorted data produces a right-skewed BST with all nodes on one side.

---

### Question 15

What is the time complexity of finding the kth smallest element in a BST using inorder traversal?

- A) O(k log n) — BST search at each of k steps
- B) O(n) — inorder traversal visits all nodes before returning
- C) O(k) — stop the inorder traversal after k nodes
- D) O(log n + k) — navigate to the minimum in O(log n), then advance k steps

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(k log n) would imply k separate BST searches. Inorder traversal is sequential — it does not search for each element individually.
- *Why B is incorrect:* O(n) applies if you run inorder traversal fully and collect all values. With early termination — stopping after the kth element is visited — only k nodes are processed.
- *Why C is correct:* An inorder traversal with a counter stops exactly when the kth element is reached. Using an iterative inorder with an explicit stack, the first k elements are processed in O(k) time (plus O(h) to initialize the stack with leftmost nodes). The tightest bound for the standard recursive approach with early termination via an exception or counter is O(k).
- *Why D is incorrect:* O(log n + k) is the complexity of the BST Iterator approach (LeetCode #173 challenge) — navigate to the minimum in O(h), then advance k−1 steps. This is a more sophisticated implementation; the simpler inorder traversal approach is O(k) total.

---

### Question 16

In the recursive BST insert function, why does the function return `root` at every level?

```python
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
```

- A) To allow the caller to detect whether a new node was created
- B) To enable the parent to update its left or right child pointer via the assignment `root.left = insert(root.left, value)`
- C) To prevent the garbage collector from freeing intermediate nodes
- D) To return the new node to the original caller

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The return value is always the `root` of the subtree (possibly unchanged). The caller does not need to detect whether a new node was created — it just reassigns its child pointer.
- *Why B is correct:* The pattern `root.left = insert(root.left, value)` works because `insert` returns the root of the subtree after modification. When `root.left` is `None` and the recursive call creates a new node and returns it, the assignment `root.left = new_node` correctly links the new node into the tree. For non-None recursion, the same subtree root is returned unchanged, and the assignment is a no-op. This pattern is the standard "return the root" tree modification idiom.
- *Why C is incorrect:* Python's garbage collector is reference-counting based. As long as the root holds a reference to its children, they will not be freed. The return statement is not needed for this purpose.
- *Why D is incorrect:* The original caller receives the (possibly updated) root of the entire tree — not the new leaf node. The function returns the root at every level, not the newly inserted node.

---

### Question 17

What is the space complexity of a recursive inorder traversal of a binary tree with height h?

- A) O(n) — all nodes are stored in a result list
- B) O(h) — the call stack depth equals the tree height
- C) O(1) — inorder traversal is in-place
- D) O(n log n) — each node is visited multiple times

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n) space applies if you collect all values in a result list (which `inorder(root, result)` does). But if the question is about call stack depth alone (auxiliary space of the recursion), it is O(h) — one frame per level of the tree.
- *Why B is correct:* Recursive inorder traversal pushes one frame per level of the tree. The maximum number of simultaneous frames at any moment equals the depth of the current path — which is at most h (tree height). For a balanced tree, h = O(log n); for a skewed tree, h = O(n).
- *Why C is incorrect:* Recursion is never in-place — each recursive call occupies a stack frame. Even if no data structures are created, the call stack itself consumes O(h) memory.
- *Why D is incorrect:* Inorder traversal visits each node exactly once — O(n) total node visits. O(n log n) would imply each node is visited log n times, which is incorrect for a single traversal.

---

### Question 18

Given a binary tree, which approach correctly checks if it is a valid BST (LeetCode #98)?

- A) For each node, check that `node.left.val < node.val` and `node.right.val > node.val`
- B) Run inorder traversal, collect values, verify the resulting list is strictly increasing
- C) Pass `min_val` and `max_val` bounds down the recursion; a node is valid if `min_val < node.val < max_val`
- D) Check that the sum of left subtree values equals the sum of right subtree values

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Checking only immediate children is insufficient. A node in the right subtree of the root could have a left child with a value smaller than the root — violating the global BST property even though its local parent-child relationship looks valid.
- *Why B is correct (but C is the intended answer):* Inorder + sorted check is valid and simple. However, option C is the canonical recursive solution that interviewers expect. It is O(n) time and O(h) space and does not require building a list. Both B and C are correct, but C is the canonical interview answer because it makes the invariant explicit and does not require extra list space.
- *Why C is correct:* This is the authoritative approach. Every node must satisfy `min_val < node.val < max_val`. Initially, bounds are (-∞, +∞). Going left, the upper bound tightens to the current node's value. Going right, the lower bound tightens. Any violation fails immediately without traversing the full subtree.
- *Why D is incorrect:* Equal sums of left and right subtrees is not a BST property at all. Many valid BSTs have highly unequal subtree sums. This check would incorrectly reject valid BSTs and incorrectly accept invalid ones.

---

### Question 19

What does the following function compute for a binary tree?

```python
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

- A) The height of the tree
- B) The number of leaf nodes
- C) The total number of nodes in the tree
- D) The sum of all node values

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Height would use `max(count_nodes(left), count_nodes(right))` instead of addition. Height measures the longest path, not the total count.
- *Why B is incorrect:* Leaf count would add 1 only when both `root.left is None` and `root.right is None` — at leaf nodes only. This function adds 1 for every node, not just leaves.
- *Why C is correct:* For each node, 1 is added to represent the current node, and recursive calls count all nodes in the left and right subtrees. The base case `None → 0` correctly handles empty subtrees. Total: every node contributes exactly 1 to the sum = total node count.
- *Why D is incorrect:* Sum of values would use `root.val + sum(left) + sum(right)`. This function adds the constant 1 for each node regardless of the node's stored value.

---

### Question 20

In level-order traversal using a queue, what must be enqueued for each dequeued node?

- A) All ancestors of the dequeued node
- B) The dequeued node's left and right children (if they exist)
- C) All nodes at the same depth as the dequeued node
- D) The dequeued node's parent and sibling

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Ancestors are nodes that were already processed at earlier levels. There is no reason to re-enqueue them. Level-order traversal moves forward, never backward.
- *Why B is correct:* Level-order traversal (BFS) processes all nodes at depth d before processing nodes at depth d+1. When a node is dequeued and processed, its children (depth d+1) are enqueued for later processing. This ensures all siblings at depth d are processed before any children at depth d+1.
- *Why C is incorrect:* Siblings at the same depth are already in the queue before the current node is dequeued — they were enqueued when their parent was processed. Re-enqueueing them would cause nodes to be visited multiple times.
- *Why D is incorrect:* The parent was already dequeued and processed at the previous level. The sibling is already in the queue. Neither should be re-enqueued.
