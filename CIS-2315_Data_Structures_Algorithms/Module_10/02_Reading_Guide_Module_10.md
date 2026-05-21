# Reading Guide: Module 10 – Sorting Algorithms: Bubble, Merge, Quick
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 10 – Sorting Algorithms: Bubble, Merge, Quick**! Sorting is a foundational topic that interviewers use to probe your understanding of recursion, divide-and-conquer, and algorithm analysis. While production code uses library sort functions, interviews expect you to implement merge sort and quick sort from scratch, explain their complexity, and know when each is preferable. Understanding sorting also enables you to recognize when pre-sorting input simplifies a problem from O(n²) to O(n log n) or O(n).

This module covers bubble sort as a baseline, merge sort as the canonical stable O(n log n) algorithm, and quick sort as the practical in-place O(n log n) average-case algorithm.

---

### 1. High-Yield Glossary

*   **Bubble sort**: A simple comparison-based sort that repeatedly steps through the array, swapping adjacent elements that are out of order. O(n²) time in average and worst case; O(n) best case on an already-sorted array with early termination. Used as a teaching baseline, not in production.

*   **Merge sort**: A divide-and-conquer sort that recursively splits the array in half, sorts each half, and merges the sorted halves. Always O(n log n) time in all cases. Requires O(n) auxiliary space for the merge step. The canonical stable, predictable sort.

*   **Quick sort**: A divide-and-conquer sort that partitions the array around a pivot element such that all elements less than the pivot are to its left and all greater are to its right, then recursively sorts both sides. O(n log n) average, O(n²) worst case (bad pivot choice). O(log n) average space for the recursive call stack; in-place.

*   **Stable sort**: A sort that preserves the relative order of elements with equal keys. Merge sort is stable; standard quick sort implementations are not. Stability matters when sorting by multiple keys.

*   **Pivot selection**: The strategy for choosing quick sort's partition element. Common choices: last element (simple, O(n²) on sorted input), random element (reduces worst-case probability), median-of-three (first/mid/last element median — used in practice).

*   **In-place sort**: A sort that requires only O(1) auxiliary space beyond the input array itself. Quick sort (with the Lomuto or Hoare partition scheme) is in-place. Merge sort is not — it requires O(n) extra space for merging.

*   **Comparison-based sort lower bound**: A theoretical result proving that any comparison-based sorting algorithm must make at least Ω(n log n) comparisons in the worst case. This makes merge sort and quick sort (average case) asymptotically optimal.

---

### 2. Certification Exam Tips
*   **Know all three sorts' complexities cold:** Bubble O(n²) / O(n²) / O(n) [worst/avg/best]; Merge O(n log n) / O(n log n) / O(n log n); Quick O(n²) / O(n log n) / O(n log n). Interviewers ask this directly.
*   **Implement merge sort recursively:** The merge step is the key. Two pointers walk the two sorted halves; the smaller element goes into the output array first. Practice until you can write it without errors under pressure.
*   **Quick sort pivot on sorted/reverse-sorted input degrades to O(n²):** This is the standard interview trap. Mention random pivot or median-of-three to show you know the fix.
*   **Merge sort is preferred when stability matters:** Sorting objects by one field then another (stable sort preserves the earlier sort order). Python's `sorted()` and `.sort()` use Timsort, which is stable.
*   **"Sort the input first" is a common optimization:** Many array problems that would be O(n²) with brute force become O(n log n) or O(n) if you sort first (e.g., 3Sum, Two Sum II on sorted input).
*   **Study Resource:** [Sorting Algorithms Visualized – sorting.at](https://sorting.at) — an animated comparison of all major sorting algorithms running simultaneously on the same input, making runtime differences viscerally clear.

---

### Required Readings & Videos
*   **Required Reading:** [Sorting Algorithms – Open Data Structures (Pat Morin), Chapter 11](https://opendatastructures.org/ods-python/11_Sorting_Algorithms.html) — covers merge sort, quick sort, and heap sort with full Python implementations and complexity analysis.
*   **Required Video:** [Sorting Algorithms – NeetCode on YouTube](https://www.youtube.com/watch?v=cbIG8oMHBSM) — a 30-minute interview-focused video implementing merge sort and quick sort, explaining partition logic and pivot selection with LeetCode-style examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement merge sort from scratch** and verify it produces sorted output for edge cases (empty array, single element, already sorted, reverse sorted).
*   **Implement quick sort from scratch** with the Lomuto partition scheme, then modify it to use a random pivot and compare performance on sorted input.
*   **Solve LeetCode #912 (Sort an Array)** by implementing merge sort — do not use Python's built-in sort.
*   **Time both implementations** on arrays of size 100, 1000, and 10000 and compare to Python's built-in `sorted()`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 11 of Open Data Structures.
- [ ] Watch the NeetCode Sorting Algorithms video.
- [ ] Implement merge sort and quick sort from scratch.
- [ ] Solve LeetCode #912.
- [ ] Proceed to the Module 10 Quiz.
