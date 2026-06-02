# Quiz: Module 12 — Divide & Conquer

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the time complexity of merge sort on an array of n elements?

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n) would require examining each element only once. Merge sort processes O(n) elements at each of O(log n) levels — one pass through the data is insufficient.
- *Why B is correct:* The recursion tree has log n levels (each level halves the problem size). At each level, all merge calls together examine every element exactly once — O(n) work per level. Total: O(n) × O(log n) = O(n log n). This is confirmed by the Master Theorem: T(n) = 2T(n/2) + O(n) → Case 2 → O(n log n).
- *Why C is incorrect:* O(n²) is the complexity of bubble sort and insertion sort on unsorted data. Merge sort avoids the pairwise comparison of all elements by dividing and conquering.
- *Why D is incorrect:* O(log n) is the complexity of binary search — a search algorithm, not a sort algorithm. Sorting must examine every element at least once, making sub-linear time impossible.

---

### Question 2

Why is merge sort considered a **stable** sort, and why does stability matter?

- A) Stable means merge sort never uses more than O(1) extra space
- B) Stable means equal elements maintain their relative order from the original array — this matters when sorting objects that were previously sorted by a different key
- C) Stable means merge sort produces the same output regardless of input order
- D) Stable means merge sort runs in O(n log n) in all cases, unlike unstable sorts

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Stability has nothing to do with space. Merge sort actually uses O(n) extra space for the merge step — it is not space-efficient. Stability is about element ordering.
- *Why B is correct:* A stable sort preserves the relative order of equal elements. In the `merge` function, `left[i] <= right[j]` takes from the left half first when equal, preserving original order. Stability matters when you need a multi-key sort: sort by last name, then sort by first name stably — the result is sorted by first name within each last-name group.
- *Why C is incorrect:* All correct sorting algorithms produce the same output for the same input, regardless of stability. Stability is specifically about what happens to equal elements.
- *Why D is incorrect:* Quicksort (unstable) also guarantees O(n log n) average case. Worst-case guarantees and stability are independent properties.

---

### Question 3

In the standard binary search implementation:

```python
mid = left + (right - left) // 2
```

Why is this formula preferred over `mid = (left + right) // 2`?

- A) The first formula is faster because it avoids a division operation
- B) The first formula prevents integer overflow when `left + right` exceeds the maximum integer value — critical in C++ and Java, good practice in Python
- C) The second formula gives a different `mid` value that would produce wrong results
- D) The `//` operator behaves differently on the two expressions in Python

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both formulas perform the same number of operations. The preferred formula is about correctness, not speed.
- *Why B is correct:* In C++ and Java, `int` has a maximum value (~2 billion). If `left = 1.5B` and `right = 1.5B`, `left + right` overflows to a negative number, producing a wrong `mid`. `left + (right - left) // 2` computes `right - left` first (a small number), then adds to `left`, avoiding overflow. Python integers are arbitrary precision (no overflow), but using this formula shows interviewers that you understand the pitfall.
- *Why C is incorrect:* Both formulas produce the same `mid` value mathematically: `(left + right) / 2 = left + (right - left) / 2`. There is no correctness difference in Python.
- *Why D is incorrect:* `//` is floor division in Python and applies identically to both expressions. The difference is about numerical overflow, not operator behavior.

---

### Question 4

Binary search requires the input array to be sorted. A student uses binary search on an unsorted array. Which of the following best describes what happens?

- A) Python raises an `IndexError` because unsorted arrays cannot be indexed
- B) The algorithm may return -1 (not found) even when the target is present, because the invariant "target is in arr[left..right]" is violated by unsorted data
- C) Binary search always finds the target — it just takes longer on unsorted data
- D) The algorithm returns the wrong index but never misses a present target

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python can index any list. There is no error at the language level — the issue is algorithmic correctness.
- *Why B is correct:* Binary search's correctness depends on the invariant: "if target is in the array, it is in `arr[left..right]`." In a sorted array, comparing `arr[mid]` to `target` correctly shrinks the search space. In an unsorted array, moving `left = mid + 1` or `right = mid - 1` may exclude the range containing the target, causing a false "not found" result.
- *Why C is incorrect:* Binary search does not take "longer" — it takes exactly O(log n) steps regardless. But on unsorted data, those steps may eliminate the portion of the array where the target actually resides.
- *Why D is incorrect:* A present target can easily be missed. For example, searching for 3 in `[5, 2, 4, 3, 1]`: mid=2 (value 4 > 3), set right=1; mid=0 (value 5 > 3), set right=-1; return -1. But 3 is at index 3.

