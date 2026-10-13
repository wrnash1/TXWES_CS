# Quiz: Module 03 — Stacks & Queues

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

Which access order defines a stack?

- A) FIFO — First In, First Out
- B) LIFO — Last In, First Out
- C) LILO — Last In, Last Out
- D) Priority order — the highest-priority element is removed first

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* FIFO describes a queue, not a stack. In a queue, the first element added is the first element removed.
- *Why B is correct:* A stack is LIFO. The last element pushed onto the stack is the first element popped. The cafeteria plate analogy: the last plate placed on top is the first one taken.
- *Why C is incorrect:* LILO is not a standard access order for any fundamental data structure. It is a distracting acronym that does not correspond to either a stack or a queue.
- *Why D is incorrect:* Priority order describes a priority queue (heap), a separate data structure covered in Module 07. Stacks have no notion of element priority — order is determined entirely by when elements were pushed.

---

### Question 2

What is the time complexity of `pop()` on a stack implemented with a Python list?

- A) O(n) — must shift all remaining elements
- B) O(log n) — uses binary search to find the top
- C) O(1) — removes from the end of the list, no shifting
- D) O(n²) — requires two passes over the list

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n) shifting occurs when you remove from the front of a Python list (`list.pop(0)`). A stack removes from the end (`list.pop()`), which requires no shifting — the last element is simply released.
- *Why B is incorrect:* Binary search applies to sorted sequences to find a target value in O(log n). `pop()` does not search for anything — it accesses the known last position directly.
- *Why C is correct:* `list.pop()` with no argument removes and returns the last element. Python lists are arrays; the last element's address is computed directly from the list's length. No traversal or shifting is needed — O(1).
- *Why D is incorrect:* O(n²) would require nested passes. There is nothing nested about removing the last element of an array.

---

### Question 3

A developer writes the following code to use a Python list as a queue:

```python
queue = []
queue.append('A')
queue.append('B')
queue.append('C')
first = queue.pop(0)
```

What is the time complexity of `queue.pop(0)`, and what is the correct fix?

- A) O(1); no fix needed — Python lists are optimized for front removal
- B) O(n); use `collections.deque` and call `popleft()` instead
- C) O(log n); use `heapq` for front removal
- D) O(n); use a singly linked list and remove the head node

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python lists are contiguous arrays. Removing the first element (`pop(0)`) requires shifting every remaining element one position to the left — O(n). Python does not special-case this operation.
- *Why B is correct:* `collections.deque` is a doubly linked list under the hood. `popleft()` removes the first node by updating one pointer — O(1). It is the standard Python idiom for a FIFO queue.
- *Why C is incorrect:* `heapq` implements a min-heap for priority queue operations. It does not preserve insertion order and is not used for FIFO queues.
- *Why D is incorrect:* A singly linked list with a head pointer does support O(1) front removal, but Python provides `collections.deque` which is the idiomatic, built-in solution. Implementing a custom linked list is unnecessary.

---

### Question 4

Consider the following balanced parentheses algorithm:

```python
def is_valid(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
    return len(stack) == 0
```

What does `is_valid('([)]')` return, and why?

- A) `True` — all four brackets are present
- B) `True` — the function only checks that open and close counts match
- C) `False` — the closing `)` does not match the most recently opened `[`
- D) `False` — the function rejects any string with mixed bracket types

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The function does not merely count brackets. It verifies that each closer matches the most recently pushed opener. Presence of all four types is irrelevant if they are incorrectly nested.
- *Why B is incorrect:* The function checks nesting order, not just counts. `'([)]'` has one of each bracket type, but the nesting is crossed — `(` wraps `[`, but `)` tries to close before `]` does.
- *Why C is correct:* Trace the algorithm: push `(`, push `[`. Then `)` arrives — `stack[-1]` is `[`, but `match[')']` is `(`. These do not match, so the function immediately returns `False`. Crossed nesting is detected at the first mismatch.
- *Why D is incorrect:* Mixed bracket types are valid as long as they are properly nested. `is_valid('()[]{}')`  returns `True` — three different bracket pairs, each correctly matched.

---

### Question 5

The Min Stack data structure must support `push`, `pop`, `top`, and `getMin` all in O(1). Which design achieves this?

