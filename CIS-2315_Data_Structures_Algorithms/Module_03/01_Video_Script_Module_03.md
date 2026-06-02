# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 03 — Stacks & Queues

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Stacks and queues are the two most fundamental abstract data types after arrays. Introduce each with a physical analogy first — stack of plates, printer queue — then build directly to code. Do not skip the analogy; it anchors the abstract definitions.
> - Monotonic stack is a top interview pattern — go slowly on the Daily Temperatures example. Draw the stack state at each step.
> - Students often confuse `deque` pronunciation ("deck") and its import path. Say it aloud: "from collections import deque — pronounced 'deck'."
> - The two-stack queue is a classic interview construction problem. Walk through both versions: `put`-heavy and `get`-heavy implementations.
> - Common mistakes: popping from an empty stack (always check before pop), confusing `append`/`pop` (stack) vs `appendleft`/`pop` (deque for queue), using a plain list as a queue (O(n) dequeue due to shifting).

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 03 | Stacks & Queues | CIS-2315"]**

"Module 02 built your pointer manipulation skills with linked lists. This module introduces the two most fundamental abstract data types in computer science: the stack and the queue. Every operating system, compiler, web browser, and scheduling system uses at least one of these. By the end of this module, you will be able to implement both from scratch in Python, explain their complexity profile, and solve the core interview problems that use them — including balanced parentheses, minimum stack, and the monotonic stack pattern."

---

## [01:30 – 06:00] Part 1 — Stacks: LIFO

**[SHOW SLIDE: "The Stack — Last In, First Out"]**

"Imagine a stack of plates in a cafeteria. You always add a plate to the top and take a plate from the top. The last plate placed on the stack is the first one removed. That is LIFO — Last In, First Out. A stack is defined entirely by that property.

The three fundamental operations are:

- **push(item)** — add to the top
- **pop()** — remove and return from the top
- **peek()** — return the top item without removing it

All three are O(1). A fourth operation, **is_empty()**, is O(1) as well.

[PAUSE]

**[DEMO — Stack using Python list]**

