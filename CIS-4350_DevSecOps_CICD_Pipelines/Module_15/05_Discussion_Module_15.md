# Discussion Forum: Module 15 — Security Champions and DevSecOps Culture

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Discussion Prompt

This week's discussion asks you to connect the organizational and cultural concepts from Module 15 to real-world practice. Security Champion programs, DORA metrics, and maturity models are not abstract theory — they are the frameworks organizations use to make DevSecOps sustainable at scale. This prompt asks you to apply those frameworks to a specific scenario and to engage critically with your classmates' approaches.

### Scenario

You are a senior engineer at a 250-person software company. The company has a 4-person Application Security team and 30 development engineers across 5 teams. The security team has recently deployed SAST and SCA tools across all pipelines, but both gates are set to warn-only because "we do not want to slow down engineering." The finding backlog has grown to 900 open items. There are no Security Champions. Engineers rarely read scan output because there is too much noise. Three engineers on the payments team have expressed genuine interest in security and have been informally helping teammates interpret findings.

---

### Your Tasks

**Initial Post (Due Wednesday at 11:59 PM)**

In 200–250 words, respond to the following:

1. Identify which DevSecOps transformation failure mode (or modes) the scenario demonstrates. Name the failure mode using the terminology from Module 15 and explain the specific evidence from the scenario that supports your identification.

2. Propose one concrete first action the organization should take to begin addressing the failure. Explain why you chose this action as the starting point rather than other possible interventions (for example, why enabling mandatory gates or hiring more security staff might not be the best first step).

3. Describe how you would formalize the three engineers on the payments team as Security Champions. What authority would you give them immediately, and what training would you recommend in their first 30 days?

---

**Peer Responses (Due Sunday at 11:59 PM)**

Read through your classmates' initial posts and write constructive replies of at least 75 words each to at least two peers. In your replies, address one of the following:

- Do you agree with your peer's identification of the failure mode? If they identified a different failure mode than you did, explain your reasoning for why you agree or disagree with their analysis.
- Evaluate your peer's proposed first action. Is it sequenced correctly? Would it address the root cause or a symptom? Suggest one refinement or alternative.
- Compare your peer's champion formalization approach to your own. What did they include that you did not? What would you add or change?

---

## Instructor Notes for Grading

Strong initial posts will:

- Correctly name the failure mode using Module 15 terminology (Security Theater, Tool Accumulation Without Process, or Security as Bottleneck) with specific textual evidence from the scenario
- Propose a first action that addresses root cause rather than symptom (for example, establishing a champion triage process before enabling mandatory gates addresses the human infrastructure gap; enabling mandatory gates before fixing the noise problem escalates the theater failure mode)
- Reference specific training resources by name (OWASP Top 10, OWASP ASVS, SANS DEV541, or equivalent) in the champion formalization response

Strong peer responses will engage substantively with the peer's reasoning — not just affirm or deny the conclusion, but analyze the logic.

---

## Discussion Rubric

| Component | Points | Criteria |
|---|---|---|
| Initial Post — Failure Mode Identification | 3 | Correct failure mode named with specific scenario evidence; uses Module 15 terminology |
| Initial Post — First Action Proposal | 2 | Action addresses root cause; sequencing rationale is explained; references specific tools or processes |
| Initial Post — Champion Formalization | 2 | Specific authority defined; named training resources; 30-day plan is realistic |
| Peer Response 1 | 1.5 | Substantive engagement with peer's reasoning; at least 75 words; adds new perspective |
| Peer Response 2 | 1.5 | Substantive engagement with peer's reasoning; at least 75 words; adds new perspective |
| **Total** | **10** | |

---

## Optional Extension Prompt

If you finish early and want to go deeper, consider this extension question (not graded, but worth discussing):

The scenario describes three engineers on the payments team who are informally helping teammates with security findings. One approach is to formalize all three as champions immediately. Another approach is to start with one champion and scale gradually.

What are the trade-offs between formalizing all three at once versus starting with one? Consider factors like training investment, coverage across the rest of the five teams, and the risk that all three champions might leave the company within 12 months. Post your thoughts as a reply to any peer who also engaged with the extension, or start a new thread.
