# Lab Activity: Module 16 — Final Exam Prep & Certification Submission

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has two parts:

- **Part 1** — Final practice: implement six canonical algorithms from memory
- **Part 2** — Certification exam submission

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Implement From Memory

The goal of this part is to reproduce six canonical algorithms without referencing notes. This simulates interview conditions. Close your notes. Open a blank Python file named `lab16_final.py`. Implement each function from memory, then verify against the expected outputs.

---

### 1.1 — Binary Search (Module 12)

Implement standard binary search returning the index of `target` in sorted `arr`, or -1 if not found.

```python
# Implement from memory, then verify:
# binary_search([1,3,5,7,9,11,13,15], 7)  → 3
# binary_search([1,3,5,7,9,11,13,15], 6)  → -1
# binary_search([], 5)                     → -1
```

---

### 1.2 — BFS Shortest Path (Module 10)

Implement BFS returning a dict of shortest distances from `start` to all reachable nodes in an unweighted graph.

```python
# Implement from memory, then verify:
# graph = {'A':['B','C'], 'B':['D'], 'C':['D','E'], 'D':[], 'E':[]}
# bfs_distances(graph, 'A')
# → {'A':0, 'B':1, 'C':1, 'D':2, 'E':2}
```

---

### 1.3 — Dijkstra (Module 11)

Implement Dijkstra returning a dict of shortest distances from `start` to all nodes.

```python
# Implement from memory, then verify:
# graph = {
#     'A': [('B',1),('C',4)],
#     'B': [('C',2),('D',5)],
#     'C': [('D',1)],
#     'D': []
# }
# dijkstra(graph, 'A')
# → {'A':0, 'B':1, 'C':3, 'D':4}
```

---

### 1.4 — Coin Change (Module 14)

Implement `coin_change(coins, amount)` returning the minimum number of coins, or -1 if impossible.

```python
# Implement from memory, then verify:
# coin_change([1,5,6,9], 11)   → 2
# coin_change([2], 3)           → -1
# coin_change([1], 0)           → 0
```

---

### 1.5 — Longest Common Subsequence (Module 14)

Implement `lcs(text1, text2)` returning the length of the longest common subsequence.

```python
# Implement from memory, then verify:
# lcs('abcde', 'ace')   → 3
# lcs('abc', 'def')     → 0
# lcs('abc', 'abc')     → 3
```

---

### 1.6 — Longest Substring Without Repeating Characters (Module 15)

Implement `length_of_longest_substring(s)`.

```python
# Implement from memory, then verify:
# length_of_longest_substring('abcabcbb')   → 3
# length_of_longest_substring('bbbbb')      → 1
# length_of_longest_substring('')           → 0
```

---

### 1.7 — Reference Implementations and Integration Test

After attempting from memory, compare to the reference implementations below:

```python
from collections import deque, Counter
import heapq

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

def bfs_distances(graph, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]: continue
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

def test_all():
    assert binary_search([1,3,5,7,9,11,13,15], 7) == 3
    assert binary_search([1,3,5,7,9,11,13,15], 6) == -1
    assert binary_search([], 5) == -1

    graph_bfs = {'A':['B','C'],'B':['D'],'C':['D','E'],'D':[],'E':[]}
    assert bfs_distances(graph_bfs, 'A') == {'A':0,'B':1,'C':1,'D':2,'E':2}

    graph_dijk = {'A':[('B',1),('C',4)],'B':[('C',2),('D',5)],'C':[('D',1)],'D':[]}
    assert dijkstra(graph_dijk, 'A') == {'A':0,'B':1,'C':3,'D':4}

    assert coin_change([1,5,6,9], 11) == 2
    assert coin_change([2], 3) == -1

    assert lcs('abcde', 'ace') == 3
    assert lcs('abc', 'def') == 0

    assert length_of_longest_substring('abcabcbb') == 3
    assert length_of_longest_substring('bbbbb') == 1

    print('All integration tests passed.')

test_all()
```

**Checkpoint:** All integration tests pass. Note any algorithms you struggled to implement from memory — those are your study targets before the certification exam.

---

## Part 2 — Certification Exam Submission

### Objective

Schedule and complete the official **Technical Interview Readiness** certification exam and submit your score verification report to Professor Nash.

### Instructions

1. Register for the exam at the on-campus testing center or an authorized provider.
2. Complete the exam.
3. Obtain your official score report PDF showing your name, passing status, and date.
4. Upload the official score report PDF to the Canvas LMS assignment box for this module to receive final credit.

### Preparation Checklist

Before sitting for the exam, confirm you can implement the following from memory:

- [ ] Binary search (standard, leftmost, on-answer)
- [ ] BFS with distance tracking
- [ ] DFS with cycle detection (three-color)
- [ ] Topological sort (Kahn's or DFS post-order)
- [ ] Dijkstra with stale-entry check
- [ ] Merge sort
- [ ] Coin Change (DP)
- [ ] Longest Common Subsequence (DP)
- [ ] Trie insert and search
- [ ] Sliding window for longest substring without repeating characters

### Exam Tips

- Read each problem statement twice. Confirm input constraints (sorted? unique values? return type?).
- State brute force complexity first, then optimize.
- Write clean variable names. Interviewers read your code as you type.
- Test your solution on the given examples before submitting.
- If stuck, reduce to a simpler subproblem you do know how to solve.

---

## Deliverables

Submit to Canvas:

1. `lab16_final.py` — all six implementations and integration test (Part 1)
2. Certification exam score report PDF (Part 2)
3. Short self-assessment (3–5 sentences): Which algorithm family from this course was most challenging for you to master? What specific technique or insight finally made it click? What would you recommend to a future CIS-2315 student struggling with the same concept?
