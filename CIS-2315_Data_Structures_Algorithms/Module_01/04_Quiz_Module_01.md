# Quiz: Module 01 — Big-O Notation and Complexity Analysis

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the time complexity of the following code?

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(2n)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n) would require only a single loop iterating n times. Two nested loops each running n times produce n × n = n² total iterations.
- *Why B is incorrect:* O(n log n) arises when one loop runs n times and an inner process halves the remaining work — like merge sort. Two flat nested loops do not produce logarithmic structure.
- *Why C is correct:* The outer loop runs n times; for each outer iteration, the inner loop runs n times. Total print statements = n × n = n². The complexity is O(n²). This is the standard nested-loop quadratic pattern.
- *Why D is incorrect:* O(2n) would result from two separate sequential loops — each running n times independently. That simplifies to O(n), not O(n²). Nested loops multiply; sequential loops add.

---

### Question 2

Which best defines amortized analysis?

- A) Calculating average-case complexity by assuming all inputs are equally likely
- B) Distributing the total cost of a sequence of operations evenly, giving average cost per operation even when individual operations vary widely
- C) Establishing a lower bound on any solution to a problem by proving no algorithm can do better
- D) Measuring heap memory used by recursive calls beyond the input data

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That describes average-case analysis, which considers probability distributions over inputs. Amortized analysis does not assume anything about input distribution — it analyzes a specific sequence of operations.
- *Why B is correct:* Amortized analysis spreads the total cost of n operations across all n, giving a per-operation average. The classic example is dynamic array append: most appends are O(1), occasional resizes are O(n), but total cost over n appends is O(n), so amortized cost per append is O(1).
- *Why C is incorrect:* That describes lower-bound proofs using Omega (Ω) notation — proving a problem's inherent difficulty. It is a separate technique unrelated to amortized analysis.
- *Why D is incorrect:* That describes space complexity of recursive call stacks — a separate concept. Amortized analysis is about time cost per operation in a sequence, not memory.

---

### Question 3

An algorithm's runtime doubles each time the input size increases by one element. What is its time complexity?

- A) O(n²)
- B) O(n log n)
- C) O(2ⁿ)
- D) O(log n)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n²) grows polynomially. If n doubles, O(n²) quadruples — not doubles-per-element. Polynomial growth is much slower than exponential growth for large n.
- *Why B is incorrect:* O(n log n) grows only slightly faster than linear. It does not double for every single element added.
- *Why C is correct:* If T(n) = 2^n, then T(n+1) = 2^(n+1) = 2 × 2^n — exactly double for each additional element. This is the defining characteristic of exponential complexity. Naive recursive Fibonacci without memoization exhibits this growth.
- *Why D is incorrect:* O(log n) decreases in growth rate as n grows — each doubling of n adds only one more step. O(log n) is the opposite pattern from doubling per element.

---

### Question 4

A recursive algorithm has recurrence T(n) = 2T(n/2) + O(n). What is its time complexity?

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n) would require T(n) = T(n/2) + O(1) — divide in half with constant work per level. Here the merge/combine step costs O(n) at every level, not O(1).
- *Why B is correct:* T(n) = 2T(n/2) + O(n) is the recurrence for merge sort. By the Master Theorem (Case 2: a=2, b=2, log_b(a)=1 equals the degree of f(n)=n), the result is O(n log n). Intuitively: log n levels of recursion, each doing O(n) total work = O(n log n).
- *Why C is incorrect:* O(n²) arises from algorithms like insertion sort with T(n) = T(n-1) + O(n), where the work per level grows linearly. Here the problem halves each level, which is far more efficient.
- *Why D is incorrect:* O(log n) arises from T(n) = T(n/2) + O(1) — halving with constant work. The O(n) merge step at every level prevents this.

---

### Question 5

Which correctly orders these complexity classes from fastest to slowest for large n?

- A) O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- B) O(log n) < O(1) < O(n) < O(n²) < O(n log n) < O(2ⁿ)
- C) O(1) < O(n) < O(log n) < O(n log n) < O(2ⁿ) < O(n²)
- D) O(1) < O(log n) < O(n log n) < O(n) < O(n²) < O(2ⁿ)

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* This is the standard ordering every interviewer expects: constant < logarithmic < linear < log-linear < quadratic < exponential. Memorize this hierarchy — it will be used in every module of the course.
- *Why B is incorrect:* O(1) is always faster than O(log n). For any n > 1, O(1) uses fewer operations. Swapping them is wrong.
- *Why C is incorrect:* O(log n) grows more slowly than O(n). `log₂(1,000,000)` = 20 steps versus 1,000,000 steps for O(n). Placing O(n) before O(log n) inverts their correct order.
- *Why D is incorrect:* O(n) grows more slowly than O(n log n). An O(n) algorithm on n=1,000,000 does 1,000,000 operations; an O(n log n) algorithm does roughly 20,000,000. Placing O(n log n) before O(n) inverts their order.

---

### Question 6

What is the space complexity of the following function?

