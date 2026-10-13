# Discussion Forum: Module 07 — Salesforce Sales Cloud and CRM

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

---

## Overview

This forum applies Module 07 Sales Cloud concepts to realistic business scenarios involving pipeline management, data quality, and sales reporting. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175–225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Reference at least one specific Salesforce object (Lead, Account, Contact, Opportunity, Activity) by name and explain its role in the scenario
- Name a specific Sales Cloud concept or tool from Module 07 (Lead conversion, Stage, Path, Validation Rule, Flow Builder, Dynamic Dashboard, Einstein Lead Scoring, etc.)
- Make a concrete recommendation or analysis grounded in the scenario details

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must do one of the following:

- Identify a data quality risk or pipeline reporting consequence your classmate did not mention
- Connect the scenario to a Salesforce object relationship your classmate overlooked
- Describe how the problem in the scenario would affect an ERP back-office integration (order management, revenue recognition, or financial forecasting)

---

## Scenarios

### Scenario A: The Unqualified Pipeline Problem

A regional insurance company has 1,800 open Opportunity records in Salesforce. Their VP of Sales reviews the monthly pipeline forecast and sees $14.2 million in expected revenue. Excited, she presents this number to the CFO for headcount planning. Three months later, the actual closed revenue for the quarter is $2.1 million — a $12 million variance. A post-mortem audit reveals that 60% of open Opportunities had Close Dates that were already in the past, and many had not been updated in over 90 days. The sales reps admit they rarely update Opportunities because "Salesforce is just for management, not for us."

**Your task:** What is the business impact of stale, unupdated Opportunities on the pipeline forecast the VP presented to the CFO? Identify at least one specific Salesforce configuration tool that could be used to enforce Opportunity data quality — prevent stale close dates or require regular Stage updates — and explain how it would work. Reference the Stage Probability forecasting formula in your analysis.

### Scenario B: The Lead Conversion Resistance

A manufacturing B2B company uses Salesforce Sales Cloud but has a persistent problem: sales reps convert Leads inconsistently, or skip conversion entirely and create duplicate Account and Contact records manually. The Salesforce admin discovers that 3,400 Lead records are marked Open and untouched, while the Accounts list has over 200 duplicate company names. Finance cannot get a clean customer count. Marketing cannot measure campaign ROI because Leads are never tied back to Opportunities. The VP of Sales blames the CRM system; the reps say Lead conversion is confusing and takes too long.

**Your task:** Explain what Lead conversion is supposed to accomplish — specifically what records it creates and why that matters for pipeline reporting and marketing attribution. What is the downstream impact on reporting when reps skip conversion and create records manually? Recommend at least one Salesforce feature or configuration change that would reduce friction in the conversion process or enforce it as a required step.

### Scenario C: The Dashboard Visibility Gap

A national staffing company has deployed Salesforce Sales Cloud across 12 regional offices. The National Sales Director builds a dashboard showing total open pipeline by region, all reps' Opportunity counts, and year-to-date closed revenue. She shares the dashboard with all 47 sales reps. Several reps immediately complain that they can now see each other's Opportunities, deal values, and close dates — information that is confidential between regions. The Salesforce admin realizes the dashboard was set up as a standard dashboard running as the National Sales Director, so every rep who views it sees the Director's full dataset.

**Your task:** Explain why the current dashboard configuration creates the visibility problem the reps are describing. What specific Salesforce dashboard feature would you configure to give each rep a personalized view showing only their own pipeline data? What is the maximum number of this type of dashboard available in Salesforce Enterprise Edition? Address the trade-off between individual rep visibility and the Director's need for an aggregated org-wide view.

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter at top of post |
| Specific Salesforce object named and applied correctly | 2 | Object name used accurately in context of scenario |
| Sales Cloud concept or tool referenced correctly | 1 | Feature named and its function explained in scenario terms |
| Concrete recommendation or analysis | 1 | Specific and grounded — not generic CRM advice |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, substantive extension | 2 | Adds risk, consequence, or connection classmate missed |
| Peer response 2: 60+ words, substantive extension | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario A describes one of the most common and damaging problems in enterprise CRM deployments. When pipeline forecasts are built on stale data, the financial consequences ripple well beyond the sales team — CFOs make headcount decisions, finance teams make cash flow projections, and supply chain teams plan inventory based on what the pipeline says. A $12 million forecast miss is not a CRM software problem; it is a data governance problem. The technology works exactly as designed — garbage in, garbage out. The Salesforce Administrator certification tests your ability to configure tools that prevent garbage from entering in the first place. Validation Rules, Path configuration, and required fields exist precisely to enforce data discipline at the point of entry, before stale records corrupt the forecast your executives rely on.
