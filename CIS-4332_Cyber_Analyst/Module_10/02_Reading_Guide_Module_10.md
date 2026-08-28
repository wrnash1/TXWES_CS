# Reading Guide: Module 10 — Digital Forensics: Evidence Collection and Chain of Custody

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


## Course: CIS-4332 Cyber Analyst

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Introduction

Digital forensics is the discipline of collecting, preserving, analyzing, and presenting digital evidence in a manner that maintains its integrity and legal admissibility. Every SOC analyst encounters forensic evidence — whether they are acquiring RAM from a compromised workstation, reviewing a disk image for attacker artifacts, or ensuring that a legal hold is honored during an active investigation. This module covers the foundational forensic concepts tested on the CySA+ exam: the order of volatility, forensic imaging, write blockers, hash verification, chain of custody, legal holds, and the key Windows forensic artifact categories.

---

## Section 1 — Order of Volatility

### 1.1 Volatility Hierarchy

| Priority | Evidence Source | Volatility Level | What Is Lost on Shutdown |
|---|---|---|---|
| 1 (Most volatile) | RAM / Physical Memory | Extreme | Active processes, injected code, decrypted keys, cleartext credentials, active network connections |
| 2 | Network State | Very High | ARP cache, routing table, active TCP/UDP connection table |
| 3 | Running Process List | High | Process names, PIDs, command-line arguments, parent-child relationships |
| 4 | Temporary File System | Moderate | Open file handles, swap/pagefile content (partially) |
| 5 | Disk (Non-volatile Storage) | Low | Hard drive and SSD contents persist through power cycle |
| 6 | Remote Logs / External | Very Low | SIEM logs, cloud logs, network device logs — accessible after the endpoint is shut down |
| 7 (Least volatile) | Archived / Physical | Minimal | Removable media, printed records, optical discs |

### 1.2 RAM Acquisition Priority

RAM contains evidence that is investigatively irreplaceable:

- Active malware processes (including fileless malware that exists only in memory)
- Injected code from process injection attacks (may not appear on disk at all)
- Decrypted file encryption keys (may allow ransomware file decryption if captured in time)
- Cleartext credentials extracted from LSASS memory by credential dumping tools
- Established C2 network connections with current attacker IP addresses
- Interactive shell sessions with attacker command history

RAM acquisition tools: WinPmem (Windows, open-source), DumpIt (Windows), Volatility Framework (for analysis of memory images), LiME (Linux Memory Extractor — kernel module for Linux systems).

---

## Section 2 — Forensic Imaging

### 2.1 Forensic Image Types

| Type | Description | Use Case |
|---|---|---|
| Bit-stream image (raw/dd) | Sector-by-sector copy of entire media including unallocated space | Maximum compatibility; can be analyzed by any tool |
| E01 (EnCase Evidence File) | Bit-stream image with embedded metadata, verification hashes, and optional compression | Professional DFIR investigations; court-accepted format |
| AFF4 | Open standard with embedded metadata and strong hash verification | Modern format gaining adoption in DFIR community |
| Logical image | Copy of only allocated (accessible) files — not unallocated space | Triage when full bit-stream is not feasible; misses deleted data |

### 2.2 Write Blockers

| Type | Description | Reliability | Use Case |
|---|---|---|---|
| Hardware write blocker | Dedicated hardware device between suspect drive and workstation | Highest — hardware enforced | All court-admissible forensic acquisitions |
| Software write blocker | OS-level configuration to mount drive read-only | Lower — subject to software bugs | Lab or training environments; less preferred for litigation |

Without a write blocker, connecting a drive to any operating system causes writes:

- Windows: volume mounts, access timestamps update, recycle bin registry writes, prefetch cache updates
- Linux: journal recovery, mount record updates, device scan writes

A drive touched without a write blocker has been forensically contaminated. Hash verification will detect the change if the drive was previously hashed.

### 2.3 Forensic Acquisition Tools

| Tool | Platform | License | Key Features |
|---|---|---|---|
| FTK Imager | Windows | Free | E01 and raw imaging, hash verification, basic file preview |
| dd / dcfldd | Linux/Unix | Free (built-in) | Raw disk imaging; dcfldd adds hashing and logging |
| Autopsy | Windows/Linux | Open-source | Full forensic suite — imaging, artifact analysis, timeline |
| WinPmem | Windows | Open-source | RAM acquisition |
| Volatility Framework | Windows/Linux | Open-source | RAM image analysis — process listing, network connections, malware detection |

---

## Section 3 — Hash Verification

### 3.1 Forensic Hash Process

```text
HASH VERIFICATION WORKFLOW

Step 1: Before acquisition
  - If possible, hash source media before beginning acquisition
  - Document: algorithm (MD5 / SHA-256), source hash value, tool used, timestamp, analyst

Step 2: After acquisition
  - Hash the forensic image immediately after creation
  - Compare source hash to image hash
  - If hashes match: image is forensically sound — bit-for-bit identical
  - If hashes do not match: re-acquire; document the discrepancy

Step 3: On transfer
  - When image is handed to another analyst or moved to another system:
    Receiving party re-hashes the image
    Compare received hash to documented source hash
    Document both parties' names, timestamps, and hash comparison result

Step 4: Documentation
  - All hash values recorded on chain of custody form
  - Algorithm, tool, analyst, and timestamp for each hash event
```

