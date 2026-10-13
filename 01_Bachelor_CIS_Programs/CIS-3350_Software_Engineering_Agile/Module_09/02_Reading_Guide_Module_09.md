# Reading Guide: Module 09 – Kanban and Lean Principles

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3350 &BULL; SOFTWARE ENGINEERING & AGILE METHODOLOGIES</text>
    
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
      <strong style="margin-left: 10px; font-size: 14px;">Scrum Alliance / Agile Alliance &bull; CIS-3350 Module 09</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=LzMnsfqjzkA" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/LzMnsfqjzkA" title="Agile Software Engineering & Scrum Sprint Masterclass" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Agile Software Engineering & Scrum Sprint Masterclass</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Kanban and Lean are foundational frameworks in the Agile ecosystem. Lean thinking — originating from the Toyota Production System — provides the philosophical basis for waste elimination, flow optimization, and pull-based systems. Kanban operationalizes these ideas for knowledge work through visualization, WIP limits, and flow management. Understanding both prepares you for PSM I exam questions about how Scrum compares to other approaches and for professional contexts where Kanban is used alongside or instead of Scrum.

---

## 1. The Toyota Production System and Lean Origins

Lean manufacturing was developed at Toyota in the 1950s and 1960s by Taiichi Ohno, Eiji Toyoda, and Shigeo Shingo as the Toyota Production System (TPS). Its core insight was that manufacturing quality and efficiency improve when waste is systematically eliminated and work is pulled through the system based on actual demand rather than pushed by a production schedule.

Lean was translated into software development terms by Mary and Tom Poppendieck in their 2003 book Lean Software Development. They mapped Toyota's manufacturing concepts to software work, arguing that the same principles of flow, pull, and waste elimination apply to building software as to building cars.

---

## 2. Lean's Five Principles

### Principle 1 — Identify Value

Value is defined from the customer's perspective: what are they willing to pay for? In software, a working feature that solves a real user problem is value. A feature that was built but nobody uses is waste. The first step in Lean thinking is to be ruthlessly clear about what constitutes genuine value in your context.

### Principle 2 — Map the Value Stream

A value stream is the complete sequence of activities required to deliver value to the customer — from initial idea to working software in production. Value stream mapping visualizes every step, classifying each as value-adding or non-value-adding. Non-value-adding steps (handoffs, approvals, waiting) are targets for elimination or reduction.

### Principle 3 — Create Flow

Once waste is identified, the goal is to make value-creating activities flow smoothly and continuously. Flow is disrupted by batch processing (accumulating many items before moving them forward), handoffs between teams, and multitasking. Creating flow means organizing work so items move from start to finish without unnecessary stopping.

### Principle 4 — Establish Pull

In a pull system, work is pulled into the next stage only when there is capacity to handle it. This contrasts with push systems where work is assigned according to a schedule regardless of whether the recipient is ready. Pull prevents overloading, reduces queue sizes, and enables faster delivery.

### Principle 5 — Seek Perfection

Lean improvement is continuous and never finished. Each improvement cycle reveals new opportunities for waste elimination and flow improvement. The pursuit of perfection is an ongoing commitment, not a destination.

---

## 3. The Seven Wastes of Lean Software Development

The Poppendiecks identified seven categories of waste in software development, adapted from Toyota's seven manufacturing wastes:

| Lean Waste | Software Manifestation |
|---|---|
| Partially done work | Code written but not integrated, tested, or deployed |
| Extra features | Building functionality users did not request (YAGNI violations) |
| Relearning | Solving the same problem multiple times due to poor knowledge transfer |
| Handoffs | Passing work between teams (e.g., dev → QA → ops) with coordination overhead |
| Delays | Waiting for approvals, reviews, environment access, or dependencies |
| Task switching | Working on multiple items simultaneously; context switching reduces all |
| Defects | Bugs requiring rework; also specification errors discovered late |

