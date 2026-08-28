# Lab: Module 11 — Incident Response

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

**Title:** Tabletop Incident Response Exercise — Ransomware Scenario

**Duration:** Approximately 75 minutes

**Environment:** No special software required — this is a structured analytical exercise using the provided scenario

**Skill Level:** Intermediate — requires completion of Module 11 video lectures and Reading Guide

---

## Objectives

Upon completing this lab, you will be able to:

1. Apply the NIST SP 800-61 incident response lifecycle phases to a real-world scenario
2. Identify appropriate containment, eradication, and recovery actions for a ransomware incident
3. Apply the order of volatility to prioritize evidence collection decisions
4. Construct a chain of custody entry for identified evidence
5. Document a communications plan for internal and external stakeholders
6. Produce an abbreviated post-incident lessons learned report

---

## Background: What Is a Tabletop Exercise?

A tabletop exercise is a discussion-based simulation in which participants work through a hypothetical incident scenario, applying their knowledge of IR procedures without actually deploying technical tools. Tabletops are one of the primary preparation activities specified in NIST SP 800-61. They reveal gaps in plans, training, and team coordination before a real incident exposes them.

In this lab, you are playing the role of the Incident Response Analyst responsible for leading the response. Work through each section, documenting your decisions and rationale.

---

## Scenario: Ransomware at Meridian Financial Services

**Organization Background:** Meridian Financial Services is a mid-sized regional bank with approximately 800 employees across 12 branch locations. They operate a hybrid environment: on-premises Active Directory, a core banking system on physical servers, and Microsoft 365 for email and collaboration. Their security team consists of three full-time security analysts and a CISO who reports to the CTO.

**Monday, 7:14 AM:** The branch manager at the downtown location calls the IT help desk. He reports that when he arrived this morning, every workstation displays a ransom note. The ransom note states that all files have been encrypted, demands 15 Bitcoin (~$450,000 at current price), and threatens to publish "sensitive customer financial records" on a dark web site in 72 hours if payment is not received.

**7:22 AM:** The help desk escalates to the security team. Analyst Jordan arrives and confirms that the ransom note is also visible on the file server in the downtown branch server room.

**7:35 AM:** Jordan runs a quick scan and finds three other branch locations are showing similar symptoms. The core banking system — located in the primary data center — appears to be operational, but Jordan cannot confirm for how long.

---

## Part 1 — Detection and Analysis (15 minutes)

### Task 1.1 — Incident Triage

Based on the information provided:

**1a.** What evidence indicates this is a ransomware incident rather than a false alarm? List at least three observable indicators.

**1b.** Using NIST SP 800-61's incident prioritization criteria, assign an initial severity level to this incident. Your answer must address all three criteria: functional impact, information impact, and recoverability. Justify each choice.

**1c.** What additional information do you need to complete your analysis? List at least five specific questions you would want answered in the first 30 minutes, and for each question, identify where you would look for the answer.

### Task 1.2 — Evidence Identification

The following systems and artifacts have been identified as potentially relevant to the investigation. Using the order of volatility, rank them from MOST volatile to LEAST volatile and explain why each item falls where it does in your ranking:

- Ransom note displayed on employee monitor
- RAM contents of an infected workstation that is still powered on
- Windows Event Logs on the file server (stored on disk)
- Active network connections from an infected workstation
- Backup tapes stored in the offsite facility
- The running process list on the infected file server
- A USB drive found near the server room door

---

## Part 2 — Containment Decisions (15 minutes)

### Task 2.1 — Short-Term Containment

At 7:40 AM, you have confirmed ransomware on at least four branch locations. The core banking system is still operational.

**2a.** List your immediate containment actions in priority order. For each action, state:

- The specific action (e.g., "disconnect VLAN 10 from the core network at the main distribution switch")
- The rationale (why this action now)
- The potential risk or downside of this action

**2b.** The CTO calls at 7:45 AM and asks you to "shut everything down immediately including the core banking system to be safe." Evaluate this request. Should you comply? What risks does immediate shutdown of the core banking system create? What is your recommendation?