### 3.2 Hash Algorithm Comparison

| Algorithm | Output Length | Collision Resistance | Recommended Use |
|---|---|---|---|
| MD5 | 128-bit | Known collisions | Widely supported; acceptable for internal investigations |
| SHA-1 | 160-bit | Deprecated | Avoid — theoretical collision attacks demonstrated |
| SHA-256 | 256-bit | Strong | Recommended for any litigation-anticipated investigation |

---

## Section 4 — Chain of Custody

### 4.1 Chain of Custody Form Components

| Component | What Is Documented |
|---|---|
| Evidence identification | Item number, description, source (device name, serial number, hostname, location) |
| Collection details | Date, time, location of collection; collecting analyst's name and signature |
| Acquisition hash | MD5 or SHA-256 hash of collected evidence at time of acquisition |
| Storage location | Where evidence is stored; storage access restrictions |
| Transfer record | Each transfer: transferring party, receiving party, date, time, reason, both signatures |
| Analysis record | Each analysis session: analyst name, start/end time, tools used, actions performed |
| Final disposition | Return to owner, retained per policy, or destroyed — with signature and date |

### 4.2 Chain of Custody Failures

| Failure | Consequence |
|---|---|
| Undocumented transfer | Gap in custody record — evidence may be challenged as tampered |
| Missing signature on transfer | Receiving party cannot attest to what they received; custody broken |
| Analysis on original (not image) | Source evidence modified; original cannot serve as reference |
| Hash mismatch not investigated | Evidence integrity cannot be confirmed; may be inadmissible |
| Unsecured storage | Access by unauthorized parties — custody broken |
| Missing timestamp | Cannot establish sequence of events; evidence handling questioned |

---

## Section 5 — Legal Holds

### 5.1 Legal Hold vs. Chain of Custody

| Concept | Definition | Who Issues | Purpose |
|---|---|---|---|
| Legal Hold (Litigation Hold) | Directive to preserve all potentially relevant data in anticipation of litigation or regulatory investigation | Legal counsel | Prevent spoliation; satisfy e-discovery obligations |
| Chain of Custody | Documented record of evidence handling from collection to disposition | IR team / Forensic examiner | Maintain evidence integrity for admissibility |

Legal hold and chain of custody are complementary. A legal hold tells you what to preserve. Chain of custody documents how you preserved and handled it.

### 5.2 Spoliation

Spoliation is the destruction, alteration, or failure to preserve evidence subject to a legal hold.

Consequences of spoliation:

- Court sanctions against the organization
- Adverse inference jury instructions (jury told to assume the destroyed evidence was harmful to the organization)
- Case dismissal in extreme cases
- Regulatory fines for compliance-related data destruction

What constitutes spoliation: wiping systems, overwriting logs, deleting backups, reformatting drives, running cleanup tools on systems subject to legal hold. Even automated data deletion (log rotation, backup rotation) must be suspended for data covered by the hold.

---

## Section 6 — Windows Forensic Artifacts

### 6.1 Key Windows Artifact Reference

| Artifact | Location | What It Reveals |
|---|---|---|
| Registry | HKCU, HKLM hives | Run key persistence, recently run programs, USB devices, user activity |
| Windows Event Log | C:\Windows\System32\winevt\Logs\ | Authentication, process creation (4688), service install (7045), account creation (4720) |
| Master File Table ($MFT) | Root of NTFS volume | File names, sizes, timestamps (including deleted files) |
| Prefetch Files | C:\Windows\Prefetch\ | Execution history — programs run including deleted executables |
| Browser History/Cache | User profile AppData | URLs visited, files downloaded, timestamps |
| LNK Files (Shortcuts) | User profile Recent | Recently accessed files — reveals attacker document activity |
| Jump Lists | User profile AppData\Roaming | Recently opened files per application |
| NTFS Timestamps | $MFT entries | Created, Modified, Accessed, Entry Modified — detectable timestamp tampering |
| Pagefile.sys / Swapfile.sys | C:\ | Partial volatile memory content that was paged to disk |

### 6.2 Key Windows Event IDs

| Event ID | Log | Description | Forensic Significance |
|---|---|---|---|
| 4624 | Security | Successful logon | Authentication trail — lateral movement detection |
| 4625 | Security | Failed logon | Brute force / credential stuffing detection |
| 4648 | Security | Logon with explicit credentials | Pass-the-hash, credential reuse detection |
| 4672 | Security | Special privileges assigned to new logon | Privileged access events |
| 4688 | Security | Process creation (requires audit policy) | Malicious process execution tracking |
| 4720 | Security | User account created | Attacker-created backdoor account |
| 4732 | Security | User added to privileged group | Privilege escalation |
| 7045 | System | Service installed | Malicious service installation for persistence |
| 4104 | PowerShell | PowerShell script block logging | Encoded/obfuscated PowerShell command content |

