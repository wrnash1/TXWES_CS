# Reading Guide: Module 07 – User Stories and Acceptance Criteria

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
      <strong style="margin-left: 10px; font-size: 14px;">Scrum Alliance / Agile Alliance &bull; CIS-3350 Module 07</strong>
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

User stories are the most common way of expressing Product Backlog items in Agile teams. They capture requirements from a user perspective, keep conversations focused on value, and — when combined with well-written acceptance criteria — create a testable, shared understanding of Done. This guide covers user story format, the Three Cs model, acceptance criteria in Given/When/Then format, the work item hierarchy (epics, stories, tasks), and the most common user story quality problems.

---

## 1. What a User Story Is

A user story is a short, simple description of a feature told from the perspective of the person who desires the new capability, usually a user or customer of the system. User stories emerged from the Extreme Programming (XP) community, popularized by Ron Jeffries' Three Cs model, and have become the standard way of describing Product Backlog items in Scrum teams worldwide.

User stories are deliberately not comprehensive specifications. They are promises for a conversation — lightweight records that prompt discussion between the Product Owner, Developers, and stakeholders during refinement and Sprint Planning.

### The Standard User Story Format

As a [user type], I can [action] so that [benefit].

- As a [user type]: identifies who needs the capability. Should be specific — not just "user," but "registered customer," "system administrator," "first-time visitor," or a named persona.
- I can [action]: describes what the user wants to do. Written from the user's perspective, not the system's. Focuses on behavior, not implementation.
- So that [benefit]: explains why the user needs this capability — the value it creates. This clause is critical for understanding priority and validating that the story is worth building.

### Full User Story Example

As a small business owner, I can generate a monthly expense summary report in PDF format so that I can share financial summaries with my accountant without manual data entry.

---

## 2. The Three Cs Model

Ron Jeffries described user stories using three components that together constitute what a story really is:

### Card

The Card is the written representation of the story — the brief text recorded on an index card, sticky note, or in a project management tool. The Card is not a specification; it is a reminder of what needs to be discussed. Its brevity is intentional: it invites conversation rather than substituting for it.

### Conversation

The Conversation is the real content of the user story. It is the dialogue between the Product Owner, Developers, and stakeholders that fills in the details, resolves ambiguities, and surfaces constraints. The Conversation happens during Product Backlog Refinement and Sprint Planning. The Card exists to prompt and guide this conversation.

A story that has never been discussed is a story that is not ready for development. Developers who start work on a story they have not discussed with the Product Owner frequently discover mid-Sprint that their assumptions were wrong.

### Confirmation

The Confirmation is the acceptance criteria — the written agreement about what Done means for this story. Acceptance criteria transform a vague story into a testable commitment. They are the record of the key points from the Conversation that the team wants to formalize as quality expectations.

---

## 3. Acceptance Criteria and Given/When/Then

### What Acceptance Criteria Are

Acceptance criteria are specific conditions that a user story must satisfy to be considered complete. They define the boundaries of the story — what is in scope and what is out — and provide the basis for testing.

Quality acceptance criteria are:

- Specific: they describe exact, observable behavior
- Testable: a test can be written that definitively passes or fails
- Unambiguous: both the Product Owner and Developers interpret them the same way
- Covering the happy path and key edge cases: the main scenario and important failure/edge scenarios

### Given/When/Then Format

The most common format for acceptance criteria in Agile teams is Given/When/Then, also known as Gherkin format or BDD (Behavior-Driven Development) format.

Structure:

- Given [initial context or precondition]: what state is the system in before the behavior occurs?
- When [action or trigger]: what does the user do, or what event occurs?
- Then [expected outcome]: what observable result does the user or system produce?

### Complete Example

User story: As a registered customer, I can reset my password so that I can regain access to my account when I forget my credentials.

Acceptance Criterion 1 — Happy path:

Given a registered customer is on the login page and clicks "Forgot Password,"
When they enter their registered email address and click Submit,
Then they receive an email with a secure password reset link within two minutes.

Acceptance Criterion 2 — Successful reset:

Given a customer has received a valid password reset link,
When they click the link within 24 hours and enter a new password meeting complexity requirements (minimum 8 characters, one uppercase, one number),
Then their password is updated and they are redirected to their dashboard with a success message.

Acceptance Criterion 3 — Expired link:

Given a customer has received a password reset link,
When they click the link after 24 hours have elapsed,
Then the link is expired, a clear error message is displayed, and they are prompted to request a new link.

Acceptance Criterion 4 — Unregistered email:

Given a visitor is on the Forgot Password page,
When they enter an email address that is not associated with any account and click Submit,
Then they see a generic confirmation message (to prevent email enumeration attacks) without revealing whether the address is registered.

---

## 4. User Stories vs. Acceptance Criteria vs. Definition of Done

This distinction is frequently tested on PSM I:

| Item | What It Defines | Scope | Owner |
|---|---|---|---|
| User Story | The feature need from the user's perspective | One backlog item | Product Owner (with team input) |
| Acceptance Criteria | The specific conditions for this story to be Done | One backlog item | Product Owner (confirmed with Developers) |
| Definition of Done | The quality standards every Increment must meet | All Increments | Scrum Team (Developers primarily) |

The Definition of Done applies universally — every Increment, regardless of which stories it contains, must meet the DoD. Acceptance criteria are item-specific — they apply only to the story they belong to. A story may meet all its acceptance criteria but still fail the Definition of Done if, for example, the DoD requires code review and code review was not performed.