- A) Sort the stack after every push so the minimum is always at the bottom
- B) Maintain a separate `min_stack` that records the current minimum at each depth level
- C) Scan the entire stack whenever `getMin` is called
- D) Store the minimum as a single variable and update it on every push and pop

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Sorting after every push is O(n log n) per push. This violates the O(1) requirement for `push`. Additionally, sorting destroys the LIFO order needed for `pop`.
- *Why B is correct:* A parallel `min_stack` pushes `min(val, min_stack[-1])` alongside each element. When the main stack pops, the min stack pops too. The current minimum is always `min_stack[-1]` — O(1) access without any scan.
- *Why C is incorrect:* Scanning the entire stack for the minimum is O(n). The problem requires O(1).
- *Why D is incorrect:* A single minimum variable works for push updates but breaks on pop. When you pop the current minimum, you have no way to recover the previous minimum without scanning the remaining elements — which is O(n).

---

### Question 6

What is the defining property of a monotonic stack, and why does it solve the "next greater element" problem in O(n)?

- A) Elements are stored in sorted order using a heap property, enabling O(log n) lookups
- B) The stack maintains elements in non-increasing order; when a new element exceeds the top, each popped element has found its next greater element
- C) The stack processes elements two at a time, halving the problem with each pass
- D) Elements are stored in increasing order from bottom to top; pops occur at the bottom

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A monotonic stack is an ordinary stack — it uses no heap property and no O(log n) operations. Sorted order in a heap allows O(log n) insert/extract, but a monotonic stack achieves O(n) total work by limiting each element to one push and one pop.
- *Why B is correct:* A monotonically decreasing stack maintains `stack[-1]` as the smallest seen so far. When element `val` at index `i` exceeds `temps[stack[-1]]`, that index's question is answered: the next greater element is `val`. Since each element is pushed once and popped at most once, total work is O(2n) = O(n).
- *Why C is incorrect:* Processing elements two at a time describes a two-pointer technique, not a monotonic stack. The monotonic stack processes elements sequentially from left to right.
- *Why D is incorrect:* Pops occur at the top, not the bottom — that is the fundamental property of any stack. A stack that pops from the bottom would be a queue.

---

### Question 7

What is the amortized time complexity of `pop()` in the two-stack queue implementation (LeetCode #232)?

- A) O(n) in the worst case, with no amortized guarantee
- B) O(n) worst case per call; O(1) amortized per operation over all operations
- C) O(log n) using binary search to locate the front element
- D) O(1) guaranteed per call regardless of queue state

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This is partially true (worst case is O(n)) but misses the amortized analysis. O(n) worst case with no amortized guarantee would mean the average is also O(n). The amortized guarantee is the important part.
- *Why B is correct:* Each element is pushed to inbox once (O(1)), transferred to outbox once (O(1)), and popped from outbox once (O(1)). Over n total operations, total work is O(3n) = O(n), so amortized cost per operation is O(1). An individual `pop` that triggers a full transfer is O(k) where k is the inbox size, but that cost is charged to the k elements being transferred.
- *Why C is incorrect:* Binary search requires sorted data with random access by index. The two-stack queue contains elements in arbitrary order and has no index access.
- *Why D is incorrect:* If the outbox is empty when `pop` is called and the inbox contains k elements, the transfer loop runs k times — O(k). The guarantee is amortized, not worst-case per call.

---

### Question 8

Which Python expression evaluates the top of a stack implemented as a Python list named `s`, without modifying the stack?

- A) `s.pop()`
- B) `s[0]`
- C) `s[-1]`
- D) `s.peek()`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `s.pop()` removes and returns the last element. This is a destructive operation — it modifies the stack. The question asks to peek without modifying.
- *Why B is incorrect:* `s[0]` accesses the first (bottom) element of the list, which is the bottom of the stack — the element that has been there the longest. The top is the last element.
- *Why C is correct:* The top of a stack implemented as a Python list is the last element. `s[-1]` accesses the last element by negative indexing — O(1), non-destructive.
- *Why D is incorrect:* Python's built-in list type has no `.peek()` method. Calling it raises `AttributeError`. The `peek()` method only exists on custom `Stack` wrapper classes.

---

### Question 9

A call stack overflows with `RecursionError: maximum recursion depth exceeded`. Which data structure concept does this error directly demonstrate?

- A) Queue overflow — the BFS queue grew too large
- B) Heap exhaustion — too many objects were allocated on the heap
- C) Stack overflow — too many function call frames were pushed onto the call stack
- D) Hash collision — too many function names mapped to the same bucket

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* BFS uses a queue, not a call stack. A BFS queue growing large would not cause a Python `RecursionError` — it would be a memory error or a logical error in the traversal.
- *Why B is incorrect:* Heap exhaustion (running out of memory for object allocation) raises `MemoryError`, not `RecursionError`. The error message specifically names "recursion depth" and "maximum."
- *Why C is correct:* Python implements function calls using a call stack. Each call pushes a new frame; each return pops it. Python enforces a recursion limit (default 1000) to prevent infinite recursion from consuming all memory. Exceeding it raises `RecursionError`. This is literally a stack overflow.
- *Why D is incorrect:* Hash collisions are a separate concept from recursion and function calls. They have no relationship to the call stack or recursion depth.