---

## CySA+ Exam Tips

Exam Tip 1: Order of volatility — always collect RAM first. Any scenario question presenting a running compromised system will test whether you know that RAM is collected before disk. Shutdown before RAM collection is always wrong.

Exam Tip 2: Write blockers prevent source drive modification during acquisition. Hardware write blockers are more reliable than software. Without a write blocker, connecting a drive modifies it.

Exam Tip 3: Hash verification proves image integrity, not evidence admissibility. Matching hashes confirm the image is bit-for-bit identical to the source. Admissibility also requires chain of custody documentation.

Exam Tip 4: Chain of custody is about documentation of who handled the evidence. Legal hold is about the requirement to preserve data. These are distinct concepts that the exam tests separately.

Exam Tip 5: Spoliation — destroying data subject to a legal hold — has serious legal consequences. If a legal hold is in effect, no system in scope can be wiped until legal counsel confirms the relevant evidence has been preserved.

Exam Tip 6: Analysis is always performed on the forensic copy — never on the original. The original is preserved in secure storage. Modifying the original destroys evidence integrity and breaks chain of custody.

Exam Tip 7: Windows Prefetch files record execution history including deleted executables. This is one of the most forensically valuable artifact types for proving that a malware binary was run even after the attacker deleted it.

Exam Tip 8: Event ID 4688 (process creation) requires audit policy to be enabled. Many organizations do not have this enabled by default. When a scenario asks why attacker process activity is not visible in Windows Event Logs, the answer is usually that process creation auditing was not configured.

---

## Glossary

- AFF4: Advanced Forensic Framework 4 — open forensic image format with embedded metadata and hash verification
- Chain of Custody: Documented record of every person who had custody of evidence, when, and what they did with it
- E01: EnCase Evidence File — compressed forensic image format with embedded metadata and hash verification
- FTK Imager: Free forensic acquisition tool for creating E01 and raw disk images with hash verification
- Legal Hold: Directive from legal counsel to preserve data relevant to anticipated or active litigation
- MFT: Master File Table — NTFS index of all files on a volume, including deleted files
- Order of Volatility: Principle that evidence must be collected from most volatile to least volatile to preserve maximum data
- Prefetch: Windows execution cache storing run history for recently executed programs
- Spoliation: Destruction or alteration of evidence subject to a legal hold — can result in court sanctions
- Volatile Evidence: Data that exists only in active system state and is permanently lost on shutdown
- Volatility Framework: Open-source tool for analyzing memory images to identify processes, connections, and malware
- Write Blocker: Hardware or software device that prevents write operations from reaching source media during forensic acquisition

---

## Study Checklist

- [ ] List the order of volatility from most to least volatile and explain what is lost at each level
- [ ] Explain why RAM must be acquired before shutting down a compromised system
- [ ] Describe the purpose of a write blocker and explain why hardware is preferred over software
- [ ] Describe the forensic hash verification process and what matching hashes confirm
- [ ] List the seven components of a complete chain of custody form
- [ ] Describe three chain of custody failures and their consequences
- [ ] Explain the difference between a legal hold and chain of custody
- [ ] Define spoliation and describe two examples of actions that constitute spoliation
- [ ] Name four Windows forensic artifact types and describe what each reveals
- [ ] Name four Windows Event IDs and their forensic significance
- [ ] Review all eight exam tips
- [ ] Complete the Module 10 Lab
- [ ] Complete the Module 10 Quiz
- [ ] Post initial response to the Module 10 Discussion by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

**1. NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response**
<https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf>
The authoritative NIST guide connecting digital forensics to the incident response lifecycle. It covers forensic readiness, the order of volatility, evidence collection procedures, and analysis methodologies directly corresponding to Sections 2 and 3 of this guide. Sections 3.1 through 3.4 are especially relevant to CySA+ exam scenarios.

**2. SANS — DFIR (Digital Forensics and Incident Response) Posters and Cheat Sheets**
<https://www.sans.org/posters/>
SANS provides free downloadable reference posters covering Windows forensic artifacts, Linux forensic techniques, memory forensics with Volatility, and chain of custody procedures. The Windows Forensic Analysis poster is particularly useful for building fluency with the artifact types (Prefetch, Registry hives, Event Logs, LNK files, NTFS $MFT) covered in Section 4 of this guide.

**3. Volatility Foundation — Memory Forensics Framework Documentation**
<https://volatilityfoundation.org/>
The official documentation and plugin reference for the Volatility memory analysis framework. Even without a lab environment, reviewing the plugin list and reading example analysis walkthroughs builds understanding of what memory forensics can reveal — running processes, network connections, injected code, and encryption keys in RAM — reinforcing the volatile evidence concepts in Section 1 of this module.
