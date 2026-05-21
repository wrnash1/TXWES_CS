# Quiz: Module 10 - Digital Forensics – Evidence Collection and Chain of Custody
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
A forensic investigator arrives at a compromised Windows workstation that is still powered on and running. The investigator needs to collect evidence before shutting the system down. According to the order of volatility, which evidence source must be collected first?

*   A) The contents of the physical hard drive, because disk data is the most reliable and persistent form of evidence
*   B) The contents of RAM (physical memory), because running processes, active network connections, and encryption keys in memory will be permanently lost when the system is powered off
*   C) The Windows Event Log files on disk, because they contain the complete authentication and system activity history needed for the investigation
*   D) The network switch's ARP cache, because it identifies all hosts that recently communicated with the compromised workstation
*   **Correct Answer:** B) The contents of RAM (physical memory), because running processes, active network connections, and encryption keys in memory will be permanently lost when the system is powered off.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Hard disk contents are non-volatile and will persist through a power cycle — they can be acquired after RAM. Collecting disk before RAM violates the order of volatility and risks losing the most time-sensitive evidence.
    *   *Why B is correct:* RAM is the most volatile evidence source on a running system. It contains running malware processes, established network connections, decrypted file keys, and attacker commands typed in interactive shells — all of which vanish permanently on shutdown. Memory acquisition must come first.
    *   *Why C is incorrect:* Windows Event Log files are stored on disk and are non-volatile; they will still be available after the memory acquisition is complete. Collecting them first would cause higher-priority volatile evidence to be lost.
    *   *Why D is incorrect:* The network switch's ARP cache is a useful pivot for identifying connected hosts, but it is an external network device — not a component of the immediate endpoint evidence. Endpoint volatile memory takes collection priority.

---

**Question 2**
In digital forensics, which of the following most accurately defines the **chain of custody**?

*   A) The order in which digital evidence sources should be collected, from most volatile to least volatile, to preserve the maximum amount of evidence from a running system
*   B) A documented, unbroken record of who collected, handled, transferred, and analyzed a piece of evidence and when — required to maintain legal admissibility throughout an investigation
*   C) The process of creating a cryptographic hash of a disk image to verify that the forensic copy is bit-for-bit identical to the original source media
*   D) A legal directive issued by an organization to preserve all potentially relevant data when litigation or a regulatory investigation is anticipated
*   **Correct Answer:** B) A documented, unbroken record of who collected, handled, transferred, and analyzed a piece of evidence and when — required to maintain legal admissibility throughout an investigation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Collecting evidence from most volatile to least volatile describes the order of volatility principle — a separate but related forensic concept. Chain of custody is about documentation of who touched the evidence, not collection order.
    *   *Why B is correct:* Chain of custody documentation records every person who had access to the evidence, every transfer between custodians, and the timestamps of each event. Any break in this chain — an undocumented handoff, missing signature, or unaccounted time gap — can make the evidence inadmissible in court or disciplinary proceedings.
    *   *Why C is incorrect:* Hashing a disk image to verify integrity is a forensic integrity verification technique (confirming the copy matches the original). It is a component of sound forensic practice but is not the definition of chain of custody.
    *   *Why D is incorrect:* A legal hold directive to preserve data describes litigation hold — a legal process concept related to e-discovery. Chain of custody is the technical evidence handling documentation record, not the legal preservation directive.

---

**Question 3**
A forensic analyst is preparing to create a disk image of a suspect's hard drive. Which tool or technique ensures the source drive is not modified during the acquisition process?

*   A) Running a full antivirus scan on the source drive before imaging to remove any malware that might interfere with the acquisition tool
*   B) Attaching the source drive through a hardware or software write blocker before beginning the imaging process to prevent any write operations from reaching the source media
*   C) Compressing the disk image file using a high-compression algorithm to reduce the storage space required for the forensic copy
*   D) Imaging the source drive while it is still installed in the suspect's running computer to capture the live file system state
*   **Correct Answer:** B) Attaching the source drive through a hardware or software write blocker before beginning the imaging process to prevent any write operations from reaching the source media.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running an AV scan on the source drive before imaging would read from and potentially write to the drive (quarantining files, updating scan timestamps), modifying the evidence. This is the opposite of forensically sound procedure.
    *   *Why B is correct:* A write blocker intercepts all write commands at the hardware or software layer and prevents them from reaching the source drive, ensuring the forensic acquisition cannot alter any data on the original media. This preserves the drive's evidential integrity and is required for court-admissible forensic images.
    *   *Why C is incorrect:* Compressing the image file affects the copy, not the source drive. While compression is a legitimate storage optimization for forensic images, it does not protect source drive integrity and is unrelated to write blocking.
    *   *Why D is incorrect:* Imaging a drive while it is installed in a running computer risks modifying the source — the OS continuously writes to the disk (log updates, swap file, access timestamps). Proper forensic acquisition removes the drive and uses a write blocker in an offline context.

