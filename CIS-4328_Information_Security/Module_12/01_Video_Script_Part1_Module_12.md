# Video Script: Module 12 — Digital Forensics (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — Introduction to Digital Forensics (2 minutes)

Welcome to Module 12, Digital Forensics. If incident response is the operational response to a security event, digital forensics is the scientific process that tells you what actually happened. Forensics answers the questions that matter for legal proceedings, insurance claims, and organizational accountability: What was accessed? What was taken? How did the attacker get in? How long were they there? Who did it?

For Security+, digital forensics content falls within Domain 4 (Operations and Incident Response), specifically exam objectives related to digital forensics tools, concepts, and proper evidence handling. You will also encounter forensics in legal and compliance contexts.

The term "digital forensics" comes from the legal concept of forensic science — science applied to legal questions. That legal grounding is important: everything you do in a forensic investigation must be defensible in court. Sloppy technique does not just produce bad analysis — it can get evidence thrown out and allow criminals to escape accountability.

---

## Segment 2 — The Forensic Process (5 minutes)

The forensic process parallels the incident response lifecycle but is more rigorously defined from a scientific and legal standpoint. The standard forensic process has five phases:

### Phase 1: Identification

Identification means recognizing that a crime or security incident has occurred and that digital evidence may exist. This includes:

- Identifying potential evidence sources (computers, servers, mobile devices, cloud accounts, network devices, IoT devices)
- Determining the scope of the investigation
- Identifying legal authority to collect evidence (internal investigation vs. law enforcement involvement)
- Documenting the initial scene state

Before touching anything, document everything you see. Photograph the workspace, screen contents, physical connections, and the position of devices. Your actions from the moment you arrive at the scene are part of the evidence record.

### Phase 2: Preservation

Preservation means protecting evidence from modification, destruction, or contamination. This is the phase where write blockers become critical.

**Write blockers** are hardware or software devices that prevent any writes to storage media during examination. When you connect a suspect hard drive to your forensics workstation, the operating system will attempt to mount the drive, update access timestamps, and potentially write data. A write blocker sits between the drive and the forensics workstation, allowing reads but blocking all write operations.

Hardware write blockers are preferred for serious investigations because they operate at the hardware level and are not dependent on software configurations. Common hardware write blockers include devices from Tableau (owned by Guidance Software / OpenText) and WiebeTech.

Software write blockers are also used — the Linux `dd` command with appropriate flags, or the Windows write-protect registry key. However, software write blockers are more susceptible to operator error or software bugs.

**Hash verification** establishes the integrity of evidence at the moment of collection. Before and after imaging a drive, calculate MD5 and SHA-256 hashes of the original media. If the hashes match the hashes of your forensic image, you have mathematically proven that the image is an exact copy. If any bit has changed — whether by accident or tampering — the hash will differ.

### Phase 3: Collection

Collection means acquiring evidence in a forensically sound manner. The primary collection technique is disk imaging.

**Disk imaging** creates a bit-for-bit copy of the entire storage media, including all partitions, unallocated space, slack space, and deleted file remnants. This is fundamentally different from a file copy: a file copy only captures allocated files. A forensic image captures everything on the physical media.

**dd** — the classic Unix/Linux disk imaging command — is widely used in forensics:

```bash
dd if=/dev/sdb of=/forensics/case001/sdb.img bs=512 conv=noerror,sync
```

Here, `if` (input file) is the suspect drive, `of` (output file) is the destination image file, `bs` is the block size, and `conv=noerror,sync` tells dd to continue past read errors rather than stopping.

After imaging, hash the image and compare to the hash of the original. Document both hashes in the chain of custody.

**FTK Imager** — AccessData's FTK Imager is a free Windows-based tool widely used in both academic and commercial forensics. It provides a GUI interface for creating forensic images, calculating hashes, and preserving evidence. It supports multiple image formats:

- **E01 (Expert Witness Format)** — the most common forensic image format; supports compression and splitting into multiple files; includes metadata about the acquisition
- **RAW (dd format)** — a flat binary copy; universally supported but larger; no built-in metadata
- **AFF (Advanced Forensics Format)** — an open-source format with built-in compression and metadata

For mobile device collection, specialized tools are used: Cellebrite UFED, Oxygen Forensics Detective, and Magnet AXIOM are industry standards. Mobile forensics involves additional complexities: passcode locks, encrypted storage, cloud backups, and proprietary file systems.

### Phase 4: Analysis

Analysis means examining the collected evidence to answer investigation questions. Analysis is always performed on forensic images or copies — never on the original evidence. This is non-negotiable.

We will cover analysis in depth in Part 2, including file system analysis, memory forensics, and log analysis.

### Phase 5: Reporting

Reporting means documenting the findings in a clear, accurate, and legally defensible format. The forensic report must:

- Document the investigation scope and methodology
- Describe every tool used and its version
- Present findings in plain language accessible to non-technical readers (judges, juries, executives)
- Include supporting evidence (screenshots, hash values, extracted artifacts)
- Be reproducible — another examiner with the same evidence and tools should reach the same conclusions
- Be accurate — do not overstate certainty; use language like "consistent with" rather than absolute conclusions where uncertainty exists

---

## Segment 3 — Write Blockers and Disk Imaging Deep Dive (4 minutes)

Let us go deeper on write blockers and imaging because these are fundamental to forensic technique.

### Why Write Blockers Are Non-Negotiable

