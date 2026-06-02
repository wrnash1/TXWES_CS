# Discussion — Module 02: Data Collection and Data Sources

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 (6 initial post + 4 peer responses)

---

## Overview

This discussion asks you to apply Module 02 concepts to realistic data collection and database scenarios. Choose one of the three scenarios below. Write an initial post of 175–225 words, then respond to at least two classmates by Sunday at 11:59 PM.

Professor Nash's note: Strong posts use precise terminology from the module — primary/secondary, OLTP/OLAP, ETL stage names, schema types. Avoid restating definitions; instead, apply them to the specific scenario with concrete reasoning.

---

## Scenario A — Hospital Data Collection Strategy

A regional hospital wants to build an analytics capability to reduce patient readmission rates. The analytics team is considering three data sources: (1) pulling records directly from the hospital's production EHR (Electronic Health Records) system, (2) designing a new discharge survey to collect post-visit patient feedback, and (3) purchasing a third-party dataset of regional population health statistics.

In 175–225 words, address all three of the following:

1. Classify each of the three data sources as primary or secondary and justify your classification.
2. The team proposes running daily analytical queries directly against the production EHR system. Identify the problem with this approach and recommend a more appropriate architectural solution.
3. Identify one data quality dimension that is most likely to be problematic for each of the three sources and explain why.

---

## Scenario B — Retail Data Architecture Decision

A mid-size online retailer currently stores all data — transaction records, product catalog, customer profiles, web clickstream logs, and customer review text — in a single relational SQL Server database. The analytics team is struggling with slow reports and increasing data volume.

In 175–225 words, address all three of the following:

1. Explain whether the current single-database approach is appropriate for both operational and analytical workloads. Use the OLTP/OLAP distinction in your answer.
2. Recommend a target architecture that separates operational and analytical data. Name the components you would include and explain the role of each.
3. The clickstream logs and customer review text are currently stored as large VARCHAR fields in a relational table. Is this the best approach for these data types? Propose a better storage solution and explain why it is more appropriate.

---

## Scenario C — ETL Pipeline Design

A financial services company collects data from five sources: a core banking system (SQL Server), a customer survey platform (Qualtrics CSV exports), a fraud detection system (real-time JSON stream), a third-party credit bureau (SFTP flat files delivered nightly), and a marketing automation platform (REST API).

In 175–225 words, address all three of the following:

1. For each of the five sources, identify which ETL stage presents the greatest challenge and explain why.
2. The fraud detection system delivers data as a real-time JSON stream rather than batch files. How does this affect the standard ETL pipeline design? What architectural change would you recommend to handle streaming data?
3. Two team members disagree about whether to use ETL or ELT for this project. One argues that ELT is always better because it preserves raw data. The other argues that ETL is better for compliance-sensitive financial data. Which position do you support, and why?

---

## Discussion Rubric

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 6 | Addresses all three questions with accurate terminology, well-reasoned positions, and concrete specifics. Within 175–225 words. |
| 4–5 | Addresses most questions accurately but lacks depth on at least one item. |
| 2–3 | Addresses some questions; contains inaccuracies or missing justifications. |
| 0–1 | Post is missing, too brief, or does not address the scenario. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 | Responds to at least two classmates with substantive additions — a counterargument, a different architectural option, or a real-world example. Minimum 60 words per response. |
| 2–3 | Responds to two classmates but responses are surface-level, or only one substantive response is provided. |
| 0–1 | Only one response submitted or responses are too brief to demonstrate engagement. |

---

## Deadlines

- Initial post: Wednesday at 11:59 PM
- Peer responses: Sunday at 11:59 PM
