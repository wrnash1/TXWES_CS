# Lab Activity: Module 09 - Peripheral Devices and Interfaces

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.2 and Domain 1.2
**Total Points:** 100
**Submission:** Upload your completed lab document to the Canvas assignment portal before the due date.

---

## Overview

This lab has three parts. Part 1 tests your ability to identify USB connector types and USB versions from descriptions and specifications. Part 2 presents a KVM switch deployment scenario you must analyze and troubleshoot. Part 3 covers authentication peripheral selection and MFA factor classification.

No physical hardware is required to complete this lab, though if you have access to a PC you are encouraged to locate and examine physical ports as noted in the observation prompts.

---

## Part 1 — USB Version and Connector Identification (35 points)

### Part 1A — USB Version from Scenario Description (15 points)

Read each scenario and identify the USB version most likely involved. In the "Reasoning" column, explain in one sentence what evidence in the scenario points to that version. Use the USB version options: USB 2.0, USB 3.0 (SuperSpeed), USB 3.1 Gen 2 (SuperSpeed 10Gbps), Thunderbolt 3, Thunderbolt 4.

| Scenario | USB Version | Reasoning |
|---|---|---|
| A user copies a 10 GB file to an external flash drive and it completes in approximately 3 minutes. The port is white/black colored. | | |
| A user connects an external SSD to a blue-colored port and observes sustained transfer speeds of 400 MB/s. | | |
| A laptop has a port with a lightning bolt icon. The user connects a Thunderbolt dock and instantly gets two 4K displays, USB peripherals, and laptop charging from one cable. | | |
| A developer's workstation has a USB-C port. They connect an external NVMe enclosure and observe 900 MB/s read speeds — close to the theoretical maximum for that drive. | | |
| A new laptop advertises "Thunderbolt 4" on all USB-C ports. The user connects an eGPU enclosure and a 4K monitor simultaneously. Both work through the same cable to the Thunderbolt dock. | | |

### Part 1B — Connector Type Identification (10 points)

Match each connector description to its correct connector name. Write the connector name in the "Match" column.

Use these connector names: USB Type-A male, USB Type-A female, USB Type-B male, USB Micro-B male, USB Type-C male, USB Mini-B male

| Connector Description | Match |
|---|---|
| Small, trapezoidal, 5-pin connector; used on digital cameras and older MP3 players before approximately 2010 | |
| Flat, rectangular, wider-than-tall connector; blue-colored version; found on the device plugging into a USB 3.0 port on a hub | |
| Very small, asymmetric 5-pin connector with one slanted edge; used on smartphones from roughly 2010-2018 | |
| Small, square-profile connector with two beveled top corners; found on the printer-side end of a USB printer cable | |
| Small, oval-shaped, reversible connector that can be inserted either side up; found on modern smartphones and laptops | |
| Flat rectangular opening on a hub, PC case, or USB port; the "socket" side that accepts USB Type-A plugs | |

### Part 1C — Speed Conversion Exercise (10 points)

The A+ exam may express USB speeds in Gbps (gigabits per second) or MB/s (megabytes per second). Complete the table by converting each speed. Show your work in the "Conversion" column using the formula: Gbps / 8 = approximate GB/s.

| USB Version | Rated Speed (Gbps) | Approximate Theoretical Max (MB/s) | Realistic Sustained Speed Estimate (MB/s) | Conversion Work |
|---|---|---|---|---|
| USB 2.0 | 0.48 Gbps | | ~30-40 MB/s | |
| USB 3.0 | 5 Gbps | | ~300-400 MB/s | |
| USB 3.1 Gen 2 | 10 Gbps | | ~700-900 MB/s | |
| Thunderbolt 3/4 | 40 Gbps | | ~3,000-3,500 MB/s | |

Note: Theoretical maximum is the mathematical ceiling. Realistic sustained speed is lower due to protocol overhead, cable quality, and device limitations.

---

