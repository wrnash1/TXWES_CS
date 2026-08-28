# Reading Guide: Module 02 — Singly and Doubly Linked Lists

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

Linked lists are the foundation of pointer-based data structure thinking. They appear directly in interview problems (reverse a list, detect a cycle, find the middle) and their node-and-reference structure reappears in trees, graphs, and more complex containers. This module covers the implementation of both singly and doubly linked lists, the complexity of every operation, and the core two-pointer patterns that solve five of the most common linked list interview problems.

---

## 1. Singly Linked List

### Structure

A singly linked list consists of nodes where each node holds a value and a reference to the next node. The list maintains a `head` pointer; if `head` is `None`, the list is empty.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # optional: enables O(1) append
        self.size = 0
```

### Core Operations

#### Prepend — O(1)

```python
def prepend(self, value):
    node = Node(value)
    node.next = self.head
    self.head = node
    if self.tail is None:
        self.tail = node
    self.size += 1
```

#### Append — O(1) with tail pointer

```python
def append(self, value):
    node = Node(value)
    if self.tail is None:
        self.head = self.tail = node
    else:
        self.tail.next = node
        self.tail = node
    self.size += 1
```

#### Delete by Value — O(n)

```python
def delete(self, value):
    if not self.head:
        return
    if self.head.value == value:
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return
    current = self.head
    while current.next:
        if current.next.value == value:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            self.size -= 1
            return
        current = current.next
```

#### Search — O(n)

```python
def search(self, value):
    current = self.head
    while current:
        if current.value == value:
            return current
        current = current.next
    return None
```

**Traversal pattern (used in every operation):**

```python
current = self.head
while current:
    # process current.value
    current = current.next
```

---

## 2. Doubly Linked List

### Structure

Each node in a doubly linked list has both a `next` and a `prev` pointer. The list maintains both `head` and `tail` pointers.

```python
class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
```

### Doubly List Append and Prepend — O(1)

```python
def append(self, value):
    node = DNode(value)
    if not self.tail:
        self.head = self.tail = node
    else:
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    self.size += 1

def prepend(self, value):
    node = DNode(value)
    if not self.head:
        self.head = self.tail = node
    else:
        node.next = self.head
        self.head.prev = node
        self.head = node
    self.size += 1
```

### Delete by Node Reference — O(1)

This is the key advantage over a singly linked list. Given a `DNode` reference, deletion is O(1):

```python
def delete_node(self, node):
    if node.prev:
        node.prev.next = node.next
    else:
        self.head = node.next

    if node.next:
        node.next.prev = node.prev
    else:
        self.tail = node.prev

    self.size -= 1
```

Four cases to handle: node has prev, node has next, node is head, node is tail. Always update both directions.

---

## 3. Complexity Summary

| Operation | Singly (no tail) | Singly (with tail) | Doubly |
|---|---|---|---|
| Prepend | O(1) | O(1) | O(1) |
| Append | O(n) | O(1) | O(1) |
| Insert at position k | O(k) | O(k) | O(k) |
| Delete by value | O(n) | O(n) | O(n) |
| Delete by node reference | O(n)* | O(n)* | O(1) |
| Search | O(n) | O(n) | O(n) |
| Access by index | O(n) | O(n) | O(n) |
| Space | O(n) | O(n) | O(n) |

*Singly linked list deletion by node reference is O(n) because you must find the preceding node.

---

## 4. Arrays vs Linked Lists

| Feature | Array (Python list) | Linked List |
|---|---|---|
| Access by index | O(1) | O(n) |
| Prepend | O(n) — shifts all | O(1) |
| Append | O(1) amortized | O(1) with tail pointer |
| Insert at position k | O(n) — shifts | O(k) traversal + O(1) link |
| Delete at position k | O(n) — shifts | O(k) traversal + O(1) unlink |
| Memory | Contiguous — cache-friendly | Non-contiguous — pointer overhead |
| Fixed capacity? | No (Python list grows) | No |

**When to choose a linked list:**

- Frequent insertions/deletions at arbitrary positions
- Need O(1) delete by node reference (doubly linked)
- Building a queue with O(1) enqueue and dequeue
- When cache performance is not critical

**When to choose an array (Python list):**

- Frequent random access by index
- Iterating through all elements sequentially
- Space efficiency matters (no pointer overhead)

---

## 5. Two-Pointer Technique

The fast-slow pointer pattern solves several classic linked list problems in O(n) time and O(1) space.

### Find Middle Node

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

When `fast` reaches the end, `slow` is at the midpoint.

### Detect Cycle (Floyd's Algorithm)

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

If a cycle exists, `fast` will eventually lap `slow` and they will point to the same node.

### Remove Nth Node from End

```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```

Advance `fast` by n+1 steps first; then move both until `fast` is None. `slow` is now just before the node to remove. The dummy head simplifies the edge case of removing the head.

### Reverse a Linked List

```python
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