When Windows mounts a volume, it updates the Last Accessed timestamps on files. When macOS mounts a drive, it creates hidden `.DS_Store` files and spotlight index entries. When any OS mounts a drive with a dirty filesystem flag, it attempts repairs. Every one of these actions modifies the original evidence.

The defense in any criminal or civil case will challenge the integrity of digital evidence. A write blocker is your technical proof that you did not modify the evidence. Without one, opposing counsel can argue that your investigation itself caused the modifications you are attributing to the suspect.

The forensic workflow for media examination:

1. Document the evidence as received (photograph, record serial number, note physical condition)
2. Connect the suspect media through a hardware write blocker
3. Calculate the MD5 and SHA-256 hash of the original media BEFORE imaging
4. Create the forensic image
5. Calculate the hash of the forensic image
6. Compare hash of original to hash of image — they must match
7. Store the original media in sealed, tamper-evident packaging
8. Perform all analysis on the forensic image copy

### dd vs. FTK Imager — Practical Comparison

**dd strengths:**

- Available on any Linux/Unix system
- Free and open source
- Highly scriptable
- Produces a raw image that any tool can read

**dd weaknesses:**

- No GUI — operator errors are easy (accidentally reversing `if` and `of` destroys evidence)
- No progress indication (dcfldd is an enhanced version that adds progress and hashing)
- Large image files (no built-in compression)

**FTK Imager strengths:**

- GUI interface reduces operator error risk
- Calculates hashes automatically during imaging
- Supports multiple output formats including compressed E01
- Can image to multiple destinations simultaneously
- Includes a basic file browser for triage
- Free to download

**FTK Imager weaknesses:**

- Windows only (though Linux-based options exist)
- Not open source
- E01 format is tied to commercial vendors' toolsets (though widely supported)

### Live vs. Dead Acquisition

**Dead acquisition** — imaging a powered-off system's storage media. The traditional forensic approach. Volatile data is lost, but the disk state is stable and will not change.

**Live acquisition** — collecting evidence from a running system. Captures volatile data (RAM, network connections, running processes) but risks modifying the system state during collection. Required when volatile evidence is critical or when the system cannot be powered off without significant business disruption.

The modern forensic approach often uses both: capture RAM and volatile state first (live), then image the disk (can be done with the system still running or after a controlled shutdown).

---

## Segment 4 — Memory Forensics Introduction (4 minutes)

Memory forensics — the analysis of RAM dumps — has become one of the most important areas of digital forensics because modern malware often operates primarily or entirely in memory, leaving minimal disk artifacts.

### Why Memory Is Forensically Valuable

System memory contains:

- **Running processes** — every executing process and its memory space
- **Network connections** — all open and recently closed network connections
- **Encryption keys** — keys actively in use are stored in memory in plaintext (BitLocker keys, VeraCrypt keys, SSL session keys)
- **Credentials** — passwords, tokens, and hashes in use by processes
- **Malware artifacts** — injected code, rootkits, and fileless malware that never wrote to disk
- **Clipboard contents** — whatever was last copied
- **Browser history and sessions** — recently viewed URLs, active session tokens
- **Command history** — recently executed commands

**Fileless malware** is a particular concern. Fileless attacks use legitimate system tools (PowerShell, WMI, mshta.exe) to execute malicious code that never writes to disk. Traditional disk forensics would find no malware artifacts. Memory forensics reveals the malicious code running in process memory.

### Memory Acquisition Tools

**WinPmem** — open source Windows memory acquisition tool. Creates a raw memory dump.

**Magnet RAM Capture** — free Windows tool from Magnet Forensics. Creates raw memory images.

**Volatility Foundation RAM Capture** — for Linux-based acquisition.

**LiME (Linux Memory Extractor)** — a Linux loadable kernel module for acquiring memory from Linux systems.

**FTK Imager** — can capture memory as well as disk images.

### Volatility Framework — The Standard Memory Analysis Tool

Volatility is the industry-standard open-source framework for memory analysis. It runs on Linux, macOS, and Windows and supports memory images from Windows, Linux, and macOS.

Key Volatility commands (Volatility 3 syntax):

- `windows.pslist` — list running processes
- `windows.cmdline` — show command line arguments for each process
- `windows.netscan` — list network connections (including recently closed)
- `windows.dlllist` — list DLLs loaded by each process
- `windows.malfind` — scan for memory regions with suspicious characteristics (executable, writable, not backed by a file on disk — a classic indicator of injected code)
- `windows.dumpfiles` — extract files from memory
- `windows.hashdump` — extract NTLM password hashes

The output of `windows.malfind` is particularly powerful: it identifies memory regions that have the characteristics of injected shellcode or process hollowing, which are techniques used by advanced malware to hide in legitimate process memory.

---

## Module 12 Part 1 Summary

The foundational forensic process and its most critical techniques:

- Five phases: Identification, Preservation, Collection, Analysis, Reporting
- Write blockers — hardware devices that prevent any writes to suspect media during examination; non-negotiable for legally defensible forensics
- Disk imaging with dd and FTK Imager creates bit-for-bit copies; MD5/SHA-256 hashes verify integrity
- Dead acquisition is more stable; live acquisition captures volatile data; modern practice often uses both
- Memory forensics with Volatility reveals fileless malware, encryption keys, credentials, and network connections that disk forensics cannot see

In Part 2 we cover log analysis, file system forensics concepts, and legal considerations. See you there.

---

*End of Part 1 Script*
