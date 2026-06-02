# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 02 — Singly and Doubly Linked Lists

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Linked lists are the first pointer-based data structure. Spend time on the mental model of nodes and references before writing any code — draw the boxes-and-arrows diagram explicitly.
> - The two-pointer / fast-slow pointer technique is a top interview pattern. Introduce it here in the context of cycle detection and finding the middle node — students will use it again in trees and graphs.
> - Common mistakes: losing the reference before updating it (causing memory leaks / lost nodes), off-by-one on head/tail updates, not handling the empty list case.
> - Python note: `None` plays the role of null pointer. Draw the distinction from arrays — no random access by index.
> - Doubly linked lists: keep the bi-directional update rule clear (`prev`, `next`, both pointers). The lab has students implement both.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 02 | Singly and Doubly Linked Lists | CIS-2315"]**

"Module 01 gave you the tools to measure algorithmic quality. Now we start building data structures. A linked list is the simplest dynamic data structure — a sequence of nodes connected by references — and it teaches you the pointer manipulation skills that appear in trees, graphs, and almost every interview problem involving in-place modification.

By the end of this module, you will be able to implement both singly and doubly linked lists from scratch in Python, perform all standard operations, and apply the two-pointer technique to solve classic linked list interview problems. Let us start with the mental model."

---

## [01:30 – 05:30] Part 1 — The Linked List Mental Model

**[SHOW SLIDE: "Linked Lists vs Arrays"]**

"An array stores elements in contiguous memory. You access element i in O(1) — just compute the address. The trade-off: inserting or deleting in the middle requires shifting, which is O(n).

A linked list stores elements in nodes scattered anywhere in memory. Each node holds a value and a reference to the next node.

```text
[head] → [5 | •] → [12 | •] → [8 | •] → [3 | None]
```

No contiguous memory. No O(1) index access — to reach the third element, you start at the head and follow two next pointers. That is O(n) access. The trade-off: inserting or deleting is O(1) once you have a pointer to the location — no shifting required.

[PAUSE]

**[DEMO — Node class in Python]**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None   # reference to next node; None means end of list
```

A `Node` object wraps a value and a pointer. The list itself is just a reference to the head node. If `head` is `None`, the list is empty.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
```

Notice: there is no array, no pre-allocated memory. The list grows by creating new `Node` objects and linking them together."

---

## [05:30 – 10:00] Part 2 — Core Operations

**[SHOW SLIDE: "Singly Linked List Operations"]**

"The fundamental operations are: insert at head, insert at tail, delete by value, and search.

**[DEMO]**

```python
def prepend(self, value):
    # Insert at head — O(1)
    new_node = Node(value)
    new_node.next = self.head   # new node points to old head
    self.head = new_node        # head now points to new node
    self.size += 1
```

Prepend is O(1) — no traversal needed. The key step: link the new node to the existing head before reassigning `self.head`. If you assign `self.head` first, you lose the reference to the rest of the list.

[PAUSE]

```python
def append(self, value):
    # Insert at tail — O(n) without a tail pointer
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.size += 1
        return
    current = self.head
    while current.next is not None:   # traverse to last node
        current = current.next
    current.next = new_node
    self.size += 1
```

Append requires traversing to the tail: O(n). Adding a `self.tail` pointer makes this O(1) — we will add that shortly.

[PAUSE]

```python
def delete(self, value):
    # Remove first node with this value — O(n)
    if self.head is None:
        return
    if self.head.value == value:   # special case: deleting head
        self.head = self.head.next
        self.size -= 1
        return
    current = self.head
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next   # bypass the node
            self.size -= 1
            return
        current = current.next
```

Deletion requires finding the node before the target so you can bypass it. This is O(n). The head special case is critical — always handle it explicitly.

[PAUSE]

```python
def to_list(self):
    # Convert to Python list for printing — O(n)
    result = []
    current = self.head
    while current:
        result.append(current.value)
        current = current.next
    return result
```

The traversal pattern — `current = self.head; while current: ...; current = current.next` — appears in virtually every linked list operation. Internalize it."

---

## [10:00 – 13:30] Part 3 — Doubly Linked Lists

**[SHOW SLIDE: "Doubly Linked List"]**

