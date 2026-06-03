# Video Script: Module 12 — Digital Forensics (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 12 | Texas Wesleyan University"]**

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome to Module 12 — Digital Forensics.

In Module 11 we learned how to respond to incidents. In this module we go deeper into the science behind how we investigate them. Digital forensics is the application of scientific methods to the recovery, analysis, and presentation of digital evidence in a way that is legally defensible.

"Legally defensible" is the phrase that defines this field. An investigator can be the most technically skilled analyst in the world, but if they cannot stand before a judge and explain exactly what they did, how they did it, and how they know the evidence is unaltered, their findings may be inadmissible. Digital forensics is equal parts technical science and legal craft.

In Part 1 we cover the forensic process — the four stages that every investigation follows — and we go deep on evidence collection: write blockers, disk imaging with dd and FTK Imager, and memory acquisition. In Part 2 we cover memory analysis, log analysis, and the legal and ethical considerations that govern the field.

---

## Section 1 — What Is Digital Forensics?

**[SHOW SLIDE: Forensics definition and scope diagram]**

Digital forensics is a branch of forensic science. Just as a physical crime scene investigator applies scientific methods to fingerprints and DNA, a digital forensic examiner applies scientific methods to files, logs, network packets, and memory contents.

The goal is to answer questions: Was this system compromised? What data was accessed or stolen? Who did this? When? How did they get in? What did they do while inside?

Digital forensics serves multiple purposes:

- **Criminal prosecution**: Building a case for law enforcement or a prosecutor.
- **Civil litigation**: Supporting or defending against lawsuits (e-discovery).
- **Incident response**: Understanding the scope and nature of a breach to guide remediation.
- **Internal investigations**: Investigating employee misconduct or policy violations.

The Security+ exam tests digital forensics primarily in the incident response context. Know the process, the tools, and the legal boundaries.

---

## Section 2 — The Forensic Process

**[SHOW SLIDE: Forensic process stages — Identification, Preservation, Collection, Analysis, Reporting]**

The digital forensic process is typically described in four to five stages. Different frameworks use slightly different labels, but the NIST and ISO definitions align closely on this structure.

**Stage 1 — Identification**

Identification is recognizing what potential evidence exists and where it lives. This includes:

- Identifying the systems, devices, and accounts involved in the incident.
- Determining what types of data each source may contain.
- Assessing legal authority to access each source — do you have consent, a warrant, or policy authorization?
- Applying the order of volatility to prioritize collection.

You cannot collect what you do not identify. A missed data source early in the investigation can be fatal to the case later.

**Stage 2 — Preservation**

Preservation protects evidence from modification. This is where write blockers and forensic imaging come in. The original evidence is isolated and protected. All analysis is performed on forensically verified copies.

Preservation also includes legal holds — formal instructions to preserve records that may be relevant to litigation. When legal hold notices are issued, normal data retention deletion policies are suspended for affected records.

**Stage 3 — Collection**

Collection is the actual acquisition of evidence. For digital evidence this means:

- Capturing volatile memory before shutdown.
- Creating verified forensic disk images.
- Collecting relevant log files from systems and cloud services.
- Preserving network capture data.
- Documenting chain of custody for each collected item.

**Stage 4 — Analysis**

Analysis examines the collected evidence to reconstruct events and answer investigative questions. This includes file system analysis, memory analysis, log correlation, and artifact analysis. Analysis is performed on forensic copies — never on original evidence.

**Stage 5 — Reporting**

The forensic report documents the investigator's methodology, findings, and conclusions in a format that can be understood by non-technical stakeholders and withstand cross-examination. It includes:

- What data was examined.
- What methods and tools were used.
- What was found.
- What it means — the investigator's conclusions.

---

## Section 3 — Write Blockers

**[SHOW SLIDE: Hardware write blocker photograph with labeled ports]**

A write blocker is the first tool an examiner deploys when working with original evidence media.

