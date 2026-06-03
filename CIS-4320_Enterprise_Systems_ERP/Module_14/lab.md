# Lab: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

**Title:** Salesforce Report and Dashboard Design

**Estimated Time:** 90–120 minutes

**Format:** Individual work with written deliverables and screenshots

**Tools Required:** Salesforce Developer Edition org, web browser, word processor

**Submission:** Upload completed lab report (PDF or DOCX) to the LMS by the module due date.

---

## Learning Objectives

By completing this lab you will be able to:

- Build all four Salesforce report formats for defined business use cases
- Apply filters, bucket fields, and summary formulas to enhance report value
- Design and configure a Salesforce dashboard with multiple component types
- Evaluate a set of proposed KPIs and improve them using the SMART framework

---

## Lab Background

Clearwater Solutions is a B2B technology company using Salesforce Sales Cloud. The VP of Sales has asked for a set of standard reports and a performance dashboard to be ready before the quarterly business review. You are the Salesforce Administrator responsible for delivering these artifacts.

The Salesforce Developer Edition org includes sample data. You will use the Opportunity object as your primary data source.

---

## Part 1: Building the Four Report Formats (40 points)

### Task 1.1: Tabular Report — Open Opportunities List

Navigate to the Reports tab. Click "New Report." Select the "Opportunities" report type.

Build a tabular report with the following specifications:

- **Columns to include:** Opportunity Name, Account Name, Stage, Amount, Close Date, Owner Full Name
- **Filter:** Close Date = Current FQ (Fiscal Quarter) and Next FQ
- **Sort:** Close Date ascending

Save the report as "Open Opportunities — Current and Next FQ" in your Private Reports folder.

**Document the following:**

1. How many records appear in your report?

2. Is a tabular report suitable for displaying as a bar chart on a dashboard? Why or why not?

3. Export the report to CSV. Open it in a spreadsheet tool. How many columns are in the export?

---

### Task 1.2: Summary Report — Pipeline by Stage

Create a new report using the "Opportunities" report type.

Build a summary report with the following specifications:

- **Group rows by:** Stage
- **Columns:** Opportunity Name, Account Name, Amount, Close Date
- **Summary fields:** Sum of Amount per Stage, Count of Opportunity Name per Stage
- **Filter:** Stage not equal to "Closed Won" and Stage not equal to "Closed Lost"

Add a **bucket field** on Amount:

- Bucket name: "Deal Size"
- Bucket values:
  - $0–$9,999 = "Small"
  - $10,000–$99,999 = "Mid-Market"
  - $100,000+ = "Enterprise"

Add the "Deal Size" bucket as a column in the report.

Save the report as "Pipeline by Stage and Deal Size."

**Document the following:**

1. Which Stage has the highest total Amount? What is that total?

2. Looking at the bucket field, which Deal Size category has the most records?

3. Would a stacked bar chart of Amount by Stage, colored by Deal Size, be a meaningful visualization? Explain your reasoning in 2–3 sentences.

---

### Task 1.3: Matrix Report — Rep Performance by Quarter

Create a new report using the "Opportunities" report type.

Build a matrix report with the following specifications:

- **Row grouping:** Owner Full Name
- **Column grouping:** Close Date (grouped by Calendar Quarter)
- **Summary field in cells:** Sum of Amount
- **Filter:** Stage = "Closed Won"
- **Date range:** Last 4 Fiscal Quarters

Save the report as "Closed Won Revenue by Rep and Quarter."

**Document the following:**

1. Which rep has the highest total closed won amount across all quarters shown?

2. Does any rep show a declining trend across quarters? Describe what you observe.

3. Why is a matrix report more suitable for this analysis than a summary report?

---

### Task 1.4: Joined Report — Open Cases vs. Open Opportunities by Account

This task requires a Joined Report, which is the most complex format.

Create a new Joined Report. Add two report blocks:

**Block 1:**

- Report type: Accounts with Cases
- Columns: Account Name, Case Number, Status, Priority
- Filter: Status != Closed

**Block 2:**

- Report type: Accounts with Opportunities
- Columns: Account Name, Opportunity Name, Stage, Amount
- Filter: Stage != Closed Won, Stage != Closed Lost

The two blocks are joined on Account Name.

Save the report as "Accounts — Open Cases and Open Opportunities."

**Document the following:**

1. How many accounts have both open cases and open opportunities simultaneously?

2. Why might this report be strategically important for a customer success team?

3. What limitation does the Joined Report format have that makes it unsuitable for a simple dashboard bar chart?

---

## Part 2: Dashboard Design (35 points)

### Task 2.1: Create a Sales Performance Dashboard

Navigate to the Dashboards tab. Click "New Dashboard." Name it "Q2 Sales Performance Dashboard."

Add the following components. For each component, specify the source report and the component type:

**Component 1 — Pipeline by Stage (Horizontal Bar Chart)**

