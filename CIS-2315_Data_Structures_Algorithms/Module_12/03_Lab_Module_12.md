# Lab Activity: Module 12 — Divide & Conquer

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement merge sort and inversion counting
- **Part 2** — Implement binary search and its variants
- **Part 3** — Binary search on answer: ship_within_days and Search in Rotated Sorted Array

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Merge Sort

**File:** `lab12_divide_conquer.py`

### 1.1 — Merge Sort Implementation

```python
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

def merge_sort(arr):
    """
    Sort arr using divide and conquer.
    Returns a new sorted list.
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

Test:

```python
print(merge_sort([5, 3, 8, 1, 9, 2, 7, 4]))   # [1, 2, 3, 4, 5, 7, 8, 9]
print(merge_sort([]))                           # []
print(merge_sort([42]))                         # [42]
print(merge_sort([3, 1]))                       # [1, 3]
print(merge_sort([1, 2, 3, 4, 5]))             # [1, 2, 3, 4, 5] — already sorted
print(merge_sort([5, 4, 3, 2, 1]))             # [1, 2, 3, 4, 5] — reverse sorted
```

**Checkpoint:** All outputs correct. Verify merge sort handles empty, single-element, already-sorted, and reverse-sorted arrays.

---

### 1.2 — Stability Test

```python
# Merge sort is stable: equal elements retain relative original order.
data = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]
sorted_data = merge_sort(data)
print(sorted_data)
# [(1, 'b'), (1, 'e'), (2, 'd'), (3, 'a'), (3, 'c')]
# Note: (1,'b') before (1,'e') — original relative order preserved
# Note: (3,'a') before (3,'c') — original relative order preserved
```

**Checkpoint:** Equal tuples appear in their original relative order — confirming merge sort is stable.

---

### 1.3 — Counting Inversions

```python
def count_inversions(arr):
    """
    Count inversions (pairs i<j where arr[i]>arr[j]) using modified merge sort.
    Returns (sorted_arr, inversion_count).
    Time: O(n log n)
    """
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
            # All remaining elements in left (from index i onward) are greater than right[j]
            inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions
```

Test:

```python
_, inv = count_inversions([3, 1, 2])
print(inv)    # 2 — inversions: (3,1) and (3,2)

_, inv2 = count_inversions([1, 2, 3, 4, 5])
print(inv2)   # 0 — already sorted, no inversions

_, inv3 = count_inversions([5, 4, 3, 2, 1])
print(inv3)   # 10 — maximum inversions for n=5: n*(n-1)/2 = 10

