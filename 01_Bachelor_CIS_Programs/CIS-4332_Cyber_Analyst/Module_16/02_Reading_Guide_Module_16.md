# Reading Guide: Module 16 — CySA+ CS0-003 Exam Preparation and Capstone

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
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA / CertifyBreakfast &bull; CIS-4332 Module 16</strong>
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

Module 16 is the capstone of CIS-4332. This reading guide provides a comprehensive review of all four CySA+ CS0-003 exam domains, exam strategy guidance, and a high-yield terms reference spanning the entire course.

Use this guide as your primary study document for the two weeks before your exam. Work through each domain section systematically, self-test on the study checklists, and use the practice questions in the Module 16 Quiz to assess your readiness.

The CySA+ CS0-003 exam is scenario-based. You will be given situations and asked what to do — not asked to recite definitions. The goal of this guide is to ensure you can apply concepts, not just recall them.

---

## Section 1 — Exam Structure Reference

The CySA+ CS0-003 exam:

- Maximum 85 questions
- 165-minute time limit
- Passing score: 750 out of 900
- Question types: multiple choice (single answer), multiple select (multiple correct), performance-based (PBQ)
- Performance-based questions appear first and carry more point weight

Domain weights:

- Domain 1 — Security Operations: 33%
- Domain 2 — Vulnerability Management: 30%
- Domain 3 — Incident Response and Digital Forensics: 20%
- Domain 4 — Reporting and Communication: 17%

---

## Section 2 — Domain 1: Security Operations

### Key Topics

**Network and System Architecture** — Analysts must understand how data flows through environments to know where to place monitoring sensors and what log sources exist. Key concepts: DMZ, segmented networks, cloud shared responsibility, east-west versus north-south traffic.

**Log Analysis and Monitoring** — Know these log types and what each captures: Windows Security event logs (authentication, process creation, service installation), syslog (Linux/Unix systems and network devices), firewall logs (allow/deny, source/destination), proxy logs (URLs, user agents, response codes), DNS logs (queries, responses, NXDOMAIN). Know how SIEM correlation rules combine these sources.

**SIEM Operations** — Know true positive vs. false positive vs. false negative vs. benign true positive. Know alert triage workflow. Know how to tune correlation rules to reduce false positives without creating false negatives.

**Threat Intelligence** — Know the four types of intelligence: strategic (for executives, risk trends), operational (for management, current campaigns), tactical (for analysts, IoCs for immediate use), technical (machine-readable data, STIX/TAXII). Know the intelligence lifecycle: direction, collection, processing, analysis, dissemination, feedback.

**Security Tools** — Know the function and distinction between: SIEM, SOAR, EDR, XDR, IDS/IPS, vulnerability scanner, threat intelligence platform, DLP, WAF.

**Threat Hunting** — Know the hunting loop (hypothesis → investigate → uncover → inform), MITRE ATT&CK structure (tactics vs. techniques), and key ATT&CK technique IDs for common attack patterns.

**Automation** — Know what SOAR does, how it differs from SIEM, Python scripting use cases for analysts, regex for log parsing, and REST API integration patterns.

### Domain 1 High-Yield Question Triggers

Questions will often describe an analyst workflow and ask which tool is most appropriate. Map tools to functions precisely. Questions about log analysis will show a log excerpt and ask what it means. Know key event IDs (4624, 4625, 4648, 4688, 4720, 7045, 1102). Questions about threat intelligence will describe a type of intelligence and ask how it is used.

---

## Section 3 — Domain 2: Vulnerability Management

### Key Topics

**Vulnerability Scanning** — Know the difference between: agent-based (installed on endpoint, continuous collection) vs. agentless (network-based, periodic); credentialed (uses authentication, sees OS-level detail) vs. non-credentialed (sees only network-exposed services). Credentialed scans find significantly more vulnerabilities.

**CVSS Scoring** — Know the CVSS v3.1 Base Score components: Attack Vector (Network, Adjacent, Local, Physical), Attack Complexity (Low, High), Privileges Required (None, Low, High), User Interaction (None, Required), Scope (Unchanged, Changed), Confidentiality/Integrity/Availability Impact (None, Low, High). Know that EPSS provides probability of exploitation within 30 days.

**Vulnerability Prioritization** — Risk = Likelihood × Impact. CVSSv3 base score measures severity. EPSS measures exploitation probability. Business context (asset criticality, data classification, internet-facing status) further modifies priority. A Critical CVSS score on an internal test server is lower priority than a High score on an internet-facing production server.

**Remediation Tracking** — Know patching SLAs by severity tier. Know that not all vulnerabilities can be patched — compensating controls (network segmentation, WAF rules, enhanced monitoring) address vulnerabilities that cannot be remediated.

**Special Environment Scanning** — Cloud: shared responsibility model determines scan scope. OT/ICS: scanning can disrupt industrial processes; passive monitoring preferred. IoT: may lack agent support; network-based identification required.

