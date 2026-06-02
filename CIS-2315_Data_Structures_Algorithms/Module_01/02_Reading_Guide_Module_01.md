# Reading Guide: Module 01 — Big-O Notation and Complexity Analysis

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Big-O notation is the vocabulary of algorithm analysis. Before you can discuss whether your solution is "good enough," you must be able to precisely describe how its runtime and memory usage scale with input size. Every technical interviewer at every company expects fluency with this language. Module 01 establishes the framework; every subsequent module applies it.

---

## 1. What Big-O Notation Measures

Big-O describes the **upper bound** on an algorithm's growth rate as input size n approaches infinity. It answers: if I make the input arbitrarily large, how does my resource usage grow?

Key principles:

- **Drop constants:** O(3n) → O(n). Constants depend on hardware and implementation details, not algorithmic structure.
- **Drop lower-order terms:** O(n² + n) → O(n²). At large n, the dominant term overwhelms smaller ones.
- **Worst-case by default:** Unless specified otherwise, Big-O refers to the worst-case scenario — the input that maximizes cost.

### Related Notations

| Notation | Meaning | Use |
|---|---|---|
| O(f(n)) | Upper bound | Worst-case guarantee |
| Ω(f(n)) | Lower bound | Best-case guarantee |
| Θ(f(n)) | Tight bound | Both upper and lower match |

For interviews, O (Big-O) is what interviewers mean when they ask for complexity.

---

## 2. Complexity Classes — Ordered Fastest to Slowest

```text
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

| Class | Name | Example |
|---|---|---|
| O(1) | Constant | Array index access, hash table lookup |
| O(log n) | Logarithmic | Binary search, balanced tree operations |
| O(n) | Linear | Single-pass array scan, linear search |
| O(n log n) | Log-linear | Merge sort, heap sort, Python `sorted()` |
| O(n²) | Quadratic | Nested loops, bubble sort, insertion sort |
| O(n³) | Cubic | Triple nested loops, naive matrix multiplication |
| O(2ⁿ) | Exponential | Recursive Fibonacci (no memo), subset enumeration |
| O(n!) | Factorial | Permutation generation, brute-force TSP |

**Interview rule:** Any solution worse than O(n²) for n > 10,000 will likely time out. O(n log n) or better is the target for most problems.

---

## 3. Reading Code for Complexity

### Single Loop — O(n)

```python
for item in arr:          # iterates n times
    process(item)         # O(1) per iteration
# Total: O(n)
```

### Nested Loops — O(n²)

```python
for i in range(len(arr)):
    for j in range(len(arr)):   # n × n iterations
        compare(arr[i], arr[j])
# Total: O(n²)
```

### Loop Halving Each Iteration — O(log n)

```python
low, high = 0, len(arr) - 1
while low <= high:            # halves search space each step
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
```

Starting from n, takes log₂(n) iterations to reach 1. Binary search is O(log n).

### O(n) Work at Each of O(log n) Levels — O(n log n)

Merge sort: splits the array O(log n) times, each level doing O(n) total merge work.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])     # T(n/2)
    right = merge_sort(arr[mid:])     # T(n/2)
    return merge(left, right)         # O(n) merge
# T(n) = 2T(n/2) + O(n)  →  O(n log n)
```

### Constant Inner Loop — Still O(n)

```python
for i in range(n):
    for j in range(10):   # constant 10 iterations, not n
        work()
# Total: O(10n) = O(n)
```

### Two Separate Passes — O(n), Not O(2n)

```python
for item in arr:     # pass 1
    process(item)
for item in arr:     # pass 2
    verify(item)
# Total: O(2n) = O(n)
```

---

## 4. Space Complexity

Space complexity measures additional memory usage as a function of input size. **Auxiliary space** excludes the input itself and counts only extra structures created by the algorithm.

### O(1) Auxiliary Space

```python
def find_max(arr):
    max_val = arr[0]       # one variable
    for item in arr:
        if item > max_val:
            max_val = item
    return max_val
# Space: O(1) — only one scalar variable
```

