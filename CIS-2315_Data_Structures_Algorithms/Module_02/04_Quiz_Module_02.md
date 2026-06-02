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