**Penetration Testing vs. Vulnerability Assessment** — Vulnerability assessment identifies weaknesses. Penetration testing actively exploits them to prove impact. Pen tests require written authorization (rules of engagement). Vulnerability assessments are less intrusive and run more frequently.

### Domain 2 High-Yield Question Triggers

Questions about scan type selection: identify whether the scenario requires internal visibility (credentialed) or external visibility (non-credentialed). Questions about prioritization: apply CVSS and business context together — never prioritize on CVSS score alone. Questions about remediation: distinguish patching, configuration changes, and compensating controls.

---

## Section 4 — Domain 3: Incident Response and Digital Forensics

### Key Topics

**NIST SP 800-61 Phases** — Know all four phases in order and what analysts do in each. Preparation: policies, playbooks, tools, training. Detection and Analysis: triage, scoping, IoC extraction, severity classification. Containment/Eradication/Recovery: short-term vs. long-term containment, persistence removal, restoration. Post-Incident Activity: lessons learned, action items, metrics.

**Severity Classification** — NIST 800-61 uses three dimensions: functional impact (None/Minimal/Significant/Severe), information impact (None/Privacy Breach/Proprietary Breach/Integrity Loss), recoverability (Regular/Supplemented/Extended/Not Recoverable).

**Digital Forensics Principles** — Order of volatility (RAM most volatile, disk least). Chain of custody (documented, unbroken, hashed). Working from forensic copies, not originals. Documentation of every action taken.

**Memory Forensics** — Volatility key plugins: `pslist` (process list), `pstree` (process tree), `netscan` (network connections), `malfind` (code injection), `cmdline` (command-line arguments), `dlllist` (loaded DLLs).

**Disk Forensics** — Key Windows artifacts: registry (persistence keys), prefetch files (execution history), event logs (authentication and process events), shellbags (folder navigation history), MFT (file system metadata including deleted files), Amcache/ShimCache (execution evidence).

**Network Forensics** — Wireshark display filters, TCP stream reconstruction, protocol anomaly identification, beaconing detection.

**Anti-Forensics** — Timestomping (MACB timestamp manipulation, detectable via MFT attribute comparison), log clearing (Event ID 1102), living-off-the-land (LOLBins), secure file deletion.

### Domain 3 High-Yield Question Triggers

Questions about what to do FIRST will almost always want you to follow volatility order or the correct IR phase sequence. Questions about evidence will test chain of custody requirements. Questions about forensic artifacts will ask what artifact proves a specific action occurred.

---

## Section 5 — Domain 4: Reporting and Communication

### Key Topics

**Metrics** — Know precise definitions: MTTD (detection time), MTTR (response time), MTTC (contain time). Know that these metrics feed IR program investment decisions.

**Vulnerability Report Structure** — Executive summary (risk language, business impact, no jargon), technical findings (CVE IDs, CVSS scores, affected assets, reproduction steps), remediation recommendations (specific, prioritized, with responsible owners).

**Incident Report Structure** — Executive summary, incident timeline, scope and affected systems, root cause analysis, containment and eradication actions taken, lessons learned, remediation recommendations, appendices (evidence, IoC list).

**Communicating to Executives** — Translate technical risk into business language. "We have 47 critical vulnerabilities" means nothing to an executive. "Three of our customer-facing web applications have remotely exploitable vulnerabilities that could expose customer payment data" is actionable.

**Compliance Reporting** — Know the difference between: gap reports (current vs. target state), audit evidence packages (proof of control operation), compliance dashboards (real-time posture metrics), and remediation plans (prioritized action items with owners and timelines).

### Domain 4 High-Yield Question Triggers

Questions about who receives which type of report: executives get summaries and risk language; technical teams get findings and remediation detail. Questions about metrics: apply the precise definition — do not confuse MTTD (detection) with MTTR (response). Questions about compliance: match the report type to the stakeholder and purpose.

---

## Section 6 — All-Course High-Yield Term Reference

This section lists the highest-frequency terms across all 16 modules, organized alphabetically within domain. Quiz yourself: cover the right column and state the definition from memory.

**Security Operations:**

- ATT&CK Tactic — The "why" of adversary behavior (high-level goal)
- ATT&CK Technique — The "how" of adversary behavior (specific method)
- Beaconing — Regular, timed C2 check-in connections
- DGA — Domain Generation Algorithm malware for C2 resilience
- Dwell Time — Gap between compromise and detection
- EDR — Endpoint telemetry collection and detection platform
- Hunting Loop — Hypothesis → Investigate → Uncover → Inform → Repeat
- IoC — Observable evidence of compromise (IP, hash, domain, registry key)
- SIEM — Log aggregation, correlation, and alerting platform
- SOAR — Alert enrichment, orchestration, and automated response platform
- STIX/TAXII — IoC sharing format and transport protocol
- XDR — Cross-domain telemetry integration platform

**Vulnerability Management:**

