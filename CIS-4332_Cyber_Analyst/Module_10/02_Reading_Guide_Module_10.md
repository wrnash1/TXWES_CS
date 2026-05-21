# Reading Guide: Module 10 - Digital Forensics – Evidence Collection and Chain of Custody
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 10 - Digital Forensics – Evidence Collection and Chain of Custody**! This module covers how analysts and forensic investigators collect, preserve, and document digital evidence from compromised systems in a manner that maintains legal admissibility and investigative integrity. You will learn the order of volatility, forensic acquisition methods, chain of custody documentation requirements, and write-blocker usage. These topics are tested under **Domain 3: Incident Response and Management (20%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn how to prioritize evidence collection by volatility, create forensically sound disk images, and maintain proper documentation throughout an investigation. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Order of Volatility**: The principle that digital evidence should be collected in order from most volatile (most likely to be lost) to least volatile (most persistent). The standard order is: CPU registers and cache → RAM (running processes, network connections, encryption keys) → swap/page file → disk storage → remote logs → archived media. CySA+ exam questions frequently ask which evidence source should be collected first — the answer is always the most volatile one that has not yet been captured.
*   **Chain of Custody**: A documented, unbroken record of who collected, handled, transferred, or analyzed a piece of evidence and when. Chain of custody documentation must be maintained from the moment evidence is collected through its presentation in any legal or disciplinary proceeding. A gap or undocumented handoff in the chain can render evidence inadmissible. CySA+ tests chain of custody as a required component of any formal forensic investigation.
*   **Write Blocker**: A hardware or software device that prevents any write operations from being sent to a storage device during forensic acquisition, ensuring the source media is not modified. Using a write blocker is required to maintain the forensic integrity of disk evidence — acquiring a disk image without one may alter file system metadata (access timestamps) and make the evidence legally challengeable.

---

### 2. Certification Exam Tips
*   **Focus Area – Evidence Volatility (Domain 3):** CySA+ CS0-003 consistently tests the order of volatility. Know that RAM must be collected before the system is powered off, because shutdown destroys all volatile memory contents. If a scenario asks what to collect first from a running compromised system, the answer is a memory image (RAM dump), not a disk image.
*   **Scenario Trap – Forensic Image vs. Live System:** Working directly on a compromised system's original disk (without imaging it first) risks altering evidence. The forensically correct procedure is to create a bit-for-bit image of the disk using a write blocker, then analyze the image — never the original. CySA+ tests this distinction in forensic methodology questions.
*   **Legal Hold vs. Evidence Preservation:** Legal hold is a directive to preserve all relevant data when litigation is anticipated — it applies broadly to backups, emails, and logs. Forensic evidence preservation is the technical act of collecting and imaging specific artifacts for investigation. CySA+ may test whether you correctly distinguish these two concepts and know when each is required.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist includes digital forensics concepts, evidence collection procedures, and chain of custody requirements mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource covers forensic acquisition workflows and volatility ordering exercises.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Digital Forensics and Evidence Handling** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details evidence collection procedures, chain of custody requirements, and forensic acquisition techniques tested on the exam.
*   **Required Video:** Watch the video lecture on **Digital Forensics – Evidence Collection and Chain of Custody** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of memory acquisition, disk imaging, and chain of custody documentation.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Acquire a memory image from a running virtual machine**: Using a memory acquisition tool (e.g., WinPmem on Windows or `dd if=/dev/mem` on Linux), capture a RAM image from a lab VM into a file, record the acquisition start/end timestamps and the MD5/SHA-256 hash of the resulting image file, and document these in a chain of custody form.
*   **Create a forensic disk image using a write blocker**: Attach a lab USB drive through a hardware or software write blocker, use `dd` or FTK Imager to create a bit-for-bit image, generate a hash of both the source drive and the resulting image to verify they match, and document any discrepancies.
*   **Complete a chain of custody form for both acquired artifacts**: Using the provided template, fill in collector name, collection date/time, device description, acquisition method, hash values, and handling notes — then review a second student's completed form to identify any documentation gaps that could affect evidence admissibility.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Digital Forensics and Evidence Handling** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Digital Forensics – Evidence Collection and Chain of Custody** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the evidence acquisition commands and chain of custody documentation steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
