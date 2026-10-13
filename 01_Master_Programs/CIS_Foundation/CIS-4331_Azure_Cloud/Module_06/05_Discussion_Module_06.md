# Discussion Forum: Module 06 - Azure Storage Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 | **Initial Post Due:** Wednesday 11:59 PM | **Peer Responses Due:** Sunday 11:59 PM

---

## Overview

Storage architecture decisions — which service to use, what redundancy to configure, what access tier to apply — have long-term cost and durability consequences. Unlike compute resources that can be easily resized, storage choices often lock in costs for months or years (especially with Archive tier minimum retention periods). This discussion develops your ability to reason through storage trade-offs in realistic organizational contexts.

Read all three scenarios. Choose **one scenario** for your initial post. Identify your scenario at the start of your post.

---

## Scenario A: The Media Company Archive Strategy

StreamVault Productions is a video production company that creates documentary content. Their digital asset management workflow generates three categories of files: (1) Raw footage files (2-50 GB each) that are accessed daily during active production (average project lasts 90 days); (2) Final master files (5-20 GB each) for completed projects that might be accessed once per year for re-releases or licensing; (3) Historical archive footage from projects completed more than 5 years ago that is accessed maybe once every 2-3 years for documentary reference. StreamVault has 500 TB of total storage across all categories. Monthly storage cost is currently $15,000 and they want to reduce it significantly.

In 175-225 words, address all of the following:

- Assign each of the three file categories (raw footage, final masters, historical archive) to an appropriate Blob Storage access tier. Justify each assignment using the access frequency and the cost vs. access trade-off from the reading guide.
- Describe how Azure Blob Storage lifecycle management policies could automate the transitions between tiers as projects move through their lifecycle. What specific rule would you write to transition raw footage files to a lower tier when a project completes?
- StreamVault wants the historical archive to survive a regional disaster in case a Texas datacenter fails (they are based in Dallas). Which redundancy option would you recommend for the historical archive storage account, and how does that compare cost-wise to LRS? Is the additional cost justified for 5+ year-old reference footage?

---

## Scenario B: The Healthcare Data Platform

MedPath Analytics processes electronic health records (EHR) data for a consortium of 30 Texas hospitals. The platform stores three types of data: (1) Active patient records accessed multiple times daily by clinical staff; (2) Discharge records from patients discharged in the last 5 years, accessed occasionally for follow-up care coordination; (3) Historical records older than 5 years, retained for HIPAA compliance (minimum 6-year retention). The HIPAA Security Rule requires that electronic PHI (protected health information) be protected against regional disasters. Texas data breach notification law requires that data remain within the United States.

In 175-225 words, address all of the following:

- Which storage redundancy option satisfies the HIPAA requirement for regional disaster protection while keeping data within the United States? Explain which redundancy options would violate the US-only requirement (if any) and which would not.
- For the historical records in HIPAA-required long-term retention, which access tier is most appropriate? The HIPAA minimum retention is 6 years, but early deletion fees apply to Archive tier after 180 days. Does the Archive tier minimum retention period conflict with the 6-year HIPAA requirement?
- MedPath wants to ensure that only clinical application systems (running as Azure VMs) can access the storage — no direct human access. Which storage access method (account keys, SAS tokens, or Azure AD with managed identities) is most appropriate for this machine-to-machine access pattern? Explain why.

---

## Scenario C: The Startup Event-Driven Architecture

TechFlow Solutions is building a real-time customer event tracking platform. When a user takes an action on their mobile app (page view, button click, purchase), an event is generated. The platform must: (1) Accept up to 10 million events per day without data loss; (2) Process each event asynchronously (event capture must not block the mobile app); (3) Store processed event summaries per user for 90 days, with fast lookup by user ID; (4) Store raw event logs indefinitely for future machine learning training data. The engineering team is three people and wants to use Azure Storage services without building complex infrastructure.

In 175-225 words, address all of the following:

- The requirement to accept events without blocking the mobile app (asynchronous capture) is a classic use case for one specific Azure Storage service. Identify the service and explain how the mobile app would write events and how the processing backend would consume them. What happens to events if the processing backend is temporarily down?
- For storing processed event summaries (requirement 3), evaluate Azure Table Storage vs. a separate Azure SQL Database. The lookup is always by user ID (a key-value access pattern), and the team wants to minimize cost and management overhead. Which service is more appropriate, and why?
- For the raw event logs (requirement 4), which blob type and access tier combination would you recommend? The logs are written once, never modified, accumulate at roughly 1 GB per day, and are accessed only when a data science team runs ML training (estimated once per quarter). Account for both the access pattern and the Archive tier's retrieval behavior in your recommendation.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5-6 pts | Scenario identified at start. All three sub-questions addressed with accurate technical content. Uses Module 06 vocabulary (blob types, access tiers, redundancy options). Word count 175-225. Demonstrates original reasoning. |
| 3-4 pts | Most sub-questions addressed. Minor technical gaps. |
| 1-2 pts | Incomplete or significant errors. |
| 0 pts | No initial post by Wednesday deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Substantive responses to two classmates. Each response is 75+ words with technical feedback: challenge a tier assignment, propose a different redundancy level, add a compliance consideration, or question a cost analysis. |
| 2-3 pts | Two responses but lacking technical depth. |
| 1 pt | One response or superficial comments only. |
| 0 pts | No peer responses by Sunday deadline. |

---

## Professor Nash's Note

Storage cost optimization is one of the highest-ROI activities in cloud cost management. Organizations often migrate to the cloud, configure everything at the highest tier for safety, and then never revisit it. A 500 TB storage environment where 80 percent of data in Hot tier should be in Cool or Archive can easily waste $8,000-$12,000 per month. Learning to match access tiers to real access patterns — and to use lifecycle management to automate transitions — is a skill that pays off immediately. The scenarios in this discussion reflect real storage architecture conversations I have seen in enterprise Azure environments.
