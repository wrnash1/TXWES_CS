# Quiz: Module 07 — Heaps & Priority Queues

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

In a 0-indexed array representing a heap, a node is stored at index `i`. What are the indices of its left child and right child?

- A) Left: `2*i`, Right: `2*i + 1`
- B) Left: `2*i + 1`, Right: `2*i + 2`
- C) Left: `i + 1`, Right: `i + 2`
- D) Left: `(i - 1) // 2`, Right: `(i + 1) // 2`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `2*i` would place the left child at index 0 when `i=0` — the root would be its own left child. This formula works for 1-indexed arrays, not 0-indexed ones.
- *Why B is correct:* For a 0-indexed heap, left child is at `2*i + 1` and right child at `2*i + 2`. This follows from the complete binary tree structure: every level doubles in node count, and the offset accounts for the 0-based index. For the root (i=0): left=1, right=2; for node at i=1: left=3, right=4. The inverse (parent) is `(i-1)//2`.
- *Why C is incorrect:* `i+1` and `i+2` would give the next two array positions, not tree children. Consecutive array positions are not parent-child relationships in a heap.
- *Why D is incorrect:* `(i-1)//2` is the parent formula, not the child formula. These options have the formula direction reversed.

---

### Question 2

What is the heap property of a **min-heap**?

- A) The root is the maximum element in the heap
- B) Every node's value is greater than or equal to its children's values
- C) Every node's value is less than or equal to its children's values
- D) Every node's value equals the average of its children's values

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* That describes a max-heap. In a min-heap, the root is the minimum, not the maximum.
- *Why B is incorrect:* That describes the max-heap property (parent ≥ children). Swapping ≥ for ≤ describes the opposite structure.
- *Why C is correct:* In a min-heap, every parent is ≤ its children. This guarantees the minimum element is always at the root (index 0), accessible in O(1). Every ancestor of any node is smaller than that node.
- *Why D is incorrect:* A heap does not impose any averaging relationship between nodes. The heap property is a positional dominance condition, not a statistical one.

---

### Question 3

After calling `heap_push` to insert a new value into a min-heap, what operation restores the heap property?

- A) Sift down — swap the new value with its smaller child until no violation exists
- B) Sift up — swap the new value with its parent while the parent is greater
- C) Rebuild the entire heap using heapify — O(n)
- D) Sort the array — O(n log n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Sift down is used during extract-min (heap pop), starting at the root. A newly inserted value is placed at the end of the array, so it has no children to sift down into initially.
- *Why B is correct:* After appending the new value to the end of the array, it is at a leaf position. It may violate the heap property with its parent. Sift up repeatedly compares the new value to its parent `(i-1)//2` and swaps if the parent is larger, bubbling the value up to its correct position. Maximum swaps = height = O(log n).
- *Why C is incorrect:* Rebuilding from scratch via heapify is O(n) — correct but extremely inefficient for a single insert. The targeted sift-up path is O(log n).
- *Why D is incorrect:* Sorting the array would be O(n log n) and destroy the heap structure being incrementally built. The heap property is weaker than sorted order and requires only local parent-child comparisons.

---

### Question 4

`heap_pop` (extract-min) removes the root of a min-heap. What is the first step, before sifting down?

- A) Remove the last element and shift all remaining elements left by one position
- B) Swap the root with the last element, then remove the last element
- C) Find the minimum of the left and right subtrees and promote it to the root
- D) Recursively pop from the left subtree until the heap is rebuilt

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Shifting all elements left is O(n) and destroys the complete binary tree structure. A heap must remain a complete binary tree to maintain the array index formula.
- *Why B is correct:* Swapping root with last element and removing the last element maintains the complete binary tree shape (only the array length changes, not any interior structure). The new root may now violate the heap property, which is why sift-down follows immediately — comparing the new root with both children and swapping with the smaller.
- *Why C is incorrect:* Promoting from a subtree minimum would require O(n) scanning and would break the structural integrity of the heap — the promoted node's subtree would itself become unbalanced.
- *Why D is incorrect:* Recursive popping is not how heap operations work. Each pop is an O(log n) single-path operation from root to leaf; no recursion into subtrees is involved.

---

### Question 5

What is the time complexity of `heapq.heapify(data)` on a list of `n` elements?

- A) O(n log n) — one sift-down per element, each O(log n)
- B) O(n) — bottom-up sift-down with convergent cost analysis
- C) O(log n) — only the root needs adjustment
- D) O(n²) — all pairs must be compared

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n log n) is the cost of building a heap by calling `heappush` n times. `heapify` uses a smarter algorithm and is asymptotically better, even though it also calls sift-down n/2 times.
- *Why B is correct:* `heapify` processes internal nodes from bottom to top. Nodes near the bottom are numerous but need few swaps; nodes near the top need more swaps but are few. Summing across all heights: n/4 nodes × 1 swap + n/8 nodes × 2 swaps + ... converges to 2n swaps total — O(n). This is a frequently tested interview fact.
- *Why C is incorrect:* O(log n) is the complexity of a single push or pop. `heapify` must process all internal nodes (n/2 of them) and cannot be that fast.
- *Why D is incorrect:* O(n²) would suggest comparing every element to every other, which no heap algorithm does. Heaps compare only along parent-child paths.

---

### Question 6

Python's `heapq` module is a **min-heap only**. How do you simulate a max-heap using `heapq`?

