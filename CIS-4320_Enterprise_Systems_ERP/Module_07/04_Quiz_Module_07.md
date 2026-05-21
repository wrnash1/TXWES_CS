# Quiz: Module 07 - Customer Relationship Management Modules

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Which business entity is the primary focus of a Customer Relationship Management (CRM) module?

* A) Raw material vendors and their delivery performance records
* B) Warehouse bin locations and inventory storage assignments
* C) Customers and sales leads — managing interactions, pipelines, and support cases
* D) Corporate employee payroll records and benefits enrollment data

* **Correct Answer:** C) CRM systems track customer details, sales interactions, pipelines, and helpdesk cases to help businesses build and maintain profitable customer relationships.
* **Distractor Analysis:**
  * *Why C is correct:* CRM is designed for the customer-facing side of the business — marketing, sales, and service — not internal operations.
  * *Why A is incorrect:* Vendor management belongs to the ERP Supply Chain Management module (SAP MM), not CRM.
  * *Why B is incorrect:* Warehouse bin locations are managed in the ERP Warehouse Management module (SAP WM/EWM), not CRM.
  * *Why D is incorrect:* Employee payroll and benefits are managed in the ERP Human Capital Management module (SAP HCM/SuccessFactors), not CRM.

---

### Question 2

In Salesforce, which of the following best describes a **sales pipeline**?

* A) A database table that stores all vendor payment records organized by invoice due date
* B) A visual representation of active sales opportunities organized by their current stage, used to forecast revenue and manage sales team priorities
* C) An automated process that generates purchase requisitions when inventory falls below the reorder point
* D) A customer service queue that routes inbound support cases to the appropriate service team

* **Correct Answer:** B) A sales pipeline is the stage-based view of all open opportunities in Salesforce, giving managers visibility into projected revenue and helping sales reps focus on deals most likely to close.
* **Distractor Analysis:**
  * *Why B is correct:* In Salesforce, the Opportunity object has a Stage picklist (Prospecting, Qualification, Proposal, Negotiation, Closed Won/Lost) that represents the pipeline stages; pipeline reports and forecasts are built from this data.
  * *Why A is incorrect:* Vendor payment records organized by due date describe the Accounts Payable aging report in an ERP financial module, not a CRM sales pipeline.
  * *Why C is incorrect:* Generating purchase requisitions when stock falls below a reorder point describes MRP in the ERP Supply Chain module, not a CRM concept.
  * *Why D is incorrect:* A case queue routes customer support tickets in Salesforce Service Cloud; it is a service concept, not a sales pipeline.

---

### Question 3

A sales representative at a software company has been emailing a prospect named Sarah Chen at Acme Corp for three months. Sarah has expressed budget approval and asked for a formal proposal. Which Salesforce action correctly models this progression?

* A) Create a new Case record linked to Acme Corp to track the service request
* B) Convert the Lead record for Sarah Chen, creating an Account for Acme Corp, a Contact for Sarah Chen, and an Opportunity for the pending deal
* C) Create a new Campaign to send marketing emails to Acme Corp's entire contact list
* D) Create a new Contract record attached to Acme Corp to formalize the agreement

* **Correct Answer:** B) Lead conversion is the correct Salesforce action when a prospect is qualified — it creates the Account, Contact, and Opportunity records that represent the company, the person, and the potential sale.
* **Distractor Analysis:**
  * *Why B is correct:* Salesforce Lead conversion is specifically designed for this scenario — a prospect who has self-identified as a buyer triggers the creation of the three linked objects that allow full pipeline tracking and reporting.
  * *Why A is incorrect:* Cases are for customer service issues, not for tracking active sales pursuits.
  * *Why C is incorrect:* Campaigns are for mass marketing outreach; they are not used to track an individual sales pursuit that is already in active negotiation.
  * *Why D is incorrect:* Contracts formalize agreements with existing customers after a deal is closed; they are not used mid-sales-cycle before an opportunity is won.

---

### Question 4

A customer calls a company's support line reporting that a product they received is defective and they want a replacement. What Salesforce object should the service agent create to track this interaction from report to resolution?

* A) Lead — to track the customer as a potential new buyer
* B) Opportunity — to record the potential revenue from a replacement sale
* C) Case — to track the customer's reported issue through assignment, investigation, and resolution
* D) Campaign — to send the customer a satisfaction survey after the issue is resolved

* **Correct Answer:** C) A Case in Salesforce Service Cloud represents a customer-reported issue; it captures the problem description, tracks status through a queue, and logs all communications until the issue is resolved and the case is closed.
* **Distractor Analysis:**
  * *Why C is correct:* The Case object is Salesforce's core service management record — it ties the defect report to the Account and Contact, tracks SLA compliance, and provides the service agent with a full history of the customer relationship.
  * *Why A is incorrect:* A Lead represents a potential new customer who has not yet purchased; an existing customer with a product defect is already in the system as an Account and Contact.
  * *Why B is incorrect:* An Opportunity tracks a potential sale; a product replacement under warranty is a service transaction, not a new revenue opportunity.
  * *Why D is incorrect:* A Campaign is a marketing outreach initiative for mass communication; it is not the correct object for tracking an individual customer service issue to resolution.

---

### Question 5

A sales manager wants to see which sales representatives have the most opportunities in the Proposal stage and what the combined value of those deals is. Where in Salesforce would this information be found?

* A) In the General Ledger account balance report, filtered by sales region
* B) In a Salesforce Report or Dashboard built on the Opportunity object, filtered by Stage equals "Proposal"
* C) In the Employee Performance scorecard in the HR module
* D) In the Vendor Evaluation report filtered by supplier delivery ratings

* **Correct Answer:** B) Salesforce Reports and Dashboards built on the Opportunity object provide exactly this view — filtering by Stage, grouping by Owner (sales rep), and summing the Amount field gives the manager the pipeline visibility they need.
* **Distractor Analysis:**
  * *Why B is correct:* Salesforce's built-in reporting engine allows users to filter, group, and summarize Opportunity records by any field combination. Pipeline reports by stage and owner are one of the most common Salesforce report types.
  * *Why A is incorrect:* The General Ledger records closed financial transactions; it does not track open sales opportunities by stage.
  * *Why C is incorrect:* Employee performance scorecards are HR module records that track workforce metrics, not sales pipeline data.
  * *Why D is incorrect:* Vendor evaluation reports measure supplier performance in the ERP procurement module; they have no connection to the sales pipeline.
