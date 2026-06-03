# Reading Guide: Module 11 — Incident Response

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports Module 11: Incident Response. You will study the NIST SP 800-61 incident response lifecycle, IR team structure, communication and notification obligations, evidence preservation, chain of custody, and the lessons learned process. These topics map to Security+ Domain 4 and are essential for any security operations role.

**Estimated reading and study time:** 2.5 to 3 hours

---

## Learning Objectives

By the end of this module you should be able to:

- Describe the four phases of the NIST SP 800-61 incident response lifecycle.
- Distinguish between events, alerts, and incidents.
- Explain the order of volatility and its impact on evidence collection.
- Describe chain of custody and why it matters for legal proceedings.
- Identify IR team roles and their responsibilities.
- Explain the purpose and structure of a lessons learned review.
- Describe communication and notification obligations in incident response.

---

## Required Reading

- **NIST SP 800-61 Revision 2** — Computer Security Incident Handling Guide (free at csrc.nist.gov). Focus on Sections 2, 3, and 4.
- **Professor Messer Security+ SY0-701 Study Guide** — Domain 4 sections on incident response
- **SANS Incident Handler's Handbook** — Available free at sans.org (search "Incident Handler's Handbook")

---

## Section A — The IR Lifecycle (NIST SP 800-61)

NIST SP 800-61 defines incident response as a four-phase cyclical process. The cycle nature is intentional — lessons from each incident improve preparation for the next.

### Phase 1 — Preparation

Preparation is the foundation that determines whether a team can respond effectively. Key preparation activities include:

- Forming and training the IR team.
- Developing the IR plan and procedure documents (playbooks).
- Establishing communication trees and escalation paths.
- Deploying detection and monitoring tools (SIEM, EDR, IDS/IPS).
- Building a jump kit — a portable collection of forensic tools, clean media, response checklists, and contact information.
- Conducting tabletop exercises and simulation drills.
- Establishing relationships with external parties: law enforcement, legal counsel, breach notification services, and forensic vendors.

The Security+ exam tests what belongs in an IR plan and what tools should be available before an incident.

### Phase 2 — Detection and Analysis

Detection begins when a monitoring tool, user report, or external notification surfaces a potentially malicious event. Not every alert is an incident. The analysis step determines:

- Is this a true positive (real incident) or false positive?
- What is the scope — which systems and data are affected?
- What is the severity — what is the business impact?
- What is the attack vector?

**Indicators of Compromise (IOCs)** are technical artifacts that suggest compromise. Common IOCs include:

- Unusual outbound network connections, especially to known malicious IPs or domains.
- Processes running from unusual directories (e.g., `%TEMP%`, `%AppData%`).
- New scheduled tasks, registry run keys, or services created by non-admin accounts.
- File hashes matching known malware.
- Spikes in failed authentication attempts.
- Unusual data transfers at unusual hours.

**Indicators of Attack (IOAs)** are behavioral patterns that suggest an active attack, even before compromise is confirmed. IOAs focus on attacker behavior rather than specific artifacts.

**Precursors** are early warning signs that an attack may be imminent. Port scans, vulnerability scans, and spearphishing campaigns targeting your sector are examples.

### Phase 3 — Containment, Eradication, and Recovery

NIST groups containment, eradication, and recovery into a single phase with three distinct steps.

**Containment** limits the damage. Short-term containment applies immediate measures (network isolation, account lockout). Long-term containment provides stable interim measures while eradication is prepared.

The containment decision must balance operational continuity against evidence preservation and attacker observation value. Pulling the plug destroys volatile evidence. Keeping a system running may allow the attacker to continue.

**Eradication** removes the attacker's presence. This includes:

- Removing malware and attacker tools.
- Closing the exploited vulnerability.
- Eliminating backdoors and persistence mechanisms.
- Resetting all compromised credentials.
- Patching affected systems.

Eradication must be verified before recovery begins. Incomplete eradication leads to re-compromise.

**Recovery** restores systems to normal operation:

- Restoring from clean, verified backups (from before the compromise date).
- Rebuilding compromised systems from known-good images.
- Re-enabling services and accounts with new credentials.
- Monitoring restored systems closely for signs of re-compromise.

### Phase 4 — Post-Incident Activity

This phase encompasses the lessons learned review and production of the post-incident report. It is the most frequently skipped phase and the most valuable for organizational improvement.

---

## Section B — Evidence Preservation and Chain of Custody

### Order of Volatility

Digital evidence exists on a spectrum from highly volatile (disappears almost instantly) to non-volatile (persists indefinitely). The order of volatility determines collection priority.

From most volatile to least volatile:

1. CPU registers, cache
2. System RAM — running processes, network connections, decryption keys, injected code
3. Swap space / virtual memory
4. Network state — ARP table, routing table, active connections
5. Running processes
6. Disk contents — files, event logs, registry
7. Remote logging systems
8. Archived media, backups

Always collect higher-volatility evidence first. If a system must be shut down for operational reasons, capture RAM before shutting down.

### Forensic Disk Imaging

A forensic image is a bit-for-bit copy of an entire storage device, including deleted files, unallocated space, and file system metadata. The imaging process must:

