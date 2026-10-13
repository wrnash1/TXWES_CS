# Quiz: Module 02 — Singly and Doubly Linked Lists

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the time complexity of prepending (inserting at the head) a singly linked list?

- A) O(n) — must find the last node first
- B) O(log n) — the list uses a sorted structure
- C) O(1) — update the head pointer and link the new node
- D) O(n²) — must update all node references

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Finding the last node requires traversal — but prepend inserts at the head, not the tail. No traversal is needed: link the new node to the existing head, then update the head pointer. Two pointer operations: O(1).
- *Why B is incorrect:* Linked lists have no sorted structure; O(log n) would imply binary search or a balanced tree, which does not apply here.
- *Why C is correct:* Prepend always inserts at the head. The operation is: create a new node, set `new_node.next = self.head`, then set `self.head = new_node`. This is two pointer assignments regardless of list length — O(1).
- *Why D is incorrect:* No other node references need updating. Only the new node's `next` and the list's `head` pointer change. All other nodes are untouched.

---

### Question 2

A singly linked list without a tail pointer must traverse the entire list to append. If you add a `tail` pointer, what does append become?

- A) O(log n) — the tail pointer allows binary search
- B) O(1) — point the current tail's `next` to the new node, update tail
- C) O(n) — the list must still be validated before appending
- D) O(n²) — two traversals are required for tail updates

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A tail pointer is a direct reference to the last node — it enables O(1) access, not binary search. O(log n) would require a sorted, tree-like structure.
- *Why B is correct:* With a `tail` pointer, append is: set `self.tail.next = new_node`, then update `self.tail = new_node`. Two pointer assignments — O(1). The tail pointer eliminates the need for traversal.
- *Why C is incorrect:* No validation traversal is required. The tail pointer gives you a direct reference to where the new node should attach.
- *Why D is incorrect:* Append with a tail pointer is two pointer operations, not two traversals. O(n²) would require a nested structure.

---

### Question 3

Why is O(1) deletion by node reference possible in a doubly linked list but not in a singly linked list?

- A) Doubly linked lists use contiguous memory, making pointer updates faster
- B) A doubly linked list node has a `prev` pointer, so its predecessor can be found without traversal
- C) Singly linked lists do not support deletion — only insertion
- D) Doubly linked lists cache node positions for O(1) lookup

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Linked lists — singly or doubly — do not use contiguous memory. That describes arrays. Both types scatter nodes across memory and use pointers.
- *Why B is correct:* To delete a node from a singly linked list, you must update its predecessor's `next` pointer — but the node has no reference to its predecessor, requiring O(n) traversal to find it. A doubly linked list node has a `prev` pointer that directly references its predecessor. Given the node to delete, you can reach both neighbors in O(1) and update both links without traversal.
- *Why C is incorrect:* Singly linked lists fully support deletion. It just costs O(n) to find the node before the target.
- *Why D is incorrect:* Linked lists do not cache positions. A doubly linked list's advantage is the bidirectional pointer, not any caching mechanism.

---

### Question 4

