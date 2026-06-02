# Lab Activity: Module 11 — Dijkstra's Shortest Path Algorithm

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement Dijkstra's algorithm with distance tracking
- **Part 2** — Add path reconstruction and handle disconnected graphs
- **Part 3** — LeetCode: Network Delay Time (#743)

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Dijkstra's Algorithm

**File:** `lab11_dijkstra.py`

### Setup: Graph Builder

```python
import heapq
from collections import defaultdict

def build_weighted_directed(edges):
    """Build directed weighted adjacency list from (u, v, weight) tuples."""
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    return graph

def build_weighted_undirected(edges):
    """Build undirected weighted adjacency list from (u, v, weight) tuples."""
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph
```

---

### 1.1 — Core Dijkstra

```python
def dijkstra(graph, start):
    """
    Shortest distances from start to all reachable nodes.
    Returns {node: distance}.
    Time: O((V + E) log V)
    """
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]    # (distance, node)

    while heap:
        d, node = heapq.heappop(heap)

        if d > dist[node]:
            continue    # stale entry — skip

        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist
```

Test:

```python
edges = [
    ('A','B',4), ('A','D',2),
    ('B','C',8), ('B','E',1),
    ('D','E',3),
    ('E','F',1),
    ('C','F',2)
]
g = build_weighted_directed(edges)

dist = dijkstra(g, 'A')
print(dist)
# {'A': 0, 'B': 4, 'D': 2, 'C': 10, 'E': 5, 'F': 6}

print(dist['A'])    # 0
print(dist['D'])    # 2 — direct edge
print(dist['E'])    # 5 — via D: 2+3
print(dist['F'])    # 6 — via D→E→F: 2+3+1
print(dist['C'])    # 10 — via D→E→B→C? No. Via B: 4+8=12 or via F→C? No back edge.
                    # Actually via A→B→E→... let's trace:
                    # A→D→E(5)→B(4+1=5 vs A→B=4, so dist[B]=4), dist[B] stays 4
                    # A→B(4)→C(12), A→B(4)→E(5 = same as D→E)
                    # F→C? No edge in this directed graph. dist[C]=12 via B→C.
                    # Correction: dist[C]=12 (via A→B(4)→C(8)), not 10.
```

**Corrected trace:**

```text
edges directed, so only forward edges exist.
A→B(4), A→D(2), B→C(8), B→E(1), D→E(3), E→F(1), C→F(2)

dist: {A:0, B:inf, D:inf, C:inf, E:inf, F:inf}, heap=[(0,A)]

Pop(0,A): B→4, D→2  →  dist={B:4,D:2}, heap=[(2,D),(4,B)]
Pop(2,D): E→2+3=5   →  dist={E:5},      heap=[(4,B),(5,E)]
Pop(4,B): C→4+8=12, E→4+1=5 (=dist[E], no update)  →  dist={C:12}, heap=[(5,E),(12,C)]
Pop(5,E): F→5+1=6   →  dist={F:6},      heap=[(6,F),(12,C)]
Pop(6,F): (no outgoing edges in this directed graph)
Pop(12,C): F→12+2=14 > dist[F]=6, no update

Final: {A:0, B:4, C:12, D:2, E:5, F:6}
```

```python
# Corrected expected output:
assert dist['A'] == 0
assert dist['D'] == 2
assert dist['B'] == 4
assert dist['E'] == 5
assert dist['F'] == 6
assert dist['C'] == 12
print('Dijkstra distances verified.')
```

**Checkpoint:** All assertions pass. `dist['F']` = 6 via A→D→E→F.

---

### 1.2 — Step Trace Verification

```python
def dijkstra_verbose(graph, start):
    """Same as dijkstra but prints each pop operation."""
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    step = 0

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            print(f'  Step {step}: skip stale ({d}, {node})')
            step += 1
            continue

        print(f'  Step {step}: pop ({d}, {node}), dist[{node}]={dist[node]}')
        step += 1

        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
                print(f'    update dist[{neighbor}] = {new_dist}')

    return dist

g2 = build_weighted_undirected([('A','B',1),('A','C',4),('B','C',2),('B','D',5),('C','D',1)])
print('Dijkstra trace from A:')
dijkstra_verbose(g2, 'A')
```

**Checkpoint:** Step-by-step output confirms the algorithm processes nodes in order of increasing distance. Observe when stale entries are skipped.

---

## Part 2 — Path Reconstruction and Disconnected Graphs

### 2.1 — Path Reconstruction

```python
def dijkstra_path(graph, start, end):
    """
    Returns (path, distance) from start to end.
    path: list of nodes from start to end.
    distance: total cost of the shortest path.
    Returns ([], float('inf')) if end is unreachable.
    """
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        if node == end:
            break    # early exit
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    if dist[end] == float('inf'):
        return [], float('inf')    # unreachable

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path, dist[end]
```

Test:

```python
g3 = build_weighted_undirected([
    ('A','B',1), ('A','C',4), ('B','C',2), ('B','D',5), ('C','D',1)
])

path, cost = dijkstra_path(g3, 'A', 'D')
print(path, cost)    # ['A', 'B', 'C', 'D'], 4

path2, cost2 = dijkstra_path(g3, 'A', 'A')
print(path2, cost2)  # ['A'], 0
```

**Checkpoint:** Shortest path A→D is `['A','B','C','D']` with cost 4 (1+2+1).

---

### 2.2 — Disconnected Graph Handling

```python
def dijkstra_safe(graph, start):
    """
    Dijkstra that returns 'unreachable' for nodes with no path from start.
    Handles nodes that appear only as edge destinations (not as keys in graph).
    """
    # Collect all nodes including edge destinations
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            all_nodes.add(neighbor)

    dist = {node: float('inf') for node in all_nodes}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist

# Graph where node 'Z' is unreachable from 'A'
g4 = build_weighted_undirected([('A','B',1),('B','C',2)])
g4['Z']    # isolated node — no edges

dist4 = dijkstra_safe(g4, 'A')
print(dist4['A'])    # 0
print(dist4['C'])    # 3
print(dist4['Z'])    # inf — unreachable
```

**Checkpoint:** `dist4['Z']` = `inf` confirming Z is unreachable.

---

## Part 3 — LeetCode: Network Delay Time (#743)

**File:** (add to `lab11_dijkstra.py`)

### 3.1 — Implementation

```python
def network_delay_time(times, n, k):
    """
    LeetCode #743: minimum time for signal from node k to reach all n nodes.
    times: list of [u, v, w] directed edges (1-indexed nodes).
    Returns max(shortest distances) or -1 if any node is unreachable.
    Time: O((V + E) log V)
    """
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n+1)}
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1
```

Test:

```python
print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2))   # 2
print(network_delay_time([[1,2,1]], 2, 1))                    # 1
print(network_delay_time([[1,2,1]], 2, 2))                    # -1 (node 1 unreachable from 2)
```

**Checkpoint:** All three tests pass. Submit to LeetCode #743.

---

### 3.2 — Integration Test

```python
def test_all():
    # Basic Dijkstra
    g = build_weighted_directed([
        ('A','B',4),('A','D',2),('B','C',8),('B','E',1),
        ('D','E',3),('E','F',1),('C','F',2)
    ])
    d = dijkstra(g, 'A')
    assert d['A'] == 0
    assert d['D'] == 2
    assert d['B'] == 4
    assert d['E'] == 5
    assert d['F'] == 6
    assert d['C'] == 12

    # Path reconstruction
    g2 = build_weighted_undirected([
        ('A','B',1),('A','C',4),('B','C',2),('B','D',5),('C','D',1)
    ])
    path, cost = dijkstra_path(g2, 'A', 'D')
    assert cost == 4
    assert path[0] == 'A' and path[-1] == 'D'

    # Network Delay Time
    assert network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    assert network_delay_time([[1,2,1]], 2, 2) == -1

    print('All assertions passed.')

test_all()
```

**Checkpoint:** All assertions pass. LeetCode #743 submitted.

---

## Deliverables

Submit to Canvas:

1. `lab11_dijkstra.py` — dijkstra, dijkstra_verbose, dijkstra_path, network_delay_time, integration test
2. LeetCode submission screenshot for #743
3. Short written answer (3–5 sentences): In the step trace from Section 1.2, identify one moment when a stale heap entry was skipped. What distance was popped, what was the current `dist` value, and why was the entry stale?

---

## Summary

| Concept | Key Point |
|---|---|
| Dijkstra = BFS + min-heap | Replace queue with `heapq`; push `(dist, node)` tuples |
| Initialization | `dist[source]=0`; all others = `float('inf')` |
| Stale entry check | `if d > dist[node]: continue` |
| Edge relaxation | `if dist[node] + w < dist[neighbor]`: update and push |
| Path reconstruction | `prev` dict; walk back from end, then reverse |
| Negative weights | Dijkstra fails — use Bellman-Ford instead |
| Network Delay Time | `max(dist.values())` after Dijkstra from source k |
| Disconnected nodes | Remain `float('inf')` — return -1 if any unreachable |
