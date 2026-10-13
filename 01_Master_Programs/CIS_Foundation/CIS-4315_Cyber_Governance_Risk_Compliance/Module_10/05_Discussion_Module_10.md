# Discussion Forum: Module 10 — Incident Management Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Discussion Overview

This discussion forum asks you to engage with realistic incident management planning scenarios drawn from the types of situations security managers encounter in practice. The scenarios test your understanding of IRP structure, team design, communication planning, and escalation procedures — all core competencies in CISM Domain 4. Your posts should demonstrate that you can apply module frameworks to analyze situations, not merely describe what those frameworks say.

---

## Forum Instructions

**Initial Post**: Respond to your assigned scenario (or any scenario if not assigned) with a response of **175–225 words** in complete, well-formed sentences. Write in paragraphs, not bullet points. Reference specific frameworks, principles, or concepts from the module material to support your analysis.

**Peer Responses**: Reply to **at least two classmates** who responded to a different scenario than your own. Each peer response must be a minimum of **60 words** and must engage substantively — extend the analysis, raise a follow-up question, or offer a counter-perspective based on the module material.

**Due Dates**: Initial post due by Thursday 11:59 PM. Peer responses due by Sunday 11:59 PM.

---

## Scenario A — The Unexercised Plan

Thornwood Manufacturing discovered on a Tuesday morning that attackers had been present on its network for 11 days, had accessed intellectual property files on the engineering drive, and had attempted — unsuccessfully — to exfiltrate a 4.2 GB archive. The IR team activated the Incident Response Plan for the first time in a real incident. Within the first four hours, several problems surfaced:

- The IRT contact list had three phone numbers that were no longer valid.

- The Communications Lead had left the company eight months ago and had not been replaced in the plan.

- The CFO refused to authorize isolation of the engineering server because it was needed for an active client delivery.

- Legal counsel had never seen the IRP before and asked for 24 hours to review it before any external notifications were sent.

The IRP itself was technically well-written and had been approved by the board two years ago. It had never been tested.

**Discussion Prompt**: Analyze the specific failures exposed in this scenario. Which of these failures could have been prevented by a plan testing program, and which represent gaps in the IRP design itself? Reference NIST SP 800-61's guidance on preparation and plan maintenance, and explain what specific actions Thornwood should take immediately after this incident to prevent recurrence. Your response should go beyond listing the problems and explain why each failure occurred at the governance level.

---

## Scenario B — The Communication Cascade Failure

Brightpath Insurance experienced a confirmed data breach at 6:47 PM on a Friday. The on-call analyst classified the incident as High severity, confirmed that customer PII records were accessed, and began technical containment. The analyst then faced these communication decisions:

- The CISO was on a flight and would be unreachable for four hours.

- The IRP notification chain listed the CISO as the sole authority to approve external communications.

- The cyber insurance policy required notification within 24 hours of a confirmed breach.

- The state breach notification law required customer notification but had no explicit deadline for carrier notification.

- A local news reporter had already called the main office asking about a "cybersecurity incident" — apparently tipped off by a post on a monitoring website that tracks dark web activity.

The analyst felt paralyzed — unable to call the CISO, uncertain about regulatory deadlines, and receiving an inquiry from the press.

**Discussion Prompt**: Evaluate the specific IRP design failures that created this paralysis. Reference the communication plan components and out-of-band communication principles from Module 10. Then describe what a well-designed IRP would have provided the analyst to handle each of the three specific challenges: the unavailable CISO, the cyber insurance 24-hour deadline, and the media inquiry. Your response should explain the principle behind each design element you recommend, not just list the elements.

---

## Scenario C — Scope and Authorization Conflict

DataVault Corp stores sensitive financial records for hedge funds and investment banks. Following a routine penetration test, a tester discovered that a configuration error in the cloud environment had exposed customer data for approximately 90 days. The CISO activated the IRP. During the response, two significant conflicts emerged:

