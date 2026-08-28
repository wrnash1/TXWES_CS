# Reading Guide: Module 03 — Stacks & Queues

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2315 &BULL; DATA STRUCTURES & ALGORITHM ANALYSIS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Stacks and queues are the two most fundamental abstract data types in computer science. Their defining property is access order — LIFO for stacks, FIFO for queues — and that property shapes which problems they solve. Every compiler, operating system, and web browser relies on one or both. In technical interviews, stacks and queues appear directly (Valid Parentheses, Min Stack, Implement Queue with Two Stacks) and as the engine behind other algorithms (stacks drive DFS and expression parsing; queues drive BFS and level-order traversal).

---

## 1. The Stack — LIFO

### Stack Structure

A stack is a Last In, First Out (LIFO) collection. Elements are added and removed from the same end, called the top. The underlying storage is typically a dynamic array (Python list), but a singly linked list with a head pointer works equally well.

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)       # O(1) amortized

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack')
        return self._data.pop()       # O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError('peek at empty stack')
        return self._data[-1]         # O(1)

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
```

### Stack Complexity

| Operation | Time | Notes |
|---|---|---|
| push | O(1) amortized | `list.append()` occasionally resizes, O(1) amortized |
| pop | O(1) | `list.pop()` at the end — no shifting |
| peek | O(1) | `list[-1]` index access |
| is_empty / len | O(1) | Direct attribute read |
| Search | O(n) | Must pop until found — not a stack operation |
| Space | O(n) | One slot per stored element |

### Stack Applications

**Balanced parentheses / bracket matching** — push openers, pop on closers, return True if stack is empty at the end.

**Function call stack** — the Python (and every language) runtime maintains a call stack. Each function invocation pushes a frame; each return pops it. `RecursionError: maximum recursion depth exceeded` means the call stack filled.

**DFS (iterative)** — replace the recursive call stack with an explicit stack to control traversal order and avoid recursion depth limits.

**Expression evaluation** — operators and operands are pushed onto separate stacks; evaluate when precedence rules allow it.

**Undo / redo** — push actions onto an undo stack; undo pops the most recent action; redo pushes it to a redo stack.

---

## 2. The Queue — FIFO

### Queue Structure

A queue is a First In, First Out (FIFO) collection. Elements are added at the back (enqueue) and removed from the front (dequeue). A plain Python list is not suitable: `list.pop(0)` is O(n) due to element shifting. Use `collections.deque` instead — it is a doubly linked list under the hood, providing O(1) `append` (right) and O(1) `popleft` (left).

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)       # O(1) — add to back

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self._data.popleft()   # O(1) — remove from front

    def peek(self):
        if self.is_empty():
            raise IndexError('peek at empty queue')
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
```

### Queue Complexity

| Operation | Time | Notes |
|---|---|---|
| enqueue | O(1) | `deque.append()` |
| dequeue | O(1) | `deque.popleft()` |
| peek | O(1) | `deque[0]` index access |
| Search | O(n) | Not a queue operation |
| Space | O(n) | One node per stored element |

### Queue Applications

**BFS** — enqueue the start node; dequeue-process-enqueue-neighbors in a loop. The FIFO order guarantees level-by-level exploration.

**Level-order tree traversal** — BFS on a tree. Each level's nodes are processed before the next level.

**Task scheduling** — operating systems use queues for process scheduling (FIFO basic policy) and I/O request queues.

