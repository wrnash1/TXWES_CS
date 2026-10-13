# Lab Activity: Module 02 — Singly and Doubly Linked Lists

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement a complete singly linked list with a tail pointer
- **Part 2** — Implement a doubly linked list and build an LRU cache
- **Part 3** — Linked list interview patterns on LeetCode

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Singly Linked List

**File:** `lab02_singly.py`

### 1.1 — Node and List Classes

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return ' -> '.join(str(v) for v in self.to_list()) + ' -> None'
```

### 1.2 — Prepend and Append

```python
    def prepend(self, value):
        """Insert at head — O(1)"""
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def append(self, value):
        """Insert at tail — O(1) using tail pointer"""
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
```

Test:

```python
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
print(ll)          # 0 -> 1 -> 2 -> 3 -> None
print(len(ll))     # 4
```

**Checkpoint:** Output matches expected. `len()` returns 4.

---

### 1.3 — Search, Delete, and to_list

```python
    def to_list(self):
        """Return Python list of values — O(n)"""
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def search(self, value):
        """Return node with value, or None — O(n)"""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        """Remove first node with this value — O(n)"""
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next is self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
```

Test:

```python
ll = SinglyLinkedList()
for v in [10, 20, 30, 40, 50]:
    ll.append(v)

print(ll.search(30))        # <Node object>
print(ll.search(99))        # None
ll.delete(30)
print(ll)                   # 10 -> 20 -> 40 -> 50 -> None
ll.delete(10)               # delete head
print(ll)                   # 20 -> 40 -> 50 -> None
ll.delete(50)               # delete tail
print(ll)                   # 20 -> 40 -> None
print(ll.tail.value)        # 40 — tail updated correctly
```

**Checkpoint:** All deletions work correctly. Tail pointer updates when the tail is deleted.

---

### 1.4 — Insert at Position

```python
    def insert_at(self, index, value):
        """Insert at given index (0-based) — O(n)"""
        if index < 0 or index > self.size:
            raise IndexError('Index out of range')
        if index == 0:
            self.prepend(value)
            return
        if index == self.size:
            self.append(value)
            return
        node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        node.next = current.next
        current.next = node
        self.size += 1
```

Test:

```python
ll = SinglyLinkedList()
for v in [1, 2, 4, 5]:
    ll.append(v)
ll.insert_at(2, 3)
print(ll)   # 1 -> 2 -> 3 -> 4 -> 5 -> None
```

**Checkpoint:** Value 3 inserted at index 2, shifting 4 and 5 right.

---

## Part 2 — Doubly Linked List and LRU Cache

**File:** `lab02_doubly.py`

### 2.1 — Doubly Linked List

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

    def append(self, value):
        """Add to tail — O(1)"""
        node = DNode(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node   # return node reference for O(1) delete

    def prepend(self, value):
        """Add to head — O(1)"""
        node = DNode(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return node

    def delete_node(self, node):
        """Remove a known node — O(1)"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None
        self.size -= 1

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.value)
            cur = cur.next
        return result

    def to_list_reverse(self):
        result, cur = [], self.tail
        while cur:
            result.append(cur.value)
            cur = cur.prev
        return result
```

Test:

```python
dl = DoublyLinkedList()
n1 = dl.append(1)
n2 = dl.append(2)
n3 = dl.append(3)
print(dl.to_list())          # [1, 2, 3]
print(dl.to_list_reverse())  # [3, 2, 1]
dl.delete_node(n2)           # delete middle node
print(dl.to_list())          # [1, 3]
dl.delete_node(n1)           # delete head
print(dl.to_list())          # [3]
print(dl.head.value)         # 3
print(dl.tail.value)         # 3
```

**Checkpoint:** Forward and reverse traversals are correct. Deleting head/middle/tail all work correctly.

---

### 2.2 — LRU Cache

An LRU (Least Recently Used) cache evicts the least recently accessed item when capacity is exceeded.

Design: maintain a doubly linked list where the tail is the most recently used item and the head is the least recently used. A hash map maps keys to their `DNode` references.

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}                  # key → DNode
        self.dll = DoublyLinkedList()  # (key, value) tuples in order

    def _move_to_tail(self, node):
        """Mark node as most recently used"""
        self.dll.delete_node(node)
        new_node = self.dll.append(node.value)
        self.map[node.value[0]] = new_node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_tail(node)
        return self.map[key].value[1]

    def put(self, key, value):
        if key in self.map:
            self.dll.delete_node(self.map[key])
            del self.map[key]
        elif self.dll.size == self.capacity:
            lru_node = self.dll.head
            del self.map[lru_node.value[0]]
            self.dll.delete_node(lru_node)
        new_node = self.dll.append((key, value))
        self.map[key] = new_node
