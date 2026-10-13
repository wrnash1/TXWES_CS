# Quiz: Module 06 — AVL Trees & Red-Black Trees

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the balance factor of an AVL node, and what range of values indicates the node is balanced?

- A) height(left) - height(right); balanced when the value is positive
- B) height(right) - height(left); balanced when the absolute value is at most 1
- C) number of left children - number of right children; balanced when equal
- D) height(right) / height(left); balanced when the ratio is 1.0

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The sign convention is opposite: the standard definition is `height(right) - height(left)`, not `height(left) - height(right)`. With the wrong sign, LL and RR cases would be misidentified.
- *Why B is correct:* Balance factor = height(right) - height(left). Values of -1, 0, or +1 mean the subtrees differ in height by at most 1 — the AVL balance condition. -1 is left-heavy by 1 (acceptable), 0 is perfectly balanced, +1 is right-heavy by 1 (acceptable). ±2 triggers a rotation.
- *Why C is incorrect:* The number of children is irrelevant to balance. A node could have a heavy subtree on both sides, making the count difference 0 but the height difference large. Height is the correct measure.
- *Why D is incorrect:* A ratio is undefined when `height(left)` is 0 (a leaf with no left child). Balance factor uses subtraction, not division, and has no division-by-zero risk.

---

### Question 2

A node `z` has balance factor -2 and the insertion was made in `z.left.left`. Which rotation restores balance?

- A) Left rotation on `z`
- B) Right rotation on `z`
- C) Left rotation on `z.left`, then right rotation on `z`
- D) Right rotation on `z.left`, then left rotation on `z`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A left rotation is used for the RR case (balance +2, right-heavy). A balance factor of -2 indicates left-heavy, which requires the opposite rotation direction.
- *Why B is correct:* Balance factor -2 means the left subtree is too tall. Insertion in `z.left.left` (the LL case) means the imbalance extends in the left-left direction. A single right rotation lifts `z.left` to become the new root, making `z` its right child — restoring balance in one step.
- *Why C is incorrect:* A left-then-right double rotation is the LR case fix — used when balance is -2 but the insertion was in `z.left.right`, not `z.left.left`. This double rotation is unnecessary and would produce an incorrect tree for the LL case.
- *Why D is incorrect:* A right-then-left double rotation is the RL case fix — used when balance is +2 and insertion was in `z.right.left`. This is the opposite heavy side from the LL case.

---

### Question 3

In the right_rotate function:

```python
def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y
```

Why must `z.height` be updated before `y.height`?

- A) Python requires lower variables to be updated first in recursive functions
- B) After the rotation, `z` is a child of `y`; `y`'s height depends on `z`'s height, so `z` must be updated first
- C) `y.height` is always the same as `z.height` before rotation, so order does not matter
- D) `z.height` is only updated for cache invalidation, not for correctness

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python has no requirement about update order. The order requirement here is purely algorithmic — it is about correctness, not a language rule.
- *Why B is correct:* After the rotation, `z` is `y.right`. When computing `y.height = 1 + max(height(y.left), height(y.right))`, the value `height(y.right)` uses `z.height`. If `z.height` has not been updated yet, `y.height` will be computed from stale data, producing an incorrect height that will cause incorrect balance factors in ancestors.
- *Why C is incorrect:* Before the rotation, `z` was the root with `y` as its left child — `y.height < z.height`. After the rotation, they have swapped roles and their heights change. They are not equal or unchanged.
- *Why D is incorrect:* `z.height` is used for correctness, not caching. Every ancestor of the rotation site uses the subtree heights to compute its own balance factor. Incorrect heights propagate upward and cause wrong balance decisions.

---

### Question 4

Which of the five Red-Black tree properties states that no two consecutive red nodes can appear on any root-to-leaf path?