**Sliding window** — a `deque` of indices maintains a monotonic window for problems like Sliding Window Maximum (LeetCode #239).

---

## 3. The Monotonic Stack Pattern

A monotonic stack maintains elements in sorted order (strictly increasing or strictly decreasing) as items are pushed. When a new element would break the monotonic property, elements are popped from the stack until the property can be restored — and each popped element has found its "answer."

### Next Greater Element Template

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # stores indices; values are decreasing
    for i, val in enumerate(nums):
        while stack and nums[stack[-1]] < val:
            idx = stack.pop()
            result[idx] = val
        stack.append(i)
    return result
```

Elements remaining in the stack when the loop ends have no greater element to the right — their result stays -1.

**Time:** O(n) — each element is pushed once and popped at most once.
**Space:** O(n) worst case (strictly decreasing input; no pops).

### LeetCode #739 — Daily Temperatures

```python
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []  # indices; temps[stack[-1]] is decreasing
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx   # days until warmer
        stack.append(i)
    return result
```

### When to Use a Monotonic Stack

- "For each element, find the next/previous element that is greater/smaller."
- Trapping Rain Water (LeetCode #42).
- Largest Rectangle in Histogram (LeetCode #84).
- Next Greater Element I/II (LeetCode #496/#503).

---

## 4. Two-Stack Queue

Implementing a queue using only two stacks is a canonical interview construction problem (LeetCode #232). It tests whether you understand the reversal property of stacks.

```python
class MyQueue:
    def __init__(self):
        self.inbox = []   # new elements pushed here
        self.outbox = []  # elements popped from here

    def push(self, x):
        self.inbox.append(x)

    def pop(self):
        self._transfer()
        return self.outbox.pop()

    def peek(self):
        self._transfer()
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox

    def _transfer(self):
        """Pour inbox into outbox only when outbox is empty."""
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
```

**Amortized analysis:** Each element is pushed to inbox once, transferred to outbox once, and popped from outbox once — three O(1) operations per element lifetime. The amortized cost per operation is O(1) even though individual `pop` calls that trigger a transfer are O(n).

---

## 5. Min Stack

LeetCode #155 requires a stack that supports `push`, `pop`, `top`, and `getMin` all in O(1). The trick: maintain a parallel auxiliary stack that tracks the running minimum at every level.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # parallel min tracking

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

The minimum at any stack depth is the top of `min_stack`. When you pop the main stack, you pop the min stack too, restoring the previous minimum.

---

## 6. Complexity Summary

| Structure | Push/Enqueue | Pop/Dequeue | Peek | Search | Space |
|---|---|---|---|---|---|
| Stack (Python list) | O(1) amortized | O(1) | O(1) | O(n) | O(n) |
| Queue (deque) | O(1) | O(1) | O(1) | O(n) | O(n) |
| Two-Stack Queue | O(1) amortized | O(1) amortized | O(1) amortized | O(n) | O(n) |
| Min Stack | O(1) | O(1) | O(1) | O(n) | O(n) |

---

## 7. Interview Exam Tips

1. **Never use `list.pop(0)` as a queue** — it is O(n). Use `collections.deque` and call `popleft()`.

2. **Always guard against empty pop/peek** — check `is_empty()` before accessing the top. Interviewers watch for this.

3. **Monotonic stack pattern cue** — if the problem asks "for each element, what is the next element smaller/larger than it," reach for a monotonic stack immediately.

4. **Two-stack queue amortized cost** — individual `pop` calls can be O(n), but amortized each element is O(1). Interviewers may ask; be ready to explain the amortized argument.

5. **Min stack uses a parallel stack** — do not try to compute the minimum by scanning the whole stack. The parallel min_stack keeps it O(1).

6. **BFS needs a queue; DFS needs a stack** — memorize this pairing. Iterative DFS pushes neighbors onto a stack; BFS enqueues them onto a deque.

7. **`collections.deque` for sliding window** — `appendleft`, `append`, `popleft`, `pop` are all O(1). Use a deque of indices for the Sliding Window Maximum pattern.

8. **Stack overflow = recursive call stack overflowed** — Python default recursion limit is 1000. If a problem has deep recursion, convert to iterative with an explicit stack.

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Stack and Queue Visualizations** — [https://visualgo.net/en/list](https://visualgo.net/en/list)
   Interactive animations showing push/pop operations on stacks and enqueue/dequeue on queues with pointer-level detail. Useful for building intuition for the LIFO and FIFO access patterns before coding.

2. **OpenDSA — Stacks Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/StackArray.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/StackArray.html)
   Free interactive OER textbook with embedded exercises covering array-based and linked-list-based stack implementations, with complexity analysis and practice problems.

3. **NeetCode — Stack Problems Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
   Free video solutions to the most common stack interview problems, including Valid Parentheses, Min Stack, and Daily Temperatures, with clear explanation of the monotonic stack pattern.

4. **Python `collections.deque` Documentation** — [https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
   Official Python documentation for `collections.deque` — the correct structure for O(1) queue operations. Covers `appendleft`, `popleft`, `rotate`, and the `maxlen` parameter.

5. **CS50 — Data Structures Shorts: Stacks and Queues** — [https://cs50.harvard.edu/x/2024/shorts/](https://cs50.harvard.edu/x/2024/shorts/)
   Short-form Harvard CS50 video lectures (5-10 minutes each) covering stacks and queues from first principles with memory diagrams. Free with no account required.

---

## 8. Study Checklist

- [ ] Watch the Module 03 video lecture by Professor Nash.
- [ ] Implement `Stack` from scratch using a Python list.
- [ ] Implement `Queue` from scratch using `collections.deque`.
- [ ] Solve LeetCode #20 (Valid Parentheses).
- [ ] Solve LeetCode #155 (Min Stack).
- [ ] Solve LeetCode #739 (Daily Temperatures — monotonic stack).
- [ ] Solve LeetCode #232 (Implement Queue using Stacks).
- [ ] Complete the Module 03 Lab.
- [ ] Complete the Module 03 Quiz.
