# Lab Activity: Module 03 — Stacks & Queues

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement a Stack and Queue from scratch
- **Part 2** — Stack interview patterns: Valid Parentheses and Min Stack
- **Part 3** — Monotonic stack and two-stack queue on LeetCode

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Implementing Stack and Queue

**File:** `lab03_stack_queue.py`

### 1.1 — Stack

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        """Add to top — O(1) amortized"""
        self._data.append(item)

    def pop(self):
        """Remove and return top — O(1)"""
        if self.is_empty():
            raise IndexError('pop from empty stack')
        return self._data.pop()

    def peek(self):
        """Return top without removing — O(1)"""
        if self.is_empty():
            raise IndexError('peek at empty stack')
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Stack({self._data})'
```

Test:

```python
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)            # Stack([10, 20, 30])
print(s.peek())     # 30
print(s.pop())      # 30
print(s.pop())      # 20
print(len(s))       # 1
print(s.is_empty()) # False
s.pop()
print(s.is_empty()) # True

# Guard test — should raise IndexError
try:
    s.pop()
except IndexError as e:
    print(f'Caught: {e}')   # Caught: pop from empty stack
```

**Checkpoint:** All prints match expected values. `IndexError` is raised on empty pop.

---

### 1.2 — Queue using collections.deque

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Add to back — O(1)"""
        self._data.append(item)

    def dequeue(self):
        """Remove from front — O(1)"""
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self._data.popleft()

    def peek(self):
        """Return front without removing — O(1)"""
        if self.is_empty():
            raise IndexError('peek at empty queue')
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Queue({list(self._data)})'
```

Test:

```python
q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q)             # Queue(['A', 'B', 'C'])
print(q.dequeue())   # 'A' — FIFO
print(q.dequeue())   # 'B'
print(q.peek())      # 'C'
print(len(q))        # 1

# Bad queue — why list.pop(0) is wrong:
bad = [1, 2, 3]
bad.pop(0)  # O(n) — shifts all elements — never use as queue
```

**Checkpoint:** Dequeue returns items in FIFO order. Guard raises `IndexError` on empty queue.

---

### 1.3 — Complexity Verification Exercise

Answer these questions in comments in your file:

```python
# Q: What is the time complexity of Stack.peek()?
# A: O(1) — list[-1] is direct index access

# Q: Why is list.pop(0) O(n) while deque.popleft() is O(1)?
# A: list stores elements contiguously; removing the first requires
#    shifting all remaining n-1 elements left by one position. O(n).
#    deque is a doubly linked list; popleft() unlinks the first node
#    and updates one pointer. O(1).

# Q: What is the space complexity of a stack holding n items?
# A: O(n) — one storage slot per item.
```

---

## Part 2 — Stack Interview Patterns

**File:** `lab03_patterns.py`

### 2.1 — Valid Parentheses (LeetCode #20)

