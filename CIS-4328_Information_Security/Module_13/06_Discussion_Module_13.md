# Discussion: Module 13 — Risk Management for Security+

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Discussion Overview

**Forum Title:** Risk Decisions in Practice — When Security and Business Goals Collide

**Points:** 50 points total (Initial post: 30 points | Two peer responses: 10 points each)

**Deadline:** Initial post due by Day 4 of the module week; peer responses due by Day 7

---

## Background

Risk management sounds clean and systematic in textbooks: identify risks, assess them, apply the right response, document everything. In practice, risk decisions are made by people with competing priorities, limited information, and real organizational pressures.

Consider the Theranos case: the company accepted enormous operational risks in pursuit of growth, ignored internal warnings about technical failures, and framed their acceptance of those risks as "moving fast" and "disrupting healthcare." The consequences were dire — patients received incorrect test results that affected medical treatment, the company collapsed, and its founder was convicted of fraud.

At the other end of the spectrum, organizations that apply excessive risk aversion — refusing to implement new technologies because "we haven't done it before" — lose competitive advantage, frustrate employees, and often end up with shadow IT problems (employees using unapproved tools because approved options are insufficient).

Finding the right balance — informed, defensible risk decisions that align with organizational strategy — is the core competency this module develops.

---

## Initial Post Prompt

Choose ONE of the two scenarios below. Identify your choice at the top of your post.

### Scenario A — The Acceptable Risk Debate

A mid-sized law firm specializing in intellectual property litigation evaluates a risk: their attorneys frequently email sensitive case documents to clients, co-counsel, and expert witnesses. The documents often contain confidential client communications and attorney work product. The email system is encrypted in transit (TLS) but attachments are not individually encrypted.

A risk assessment identifies this as a High risk. The security team recommends implementing an enterprise Digital Rights Management (DRM) solution that would encrypt all attachments and restrict forwarding. Cost: $180,000/year.

The managing partners push back: "Our clients expect to be able to forward documents. If we lock down documents, we lose business. We will accept this risk."

Address all of the following in your post:

1. Is "we will accept this risk" a valid risk response in this scenario? What specific conditions must be met for risk acceptance to be defensible? Apply the concepts from this module — this is not a yes/no question.

2. The managing partners are making a business decision that has security consequences. Using the concept of risk appetite, evaluate whether their response is consistent with a law firm's appropriate risk posture. (Consider: what are a law firm's obligations to clients regarding confidentiality?)

3. Calculate a simplified ALE for this risk using reasonable assumptions. Show your work. (Assume: AV = $2,000,000 representing client data and professional reputation; EF = 0.30; ARO = 0.15.) Is the $180,000/year DRM solution financially justified by the numbers alone?

4. What risk response alternative — other than the full DRM solution — might reduce the risk to an acceptable level at a lower cost? Propose a specific control and explain how it changes the risk equation.

### Scenario B — The BIA That Nobody Took Seriously

A regional grocery chain with 45 stores operates a point-of-sale (POS) system that processes all customer transactions. The IT director commissioned a Business Impact Analysis three years ago. The BIA identified the POS system as having an MTD of 4 hours and recommended an RTO of 2 hours.

The BIA report sat on a shelf. No disaster recovery plan was updated. No backup POS system was procured. Eighteen months later, a ransomware attack encrypts the POS system servers. Stores resort to cash-only transactions, losing an estimated $150,000 in sales per hour. Twelve hours into the outage, two stores close entirely. Recovery takes 22 hours total.

Address all of the following in your post:

1. The BIA correctly identified the MTD as 4 hours, but the actual outage lasted 22 hours. Map the specific failure to the gap between MTD, RTO, and the actual outage duration. What was the theoretical cost of the gap between the recommended RTO (2 hours) and the actual recovery time (22 hours)?

2. The IT director argues: "We did the BIA. We identified the risk. The organization chose not to fund the recovery solution — that is risk acceptance." Is this a valid claim? What distinguishes legitimate risk acceptance from negligence? What documentation and process would have been required for this to constitute valid risk acceptance?

3. Had a formal risk register been maintained, what specific fields would have flagged this risk as requiring senior leadership attention before the incident occurred? Who should have been the Risk Owner for this entry?

4. After the incident, the CEO asks: "What is the total financial impact of our failure to implement the recommended BIA controls?" Structure a complete response using the concepts of ALE, actual loss, and the cost of the missed mitigation. Use the $150,000/hour loss figure and the 22-hour outage in your analysis.

---

## Initial Post Requirements

- Minimum length: 450 words
- Maximum length: 750 words
- Use proper paragraph structure
- Show calculation work explicitly for any quantitative questions
- Reference at least one assigned reading from the Module 13 Reading Guide
- Defend your conclusions — unsupported opinions earn partial credit

---

## Peer Response Requirements

Respond substantively to two classmates. Each response must:

- Minimum length: 150 words
- Either add an analysis point the original poster did not address, challenge a conclusion with reasoning, or extend the quantitative analysis with an alternative assumption
- Financial/quantitative responses that alter the numbers with different assumptions are especially welcome — explain your alternative inputs

---

## Grading Rubric

### Initial Post (30 points)

| Criterion | Excellent (Full Credit) | Satisfactory (Partial) | Insufficient |
|---|---|---|---|
| Risk concept application (Q1 + Q2 / Q1 + Q2) | Applies module vocabulary accurately; distinguishes concepts correctly (8 pts) | Correct concepts named without distinction (5 pts) | Vague or incorrect (0–2 pts) |
| Quantitative analysis (Q3 / Q4 calculation) | Shows correct work; reaches correct conclusion; interprets result (8 pts) | Attempt at calculation with errors; interpretation present (5 pts) | No calculation attempted (0–2 pts) |
| Risk management recommendation (Q4 / Q3) | Specific, actionable, grounded in module concepts (7 pts) | Recommendation made without grounding (4 pts) | Missing (0–2 pts) |
| Strategic reasoning quality (Q2 / Q2 + Q3) | Demonstrates integrated thinking about business and security tradeoffs (7 pts) | States a position without analysis (4 pts) | Not attempted (0–2 pts) |

### Peer Responses (10 points each)

| Criterion | Full Credit | Partial | Minimal |
|---|---|---|---|
| Substantive extension or challenge | New point, reasoned challenge, or quantitative alternative (7 pts) | Minor addition or restatement (4 pts) | Agreement only (0 pts) |
| Length and professionalism | 150+ words, respectful (3 pts) | Under 150 words or informal (1 pt) | Under 75 words (0 pts) |

---

## Instructor Notes

Scenario A generates strong debate around the "business decision vs. security decision" boundary and whether risk acceptance can override professional obligations (attorneys have Bar-mandated client confidentiality duties that constrain their risk appetite — a point students often miss). Scenario B is designed to illustrate that doing a BIA without acting on it provides almost no security value — and may actually increase liability by documenting knowledge of the risk without treatment.

The Q4 financial calculation in Scenario B should yield approximately $3.3 million in direct sales losses (22 hours × $150K) and should be compared against a BIA-driven recovery investment. Exact numbers depend on student assumptions — any reasonable, justified calculation earns full marks.

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 13*
