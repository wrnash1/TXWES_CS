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

---

### Question 11

**Each question is worth 5 points.**

In a min-heap stored as an array, what is the index of the right child of the node at index `i`?

- A) `2i`
- B) `2i + 1`
- C) `2i + 2`
- D) `(i - 1) // 2`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `2i` is the left child formula in a 1-indexed array (where the root is at index 1). For 0-indexed arrays (Python's convention), the formulas shift: left child = `2i + 1`, right child = `2i + 2`.
- *Why B is incorrect:* `2i + 1` is the index of the left child in a 0-indexed array.
- *Why C is correct:* In a 0-indexed array: left child of node at `i` is at `2i + 1`; right child is at `2i + 2`. Parent is at `(i - 1) // 2`. For i=0 (root): left = 1, right = 2. For i=1: left = 3, right = 4. These formulas are fundamental to array-based heap implementation.
- *Why D is incorrect:* `(i - 1) // 2` is the parent formula. The parent of node `i` is at `(i - 1) // 2`.

---

### Question 12

What is the minimum number of elements that must be in a min-heap of height 4 (where height is the number of edges from root to the deepest leaf)?

- A) 4
- B) 8
- C) 16
- D) 31

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* 4 is the height itself. A tree with only 4 nodes can have various heights; the relationship between minimum nodes and height is 2^h.
- *Why B is incorrect:* A complete binary tree of height 3 has at least 2³ = 8 nodes... but for height 4, the minimum (complete) configuration starts from 2⁴.
- *Why C is correct:* The minimum number of nodes in a heap of height h is achieved by the smallest complete binary tree reaching that height: 2^h nodes minimum (a full tree of height h−1 plus one node at level h). For height 4: minimum nodes = 2⁴ = 16. A heap with 15 nodes has height 3; adding the 16th node creates a tree of height 4.
- *Why D is incorrect:* 31 = 2⁵ − 1 is the maximum number of nodes in a perfect binary tree of height 4 (all levels completely filled). This is the maximum, not the minimum.

---

### Question 13

A min-heap contains the values `[1, 3, 2, 7, 5, 4, 6]`. After calling `heappop()`, what is the new root?

- A) `2`
- B) `3`
- C) `4`
- D) `7`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `heappop()` removes the root (1) and replaces it with the last element (6). The heap array becomes `[6, 3, 2, 7, 5, 4]`. Sift-down on 6: compare children 3 (index 1) and 2 (index 2) — 2 is smaller, swap 6 and 2 → `[2, 3, 6, 7, 5, 4]`. Next, sift-down on 6 at index 2: children are 4 (index 5). 4 < 6, swap → `[2, 3, 4, 7, 5, 6]`. No more children. New root = 2.
- *Why B is incorrect:* 3 is at index 1 and does not become the root. After sift-down, 2 (originally at index 2) becomes the root because it is the second-smallest element.
- *Why C is incorrect:* 4 ends up as the right child of the root (index 2) after sift-down, not as the root itself.
- *Why D is incorrect:* 7 is near the bottom of the heap and does not move during this sift-down sequence.

---

### Question 14

Why does Python's `heapq` module implement only a min-heap, and how do you simulate a max-heap?

- A) Python's `heapq` supports both; use `heapq.maxheap()` for max-heap behavior
- B) Python's `heapq` is min-heap only; simulate max-heap by storing negated values and negating on retrieval
- C) Python's `heapq` is min-heap only; simulate max-heap by reversing the output array after each `heappop`
- D) Python's `heapq` is min-heap only; convert to max-heap by calling `heapq.heapify` with the `reverse=True` parameter

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python's `heapq` module has no `maxheap()` function. It provides only min-heap behavior through `heappush`, `heappop`, and `heapify`.
- *Why B is correct:* The standard Python idiom for max-heap: push `-val` instead of `val`. The min-heap will maintain the most-negative value at the top — which corresponds to the maximum original value. On retrieval, negate: `-heappop(heap)`. This is O(log n) per operation, identical to a native max-heap.
- *Why C is incorrect:* Reversing the output array after each `heappop` has O(n) cost per pop and would not produce correct heap ordering on subsequent operations.
- *Why D is incorrect:* `heapq.heapify` has no `reverse` parameter. The function signature is `heapq.heapify(x)` — no keyword arguments are supported.

---

### Question 15

What is the time complexity of finding the K smallest elements from an array of n elements using a max-heap of size K?

- A) O(n log n)
- B) O(n log K)
- C) O(K log n)
- D) O(n + K)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n log n) would be the cost of sorting the entire array. Using a heap of size K is asymptotically better when K << n.
- *Why B is correct:* Build the initial max-heap from the first K elements: O(K). For each of the remaining n−K elements: compare with the heap maximum (O(1)), and if smaller, replace (heapreplace: O(log K)). Total: O(K + (n−K) log K) = O(n log K). For K << n, log K << log n, making this much faster than O(n log n).
- *Why C is incorrect:* O(K log n) would imply K heap operations each costing log n. But heap operations cost log K (heap size K), not log n.
- *Why D is incorrect:* O(n + K) would require a linear-time selection algorithm (like quickselect). The heap approach is O(n log K), not linear.

---

### Question 16

`heapq.heapify([5, 3, 8, 1, 4])` is called. What value is at index 0 after the call?

