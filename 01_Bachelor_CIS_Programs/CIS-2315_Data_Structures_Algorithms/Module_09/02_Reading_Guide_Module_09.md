# Reading Guide: Module 09 — Graph Representations

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

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">MIT OpenCourseWare / freeCodeCamp &bull; CIS-2315 Module 09</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=8hly31xKli0" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/8hly31xKli0" title="Data Structures and Algorithms Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Data Structures and Algorithms Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

A graph G = (V, E) is a set of vertices connected by edges. Graphs generalize trees (which are graphs with no cycles) and are the correct model for any problem involving connections, relationships, dependencies, or paths. This module covers how to represent graphs in code and the vocabulary required to reason about them. BFS and DFS algorithms follow in Module 10.

---

## 1. Graph Terminology

| Term | Definition |
|---|---|
| Vertex (node) | A point in the graph |
| Edge (arc) | A connection between two vertices |
| Directed graph | Edges have direction: u → v does not imply v → u |
| Undirected graph | Edges are bidirectional: u-v and v-u are the same edge |
| Weighted graph | Each edge has a numerical weight |
| Degree | Number of edges touching a vertex |
| In-degree | Number of edges arriving at a vertex (directed graphs) |
| Out-degree | Number of edges leaving a vertex (directed graphs) |
| Path | A sequence of vertices connected by edges |
| Cycle | A path that starts and ends at the same vertex |
| Connected | Every vertex reachable from every other (undirected) |
| Strongly connected | Every vertex reachable from every other in both directions (directed) |
| Connected component | A maximal connected subgraph |
| Tree | Connected acyclic undirected graph with exactly V-1 edges |
| DAG | Directed Acyclic Graph — no cycles; used for dependency ordering |

---

## 2. Adjacency List

The adjacency list maps each vertex to the list of its neighbors. It is the standard representation for interview problems.

### Undirected Graph

```python
from collections import defaultdict

def build_undirected(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)    # both directions
    return graph

edges = [('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')]
g = build_undirected(edges)
# g['A'] = ['B', 'C']
# g['D'] = ['B', 'C', 'E']
```

### Directed Graph

```python
def build_directed(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)    # only forward direction
    return graph
```

### Weighted Graph

Store `(neighbor, weight)` tuples:

```python
def build_weighted(edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))    # omit for directed
    return graph
```

### Complexity

- Space: O(V + E)
- Add edge: O(1) amortized
- Check edge (u, v): O(degree(u))
- Iterate neighbors of u: O(degree(u))

Best for: sparse graphs, most interview problems.

---

## 3. Adjacency Matrix

A V×V array where `matrix[i][j]` is 1 (or the edge weight) if edge i→j exists, else 0.

```python
def build_matrix(n, edges, directed=False):
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix
```

For weighted graphs, store the weight value; use `float('inf')` for absent edges.

### Properties

- Undirected graph: matrix is symmetric (`matrix[i][j] == matrix[j][i]`)
- Check edge (u, v): O(1)
- Iterate all neighbors of u: O(V) — must scan entire row

### Matrix Complexity

- Space: O(V²) — always
- Check edge: O(1)
- Iterate neighbors: O(V)

Best for: dense graphs, algorithms that require O(1) edge existence checks (Floyd-Warshall).

---

## 4. Comparison: Adjacency List vs. Adjacency Matrix

| Property | Adjacency List | Adjacency Matrix |
|---|---|---|
| Space | O(V + E) | O(V²) |
| Add edge | O(1) | O(1) |
| Check edge (u, v) | O(deg(u)) | O(1) |
| Iterate neighbors | O(deg(u)) | O(V) |
| Best for | Sparse graphs | Dense graphs |
| Interview default | Yes | No (unless graph is dense) |

---

## 5. Degree and Graph Properties

### Degree (Undirected)

```python
def degree(graph, vertex):
    return len(graph[vertex])
```

### In-degree and Out-degree (Directed)

```python
def out_degree(graph, vertex):
    return len(graph[vertex])

def in_degree(graph, vertex):
    return sum(1 for neighbors in graph.values() for n in neighbors if n == vertex)
```

