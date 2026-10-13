# Reading Guide: Module 02 — Linux Installation and System Navigation

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
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
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA / LearnLinuxTV &bull; CIS-3325 Module 02</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ (XK0-005) & LPI Linux Essentials Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ (XK0-005) & LPI Linux Essentials Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Module 2 covers two foundational skill areas: the Linux installation process and the core filesystem navigation commands. Understanding how Linux is installed — and the partitioning and filesystem decisions made during installation — is tested directly on the Linux+ exam. The navigation commands introduced in this module are the ones you will use in every lab and every real-world Linux administration task.

---

### 1. High-Yield Glossary

- **ISO image**: A disk image file containing the complete contents of a CD/DVD or installation media. Used to install operating systems. Verify checksums (SHA-256) before use.
- **BIOS (Basic Input/Output System)**: Legacy firmware that initializes hardware before the OS boots. Uses MBR partitioning. Supports disks up to 2 TB with up to 4 primary partitions.
- **UEFI (Unified Extensible Firmware Interface)**: Modern replacement for BIOS. Uses GPT partitioning. Supports disks larger than 2 TB and up to 128 partitions. Required for Secure Boot.
- **MBR (Master Boot Record)**: Legacy disk partitioning standard. Maximum disk size 2 TB. Maximum 4 primary partitions (or 3 primary + 1 extended containing logical partitions).
- **GPT (GUID Partition Table)**: Modern partitioning standard for UEFI. Supports disks up to 9.4 ZB and up to 128 partitions per disk.
- **ext4**: The Fourth Extended Filesystem. Default filesystem on Ubuntu and Debian. Supports journaling, files up to 16 TB, volumes up to 1 EB. Can be grown and shrunk.
- **XFS**: High-performance journaling filesystem. Default on RHEL-family distributions. Can be grown but NOT shrunk. Use `xfs_growfs` to expand.
- **btrfs**: Modern copy-on-write filesystem with built-in snapshots, RAID, and compression. Default on SUSE and Fedora. More complex to administer.
- **swap**: Disk space used as virtual memory when RAM is full. A swap partition is created during installation.
- **`fdisk`**: Interactive command-line partitioning tool for MBR disks. Run with `sudo fdisk /dev/sdX`.
- **`parted`**: Partitioning tool supporting both MBR and GPT. Can be used non-interactively in scripts.
- **`mkfs.ext4`**: Formats a partition with the ext4 filesystem. Full syntax: `sudo mkfs.ext4 /dev/sdb1`.
- **`mkfs.xfs`**: Formats a partition with the XFS filesystem.
- **`pwd`**: Print Working Directory. Shows your current location in the filesystem.
- **`ls`**: List directory contents. Key flags: `-l` (long format), `-a` (all/hidden files), `-h` (human-readable sizes), `-R` (recursive).
- **`cd`**: Change Directory. `cd ~` or `cd` alone returns to home. `cd ..` moves up one level.
- **Absolute path**: A path that starts from root (`/`). Example: `/home/student/documents`. Always starts with `/`.
- **Relative path**: A path relative to the current directory. Example: `documents` or `./documents` when already in `/home/student`.
- **`mkdir`**: Make Directory. `mkdir -p` creates parent directories as needed.
- **`rmdir`**: Remove empty directory. Fails if directory contains files.
- **`touch`**: Creates an empty file or updates a file's timestamps.
- **`cp`**: Copy files. `cp -r` for directories. `cp -p` preserves permissions and timestamps. `cp -i` prompts before overwriting.
- **`mv`**: Move or rename files and directories. No `-r` flag needed for directories.
- **`rm`**: Remove files permanently. `rm -r` for directories. `rm -i` prompts before deleting. `rm -rf` silently and permanently removes directory trees — use with extreme caution.
- **`file`**: Determines file type by reading file content, not extension. Returns type description like "ASCII text" or "ELF 64-bit executable."
- **`which`**: Searches PATH for the executable that runs when a command name is typed.
- **`whereis`**: Locates the binary, source, and man page for a command.
- **`man`**: Opens the manual page for a command. Navigate with arrow keys, search with `/`, quit with `q`.
- **Man page sections**: Section 1 = user commands. Section 5 = file formats. Section 8 = system administration. Specify with: `man 5 passwd`.

