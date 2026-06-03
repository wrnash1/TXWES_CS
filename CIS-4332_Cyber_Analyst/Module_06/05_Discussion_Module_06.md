# Discussion Forum: Module 06 — SIEM and Log Analysis

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Overview

SIEM analysis is as much about judgment as it is about technical skill. Writing a query is straightforward once you know the syntax — but deciding which log sources to trust, how to tune a noisy rule, and when an alert is a real incident versus a false positive requires contextual reasoning. This week's discussion puts you in the analyst seat for three realistic scenarios and asks you to defend your decisions.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A — The Missing Log Source

Your SOC has a well-configured SIEM with endpoint logs, firewall logs, and authentication logs feeding into it. A post-incident review reveals that an attacker exfiltrated 8 GB of sensitive data over four days. Review of the available SIEM logs shows no alerts fired during the exfiltration period. A network engineer mentions that DNS logs and NetFlow data have never been configured to feed the SIEM, despite being available.

In 175–225 words, address all three of the following points:

1. Explain specifically how DNS logs and NetFlow data would have provided earlier detection of this exfiltration. Reference the types of patterns those sources reveal that endpoint and firewall logs alone cannot.

2. Identify two additional log sources that the SOC should consider adding to improve future exfiltration detection, and explain what detection value each provides.

3. Describe the process a SOC should follow to identify and prioritize missing log sources — what questions should drive the gap analysis, and who should be involved in the decision?

---

## Scenario B — The Tuning Dilemma

A Tier 1 analyst has been tasked with tuning the SIEM's brute-force detection rule. The current rule fires on two or more failed logins per account per five-minute window and generates 350 alerts per day. Over 90 days, three of those alerts were confirmed true positives.

The analyst has two options:

Option 1: Raise the threshold to 20 failed logins per five-minute window and add allowlist entries for 12 known service accounts.

Option 2: Add a condition requiring that a successful login follow the failed logins within 10 minutes, reducing the rule to only fire when brute force succeeds.

In 175–225 words, address all three of the following points:

1. Analyze Option 1 — what detection capability does it preserve, and what attack scenarios could it miss?

2. Analyze Option 2 — what is the security significance of only alerting when brute force succeeds? What is the argument for and against this approach?

3. Recommend a final approach — could a combination of both options be implemented? Should both rules coexist at different severity levels? Justify your recommendation.

---

## Scenario C — The Unexplained Spike

At 11:47 PM on a Saturday, your SIEM fires a data volume alert: a single finance department workstation transferred 2.3 GB outbound to an IP address in Eastern Europe over 22 minutes. No SIEM alerts fired for this host in the previous 90 days. The host belongs to a finance analyst who has been on PTO for two weeks.

In 175–225 words, address all three of the following points:

1. Classify this alert as true positive, false positive, or requires further investigation. Provide your initial reasoning based only on the information available.

2. Identify five specific additional data points you would gather in the next 15 minutes to confirm or rule out a compromise — cite which log sources each data point comes from.

3. Assuming initial investigation supports a true positive finding, describe the immediate SIEM-based and non-SIEM actions you would take. Reference the MTTD and MTTR metrics and explain how rapid alert triage contributes to reducing both.

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Identify a log source or detection technique the original post missed
- Challenge the tuning recommendation with a specific trade-off the post did not address
- Reference a specific SIEM use case or correlation rule design concept from the Reading Guide
- Connect the scenario to a documented real-world breach or detection failure

Responses consisting only of agreement without technical content will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5–6 points: All three prompt points addressed with technical precision. Log sources named correctly. Detection logic explained accurately. Meets 175–225 word count.
- 3–4 points: Most prompt points addressed with reasonable accuracy. Meets minimum word count.
- 1–2 points: Fewer than two points addressed or significant technical errors present.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more responses of 75+ words with specific technical additions or challenges.
- 2 points: One qualifying response or both responses are superficial.
- 0 points: No peer responses submitted.

---

## A Note from Professor Nash

The scenarios in this discussion represent the kinds of judgment calls analysts make every shift. There is rarely a perfectly clean answer — a tuning decision that eliminates false positives always carries some risk of missing a real attack. The goal is not to find the one correct answer but to reason carefully about the trade-offs and communicate your logic clearly. That reasoning process is exactly what CySA+ scenario questions test, and it is what hiring managers look for in entry-level analyst candidates. Practice articulating your decision-making process here.
