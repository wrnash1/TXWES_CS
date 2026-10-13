# Video Script: Module 07 - Customer Relationship Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22-24 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### [00:00 - 01:30] Opening

Professor Nash on camera. Title card: "Module 07 - Customer Relationship Management Modules."

"Welcome back to CIS-4320. In Module 06 we covered the supply chain — the back-office operational engine. Now we move to the front office: Customer Relationship Management.

CRM is where your business faces its customers. Every sales conversation, every support call, every marketing campaign, every renewal negotiation — CRM is the system of record for all of it. While ERP focuses on internal operations — procurement, manufacturing, finance — CRM focuses on external relationships and revenue. The most important CRM platform in the world today is Salesforce, and the Salesforce Certified Associate exam is one of the credentials this course prepares you for.

Today we cover the Salesforce data model, the core CRM objects, the Sales Cloud and Service Cloud functional areas, CRM-ERP integration architecture, and how to think about CRM as the front-office complement to ERP's back-office capabilities. These concepts appear heavily on the Salesforce Associate exam."

---

### [01:30 - 05:00] CRM vs. ERP — Front Office and Back Office

Cut to slide: "CRM and ERP — Two Sides of the Enterprise."

"Let me start by clearly separating CRM from ERP because students often confuse them.

ERP — Enterprise Resource Planning — manages the inside of the business: financial accounting, procurement, inventory, manufacturing, payroll. The primary audience for ERP is the internal team: accountants, warehouse managers, HR administrators.

CRM — Customer Relationship Management — manages the outside of the business: the relationships with customers, prospects, and partners. The primary audience is the revenue-generating team: sales representatives, account managers, marketing, and customer service.

[SHOW DIAGRAM: Two columns side by side. Left column labeled 'ERP (Back Office)' with items: Financial Accounting, Procurement, Inventory, Manufacturing, Payroll. Right column labeled 'CRM (Front Office)' with items: Sales Pipeline, Customer Accounts, Marketing Campaigns, Support Cases, Service History. A double-headed arrow in the middle labeled 'Integration: Quotes, Orders, Invoices, Fulfillment Status.' Below: SAP S/4HANA as the ERP example; Salesforce as the CRM example.]

The integration point is critical: when a sales rep in Salesforce wins a deal and converts an Opportunity to an Order, that order flows into the ERP system for fulfillment, inventory management, and financial accounting. The customer does not see or care about this handoff — but the business absolutely depends on it working correctly. This is the CRM-ERP integration we will discuss at the end of the module."

---

### [05:00 - 10:00] Salesforce Data Model — Core Objects

Cut to slide: "Salesforce Core Objects — The CRM Data Model."

"Salesforce organizes customer data around five core objects. Understanding these objects is the foundation of the Salesforce Associate exam.

First: Leads. A Lead is an unqualified prospective customer — someone who has expressed interest but has not yet been verified as a real opportunity. Leads can come from trade shows, web forms, purchased lists, or marketing campaigns. The key point about Leads is that they are a staging area. You do not do business with a Lead — you do business with an Account, Contact, and Opportunity.

Second: Accounts. An Account represents a company or organization you do business with. Accounts are the anchor of the Salesforce data model — almost everything else attaches to an Account. Your existing customers, your key prospects, and your partners are all Accounts.

Third: Contacts. A Contact is an individual person at an Account. A Contact is always associated with an Account. Sarah Chen, the procurement manager at Acme Corp, is a Contact linked to the Acme Corp Account.

Fourth: Opportunities. An Opportunity represents a potential sale in progress. It is linked to an Account and typically to one or more Contacts. An Opportunity has a Stage — from Prospecting through Closed Won or Closed Lost — and an Amount that represents the expected revenue.

Fifth: Cases. A Case represents a customer issue, question, or complaint that needs resolution. Cases are the core of Service Cloud. A Case is linked to an Account and Contact, and the service team manages it from open to closed.

