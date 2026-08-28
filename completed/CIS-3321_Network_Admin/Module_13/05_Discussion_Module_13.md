# Discussion: Module 13 — Unified Communications and Collaboration

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Overview

This discussion asks you to apply UC and VoIP concepts to real-world network design and troubleshooting scenarios. Strong posts demonstrate command of the technical content, show quantitative reasoning where appropriate, and engage honestly with trade-offs rather than just listing features.

**Due:** See course calendar.

**Grading:** Initial post (60 points) + two peer replies (20 points each) = 100 points.

---

## Prompt A — Required for All Students

### VoIP Quality Complaint Investigation

A school district has recently migrated from a traditional PBX phone system to a SIP-based VoIP system using Microsoft Teams Phone. After the cutover, the help desk receives the following complaints:

- Teachers report that calls with parents sound "choppy and cut out" — but only during 8–9 AM and 12–1 PM.
- The IT director says ping times to the Teams cloud servers are 25 ms — well within acceptable range.
- The school's WAN link is a 100 Mbps fiber circuit, and average utilization is reported at 65%.

Using Module 13 concepts, analyze the possible root causes. Your post must:

- Identify which VoIP quality metric is most likely causing the choppy audio, given that average latency appears acceptable.
- Explain why the problem occurs specifically at 8–9 AM and 12–1 PM (consider what those times represent in a school environment).
- Propose two specific technical remedies, referencing at least one QoS mechanism from the module.
- State what diagnostic tool or metric you would use to confirm your diagnosis.

Your initial post should be 275–350 words and cite specific concepts from the Module 13 lectures or reading guide.

---

## Prompt B — Choose One

### Option 1: QoS Design for a Call Center

A regional insurance company is building a new call center with 200 agent workstations, each running Microsoft Teams with active voice and video calls throughout the business day. The WAN connection to corporate headquarters is a 500 Mbps fiber link.

Design a QoS policy for this environment:

- Specify which DSCP values you would use for voice RTP, video, SIP signaling, and general data.
- Describe the queuing mechanism and explain why you chose it.
- Calculate the minimum WAN bandwidth that should be reserved for voice if all 200 agents are on simultaneous G.711 calls.
- Explain how Call Admission Control would be configured and what it would do if the WAN voice allocation is fully utilized.

### Option 2: SIP vs. H.323 Migration Decision

Your company operates an aging H.323-based video conferencing infrastructure with 15 conference rooms and 400 desk phones. The systems integrator recommends migrating to SIP. Your CTO asks for a technical briefing memo.

Write a 300–400 word technical memo that: (a) explains the key architectural differences between H.323 and SIP at the component level, (b) identifies three specific technical advantages of migrating to SIP, (c) describes one risk or complexity of the migration that the CTO should be aware of, and (d) recommends whether to migrate and on what timeline.

### Option 3: Cloud UCaaS vs. On-Premises UC

Your organization of 500 employees is deciding between two options for their UC replacement:

- Option A: Microsoft Teams Phone (cloud UCaaS) — $22/user/month, no on-premises hardware
- Option B: Cisco Unified Communications Manager (CUCM) on-premises — $180,000 upfront hardware/licensing, $15,000/year maintenance

Analyze both options over a 5-year total cost of ownership. Then evaluate: which option gives the network administrator more control over QoS, Voice VLAN design, and call quality? Which option is more appropriate if the organization has unreliable internet connectivity? Make a final recommendation with justification.

---

## Peer Reply Guidelines

Reply to two classmates who chose different prompts or reached different conclusions. Each reply must:

- Be at least 100 words
- Engage with a specific technical claim — provide a counter-example, add a consideration they missed, or validate their reasoning with additional evidence
- Avoid generic praise — engage with the substance of their technical argument

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Technical accuracy — correct use of UC/QoS concepts | 25 |
| Analytical depth — addresses root causes and trade-offs | 20 |
| Scenario completeness — all parts of chosen prompt addressed | 15 |
| Peer Reply 1 — substantive technical engagement | 20 |
| Peer Reply 2 — substantive technical engagement | 20 |
| Total | 100 |
