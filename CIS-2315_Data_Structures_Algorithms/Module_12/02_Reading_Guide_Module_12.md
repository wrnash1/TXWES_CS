# Reading Guide: Module 12 — Divide & Conquer

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Divide and conquer splits a problem into independent subproblems of the same type, solves each recursively, and combines the results. The independence of subproblems (unlike overlapping subproblems in dynamic programming) means the combination step is the primary source of algorithmic insight. Merge sort, binary search, and the fast Fourier transform all use this pattern. The Master Theorem provides a systematic way to analyze divide-and-conquer recurrences without drawing full recursion trees.

---

## 1. The Pattern

Every divide-and-conquer algorithm has three steps:

1. **Divide:** split the problem into smaller subproblems.
2. **Conquer:** recursively solve each subproblem (base case: subproblem small enough to solve directly).
3. **Combine:** merge the results of the subproblems into the answer for the original problem.

The recurrence T(n) = a·T(n/b) + f(n) captures this structure: `a` subproblems of size `n/b`, combined at cost `f(n)`.

---

## 2. Merge Sort

### Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
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

### Properties

- **Time:** O(n log n) — log n levels, O(n) merge work per level.
- **Space:** O(n) — the merged arrays require linear extra space.
- **Stable:** equal elements maintain their relative order.
- **Recurrence:** T(n) = 2T(n/2) + O(n) → O(n log n) by Master Theorem Case 2.

### Merge Sort vs. Quicksort

| Property | Merge Sort | Quicksort |
|---|---|---|
| Worst case | O(n log n) | O(n²) |
| Average case | O(n log n) | O(n log n) |
| Space | O(n) | O(log n) avg |
| Stable | Yes | No (standard) |
| Cache behavior | Poor (splits to new arrays) | Good (in-place) |

Choose merge sort when stability or worst-case guarantees matter.

---

## 3. Binary Search

### Standard Implementation

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Invariant:** `target`, if present, is always within `[left, right]`.

### Off-by-One Guide

| Condition | Use case |
|---|---|
| `while left <= right` | Standard search — return index when found |
| `while left < right` | Finding boundary — left and right converge to the answer |

### Leftmost Occurrence

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

### Binary Search on Answer

When the answer lies in a numeric range and a monotone `feasible(x)` function determines if x is sufficient, binary search the range:

```python
# Template
left, right = lower_bound, upper_bound
while left < right:
    mid = left + (right - left) // 2
    if feasible(mid):
        right = mid       # mid works, try smaller
    else:
        left = mid + 1    # mid too small, increase
return left
```

**Time:** O(log(range) × cost of feasible).

---

## 4. Master Theorem

For T(n) = a·T(n/b) + f(n) where a ≥ 1, b > 1:

Let `c = log_b(a)` (the critical exponent).

- **Case 1:** `f(n) = O(n^(c-ε))` → T(n) = Θ(n^c) — recursion dominates
- **Case 2:** `f(n) = Θ(n^c)` → T(n) = Θ(n^c · log n) — equal work per level
- **Case 3:** `f(n) = Ω(n^(c+ε))` → T(n) = Θ(f(n)) — combine step dominates

### Common Applications

| Algorithm | Recurrence | Case | Result |
|---|---|---|---|
| Merge sort | T(n)=2T(n/2)+O(n) | 2 | O(n log n) |
| Binary search | T(n)=T(n/2)+O(1) | 2 | O(log n) |
| Naive integer multiply | T(n)=4T(n/2)+O(n) | 1 | O(n²) |
| Karatsuba multiply | T(n)=3T(n/2)+O(n) | 1 | O(n^1.585) |

---

## 5. Counting Inversions

An inversion in array `arr` is a pair (i, j) where i < j but `arr[i] > arr[j]`. Brute force: O(n²). Modified merge sort: O(n log n).

```python
def count_inversions(arr):
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
            inversions += len(left) - i    # all remaining left elements > right[j]
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions
```

---

## 6. Interview Exam Tips

1. **`mid = left + (right - left) // 2`** — not `(left + right) // 2`. In Python, integers don't overflow, but this is good practice for C++/Java interviews and shows you know the classic bug.

2. **Always state the loop invariant** — for binary search: "target, if present, is always in `[left, right]`." This instantly communicates correctness to an interviewer.

3. **Binary search on answer vs. binary search on array** — recognize when the problem asks you to find a minimum/maximum value satisfying a condition. If the feasible function is monotone, binary search applies.

4. **Merge sort is O(n) space** — the merge step requires creating new arrays. In-place merge exists but is complex. State the space cost in interviews.

5. **Stable sort matters** — when sorting objects by one key that may have equal values, a stable sort preserves the relative order from a previous sort. Merge sort is stable; Python's built-in `sort` is also stable (Timsort).

6. **Master Theorem Case 2 applies to both merge sort and binary search** — memorize: T(n)=2T(n/2)+O(n) → O(n log n), and T(n)=T(n/2)+O(1) → O(log n).

7. **Counting inversions extends merge sort** — recognizing that merge sort's merge step naturally reveals inversion count is a frequently asked "insight" question. The answer: every time a right-half element is placed before a remaining left-half element, those pairs are inversions.

8. **Off-by-one in binary search** — the most common binary search bug. When in doubt: for a "find if exists" search, use `left <= right`. For a "find the boundary" search, use `left < right` and the answer is `left` after the loop.

---

## 7. Study Checklist

- [ ] Watch the Module 12 video lecture by Professor Nash.
- [ ] Implement `merge_sort` and `merge` from scratch and test on several inputs.
- [ ] Implement binary search with `while left <= right`.
- [ ] Implement `search_leftmost` for the leftmost occurrence.
- [ ] Trace the binary search on answer template for ship_within_days.
- [ ] Implement `count_inversions` and verify on `[3,1,2]` (2 inversions).
- [ ] Apply the Master Theorem to merge sort and binary search recurrences.
- [ ] Solve LeetCode #33 (Search in Rotated Sorted Array).
- [ ] Complete the Module 12 Lab.
- [ ] Complete the Module 12 Quiz.
