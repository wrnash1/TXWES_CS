# Reading Guide: Module 07 - Customer Relationship Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

Customer Relationship Management (CRM) is the front-office counterpart to ERP's back-office capabilities. While ERP manages procurement, finance, and manufacturing, CRM manages the customer-facing operations that generate revenue: marketing campaigns, sales pipelines, customer accounts, and support cases. Salesforce is the dominant CRM platform globally, and the Salesforce Certified Associate exam is a targeted credential for this course. This module covers the Salesforce data model, Sales Cloud, Service Cloud, CRM automation tools, and CRM-ERP integration architecture.

---

## Section 1: High-Yield Glossary

**Customer Relationship Management (CRM)**
Software that manages a company's interactions with current and potential customers. CRM systems centralize customer data, track sales activities, manage support cases, and enable marketing campaigns. Salesforce is the market-leading SaaS CRM platform.

**Lead**
An unqualified prospective customer who has expressed interest in the company's products or services. In Salesforce, a Lead is a staging record that has not yet been confirmed as a real business opportunity. Leads are converted to Accounts, Contacts, and Opportunities when qualified.

**Account**
The Salesforce object representing a company or organization — a customer, prospect, or partner. Accounts are the anchor of the Salesforce data model; most other objects relate back to an Account.

**Contact**
An individual person at an Account. Contacts store personal and professional information for people the company interacts with — buyers, decision-makers, influencers, support users. A Contact must be linked to an Account.

**Opportunity**
A potential sale in progress. An Opportunity is linked to an Account and has a Stage (pipeline position), Amount (expected revenue), and Close Date. Opportunities drive Salesforce pipeline reports and revenue forecasts.

**Case**
A customer service issue, question, or complaint that needs resolution. Cases are the central object in Service Cloud. A Case tracks a customer problem from initial report through resolution and closure.

**Lead Conversion**
The Salesforce process of converting a qualified Lead into three linked records: an Account (the company), a Contact (the person), and an Opportunity (the potential deal). The original Lead is marked Converted and retained for historical reporting.

**Stage**
The pipeline position of an Opportunity, representing where the deal is in the sales process. Common stages: Prospecting, Qualification, Needs Analysis, Proposal, Negotiation, Closed Won, Closed Lost. Each stage has a Probability percentage used in revenue forecasting.

**Entitlement**
A Service Cloud record that defines the level of support a customer is entitled to under their service contract. Entitlements define SLA metrics such as first response time and resolution time.

**Milestone**
A Service Cloud SLA checkpoint within a Case. Milestones track whether required response and resolution times are being met. When a Milestone is at risk, escalation rules can notify managers or reassign the Case.

**Flow Builder**
Salesforce's point-and-click automation tool for building rules-based workflows. Flow Builder replaces Process Builder and Workflow Rules and can automate complex multi-step processes without writing code.

**Approval Process**
A Salesforce configuration that routes a record to one or more approvers before a business action is taken. Common use: routing large discount requests to a sales manager before a quote is sent to the customer.

**Validation Rule**
A Salesforce formula-based rule that prevents saving a record if a logical condition is not met. Example: "Close Date must be in the future for all new Opportunities." Validation Rules enforce data quality at the entry point.

**Sales Cloud**
The Salesforce product suite for sales teams — covering Leads, Accounts, Contacts, Opportunities, Quotes, Products, and forecasting. Sales Cloud is the core CRM application for pipeline management and revenue tracking.

**Service Cloud**
The Salesforce product suite for customer service teams — covering Cases, Queues, Entitlements, Knowledge Base, and escalation management. Service Cloud operationalizes post-sale customer support.

**Knowledge Base**
A repository of documented solutions and troubleshooting guides in Service Cloud. Agents use the Knowledge Base to find resolutions quickly; customers can search it through a self-service portal.

---

## Section 2: CRM vs. ERP Comparison

### Front Office vs. Back Office

```text
[Front Office -- CRM]                   [Back Office -- ERP]
  Marketing campaigns                     Financial accounting (FI)
  Sales pipeline management               Procurement and inventory (MM)
  Customer account records                Manufacturing and production (PP)
  Support case management                 Human capital management (HCM)
  Revenue forecasting                     Financial close and reporting

Primary Audience: Sales, Marketing,      Primary Audience: Finance, Operations,
                  Customer Service                         HR, IT

System of Record for: Customers,         System of Record for: Transactions,
                       Deals, Issues                          Assets, Employees

Example Platform: Salesforce             Example Platform: SAP S/4HANA
```

### CRM vs. ERP Module Comparison

