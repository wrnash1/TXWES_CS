# Reading Guide: Module 06 – Product Backlog: Creation and Refinement

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
      <strong style="margin-left: 10px; font-size: 14px;">Scrum Alliance / Agile Alliance &bull; CIS-3350 Module 06</strong>
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

The Product Backlog is Scrum's primary planning artifact. It is the single source of truth for what the team will build, in what order, and why. Understanding the Product Backlog deeply — its structure, ownership, refinement process, and quality criteria — is essential for the PSM I exam and for effective Agile practice. This guide covers the Product Backlog from definition through maintenance, including the INVEST criteria and common failure modes.

---

## 1. Product Backlog Fundamentals

### Definition

The Scrum Guide defines the Product Backlog as an emergent, ordered list of what is needed to improve the product. It is the single source of work undertaken by the Scrum Team.

### Key Characteristics

The Product Backlog is never complete: it is dynamic and evolves as long as the product exists.

The Product Backlog is emergent: it grows, changes, and becomes more detailed over time as the team learns more about the product and its users.

The Product Backlog is ordered: items are arranged in a complete ranking, with the highest-value, most-ready items at the top.

The Product Backlog is the single source: there is one Product Backlog per product. Multiple teams working on the same product share one Product Backlog.

### Product Backlog Item (PBI) Attributes

Each Product Backlog item has four standard attributes:

| Attribute | Owner | Description |
|---|---|---|
| Description | Product Owner | What the item is and why it is valuable |
| Order | Product Owner | Position in the ordered list relative to other items |
| Estimate (size) | Developers | Relative effort required to complete the item |
| Value | Product Owner | Business or user value delivered by completing the item |

Additional attributes commonly added by teams: acceptance criteria, definition of done compliance notes, dependencies, and technical notes.

---

## 2. The Product Goal

The Product Goal is the commitment associated with the Product Backlog. It is a long-term objective that describes the future state of the product and serves as the target for the Scrum Team to plan against.

The Product Backlog defines all the work needed to achieve the Product Goal. When the Product Goal is achieved — or abandoned as no longer valuable — the team may set a new Product Goal and build a new Product Backlog around it.

A Scrum Team pursues one Product Goal at a time. The Product Goal gives the Product Backlog coherence: items in the backlog should contribute to achieving the Product Goal; items that do not should be removed or deferred.

---

## 3. Product Backlog Ownership

The Product Owner is fully accountable for the Product Backlog. Their four key responsibilities:

Responsibility 1 — Developing and communicating the Product Goal: The Product Owner is responsible for defining a clear, meaningful Product Goal that the entire organization understands.

Responsibility 2 — Creating and communicating Product Backlog items: The Product Owner writes or facilitates the writing of PBIs, ensuring each item is clear enough to be understood by stakeholders, Developers, and other Product Owners.

Responsibility 3 — Ordering the Product Backlog: The Product Owner makes the hard trade-off decisions about which items to prioritize. Order reflects value, dependency, risk, learning opportunity, or any other factor the Product Owner deems relevant.

Responsibility 4 — Ensuring transparency: The Product Backlog should be visible, understandable, and accessible to the entire Scrum Team and relevant stakeholders.

### Delegation vs. Accountability

The Product Owner may delegate any of these activities to Developers, business analysts, or other team members. However, delegation does not transfer accountability. The Product Owner remains accountable for the outcomes of all Product Backlog decisions.

Stakeholders who want to influence the Product Backlog must go through the Product Owner. They cannot directly add, order, or modify items in the backlog without the Product Owner's involvement.

---

## 4. Product Backlog Refinement

### What Refinement Is

Product Backlog Refinement is the ongoing activity in which the Product Owner and Developers collaboratively decompose large Product Backlog items into smaller, more precise items and add details such as estimates and acceptance criteria.

Refinement is not a Scrum event — it does not appear in the list of the five official Scrum events. It is an ongoing activity that happens throughout the Sprint at whatever frequency the team finds useful.

### Refinement Capacity

The Scrum Guide states that Product Backlog Refinement typically consumes no more than 10% of the Developers' capacity. For a two-week Sprint with five Developers at 8 hours per day, 10% is approximately 4 hours per Developer per Sprint.

### Participants in Refinement

The Product Owner and Developers conduct refinement together. The Scrum Master may participate to facilitate or coach, but refinement is primarily a collaborative conversation between the Product Owner (who brings business context and value information) and the Developers (who bring technical feasibility knowledge and size estimates).

### What Happens During Refinement

During refinement sessions, the team:

- Reviews upcoming Product Backlog items to evaluate whether they are ready for Sprint Planning
- Breaks large items (epics) into smaller stories or tasks
- Adds acceptance criteria to items
- Adds or updates size estimates
- Removes items that are no longer relevant
- Re-orders items as business context changes
- Identifies and documents dependencies between items

### The Gradient of Backlog Detail

A well-refined backlog has a gradient of detail:

- Top of backlog (next 1–2 Sprints): items are small, well-defined, estimated, and ready for Sprint Planning
- Middle of backlog (3–10 Sprints out): items are medium-sized, partially defined, with rough estimates
- Bottom of backlog (more than 10 Sprints out): items are large, vague epics with minimal detail

This gradient reflects the Agile principle of "just enough" planning — detailed specification is done only when the work is close enough to matter.

---

## 5. INVEST Criteria for Product Backlog Items

INVEST is a quality checklist for evaluating whether a Product Backlog item is well-written and ready for Sprint-level work.