```python
def is_valid(s):
    """
    Return True if all brackets are correctly matched and nested.
    Time: O(n), Space: O(n)
    """
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

Test:

```python
print(is_valid('()'))        # True
print(is_valid('()[]{}'))    # True
print(is_valid('([{}])'))    # True
print(is_valid('(]'))        # False
print(is_valid('([)]'))      # False
print(is_valid('{[]'))       # False — unclosed opener
print(is_valid(''))          # True — empty string is valid
```

**Checkpoint:** All seven test cases match expected booleans.

---

### 2.2 — Min Stack (LeetCode #155)

```python
class MinStack:
    """
    Stack supporting O(1) push, pop, top, and getMin.
    Uses a parallel auxiliary stack to track running minimum.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

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

Test:

```python
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin())   # -3
ms.pop()
print(ms.top())      # 0
print(ms.getMin())   # -2
```

Trace the `min_stack` state manually:

```python
# After push(-2): stack=[-2],        min_stack=[-2]
# After push(0):  stack=[-2, 0],     min_stack=[-2, -2]
# After push(-3): stack=[-2, 0, -3], min_stack=[-2, -2, -3]
# getMin() = min_stack[-1] = -3
# pop():          stack=[-2, 0],     min_stack=[-2, -2]
# top() = 0,   getMin() = -2
```

**Checkpoint:** All assertions pass. Manually verify the `min_stack` state after each operation.

---

## Part 3 — Monotonic Stack and Two-Stack Queue

**File:** `lab03_advanced.py`

### 3.1 — Daily Temperatures (LeetCode #739)

```python
def daily_temperatures(temps):
    """
    For each day, return the number of days until a warmer temperature.
    If no warmer day exists, return 0 for that day.
    Time: O(n), Space: O(n)
    """
    result = [0] * len(temps)
    stack = []   # indices; temps[stack[-1]] is monotonically decreasing

    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result
```

Test:

```python
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]

print(daily_temperatures([30, 40, 50, 60]))
# [1, 1, 1, 0]

print(daily_temperatures([30, 60, 90]))
# [1, 1, 0]
```

Trace exercise — fill in the stack state for `[73, 74, 75, 71, 69, 72, 76, 73]`:

```python
# i=0, temp=73: push 0.       stack=[0]        result=[0,0,0,0,0,0,0,0]
# i=1, temp=74: pop 0, r[0]=1. push 1. stack=[1]
# i=2, temp=75: pop 1, r[1]=1. push 2. stack=[2]
# i=3, temp=71: 71<75, push 3. stack=[2,3]
# i=4, temp=69: 69<71, push 4. stack=[2,3,4]
# i=5, temp=72: pop 4, r[4]=1. pop 3, r[3]=2. 72<75, push 5. stack=[2,5]
# i=6, temp=76: pop 5, r[5]=1. pop 2, r[2]=4. push 6. stack=[6]
# i=7, temp=73: 73<76, push 7. stack=[6,7]
# Remaining in stack: indices 6,7 — no warmer day — result stays 0.
```

**Checkpoint:** Local tests produce the expected output. Submit to LeetCode #739.

---

### 3.2 — Implement Queue using Stacks (LeetCode #232)

```python
class MyQueue:
    """
    Queue implemented with two stacks (inbox and outbox).
    All operations are O(1) amortized.
    """
    def __init__(self):
        self.inbox = []    # new elements pushed here
        self.outbox = []   # elements dequeued from here

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

Test:

```python
mq = MyQueue()
mq.push(1)
mq.push(2)
mq.push(3)
print(mq.peek())   # 1 — FIFO: first pushed is first peeked
print(mq.pop())    # 1
print(mq.pop())    # 2
mq.push(4)
print(mq.pop())    # 3
print(mq.pop())    # 4
print(mq.empty())  # True
```

Amortized analysis exercise:

```python
# Each element undergoes exactly 3 O(1) operations over its lifetime:
# 1. push() to inbox
# 2. inbox.pop() during _transfer()
# 3. outbox.pop() during pop()
# Total work per element = O(1) amortized, regardless of when _transfer fires.
```

**Checkpoint:** All test cases produce FIFO output. Submit to LeetCode #232.

---

### 3.3 — Test All Locally

```python
# Quick integration test
if __name__ == '__main__':
    # Valid parentheses
    assert is_valid('()[]{') == False
    assert is_valid('([{}])') == True

    # Daily temperatures
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    # Two-stack queue
    q = MyQueue()
    for v in [10, 20, 30]:
        q.push(v)
    assert q.pop() == 10
    assert q.pop() == 20
    assert q.peek() == 30

    print('All assertions passed.')
```

**Checkpoint:** Script runs without assertion errors. Submit #20, #739, #232 to LeetCode.

---

## Deliverables

Submit to Canvas:

1. `lab03_stack_queue.py` — Stack and Queue implementations with test output
2. `lab03_patterns.py` — Valid Parentheses and Min Stack with test output
3. `lab03_advanced.py` — Daily Temperatures and two-stack queue with trace comments
4. LeetCode submission screenshots for #20, #155, #739, and #232

---

## Summary

| Concept | Key Point |
|---|---|
| Stack (LIFO) | push/pop/peek all O(1) using Python list |
| Queue (FIFO) | enqueue/dequeue O(1) using collections.deque — never list.pop(0) |
| Valid parentheses | Push openers, pop on closers, return stack.empty() |
| Min stack | Parallel min_stack tracks running minimum — getMin() is O(1) |
| Monotonic stack | Pop while new element breaks order; each element pushed/popped once = O(n) |
| Daily temperatures | Monotonic decreasing stack of indices — result[idx] = i - idx |
| Two-stack queue | inbox + outbox; _transfer only when outbox empty; O(1) amortized |
| Amortized O(1) | Each element moves at most once per stack — total work O(n) over n ops |
