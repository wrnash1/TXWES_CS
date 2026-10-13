# Video Script: Module 12 — Digital Forensics for Security Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Slide 1 — Introduction

Welcome to Module 12: Digital Forensics for Security Analysts. I am Professor Nash.

In Module 11 we covered incident response — the structured process for detecting, containing, and recovering from security incidents. In this module we go deeper into one of the most technically demanding skills an analyst can develop: digital forensics.

Digital forensics is the practice of collecting, preserving, analyzing, and presenting digital evidence. For security analysts, forensics is not about courtroom testimony — it is about answering a precise question: what exactly happened? When you need to understand how an attacker got in, what they did, and what data they touched, forensics gives you the answers.

---

## Slide 2 — Why Forensics Matters for Analysts

Forensics skills serve analysts in several ways beyond dedicated forensic investigations.

First, forensics improves your triage. When you understand what artifacts malware leaves behind in memory and on disk, you know exactly what to look for during incident investigation.

Second, forensics enables you to reconstruct attacker timelines with precision. A timeline showing exactly when each malicious action occurred is one of the most valuable outputs an analyst can produce for an IR team.

Third, the CySA+ CS0-003 exam includes digital forensics in Domain 4. You will be tested on memory forensics concepts, disk artifact analysis, network forensics, and chain of custody principles.

---

## Slide 3 — Forensic Principles

Before diving into tools and techniques, let us establish the foundational principles that govern all digital forensic work.

The first principle is preservation. Forensic analysis must never alter the evidence being examined. You always work from a forensic copy, never from the original.

The second principle is chain of custody. Every piece of evidence must have a documented, unbroken record of who collected it, who handled it, and where it has been. Gaps in chain of custody can invalidate evidence in legal proceedings.

The third principle is documentation. Every action taken during an investigation must be recorded with sufficient detail that another analyst could independently replicate the work.

The fourth principle is order of volatility. Evidence should be collected from most volatile to least volatile. Running processes disappear when a system is powered off. Hard drive contents persist after power-off.

---

## Slide 4 — Order of Volatility

The order of volatility, from most to least volatile, is:

- CPU registers and cache
- RAM (running processes, network connections, encryption keys)
- Swap space and virtual memory
- Network traffic (in-flight packets)
- Running processes and open files
- Disk contents
- Remote logging and monitoring data
- Physical configuration and network topology

This order tells you what to capture first. If you need to understand an attacker's command-and-control channel, you must capture RAM before you shut the system down — because that connection disappears the moment power is cut.

---

## Slide 5 — Memory Forensics with Volatility

Volatility is the industry-standard open-source framework for memory forensics. It analyzes RAM dumps — binary images of a system's memory captured at a point in time.

What can you find in a RAM dump? Running processes and their parent-child relationships. Network connections active at capture time. Loaded DLLs and injected code. Decrypted strings from malware that encrypts its on-disk payload. Command history. Cached credentials.

Volatility works by applying plugins against a memory image. Common plugins include:

- `pslist` — lists running processes
- `pstree` — shows process parent-child relationships
- `netscan` — shows active and recently closed network connections
- `malfind` — identifies memory regions suggesting code injection
- `dlllist` — lists DLLs loaded by each process
- `cmdline` — shows command-line arguments for each process

---

## Slide 6 — Memory Forensics Workflow

The memory forensics workflow follows these steps.

Step one: acquire the memory image. Tools like WinPmem, DumpIt, and LiME (for Linux) capture RAM to a file without modifying the running system.

Step two: identify the OS profile. Volatility needs to know the OS and version to correctly parse memory structures. The `imageinfo` or `kdbgscan` plugin identifies this.

Step three: run baseline plugins. Start with `pslist`, `pstree`, and `netscan` to get an overview of what was running and what connections existed.

Step four: investigate anomalies. Processes with no parent, processes injecting into system processes, unexpected network connections — follow these leads with targeted plugins.

Step five: document findings. Every finding gets recorded with the plugin used, the exact command run, and the output observed.

---

## Slide 7 — Disk Forensics with Autopsy

Autopsy is a graphical digital forensics platform built on The Sleuth Kit. It allows analysts to examine disk images — bit-for-bit copies of storage media — without modifying the original.

Autopsy provides:

- File system browsing and deleted file recovery
- Keyword search across entire disk images
- Hash-based file identification against known malware and known-good databases
- Artifact extraction including browser history, email, and recently accessed files
- Timeline analysis combining file system timestamps
- Registry analysis for Windows systems

When you receive a disk image from an affected system, Autopsy lets you answer: what files were created or modified, what programs were run, what websites were visited, and what was deleted.

---

## Slide 8 — Key Disk Artifacts

Knowing where evidence lives on disk is as important as knowing how to use the tools. Key Windows artifacts include:

The Windows Registry stores system and application configuration, user activity, and malware persistence. The `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` key is a classic malware persistence location.

Prefetch files cache execution data for programs run on the system. They prove a program was executed even after the executable has been deleted.

Windows Event Logs record authentication, service starts, and application events. Event ID 4624 is successful logon. Event ID 4688 is process creation.

Shellbags are registry entries that record which folders a user browsed, even after the folder is deleted.

The MFT (Master File Table) is the NTFS index of every file and directory, including metadata for deleted files.

