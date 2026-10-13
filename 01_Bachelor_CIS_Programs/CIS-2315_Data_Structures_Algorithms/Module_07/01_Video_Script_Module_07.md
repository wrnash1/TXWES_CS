# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 07 — Heaps & Priority Queues

**Estimated Duration:** 21–25 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Draw the heap as a tree first, then show the array mapping. Students must see both representations.
> - Heapify direction matters: sift-up for insert (push up from a leaf), sift-down for extract-min (push down from root). Draw both paths explicitly.
> - Python's `heapq` is a min-heap. For a max-heap, negate values (push `-val`, negate on pop). Demonstrate this explicitly — it trips up many students.
> - K-th largest / smallest element is the most common heap interview pattern. Show the K-size heap approach.
> - Merge K sorted lists: classic interview problem using a heap. Walk through the algorithm.
> - The array index formula (children at 2i+1 and 2i+2, parent at (i-1)//2) must be memorized.
> - Common mistakes: confusing min-heap with max-heap, forgetting that heap sort is O(n log n) in all cases (not O(n log n) average like quicksort), misidentifying parent/child indices.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 07 | Heaps & Priority Queues | CIS-2315"]**

"This module covers the heap — the most efficient data structure for repeatedly finding and removing the minimum (or maximum) element. A heap supports insert and extract-min both in O(log n), making it the engine behind priority queues, heap sort, Dijkstra's shortest path algorithm, and the top-K element pattern that appears in dozens of interview problems. Python provides `heapq` as a built-in min-heap. By the end of this module you will understand the heap property, the array representation, the sift-up and sift-down operations, and the key patterns that appear in interviews."

---

## [01:30 – 07:00] Part 1 — Heap Structure and Array Representation

**[SHOW SLIDE: "The Heap — Complete Binary Tree with Heap Property"]**

"A heap is a complete binary tree (all levels fully filled except possibly the last, which fills left to right) that satisfies the heap property.

In a **min-heap**: every node's value is ≤ its children's values. The minimum is always at the root.

In a **max-heap**: every node's value is ≥ its children's values. The maximum is always at the root.

**[SHOW DIAGRAM: min-heap tree with values 1, 3, 5, 4, 8, 7, 6]**

```text
         1
       /   \
      3     5
     / \   / \
    4   8 7   6
```

[PAUSE]

**Array representation:** Because the heap is a complete binary tree, we can store it in an array without any pointers. For a node at index i:

- Left child: index `2*i + 1`
- Right child: index `2*i + 2`
- Parent: index `(i - 1) // 2`

The tree above stored as an array: `[1, 3, 5, 4, 8, 7, 6]`

```text
Index:  0  1  2  3  4  5  6
Value: [1, 3, 5, 4, 8, 7, 6]
```

Root at index 0. Left child of node at index 1 is at index 3. Right child is at index 4. Parent of node at index 3 is `(3-1)//2 = 1`. ✓

[PAUSE]

This array representation is why heaps are cache-friendly — nodes are stored contiguously in memory, with no pointer overhead."

---

## [07:00 – 12:00] Part 2 — Heap Operations

**[SHOW SLIDE: "Insert (Sift Up) and Extract-Min (Sift Down)"]**

"**Insert — O(log n):**

To insert a new value, append it to the end of the array, then bubble it up (sift up) until the heap property is restored.

```python
def heap_push(heap, val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] > heap[i]:     # min-heap: parent should be smaller
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break
```

Worst case: bubble all the way from a leaf to the root — O(log n) swaps.

[PAUSE]

**Extract-Min — O(log n):**

To remove the minimum (root), swap it with the last element, remove the last element, then sift down until the heap property is restored.

```python
def heap_pop(heap):
    if len(heap) == 1:
        return heap.pop()
    min_val = heap[0]
    heap[0] = heap.pop()     # move last element to root
    i = 0
    n = len(heap)
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
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

Sift down always swaps with the smaller child to preserve the min-heap property.

[PAUSE]

**Python's heapq:**

```python
import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(heapq.heappop(h))   # 1 — always the minimum
print(heapq.heappop(h))   # 3
print(heapq.heappop(h))   # 5
```

`heapq` is a min-heap. For a max-heap, negate values: push `-val`, negate when popping."

---

## [12:00 – 16:00] Part 3 — Heapify: O(n) Build

**[SHOW SLIDE: "heapify — Building a Heap in O(n)"]**

"You might expect building a heap from a list to cost O(n log n) — one push per element. But there is a smarter algorithm: sift down every internal node from the last internal node to the root.

```python
def heapify(arr):
    n = len(arr)
    # Start from the last internal node, go to root
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)
```

**Why O(n)?** Most nodes are near the bottom of the tree and need few swaps. The analysis shows:

- n/2 nodes are leaves (0 swaps each)
- n/4 nodes are at height 1 (at most 1 swap each)
- n/8 nodes are at height 2 (at most 2 swaps each)
- ...

Summing: total swaps ≤ n/4 · 1 + n/8 · 2 + n/16 · 3 + ... ≤ 2n = O(n).

Python's `heapq.heapify(list)` does this in O(n). Use it to convert an unsorted list to a heap:

```python
import heapq
data = [5, 3, 8, 1, 9, 2, 7]
heapq.heapify(data)
print(data)   # [1, 3, 2, 5, 9, 8, 7] — min at index 0
```"

---

## [16:00 – 20:00] Part 4 — Key Interview Patterns

**[SHOW SLIDE: "Top K Elements Pattern"]**

"The most common heap interview pattern: find the K largest (or smallest) elements in a stream or list.

**K Largest Elements — maintain a min-heap of size K:**

```python
import heapq