| Function | Salesforce CRM | SAP S/4HANA ERP | Oracle Cloud |
|---|---|---|---|
| Customer master data | Account object | Customer master (SD) | Customer Master |
| Sales pipeline | Opportunity stages | SD -- Sales Orders (VA01) | Oracle Sales |
| Sales quotes | Quote object with Products | SD -- Quotations (VA21) | Oracle CPQ |
| Order management | Salesforce Order Management | SD -- Sales Orders (VA01) | Oracle Order Management |
| Customer support | Service Cloud Cases | CS -- Customer Service | Oracle Service |
| Marketing | Marketing Cloud | SAP Marketing Cloud | Oracle Marketing |
| Field service | Field Service (optional) | SAP Field Service Mgmt | Oracle Field Service |
| Revenue forecasting | Forecast object | CO-PA Profitability Analysis | Oracle Revenue Management |

---

## Section 3: Salesforce Data Model

### Core Object Relationships

```text
[Lead]
  (Unqualified prospect -- staging record)
          |
          | Lead Conversion (qualified)
          |
          v
[Account] ----1:M----> [Contact]
(Company)              (Person at company)
    |
    1:M
    |
    v
[Opportunity]          [Case]
(Potential sale)       (Support issue)
    |                      |
    Both link to Account   Both link to Account and Contact
```

### Standard Object Quick Reference

| Object | Represents | Key Fields | Related To |
|---|---|---|---|
| Lead | Unqualified prospect | Company, Email, Lead Source, Status | None (standalone until converted) |
| Account | Company or organization | Name, Industry, Annual Revenue, Type | Contacts, Opportunities, Cases |
| Contact | Individual person | First/Last Name, Title, Email, Account | Account |
| Opportunity | Potential deal in progress | Amount, Stage, Close Date, Account | Account, Contacts |
| Case | Customer service issue | Subject, Status, Priority, Origin | Account, Contact |
| Campaign | Marketing initiative | Type, Start/End Date, Budget, ROI | Leads, Contacts via Campaign Members |

### Lead Conversion Outcome

```text
Before Conversion:           After Conversion:
[Lead Record]          -->   [Account] + [Contact] + [Opportunity]
  Company: Acme Corp          Account: Acme Corp
  Name: Sarah Chen            Contact: Sarah Chen (linked to Acme)
  Email: s.chen@acme.com      Opportunity: Acme - Software Deal
  Status: Qualified            Stage: Qualification
                               Amount: $45,000
                              Lead Status: Converted (retained)
```

---

## Section 4: Sales Cloud -- Pipeline Management

### Opportunity Stage Sequence and Probability

| Stage | Typical Probability | Description |
|---|---|---|
| Prospecting | 10% | Initial identification of potential deal |
| Qualification | 20% | Confirming budget, authority, need, timeline |
| Needs Analysis | 40% | Understanding customer requirements in detail |
| Proposal / Price Quote | 60% | Formal proposal submitted to customer |
| Negotiation / Review | 80% | Terms being finalized |
| Closed Won | 100% | Deal signed and won |
| Closed Lost | 0% | Deal lost to competitor or no decision |

### Pipeline Forecast Formula

```text
Forecasted Revenue = Opportunity Amount x Stage Probability

Example:
  Opportunity: Acme Software Deal
  Amount: $120,000
  Stage: Proposal (60%)
  Forecasted Revenue: $120,000 x 0.60 = $72,000

Total Forecast = Sum of (Amount x Probability) for all open Opportunities
```

### Sales Cloud Automation Tools

| Tool | Purpose | Requires Code? |
|---|---|---|
| Validation Rule | Prevents saving records that violate data quality rules | No -- formula-based |
| Flow Builder | Automates multi-step processes (create records, send emails, update fields) | No -- point-and-click |
| Approval Process | Routes records to approvers before actions are taken | No -- wizard-based |
| Assignment Rule | Automatically assigns new Leads or Cases to owners or queues | No -- criteria-based |
| Escalation Rule | Escalates Cases to new owners if not resolved within a time limit | No -- criteria-based |

---

## Section 5: Service Cloud -- Case Management

### Case Lifecycle

```text
[Customer Contact]
 (phone / email / chat / web form)
          |
[Case Created]
 Status: New
          |
[Case Assigned]
 Routed to Queue or Agent
          |
[Investigation]
 Agent communicates with customer
 SLA Clock Running
          |
[Resolution]
 Solution posted; customer notified
          |
[Case Closed]
 CSAT survey triggered (optional)
```

### SLA Management -- Entitlements and Milestones

| Concept | Description | Salesforce Object |
|---|---|---|
| Entitlement | Defines support level per contract (response times, coverage hours) | Entitlement |
| Milestone | SLA checkpoint within a Case (First Response, Resolution) | Milestone |
| Escalation Rule | Automatic reassignment if Milestone deadline is approaching | Escalation Rule |
| Knowledge Article | Documented solution linked to a Case resolution | Knowledge |

---

## Section 6: CRM-ERP Integration Architecture

### Order-to-Cash Integration Flow