## Part 2 — KVM Switch Scenario Analysis (35 points)

### Scenario Setup

A small law firm has two attorneys who share a single office assistant. The office assistant's desk has one high-resolution monitor, one mechanical keyboard, and one mouse. They need to be able to control three separate computers from this one desk:

- Computer 1: Their own Windows 11 desktop for email and document drafting
- Computer 2: A Windows 10 machine running legal case management software that must remain on a separate, isolated machine per firm policy
- Computer 3: A Linux workstation used for secure file review

They purchase a 4-port KVM switch and connect all three computers. The KVM switch has one HDMI video input port per connected computer, one USB Type-B input port per computer (for keyboard/mouse), and one shared HDMI output to the monitor plus one shared USB Type-A hub output.

### Part 2A — Configuration Planning (10 points)

Answer the following setup questions:

**Question 2A-1:** How many HDMI cables are needed to fully cable this KVM switch configuration? List what each cable connects.

Your answer: ___________________________________________________________

**Question 2A-2:** How many USB cables are needed for keyboard/mouse routing? What type of USB connector is on the KVM switch side, and what type is on the PC side?

Your answer: ___________________________________________________________

**Question 2A-3:** The firm's IT policy specifies that Computer 2 must remain powered on at all times, even when the KVM is switched to Computer 1 or Computer 3. Is this compatible with KVM switch operation? Explain why or why not.

Your answer: ___________________________________________________________

**Question 2A-4:** One attorney asks whether the KVM switch will work because Computer 3 runs Linux and the other two run Windows. Write a 2-3 sentence response explaining KVM switch OS compatibility.

Your answer: ___________________________________________________________

### Part 2B — Troubleshooting Scenarios (25 points)

For each troubleshooting scenario below, identify the most likely cause and describe the correct diagnostic/resolution step. Each answer should be 2-4 sentences.

**Trouble Scenario 1:** After the KVM switch is installed, switching to Computer 2 produces a working keyboard and mouse but a blank monitor screen. Computer 2 is confirmed to be powered on and running.

Most likely cause and resolution: ___________________________________________________________

**Trouble Scenario 2:** The KVM switch toggles correctly between Computer 1 and Computer 2, but Computer 3 cannot be reached at all. Pressing the button or using the hotkey to select Computer 3 produces no change — the system stays on Computer 2.

Most likely cause and resolution: ___________________________________________________________

**Trouble Scenario 3:** After switching to Computer 1, the mouse pointer moves very slowly and the keyboard has a noticeable input delay. The same keyboard and mouse work at normal speed when directly connected to Computer 1 without the KVM switch.

Most likely cause and resolution: ___________________________________________________________

**Trouble Scenario 4:** The attorneys want to cut and paste text between Computer 1 and Computer 2. They assume the KVM switch clipboard integration handles this. After setup, they find they cannot copy text from Computer 1 and paste it into Computer 2.

Most likely cause and resolution: ___________________________________________________________

**Trouble Scenario 5:** The monitor is a 4K display. When connected directly to Computer 1, it displays at 3840x2160. After the KVM switch is installed, the maximum available resolution is 1920x1080.

Most likely cause and resolution: ___________________________________________________________

---

## Part 3 — Authentication Peripheral Selection and MFA Analysis (30 points)

### Part 3A — MFA Factor Classification (10 points)

Classify each authentication method below by its MFA factor category. Use: Something you know, Something you have, Something you are.

| Authentication Method | MFA Factor Category |
|---|---|
| 8-character password containing letters and numbers | |
| Fingerprint scan on a laptop touchpad | |
| Physical hardware token that generates a 6-digit code every 30 seconds | |
| Iris scan camera embedded in a laptop bezel | |
| U.S. Department of Defense Common Access Card (CAC) inserted into a USB reader | |
| 4-digit PIN typed at a Windows login screen | |
| Facial recognition via infrared depth camera (Windows Hello) | |
| Smart card with embedded cryptographic chip issued by corporate IT | |