---

### Question 10

Given a stack containing `[1, 2, 3]` (3 is the top), what is the state of the stack after executing the following code?

```python
temp = []
while s:
    temp.append(s.pop())
while temp:
    s.push(temp.pop())
```

- A) `[3, 2, 1]` — the stack is reversed
- B) `[1, 2, 3]` — the stack is unchanged
- C) `[]` — both stacks emptied simultaneously
- D) `[2, 1, 3]` — only the middle element moves

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The first while loop pops 3, 2, 1 into `temp` — `temp` is `[3, 2, 1]` (1 is the top). The second while loop pops 1, 2, 3 from `temp` back into `s` — pushing them in reverse order of how they came out, which is the original order.
- *Why B is correct:* Two stack reversals produce the original order. First reversal: `s=[1,2,3]` → `temp=[3,2,1]`. Second reversal: `temp=[3,2,1]` → `s=[1,2,3]`. The two reversals cancel, and the stack is restored to its original state.
- *Why C is incorrect:* Both loops terminate when their respective sources are empty, not simultaneously. At no point are both stacks empty at the same time during the loop (unless the starting stack was empty).
- *Why D is incorrect:* The code applies the same pop-then-repush operation to all elements uniformly. No element is treated differently from any other. There is no mechanism to move only the middle element.

---

### Question 11

**Each question is worth 5 points.**

A browser's back/forward navigation maintains two stacks: `back_stack` and `forward_stack`. When the user visits a new page, the current page is pushed to `back_stack` and `forward_stack` is cleared. When the user clicks Back, the current page is pushed to `forward_stack` and the top of `back_stack` is popped. Which operation is O(1) and which is amortized O(n)?

- A) Visiting a new page is O(1); pressing Back is O(n) because `forward_stack` must be rebuilt
- B) Both operations are O(1) — all operations are stack push/pop
- C) Pressing Back is O(n) because the forward stack must be searched for a matching page
- D) Visiting a new page is O(n) because the forward stack must be fully cleared

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Clearing `forward_stack` might seem expensive, but clearing means resetting a reference to an empty list — O(1). There is no per-element loop required to empty the stack.
- *Why B is correct:* All operations are stack operations. Visiting a new page: push to `back_stack` (O(1)), clear `forward_stack` by assigning `[]` (O(1)) — total O(1). Pressing Back: push current to `forward_stack` (O(1)), pop from `back_stack` (O(1)) — total O(1). No scanning or traversal is required.
- *Why C is incorrect:* No search is performed. The forward stack operation is a simple push of the current page — O(1). The forward stack is not searched; it is treated as a pure LIFO container.
- *Why D is incorrect:* Clearing the forward stack by `forward_stack = []` is O(1) — it creates a new empty list reference. The old list's memory will be reclaimed by the garbage collector, but that cost is not charged to the operation.

---

### Question 12

What is the output of the following code?

```python
s = []
for ch in 'ABCDE':
    s.append(ch)
result = []
for _ in range(3):
    result.append(s.pop())
print(result)
```

- A) `['A', 'B', 'C']`
- B) `['E', 'D', 'C']`
- C) `['C', 'D', 'E']`
- D) `['A', 'B', 'C', 'D', 'E']`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `s.pop()` removes from the top (end) of the stack. After pushing 'A' through 'E', the top is 'E'. The first pop returns 'E', not 'A'.
- *Why B is correct:* After the first loop, `s = ['A','B','C','D','E']` with 'E' at the top. Three pops return 'E', then 'D', then 'C' in that order. `result = ['E','D','C']`.
- *Why C is incorrect:* `['C','D','E']` would be the result if pops were in reverse order — i.e., if the stack were reversed before popping, or if elements were dequeued rather than popped.
- *Why D is incorrect:* `result` only receives 3 elements from the 3 iterations of the second loop. The remaining 2 elements ('A' and 'B') stay in `s` and are never moved to `result`.

---

### Question 13

Which statement correctly describes the difference between a stack and a queue when used to implement graph traversal?