```text
[Salesforce CRM]                         [SAP ERP]
  Lead (prospect)
       |
  Account / Contact / Opportunity
       |
  Quote (products + pricing)
       |
  Closed Won Opportunity
       |
  Order Record created
       |                 API/Middleware
       +---------------->----------->[Sales Order (SD -- VA01)]
                                              |
                                      [Availability Check (MM)]
                                              |
                                      [Delivery + Goods Issue (MM)]
                                              |
                                      [Invoice (SD -- VF01)]
                                              |
                                      [Revenue Recognition (FI)]
                                              |
       <---------Payment Status---------[Customer Payment (FI-AR)]
```

### CRM-ERP Integration Points Table

| Integration | From | To | Trigger | Data Exchanged |
|---|---|---|---|---|
| Closed deal to order | Salesforce | SAP SD | Opportunity Closed Won | Customer, products, quantities, pricing |
| Customer account sync | Salesforce | SAP SD | Account created/updated | Customer name, address, payment terms |
| Product/pricing sync | SAP SD | Salesforce | Catalog update | Product descriptions, prices, availability |
| Invoice sync | SAP FI | Salesforce | Invoice posted | Invoice number, amount, due date |
| Payment status | SAP FI-AR | Salesforce | Payment cleared | Open balance, overdue status |

---

## Section 7: Salesforce Platform Facts

### Platform Architecture

| Characteristic | Salesforce Detail |
|---|---|
| Deployment model | SaaS only -- no on-premise option |
| Release schedule | Three releases per year: Spring, Summer, Winter |
| Multi-tenancy | All customers share one platform; data is logically isolated |
| Customization method | Clicks (configuration) before code (development) |
| Mobile | Native mobile app included (Salesforce Mobile) |
| AppExchange | Marketplace for pre-built apps and integrations |
| Admin certification | Salesforce Administrator ($200 exam, entry-level) |
| Associate certification | Salesforce Certified Associate (no prerequisite, entry-level) |

### Salesforce vs. SAP CRM

| Feature | Salesforce | SAP CRM / SAP Sales Cloud |
|---|---|---|
| Market position | Global CRM market leader | Strong in SAP-installed enterprises |
| Deployment | SaaS only | SaaS (Sales Cloud) or hybrid |
| ERP integration | Via API to any ERP | Native integration to SAP S/4HANA |
| Strength | CRM depth, ecosystem, ease of use | Single-vendor SAP stack, deep ERP data |
| Trailhead learning | Free, comprehensive | SAP Learning Hub (subscription) |

---

## Section 8: Certification Exam Tips

1. **Know the five standard Salesforce objects.** Lead, Account, Contact, Opportunity, Case -- what each represents, who uses it, and what it relates to. This is foundational for every Salesforce Associate exam scenario.

2. **Lead conversion creates three records.** Account + Contact + Opportunity. If a scenario says "a prospect is qualified," the next step is Lead conversion.

3. **Cases are the core Service Cloud object.** When a scenario involves a customer reporting a problem, the answer involves creating a Case, not a Lead or Opportunity.

4. **Salesforce automation tools are configuration, not code.** Flow Builder, Approval Processes, and Validation Rules require no Apex code. If the question asks what an admin can do without a developer, these are the answers.

5. **Salesforce is SaaS-only with three releases per year.** Spring, Summer, Winter. All customers receive the same update on the same schedule. This is a distinguishing characteristic vs. SAP on-premise.

6. **Stage probability drives forecasting.** Forecast Amount = Opportunity Amount x Stage Probability. Know the formula and be able to apply it.

7. **CRM and ERP serve different audiences.** CRM serves sales, marketing, and service. ERP serves finance, operations, and HR. Both are required; neither replaces the other.

8. **The integration point is the Order record.** When a Salesforce Opportunity is Closed Won, the resulting Order flows to the ERP system for fulfillment. This is where CRM and ERP hand off.

---

## Section 9: Required Trailhead and Study Resources

Complete before attempting the quiz:

- **Salesforce Trailhead -- Salesforce Associate Certification Prep**
  URL: trailhead.salesforce.com -- search "Salesforce Associate Certification Prep"
  Covers all Salesforce Associate exam domains including the data model and platform features.

- **Salesforce Trailhead -- CRM for Lightning Experience**
  URL: trailhead.salesforce.com -- search "CRM for Lightning Experience"
  Practical walkthrough of Leads, Accounts, Contacts, and Opportunities in the Lightning UI.

---

## Section 10: Study Checklist

- Memorize the five standard Salesforce objects and what each represents.
- Trace the Lead conversion process and name the three records created.
- Review the Opportunity stage sequence and the forecasting formula.
- Study the Service Cloud case lifecycle diagram in Section 5.
- Review the CRM-ERP integration flow in Section 6.
- Study the Salesforce platform facts table in Section 7.
- Complete the Salesforce Trailhead "CRM for Lightning Experience" module.
- Watch the Module 07 video lecture.
- Complete Lab 07.
- Post to Discussion Forum 07 by Wednesday at 11:59 PM.
- Complete Quiz 07 (10 questions).