Conflict 1: The forensic investigator determined that the exposed data included records from EU-based clients, triggering a GDPR notification obligation with a 72-hour deadline. However, DataVault's legal counsel was reviewing the exposure scope and estimated the review would take five to seven business days. The 72-hour window would expire before legal counsel completed the review.

Conflict 2: To fully contain the exposure, the IR team needed to temporarily disable external API access to the cloud environment. Two major clients had SLAs guaranteeing 99.9% uptime. Disabling the API would violate those SLAs and potentially trigger contractual penalties. The IR Manager wanted to proceed; the COO wanted to wait for client approval, which would take at minimum 48 hours to obtain.

**Discussion Prompt**: Analyze each conflict using CISM Domain 4 principles and the IRP planning framework from Module 10. For Conflict 1, explain how a well-designed IRP would address the tension between legal review timelines and regulatory notification deadlines. For Conflict 2, explain why the system isolation authority in the IRP must address SLA and contractual considerations in advance, and what the appropriate resolution is. Your analysis should reference the concept of pre-negotiated decision authorities and explain the consequences of the delays being proposed.

---

## Peer Response Guidelines

When responding to a classmate, consider these engagement approaches:

- For Scenario A responses: ask your classmate what specific exercise format (tabletop, functional, or full-scale simulation) would have caught each specific failure they identified, and why.

- For Scenario B responses: ask your classmate how they would handle the media inquiry specifically — what would the holding statement say, and who has authority to release it in the CISO's absence?

- For Scenario C responses: ask your classmate whether their proposed resolution for either conflict would change if DataVault's clients were US-only rather than including EU clients — and why.

Peer responses that only validate the classmate's analysis without adding a question, extension, or counter-perspective will receive partial credit.

---

## Grading Rubric — 10 Points Total

| Criterion | Points | Description |
|---|---|---|
| Content accuracy | 3 | Response accurately applies module frameworks and CISM Domain 4 principles |
| Depth of analysis | 3 | Response diagnoses root causes and explains governance-level reasoning, not just surface symptoms |
| Specific framework reference | 2 | Response explicitly references at least one named framework or principle (NIST SP 800-61, RACI, escalation criteria, communication plan components, etc.) |
| Peer engagement quality | 2 | Both peer responses meet 60-word minimum and add substantive new content |
| **Total** | **10** | |

### Grade Descriptors

**9–10 points**: Initial post demonstrates thorough understanding of IRP design principles, correctly identifies governance-level root causes, and provides specific actionable recommendations. Peer responses extend the conversation meaningfully.

**7–8 points**: Initial post applies most concepts correctly and identifies relevant gaps. Peer responses are substantive but may lack specificity or framework grounding.

**5–6 points**: Initial post shows basic familiarity but primarily lists problems without governance analysis or framework reference. Peer responses meet length minimums but add limited value.

**Below 5 points**: Post does not meet length requirement, applies no module frameworks, or does not engage with the scenario.

---

## Professor Nash — Closing Note

The three scenarios in this forum are not hypothetical — they are composites of real incidents that I have either worked on or studied closely. The analyst paralyzed on a Friday night because the CISO was unreachable is not an unusual situation. The conflict between a forensic hold and a DRP recovery time objective is an argument that happens in virtually every major incident involving production systems. The gap between "we have an IRP" and "the IRP works when we need it" is one of the most common and dangerous deficiencies in enterprise security programs.

This is why the CISM exam dedicates an entire domain to incident management and why ISACA requires not just that a plan exists, but that it is tested, maintained, and authorized. A plan on a shelf has never stopped an attacker.

When you engage with these scenarios, try to inhabit the role of the person who has to make the decision at 11 PM with incomplete information and a phone that won't connect to the CISO. That is the reality of incident management. The goal of planning is to make that moment as structured and as clear as possible — so that good decisions happen even under pressure.

See you in the forum, and see you in Module 11, where we put the plan into action.

— Professor Nash
