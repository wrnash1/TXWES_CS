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

This reading guide supports Module 10: Application Security. You will study the OWASP Top 10, the secure software development lifecycle, testing methodologies, and code signing. These topics map to Security+ Domain 4 (Application Security) and appear throughout real-world security assessments and breach investigations.

**Estimated reading and study time:** 2.5 to 3 hours

---

## Learning Objectives

By the end of this module you should be able to:

- Identify and describe each of the ten OWASP Top 10 vulnerability categories.
- Explain the mechanisms behind injection, XSS, IDOR, and SSRF attacks.
- Compare static application security testing (SAST) and dynamic application security testing (DAST).
- Describe the phases of a secure software development lifecycle.
- Explain what code signing proves and what it does not prove.
- Identify security controls appropriate for each OWASP category.

---

## Required Reading

### OER Textbook Sections

Refer to the ZTC_OER_Reading_Materials list for open-access chapter links. For this module read:

- **OWASP Top 10 2021** — Full document (free at owasp.org/Top10)
- **OWASP Testing Guide v4.2** — Chapter 1: Introduction to the OWASP Testing Guide
- **NIST SP 800-64** — Security Considerations in the System Development Life Cycle, Sections 2 and 3
- **Professor Messer Security+ SY0-701 Study Guide** — Domain 4 sections on application security

---

## Section A — OWASP Top 10 (2021)

The OWASP Top 10 is the industry-standard reference for web application security risk. The 2021 edition reflects data from thousands of organizations and hundreds of security firms. Each category has an assigned identifier (A01 through A10), example attack scenarios, and recommended countermeasures.

### A01 — Broken Access Control

Access control enforces the rule that authenticated users may only access resources and perform actions within their intended permissions. Broken Access Control moved to number one in 2021, appearing in 94 percent of applications tested. The key subtypes are:

- **Vertical privilege escalation**: A regular user accesses admin functions.
- **Horizontal privilege escalation / IDOR**: A user accesses another user's resources by manipulating an ID in the request.
- **Forced browsing**: Accessing URLs that are not linked but are accessible without authorization.

The primary countermeasure is server-side enforcement of access control checks on every protected resource, every time.

### A02 — Cryptographic Failures

This category captures failures in protecting data in transit and at rest. Key failure modes include:

- Transmitting sensitive data over HTTP (unencrypted).
- Using deprecated algorithms: MD5, SHA-1, DES, 3DES, RC4.
- Storing passwords as plain text or reversibly encrypted rather than using one-way hashing with a salt.
- Generating weak random values for cryptographic functions.

Current recommendations include TLS 1.2 or 1.3 for transport, bcrypt or Argon2 for password hashing, and AES-256-GCM for symmetric encryption of stored sensitive data.

### A03 — Injection

Injection flaws occur when the interpreter cannot distinguish between code/commands and data. Subtypes include SQL injection, LDAP injection, OS command injection, and template injection.

Parameterized queries are the primary defense against SQL injection. The key principle is that user-supplied data must never be directly concatenated into query or command strings.

### A04 — Insecure Design

Insecure design covers architectural weaknesses that no implementation fix can fully address. Threat modeling during the design phase is the countermeasure. The STRIDE methodology — Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege — provides a structured approach to identifying design-level threats.

### A05 — Security Misconfiguration

This category spans all layers of the stack: network, platform, web server, application server, database, and framework. Common misconfigurations include:

- Default credentials on databases, admin panels, or network devices.
- Directory listing enabled on web servers.
- Verbose error messages or stack traces exposed to users.
- Overly permissive cloud storage policies (public S3 buckets).
- Unnecessary features, ports, or services enabled.

Automated configuration management and hardening baselines are the primary countermeasures.

### A06 — Vulnerable and Outdated Components

Applications depend on third-party libraries, frameworks, and runtime environments. Each dependency may carry known vulnerabilities. Key concepts:

- **CVE (Common Vulnerabilities and Exposures)**: A public list of known software vulnerabilities maintained by MITRE.
- **CVSS (Common Vulnerability Scoring System)**: A numerical score (0–10) that rates the severity of CVEs.
- **SBOM (Software Bill of Materials)**: A formal list of all components in a software product, enabling rapid identification of affected systems when new CVEs are published.

