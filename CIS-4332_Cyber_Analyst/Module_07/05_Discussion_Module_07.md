# Discussion Forum: Module 07 - Malware Analysis Fundamentals

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Overview

Malware analysis gives you the ability to move from detecting that something happened to understanding what it is and what it can do. This week's discussion asks you to reason through real analysis scenarios — static and dynamic methodology, IOC extraction, and ATT&CK behavior mapping — as you would in an actual SOC investigation. Your goal is not just to identify the correct term but to explain the reasoning behind each analytical decision.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A: The Packed Sample Problem

A SOC analyst receives a suspicious file hash from a threat intelligence feed. The file is an executable flagged as associated with a known APT group's toolset. The analyst downloads the sample to an isolated analysis workstation and runs standard static analysis: strings extraction, PE header review, and import table inspection. The strings output contains almost no readable content. The import table contains only five functions: LoadLibraryA, GetProcAddress, VirtualAlloc, CreateThread, and ExitProcess. The PE has two sections: one with normal entropy and one with entropy of 7.97. The analyst concludes: "Static analysis shows this sample has minimal capabilities — only basic library loading functions. I don't see enough indicators to escalate this."

In 175-225 words, address all three of the following points:

1. Explain why the analyst's conclusion is incorrect. What do the five imported functions, the high-entropy section, and the near-empty strings output collectively indicate about this sample? Reference the specific static analysis concept from the Reading Guide that explains this finding.
2. Describe what the analyst should do next and what additional information dynamic sandbox analysis would likely produce that static analysis cannot reveal for this sample.
3. Explain what a malware author gains by using packing, and identify the specific limitation it creates for signature-based antivirus detection.

---

## Scenario B: The IOC Triage Decision

Your threat intelligence team has just completed sandbox analysis of a malware sample. The sandbox report produced the following indicators: a SHA-256 file hash, a C2 IP address on port 443, a C2 domain name using a subdomain pattern consistent with domain generation algorithm output, a mutex name, a registry run key path and value name, and a scheduled task name. Your team has time to implement exactly three detection rules before the shift ends.

Your manager asks: "Which three IOCs give us the best immediate detection coverage for the lowest false positive risk?"

In 175-225 words, address all three of the following points:

1. Identify and justify which three IOCs you would prioritize for immediate rule creation. For each, explain why it provides high detection value with low false positive risk.
2. Explain why the C2 IP address on port 443, while clearly malicious, may be a lower-priority detection rule than some of the other IOCs listed. What operational limitation reduces its long-term value?
3. Explain what the mutex name offers as a detection IOC that other IOCs on this list do not. Why are mutexes considered high-fidelity indicators, and what is the one practical limitation of mutex-based detection?

---

## Scenario C: The Double-Extortion Investigation

An EDR alert fires on a finance workstation showing a process named `archivelogs.exe` executing from `C:\Users\Public\` and initiating a large outbound data transfer to an external IP on port 443. The transfer is estimated at 14 GB over 22 minutes. Forty minutes later, a second process from the same directory begins renaming files across multiple mapped network drives, appending the extension `.locked` to each file. A ransom note appears on the desktop.

A Tier 1 analyst's first instinct is to immediately shut down the workstation to stop the encryption.

In 175-225 words, address all three of the following points:

1. Identify which phase of the double-extortion model each of the two observed behaviors represents. Explain why the exfiltration phase is actually the more critical detection window from a defender's perspective.
2. Evaluate the Tier 1 analyst's instinct to immediately shut down the workstation. What is the risk of immediate shutdown in this scenario, and what should the analyst do instead using EDR capabilities?
3. Describe the two ATT&CK techniques represented by the behaviors described (one for the exfiltration phase and one for the encryption phase). Explain what detection control — SIEM, EDR, or DLP — would have been best positioned to alert on the exfiltration phase before encryption began.

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Identify a packing technique or evasion method the original post did not mention
- Challenge the IOC prioritization with a different analytical framework or risk weighting
- Reference a specific ATT&CK technique the original post did not cite
- Connect the scenario to a real-world malware family or documented intrusion that matches the described behavior

Responses consisting only of agreement without technical content will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5-6 points: All three prompt points addressed with technical precision. Static vs. dynamic concepts explained accurately. IOC types and ATT&CK technique IDs cited correctly. Meets 175-225 word count.
- 3-4 points: Most prompt points addressed with some technical accuracy. Meets minimum word count.
- 1-2 points: Fewer than two points addressed or significant technical errors.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more responses of 75 words each with specific technical additions.
- 2 points: One qualifying response or both are superficial.
- 0 points: No responses submitted.

---

## A Note from Professor Nash

The packed sample scenario in Scenario A is one of the most important concepts for both the exam and the job. When you see minimal imports and near-empty strings, your brain should immediately flag: this is packed. An analyst who concludes "minimal capabilities" from a packed sample's import table is going to miss the real payload entirely. Packing is specifically designed to make you draw that wrong conclusion. Once you recognize the pattern — five loader-functions, high entropy, no readable strings — you know you are looking at a shell, not the actual malware. That recognition needs to be reflexive. Use this discussion to build that reflex in your own words.