- Source: Pipeline by Stage and Deal Size (from Task 1.2)
- Chart type: Horizontal Bar
- Measure: Sum of Amount
- Group by: Stage
- Title: "Open Pipeline by Stage"

**Component 2 — Closed Won Revenue by Rep (Bar Chart)**

- Source: Closed Won Revenue by Rep and Quarter (from Task 1.3)
- Chart type: Grouped Bar (reps on X-axis)
- Measure: Sum of Amount (most recent full quarter)
- Title: "Closed Won Revenue — Latest Quarter"

**Component 3 — Total Open Pipeline (Metric)**

- Source: Pipeline by Stage and Deal Size
- Component type: Metric
- Display: Sum of Amount (Grand Total)
- Title: "Total Open Pipeline"

**Component 4 — Open Opportunity Count (Metric)**

- Source: Open Opportunities — Current and Next FQ
- Component type: Metric
- Display: Record Count
- Title: "Open Opportunities This FQ"

**Component 5 — Account Health (Table)**

- Source: Accounts — Open Cases and Open Opportunities
- Component type: Table (Block 1 — Cases)
- Display: Account Name, Open Case Count
- Title: "Accounts with Open Cases"

After adding all components, arrange them so that the two Metric components appear at the top, the bar charts below them, and the table at the bottom.

**Document the following:**

1. Screenshot the completed dashboard (or describe it in detail if screenshots are not possible).

2. What is the current "running user" on your dashboard? What would happen to the data displayed if you changed it to a specific Standard User instead of an admin?

3. A colleague asks you to make this dashboard available to all sales reps. Walk through the steps needed to share it appropriately. What folder permissions are required?

---

### Task 2.2: Configure a Dashboard Subscription

Configure the Q2 Sales Performance Dashboard to send a weekly email summary every Monday at 8:00 AM.

Document:

1. What options are available for subscription frequency?

2. Who receives the subscription you configured?

3. What is included in the subscription email — does the recipient get the live dashboard or a snapshot?

---

## Part 3: KPI Design Evaluation (25 points)

### Task 3.1: Critique Weak KPIs

The Clearwater VP of Sales has proposed the following "KPIs" for the QBR dashboard. Evaluate each one using the six-component KPI framework (definition, numerator/denominator, target, time horizon, owner, data source).

For each proposed KPI, identify what components are missing and rewrite it as a properly defined KPI.

**Proposed KPI 1:** "Track how many deals we close."

Your evaluation:

- What components are present?
- What components are missing?
- Rewritten KPI:

**Proposed KPI 2:** "Customer satisfaction."

Your evaluation:

- What components are present?
- What components are missing?
- Rewritten KPI:

**Proposed KPI 3:** "Quota attainment is 87%."

Your evaluation:

- What components are present?
- What components are missing?
- Rewritten KPI (if improvement needed):

---

### Task 3.2: Define Five KPIs for a Dashboard

Design five KPIs for the Clearwater Solutions executive dashboard. Each KPI must be fully defined using all six components.

**Format for each KPI:**

- KPI Name:
- Definition:
- Formula (numerator / denominator):
- Target:
- Time Horizon:
- Owner (job title):
- Data Source:
- Visualization type (gauge, metric, trend line, etc.):

KPIs should span at least three different business functions (sales, finance, operations, customer service, etc.).

---

### Task 3.3: Dashboard Redesign Recommendation

A screenshot of an existing Clearwater executive dashboard shows 24 metrics on a single screen, with no color coding, no trend indicators, and all numbers showing a point-in-time value with no comparison period.

Write a 200–250 word recommendation memo to the VP that:

- Identifies the three most significant problems with the current dashboard
- Recommends specific improvements based on the executive dashboard design principles from Module 14
- Proposes how many metrics the redesigned dashboard should show and which ones to prioritize

---

## Submission Checklist

Before submitting, verify:

- Part 1: All four reports created and documented; screenshots or descriptions of each; all analysis questions answered
- Part 2: Dashboard created with all five components; documentation of running user and sharing; subscription configured and documented
- Part 3: All three existing KPIs evaluated and rewritten; five new KPIs fully defined; redesign memo written
- Document has your name, student ID, and date on the cover page

---

## Grading Rubric

| Section | Points | Criteria |
|---------|--------|----------|
| Part 1 — Tabular, Summary, Matrix reports | 30 | Each report meets the stated specifications; analysis questions answered accurately |
| Part 1 — Joined report | 10 | Joined report configured correctly; limitations question answered with specificity |
| Part 2 — Dashboard components and configuration | 25 | All five components present; running user concept explained correctly; sharing steps are accurate |
| Part 2 — Dashboard subscription | 10 | Subscription configured; all three documentation questions answered |
| Part 3 — KPI critique | 10 | Each weak KPI correctly evaluated; rewritten KPIs include all six components |
| Part 3 — KPI design and memo | 15 | Five KPIs fully defined; memo addresses all three required points; 200–250 words |
| **Total** | **100** | |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
