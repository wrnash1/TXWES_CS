# Reading Guide: Module 08 – Heaps and Priority Queues
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 08 – Heaps and Priority Queues**! A heap is a complete binary tree stored in an array that maintains the heap property, enabling O(log n) insertion and O(log n) deletion of the minimum (or maximum) element. Heaps power priority queues, which are essential for Dijkstra's shortest path algorithm, Prim's MST, and a wide class of "top K" interview problems. Understanding how heaps work internally — not just how to call `heapq.heappush` — is expected at mid-level and above.

This module covers min-heap and max-heap structure, array-based storage, heapify, and the top-K and k-way merge interview patterns.

---

### 1. High-Yield Glossary

*   **Heap**: A complete binary tree (all levels filled left to right) satisfying the heap property. In a min-heap, every parent's value is ≤ its children's values. In a max-heap, every parent's value is ≥ its children's values. The extremal element (min or max) is always at the root.

*   **Min-heap**: A heap where the smallest element is at the root. `heapq` in Python is a min-heap by default. Used when you repeatedly need to extract the minimum (Dijkstra, scheduling, top-K largest using a min-heap of size K).

*   **Max-heap**: A heap where the largest element is at the root. Python simulates a max-heap by negating values before pushing. Used when you need to repeatedly extract the maximum (k-th largest, sliding window maximum).

*   **Sift-up (bubble-up)**: The process of restoring the heap property after insertion. The new element is placed at the end of the array and repeatedly swapped with its parent until the heap property holds. O(log n) time.

*   **Sift-down (heapify-down)**: The process of restoring the heap property after extracting the root. The last element replaces the root, then is repeatedly swapped with its smaller (min-heap) or larger (max-heap) child until the property holds. O(log n) time.

*   **Heapify (build-heap)**: Converting an arbitrary array of n elements into a valid heap in O(n) time by calling sift-down on every non-leaf node from bottom to top. More efficient than inserting n elements one by one (which would be O(n log n)).

*   **Priority queue**: An abstract data type that allows inserting elements with priorities and extracting the element with the highest (or lowest) priority. Typically implemented with a heap. Python's `heapq` module implements a min-priority queue.

---

### 2. Certification Exam Tips
*   **Top-K problems: use a heap of size K:** To find the K largest elements, maintain a min-heap of size K as you iterate. Push each element; if heap size exceeds K, pop the minimum. At the end, all K elements remaining are the largest. O(n log K) time, O(K) space.
*   **Python max-heap trick:** Python's `heapq` is always a min-heap. To simulate a max-heap, negate values on push and negate again on pop: `heapq.heappush(h, -val)`, then `-heapq.heappop(h)`.
*   **Heapify vs. repeated insertion:** Building a heap with `heapq.heapify([...])` is O(n). Pushing n elements one by one is O(n log n). Interviewers may ask why — know the proof sketch (half the nodes are leaves, do O(1) work; the analysis sums a converging series).
*   **K-way merge uses a heap:** Merging K sorted arrays (LeetCode #23) uses a min-heap. Push the first element of each array with its source index. Pop minimum, push the next from its source. O(N log K) total where N is total elements.
*   **Dijkstra needs a min-heap:** Each time you explore a node, push its neighbors with updated distances. Pop the minimum distance node next. O((V + E) log V) with a binary heap.
*   **Study Resource:** [Python heapq documentation](https://docs.python.org/3/library/heapq.html) — official Python docs with heap operation examples and the `nlargest`/`nsmallest` functions. Knowing the standard library API is expected in interviews.

---

### Required Readings & Videos
*   **Required Reading:** [Heaps – Open Data Structures (Pat Morin), Chapter 10](https://opendatastructures.org/ods-python/10_Heaps.html) — covers the array-based binary heap, sift-up, sift-down, and the O(n) build-heap proof.
*   **Required Video:** [Heap / Priority Queue – NeetCode on YouTube](https://www.youtube.com/watch?v=pLh-Q56i_yI) — a 30-minute interview-focused video covering heap internals, Python `heapq` API, and the top-K and K-way merge patterns with LeetCode walkthroughs.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a MinHeap class from scratch** with `push`, `pop`, `peek`, `_sift_up`, and `_sift_down` methods using an internal Python list.
*   **Solve LeetCode #215 (Kth Largest Element in an Array)** using a min-heap of size K.
*   **Solve LeetCode #347 (Top K Frequent Elements)** using `heapq.nlargest` with a frequency map.
*   **Solve LeetCode #23 (Merge k Sorted Lists)** using a min-heap for the K-way merge.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 10 of Open Data Structures.
- [ ] Watch the NeetCode Heap / Priority Queue video.
- [ ] Implement a MinHeap class from scratch.
- [ ] Solve LeetCode #215, #347, and #23.
- [ ] Proceed to the Module 08 Quiz.