- A) Property 1 (every node is red or black)
- B) Property 3 (every NIL leaf is black)
- C) Property 4 (if a node is red, both children are black)
- D) Property 5 (equal black-height on all root-to-leaf paths)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Property 1 establishes the color domain (red or black) but says nothing about adjacency of colors. It is the foundation that makes Properties 2–5 meaningful.
- *Why B is incorrect:* Property 3 ensures that NIL sentinel nodes (the leaves in the formal Red-Black definition) are black. This prevents inconsistency at tree boundaries but does not directly restrict consecutive red nodes among internal nodes.
- *Why C is correct:* Property 4 states: if a node is red, then both its children are black. This directly forbids any red node from having a red child. Therefore no two consecutive reds can appear on any path from root to leaf.
- *Why D is incorrect:* Property 5 (equal black-height) ensures path length uniformity but does not mention red node adjacency. A tree could violate Property 4 while satisfying Property 5 if red nodes alternated with consistent patterns.

---

### Question 5

A Red-Black tree has black-height bh (every root-to-NIL path has exactly bh black nodes). What is the maximum possible height of the tree?

- A) bh
- B) bh + 1
- C) 2 · bh
- D) 2^bh

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Height bh would require every path to have no red nodes at all — a possible but not necessary configuration. The maximum allows red nodes to be interspersed.
- *Why B is incorrect:* bh + 1 would only account for one extra red node per path. The maximum occurs when every black node is followed by a red node — alternating throughout the path.
- *Why C is correct:* The minimum path has all black nodes — length bh. The maximum path alternates red and black, giving at most 2 nodes per "black slot": one red followed by one black. Maximum path length: 2 · bh. This is why Red-Black trees are said to be approximately twice as tall as strictly balanced AVL trees.
- *Why D is incorrect:* 2^bh is the minimum number of nodes in a Red-Black tree of black-height bh (from the property that a subtree of black-height h has at least 2^h - 1 internal nodes). It is a node count, not a height.

---

### Question 6

Inserting values `[1, 2, 3]` into an AVL tree triggers which rotation, and what is the root after the rotation?

- A) LL case — right rotation — root becomes `1`
- B) RR case — left rotation — root becomes `2`
- C) LR case — left-right double rotation — root becomes `2`
- D) RL case — right-left double rotation — root becomes `3`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The LL case occurs when the imbalance is on the left side (left-heavy). Inserting `[1, 2, 3]` creates right-heavy imbalance at node `1`, not left-heavy. The LL case and right rotation are for the opposite scenario.
- *Why B is correct:* Insert 1 (root). Insert 2 (right child of 1, height 2). Insert 3 (right child of 2). Now node 1 has balance factor +2 and its right child 2 has balance factor +1 — the RR case. Left rotation on node 1: node 2 becomes root, 1 becomes 2's left child, 3 remains 2's right child. Root = 2, height = 2.
- *Why C is incorrect:* The LR case fires when a node is left-heavy but the imbalance is in the left child's right subtree (e.g., inserting `[3, 1, 2]`). Inserting `[1, 2, 3]` is right-heavy, not left-heavy.
- *Why D is incorrect:* The RL case fires when a node is right-heavy but the imbalance is in the right child's left subtree (e.g., inserting `[1, 3, 2]`). Inserting `[1, 2, 3]` puts the imbalance in the right child's right subtree — the RR case, not RL.

---

### Question 7

What is the maximum number of rotations an AVL insert operation performs?

- A) 0 — AVL insert never rotates
- B) 1 — at most one single rotation per insert
- C) 2 — at most two rotations (the LR and RL cases each require two)
- D) O(log n) — one rotation per level of the tree

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Rotations are the mechanism that maintains AVL balance. Inserting a key that causes an imbalance always triggers at least one rotation.
- *Why B is incorrect:* Single-rotation cases (LL and RR) require only one rotation. But double-rotation cases (LR and RL) require two rotations — first on the child, then on the root. The answer must account for the maximum.
- *Why C is correct:* The worst case is an LR or RL imbalance: first a rotation on the child subtree (to convert it into an LL or RR case), then a rotation on the root. That is exactly 2 rotations. After these two rotations, the subtree's height has decreased by 1, restoring all ancestor balance factors — no further rotations propagate upward.
- *Why D is incorrect:* O(log n) rotations per insert applies to AVL delete in the worst case, not insert. AVL insert always terminates after at most 2 rotations because a single rotation restores the subtree height, preventing cascading imbalances upward.