def k_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)      # min-heap of k elements
    for num in nums[k:]:
        if num > heap[0]:    # larger than current minimum in heap
            heapq.heapreplace(heap, num)   # pop min, push num
    return heap
```

The heap always contains the K largest values seen so far. Anything smaller than the current minimum of the heap gets rejected. Time: O(n log k).

[PAUSE]

**Merge K Sorted Lists (LeetCode #23):**

```python
import heapq

def merge_k_sorted(lists):
    result = []
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, elem_idx)
    while heap:
        val, li, ei = heapq.heappop(heap)
        result.append(val)
        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei + 1], li, ei + 1))
    return result
```

The heap always contains the current minimum from each remaining list. For K lists with total N elements, time is O(N log K)."

---

## [20:00 – 23:00] Part 5 — Heap Sort and Complexity

**[SHOW SLIDE: "Heap Sort and Complexity Summary"]**

"Heap sort uses a heap to sort in O(n log n) with O(1) auxiliary space:

1. Build a max-heap from the array — O(n)
2. Repeatedly extract the max, placing it at the end — O(n log n)

Total: O(n log n) time, O(1) space (sorting in place). Unlike merge sort, heap sort requires no extra array.

**Complexity Summary:**

| Operation | Time | Notes |
|---|---|---|
| Push (insert) | O(log n) | Sift up |
| Pop (extract-min) | O(log n) | Sift down |
| Peek (min/max) | O(1) | Root access |
| Build from list | O(n) | heapify |
| Heap sort | O(n log n) | Build O(n) + n pops × O(log n) |
| Space | O(n) | Array storage |

The Module 07 lab has you implement heap push and pop from scratch, use Python's `heapq` for the K-largest pattern, and solve LeetCode #703 and #215. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 07 — Heaps & Priority Queues]**

---

## Additional Resources

- [VisuAlgo — Heap Visualization](https://visualgo.net/en/heap)
- [NeetCode — Heap / Priority Queue](https://www.youtube.com/watch?v=HqPJF2L5h9U)
- [LeetCode #703 — Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [LeetCode #215 — Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LeetCode #23 — Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