| Letter | Criterion | What It Means |
|---|---|---|
| I | Independent | The item can be delivered without requiring another item to be Done first |
| N | Negotiable | The implementation approach is not locked; the team has room for judgment |
| V | Valuable | The item delivers clear value to a user, customer, or the business |
| E | Estimable | The team has enough information to estimate the item's size |
| S | Small | The item can be completed within one Sprint |
| T | Testable | Acceptance criteria exist so the team can confirm when the item is Done |

Items that fail multiple INVEST criteria need more refinement before they are suitable for Sprint Planning. A common PSM I exam question will present a PBI and ask whether it is ready for Sprint Planning — applying INVEST is the evaluation framework.

---

## 6. Ordering the Product Backlog

Ordering is more precise than prioritization. Prioritization groups items into categories (high/medium/low). Ordering creates a complete sequence — item 1 before item 2 before item 3. The Product Owner makes explicit trade-off decisions through ordering.

Factors that influence ordering decisions:

- Value to users and the business: higher-value items generally rank higher
- Risk and uncertainty: high-risk items may be ordered early to learn fast (fail early rather than fail late)
- Dependencies: item B that depends on item A must be ordered after A
- Learning value: items that will teach the team something important about the product or technology
- Market timing: items needed for a specific release window
- Cost of delay: the business cost of not delivering an item sooner

The Product Owner owns ordering decisions. Stakeholders, managers, and Developers may provide input, but the Product Owner makes the final call.

---

## 7. Common Product Backlog Problems

Problem 1 — Backlog too large: A Product Backlog with hundreds of items is difficult to maintain and likely contains items that will never be built. Regularly reviewing and pruning low-value, stale items is a healthy practice.

Problem 2 — No ordering: All items marked "high priority" means the Product Owner has not made the hard sequencing decisions that are their core responsibility.

Problem 3 — Items too large for Sprint Planning: If most items require multiple Sprints, the backlog needs more refinement. Large epics must be decomposed into Sprint-sized stories.

Problem 4 — Missing acceptance criteria: Items without acceptance criteria produce ambiguous Done states at Sprint end. Acceptance criteria make the Definition of Done item-specific and testable.

Problem 5 — Backlog managed by committee: When multiple stakeholders add and order items without going through the Product Owner, the backlog loses coherence and the Product Owner loses accountability.

Problem 6 — Backlog as a wish list: A backlog that includes every possible feature idea without ordering or value assessment is not a planning tool — it is a wish list. The Product Owner must make hard choices about what to include and in what order.

---

## 8. PSM I Exam Tips

Tip 1: The Product Backlog is never complete. If an exam question describes a completed or frozen backlog, it is describing non-Scrum behavior.

Tip 2: The Product Owner orders the backlog; Developers estimate the items. These two responsibilities belong to different people and are not interchangeable on the exam.

Tip 3: Product Backlog Refinement is not a Scrum event. It does not appear in the five official events. When exam questions ask how many Scrum events there are, the answer is five, and refinement is not one of them.

Tip 4: The INVEST criteria — Independent, Negotiable, Valuable, Estimable, Small, Testable — are the standard framework for evaluating PBI readiness. Know all six.

Tip 5: Stakeholders influence the Product Backlog through the Product Owner, not directly. Any question that puts stakeholders in direct control of the backlog is describing incorrect Scrum behavior.

Tip 6: The Product Goal is the commitment associated with the Product Backlog. Know this pairing: Product Backlog → Product Goal; Sprint Backlog → Sprint Goal; Increment → Definition of Done.

Tip 7: There is one Product Backlog per product. Multiple Scrum Teams working on the same product share one Product Backlog. This is tested on PSM I.

Tip 8: Refinement consumes no more than 10% of Developers' capacity. This is the Scrum Guide's guidance — know the percentage.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 06 topics:

**1. "What Is a Product Backlog?" — Scrum.org**
<https://www.scrum.org/resources/what-is-a-product-backlog>
Scrum.org's official resource page on the Product Backlog. Covers the emergent nature, ordering principles, relationship to the Product Goal, and the Product Owner's four key accountabilities. Includes a short video.

**2. "User Stories Applied" — Mike Cohn, Mountain Goat Software (excerpt)**
<https://www.mountaingoatsoftware.com/agile/user-stories>
A free overview of user story writing from Mountain Goat Software, covering the standard format, the INVEST criteria, and common story-writing mistakes. Cohn is the practitioner who popularized user stories in Agile teams.

**3. "Product Backlog Refinement Explained" — Scrum.org**
<https://www.scrum.org/resources/blog/product-backlog-refinement-explained-110>
A detailed Scrum.org blog post explaining when, why, and how refinement should occur. Addresses the 10% capacity guideline, who participates, and how to assess whether a backlog item is ready for Sprint Planning. Free access.

---

## 9. Study Checklist

- [ ] Define the Product Backlog in the Scrum Guide's exact language and explain what "emergent" means in this context
- [ ] List the four attributes of a Product Backlog item and state who is responsible for each
- [ ] Explain what the Product Goal is and how it relates to the Product Backlog
- [ ] Describe the four Product Owner responsibilities for the Product Backlog
- [ ] Explain the difference between delegation and accountability in the context of Product Backlog management
- [ ] Define Product Backlog Refinement: what it is, who participates, and how much capacity it consumes
- [ ] Recite the INVEST criteria from memory and give one example of a PBI that fails each criterion
- [ ] Explain the difference between ordering and prioritization
- [ ] Describe four common Product Backlog problems and how to address each
- [ ] Complete this module's Lab (write a 10-item Product Backlog for a hypothetical product) and Quiz

---



---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 06 – Product Backlog: Creation and Refinement** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 06 – Product Backlog: Creation and Refinement**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 06 – Product Backlog: Creation and Refinement**:

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
> **Question:** In the context of **Module 06 – Product Backlog: Creation and Refinement**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