---

### Question 8

Which of the following best describes when to choose a Red-Black tree over an AVL tree?

- A) When lookup operations dominate and insertions are rare
- B) When the tree will contain fewer than 100 elements
- C) When insertions and deletions are frequent relative to lookups
- D) When all inserted keys are already sorted

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* When lookups dominate, AVL trees are the better choice. AVL trees have strictly tighter balance (height ≤ 1.44 log n) compared to Red-Black trees (height ≤ 2 log n), resulting in fewer comparisons per lookup.
- *Why B is incorrect:* Tree size does not determine the choice between AVL and Red-Black. Both structures have O(log n) complexity regardless of size. The deciding factor is the read/write ratio.
- *Why C is correct:* Red-Black trees require at most 3 rotations per delete (vs. O(log n) for AVL). For workloads with many insertions and deletions, Red-Black trees perform fewer total rotations and therefore less total work. This is why Java's `TreeMap`, C++'s `std::map`, and the Linux kernel process scheduler all use Red-Black trees.
- *Why D is incorrect:* Sorted input is actually the worst case for plain BSTs (creating a chain), but both AVL and Red-Black trees handle it in O(log n) per insert. The distribution of input keys does not affect the choice between the two self-balancing variants.

---

### Question 9

Which production software component uses a Red-Black tree as its underlying sorted data structure?

- A) Python's `list` — dynamic array
- B) Python's `dict` — hash map (since Python 3.6)
- C) Java's `TreeMap` and C++'s `std::map`
- D) Python's `heapq` — binary heap

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python's `list` is a dynamic array (contiguous memory, O(1) index access, O(n) insert/delete in the middle). It uses no tree structure.
- *Why B is incorrect:* Python's `dict` is a hash map — O(1) average lookup. As of Python 3.7+ it preserves insertion order using a compact hash table, not a tree. It does not maintain sorted order.
- *Why C is correct:* Java's `TreeMap` is documented as backed by a Red-Black tree, providing O(log n) `get`, `put`, and `remove` with keys maintained in sorted order. C++'s `std::map` and `std::set` are also Red-Black trees in all standard library implementations. The Linux kernel's Completely Fair Scheduler (CFS) uses a Red-Black tree to schedule tasks.
- *Why D is incorrect:* Python's `heapq` implements a binary min-heap (array-based), which provides O(log n) push/pop. It is not a BST and does not maintain sorted order of all elements — only the min-heap property.

---

### Question 10

A student proposes using a plain BST instead of an AVL tree because "the average case is O(log n) anyway." Under what realistic conditions would this reasoning be wrong?

- A) When the BST is used for lookups on uniformly random data
- B) When data is inserted in a pattern that creates nearly sorted sequences
- C) When the BST holds fewer than 10 nodes
- D) When the BST is built once and never modified

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* On uniformly random input, a plain BST does have expected O(log n) height, so the student's reasoning holds in this specific case. The flaw appears on non-random inputs.
- *Why B is correct:* Real-world data is often nearly sorted — timestamps, sequential IDs, log entries, ordered event streams. Even partial sorted ordering produces nearly-skewed BSTs with heights much closer to O(n) than O(log n). Database insertions often exhibit temporal locality (recent records share similar keys), making plain BSTs consistently underperform AVL trees in production.
- *Why C is incorrect:* For 10 nodes, the height difference between balanced (height ~4) and skewed (height ~9) is negligible in absolute terms. The performance gap matters at scale.
- *Why D is incorrect:* A BST built once from random data and never modified would have expected O(log n) height, and the student's reasoning would be approximately correct. The problem arises when the insert sequence is non-random or nearly sorted.

