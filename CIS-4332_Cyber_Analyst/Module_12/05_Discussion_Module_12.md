# Discussion Forum: Module 12 — Digital Forensics for Security Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Overview

This discussion explores the practical and ethical dimensions of digital forensics work. Each scenario presents a situation where forensic principles, technical decisions, and professional judgment intersect. Select one scenario, post your initial analysis, and respond to two peers who addressed different scenarios.

---

## Scenario A — The Evidence Preservation Dilemma

You are an analyst responding to a confirmed ransomware incident at a hospital. Two servers are actively encrypting patient record files. You have the capability to immediately isolate both servers from the network, which would stop the encryption but destroy volatile memory evidence — including the encryption keys that might allow decryption of already-encrypted files without paying the ransom. Your incident manager is unreachable. The IR playbook says "isolate immediately on confirmed ransomware," but it was written before your forensic team acquired memory capture capability.

In 175–225 words, address the following: How do you weigh the business impact of continued encryption against the potential value of the memory evidence? Does the healthcare context change your calculus compared to, say, a retail company? What specific volatile evidence would you attempt to capture in the time available before isolation, and in what order? After the incident, what playbook update would you recommend to prevent this dilemma from recurring?

---

## Scenario B — Chain of Custody Under Pressure

You collect a memory image from a compromised executive's laptop at 09:15. You hash the image and place it on a shared investigative network drive. At 11:30 your manager tells you the company's outside legal counsel needs a copy immediately for a potential litigation hold — they want you to email it directly to the attorney. You know that emailing a 16 GB raw memory image is technically impractical, but the manager says "figure it out." A colleague suggests using a consumer cloud storage link to share it. You also realize you forgot to document the 11:30 transfer in the chain of custody log.

In 175–225 words, address the following: What are the specific chain of custody violations that have occurred or are at risk of occurring here? What is the correct procedure for transferring forensic evidence to outside legal counsel? How do you handle the pressure from your manager while maintaining forensic integrity? What documentation must you create retroactively, and can retroactive documentation repair a chain of custody gap?

---

## Scenario C — The Anti-Forensics Discovery

You are analyzing a disk image from a suspected insider threat case. During timeline reconstruction using Autopsy, you notice that dozens of files in the suspect's home directory all have MACB timestamps of January 1, 2001 — clearly impossible given the OS was installed in 2023. You also find that the Windows Security event log has zero entries before the day the suspect was terminated, and the System event log has Event ID 1102 at 16:42 on the final day of employment.

In 175–225 words, address the following: What two distinct anti-forensic techniques has the suspect apparently used? What forensic evidence might still survive despite these cleanup efforts? If the `$FILE_NAME` MFT attribute timestamps differ from the `$STANDARD_INFORMATION` timestamps, what does this discrepancy prove? How would you document these anti-forensic findings in your investigation report in a way that is factual, defensible, and useful to legal counsel?

---

## Posting Instructions

**Initial Post:** Due Wednesday at 11:59 PM. Select one scenario. Write 175–225 words directly addressing all questions. Use correct forensics terminology. Reference course concepts (order of volatility, chain of custody, MFT attributes, anti-forensic techniques) where applicable.

**Peer Responses:** Due Sunday at 11:59 PM. Reply to at least two classmates who chose different scenarios from yours. Each reply must be at least 75 words and add substantive value — extend the analysis, challenge an assumption respectfully, or offer an alternative approach grounded in course content.

---

## Discussion Rubric — 10 Points Total

### Initial Post — 6 Points

- 5–6 pts: Addresses all scenario questions with technical accuracy, correct forensics terminology, and clear reasoning. Word count within range. References course frameworks.
- 3–4 pts: Addresses most questions but lacks depth or technical precision.
- 1–2 pts: Superficial treatment of the scenario or misses key questions.
- 0 pts: No initial post submitted.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies (75+ words each) to classmates on different scenarios. Replies add analysis, challenge assumptions, or provide alternative perspectives grounded in course content.
- 2–3 pts: One substantive reply, or two replies that are superficial.
- 1 pt: Replies present but below length or quality threshold.
- 0 pts: No peer responses submitted.