The connection to Agile: Agile Manifesto Principle 10 — "Simplicity — the art of maximizing the amount of work not done — is essential" — is a direct expression of Lean waste elimination. Short Sprints reduce partially done work. Continuous delivery reduces handoffs. Automated testing reduces defect waste.

---

## 4. Kanban: Definition and Core Practices

Kanban is a method for managing knowledge work that originated in Toyota's manufacturing floor. David Anderson adapted it for software at Microsoft in the early 2000s and formalized it in his 2010 book Kanban: Successful Evolutionary Change for Your Technology Business.

Kanban does not prescribe roles, events, or planning cadences. It is a method for improving an existing process incrementally, not a replacement for the process.

### Core Practice 1 — Visualize the Workflow

Create a board that represents the team's process as columns. Each work item is a card that moves left to right through the columns. Common column configurations:

- Simple: To Do | In Progress | Done
- Detailed: Backlog | Analysis | Development | Testing | Deployment | Done
- With sub-states: Development: In Progress | Waiting for Review | In Review

Visualization makes invisible problems visible. A card that has been in "In Testing" for five days is immediately apparent on a Kanban board; it would be invisible in a spreadsheet.

### Core Practice 2 — Limit Work in Progress (WIP)

WIP limits are maximum counts assigned to each column (or to the team overall) that restrict how many items can be in that stage simultaneously. WIP limits are the defining practice of Kanban.

Why WIP limits work: Little's Law, a mathematical principle from queueing theory, states:

Average Cycle Time = WIP / Throughput

Holding throughput constant, if you reduce WIP, cycle time decreases. Teams that maintain lower WIP move items through the system faster on average, even if they are working at the same rate.

WIP limits also force teams to resolve blockers before starting new work: "Stop starting, start finishing."

### Core Practice 3 — Manage Flow

Track how items move through the board and use flow metrics to identify improvement opportunities:

- Cycle time: How long from when work begins on an item to when it is done
- Lead time: How long from when a request is made to when work is done (includes wait time before work begins)
- Throughput: How many items are completed per unit of time (e.g., items per week)
- WIP: The current number of items in progress

Cumulative flow diagrams (CFDs) visualize all four metrics simultaneously, showing how items accumulate in various stages over time. Widening bands in a specific column indicate a bottleneck.

### Core Practice 4 — Make Policies Explicit

Document the rules that govern how work moves through the board:

- What does "ready for development" mean? (the equivalent of a Definition of Ready)
- When can a card move from Development to Testing? (similar to a Definition of Done for that stage)
- How are blocked items handled?
- What happens when a WIP limit is reached?

Explicit policies eliminate inconsistent behavior and reduce the need for constant management direction.

---

## 5. Scrum vs. Kanban — Side-by-Side Comparison

| Dimension | Scrum | Kanban |
|---|---|---|
| Cadence | Fixed Sprints (1–4 weeks) | Continuous flow; no required cadence |
| Prescribed roles | Yes: Product Owner, Scrum Master, Developers | No prescribed roles |
| Prescribed events | Yes: 5 events with timeboxes | No prescribed events |
| WIP management | Implicit (Sprint scope limits work) | Explicit WIP limits on board columns |
| Iteration commitment | Sprint Goal | No Sprint Goal; items pulled individually |
| Accepting new work | Protected Sprint scope; new items to Product Backlog | New items can be pulled anytime within WIP limits |
| Output metric | Velocity (story points per Sprint) | Throughput (items per week) and cycle time |
| Best fit | Product development with evolving features | Operations, support, continuous maintenance |
| Change management | Changes deferred to next Sprint | Changes accepted anytime within limits |

---

## 6. Scrumban

Scrumban is an informal term for teams that combine Scrum's structural elements with Kanban's flow-based practices. Common Scrumban configurations:

- Using a Kanban board within a Sprint to visualize and limit WIP at the task level
- Using Kanban's cycle time and throughput metrics alongside Scrum's velocity
- Applying Kanban WIP limits to specific workflow stages (e.g., no more than 2 items in code review at once)
- Retaining Scrum events (Daily Scrum, Retrospective) while using Kanban flow management

