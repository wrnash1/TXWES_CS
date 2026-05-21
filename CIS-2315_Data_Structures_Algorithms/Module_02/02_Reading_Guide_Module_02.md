# Reading Guide: Module 02 – Arrays and Dynamic Arrays
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 02 – Arrays and Dynamic Arrays**! Arrays are the most fundamental data structure in computer science and the foundation for dozens of interview problem patterns. A large fraction of LeetCode problems — two-pointer, sliding window, prefix sums, and more — are solved directly on arrays. Understanding how static and dynamic arrays work internally explains both their performance characteristics and the subtle bugs that trap candidates in interviews.

This module covers array memory layout, indexing, resizing, and the two-pointer and sliding window patterns that appear on virtually every technical interview track.

---

### 1. High-Yield Glossary
Review these essential definitions carefully:

*   **Static array**: A contiguous block of memory of fixed size allocated at compile time or initialization. Elements are accessed in O(1) via index arithmetic (base_address + index × element_size), but the capacity cannot change after allocation.

*   **Dynamic array**: A resizable array (Python `list`, Java `ArrayList`) that starts with an initial capacity and automatically allocates a larger backing array (typically doubling in size) when the current capacity is exceeded. Appending is O(1) amortized due to the doubling strategy.

*   **Index / random access**: Direct element retrieval using a numeric position in O(1) time, possible because all elements are stored at predictable memory offsets. This is the primary performance advantage of arrays over linked lists.

*   **Two-pointer technique**: An algorithmic pattern where two index variables traverse an array — often from both ends toward the center, or at different speeds — to solve problems like removing duplicates, finding pairs that sum to a target, or reversing a string in O(n) time and O(1) space.

*   **Sliding window**: A pattern for computing results over every contiguous subarray of a fixed or variable size. Instead of recomputing from scratch each time, the window "slides" by adding the new element and removing the element that just left, reducing O(n·k) solutions to O(n).

*   **Prefix sum array**: A preprocessing technique where `prefix[i]` stores the sum of all elements from index 0 through i–1. Range sum queries that would cost O(n) each then become O(1) lookups: `sum(l, r) = prefix[r+1] - prefix[l]`.

*   **Amortized O(1) append**: The average cost of appending to a dynamic array over many operations. When the backing array is full, it doubles in size at cost O(n); but because doubling happens exponentially less often, the average cost per append across n operations is O(1).

---

### 2. Certification Exam Tips
*   **Two-pointer is the answer to many O(n) array problems:** Whenever you see "find a pair," "remove in-place," or "reverse," ask yourself whether two pointers can do it in one pass. Practice sorted-array two-sum, container with most water, and trapping rain water.
*   **Sliding window template:** Fixed-window problems (max sum of k elements) use a simple add/remove pattern. Variable-window problems (longest substring without repeating characters) use a `while window_invalid: shrink_left` pattern. Memorize both templates.
*   **Off-by-one errors kill interviews:** Array boundary bugs are the #1 source of wrong answers on easy problems. Always check: what happens when the array is empty? When there is one element? When i equals n–1?
*   **Prefix sums unlock subarray problems:** If an interview problem involves ranges or cumulative counts (subarray sum equals k, pivot index), reach for prefix sums immediately.
*   **Know the complexity table for arrays:** Access O(1), Search O(n), Insert at end O(1) amortized, Insert at middle O(n), Delete at middle O(n).
*   **Study Resource:** Work through the [LeetCode Array Explore Card](https://leetcode.com/explore/learn/card/fun-with-arrays/) — a free, structured set of problems and explanations specifically designed to build array fluency for interviews.

---

### Required Readings & Videos
*   **Required Reading:** [Arrays – Open Data Structures (Pat Morin), Chapter 2](https://opendatastructures.org/ods-python/2_Array_Based_Lists.html) — covers static and dynamic array implementation with Python code and complexity proofs.
*   **Required Video:** [Arrays for Coding Interviews – NeetCode on YouTube](https://www.youtube.com/watch?v=QJNwK2uJyGs) — a 30-minute walkthrough of array data structure internals and the two-pointer/sliding window patterns with LeetCode examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a dynamic array class in Python** supporting `append`, `get`, `set`, and `insert` with correct O(n) resizing logic.
*   **Solve LeetCode #26 (Remove Duplicates from Sorted Array)** using the two-pointer technique in O(n) time, O(1) space.
*   **Solve LeetCode #643 (Maximum Average Subarray I)** using the sliding window pattern.
*   **Measure resizing events** by printing a message each time your dynamic array doubles, then verify the amortized O(1) append claim by running 10,000 appends and plotting resize frequency.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 2 of Open Data Structures.
- [ ] Watch the NeetCode Arrays video.
- [ ] Implement the dynamic array class from scratch (no using Python list internally).
- [ ] Solve LeetCode #26 and #643.
- [ ] Proceed to the Module 02 Quiz.
