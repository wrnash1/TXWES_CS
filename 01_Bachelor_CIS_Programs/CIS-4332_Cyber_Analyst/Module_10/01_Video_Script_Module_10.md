# Video Script: Module 10 — Digital Forensics: Evidence Collection and Chain of Custody

## Course: CIS-4332 Cyber Analyst

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

## Estimated Duration: 20-22 minutes

---

## SEGMENT 1 — Opening (0:00–1:30)

Welcome back. This module is about digital forensics — and specifically the foundational skills that every SOC analyst needs even if they never become a full-time forensic examiner. You do not need to be a DFIR specialist to understand why evidence must be collected in a specific order, why a chain of custody form matters, and why touching a suspect drive incorrectly can destroy both the evidence and the legal case.

The CySA+ exam tests these concepts directly. More importantly, the actions you take in the first thirty minutes of an incident response — whether you preserve or destroy forensic evidence — determine what the investigation can tell you. This module gives you the framework to make the right decisions.

We will cover: the order of volatility, forensic imaging and write blockers, hash verification, chain of custody documentation, legal holds, and the categories of artifacts that forensic analysis recovers from Windows and Linux systems.

---

## SEGMENT 2 — Order of Volatility (1:30–5:00)

[SHOW DIAGRAM: Order of volatility pyramid — RAM at top, disk at bottom, network at bottom-right]

The order of volatility is the principle that governs what you collect first at a forensic scene. The rule is straightforward: collect the most volatile evidence first, because it disappears when you are not looking.

At the top of the volatility ladder is RAM — physical memory. Everything in RAM is gone the moment the system powers off. And RAM contains the most investigatively valuable data on a running compromised system: active malware processes, decrypted file encryption keys, cleartext credentials loaded into memory, injected shellcode that exists nowhere on disk, and live network connections showing exactly who the attacker is communicating with right now. RAM acquisition must come first.

Below RAM is network state. This includes the current ARP cache — a mapping of IP addresses to MAC addresses for recently contacted systems — active network connections, and the routing table. This data is volatile, but slightly less so than RAM because network state can sometimes be partially reconstructed from SIEM logs. RAM cannot be reconstructed.

Next comes running process information: the list of active processes, their command-line arguments, their loaded DLLs, their parent-child relationships. This is related to RAM but can sometimes be captured with lighter-weight tools before full memory acquisition.

Below that is the file system. Hard drives and SSDs are non-volatile — data on disk persists through a power cycle. But within the file system, some artifacts are time-sensitive: recently deleted files before they are overwritten, temporary files, browser cache. The file system comes after volatile sources.

At the bottom: removable media, external logs, archived data, printed documents. These are stable and can be collected last.

The exam frequently tests this hierarchy in scenario questions. When you see a running compromised system, the answer is always: collect RAM first.

---

## SEGMENT 3 — Forensic Imaging and Write Blockers (5:00–9:00)

[SHOW DIAGRAM: Write blocker between suspect drive and forensic workstation — arrows showing blocked write path]

After collecting volatile evidence, you need to create a forensic image of the storage media — a bit-for-bit copy of every sector on the drive, including unallocated space, deleted file remnants, and file system metadata.

The cardinal rule of forensic acquisition is: you never work directly on the original evidence. You work on the image. The original is preserved in a sealed evidence bag, logged into the chain of custody, and stored securely. If anything goes wrong with your analysis — a tool crashes, a drive fails — the original is intact and you can re-image it.

To create an unmodified forensic image, you use a write blocker. A write blocker is a hardware device or software solution that sits between the suspect drive and the forensic workstation. It intercepts every write command sent from the workstation to the drive and prevents it from reaching the source media. The drive can only be read.

Without a write blocker, simply connecting a drive to a Windows workstation causes writes to occur. Windows mounts the volume, updates access timestamps, writes registry metadata, and modifies the file system. The drive has been contaminated before you even opened a forensic tool. A write blocker prevents all of this.

Hardware write blockers: Tableau forensic bridges, ICS Image MaSSter, Logicube Forensic Falcon. These are purpose-built hardware devices used in professional DFIR labs.

Software write blockers: operating system-level tools that configure a drive as read-only before mounting. Less reliable than hardware because a software bug or OS vulnerability could potentially allow writes through.

Imaging tools: FTK Imager (free, widely used), dd (Unix command-line), Autopsy (open-source, includes imaging), Cellebrite (mobile and endpoint forensics).

Standard forensic image formats: E01 (EnCase Evidence File — includes metadata and compression), raw/dd (uncompressed bit-for-bit copy), AFF4 (open standard with metadata support).

---

## SEGMENT 4 — Hash Verification (9:00–11:30)

[SHOW SCREEN: FTK Imager hash verification result — source MD5 vs. image MD5 shown as matching]

After creating a forensic image, you verify its integrity using cryptographic hashing. You generate the MD5 or SHA-256 hash of the source drive and the hash of the image file. If the hashes are identical, the image is a bit-for-bit perfect copy of the source.

Why does this matter? Because in a legal proceeding, the defense will challenge whether your evidence has been tampered with. Matching hashes prove that every single bit in your image was copied exactly from the source, and that no modification occurred during acquisition. If the hashes do not match, the image is not forensically sound — something changed during copying, and you need to re-image.

MD5 produces a 128-bit hash. It is fast and widely supported. SHA-256 produces a 256-bit hash and is cryptographically stronger — use SHA-256 for any investigation where litigation is anticipated.

