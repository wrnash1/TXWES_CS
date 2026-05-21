# Quiz: Module 03 – Linked Lists: Singly and Doubly
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the time complexity of deleting a node from the middle of a singly linked list when you are given only a pointer to that node (not to its predecessor)?
*   A) O(1)
*   B) O(n)
*   C) O(log n)
*   D) O(n²)
*   **Correct Answer:** A) O(1)
*   **Distractor Analysis:**
    *   *Why correct:* Copy the value of the next node into the current node and then set current.next = current.next.next, effectively deleting the next node while keeping the pointer valid. This is O(1) — a classic interview trick (LeetCode #237).
    *   B is incorrect: O(n) would be required if you had to traverse from the head to find the predecessor, but the trick above avoids that.
    *   C is incorrect: O(log n) has no application here; there is no halving or search structure.
    *   D is incorrect: O(n²) would imply nested traversal which is entirely unnecessary for a single deletion.

---

**Question 2**
Which of the following is the most accurate definition of **Floyd's cycle detection algorithm** (fast and slow pointer)?
*   A) An algorithm that finds the shortest path between two nodes in a graph by expanding outward one level at a time, using a queue to track visited nodes.
*   B) A two-pointer technique where one pointer advances one node per step and another advances two nodes per step; if a cycle exists they will eventually meet, and the cycle entry point can be found by resetting one pointer to the head and advancing both one step at a time until they meet again.
*   C) A method for reversing a linked list in-place by maintaining three pointers (prev, curr, next) and redirecting each node's next pointer to its predecessor.
*   D) A divide-and-conquer approach that splits a linked list in half recursively until single nodes remain, then merges them back in sorted order.
*   **Correct Answer:** B) A two-pointer technique where one pointer advances one node per step and another advances two nodes per step; if a cycle exists they will eventually meet, and the cycle entry point can be found by resetting one pointer to the head and advancing both one step at a time until they meet again.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes Breadth-First Search (BFS) on a graph, not Floyd's algorithm on a linked list.
    *   *Why B is correct:* Floyd's algorithm uses exactly this two-phase approach: phase 1 detects the cycle (fast meets slow), phase 2 finds the entry node.
    *   *Why C is incorrect:* That describes iterative in-place reversal, a separate linked list technique.
    *   *Why D is incorrect:* That describes merge sort applied to a linked list, not cycle detection.

---

**Question 3**
Which advantage does a doubly linked list have over a singly linked list?
*   A) Doubly linked lists use less memory per node.
*   B) Doubly linked lists allow O(1) deletion of a node when given only a pointer to that node, without the copy-value trick.
*   C) Doubly linked lists support O(1) random access by index.
*   D) Doubly linked lists eliminate the need for a head pointer.
*   **Correct Answer:** B) Doubly linked lists allow O(1) deletion of a node when given only a pointer to that node, without the copy-value trick.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Doubly linked list nodes store an extra `prev` pointer, using *more* memory per node, not less.
    *   *Why B is correct:* With a `prev` pointer, you can access the predecessor directly (node.prev) and splice out the current node in O(1) cleanly, without the copy-value workaround.
    *   *Why C is incorrect:* Neither singly nor doubly linked lists support O(1) random access; reaching index k always requires O(k) traversal.
    *   *Why D is incorrect:* Both list types still need a head reference to start traversal.

---

**Question 4**
You need to find the k-th node from the end of a singly linked list in a single pass. Which technique works best?
*   A) Traverse the list twice: first to count n nodes, then to access node n–k.
*   B) Copy all nodes into an array, then access index (length–k) directly.
*   C) Use the runner technique: advance one pointer k steps ahead, then move both pointers one step at a time until the lead pointer reaches the end.
*   D) Use a recursive function that counts nodes on the call stack and returns the target on the way back up.
*   **Correct Answer:** C) Use the runner technique: advance one pointer k steps ahead, then move both pointers one step at a time until the lead pointer reaches the end.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Two passes work correctly but do not satisfy "single pass." It is O(n) time but misses the one-pass constraint.
    *   *Why B is incorrect:* Copying to an array is O(n) time and O(n) space; the runner technique uses O(1) space.
    *   *Why C is correct:* The runner/two-pointer technique covers the list in exactly one pass with O(1) auxiliary space. When the lead pointer exits, the trailing pointer is at node n–k.
    *   *Why D is incorrect:* Recursion uses O(n) call stack space — it solves the problem but wastes memory unnecessarily.

---

**Question 5**
What is the purpose of using a dummy (sentinel) head node when implementing linked list operations?
*   A) It increases the traversal speed by storing a pointer to the middle of the list.
*   B) It eliminates special-case code for operations at the head of the list, because the dummy node is always present and the real list starts at dummy.next.
*   C) It reduces memory usage by sharing a single node reference across multiple lists.
*   D) It prevents the garbage collector from freeing the first node while the list is being modified.
*   **Correct Answer:** B) It eliminates special-case code for operations at the head of the list, because the dummy node is always present and the real list starts at dummy.next.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A dummy head stores no list data and provides no pointer to the middle; it is positioned before the first real element.
    *   *Why B is correct:* With a dummy head, insert and delete operations at any position use the same pointer-update logic, removing the `if head is None` and `if removing head` branches.
    *   *Why C is incorrect:* Dummy nodes do not share references across lists; each list has its own dummy head.
    *   *Why D is incorrect:* Garbage collection behavior is unrelated to the algorithmic purpose of a dummy head node.
