# Discussion Forum: Module 11 — Incident Response for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Overview

This discussion forum builds applied judgment around incident response decision-making. Each scenario below presents a real-world IR dilemma that analysts face. You will select one scenario, post your initial analysis, and respond substantively to two peers who addressed different scenarios.

---

## Scenario A — The Triage Dilemma

Your SIEM fires a high-severity alert at 11:47 PM on a Friday. The alert indicates that a server in your DMZ has made 47 outbound connections to a flagged IP address over the past six hours. You begin triage and discover that the flagged IP belongs to a CDN provider used by several legitimate SaaS applications your company subscribes to. However, the volume of connections is three times higher than baseline, and two of the connections transferred unusually large payloads. Your playbook does not explicitly cover this scenario. Your senior analyst is on vacation.

In 175–225 words, address the following: What is your triage determination — true positive, false positive, or inconclusive — and what specific evidence tips your judgment? What is the single most important next action you would take before the end of your shift, and why? How should the absence of a matching playbook and unavailable senior analyst affect your decision-making process?

---

## Scenario B — The Containment Tradeoff

Your organization has confirmed a compromise of a domain controller. Forensic analysis is underway and the IR team lead wants to preserve the system in its current state to collect volatile memory artifacts. However, the domain controller is actively serving authentication requests for 400 users, and HR has flagged that payroll processing runs in 90 minutes and requires AD authentication. Isolating the DC immediately will disrupt payroll. Delaying isolation keeps a confirmed compromised system online.

In 175–225 words, address the following: What factors must be weighed before making the isolation decision? Who should make the final call, and what information should the analyst provide to that decision-maker? Is there a technical middle-ground option that partially addresses both concerns? Describe one specific risk of delaying isolation and one specific risk of immediate isolation.

---

## Scenario C — The Lessons Learned Failure

Your organization experienced a significant ransomware incident six months ago. A formal lessons learned meeting was held and produced 11 action items, including deploying network segmentation, enabling PowerShell script block logging, and restricting RDP access. You are now investigating a new ransomware incident and discover that the attacker used the exact same initial access technique as the previous incident — and that 8 of the 11 action items were never implemented.

In 175–225 words, address the following: What does this pattern indicate about the organization's IR program maturity? What specific failure in the Post-Incident Activity phase allowed this recurrence? As the analyst investigating the new incident, how should you communicate this finding to management, and what risk does raising it create for your professional relationships? What structural change would most effectively prevent this failure mode in future incidents?

---

## Posting Instructions

**Initial Post:** Due Wednesday at 11:59 PM. Select one scenario. Write 175–225 words directly addressing all questions in the prompt. Use correct IR terminology. Reference NIST SP 800-61 or CySA+ concepts where applicable.

**Peer Responses:** Due Sunday at 11:59 PM. Reply to at least two classmates who addressed different scenarios from yours. Each reply must be at least 75 words and add substantive value — extend the analysis, respectfully challenge an assumption, or offer an alternative approach grounded in course content.

---

## Discussion Rubric — 10 Points Total

### Initial Post — 6 Points

- 5–6 pts: Addresses all scenario questions with technical accuracy, correct IR terminology, and clear reasoning. Word count within range. References course frameworks (NIST 800-61, CySA+ concepts).
- 3–4 pts: Addresses most scenario questions but lacks depth, technical precision, or framework references.
- 1–2 pts: Addresses the scenario only superficially or misses key questions.
- 0 pts: No initial post submitted.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies (75+ words each) to classmates on different scenarios. Replies extend analysis, challenge assumptions, or contribute alternative perspectives grounded in course content.
- 2–3 pts: One substantive reply, or two replies that are superficial (agreement without added analysis).
- 1 pt: Replies present but below minimum length or quality threshold.
- 0 pts: No peer responses submitted.