The simplest Python stack uses a list, because `list.append()` adds to the right end in O(1), and `list.pop()` removes from the right end in O(1). The right end is the top of the stack.

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack')
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('peek at empty stack')
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
```

[PAUSE]

Let me demonstrate:

```python
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())   # 30 — top of stack
print(s.pop())    # 30 — removed
print(s.pop())    # 20 — removed
print(len(s))     # 1 — only 10 remains
```

Notice: always check `is_empty()` before pop and peek. Popping from an empty stack is one of the most common bugs in stack problems.

[PAUSE]

**Where does Python itself use a stack?** The call stack. Every time your program calls a function, Python pushes a frame onto the call stack. When the function returns, the frame is popped. If you recurse too deeply, Python raises `RecursionError: maximum recursion depth exceeded` — the call stack overflowed. Understanding the stack data structure is literally understanding how your own code runs."

---

## [06:00 – 10:00] Part 2 — Stack Interview Pattern: Balanced Parentheses

**[SHOW SLIDE: "LeetCode #20 — Valid Parentheses"]**

"The classic stack interview problem is balanced parentheses. Given a string of brackets — `(`, `)`, `[`, `]`, `{`, `}` — determine whether every open bracket has a matching close bracket in the correct order.

The algorithm:

1. For every character in the string:
   - If it is an opening bracket, push it onto the stack.
   - If it is a closing bracket, check whether the top of the stack is the matching opener. If so, pop. If not (or the stack is empty), return `False`.
2. After scanning the full string, return `True` only if the stack is empty.

[PAUSE]

**[DEMO]**

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

Let me trace through `'([{}])'`:

- `(` → push. Stack: `['(']`
- `[` → push. Stack: `['(', '[']`
- `{` → push. Stack: `['(', '[', '{']`
- `}` → matches `{` on top → pop. Stack: `['(', '[']`
- `]` → matches `[` on top → pop. Stack: `['(']`
- `)` → matches `(` on top → pop. Stack: `[]`
- End: stack is empty → return `True`.

Now trace `'([)]'`:

- `(` → push. Stack: `['(']`
- `[` → push. Stack: `['(', '[']`
- `)` → top is `[`, not `(` → mismatch → return `False`.

Time: O(n). Space: O(n) worst case (all openers). This problem appears in the first five minutes of many phone screens."

---

## [10:00 – 14:00] Part 3 — Queues: FIFO

**[SHOW SLIDE: "The Queue — First In, First Out"]**

"A queue is the opposite principle: First In, First Out. Think of a printer queue — the first document sent is the first printed. Or a line at a coffee shop — the first person in line is the first served.

The operations are:

- **enqueue(item)** — add to the back
- **dequeue()** — remove from the front
- **peek()** — view the front item without removing
- **is_empty()** — O(1) check

All operations must be O(1). This rules out using a plain Python list as a queue: `list.pop(0)` removes from the front but requires shifting all remaining elements — that is O(n). Instead, Python provides `collections.deque`.

[PAUSE]

**[DEMO — Queue using collections.deque]**

`deque` is a double-ended queue — a doubly linked list under the hood. `append()` adds to the right. `popleft()` removes from the left. Both are O(1).

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)     # add to right (back)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self._data.popleft()  # remove from left (front)

    def peek(self):
        if self.is_empty():
            raise IndexError('peek at empty queue')
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
```

[PAUSE]

```python
q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q.dequeue())  # 'A' — first in, first out
print(q.dequeue())  # 'B'
print(q.peek())     # 'C'
```

Where are queues used? BFS uses a queue to process nodes level by level. Task schedulers, web request queues, and operating system process scheduling all use queues. Any system where fairness requires items to be processed in the order they arrived."

---

## [14:00 – 18:30] Part 4 — Monotonic Stack Pattern

**[SHOW SLIDE: "Monotonic Stack — Next Greater Element"]**

"The monotonic stack is one of the most important interview patterns you will learn in this course. It solves problems that ask: for each element, what is the next element that is greater (or smaller) than it?

The key insight: maintain a stack where elements are always in monotonically decreasing order. When a new element breaks that order, the stack tells you which previous elements have found their 'next greater.'

[PAUSE]

**[DEMO — LeetCode #739 Daily Temperatures]**

Problem: Given a list of daily temperatures, return a list where each entry is the number of days you have to wait for a warmer day. If no such day exists, put 0.

```python
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []   # stores indices

    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result
```

Let me trace through `[73, 74, 75, 71, 69, 72, 76, 73]`:

- i=0, temp=73: stack empty, push 0. Stack: [0]
- i=1, temp=74: 74 > temps[0]=73 → pop 0, result[0]=1-0=1. Stack empty, push 1. Stack: [1]
- i=2, temp=75: 75 > temps[1]=74 → pop 1, result[1]=2-1=1. Push 2. Stack: [2]
- i=3, temp=71: 71 < 75, just push. Stack: [2,3]
- i=4, temp=69: 69 < 71, just push. Stack: [2,3,4]
- i=5, temp=72: 72 > 69 → pop 4, result[4]=5-4=1. 72 > 71 → pop 3, result[3]=5-3=2. 72 < 75, stop. Push 5. Stack: [2,5]
- i=6, temp=76: 76 > 72 → pop 5, result[5]=6-5=1. 76 > 75 → pop 2, result[2]=6-2=4. Push 6. Stack: [6]
- i=7, temp=73: 73 < 76, push. Stack: [6,7]

Remaining stack indices never got a warmer day — result stays 0.

Final: `[1, 1, 4, 2, 1, 1, 0, 0]`.

Time: O(n) — each index is pushed and popped at most once. Space: O(n) worst case."

---

## [18:30 – 21:30] Part 5 — Implementing Queue with Two Stacks

**[SHOW SLIDE: "LeetCode #232 — Implement Queue using Stacks"]**

"A classic interview construction problem: implement a queue using only two stacks. This tests whether you understand both data structures at a deep level.

The idea: one stack is for pushing (inbox), one is for popping (outbox). When you dequeue and the outbox is empty, pour the entire inbox into the outbox — this reversal produces FIFO order.

[PAUSE]

**[DEMO]**

```python
class MyQueue:
    def __init__(self):
        self.inbox = []   # push here
        self.outbox = []  # pop from here

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
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
```

The amortized cost of each operation is O(1). Every element is pushed once, transferred once, and popped once — three operations over its lifetime, which is O(1) amortized even though individual `pop` calls that trigger a transfer are O(n)."

---

## [21:30 – 23:30] Part 6 — Complexity Summary and Closing

**[SHOW SLIDE: "Stack and Queue Complexity"]**

"Let me consolidate the complexity for both data structures.

| Operation | Stack (list) | Queue (deque) |
|---|---|---|
| Push / Enqueue | O(1) | O(1) |
| Pop / Dequeue | O(1) | O(1) |
| Peek | O(1) | O(1) |
| Search | O(n) | O(n) |
| Space | O(n) | O(n) |

Everything you do at the top of a stack or the front of a queue is O(1). Never search a stack — pop everything or use a different structure.

[PAUSE]

**When do you reach for a stack?**

- Any problem involving matching, nesting, or backtracking.
- DFS traversal (iterative version uses an explicit stack).
- Undo/redo functionality.
- Expression evaluation and syntax parsing.

**When do you reach for a queue?**

- BFS traversal.
- Level-order processing.
- Any system requiring fair FIFO ordering.
- Sliding window problems often use a deque for O(1) front and back access.

The Module 03 lab has you implement both from scratch and solve four LeetCode problems. The quiz covers LIFO vs FIFO, operation complexity, and the monotonic stack pattern. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 03 — Stacks & Queues]**

---

## Additional Resources

- [VisuAlgo — Stack Visualization](https://visualgo.net/en/list)
- [NeetCode — Stack & Queue Playlist](https://www.youtube.com/watch?v=KInG04mAjO0)
- [LeetCode #20 — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [LeetCode #155 — Min Stack](https://leetcode.com/problems/min-stack/)
- [LeetCode #739 — Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- [LeetCode #232 — Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
