# Quiz: Module 07 — Salesforce Sales Cloud and CRM

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

### Question 1

A sales representative at a technology company receives a list of contacts from a recent trade show. These contacts have expressed general interest but have not been qualified as real buyers. Which Salesforce object should be created for each contact on this list?

- A) Account — because each contact represents a company to do business with
- B) Opportunity — because each contact is a potential revenue source
- C) Lead — because these are unqualified prospects that have not yet been confirmed as real business opportunities
- D) Case — because trade show contacts often have questions that need resolution

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Leads are the purpose-built Salesforce object for unqualified prospects. They are isolated from active customer records until a rep confirms the prospect is worth pursuing, at which point the Lead is converted.
- *Why A is incorrect:* Accounts represent companies you actively do business with. Creating Accounts for unqualified trade show contacts pollutes the customer database with unverified records.
- *Why B is incorrect:* Opportunities represent active deals in progress with confirmed potential. Creating Opportunities for unqualified trade show contacts before any qualification has occurred misrepresents the pipeline.
- *Why D is incorrect:* Cases are customer service records for issues and requests. They are not used for new prospect tracking.

---

### Question 2

When a Salesforce rep converts a qualified Lead, which three records does Salesforce create simultaneously?

- A) Campaign, Event, and Task
- B) Account, Contact, and Opportunity
- C) Quote, Contract, and Order
- D) Report, Dashboard, and Activity

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Lead conversion is one of the most tested Salesforce concepts. A single conversion action creates the Account (company), Contact (individual), and Opportunity (deal) — all linked to each other. The original Lead is marked Converted and retained.
- *Why A is incorrect:* Campaigns, Events, and Tasks are marketing and activity objects. They are not created by Lead conversion.
- *Why C is incorrect:* Quotes, Contracts, and Orders come later in the sales lifecycle — after an Opportunity is won. They are not products of Lead conversion.
- *Why D is incorrect:* Reports and Dashboards are analytics objects. Tasks and Activities are not automatically created by Lead conversion (though a rep can manually log them afterward).

---

### Question 3

A Salesforce Opportunity has an Amount of $150,000 and is currently in the Proposal/Price Quote stage, which carries a default probability of 60%. What is the forecasted revenue contribution of this deal?

- A) $150,000 — the full amount is always used in pipeline reporting
- B) $90,000 — calculated as Amount × Probability ($150,000 × 0.60)
- C) $60,000 — calculated as Amount × (1 − Probability) representing the at-risk portion
- D) $0 — forecasted revenue is only counted for Closed Won opportunities

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Forecast Amount = Opportunity Amount × Stage Probability. $150,000 × 0.60 = $90,000. This probability-weighted value reflects the statistical expected value of the deal.
- *Why A is incorrect:* Using the full Amount regardless of stage would overstate the forecast for deals that may not close. Probability weighting is the foundation of pipeline forecasting.
- *Why C is incorrect:* The (1 − Probability) calculation gives the risk remainder — how much is at risk of not closing. The forecasted contribution is the probability-weighted expected value, not the risk portion.
- *Why D is incorrect:* Open Opportunities across all stages are included in pipeline forecasts. Counting only Closed Won deals would make forecasting reports useless — those are already booked revenue, not future predictions.

---

### Question 4

An administrator needs to ensure that sales reps cannot save an Opportunity if the Close Date is set to a date in the past. Which Salesforce tool is the correct solution?

- A) Assignment Rule — to route past-date Opportunities to a manager queue
- B) Approval Process — to send Opportunities with past-close dates to a manager for approval before saving
- C) Validation Rule — to block saving the Opportunity record when the Close Date is earlier than today
- D) Flow Builder — to automatically update the Close Date to tomorrow whenever it is set to a past date

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Validation Rules prevent a record from being saved when a formula condition evaluates to true. The formula `CloseDate < TODAY()` with an error message blocks the save at the point of data entry — the correct tool for enforcing field-level data quality constraints.
- *Why A is incorrect:* Assignment Rules determine record ownership routing. They do not validate field values or block record saves.
- *Why B is incorrect:* Approval Processes route records to human reviewers before specific actions. They do not enforce field validation at save time and require manual reviewer action.
- *Why D is incorrect:* A Flow that silently changes a date the rep intentionally set creates confusion and audit problems. Validation Rules are the standard approach for blocking invalid data entry, not auto-correcting it.

