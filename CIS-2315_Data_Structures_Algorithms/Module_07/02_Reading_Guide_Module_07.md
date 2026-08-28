# Reading Guide: Module 07 — Heaps & Priority Queues

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

A heap is a complete binary tree stored as an array that satisfies the heap property: the minimum (or maximum) is always accessible at the root in O(1). Insert and extract-min are both O(log n). Python provides `heapq` as a built-in min-heap. Heaps power priority queues, heap sort, Dijkstra's algorithm, and the top-K element pattern — one of the most common interview problem families.

---

## 1. Heap Structure

### Heap Properties

A **min-heap** satisfies: every node's value ≤ its children's values. The root is the minimum.

A **max-heap** satisfies: every node's value ≥ its children's values. The root is the maximum.

A heap is also a **complete binary tree**: all levels fully filled except possibly the last, which fills left to right. This completeness property is what allows the array representation.

### Array Representation

For a node at array index i:

- Left child: index `2*i + 1`
- Right child: index `2*i + 2`
- Parent: index `(i - 1) // 2`

The root is at index 0. This formula works for any 0-indexed array.

```text
Tree:         1
            /   \
           3     5
          / \   / \
         4   8 7   6

Array: [1, 3, 5, 4, 8, 7, 6]
Index:  0  1  2  3  4  5  6
```

---

## 2. Heap Operations

### Insert — Sift Up — O(log n)

Append the new value to the end of the array, then bubble it up by swapping with its parent while the heap property is violated.

```python
def heap_push(heap, val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] > heap[i]:      # min-heap violation
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break
```

Maximum swaps = height of tree = O(log n).

### Extract-Min — Sift Down — O(log n)

Swap root with last element, remove last element, then sift the new root down by swapping with the smaller child while the heap property is violated.

```python
def heap_pop(heap):
    if len(heap) == 1:
        return heap.pop()
    min_val = heap[0]
    heap[0] = heap.pop()      # move last element to root
    i = 0
    n = len(heap)
    while True:
        left, right = 2*i+1, 2*i+2
        smallest = i
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
    return min_val
```

### Heapify — O(n)

Convert an unordered array to a heap by sifting down every internal node from the last internal node (index `n//2 - 1`) to the root.

```python
import heapq
data = [5, 3, 8, 1, 9, 2, 7]
heapq.heapify(data)    # modifies in place — O(n)
# data[0] is now the minimum
```

**Why O(n) not O(n log n)?** Most nodes are near the bottom and require few swaps. The exact sum converges to 2n, giving O(n).

### Peek — O(1)

The minimum is always at `heap[0]`. No popping needed.

---

## 3. Python heapq Module

```python
import heapq

h = []
heapq.heappush(h, 5)   # push 5
heapq.heappush(h, 1)   # push 1
heapq.heappush(h, 3)   # push 3
print(h[0])            # 1 — peek at min, O(1)
print(heapq.heappop(h))  # 1 — extract min, O(log n)
```

**Max-heap with heapq:** Negate values on push and pop.

```python
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
print(-heapq.heappop(max_heap))   # 5 — largest value
```

**heapq.heapreplace(heap, item):** Pop min and push item in one O(log n) call — more efficient than separate pop + push.

**heapq.nlargest(k, iterable)** and **heapq.nsmallest(k, iterable):** Return the k largest/smallest items — O(n log k).

---

## 4. Key Interview Patterns

### K-th Largest Element (LeetCode #215, #703)

Maintain a min-heap of size K. The root is the K-th largest element seen so far.

```python
def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)        # min-heap of first k elements
    for num in nums[k:]:
        if num > heap[0]:      # larger than the K-th largest so far
            heapq.heapreplace(heap, num)
    return heap[0]             # K-th largest
```

Time: O(n log k). Space: O(k).

**Why a min-heap?** We want to track the K largest values. By keeping a min-heap of size K, the smallest of those K values is at the root. Any incoming value larger than the root displaces it.

### Merge K Sorted Lists (LeetCode #23)

```python
def merge_k_sorted(lists):
    result = []
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    while heap:
        val, li, ei = heapq.heappop(heap)
        result.append(val)
        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei+1], li, ei+1))
    return result
```

