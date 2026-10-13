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

---

### Question 11

**Each question is worth 5 points.**

What does Theta notation Θ(f(n)) signify, as distinct from Big-O notation O(f(n))?

- A) Θ(f(n)) is a stricter upper bound than O(f(n)) because it excludes constant factors
- B) Θ(f(n)) means the algorithm's growth rate is bounded both above and below by f(n) — it is a tight bound
- C) Θ(f(n)) describes the best-case runtime, while O(f(n)) describes worst-case
- D) Θ(f(n)) and O(f(n)) are interchangeable; both denote upper bounds

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both Θ and O drop constant factors. The distinction is not about strictness of constants but about whether the bound is one-sided (upper only, O) or two-sided (upper and lower, Θ).
- *Why B is correct:* Θ(f(n)) means there exist positive constants c₁, c₂, and n₀ such that c₁·f(n) ≤ T(n) ≤ c₂·f(n) for all n ≥ n₀. Both the upper bound (O) and lower bound (Ω) match f(n). This is the tight or exact asymptotic bound.
- *Why C is incorrect:* Best-case and worst-case refer to input scenarios. Θ describes the asymptotic growth for a specific case — it does not distinguish between best and worst inputs.
- *Why D is incorrect:* O(f(n)) is only an upper bound — the algorithm could run faster. Θ(f(n)) is strictly tighter because it also guarantees the algorithm cannot run asymptotically faster than f(n).

---

### Question 12

Consider the following code. What is its time complexity?

```python
def process(arr):
    n = len(arr)
    i = 1
    while i < n:
        for j in range(n):
            print(arr[i], arr[j])
        i *= 2
```

- A) O(n²)
- B) O(n log n)
- C) O(log n)
- D) O(n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n²) would require the outer loop to run n times. Here the outer loop runs only log₂(n) times because `i` doubles each iteration (1, 2, 4, 8, … until i ≥ n).
- *Why B is correct:* The outer `while` loop runs log₂(n) times (doubling `i` each time). For each outer iteration, the inner `for` loop runs n times. Total iterations = n × log n = O(n log n). This is the hallmark pattern of O(n log n): one loop that halves/doubles and one linear loop nested inside.
- *Why C is incorrect:* O(log n) would require only the outer loop with no inner work. The O(n) inner `for` loop multiplies the log factor by n.
- *Why D is incorrect:* O(n) would require a single linear pass. The nested structure multiplies costs — log n outer iterations each doing n work yields n log n total.

---

### Question 13

Which of the following recurrences corresponds to an O(n²) algorithm?

- A) T(n) = T(n/2) + O(n)
- B) T(n) = T(n − 1) + O(n)
- C) T(n) = 2T(n/2) + O(n)
- D) T(n) = T(n − 1) + O(1)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* T(n) = T(n/2) + O(n) solves to O(n) by the Master Theorem (Case 3 or geometric series: n + n/2 + n/4 + … ≈ 2n). This is not quadratic.
- *Why B is correct:* T(n) = T(n−1) + O(n) expands as: T(n) = O(n) + O(n−1) + O(n−2) + … + O(1) = O(n(n+1)/2) = O(n²). This is the recurrence for selection sort or insertion sort's worst case — reduce by 1 each level, do O(n) work each level.
- *Why C is incorrect:* T(n) = 2T(n/2) + O(n) is the merge sort recurrence, which solves to O(n log n) by the Master Theorem.
- *Why D is incorrect:* T(n) = T(n−1) + O(1) expands as n additions of O(1) = O(n). This is linear — e.g., iterative factorial or tail-recursive sum.

---

### Question 14

A function processes an n×n matrix using three nested loops each from 0 to n. What is the time complexity?

- A) O(n²)
- B) O(n³)
- C) O(3n)
- D) O(n log n)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n²) is produced by two nested loops each running 0 to n. A third nested loop adds another factor of n, making it n × n × n = n³.
- *Why B is correct:* Three nested loops each iterating n times produce n³ total iterations. This is O(n³) — cubic complexity. The classic example is naive matrix multiplication.
- *Why C is incorrect:* O(3n) = O(n). Three sequential (not nested) loops over n elements would yield 3n total operations, which simplifies to O(n). Nesting multiplies; sequencing adds.
- *Why D is incorrect:* O(n log n) requires a halving structure inside a linear loop (like merge sort). Three flat nested loops produce no such logarithmic reduction.

---

### Question 15

What is the time complexity of looking up a key in a Python dictionary (`d[key]`) in the average case?

- A) O(n) — the dictionary scans all keys linearly
- B) O(log n) — the dictionary uses a balanced BST internally
- C) O(1) amortized — hash tables provide constant-time average lookup
- D) O(n log n) — hashing requires sorting keys first

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python's `dict` is a hash table, not a linked list or array. A hash table computes the bucket index from the key's hash value in O(1), then checks one or a few entries — not all n entries.
- *Why B is incorrect:* Python's `dict` uses open-addressing hash tables, not balanced BSTs. BST lookup is O(log n); hash table lookup is O(1) average.
- *Why C is correct:* A hash table computes `hash(key) % capacity` to find the bucket in O(1). With a good hash function and low load factor, collisions are rare and lookup remains O(1) amortized. Python's dict is highly optimized and achieves near-constant lookup even for large n. Worst case (all keys collide) is O(n), but this is negligible in practice.
- *Why D is incorrect:* Hash functions compute a numeric value from a key in O(1) (for fixed-size keys). No sorting is involved. Sorting is an entirely separate operation with O(n log n) complexity.

---

### Question 16

An algorithm has two phases: Phase 1 runs in O(n log n) and Phase 2 runs in O(n²). What is the overall time complexity?

