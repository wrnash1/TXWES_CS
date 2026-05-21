# Quiz: Module 10 – Sorting Algorithms: Bubble, Merge, Quick
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the worst-case time complexity of quick sort when the pivot is always chosen as the first or last element and the input is already sorted?
*   A) O(n log n)
*   B) O(n)
*   C) O(n²)
*   D) O(log n)
*   **Correct Answer:** C) O(n²)
*   **Distractor Analysis:**
    *   *Why correct:* On sorted input with a first/last element pivot, every partition step splits into one subarray of size 0 and one of size n–1. This produces n recursive calls each doing O(n) work — O(n²) total.
    *   A is incorrect: O(n log n) is quick sort's average-case performance with good pivots, not its worst case on sorted input.
    *   B is incorrect: O(n) would require a linear-time algorithm; partitioning alone costs O(n) per level.
    *   D is incorrect: O(log n) describes the recursive depth with balanced partitions, not the total cost of an unbalanced sort.

---

**Question 2**
Which of the following is the most accurate definition of a **stable sort**?
*   A) A sorting algorithm that always produces the same output regardless of the pivot strategy used, making its behavior predictable across all inputs.
*   B) A sorting algorithm that preserves the original relative order of elements that compare as equal, so two records with the same key appear in their original input order in the sorted output.
*   C) A sorting algorithm that runs in O(n log n) time in both the best and worst case, ensuring stable performance guarantees across all input types.
*   D) A sorting algorithm that performs an equal number of comparisons and swaps, ensuring that no element is moved more times than necessary to reach its sorted position.
*   **Correct Answer:** B) A sorting algorithm that preserves the original relative order of elements that compare as equal, so two records with the same key appear in their original input order in the sorted output.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes determinism (same input → same output), which all correct sorting algorithms share. Stability is specifically about equal-key ordering.
    *   *Why B is correct:* Stability matters when sorting records by multiple fields — e.g., first by date, then by name. A stable sort preserves the date order among equal-name records.
    *   *Why C is incorrect:* That describes complexity consistency (like merge sort's O(n log n) guarantee), not stability. Quick sort is unstable but has O(n log n) average case.
    *   *Why D is incorrect:* That does not correspond to any standard property of sorting algorithms. The number of comparisons and swaps are separate metrics with no required equality.

---

**Question 3**
In the merge step of merge sort, two sorted subarrays must be combined. What is the time and space complexity of this merge step for arrays of total size n?
*   A) O(n) time, O(1) space — elements are merged in-place by shifting.
*   B) O(n log n) time, O(n) space — a second sort is required after combining.
*   C) O(n) time, O(n) space — two pointers walk each subarray and elements are copied into a temporary array.
*   D) O(n²) time, O(1) space — each element in the left array is compared to each element in the right array.
*   **Correct Answer:** C) O(n) time, O(n) space — two pointers walk each subarray and elements are copied into a temporary array.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* In-place merging of two sorted arrays is possible but requires O(n²) time in simple implementations; O(n) time in-place merge requires very complex algorithms not used in practice.
    *   *Why B is incorrect:* No second sort is needed; merging two already-sorted arrays is a linear scan. O(n log n) merge would defeat the purpose of merge sort's recursion.
    *   *Why C is correct:* The standard merge allocates a temporary array of size n, then uses two pointers to copy the smaller of the two current front elements, advancing one pointer per step. Total comparisons and copies are O(n).
    *   *Why D is incorrect:* A pairwise comparison of left against right would be O(n²). The key insight of merge sort is that the subarrays are already sorted, so each element is compared at most once.

---

**Question 4**
Which sorting algorithm is most appropriate when memory is severely constrained (only O(1) extra space is available) and average O(n log n) performance is acceptable?
*   A) Merge sort — O(n log n) guaranteed, easy to implement.
*   B) Bubble sort — O(1) space and always terminates.
*   C) Quick sort — O(log n) average stack space (in-place), O(n log n) average time.
*   D) Counting sort — O(1) auxiliary space when values fit in a small range.
*   **Correct Answer:** C) Quick sort — O(log n) average stack space (in-place), O(n log n) average time.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Merge sort requires O(n) auxiliary space for the temporary merge buffer — not suitable when memory is severely constrained.
    *   *Why B is incorrect:* Bubble sort uses O(1) space but is O(n²) in average and worst case — far too slow to be "acceptable" when O(n log n) is achievable.
    *   *Why C is correct:* Quick sort partitions in-place (O(1) extra space per level), using O(log n) stack space for the recursive calls. Average O(n log n) time makes it the standard choice for memory-constrained, performance-sensitive sorting.
    *   *Why D is incorrect:* Counting sort requires O(k) auxiliary space where k is the value range — this can be very large, and the question specifies O(1) space. Also, counting sort is a non-comparison sort limited to integer keys.

---

**Question 5**
Python's built-in `sorted()` function uses Timsort. What are the key properties of Timsort that make it practical?
*   A) Timsort is O(n) for all inputs by detecting sorted runs and skipping any comparison-based work entirely.
*   B) Timsort combines merge sort and insertion sort: it identifies natural sorted runs and uses insertion sort for small runs, then merges them — achieving O(n) best case on nearly sorted data and O(n log n) worst case, with stability.
*   C) Timsort is a parallel sort that distributes work across CPU cores, making it faster than merge sort on multi-core machines for large inputs.
*   D) Timsort uses hash-based bucketing to achieve O(1) average case by assigning each element to a pre-sorted bucket.
*   **Correct Answer:** B) Timsort combines merge sort and insertion sort: it identifies natural sorted runs and uses insertion sort for small runs, then merges them — achieving O(n) best case on nearly sorted data and O(n log n) worst case, with stability.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Timsort's best case is O(n) only when the input is a single sorted run. It still needs O(n) time to scan the array; it cannot skip to O(1).
    *   *Why B is correct:* Timsort's hybrid design exploits real-world data patterns (partially sorted arrays) and achieves O(n) for already-sorted inputs, O(n log n) worst case, and is stable — making it ideal as a general-purpose sort.
    *   *Why C is incorrect:* Timsort is single-threaded; it does not use parallelism. Its advantage comes from adaptive run detection, not CPU core distribution.
    *   *Why D is incorrect:* Timsort is comparison-based; it does not use hashing. Bucket/hash-based sorts are separate non-comparison algorithms.