---

### Question 11

**Each question is worth 5 points.**

In an AVL tree, the balance factor of a node is defined as `height(right_subtree) − height(left_subtree)`. What is the valid range of balance factors for all nodes in a valid AVL tree?

- A) −2 to +2
- B) 0 to +2
- C) −1 to +1
- D) 0 only (all nodes must be perfectly balanced)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A balance factor of ±2 indicates an imbalance that triggers a rotation. In a valid (post-operation) AVL tree, balance factors of ±2 do not persist — they trigger immediate rebalancing.
- *Why B is incorrect:* This range excludes negative balance factors. A left-heavy node (more nodes in the left subtree) has a negative balance factor, which is perfectly valid in an AVL tree as long as the magnitude is at most 1.
- *Why C is correct:* The AVL invariant requires that every node's balance factor is in {−1, 0, +1}. −1 means left-heavy by one level; 0 means equal height; +1 means right-heavy by one level. Any balance factor with magnitude ≥ 2 triggers a rotation to restore the invariant.
- *Why D is incorrect:* Requiring balance factor 0 for all nodes would mean every subtree must have perfectly equal height — this is only achievable for trees with 2ⁿ − 1 nodes. AVL trees allow ±1 imbalance at every node, which is why they are called "height-balanced" rather than "perfectly balanced."

---

### Question 12

After inserting value 30 into an AVL tree that currently contains `[10, 20]` (a right-skewed chain), which rotation is triggered and what does the resulting tree look like?

- A) Left rotation on node 10 — new root is 20
- B) Right rotation on node 20 — new root is 10
- C) Left-Right rotation — 20 becomes root after two steps
- D) No rotation — the tree is already balanced

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The sequence `10 → 20 → 30` is a right-right (RR) case. Node 10 becomes unbalanced with balance factor +2 (right-heavy). The fix is a single left rotation on node 10: node 20 becomes the new root, node 10 becomes 20's left child, and node 30 stays as 20's right child. Result: balanced tree with root 20, left child 10, right child 30.
- *Why B is incorrect:* A right rotation would move node 20's left child up to become the root. Since node 20 has no left child in this sequence, a right rotation on node 20 is not applicable.
- *Why C is incorrect:* LR rotation applies when the imbalance is Left-Right (the right child's left subtree is taller). Here the imbalance is Right-Right — the right child's right subtree is taller. LR is not the correct rotation case.
- *Why D is incorrect:* After inserting 30, node 10 has balance factor +2 (right subtree height 2, left subtree height 0). This violates the AVL invariant and requires a rotation.

---

### Question 13

Which Red-Black tree property is violated when a red node has a red parent?

- A) Property 1 — every node is red or black
- B) Property 3 — every NIL leaf is black
- C) Property 4 — if a node is red, both its children must be black
- D) Property 5 — all paths from a node to descendant NIL leaves have the same black-height

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Property 1 only states that each node has a color attribute (red or black). A red node with a red parent satisfies property 1 — both are validly colored.
- *Why B is incorrect:* Property 3 concerns NIL sentinel nodes, not internal nodes. A red node with a red parent does not affect NIL coloring.
- *Why C is correct:* Property 4 states that if a node is red, both its children must be black. Equivalently, no two consecutive red nodes may appear on any root-to-leaf path. A red node with a red parent directly violates this — the parent is red and has a red child.
- *Why D is incorrect:* Property 5 concerns the count of black nodes on root-to-leaf paths. A red node with a red parent doesn't directly change black-height counts — it violates the consecutive-red constraint, which is property 4.

---

### Question 14

How many rotations does AVL insert require at most to restore balance after a single insertion?