Hash verification is documented on the chain of custody form: source hash, image hash, the tool and algorithm used, the analyst who performed the verification, and the timestamp. You also hash again when the image is transferred to another analyst or location. The receiving analyst re-hashes the image and compares it to the documented source hash. Any discrepancy must be investigated.

---

## SEGMENT 5 — Chain of Custody (11:30–14:30)

Chain of custody is the documented, unbroken record of who had possession of the evidence, what they did with it, when they received it, and when they transferred it. Every time evidence changes hands, both parties sign the chain of custody form.

Why does this matter? Because forensic evidence is only admissible in legal proceedings if the integrity of the evidence can be demonstrated. A break in the chain of custody — an undocumented handoff, a missing signature, an unexplained time gap where the evidence was unaccounted for — allows a defense attorney to argue that the evidence may have been tampered with during that gap.

A complete chain of custody form documents:

Initial acquisition: who collected the evidence, from what device or location, using what tools, at what time. The hash value of the collected evidence. The evidence tag number.

Storage: where the evidence is stored — a locked evidence room, a secure safe, a write-protected drive. Access is restricted to documented custodians.

Transfer: every time evidence moves from one person to another or from one location to another, both parties sign with name, date, time, and reason for transfer.

Analysis: when an analyst accesses the evidence for examination, they document what was accessed, what tools were used, and when the analysis session began and ended. Analysis is always performed on the forensic copy — never on the original.

Final disposition: when the investigation concludes, evidence is either returned to its owner, retained per the evidence retention policy, or destroyed per legal guidance.

---

## SEGMENT 6 — Legal Holds and Forensic Preservation (14:30–17:00)

[SHOW DIAGRAM: Legal hold process — notification triggers preservation, evidence feeds litigation]

A legal hold is a directive from an organization's legal team to preserve all data and documents potentially relevant to anticipated or active litigation or regulatory investigation. The legal hold obligation supersedes the normal data retention and deletion schedules.

Here is why this matters for an IR analyst: if you are conducting a forensic investigation on systems that are also under a legal hold, you must coordinate with legal counsel before taking any action that modifies or deletes data. Destroying or modifying data subject to a legal hold is called spoliation — and courts take it seriously. Spoliating evidence can result in sanctions, adverse jury instructions, or losing the legal case entirely.

The practical guidance for analysts: if your organization's legal team has notified you that a legal hold is in effect, do not wipe systems. Do not overwrite logs. Do not delete backups. Do not take any remediation action that destroys data until you have explicit confirmation from legal counsel that the relevant evidence has been preserved separately.

IR investigation and legal hold can coexist — in fact, a well-documented forensic acquisition performed under legal hold is exactly the right process. Communicate with legal counsel, document everything, and do not take shortcuts.

---

## SEGMENT 7 — Forensic Artifacts on Windows Systems (17:00–19:30)

[SHOW DIAGRAM: Windows artifact map — registry, event logs, prefetch, browser history, MFT]

When you analyze a Windows disk image, there are specific artifact categories that yield the highest investigative value.

The Windows Registry contains evidence of: recently run programs, USB devices that were connected, recently opened documents, attacker-created registry run key persistence entries, and service configurations.

The Windows Event Log contains authentication events (Event ID 4624 successful logon, 4625 failed logon), process creation events (Event ID 4688), service installation events (Event ID 7045), and account management events (Event ID 4720 user account created).

The Master File Table is the NTFS file system's index of all files — including deleted files. Deleted files are not immediately removed from the MFT; the entry is marked as available for reuse. Forensic tools can recover file names, sizes, and timestamps of deleted files from the MFT long after they are deleted.

Prefetch files in the Windows Prefetch directory are cached execution records. Windows stores prefetch entries for applications that have been run, including executables that have since been deleted. If an attacker ran a tool and deleted it, the prefetch record may still show it was executed.

Browser artifacts (history, cookies, cached files, download records) reveal websites visited, files downloaded, and attacker reconnaissance activity.

---

## SEGMENT 8 — Module Summary and Lab Preview (19:30–21:30)

Let me bring this together.

The order of volatility tells you what to collect first: RAM, then network state, then running processes, then file system, then external artifacts. Violating this order means the most valuable evidence is lost.

Write blockers prevent modifications to source media during forensic acquisition. Hardware write blockers are more reliable than software. Never connect a suspect drive without a write blocker.

Hash verification proves your forensic image is identical to the source. Document the hash values on the chain of custody form. Re-verify when the image is transferred.

Chain of custody documentation is the unbroken record of evidence handling. Every transfer is signed. Analysis is always performed on the copy. A break in custody jeopardizes legal admissibility.

Legal holds require preserving evidence without modification. IR and legal can coexist; coordinate with counsel, do not destroy data.

Windows forensic artifacts — registry, event logs, MFT, prefetch, browser history — each contain specific categories of evidence that support different investigative questions.

In the lab this week, you will analyze a simulated forensic evidence collection scenario for a compromised Windows workstation. You will apply the order of volatility, review a chain of custody form for errors, and identify the forensic artifacts that answer specific investigative questions.

For the CySA+ exam: know the order of volatility, know why write blockers are required, know the difference between chain of custody and legal hold, and know what Windows artifact type corresponds to what investigative question.

I will see you in the lab.

---

Texas Wesleyan University | CIS-4332 Cyber Analyst | Professor Nash