---

### 2. Partition Layout Reference

| Mount Point | Purpose | Typical Size |
|---|---|---|
| `/` (root) | Core OS | 10–20 GB minimum |
| `/boot` | Kernel and boot files | 500 MB – 1 GB |
| `/home` | User home directories | Remaining space |
| `/var` | Logs, databases, caches | 10+ GB for servers |
| `/tmp` | Temporary files | 2–5 GB |
| swap | Virtual memory | Equal to RAM (up to 8 GB RAM) |

---

### 3. ls Long Format Output

When you run `ls -l`, each line has this format:

```
-rw-r--r-- 1 student student 4096 Jun  1 09:23 myfile.txt
```

Reading left to right:

- `-rw-r--r--` — file type and permissions (covered in Module 4)
- `1` — hard link count
- `student` — owner
- `student` — group
- `4096` — size in bytes (use `-h` for human-readable)
- `Jun  1 09:23` — last modification date and time
- `myfile.txt` — filename

The first character of the permissions string identifies the file type: `-` = regular file, `d` = directory, `l` = symbolic link, `b` = block device, `c` = character device.

---

### 4. Path Quick Reference

| Path Expression | Meaning |
|---|---|
| `/` | Root of the filesystem |
| `~` | Current user's home directory |
| `.` | Current directory |
| `..` | Parent directory |
| `/etc/passwd` | Absolute path (starts with `/`) |
| `../config` | Relative path (up one level, then into config) |

---

### Required Readings and Videos

- **Required Reading**: [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) — Chapters 2, 3, and 4. Chapter 2: navigation; Chapter 3: exploring the system; Chapter 4: manipulating files and directories.
- **Required Video**: [LearnLinuxTV — Linux Fundamentals](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), Episodes 4–6. These cover filesystem navigation and file manipulation.

---

#
---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 02 — Linux Installation and System Navigation** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 02 — Linux Installation and System Navigation**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 02 — Linux Installation and System Navigation**:

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
> **Question:** In the context of **Module 02 — Linux Installation and System Navigation**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**

## Study Checklist

- [ ] Explain the difference between BIOS/MBR and UEFI/GPT.
- [ ] List the standard partition mount points and the purpose of each.
- [ ] Describe when to use XFS vs. ext4 and what the key difference is between them.
- [ ] Run `ls -lah` and identify all fields in the output.
- [ ] Demonstrate the difference between an absolute path and a relative path.
- [ ] Use `man ls` to look up a flag not covered in the reading guide.
- [ ] Complete the Module 2 lab.
- [ ] Complete the Module 2 quiz.

---

## 9. Supplemental Resources

**1. [Linux Filesystem Hierarchy Standard — The Linux Documentation Project](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/)**
A complete reference to the Linux Filesystem Hierarchy Standard (FHS), explaining the purpose of every top-level directory. Essential background for understanding where configuration files, binaries, logs, and variable data are stored by convention.

**2. [Red Hat — How to Manage Partitions with fdisk](https://www.redhat.com/sysadmin/fdisk-partitioning)**
A practical Red Hat sysadmin article covering `fdisk` for MBR partitioning and `gdisk` for GPT. Includes step-by-step partition creation and the MBR-vs-GPT decision framework used in real enterprise deployments.

**3. [man7.org — ls(1) Manual Page](https://man7.org/linux/man-pages/man1/ls.1.html)**
The online version of the `ls` man page from the Linux man-pages project. Useful for reviewing all available flags and their descriptions when not at a terminal, and for understanding the full output format of `ls -l`.
