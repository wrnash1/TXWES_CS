# Discussion Forum: Module 08 — Salesforce Service Cloud and Case Management

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

---

## Overview

This forum applies Module 08 Service Cloud concepts to realistic business scenarios involving SLA management, knowledge base strategy, and case routing design. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175–225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Reference at least one specific Service Cloud object or feature (Case, Queue, Entitlement, Milestone, Escalation Rule, Knowledge Article, Omni-Channel, Service Console) by name
- Name a specific Service Cloud configuration tool or concept from Module 08
- Make a concrete recommendation or analysis grounded in the scenario details

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must do one of the following:

- Identify an SLA risk or customer satisfaction consequence your classmate did not mention
- Connect the scenario to a specific Service Cloud object relationship or reporting impact your classmate overlooked
- Describe how the Service Cloud configuration your classmate recommended would affect a related business process (billing, sales relationship, ERP integration, or knowledge retention)

---

## Scenarios

### Scenario A: The SLA Black Hole

A healthcare technology company provides software to 300 hospital clients. Their support contracts define three tiers: Platinum (1-hour first response, 4-hour resolution), Gold (4-hour first response, 24-hour resolution), and Silver (24-hour first response, 72-hour resolution). After deploying Salesforce Service Cloud, the support director reviews a quarterly report and discovers that 18% of Platinum Cases were not responded to within the contractual 1-hour window, and 11% were not resolved within 4 hours. When she asks the support team what happened, agents say they did not know which Cases had urgent SLA deadlines. The Cases appeared in the queue mixed with Gold and Silver cases, and there was no visual indicator of urgency or countdown.

**Your task:** What specific Service Cloud features should have been configured to prevent agents from missing Platinum SLA deadlines? Reference the Entitlement-Milestone structure and explain how Warning Actions and Violation Actions could have provided automated intervention before the deadline was missed. What configuration failure in the implementation led to this problem, and what would you do differently?

### Scenario B: The Knowledge Wasteland

A financial services firm has been using Salesforce Service Cloud for two years. Their support team closes an average of 1,200 Cases per month. A new support manager reviews the Knowledge Base and finds only 47 articles — most written in the first month after deployment and never updated. Agent surveys reveal that 70% of agents never use the Knowledge Base because "the articles are outdated and don't match our current product version." Meanwhile, the average handle time for Cases has increased 40% over the past year, and senior agents spend significant time re-explaining solutions that junior agents have already received. Customer satisfaction scores are declining.

**Your task:** Diagnose the root cause of the Knowledge Base failure at this company. What process should have been in place from the beginning to ensure articles stay current and new articles are created from Case resolutions? Reference specific Knowledge lifecycle stages and the specific mechanism that allows agents to create articles directly from closed Cases. What governance or workflow change would you recommend to rebuild the Knowledge Base into a functional tool?

### Scenario C: The Routing Disaster

A national retailer operates a centralized customer service center with 85 agents organized into four teams: General Inquiries, Order Issues, Returns and Refunds, and Technical Support (for their mobile app and website). Currently, all inbound Cases — regardless of origin or subject — go into a single shared queue. Agents claim Cases manually from the queue in the order they see fit. Management has noticed that Technical Support cases (which require specialized skills) are frequently claimed by General Inquiry agents who cannot resolve them, causing cases to sit in a "Working" status for days before being re-routed. The Technical Support team, meanwhile, is idle while their queue empties of appropriate cases.

**Your task:** Design a Salesforce Service Cloud routing solution that ensures Technical Support Cases reach the Technical Support team automatically. What specific Service Cloud features would you use? Describe how you would differentiate Technical Support Cases from General Inquiry Cases at the point of creation so that routing can occur correctly. Reference at least two specific Service Cloud configuration objects by name and explain how they work together.

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter at top of post |
| Specific Service Cloud object or feature named and applied | 2 | Feature name used accurately in context of scenario |
| Service Cloud tool or concept referenced correctly | 1 | Configuration feature named and its function explained in scenario terms |
| Concrete recommendation or analysis | 1 | Specific and grounded — not generic CRM advice |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, substantive extension | 2 | Adds SLA risk, customer impact, or connection classmate missed |
| Peer response 2: 60+ words, substantive extension | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario A describes a failure pattern I have seen in multiple enterprise Salesforce deployments. Companies invest in purchasing Salesforce Service Cloud licenses, go through a full implementation, and then discover six months later that none of the SLA management features were actually configured. Entitlements were never linked to Accounts. Entitlement Processes were never defined. Milestones with Warning Actions were never set up. The result is a very expensive Case list view with no automation behind it. Buying the platform is not the same as configuring it to deliver business value. On the Salesforce Administrator exam — and in your professional career — the ability to understand which features map to which business requirements, and to know when those features are missing, is exactly what separates an effective administrator from someone who simply completed the implementation checklist.