[SHOW DIAGRAM: An entity-relationship style diagram. Lead (top left) with a dashed arrow labeled 'Lead Conversion' pointing to three boxes: Account, Contact, Opportunity. Below Account: Cases (linked to Account and Contact). Arrows labeled '1:M' from Account to Contact, Account to Opportunity, Account to Case. Note at bottom: 'All five objects are standard objects in Salesforce — no custom development required.']

The Lead conversion process is important for the exam. When a salesperson qualifies a Lead — meaning the prospect is real, has budget, and is interested — they convert the Lead. Salesforce converts the Lead record into three linked records: an Account for the company, a Contact for the person, and an Opportunity for the potential deal. The original Lead record is marked Converted and remains in the system for reporting."

---

### [10:00 - 14:00] Sales Cloud — Pipeline Management

Cut to slide: "Sales Cloud — Managing the Pipeline."

"Salesforce Sales Cloud is the suite of features that supports the sales team from lead generation to closed deal. The centerpiece is the Opportunity pipeline.

An Opportunity moves through a series of stages that represent where you are in the sales process. Each stage has a Probability percentage — a built-in forecast of likelihood to close. A typical Sales Cloud stage sequence might look like this: Prospecting at 10%, Qualification at 20%, Needs Analysis at 40%, Proposal/Price Quote at 60%, Negotiation at 80%, Closed Won at 100%, Closed Lost at 0%.

[SHOW DIAGRAM: A horizontal pipeline visualization showing stages as boxes from left to right: Prospecting (10%) through Qualification (20%) through Needs Analysis (40%) through Proposal (60%) through Negotiation (80%) through Closed Won (100%). Below the pipeline, a bar chart showing number of deals at each stage. A caption: 'Forecast Amount = Opportunity Amount x Stage Probability.']

Salesforce builds pipeline reports and forecasts from this data automatically. The sales manager can see every open opportunity, which stage it is in, who owns it, when it is expected to close, and what the forecasted revenue is — all from a real-time dashboard.

Three Sales Cloud automation tools are important for the exam. First, Approval Processes allow deals above a certain discount threshold to be routed to a manager for approval before the quote is sent to the customer. Second, Flow Builder allows rules-based automation — for example, automatically creating a follow-up task when an Opportunity moves to the Proposal stage. Third, Validation Rules prevent data entry errors — for example, requiring that an Expected Close Date be in the future.

Exam tip: All three tools — Approval Processes, Flow Builder, and Validation Rules — are configuration, not code. They are no-code or low-code automation tools that administrators set up in the Salesforce UI."

---

### [14:00 - 18:00] Service Cloud — Case Management and SLAs

Cut to slide: "Service Cloud — Customer Support Operations."

"Salesforce Service Cloud adds customer service capabilities on top of the core CRM platform. The central object is the Case.

A Case lifecycle works like this: a customer contacts support by phone, email, web form, or chat. A Case is created and assigned to a queue or a specific agent. The agent investigates, communicates with the customer, and resolves the issue. The Case is closed and a satisfaction survey may be sent automatically.

Service Level Agreements — SLAs — are managed in Service Cloud through a feature called Entitlements and Milestones. An Entitlement defines what level of service a customer is entitled to based on their support contract — for example, Priority 1 issues resolved within 4 hours, Priority 2 within 24 hours. A Milestone is a checkpoint that tracks whether those SLA times are being met. If a Case is approaching its resolution deadline, Service Cloud can automatically escalate it to a senior agent or a manager.

[SHOW DIAGRAM: Case lifecycle flow. Box 1: 'Case Created' (phone/email/chat). Arrow to Box 2: 'Case Assigned' (queue or agent). Arrow to Box 3: 'Investigation and Customer Communication.' Arrow to Box 4: 'Resolution Posted.' Arrow to Box 5: 'Case Closed — CSAT Survey Sent.' Below the flow, a parallel SLA timeline: 'SLA Clock Starts to Milestone 1: First Response Within 2 Hours to Milestone 2: Resolution Within 24 Hours to SLA Met or Escalated.']

