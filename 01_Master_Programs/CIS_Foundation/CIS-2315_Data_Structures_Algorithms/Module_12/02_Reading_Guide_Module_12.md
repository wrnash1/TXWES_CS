# Reading Guide: Module 12 — Divide & Conquer

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2315 &BULL; DATA STRUCTURES & ALGORITHM ANALYSIS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Sorting Visualizations (Merge Sort)** — [https://visualgo.net/en/sorting](https://visualgo.net/en/sorting)
   Step-by-step animated visualization of merge sort showing the divide and merge phases. Observe how sub-arrays are sorted at each recursion level and then merged in linear time.

2. **OpenDSA — Binary Search and Merge Sort** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/MergeSort.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/MergeSort.html)
   Free interactive OER textbook covering merge sort with embedded exercises, correctness proofs, and the derivation of O(n log n) via the recurrence T(n) = 2T(n/2) + O(n).

3. **NeetCode — Binary Search Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB](https://www.youtube.com/playlist?list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB)
   Free video solutions for binary search interview problems including Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array, and the Binary Search on Answer pattern (Ship Packages Within D Days).

4. **MIT OCW 6.006 — Merge Sort and Recurrences (Lecture 3)** — [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
   MIT lecture notes covering the Master Theorem for divide-and-conquer recurrences, including all three cases and worked examples with merge sort, binary search, and other algorithms.

5. **Python `bisect` Module Documentation** — [https://docs.python.org/3/library/bisect.html](https://docs.python.org/3/library/bisect.html)
   Official Python documentation for `bisect_left`, `bisect_right`, and `insort`. Shows how to use Python's built-in binary search functions for sorted arrays in interview problems requiring O(log n) search.

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
