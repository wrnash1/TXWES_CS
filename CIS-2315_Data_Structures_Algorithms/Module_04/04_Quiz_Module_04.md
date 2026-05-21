# Quiz: Module 04 – Stacks and Queues
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
Which data structure should you use to implement a DFS (Depth-First Search) iteratively?
*   A) Queue
*   B) Stack
*   C) Hash map
*   D) Min-heap
*   **Correct Answer:** B) Stack
*   **Distractor Analysis:**
    *   *Why correct:* DFS explores as deep as possible before backtracking — exactly LIFO behavior. Each node's unvisited neighbors are pushed onto the stack; the most recently pushed node is explored next.
    *   A is incorrect: A queue implements BFS (breadth-first), not DFS.
    *   C is incorrect: A hash map tracks visited nodes but does not drive traversal order.
    *   D is incorrect: A min-heap is used in Dijkstra's shortest path algorithm, not plain DFS.

---

**Question 2**
Which of the following is the most accurate definition of a **monotonic stack** in the context of algorithms?
*   A) A stack that stores elements in sorted order by repeatedly inserting new elements at their correct position using binary search, enabling O(log n) push.
*   B) A stack maintained in strictly increasing or decreasing order by popping elements that violate the ordering constraint before each push, enabling O(n) total solutions to problems like Next Greater Element.
*   C) A stack that limits its size to O(log n) elements by evicting the oldest item when capacity is exceeded, trading recency for space efficiency.
*   D) A stack backed by two queues to achieve O(1) push and amortized O(1) pop by lazily moving elements between queues only when needed.
*   **Correct Answer:** B) A stack maintained in strictly increasing or decreasing order by popping elements that violate the ordering constraint before each push, enabling O(n) total solutions to problems like Next Greater Element.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes insertion into a sorted array or a sorted structure, not a stack. Stacks do not use binary search.
    *   *Why B is correct:* The monotonic stack processes each element at most twice (one push, one pop), giving O(n) total work. The invariant (increasing or decreasing) is what enables finding the next-greater or next-smaller element efficiently.
    *   *Why C is incorrect:* That describes an LRU cache or eviction policy, not a monotonic stack.
    *   *Why D is incorrect:* That describes implementing a stack using two queues (or a queue using two stacks), a separate classic interview problem.

---

**Question 3**
You implement a queue using two stacks (s1 for push, s2 for pop). What is the amortized time complexity of the dequeue operation?
*   A) O(n) per dequeue always
*   B) O(log n) per dequeue
*   C) O(1) amortized per dequeue
*   D) O(n²) worst case total
*   **Correct Answer:** C) O(1) amortized per dequeue
*   **Distractor Analysis:**
    *   *Why A is incorrect:* O(n) is the worst case for a *single* dequeue when s2 is empty and all n elements must be moved from s1 — but that expensive operation only occurs once every n dequeues.
    *   *Why B is incorrect:* There is no logarithmic structure in transferring elements between two stacks.
    *   *Why C is correct:* Each element is pushed to s1 once and moved to s2 once — two operations total per element across all dequeues. Dividing by n operations gives O(1) amortized.
    *   *Why D is incorrect:* Total cost for n dequeues is O(n), not O(n²). O(n²) would imply O(n) work per operation always.

---

**Question 4**
While checking for valid parentheses in the string `"({[]})"`, a stack-based algorithm processes each character. What is the correct final state of the stack after processing the entire string?
*   A) The stack contains `[`, `{` because they were pushed but not matched.
*   B) The stack is empty, indicating all brackets were matched correctly.
*   C) The stack contains `)` because closing brackets are pushed, not popped.
*   D) The stack contains all six characters because push and pop happen at different phases.
*   **Correct Answer:** B) The stack is empty, indicating all brackets were matched correctly.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `{` and `[` are pushed then properly popped when their matching `}` and `]` are encountered. A non-empty stack means unmatched openers remain.
    *   *Why B is correct:* In `"({[]})"`, every opening bracket is matched by a corresponding closing bracket in correct order. A valid string always leaves an empty stack.
    *   *Why C is incorrect:* Closing brackets trigger a pop (to check the matching opener); they are never pushed themselves.
    *   *Why D is incorrect:* The algorithm interleaves pushes and pops as each character is read, not in two separate phases.

---

**Question 5**
Which Python data structure provides O(1) operations at both the front and back, making it the preferred choice for implementing both stacks and queues in interview solutions?
*   A) `list` — supports O(1) append and O(1) pop from the right end only.
*   B) `collections.deque` — supports O(1) append and O(1) popleft at both ends.
*   C) `heapq` — supports O(log n) push and O(log n) pop with automatic ordering.
*   D) `dict` — supports O(1) insertion and deletion by key, usable as a queue with integer keys.
*   **Correct Answer:** B) `collections.deque` — supports O(1) append and O(1) popleft at both ends.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Python `list.insert(0, x)` and `list.pop(0)` are O(n) because all elements shift. Using a list as a queue is a common and costly interview mistake.
    *   *Why B is correct:* `collections.deque` is implemented as a doubly-linked list of fixed-size blocks, giving true O(1) operations at both ends. It is the correct tool for BFS queues and sliding window deque problems.
    *   *Why C is incorrect:* `heapq` is a priority queue, not a general stack or FIFO queue. Its operations are O(log n), not O(1).
    *   *Why D is incorrect:* Using a dict as a queue is non-standard, error-prone, and does not provide O(1) ordered removal semantics.