Given a linked list with the values `1 → 2 → 3 → 4 → 5`, what does the following code return?

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow.value
```

- A) `2`
- B) `3`
- C) `4`
- D) `5`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* After one iteration, `slow` is at node 2 and `fast` is at node 3. The loop continues because `fast.next` (node 4) exists.
- *Why B is correct:* Trace the pointers: start — slow=1, fast=1. Iteration 1 — slow=2, fast=3. Iteration 2 — slow=3, fast=5. After iteration 2, `fast.next` is None, so the loop stops. `slow` is at node 3 — the middle of the five-element list. The fast-slow pointer finds the middle in one pass.
- *Why C is incorrect:* Node 4 would be reached if `slow` advanced one more time. But the loop terminates when `fast.next` is None (after slow reaches 3).
- *Why D is incorrect:* Node 5 is the last element, not the middle. `fast` reaches 5, but `slow` only reaches 3.

---

### Question 5

In the standard iterative linked list reversal algorithm, why must `next_node = current.next` be saved before modifying `current.next`?

- A) To preserve the original list order for comparison after reversal
- B) To avoid losing the reference to the rest of the unreversed list when `current.next` is overwritten
- C) Because Python requires variable assignment before pointer modification
- D) To allow the algorithm to run in O(1) space rather than O(n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The original list is being modified in place — it is not preserved for comparison. The reason for saving `next_node` is operational correctness during the reversal, not for reference afterward.
- *Why B is correct:* The line `current.next = prev` overwrites the `next` pointer, severing the connection to the rest of the list. If you have not saved `current.next` first, you have no way to advance `current` to the next node — the rest of the list is unreachable. Saving `next_node = current.next` before the overwrite preserves the forward reference.
- *Why C is incorrect:* Python has no such requirement. This is a logical necessity of the algorithm, not a language constraint.
- *Why D is incorrect:* The O(1) space comes from using pointer variables (`prev`, `current`, `next_node`) instead of a copy of the list. Saving `next_node` is one scalar variable — it does not change the space complexity, and space efficiency is not why it is needed.

---

### Question 6

An LRU (Least Recently Used) cache must support `get(key)` and `put(key, value)` both in O(1). Which data structure combination achieves this?

- A) Array + binary search tree
- B) Hash map alone
- C) Doubly linked list + hash map
- D) Singly linked list + sorted array

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A binary search tree supports O(log n) operations, not O(1). An array insertion/deletion is O(n) due to shifting. Neither meets the O(1) requirement.
- *Why B is incorrect:* A hash map provides O(1) `get` and `put` for key-value pairs, but it has no inherent ordering. An LRU cache must track which item was used least recently and evict it — a hash map alone cannot maintain access order.
- *Why C is correct:* The doubly linked list maintains access order: the most recently used item is at the tail, the least recently used at the head. The hash map maps each key to its node reference for O(1) access. On `get`: find the node (O(1) via hash map), move it to the tail (O(1) via doubly linked list delete + append). On `put` with eviction: delete the head node (O(1)), remove from map (O(1)), add new node at tail (O(1)).
- *Why D is incorrect:* A singly linked list cannot delete a node in O(1) without knowing the previous node. A sorted array insertion/deletion is O(n). Neither combination achieves O(1) for both operations.

---

### Question 7

What is the time complexity of searching for a value in a singly linked list?

- A) O(1) — use the head pointer for direct access
- B) O(log n) — use binary search from the midpoint
- C) O(n) — must traverse from head until value is found or list ends
- D) O(n log n) — linked lists require a merge-sort-like search

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The head pointer only gives O(1) access to the first node. To reach any other node, you must follow `next` pointers sequentially. There is no O(1) path to arbitrary positions.
- *Why B is incorrect:* Binary search requires O(1) random access by index — you must be able to jump directly to the midpoint. Linked lists have no index — reaching the midpoint requires O(n/2) traversal. Binary search does not apply.
- *Why C is correct:* In the worst case (target not in list, or target is the last node), every node must be visited. There are n nodes, and each requires one pointer dereference — O(n).
- *Why D is incorrect:* O(n log n) has no connection to searching a linked list. It is the complexity of efficient sorting algorithms.

---

### Question 8

A developer uses a `visited` set to detect a cycle in a linked list. What is the space complexity compared to Floyd's two-pointer algorithm?

- A) Both are O(1) space
- B) Both are O(n) space
- C) The visited set is O(n); Floyd's is O(1)
- D) The visited set is O(1); Floyd's is O(n)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The visited set stores a reference for every node visited. In a list of n nodes, it can hold up to n entries — O(n) space. Floyd's algorithm uses only two pointer variables regardless of list length — O(1).
- *Why B is incorrect:* Floyd's algorithm uses exactly two extra pointer variables (`slow` and `fast`). Two variables regardless of input size is O(1) auxiliary space.
- *Why C is correct:* The visited set approach: `if node in visited: return True; visited.add(node)` — in the worst case (no cycle), every node is added. Space is O(n). Floyd's algorithm only ever uses two pointer variables — O(1) space. Both algorithms have O(n) time complexity; the space is the difference.
- *Why D is incorrect:* This reverses the correct answer. The visited set is the O(n) approach; Floyd's two-pointer is the O(1) approach.

---

### Question 9

Which comparison best describes the trade-off between arrays and singly linked lists?

- A) Arrays have O(1) insert/delete anywhere; linked lists have O(1) index access
- B) Arrays have O(1) index access; linked lists have O(1) insert/delete at a known position
- C) Arrays and linked lists have the same complexity for all operations
- D) Linked lists are strictly better than arrays in every operation

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This reverses the correct comparison. Arrays have O(n) insert/delete in the middle (due to shifting). Linked lists have O(n) index access (due to traversal).
- *Why B is correct:* Arrays store elements contiguously, enabling O(1) access by index via address arithmetic. But insertion or deletion anywhere except the end requires shifting elements — O(n). Linked lists have no index; access requires traversal — O(n). But once you have a reference to the target position, insertion or deletion is just pointer reassignment — O(1). The trade-off is index access vs positional modification.
- *Why C is incorrect:* The two structures have meaningfully different complexity profiles. This is the core reason they are both taught and why the choice matters for algorithm design.
- *Why D is incorrect:* Neither structure is strictly better. Arrays dominate for random access, iteration, and cache performance. Linked lists dominate for frequent positional insertions and deletions and when O(1) delete-by-reference is required.

---

### Question 10

What does adding a dummy head node `dummy = Node(0); dummy.next = head` accomplish in a linked list algorithm?

- A) It stores the size of the list for O(1) length queries
- B) It eliminates special-case handling for operations that affect the head node
- C) It converts the singly linked list into a doubly linked list
- D) It prevents the garbage collector from freeing the head node

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A dummy node holds an arbitrary value and a `next` pointer — it does not store a count. O(1) length requires a separate `size` attribute.
- *Why B is correct:* Without a dummy node, operations that might affect the head node (delete the first element, insert before the first element) require special-case `if` branches. With `dummy.next = head`, every operation treats the dummy node as the node before the head, making the head just another node in the list — no special case. The final list is `dummy.next`. This pattern appears in Remove Nth Node From End, Merge Two Sorted Lists, and many other problems.
- *Why C is incorrect:* A dummy node is still a singly linked node — it has only a `next` pointer. Adding it does not create a doubly linked list.
- *Why D is incorrect:* Python's garbage collector operates on reference counts, not on special sentinel objects. The dummy node has no relationship to garbage collection behavior.

---

### Question 11

**Each question is worth 5 points.**

What is the time complexity of accessing the kth element of a singly linked list (0-indexed)?

- A) O(1) — use the head pointer and index directly
- B) O(k) — traverse k steps from the head
- C) O(log k) — use binary search on the list
- D) O(n) always, regardless of k

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Linked lists store nodes in non-contiguous memory connected by pointers. Unlike arrays, there is no base-address + offset formula. Reaching the kth node requires following exactly k `next` pointers from the head.
- *Why B is correct:* Starting at `head`, advance `current = current.next` exactly k times to reach the kth node. This costs k pointer dereferences — O(k). For the last element (k = n−1), this becomes O(n). For the first element (k = 0), it is O(1). The general case is O(k).
- *Why C is incorrect:* Binary search requires O(1) random access to jump to any midpoint. Linked lists lack this property — reaching the midpoint costs O(n/2) traversal. Binary search cannot be applied to a linked list in its standard form.
- *Why D is incorrect:* O(n) is the worst case (accessing the last element), but not always the cost. Accessing `head` (k=0) is O(1), and accessing any early node is O(k). The tightest correct answer for the kth element specifically is O(k).

---

### Question 12

In Floyd's cycle detection algorithm, if a cycle of length L exists and the distance from the head to the cycle entry point is F, how many steps does `slow` take before it meets `fast` inside the cycle?

- A) Exactly F steps
- B) F + L steps
- C) At most F + L steps — `slow` meets `fast` no later than one full cycle after entering the loop
- D) 2F steps — because `fast` travels exactly twice as far

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `slow` enters the cycle after F steps. Once inside, `fast` is somewhere in the cycle and gains one node per step on `slow`. They will meet within at most L additional steps. So `slow` travels at most F + L total steps, not just F.
- *Why B is incorrect:* F + L is the upper bound, not an exact count. Depending on where `fast` is when `slow` enters the cycle, they may meet in fewer than L additional steps.
- *Why C is correct:* Once `slow` enters the cycle (after F steps), the relative speed of `fast` over `slow` is 1 node per step. Since the cycle has length L, `fast` will catch `slow` within at most L steps. Total steps for `slow` ≤ F + L. This is the standard analysis used to prove Floyd's algorithm terminates.
- *Why D is incorrect:* `fast` does travel 2× the steps of `slow`, but this describes a ratio, not when they meet. The meeting point analysis requires reasoning about the cycle's modular arithmetic, not simply doubling F.

---

### Question 13

Which operation on a doubly linked list has a different time complexity compared to a singly linked list?

- A) Search by value
- B) Traversal from head to tail
- C) Deletion given only the node reference (not a predecessor reference)
- D) Insertion at the head

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Both singly and doubly linked lists require O(n) traversal to find a node by value. The `prev` pointer does not help search — you still scan from head.
- *Why B is incorrect:* Traversal from head to tail is O(n) for both types. A doubly linked list can also traverse in reverse, but forward traversal costs the same.
- *Why C is correct:* In a singly linked list, deleting a node given only its own reference requires finding its predecessor — O(n) traversal. In a doubly linked list, the node's `prev` pointer directly references the predecessor, enabling O(1) deletion with no traversal.
- *Why D is incorrect:* Head insertion is O(1) for both singly and doubly linked lists. For doubly, you additionally set `self.head.prev = new_node`, which is one extra pointer assignment — still O(1).

---

### Question 14

A linked list contains the values `1 → 3 → 5 → 7 → 9`. After calling `reverse_list(head)`, what is the value of the new tail (the last node in the reversed list)?

- A) `9`
- B) `1`
- C) `5`
- D) `3`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `9` was the original tail — after reversal it becomes the new head (first node).
- *Why B is correct:* Reversing `1 → 3 → 5 → 7 → 9` produces `9 → 7 → 5 → 3 → 1`. The node that was originally the head (`1`) becomes the new tail. Its `next` pointer is set to `None` during the reversal when `current.next = prev` is executed with `prev = None`.
- *Why C is incorrect:* `5` is the middle node and remains in the middle after reversal: `9 → 7 → 5 → 3 → 1`.
- *Why D is incorrect:* `3` becomes the second-to-last node in the reversed list.

---

### Question 15

What memory advantage does an array have over a linked list when iterating through all n elements?

- A) Arrays use less total memory because they store no pointers
- B) Arrays benefit from CPU cache locality — contiguous memory means cache lines load multiple elements at once
- C) Arrays require fewer comparisons per element during iteration
- D) Arrays have no memory advantage; linked lists iterate in the same time

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* For Python objects, arrays (lists) and linked lists both store references (pointers) to objects. Python's `list` stores an array of pointers, and a linked list node stores both a value reference and a `next` pointer. The pointer count per element is similar or the linked list is higher due to the extra `next` (and `prev` for doubly) pointer.
- *Why B is correct:* Modern CPUs cache memory in 64-byte cache lines. When you access `arr[0]`, the CPU loads `arr[0]` through `arr[7]` (or more) into the L1 cache simultaneously. Subsequent accesses to `arr[1]`, `arr[2]`, etc., are served from cache — extremely fast. Linked list nodes are scattered across the heap; following each `next` pointer may cause a cache miss, requiring a fetch from main memory — orders of magnitude slower per access.
- *Why C is incorrect:* Both structures compare elements the same way during iteration. Iteration does not involve comparisons — it is just pointer dereferencing.
- *Why D is incorrect:* Cache performance is a measurable, significant difference. In microbenchmarks, iterating a Python list is typically 2-5× faster than iterating a linked list of the same size due to cache effects.

---

### Question 16

In the remove-nth-from-end algorithm using two pointers, why is the gap set to `n + 1` rather than `n`?

- A) To handle the edge case where the list has exactly n nodes
- B) So that when `fast` reaches `None`, `slow` is positioned at the node just before the target, enabling `slow.next = slow.next.next`
- C) To ensure `fast` and `slow` maintain equal spacing throughout
- D) Because Python's 0-based indexing requires an offset of 1

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* While using n+1 does handle the head-removal edge case (when the list has exactly n nodes), that is a side effect. The core reason for the n+1 gap is the positional requirement for deletion — `slow` must stop one node before the target, not at the target.
- *Why B is correct:* To delete a node, you need its predecessor's `next` pointer. If the gap were n, when `fast` hits `None`, `slow` would be exactly at the node to delete — but you can't delete without the predecessor. With a gap of n+1, `slow` stops one node earlier, so `slow.next` is the node to delete, and `slow.next = slow.next.next` performs the deletion cleanly.
- *Why C is incorrect:* The two pointers maintain a fixed gap of n+1 throughout — the gap does not change. This is true but it is the mechanism, not the reason for choosing n+1 over n.
- *Why D is incorrect:* Python's 0-based indexing is unrelated. The n+1 gap is a fundamental algorithm design choice for linked list deletion, not a language-specific offset.

---

### Question 17

When merging two sorted linked lists (LeetCode #21), what is the time complexity of the optimal iterative solution?

- A) O(n + m) where n and m are the lengths of the two lists
- B) O(n × m) — each node in one list is compared to every node in the other
- C) O(n log n) — one list must be sorted before merging
- D) O(n) where n is the length of the shorter list

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The merge algorithm compares the front elements of both lists, links the smaller one to the result, and advances one pointer. Each comparison advances at least one pointer. After at most n + m comparisons, all nodes from both lists are exhausted. Every node is visited exactly once — O(n + m).
- *Why B is incorrect:* O(n × m) would require comparing every node in one list to every node in the other — that would be a brute-force cartesian product. The merge algorithm never compares a pair more than once because pointers only advance forward.
- *Why C is incorrect:* Both input lists are already sorted by assumption (the problem states "two sorted lists"). No sorting step is needed.
- *Why D is incorrect:* The longer list's remaining nodes must still be attached to the result after the shorter list is exhausted. Both lists must be fully processed — the complexity depends on both n and m.

---

### Question 18

A problem asks you to check whether a singly linked list is a palindrome in O(n) time and O(1) extra space. Which approach achieves this?

- A) Copy all values into an array, then use two pointers on the array
- B) Use a stack to store the first half, then compare with the second half
- C) Find the middle using fast-slow pointers, reverse the second half in place, then compare from both ends
- D) Recursively compare the first and last nodes, shrinking the list each time

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Copying values into an array uses O(n) extra space. The constraint is O(1) extra space, so this approach is disqualified even though it achieves O(n) time.
- *Why B is incorrect:* A stack storing n/2 values uses O(n) extra space. The constraint is O(1), so this approach is disqualified.
- *Why C is correct:* Step 1: find the midpoint using fast-slow pointers — O(n), O(1) space. Step 2: reverse the second half in place — O(n), O(1) space. Step 3: compare node by node from both ends — O(n), O(1) space. Total: O(n) time, O(1) space. This is the canonical O(1) space palindrome-check solution for linked lists.
- *Why D is incorrect:* Recursion uses O(n) stack space (n recursive frames). Even though no explicit data structure is allocated, the call stack is auxiliary space — this does not satisfy O(1) extra space.

---

### Question 19

In Python, what is `node.next = node.next.next` doing in the context of a linked list?

- A) Swapping two adjacent nodes
- B) Removing the node immediately after `node` from the list by bypassing it
- C) Moving `node` to the position after its successor
- D) Reversing the direction of the link between `node` and its successor

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Swapping nodes requires updating both nodes' values or relinking multiple pointers. `node.next = node.next.next` only changes one pointer — `node`'s forward reference. No swap occurs.
- *Why B is correct:* Before: `node → A → B → …`. After `node.next = node.next.next`: `node → B → …`. Node A is bypassed — its predecessor (`node`) now skips over it and points directly to A's successor (B). In garbage-collected languages like Python, A will be freed if no other references to it exist. This is the standard linked list node deletion pattern.
- *Why C is incorrect:* `node`'s position in the list does not change. Only its `next` pointer is updated. `node` itself stays where it is.
- *Why D is incorrect:* Reversing a link would require setting `node.next.next = node` (pointing backward). This code only modifies `node`'s forward pointer.

---

### Question 20

What is the space complexity of a recursive linked list reversal, compared to an iterative reversal?

- A) Both are O(1) — recursion uses no extra memory for linked lists
- B) Recursive is O(n); iterative is O(1) — recursion uses O(n) call stack frames
- C) Both are O(n) — the output list requires O(n) space
- D) Recursive is O(log n); iterative is O(1) — recursion halves the list each call

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Each recursive call adds one frame to the Python call stack, storing the return address and local variable `head`. For a list of n nodes, the recursion reaches depth n before unwinding — O(n) stack frames.
- *Why B is correct:* The recursive reversal calls itself once per node, building a call stack n frames deep before any reversal happens. When the base case is reached, the stack unwinds and pointers are updated. Total auxiliary space: O(n) for the call stack. The iterative reversal uses three pointer variables (`prev`, `current`, `next_node`) regardless of list length — O(1) auxiliary space.
- *Why C is incorrect:* Neither version creates a new list — both reverse in place by modifying existing `next` pointers. The output is the same list with redirected pointers. No O(n) output allocation occurs.
- *Why D is incorrect:* The recursive reversal does not halve the list — it recurses on `head.next`, which is one node shorter (n−1, then n−2, …). This is O(n) depth recursion, not O(log n).
