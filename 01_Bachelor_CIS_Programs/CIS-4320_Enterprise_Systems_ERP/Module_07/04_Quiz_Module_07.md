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

---

### Question 11

(5 points)

A Salesforce administrator needs to ensure that the "Decision Maker" field on an Opportunity is required before a rep can move the Stage to "Proposal/Price Quote." Which Salesforce feature enforces this requirement at a specific stage, not globally?

- A) Validation Rule — with a formula checking that Stage = "Proposal/Price Quote" AND Decision Maker is blank
- B) Required Field setting on the page layout — marking the field as required globally
- C) Assignment Rule — routing the record to the manager if the Decision Maker is missing
- D) Duplicate Rule — flagging the record as a duplicate if the Decision Maker is missing

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* A Validation Rule can combine Stage-conditional logic with a field-blank check: `AND(ISPICKVAL(StageName, "Proposal/Price Quote"), ISBLANK(Decision_Maker__c))`. This blocks the save only when the condition is true, enforcing the requirement at the specific stage without requiring it universally.
  - *Why B is incorrect:* Making a field required on the page layout enforces it globally on every save regardless of Stage — this would block records at Prospecting and Qualification stages too, which is not the requirement.
  - *Why C is incorrect:* Assignment Rules route records to owners; they do not enforce data completeness requirements or block record saves.
  - *Why D is incorrect:* Duplicate Rules identify potential duplicate records based on matching criteria; they do not enforce field completeness requirements.

---

### Question 12

(5 points)

A customer service team leader notices that 40% of Cases are being closed by agents without a Knowledge Article being attached. Management wants to require agents to link at least one Knowledge Article before closing a Case. Which combination of Salesforce features best enforces this?

- A) A Validation Rule that blocks the Status change to "Closed" when no Knowledge Articles are associated with the Case
- B) A Flow that sends the agent an email reminder when a Case has been open for 24 hours without a Knowledge Article
- C) An Approval Process that routes all Cases to the team leader before they can be closed
- D) A required field on the Case layout making the Knowledge Article lookup field mandatory

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* A Validation Rule can check whether the Case is being set to "Closed" status and whether no Knowledge Articles are related. This blocks the save at the exact moment the agent attempts to close without compliance — the most targeted and efficient enforcement mechanism.
  - *Why B is incorrect:* An email reminder is advisory and does not prevent the non-compliant action from occurring. Agents could still close cases without linking a Knowledge Article.
  - *Why C is incorrect:* Routing all Cases to the team leader for closure approval adds review overhead on every case, not just non-compliant ones, and creates a bottleneck that slows resolution times.
  - *Why D is incorrect:* The Knowledge Article related list is not a single lookup field on the Case record; it is a relationship managed through a junction object. A "required field" on the layout cannot enforce a related list entry.

---

### Question 13

(5 points)

In Salesforce Sales Cloud, which object stores the record of a formal written commercial offer sent to a customer, including specific product line items, quantities, and a calculated total price?

- A) Opportunity
- B) Order
- C) Quote
- D) Contract

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* A Quote is the formal price proposal document associated with an Opportunity. It contains Quote Line Items (specific products with quantities and prices) and can be converted to PDF and sent to the customer. Multiple competing Quotes can be created for a single Opportunity.
  - *Why A is incorrect:* An Opportunity represents the deal itself — the potential revenue event. It is the parent of a Quote but does not itself contain itemized products and a formal price document.
  - *Why B is incorrect:* An Order is created after a Quote is accepted; it represents the formal commitment from the customer to purchase. It comes after the Quote in the lifecycle.
  - *Why D is incorrect:* A Contract is a legal agreement governing the relationship with a customer over time (terms, renewal dates, pricing). It is distinct from a point-in-time price proposal.

---

### Question 14

(5 points)

A Salesforce Opportunity record shows: Amount = $320,000, Stage = "Value Proposition" (Probability = 25%), Close Date = 3 months from today. What is the weighted forecast amount for this deal?

