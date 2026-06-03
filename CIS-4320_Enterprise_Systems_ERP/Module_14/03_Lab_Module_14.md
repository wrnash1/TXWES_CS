# Lab: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

In this lab you will build a multi-component Salesforce dashboard backed by four reports, evaluate a KPI design scenario, and critically assess a sample executive dashboard for design compliance. You will also document the data quality conditions required for your reports to be trustworthy.

**Estimated Time:** 75–90 minutes

**Deliverables:** Screenshots (Parts A and B) + written analysis (Parts C and D) submitted as a single PDF or Word document.

---

## Prerequisites

- Access to a Salesforce Developer Org (trailhead.salesforce.com — free)
- At least 15 Opportunity records with varied: Stage (Prospecting, Qualification, Proposal, Closed Won, Closed Lost), Close Date (spread across 3+ months), Amount ($5,000–$500,000), and Owner (at least 2 different users if possible)
- If you do not have enough records, use the Data Import Wizard to load sample data from a provided CSV template, or manually create records

---

## Part A — Build Four Source Reports (30 minutes)

### Report 1 — Pipeline by Stage (Summary Report)

1. Go to the **Reports** tab and click **New Report**.

2. Select the **Opportunities** report type. Click **Start Report**.

3. In the report builder, set the following:
   - Format: **Summary**
   - Group rows by: **Stage**
   - Columns to include: Opportunity Name, Account Name, Amount, Close Date, Owner Full Name
   - Add a summary: **Sum of Amount** at the Stage group level

4. Apply a filter: **Close Date** equals **This Quarter**.

5. Add an embedded chart:
   - Chart type: **Donut**
   - Plot values: **Sum of Amount**
   - Grouped by: **Stage**

6. Save the report as **Pipeline by Stage — Module 14 Lab** in the My Personal Custom Reports folder.

7. Take a screenshot of the completed report showing groupings, totals, and the embedded chart.

### Report 2 — Won vs. Lost by Month (Matrix Report)

1. Click **New Report** → **Opportunities** → **Start Report**.

2. Set the format to **Matrix**.

3. Row grouping: **Stage** (filter to show only Closed Won and Closed Lost using a field filter on Stage).

4. Column grouping: **Close Month** (group Close Date by Calendar Month).

5. Summary: **Count of Opportunities** and **Sum of Amount**.

6. Save as **Won vs. Lost by Month — Module 14 Lab**.

7. Screenshot the matrix grid showing counts and amounts by stage and month.

### Report 3 — Open Cases by Priority (Summary Report)

1. Click **New Report** → select the **Cases** report type → **Start Report**.

   Note: If your Developer Org has no Cases, create three sample Case records before this step — any subject, with Priority set to High, Medium, or Low.

2. Format: **Summary**.

3. Group rows by: **Priority**.

4. Columns: Case Number, Subject, Status, Date/Time Opened, Owner Full Name.

5. Filter: **Status** does not equal **Closed**.

6. Summary: **Count of Cases** at the Priority group level.

7. Save as **Open Cases by Priority — Module 14 Lab**.

8. Screenshot the grouped report.

### Report 4 — Accounts with No Open Opportunities (Tabular Report with Cross-Filter)

1. Click **New Report** → **Accounts with Opportunities** → **Start Report**.

2. Format: **Tabular**.

3. Columns: Account Name, Industry, Annual Revenue, Phone.

4. Add a **Cross-Filter**: Account does not have Opportunities where Stage is not equal to Closed Lost and Closed Won (i.e., show accounts with no open/active opportunities).

   Steps: Click **Add Cross-Filter** → Choose relationship: **Opportunities** → Select **without** → Add sub-filter: Stage not in (Prospecting, Qualification, Needs Analysis, Value Proposition, Id. Decision Makers, Perception Analysis, Proposal/Price Quote, Negotiation/Review).

5. Save as **Accounts with No Open Opportunities — Module 14 Lab**.

6. Screenshot the filtered account list.

---

## Part B — Build the Executive Dashboard (25 minutes)

### Dashboard Setup

1. Go to the **Dashboards** tab and click **New Dashboard**.

2. Name: **Sales & Service Executive View — Module 14 Lab**

3. Description: Executive overview of pipeline, closed business, and service cases.

4. Leave the running user as yourself for now.

### Add Four Components

**Component 1 — Pipeline Total (Metric)**

