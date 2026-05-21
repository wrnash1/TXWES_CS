# Quiz: Module 02 – Arrays and Dynamic Arrays
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the time complexity of accessing an element by index in a static array?
*   A) O(n)
*   B) O(log n)
*   C) O(1)
*   D) O(n²)
*   **Correct Answer:** C) O(1)
*   **Distractor Analysis:**
    *   *Why correct:* Arrays store elements at contiguous memory addresses; the address of any element is computed in a single arithmetic step (base + index × size), making access constant time regardless of array length.
    *   A is incorrect: O(n) access would require scanning each element, as in a linked list.
    *   B is incorrect: O(log n) describes binary search, not direct index access.
    *   D is incorrect: O(n²) is far too expensive and describes nested iteration, not single access.

---

**Question 2**
Which of the following is the most accurate definition of a **dynamic array** in the context of data structures?
*   A) An array stored across multiple non-contiguous memory blocks, using pointers to link each block to the next, allowing unlimited growth without copying.
*   B) A resizable array that maintains a contiguous backing buffer, doubling its capacity when full and copying existing elements to the new buffer, achieving O(1) amortized append.
*   C) An array whose elements are sorted automatically on every insertion, maintaining order at the cost of O(log n) per insert using a binary search to find the correct position.
*   D) A fixed-size array that uses a circular index to wrap around to the beginning when the end is reached, enabling efficient queue operations without shifting elements.
*   **Correct Answer:** B) A resizable array that maintains a contiguous backing buffer, doubling its capacity when full and copying existing elements to the new buffer, achieving O(1) amortized append.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes a linked list, not a dynamic array. Dynamic arrays require contiguous memory.
    *   *Why B is correct:* Python's `list` and Java's `ArrayList` work exactly this way — contiguous buffer, double-on-full, amortized O(1) append.
    *   *Why C is incorrect:* That describes a sorted array or insertion into a sorted structure, not the behavior of a dynamic array.
    *   *Why D is incorrect:* That describes a circular buffer (ring buffer), a distinct data structure used for fixed-capacity queues.

---

**Question 3**
You are given a sorted array and asked to find two numbers that add up to a target value. Which approach achieves O(n) time and O(1) space?
*   A) Use a nested loop to check every pair.
*   B) Use a two-pointer approach: one pointer at the start, one at the end, move them toward each other based on the current sum.
*   C) Sort the array first, then use binary search for each element.
*   D) Build a hash map of all elements, then check for each element's complement.
*   **Correct Answer:** B) Use a two-pointer approach: one pointer at the start, one at the end, move them toward each other based on the current sum.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A nested loop is O(n²) time — correct but far too slow.
    *   *Why B is correct:* Because the array is sorted, pointers from both ends can determine in O(1) whether to move left or right, covering all pairs in a single O(n) pass with no extra memory.
    *   *Why C is incorrect:* The array is already sorted; sorting again is wasted work. Binary search per element gives O(n log n), not O(n).
    *   *Why D is incorrect:* The hash map approach is O(n) time but also O(n) space — valid, but the question asks for O(1) space.

---

**Question 4**
When a dynamic array doubles its capacity, what is the time complexity of that single resize operation?
*   A) O(1)
*   B) O(log n)
*   C) O(n)
*   D) O(n²)
*   **Correct Answer:** C) O(n)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The resize copies all existing elements to the new buffer, which takes time proportional to n — not constant.
    *   *Why B is incorrect:* There is no halving or logarithmic structure in a flat copy of n elements.
    *   *Why C is correct:* Copying n elements one by one is exactly O(n). The key insight is that this expensive operation happens so rarely (exponentially less often as n grows) that the amortized cost per append is still O(1).
    *   *Why D is incorrect:* A flat copy loop has no nesting; O(n²) would require n work per element copied.

---

**Question 5**
You need the sum of elements between index `l` and index `r` (inclusive) in a static array, and this query will be repeated thousands of times on the same array. What preprocessing strategy reduces each query to O(1)?
*   A) Sort the array so binary search can locate the boundaries quickly.
*   B) Store a prefix sum array where `prefix[i]` = sum of all elements from index 0 to i–1, then answer each query as `prefix[r+1] - prefix[l]`.
*   C) Use a sliding window that recomputes the sum by moving one index at a time between queries.
*   D) Build a hash map from each index to its element value for fast direct lookup.
*   **Correct Answer:** B) Store a prefix sum array where `prefix[i]` = sum of all elements from index 0 to i–1, then answer each query as `prefix[r+1] - prefix[l]`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Sorting changes element positions and does not help with range sum queries; it also takes O(n log n) preprocessing with no benefit per query.
    *   *Why B is correct:* Prefix sums take O(n) to build, then make every range sum query O(1) through a simple subtraction. This is a classic interview pattern.
    *   *Why C is incorrect:* A sliding window moves incrementally and still costs O(n) total if the query window jumps around arbitrarily between calls.
    *   *Why D is incorrect:* A hash map gives O(1) access to individual elements but does not help sum a range; you would still need O(r–l) operations per query.