---

### Question 5

A sales manager wants to build a Salesforce report that shows total Opportunity Amount grouped by Stage, with each Stage as a row showing a subtotal. Which report type must be selected?

- A) Tabular — because tabular reports display all records in a structured format
- B) Joined — because multiple Opportunity objects need to be combined in one view
- C) Summary — because Summary reports support row groupings with subtotals
- D) Matrix — because Matrix reports show data in a two-dimensional grid layout

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Summary reports support grouping records by one or more fields in rows, with subtotals for each group. "Total Amount grouped by Stage" is the canonical Summary report use case.
- *Why A is incorrect:* Tabular reports are flat lists with no grouping or subtotals. They cannot aggregate data by a field like Stage.
- *Why B is incorrect:* Joined reports combine multiple report blocks with different source objects. The scenario only involves one object (Opportunities) and does not require combining datasets.
- *Why D is incorrect:* Matrix reports group by two fields — one for rows and one for columns — creating a cross-tabulation. The scenario describes a single dimension (Stage), which matches Summary, not Matrix.

---

### Question 6

What is the key difference between a standard Salesforce Dashboard and a Dynamic Dashboard?

- A) Standard Dashboards can have up to 10 components; Dynamic Dashboards can have up to 20
- B) Standard Dashboards run as a fixed user so all viewers see the same data; Dynamic Dashboards run as the logged-in user so each viewer sees their own data
- C) Standard Dashboards refresh in real time; Dynamic Dashboards must be refreshed manually
- D) Standard Dashboards support bar charts and tables; Dynamic Dashboards support only metric tiles

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* This is a high-frequency exam topic. Standard dashboards run as a specified "running user" — everyone who views the dashboard sees that user's data. Dynamic Dashboards execute as the logged-in viewer, so each person sees only the records they have access to.
- *Why A is incorrect:* The component limit is reversed — standard dashboards support up to 20 components, and Dynamic Dashboards also support up to 20. There is no 10-component limit on standard dashboards.
- *Why C is incorrect:* Both standard and Dynamic Dashboards refresh on demand or on a schedule; the real-time vs. manual distinction does not define the difference between them.
- *Why D is incorrect:* Both standard and Dynamic Dashboards support the same component types: Charts, Gauges, Metrics, Tables, and custom components.

---

### Question 7

A Salesforce administrator is asked to configure automatic routing of newly created Leads to specific sales reps based on the Lead's geographic region. Which feature should the administrator configure?

- A) Validation Rule — to flag Leads that do not have a region specified
- B) Lead Assignment Rule — to automatically assign new Leads to owners based on defined criteria
- C) Flow Builder — to create a Task for the default Lead owner to manually reassign the record
- D) Approval Process — to route the Lead to the regional manager before it is assigned to a rep

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Lead Assignment Rules are the purpose-built Salesforce feature for automatic Lead routing. Criteria can include geography, industry, lead source, company size, or any Lead field. When criteria are met, the rule assigns the Lead to the matching rep or queue automatically at record creation.
- *Why A is incorrect:* Validation Rules block invalid saves — they do not route records to different owners. A missing region field could be caught by a Validation Rule, but routing itself requires an Assignment Rule.
- *Why C is incorrect:* A Flow that creates a Task for manual reassignment is a workaround, not the standard solution. It adds unnecessary manual steps that Assignment Rules eliminate.
- *Why D is incorrect:* Approval Processes route records for human approval before a business action. Routing a Lead to a regional manager before rep assignment is a governance model choice, but it is not the standard Lead routing mechanism.

