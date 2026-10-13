# Discussion Forum: Module 02 - Azure Physical Architecture

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 | **Initial Post Due:** Wednesday 11:59 PM | **Peer Responses Due:** Sunday 11:59 PM

---

## Overview

This discussion asks you to apply Azure's physical architecture concepts — regions, Availability Zones, region pairs, management hierarchy — to real organizational decision-making. Architecture decisions have direct consequences for uptime, compliance, cost, and management complexity. The ability to reason through these trade-offs clearly is a core skill for Azure practitioners and is tested in AZ-900 scenario questions.

Read all three scenarios. Choose **one scenario** for your initial post. Identify your scenario choice at the start of your post.

---

## Scenario A: The Retail Chain Reliability Design

FastMart is a national retail chain with 800 stores across the continental United States. They are migrating their point-of-sale transaction processing system to Azure. The system must meet a 99.99 percent uptime SLA because even brief outages prevent customers from completing purchases. FastMart's legal team has confirmed that POS transaction data must remain within the United States. The initial deployment region under consideration is East US. The development team lead has proposed deploying all POS processing virtual machines to a single Availability Zone to simplify the deployment configuration.

In 175-225 words, address all of the following:

- Evaluate the development team lead's proposal to use a single Availability Zone. Does this meet the 99.99 percent uptime requirement? Use the SLA table from the reading guide to support your answer.
- What specific change to the deployment architecture would achieve the 99.99 percent SLA target while staying within East US?
- The legal team's US data residency requirement is already satisfied by East US, but the architecture team wants to add geo-redundant disaster recovery. Which paired region would they replicate to, and does that replication destination satisfy the US data residency requirement?

---

## Scenario B: The University Cloud Strategy

Texas Wesleyan University (fictional scenario — not actual TXWES IT policy) is designing its Azure management hierarchy. The university has four colleges (Business, Science, Arts, and Education), a central IT department, and a research office that handles federally funded grants. The Provost's office requires that all university Azure spending appear in a single monthly invoice. The IT Security office needs to enforce a baseline security policy across all college deployments without configuring it separately for each college. The Research office has strict data governance requirements because some grants include export-controlled data under ITAR regulations.

In 175-225 words, address all of the following:

- Design the management group and subscription structure that satisfies both the unified billing requirement and the organization-wide security policy requirement. Explain which hierarchy level you use for each requirement and why.
- The Research office's ITAR requirement is the most complex constraint. What Azure deployment approach — standard region with compliance configurations, Azure Government, or another option — would you recommend for the export-controlled research workloads? Justify your recommendation.
- Propose a naming convention for the subscriptions in your design. A good naming convention communicates the organization unit, environment, and purpose at a glance. Share your convention and give two example subscription names.

---

## Scenario C: The Multinational Compliance Problem

GlobalEdge Analytics is a data analytics company headquartered in Dallas with offices in Germany, Japan, and Canada. They are building a customer data analytics platform that will process customer behavioral data. German customers are covered by GDPR, which requires their personal data to remain within the European Union. Japanese regulations require that Japanese resident data be stored within Japan. Canadian data must remain in Canada. The US data has no geographic restriction. The platform must provide consistent response times globally.

In 175-225 words, address all of the following:

- How many Azure regions does this architecture require at a minimum, and which specific regions would you select? Name each region and the regulatory requirement it satisfies.
- The company's operations team wants to minimize management overhead. They propose using a single Azure subscription for all four geographic deployments. Is this feasible from a technical standpoint? Is it advisable from a compliance and governance standpoint? Explain.
- The US deployment has no geographic restriction but must serve as the primary analytics processing hub with the lowest-latency connection to the Dallas headquarters. Which US region would you select and why?

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5-6 pts | Scenario identified at start. All three sub-questions addressed with accurate technical content. Uses correct Azure architecture terminology (Availability Zones, region pairs, management groups, subscriptions). Word count 175-225. Analysis is original — not a restatement of definitions. |
| 3-4 pts | Most sub-questions addressed. Minor technical inaccuracies. Word count may be slightly outside range. |
| 1-2 pts | Only one or two sub-questions addressed, or significant technical errors. |
| 0 pts | No initial post submitted by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive responses to at least two classmates. Each response is 75+ words and provides specific technical feedback: challenges an assumption, adds a constraint not considered, proposes an alternative architecture element, or extends the analysis with a real-world implication. |
| 2-3 pts | Two responses submitted but one or both are under 75 words or lack technical substance. |
| 1 pt | Only one response, or both are superficial. |
| 0 pts | No peer responses by Sunday deadline. |

---

## Professor Nash's Note

Architecture decisions in real cloud environments are rarely made with perfect information. You will have incomplete requirements, budget constraints, and organizational politics all pushing in different directions. The value of these discussions is not finding the one "right" answer — it is practicing the discipline of reasoning through trade-offs transparently and communicating your architectural rationale to stakeholders who may not have your technical background. When you can explain to a compliance officer *why* you chose Germany West Central over North Europe, or explain to a CFO *why* a separate subscription for R&D protects the company from accidental budget overruns, you are delivering real professional value. That skill starts here.
