# Reading Guide: Module 13 — Compliance and Security Controls Validation

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4332 &BULL; CYBERSECURITY ANALYST & THREAT HUNTING</text>
    
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
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA / CertifyBreakfast &bull; CIS-4332 Module 13</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W" title="CompTIA Cybersecurity Analyst (CySA+ CS0-003) Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Cybersecurity Analyst (CySA+ CS0-003) Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Introduction

Module 13 addresses a discipline that is foundational to every mature security program: compliance and security controls validation. Detection and response skills matter only if the controls that generate detectable events are actually functioning. A SIEM that loses log sources goes dark. A firewall with misconfigured rules allows traffic it should block. MFA with legacy exceptions leaves accounts exposed.

Controls validation is the practice of verifying that security controls are implemented, operating, and effective. Compliance is the practice of demonstrating that your security program meets defined standards, frameworks, or regulatory requirements.

The CySA+ CS0-003 exam tests these concepts across Domain 2 (Vulnerability Management) and Domain 3 (Reporting and Communication). This reading guide prepares you to select the right framework for a given context, categorize controls correctly, perform gap analysis, and produce audit-quality evidence.

---

## Section 1 — High-Yield Glossary

**Security Control** — A safeguard or countermeasure prescribed to meet a security requirement. Controls can be technical, administrative, or physical.

**Control Framework** — A structured set of security practices and safeguards organized to help organizations manage security risk. Examples: NIST CSF, CIS Controls, NIST 800-53.

**NIST Cybersecurity Framework (CSF)** — A voluntary framework published by the National Institute of Standards and Technology organizing cybersecurity activities into five core functions: Identify, Protect, Detect, Respond, Recover. Version 2.0 (2024) added a sixth function, Govern.

**CIS Controls** — 18 prioritized security controls published by the Center for Internet Security, organized into three implementation groups by organizational maturity. Formerly called the SANS Critical Security Controls.

**NIST SP 800-53** — A comprehensive catalog of security and privacy controls for federal information systems, widely used beyond the federal sector for rigorous control documentation.

**Gap Analysis** — A structured comparison of current security posture against a target framework or standard, identifying where controls are missing or insufficient.

**Audit** — A formal, independent review verifying that controls exist and are operating as intended. Audits produce findings and recommendations.

**Audit Evidence** — Documentation proving that a control exists and is functioning. Types include policies, configuration screenshots, log extracts, scan reports, and training records.

**Preventive Control** — A control that stops a security event from occurring. Examples: firewalls, MFA, encryption.

**Detective Control** — A control that identifies when a security event has occurred. Examples: IDS, SIEM, audit logs.

**Corrective Control** — A control that restores systems to normal operation after a security event. Examples: backups, patch management, IR procedures.

**Deterrent Control** — A control that discourages potential threat actors. Examples: warning banners, visible surveillance cameras, published penalties.

**Technical Control** — A control implemented through technology in hardware or software. Examples: firewalls, access control lists, encryption, MFA.

**Administrative Control** — A control implemented through policy, procedure, or training. Examples: security awareness training, acceptable use policies, separation of duties.

**Physical Control** — A control implemented in the physical environment. Examples: locks, badge readers, security guards, cage servers.

**SCAP (Security Content Automation Protocol)** — A NIST standard providing a common language for expressing security configurations and automating compliance checking.

**Control Inheritance** — The concept that a control implemented centrally (such as centralized identity management) is credited to all systems that rely on it, without each system independently implementing the control.

**Compliance Dashboard** — A real-time or near-real-time view aggregating data from multiple security tools to display an organization's current compliance posture against a selected framework.

---

## Section 2 — Control Frameworks Compared

### NIST Cybersecurity Framework

The NIST CSF is outcome-based and technology-neutral. It does not tell you which tools to use — it tells you what outcomes you need to achieve. This flexibility makes it broadly applicable.

The six CSF 2.0 functions and their core concerns:

**Govern** (new in v2.0) — Organizational context, risk management strategy, supply chain risk, policies, oversight.

**Identify** — Asset management, business environment, governance, risk assessment, risk management strategy.

**Protect** — Identity management and access control, awareness and training, data security, information protection processes and procedures, maintenance, protective technology.

**Detect** — Anomalies and events, security continuous monitoring, detection processes.

**Respond** — Response planning, communications, analysis, mitigation, improvements.

**Recover** — Recovery planning, improvements, communications.

For the CySA+ exam, the Detect function is the most directly relevant to analyst work. Understand that continuous monitoring, anomaly detection, and detection process maintenance all fall under Detect.