### Task 2.2 — Evidence Preservation Before Containment

Before powering off any infected systems, identify what evidence you would capture. For each item:

- Name the evidence
- Describe how you would collect it
- State why it is important to collect before shutdown

Your answer must address volatile memory, running process information, and network connections.

### Task 2.3 — Chain of Custody Entry

You collect a forensic image of the hard drive from an infected workstation at the downtown branch. Complete the chain of custody entry below:

| Field | Your Entry |
|---|---|
| Evidence ID | |
| Description | |
| Collection date/time | |
| Collection location | |
| Collected by (use your name) | |
| MD5 hash (use this simulated value: `a3b8c1d7e2f4a9b0c5d6e7f8a1b2c3d4`) | |
| SHA-256 hash (use this simulated value: `e3b0c44298fc1c149afbf4c8996fb924...`) | |
| Transfer 1: transferred to | |
| Transfer 1: date/time | |
| Storage location | |

---

## Part 3 — Communication Plan (15 minutes)

### Task 3.1 — Internal Communication

**3a.** List all internal stakeholders who must be notified of this incident in the first two hours. For each stakeholder, state: their role, when they are notified, what information is shared, and what you need from them.

**3b.** The attackers claim they will publish customer financial records in 72 hours. An employee posts about the incident on their personal Twitter/X account: "major ransomware attack at work, bank systems down, hope customer data is safe!" How do you respond to this? What communication controls in the IR plan should have prevented this?

### Task 3.2 — External Communication

**3c.** As a bank, Meridian Financial Services is regulated by multiple agencies. Identify at least two regulatory bodies or legal requirements that may impose breach notification obligations in this scenario. For each, state the potential notification deadline and what must be disclosed.

**3d.** Draft a brief customer notification (three to five sentences) for the bank's website assuming you have confirmed that customer data has NOT been exfiltrated but branch banking systems are temporarily unavailable.

---

## Part 4 — Eradication and Recovery (10 minutes)

### Task 4.1 — Eradication Steps

At 2:00 PM on Monday, the security team has identified the attack vector: a phishing email received by a branch employee on Friday afternoon. The employee clicked a malicious link that downloaded a dropper, which then spread laterally over the weekend using stolen administrator credentials.

List your eradication steps in order. Address: removing malware, addressing the attack vector, handling compromised credentials, and closing the vulnerability that allowed lateral movement.

### Task 4.2 — Recovery Prioritization

The following systems need to be restored. Rank them in order of restoration priority and explain your reasoning for each:

- Branch workstations (affected by ransomware)
- Branch file server (encrypted)
- Core banking system (currently operational but at risk)
- Email system
- ATM network (currently down due to containment network isolation)
- Customer-facing online banking portal

---

## Part 5 — Post-Incident Lessons Learned (20 minutes)

### Task 5.1 — Lessons Learned Meeting Agenda

It is now two weeks after the incident. Draft an agenda for the lessons learned meeting. Include at least five agenda items, a timeframe for each, and the appropriate participants for each agenda item.

### Task 5.2 — Root Cause Analysis

Using the "five whys" technique, document the root cause analysis for this incident. Start from the immediate cause (ransomware executed on an employee workstation) and drill down to the underlying organizational failure. Show at least five levels.

### Task 5.3 — Incident Report Executive Summary

Write a one-page executive summary (approximately 300 words) of this incident suitable for presentation to the board of directors. It must be non-technical, include the business impact, and end with three specific recommendations.

---

## Lab Report Submission Requirements

Submit a single document containing all completed tasks. Label each task clearly.

**Format:** PDF or Word document

**Minimum length:** 800 words excluding tables and lists

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Triage and evidence ranking | 20 |
| Part 2 — Containment decisions, evidence preservation, chain of custody | 25 |
| Part 3 — Communication plan (internal and external) | 20 |
| Part 4 — Eradication and recovery prioritization | 15 |
| Part 5 — Lessons learned agenda, root cause, executive summary | 20 |
| **Total** | **100** |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 11*
