# Discussion Forum: Module 07 — Security Architecture and Controls

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Overview

This week's discussion connects security architecture and control framework concepts to real-world incidents and decisions. You will analyze scenarios involving defense-in-depth failures, framework selection, and control gaps, and engage substantively with your classmates' analyses.

**Initial Post:** Due Wednesday at 11:59 PM — 175–225 words in complete sentences

**Peer Responses:** Due Sunday at 11:59 PM — minimum 60 words each, respond to at least 2 classmates

---

## Scenario A — When One Layer Fails

In May 2021, Colonial Pipeline, one of the largest fuel pipeline operators in the United States, suffered a ransomware attack that halted pipeline operations for six days, causing fuel shortages across the eastern seaboard. Post-incident analysis revealed that attackers gained initial access through a compromised VPN password for an account that was no longer in active use. The account had no multi-factor authentication. Once inside, the attackers moved laterally through the network before deploying ransomware.

Respond to the following in 175–225 words: From a defense-in-depth perspective, identify at least two specific control failures that contributed to this incident and explain which architecture layers they represent. Then describe what controls at those layers — if properly implemented — could have interrupted the attack chain. Your response should reference specific control types (preventive, detective, corrective) and at least one control category (technical, administrative, physical).

---

## Scenario B — Choosing the Right Framework

A regional community bank with 200 employees has just completed its first formal security risk assessment. The results identified significant gaps in access control, patch management, and employee security awareness. The board has approved a modest budget to begin building a formal security program. The CISO has narrowed the choice to three frameworks: NIST SP 800-53, CIS Controls v8, and NIST CSF 2.0.

Respond to the following in 175–225 words: Which framework — or combination of frameworks — would you recommend the bank use, and why? Your response should explain the strengths and limitations of at least two of the three frameworks in the context of this specific organization. Address how the chosen approach helps the CISO prioritize with limited resources while building toward a more mature program over time.

---

## Scenario C — Zero Trust in a Legacy Environment

A state government agency manages a network built over 25 years. It includes modern Windows 11 workstations, Windows Server 2012 systems that cannot be patched or upgraded due to legacy application dependencies, and several Internet of Things devices that cannot support agent-based security software. The agency's CIO has read about Zero Trust Architecture and has directed the security team to "implement Zero Trust."

Respond to the following in 175–225 words: What are the practical challenges of implementing Zero Trust principles in an environment with legacy systems and unmanageable devices? Identify two specific Zero Trust principles and explain how each could be applied even within these constraints. Your response should be realistic — acknowledge what is not immediately achievable — while showing how incremental progress toward Zero Trust is still possible and valuable.

---

## Peer Response Requirements

After posting your initial response to one scenario, read your classmates' posts and write substantive replies to at least two peers. Each reply must be a minimum of 60 words and must add value — a new perspective, a challenge to an assumption, a connection to the lab or reading guide, or a relevant example. Responses such as "I agree, great post" do not earn peer response credit.

---

## Discussion Rubric — 10 Points Total

| Criteria | Points | Description |
|---|---|---|
| Initial post directly addresses the scenario question | 2 | Answers what was asked; not a generic security essay |
| Accurate use of framework and architecture terminology | 2 | CSF functions, control types/categories, Zero Trust principles used correctly |
| Demonstrates analysis beyond lecture recall | 2 | Takes a position, makes tradeoff judgments, applies concepts to specifics |
| Word count met (175–225 words) in complete sentences | 1 | Full sentences; professional tone; not a bullet list |
| Peer response 1 — substantive, 60+ words, adds value | 1.5 | Engages with peer's reasoning; does not merely agree |
| Peer response 2 — substantive, 60+ words, adds value | 1.5 | Engages with peer's reasoning; does not merely agree |

---

## A Note from Professor Nash

Scenario A is based on a real incident that I use in this course because it illustrates something important: sophisticated attackers do not need sophisticated entry points. The Colonial Pipeline attack began with a single unused VPN account and no MFA. That is a Tier 1 CIS Control failure — account management. The most fundamental cyber hygiene, not a zero-day exploit, was the entry vector.

As you analyze these scenarios, I want you to resist the impulse toward complexity. The most dangerous security gaps are often the most basic ones. The frameworks we studied this week — particularly CIS Controls Implementation Group 1 — exist precisely because the industry has learned that organizations frequently skip essential hygiene while pursuing advanced capabilities. Get the basics right before you implement the advanced controls.

I also want you to push each other in the peer responses. The best discussions I have seen in this course happen when students challenge each other's framework recommendations. There is rarely one correct answer, and the reasoning behind your recommendation matters as much as the recommendation itself.

— Professor Nash