### CIS Controls v8

The CIS Controls take a different approach — they are highly prescriptive. Rather than describing outcomes, they describe specific safeguards. This makes them excellent for implementation guidance and gap analysis but potentially too rigid for organizations with unusual architectures.

The 18 controls are:

1. Inventory and Control of Enterprise Assets
2. Inventory and Control of Software Assets
3. Data Protection
4. Secure Configuration of Enterprise Assets and Software
5. Account Management
6. Access Control Management
7. Continuous Vulnerability Management
8. Audit Log Management
9. Email and Web Browser Protections
10. Malware Defenses
11. Data Recovery
12. Network Infrastructure Management
13. Network Monitoring and Defense
14. Security Awareness and Skills Training
15. Service Provider Management
16. Application Software Security
17. Incident Response Management
18. Penetration Testing

CIS Controls 1 through 6 are the foundational hygiene controls — organizations that cannot pass these have fundamental security problems that make the rest of the controls less effective.

### NIST SP 800-53

NIST 800-53 revision 5 contains over 1,000 individual controls organized into 20 control families. It is the most comprehensive control catalog available and is mandatory for federal agencies.

The 20 control families include: Access Control (AC), Audit and Accountability (AU), Configuration Management (CM), Incident Response (IR), Maintenance (MA), Risk Assessment (RA), System and Communications Protection (SC), System and Information Integrity (SI), and others.

Analysts supporting federal contracts or FedRAMP-authorized cloud products will work with 800-53 regularly.

---

## Section 3 — Control Testing Methodology

### The Three Testing Methods

NIST defines three methods for assessing whether controls are implemented and effective:

**Examine** — Review documentation, policy, configurations, and system records. Examination confirms design intent. Example: reviewing a firewall ruleset to verify that inbound RDP from the internet is blocked.

**Interview** — Question personnel responsible for implementing, operating, and overseeing controls. Interviews confirm procedural compliance. Example: asking the SOC manager whether analysts review privilege escalation alerts daily as required by policy.

**Test** — Exercise the control and observe whether it functions as intended. Testing confirms operational effectiveness. Example: sending a test phishing email to verify that email filtering quarantines it before delivery.

Examination alone can confirm a control exists. Only testing confirms it works.

### Testing Cadence

Controls should be tested on a schedule tied to their risk level and rate of change. Critical controls (MFA, privileged access management, network egress filtering) should be tested more frequently than lower-risk controls. After any significant infrastructure change, affected controls should be re-tested.

Penetration testing provides the most rigorous form of control testing by having skilled adversaries actively attempt to defeat the controls.

---

## Section 4 — Regulatory Compliance Requirements

### HIPAA

The HIPAA Security Rule requires covered entities and business associates to implement administrative, physical, and technical safeguards to protect electronic Protected Health Information (ePHI). Required safeguards include access controls, audit controls, integrity controls, and transmission security.

### PCI DSS

PCI DSS version 4.0 contains 12 requirements organized around protecting cardholder data. Requirements include maintaining a secure network, protecting cardholder data, managing vulnerabilities, implementing strong access control, monitoring and testing networks, and maintaining an information security policy.

### SOX

Sarbanes-Oxley Section 404 requires management to assess and report on internal controls over financial reporting. IT controls protecting financial systems — access controls, change management, backup and recovery — fall under SOX scope.

### GDPR

The GDPR requires organizations handling EU resident data to implement "appropriate technical and organizational measures" to protect personal data. Breach notification is required within 72 hours of discovery.

---

## Section 5 — Gap Analysis Methodology

A gap analysis is the systematic process of identifying where your current security program falls short of a target standard. It is the foundation for security roadmap development.

### Step-by-Step Process

**Step 1 — Scope the analysis.** Define which framework or regulation you are measuring against and which systems, business units, or processes are in scope.

**Step 2 — Gather current state documentation.** Collect information about existing controls through policy review, technical configuration review, and interviews.

**Step 3 — Map existing controls to framework requirements.** For each framework requirement, identify which existing control (if any) satisfies it.

**Step 4 — Identify gaps.** A gap exists where a requirement has no satisfying control, or where the existing control partially satisfies the requirement.

**Step 5 — Rate gap severity.** Score each gap by the risk it represents. Consider: what is the likelihood of exploitation if this control is absent, and what is the potential impact?

**Step 6 — Produce the gap report.** Document each gap with a description, severity rating, current state, target state, and recommended remediation actions.

**Step 7 — Develop the remediation roadmap.** Prioritize gaps by risk. Assign owners. Set target completion dates. Build into the organization's security roadmap.