- A) A stack explores nodes closest to the source first; a queue explores nodes deepest first
- B) A stack enables depth-first search; a queue enables breadth-first search
- C) Both explore nodes in the same order; only performance differs
- D) A queue enables depth-first search; a stack enables breadth-first search

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This reverses the correct description. A queue explores closest (shallowest) nodes first — this is BFS. A stack explores deepest first — this is DFS. The description in option A applies to a queue, not a stack.
- *Why B is correct:* Iterative DFS: push the starting node onto a stack, then repeatedly pop a node and push its unvisited neighbors. Neighbors pushed last are explored first — LIFO behavior drives depth-first exploration. Iterative BFS: enqueue the starting node, then repeatedly dequeue a node and enqueue its unvisited neighbors. Neighbors enqueued earliest are processed first — FIFO behavior drives breadth-first (level-by-level) exploration.
- *Why C is incorrect:* The traversal orders are fundamentally different. DFS follows a single path as deep as possible before backtracking; BFS explores all nodes at distance k before exploring nodes at distance k+1. The data structure choice (stack vs queue) is precisely what produces these different orders.
- *Why D is incorrect:* This is the complete reversal of the correct answer. Queue = BFS; Stack = DFS. This is a common confusion point that interviewers test.

---

### Question 14

In the valid parentheses problem (`is_valid`), what should the function return for the empty string `""`?

- A) `False` — an empty string contains no matching pairs
- B) `True` — the stack is empty after processing, satisfying `len(stack) == 0`
- C) `None` — the function should raise an exception for empty input
- D) `False` — the function requires at least one bracket pair

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Validity means every opener has a matching closer in correct order. An empty string trivially satisfies this — there are no openers without closers. Mathematically, an empty set of bracket pairs is a valid (empty) sequence of matching pairs.
- *Why B is correct:* The loop body never executes for an empty string. The stack remains empty. The final `return len(stack) == 0` evaluates to `return 0 == 0` which is `True`. An empty string is a valid (trivially balanced) bracket string — this is the standard convention.
- *Why C is incorrect:* Raising an exception for an empty string would be incorrect behavior. The function should handle all string inputs, including empty.
- *Why D is incorrect:* No requirement in the problem states that at least one pair must be present. The empty case is well-defined and the correct answer is `True`.

---

### Question 15

A circular queue (ring buffer) of capacity `k` is implemented with a fixed array. When is the queue considered full?

- A) When the `front` pointer equals the `rear` pointer
- B) When `(rear + 1) % k == front` — the next rear position would equal front
- C) When all array indices contain non-null values
- D) When `rear == k - 1` — the rear pointer reaches the last index

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `front == rear` indicates the queue is empty, not full. This is the standard empty condition for a circular buffer. Confusing full and empty is a classic ring buffer bug.
- *Why B is correct:* In a circular buffer, `rear` points to the next position to fill. After filling the position, `rear = (rear + 1) % k`. The queue is full when `rear`'s next position (mod k) would wrap into `front` — meaning there is one unused slot (a common convention to distinguish full from empty). `(rear + 1) % k == front` is the standard full condition.
- *Why C is incorrect:* Checking all array indices for non-null values is O(k) — not suitable for a real-time check. The purpose of a ring buffer is O(1) full/empty detection.
- *Why D is incorrect:* `rear == k - 1` only detects that the rear reached the physical end of the array — but a circular buffer wraps around. The rear pointer resets to 0 and continues filling from the beginning when space is available.

---

### Question 16

The "decode string" problem (LeetCode #394) asks you to decode strings like `"3[a2[c]]"` → `"accaccacc"`. Which data structure naturally handles the nested bracket structure?

- A) A queue — process characters in FIFO order
- B) A stack — push current state when entering `[`, pop and combine when encountering `]`
- C) A hash map — store the multiplier for each character
- D) A priority queue — process higher multipliers first

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A queue processes in FIFO order, which is appropriate for level-by-level problems, not nested structures. Nested brackets require remembering the state at each nesting level — FIFO order doesn't preserve this hierarchy.
- *Why B is correct:* Nested brackets map directly to recursive structure, which maps to a stack. When `[` is encountered, push the current string and current multiplier onto the stack (saving state for this nesting level). When `]` is encountered, pop the previous string and multiplier, compute `prev_string + multiplier × current_string`. The stack naturally handles arbitrary nesting depth in O(n) time.
- *Why C is incorrect:* A hash map stores key-value pairs. There is no meaningful key for each multiplier in a nested string — the same multiplier digit (e.g., `3`) can appear at multiple nesting levels with different targets.
- *Why D is incorrect:* Priority queues reorder elements by priority. The decode problem requires preserving the original order of the string and handling nesting levels — neither of which relates to priority ordering.

---

### Question 17

`collections.deque` supports both `appendleft` and `popleft` in O(1). How does it achieve this, unlike a Python list?