Three-pointer technique: always save `current.next` before overwriting it. Returns the new head.

---

## 6. LRU Cache — Doubly Linked List + Hash Map

The Least Recently Used (LRU) cache is a classic interview problem (LeetCode #146) that requires O(1) `get` and `put` operations.

Design: a doubly linked list maintains the usage order (most recent at tail, least recent at head). A hash map provides O(1) node access.

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}          # key → DNode
        self.list = DoublyLinkedList()

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self.list.delete_node(node)
        self.list.append(node.value)    # move to most-recently-used end
        self.map[key] = self.list.tail
        return node.value[1]            # value stored as (key, val) tuple

    def put(self, key, value):
        if key in self.map:
            self.list.delete_node(self.map[key])
        elif self.list.size == self.capacity:
            lru = self.list.head
            del self.map[lru.value[0]]
            self.list.delete_node(lru)
        self.list.append((key, value))
        self.map[key] = self.list.tail
```

`get` and `put` are both O(1) — hash map for lookup, doubly linked list for O(1) delete and O(1) append.

---

## 7. Interview Exam Tips

1. **Always handle edge cases first:** empty list (`head is None`), single-node list, deleting the head or tail.

2. **Save `next` before modifying `next`:** In reversal and pointer manipulation, `next_node = current.next` before `current.next = prev`.

3. **Fast-slow pointer:** Use for cycle detection, finding middle, and kth-from-end problems. It is O(n) time, O(1) space — always preferred over a visited set.

4. **Dummy head node:** Adding a `dummy.next = head` node eliminates special cases for deleting the head. Remove it at the end with `return dummy.next`.

5. **Doubly linked list for O(1) delete:** When a problem requires deleting the current node efficiently, the answer is a doubly linked list. Singly linked deletion by node reference is O(n).

6. **`tail` pointer for O(1) append:** Without a tail pointer, appending requires O(n) traversal. Maintaining a `tail` reference is almost always worth it.

7. **Draw the list before coding:** For complex pointer operations (reversal, merge), drawing the before and after states prevents mistakes.

8. **LRU cache = doubly linked list + hash map:** This is the canonical use of doubly linked lists in interviews. Know it cold.

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Linked List Visualizations** — [https://visualgo.net/en/list](https://visualgo.net/en/list)
   Step-by-step animated visualizations of singly and doubly linked list insertions, deletions, and searches. Watch the pointer arrows update in real time to build intuition before coding.

2. **OpenDSA — Lists Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/ListADT.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/ListADT.html)
   Interactive OER textbook chapter covering list ADTs, singly linked lists, and doubly linked lists with embedded practice exercises and complexity analysis.

3. **LeetCode Explore: Linked List** — [https://leetcode.com/explore/learn/card/linked-list/](https://leetcode.com/explore/learn/card/linked-list/)
   Free LeetCode learning card with explanations, code examples, and practice problems specifically covering singly linked lists, doubly linked lists, and two-pointer techniques. No premium required.

4. **CS50 — Week 5: Data Structures (Harvard)** — [https://cs50.harvard.edu/x/2024/weeks/5/](https://cs50.harvard.edu/x/2024/weeks/5/)
   Free Harvard lecture covering linked lists from first principles with memory diagrams showing exactly how pointers work at the memory address level.

5. **Abdul Bari — Linked Lists Playlist (YouTube)** — [https://www.youtube.com/watch?v=NobHlGUjV3g](https://www.youtube.com/watch?v=NobHlGUjV3g)
   Clear video explanations of singly and doubly linked list operations with diagram-based walkthroughs of insertion, deletion, and reversal algorithms.

---

## 8. Study Checklist

- [ ] Watch the Module 02 video lecture by Professor Nash.
- [ ] Implement a singly linked list from scratch: prepend, append, delete, search, to_list.
- [ ] Add a tail pointer and confirm append is O(1).
- [ ] Implement a doubly linked list with O(1) append, prepend, and delete_node.
- [ ] Implement find_middle, has_cycle, reverse, and remove_nth_from_end.
- [ ] Solve LeetCode #206 (Reverse Linked List), #141 (Linked List Cycle), #876 (Middle of Linked List).
- [ ] Complete the Module 02 Lab.
- [ ] Complete the Module 02 Quiz.
