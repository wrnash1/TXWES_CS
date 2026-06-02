# Discussion Forum: Module 01 - Cloud Computing Concepts

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 | **Initial Post Due:** Wednesday 11:59 PM | **Peer Responses Due:** Sunday 11:59 PM

---

## Overview

This discussion asks you to apply the conceptual frameworks from Module 01 — service models, deployment models, the Shared Responsibility Model, and CAPEX vs. OPEX — to realistic organizational scenarios. These are the types of situations you will encounter as an IT professional or cloud architect, and they represent the applied reasoning that AZ-900 scenario questions test.

Read all three scenarios below. Choose **one scenario** for your initial post. You must identify which scenario you selected at the beginning of your post.

---

## Scenario A: The Regional Hospital System

MidSouth Health Network operates 12 hospitals across three states. They currently run all clinical applications — electronic health records, medical imaging storage, and patient scheduling — on servers in a single on-premises data center. The IT director has been tasked with evaluating a cloud migration strategy. Key constraints include HIPAA compliance for all patient data, a requirement that diagnostic imaging files (averaging 500 GB per scan session) remain accessible within 2 seconds from any hospital location, and a state regulation requiring that patient data reside within U.S. borders. The network has 8,000 clinicians who access the systems simultaneously during peak shift hours.

In 175-225 words, address all of the following:

- Which cloud deployment model (public, private, or hybrid) would you recommend for MidSouth Health Network, and why? Be specific about which workloads would go where.
- Identify one layer of the Shared Responsibility Model where the hospital's IT team retains accountability regardless of which service model they choose for clinical applications.
- Explain how the proposed cloud architecture changes MidSouth's spending from a CAPEX perspective. What financial risk does this eliminate?

---

## Scenario B: The Fast-Growth SaaS Startup

NovaBuild Technologies is a 12-person startup that has built a construction project management application. They expect to grow from 200 customers to 20,000 customers within 18 months based on a signed distribution agreement with a national construction equipment vendor. Their lead developer wants to deploy the application backend to Azure App Service with Azure SQL Database. The CTO is questioning whether they should instead rent dedicated servers from a colocation provider to maintain full OS-level control and reduce per-unit cost at scale.

In 175-225 words, address all of the following:

- Evaluate the CTO's concern about OS-level control. Is that control necessary for this use case? Use the IaaS vs. PaaS framework from Module 01 to support your position.
- The growth scenario (200 to 20,000 customers in 18 months) involves a specific cloud characteristic that makes Azure App Service the more appropriate choice than a fixed colocation server lease. Name that characteristic and explain why it is critical here.
- How does the startup's financial situation (12 people, early-stage) influence the CAPEX vs. OPEX analysis? What risk does the colocation option introduce that cloud eliminates?

---

## Scenario C: The State Government Agency

The Texas Department of Transportation manages a statewide road condition monitoring system. The system collects sensor data from 45,000 road segments every 15 minutes, stores 7 years of historical data for trend analysis, and serves a public-facing website showing real-time road conditions to drivers. A state legislature mandate requires that all citizen data be stored on state-owned infrastructure. However, the agency's IT staff of six cannot manage the current on-premises servers and the analytics workloads simultaneously during winter weather events when demand spikes dramatically.

In 175-225 words, address all of the following:

- The legislature's mandate creates a constraint that rules out one deployment model entirely. Identify which model is ruled out and explain why.
- Given the remaining options and the demand spike problem, which deployment model do you recommend? Describe which components of the system would be placed in each environment.
- Identify whether the public-facing road conditions website is better suited to IaaS or PaaS, and explain your reasoning based on the staffing constraint (IT team of six).

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5-6 pts | Correctly identifies scenario choice. Addresses all three sub-questions with technical accuracy. Uses Module 01 vocabulary (service model names, deployment model names, CAPEX/OPEX, Shared Responsibility). Word count is 175-225 words. Demonstrates original analysis rather than restating definitions. |
| 3-4 pts | Addresses most sub-questions but lacks depth on one or more. Minor inaccuracies in service/deployment model application. Word count may be slightly outside range. |
| 1-2 pts | Post is incomplete or addresses only one sub-question. Significant technical inaccuracies. Word count substantially below minimum. |
| 0 pts | No initial post submitted by the Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Responds to at least two classmates who chose different scenarios from each other (or different from your own). Each response is at least 75 words and contributes substantive technical feedback: agreeing or disagreeing with a specific recommendation, adding a constraint the original poster may not have considered, or connecting the scenario to a concept from the reading guide. |
| 2-3 pts | Responds to two peers but one or both responses are under 75 words or lack substantive technical content. |
| 1 pt | Only one peer response submitted, or both responses are superficial ("Great post! I agree."). |
| 0 pts | No peer responses submitted by the Sunday deadline. |

---

## Professor Nash's Note

These three scenarios are drawn from the types of cloud strategy conversations that happen in real organizations. When you are evaluating a client's environment or advising an IT manager, you will rarely have a clear-cut "use public cloud" or "use private cloud" answer — you will have constraints, regulations, budget pressures, and staffing realities that all push in different directions. The goal of this discussion is for you to practice reasoning through those competing factors using a precise technical vocabulary. Future employers will evaluate whether you can communicate cloud architecture decisions clearly and justify your reasoning. This discussion is practice for that professional skill.
