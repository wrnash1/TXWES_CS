# Discussion Forum: Module 04 - Azure Container Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 | **Initial Post Due:** Wednesday 11:59 PM | **Peer Responses Due:** Sunday 11:59 PM

---

## Overview

Choosing the right container service in Azure requires matching the complexity of the service to the complexity of the workload. This discussion develops that judgment through three realistic organizational scenarios involving different container service selection challenges.

Read all three scenarios. Choose **one scenario** for your initial post. Identify your scenario at the start of your post.

---

## Scenario A: The Startup Architecture Decision

PeakRoute Technologies is a four-person startup building a route optimization SaaS platform. Their backend consists of five services: a REST API gateway, an optimization engine, a mapping data service, a user authentication service, and a notification service. The team's two backend developers have experience with Docker but no Kubernetes experience. Their CTO is concerned about operational overhead — the team cannot afford to spend time managing infrastructure. The platform needs to handle zero traffic at 3 AM and peak traffic from 1,000 concurrent users during business hours. Monthly cloud budget for compute is $200.

In 175-225 words, address all of the following:

- The CTO's concern about operational overhead rules out one Azure container service entirely. Which service is ruled out and why? Identify the specific operational characteristic that makes it inappropriate for this team.
- Between Azure Container Apps and Azure Container Instances, which is better suited for this five-service application? Justify your choice by citing at least two specific Container Apps features from the reading guide that address the startup's constraints.
- The optimization engine performs computationally expensive calculations and is only needed when a route planning request is received. It may be idle for 10-minute stretches. Which billing characteristic of the recommended service makes this idle pattern particularly cost-effective? Quantify the savings concept even if you cannot give an exact dollar amount.

---

## Scenario B: The Enterprise Modernization

Consolidated National Bank is migrating 40 microservices from on-premises Kubernetes clusters to Azure. The bank's platform team has deep Kubernetes expertise and manages a certified Kubernetes environment. They need: strict network policy enforcement between services, custom Kubernetes admission controllers for security policy enforcement, support for stateful workloads (databases, message brokers) with persistent storage, integration with the bank's on-premises Active Directory, and the ability to deploy custom Kubernetes operators. The migration timeline is 18 months.

In 175-225 words, address all of the following:

- The bank's requirements include "custom Kubernetes admission controllers" and "custom Kubernetes operators." Which Azure container service supports these and which does not? Explain why this distinction exists.
- The bank has deep Kubernetes expertise and is migrating an existing Kubernetes environment. Does this context change your service recommendation compared to a team with no Kubernetes experience? Explain your reasoning using the Container Services comparison table from the reading guide.
- Network policy enforcement between services is a security requirement. In AKS, which networking mode (Kubenet vs. Azure CNI) provides better support for this requirement, and why? Note: Azure CNI gives each pod a routable IP in the VNet — research this concept and explain its significance for network policy enforcement.

---

## Scenario C: The University Research Pipeline

Texas Wesleyan's computer science research lab (fictional scenario) runs weekly bioinformatics data processing pipelines. Each pipeline consists of three sequential processing steps: (1) data normalization (runs for 5 minutes), (2) genomic alignment (runs for 45 minutes, computationally intensive), and (3) results aggregation (runs for 10 minutes). The pipeline runs every Sunday at midnight. The lab has no cloud infrastructure expertise beyond basic Azure portal usage. Total monthly compute budget is $15. The pipelines are triggered by a file being uploaded to Azure Blob Storage.

In 175-225 words, address all of the following:

- Evaluate whether Azure Container Instances, Azure Container Apps, or Azure Kubernetes Service is most appropriate for this pipeline. Justify your choice based on the trigger mechanism, duration, frequency, and expertise constraints.
- The genomic alignment step is computationally intensive. ACI supports custom CPU and memory allocation. If the alignment container needs 2 vCPUs and 4 GB RAM for 45 minutes once per week, estimate the ACI cost for the alignment step alone. Use the rates from the Module 04 lab ($0.0000149 per vCPU-second and $0.0000015 per GB-second). Show your calculation.
- The pipeline is triggered by a file upload to Blob Storage. Which Azure container service has native event-driven scaling that can respond to Blob Storage events directly? How does this align with the pipeline's trigger mechanism?

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5-6 pts | Scenario identified at start. All three sub-questions addressed with accurate technical content. Uses Module 04 vocabulary. Word count 175-225. Demonstrates original analysis. |
| 3-4 pts | Most sub-questions addressed. Minor technical gaps. |
| 1-2 pts | Incomplete response or significant technical errors. |
| 0 pts | No initial post by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive responses to two classmates. Each response is 75+ words with specific technical feedback: challenge a service selection, add a constraint not considered, propose a cost optimization, or extend the analysis. |
| 2-3 pts | Two responses but lacking technical depth. |
| 1 pt | One response or superficial comments only. |
| 0 pts | No peer responses by Sunday deadline. |

---

## Professor Nash's Note

Container service selection is one of those decisions where the technically correct answer and the practically appropriate answer can differ significantly. The technically correct answer for a large production microservices platform might be AKS — but if the team has no Kubernetes experience, the operational learning curve may introduce more risk than the architectural benefits justify. Azure Container Apps exists precisely because many organizations want Kubernetes capabilities without Kubernetes complexity. When you evaluate a technology recommendation, always factor in team skill set, organizational risk tolerance, and operational overhead alongside pure technical capability.
