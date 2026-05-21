# Quiz: Module 11 – Searching: Binary Search and Variants
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the time complexity of binary search on a sorted array of n elements?
*   A) O(n)
*   B) O(n²)
*   C) O(log n)
*   D) O(n log n)
*   **Correct Answer:** C) O(log n)
*   **Distractor Analysis:**
    *   *Why correct:* Each comparison halves the search space. Starting with n elements, after k steps there are n/2^k candidates. When n/2^k = 1, k = log₂(n) steps have been taken.
    *   A is incorrect: O(n) describes linear search — examining each element one by one without halving.
    *   B is incorrect: O(n²) is never a characteristic of binary search; it would imply nested iteration.
    *   D is incorrect: O(n log n) describes efficient sorting, not a single search operation.

---

**Question 2**
Which of the following is the most accurate definition of **binary search on the answer** as a problem-solving technique?
*   A) A technique that uses binary search to locate a target value in a sorted 2D matrix by treating the matrix as a flattened 1D sorted array with index arithmetic.
*   B) A technique that binary searches over the range of possible answer values (rather than array indices), using a feasibility check function to determine whether a candidate answer is too small or too large, applicable when feasibility is monotone.
*   C) A technique that applies binary search to a BST, comparing the target to the current node and going left or right based on the BST property until the value is found or a null is reached.
*   D) A technique that combines binary search with memoization to reduce the number of redundant feasibility checks when the answer space has overlapping subproblems.
*   **Correct Answer:** B) A technique that binary searches over the range of possible answer values (rather than array indices), using a feasibility check function to determine whether a candidate answer is too small or too large, applicable when feasibility is monotone.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes binary search on a sorted matrix (LeetCode #74), which is still binary search on an index, not on the answer value.
    *   *Why B is correct:* "Binary search on answer" applies when the problem asks for a minimum or maximum value satisfying some condition, and larger/smaller values always satisfy/fail that condition monotonically. LeetCode #875 (Koko Eating Bananas) is the canonical example.
    *   *Why C is incorrect:* That describes standard BST search, which binary searches the tree structure by value, not the range of possible answers.
    *   *Why D is incorrect:* Binary search on answer does not use memoization; the feasibility check function is typically re-evaluated fresh at each midpoint.

---

**Question 3**
In the binary search template `lo, hi = 0, len(arr)-1; while lo <= hi: mid = lo + (hi-lo)//2`, why is `mid` calculated as `lo + (hi-lo)//2` rather than `(lo + hi) // 2`?
*   A) The formula `lo + (hi-lo)//2` is faster because it avoids a subtraction.
*   B) The formula `(lo + hi) // 2` can cause integer overflow when `lo` and `hi` are large integers, whereas `lo + (hi-lo)//2` cannot overflow because the difference is always within bounds.
*   C) The formula `lo + (hi-lo)//2` always rounds up to avoid missing the target when the array length is odd.
*   D) Python requires this form because its `//` operator behaves differently for sums versus differences of large integers.
*   **Correct Answer:** B) The formula `(lo + hi) // 2` can cause integer overflow when `lo` and `hi` are large integers, whereas `lo + (hi-lo)//2` cannot overflow because the difference is always within bounds.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Both forms require the same number of arithmetic operations; the difference is overflow safety, not speed.
    *   *Why B is correct:* In languages with fixed-size integers (Java, C++, C), `lo + hi` can overflow a 32-bit int when both are near INT_MAX. `hi - lo` is at most the array length, which is safe. Python has arbitrary-precision integers so overflow does not apply, but the form is best practice from Java/C++ interview environments.
    *   *Why C is incorrect:* Both forms produce the same floor-division result; neither consistently rounds up.
    *   *Why D is incorrect:* Python's `//` is floor division and behaves identically for both forms given the same mathematical input.

---

**Question 4**
You are given a sorted array that has been rotated at an unknown pivot: `[5, 6, 7, 0, 1, 2, 4]`. You want to find target = 0. After computing `mid = 3` (value 0), binary search has already found the answer. But suppose `mid` pointed to value `6`. Which portion of the array is definitively sorted and how would you decide which half to search?
*   A) The right half `[7, 0, 1, 2, 4]` is sorted because it contains the end of the array; search it for the target.
*   B) The left half `[5, 6]` is sorted (arr[lo] <= arr[mid]); if target is in [arr[lo], arr[mid]), search left; otherwise search right.
*   C) Neither half can be determined as sorted without first finding the pivot index by linearly scanning.
*   D) Always search the left half first regardless of which side is sorted; fall back to the right half if not found.
*   **Correct Answer:** B) The left half `[5, 6]` is sorted (arr[lo] <= arr[mid]); if target is in [arr[lo], arr[mid]), search left; otherwise search right.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `[7, 0, 1, 2, 4]` is not sorted — it contains the rotation point (7 > 0). Treating it as sorted would lead to incorrect binary search behavior.
    *   *Why B is correct:* Checking `arr[lo] <= arr[mid]` identifies which half is sorted. Here arr[lo]=5 <= arr[mid]=6, so the left half [5,6] is sorted. Since 0 is not in [5,6], search the right half.
    *   *Why C is incorrect:* Finding the pivot requires O(n) scan, defeating the purpose of O(log n) binary search. The comparison `arr[lo] <= arr[mid]` identifies the sorted half in O(1).
    *   *Why D is incorrect:* Blindly choosing a side regardless of target range can permanently eliminate the half containing the target.

---

**Question 5**
Using Python's `bisect` module, `bisect_left(arr, x)` returns the leftmost index where `x` can be inserted to keep `arr` sorted. If `arr = [1, 3, 3, 5, 7]` and `x = 3`, what does `bisect_left(arr, 3)` return?
*   A) 0 — it always returns the beginning of the array for safety.
*   B) 1 — the first index where arr[i] >= 3.
*   C) 3 — the first index where arr[i] > 3.
*   D) 5 — the position after all elements equal to 3.
*   **Correct Answer:** B) 1 — the first index where arr[i] >= 3.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `bisect_left` does not default to index 0; it finds the actual leftmost insertion point for the given value.
    *   *Why B is correct:* `bisect_left` finds the first index where `arr[i] >= x`. In `[1, 3, 3, 5, 7]`, the first element >= 3 is at index 1 (value 3). Inserting 3 at index 1 would give `[1, 3, 3, 3, 5, 7]`.
    *   *Why C is incorrect:* Index 3 (value 5) is where `arr[i] > 3` — that is `bisect_right(arr, 3)`, not `bisect_left`.
    *   *Why D is incorrect:* Index 5 is after all 3s — the result of `bisect_right`, not `bisect_left`.