- A) Use `heapq.heapmax()` — a built-in max-heap function
- B) Pass `reverse=True` to `heapq.heappush()`
- C) Negate values on push (`-val`) and negate again on pop
- D) Sort the heap in reverse order before each operation

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `heapq.heapmax()` does not exist. Python's `heapq` module has no built-in max-heap function. The module only provides min-heap operations.
- *Why B is incorrect:* `heapq.heappush()` has no `reverse` parameter. All `heapq` operations work on the min-heap invariant only; there is no flag to invert behavior.
- *Why C is correct:* By pushing `-val` instead of `val`, the largest original value becomes the most negative number — the minimum in the negated min-heap. When popping, negate again to recover the original value. This is the standard Python idiom: `heapq.heappush(h, -val)` to push; `-heapq.heappop(h)` to pop the maximum.
- *Why D is incorrect:* Sorting is O(n log n) and would be required before every operation, making the structure no longer a heap at all. This defeats the purpose.

---

### Question 7

What does `heapq.heapreplace(heap, item)` do, and when is it more efficient than `heappop` followed by `heappush`?

- A) It inserts `item` at a random position — O(1)
- B) It pops the minimum and pushes `item` in one O(log n) call, saving one sift operation
- C) It replaces the entire heap with a single-element heap containing `item` — O(1)
- D) It is never more efficient than separate pop and push operations

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `heapreplace` always pops the root (minimum) and pushes the new item — both steps involving sift operations. It is not a random insertion and is not O(1).
- *Why B is correct:* `heapreplace` atomically removes the current root and places `item` at the root, then sifts down once — one O(log n) call instead of two. This is especially efficient in the K-th largest pattern: when a new value is larger than the heap minimum, `heapreplace` discards the minimum and inserts the new value in a single pass.
- *Why C is incorrect:* `heapreplace` operates on the existing heap of n elements. It does not replace the whole heap — only the root element, followed by a sift-down to restore order.
- *Why D is incorrect:* `heapreplace` is measurably more efficient when used correctly: one sift-down instead of one sift-down (pop) plus one sift-up (push). The savings matter in tight loops like streaming K-th largest computations.

---

### Question 8

For the K-th largest element pattern, why is a **min-heap** of size K used — rather than a max-heap of all elements?

- A) A max-heap would require O(n²) time to find the K-th largest
- B) The min-heap of size K keeps the K largest values seen; its root is the K-th largest, and values smaller than it are discarded in O(log k) time
- C) Python's `heapq` only supports min-heaps, so there is no choice
- D) A min-heap of size K uses less memory than a max-heap of size K

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A max-heap of all elements would give O(k log n) time for K pops — better than O(n²). The max-heap approach is valid but uses O(n) space. The min-heap approach wins on space.
- *Why B is correct:* The K-element min-heap acts as a filter: the root is the smallest of the K largest values seen so far — exactly the K-th largest. Any incoming value larger than the root displaces it (via `heapreplace`), keeping exactly the top K. Processing all n elements is O(n log k) time, O(k) space — optimal for streaming data.
- *Why C is incorrect:* While Python's `heapq` is min-heap only, the algorithm choice is conceptual, not a Python limitation. Even with max-heap support, the min-heap-of-size-K approach is preferred for its O(k) space efficiency.
- *Why D is incorrect:* A min-heap of size K and a max-heap of size K use the same memory — both store K elements. The advantage is in time complexity (O(n log k) vs O(n log n) for sorting) and streaming suitability, not memory.

---

### Question 9

In the Merge K Sorted Lists algorithm (LeetCode #23), each heap entry is a tuple `(val, list_idx, elem_idx)`. Why is `list_idx` included in the tuple?

- A) To sort the output by list index rather than by value
- B) To break ties when two lists contain equal values — Python compares tuples lexicographically
- C) To allow the heap to store pointers instead of values
- D) `list_idx` is not needed — only `val` and `elem_idx` are required

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The output is sorted by value, not by list index. `list_idx` is used for heap comparison disambiguation, not for output ordering.
- *Why B is correct:* Python compares tuples lexicographically: first by `val`, then by `list_idx` if values are equal, then by `elem_idx`. Without `list_idx`, two entries with equal `val` would compare `elem_idx` directly — which is fine in most cases, but adding `list_idx` first makes the comparison well-defined and avoids any accidental comparison of non-comparable objects if the tuple ever held complex objects instead of integers.
- *Why C is incorrect:* The tuple stores actual values and integer indices, not pointers. After popping `(val, li, ei)`, the algorithm looks up `lists[li][ei+1]` — a direct array access, not a pointer dereference.
- *Why D is incorrect:* Without `list_idx`, tuples `(val, elem_idx)` from different lists could have ambiguous ordering when values match. Including `list_idx` ensures Python's tuple comparison never reaches an incomparable stage.

---

### Question 10

Compared to quicksort, what is the key advantage of heap sort in terms of worst-case time complexity?

- A) Heap sort is O(n) in all cases; quicksort is O(n log n) average
- B) Heap sort is O(n log n) worst case; quicksort degrades to O(n²) worst case
- C) Heap sort uses O(log n) extra space; quicksort uses O(n) extra space
- D) Heap sort is stable; quicksort is not

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Heap sort is O(n log n) in all cases, not O(n). The build phase is O(n) but the n extraction pops are each O(log n), giving O(n log n) total.
- *Why B is correct:* Heap sort guarantees O(n log n) in the worst case because every sift-down is bounded by tree height O(log n), regardless of input. Quicksort's worst case is O(n²) when the pivot selection consistently produces unbalanced partitions — for example, on already-sorted input with a naive first-element pivot.
- *Why C is incorrect:* Heap sort uses O(1) auxiliary space (sorting in place); quicksort uses O(log n) average stack space for recursion (O(n) worst case). The space comparison is the opposite of what this option claims.
- *Why D is incorrect:* Heap sort is **not** stable — elements with equal values may be reordered during the sift-down phase. Merge sort is the canonical stable O(n log n) sort. Quicksort can also be made stable with extra space, but neither heap sort nor standard quicksort preserves equal-element order.
