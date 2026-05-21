# Reading Guide: Module 13 - Digital Forensics and Threat Intelligence
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 13 – Digital Forensics and Threat Intelligence**! Digital forensics is the science of collecting, preserving, and analyzing digital evidence to support incident investigations and legal proceedings. Threat intelligence transforms raw data about adversaries into actionable knowledge. SY0-701 tests both disciplines in Domain 4 (Security Operations, 28%).

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Order of Volatility**: The forensic principle that evidence collection must prioritize the most volatile (short-lived) data sources first, because they will be lost when power is removed or time passes. The standard order from most to least volatile: CPU registers and cache → RAM (running processes, network connections, clipboard) → Swap/pagefile → Disk storage → Remote logging/SIEM data → Archived/backup media. SY0-701 tests order of volatility in scenarios where an analyst must decide what to collect first from a live compromised system.
*   **Chain of Custody**: The documented, unbroken record of who collected, handled, transferred, and had access to digital evidence from the moment of collection through final disposition. A broken chain of custody can render evidence inadmissible in legal proceedings. Every transfer of evidence must be logged with date, time, identity of the handler, and the condition of the evidence.
*   **Forensic Imaging**: The process of creating a bit-for-bit exact copy (forensic image) of a storage device, including deleted files, unallocated space, and file system metadata — everything on the drive, not just active files. Write blockers are used to prevent any writes to the original media during imaging, preserving the original evidence. Hash values (MD5, SHA-256) are computed for both the original and the image to verify integrity.
*   **Threat Intelligence**: Processed and analyzed information about threat actors, their tactics, techniques, and procedures (TTPs), and indicators of compromise (IOCs) — structured to support defensive decision-making. Sources include commercial threat intelligence feeds, government sharing programs (ISACs), and open-source repositories. STIX (Structured Threat Information eXpression) is the data format; TAXII (Trusted Automated eXchange of Intelligence Information) is the transport protocol.
*   **MITRE ATT&CK Framework**: A publicly available knowledge base that catalogs adversary tactics and techniques observed in real-world attacks, organized by attack phase (Initial Access, Execution, Persistence, Privilege Escalation, etc.). Security teams use ATT&CK to map detected activity to known adversary behaviors, identify defensive gaps, and build detection rules. SY0-701 tests ATT&CK as a threat intelligence and detection engineering resource.
*   **Threat Hunting**: A proactive security practice in which analysts actively search through network and endpoint data for signs of adversary activity that has evaded existing automated detections — as opposed to reactively responding to SIEM alerts. Threat hunters form a hypothesis (e.g., "an attacker is using living-off-the-land techniques with PowerShell") and then query data to confirm or refute it. IOCs and ATT&CK TTPs are key inputs to hunting hypotheses.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Digital forensics and threat intelligence fall under **Domain 4 – Security Operations (28%)** of SY0-701. Order of volatility and chain of custody are the most frequently tested forensics concepts on the exam.
*   **Order of Volatility Memory Aid:** "RAM before disk, disk before remote." The most volatile data (CPU registers, RAM) disappears when power is cut. Disk data persists after shutdown. Remote/SIEM logs are the most durable. If a question asks what to collect first from a live system, the answer involves RAM (running processes, open connections) before disk imaging.
*   **Write Blocker Purpose:** Write blockers prevent the forensic examiner's workstation from writing to the evidence drive during imaging. Without a write blocker, the act of connecting the drive to a computer modifies timestamps and metadata — compromising evidence integrity. SY0-701 tests write blockers as the correct tool when imaging original media.
*   **STIX vs. TAXII:** STIX is the language/format used to describe threat intelligence (what the threat looks like). TAXII is the protocol used to share/transport that intelligence between organizations (how it moves). Think: STIX = the data, TAXII = the delivery mechanism.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include order of volatility tables, chain of custody documentation examples, and MITRE ATT&CK framework walkthroughs aligned to SY0-701 exam objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Digital Forensics" and "Threat Intelligence" sections in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on the order of volatility, chain of custody requirements, and threat intelligence sharing formats.
*   **Required Video:** Watch the digital forensics and threat intelligence video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos include forensic acquisition workflow diagrams and ATT&CK framework navigation tutorials.

---

### Lab & Command Integration
In this week's hands-on lab, you will practice collecting volatile evidence from a simulated live system in the correct order of volatility, verify forensic image integrity using hash values, and map a sample set of IOCs to MITRE ATT&CK techniques. These are direct SY0-701 performance-based question skills.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to apply the order of volatility to any evidence collection scenario.
- [ ] Read the "Digital Forensics" and "Threat Intelligence" sections in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the forensics and threat intelligence video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize order of volatility: CPU/RAM first, disk second, remote logs last. STIX = format; TAXII = transport.
- [ ] Proceed to the weekly hands-on lab activity.
