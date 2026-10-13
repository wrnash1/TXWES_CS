# Discussion Forum: Module 04 - Log Analysis and SIEM Operations

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Overview

Log analysis is where abstract security knowledge becomes operational. This week's discussion asks you to apply log reading skills to scenarios that require both technical accuracy and practical judgment. Strong initial posts cite specific Event IDs, identify ATT&CK techniques, and propose concrete SIEM query logic — not just general descriptions. Your peer responses should challenge the analysis, propose alternative interpretations, or identify a pattern the original post missed.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A: The Quiet After-Hours Login

The SIEM generates a single Medium-severity alert at 11:43 PM on a Tuesday. The alert fires on Event ID 4624, Logon Type 10 (RemoteInteractive), for user "marketing_shared" on the system EXEC-LAPTOP-04, a C-suite executive's laptop. The source IP is 192.168.10.55, which resolves to a desktop workstation in the marketing department. The marketing_shared account is a shared login used by five members of the marketing team for accessing a collaborative document tool. No other alerts are associated with this event.

In 175-225 words, address all three of the following points:

1. Identify what type of activity Event ID 4624 with Logon Type 10 represents and explain why this combination at 11:43 PM on an executive laptop warrants investigation even though the account is a legitimate shared account.
2. Describe three specific additional log sources or queries you would run to determine whether this event is benign or malicious. For each, specify what you would look for.
3. Explain what outcome (true positive or false positive) is more likely in this specific scenario and justify your reasoning based on the observable facts. Identify what single piece of evidence would most definitively resolve the question.

---

## Scenario B: The Noisy SIEM

Your organization's SIEM is generating 2,400 alerts per day. Your analysis of the past two weeks' alerts reveals the following breakdown:

- 71% of alerts are from a single correlation rule: "Service Account Logon Outside Business Hours"
- Of those, 99.7% are from a batch processing system that runs nightly backups from 2-4 AM
- The remaining 0.3% are genuinely suspicious — service account use from unusual source IPs
- Analysts are spending 65% of their investigation time on this single rule

In 175-225 words, address all three of the following points:

1. Identify what the core problem is using the correct SIEM/SOC terminology from the Reading Guide. What operational risk does a situation like this create for the SOC team?
2. Describe two specific technical modifications to the SIEM correlation rule that would eliminate the noise while preserving detection of genuinely suspicious activity. Be specific — reference source IP ranges, time windows, or account exclusion logic.
3. Explain the process an analyst should follow to propose and implement a rule change. Who needs to be involved, and what documentation should be produced to ensure the change does not create a new detection gap?

---

## Scenario C: The Missing Months

An internal audit discovers that a privileged user account — a domain admin — made 14 unauthorized changes to critical system configurations over a three-month period. The account owner denies making the changes. The investigation team requests the relevant Windows Event Logs to determine whether the account owner was logged into those systems at the times of the changes. The SIEM administrator responds that the logs are only available for the most recent 45 days; the earlier two months of logs were automatically purged by the retention policy.

In 175-225 words, address all three of the following points:

1. Explain what investigation capabilities have been permanently lost due to the 45-day retention policy, and describe the specific type of evidence that Event ID 4688 (process creation) and Event ID 4624 (logon) would have provided if retained.
2. If the organization processes payment card data and falls under PCI DSS, explain whether the 45-day retention policy is compliant and what the remediation requirement is.
3. Recommend a practical log retention architecture that satisfies both cost constraints and security investigation needs — specifically, how to balance "hot" storage (immediately queryable) versus "cold" storage (archived but retrievable) to meet compliance requirements without storing all logs in expensive immediately-accessible storage.

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Identify a log source or query approach the original post did not mention
- Challenge an Event ID interpretation with a specific counter-scenario
- Propose a more precise SIEM rule modification than the original post described
- Reference a specific compliance framework requirement that affects the scenario analysis

Responses consisting only of agreement without technical substance will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5-6 points: All three prompt points addressed with technical precision. Correct Event IDs referenced where applicable. SIEM concepts (correlation, normalization, false positive, retention) used accurately. Meets 175-225 word count. Demonstrates original analytical reasoning.
- 3-4 points: Most prompt points addressed with some accuracy. Some technical terms used imprecisely. Meets minimum word count.
- 1-2 points: Fewer than two prompt points addressed, significant technical errors, or below minimum word count.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more responses of 75 words each that add specific technical value — an additional log source, a rule modification suggestion, a compliance citation, or a challenge to the original analysis.
- 2 points: Only one qualifying response, or both responses are superficial.
- 0 points: No peer responses submitted.

---

## A Note from Professor Nash

The ability to read a log entry and immediately recognize what it represents — without having to look it up — is what separates analysts who are effective under pressure from those who slow down when it counts. Study the Event ID table in the Reading Guide until those numbers are automatic. When you write your initial post this week, pull out specific Event IDs by number and explain precisely what each one reveals. That level of specificity is what the CySA+ exam expects, and it is the standard for this discussion.