Knowledge Base integration is another key Service Cloud capability. When an agent resolves a Case, they can link it to a Knowledge Article — a documented solution. Future agents handling similar issues can search the Knowledge Base and find the resolution without starting from scratch. Over time, the Knowledge Base becomes the institutional memory of every issue the support team has ever resolved.

Exam tip: On the Salesforce Associate exam, understand the distinction between Sales Cloud objects (Lead, Opportunity) and Service Cloud objects (Case, Entitlement). Both use the same Account and Contact as the customer anchor."

---

### [18:00 - 21:00] CRM-ERP Integration Architecture

Cut to slide: "CRM + ERP — The Complete Customer Journey."

"The most powerful business capability comes from connecting CRM and ERP. Let me trace a complete customer journey to show where the handoff happens.

Step one: A prospect becomes a qualified Lead in Salesforce. Step two: The Lead is converted to Account, Contact, and Opportunity. Step three: The sales rep builds a Quote in Salesforce using the Products catalog. Step four: The customer accepts the proposal and the Opportunity is marked Closed Won. Step five: The closed Opportunity triggers an Order record in Salesforce. Step six: The Order flows via integration to the SAP SD module where a Sales Order is created. Step seven: SAP SD triggers MM inventory management to check stock availability. Step eight: SAP posts the delivery, goods issue, and revenue recognition to FI. Step nine: The customer's payment in SAP FI AR flows back to Salesforce to update the Account's payment status.

[SHOW DIAGRAM: Two swim lanes. Top lane labeled 'Salesforce CRM': Lead then Account/Contact/Opportunity then Quote then Closed Won then Order. Bottom lane labeled 'SAP ERP': Sales Order (SD) then Availability Check (MM) then Goods Issue (MM) then Revenue Recognition (FI) then Customer Payment (FI-AR). A vertical dashed line between the lanes labeled 'Integration Layer (API/Middleware)' with arrows crossing in both directions at the Order/Sales Order boundary and at the Payment boundary.]

The integration layer in the middle — labeled here as API or Middleware — is where most CRM-ERP integration projects succeed or fail. The data formats, field mappings, error handling, and timing of data transfers must all be carefully designed. We will cover integration architecture in detail in Module 11."

---

### [21:00 - 23:00] Module Summary and Exam Tips

Cut to slide: "Module 07 Key Takeaways."

"Key takeaways for Module 07:

One: CRM manages external customer relationships — the front office. ERP manages internal operations — the back office. Both are needed; neither replaces the other.

Two: Salesforce core objects — Lead, Account, Contact, Opportunity, Case — are the data model foundation. Know what each object represents and how they relate.

Three: Lead conversion creates Account, Contact, and Opportunity from a qualified Lead. This is a high-frequency exam concept.

Four: Sales Cloud manages the pipeline through Opportunity stages and probabilistic forecasting. Service Cloud manages Cases through queues, SLA milestones, and Knowledge Base.

Five: Salesforce automation tools — Flow Builder, Approval Processes, Validation Rules — are all configuration, not code.

Six: CRM-ERP integration connects the closed deal in Salesforce to fulfillment and revenue recognition in SAP ERP.

Exam tips for the Salesforce Associate exam: Know the five standard objects and what each one represents. Know that Lead conversion creates Account plus Contact plus Opportunity. Know that Cases are the core Service Cloud object. Know that Salesforce is a SaaS platform with three releases per year — Spring, Summer, and Winter — and that all customers receive updates on the same schedule."

---

### [End Card]

Text on screen:

- Complete Reading Guide 07
- Complete Lab 07 (CRM Scenario Analysis)
- Complete Quiz 07 (10 questions)
- Post to Discussion Forum 07 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com — search "Salesforce Associate Certification"