- A) O(log n) rotations — one per level traversed back up
- B) Exactly 1 rotation always
- C) At most 2 rotations — a single or double rotation suffices
- D) At most 3 rotations — one per rotation case type

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(log n) rotations per insert applies to some other balanced tree operations (like Red-Black delete or B-tree rebalancing). AVL insert triggers at most one rotation site (single or double), then the height of the subtree is restored to what it was before the insert — no further rotations propagate up.
- *Why B is incorrect:* A single rotation (right or left) handles LL and RR cases. LR and RL cases require a double rotation (two rotations). So "exactly 1" is too restrictive — double rotations use 2.
- *Why C is correct:* AVL insertion requires at most 2 rotations. LL and RR cases require 1 rotation; LR and RL cases require 2 rotations (rotate the child, then the root). After the rotation(s), the subtree height returns to its pre-insertion value and no further rebalancing propagates upward.
- *Why D is incorrect:* 3 rotations is the maximum for Red-Black tree insertion fixup, not AVL. AVL has exactly two rotation types (single and double) and requires at most 2 rotations per insert.

---

### Question 15

What is the worst-case height of an AVL tree with n nodes?

- A) O(n)
- B) O(n log n)
- C) O(log n) — specifically at most 1.44 × log₂(n)
- D) O(√n)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n) is the worst-case height of an unbalanced BST. AVL trees maintain the balance factor invariant, which prevents any path from exceeding 1.44 × log₂(n+2). An AVL tree is never a linear chain.
- *Why B is incorrect:* O(n log n) is not a valid tree height — it is the complexity of sorting algorithms. No balanced tree has height O(n log n).
- *Why C is correct:* AVL trees guarantee height at most 1.44 × log₂(n+2) ≈ 1.44 log₂(n). This is proven using Fibonacci numbers: the minimum number of nodes in an AVL tree of height h is Fib(h+2) − 1 (where Fib is the Fibonacci sequence). Inverting this gives h ≤ 1.44 log₂(n). Every operation on an AVL tree is therefore O(log n) worst-case.
- *Why D is incorrect:* O(√n) would require a specific tree structure not related to any standard rebalancing scheme. No common balanced tree achieves O(√n) height.

---

### Question 16

In AVL tree terminology, what is a "Left-Right (LR)" imbalance and how is it resolved?

- A) The left subtree is taller than the right; resolved by a single right rotation
- B) The root's left child is right-heavy; resolved by a left rotation on the left child followed by a right rotation on the root
- C) The root is left-heavy and the left child is also left-heavy; resolved by a single right rotation
- D) The right subtree is taller than the left; resolved by a single left rotation

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A left subtree that is taller by exactly the right amount (LL case — root left-heavy, left child left-heavy) requires only a single right rotation. The LR case is more complex because the imbalance is in the opposite direction within the left subtree.
- *Why B is correct:* LR imbalance occurs when the root's balance factor is −2 (left-heavy) but the left child's balance factor is +1 (right-heavy). The standard fix is: first, rotate left on the left child (converting LR to LL), then rotate right on the root. Two rotations total. The result is a balanced subtree with the previously inserted node as the new root.
- *Why C is incorrect:* That describes the LL case, not LR. LL (root left-heavy, left child left-heavy) is resolved by a single right rotation on the root.
- *Why D is incorrect:* A right-heavy root with a right-heavy right child is the RR case, resolved by a single left rotation. This is the mirror image of the LL case, unrelated to LR.

---

### Question 17

A Red-Black tree has black-height 4. What is the maximum possible number of nodes it can contain?

- A) 4
- B) 8
- C) 15
- D) 255

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* 4 is the black-height itself — the number of black nodes on any root-to-leaf path. The total node count is much larger.
- *Why B is incorrect:* A perfect binary tree of height 4 has 2⁴ − 1 = 15 internal nodes. This would be the case if all non-NIL nodes were black (all-black tree with black-height 4).
- *Why C is incorrect:* 15 is the node count for an all-black tree of height 4 (black-height = 4, no red nodes). The maximum size occurs when red nodes are interspersed.
- *Why D is correct:* The maximum node count in a Red-Black tree with black-height bh is achieved by making every path alternate red-black (maximum 2×bh edges from root to NIL). A perfect tree with paths of length 2×bh has 2^(2×bh) − 1 nodes. For bh=4: 2⁸ − 1 = 255 nodes. The actual maximum formula is 2^(2×bh+1) − 1 for the full tree including NIL... in practice, the maximum number of internal nodes is 2^(2×4) − 1 = 255.

