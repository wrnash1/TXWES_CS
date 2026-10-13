# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 01 — Big-O Notation and Complexity Analysis

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - This module establishes the language every technical interview uses. Students who cannot express complexity cannot pass coding screens, even if their code is correct.
> - The key mental models: (1) Big-O as "what happens as input grows large"; (2) dropping constants and lower-order terms; (3) the complexity hierarchy table; (4) reading loops and recursion to determine class.
> - Show real Python timing with `time.perf_counter()` — seeing 600ms vs 10ms for the same logical problem is memorable.
> - Do NOT go deep into formal proofs or Master Theorem derivation in the video — save that for the reading guide. Keep the video focused on pattern recognition.
> - The space complexity section is often undertaught. Give it equal time — interviewers ask about it as often as time complexity.

---

## [00:00 – 02:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 01 | Big-O Notation and Complexity Analysis | CIS-2315"]**

"Welcome to CIS-2315 — Data Structures and Algorithms. This course is built around one goal: preparing you for the technical coding interview. Whether you are targeting an internship, a new grad position, or a career change into software engineering, the technical interview is the gating challenge. Every major technology company uses the same format: here is a problem, solve it in 30 to 45 minutes, and explain your reasoning.

This first module gives you the vocabulary that the entire course is built on. Big-O notation is how you describe the quality of your solution. It is not just a grade — it is the language you use to communicate with your interviewer. When you say 'this runs in O(n log n) time and O(n) space,' you are demonstrating that you understand not just whether your code works, but how it will perform at scale.

Let us get into it."

---

## [02:00 – 06:30] Part 1 — What Big-O Actually Means

**[SHOW SLIDE: "What Big-O Measures"]**

"Big-O notation describes how an algorithm's resource consumption — time or memory — grows as the input size gets large. We always express it as a function of n, where n is the size of the input.

The key insight is that we care about the trend at large scale. We drop constant factors and lower-order terms. If an algorithm does 3n + 100 operations, we say it is O(n) — because as n gets large, the 3 and the 100 become irrelevant compared to n itself.

**[DEMO — Python timing]**

Let me show you this concretely.

```python
import time

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

def constant_work(n):
    return n * n + 3 * n + 100   # same work regardless of n

sizes = [1000, 10000, 100000, 1000000]

for n in sizes:
    arr = list(range(n))
    target = -1   # worst case — not in list
    start = time.perf_counter()
    linear_search(arr, target)
    elapsed = time.perf_counter() - start
    print(f'n={n:>8}: {elapsed*1000:.3f}ms')
```

Run this and observe: when n goes from 1,000 to 1,000,000 — a factor of 1,000 — the time also grows by roughly a factor of 1,000. That is linear behavior. That is O(n).

[PAUSE]

Now contrast that with constant time:

```python
def get_first(arr):
    return arr[0]   # always one operation regardless of array size
```

Whether the array has 10 elements or 10 million, this takes the same time. That is O(1).

**The question Big-O answers:** if I double the input, what happens to the resource consumption? Doubles? That is O(n). Quadruples? That is O(n²). Barely changes? That is O(log n) or O(1)."

---

## [06:30 – 10:30] Part 2 — The Complexity Hierarchy

**[SHOW SLIDE: "Complexity Classes — Fastest to Slowest"]**

"There are a handful of complexity classes you need to know cold. Let me put them in order from fastest to slowest:

O(1) — Constant. Array index access, hash table lookup, stack push/pop.
O(log n) — Logarithmic. Binary search, operations on balanced trees.
O(n) — Linear. One pass through an array. Linear search.
O(n log n) — Log-linear. Efficient sorting: merge sort, heap sort, Python's built-in `sorted()`.
O(n²) — Quadratic. Nested loops: bubble sort, naive duplicate detection.
O(2ⁿ) — Exponential. Brute-force recursive solutions: Fibonacci without memoization, subset enumeration.
O(n!) — Factorial. Permutation generation: brute-force traveling salesman.

**[DEMO — benchmarking O(n) vs O(n²)]**

```python
import time

def has_duplicate_n2(arr):
    # O(n²) — check every pair
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def has_duplicate_n(arr):
    # O(n) — use a set
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False

import random
data = list(range(5000))   # no duplicates — worst case
random.shuffle(data)

for fn, label in [(has_duplicate_n2, 'O(n²)'), (has_duplicate_n, 'O(n)')]:
    start = time.perf_counter()
    fn(data)
    ms = (time.perf_counter() - start) * 1000
    print(f'{label}: {ms:.2f}ms')
```

For n=5000, O(n²) typically takes 20–40ms while O(n) takes under 1ms. Scale that to n=100,000 and O(n²) becomes seconds while O(n) stays under 10ms.

[PAUSE]

**The rule interviewers apply:** a solution that is worse than O(n²) for large inputs will typically fail the time limit on LeetCode and HackerRank, and will be flagged in a live interview. O(n log n) or better is the goal for most problems."

---

## [10:30 – 14:00] Part 3 — Reading Code for Complexity