---

## Slide 9 — Network Forensics with Wireshark

Wireshark is the industry-standard packet analysis tool. Network forensics involves capturing and analyzing network traffic to understand what data was transmitted during an incident.

Wireshark allows analysts to:

- Capture live traffic or load saved PCAP files
- Filter traffic by protocol, IP address, port, and payload content
- Reconstruct TCP streams to see the full content of a conversation
- Identify protocol anomalies indicating malicious activity
- Extract transferred files from packet captures
- Follow HTTP, DNS, FTP, and other application-layer conversations

For incident investigations, network forensics answers: what commands did the attacker send over the C2 channel, what data was exfiltrated, and what external hosts communicated with the compromised system?

---

## Slide 10 — Network Forensic Indicators

Key network indicators analysts look for include:

DNS queries to unusual or newly registered domains — often indicators of DGA malware or C2 infrastructure.

HTTP/HTTPS connections with unusual user-agent strings — attackers often use default or modified agents that differ from legitimate browser traffic.

Large outbound data transfers at unusual times — potential exfiltration indicators.

Beaconing patterns — regular, timed connections to external hosts indicating C2 check-in behavior.

Connections to known-malicious IPs or Tor exit nodes — direct indicators of attacker infrastructure.

Use of non-standard ports — for example, HTTP traffic on port 8080 or 4444, common in remote access tools.

---

## Slide 11 — Artifact Analysis

Artifact analysis is the process of extracting meaningful evidence from individual artifacts found during memory, disk, or network forensics.

A forensic artifact is any piece of data created as a byproduct of system or user activity. Artifacts can prove that an action occurred even when an attacker attempts to cover their tracks.

For example: an attacker deletes a malicious executable from disk. But the Windows prefetch file still exists, proving it was run. The MFT entry still shows the file existed with its creation timestamp. The Amcache entry records the executable's hash. The event log shows process creation. Four independent artifacts confirm execution even though the file itself is gone.

This is why artifact analysis provides more reliable evidence than searching for the malware file itself.

---

## Slide 12 — Timeline Reconstruction

Timeline reconstruction is the process of combining timestamps from multiple evidence sources into a single chronological record of all activity during an incident.

Sources for timeline data include:

- File system MACB timestamps (Modified, Accessed, Changed, Born)
- Windows event log timestamps
- Registry key last-modified timestamps
- Prefetch file execution timestamps
- Browser history timestamps
- Network log timestamps
- Authentication log timestamps

Tools like Autopsy and Plaso automate much of this work by pulling timestamps from multiple sources and merging them into a super-timeline.

A complete incident timeline is the most powerful deliverable an analyst can produce. It shows exactly when the attacker entered, what they did, and in what sequence.

---

## Slide 13 — Chain of Custody

Chain of custody is the documented record proving that evidence has not been tampered with from collection through analysis, storage, and eventual presentation.

For evidence to be admissible in legal proceedings, chain of custody must be unbroken. This means:

- Document who collected the evidence, when, and from where
- Hash the evidence immediately after collection using MD5 and SHA-256
- Store evidence in a secure, access-controlled location
- Log every access to the evidence, including who accessed it and why
- Hash again before and after any analysis to verify no alteration
- Transfer evidence only through documented handoffs

Even in internal investigations, chain of custody discipline ensures integrity and protects you professionally.

---

## Slide 14 — Anti-Forensic Techniques

Attackers know forensics is coming. Common anti-forensic techniques include:

Timestomping — modifying file timestamps to hide when files were created or modified.

Secure deletion — overwriting file contents before deletion to prevent recovery.

Log clearing — deleting or modifying Windows event logs.

Steganography — hiding data inside innocuous files.

Encryption — encrypting stolen data or communication channels.

Living-off-the-land — using built-in OS tools like PowerShell and WMI to avoid creating obvious malware artifacts.

Understanding anti-forensic techniques helps you recognize when they have been used and sometimes recover evidence despite them.

---

## Slide 15 — CySA+ Exam Connection

For the CySA+ CS0-003 exam, focus on:

- The order of volatility and why it governs evidence collection sequencing
- Volatility plugins and what each reveals about a memory image
- Key Windows disk artifacts and what each proves
- Wireshark as a network forensics tool — filter syntax and stream reconstruction
- Chain of custody requirements and why they matter
- Anti-forensic techniques and how to detect them

Exam questions will present forensic scenarios and ask which tool, technique, or artifact is most appropriate to answer a specific investigative question.

---

## Slide 16 — Summary

Module 12 covered the foundational skills of digital forensics for security analysts.

We examined memory forensics with Volatility, disk forensics with Autopsy, and network forensics with Wireshark. We explored key Windows artifacts and how they survive attacker cleanup attempts. We covered timeline reconstruction as the synthesis of all forensic evidence into an authoritative incident record, and chain of custody as the professional standard for evidence integrity.

---

## Slide 17 — Looking Ahead

In Module 13 we shift to Compliance and Security Controls Validation. You will learn how analysts work with the NIST Cybersecurity Framework and CIS Controls to test and validate security controls, collect audit evidence, and perform gap analysis.

Complete all Module 12 activities before our next session.

---

End of Module 12 Video Script — 225 lines