### A07 — Identification and Authentication Failures

Authentication failures include weak password policies, missing multi-factor authentication, broken session management, and insecure credential storage. Two specific attack types to know:

- **Credential stuffing**: Using lists of known username/password pairs from previous breaches to automate login attempts against other sites.
- **Session fixation**: An attacker establishes a known session token and tricks the victim into using it, gaining access after the victim authenticates.

### A08 — Software and Data Integrity Failures

This category covers scenarios where applications rely on plugins, libraries, or updates from untrusted sources without integrity verification. Supply chain attacks, where malicious code is inserted into the software build or distribution process, fall under this category.

Subresource Integrity (SRI) is a browser mechanism that verifies the integrity of externally loaded JavaScript by comparing a cryptographic hash in the HTML tag to the actual file hash.

### A09 — Security Logging and Monitoring Failures

Without adequate logging, breaches go undetected for extended periods. Effective logging requires:

- Recording all authentication attempts (success and failure).
- Capturing the source IP, timestamp, and user identity for all security-relevant events.
- Storing logs on a separate, protected system the application cannot modify.
- Alerting on anomalous patterns in near real-time.

A SIEM (Security Information and Event Management) system centralizes log collection and applies correlation rules to detect threats.

### A10 — Server-Side Request Forgery (SSRF)

SSRF forces the server to make outbound HTTP requests to attacker-chosen destinations. In cloud environments, SSRF frequently targets the instance metadata service (IMDS) at 169.254.169.254 to retrieve IAM credentials. Countermeasures include URL allow-listing, blocking RFC-1918 addresses in outbound requests, and restricting outbound network access from application servers.

---

## Section B — Secure Software Development Lifecycle

The Secure SDLC integrates security activities into every phase rather than treating security as a final gate.

### Phase 1 — Requirements

Security requirements are gathered alongside functional requirements. This includes identifying applicable regulations (PCI-DSS for payment card data, HIPAA for health data, GDPR for personal data of EU residents), conducting an initial data classification, and capturing security acceptance criteria for each user story.

### Phase 2 — Design

Threat modeling identifies potential attack vectors before implementation. The output of threat modeling is a list of threats with associated mitigations designed into the architecture. Data flow diagrams (DFDs) identify trust boundaries where data crosses from one zone to another.

Secure design principles applied in this phase:

- **Least privilege**: Components receive only the permissions they require.
- **Defense in depth**: Multiple layers of controls so no single failure is catastrophic.
- **Fail-safe defaults**: Default behavior denies access; access must be explicitly granted.
- **Separation of duties**: No single component or user controls an entire sensitive workflow.
- **Economy of mechanism**: Simple designs are easier to analyze and secure than complex ones.

### Phase 3 — Development

Secure coding standards provide language-specific guidelines. Peer code review with a security checklist ensures a second developer validates security-relevant code paths. Pre-commit hooks prevent secrets — API keys, passwords, private keys — from entering version control.

### Phase 4 — Testing

Security testing includes SAST, DAST, and penetration testing. Security test cases derived from the threat model are executed alongside functional tests. Acceptance criteria include passing SAST and DAST scans with no critical or high findings.

### Phase 5 — Deployment

Hardened build pipelines sign artifacts and verify integrity before deploying to production. Configuration baselines are applied to infrastructure. Deployment to production requires formal change approval.

### Phase 6 — Maintenance

Vulnerability management monitors CVEs in all components and applies patches within defined SLAs based on severity. Bug bounty or responsible disclosure programs allow external researchers to report vulnerabilities safely.

---

## Section C — SAST vs. DAST

| Attribute | SAST | DAST |
|---|---|---|
| What it tests | Source code or compiled binary | Running application |
| Testing approach | White-box | Black-box |
| When in SDLC | Early (development, CI) | Late (staging, pre-prod) |
| Can find | Logic flaws, hardcoded secrets, unsafe functions | Runtime bugs, auth bypasses, injection in live app |
| Cannot find | Runtime-only issues | Code-level logic errors |
| Example tools | SonarQube, Checkmarx, Semgrep | OWASP ZAP, Burp Suite, Nikto |

IAST (Interactive Application Security Testing) instruments the application at runtime, combining code-level visibility with runtime context.

---

## Section D — Code Signing

