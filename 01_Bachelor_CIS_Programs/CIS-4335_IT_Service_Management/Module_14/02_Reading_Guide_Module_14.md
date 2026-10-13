# Reading Guide: Module 14 — Risk and Compliance in ITSM

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">AXELOS / PeopleCert &bull; CIS-4335 Module 14</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=951xIKQmols" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/951xIKQmols" title="ITIL 4 Foundation IT Service Management Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>ITIL 4 Foundation IT Service Management Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

Risk and compliance are not separate disciplines layered on top of IT service management — they are woven into it. Every change request includes a risk assessment. Every incident has a compliance dimension when sensitive data is involved. Every asset that is deployed or disposed of creates audit evidence. This module connects the risk and compliance frameworks that govern real-world IT organizations to the ITIL 4 practices you have been studying throughout this course.

Use this guide alongside the Module 14 video lecture and ITIL 4 Foundation study resources.

---

## Risk in ITSM

### ITIL 4 Definition of Risk

ITIL 4 defines risk as a possible event that could cause harm or loss, or affect the ability to achieve objectives. Risk has two defining characteristics:

- **Likelihood** — how probable is the event
- **Impact** — how severe would the consequences be

Risk exposure is typically expressed as the product of likelihood and impact. A low-likelihood, high-impact risk may warrant more attention than a high-likelihood, low-impact risk, depending on the specific nature of the impact.

### Risk Responses

When a risk is identified and assessed, the organization must decide how to respond. ITIL 4 recognizes four risk response strategies:

| Response | Description | When to Use |
|---|---|---|
| Avoid | Eliminate the activity or condition that creates the risk | When the risk exceeds acceptable tolerance and the activity is not essential |
| Mitigate | Implement controls that reduce likelihood, impact, or both | Most common response — reduces risk to an acceptable level |
| Transfer | Shift the financial consequences to another party (e.g., insurance, contracts) | When financial impact is the primary concern and the risk cannot be eliminated |
| Accept | Acknowledge the risk and take no further action | When the cost of control exceeds the value of risk reduction and risk is within tolerance |

### The Risk Register

A risk register is the central management tool for tracking identified risks. In ITSM, risk registers exist at multiple levels:

- **Service-level registers** track risks specific to individual services — availability risks, capacity risks, security risks
- **Project-level registers** track risks in change and improvement initiatives
- **Organizational registers** aggregate high-level strategic and operational risks for executive review

A risk register entry contains: risk description, category, likelihood score, impact score, risk score, risk owner, response strategy, controls in place, and residual risk level.

**Residual risk** is the risk that remains after controls are applied. No set of controls eliminates all risk — residual risk is what the organization accepts after implementing its chosen response.

### ITIL 4 Risk Integration

ITIL 4 does not treat risk as a standalone practice separate from service management — it embeds risk consideration throughout the Service Value System.

**Change Enablement** requires that every change be assessed for risk before authorization. The change model for each change type (standard, normal, emergency) defines the level of risk assessment required.

**Problem Management** analyzes the root causes of incidents and identifies the risks that vulnerabilities create if not addressed.

**Continual Improvement** evaluates the risk of proposed improvements — an improvement initiative can introduce new dependencies, temporary instability, or resource constraints.

**Service Level Management** identifies the risks to meeting SLA commitments — availability risks, capacity risks, third-party dependency risks.

---

## ISO 27001

### What Is ISO 27001?

ISO 27001 is the international standard for Information Security Management Systems (ISMS). It is published by the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC). An organization certified to ISO 27001 has demonstrated to an independent auditor that it has established, implemented, maintained, and continually improved an ISMS that meets the standard's requirements.

### The ISMS

An Information Security Management System is a management framework that defines how an organization:

- Identifies and assesses information security risks
- Selects and implements controls to address those risks
- Monitors and measures the effectiveness of those controls
- Continually improves the system based on measurement and review

The ISMS is not a technology product — it is a set of policies, processes, roles, and records that together constitute a systematic approach to managing information security.

### ISO 27001 Structure

ISO 27001 has two parts: the main body (Clauses 4–10) and Annex A.

**Clauses 4–10** contain the mandatory requirements for the ISMS — context, leadership, planning, support, operation, performance evaluation, and improvement. These clauses apply to every organization regardless of size or industry.

**Annex A** contains 114 controls organized into 14 domains. Organizations do not need to implement every control — they must document which controls they have selected and why in a document called the Statement of Applicability (SoA). Controls that are excluded must have a documented justification.

