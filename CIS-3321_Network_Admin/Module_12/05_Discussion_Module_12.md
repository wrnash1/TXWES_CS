# Discussion: Module 12 — Wide Area Networks

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Overview

This discussion asks you to apply Module 12 WAN concepts to realistic enterprise scenarios. Strong posts demonstrate technical depth, reference specific technologies from the lectures, and engage thoughtfully with the trade-offs involved in WAN design decisions.

**Due:** See course calendar.

**Grading:** Initial post (60 points) + two peer replies (20 points each) = 100 points.

---

## Prompt A — Required for All Students

### WAN Technology Selection

A regional healthcare company has 12 clinic locations across three Texas cities (Fort Worth, Dallas, Dallas suburbs). They are redesigning their WAN with these requirements:

- Electronic Health Record (EHR) system must be highly responsive — maximum acceptable one-way latency: 20 ms
- HIPAA requires that all patient data in transit be encrypted
- VoIP between clinics — approximately 30 concurrent calls per clinic
- Monthly budget for WAN: $8,000 total across all locations
- The company currently uses MPLS at $900/month per location (12 locations = $10,800/month)

Evaluate at least two WAN technology options (from MPLS, SD-WAN, broadband fiber, Metro Ethernet, cellular, or a hybrid approach) and recommend a design. Your recommendation must:

- Address the latency and encryption requirements
- Estimate whether the $8,000 budget is achievable
- Identify one significant risk of your recommended approach

Your initial post should be 275–375 words and must cite specific technologies and concepts from Module 12.

---

## Prompt B — Choose One

### Option 1: MPLS vs. SD-WAN Debate

Your company is debating whether to renew its MPLS contract or migrate to SD-WAN. The network manager prefers MPLS because "it's proven, reliable, and the carrier handles everything." You believe SD-WAN is the better long-term direction.

Write a response to the network manager that: (a) acknowledges the legitimate advantages of MPLS the manager cited, (b) presents three specific technical advantages of SD-WAN for a cloud-first environment, and (c) proposes a migration strategy that reduces risk (hint: consider a hybrid approach during transition). Reference specific SD-WAN capabilities from the module.

### Option 2: Remote Site Connectivity

You are the network architect for an oil and gas company. You have three types of remote sites:

- Offshore drilling platforms (no terrestrial connectivity possible)
- Remote land-based drilling sites in west Texas (cellular available, no fiber)
- Urban office in Houston (all options available)

For each site type, recommend a WAN technology, justify your choice based on bandwidth, latency, cost, and availability requirements, and identify the biggest reliability concern. Which site type presents the greatest networking challenge and why?

### Option 3: WAN Optimization Business Case

Your manager asks you to justify a $45,000 WAN optimization appliance purchase. The current situation: the company has a 10 Mbps MPLS link between headquarters and a branch office. Branch users complain that file transfers take 45 minutes for files that take 2 minutes on the LAN. The branch performs 500 GB of nightly backups over the WAN.

Build a business case: explain what WAN optimization technique addresses each problem (slow file transfers, slow backups), estimate the performance improvement that deduplication might provide for the nightly backup, and calculate the equivalent bandwidth increase that would cost the same $45,000 annually via MPLS bandwidth upgrade (assume MPLS upgrade from 10 to 20 Mbps = $800/month additional).

---

## Peer Reply Guidelines

Reply to two classmates who chose different prompts or reached different conclusions than you. Each reply must:

- Be at least 100 words
- Engage with a specific technical claim in their post
- Either provide a counter-example, add a relevant technical consideration, or share supporting or contradicting real-world context

Replies that only say "I agree" or simply restate the original post will not receive credit.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Technical accuracy — correct WAN concepts and terminology | 25 |
| Depth of analysis — addresses trade-offs not just features | 20 |
| Scenario application — all parts of the chosen prompts addressed | 15 |
| Peer Reply 1 — substantive technical engagement | 20 |
| Peer Reply 2 — substantive technical engagement | 20 |
| Total | 100 |
