# Discussion Forum: Module 11 — Azure Identity, Security, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 10 | Initial Post Due: Wednesday 11:59 PM | Peer Responses Due: Sunday 11:59 PM

---

## Instructions

Read all three scenarios below. Choose **one** scenario that interests you most and write your initial post responding to that scenario. Your initial post must be 175–225 words. Then respond to **two classmates** who chose different scenarios. Each peer response must be at least 75 words and add substantive insight beyond simple agreement.

---

## Scenario 1: Zero Trust Security for a Remote-First Company

A technology consulting firm transitioned to fully remote work in 2020 and never returned to a central office. All 300 employees work from home, coffee shops, co-working spaces, and client sites worldwide. The IT director has decided to adopt a Zero Trust security architecture. Previously, the company used a traditional perimeter model: VPN into the office network, then trust everything inside. Now the company needs to enforce strict identity verification and access control without a traditional network perimeter. The CTO is concerned that requiring MFA on every single sign-in — regardless of context — will frustrate employees and hurt productivity, but the CISO insists on strong authentication for all access to sensitive applications.

**Discussion Prompt:** How would you design a Conditional Access policy strategy to satisfy both the CISO's security requirements and the CTO's usability concerns? Which signal conditions (location, device compliance, sign-in risk, application sensitivity) would you include in your policies? Would you use Security Defaults or Conditional Access Policies, and what licensing tier is required? How does Zero Trust differ from the traditional perimeter security model, and why is it better suited to remote-first organizations?

---

## Scenario 2: Cloud Governance for a Multi-Subscription Enterprise

A Fortune 500 financial services company is formalizing its Azure governance framework. It has 47 Azure subscriptions organized into business units: Retail Banking, Commercial Banking, Investment Management, and Shared Services. The cloud governance team has identified several compliance issues discovered during a recent audit: (1) resources in 12 subscriptions do not have required cost center tags, (2) 6 subscriptions have storage accounts with public blob access enabled, and (3) 3 subscriptions have virtual machines deployed in regions outside the company's approved US and EU regions. The governance team wants to implement a solution that prevents future violations and reports on existing non-compliance without disrupting existing workloads.

**Discussion Prompt:** Design a Management Group and Azure Policy strategy to address all three compliance issues. Which Management Group hierarchy would you create for this organization? For each of the three compliance issues, specify the appropriate Azure Policy effect (Deny, Audit, Modify, DeployIfNotExists) and explain your reasoning. How does the Audit effect differ from Deny for addressing existing non-compliant resources versus preventing future ones? Would you use built-in policy definitions or custom policies for these requirements?

---

## Scenario 3: Secrets Management and Least Privilege for a Microservices Application

A fintech startup is deploying a microservices application to Azure Kubernetes Service. The application has 8 microservices. Two services (payment-processor and fraud-detector) need access to a shared database connection string stored in Azure Key Vault. Three services (api-gateway, user-service, order-service) need to read a third-party API key. The remaining three services do not access Key Vault at all. The security architect is reviewing two options: Option A — grant all 8 services the Key Vault Reader role at the Key Vault level. Option B — create separate managed identities for each service and grant the Key Vault Secrets User role scoped to only the specific secrets each service needs.

**Discussion Prompt:** Which option would you recommend and why? How does Option B implement the principle of least privilege compared to Option A? What are managed identities in Azure, and why are they preferred over service account passwords for application-to-Key Vault authentication? If the payment-processor service was compromised by a malicious actor, how does Option B limit the blast radius compared to Option A? Reference at least one specific Azure RBAC Key Vault role in your response.

---

## Peer Response Guidelines

When responding to a classmate:

- Add at least one technical detail they did not address — a specific Entra ID feature, policy effect, RBAC role, or Key Vault capability
- If their recommendation could have unintended consequences (for example, a Deny policy breaking an existing workload), point it out and suggest a mitigation
- If you would design the solution differently, explain your reasoning with specific Azure feature references rather than general principles
- Responses that simply agree or restate the original post will not earn full credit

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post directly and specifically addresses the scenario's security, identity, or governance requirements | 4 |
| Initial post references specific Azure features, RBAC roles, policy effects, licensing tiers, or technical details | 2 |
| Peer response 1: substantive, adds new technical insight, 75+ words | 2 |
| Peer response 2: substantive, adds new technical insight, 75+ words | 2 |
| **Total** | **10** |

---

## Professor Nash Note

The scenarios in this discussion reflect real security and governance decisions that cloud architects make in production environments. Scenario 1 touches the tension between security friction and usability — a debate every security team has. The key insight is that Conditional Access is not binary: you do not have to choose between MFA everywhere and MFA nowhere. Intelligent, context-aware policies can dramatically reduce friction for low-risk scenarios while maintaining strong controls for high-risk ones. In Scenario 3, I want you to think carefully about what "least privilege" actually means in practice. Option A sounds reasonable — it is simpler and the services only have Reader access. But Reader at the Key Vault level means any compromised service can read every secret in the vault. Option B scopes each identity to only the secrets it actually needs. The blast radius difference is significant. Make that case with specifics.

---

*Discussion 11 — Module 11: Azure Identity, Security, and Governance | CIS-4331 | Texas Wesleyan University*