```python
def find_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item in seen:
            result.append(item)
        else:
            seen.add(item)
    return result
```

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(1) space means a fixed amount of memory regardless of input size. The `seen` set and `result` list both grow with input. In the worst case (all duplicates), `seen` holds n/2 elements and `result` holds n/2 elements — both proportional to n.
- *Why B is incorrect:* O(log n) space would require a structure that grows logarithmically — like the call stack depth of binary search. This function uses a flat set and list, both of which can grow linearly.
- *Why C is correct:* Both `seen` and `result` can hold up to O(n) elements in the worst case. The set holds each unique element seen so far (up to n), and the result list holds each duplicate found (up to n/2). The dominant term is O(n).
- *Why D is incorrect:* O(n²) would require a structure like a 2D matrix of size n×n. No such structure exists here. The set and list each grow linearly.

---

### Question 7

A developer notices their solution for a LeetCode problem runs in O(n²) time but O(1) space. They want to optimize it to O(n) time. What will most likely be required?

- A) Adding a second nested loop to process elements more efficiently
- B) Sorting the input first, which takes O(n log n) but enables O(1) passes
- C) Using a hash map or hash set to enable O(1) lookups, increasing space to O(n)
- D) Using recursion instead of iteration, which reduces the time complexity

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Adding a second nested loop makes the problem worse — more nesting means higher time complexity, not lower.
- *Why B is incorrect:* Sorting takes O(n log n) and enables subsequent O(n) passes, giving O(n log n) total. This is an improvement over O(n²), but it does not achieve O(n) and it uses O(log n) or O(n) extra space for the sort.
- *Why C is correct:* The classic optimization from O(n²) to O(n) is the time-space tradeoff: replace the inner loop (which searches for a value in O(n)) with a hash map lookup (O(1) amortized). This reduces the nested loop to a single pass. The cost is O(n) extra memory. This pattern appears in Two Sum, Group Anagrams, Contains Duplicate, and dozens of other LeetCode problems.
- *Why D is incorrect:* Replacing iteration with recursion does not change the algorithmic complexity — a recursive O(n²) algorithm is still O(n²). Recursion is a control flow mechanism, not a complexity optimizer.

---

### Question 8

What is the time complexity of `list.append()` in Python?

- A) O(n) — elements must be shifted to make room
- B) O(log n) — the list uses a tree structure internally
- C) O(1) — always exactly one operation
- D) O(1) amortized — usually O(1), occasionally O(n) for resizing

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Elements do not need to be shifted for append. Shifting is required for insertion at an arbitrary index (`list.insert(i, val)`), which is O(n). Append adds to the end of the backing array.
- *Why B is incorrect:* Python's `list` is a dynamic array, not a tree. It uses a contiguous block of memory with a capacity counter. There is no logarithmic structure.
- *Why C is incorrect:* Most appends are O(1), but when the backing array is full, Python must allocate a new (larger) array and copy all existing elements — an O(n) operation. Calling it always O(1) ignores the occasional resize cost.
- *Why D is correct:* Python's list doubles its capacity when full. The resize costs O(n) but happens exponentially rarely. Over n appends, total resize work is 1+2+4+...+n = 2n — so the average cost per append is O(1). This is amortized constant time. Interviewers expect you to say "O(1) amortized" when asked about append.

---

### Question 9

Which code achieves O(n) time and O(1) extra space for finding the maximum element in an unsorted array?

- A) Sort the array, then return the last element
- B) Use a nested loop to compare every pair of elements
- C) Iterate once through the array, tracking the running maximum
- D) Build a max-heap from the array, then extract the top element

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Sorting takes O(n log n) time and O(log n) or O(n) space depending on the algorithm. This is more expensive than necessary for finding a maximum.
- *Why B is incorrect:* Comparing every pair is O(n²) — far more expensive than needed. For each element, comparing it to all others is redundant once you track the running maximum.
- *Why C is correct:* A single linear pass with one variable `max_val` finds the maximum in O(n) time using O(1) extra space. This is the optimal solution — you must look at every element at least once (Ω(n) lower bound), and one variable is the minimum space.
- *Why D is incorrect:* Building a max-heap is O(n) time, but it requires O(n) extra space for the heap structure. The single-pass approach achieves the same time complexity with O(1) space.

---

### Question 10

A function makes exactly one recursive call on half the input and does O(1) work at each call. What is its time and space complexity?

- A) Time O(n), Space O(1)
- B) Time O(log n), Space O(log n)
- C) Time O(log n), Space O(1)
- D) Time O(n), Space O(log n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n) time would require visiting every element. This function halves the input at each step — it reaches the base case after log n calls, not n calls.
- *Why B is correct:* Time: the recurrence T(n) = T(n/2) + O(1) resolves to O(log n) — log₂(n) recursive calls before reaching the base case. Space: each call adds one frame to the call stack, and there are log n calls active simultaneously at the deepest point. Even though no extra data structures are used, the recursive call stack consumes O(log n) auxiliary space.
- *Why C is incorrect:* The time complexity is correct (O(log n)), but the space is wrong. Recursion always uses stack space proportional to the maximum depth. With log n levels of recursion, space is O(log n), not O(1). O(1) space would require an iterative implementation.
- *Why D is incorrect:* O(n) time is wrong for the same reason as A — the function halves its input at every call and reaches the base case after log n steps.