- A) $320,000
- B) $80,000
- C) $240,000
- D) $160,000

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Forecast Amount = Amount × Probability. $320,000 × 0.25 = $80,000. Value Proposition at 25% probability reflects early-stage uncertainty, so only $80,000 of the potential $320,000 contributes to the weighted pipeline forecast.
  - *Why A is incorrect:* $320,000 is the unweighted face value of the Opportunity. Using this figure without the probability weighting would overstate the forecast for an early-stage deal.
  - *Why C is incorrect:* $240,000 represents $320,000 × 0.75, which is the (1 − Probability) remainder — the risk portion, not the forecasted contribution.
  - *Why D is incorrect:* $160,000 would correspond to a 50% probability weighting, which does not match the stated 25% for Value Proposition stage.

---

### Question 15

(5 points)

A Salesforce administrator wants to display a real-time count of open Cases on the Account record, visible to all account team members. Which Salesforce feature should be used?

- A) A Custom Report exported to Excel and uploaded to the Account as a file attachment
- B) A Roll-Up Summary field on the Account that counts Case records with Status not equal to "Closed"
- C) A scheduled Dashboard refreshed nightly showing open Case counts per Account
- D) A Custom Formula field on the Case that calculates the number of days it has been open

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Roll-Up Summary fields on a master object (Account) can COUNT, SUM, MIN, or MAX values from related child records (Cases) filtered by criteria. A COUNT with filter "Status != Closed" gives the real-time open Case count directly on the Account record.
  - *Why A is incorrect:* Exporting a report to Excel and uploading it manually defeats the purpose of a CRM — it creates a static, stale data artifact rather than a live count.
  - *Why C is incorrect:* A nightly Dashboard refresh is not "real-time" — it would be up to 24 hours stale. A Roll-Up Summary field updates in real time as Cases are created or closed.
  - *Why D is incorrect:* A formula field on the Case calculates a value for that specific Case record; it does not aggregate or summarize data across multiple child records onto the parent Account.

---

### Question 16

(5 points)

In Salesforce Service Cloud, what is the purpose of an **Entitlement**?

- A) An authorization control that restricts which users can create Case records
- B) A record that defines the support level a customer is contractually entitled to — including response time SLAs, support hours, and the number of support incidents covered
- C) A billing record tracking how many service calls have been invoiced to the customer account
- D) A knowledge base category that organizes articles by product line for agent use

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Entitlements in Salesforce Service Cloud define the service level commitments for a customer or asset. They specify response time SLAs, coverage hours, and incident counts. When a Case is created, Salesforce checks the customer's entitlement to apply the correct milestone timers and escalation rules.
  - *Why A is incorrect:* Access control for Case creation is managed through Profiles and Permission Sets — not Entitlements. Entitlements are service-level objects, not security objects.
  - *Why C is incorrect:* Billing and invoice records for service calls are typically managed in the ERP (FI-AR) or in Salesforce Billing. Entitlements define what is covered, not what is charged.
  - *Why D is incorrect:* Knowledge base categorization is managed through Data Categories on Knowledge Articles — a separate configuration feature, not Entitlements.

---

### Question 17

(5 points)

A Salesforce Matrix Report groups Opportunity Amount by both Stage (rows) and Product Family (columns). The report shows totals for each Stage-Product combination. Which statement about this report type is accurate?

- A) A Matrix Report can only group by two fields and supports a maximum of 2,000 records
- B) A Matrix Report is the correct type for cross-tabulation — it shows aggregated values at the intersection of row and column groupings, making it ideal for comparing two dimensions simultaneously
- C) A Matrix Report can display individual record details in the cells rather than aggregated values
- D) Matrix Reports cannot include chart components — only Summary and Joined reports support charts

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Matrix reports provide cross-tabulation: rows grouped by one field (Stage), columns grouped by another (Product Family), with aggregated values (sum of Amount) at each intersection. This is the correct tool for comparing two dimensions simultaneously.
  - *Why A is incorrect:* While Matrix reports do group by two dimensions, the 2,000-record limit applies to Tabular reports (for export purposes), not to all report types in the same way.
  - *Why C is incorrect:* Matrix report cells show aggregated values (sums, counts, averages) — not individual record details. Tabular reports display individual records; Summary and Matrix reports display aggregates.
  - *Why D is incorrect:* Matrix reports do support chart components. Charts can be added to Summary, Matrix, and Joined reports in Salesforce.