### Part 3B — Peripheral Selection Scenarios (20 points)

For each deployment scenario below, identify the correct authentication peripheral, state which MFA factor it represents, and write 2-3 sentences explaining why it is the appropriate choice. Peripheral options: USB fingerprint reader, USB smart card reader, iris scanner, facial recognition camera.

**Deployment Scenario 1:** A hospital requires nurses to authenticate to medication dispensing terminals quickly while wearing gloves. The hospital's IT policy requires two-factor authentication: a physical credential and a biometric factor. The gloves prevent fingerprint scanning.

Peripheral selection: ___________________________________________________________

MFA factor: ___________________________________________________________

Justification: ___________________________________________________________

**Deployment Scenario 2:** A federal agency requires all employees to authenticate to their Windows workstations using government-issued PIV credentials. The agency's security policy requires "something you have" authentication tied to a cryptographic certificate stored on the credential itself.

Peripheral selection: ___________________________________________________________

MFA factor: ___________________________________________________________

Justification: ___________________________________________________________

**Deployment Scenario 3:** A software company wants to enable hands-free workstation login for developers. Developers should be automatically recognized and logged in when they sit down at their assigned workstation without touching any device or typing any credential.

Peripheral selection: ___________________________________________________________

MFA factor: ___________________________________________________________

Justification: ___________________________________________________________

**Deployment Scenario 4:** A financial trading firm requires traders to log in to their terminals in under 3 seconds without removing their hands from their keyboards. The fastest possible authentication that qualifies as "something you are" is required.

Peripheral selection: ___________________________________________________________

MFA factor: ___________________________________________________________

Justification: ___________________________________________________________

---

## Deliverables and Submission

Submit one document containing all of the following:

1. Part 1A — USB version identification table with reasoning column complete (5 rows)
2. Part 1B — Connector type matching table complete (6 rows)
3. Part 1C — Speed conversion table with conversion work shown (4 rows)
4. Part 2A — Four configuration planning answers
5. Part 2B — Five troubleshooting scenario responses (2-4 sentences each)
6. Part 3A — MFA factor classification table complete (8 rows)
7. Part 3B — Four peripheral selection scenarios answered with peripheral, factor, and justification

Accepted formats: PDF, DOCX, or Google Docs link with comment access enabled.

---

## Grading Rubric

| Section | Points Possible | Criteria |
|---|---|---|
| Part 1A — USB Version Scenarios | 15 | Each of 5 rows: correct version (2 pts) + accurate one-sentence reasoning (1 pt) |
| Part 1B — Connector Matching | 10 | 2 points each for all 6 connectors correctly matched (10 pts total; partial credit: 1 pt for close but incorrect connector name) |
| Part 1C — Speed Conversion | 10 | 2.5 pts each row: correct theoretical max calculated, conversion work shown |
| Part 2A — KVM Configuration | 10 | 2.5 pts each: cable counts correct, OS compatibility question answered accurately with reference to KVM hardware-agnostic operation |
| Part 2B — KVM Troubleshooting | 25 | 5 pts each scenario: correct root cause identified; resolution is specific and actionable (not generic "check cables") |
| Part 3A — MFA Classification | 10 | 1.25 pts each row; all 8 rows must correctly assign factor category |
| Part 3B — Peripheral Selection | 30 | 7.5 pts each scenario: correct peripheral named (2.5 pts), correct MFA factor stated (2.5 pts), justification 2-3 sentences addressing scenario-specific constraints (2.5 pts) |
| **Total** | **100** | |

---

## Reference Notes

If you are uncertain about a USB speed or connector type, the Reading Guide Section 1-2 tables provide complete reference information. For KVM troubleshooting, Section 4 of the Reading Guide includes a troubleshooting table. For MFA factor categories, Section 5 includes the complete factor classification table.

Do not cite fabricated URLs. Base all answers on module content and professormesser.com or comptia.org if additional reference is needed.
