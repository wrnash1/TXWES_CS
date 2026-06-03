# Discussion Forum: Module 12 — Digital Forensics and Post-Incident Analysis

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Overview

This discussion forum asks you to engage critically with the real-world application of digital forensics and post-incident analysis concepts. You will choose one of three scenarios below and write a 175–225 word original response in complete sentences (no bullet points). You will then write two peer responses of at least 60 words each, responding to classmates who addressed different scenarios than you. Each peer response must engage substantively with your classmate's argument — do not simply agree or summarize.

---

## Scenario A — The Rushed Investigation

A regional hospital experienced a ransomware attack on a Saturday morning. The CISO, under pressure from hospital leadership to restore operations as quickly as possible, directed the IT team to wipe and rebuild all affected servers immediately. No forensic images were created, no memory dumps were captured, and no chain of custody documentation was prepared. The CISO's reasoning was that patient care took priority over any investigation. Three weeks later, the hospital's cyber insurance carrier denied the claim, stating that the organization could not demonstrate what data was accessed or provide evidence of the attack's origin, as required by the policy terms. The hospital now faces potential HIPAA regulatory action and cannot determine whether a reportable breach of protected health information occurred.

Write a 175–225 word response in complete sentences addressing the following: Was the CISO's decision reasonable given the patient care emergency, or does it represent a governance failure? What should the CISO have done differently, and how could the organization have balanced the need for rapid recovery with the obligation to preserve evidence? Reference at least one specific forensic principle or procedure from Module 12 in your answer.

---

## Scenario B — The Incomplete After-Action Report

Meridian Technologies suffered a business email compromise attack in which an attacker impersonated the CFO and directed a finance employee to wire $2.1 million to a fraudulent account. The security team conducted a thorough investigation, produced a 34-page after-action report, and presented it to the board three weeks after the incident. The report contained an excellent timeline, strong technical findings, and detailed root cause analysis tracing the vulnerability to a lack of multi-factor authentication on executive email accounts. However, the report's recommendations section listed only general areas for improvement — "strengthen email security," "improve employee training," "implement MFA" — with no assigned owners, no due dates, and no success criteria. The board accepted the report and considered the matter closed. Fourteen months later, a nearly identical business email compromise attack succeeded at Meridian.

Write a 175–225 word response in complete sentences addressing the following: Why did a technically strong after-action report fail to prevent recurrence? What specific governance mechanisms should have been in place to ensure the recommendations were implemented and verified? Drawing on Module 12 content, explain what a properly structured recommendations section should contain and how accountability should be enforced.

---

## Scenario C — The Root Cause Debate

Two members of a financial services firm's security team are debating the root cause of a recent data breach. The breach occurred when an attacker used valid VPN credentials stolen through a phishing campaign to access the firm's internal network and exfiltrate client data over 11 days. Sarah, the threat intelligence analyst, argues that the root cause is the phishing campaign itself — the attacker's technique was the cause, and the solution is better email filtering and user training. Marcus, the security architect, argues that the root cause is the firm's failure to implement multi-factor authentication on VPN access — if MFA had been required, stolen credentials alone would not have been sufficient for the attacker to gain access. The CISO must decide which root cause to prioritize in the after-action report and corresponding remediation plan.

Write a 175–225 word response in complete sentences addressing the following: Who presents the stronger root cause argument, Sarah or Marcus, and why? How does the Five Whys technique help resolve this kind of disagreement? Is it possible for an incident to have multiple simultaneous root causes, and if so, how should the after-action report and remediation plan address them? Support your answer with concepts from Module 12.

---

## Peer Response Requirements

After posting your original response, write two peer responses meeting the following criteria.

- Each response must be at least 60 words
- Each response must address a classmate who responded to a different scenario than the one you chose
- Responses must engage substantively with your classmate's argument — pose a follow-up question, offer a counterargument, extend their reasoning with an additional example, or respectfully challenge an unsupported claim
- Responses that only agree, summarize, or offer praise without substantive engagement will not receive full credit

---

## Grading Rubric

| Criterion | Excellent (9–10) | Proficient (7–8) | Developing (5–6) | Insufficient (0–4) | Points |
|---|---|---|---|---|---|
| Content accuracy | Response demonstrates thorough command of forensic or post-incident concepts; all claims are accurate and well-supported | Response is mostly accurate with minor errors or omissions | Response contains some accurate content but also significant gaps or misconceptions | Response is largely inaccurate or does not engage with module concepts | 30 |
| Depth of analysis | Response moves beyond surface-level description to analyze implications, trade-offs, and governance significance | Response includes some analysis beyond description | Response is primarily descriptive with limited analytical depth | Response is purely descriptive or restates scenario without analysis | 25 |
| Use of module concepts | Response explicitly references and correctly applies at least one specific concept, principle, or framework from Module 12 | Response references module content but application is surface-level | Response mentions module content without demonstrating understanding | Response makes no reference to module concepts | 20 |
| Writing quality | Complete sentences throughout; 175–225 words; clear, professional tone; no bullet points | Mostly complete sentences; near word count; generally clear | Some sentence fragments or bullets; significantly outside word count | Bullet points used; far outside word count; unclear writing | 15 |
| Peer responses | Two responses; both 60+ words; both engage substantively with different scenarios | Two responses; meets length; engagement somewhat surface-level | One response or both responses are very brief | No peer responses submitted | 10 |
| **Total** | | | | | **100** |

---

## Professor Nash Closing Note

The scenarios in this discussion are drawn from patterns I have seen repeatedly in professional practice. The hospital scenario, the incomplete recommendations, and the root cause debate are not hypothetical edge cases — they are among the most common governance failures in post-incident analysis.

What I find most instructive about these scenarios is that none of them represent technical failures. The hospital had IT staff. Meridian had skilled investigators. The financial firm had a capable security team. The failures were governance failures — the absence of policy, process, accountability structure, and strategic thinking before and after incidents occurred.

As information security managers, your job is not only to respond to incidents technically. Your job is to ensure that your organization learns from every incident, protects its legal position, and emerges with stronger controls than it had before. The after-action report is not paperwork. It is your most important deliverable in the aftermath of any serious incident.

I look forward to reading your perspectives this week.

— Professor Nash