---

## 5. Work Item Hierarchy: Epics, Stories, and Tasks

### Epics

An Epic is a large user story that is too big to complete in one Sprint. Epics represent high-level features or capabilities that will require multiple stories to implement fully. They sit at the top of the Product Backlog when a product is new or a major capability is first being described.

Epics must be decomposed into user stories through Product Backlog Refinement before they are ready for Sprint Planning. A story that takes more than one Sprint to complete is too large and should be treated as an epic until it is split.

Example Epic: "As a customer, I can manage my subscription." This encompasses billing management, plan changes, cancellation, payment method updates, and invoice history — multiple Sprints of work.

### User Stories (Sprint-ready)

User stories are refined, Sprint-sized items that meet the INVEST criteria. They are the unit of work the team commits to during Sprint Planning and the items that are demonstrated at Sprint Review.

### Tasks

Tasks are the technical activities Developers create during Sprint Planning to plan how they will implement a user story. Tasks live in the Sprint Backlog, not the Product Backlog. They are created by the Developers and are at a finer grain than stories — typically one to eight hours of work each.

Tasks are not user-facing; they are implementation activities. "Write unit tests for the password reset endpoint" is a task, not a user story.

---

## 6. Common User Story Mistakes

Mistake 1 — Missing "so that" clause: "As a user, I can search for products" omits the benefit. Why do they want to search? The benefit clause is what enables the team to evaluate priority and test whether the feature actually delivers value.

Mistake 2 — System-centric stories: "The system shall implement Redis caching for product pages" is a technical decision written in system-specification language. Rewrite as a user story with a user benefit, then let the implementation approach emerge from the team's conversation.

Mistake 3 — Acceptance criteria as UI specifications: "The submit button will be blue with a 16px Helvetica font" is a design spec. Acceptance criteria should describe behavior and outcome, not visual design details.

Mistake 4 — Stories too large for one Sprint: Stories that cannot be completed in one Sprint must be split. Common splitting patterns include splitting by user type, by workflow step, by data type, or by happy path vs. edge cases.

Mistake 5 — No acceptance criteria: Stories without acceptance criteria have no confirmation — the "C" in the Three Cs is missing. The team does not know when they are done, leading to ambiguous Sprint Reviews and Definition of Done disputes.

---

## 7. PSM I Exam Tips

Tip 1: User stories are not mandated by the Scrum Guide. The Scrum Guide does not prescribe how Product Backlog items are written. User stories are a common practice, not a Scrum rule. PSM I questions that ask about mandatory formats for PBIs are testing this knowledge.

Tip 2: Acceptance criteria are item-specific; the Definition of Done applies to all Increments. Both must be satisfied for a story to be truly Done.

Tip 3: The "so that" clause is the most important part of a user story from a value perspective. Stories without it cannot be prioritized by value because value is unstated.

Tip 4: The Three Cs — Card, Conversation, Confirmation — describe what a user story actually is. Know these terms and what each represents.

Tip 5: An epic is a large user story, not a Scrum framework element. The Scrum Guide does not use the word "epic." It is a common practice term, not an official Scrum term.

Tip 6: Tasks are created by Developers during Sprint Planning and live in the Sprint Backlog. They are not Product Backlog items.

Tip 7: Given/When/Then acceptance criteria format is a BDD (Behavior-Driven Development) practice. It is widely used with Scrum but is not mandated by the Scrum Guide.

Tip 8: PSM I questions about user stories often present poorly written stories and ask what is wrong with them. Apply the INVEST criteria and look for missing "so that" clauses, overly large stories, and non-testable acceptance criteria.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 07 topics:

**1. "User Stories" — Agile Alliance Glossary**
<https://www.agilealliance.org/glossary/user-stories/>
The Agile Alliance's canonical glossary entry on user stories. Covers the Three Cs model, the standard format, common variations, and the distinction between user stories and traditional requirements. Includes references to further reading.

**2. "Introduction to Given When Then" — Martin Fowler**
<https://martinfowler.com/bliki/GivenWhenThen.html>
A concise explanation of the Given/When/Then (Gherkin) acceptance criteria format by a Manifesto signatory. Explains the relationship between BDD (Behavior-Driven Development) and Agile acceptance testing. Free access on martinfowler.com.

**3. "Story Splitting Flowchart" — Richard Lawrence**
<https://www.agileforall.com/splitting-user-stories/>
A free, practical guide to splitting user stories with a flowchart decision tree. Covers ten splitting patterns with worked examples. Highly useful for the epic decomposition exercises in this module's lab. Free access on agileforall.com.

---

## 8. Study Checklist

- [ ] Write five user stories in the standard format for an app of your choice
- [ ] For each story, write 2–3 acceptance criteria in Given/When/Then format
- [ ] Explain the Three Cs model: what is the Card, what is the Conversation, and what is the Confirmation?
- [ ] Explain the difference between acceptance criteria and the Definition of Done
- [ ] Define Epic, User Story, and Task and explain how they differ in scope and ownership
- [ ] Identify five common user story mistakes and rewrite one poorly written story to fix all five
- [ ] State whether user stories are required by the Scrum Guide (they are not)
- [ ] Complete this module's Lab and Quiz

---



---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 07 – User Stories and Acceptance Criteria** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 07 – User Stories and Acceptance Criteria**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 07 – User Stories and Acceptance Criteria**:

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
> **Question:** In the context of **Module 07 – User Stories and Acceptance Criteria**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