- CVSS — Common Vulnerability Scoring System (base score 0–10)
- EPSS — Exploit Prediction Scoring System (probability of exploitation)
- False Negative — Missed vulnerability that the scanner should have found
- False Positive — Reported vulnerability that does not actually exist
- Patch Tuesday — Microsoft's second Tuesday monthly patching cycle
- Remediation SLA — Maximum allowed days to patch by severity tier
- Risk-based Prioritization — Combining CVSS, EPSS, and business context

**Incident Response:**

- Chain of Custody — Documented unbroken evidence handling record
- Containment — Stopping incident spread without full remediation
- Eradication — Removing root cause including all persistence mechanisms
- MTTC — Mean Time to Contain
- MTTD — Mean Time to Detect
- MTTR — Mean Time to Respond
- Order of Volatility — Evidence collection sequence: RAM → Network → Disk
- Playbook — Step-by-step IR procedure for a specific incident type
- Triage — Initial alert classification for severity and scope

**Digital Forensics:**

- MACB Timestamps — Modified, Accessed, Changed, Born file system timestamps
- Malfind — Volatility plugin detecting process injection via RWX memory regions
- MFT — Master File Table (NTFS index including deleted file records)
- Prefetch File — Windows execution history artifact (proves a program ran)
- Shellbag — Registry artifact recording folder navigation history
- Timestomping — Anti-forensic MACB timestamp manipulation

---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 16 — CySA+ CS0-003 Exam Preparation and Capstone** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 16 — CySA+ CS0-003 Exam Preparation and Capstone**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 16 — CySA+ CS0-003 Exam Preparation and Capstone**:

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
> **Question:** In the context of **Module 16 — CySA+ CS0-003 Exam Preparation and Capstone**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**

## Study Checklist — Final Exam Preparation

- [ ] State all four CySA+ CS0-003 domains and their percentage weights from memory
- [ ] Describe what analysts do in each NIST 800-61 phase
- [ ] Explain the difference between SIEM and SOAR with a concrete example
- [ ] Define MTTD, MTTR, and MTTC precisely
- [ ] List five Volatility plugins and what each reveals
- [ ] Name six key Windows disk artifacts and what each proves
- [ ] Explain the CVSS + EPSS + business context prioritization model
- [ ] Describe the hunting loop in four steps
- [ ] State the key difference between a vulnerability assessment and a penetration test
- [ ] Explain what breaks chain of custody and why it matters
- [ ] Complete the Module 16 Capstone Lab (20-question practice exam)
- [ ] Complete the Module 16 Quiz
- [ ] Post your Module 16 Discussion initial post by Wednesday

---

## 9. Supplemental Resources

**1. CompTIA CySA+ CS0-003 Official Exam Objectives**
<https://www.comptia.org/training/resources/exam-objectives>
The authoritative source for the CySA+ CS0-003 exam domain weights, objective statements, and topic coverage. The exam objectives document is the single most important study reference because it defines exactly what CompTIA will test. Each objective is a direct signal about what you must know. Download the free PDF and use it as a checklist — cross-reference every objective against the course modules to identify any remaining gaps before exam day. Pay particular attention to the domain weights (Domain 1: 33%, Domain 2: 30%, Domain 3: 20%, Domain 4: 17%) to allocate review time proportionally.

**2. Professor Messer's CompTIA CySA+ Course Notes**
<https://www.professormesser.com/cysa-plus/cs0-003/cs0-003-video/cs0-003-training-course/>
Professor Messer provides free video training for every CompTIA certification exam, including CySA+ CS0-003. His course covers all exam domains with concise, exam-focused explanations and is widely used as a final exam preparation resource by security professionals. The short-format videos (typically 5–15 minutes per topic) are well-suited for reviewing specific concept areas where additional reinforcement is needed after completing this course. The accompanying study group and practice questions on his site complement the capstone lab questions in this module.

**3. CompTIA CertMaster Practice — CySA+ CS0-003**
<https://www.comptia.org/training/certmaster-practice/cysa>
CompTIA's official adaptive practice question platform for CySA+ provides scenario-based questions that mirror the actual exam format, difficulty, and reasoning style. The platform adapts to your performance, focusing additional questions on weak areas. While this is a paid resource (available standalone or bundled with exam purchase), it is the closest available simulation to actual exam conditions. The reasoning explanations for both correct and incorrect answers mirror the distractor analysis format used throughout this course and reinforce the specific "why" behind each correct answer that the exam tests.

---

## Required Resources

- CompTIA CySA+ CS0-003 Official Exam Objectives — comptia.org (free)
- NIST SP 800-61 Rev. 2 — nvlpubs.nist.gov (free)
- MITRE ATT&CK Enterprise Matrix — attack.mitre.org (free)
- CompTIA CertMaster Learn or Professor Messer's CySA+ course (recommended supplemental)
- Module 16 Video Lecture (Professor Nash)
