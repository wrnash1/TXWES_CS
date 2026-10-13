# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 12 — Divide & Conquer

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Draw the recursion tree for merge sort on a 8-element array. Students must see the split levels and the merge levels separately.
> - Binary search: draw the search space halving at each step. Emphasize the `mid = left + (right - left) // 2` formula to avoid integer overflow (relevant in Java/C++ interviews, good habit in Python too).
> - The Master Theorem is for analysis, not implementation. Introduce it with the T(n) = aT(n/b) + f(n) pattern; do not over-formalize.
> - Common interview patterns: binary search on answer (not just on sorted arrays), merge sort for inversion count.
> - Common mistakes: off-by-one errors in binary search (`left < right` vs `left <= right`), not returning `mid` when found, using `left + right // 2` without parentheses.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 12 | Divide & Conquer | CIS-2315"]**

"Divide and conquer is an algorithmic strategy: split the problem into smaller subproblems, solve each subproblem recursively, and combine the results. It powers merge sort, quicksort, binary search, and the fast Fourier transform. The key difference from plain recursion is that the subproblems are independent — they do not share state, so results can be combined cleanly. This module covers merge sort, binary search, and the Master Theorem for analyzing divide-and-conquer recurrences."

---

## [01:30 – 09:00] Part 1 — Merge Sort

**[SHOW SLIDE: "Merge Sort — Split, Recurse, Merge"]**

"Merge sort is the canonical divide-and-conquer sorting algorithm. It splits the array in half, recursively sorts each half, and merges the two sorted halves into one sorted array.

**[SHOW DIAGRAM: recursion tree for `[5, 3, 8, 1, 9, 2, 7, 4]`]**

```text
Split phase:
[5,3,8,1,9,2,7,4]
  [5,3,8,1]   [9,2,7,4]
  [5,3][8,1]  [9,2][7,4]
  [5][3][8][1][9][2][7][4]

Merge phase:
  [3,5][1,8]  [2,9][4,7]
  [1,3,5,8]   [2,4,7,9]
  [1,2,3,4,5,7,8,9]
```

[PAUSE]

```python
def merge_sort(arr):
    """
    Sort arr in O(n log n) time using divide and conquer.
    Returns a new sorted list; does not modify arr in place.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # recursively sort left half
    right = merge_sort(arr[mid:])    # recursively sort right half
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    Time: O(n) where n = len(left) + len(right)
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**[DEMO: `merge_sort([5,3,8,1,9,2,7,4])` — show output `[1,2,3,4,5,7,8,9]`]**

[PAUSE]

**Why O(n log n)?**

The recursion tree has `log n` levels (each level halves the problem). At each level, the total work across all merge calls is O(n) — every element is examined once per level. Total: O(n) × O(log n) = O(n log n).

**Why merge sort over quicksort?**

Merge sort is stable (equal elements maintain relative order) and guarantees O(n log n) worst case. Quicksort averages O(n log n) but degrades to O(n²) on sorted input with a naive pivot. When stability or worst-case guarantees matter, use merge sort."

---

## [09:00 – 16:00] Part 2 — Binary Search

**[SHOW SLIDE: "Binary Search — Halving the Search Space"]**

"Binary search finds a target in a sorted array in O(log n) time by repeatedly halving the search space.

```python
def binary_search(arr, target):
    """
    Return the index of target in sorted arr, or -1 if not found.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2    # avoids integer overflow in C++/Java

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1    # target is in right half
        else:
            right = mid - 1   # target is in left half

    return -1
```

**[DEMO: `binary_search([1,3,5,7,9,11,13,15], 7)` — trace: left=0,right=7,mid=3,arr[3]=7 → return 3]**

[PAUSE]

**Three binary search variants:**

**Find leftmost (first occurrence):**

```python
def search_leftmost(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if left < len(arr) and arr[left] == target else -1
```

**Search on answer (binary search on value range):**

The classic advanced pattern: when the answer lies in a range and you can write a function `feasible(x)` that is monotone (False for small x, True for large x), binary search finds the boundary.

```python
# Example: Find minimum capacity to ship packages within D days (LeetCode #1011)
def ship_within_days(weights, days):
    def feasible(capacity):
        day_count, load = 1, 0
        for w in weights:
            if load + w > capacity:
                day_count += 1
                load = 0
            load += w
        return day_count <= days

    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid    # mid works — try smaller
        else:
            left = mid + 1  # mid too small — increase
    return left
```

**[DEMO: `ship_within_days([1,2,3,4,5,6,7,8,9,10], 5)` — expected 15]**"

---

## [16:00 – 20:00] Part 3 — Master Theorem

**[SHOW SLIDE: "Master Theorem — Analyzing Divide and Conquer"]**

"The **Master Theorem** gives the asymptotic complexity of recurrences of the form:

```text
T(n) = a · T(n/b) + f(n)
```

Where:

- `a` = number of subproblems
- `b` = factor by which n is reduced
- `f(n)` = cost of work outside the recursive calls (split + combine)

Three cases:

**Case 1:** `f(n) = O(n^(log_b(a) - ε))` for some ε > 0 → T(n) = Θ(n^log_b(a))
**Case 2:** `f(n) = Θ(n^log_b(a))` → T(n) = Θ(n^log_b(a) · log n)
**Case 3:** `f(n) = Ω(n^(log_b(a) + ε))` → T(n) = Θ(f(n))

[PAUSE]

**Examples:**

Merge sort: T(n) = 2T(n/2) + O(n)
a=2, b=2, log_b(a) = log_2(2) = 1. f(n) = O(n) = O(n^1). Case 2: T(n) = Θ(n log n). ✓

Binary search: T(n) = T(n/2) + O(1)
a=1, b=2, log_b(a) = log_2(1) = 0. f(n) = O(1) = O(n^0). Case 2: T(n) = Θ(log n). ✓

The Master Theorem tells you complexity without needing to draw the full recursion tree. Memorize the three cases and the two canonical examples (merge sort and binary search) — interviewers ask about both."

---

## [20:00 – 24:00] Part 4 — Count Inversions

**[SHOW SLIDE: "Merge Sort Application: Counting Inversions"]**

"An **inversion** is a pair (i, j) where i < j but arr[i] > arr[j] — an out-of-order pair. Counting inversions with a nested loop is O(n²). Modified merge sort counts them in O(n log n).

The insight: when merging two sorted halves, whenever we take an element from the right half before exhausting the left half, the number of remaining elements in the left half equals the number of inversions contributed by that right-half element.

```python
def count_inversions(arr):
    """Returns (sorted_arr, inversion_count) in O(n log n)."""
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])

    merged = []
    inversions = left_inv + right_inv
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i    # all remaining left elements form inversions
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions
```

**[DEMO: `count_inversions([3,1,2])` — inversions are (3,1) and (3,2) → should return 2]**

The Module 12 lab covers merge sort implementation and inversion counting, binary search and its variants, and the binary search on answer pattern with ship_within_days. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 12 — Divide & Conquer]**

---

## Additional Resources

- [VisuAlgo — Merge Sort Visualization](https://visualgo.net/en/sorting)
- [NeetCode — Binary Search](https://www.youtube.com/watch?v=s4DPM8ct1pI)
- [LeetCode #33 — Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [LeetCode #1011 — Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- [LeetCode #912 — Sort an Array (merge sort practice)](https://leetcode.com/problems/sort-an-array/)
