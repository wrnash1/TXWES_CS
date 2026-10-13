# Reading Guide: Module 10 — Application Security


<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CIS-4328 Module 10</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy" title="CompTIA Security+ (SY0-701) Complete Training Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Security+ (SY0-701) Complete Training Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->


## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports the Module 10 video lectures on application security. Application security content appears throughout the Security+ exam, particularly in scenarios involving web application vulnerabilities and secure development practices. Complete all readings before the quiz and lab.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the security activities that occur in each phase of the Secure SDLC
2. Apply the STRIDE threat model to identify threats in a system design
3. Explain the OWASP Top 10 vulnerabilities from an attacker and defender perspective
4. Distinguish between input validation and output encoding and apply each correctly
5. Describe secure coding practices including error handling, cryptography, and secrets management
6. Conduct a structured security-focused code review using a checklist approach
7. Compare SAST and DAST tools: what each finds, when each runs, and their limitations
8. Describe how SCA tools address third-party dependency risks

---

## Assigned Readings (Zero-Cost / Open Access)

### Primary Reading

**OWASP Top 10 — 2021**

- Access: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
- Read: All 10 categories with their description, example attack scenarios, and prevention guidance
- Focus areas: A01 Broken Access Control, A03 Injection, A07 Identification and Authentication Failures, A08 Software and Data Integrity Failures
- Estimated reading time: 45–60 minutes

**OWASP Input Validation Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- Read: Full document
- Focus areas: allowlist vs. blocklist, server-side enforcement, canonicalization

**OWASP XSS Prevention Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Read: Full document
- Focus areas: output encoding rules by context, Content Security Policy

### Supplemental Reading

**OWASP SQL Injection Prevention Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Read: Full document
- Focus areas: parameterized queries, stored procedures, escaping as last resort

**OWASP Authentication Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- Read: Sections 1–4 (password storage, authentication guidelines, session management basics)

**Microsoft Threat Modeling Tool Documentation — STRIDE**