Scrumban is not an official framework and is not mentioned in the Scrum Guide. However, the Scrum Guide explicitly states that Scrum is a framework within which teams can employ various processes and techniques — Kanban practices are a natural complement.

---

## 7. PSM I Exam Tips

Tip 1: Scrum has prescribed roles, events, and artifacts. Kanban has none of these. PSM I questions that describe a "Scrum team" using a Kanban board are not violating Scrum; the Scrum Guide does not prohibit Kanban tools within a Sprint.

Tip 2: WIP limits are a Kanban concept, not a Scrum concept. The Scrum Guide does not mention WIP limits. If a PSM I question mentions WIP limits, it is in a Kanban or Scrumban context.

Tip 3: Lean's pull principle is foundational to understanding why Scrum's Sprint Planning is designed as it is — Developers pull work from the Product Backlog rather than having it pushed onto them.

Tip 4: Lean's seven wastes map directly to common software problems. "Partially done work" is particularly relevant to Scrum — items that do not meet the Definition of Done at Sprint end are partially done work waste.

Tip 5: Cycle time and throughput are Kanban metrics. Velocity is a Scrum-adjacent metric. Both are legitimate planning tools but measure different things and are not interchangeable.

Tip 6: The PSM I exam may present scenarios describing Kanban practices (continuous flow, no Sprints, WIP limits) and ask whether this is Scrum. The answer is no — these are Kanban practices. Scrum requires Sprints and Sprint events.

Tip 7: Agile Manifesto Principle 10 (maximize work not done) is the Manifesto's expression of Lean waste elimination. When exam questions connect Lean to Agile, this principle is the bridge.

Tip 8: Kanban does not require or prohibit any specific estimation technique. Some Kanban teams use story points; others use T-shirt sizes; some use no estimates at all (#NoEstimates). The absence of prescribed estimation is a key Kanban characteristic.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 09 topics:

**1. "Kanban Guide for Scrum Teams" — Scrum.org**
<https://www.scrum.org/resources/kanban-guide-scrum-teams>
An official Scrum.org guide describing how Kanban practices can be applied within a Scrum Team context. Covers flow metrics, WIP limits, and the relationship between the Sprint and Kanban's continuous flow. Free PDF download from Scrum.org.

**2. "Lean Software Development: An Agile Toolkit" — Chapter Summary (Mary Poppendieck)**
<https://www.informit.com/articles/article.aspx?p=169223>
A free excerpt and summary from the original Poppendieck Lean Software Development book on InformIT. Covers the seven wastes of software development with software-specific examples. Essential reading for Module 09's waste analysis lab.

**3. "Little's Law for Everyone" — Dr. Neil Gunther**
<https://www.agilealliance.org/resources/experience-reports/littles-law-applied-to-agile-development/>
An accessible Agile Alliance article applying Little's Law to software development teams. Explains the math behind WIP limits and cycle time improvement with worked numerical examples. Free access via the Agile Alliance resource library.

---

## 8. Study Checklist

- [ ] State the five Lean principles from memory and give one software example for each
- [ ] List the seven wastes of Lean software development and identify a specific example of each in a software team context
- [ ] Describe the four core Kanban practices and explain why each improves team performance
- [ ] Explain Little's Law and how it justifies WIP limits
- [ ] Complete the Scrum vs. Kanban comparison table from memory across all eight dimensions
- [ ] Explain what Scrumban is and give two examples of how a Scrum team might incorporate Kanban practices
- [ ] Explain the connection between Lean's pull principle and Scrum's Sprint Planning
- [ ] Complete this module's Lab and Quiz

---



---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 09 – Kanban and Lean Principles** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 09 – Kanban and Lean Principles**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 09 – Kanban and Lean Principles**:

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
> **Question:** In the context of **Module 09 – Kanban and Lean Principles**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