### Key Annex A Domains for ITSM

| Domain | Relevant ITSM Connection |
|---|---|
| A.8 — Asset Management | Maps to IT Asset Management practice |
| A.9 — Access Control | User account management, privileged access, access reviews |
| A.12 — Operations Security | Change management, malware protection, backup, logging |
| A.16 — Incident Management | Aligns with ITIL 4 Incident Management practice |
| A.15 — Supplier Relationships | Third-party access controls, vendor assessments |

### Risk Assessment Under ISO 27001

ISO 27001 requires a formal, documented risk assessment process. The key steps are:

1. Identify information assets and their owners
2. Identify threats to each asset (unauthorized access, data loss, system failure, natural disaster)
3. Identify vulnerabilities that each threat could exploit
4. Assess likelihood and impact for each threat-vulnerability combination
5. Calculate risk scores
6. Select controls from Annex A (or other sources) to address risks exceeding the organization's tolerance
7. Document all decisions in the risk treatment plan and Statement of Applicability

---

## SOC 2

### What Is SOC 2?

SOC 2 — System and Organization Controls 2 — is an auditing framework developed by the American Institute of Certified Public Accountants (AICPA). It is used by service organizations — cloud providers, SaaS companies, managed service providers, data processing firms — to demonstrate that their controls meet defined standards for protecting customer data.

SOC 2 evaluates controls against five Trust Services Criteria:

| Criterion | Description | Mandatory? |
|---|---|---|
| Security | Protection against unauthorized access | Yes |
| Availability | System availability for operation and use | No |
| Processing Integrity | Completeness and accuracy of processing | No |
| Confidentiality | Protection of confidential information | No |
| Privacy | Collection and use of personal information | No |

Security is the only mandatory criterion. Organizations select additional criteria based on their customer agreements and business context. A cloud infrastructure provider might include Availability; a company handling personal health data might include Privacy.

### Type I vs. Type II Reports

**SOC 2 Type I** evaluates whether the described controls are suitably designed at a specific point in time. It is a point-in-time snapshot.

**SOC 2 Type II** evaluates whether the controls operated effectively over a defined period — typically six to twelve months. It demonstrates sustained operational performance, not just design adequacy.

Most enterprise customers require SOC 2 Type II reports from their service providers because it provides evidence of consistent operation, not just design intent.

### SOC 2 and ITSM Evidence

SOC 2 auditors look for evidence that controls are operating consistently. ITIL 4 practices generate much of this evidence:

- **Change Management tickets** — evidence that changes are authorized before deployment (Security criterion)
- **Incident records** — evidence that security incidents are detected, logged, and resolved (Security criterion)
- **Deployment records** — evidence that software testing and approval gates are followed (Processing Integrity criterion)
- **Asset inventories** — evidence that systems processing customer data are identified and controlled (Security criterion)
- **User access reviews** — evidence that access to systems is regularly reviewed and revoked for departed users (Security criterion)

---

## Audit Evidence Collection

### What Auditors Look For

An audit is an independent assessment of whether controls meet a defined standard. Auditors look for evidence that:

1. Required policies and procedures exist and are formally approved
2. Controls described in policies are actually implemented
3. Controls are operating consistently — not just at audit time
4. Exceptions are identified, documented, and remediated

### Types of Audit Evidence

**System-generated logs** are the most credible evidence type because they are created automatically during operations. Examples include: change management ticket history showing approvals, access logs showing authentication events, deployment logs showing what was deployed and when, and backup completion records.

**Policy documents** demonstrate that required governance structures exist. Auditors verify that policies are current, formally approved, and distributed to relevant staff.

**Configuration exports** show the actual technical state of systems. A firewall rule export, a user account list, or an encryption setting report demonstrates that technical controls are implemented and not just documented.

**Staff interviews** verify that employees understand and follow policies. If a policy says all changes require CAB approval but staff consistently bypass the CAB for urgent changes, the interview will reveal the gap between policy and practice.

### Continuous Evidence Readiness

Organizations with mature compliance programs collect evidence continuously as a byproduct of normal operations. ITSM ticketing systems that record all changes, incidents, and service requests are continuously generating audit evidence. When an audit arrives, the evidence is organized and accessible — not assembled under pressure. This approach also enables proactive identification of control failures before they become audit findings.

---

## Gap Analysis

A gap analysis compares the organization's current control state against the requirements of a target standard. The output is a structured inventory of gaps — where required controls are absent, inadequately designed, or not demonstrably operating.