### O(n) Space — Hash Set or Map

```python
def has_duplicate(arr):
    seen = set()           # up to n elements
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False
# Space: O(n) — set grows with input
```

### O(n) Recursive Call Stack

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
# n active stack frames simultaneously → O(n) space
```

Even with no explicit data structures, deep recursion uses O(n) stack space.

### Common Space Complexities

| Operation | Space |
|---|---|
| Variables, pointers | O(1) |
| Copy of input array | O(n) |
| Hash map / set | O(n) |
| Recursion depth d | O(d) |
| 2D matrix of input | O(n²) |

---

## 5. Amortized Analysis

Amortized analysis gives the **average cost per operation** over a sequence of operations, even when individual operations vary in cost.

Dynamic array append example: Python's `list.append()` is O(1) amortized:

- Most appends copy one element to an existing slot: O(1).
- Occasionally, the backing array is full and must double in size: O(n).
- Resizes happen at sizes 1, 2, 4, 8, ..., n — total copies = 1+2+4+...+n = 2n.
- Spread over n appends: 2n / n = **O(1) amortized** per append.

This is why Python's `list.append()` is considered O(1) even though it sometimes takes O(n).

---

## 6. Recursive Complexity — Master Theorem

For divide-and-conquer algorithms with recurrence T(n) = aT(n/b) + f(n):

The two patterns you need for interviews:

| Recurrence | Example | Complexity |
|---|---|---|
| T(n) = T(n/2) + O(1) | Binary search | O(log n) |
| T(n) = 2T(n/2) + O(n) | Merge sort | O(n log n) |
| T(n) = T(n-1) + O(1) | Tail recursion, factorial | O(n) |
| T(n) = 2T(n-1) + O(1) | Naive Fibonacci | O(2ⁿ) |

---

## 7. The Time-Space Tradeoff

Many interview problems have a slow but space-efficient solution and a fast but memory-intensive solution. Recognizing and making this tradeoff deliberately is a key interview skill.

Two Sum (LeetCode #1) illustrates this tradeoff:

```python
# Brute force: O(n²) time, O(1) space
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimized: O(n) time, O(n) space
def two_sum_hash(nums, target):
    seen = {}                        # O(n) space
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

We spend O(n) memory to reduce time from O(n²) to O(n). In interviews, this optimization is almost always worth making.

---

## 8. Interview Exam Tips

1. **State complexity unprompted** — after every solution, say "this is O(n) time and O(n) space because..." before the interviewer asks. This demonstrates senior-level thinking.

2. **Identify the dominant term** — for a function with an O(n²) loop and an O(n) loop, the overall complexity is O(n²). Drop the smaller term.

3. **Count loops, not lines** — complexity comes from loops and recursive calls, not from the number of lines.

4. **A loop of constant size is O(1)** — `for i in range(10)` is a constant factor, not O(n).

5. **Know auxiliary space vs total space** — interviewers often ask "what is the space complexity?" and mean extra memory beyond the input.

6. **Recursion uses stack space** — every recursive call adds O(1) to the stack. Depth d means O(d) space.

7. **Amortized O(1) for append** — Python `list.append()` and dict operations are O(1) amortized. State this correctly.

8. **The Big-O table** — memorize: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ). You will be asked to order them.

9. **Practical limit** — for n = 10⁵ (100,000), O(n log n) is fine; O(n²) is 10¹⁰ operations and will time out on LeetCode.

10. **Space-time tradeoff** — using O(n) extra memory (a hash map) to reduce time from O(n²) to O(n) is almost always the right move in interviews.

---

## 9. Study Checklist

- [ ] Watch the Module 01 video lecture by Professor Nash.
- [ ] Read the Big-O Cheat Sheet and memorize the complexity class ordering.
- [ ] Watch the NeetCode Big-O video.
- [ ] Write out the time and space complexity of 10 code snippets from memory.
- [ ] Complete the Module 01 Lab — benchmark O(n) vs O(n²) and annotate a LeetCode solution.
- [ ] Complete the Module 01 Quiz.
