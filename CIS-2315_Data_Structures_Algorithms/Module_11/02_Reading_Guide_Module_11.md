# Reading Guide: Module 11 – Searching: Binary Search and Variants
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 11 – Searching: Binary Search and Variants**! Binary search is one of the most deceptively difficult topics in technical interviews. The core idea is simple — halve the search space each step — but the off-by-one bugs in boundary conditions trip up even experienced engineers. More importantly, binary search applies far beyond sorted arrays: it solves problems on rotated arrays, 2D matrices, and even abstract "search spaces" where you binary search on the answer value rather than an array index.

This module covers the standard binary search template, left/right boundary variants, and the generalized "binary search on answer" pattern.

---

### 1. High-Yield Glossary

*   **Binary search**: An algorithm for finding a target in a sorted collection by repeatedly comparing the target to the middle element and eliminating half the remaining search space. Time complexity O(log n); requires a sorted (or monotonically ordered) input.

*   **Search space**: The set of candidate values or indices that binary search considers at any point. Each iteration divides the search space in half by updating `lo` or `hi` based on the comparison result.

*   **Left boundary (lower bound) search**: A variant of binary search that finds the leftmost position where a target could be inserted while maintaining sorted order (the first index where `arr[i] >= target`). Used in `bisect_left` in Python.

*   **Right boundary (upper bound) search**: A variant that finds the rightmost valid position — the first index where `arr[i] > target`. Used in `bisect_right`. Together with left boundary, enables counting occurrences of a target in O(log n).

*   **Binary search on answer**: A technique where instead of searching an array for a value, you binary search over the range of possible answer values and use a feasibility check function `f(mid)` to determine which half contains the optimal answer. Applied when the answer space is monotonically ordered.

*   **Rotated sorted array**: A sorted array that has been rotated at some pivot index (e.g., `[4,5,6,7,0,1,2]`). Binary search still applies by checking which half is sorted and whether the target falls within it.

*   **Off-by-one error in binary search**: The most common bug in binary search implementations, caused by incorrect update rules for `lo` and `hi` (e.g., using `mid` vs. `mid+1` or `mid-1`). The standard template uses `lo = mid + 1` and `hi = mid – 1` for a classic search, but boundary variants require careful adjustment.

---

### 2. Certification Exam Tips
*   **Memorize one binary search template and stick to it:** Use `lo, hi = 0, len(arr)-1`; `while lo <= hi:`; `mid = lo + (hi-lo)//2`; update `lo = mid+1` or `hi = mid-1`. The `lo + (hi-lo)//2` form avoids integer overflow (relevant in Java/C++).
*   **Left/right boundary variants are their own templates:** For "first true" (leftmost), keep going right even when found: `hi = mid - 1` on match. For "last true" (rightmost), keep going left: `lo = mid + 1` on match. Practice both.
*   **"Binary search on answer" recognizes monotone feasibility:** If the problem asks "find the minimum X such that condition Y is satisfied" and Y has a monotone structure (once true, stays true as X increases), binary search on X with a check function.
*   **Rotated array — identify which half is sorted:** `if arr[lo] <= arr[mid]` means the left half is sorted; otherwise the right half is sorted. Then determine which side contains the target.
*   **LeetCode #704, #35, #33, #153, #875 are the core problems:** Solve them in this order. #704 is basic; #35 is lower bound; #33 is rotated; #153 is minimum in rotated; #875 is binary search on answer.
*   **Study Resource:** [Binary Search – LeetCode Explore Card](https://leetcode.com/explore/learn/card/binary-search/) — a structured progression of binary search problems with template explanations, covering all variants discussed in this module.

---

### Required Readings & Videos
*   **Required Reading:** [Binary Search – Open Data Structures (Pat Morin), Chapter 1.4 and Chapter 4](https://opendatastructures.org/ods-python/1_4_The_Queue_Stack_Deque.html) — covers the binary search algorithm in the context of sorted arrays and the SortedArray structure.
*   **Required Video:** [Binary Search – NeetCode on YouTube](https://www.youtube.com/watch?v=s4DPM8ct1pI) — a 25-minute interview-focused video covering the standard template, left/right boundary searches, and rotated array binary search with worked examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement binary search three ways:** standard (find exact), lower bound (first occurrence), and upper bound (last occurrence), and verify on arrays with duplicates.
*   **Solve LeetCode #704 (Binary Search)** — canonical implementation verification.
*   **Solve LeetCode #33 (Search in Rotated Sorted Array)** — binary search with rotated-half identification.
*   **Solve LeetCode #875 (Koko Eating Bananas)** — binary search on the answer value, not an array index.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 1.4 and Chapter 4 of Open Data Structures.
- [ ] Watch the NeetCode Binary Search video.
- [ ] Implement all three binary search variants from scratch.
- [ ] Solve LeetCode #704, #33, and #875.
- [ ] Proceed to the Module 11 Quiz.
