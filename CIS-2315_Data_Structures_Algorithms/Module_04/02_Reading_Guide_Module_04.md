# Reading Guide: Module 04 – Stacks and Queues
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 04 – Stacks and Queues**! Stacks and queues are abstract data types built on top of arrays or linked lists that enforce a specific access order. They appear constantly in technical interviews — stacks power bracket matching, expression evaluation, and DFS; queues power BFS, task scheduling, and sliding window maximum. Knowing both their interface and their internal implementation is essential.

This module covers LIFO/FIFO semantics, monotonic stacks, deques, and the interview problems these structures solve.

---

### 1. High-Yield Glossary

*   **Stack**: A Last-In-First-Out (LIFO) abstract data type supporting `push` (add to top), `pop` (remove from top), and `peek` (read top without removing). All three operations are O(1). Used for call stacks, undo history, DFS traversal, and bracket validation.

*   **Queue**: A First-In-First-Out (FIFO) abstract data type supporting `enqueue` (add to back) and `dequeue` (remove from front). All operations are O(1) when implemented with a doubly linked list or circular array. Used for BFS traversal, task scheduling, and sliding window problems.

*   **Deque (double-ended queue)**: A generalization of both stack and queue that supports O(1) insertion and deletion at both ends. Python's `collections.deque` is the standard interview tool — use it instead of a list when you need efficient operations at both ends.

*   **Monotonic stack**: A stack that is maintained in strictly increasing or strictly decreasing order. When a new element violates the order, elements are popped until the constraint is satisfied. Used to find the next greater element, largest rectangle in histogram, and similar problems in O(n) time.

*   **LIFO (Last-In-First-Out)**: The access order of a stack — the most recently added element is the first one removed. Analogous to a pile of plates: you always take from the top.

*   **FIFO (First-In-First-Out)**: The access order of a queue — the first element added is the first one removed. Analogous to a line at a store: customers are served in the order they arrived.

*   **Circular buffer (ring buffer)**: An array-based queue implementation where the front and back indices wrap around using modulo arithmetic, enabling O(1) enqueue and dequeue without shifting elements. Used in fixed-capacity queue implementations.

---

### 2. Certification Exam Tips
*   **Brackets and parentheses = stack:** Any problem involving matching pairs (valid parentheses, HTML tag matching, decode string) is solved with a stack. The pattern: push opening brackets, pop on closing, check for mismatch.
*   **BFS always uses a queue:** When you see "shortest path," "level-order traversal," or "minimum steps," BFS is the algorithm and a queue is the data structure. Use `collections.deque` and `popleft()`.
*   **Monotonic stack solves Next Greater Element in O(n):** Brute force is O(n²); a monotonic stack processes each element at most twice (pushed once, popped once), giving O(n).
*   **Implement a queue using two stacks:** This is a classic interview question (LeetCode #232). Push always goes to stack1; pop moves all elements to stack2 if stack2 is empty. Amortized O(1) per operation.
*   **Know Python's stack and queue tools:** Stack → `list` with `.append()` and `.pop()`. Queue → `collections.deque` with `.append()` and `.popleft()`. Priority queue → `heapq`.
*   **Study Resource:** Work through [LeetCode Stack Explore Card](https://leetcode.com/explore/learn/card/queue-stack/) — a free structured module covering stack and queue fundamentals with progressively harder problems.

---

### Required Readings & Videos
*   **Required Reading:** [Stacks and Queues – Open Data Structures (Pat Morin), Chapter 2.3–2.4](https://opendatastructures.org/ods-python/2_3_ArrayDeque.html) — covers array-based implementations of stacks, queues, and deques with code and complexity proofs.
*   **Required Video:** [Stack & Queue – NeetCode on YouTube](https://www.youtube.com/watch?v=0Z5WWrME8bg) — a 25-minute walkthrough of stack and queue internals, the monotonic stack pattern, and LeetCode problem walkthroughs.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a stack using a Python list** and a queue using a singly linked list, verifying O(1) operations for both.
*   **Solve LeetCode #20 (Valid Parentheses)** using a stack — the canonical bracket-matching problem.
*   **Solve LeetCode #496 (Next Greater Element I)** using a monotonic stack, comparing your O(n) solution to a brute-force O(n²) approach.
*   **Solve LeetCode #232 (Implement Queue Using Two Stacks)** and explain the amortized O(1) cost.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 2.3–2.4 of Open Data Structures.
- [ ] Watch the NeetCode Stack & Queue video.
- [ ] Implement a stack and linked-list queue from scratch.
- [ ] Solve LeetCode #20, #496, and #232.
- [ ] Proceed to the Module 04 Quiz.
