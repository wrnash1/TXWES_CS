# Discussion: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be 175–225 words and address all embedded questions. After posting, reply substantively to **two classmates** who chose different scenarios. Peer replies must be at least 75 words and add new analytical content. Initial posts are due Thursday 11:59 PM; peer replies are due Sunday 11:59 PM.

---

## Scenario 1: The Dashboard Nobody Uses

A regional distribution company launched a Salesforce executive dashboard six months ago. The IT team spent three weeks building it. It has 22 metrics displayed simultaneously, including last month's sales by product, year-to-date revenue by territory, open case age distribution, inventory reorder alerts, a count of contacts by state, and twelve other numbers — all shown as static text values with no trend indicators or color-coded thresholds.

The executive team logged in to view it the day it launched, and nobody has opened it since. The VP of Operations sent an email saying "I still use the spreadsheet my assistant sends me on Monday mornings."

Address the following in your post:

- Using at least two specific dashboard design principles from Module 14, diagnose why this dashboard failed to gain adoption.
- What does the VP's preference for the Monday morning spreadsheet reveal about what executives actually need from reporting tools?
- How would you approach rebuilding this dashboard? Specifically: how many metrics would you include, and how would you decide which ones to keep?
- What stakeholder process would you follow before starting the redesign, and why does a technical redesign alone not guarantee adoption?

Your response should demonstrate understanding of executive dashboard design principles, KPI selection, and organizational change dimensions of reporting adoption.

---

## Scenario 2: The Data Quality Crisis

Nexus Insurance is about to launch a new Salesforce CRM Analytics dashboard for their sales leadership team. During the final user acceptance testing, a sales director notices that the pipeline number in CRMA shows $48 million, but the same time period shows $61 million in the old spreadsheet report. The discrepancy is $13 million.

Investigation reveals three contributing factors: the CRMA dataflow filters out opportunities marked "Pending Approval" (about 12% of pipeline), a custom Stage value added by a regional team is not mapped correctly in the dataflow transformation, and some opportunities have $0 amounts because reps created them without entering line items.

Address the following in your post:

- Which of the three data quality issues is the most operationally dangerous if left unaddressed, and why?
- How does a data quality problem like this affect executive trust in the reporting system, and how difficult is it to rebuild that trust once it is broken?
- For each of the three issues, propose a specific remedy — either in the CRMA configuration, in the Salesforce data model, or as a business process change.
- What governance process should have caught these issues before the launch demonstration?

Your response should demonstrate understanding of data quality, ETL/dataflow concepts, report accuracy, and analytics governance.

---

## Scenario 3: Choosing Between Reporting Tools

A manufacturing company is evaluating how to improve executive reporting across two systems: SAP S/4HANA for operations and finance, and Salesforce for sales and customer service. The CIO has presented three options:

**Option A:** Build native SAP Crystal Reports for finance, build native Salesforce dashboards for sales, and accept that executives must log in to two separate systems to see the full business picture.

**Option B:** Implement SAP Analytics Cloud (SAC) and use its live connection to S/4HANA for finance data, plus ingest Salesforce data via an API connector into SAC's analytical store for a unified view.

**Option C:** Implement Salesforce CRM Analytics, ingest SAP finance data into CRMA datasets via an API or flat-file export, and build the unified executive view in Salesforce.

Address the following in your post:

- What are the main trade-offs between Options A, B, and C for this company?
- Which option would you recommend, and what is the deciding factor in your recommendation?
- What is one data quality or latency challenge that the company would face in implementing your recommended option?
- How does an organization's existing skill set (SAP versus Salesforce expertise) legitimately influence the right tool choice, even when a theoretically "better" option exists?

Your response should demonstrate understanding of SAP Analytics Cloud, CRM Analytics, reporting architecture trade-offs, and organizational factors in technology decisions.

---

## Peer Response Guidelines

When replying to a classmate's post:

- Reference a specific claim or recommendation from their post and either add supporting evidence or offer a counter-argument
- Draw on Module 14 reading or video content to support your point
- Generic agreement ("Good points!") does not meet the 75-word requirement — every word must contribute new analytical value

---

## 10-Point Grading Rubric

| Criterion | 2 Points | 1 Point | 0 Points |
|-----------|----------|---------|----------|
| **Addresses all scenario questions** | All embedded questions substantively answered | Most questions answered; one is missing or very brief | Multiple questions unanswered or response is off-topic |
| **Demonstrates module content mastery** | Accurately references at least two specific Module 14 concepts with correct terminology | Uses module vocabulary but imprecisely or without clear connection to the scenario | Little or no use of module-specific content |
| **Analysis depth and specificity** | Concrete, specific recommendations with clear trade-off reasoning | Recommendations made without specific reasoning or trade-off acknowledgment | Opinions stated without analysis |
| **Writing quality** | Well organized, 175–225 words, professional tone, minimal grammatical errors | Mostly clear; minor organizational issues; length within 10% of target | Unclear, significantly off word count, or major errors impede comprehension |
| **Peer responses (two required)** | Both replies 75+ words, engage classmate's specific argument, add new content | One strong reply; second reply is brief or generic | Zero or one reply; replies add no new content |

**Total: 10 points**

---

## Sample Strong Opening Lines (to inspire, not copy)

For Scenario 1: "The most fundamental mistake in this dashboard is that it was designed around available data rather than around the decisions the executives actually need to make — when you put 22 metrics in front of a busy executive, you are asking them to do the analyst's job of identifying what matters..."

For Scenario 2: "The $13 million discrepancy would have been manageable if discovered during development, but presenting it to a sales director during UAT has created something much harder to fix than a configuration error — a credibility problem that will follow this dashboard for years..."

For Scenario 3: "The answer is almost never purely technical — Option B may be architecturally superior on paper, but if the company's entire analytics team lives in Salesforce and has no SAC experience, Option B's 'advantage' evaporates in the face of a six-month learning curve and significant consulting costs..."

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
