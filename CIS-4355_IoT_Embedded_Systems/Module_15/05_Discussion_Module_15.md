# Discussion Forum: Module 15 — IoT Project Deployment and Management

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Overview

Fleet management at scale involves trade-offs between speed, safety, cost, and reliability. This week's scenarios present situations where a team must make deployment and management decisions with real consequences. Your post should demonstrate that you can reason through these trade-offs technically, acknowledging the costs of each choice.

---

## Scenario 1 — The Staggered OTA Disaster

A smart city company manages 80,000 connected streetlight controllers. An urgent firmware update patches a critical remote code execution vulnerability (CVE with CVSS score 9.8) that has just been published. The security team wants to deploy the patch immediately to all 80,000 devices. The engineering team insists on a staged rollout: 80 devices in the canary group for 48 hours, then 8,000 for 48 hours, then the remaining fleet.

A city official is told the rollout will take approximately 7 days. The official argues that during those 7 days, 79,920 devices remain exploitable and demands the patch be deployed simultaneously to all devices.

Discuss the following:

- What specific risk does the 7-day staged rollout expose, and is the city official's concern technically valid? Explain using the CVE severity score as context.
- What specific risk does a simultaneous 80,000-device deployment introduce, and has this risk materialized in real-world IoT fleet updates? Reference any real-world examples or analogies.
- Propose a modified rollout strategy that balances speed of patching against safety of the update process. Specify the canary group size, the monitoring window duration, the halt criteria, and the reason you chose those values for a security-critical patch (as opposed to a feature update).

Your initial post should be 175–225 words. Take a clear position on whether to prioritize speed or safety, with technical justification.

---

## Scenario 2 — The Orphaned Device Problem

A telecommunications company ran an IoT pilot program in 2021 with 5,000 environmental sensors. The pilot concluded in 2022 and was considered a failure — the devices were removed from production, the device registry was cleared, and the MQTT broker was decommissioned. However, an IT audit in 2024 reveals that the 5,000 devices were resold to a liquidator without any firmware erasure or certificate revocation. The certificates were issued with a 5-year validity period (expiring in 2026) and were never added to the CRL. The original CA that issued the certificates is still active.

Discuss the following:

- What is the current security posture of the orphaned certificates? Can the devices still authenticate to any backend services using these certificates?
- The device registry and broker were decommissioned, but the CA is still active. What does this mean for the organization's ability to revoke the certificates now?
- Propose a complete remediation plan. Your plan must address: immediate certificate invalidation, risk assessment for what the devices may have connected to since 2022, and process changes to prevent this situation in future decommissioning cycles.

Your initial post should be 175–225 words. Peer responses should evaluate whether the proposed process changes are specific enough to be actionable.

---

## Scenario 3 — Designing Monitoring for a Medical IoT Fleet

A hospital system is deploying 1,200 connected infusion pumps across three campuses. Each pump publishes telemetry every 30 seconds: pump status, drug delivery rate, alarm state, battery level, and network connection quality. The IT team has been asked to design the monitoring and alerting system for this fleet.

The team debates two approaches:

Approach A: Alert on every deviation from nominal — any pump not reporting within 45 seconds triggers an alert, any battery below 80% triggers an alert, any reconnect event triggers an alert.

Approach B: Alert only on high-confidence failure indicators — pump offline for more than 5 minutes, battery below 20%, three or more reconnects within one hour, or an active alarm state not acknowledged within 2 minutes.

Discuss the following:

- Which approach is correct for a medical device fleet, and why? In your answer, explicitly define the consequence of alert fatigue in a medical context.
- For each of the four alert conditions in Approach B, explain why that specific threshold value is appropriate for an infusion pump specifically — not just for IoT devices in general.
- What additional alert condition, not listed in either approach, would you add for this specific application? Justify it with a patient safety argument.

Your initial post should be 175–225 words. The medical context is intentional — generic IoT monitoring arguments are not sufficient for full credit.

---

## Discussion Instructions

### Initial Post

Due: Wednesday at 11:59 PM

Choose one scenario (or address all three for extra credit). Write 175–225 words per scenario addressed. Your post must:

- Make a specific, justified recommendation — not just a list of trade-offs
- Use terminology from Module 15 (staged rollout, CRL, device twin, alert fatigue, canary group, decommissioning)
- Acknowledge the cost of your recommended approach

### Peer Responses

Due: Sunday at 11:59 PM

Reply to at least two classmates (minimum 60 words each). In your replies:

- In Scenario 1, challenge or validate their canary group size and monitoring window choices with specific reasoning
- In Scenario 2, evaluate whether their remediation plan addresses all four decommissioning steps from the reading
- In Scenario 3, evaluate whether their additional alert condition is medically justified or just generically reasonable

---

## Discussion Rubric (10 Points Total)

### Initial Post — 6 Points

- 5–6 pts: Addresses all sub-questions with specific, technically justified answers. Correct Module 15 terminology. Explicit acknowledgment of the chosen approach's cost or limitation. Meets 175-word minimum.
- 3–4 pts: Addresses most sub-questions. Terminology used but not always precisely. Recommendation made but justification is general rather than specific to the scenario context.
- 0–2 pts: Post missing, below minimum length, or does not engage with the technical or domain-specific context of the scenario.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies that add domain-specific value — not just "I agree." Each challenges a specific number, threshold, or design choice with technical or contextual reasoning. Meets the 60-word minimum.
- 2 pts: One substantive reply, or two replies that only restate agreement without new content.
- 0 pts: No peer responses submitted.

---
