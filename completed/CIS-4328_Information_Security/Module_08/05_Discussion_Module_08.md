# Discussion Forum — Module 08: Endpoint Security

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This discussion applies Module 08's endpoint security concepts to real-world organizational decisions — specifically the tension between security effectiveness and operational reality, and the rapidly evolving endpoint threat landscape that is outpacing traditional protection models.

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM

**Minimum Participation:** One original post (250–350 words) and two substantive replies (100+ words each).

---

## Scenario A — The Patch Management Dilemma

A large utility company operates industrial control systems (ICS) that manage power grid infrastructure. These systems run embedded Windows operating systems and cannot be patched during regular operations — any maintenance requires a six-to-twelve-hour planned outage, and production schedules only allow two planned outages per year. The company's IT team has identified 47 critical and high-severity vulnerabilities across these systems, four of which are on the CISA KEV catalog.

Patching is genuinely difficult: the vendor for one of the systems no longer exists, and no patches are available at any price. For another system, the vendor's patch breaks a critical monitoring function that the company's engineers have not been able to resolve.

In 250–350 words, respond to all three of the following:

1. For the four CISA KEV vulnerabilities that cannot be immediately patched, what compensating controls would you implement? Be specific — name the control type, describe the mechanism, and explain how it reduces risk without patching. Use terminology from Module 07 (network architecture) and Module 08 (endpoint security).

2. One system has a vendor who is no longer in business and no patch is available. What does this represent in terms of vulnerability classification, and what is the organization's long-term obligation under a risk management framework? What are the realistic options?

3. Some security practitioners argue that critical infrastructure operators should accept higher residual risk from unpatched vulnerabilities because the operational cost of patching (planned outages) could itself create public safety risks. Do you agree with this position? Where does acceptable residual risk end and negligence begin?

---

## Scenario B — The EDR Deployment Decision

A mid-size regional hospital is evaluating whether to deploy EDR across all endpoints. Their current endpoint protection is traditional signature-based antivirus. They have experienced two ransomware incidents in the past 18 months, both of which bypassed the AV and were detected only after encryption had begun.

The EDR vendor's proposal includes continuous telemetry recording, behavioral detection, and automated isolation of compromised endpoints. The hospital's IT director has raised three objections: the cost is four times their current AV spend, the automated isolation feature could disconnect clinical workstations from patient monitoring systems, and the telemetry data volume is too large for their current storage infrastructure.

In 250–350 words, respond to all three of the following:

1. Evaluate the IT director's three objections. For each objection, state whether it represents a legitimate technical concern, a manageable risk, or a misunderstanding of how EDR works. Provide your reasoning using Module 08 concepts.

2. The hospital had two ransomware incidents that bypassed AV. Using the EDR capabilities described in the video scripts, explain at which specific point in the attack chain EDR would have detected and potentially stopped each stage of the attack — even without a known signature.

3. If the hospital cannot afford full EDR deployment across all endpoints, how should they prioritize which systems get EDR first? Propose a prioritization framework using the concepts of asset criticality, attack surface, and data sensitivity from the Module 08 reading.

---

## Peer Reply Guidance

When replying to classmates, engage with one of these angles:

- If your classmate proposed network segmentation as a compensating control for the ICS vulnerabilities, ask them to address whether segmentation would be effective if the attacker already has a foothold on the ICS network — and what additional controls would apply at that point.

- If your classmate argued that EDR's automated isolation is the primary concern for the hospital, challenge them to compare the risk of a brief automated isolation to the alternative: an undetected ransomware event that encrypts clinical data and takes systems offline for days.

- If your classmate proposed a specific EDR prioritization framework, ask them to address how they would handle endpoints that have both high asset criticality and high operational constraints (e.g., clinical workstations that cannot tolerate any performance impact).

---

## Research Starting Points

- CISA ICS Security Guidance: [https://www.cisa.gov/topics/industrial-control-systems](https://www.cisa.gov/topics/industrial-control-systems)

- CISA Known Exploited Vulnerabilities: [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

- Health-ISAC Ransomware Guidance: [https://h-isac.org/](https://h-isac.org/)

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Original post addresses all prompt questions | 40 |
| Demonstrates correct use of Module 08 terminology | 25 |
| Arguments are specific and technically grounded | 15 |
| Two substantive replies that add new reasoning | 20 |
| **Total** | **100** |

---

Module 08 Discussion — End