---

**Question 4**
After acquiring a forensic disk image, the analyst generates an MD5 hash of the source drive and an MD5 hash of the image file. The two hashes are identical. What does this confirm?

*   A) The disk image file is free of malware and safe to analyze on any workstation without additional precautions
*   B) The forensic image is a bit-for-bit identical copy of the source drive — any analysis performed on the image will produce results that accurately represent the original evidence
*   C) The hash values confirm that the chain of custody form has been completed correctly and that all evidence handling was properly documented
*   D) The identical hashes confirm that the source drive was not encrypted, since encrypted drives produce different hash outputs than unencrypted drives
*   **Correct Answer:** B) The forensic image is a bit-for-bit identical copy of the source drive — any analysis performed on the image will produce results that accurately represent the original evidence.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Identical MD5 hashes confirm data integrity between source and copy; they say nothing about whether the drive contains malware. Malware on the drive would produce the same hash on both the source and image — confirming the copy is accurate, not that it is clean.
    *   *Why B is correct:* Hash verification is the standard method for confirming forensic image integrity. Identical hashes on source and image prove no bits were altered during acquisition — the image is an exact duplicate. This allows investigators to analyze the image rather than the original without compromising evidential integrity.
    *   *Why C is incorrect:* Hash verification confirms image integrity only; it has no relationship to chain of custody documentation, which is a separate record-keeping process involving signatures, timestamps, and custody transfer logs.
    *   *Why D is incorrect:* Encrypted drives do produce consistent hashes — the hash captures the actual bit pattern on disk regardless of whether those bits are plaintext or ciphertext. Encryption status does not cause hash differences between source and image.

---

**Question 5**
An organization's legal team issues a litigation hold following a data breach lawsuit. The IR team is simultaneously conducting a forensic investigation of the same systems. Which two actions together correctly address both the legal hold requirement and the forensic investigation requirement?

*   A) Immediately wipe all affected systems and restore from backup to minimize legal liability, and notify the legal team after the restoration is complete
*   B) Preserve all relevant logs, emails, and data in their current state per the legal hold directive without modification, and separately create forensic images of affected systems using write blockers for the IR investigation — maintaining chain of custody documentation for all collected artifacts
*   C) Hand all evidence directly to outside legal counsel and suspend the IR investigation until the lawsuit is resolved to avoid any conflict between forensic and legal processes
*   D) Delete any logs that contain sensitive employee data before preserving the rest, to minimize privacy exposure in the litigation, then proceed with the forensic imaging
*   **Correct Answer:** B) Preserve all relevant logs, emails, and data in their current state per the legal hold directive without modification, and separately create forensic images of affected systems using write blockers for the IR investigation — maintaining chain of custody documentation for all collected artifacts.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Wiping affected systems during an active litigation hold is spoliation of evidence — a serious legal violation that can result in court sanctions, adverse jury instructions, or dismissal of the organization's legal position. Systems under legal hold must never be wiped.
    *   *Why B is correct:* Legal hold requires preserving data without modification; forensic investigation requires acquiring evidence with integrity controls (write blockers, hashing, chain of custody). These two requirements are compatible when properly coordinated — both protect evidence, just for different purposes (legal versus investigative). Maintaining chain of custody documentation satisfies both.
    *   *Why C is incorrect:* Suspending the IR investigation creates ongoing security risk and does not satisfy the organization's duty to investigate and remediate the breach. Legal and forensic processes can and should proceed in parallel with proper coordination.
    *   *Why D is incorrect:* Selectively deleting logs during a litigation hold constitutes spoliation of evidence regardless of the privacy rationale. Privacy concerns must be addressed through legal counsel's guidance on redaction of produced documents, not destruction of evidence.
