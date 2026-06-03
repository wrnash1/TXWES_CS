# Discussion Forum: Module 11 — Incident Detection and Response Procedures

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Discussion Overview

This discussion forum asks you to engage with realistic incident detection and response scenarios. The three scenarios cover detection architecture gaps, the containment trade-off decision, and the lessons-learned improvement process — the execution-level competencies that complete the CISM Domain 4 coverage begun in Module 10. Your posts should demonstrate that you can reason through these decisions using module frameworks rather than relying on general intuition.

---

## Forum Instructions

**Initial Post**: Respond to your assigned scenario (or any scenario if not assigned) with a response of **175–225 words** in complete, well-formed sentences. Write in paragraphs, not bullet points. Reference specific concepts, frameworks, or principles from the Module 11 material.

**Peer Responses**: Reply to **at least two classmates** who responded to a different scenario than your own. Each peer response must be a minimum of **60 words** and must add substantive value — extend the analysis, challenge an assumption, or connect the discussion to a concept from an earlier module.

**Due Dates**: Initial post due by Thursday 11:59 PM. Peer responses due by Sunday 11:59 PM.

---

## Scenario A — The Detection Architecture Gap

Keystone Energy operates natural gas distribution infrastructure across four southeastern states. The company's SOC uses a SIEM with 94 active correlation rules, a perimeter IDS, and traditional antivirus on all endpoints. Last year, Keystone invested $2.4 million in security technology.

During a routine third-party security assessment, the assessors discovered that a sophisticated threat actor had been present in Keystone's operational technology (OT) network for an estimated 47 days. The attacker had moved from the corporate IT network to the OT environment through an improperly segmented engineering workstation. The OT network had no EDR agents deployed (the equipment vendor said agents were "incompatible" with industrial control system software), no UEBA capability, and no dedicated NDR for the OT segment. The existing SIEM had no data sources from the OT network.

The attacker had read-only access to SCADA system configuration files. No operational disruption occurred. The breach was discovered only because the assessors were specifically probing OT-IT boundary controls.

**Discussion Prompt**: Analyze the detection architecture gap that allowed 47 days of undetected attacker presence in the OT environment. Identify specifically which detection capabilities were missing and explain what each would have contributed to earlier detection. Then, given that traditional EDR agents may genuinely be incompatible with some OT equipment, propose two compensating detection controls that Keystone could implement to provide detection coverage in environments where agent deployment is not possible. Ground your analysis in the detection technology framework from Module 11.

---

## Scenario B — The Containment Trade-off

GulfTech Pharmaceuticals is a mid-sized drug manufacturer subject to FDA regulations and processing proprietary drug formulation data — trade secrets worth an estimated $340 million in competitive value. On a Wednesday afternoon, GulfTech's IR team detects an active intrusion on RESEARCH-DB-04, the primary database server for the R&D division. Evidence indicates the attacker has been present for 6 days and has been systematically accessing files containing drug formulation data.

The IR team is split on the containment decision:

Position A (the Technical Lead): "We should covertly monitor the attacker for 24–48 more hours before isolating. We need to understand their full scope — what else have they accessed, what have they exfiltrated, where else in the environment are they? If we isolate now, we see only what we already know."

Position B (the CISO): "We need to isolate RESEARCH-DB-04 immediately. Every additional hour risks additional exfiltration of $340 million in trade secret data. We contain now and investigate what we have."

Both positions have merit. The company's legal counsel has just confirmed that there is no immediate regulatory obligation to delay containment.

**Discussion Prompt**: Analyze both positions using the evidence-versus-speed trade-off framework from Module 11. Explain the specific risks and benefits of each approach in this particular context — a pharmaceutical company with high-value trade secret data and a 6-day dwell time. Then argue for a specific course of action, explaining why the factors in this scenario favor the approach you recommend. Do not simply say "it depends" — commit to a position and justify it. Your analysis should acknowledge the strongest counterargument to your recommended position.

---

## Scenario C — Lessons Learned That Never Were

CivicTech Municipal Services provides IT services to 23 city government agencies. Over the past three years, CivicTech experienced four significant security incidents:

Year 1 — A ransomware attack affecting 7 file servers. Recovery took 11 days. A lessons-learned meeting was scheduled but canceled because the IT director said "everyone is too busy catching up from the downtime."