---

### Question 18

Which of the following Python standard library data structures is implemented using a Red-Black tree (or equivalent balanced BST) internally?

- A) `list` — Python's dynamic array
- B) `dict` — Python's hash map
- C) `heapq` — Python's heap module
- D) `sortedcontainers.SortedList` — third-party sorted container

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Python's `list` is a dynamic array (contiguous memory block). It has O(1) amortized append but O(n) insert/delete in the middle. No tree structure is used.
- *Why B is incorrect:* Python's `dict` is a hash table using open addressing. Hash tables provide O(1) average lookup but do not maintain sorted order. No tree structure is involved.
- *Why C is incorrect:* `heapq` implements a binary min-heap stored as an array. It provides O(log n) push and pop but does not maintain sorted order of all elements.
- *Why D is correct:* `sortedcontainers.SortedList` (a popular third-party library) provides O(log n) add, remove, and sorted iteration. Internally it uses a list-of-sorted-sublists with a splitting strategy that gives O(log n) amortized operations — functionally equivalent to a balanced BST for sorted-order operations. This is the practical Python tool for balanced-BST-like behavior.

---

### Question 19

After a right rotation on node `y` (which has a left child `x`), which node becomes the new root of the subtree?

- A) y remains the root; only its children change
- B) x becomes the new root; y becomes x's right child
- C) x becomes the new root; y becomes x's left child
- D) A new node is created to become the root

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The entire point of a rotation is to change which node is the subtree root. A right rotation on y promotes y's left child (x) to be the new root.
- *Why B is correct:* Right rotation on y: x (y's left child) becomes the new subtree root. y becomes x's right child. x's original right subtree (T₂) becomes y's new left child. The in-order relationships are preserved: all nodes in T₂ are still between x and y in value.
- *Why C is incorrect:* After a right rotation, y becomes x's right child (not left). x's left subtree, x itself, and y (with its right subtree) form the new arrangement left-to-right.
- *Why D is incorrect:* Rotations never create new nodes. They rearrange existing pointers among existing nodes. The total set of nodes in the subtree is unchanged — only the root pointer and a few child/parent pointers are updated.

---

### Question 20

What is the fundamental advantage of Red-Black trees over AVL trees for write-heavy workloads?

- A) Red-Black trees are shorter than AVL trees for the same n
- B) Red-Black trees require at most 3 rotations per insert or delete; AVL delete may require O(log n) rotations
- C) Red-Black trees use less memory because red nodes store no value
- D) Red-Black trees support O(1) lookup while AVL trees are O(log n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* AVL trees are actually shorter than Red-Black trees for the same n. AVL height ≤ 1.44 log₂(n); Red-Black height ≤ 2 log₂(n). The tighter AVL height bound makes AVL faster for read-heavy workloads.
- *Why B is correct:* AVL insert requires at most 2 rotations, but AVL delete may require O(log n) rotations (one per level on the way back up). Red-Black insert requires at most 2 rotations and delete requires at most 3 rotations — both constant. For write-heavy workloads (many inserts and deletes), the O(log n) rebalancing of AVL delete becomes expensive. Red-Black's constant rotation bound makes writes faster in practice, which is why Java `TreeMap`, C++ `std::map`, and the Linux scheduler all use Red-Black trees.
- *Why C is incorrect:* Red and black are conceptual color labels — not separate storage. In practice, the color is stored as a 1-bit flag in the node. Red-Black nodes are not smaller than AVL nodes.
- *Why D is incorrect:* Both AVL and Red-Black trees have O(log n) lookup. The difference is in insert/delete rotation counts, not in search performance.
