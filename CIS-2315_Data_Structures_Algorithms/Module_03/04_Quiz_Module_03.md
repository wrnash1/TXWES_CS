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
