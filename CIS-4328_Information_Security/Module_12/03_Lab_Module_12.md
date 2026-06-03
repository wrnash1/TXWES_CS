# Lab: Module 12 — Digital Forensics

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

In this lab you will perform hands-on digital forensic activities using free, open-source tools. You will create a forensic disk image with hash verification, analyze a pre-collected memory image using Volatility, analyze Windows event logs to reconstruct attacker activity, and practice file carving. All activities use legal, purpose-built forensic training resources.

**Estimated completion time:** 2 to 2.5 hours

**Tools required:** FTK Imager (free from exterro.com), Volatility 3 (free from volatilityfoundation.org), Event Viewer (Windows built-in), Eric Zimmermann's EvtxECmd (free from github.com/EricZimmermann), a hex editor (HxD, free from mh-nexus.de)

---

## Learning Outcomes

By completing this lab you will be able to:

- Create a forensically sound image and verify it with hash comparison.
- Perform basic memory analysis to identify running processes and network connections.
- Analyze Windows event logs to identify indicators of compromise.
- Use file signatures to identify file types and understand file carving.
- Document findings in a structured lab report using forensic methodology.

---

## Part 1 — Forensic Disk Imaging with FTK Imager

### Step 1 — Download and Install FTK Imager

Download FTK Imager (version 4.7 or current) from `exterro.com/digital-forensics-software/ftk-imager`. Install it on your forensic workstation. No license is required for the free version.

### Step 2 — Create an Image of a USB Drive or Logical Drive

For this exercise you will image a small USB drive (any capacity) or use FTK Imager's ability to image a logical drive (a partition on your existing hard disk). If using a physical USB drive, attach it before opening FTK Imager.

In FTK Imager:

1. Select **File** → **Create Disk Image**
2. Select **Physical Drive** (for USB) or **Logical Drive** (for a partition)
3. Select the target drive from the dropdown
4. Click **Add** to add a destination
5. Select **Raw (dd)** as the image type
6. Set the image folder and filename (e.g., `lab_image_mod12.img`)
7. Fill in the case information fields: Case Number `LAB-MOD12-001`, Evidence Number `E-001`, Examiner Name (your name)
8. Click **Finish** and then **Start**

FTK Imager will create the image and automatically compute MD5 and SHA-1 hashes for both the source and the image.

### Step 3 — Verify the Image

When imaging completes, FTK Imager displays the hash comparison result. Take a screenshot showing both the source hash and the image hash.

**Lab Question 1:** What does it mean if the MD5 hash of the source drive matches the MD5 hash of the image? What would you conclude if they did not match?

### Step 4 — Mount the Image Read-Only

In FTK Imager, select **File** → **Image Mounting**. Mount the image you just created as a read-only logical drive. Browse the mounted drive in Windows Explorer.

**Lab Question 2:** Why is mounting the image read-only rather than the original drive important for maintaining forensic integrity? What risk would mounting the original drive introduce?

---

## Part 2 — Memory Analysis with Volatility

### Step 1 — Download a Training Memory Image

Download the Volatility Foundation's sample memory image for training. A suitable image is available from the Volatility GitHub repository or from established DFIR training sites such as:

- `github.com/volatilityfoundation/volatility/wiki/Memory-Samples` — links to training images
- MemLabs challenges at `github.com/stuxnet999/MemLabs` — beginner memory forensics challenges

Download a Windows 7 or Windows 10 training image for this exercise.

### Step 2 — Identify the Image Profile

With Volatility 3 installed, open a terminal in the Volatility directory and run:

```
python vol.py -f <path-to-memory-image> windows.info
```

Record the OS version, build number, and machine name.

**Lab Question 3:** Why must you identify the correct OS profile before running other Volatility plugins? What would happen if you applied a Windows 7 plugin to a Windows 10 image?

### Step 3 — List Running Processes

Run the following commands:

```
python vol.py -f <image> windows.pslist
python vol.py -f <image> windows.pstree
```

Review the output. Look for:

- Processes with unusual parent-child relationships (e.g., `cmd.exe` spawned from a non-interactive process like `svchost.exe`)
- Processes running from unusual paths (e.g., `%TEMP%`, `%AppData%\Roaming`)
- Multiple instances of processes that should be unique (e.g., two instances of `lsass.exe`)

**Lab Question 4:** List any process in the output that you consider suspicious and explain your reasoning. If no process appears suspicious in your sample image, describe what characteristics would make a process suspicious in a real investigation.