1. Write-protect the original device before any imaging begins.
2. Hash the original device (MD5 and SHA-256) before copying.
3. Copy the device to forensic media using a validated tool.
4. Hash the resulting image and verify it matches the original hash.
5. Store the original device securely and work only from the image.

Common forensic imaging tools include `dd` (Linux/macOS command-line), FTK Imager (Windows GUI), and Guymager (open-source GUI). Each creates an identical copy with verified hash integrity.

### Write Blockers

A write blocker is a hardware device or software mode that permits reading from a storage device while blocking all writes. Write blockers prevent the imaging process from modifying access timestamps, metadata, or file contents on the original evidence.

Hardware write blockers are preferred in legal proceedings because they operate at the hardware level, independent of the operating system.

### Chain of Custody

Chain of custody is the documented, unbroken record of who handled evidence, when, and under what circumstances. It answers the question: "How do we know this evidence has not been modified since collection?"

Chain of custody documentation includes:

- A unique identifier (evidence tag number) for each item.
- Date and time of collection.
- Person who collected the evidence and their role.
- Description of the item (make, model, serial number, hash).
- Signature of the collecting investigator.
- Every transfer: from/to whom, date/time, purpose.
- Storage location and conditions.
- Access log during storage.

Digital chain of custody relies on cryptographic hashing. If the SHA-256 hash of the forensic image matches the hash of the original at every analysis stage, the chain of digital integrity is maintained.

---

## Section C — Communication and Notification

### Internal Communication

Internal IR communication follows the escalation chain in the IR plan. The Security+ exam tests the concept that communication must be pre-planned and role-specific — impromptu communication during an incident leads to contradictory statements and leaked information.

### Regulatory Notification Requirements

| Regulation | Sector | Notification Requirement |
|---|---|---|
| HIPAA Breach Notification Rule | Healthcare | Within 60 days to affected individuals; immediate to HHS if 500+ records |
| PCI-DSS | Payment cards | Within 24–72 hours to card brands and acquiring bank |
| GDPR | EU personal data | Within 72 hours to supervisory authority |
| SEC (public companies) | Financial/public | Material incidents disclosed within 4 business days |
| State breach notification laws | All sectors | Varies by state — typically 30–90 days |

### Law Enforcement

Organizations must decide whether to involve law enforcement. Engagement may provide investigative resources but can reduce control over the investigation timeline. The IR plan should pre-determine the threshold for law enforcement notification (e.g., confirmed data theft, nation-state attribution, critical infrastructure impact).

---

## Section D — Lessons Learned

The lessons learned review is a formal post-incident meeting with the objective of process improvement. Best practices:

- Conduct within one to two weeks of incident closure.
- Include all stakeholders: IR team, affected business units, legal, communications.
- Use a blameless format focused on systemic improvement.
- Document findings in a written report with action items.

Questions the review should answer:

1. What happened and in what sequence?
2. When was the earliest detectable indicator, and when was it actually detected?
3. Were IR procedures followed? If not, why not?
4. What worked well?
5. What did not work or caused delays?
6. What controls would have prevented the incident?
7. What monitoring would have detected it earlier?
8. What changes are recommended?

---

## Key Terms

- **NIST SP 800-61**: NIST's Computer Security Incident Handling Guide
- **IR lifecycle phases**: Preparation, Detection and Analysis, Containment/Eradication/Recovery, Post-Incident Activity
- **IOC (Indicator of Compromise)**: Technical artifact suggesting compromise
- **IOA (Indicator of Attack)**: Behavioral pattern suggesting an active attack
- **Precursor**: Early warning sign that an attack may be imminent
- **Order of volatility**: Hierarchy of evidence from most to least fleeting
- **Write blocker**: Device preventing writes to evidence media during imaging
- **Chain of custody**: Documented record of all evidence handling
- **Forensic image**: Bit-for-bit copy of a storage device with verified hash
- **Containment**: Limiting incident damage without full remediation
- **Eradication**: Removing attacker presence and closing vulnerabilities
- **Recovery**: Restoring systems to normal, verified-clean operation
- **Tabletop exercise**: Discussion-based IR simulation
- **Lessons learned**: Post-incident review for process improvement
- **Jump kit**: Portable collection of forensic tools and response resources

---

## Review Questions

1. List the four phases of the NIST SP 800-61 IR lifecycle in order.
2. What is the difference between an event, an alert, and an incident?
3. Define the order of volatility. Which evidence type is collected first?
4. Why are forensic disk images hashed before and after imaging?
5. What is a write blocker and why is hardware preferable to software?
6. What information must a chain of custody log contain?
7. Under HIPAA, how many days does a covered entity have to notify affected individuals after a breach?
8. What is a tabletop exercise and what gaps does it reveal?
9. Why is the lessons learned phase described as the most frequently skipped?
10. What is the "observation dilemma" in containment, and when might an organization choose observation over immediate ejection?

---

## Certification Exam Tip

Security+ SY0-701 frequently tests the four NIST IR phases in order, the definition of chain of custody, and the order of volatility. Expect scenario questions that ask you to identify the correct phase for a given action (e.g., "The team is wiping and rebuilding compromised servers" — that is eradication, not recovery). Know that recovery follows eradication and involves restoring from clean backups with monitoring.

---

*End of Reading Guide — Module 11*