---

### Question 5

In the binary search on answer template:

```python
left, right = lower_bound, upper_bound
while left < right:
    mid = left + (right - left) // 2
    if feasible(mid):
        right = mid
    else:
        left = mid + 1
return left
```

What is the invariant maintained by this loop, and what does `left` equal when the loop terminates?

- A) `left` is the maximum value for which `feasible` is False; `right` converges to `left`
- B) All values `< left` are infeasible; all values `>= left` are feasible. `left` equals the minimum value for which `feasible` is True
- C) `left` and `right` alternate — the answer is their midpoint at termination
- D) The loop maintains `feasible(left) == True` at all times

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The invariant is about feasibility, not infeasibility being maximized. `left` converges to the minimum feasible value, not the maximum infeasible one.
- *Why B is correct:* When `feasible(mid)` is True, `right = mid` because mid could be the answer (try smaller). When False, `left = mid + 1` because mid is definitely not the answer (search higher). This maintains: everything below `left` is infeasible, everything at or above `left` is feasible. At termination, `left == right` = the minimum feasible value.
- *Why C is incorrect:* `left` and `right` both converge monotonically (left increases, right decreases) until they meet. The answer is `left` (or equivalently `right`) at that point, not a midpoint.
- *Why D is incorrect:* The loop does not ensure `feasible(left) == True` during execution — `left` may point to infeasible values during intermediate steps. The invariant holds at termination, not throughout.

---

### Question 6

Apply the Master Theorem to binary search: T(n) = T(n/2) + O(1). What is a, b, and the resulting complexity?

- A) a=2, b=2, c=log₂(2)=1, Case 2 → O(n log n)
- B) a=1, b=2, c=log₂(1)=0, Case 2 with f(n)=O(n⁰)=O(1) → O(log n)
- C) a=1, b=2, c=log₂(1)=0, Case 1 with f(n)=O(1) dominating → O(1)
- D) a=2, b=2, c=log₂(2)=1, Case 1 → O(n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* a=2 would mean two recursive calls per level. Binary search makes only one call (halving the remaining range). T(n)=2T(n/2)+O(n) is merge sort, not binary search.
- *Why B is correct:* Binary search: a=1 (one subproblem), b=2 (half the size), f(n)=O(1) (comparison at each level). c = log₂(1) = 0. f(n) = O(1) = O(n⁰) = Θ(n^c). This is Case 2: T(n) = Θ(n^c · log n) = Θ(n⁰ · log n) = Θ(log n).
- *Why C is incorrect:* Case 1 applies when f(n) grows slower than n^c. Here f(n) = Θ(n^c) — exactly equal — which is Case 2, not Case 1.
- *Why D is incorrect:* a=2, b=2 describes merge sort, not binary search. O(n) from the Master Theorem with these values would apply to a different case.

---

### Question 7

In the counting inversions algorithm, when a right-half element `right[j]` is placed before remaining left-half elements, the inversion count increases by `len(left) - i`. Why is this the correct count?

- A) Because `i` elements in the left half have already been processed and cannot form inversions
- B) All remaining left-half elements (indices i through end) are greater than `right[j]` — since left is sorted, every one of them forms an inversion with `right[j]`
- C) `len(left) - i` counts the total number of elements in both halves
- D) It counts the inversions between the two halves that were already discovered in previous recursive calls

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Elements already placed (indices 0..i-1) have already been accounted for. The count `len(left) - i` counts the newly discovered inversions from `right[j]` with unplaced left elements.
- *Why B is correct:* The left half is sorted. If `left[i] > right[j]` (causing us to place `right[j]` first), then `left[i+1] > left[i] > right[j]`, `left[i+2] > right[j]`, ..., all the way to `left[len(left)-1] > right[j]`. There are exactly `len(left) - i` such elements. Each forms an inversion pair with `right[j]` because they have smaller index in the original array (they came from the left half) but larger value.
- *Why C is incorrect:* `len(left) - i` counts remaining elements in the left half only, not in both halves.
- *Why D is incorrect:* Previous recursive calls counted inversions within each half. The merge step counts cross-inversions between the two halves — new information discovered during the combine phase.