- Click **+ Component** → Source Report: **Pipeline by Stage — Module 14 Lab**
- Component Type: **Metric**
- Metric: **Sum of Amount**
- Header: **Total Open Pipeline**
- Footer: **This Quarter**
- Position: top-left

**Component 2 — Pipeline by Stage (Donut Chart)**

- Click **+ Component** → Source Report: **Pipeline by Stage — Module 14 Lab**
- Component Type: **Donut Chart**
- Plot values: **Sum of Amount** grouped by **Stage**
- Header: **Pipeline Distribution by Stage**
- Position: top-right

**Component 3 — Won vs. Lost Amounts (Bar Chart)**

- Click **+ Component** → Source Report: **Won vs. Lost by Month — Module 14 Lab**
- Component Type: **Bar Chart**
- Plot values: **Sum of Amount** grouped by **Stage**
- Header: **Closed Won vs. Closed Lost — This Quarter**
- Position: middle-left

**Component 4 — Open Cases by Priority (Table)**

- Click **+ Component** → Source Report: **Open Cases by Priority — Module 14 Lab**
- Component Type: **Table**
- Show: Priority groupings and Count of Cases
- Header: **Open Cases by Priority**
- Position: middle-right

### Dashboard Finalization

1. Save and refresh the dashboard.

2. Take a screenshot of the completed four-component dashboard.

3. Note the **Last Refreshed** timestamp displayed on the dashboard — record this in your write-up.

4. Click the **Refresh** button, wait for completion, and take a second screenshot showing the updated timestamp.

---

## Part C — KPI Design Analysis (10 minutes)

Read the following scenario and answer the questions below.

### Scenario

A regional sales director asks you to build a dashboard KPI called "Sales Activity Score." She defines it as: the total number of calls logged, emails sent, and tasks completed by her team in the current month, added together into a single number. She wants this displayed prominently at the top of her dashboard with a green/yellow/red indicator.

### Questions

Answer each question in 2–4 sentences:

1. Does this metric meet the definition of a KPI as defined in the reading? Identify which KPI criteria it satisfies and which it does not.

2. What is missing from the director's definition that would make this metric actionable? What additional information would you need before configuring the indicator thresholds?

3. Propose a revised version of this metric that better meets KPI design standards. Define the formula, the target threshold, and the alert threshold.

4. Identify one leading indicator and one lagging indicator that together would give a more complete picture of this sales team's performance than the Activity Score alone.

---

## Part D — Dashboard Design Critique (10 minutes)

Review the following description of a sample executive dashboard and answer the critique questions.

### Dashboard Description

A Finance VP's monthly dashboard contains: 22 numeric tiles showing various account balances and transaction counts, no charts or visualizations, no color-coded thresholds, no trend data (just current-month point-in-time values), a last-refresh timestamp from 11 days ago, and a note at the bottom saying "Data accurate as of last BW extraction."

### Critique Questions

Answer each question in 2–4 sentences:

1. Identify three specific violations of executive dashboard design principles in this example.

2. The last-refresh timestamp is 11 days old. What are two possible causes of this, and what steps would you take to investigate and resolve the issue?

3. Redesign this dashboard conceptually. Describe what you would change — how many metrics you would show, what visualizations you would use, and what context (trends, targets, benchmarks) you would add. You do not need to build it; describe it in 5–8 sentences.

---

## Submission Checklist

Before submitting, verify you have included:

- [ ] Screenshot: Report 1 — Pipeline by Stage (summary with chart)
- [ ] Screenshot: Report 2 — Won vs. Lost by Month (matrix grid)
- [ ] Screenshot: Report 3 — Open Cases by Priority (summary)
- [ ] Screenshot: Report 4 — Accounts with No Open Opportunities (cross-filter)
- [ ] Screenshot: Completed four-component dashboard (initial view)
- [ ] Screenshot: Dashboard after manual refresh (showing updated timestamp)
- [ ] Written answers to all four Part C questions
- [ ] Written answers to all three Part D questions

---

## Grading Criteria

| Component | Points |
|---|---|
| Four reports built correctly with proper type, grouping, and filters | 40 |
| Dashboard with four correctly configured components | 20 |
| Part C — KPI analysis (completeness and accuracy of reasoning) | 20 |
| Part D — Dashboard critique (accuracy and depth of critique and redesign) | 20 |
| **Total** | **100** |

---

*End of Lab — Module 14*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials
