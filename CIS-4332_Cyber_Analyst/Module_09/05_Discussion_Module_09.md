# Discussion Forum: Module 09 — Incident Response: Containment and Recovery

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Overview

Containment and recovery decisions are made under pressure, often with incomplete information, and the consequences of getting them wrong are severe. A missed persistence mechanism causes re-infection the day after recovery. An untrusted backup restores the ransomware along with the data. A system returned to production with the original vulnerability still present is compromised again within hours. This week's discussion asks you to analyze three realistic containment and recovery decision scenarios and reason through the correct actions using the frameworks from the Reading Guide.

Initial Post: Due Wednesday at 11:59 PM

Peer Responses: Due Sunday at 11:59 PM (minimum two responses)

---

## Scenario A: The Shutdown Instinct

A Tier 2 analyst receives an escalation for a confirmed malware infection on a finance workstation. The malware has an active C2 connection and the sandbox report shows it uses CreateRemoteThread to inject into explorer.exe and establishes two persistence mechanisms. The Tier 2 analyst's first action is to instruct the on-site technician to power off the workstation immediately — reasoning that powering it off stops the C2 connection and prevents the attacker from doing any more damage while the team coordinates a response.

Three hours later, when the IR team attempts memory forensics on the powered-off workstation, they find they cannot recover the injected code from RAM. The C2 connection log was not captured. The attacker's decrypted configuration — which would have revealed the attacker's staging server — was not retrieved. The DFIR team must proceed with significantly less evidence.

In 175-225 words, address all three of the following points:

1. Identify the specific analytical error in the Tier 2 analyst's containment decision. What data was lost as a direct result of the shutdown, and why is that data forensically significant? Reference the specific concept from the Reading Guide that explains the correct action.
2. Explain what the correct containment action should have been and how it would have preserved the evidence that was lost. Be specific about what EDR capability accomplishes this and how it differs from a physical shutdown.
3. Describe a scenario in which shutdown might be the correct containment action — explaining the specific conditions that would make it preferable to EDR network isolation. What changes when volatile evidence is no longer the priority?

---

## Scenario B: The Incomplete Eradication

A confirmed Trojan infection is identified on WS-ACCOUNTS-02. The IR team contains the system using EDR network isolation, removes the malware binary from `C:\Users\Public\update.exe`, deletes the attacker-created registry run key at `HKCU\...\Run\SystemUpdate`, runs a post-eradication EDR scan that returns clean, and returns the system to production. Seven days later, WS-ACCOUNTS-02 is generating C2 beaconing alerts again.

The re-investigation reveals that the original malware had also created a scheduled task named `MicrosoftEdgeUpdater` pointing to a second copy of the payload stored at `C:\ProgramData\Edge\msedge_update.exe`. The scheduled task had survived the eradication process because the team only searched for the primary file path and registry run key — not for additional persistence mechanisms.

In 175-225 words, address all three of the following points:

1. Identify what eradication step from the Reading Guide was not completed correctly. Explain why checking only the confirmed IOC artifacts is insufficient for a complete eradication and what the team should have done instead.
2. Describe how the team should have structured the verification step (Step 5 of the eradication checklist) to catch the missed scheduled task before the system was returned to production. What specific query or search would have detected it?
3. Explain what a WMI subscription persistence mechanism is and why it is significant to include WMI subscription checks in every eradication process — even when the primary malware analysis report did not identify a WMI-based persistence technique.

---

## Scenario C: The Backup Decision

A ransomware attack has encrypted files on a file server at a healthcare organization. The IR team has contained the file server using EDR isolation and has determined the following about available backup options:

Option 1: Daily incremental backups on a NAS device on the same subnet as the encrypted file server. Last backup was 6 hours before the encryption began. The NAS is currently accessible on the network.

Option 2: Weekly full backups to an immutable cloud storage bucket. Last backup was Sunday evening, 72 hours before the encryption event. The cloud storage bucket has write-protection enabled — no credentials found in the organization's Active Directory environment have write access to delete or modify it.

The IR team lead recommends Option 1 because it provides more recent data and therefore less data loss. The CISO rejects Option 1 and insists on Option 2 despite the additional 72-hour data loss.

In 175-225 words, address all three of the following points:

1. Explain why the CISO's decision to use Option 2 is correct. Address the specific risk that Option 1 presents given the network environment described, and why the NAS device's backup contents cannot be trusted without additional verification.
2. Describe what verification steps the IR team should take before beginning the restore from Option 2, even though the cloud backup is immutable. What are they confirming, and why does immutability not eliminate all verification requirements?
3. Explain the concept of Recovery Point Objective and how it applies to the CISO's decision. What does accepting the 72-hour data loss mean in operational terms for a healthcare organization, and what type of pre-incident planning could have reduced this data loss?

---

## Peer Response Guidelines

When replying to classmates, your response must be at least 75 words and must do one or more of the following:

- Identify an additional forensic artifact that was lost or preserved that the original post did not mention
- Challenge the backup integrity assessment with a different technical risk scenario
- Reference a specific NIST SP 800-61 phase or eradication checklist step the original post did not cite
- Connect one of the scenarios to a real-world incident pattern where incomplete eradication or incorrect backup selection had documented consequences

Responses consisting only of agreement without technical content will receive no credit.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5-6 points: All three prompt points addressed with technical precision. Eradication steps, volatile evidence concepts, and backup integrity concepts applied accurately. Meets 175-225 word count.
- 3-4 points: Most prompt points addressed with some technical accuracy. Meets minimum word count.
- 1-2 points: Fewer than two points addressed or significant technical errors.
- 0 points: No initial post submitted.

### Peer Responses (4 Points)

- 4 points: Two or more responses of 75 words each with specific technical additions.
- 2 points: One qualifying response or both are superficial.
- 0 points: No responses submitted.

---

## A Note from Professor Nash

Scenario B is the eradication failure pattern I see most often cause re-infections in real environments. The team removed what they knew about and declared success. The scheduled task and the second binary were right there — they just were not searched for. The lesson is not that eradication is hard. The lesson is that eradication requires a systematic search for all persistence mechanism types across all in-scope systems — not just removing the specific artifacts that appeared in the initial analysis. A threat actor who knows anything about incident response will use multiple persistence mechanisms specifically because they expect you to find the obvious one and stop there. Do not stop there.
