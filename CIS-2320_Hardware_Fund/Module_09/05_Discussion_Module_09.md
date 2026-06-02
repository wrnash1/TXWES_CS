# Discussion Forum: Module 09 - Peripheral Devices and Interfaces

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.2 and Domain 1.2
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

## Overview

This discussion asks you to apply peripheral interface and authentication concepts to realistic deployment and troubleshooting scenarios. You will select one scenario below, answer all three sub-questions, and then engage substantively with two classmates who chose different scenarios.

Choose one scenario (A, B, or C). Write your initial post addressing all three sub-questions in 175-225 words total.

---

## Scenario A — The USB Speed Mystery

A graphic design firm recently upgraded all workstations to new laptops. The IT technician noticed that a USB 3.0 external SSD used for transferring large project files is copying at only 30-35 MB/s on the new laptops, the same speed it achieved on the old desktops. The new laptops have USB-C ports only. The technician is using a USB-A to USB-C adapter to connect the old USB 3.0 drive.

Address all three of the following:

1. Explain the most technically likely reason the drive is not achieving USB 3.0 speeds (300+ MB/s) on the new laptops, even though both the laptops and the drive are theoretically USB 3.0 capable. Focus specifically on the adapter and port characteristics involved.

2. What is the correct way to confirm which USB version a specific USB-C port on a laptop actually supports, since the connector shape alone does not reveal this? Describe at least two methods a technician could use to verify the port's actual capability.

3. What is the recommended long-term solution for this firm to achieve full USB 3.0 speeds when connecting their existing USB-A external drives to the new USB-C laptops, and what should they look for when purchasing the necessary accessory?

---

## Scenario B — The KVM Switch Rollout

A university IT department is rolling out KVM switches across 15 faculty offices. Each office will have one 4K monitor, one keyboard, and one mouse shared between a personal Windows laptop (brought in by the faculty member) and a university-issued Windows desktop. The IT director asks the department's junior technician to document the setup procedure and prepare answers to expected faculty questions.

Address all three of the following:

1. A faculty member asks: "If I switch to the university desktop while a large file is uploading on my personal laptop, will the upload be interrupted?" Write a technically accurate 3-4 sentence explanation of how KVM switching affects — or does not affect — processes running on a computer that has been switched away from.

2. After rollout, three faculty members report that when they switch to their personal laptop, the monitor shows a blank screen, but switching to the university desktop works correctly in all three offices. The KVM switches, monitors, keyboards, and mice are all identical across all offices. What is the single most likely explanation for why these specific three offices have the same fault on the same computer type, and what is the first physical check a technician should perform?

3. A faculty member in one of the affected offices says their laptop uses HDMI while the KVM switch uses DisplayPort. They connected the laptop using an HDMI-to-DisplayPort adapter. Explain whether this is a valid troubleshooting finding and what the recommended resolution is.

---

## Scenario C — The Enterprise Authentication Upgrade

A mid-sized financial services company currently uses only username and password for workstation authentication. After a security audit, the auditor recommends implementing multi-factor authentication using a "something you have" factor for all 200 workstations. The IT manager is evaluating two options: issuing smart cards with USB smart card readers, or issuing hardware TOTP tokens (time-based one-time password devices that display a 6-digit code every 30 seconds).

Address all three of the following:

1. Both smart cards and hardware TOTP tokens represent the "something you have" authentication factor. Explain the key operational difference between the two in terms of how authentication actually works at the workstation level — specifically, what hardware peripheral is required at each workstation for each option, and how the user interacts with it during login.

2. The IT manager asks whether adding a biometric factor in the future would change the MFA factor category. Explain what factor category biometrics represent, and describe what hardware peripheral would be needed at each workstation to enable fingerprint-based login alongside the existing password, and whether this would qualify as true multi-factor authentication.

3. One department handles extremely sensitive client data and has been told their workstations must use "something you have" plus "something you are" — no password required. Design a two-factor authentication solution for this department that satisfies both requirements. Identify the specific peripherals needed at each workstation and explain why this combination satisfies both factor categories without a password.

---

## Discussion Rubric (10 Points Total)

**Initial Post — 6 Points (due Wednesday at 11:59 PM)**

- 5-6 pts: All three sub-questions answered with technical accuracy. Response uses correct terminology (USB version names and speeds, MFA factor categories, specific connector and peripheral names). Stays within 175-225 words. Demonstrates understanding beyond surface-level definitions.
- 3-4 pts: Two of three sub-questions adequately addressed, or all three addressed with surface-level explanations that lack technical specificity.
- 1-2 pts: Only one sub-question addressed, or significant technical inaccuracies present.
- 0 pts: No initial post submitted.

**Peer Responses — 4 Points (due Sunday at 11:59 PM)**

Respond to at least two classmates who chose different scenarios from yours. Each response must be at least 75 words and do one of the following: correct a technical inaccuracy respectfully with supporting reasoning, add a meaningful technical detail or real-world context they did not mention, describe how you would handle their scenario differently and explain why, or raise a follow-up question that pushes the technical discussion deeper.

- 4 pts: Two substantive responses meeting the criteria above, each at least 75 words.
- 2 pts: One substantive response, or two responses that are generic without added technical content.
- 0 pts: No peer responses submitted.

---

*Professor Nash — Texas Wesleyan University*
*Peripheral and interface questions on the A+ exam are almost always scenario-based. The skills you practice in this discussion — reading a situation carefully, identifying the specific technical principle at stake, and explaining your reasoning — are exactly the skills the exam is testing.*