Code signing uses asymmetric cryptography to bind a software publisher's identity to a software artifact.

**Process:**

1. Developer obtains a code-signing certificate from a trusted CA (Comodo, DigiCert, etc.).
2. Before release, the developer hashes the compiled binary.
3. The developer encrypts the hash with their private key, producing a digital signature.
4. The signature and certificate are embedded in or distributed alongside the binary.
5. End users or operating systems verify the signature by decrypting with the publisher's public key and comparing hashes.

**What code signing guarantees:**

- **Authenticity**: The binary was signed by the holder of the private key.
- **Integrity**: The binary has not changed since signing.

**What code signing does not guarantee:**

- The software is free of malware or vulnerabilities.
- The private key has not been compromised.

The SolarWinds supply chain attack illustrates this limitation — attackers signed malicious code with the legitimate SolarWinds key because they compromised the build environment.

---

## Key Terms

- **OWASP**: Open Web Application Security Project
- **IDOR**: Insecure Direct Object Reference
- **SSRF**: Server-Side Request Forgery
- **XSS**: Cross-Site Scripting (reflected, stored, DOM-based)
- **SQL Injection**: Injection of SQL code through unsanitized input
- **Parameterized query**: A query that separates code from data, preventing injection
- **SAST**: Static Application Security Testing (white-box)
- **DAST**: Dynamic Application Security Testing (black-box)
- **IAST**: Interactive Application Security Testing
- **Threat modeling**: Structured analysis of threats during design phase
- **STRIDE**: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
- **SBOM**: Software Bill of Materials
- **CVE**: Common Vulnerabilities and Exposures
- **CVSS**: Common Vulnerability Scoring System
- **Code signing**: Digital signature applied to software to prove origin and integrity
- **DevSecOps**: Development, Security, and Operations integrated practice
- **Shift left**: Moving security testing earlier in the development lifecycle
- **SRI**: Subresource Integrity
- **IMDS**: Instance Metadata Service (cloud metadata endpoint)

---

## Review Questions

1. What is IDOR and what access control check does it bypass?
2. Explain the difference between reflected XSS and stored XSS.
3. Why does parameterized querying prevent SQL injection?
4. What does A08 (Software and Data Integrity Failures) have in common with supply chain attacks?
5. Compare SAST and DAST: what does each test, when is each applied, and what type of issues does each find?
6. In a DAST test, what does "black-box" mean?
7. What two properties does code signing guarantee, and what does it fail to guarantee?
8. Define "shift left" in the context of application security.
9. What is a threat model and which phase of the SDLC should it occur in?
10. Why is A09 (Logging and Monitoring Failures) in the OWASP Top 10 even though it is not an attack technique itself?

---

## 9. Supplemental Resources

**1. OWASP Top 10 2021**
<https://owasp.org/www-project-top-ten/>
The authoritative reference for web application security risk categories, updated in 2021 with data from thousands of real-world applications. Each category includes attack scenarios, prevention techniques, and example code. Required reading for all Module 10 lab and quiz content covering injection, broken access control, XSS, SSRF, and supply chain integrity.

**2. OWASP Web Security Testing Guide (WSTG) v4.2**
<https://owasp.org/www-project-web-security-testing-guide/>
A comprehensive manual for testing web application security covering all OWASP Top 10 categories with specific test cases, HTTP request examples, and tool recommendations. Directly supports the Module 10 lab's SQL injection, XSS, and IDOR testing exercises and provides the methodology used in professional penetration testing engagements.

**3. NIST SP 800-218 — Secure Software Development Framework (SSDF)**
<https://csrc.nist.gov/publications/detail/sp/800-218/final>
NIST's framework for integrating security into software development practices, covering secure design, code review, testing, and supply chain integrity. Directly supports Module 10 Secure SDLC content and the shift-left security concept, and maps to Executive Order 14028 requirements for software supply chain security.

---

## Certification Exam Tip

Security+ SY0-701 Domain 4 tests OWASP categories, secure development concepts, and testing methodologies. Pay close attention to the SAST versus DAST comparison — exam questions frequently ask which tool applies to which scenario and what "white-box" versus "black-box" means. Know code signing as a supply chain control and be able to explain its limitations.

---

*End of Reading Guide — Module 10*



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
