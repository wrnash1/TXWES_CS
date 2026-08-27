# Reading Guide: Module 11 — Dijkstra's Shortest Path Algorithm

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Dijkstra's algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights. It extends BFS by replacing the FIFO queue with a min-heap (priority queue), always expanding the unvisited vertex with the smallest known distance. This greedy strategy guarantees that when a vertex is popped from the heap, its distance is final.

---

## 1. Algorithm

### Core Implementation

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Shortest distances from start to all reachable nodes.
    graph: {node: [(neighbor, weight), ...]}
    Returns dict {node: shortest_distance}.
    Time: O((V + E) log V), Space: O(V + E)
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

### Step-by-Step Logic

1. Initialize all distances to `float('inf')`, source distance to 0.
2. Push `(0, source)` onto the min-heap.
3. Pop the pair with the smallest distance.
4. If the popped distance is greater than the current best for that node, it is a stale entry — skip it.
5. For each neighbor, compute the candidate distance through the current node. If it improves the known best, update and push the new pair.

### Stale Entry Pattern

Dijkstra with a binary heap uses "lazy deletion": when a shorter path to a node is found, the old (larger) distance is not removed from the heap — it remains as a stale entry. The stale entry is detected and skipped at step 4. This is the standard interview implementation.

---

## 2. Path Reconstruction

To recover the actual shortest path (not just the distance), maintain a `prev` dictionary tracking which node each node was reached from:

```python
def dijkstra_path(graph, start, end):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        if node == end:
            break
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path, dist[end]
```

Reconstruction walks `prev` pointers from `end` back to `start`, then reverses to get the forward path.

---

## 3. Why Non-Negative Weights?

Dijkstra's greedy property: when a node is popped from the heap, its distance is final. This holds only if all edge weights are ≥ 0.

With a negative-weight edge, a node popped early (with a seemingly small distance) might have a shorter path discovered later through a negative edge. Example:

```text
A → B (weight 1)
A → C (weight 3)
C → B (weight -3)   ← negative edge
```

Dijkstra finalizes `dist[B] = 1` (via A→B) before processing C. The shorter path A→C→B = 3 + (-3) = 0 is never discovered.

**For negative weights: use Bellman-Ford.**
Bellman-Ford iterates V-1 times over all edges, guaranteeing correct results even with negative weights. It also detects negative cycles. Time: O(V · E).

---

## 4. Network Delay Time (LeetCode #743)

Given a directed weighted graph and source k, find the time for a signal to reach all n nodes. Return -1 if any node is unreachable.

```python
def network_delay_time(times, n, k):
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

The answer is the maximum distance across all nodes — the last node to receive the signal determines the total delay.

---

## 5. Complexity

| Operation | Time | Notes |
|---|---|---|
| Dijkstra (binary heap) | O((V + E) log V) | Standard implementation |
| Dijkstra (Fibonacci heap) | O(E + V log V) | Theoretical optimum; not in Python stdlib |
| Bellman-Ford | O(V · E) | Handles negative weights |
| Path reconstruction | O(V) | Follow prev pointers |

---

## 6. Dijkstra vs. BFS vs. Bellman-Ford

| Algorithm | Edge Weights | Guarantee | When to Use |
|---|---|---|---|
| BFS | Unweighted (all = 1) | Shortest hops | Unweighted graphs |
| Dijkstra | Non-negative | Shortest weighted path | Weighted, non-negative edges |
| Bellman-Ford | Any (including negative) | Shortest path + negative cycle detection | Negative weights present |

---

## 7. Interview Exam Tips

1. **Dijkstra = BFS + priority queue** — state this analogy. The only change from BFS is replacing the FIFO queue with a min-heap on `(distance, node)` tuples.

2. **Initialize with `float('inf')`** — not 0, not -1. Unvisited distances start at infinity so any real distance improves them.

3. **Always skip stale entries** — `if d > dist[node]: continue` is required. Without this, stale entries cause incorrect relaxations.

4. **Tuple comparison in heapq** — Python compares `(d1, node1) < (d2, node2)` lexicographically: first by `d`, then by `node` if distances are equal. For string or object nodes, ensure the node type is comparable or use an index.

5. **Dijkstra does not work with negative edges** — if the problem has negative weights, mention Bellman-Ford. For negative cycles, standard shortest path is undefined.

6. **`max(dist.values())` for Network Delay Time** — the answer to "when does the last signal arrive" is the maximum shortest distance.

7. **Early exit** — if only the distance to a single target is needed, add `if node == end: break` after popping. No early exit is needed if distances to all nodes are required.

8. **Nodes not in the initial graph dict** — use `defaultdict(list)` or ensure all nodes are keys. If a node appears only as a destination, it needs a key in `graph` for `dist` initialization.

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Dijkstra's Algorithm Visualization** — [https://visualgo.net/en/sssp](https://visualgo.net/en/sssp)
   Animated step-by-step visualization of Dijkstra's algorithm on a weighted graph, showing the priority queue state, distance updates, and the sequence of node extractions. Select "Dijkstra" mode.

2. **Khan Academy — Dijkstra's Algorithm** — [https://www.khanacademy.org/computing/computer-science/algorithms/graph-search/a/dijkstras-algorithm](https://www.khanacademy.org/computing/computer-science/algorithms/graph-search/a/dijkstras-algorithm)
   Free article covering the algorithm step by step with a worked example, pseudocode, and explanation of the greedy proof of correctness.

3. **OpenDSA — Shortest Path Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Dijkstra.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Dijkstra.html)
   Free interactive OER textbook with embedded Dijkstra exercises, complexity analysis, and a comparison with Bellman-Ford for negative-weight graphs.

4. **NeetCode — Dijkstra's Algorithm (YouTube)** — [https://www.youtube.com/watch?v=XEb7_z5dG3c](https://www.youtube.com/watch?v=XEb7_z5dG3c)
   Free video walkthrough of Dijkstra's algorithm on the Network Delay Time problem (LeetCode #743), with step-by-step heap trace and code implementation in Python.

5. **MIT OCW 6.006 — Dijkstra's Algorithm Lecture** — [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
   MIT lecture notes and video on Dijkstra's algorithm including the formal proof of correctness (why greedy works), the role of non-negative edge weights, and the time complexity with a binary heap vs Fibonacci heap.

---

## 8. Study Checklist

- [ ] Watch the Module 11 video lecture by Professor Nash.
- [ ] Implement `dijkstra(graph, start)` returning distances to all nodes.
- [ ] Add path reconstruction with a `prev` dictionary.
- [ ] Trace Dijkstra step-by-step on a 5-node weighted graph.
- [ ] Verify that negative-weight edges produce incorrect results with Dijkstra.
- [ ] Solve LeetCode #743 (Network Delay Time).
- [ ] Attempt LeetCode #1631 (Path With Minimum Effort) as a stretch goal.
- [ ] Complete the Module 11 Lab.
- [ ] Complete the Module 11 Quiz.
