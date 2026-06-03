# Discussion Forum: Module 10 — Azure Databases

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 10 | Initial Post Due: Wednesday 11:59 PM | Peer Responses Due: Sunday 11:59 PM

---

## Instructions

Read all three scenarios below. Choose **one** scenario that interests you most and write your initial post responding to that scenario. Your initial post must be 175–225 words. Then respond to **two classmates** who chose different scenarios. Each peer response must be at least 75 words and add substantive insight beyond simple agreement.

---

## Scenario 1: Legacy SQL Server Migration Decision

A manufacturing company runs a critical production scheduling application that has been in operation for 14 years. The application is backed by an on-premises SQL Server 2012 database that the company wants to move to Azure. The DBA has catalogued the following features the application actively uses: SQL Server Agent jobs for nightly data archival, four linked servers connecting to partner SQL Server databases at supplier companies, cross-database queries joining tables from three different databases on the same SQL Server instance, and CLR stored procedures written in C#. The IT director wants a fully managed PaaS solution and is concerned about the long-term maintenance costs of managing SQL Server VMs. The development team estimates a full application rewrite to eliminate these features would take 18 months.

**Discussion Prompt:** Which Azure SQL service would you recommend and why? Is there a scenario in which SQL Server on Azure VM would actually be the better choice despite the IT director's PaaS preference? What risks should the team evaluate when choosing between Azure SQL Managed Instance and Azure SQL Database? If the team chose Azure SQL Database and the migration revealed unsupported features, what tool would you use to identify those issues before migration?

---

## Scenario 2: Real-Time Global Gaming Leaderboard

A mobile gaming company is building a global leaderboard system for a multiplayer game with millions of active players in North America, Europe, Southeast Asia, and Australia. The leaderboard must show a player's current rank and score within 100 milliseconds from any region. The leaderboard is updated thousands of times per second as players complete matches. Exact rank accuracy is important but not critical — a leaderboard rank that is 2–3 seconds stale is acceptable. Players are more sensitive to leaderboard display latency than to whether the rank is exactly accurate in real time. The engineering team is evaluating Azure SQL Database with geo-replication versus Azure Cosmos DB for this use case.

**Discussion Prompt:** Which service would you recommend for this leaderboard system and why? Which Cosmos DB consistency level would you select given the requirement that slight staleness is acceptable? How does Cosmos DB's global distribution model address the 100 ms latency requirement? What are the cost implications of enabling multi-region writes in Cosmos DB, and are they justified for this use case? Reference specific Cosmos DB features such as consistency levels or SLA figures in your response.

---

## Scenario 3: Healthcare Analytics Platform

A hospital network is building a new analytics platform to analyze 5 years of patient outcome data, clinical trial results, and operational metrics across 12 hospitals. The platform needs to: (1) run complex SQL queries joining data from multiple sources, (2) support business intelligence tools like Power BI, (3) handle datasets up to 20 TB, and (4) allow data scientists to run Python-based machine learning models on the same platform without exporting data to another system. The IT team is evaluating Azure SQL Database versus Azure Synapse Analytics for this platform.

**Discussion Prompt:** Which service would you recommend for this healthcare analytics platform, and why? What specific Azure Synapse Analytics feature would allow both SQL analysts and Python data scientists to work on the same platform? How does HIPAA compliance factor into the service selection — does Azure Synapse Analytics support compliance frameworks? What limitation of Azure SQL Database makes it a poor fit for 20 TB analytical workloads, even in the Hyperscale tier?

---

## Peer Response Guidelines

When responding to a classmate:

- Add at least one technical detail they did not mention — a specific Azure feature, pricing implication, SLA figure, or migration tool
- If you would choose a different service than they recommended, explain your reasoning using specific technical differences between the services
- Challenge assumptions: if their recommendation depends on a constraint they have not examined closely, point it out
- Avoid responses that simply restate their argument or express agreement without adding new content

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post demonstrates clear understanding of the scenario's specific database requirements | 4 |
| Initial post references specific Azure database services, features, SLAs, or technical details | 2 |
| Peer response 1: substantive, adds new technical insight, 75+ words | 2 |
| Peer response 2: substantive, adds new technical insight, 75+ words | 2 |
| **Total** | **10** |

---

## Professor Nash Note

Database architecture decisions are some of the highest-stakes choices in enterprise IT — getting them wrong causes years of technical debt. Notice that Scenario 1 involves a real tension that most organizations face: the business wants PaaS for low maintenance costs, but the application has deep dependencies on SQL Server features that PaaS tiers do not fully support. The right answer is not simply "use the PaaS service" — it requires examining what actually works and what the fallback options are. In Scenario 2, I want you to think carefully about consistency levels. The temptation is always to choose Strong consistency, but Bounded Staleness is specifically designed for leaderboard use cases and is far more efficient. Make the case using Cosmos DB's actual consistency level definitions, not intuition.

---

*Discussion 10 — Module 10: Azure Databases | CIS-4331 | Texas Wesleyan University*
