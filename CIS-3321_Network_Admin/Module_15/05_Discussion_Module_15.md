# Discussion: Module 15 — Network Documentation and Policies

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Overview

This discussion asks you to engage with the policy and documentation aspects of network administration — topics that matter enormously in professional practice but are sometimes undervalued in technical training. Strong posts demonstrate understanding of why these administrative disciplines exist and how they apply in realistic organizational contexts.

**Due:** See course calendar.

**Grading:** Initial post (60 points) + two peer replies (20 points each) = 100 points.

---

## Prompt A — Required for All Students

### Change Management Scenario

The following scenario describes a real-world situation. Read it carefully and analyze it through the lens of Module 15.

Scenario: At a regional bank, a network engineer receives a call from the branch manager on a Friday afternoon: "The credit card processing system is running slow. Can you do something?" Without opening a change request, the engineer makes three "quick" adjustments to the firewall rule set — removing a QoS policy that was throttling the card processing application, changing a NAT rule to reduce translation overhead, and disabling a logging policy to reduce processing load. The changes appear to work — the branch manager confirms the application feels faster. Over the weekend, the bank's intrusion detection system generates 47 security alerts from what appears to be a port scan of the internal network. The security team investigates Monday morning and discovers the logging policy the engineer disabled would have captured the source of the intrusion — but the logs are now empty.

For your initial post, address all of the following:

- Which change management step(s) did the engineer violate, and specifically what should have been done instead?
- Which of the three changes represents the most significant risk, and why?
- How would a proper change request have protected both the bank and the engineer personally?
- What change type (standard, normal, or emergency) was appropriate for this scenario and why?

Your post should be 300–400 words and reference specific change management concepts from Module 15.

---

## Prompt B — Choose One

### Option 1: DR Plan for a Small Business

You are the part-time IT consultant for a 25-person accounting firm. The owner asks you to design a basic disaster recovery plan. The firm's critical systems are: QuickBooks Online (SaaS — no local installation), a local Windows file server with client tax files, and an on-premises email server (Microsoft Exchange).

Design a DR plan outline for this firm that:

- Assigns an RTO and RPO for each critical system with justification
- Recommends a DR site type for on-premises components
- Describes the backup strategy needed to meet the RPO for the file server
- Identifies the biggest gap in the current setup (hint: consider which systems are cloud-based vs. on-premises)
- Recommends one improvement the owner can implement for under $500/month that significantly improves resilience

### Option 2: SLA Negotiation

Your company is selecting a new primary ISP for its headquarters. Two vendors have submitted proposals:

- Vendor A: 500 Mbps dedicated fiber, 99.9% availability SLA, 4-hour MTTR, $1,200/month
- Vendor B: 1 Gbps dedicated fiber, 99.99% availability SLA, 2-hour MTTR, $2,400/month

Your network supports VoIP (150 concurrent calls), a cloud ERP system (production staff of 80), and video conferencing. There is no secondary internet circuit.

Analyze the two SLAs: (a) calculate the annual allowed downtime for each, (b) assess whether the 99.9% SLA is sufficient for your application mix without a backup circuit, (c) calculate the annual cost difference, and (d) make a recommendation — Vendor A, Vendor B, or a hybrid approach — with full justification. Reference specific SLA metrics from the module.

### Option 3: AUP Design

Your organization has no Acceptable Use Policy. You have been asked to draft one. The organization is a 200-person healthcare clinic that has HIPAA compliance obligations.

Draft the key sections of an AUP for this clinic (you do not need to write full legal language — use clear professional writing): (a) permitted use statement, (b) prohibited activities (include at least 5 specific items relevant to healthcare), (c) privacy and monitoring notice, (d) BYOD provisions, (e) consequences of violations. Explain which provision is most important for HIPAA compliance and why.

---

## Peer Reply Guidelines

Reply to two classmates who chose different prompts or who reached different conclusions. Each reply must:

- Be at least 100 words
- Engage with a specific argument or recommendation in their post
- Add a technical consideration they did not address, challenge an assumption, or provide a real-world example that supports or contradicts their conclusion

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Technical accuracy — correct documentation and policy concepts | 25 |
| Analytical depth — explains the reasoning behind recommendations | 20 |
| Scenario completeness — all required parts of the prompt addressed | 15 |
| Peer Reply 1 — substantive technical engagement | 20 |
| Peer Reply 2 — substantive technical engagement | 20 |
| Total | 100 |