### Common Gap Analysis Pitfalls

Analysts performing gap analysis frequently make these mistakes:

Confusing control existence with control effectiveness. A firewall ruleset that exists but is not reviewed is not an effective control.

Over-relying on self-reported compliance. Personnel will often say a control is implemented when it is not consistently applied.

Ignoring control scope exceptions. MFA that is enforced for all users except the five legacy application service accounts is not fully implemented MFA.

---

## Section 6 — Audit Evidence Best Practices

When supporting an audit, analysts produce evidence packages that demonstrate control operation. Best practices include:

**Timeliness** — Collect evidence from the audit period. Evidence of controls operating last year does not demonstrate they are operating today.

**Completeness** — Evidence must cover the full scope. A log extract covering one week of a three-month audit period is insufficient.

**Integrity** — Evidence must be unaltered. Log exports should include hash verification or be exported directly from the logging system.

**Specificity** — Evidence must clearly demonstrate the specific control being validated. Generic screenshots that could apply to any system are weak evidence.

**Traceability** — Evidence should be labeled with the control requirement it satisfies, the system it came from, and the date it was collected.

---

## Section 7 — CySA+ Exam Focus Areas

The exam tests compliance and controls validation at several specific levels:

- Know the NIST CSF five/six functions by name and be able to assign security activities to the correct function
- Know that CIS Controls are organized into 18 controls and three implementation groups
- Distinguish control types (technical, administrative, physical) and functions (preventive, detective, corrective, deterrent)
- Understand gap analysis as a process — be able to describe what a gap is and how it is identified
- Know what audit evidence is required for a given control type
- Understand continuous monitoring as the mechanism that moves compliance from point-in-time to ongoing

---


---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 13 — Compliance and Security Controls Validation** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 13 — Compliance and Security Controls Validation**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 13 — Compliance and Security Controls Validation**:

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
> **Question:** In the context of **Module 13 — Compliance and Security Controls Validation**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


## Study Checklist

- [ ] Define all glossary terms without referencing notes
- [ ] List the NIST CSF functions in order and describe what each covers
- [ ] Name the first six CIS Controls from memory
- [ ] Classify five example controls by type (technical/administrative/physical) and function (preventive/detective/corrective/deterrent)
- [ ] Describe the seven steps of gap analysis
- [ ] List four types of audit evidence and explain what each demonstrates
- [ ] Explain the difference between a point-in-time audit and continuous monitoring
- [ ] Complete the Module 13 Lab
- [ ] Complete the Module 13 Quiz
- [ ] Post your Module 13 Discussion initial post by Wednesday

---

## 9. Supplemental Resources

**1. NIST Cybersecurity Framework v2.0 — Official Documentation**
<https://www.nist.gov/cyberframework>
The authoritative source for NIST CSF v2.0, which added the Govern function and updated guidance across Identify, Protect, Detect, Respond, and Recover. The site includes the full framework core, implementation tiers, profiles, and quick-start guides by organization type. For the exam, the ability to map an organizational activity to the correct CSF function is a high-frequency question type — this resource provides the primary reference material for that skill.

**2. CIS Controls v8 — Center for Internet Security**
<https://www.cisecurity.org/controls/v8>
The definitive reference for all 18 CIS Controls and their associated Safeguards, including Implementation Group (IG1/IG2/IG3) assignments. Each Control includes a "why" statement, asset type, security function, and specific Safeguards with activity descriptions. For compliance and gap analysis work, this resource is the mapping authority — exam questions regularly present a security gap and ask which CIS Safeguard addresses it. The free download requires registration.

**3. CISA Cybersecurity Performance Goals (CPGs)**
<https://www.cisa.gov/cross-sector-cybersecurity-performance-goals>
CISA's voluntary baseline security practices for critical infrastructure, cross-walked to NIST CSF and CIS Controls. The CPGs represent the minimum security baseline that CISA recommends all organizations achieve regardless of sector. Reviewing the CPG table reinforces the practical application of compliance frameworks — mapping CPG items to their parent NIST CSF function and CIS Control Safeguard builds the multi-framework translation skill tested in CySA+ Domain 2 and Domain 3 scenario questions.

---

## Required Resources

- NIST Cybersecurity Framework v2.0 — nist.gov/cyberframework (free)
- CIS Controls v8 — cisecurity.org/controls (free registration required)
- NIST SP 800-53 Rev. 5 — nvlpubs.nist.gov (free)
- CompTIA CySA+ CS0-003 Exam Objectives — Domains 2 and 3
- Module 13 Video Lecture (Professor Nash)