---

### Question 8

Which of the following correctly describes what the Opportunity Path feature provides to a sales representative?

- A) A visual progress bar at the top of the record showing the current Stage, required fields for that Stage, and admin-authored guidance notes
- B) A predictive AI score from 1 to 99 showing the probability the deal will close based on historical data
- C) A list of all competitor products that should be addressed during the sales process
- D) An automated email to the customer summarizing the current deal status and next steps

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Path is a UI component configured by administrators. It displays as a visual step bar above the record, highlights the active Stage, shows Key Fields the rep should complete at that Stage, and displays Guidance for Success text written by the admin.
- *Why B is incorrect:* A predictive AI score from 1 to 99 describes Einstein Opportunity Scoring — a separate AI feature, not Path. Path is a UI guidance tool, not a machine learning prediction.
- *Why C is incorrect:* Competitor product tracking is handled through the Competitors related list on Opportunities — a different feature entirely, not Path.
- *Why D is incorrect:* Automated customer-facing emails are configured via Flow Builder or email templates. Path is an internal UI tool for the sales rep, not a customer communication feature.

---

### Question 9

Einstein Activity Capture is enabled for a sales team. What impact does this have on the reps' daily workflow?

- A) It automatically creates new Opportunity records when an email mentions pricing
- B) It automatically logs emails and calendar events from Gmail or Outlook to related Salesforce records, reducing manual data entry
- C) It sends automated follow-up emails to Leads and Contacts on behalf of the rep
- D) It scores each sales rep's activity level and generates a performance report for managers

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Einstein Activity Capture syncs emails and calendar events from the rep's connected Gmail or Outlook account into Salesforce, automatically attaching them to the related Contacts, Accounts, and Opportunities. The rep no longer needs to manually log every interaction.
- *Why A is incorrect:* Einstein Activity Capture does not parse email content and create Opportunity records. Creating records from email content would require custom development or a separate email-to-case/opportunity product.
- *Why C is incorrect:* Sending automated emails on behalf of reps is handled by Email Automation features or Salesforce Engage — not Einstein Activity Capture. Activity Capture logs existing emails; it does not send new ones.
- *Why D is incorrect:* Scoring rep activity and generating manager reports describes a sales management analytics capability. While Activity Capture data feeds into activity reports, the feature itself is about logging synchronization, not performance scoring.

---

### Question 10

A Salesforce Opportunity moves from Negotiation/Review (80% probability) to Closed Won (100% probability). The deal Amount is $200,000. What happens to the Forecast Category field when the Stage changes to Closed Won?

- A) The Forecast Category remains as "Best Case" because the deal has not yet been invoiced
- B) The Forecast Category changes to "Closed" and the full $200,000 is recognized as booked revenue in the forecast
- C) The Forecast Category changes to "Pipeline" to keep the deal visible in open pipeline reports
- D) The Forecast Category is manually updated by the manager after reviewing the deal in the weekly pipeline call

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In Salesforce's standard forecast model, Closed Won maps to the "Closed" Forecast Category. The full Amount ($200,000 at 100% probability = $200,000) moves from forecast to booked revenue. This is the final state in the opportunity lifecycle and is reflected immediately in forecast rollup reports.
- *Why A is incorrect:* "Best Case" is the Forecast Category for Proposal and Negotiation stages — it reflects deals that are likely but not yet confirmed. Closed Won always maps to "Closed," not "Best Case."
- *Why C is incorrect:* "Pipeline" is the Forecast Category for early-stage Opportunities like Prospecting and Qualification. A Closed Won deal exits the open pipeline and moves to closed bookings.
- *Why D is incorrect:* Forecast Category is automatically set by the Stage field (based on the Sales Process configuration). Managers can override forecast amounts manually in the Forecasts tab, but the Forecast Category itself is system-driven by Stage, not manually set by the manager.
