# Discussion: Module 05 — Risk Treatment and Control Selection

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

---

## Overview

This week's discussion scenarios ask you to apply the full risk treatment decision framework — choosing between avoidance, transfer, mitigation, and acceptance, selecting appropriate controls, and reasoning through cost-benefit trade-offs. As with previous discussions, your goal is to demonstrate analytical judgment, not just recall of definitions. Use precise terminology and connect your reasoning directly to the facts of each scenario.

---

## Due Dates

- Initial post: Wednesday at 11:59 PM
- Peer responses: Sunday at 11:59 PM

---

## Scenario A — When Risk Acceptance Goes Wrong

CrownTech Solutions is a software-as-a-service company that provides project management tools to mid-market enterprises. Two years ago, a junior security analyst flagged a known SQL injection vulnerability in the company's API layer in a routine assessment report. The report was reviewed by the then-CISO, who noted the risk but did not formally document a treatment decision, assign an owner, or enter the vulnerability in the risk register. No controls were implemented. Six months ago, CrownTech hired a new CISO. Last week, an attacker exploited the SQL injection vulnerability to extract the personal data of 180,000 customers. During the post-incident review, the new CISO discovers the two-year-old assessment report. Senior leadership asks: "Did we formally accept this risk two years ago?"

In 175–225 words, respond to the following questions in complete sentences.

Was the previous CISO's inaction formal risk acceptance, informal acceptance, or something else entirely? Explain the difference with precision. What governance failures does this scenario illustrate, and which specific elements were missing that would have made a formal acceptance legitimate? If the previous CISO had wanted to formally accept this risk two years ago — rather than mitigate it — what specific steps would have been required to do so properly? Conclude by explaining the practical consequence of the governance failure in the context of a regulatory investigation or litigation: why does the absence of formal documentation matter to a regulator or plaintiff's attorney?

---

## Scenario B — The Insurance Debate

Magnolia Mortgage Company processes approximately $2.4 billion in residential mortgage applications annually and stores extensive personal and financial data on applicants. The CISO has completed a risk assessment that places the ransomware risk at an ALE of $890,000. The CISO proposes a combination of endpoint detection and response (EDR) software, immutable cloud backups, and a security awareness training program at a combined annual cost of $185,000 — which would reduce the ALE to $120,000. The CFO pushes back: "Instead of spending $185,000 on controls, let's just buy a $2 million cyber insurance policy for $95,000 per year. That's cheaper, and if something happens, we're covered."

In 175–225 words, respond to the following questions in complete sentences.

Evaluate the CFO's argument on its merits. Is the CFO's comparison of $185,000 versus $95,000 an accurate picture of the financial trade-off? What does the CFO's framing leave out? Explain specifically what cyber insurance does and does not cover that is relevant to Magnolia's situation as a mortgage company. Then present the CISO's strongest counter-argument — not as a rejection of insurance, but as a case for why controls and insurance serve different purposes and should be used together. What is the optimal risk treatment strategy for the ransomware risk, incorporating both the cost-benefit analysis and the limitations of insurance?

---

## Scenario C — Control Selection for a Healthcare Startup

PulsePoint Health is a 60-employee health technology startup that has just launched a telehealth platform connecting patients with licensed therapists. The platform handles protected health information (PHI) including session notes, diagnoses, and prescription histories. The startup's founding CTO — who has a software engineering background but no formal security training — has implemented the following controls: HTTPS encryption for all data in transit, a password policy requiring eight-character minimum passwords, and a shared admin account used by all engineers for database access.

The company has just hired its first security manager, who immediately identifies significant gaps. The board asks the security manager to prioritize the three most critical control improvements, justify each recommendation, and identify the functional type and implementation method of each proposed control.

In 175–225 words, respond to the following questions in complete sentences.

Identify the three most critical control gaps in PulsePoint's current security posture — not just what controls are missing, but why each gap is particularly serious in the context of a telehealth platform handling PHI. For each gap, recommend a specific control, state its functional type and implementation method, and explain how it directly reduces the identified risk. Then address the following governance question: given that PulsePoint's CTO implemented the existing controls without formal risk assessment or documented treatment decisions, what foundational risk management activity should the new security manager complete before selecting any additional controls? Explain why this activity is a prerequisite rather than an optional step.

---

## Peer Response Requirements

After submitting your initial post, read your classmates' responses and write substantive replies to at least two peers.

Each peer response must be at least 60 words and must accomplish one of the following.

- Offer a different perspective on the risk treatment trade-offs your peer analyzed, with specific reasoning
- Identify a regulatory consideration — HIPAA, PCI DSS, state data breach law, or other applicable requirement — that your peer's analysis did not address and explain its relevance
- Extend your peer's control recommendations by suggesting a complementary control from a different functional type or implementation method, explaining how it strengthens the defense-in-depth posture

Responses that simply affirm your peer's conclusions without adding new reasoning will not receive peer response credit.

---

## Grading Rubric — 10 Points Total

| Criterion | Points | Full Credit Description |
|-----------|--------|------------------------|
| Initial post addresses all scenario questions | 3 | All required questions answered substantively; no question skipped or only superficially addressed |
| Risk treatment and control terminology is accurate | 3 | Treatment options, control functional types, and implementation methods all used correctly; no factual errors |
| Writing quality and word count | 2 | 175–225 words; complete sentences; professional tone; organized response |
| Peer responses (two required) | 2 | Two responses submitted by Sunday; each is 60+ words; each contributes new analysis beyond agreement |

---

## A Note from Professor Nash

The three scenarios this week cover the full range of Module 05 content: governance failure in risk acceptance (Scenario A), the insurance-versus-controls debate that every security leader eventually faces (Scenario B), and practical control selection for a real-world environment (Scenario C).

Pay particular attention to Scenario B. The CFO's argument is not unreasonable on its surface — $95,000 is less than $185,000. Your job is to engage seriously with that logic and explain precisely where it falls short, using the concepts from this module. Dismissing the CFO's view without engaging with its merits will not receive full credit. The best responses will acknowledge the legitimate points in the CFO's position while building a clear, evidence-based case for the CISO's approach.

This is the kind of conversation you will have with finance leaders throughout your career. Practice making it well.
