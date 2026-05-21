# Quiz: Module 08 – Heaps and Priority Queues
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the time complexity of extracting the minimum element from a min-heap?
*   A) O(1)
*   B) O(log n)
*   C) O(n)
*   D) O(n log n)
*   **Correct Answer:** B) O(log n)
*   **Distractor Analysis:**
    *   *Why correct:* Extracting the root (minimum) replaces it with the last element, then sifts down through at most O(log n) levels to restore the heap property.
    *   A is incorrect: O(1) describes peeking at the minimum (just read the root) without removing it.
    *   C is incorrect: O(n) would imply scanning all elements, which heaps are specifically designed to avoid.
    *   D is incorrect: O(n log n) is the cost of sorting an entire array using a heap (heap sort), not a single extraction.

---

**Question 2**
Which of the following is the most accurate definition of the **heap property** for a min-heap?
*   A) The tree is sorted in ascending order left to right at every level, so the smallest element in each row is always on the leftmost branch.
*   B) For every node N in the tree, N's value is less than or equal to the values of both its children, ensuring the minimum element is always at the root.
*   C) The left subtree of every node contains only values less than the node, and the right subtree contains only values greater, enabling O(log n) search by the BST property.
*   D) All leaf nodes store values that are smaller than all internal nodes, pushing the minimum to the bottom level of the tree for efficient range queries.
*   **Correct Answer:** B) For every node N in the tree, N's value is less than or equal to the values of both its children, ensuring the minimum element is always at the root.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The heap property is a parent-child constraint, not a left-to-right level-order sort. Elements within the same level have no required ordering relative to each other.
    *   *Why B is correct:* This is the exact min-heap invariant. It applies to every parent-child pair throughout the tree, which guarantees the global minimum lives at the root.
    *   *Why C is incorrect:* That describes the BST property, not the heap property. Heaps do not support efficient search; BSTs do.
    *   *Why D is incorrect:* The minimum in a min-heap is always at the root (top), not at the leaves (bottom). This describes the opposite structure.

---

**Question 3**
You need to find the K largest elements in an array of n elements. Which heap strategy gives O(n log K) time and O(K) space?
*   A) Build a max-heap from the entire array, then extract the maximum K times.
*   B) Maintain a min-heap of size K; push each element and pop if the heap exceeds K. The K elements remaining are the largest.
*   C) Sort the array in descending order and take the first K elements.
*   D) Insert all elements into a min-heap, then extract the minimum until n–K elements have been removed.
*   **Correct Answer:** B) Maintain a min-heap of size K; push each element and pop if the heap exceeds K. The K elements remaining are the largest.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Building a max-heap is O(n) but extracting K maximums is O(K log n), not O(n log K). Also uses O(n) space for the full heap.
    *   *Why B is correct:* Each of the n elements is pushed in O(log K) time (heap of size K); pops are also O(log K). Total: O(n log K) with O(K) space — optimal for streaming top-K.
    *   *Why C is incorrect:* Sorting is O(n log n), which is worse than O(n log K) when K << n. Also uses O(n) space in many implementations.
    *   *Why D is incorrect:* This approach uses O(n) space and O(n log n) total time (inserting all n then extracting n–K) — far worse than the size-K heap approach.

---

**Question 4**
Why is building a heap from an unsorted array using `heapify` O(n) rather than O(n log n)?
*   A) Because `heapify` sorts the array first using merge sort, which has O(n log n) cost, and then the sorted array is already a valid heap.
*   B) Because half the nodes are leaves and do O(1) work; the remaining nodes at higher levels do progressively more work, but the sum of this geometric series converges to O(n).
*   C) Because `heapify` uses a hash table internally to locate each element's correct position in O(1), avoiding the log n comparison cost.
*   D) Because the array is already partially sorted in most real-world cases, and heapify exploits this with an adaptive algorithm.
*   **Correct Answer:** B) Because half the nodes are leaves and do O(1) work; the remaining nodes at higher levels do progressively more work, but the sum of this geometric series converges to O(n).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `heapify` does not sort the array. Heaps are not sorted structures; only the parent-child relationship is constrained, not sibling ordering.
    *   *Why B is correct:* In a heap with n nodes, approximately n/2 are leaves (sift-down cost 0), n/4 have height 1 (cost 1), n/8 have height 2 (cost 2), etc. Summing c·n/2^(c+1) over all heights gives a series that converges to O(n).
    *   *Why C is incorrect:* `heapify` uses no hash table. It calls sift-down on each internal node using array index arithmetic.
    *   *Why D is incorrect:* `heapify`'s O(n) complexity holds for any input order, not just partially sorted inputs. It is not an adaptive algorithm.

---

**Question 5**
In Python, how do you simulate a max-heap using the `heapq` module, which only provides a min-heap?
*   A) Call `heapq.heapify_max(arr)` — Python provides both min and max heap functions.
*   B) Negate all values before pushing (`heapq.heappush(h, -val)`) and negate again after popping (`-heapq.heappop(h)`).
*   C) Reverse the list before calling `heapq.heapify`, which converts it to a max-heap automatically.
*   D) Use `heapq.heappush(h, val)` normally; pass `reverse=True` to `heapq.heappop(h)` to extract the maximum.
*   **Correct Answer:** B) Negate all values before pushing (`heapq.heappush(h, -val)`) and negate again after popping (`-heapq.heappop(h)`).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Python's `heapq` module does not provide a `heapify_max` function for general use. `heapq._heapify_max` is a private/internal function not intended for production use.
    *   *Why B is correct:* Negating values before pushing turns the min-heap into a max-heap: the most negative value (largest original) reaches the root. Negating again on pop restores the true value. This is the standard Python interview technique.
    *   *Why C is incorrect:* Reversing the list before `heapify` does not produce a max-heap; `heapify` runs sift-down from bottom to top regardless of initial order and always produces a min-heap.
    *   *Why D is incorrect:* `heapq.heappop` does not accept a `reverse` parameter. Python's `heapq` functions have no such keyword argument.