Year 2 — A phishing attack that compromised the email accounts of 14 employees including two city council members. No lessons-learned meeting occurred. The CISO documented the incident in a ticket and moved on.

Year 3 (February) — A credential stuffing attack on the citizen payment portal. Lessons-learned meeting held but attended only by three technical staff members. No executive was present. Findings were documented but no action items were assigned.

Year 3 (October) — A data breach affecting the same citizen payment portal compromised the same type of credentials as the February incident. Investigators determined that the vulnerability exploited in October had been identified as a finding in the February lessons-learned report — but no one had been assigned to remediate it.

**Discussion Prompt**: Analyze the organizational failure pattern illustrated across these four incidents. Explain specifically what went wrong at each stage of the lessons-learned process — not just "meetings weren't held" but the deeper governance and cultural failures that allowed the same vulnerability to persist from February to October of Year 3. Reference the lessons-learned structure from Module 11 and the IRP update authorization requirements. Then describe what a properly functioning lessons-learned program would have done differently after the February Year 3 incident that would have prevented the October breach.

---

## Peer Response Guidelines

When responding to a classmate, consider the following engagement approaches:

- For Scenario A responses: ask your classmate how they would prioritize the two compensating controls they proposed given a fixed budget — which would they fund first and why? Or challenge whether one of their proposed controls addresses the detection gap at the right layer.

- For Scenario B responses: ask your classmate whether their recommendation would change if the drug formulation data had already been confirmed exfiltrated rather than merely accessed — and if so, how and why. Or ask them to respond to the strongest counterargument against their position.

- For Scenario C responses: ask your classmate what governance structure change — not just a process change — would prevent the pattern of lessons-learned meetings being canceled or attendance being inadequate. Or challenge whether assigning action item owners alone is sufficient, and what accountability mechanism would ensure follow-through.

Peer responses that restate what the classmate wrote without adding a question, challenge, or extension will receive partial credit only.

---

## Grading Rubric — 10 Points Total

| Criterion | Points | Description |
|---|---|---|
| Content accuracy | 3 | Response accurately applies Module 11 frameworks and CISM Domain 4 concepts |
| Depth of analysis | 3 | Response identifies root causes and governance-level failures, not just surface descriptions; makes and defends a specific position where the scenario requires it |
| Specific framework reference | 2 | Response explicitly references at least one named framework, principle, or concept (detection technology stack, order of volatility, evidence vs. speed trade-off, lessons-learned structure, etc.) |
| Peer engagement quality | 2 | Both peer responses meet 60-word minimum and add substantive new content — a question, a challenge, or an analytical extension |
| **Total** | **10** | |

### Grade Descriptors

**9–10 points**: Initial post demonstrates deep engagement with module concepts, makes specific and defensible analytical claims, and references module frameworks correctly. Peer responses meaningfully advance the conversation.

**7–8 points**: Initial post applies most concepts correctly and reaches a reasoned conclusion. Peer responses are substantive but may lack analytical sharpness or framework grounding.

**5–6 points**: Initial post identifies relevant issues but remains descriptive rather than analytical. Peer responses meet length minimums but add limited intellectual value.

**Below 5 points**: Post does not meet length requirement, does not engage with the scenario, or applies no module frameworks.

---

## Professor Nash — Closing Note

These three scenarios represent the arc of incident response execution: what happens when your detection architecture has gaps (Scenario A), what the hardest real-time decision in incident response looks like (Scenario B), and what happens when the improvement loop breaks down (Scenario C).

Scenario B is the one I hear debated most often among practitioners. In my experience, the "monitor longer" argument is intellectually compelling and tactically seductive — and it is correct exactly often enough to make the decision genuinely hard. The pharmaceutical context changes the calculus significantly compared to a ransomware scenario where every second of delay means more encrypted files.

Scenario C is, in many ways, the most important scenario in this entire course. Technical controls are difficult and expensive. Governance processes — lessons-learned meetings, action item tracking, IRP updates — are inexpensive and entirely within the organization's control. And yet organizations consistently fail to execute them. Why? Because security governance is less urgent than putting out the fire. And then another fire starts.

That is the professional challenge you are training for. Not just putting out fires — building an organization that learns from each fire so that the next one is smaller. That is what CISM-level security management looks like.

See you in Module 12.

— Professor Nash
