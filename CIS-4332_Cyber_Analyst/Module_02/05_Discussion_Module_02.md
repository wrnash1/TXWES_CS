# Discussion Forum: Module 02 - Threat Intelligence and MITRE ATT&CK

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Overview

This week's discussion asks you to apply ATT&CK mapping and CTI analysis skills to real decision-making scenarios. Strong initial posts demonstrate that you can identify specific tactics and techniques, reason about intelligence quality, and connect framework knowledge to operational action. Your peer responses should advance the conversation — challenge an assumption, propose an alternative technique mapping, or surface a nuance the original post missed.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A: The Partial Map

Your SOC manager shows you a threat intelligence report from a government advisory. The advisory describes a campaign in which attackers sent targeted emails with PDF attachments to employees at financial institutions. When the PDF was opened, it ran an embedded script that downloaded a file from a cloud storage URL. That file then created a new Windows service that survived reboots. The advisory does not include any specific IOCs — no hashes, no IPs, no domain names. Your manager asks: "Without IOCs, is this report useful to us?"

In 175-225 words, address all three of the following points:

1. Map the described attacker behaviors to specific ATT&CK tactics and techniques. Use technique IDs where available.
2. Explain whether the absence of specific IOCs makes this report low-value or still useful. Reference the Pyramid of Pain in your answer.
3. Describe one concrete defensive action your SOC could take based solely on the technique-level information in the report, even without any IOCs.

---

## Scenario B: Intelligence Triage Under Time Pressure

It is Monday morning. Your threat intelligence analyst hands you four items before the 8 AM briefing and says you have 15 minutes to decide which one to act on first:

Item 1 — A TLP:GREEN report from an ISAC partner describing active exploitation of a CVE in the same VPN appliance your organization uses, with specific IOCs from attacks in the last 72 hours.

Item 2 — A TLP:CLEAR blog post from a reputable security vendor about a new ransomware family targeting healthcare organizations. Your organization is in the retail sector.

Item 3 — An anonymous tip submitted to your security inbox claiming that your organization is being actively targeted by a specific threat group, with no supporting evidence or source attribution.

Item 4 — A TLP:AMBER report from a commercial threat intelligence vendor describing a credential-stuffing campaign targeting e-commerce login pages, with a list of 200 malicious IPs.

In 175-225 words, address all three of the following points:

1. Rank all four items in order of priority (1 = act on immediately) and justify your top two choices in detail.
2. Explain why the anonymous tip (Item 3) does or does not warrant immediate action. What additional steps would you take to evaluate it?
3. Identify what intelligence lifecycle phase you are performing when you make these triage decisions.

---

## Scenario C: Building ATT&CK-Based Detections

A new Tier 1 analyst on your team asks: "Why do we care about ATT&CK technique IDs? We just watch for alerts that fire." You want to give them a concrete example of how ATT&CK knowledge improves detection quality beyond waiting for alerts to fire.

You recall a recent incident where an attacker used T1059.001 — PowerShell execution — to run encoded commands that bypassed script block logging, and T1055 — Process Injection — to inject into a legitimate Windows process to hide their activity. Neither behavior triggered an alert because no rules for those techniques existed.

In 175-225 words, address all three of the following points:

1. Explain to the new analyst, in plain language, why knowing the ATT&CK technique ID gives you an advantage over simply waiting for alert-based detection.
2. Describe the general structure of a detection rule you would build for T1059.001 — specifically, what observable evidence in Windows event logs would you look for?
3. Explain how the intelligence-driven detection process (CTI → ATT&CK technique → log source → rule) closes the gap that left the organization blind to these two techniques.

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Correct or refine a technique mapping with the proper ATT&CK ID and a brief explanation
- Challenge the Pyramid of Pain reasoning with a specific counterexample
- Identify an intelligence source or ISAC the original post did not mention that would be relevant
- Connect the scenario to a publicly documented real-world breach or threat actor group

Responses that only agree or paraphrase the original post will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5-6 points: All three prompt points addressed with technical precision. ATT&CK technique IDs used correctly. CTI concepts (Pyramid of Pain, TLP, intelligence lifecycle) applied accurately. Meets 175-225 word count. Demonstrates original analysis beyond restating definitions.
- 3-4 points: Most prompt points addressed with some technical accuracy. Technique IDs partially correct or missing. Meets minimum word count.
- 1-2 points: Fewer than two prompt points addressed, significant technical errors, or does not meet word count.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more responses of 75 words each that add substantive technical value — corrects a mapping, challenges reasoning, or adds a relevant source.
- 2 points: Only one qualifying response, or both responses are superficial.
- 0 points: No peer responses submitted.

---

## A Note from Professor Nash

ATT&CK mapping is a skill you will use every day as a working analyst. The exam will give you a scenario and ask you to identify the tactic. Your employer will give you a log entry and ask what the attacker was trying to do. These are the same question. The more comfortable you are mapping behaviors to the framework now, the faster and more confident you will be under pressure. Use this discussion to practice that translation — scenario text to tactic and technique — until it becomes automatic.
