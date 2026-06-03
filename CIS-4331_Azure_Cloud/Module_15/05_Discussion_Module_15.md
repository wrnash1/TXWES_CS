# Discussion Forum: Module 15 — Azure Compliance, Privacy, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Instructions

Read all three scenarios below. Choose ONE scenario to respond to in your initial post. Your initial post must be 175–225 words and address all the prompt questions for your chosen scenario. Then write two peer responses of 75–100 words each, engaging substantively with classmates who responded to any scenario.

**Due dates:** Initial post due by Day 3 of the module week. Peer responses due by Day 7.

---

## Scenario A — The Government Contractor

A defense technology company has won a new contract to build a software platform for a US Army logistics unit. The contract requires that all cloud infrastructure meet FedRAMP High requirements and that data never leave US government-controlled infrastructure. The company's current Azure environment uses standard commercial Azure subscriptions in the East US region. Their cloud architect has been tasked with designing the compliant target architecture.

**Respond to the following:**

- Which Azure cloud environment should the company migrate to, and why is the commercial Azure cloud insufficient for this requirement even if the correct policies are applied?
- The Army requires evidence of the cloud platform's FedRAMP authorization before signing off. Where would the architect obtain this evidence, and what specific document type would they provide?
- Beyond the infrastructure environment, what ongoing compliance practice would FedRAMP require after initial authorization?

**Consider:** Azure Government, FedRAMP High P-ATO, the Service Trust Portal, continuous monitoring, and data sovereignty in your response.

---

## Scenario B — The GDPR Data Breach

A European retail company uses Azure to store customer order data, including names, email addresses, home addresses, and payment reference numbers. At 2:00 AM on a Tuesday, the company's security team detects unauthorized access to their Azure SQL Database. Logs confirm that approximately 50,000 customer records were accessed. The breach is contained by 4:00 AM. The company's GDPR compliance officer is notified at 8:00 AM.

**Respond to the following:**

- Under GDPR, what is the deadline for reporting this breach to the relevant supervisory authority, measured from the point of discovery? Does the timeline in this scenario create a compliance risk?
- The compliance officer asks whether Microsoft is required to notify the company of the breach. What contractual commitment governs Microsoft's breach notification obligations to Azure customers?
- Two weeks after the breach, a customer emails the company requesting that all their personal data be permanently deleted. What GDPR right is the customer exercising, and what Azure tools or practices support fulfilling this request?

**Consider:** GDPR breach notification timelines, the Data Processing Addendum, right to erasure, Azure SQL data management, and Purview in your response.

---

## Scenario C — Governance at Scale

A national insurance company has 12 business units each with their own Azure subscription under a shared management group. The IT governance team has identified three problems. First, some business units are deploying resources in non-approved regions, causing data residency concerns. Second, resources are being created without required cost-allocation tags, making it impossible to charge back cloud costs to the correct department. Third, a recent security audit found that several storage accounts have public access enabled, violating company policy.

**Respond to the following:**

- For each of the three problems, identify the specific Azure Policy effect (Deny, Audit, Modify, DeployIfNotExists) that would be most appropriate and explain your reasoning.
- The governance team wants to address all three problems simultaneously and ensure every new subscription provisioned in the future starts compliant. Which Azure service beyond Policy alone would you recommend and why?
- One business unit's director pushes back, arguing that enforcing these policies will slow down their team's ability to deploy quickly. How would you respond to this concern while still maintaining governance?

**Consider:** Azure Policy effects, Azure Blueprints, initiative definitions, management group scope, and the balance between governance and agility in your response.

---

## Peer Response Guidelines

Your peer responses should do at least two of the following:

- Build on a point your classmate made with additional detail or a real-world example
- Respectfully challenge an assumption or recommendation and offer an alternative perspective
- Connect the scenario to concepts from a different module in this course
- Ask a clarifying question that would deepen the analysis

Responses that only say "great post" or restate the classmate's points without adding new analysis will not receive full credit.

---

## Grading Rubric — 10 Points Total

| Criteria | Points |
|---|---|
| Initial post addresses all prompt questions for the chosen scenario | 3 |
| Initial post demonstrates accurate understanding of Azure compliance and governance tools | 2 |
| Initial post is 175–225 words (penalty for significant deviation) | 1 |
| Peer response 1 adds substantive analysis or perspective | 2 |
| Peer response 2 adds substantive analysis or perspective | 2 |
| **Total** | **10** |

---

## Example Starter Phrases

To help you open your initial post with substance rather than filler:

- "The core compliance gap in this scenario is not just technical — it is jurisdictional, because..."
- "GDPR's 72-hour breach notification requirement creates immediate pressure here because..."
- "The right Azure Policy effect for the region restriction problem is Deny rather than Audit because..."
- "Azure Blueprints adds value beyond Policy alone in this scenario because it addresses..."

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 15 Discussion*
