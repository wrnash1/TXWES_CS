# Discussion Forum: Module 05 — Binary Trees & BSTs

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Background

Binary trees are the pivot point of this course. Everything before this module — recursion, pointers, traversal thinking — was preparation. Everything after — heaps, AVL trees, graphs, BFS, DFS — extends these ideas. The tree is the first data structure where the "shape" of the structure directly determines the complexity of every operation. A balanced tree with O(log n) height gives you O(log n) search; a skewed tree degrades every operation to O(n). BST deletion with two children is the most complex algorithmic procedure you have encountered so far — it requires finding the inorder successor, replacing a value in place, and then deleting the successor recursively. This discussion asks you to reason about traversal semantics, validation correctness, and what makes BST operations work.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Traversal Semantics and Use Cases

Four traversal orders exist for binary trees — inorder, preorder, postorder, and level-order — and each is the natural choice for different problems. The relationship between inorder traversal and sorted order is the key property of BSTs. Understanding why each traversal produces its particular order requires tracing the recursive calls and understanding what "Left before Root before Right" actually means in execution.

In 175–225 words, respond to the following:

- From the Module 05 lab (Part 1, Sections 1.2 and 1.3), you ran all four traversals on the tree `[4, 2, 6, 1, 3, 5, 7]`. For inorder and preorder, trace the first four nodes visited in order and explain, for each, why that node is visited at that moment. What recursive call is active when node `1` is first visited in inorder?
- The reading guide states that inorder of a BST produces sorted output. Explain precisely why this is true — not just "because of the BST property," but what it means for the recursive calls. Why does visiting Left before Root before Right, combined with the BST ordering property, produce ascending order?
- Postorder visits children before parents. The reading guide gives "computing directory sizes" as a real-world use case. Explain why postorder is natural for this task and why preorder or inorder would not work correctly for it.

Reference the lab or reading guide in your response.

---

### Scenario B — BST Validation with Ancestor Bounds

LeetCode #98 (Validate BST) has a famous incorrect solution: check only that `root.left.value < root.value` and `root.right.value > root.value` at each node. This passes many test cases but fails on carefully constructed invalid trees. The correct solution passes inherited `min_val` and `max_val` bounds downward with each recursive call.

In 175–225 words, respond to the following:

- From the Module 05 lab (Part 3, Section 3.3), you tested `is_valid_bst` on a tricky invalid tree where `root.right.left.value = 4` but the root is 10. Describe exactly why this tree is not a valid BST and why a local-only check would incorrectly return `True` for it.
- The reading guide's `is_valid_bst` passes `min_val` and `max_val` to each recursive call. Trace through the tree above for at least three nodes and show what `min_val` and `max_val` are at each call. At what point does the check catch the invalid node?
- The same "inherited bounds" pattern appears in other tree interview problems. Describe one other problem where passing constraints downward through a tree is necessary. What would go wrong if the constraint were checked only locally?

Reference the lab or reading guide in your response.

---

### Scenario C — BST Delete and the Inorder Successor

BST deletion is the most complex single operation in this module. When the node to be deleted has two children, the algorithm replaces its value with the inorder successor (the leftmost node of the right subtree) and then recursively deletes the successor. This approach preserves the BST property without restructuring pointers. Understanding why the inorder successor is the correct replacement requires understanding the BST invariant.

In 175–225 words, respond to the following:

- From the Module 05 lab (Part 2, Section 2.2), you deleted node `7` from the BST `[5, 3, 7, 2, 4, 6, 8]`. Node `7` has two children (6 and 8). Trace through the `_delete` algorithm: what is the inorder successor of `7`, and why? After the replacement and recursive deletion, what does the tree look like? Run `bst.inorder()` before and after to confirm.
- The reading guide explains that the inorder successor has at most one child (no left child). Why is this guaranteed? And why does this guarantee make the successor deletion simpler than the original deletion?
- Could you use the inorder predecessor (rightmost node of the left subtree) instead of the successor for the two-children case? What would the algorithm look like? Would the result still be a valid BST?

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 05 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: add a second example, challenge a claim with a counter-case, extend the concept to a harder problem, or describe a real-world application that illustrates the point

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 5–6 pts | Scenario answered fully with specific, concrete examples. Reference to lab or reading guide. 175–225 words. Complete sentences. |
| 3–4 pts | Mostly addressed but vague or generic. Close to word count. |
| 1–2 pts | Significant parts missing or well below word count. |
| 0 pts | Not submitted. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 pts | Two responses to classmates with different scenarios. Each 60+ words and adds genuine value. |
| 2 pts | One peer response only, or responses lack substance. |
| 0 pts | No peer responses. |

---

## A Note from Professor Nash

The binary tree is where data structure thinking becomes genuinely non-trivial. An array has one dimension; a tree has depth, branching, and structure that changes meaning. When someone says "search is O(log n)," they mean it for a balanced tree — and a BST is only balanced if you are careful about insertion order or use a self-balancing variant. Module 06 fixes the worst-case problem with AVL trees. For now, understand the base case: why the operations work, why the traversals produce what they produce, and why validation requires inherited bounds. Your posts this week should demonstrate that understanding. I look forward to them.