Without a write blocker, simply connecting a storage device to a computer running Windows or macOS will modify the device. The operating system writes to update last-access timestamps, mount records, and volume metadata. These modifications change the digital fingerprint of the evidence. In court, opposing counsel will challenge whether the changes were investigator-introduced or pre-existing.

A **hardware write blocker** sits between the suspect drive and the forensic workstation. It intercepts all write commands at the hardware level and returns a "success" response to the OS without actually executing the write. The OS believes it succeeded, but the drive was never written to.

Hardware write blockers are preferred in legal proceedings because they operate independently of software and are harder to challenge. A software write blocker — typically a kernel-level driver — can also be challenged as improvable via software misconfiguration.

Common hardware write blocker manufacturers include Tableau (acquired by Guidance Software/OpenText) and WiebeTech.

After attaching the write blocker, the examiner verifies the device can be read and then hashes the device — producing both an MD5 and SHA-256 hash of the entire drive — before imaging begins.

---

## Section 4 — Disk Imaging with dd

**[SHOW SLIDE: dd command syntax diagram]**

The `dd` command is a Unix/Linux utility that copies data at the bit level. It has been used for forensic imaging for decades. The basic syntax for creating a forensic image is:

```
dd if=/dev/sdb of=/mnt/evidence/sdb.img bs=4096 conv=noerror,sync status=progress
```

Breaking this down:

- `if=/dev/sdb` — input file: the source drive (the suspect device)
- `of=/mnt/evidence/sdb.img` — output file: the destination image file on forensic media
- `bs=4096` — block size: read and write in 4096-byte chunks (improves performance)
- `conv=noerror,sync` — on read error, pad with zeros rather than stopping (preserves image structure even if the drive has bad sectors)
- `status=progress` — shows live progress during imaging

After imaging, the investigator hashes both the source and the image to verify they match:

```
md5sum /dev/sdb
md5sum /mnt/evidence/sdb.img
sha256sum /dev/sdb
sha256sum /mnt/evidence/sdb.img
```

If the hashes match, the image is forensically sound. The hash values are documented in the chain of custody.

`dcfldd` is an enhanced version of dd with built-in hash verification during imaging, preferred by many forensic investigators for its integrated validation.

---

## Section 5 — Disk Imaging with FTK Imager

**[SHOW SLIDE: FTK Imager interface screenshot]**

FTK Imager, developed by AccessData (now Exterro), is a free Windows-based graphical forensic imaging tool that is widely used by law enforcement and corporate investigators. It provides a GUI alternative to the command-line dd.

FTK Imager capabilities include:

- Create forensic images in multiple formats: E01 (EnCase), AD1, and raw (dd-compatible).
- Verify image integrity with MD5 and SHA-1 hashing automatically during imaging.
- Mount forensic images as read-only drives for browsing without alteration.
- Preview file system contents without creating an image (for triage).
- Acquire memory (RAM) dumps from live systems.
- Export specific files or directories from an image.

The E01 (Expert Witness Format) is the most common format in law enforcement and corporate forensics. It stores the image in compressed, split segments with embedded hash values, case notes, and examiner information. This self-documenting format makes it court-friendly.

When FTK Imager completes imaging, it automatically generates a verification report that records the computed hashes and confirms whether the image hash matches the source hash. This verification report is attached to the case documentation.

---

## Closing — Part 1

**[INSTRUCTOR ON CAMERA]**

We have covered the five-stage forensic process — Identification, Preservation, Collection, Analysis, and Reporting. We went deep on the tools that make sound collection possible: write blockers, dd, and FTK Imager.

The theme of everything in Part 1 is integrity — proving that the evidence you analyzed is identical to what you collected from the original device. Every step from write blocker to hash verification exists to protect that chain of integrity.

In Part 2 we shift to what happens after collection: memory analysis, log analysis, and the legal considerations that shape what investigators can and cannot do.

See you in Part 2.

---

*End of Part 1*