_, inv4 = count_inversions([2, 4, 1, 3, 5])
print(inv4)   # 3 — inversions: (2,1), (4,1), (4,3)
```

**Checkpoint:** All inversion counts correct. For reversed array of length n, count = n*(n-1)/2.

---

## Part 2 — Binary Search

### 2.1 — Standard Binary Search

```python
def binary_search(arr, target):
    """
    Return index of target in sorted arr, or -1 if not found.
    Loop invariant: target is in arr[left..right] if present.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2    # avoids overflow in C++/Java

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Test:

```python
arr = [1, 3, 5, 7, 9, 11, 13, 15]

print(binary_search(arr, 7))    # 3 — index 3
print(binary_search(arr, 1))    # 0 — first element
print(binary_search(arr, 15))   # 7 — last element
print(binary_search(arr, 6))    # -1 — not present
print(binary_search([], 5))     # -1 — empty array
```

**Checkpoint:** All outputs correct. Binary search returns the index, not the value.

---

### 2.2 — Leftmost Occurrence

```python
def search_leftmost(arr, target):
    """
    Return index of the FIRST occurrence of target in sorted arr.
    Returns -1 if target is not present.
    Uses 'left < right' convergence for boundary finding.
    """
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if left < len(arr) and arr[left] == target else -1
```

Test:

```python
arr2 = [1, 2, 2, 2, 3, 4, 5]
print(search_leftmost(arr2, 2))    # 1 — first occurrence of 2
print(search_leftmost(arr2, 3))    # 4 — index of 3
print(search_leftmost(arr2, 6))    # -1 — not present

arr3 = [5, 5, 5, 5, 5]
print(search_leftmost(arr3, 5))    # 0 — all equal, first index
```

**Checkpoint:** Returns the first occurrence index for duplicates.

---

## Part 3 — Binary Search on Answer

### 3.1 — Ship Packages Within D Days (LeetCode #1011)

```python
def ship_within_days(weights, days):
    """
    Find the minimum ship capacity to deliver all packages in 'days' days.
    Packages must be shipped in order; each day's load cannot exceed capacity.

    Binary search on the answer: capacity in [max(weights), sum(weights)].
    feasible(cap): can we ship all packages in 'days' days with capacity cap?
    Time: O(n log(sum(weights) - max(weights)))
    """
    def feasible(capacity):
        day_count, load = 1, 0
        for w in weights:
            if load + w > capacity:
                day_count += 1
                load = 0
            load += w
        return day_count <= days

    left = max(weights)     # minimum possible: must fit the heaviest package
    right = sum(weights)    # maximum needed: ship everything in one day

    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid     # mid works — try smaller
        else:
            left = mid + 1  # mid too small — increase

    return left
```

Test:

```python
print(ship_within_days([1,2,3,4,5,6,7,8,9,10], 5))    # 15
print(ship_within_days([3,2,2,4,1,4], 3))               # 6
print(ship_within_days([1,2,3,1,1], 4))                 # 3
```

Trace `ship_within_days([1,2,3,4,5,6,7,8,9,10], 5)`:

```text
left=10 (max), right=55 (sum)

mid=32: feasible(32)=True (2 days) → right=32
mid=21: feasible(21)=True (3 days) → right=21
mid=15: feasible(15)=True (5 days) → right=15
mid=12: feasible(12)=False (6 days) → left=13
mid=14: feasible(14)=False (6 days) → left=15
left==right==15 → return 15 ✓
```

**Checkpoint:** All three tests pass. Submit to LeetCode #1011.

---

### 3.2 — Search in Rotated Sorted Array (LeetCode #33)

```python
def search_rotated(nums, target):
    """
    Search for target in a rotated sorted array (no duplicates).
    Returns index or -1.
    Key insight: one half is always sorted; check which half and narrow.
    Time: O(log n)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1    # target is in sorted left half
            else:
                left = mid + 1     # target is in right half
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1     # target is in sorted right half
            else:
                right = mid - 1    # target is in left half

    return -1
```

Test:

```python
print(search_rotated([4,5,6,7,0,1,2], 0))   # 4
print(search_rotated([4,5,6,7,0,1,2], 3))   # -1
print(search_rotated([1], 0))               # -1
```

**Checkpoint:** All three tests pass. Submit to LeetCode #33.

---

### 3.3 — Integration Test

```python
def test_all():
    # Merge sort
    assert merge_sort([5,3,8,1]) == [1,3,5,8]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]

    # Inversions
    _, inv = count_inversions([3,1,2])
    assert inv == 2
    _, inv2 = count_inversions([5,4,3,2,1])
    assert inv2 == 10

    # Binary search
    assert binary_search([1,3,5,7,9], 7) == 3
    assert binary_search([1,3,5,7,9], 6) == -1

    # Leftmost
    assert search_leftmost([1,2,2,2,3], 2) == 1

    # Ship packages
    assert ship_within_days([1,2,3,4,5,6,7,8,9,10], 5) == 15

    # Rotated search
    assert search_rotated([4,5,6,7,0,1,2], 0) == 4
    assert search_rotated([4,5,6,7,0,1,2], 3) == -1

    print('All assertions passed.')

test_all()
```

**Checkpoint:** All assertions pass. LeetCode #1011 and #33 submitted.

---

## Deliverables

Submit to Canvas:

1. `lab12_divide_conquer.py` — all implementations and integration test
2. LeetCode submission screenshots for #1011 and #33
3. Short written answer (3–5 sentences): Apply the Master Theorem to merge sort's recurrence T(n) = 2T(n/2) + O(n). Identify a, b, c, which case applies, and the resulting complexity.

---

## Summary

| Concept | Key Point |
|---|---|
| Merge sort | T(n)=2T(n/2)+O(n) → O(n log n); stable; O(n) space |
| Merge | Two-pointer combine of sorted halves — O(n) |
| Inversion count | Merge step: right-before-left → `inversions += len(left) - i` |
| Binary search | `mid = left + (right-left)//2`; `while left <= right` |
| Leftmost occurrence | `while left < right`; `right = mid` when `arr[mid] >= target` |
| Binary search on answer | Monotone `feasible(x)`; converge with `while left < right` |
| Rotated sorted array | One half always sorted; check which half contains target |
| Master Theorem Case 2 | T(n)=aT(n/b)+O(n^c) with f(n)=Θ(n^c) → O(n^c log n) |