---

### Question 18

(5 points)

Which Salesforce feature allows an administrator to define the specific stages and stage-transition requirements for a particular type of sales process, ensuring that different product lines or business units follow different Opportunity stage sequences?

- A) Sales Process (with associated Record Types)
- B) Opportunity Teams
- C) Territory Management
- D) Price Books

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Sales Processes define the set of Stage picklist values available for Opportunities of a given type. Record Types link Opportunities to a specific Sales Process, allowing different business units or product categories to have different stage sequences (e.g., a hardware sales process vs. a services sales process).
  - *Why B is incorrect:* Opportunity Teams define the internal team members who collaborate on a deal and their access levels. They do not control the stage sequence or process flow.
  - *Why C is incorrect:* Territory Management controls which users are assigned to which geographic or segmentation-based territories. It affects record ownership and visibility, not stage workflows.
  - *Why D is incorrect:* Price Books define the products and prices available for selection on an Opportunity or Quote. They do not control stage sequences or process flow.

---

### Question 19

(5 points)

A B2B technology company uses Salesforce. An Account has three Contacts: the Economic Buyer (CFO), the Technical Evaluator (IT Director), and the Champion (internal advocate). Which Salesforce feature allows the sales team to track each Contact's role in the purchasing decision directly on the Opportunity?

- A) Account Team Members
- B) Opportunity Contact Roles
- C) Opportunity Splits
- D) Campaign Members

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Opportunity Contact Roles allow a sales rep to link multiple Contacts to a single Opportunity and assign each Contact a role (Economic Buyer, Technical Evaluator, Champion, Decision Maker, etc.). This captures the full decision-making structure within the buying organization.
  - *Why A is incorrect:* Account Team Members tracks the internal Salesforce users who work on an Account, not the external customer contacts involved in a purchasing decision.
  - *Why C is incorrect:* Opportunity Splits allocate credit for the Opportunity revenue among the internal sales team members. They deal with internal credit attribution, not external contact roles.
  - *Why D is incorrect:* Campaign Members track which Contacts or Leads responded to a specific marketing campaign. They are a marketing attribution tool, not a deal-role tracking feature.

---

### Question 20

(5 points)

Salesforce Einstein Lead Scoring assigns each Lead a score from 1 to 99. A score of 85 means:

- A) The Lead has been contacted 85 times by the sales team and is a high-engagement prospect
- B) The Lead is ranked in the 85th percentile compared to other Leads in the org — indicating it shares characteristics with Leads that have historically converted at a higher rate
- C) The Lead was submitted 85 days ago and is being flagged for follow-up before expiring
- D) The Lead has 85% probability of becoming a customer within 30 days based on external market data

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Einstein Lead Scoring uses machine learning trained on the org's historical Lead conversion data. A score of 85 means the Lead is in the 85th percentile of conversion likelihood compared to other Leads in that specific org — it shares field characteristics (industry, company size, source, engagement) with Leads that historically converted.
  - *Why A is incorrect:* The score is not a count of interactions; Einstein calculates it from field data and historical conversion patterns, not activity frequency.
  - *Why C is incorrect:* The score does not represent days since creation; Salesforce has separate "Days Since Last Activity" fields for aging tracking.
  - *Why D is incorrect:* Einstein Lead Scoring is a relative ranking within the org's own data, not an absolute probability percentage derived from external market data. The 85th percentile in one org may correspond to a very different conversion rate than in another org.
