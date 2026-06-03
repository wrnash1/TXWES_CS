# Discussion Forum: Module 12 - Azure Governance and Compliance

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 | **Initial Post Due:** Wednesday 11:59 PM | **Peer Responses Due:** Sunday 11:59 PM

---

## Overview

Cloud governance failures are not hypothetical risks — they result in real compliance violations, audit findings, regulatory fines, and security incidents. The Azure governance tools in this module exist because organizations cannot manually review every resource configuration across hundreds of subscriptions. Policy, management groups, and compliance dashboards automate what would otherwise require armies of auditors. This discussion asks you to apply governance thinking to realistic organizational scenarios.

Read all three scenarios. Choose **one scenario** for your initial post. Identify your scenario at the start of your post.

---

## Scenario A: The Governance Debt Reckoning

Pinnacle Insurance Group has been using Azure for four years. In the early days, subscriptions were provisioned quickly to meet business demands, and governance was not a priority. Today they have 22 subscriptions with the following problems discovered during an external audit:

- Resources in 18 of 22 subscriptions have no consistent tagging — cost attribution reports are impossible to produce
- 7 subscriptions have resources deployed in Southeast Asia and South America, violating their data residency policy requiring all data to stay within the US
- 4 subscriptions have storage accounts with public blob access enabled, creating potential data exposure risks
- There is no management group hierarchy — all subscriptions sit directly under the Root Management Group without any organizational structure

The cloud governance team has been tasked with implementing a governance framework in 60 days without disrupting existing production workloads.

In 175-225 words, address all of the following:

- Design a management group hierarchy for Pinnacle Insurance. How many management groups would you create and how would you organize the 22 subscriptions? Justify the design based on their governance needs.
- For the data residency violation (resources in Southeast Asia and South America), which Azure Policy effect would you use to prevent future violations? Why would you NOT immediately switch to a Deny effect for this policy given that production workloads exist in those regions?
- For the tagging problem, describe a Policy approach using the Modify effect rather than Deny to remediate existing untagged resources without blocking current operations. What is the limitation of Modify for resources that already exist without tags?

---

## Scenario B: The Healthcare Compliance Architecture

Meridian Health Network is a regional hospital system migrating from on-premises infrastructure to Azure. They are subject to HIPAA, which requires strict controls around protected health information (PHI). Their compliance team has identified three specific HIPAA technical safeguard requirements they need to address:

- Requirement 1: All PHI data at rest must be encrypted
- Requirement 2: Access to systems containing PHI must be logged and auditable
- Requirement 3: PHI data must be discoverable — the organization must know what PHI they hold and where it lives

The cloud architect proposes using three Azure services to address these requirements: Azure Policy for encryption enforcement, Defender for Cloud for audit logging, and Microsoft Purview for PHI data discovery. The compliance officer is skeptical, asking: "How does configuring Azure resources help me prove HIPAA compliance? HIPAA talks about patient data, not resource configurations."

In 175-225 words, address all of the following:

- For Requirement 1 (encryption at rest), describe a specific Azure Policy configuration that would enforce encryption on Azure SQL Databases and Azure Storage accounts. What effect would you use, and at what scope would you assign the policy to cover all hospital subscriptions?
- For Requirement 3 (PHI data discovery), explain what Microsoft Purview does that Azure Policy cannot. Why is it insufficient to only know that storage accounts are encrypted — what additional information does Purview provide that Azure Policy cannot?
- Respond to the compliance officer's skepticism. How does enforcing resource configurations (via Policy) relate to patient data protection? What is the difference between technical controls (configuration enforcement) and the compliance evidence that auditors need?

---

## Scenario C: The Policy Design Dilemma

TechForward Global is a software company deploying a new SaaS platform on Azure. The platform team has been given these governance requirements by their enterprise cloud governance board:

- All Azure resources must be deployed only in East US and West US 2 (company network policy)
- All resources must have three required tags: CostCenter, Environment (Prod/Dev/Test), and Owner (email)
- Azure SQL Databases must have Transparent Data Encryption enabled
- Storage accounts must use HTTPS-only transfers

The platform team's lead architect is pushing back on the governance board. She argues: "Applying a Deny policy for all four requirements will break our CI/CD pipelines. Our deployment scripts were written before these policies existed and will fail until we update every script. We'll lose two weeks of velocity fixing pipelines. Can we use Audit mode for everything and just report on non-compliance?"

In 175-225 words, address all of the following:

- The architect is requesting Audit mode for all four policies. Evaluate her argument. For which of the four policy requirements does the Audit-first approach make good sense, and for which requirements would you argue that Deny is necessary from the start? Justify each decision based on the nature of the risk if the configuration is non-compliant.
- The governance board proposes a phased approach: run all four policies in Audit mode for 30 days, then switch to Deny. Design the 30-day Audit period as an actionable plan: what does the platform team do during that 30 days to prepare CI/CD pipelines for the Deny transition? What data from the Policy compliance dashboard informs their remediation priority?
- The architect mentioned that existing deployment scripts will fail when Deny policies are applied. Explain why this is actually a feature of governance design, not a bug. What does it mean that deployment scripts must be policy-aware, and how does policy-as-guardrails change how engineering teams write infrastructure-as-code?

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5-6 pts | Scenario identified at start. All three sub-questions addressed with accurate technical content. Uses Module 12 vocabulary (Azure Policy, Deny/Audit/Modify/DeployIfNotExists effects, Management Groups, scope inheritance, Microsoft Purview, policy initiatives, compliance dashboard, etc.). Word count 175-225. Demonstrates original reasoning. |
| 3-4 pts | Most sub-questions addressed. Minor gaps in policy effect selection or scope reasoning. |
| 1-2 pts | Incomplete or significant errors in governance reasoning or service selection. |
| 0 pts | No initial post by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive responses to two classmates. Each response is 75+ words with technical engagement: challenge a policy effect choice with an alternative, propose a different management group structure with justification, raise a compliance or operational consideration the poster missed, or add a specific real-world constraint that changes the recommendation. |
| 2-3 pts | Two responses but lacking technical depth or critical engagement. |
| 1 pt | One response or only agreement without substantive discussion. |
| 0 pts | No peer responses by Sunday deadline. |

---

## Professor Nash's Note

The governance board vs. architect tension in Scenario C represents a real organizational dynamic that cloud practitioners encounter regularly. Governance teams want controls. Engineering teams want velocity. The healthy resolution is not to choose between them — it is to design governance that enables compliant velocity. Policy-as-guardrails means engineers write infrastructure code knowing the boundaries, and CI/CD pipelines validate compliance before deployment rather than failing in production. The Audit-first approach is genuinely valuable: it converts governance from a theoretical framework into a specific backlog of remediation work. But Audit without a Deny deadline is just documentation of non-compliance. The governance design is only as strong as the organization's commitment to eventually enforcing it.

---

Discussion 12 | CIS-4331 Azure Cloud | Texas Wesleyan University