- A) O(n log n + n²) = O(n² + n log n)
- B) O(n²) — the dominant term rules
- C) O(n³ log n) — the phases multiply
- D) O(2n²) — they add because they are sequential

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Writing O(n log n + n²) is technically valid but not simplified. In asymptotic analysis, we drop lower-order terms. Since n² grows faster than n log n for all n > 1, the sum simplifies to O(n²).
- *Why B is correct:* When sequential phases have different complexities, the overall complexity is the maximum (dominant) term. O(n²) dominates O(n log n) because n²/( n log n) = n/log n → ∞ as n → ∞. The smaller term becomes negligible at scale.
- *Why C is incorrect:* Sequential phases add their costs, not multiply them. Multiplication applies to nested operations. Running one O(n log n) algorithm followed by one O(n²) algorithm costs O(n log n) + O(n²), not O(n³ log n).
- *Why D is incorrect:* O(2n²) simplifies to O(n²). The coefficient 2 is a constant factor and is dropped per Big-O rules. Even if both phases were O(n²), the sum would still be O(n²), not O(2n²).

---

### Question 17

What is the space complexity of iterative binary search on a sorted array?

- A) O(n) — the array must be copied
- B) O(log n) — the search range halves each iteration
- C) O(1) — only a fixed number of pointer variables are used
- D) O(n log n) — sorting the array first is required

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Iterative binary search does not copy the input array. It operates in-place using two index variables (`low` and `high`). The array is already given as input and is not counted toward auxiliary space.
- *Why B is incorrect:* O(log n) space applies to recursive binary search — each recursive call adds a frame to the call stack, and there are log n levels. The iterative version uses a loop instead of recursion, eliminating stack frames.
- *Why C is correct:* Iterative binary search uses exactly three variables: `low`, `high`, and `mid`. These are scalar integers regardless of n. O(1) auxiliary space — this is one of the key advantages of the iterative implementation over the recursive one.
- *Why D is incorrect:* Binary search requires the array to already be sorted. If sorting is needed, it adds O(n log n) time, but this question asks about the binary search algorithm itself, which assumes a sorted input.

---

### Question 18

Which scenario best illustrates an O(n!) time complexity?

- A) Searching for an element in a sorted array using binary search
- B) Generating all possible orderings (permutations) of n distinct elements
- C) Merging two sorted arrays of size n/2 each
- D) Finding the nth Fibonacci number using dynamic programming

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Binary search on a sorted array is O(log n) — it halves the search space each step.
- *Why B is correct:* The number of permutations of n distinct elements is n! = n × (n−1) × (n−2) × … × 1. Any algorithm that enumerates all permutations must generate n! outputs and therefore runs in O(n!) time. This is the slowest complexity class in common use, appearing in brute-force solutions to the Traveling Salesman Problem and similar combinatorial problems.
- *Why C is incorrect:* Merging two sorted arrays of total size n is O(n) — a single linear pass comparing front elements of each array.
- *Why D is incorrect:* Dynamic programming computes Fibonacci by storing previously computed values. The time complexity is O(n) (n subproblems, each O(1) with memoization) and space is O(n) for the memo table.

---

### Question 19

A developer claims their algorithm is O(n) time. Under what condition would this claim be misleading even if technically correct?

- A) The algorithm has a very large constant factor, such as 10⁹ × n operations
- B) The algorithm uses O(n) space, which is always worse than O(1) space
- C) The algorithm is only O(n) in the best case but O(n²) in the worst case
- D) The algorithm sorts its input before processing, adding hidden O(n log n) cost

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A large constant factor is a valid concern for practical performance, but it does not make the O(n) claim technically wrong. The constant is dropped in Big-O analysis because it is hardware/implementation dependent. A truly large constant might matter in practice, but option C is a more direct example of a technically misleading (though not incorrect) claim.
- *Why B is incorrect:* O(n) space is not "always worse" than O(1) space — it depends on context. The time-space tradeoff often makes O(n) space acceptable. This statement is a false universal claim.
- *Why C is correct:* Big-O by convention refers to worst-case unless otherwise specified. If an algorithm is O(n) best-case but O(n²) worst-case, claiming "O(n)" without qualification is misleading. The interviewer hears "worst-case O(n)" when none was stated. Always clarify: "O(n) average case, O(n²) worst case."
- *Why D is incorrect:* If sorting is part of the algorithm, its O(n log n) cost must be included in the overall analysis. An algorithm that sorts first is O(n log n), not O(n). This would be an incorrect claim, not merely a misleading one — the sorting cost cannot be hidden.

---

### Question 20

What is the time complexity of the following Python code, where `n = len(arr)` and `arr` contains integers?

```python
def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False
```

- A) O(n²) — for each element, we search the entire set
- B) O(n log n) — set membership uses a sorted structure
- C) O(n) — single pass; set lookup and insert are O(1) amortized
- D) O(1) — the function returns as soon as a pair is found

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Set membership (`in`) on a Python `set` is O(1) amortized — not O(n). Python's `set` is a hash table. The loop runs n times, each iteration doing O(1) set operations, yielding O(n) total.
- *Why B is incorrect:* Python's `set` is a hash table, not a balanced BST or sorted structure. BST membership is O(log n); hash set membership is O(1) amortized. There is no sorting happening here.
- *Why C is correct:* The `for` loop iterates n times. Each iteration does two O(1) amortized hash table operations: `target - num in seen` (lookup) and `seen.add(num)` (insert). Total time = n × O(1) = O(n). This is the standard hash-set pattern for the "pair with target sum" problem.
- *Why D is incorrect:* O(1) would mean the function takes a constant amount of time regardless of input size. In the worst case (no pair exists), the loop runs all n iterations. The early-return optimizes the best case, but Big-O refers to worst-case unless stated otherwise.
