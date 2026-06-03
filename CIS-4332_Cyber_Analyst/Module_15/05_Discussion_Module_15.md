# Discussion Forum: Module 15 — Advanced Threat Hunting

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Overview

Threat hunting exists at the intersection of analytical skill, threat intelligence, and organizational culture. This discussion explores the strategic and practical dimensions of building and running a hunting program. Each scenario presents a real challenge that hunting teams face. Select one scenario, post your analysis, and respond to two peers on different scenarios.

---

## Scenario A — Building the First Hunt Program

You are the only dedicated threat hunter at a 600-employee manufacturing company. The organization has a SIEM, an EDR platform, and a Tier 1 SOC team that handles alert triage. There is no formal threat hunting program. Your manager has given you four hours per week for hunting activities and asked you to "start hunting." You have no documented hypotheses, no hunt history, no ATT&CK coverage map, and no established relationship with the IR team.

In 175–225 words, address the following: What is the first action you take before writing a single hunt query, and why? How would you prioritize which ATT&CK techniques to hunt first, given the manufacturing industry context and limited time budget? What relationship with the Tier 1 SOC and IR team do you need to establish before your hunts can have organizational impact? What does success look like for your first three months, and how would you measure it to justify continued investment in the program?

---

## Scenario B — The Hunt That Finds Something Unexpected

Your hunt hypothesis was: "We hypothesize that threat actors may be using DNS tunneling to exfiltrate data from our legal department workstations." While investigating DNS query logs, you find no evidence of tunneling, but you do discover that one legal department workstation has been making HTTP connections (not HTTPS) to a domain registered 12 days ago with a 1-year registration, hosted on infrastructure associated with multiple recently-registered domains. The domain resolves to a shared hosting IP used by thousands of legitimate small websites. There is no threat intelligence match on the domain.

In 175–225 words, address the following: How do you assess the risk level of this finding given the ambiguous evidence? What additional investigation steps would you take to determine whether this is malicious, a shadow-IT application, or a false lead? At what threshold of evidence do you escalate to the IR team versus continuing independent investigation? How does this unexpected finding affect your original DNS tunneling hypothesis — do you document it as a negative result on the hypothesis, a separate finding, or both?

---

## Scenario C — Hunting Program Metrics and Executive Justification

Your threat hunting program has been running for six months. You have completed 23 documented hunts. Three hunts led to confirmed incident escalations. Seven hunts resulted in new detection rules being added to the SIEM. Thirteen hunts were negative (no findings). Your annual budget review is next month and your manager is presenting to the executive team. A CFO asks: "How do I know if threat hunting is worth the investment? We could just rely on our automated detection."

In 175–225 words, address the following: What metrics from your six-month program most directly demonstrate value to a non-technical executive? How do you explain the business value of the 13 negative hunts — why is "we found nothing" a meaningful positive outcome? How would you calculate a return-on-investment estimate for the three confirmed incident escalations? What argument would you make for why automated detection alone is insufficient, without disparaging the automated systems that the executive team has already approved and funded?

---

## Posting Instructions

**Initial Post:** Due Wednesday at 11:59 PM. Select one scenario. Write 175–225 words directly addressing all questions. Use correct threat hunting terminology. Reference MITRE ATT&CK, the hunting loop, or other course concepts where applicable.

**Peer Responses:** Due Sunday at 11:59 PM. Reply to at least two classmates who chose different scenarios from yours. Each reply must be at least 75 words and add substantive analysis — extend the argument, challenge an assumption, or offer an alternative approach grounded in course content.

---

## Discussion Rubric — 10 Points Total

### Initial Post — 6 Points

- 5–6 pts: Addresses all scenario questions with technical accuracy, correct hunting terminology, and clear reasoning. Word count within range. References course frameworks.
- 3–4 pts: Addresses most questions but lacks depth or technical precision.
- 1–2 pts: Superficial treatment or misses key questions.
- 0 pts: No initial post submitted.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies (75+ words each) to classmates on different scenarios. Replies add analysis, challenge assumptions, or offer alternative approaches grounded in course content.
- 2–3 pts: One substantive reply, or two replies that are superficial.
- 1 pt: Replies present but below length or quality threshold.
- 0 pts: No peer responses submitted.