- A) It uses a hash table to track both ends
- B) It uses a doubly linked list (or block-based doubly linked structure), allowing O(1) operations at both ends
- C) It preallocates extra capacity at the front of the array
- D) It sorts elements to keep the front accessible in O(1)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A hash table provides O(1) access by key, not O(1) access to ends. A deque needs ordered front/back access, not key-based access.
- *Why B is correct:* CPython's `collections.deque` is implemented as a doubly-linked list of fixed-size memory blocks (not individual node links). This allows O(1) insertion and removal at both the front and back without shifting. This is fundamentally different from Python's `list`, which is a contiguous array requiring O(n) shifts for front operations.
- *Why C is incorrect:* A Python list is a contiguous array. Even with extra capacity at the front, inserting at position 0 still requires updating the reference count and internal array pointer — it does not change the O(n) shifting cost. Real O(1) front access requires a non-contiguous structure.
- *Why D is incorrect:* Sorting is O(n log n) and is unrelated to achieving O(1) end access. Sorting a deque on every operation would destroy the insertion order.

---

### Question 18

In the daily temperatures monotonic stack solution, what value is stored in the stack — the temperature value or the index?

- A) The temperature value — to compare with incoming temperatures directly
- B) The index — to compute the number of days between current and future warmer day
- C) Both — a tuple of (index, temperature) for efficient comparison
- D) A hash of the temperature — to enable O(1) lookup by temperature

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Storing only temperature values would allow comparison, but the answer requires the number of days elapsed — a distance in indices. If you only store values, you cannot compute `result[i] = j - i` because `i` (the original index) is lost.
- *Why B is correct:* The stack stores indices. When a warmer day at index `j` is found, all cooler days at indices on the stack are popped, and for each popped index `i`, `result[i] = j - i`. The temperature at index `i` is retrieved as `temps[i]` using the stored index — O(1) array access.
- *Why C is incorrect:* Storing both is redundant — the temperature is fully accessible from the index via `temps[i]`. Storing a tuple wastes space and adds complexity without benefit.
- *Why D is incorrect:* Hashing temperatures adds unnecessary O(1) overhead and does not help compute the index distance. There is no lookup-by-temperature operation in this problem.

---

### Question 19

What is the time complexity of the valid parentheses algorithm (`is_valid`) on a string of length n?

- A) O(n²) — for each closer, the entire stack is scanned
- B) O(n log n) — the stack is sorted to match brackets
- C) O(n) — each character is pushed or popped at most once
- D) O(1) — hash map lookups make all operations constant

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The algorithm does not scan the stack. When a closing bracket is encountered, only `stack[-1]` (the top) is accessed — O(1). There is no loop over the stack contents.
- *Why B is incorrect:* No sorting occurs. The hash map `match = {')': '(', ']': '[', '}': '{'}` provides O(1) lookup of the expected opener for each closer. Sorting is irrelevant to this problem.
- *Why C is correct:* The outer `for` loop iterates over each of the n characters once. Each character causes at most one stack `append` (O(1)) or one `stack[-1]` access plus one `pop` (O(1)). Total: n iterations × O(1) per iteration = O(n). The final `len(stack) == 0` check is O(1).
- *Why D is incorrect:* O(1) total would mean the algorithm takes a fixed number of operations regardless of string length. The outer loop runs n times — the algorithm is O(n), not O(1). The hash map lookups are O(1) per character, contributing to the O(n) overall.

---

### Question 20

A stack-based expression evaluator processes the postfix expression `"5 3 2 * + 8 -"`. What is the final result?

- A) `7`
- B) `3`
- C) `-3`
- D) `9`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Trace: push 5, push 3, push 2. `*` → pop 2 and 3, push 6. `+` → pop 6 and 5, push 11. push 8. `-` → pop 8 and 11, push 11 − 8 = 3. The result is 3, not 7.
- *Why B is correct:* Full trace of `"5 3 2 * + 8 -"`: Push 5 → [5]. Push 3 → [5,3]. Push 2 → [5,3,2]. `*`: pop 2,3 → push 3×2=6 → [5,6]. `+`: pop 6,5 → push 5+6=11 → [11]. Push 8 → [11,8]. `-`: pop 8,11 → push 11−8=3 → [3]. Final stack: [3]. Result = 3.
- *Why C is incorrect:* `-3` would result from `8 - 11 = -3`, which would happen if the subtraction popped the operands in the wrong order (subtracting the first-popped from the second-popped). The correct convention is: pop `b` first, pop `a` second, compute `a op b` → 11 − 8 = 3.
- *Why D is incorrect:* 9 does not appear in any correct intermediate step of this expression evaluation.
