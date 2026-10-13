# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 11 — Dijkstra's Shortest Path Algorithm

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Draw the weighted graph on the whiteboard first. Show the dist table being updated step by step before coding.
> - Dijkstra is BFS with a priority queue instead of a regular queue. State this analogy explicitly.
> - Emphasize: Dijkstra requires non-negative edge weights. Negative weights break the greedy argument.
> - Python: use `heapq` with `(distance, node)` tuples. Demonstrate why order matters for tuple comparison.
> - The "lazy deletion" pattern: when a stale `(dist, node)` pair is popped, skip it if `dist > current best`. This is the standard interview implementation.
> - Network Delay Time (LeetCode #743) is the canonical Dijkstra interview problem. Walk through it step by step.
> - Common mistakes: forgetting to initialize dist to infinity, not skipping stale heap entries, confusing weighted and unweighted shortest path.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 11 | Dijkstra's Shortest Path | CIS-2315"]**

"Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights. It is the engine behind GPS navigation, network routing, and any system that needs to find optimal paths through a cost graph. Conceptually, Dijkstra is BFS with a priority queue: instead of processing nodes in FIFO order, we always process the node with the currently known shortest distance. This greedy choice guarantees optimality when all edge weights are non-negative."

---

## [01:30 – 08:00] Part 1 — The Algorithm

**[SHOW SLIDE: "Dijkstra's Algorithm — Greedy Shortest Path"]**

"**[SHOW DIAGRAM: weighted graph with nodes A, B, C, D, E]**

```text
        4       8
    A ───── B ───── C
    │       │       │
  2 │     1 │     2 │
    │       │       │
    D ───── E ───── F
        3       1
```

Nodes: A, B, C, D, E, F
Edge weights shown on each edge.

[PAUSE]

Dijkstra's algorithm:

1. Initialize `dist[source] = 0`, `dist[all others] = infinity`.
2. Push `(0, source)` onto a min-heap.
3. While the heap is not empty:
   a. Pop `(d, node)` — the node with the smallest current known distance.
   b. If `d > dist[node]`, skip (stale entry).
   c. For each neighbor: if `dist[node] + weight < dist[neighbor]`, update `dist[neighbor]` and push `(new_dist, neighbor)` onto the heap.

The key insight: the first time a node is popped from the heap, its distance is finalized. Any later entries for that node in the heap are stale and skipped.

[PAUSE]

```python
import heapq

def dijkstra(graph, start):
    """
    Returns shortest distances from start to all reachable nodes.
    graph: {node: [(neighbor, weight), ...]}
    Time: O((V + E) log V) with a binary min-heap
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

**[DEMO: trace Dijkstra on the graph above from source A. Show dist table and heap state at each step]**

```text
Initial: dist={A:0, B:inf, C:inf, D:inf, E:inf, F:inf}, heap=[(0,A)]

Pop (0,A): process neighbors B(4), D(2)
  B: 0+4=4 < inf → dist[B]=4, push (4,B)
  D: 0+2=2 < inf → dist[D]=2, push (2,D)
  heap=[(2,D),(4,B)]

Pop (2,D): process neighbor E(3)
  E: 2+3=5 < inf → dist[E]=5, push (5,E)
  heap=[(4,B),(5,E)]

Pop (4,B): process neighbors C(8), E(1)
  C: 4+8=12 < inf → dist[C]=12, push (12,C)
  E: 4+1=5 = dist[E]=5 → no update (not strictly less)
  heap=[(5,E),(12,C)]

Pop (5,E): process neighbor F(1)
  F: 5+1=6 < inf → dist[F]=6, push (6,F)
  heap=[(6,F),(12,C)]

Pop (6,F): no neighbors to update
Pop (12,C): no updates
Final: dist={A:0, B:4, C:12, D:2, E:5, F:6}
```"

---

## [08:00 – 13:00] Part 2 — Shortest Path Reconstruction

**[SHOW SLIDE: "Recovering the Shortest Path (not just the distance)"]**

"The `dijkstra` function above returns only distances. To recover the actual path, track which node each node was reached from using a `prev` (predecessor) dictionary.

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
            break    # early exit — destination reached

        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    # Reconstruct path by following prev pointers from end to start
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()

    return path, dist[end]
```

**[DEMO: dijkstra_path from A to F in the graph above — expected path A→D→E→F, distance 6]**

[PAUSE]

The reconstruction walks backward through `prev` pointers: F → prev[F]=E → prev[E]=D → prev[D]=A → None. Reversing gives the forward path A→D→E→F."

---

## [13:00 – 18:00] Part 3 — Why Dijkstra Fails on Negative Weights

**[SHOW SLIDE: "Negative Weights — The Fatal Assumption"]**

"Dijkstra's greedy property assumes: once a node is popped from the heap, its distance is final. This holds only when all edge weights are non-negative.

**[SHOW DIAGRAM: small graph with a negative edge]**

```text
A ─── 1 ─── B
│           │
4          -3
│           │
└─── 3 ─── C
```

Dijkstra from A: would finalize dist[B]=1 early (B popped first). But the path A→C→B = 3 + (-3) = 0 < 1 is shorter. Dijkstra misses this because B was already finalized.

[PAUSE]

**For negative edge weights, use Bellman-Ford:** it iterates V-1 times over all edges, relaxing distances, and detects negative cycles. Time: O(V · E) — slower than Dijkstra but correct for any weights.

For interview problems: if the problem says "non-negative weights" or uses concepts like travel time or cost, Dijkstra is the right choice. If negative weights appear, mention Bellman-Ford."

---

## [18:00 – 22:00] Part 4 — Network Delay Time (LeetCode #743)

**[SHOW SLIDE: "LeetCode #743 — Network Delay Time"]**

"Given a network of n nodes and directed edges `(u, v, weight)` representing signal travel times, and a source node `k`, find the minimum time for a signal from k to reach all nodes. If some node is unreachable, return -1.

This is exactly Dijkstra from source k. The answer is `max(dist.values())` — the time for the last node to receive the signal.

```python
def network_delay_time(times, n, k):
    """
    times: list of (u, v, w) directed edges
    n: number of nodes (1-indexed)
    k: source node
    Returns minimum time for signal to reach all nodes, or -1.
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

**[DEMO: times=[(2,1,1),(2,3,1),(3,4,1)], n=4, k=2 → expected output 2]**

The maximum distance from 2 to all other nodes: dist={1:1, 2:0, 3:1, 4:2}. Max = 2.

The Module 11 lab has you implement Dijkstra, add path reconstruction, handle disconnected graphs, and solve LeetCode #743. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 11 — Dijkstra's Shortest Path]**

---

## Additional Resources

- [VisuAlgo — Dijkstra Visualization](https://visualgo.net/en/sssp)
- [NeetCode — Dijkstra's Algorithm](https://www.youtube.com/watch?v=XEb7_z5dG3c)
- [LeetCode #743 — Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- [LeetCode #1631 — Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
- [LeetCode #787 — Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