Time: O(N log K) where N = total elements, K = number of lists.

---

## 5. Complexity Summary

| Operation | Time | Notes |
|---|---|---|
| Push (insert) | O(log n) | Sift up from leaf |
| Pop (extract-min) | O(log n) | Sift down from root |
| Peek (min/max) | O(1) | `heap[0]` |
| Build from list | O(n) | `heapify` — bottom-up sift-down |
| Heap sort | O(n log n) | Build O(n) + n pops × O(log n) |
| K-th largest | O(n log k) | Maintain size-k min-heap |
| Merge K sorted lists | O(N log K) | N total elements, K lists |
| Space | O(n) | Array storage |

---

## 6. Interview Exam Tips

1. **Python `heapq` is min-heap only** — for max-heap, negate values on push (`-val`) and negate on pop.

2. **`heap[0]` is O(1) peek** — never pop just to see the minimum. Access `heap[0]` directly.

3. **heapify is O(n), not O(n log n)** — converting an existing list to a heap is O(n). Interviewers sometimes ask this as a gotcha.

4. **K-th largest uses a min-heap of size K** — this counterintuitive choice is worth memorizing: a min-heap lets you efficiently discard values smaller than the K-th largest.

5. **Heap sort is O(n log n) worst case** — unlike quicksort (O(n²) worst case), heap sort guarantees O(n log n). Mention this in system design discussions.

6. **Array index formula** — left child = `2i+1`, right child = `2i+2`, parent = `(i-1)//2`. Memorize this for interviews requiring a custom heap.

7. **Tie-breaking in heaps** — when pushing tuples, Python compares lexicographically. `(val, index)` tuples break ties by index. This is required for Merge K Sorted Lists where values can be equal.

8. **`heapq.heapreplace`** — more efficient than `pop` + `push` when you know the new value is ≥ the current min. One O(log n) call instead of two.

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Binary Heap Visualizations** — [https://visualgo.net/en/heap](https://visualgo.net/en/heap)
   Animated step-by-step visualization of heap insert (sift-up) and extract-min (sift-down) operations. Watch how the array index formula maps to the tree representation in real time.

2. **OpenDSA — Heaps Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Heaps.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Heaps.html)
   Free interactive OER textbook covering the heap property, array representation, heapify algorithm, and the O(n) proof for `heapify`. Includes embedded exercises.

3. **Python `heapq` Module Documentation** — [https://docs.python.org/3/library/heapq.html](https://docs.python.org/3/library/heapq.html)
   Official Python documentation for all `heapq` functions including `heappush`, `heappop`, `heapify`, `heapreplace`, `nlargest`, and `nsmallest`. Includes worked examples and a note on max-heap simulation with negated values.

4. **NeetCode — Heap / Priority Queue Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
   Free video solutions for common heap interview problems including Kth Largest Element, Top K Frequent Elements, and Merge K Sorted Lists, each with clear explanation of the min-heap-of-size-K pattern.

5. **Abdul Bari — Heap Sort (YouTube)** — [https://www.youtube.com/watch?v=HqPJF2L5h9U](https://www.youtube.com/watch?v=HqPJF2L5h9U)
   Clear diagram-based walkthrough of heapify, heap sort, and the O(n log n) time complexity analysis. Useful for understanding why `heapify` is O(n) despite appearing to be O(n log n).

---

## 7. Study Checklist

- [ ] Watch the Module 07 video lecture by Professor Nash.
- [ ] Implement `heap_push` and `heap_pop` from scratch.
- [ ] Memorize the array index formula for children and parent.
- [ ] Use `heapq.heapify` to build a heap from a list; verify O(n).
- [ ] Implement the K-th largest pattern using a min-heap.
- [ ] Solve LeetCode #703 (Kth Largest Element in a Stream).
- [ ] Solve LeetCode #215 (Kth Largest Element in an Array).
- [ ] Attempt LeetCode #23 (Merge K Sorted Lists) as a stretch goal.
- [ ] Complete the Module 07 Lab.
- [ ] Complete the Module 07 Quiz.