### Gap Analysis Process

1. Define the target standard (ISO 27001, SOC 2, PCI-DSS, HIPAA, or internal policy)
2. Document the organization's current controls for each requirement
3. For each requirement, assess: Is the required control present? Is it adequately designed? Is there evidence it is operating?
4. Record gaps — requirements where the answer to any assessment question is "no"
5. Prioritize gaps by risk — high-impact gaps with no compensating control are the highest priority
6. Build a remediation roadmap — assigning owners, timelines, and success criteria to each gap

### Gap Analysis Output

The gap analysis produces a report that includes: total number of requirements assessed, number and percentage of requirements met, list of identified gaps with descriptions, risk ratings for each gap, and recommended remediation actions. For ISO 27001 certification, the gap analysis output directly shapes the implementation roadmap and the initial Statement of Applicability.

---

## Compliance Dashboards

A compliance dashboard provides a visual, consolidated view of the organization's compliance posture. Dashboards serve multiple stakeholders simultaneously:

**IT Leadership** needs a strategic summary: What percentage of controls are implemented? How many open audit findings exist? What are the most significant risks? When are upcoming certification renewals?

**Operations Teams** need tactical visibility: Which specific controls are failing? What remediation tasks are overdue? Which systems are out of compliance on a specific control?

**Auditors** benefit from structured evidence summaries that reduce the time required to locate and verify evidence during an audit engagement.

Effective compliance dashboards show control coverage percentage, control testing results (passed/failed/untested), open risk register items with scores and owners, outstanding audit findings with remediation timelines, and upcoming compliance milestones and deadlines.

---

## Key Terms for the ITIL 4 Foundation Exam

| Term | Definition |
|---|---|
| Risk | A possible event that could cause harm or loss, or affect the ability to achieve objectives |
| Risk register | A documented record of identified risks, their assessments, and response strategies |
| Residual risk | The risk that remains after controls are applied |
| ISMS | Information Security Management System — a management framework for systematically managing information security risk |
| ISO 27001 | International standard for ISMS — requires formal risk assessment, control selection, and continual improvement |
| Statement of Applicability | Document listing which ISO 27001 Annex A controls are selected, implemented, or excluded with justification |
| SOC 2 | AICPA auditing framework evaluating controls against Trust Services Criteria |
| SOC 2 Type I | Point-in-time assessment of control design adequacy |
| SOC 2 Type II | Assessment of control operating effectiveness over a defined period |
| Gap analysis | Comparison of current controls against a target standard to identify missing or inadequate controls |

---

## Study Questions

1. What are the four risk response strategies in ITIL 4, and when is each appropriate?

2. What is the difference between risk likelihood, risk impact, and residual risk?

3. What is the Statement of Applicability in ISO 27001, and why does it matter?

4. What is the difference between a SOC 2 Type I and Type II report? Which do enterprise customers typically require and why?

5. How do ITSM ticketing systems generate SOC 2 audit evidence as a byproduct of normal operations?

6. An organization is preparing for ISO 27001 certification. Describe the five steps of a risk assessment process under ISO 27001.

7. What is the purpose of a compliance dashboard, and what three stakeholder groups does it serve?

---

## Supplemental Resources

**1. ISO — ISO/IEC 27001 Information Security Management Overview**
<https://www.iso.org/isoiec-27001-information-security.html>
The official ISO page for the ISO/IEC 27001 standard, covering the ISMS framework, certification process, and the relationship to ISO 27002 controls. Essential reference for understanding what ISO 27001 certification requires and how Statement of Applicability and risk assessment fit within the standard.

**2. AICPA — SOC 2 Report Overview**
<https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2>
Official AICPA resource on SOC 2 reports, Trust Services Criteria, and the distinction between Type I and Type II assessments. Directly relevant to the audit evidence and SOC 2 concepts covered in this module.

**3. NIST — Risk Management Framework (RMF) Overview**
<https://csrc.nist.gov/projects/risk-management/about-rmf>
NIST's Risk Management Framework provides a structured process for identifying, assessing, and responding to information security risks. Complements ITIL 4's risk management concepts with detailed U.S. government-standard methodology for risk categorization, control selection, and continuous monitoring.

---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 14 — Risk and Compliance in ITSM** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 14 — Risk and Compliance in ITSM**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 14 — Risk and Compliance in ITSM**:

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
> **Question:** In the context of **Module 14 — Risk and Compliance in ITSM**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