---

### Question 8

Search in Rotated Sorted Array (LeetCode #33) requires binary search on a rotated array. The key insight is:

- A) The array must be un-rotated before applying binary search — sort first, then search
- B) At any `mid` point, exactly one half of the array is fully sorted — use the sorted half to determine which side contains the target
- C) Binary search cannot work on rotated arrays — use linear search
- D) The rotation point must be found first with O(n) scan, then binary search the correct half

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Sorting first costs O(n log n), making the search O(n log n) total — wasteful when O(log n) is achievable.
- *Why B is correct:* In a rotated sorted array, when `mid` splits the array, one of the two halves (left or right of `mid`) is guaranteed to be fully sorted. Check if `nums[left] <= nums[mid]` — if True, the left half is sorted. If the target is within the sorted half's range, search there; otherwise search the other half. This maintains O(log n) by halving the search space each step.
- *Why C is incorrect:* Binary search can work on rotated arrays with the modification described in B. O(log n) is achievable.
- *Why D is incorrect:* Finding the rotation point with O(n) scan defeats the purpose. A single binary search pass simultaneously finds the rotation structure and the target.

---

### Question 9

What is the space complexity of merge sort?

- A) O(1) — sorting is done in place
- B) O(log n) — only the recursion stack is used
- C) O(n) — the merge step requires an auxiliary array proportional to input size
- D) O(n log n) — a new array is allocated at every level of the recursion tree

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Merge sort is not in-place. The `merge` function creates a new `result` list for each merge, requiring extra space proportional to the number of elements being merged.
- *Why B is incorrect:* O(log n) describes only the recursion stack depth. The dominant space cost is the auxiliary arrays created during merging.
- *Why C is correct:* At any given time, the merge step at the top level creates one array of size n. Lower levels create smaller arrays, but those are discarded before the top-level merge begins. The peak extra space is O(n) for the final merge of two n/2 arrays.
- *Why D is incorrect:* O(n log n) would require keeping all intermediate arrays alive simultaneously. In practice, each level's temporary arrays are garbage-collected before the next level allocates. The peak usage is O(n), not O(n log n).

---

### Question 10

The binary search on answer template finds the minimum capacity for the ship packages problem. The search range is `[max(weights), sum(weights)]`. Why are these the correct bounds?

- A) `max(weights)` is the answer when the ship has only one day; `sum(weights)` is the answer when each package gets its own day
- B) `max(weights)` is the minimum possible capacity (a single package must fit); `sum(weights)` is the maximum needed capacity (everything ships in one day)
- C) These bounds minimize the number of binary search iterations
- D) The bounds represent the number of packages and the total weight, used as array indices

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `max(weights)` represents the minimum capacity, not the answer for one day. The answer for one day is `sum(weights)`, but framing it as "one day" vs "one package per day" confuses the bound semantics.
- *Why B is correct:* The ship's capacity must be at least `max(weights)` — otherwise the heaviest single package cannot be loaded on any day. The capacity never needs to exceed `sum(weights)` — at that capacity, all packages fit in one trip. The answer lies somewhere in this range: the minimum capacity where `feasible(capacity)` is True.
- *Why C is incorrect:* The bounds are chosen for correctness, not efficiency. A tighter range would reduce iterations by a constant factor, but the bounds must contain the correct answer.
- *Why D is incorrect:* The bounds are weight values (capacity units), not array indices or package counts. Using them as indices would make no sense in context.