**[SHOW SLIDE: "How to Read Code for Complexity"]**

"The practical skill is reading code — yours or someone else's — and immediately knowing its complexity class. Here are the patterns.

**Single loop:** O(n)

```python
for item in arr:
    process(item)   # O(1) work per iteration → O(n) total
```

**Nested loops over same input:** O(n²)

```python
for i in range(len(arr)):
    for j in range(len(arr)):
        compare(arr[i], arr[j])   # n² pairs → O(n²)
```

**Loop that halves each iteration:** O(log n)

```python
low, high = 0, len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
```

Each iteration eliminates half the remaining search space. Starting from n, it takes log₂(n) steps to reach 1. Binary search is O(log n).

[PAUSE]

**A loop inside binary search:** O(n log n)

If you do O(n) work at each level of a log n recursion, or run binary search n times, you get O(n log n). This is the complexity of merge sort and heap sort.

**Dropping constants and lower-order terms:**

```python
for i in range(n):          # O(n)
    work(i)
for i in range(n):          # O(n) again
    more_work(i)
for i in range(n):          # O(n) again
    for j in range(10):     # constant inner loop — still O(n) overall
        constant_work()
```

Three O(n) sections: total is O(3n) = O(n). The constant 3 is dropped. The inner loop of 10 is a constant multiplier — absorbed into O(n)."

---

## [14:00 – 17:30] Part 4 — Space Complexity

**[SHOW SLIDE: "Space Complexity"]**

"Space complexity measures how much additional memory an algorithm uses as a function of input size. In interviews, when you are asked for space complexity, they typically mean *auxiliary space* — extra memory beyond the input itself.

**O(1) auxiliary space — the input is not counted, no extra structures:**

```python
def find_max(arr):
    max_val = arr[0]          # one variable — O(1)
    for item in arr:
        if item > max_val:
            max_val = item
    return max_val
```

One variable regardless of input size. O(1) space.

[PAUSE]

**O(n) space — proportional to input size:**

```python
def get_unique(arr):
    seen = set()              # grows with input — O(n)
    for item in arr:
        seen.add(item)
    return seen
```

The set can hold up to n elements. O(n) space.

[PAUSE]

**O(n) recursive call stack:**

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)   # n recursive calls on the stack
```

Each recursive call adds a frame to the call stack. For input n, there are n frames active simultaneously. Even though no explicit data structure is used, this is O(n) space.

[PAUSE]

**The time-space tradeoff:**

Many interview problems have an O(n²) brute force that uses O(1) space, and an O(n) optimized solution that uses O(n) space (a hash map or set). This tradeoff — buying speed with memory — is the most common optimization move in interviews. You are expected to recognize it and make it deliberately."

---

## [17:30 – 20:30] Part 5 — Amortized Analysis and Recursive Complexity

**[SHOW SLIDE: "Amortized Analysis"]**

"Two more concepts you need for interviews.

**Amortized analysis — cost per operation averaged over a sequence:**

Python's `list.append()` is O(1) amortized even though the underlying dynamic array occasionally doubles in size (an O(n) resize). The key is how rarely the expensive operation happens.

```python
arr = []
for i in range(n):
    arr.append(i)   # mostly O(1), occasionally O(n) for resize
# Total work: O(n) — the resizes together cost O(n) amortized over n appends
```

If you double capacity each resize, total copy operations across all resizes = 1 + 2 + 4 + ... + n = 2n. Over n appends, that is 2n / n = O(1) amortized per append.

[PAUSE]

**Recursive complexity — the Master Theorem shortcut:**

For recursive algorithms that divide the input, the Master Theorem gives you complexity directly. For interviews, you only need to recognize two patterns:

Pattern 1: Divide in half, O(n) work per level → O(n log n). This is merge sort.

Pattern 2: Divide in half, O(1) work per level → O(log n). This is binary search.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # T(n/2)
    right = merge_sort(arr[mid:])   # T(n/2)
    return merge(left, right)       # O(n) merge work
# T(n) = 2T(n/2) + O(n) → O(n log n)
```"

---

## [20:30 – 22:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 01 Lab Preview"]**

"The Module 01 lab has three parts.

Part 1 benchmarks complexity classes directly — you will write Python timing code and observe how runtime scales with input size for O(1), O(n), O(n log n), and O(n²) algorithms.

Part 2 covers complexity analysis by inspection — you will receive code snippets and practice identifying the time and space complexity of each.

Part 3 connects to LeetCode — you will solve an Easy-level problem, analyze its brute force and optimized complexities, and annotate your solution.

The quiz covers Big-O definitions, complexity class ordering, reading code for complexity, amortized analysis, and the space complexity of common operations. Read the guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 01 — Big-O Notation and Complexity Analysis]**

---

## Additional Resources

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com) — reference for all major data structures and sorting algorithms
- [OpenDSA — Mathematical Background](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Limitations.html)
- [NeetCode — Big O Notation](https://www.youtube.com/watch?v=BgLTDT03QtU)
- [VisuAlgo — Sorting Visualizations](https://visualgo.net/en/sorting)
