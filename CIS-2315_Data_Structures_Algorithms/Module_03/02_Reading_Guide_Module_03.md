# Reading Guide: Module 03 – Linked Lists: Singly and Doubly
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 03 – Linked Lists: Singly and Doubly**! Linked lists are the classic example of a pointer-based data structure and one of the most heavily tested topics in technical interviews. Problems like reversing a list, detecting a cycle, finding the middle node, and merging sorted lists appear on LeetCode, Google, and Meta interviews regularly. Mastering linked lists also builds the pointer manipulation skills needed for trees and graphs.

This module covers the internal structure of singly and doubly linked lists, their time/space trade-offs versus arrays, and the most common interview patterns.

---

### 1. High-Yield Glossary

*   **Singly linked list**: A linear data structure where each node holds a data value and a single `next` pointer to the following node. The last node's `next` is `None`. Traversal is O(n) forward-only; there is no backward link.

*   **Doubly linked list**: A linked list where each node holds a data value, a `next` pointer, and a `prev` pointer to the preceding node. This enables O(1) deletion of a node given only its reference, and O(n) traversal in either direction.

*   **Head and tail pointers**: References to the first and last nodes of the list. Maintaining a tail pointer allows O(1) append to the end; without it, appending requires O(n) traversal to find the last node.

*   **Fast and slow pointer (Floyd's algorithm)**: A two-pointer technique where one pointer advances one node at a time and another advances two. When they meet, a cycle exists; when the fast pointer reaches the end, the slow pointer is at the middle. Essential for cycle detection (LeetCode #141/#142) and finding the midpoint.

*   **Sentinel / dummy node**: A placeholder node inserted at the head (or both head and tail) of a list to eliminate special-case logic for empty lists or operations at the boundary. Common in implementations to avoid `if head is None` checks.

*   **In-place reversal**: Reversing a linked list without allocating a new list by updating `next` pointers iteratively with three pointers (prev, curr, next). Runs in O(n) time and O(1) auxiliary space.

*   **Runner technique**: A variant of fast/slow pointers where one pointer is advanced k steps ahead of the other before both start moving, used to find the k-th node from the end in one pass.

---

### 2. Certification Exam Tips
*   **Draw every pointer change on paper:** Linked list bugs are almost always pointer update errors. Before coding, sketch the before/after state of `prev`, `curr`, and `next` for one iteration of your loop.
*   **Handle edge cases first:** What happens with an empty list? A single-node list? A two-node list? State these explicitly before your interviewer asks.
*   **Cycle detection is always fast/slow pointers:** If you see "cycle," reach for Floyd's algorithm immediately. Memorize the two-phase approach: detect (meet in cycle), then find entry point (reset one pointer to head, advance both one step at a time).
*   **Merging sorted lists is a common variant:** LeetCode #21 (Merge Two Sorted Lists) and #23 (Merge k Sorted Lists). The two-list version is O(m+n); the k-list version uses a min-heap for O(N log k).
*   **Dummy head simplifies boundary logic:** For problems that modify the list structure (remove nth from end, insert, partition), always use a dummy node — it removes the "is head being changed?" special case.
*   **Study Resource:** Explore the [LeetCode Linked List Explore Card](https://leetcode.com/explore/learn/card/linked-list/) for a structured set of problems with hints, progressing from basic traversal to advanced in-place manipulation.

---

### Required Readings & Videos
*   **Required Reading:** [Linked Lists – Open Data Structures (Pat Morin), Chapter 3](https://opendatastructures.org/ods-python/3_Linked_Lists.html) — covers singly and doubly linked list implementations with Python code and full complexity analysis.
*   **Required Video:** [Linked List – NeetCode on YouTube](https://www.youtube.com/watch?v=Hj_rA0dhr2I) — a 30-minute deep dive covering node structure, reversal, and cycle detection with LeetCode walkthroughs.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a `SinglyLinkedList` class** with `append`, `prepend`, `delete_by_value`, `reverse`, and `__str__` methods from scratch.
*   **Solve LeetCode #206 (Reverse Linked List)** iteratively and recursively, comparing stack space usage.
*   **Solve LeetCode #141 (Linked List Cycle)** using Floyd's fast/slow pointer algorithm.
*   **Solve LeetCode #876 (Middle of the Linked List)** using the fast/slow pointer to find the midpoint in one pass.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 3 of Open Data Structures.
- [ ] Watch the NeetCode Linked List video.
- [ ] Implement the SinglyLinkedList class from scratch.
- [ ] Solve LeetCode #206, #141, and #876.
- [ ] Proceed to the Module 03 Quiz.