### Connectivity Check (Undirected)

```python
def is_connected(graph):
    if not graph:
        return True
    start = next(iter(graph))
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return len(visited) == len(graph)
```

---

## 6. Cycle Detection

### Undirected Graph (DFS with Parent Tracking)

A back edge to any node other than the direct parent indicates a cycle:

```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:    # back edge
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

### Directed Graph (DFS with Recursion Stack)

A back edge to a node currently in the recursion stack (currently being processed) indicates a cycle:

```python
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:    # back edge in directed graph
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
```

---

## 7. Interview Tips

1. **Always clarify directed vs. undirected** — in problems like "Number of Islands," the graph is implicit (grid) and undirected. In "Course Schedule," the graph is directed (prerequisites).

2. **Use `defaultdict(list)` for adjacency lists** — avoids `KeyError` when accessing nodes with no outgoing edges, which simplifies BFS/DFS code.

3. **For grid problems, the graph is implicit** — model cells as nodes and cardinal neighbors (up/down/left/right) as edges. Build the graph on the fly during traversal rather than constructing an explicit adjacency list.

4. **Adjacency matrix means O(1) edge check** — if an algorithm requires "does edge (u,v) exist?" repeatedly, the matrix is the right choice. Otherwise, default to adjacency list.

5. **V and E matter for complexity** — "O(V + E)" is not the same as "O(n)." For a dense graph, E can be O(V²), making O(V + E) = O(V²). Always state complexity in terms of V and E.

6. **Isolated vertices:** a vertex with no edges may not appear in an adjacency list built from edge lists alone. Add it explicitly if needed: `graph[vertex]` with `defaultdict(list)` creates an empty list without error.

7. **Trees are graphs** — a tree is a connected acyclic undirected graph with V-1 edges. Tree traversal algorithms are special cases of graph traversal with no `visited` set needed (trees have no cycles).

8. **DAGs power dependency resolution** — topological sort (Module 10) works only on DAGs. If the problem involves ordering with prerequisites, the graph is a DAG and cycle detection matters.

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Graph Visualizations** — [https://visualgo.net/en/graphds](https://visualgo.net/en/graphds)
   Interactive visualization of directed and undirected graph representations, including adjacency list and adjacency matrix views. Build and modify graphs interactively to observe how the two representations differ.

2. **OpenDSA — Graphs Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/GraphIntro.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/GraphIntro.html)
   Free interactive OER textbook covering graph terminology (vertices, edges, directed, weighted), adjacency representations, and degree analysis with embedded exercises.

3. **CS50 — Graphs Lecture (Harvard)** — [https://cs50.harvard.edu/ai/2024/weeks/3/](https://cs50.harvard.edu/ai/2024/weeks/3/)
   Harvard's free CS50 AI lecture on graph search, covering graph representations and traversal strategies with clear diagrams. No enrollment required.

4. **Khan Academy — Graph Representation** — [https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)
   Free Khan Academy article covering adjacency lists and adjacency matrices with space complexity analysis and when to use each representation.

5. **NeetCode — Graphs Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI](https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI)
   Free video solutions for common graph representation and traversal problems including Number of Islands, Clone Graph, and Course Schedule, each with clear adjacency list construction and traversal walkthroughs.

---

## 8. Study Checklist

- [ ] Watch the Module 09 video lecture by Professor Nash.
- [ ] Build an undirected adjacency list from an edge list.
- [ ] Build a directed adjacency list and compute in-degree for each vertex.
- [ ] Build an adjacency matrix and verify the symmetric property for undirected graphs.
- [ ] Implement the degree function for both directed and undirected graphs.
- [ ] Implement and test `is_connected` on a connected graph and a disconnected graph.
- [ ] Implement `has_cycle_undirected` and test on a graph with a cycle and a tree.
- [ ] Complete the Module 09 Lab.
- [ ] Complete the Module 09 Quiz.



---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 09 — Graph Representations** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 09 — Graph Representations**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 09 — Graph Representations**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 09 — Graph Representations**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