### Step 4 — List Network Connections

Run:

```
python vol.py -f <image> windows.netscan
```

Identify all established and listening connections. Note external IP addresses.

**Lab Question 5:** What types of evidence would a network connection entry in a memory image provide that a static disk image could not? Give a specific example of how a network connection finding could change the direction of an investigation.

### Step 5 — Search for Suspicious Memory Regions

Run:

```
python vol.py -f <image> windows.malfind
```

Review the output for memory regions marked as executable that are not associated with a loaded DLL.

**Lab Question 6:** What does it mean when `malfind` identifies a memory region with `PAGE_EXECUTE_READWRITE` permissions? Why is this combination of permissions suspicious in a legitimate process?

---

## Part 3 — Windows Event Log Analysis

### Step 1 — Examine Security Event Log

Open Windows Event Viewer (run `eventvwr.msc`). Navigate to **Windows Logs** → **Security**.

Filter for the following Event IDs by selecting **Filter Current Log** and entering the IDs:

- 4625 (Failed logons)
- 4624 (Successful logons)
- 4720 (User account created)
- 4698 (Scheduled task created)

**Lab Question 7:** On your own system (or a provided training log), find any 4625 events. Record the username, source IP address, and timestamp. How many consecutive 4625 events would you flag as a brute-force attempt?

### Step 2 — Analyze a Provided Suspicious Event Log

Download the sample .evtx file provided in the course LMS (filename: `Module12_Suspicious_Security.evtx`). If the file is not available, use EvtxECmd to export your own Security log:

```
EvtxECmd.exe -f "C:\Windows\System32\winevt\Logs\Security.evtx" --csv C:\Lab\output
```

Open the CSV in Excel or Timeline Explorer. Sort by Event ID 4698 (scheduled task created).

**Lab Question 8:** For any scheduled task creation events found, record: the task name, the program it runs, the creating user, and the timestamp. Explain why scheduled tasks are a common attacker persistence mechanism.

---

## Part 4 — File Signatures and File Carving Concepts

### Step 1 — Examine File Signatures with a Hex Editor

Open HxD (free hex editor). Open any JPEG image file on your system. Examine the first 4 bytes.

A JPEG file begins with: `FF D8 FF E0` or `FF D8 FF E1`

Open a PDF file. A PDF begins with: `25 50 44 46` (which is ASCII for `%PDF`)

**Lab Question 9:** Why do file signatures (magic bytes) at the start of a file allow forensic tools to identify file types even when the file extension has been changed or the file system entry is missing? Create a table listing the magic bytes for at least three file types.

### Step 2 — Conceptual File Carving Exercise

You are investigating a USB drive that was formatted before you could image it. The format operation marked all blocks as unallocated but did not overwrite the data.

**Lab Question 10:** Describe the steps a forensic tool would take to recover JPEG image files from the unallocated space of this USB drive using file carving. What are the limitations of this technique? Under what circumstances might file carving fail to recover usable files?

---

## Part 5 — Chain of Custody Documentation

Complete a chain of custody form for the disk image you created in Part 1.

```
CHAIN OF CUSTODY — FORENSIC DISK IMAGE
Case Number: LAB-MOD12-001
Evidence Tag: E-001
Date/Time Created: _____________________________
Created By: ____________________________________
Source Device: _________________________________
  Make/Model: __________________________________
  Serial Number: _______________________________
Image Format: Raw (dd) / .img
Image File Path: ________________________________
MD5 Hash (source): _____________________________
MD5 Hash (image): ______________________________
SHA-1 Hash (source): ____________________________
SHA-1 Hash (image): _____________________________
Hashes Match: Yes / No
Image stored at: ________________________________
```

---

## Deliverables

Submit a lab report containing:

- Answers to Lab Questions 1 through 10.
- Screenshots from Part 1 Steps 3 and 4.
- Screenshot of Volatility pslist output from Part 2.
- Completed chain of custody form from Part 5.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Disk imaging and hash verification (Questions 1–2 + screenshots) | 20 |
| Part 2 — Memory analysis (Questions 3–6 + screenshot) | 35 |
| Part 3 — Event log analysis (Questions 7–8) | 20 |
| Part 4 — File signatures and carving (Questions 9–10) | 15 |
| Part 5 — Chain of custody documentation | 10 |
| **Total** | **100** |

---

*End of Lab — Module 12*