```

Test:

```python
cache = LRUCache(3)
cache.put(1, 'one')
cache.put(2, 'two')
cache.put(3, 'three')
print(cache.get(1))    # 'one'  — 1 is now most recently used
cache.put(4, 'four')   # capacity exceeded; evict LRU = key 2
print(cache.get(2))    # -1     — key 2 was evicted
print(cache.get(3))    # 'three'
print(cache.get(4))    # 'four'
```

**Checkpoint:** `get(2)` returns -1 because key 2 was the least recently used when 4 was inserted.

---

## Part 3 — Linked List Interview Patterns

**File:** `lab02_patterns.py`

Implement each function from scratch, then submit to LeetCode to verify.

### 3.1 — Reverse a Linked List (LeetCode #206)

```python
def reverse_list(head):
    """
    Reverse a singly linked list in place.
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

### 3.2 — Detect Cycle (LeetCode #141)

```python
def has_cycle(head):
    """
    Detect if a linked list has a cycle using Floyd's algorithm.
    Time: O(n), Space: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

### 3.3 — Find Middle Node (LeetCode #876)

```python
def middle_node(head):
    """
    Return the middle node. For even-length lists, return the second middle.
    Time: O(n), Space: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### 3.4 — Remove Nth Node from End (LeetCode #19)

```python
def remove_nth_from_end(head, n):
    """
    Remove the nth node from the end of the list.
    Time: O(L), Space: O(1) — L = length of list
    """
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

### 3.5 — Test Locally

Build a helper to construct a linked list from a Python list:

```python
def make_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

def list_to_array(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

# Test reverse
head = make_list([1, 2, 3, 4, 5])
print(list_to_array(reverse_list(head)))   # [5, 4, 3, 2, 1]

# Test middle
head = make_list([1, 2, 3, 4, 5])
print(middle_node(head).value)             # 3

head = make_list([1, 2, 3, 4])
print(middle_node(head).value)             # 3 (second middle for even length)

# Test remove nth from end
head = make_list([1, 2, 3, 4, 5])
print(list_to_array(remove_nth_from_end(head, 2)))   # [1, 2, 3, 5]
```

**Checkpoint:** All local tests pass. Submit each function to LeetCode and confirm all test cases pass.

---

## Deliverables

Submit to Canvas:

1. `lab02_singly.py` — complete singly linked list with all operations tested
2. `lab02_doubly.py` — doubly linked list + LRU cache with test output
3. `lab02_patterns.py` — all four interview pattern functions with local test output
4. LeetCode submission screenshots for #206, #141, #876, and #19

---

## Summary

| Concept | Key Point |
|---|---|
| Singly prepend | O(1) — link new node to head, update head |
| Singly append (with tail) | O(1) — link tail to new node, update tail |
| Singly delete | O(n) — find predecessor, bypass target |
| Doubly delete_node | O(1) — update prev/next on both neighbors |
| Two-pointer (slow/fast) | O(n) time, O(1) space for middle/cycle |
| Reversal | Three pointers: prev, current, next_node |
| LRU cache | Doubly linked list + hash map — both ops O(1) |
| Dummy head | Eliminates head-deletion edge case |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — Cycle Entry Point Detection

Floyd's algorithm can do more than detect whether a cycle exists — it can find the exact node where the cycle begins. After `slow` and `fast` meet inside the cycle, reset one pointer to `head` and advance both one step at a time. The node where they meet again is the cycle entry point. Implement `find_cycle_entry(head)` that returns the entry node (or `None` if no cycle), verify it on a hand-crafted cycle, and explain in a comment why the two-pointer reset proves correctness mathematically.

### 9.2 — Merge K Sorted Linked Lists

Implement `merge_k_sorted(lists)` where `lists` is a Python list of `k` sorted singly linked list heads. Use a min-heap (`heapq`) to always extract the smallest current head across all lists. The time complexity should be O(N log k) where N is the total number of nodes and k is the number of lists. Compare this to the naive O(Nk) approach of merging lists one pair at a time, and add a comment explaining why the heap approach is asymptotically superior for large k. This is LeetCode #23.

### 9.3 — Reorder List In-Place

LeetCode #143 asks you to reorder a list `L₀ → L₁ → … → Lₙ` into `L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → Lₙ₋₂ → …` in O(n) time and O(1) extra space. The solution requires three techniques from this module in sequence: (1) find the middle using fast-slow pointers, (2) reverse the second half in place, then (3) interleave the two halves. Implement the complete solution, verify it locally on lists of both odd and even length, and annotate each of the three phases with its time and space complexity.