- A) `5` — the original first element
- B) `8` — the maximum value floats to the top
- C) `1` — the minimum value is the root of a min-heap
- D) `3` — the average of all values

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `heapify` rearranges the array in-place to satisfy the min-heap property. The original first element (5) is not guaranteed to remain at index 0.
- *Why B is incorrect:* `heapq` is a min-heap. The minimum value becomes the root, not the maximum.
- *Why C is correct:* `heapq.heapify` transforms the array into a valid min-heap in O(n) time. In a min-heap, the smallest element is always at index 0 (the root). The smallest value in `[5, 3, 8, 1, 4]` is 1, so after `heapify`, `heap[0] == 1`.
- *Why D is incorrect:* Heaps are not sorted by averages. The root is always the minimum (for min-heap) or maximum (for max-heap), not the average.

---

### Question 17

In the Merge K Sorted Lists problem (LeetCode #23), why is a min-heap of size K used instead of repeatedly scanning all K list heads?

- A) A min-heap guarantees the result is sorted; scanning does not
- B) A min-heap finds the minimum of K elements in O(log K) instead of O(K), reducing total time from O(NK) to O(N log K)
- C) A min-heap uses less memory than storing K list head pointers
- D) A min-heap automatically advances list pointers; scanning requires manual iteration

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both approaches can produce a sorted merged list. The heap approach doesn't change the correctness of the merge — it reduces the time to find the minimum at each step.
- *Why B is correct:* At each step, you need the minimum among K current list heads. Linear scan: O(K) per step. For N total elements: O(NK). Min-heap of K elements: O(log K) per push/pop. For N total elements: O(N log K). When K is large (e.g., K=1,000 and N=1,000,000), O(NK) = O(10⁹) vs O(N log K) ≈ O(10⁷). The heap provides a 100× speedup in this case.
- *Why C is incorrect:* A min-heap of K tuples uses the same O(K) space as K head pointers. Memory is not the differentiator.
- *Why D is incorrect:* Both approaches require manually advancing the pointer of the list whose head was selected. The heap does not automate this — you push the next node from the selected list after popping.

---

### Question 18

What does the following code compute?

```python
import heapq
data = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(data)
result = []
while data:
    result.append(heapq.heappop(data))
print(result)
```

- A) The original list unchanged
- B) The list sorted in ascending order
- C) The list sorted in descending order
- D) Only the three smallest elements

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `heapify` rearranges the list in place, and `heappop` removes elements in sorted order. The result is not the original list.
- *Why B is correct:* `heapq.heappop` always removes and returns the minimum element. Calling it repeatedly until the heap is empty extracts elements in ascending sorted order. This is essentially heap sort (using a min-heap). For `[3, 1, 4, 1, 5, 9, 2, 6]`: result = `[1, 1, 2, 3, 4, 5, 6, 9]`.
- *Why C is incorrect:* Descending order would require a max-heap (or negating values). This code uses a min-heap, which produces ascending order.
- *Why D is incorrect:* The `while data:` loop continues until the heap is empty — all 8 elements are extracted, not just 3.

---

### Question 19

What is the time complexity of `heapq.nlargest(k, iterable)` for finding the K largest elements?

- A) O(n) always
- B) O(n log k)
- C) O(n log n)
- D) O(k log n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n) would require a linear-time selection algorithm like quickselect, which Python's `heapq.nlargest` does not use for general iterables. For special cases (k=1 or k close to n), Python may optimize, but the general complexity is O(n log k).
- *Why B is correct:* `heapq.nlargest(k, iterable)` maintains a min-heap of size k. For each of the n elements, it compares with the heap minimum and replaces if larger — O(log k) per element. Total: O(n log k). This is asymptotically better than sorting (O(n log n)) when k << n.
- *Why C is incorrect:* O(n log n) is the cost of sorting the entire iterable. `heapq.nlargest` does better than full sorting when k is small.
- *Why D is incorrect:* O(k log n) would apply if you searched a sorted array for k elements. The heap approach iterates all n elements and maintains a heap of size k — resulting in O(n log k).

---

### Question 20

After building a min-heap from `[9, 4, 7, 1, 2]` using `heapq.heapify`, which of the following is guaranteed to be true?

- A) The array is fully sorted in ascending order
- B) The first element `heap[0]` equals the minimum value in the original array
- C) Elements at even indices are smaller than elements at odd indices
- D) Each element is smaller than all elements to its right

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `heapify` produces a valid heap, not a fully sorted array. A heap satisfies the parent ≤ children property, but siblings at the same level can be in any order. The resulting array `[1, 2, 7, 4, 9]` (one valid arrangement) is not fully sorted.
- *Why B is correct:* The min-heap property guarantees the minimum element is at the root (index 0). For any valid min-heap, `heap[0]` is the global minimum. This is the entire purpose of the heap data structure.
- *Why C is incorrect:* The heap property relates parents to children (index i to 2i+1 and 2i+2), not even indices to odd indices. Even-indexed nodes are not necessarily smaller than odd-indexed nodes.
- *Why D is incorrect:* The heap property only requires each node to be ≤ its direct children, not ≤ all elements to its right. Elements to the right may be in any order relative to elements to the left, as long as every parent-child relationship satisfies the heap property.
