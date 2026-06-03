# Discussion Forum: Module 14 — Security Automation and Scripting for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Overview

This discussion explores the judgment decisions that arise when security teams implement automation. Automation amplifies analyst capability but also amplifies errors — a misconfigured playbook that fires at scale can cause as much disruption as the threat it was designed to counter. Each scenario below presents a situation where automation design, scope, and risk management require careful analysis. Select one scenario, post your analysis, and respond to two peers on different scenarios.

---

## Scenario A — The Runaway Playbook

Your SOAR team deploys a new playbook that automatically blocks outbound connections to any IP address that appears in a commercial threat intelligence feed with a malicious classification. The playbook goes live on a Monday morning. By noon, three business-critical SaaS applications are unreachable — the threat intelligence feed incorrectly flagged their CDN provider's IP ranges as malicious due to a data quality issue on the feed provider's side. The blocks affected 400 employees. It took four hours to identify the root cause and reverse the blocks.

In 175–225 words, address the following: What specific playbook design failures contributed to this incident? What testing and validation procedures should have been performed before the playbook went live? What architectural safeguards — such as allowlisting, confidence thresholds, or human approval gates — would have prevented or limited the damage? After this incident, what change to your SOAR governance process would you implement to prevent similar runaway automation in the future?

---

## Scenario B — The Script That Grew

An analyst on your team wrote a quick Python script 18 months ago to pull failed login events from the SIEM and email a daily summary to the SOC manager. It worked well. Over time, other analysts added features: it now queries three additional APIs, runs four different log sources, generates a PDF report, and automatically escalates alerts that exceed thresholds by creating ServiceNow tickets. Nobody documented any of the changes. The script has no version control. Last week it started failing silently — creating duplicate tickets and missing some log sources entirely — and nobody can figure out why because there is no change history.

In 175–225 words, address the following: What software engineering practices should govern analyst-written security scripts that grow beyond their original scope? Specifically, what would a minimal but effective governance process look like for scripts that touch production systems or generate automated tickets? How do you balance the operational need to keep improving useful automation against the risk of undocumented, unreviewed changes? What specific failure modes in the described scenario could have been caught by even basic engineering practices?

---

## Scenario C — Automation Versus Analyst Judgment

Your SOC manager has proposed fully automating Tier 1 alert triage using a combination of SIEM correlation rules and a SOAR playbook that classifies alerts as false positive, confirmed incident, or needs review — closing false positives automatically and escalating the rest. The proposal projects a 60% reduction in Tier 1 analyst headcount because "the machine handles it." You support automation but have concerns about the proposal as written.

In 175–225 words, address the following: What types of alerts can and should be closed automatically without analyst review, and what types must retain human judgment in the loop? What risk does the organization accept by eliminating analyst review of automatically-closed false positives? How would you detect if the automation's false-positive classification logic degraded over time — for example, as attacker techniques evolved to evade the rules — given that the closed alerts are no longer reviewed by humans? What would you recommend as a balanced approach that captures automation efficiency gains while preserving detection integrity?

---

## Posting Instructions

**Initial Post:** Due Wednesday at 11:59 PM. Select one scenario. Write 175–225 words directly addressing all questions. Use correct automation and SOAR terminology. Reference course concepts where applicable.

**Peer Responses:** Due Sunday at 11:59 PM. Reply to at least two classmates who chose different scenarios from yours. Each reply must be at least 75 words and add substantive analysis — extend the argument, challenge an assumption, or offer an alternative design approach grounded in course content.

---

## Discussion Rubric — 10 Points Total

### Initial Post — 6 Points

- 5–6 pts: Addresses all scenario questions with technical accuracy, correct automation terminology, and clear reasoning. Word count within range. References course frameworks.
- 3–4 pts: Addresses most questions but lacks depth or technical precision.
- 1–2 pts: Superficial treatment or misses key questions.
- 0 pts: No initial post submitted.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies (75+ words each) to classmates on different scenarios. Replies add analysis, challenge assumptions, or offer alternative design approaches grounded in course content.
- 2–3 pts: One substantive reply, or two replies that are superficial.
- 1 pt: Replies present but below length or quality threshold.
- 0 pts: No peer responses submitted.
