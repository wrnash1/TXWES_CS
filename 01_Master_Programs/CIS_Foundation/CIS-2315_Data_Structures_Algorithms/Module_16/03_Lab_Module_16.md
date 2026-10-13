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

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to go beyond the core curriculum and build advanced interview readiness.

### 9.1 — Mock Interview: 45-Minute Timed Session

Simulate a real technical interview. Set a 45-minute timer and attempt all three problems without notes or autocomplete. Then review each solution against the reference implementations. Problems: (1) LeetCode #200 (Number of Islands) — use BFS or DFS to count connected components in a 2D grid. (2) LeetCode #300 (Longest Increasing Subsequence) — implement the O(n²) DP solution, then the O(n log n) patience sort. (3) LeetCode #56 (Merge Intervals) — sort intervals by start time, then greedily merge overlapping pairs. After the timer ends, write a 3-sentence self-assessment: what did you get right, where did you struggle, and which concept needs one more review session before the exam.

### 9.2 — System Design: Design a Spell Checker

Design a spell checker that: (1) checks if a word is correctly spelled in O(L), (2) returns all correctly spelled words that are within edit distance 1 of the input (one insertion, deletion, or substitution), and (3) returns all words that start with the input as a prefix in O(L + output). Choose the data structures for each operation and justify your choice. Implement the edit distance 1 generation function `generate_candidates(word, alphabet)` that returns all strings within edit distance 1 of `word` (this set has O(L × A) elements). Then filter candidates through the spell checker's dictionary using a Trie or hash set. Analyze the time and space complexity of the full system for a dictionary of N words each of average length L.

### 9.3 — End-to-End Algorithm Portfolio Review

For each of the 10 algorithm families below, write a 2-sentence summary explaining (a) the core insight and (b) the canonical LeetCode problem that best illustrates it. Do this from memory, then compare against the course materials. The 10 families: (1) Binary Search, (2) Two Pointers / Sliding Window, (3) BFS / DFS, (4) Topological Sort, (5) Dijkstra's Algorithm, (6) Merge Sort / Divide & Conquer, (7) Greedy (Activity Selection), (8) Dynamic Programming 1D (Coin Change), (9) Dynamic Programming 2D (LCS), (10) Trie. This exercise identifies any remaining gaps before the certification exam and produces a personal one-page cheat sheet.