- Access: [https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- Read: Full page
- Focus: STRIDE category definitions and example mitigations

---

## Key Terms and Definitions

**Secure SDLC (S-SDLC)** — A software development lifecycle that integrates security activities into every phase: requirements, design, implementation, testing, deployment, and maintenance.

**Threat Modeling** — A structured process for identifying, enumerating, and prioritizing security threats against a system before implementation.

**STRIDE** — A threat modeling framework representing six categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.

**Trust Boundary** — A line in a data flow diagram marking where data moves between security domains with different privilege levels; a primary focus of threat modeling.

**OWASP Top 10** — The Open Web Application Security Project's list of the ten most critical web application security risks, updated periodically.

**Broken Access Control (A01)** — A class of vulnerabilities where users can act outside their intended permissions, including IDOR and horizontal/vertical privilege escalation.

**IDOR (Insecure Direct Object Reference)** — A specific type of broken access control where an application exposes a direct reference to an internal object (such as a database key) without verifying the requesting user's authorization.

**Injection (A03)** — A class of attacks where untrusted data is sent to an interpreter as part of a command or query, causing the interpreter to execute attacker-controlled data as code.

**SQL Injection** — An injection attack that inserts malicious SQL code into a query, allowing attackers to bypass authentication, retrieve data, or modify the database.

**Parameterized Query** — A SQL query template where user-supplied values are passed separately from the query structure, preventing injection; also called a prepared statement.

**XSS (Cross-Site Scripting)** — An injection attack where malicious scripts are injected into web pages viewed by other users; exploits insufficient output encoding.

**Reflected XSS** — XSS where the malicious script is reflected off the web server in the immediate response to a crafted request.

**Stored XSS** — XSS where the malicious script is permanently stored on the server (in a database, comment field, etc.) and served to all users who view the content.

**CSP (Content Security Policy)** — A browser security header that restricts the sources from which scripts, styles, and other resources may be loaded.

**Input Validation** — The process of verifying that data entering an application conforms to expected type, length, range, and format before processing.

**Output Encoding** — The process of converting special characters in data to safe representations appropriate for the output context, preventing injection into HTML, JavaScript, SQL, or other languages.

**SAST (Static Application Security Testing)** — Automated analysis of source code, bytecode, or binary code to identify security vulnerabilities without executing the application.

**DAST (Dynamic Application Security Testing)** — Automated security testing of a running application from the outside, simulating external attacker behavior.

**IAST (Interactive Application Security Testing)** — Security testing that uses an agent embedded in the running application to monitor execution during functional tests.

**SCA (Software Composition Analysis)** — Automated analysis of third-party libraries and open-source dependencies to identify known vulnerabilities.

**Credential Stuffing** — An attack that uses breach databases of stolen username/password pairs to authenticate against other services, exploiting password reuse.

**Defense in Depth** — A security strategy that uses multiple overlapping controls so that the failure of one control does not lead to full compromise.

**Shift Left** — The practice of moving security testing and validation earlier in the development lifecycle to reduce the cost and impact of discovered vulnerabilities.

---

## Concept Deep Dives

### STRIDE Applied — Worked Example

Imagine you are threat modeling a web application login endpoint. The endpoint accepts a username and password over HTTPS and validates credentials against a database.

Apply STRIDE at the trust boundary where the user's browser submits credentials to the web server:

| Threat | STRIDE Category | Example | Mitigation |
|---|---|---|---|
| Attacker submits stolen credentials | Spoofing | Credential stuffing attack | MFA, rate limiting, breach password checking |
| Attacker intercepts credentials in transit | Tampering | MITM on HTTP (not HTTPS) | Enforce HTTPS, HSTS header |
| User denies logging in | Repudiation | Insider disputes audit log | Log authentication events with timestamp and IP |
| Error message reveals username validity | Information Disclosure | "That username does not exist" | Return generic error: "Invalid username or password" |
| Attacker floods login with requests | Denial of Service | Brute force / rate exhaustion | Rate limiting, CAPTCHA, account lockout |
| Attacker escalates after login | Elevation of Privilege | Exploits session fixation | New session token on authentication |

Every row becomes a security requirement or design decision.

### SAST vs. DAST — Decision Guide

| Question | SAST | DAST |
|---|---|---|
| When does it run? | At code commit / build time | Against running application in staging |
| Does it need source code? | Yes | No |
| Does it need the app to run? | No | Yes |
| False positive rate | Higher | Lower |
| Finds code-level flaws? | Yes | Partially |
| Finds runtime/config flaws? | No | Yes |
| Can pinpoint vulnerable line? | Yes | No |
| Suitable for production use? | Yes (code review) | No (can disrupt services) |

---

## Security+ Exam Alignment

### Relevant Exam Objectives (SY0-701)

- **1.3** — Explain various types of vulnerabilities (web application vulnerabilities: injection, XSS, IDOR, CSRF, directory traversal, insecure deserialization)
- **2.4** — Explain the importance of resilience and recovery in security architecture (secure coding, code review)
- **2.6** — Explain the security implications of proper hardware, software, and data asset management (SAST, DAST, SCA)

### High-Probability Exam Topics from This Module

- Distinguishing SQL injection from XSS: injection targets the database/server; XSS targets the client browser
- Identifying the correct defense for injection attacks (parameterized queries, not input validation alone)
- Distinguishing reflected XSS from stored XSS
- Identifying IDOR as a broken access control vulnerability
- Knowing that SAST runs without executing the application; DAST requires a running application
- Understanding credential stuffing vs. brute force (stuffing uses real breach credentials; brute force tries all combinations)

---

## Review Questions (Self-Check — Not Graded)

1. A developer writes a search function that builds a SQL query by concatenating user input with no validation or parameterization. An attacker enters `'; DROP TABLE users; --`. What type of attack is this and what is the correct remediation?

2. A web application displays a user's profile name on the page without encoding. A user saves their profile name as `<script>alert('XSS')</script>`. When another user views the first user's profile, a JavaScript alert fires. What type of XSS is this and what control would prevent it?

3. A developer implements server-side access control for an API endpoint but the front-end JavaScript also hides the "Admin" button from non-admin users. An attacker bypasses the JavaScript and calls the API endpoint directly. Is the application vulnerable? Why?

4. A SAST tool flags a line of code as a potential SQL injection vulnerability. The developer argues the flagged code is actually safe because the input is already validated upstream. Is the developer necessarily correct? What is the name of this SAST limitation?

5. An organization wants to find vulnerabilities in the third-party npm packages their Node.js application uses. Which tool category addresses this need?

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 10*



---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 10 — Application Security** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 10 — Application Security**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 10 — Application Security**:

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
> **Question:** In the context of **Module 10 — Application Security**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
