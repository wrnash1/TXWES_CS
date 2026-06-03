# Discussion Forum: Module 12 — IoT Security

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Overview

This week's discussion asks you to apply the security concepts from Module 12 to three realistic scenarios. You will analyze attack vectors, identify OWASP IoT categories, and propose concrete remediation strategies. Strong posts go beyond naming categories — they explain *why* a control works and what its limitations are.

---

## Scenario 1 — The Hospital HVAC Incident

A regional hospital's facilities team deployed 240 IP-connected HVAC sensors three years ago. The sensors monitor temperature and humidity in patient rooms, operating rooms, and pharmaceutical storage. A security consultant's recent audit found: all 240 devices use the same factory-default username and password (never changed), the devices transmit readings over plain HTTP on port 80, and the devices are on the same network segment as clinical workstations and the hospital's Electronic Health Record (EHR) system.

Discuss the following:

- Which OWASP IoT Top 10 categories are present in this scenario? Identify at least two and explain how each one manifests in the described deployment.
- What is the most likely attack path an adversary would use to move from a compromised HVAC sensor to the EHR system? Describe the attack steps in plain language.
- Propose a prioritized remediation plan. Which control should be implemented first, and why?

Your initial post should be 175–225 words and address all three points. Support your remediation priority decision with a specific technical justification — not just "best practice."

---

## Scenario 2 — The Firmware Update Dilemma

A consumer electronics company ships a popular smart home hub. Six months after launch, a critical remote code execution vulnerability is discovered in the JSON parsing library embedded in the firmware. There are 800,000 devices in the field. The devices have an OTA update mechanism, but it was not designed with firmware signing — the device downloads a firmware image from a URL and flashes it without any cryptographic verification. The company's security team proposes two options:

Option A: Push the patched firmware to all 800,000 devices immediately via the existing unsigned OTA mechanism.

Option B: Delay the update by two weeks to implement firmware signing before deploying the patch, accepting the risk that the RCE vulnerability is unpatched and publicly known during those two weeks.

Discuss the following:

- What security risk does each option introduce? Be specific about what an attacker can do under each option.
- Which option would you choose, and what additional safeguard would you implement alongside it to reduce the risk introduced by your choice?
- What does this scenario reveal about the relationship between OWASP IoT #4 (Lack of Secure Update Mechanism) and #5 (Insecure or Outdated Components)?

Your initial post should be 175–225 words and take a clear position on the option choice with technical justification.

---

## Scenario 3 — Certificate Revocation at Scale

An industrial IoT company deploys 15,000 sensors across 30 manufacturing facilities. Each sensor has a unique X.509 client certificate for mutual TLS authentication to the cloud MQTT broker. A third-party logistics contractor who had temporary access to the provisioning server reports that a USB drive containing 200 device private keys may have been lost or stolen. The security team must decide how to respond.

Discuss the following:

- What is the immediate security action that must be taken for the 200 potentially compromised devices, and what mechanism enables it?
- If the company has not implemented Certificate Revocation List checking on the MQTT broker, what is the impact of that gap in this situation?
- What operational challenge does revocation at scale present, and what architectural feature — beyond a CRL — could allow the company to respond more quickly?

Your initial post should be 175–225 words. Peer responses should engage with the architectural suggestion and either endorse it with supporting reasoning or propose an alternative.

---

## Discussion Instructions

### Initial Post

Due: Wednesday at 11:59 PM

Choose one scenario (or address all three for extra credit). Write 175–225 words per scenario addressed. Your post must:

- Identify relevant OWASP IoT categories by number and name
- Propose specific, technically justified controls — not generic advice
- Acknowledge at least one trade-off or limitation of your proposed solution

### Peer Responses

Due: Sunday at 11:59 PM

Reply to at least two classmates (minimum 60 words each). In your replies:

- Evaluate the technical accuracy of their proposed remediation
- Add a constraint or real-world consideration they may not have addressed
- If you disagree with their option choice in Scenario 2, explain your reasoning with technical specifics

---

## Discussion Rubric (10 Points Total)

### Initial Post — 6 Points

- 5–6 pts: Addresses all prompt sub-questions for the chosen scenario(s). Correct OWASP category identification. Technically specific remediation with explicit trade-off acknowledgment. Meets word count.
- 3–4 pts: Addresses most sub-questions. OWASP categories identified but explanation is superficial. Remediation proposed but lacks technical specificity or trade-off discussion.
- 0–2 pts: Post is missing, significantly below word count, or does not engage with the scenario's technical content.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies that add technical value — new considerations, alternative approaches, or well-reasoned disagreement. Each reply meets the 60-word minimum.
- 2 pts: One substantive reply, or two replies that are superficial (e.g., "Great point, I agree with your approach.").
- 0 pts: No peer responses submitted by the deadline.

---