"A doubly linked list adds a `prev` pointer to each node, allowing traversal in both directions.

```text
None ← [5 | prev | next] ↔ [12 | prev | next] ↔ [8 | prev | next] → None
```

Each node has `prev` (pointing left) and `next` (pointing right). The list has both a `head` and a `tail` pointer.

**[DEMO]**

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
        # Insert at tail — O(1) with tail pointer
        new_node = DNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail    # new node points back to old tail
            self.tail.next = new_node    # old tail points forward to new node
            self.tail = new_node         # update tail pointer
        self.size += 1

    def delete_node(self, node):
        # Delete a specific node — O(1) given the node
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next        # deleting head

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev        # deleting tail

        self.size -= 1
```

`delete_node` is O(1) if you already have the node — no traversal. This is the key advantage of doubly linked lists: you can delete the current node without knowing the previous node."

---

## [13:30 – 17:30] Part 4 — Two-Pointer Technique

**[SHOW SLIDE: "Two Pointers on Linked Lists"]**

"Two of the most common linked list interview problems are: detecting a cycle, and finding the middle node. Both use the same technique: two pointers moving at different speeds.

**Finding the middle node:**

```python
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next         # moves one step
        fast = fast.next.next    # moves two steps
    return slow   # when fast reaches end, slow is at middle
```

When `fast` has traversed the full list, `slow` has traversed half. For a list of length 5, `fast` takes 2 full steps and hits the end; `slow` is at position 3 — the middle. This runs in O(n) time with O(1) space.

[PAUSE]

**Cycle detection (Floyd's algorithm):**

```python
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:   # pointers met — there is a cycle
            return True
    return False
```

If there is no cycle, `fast` will reach `None`. If there is a cycle, `fast` laps `slow` — they will meet at the same node. This is O(n) time and O(1) space — no visited set required.

[PAUSE]

**Reversing a linked list:**

```python
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next   # save next before overwriting
        current.next = prev        # reverse the pointer
        prev = current             # advance prev
        current = next_node        # advance current
    return prev   # prev is now the new head
```

Three-pointer technique: `prev`, `current`, `next_node`. Every reversal problem reduces to this pattern. The key: save `current.next` before overwriting it."

---

## [17:30 – 20:30] Part 5 — Complexity Summary

**[SHOW SLIDE: "Linked List Complexity"]**

"Let me summarize the complexity of each operation. This is what you say in an interview.

| Operation | Singly (no tail) | Singly (with tail) | Doubly |
|---|---|---|---|
| Prepend | O(1) | O(1) | O(1) |
| Append | O(n) | O(1) | O(1) |
| Insert at position | O(n) | O(n) | O(n) |
| Delete by value | O(n) | O(n) | O(n) |
| Delete by node ref | O(n) | O(n) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Access by index | O(n) | O(n) | O(n) |

Space: O(n) for n nodes.

[PAUSE]

The most important comparison: array vs linked list. Arrays give O(1) random access but O(n) insert/delete (shifting). Linked lists give O(n) access but O(1) insert/delete at a known position.

When do you choose a linked list over an array? When you are frequently inserting or deleting and rarely need index access. In practice, Python lists dominate — but linked lists appear constantly in interviews because they test pointer manipulation skills."

---

## [20:30 – 22:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 02 Lab Preview"]**

"The Module 02 lab has three parts.

Part 1 has you implement a complete singly linked list with all standard operations and a tail pointer for O(1) appends.

Part 2 has you implement a doubly linked list and use it to build an LRU cache — a classic interview problem that combines a doubly linked list with a hash map.

Part 3 covers linked list interview patterns: reversing a list, finding the middle, detecting a cycle, and removing the nth node from the end.

The quiz covers all operations and their complexities, the two-pointer technique, and array vs linked list trade-offs. Read the guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 02 — Singly and Doubly Linked Lists]**

---

## Additional Resources

- [VisuAlgo — Linked List Visualization](https://visualgo.net/en/list)
- [NeetCode — Linked List Playlist](https://www.youtube.com/watch?v=Hj_rA0dhr2I)
- [LeetCode #206 — Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [LeetCode #141 — Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [LeetCode #876 — Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
