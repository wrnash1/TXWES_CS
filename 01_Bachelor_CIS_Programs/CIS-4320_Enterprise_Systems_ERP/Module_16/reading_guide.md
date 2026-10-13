# Reading Guide: Module 16 — ERP Certification Exam Preparation and Capstone

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Overview

This final reading guide synthesizes key content from all fifteen previous modules and organizes it into a structured certification review format. It is organized by exam topic area for both Salesforce Administrator and SAP S/4HANA Essentials, then closes with capstone preparation guidance. Allocate 90–120 minutes. Active recall — reading a heading, then writing what you know before reading the content — is the most effective study technique at this stage.

---

## Part 1: Salesforce Administrator Exam Review

### Topic 1: Organization Setup and Configuration (20% of exam)

**User Management:** Administrators create and deactivate users. Users cannot be permanently deleted — they can only be deactivated. A deactivated user's records remain and can be reassigned. Username must be globally unique across all Salesforce orgs. The email field is separate from username; changing the email does not change the login username.

**Profiles and Licenses:** every user needs a user license (Salesforce, Salesforce Platform, Chatter Free, etc.) and a profile. The profile must be compatible with the user license. If you try to assign a profile that requires the Salesforce license to a user with a Chatter Free license, the assignment fails.

**Login Policies:** login hours (specified per profile) restrict when a user can access the org. IP range restrictions can be set at the profile level (trusted network ranges) or at the org level.

**Company Settings:** the company information page sets the default locale, language, time zone, and currency. Fiscal year settings determine whether to use the standard calendar year or a custom fiscal year.

---

### Topic 2: Object Manager and Lightning App Builder (20% of exam)

**Object Relationships:** three types of field-level relationships in Salesforce.

Master-Detail: creates a tight parent-child link. The child record cannot exist without the parent. Deleting the parent deletes all children (cascade delete). The child inherits the parent's sharing settings. Roll-up summary fields (sum, count, min, max) can aggregate child data to the parent.

Lookup: a flexible, optional reference from one record to another. Lookup relationships do not cascade delete and do not inherit sharing.

Many-to-Many: implemented using a junction object with two master-detail relationships — one to each parent object.

**Custom vs. Standard Fields:** custom fields have the `__c` suffix in their API name. Standard fields are provided by Salesforce and cannot be deleted (though they can often be hidden from page layouts).

**Record Types:** allow different page layouts and picklist values for different categories of records within the same object. For example, an Opportunity with record type "Enterprise" might have different required fields and a different page layout than one with record type "SMB."

**Page Layouts vs. FLS:** page layouts control which fields appear on the record page and their order. Field-Level Security controls whether a user can see a field at all. FLS supersedes the page layout — a field on the layout that is hidden by FLS will not appear.

---

### Topic 3: Sales and Marketing Applications (12% of exam)

**Lead Conversion:** converts a Lead into (optionally) an Account, Contact, and Opportunity. Lead field mapping must be configured for custom fields to transfer to the converted objects. A converted lead cannot be unconverted.

**Opportunity Stages:** defined via a Sales Process (Setup > Sales Processes). Each Stage has an associated Probability. The Forecast Category is set by the Stage. Forecast categories (Pipeline, Best Case, Commit, Closed, Omitted) aggregate into pipeline forecasts.

**Campaigns:** used to track marketing program effectiveness. Campaign Member records link Leads or Contacts to a Campaign and capture the response status (Sent, Opened, Responded, Converted, etc.). Campaign influence on opportunities tracks which campaigns contributed to a won deal.

**Price Books:** catalogs of products and prices. Every Salesforce org has a Standard Price Book. Custom Price Books allow different pricing for different customer segments or regions. An Opportunity uses exactly one Price Book.

---

### Topic 4: Service and Support Applications (11% of exam)

**Case Management:** Cases represent customer issues. Cases are assigned to users or queues via Assignment Rules. Escalation Rules automatically change case ownership or send notifications when cases are not resolved within a defined time period.

**Entitlement Management:** Entitlements define service level agreements (response time, resolution time) for specific accounts or contacts. Milestones are the measurable time targets within an entitlement. Escalation actions trigger when a milestone is at risk of being violated.

**Knowledge Management:** Salesforce Knowledge stores articles that agents and customers can reference for answers. Articles go through a publishing workflow. Article types control the layout and data captured in each article category.

---

### Topic 5: Data Management (10% of exam)

**Import Wizard vs. Data Loader:**

| Feature | Import Wizard | Data Loader |
|---------|---------------|-------------|
| Max records | 50,000 | 5,000,000 |
| Supported objects | Accounts, Contacts, Leads, Campaign Members, custom | All standard and custom |
| Delete operation | No | Yes |
| Upsert | Yes | Yes |
| Requires Java | No | Yes |

**External ID Fields:** custom fields with the "External ID" attribute can be used as upsert keys in Data Loader. The system matches records by external ID — if a match is found, the record is updated; if not, a new record is created.

**Duplicate Management:** Matching Rules define the criteria for identifying potential duplicates (fuzzy name matching, email matching, etc.). Duplicate Rules define the action taken when a duplicate is detected: block the save, show an alert, or allow with logging.

---

### Topic 6: Process Automation (12% of exam)

**Validation Rules:** execute when a record is saved. If the rule formula evaluates to TRUE, the error message is displayed and the save is blocked. Validation rules fire for all save operations — UI, API, flows, and workflows.

**Flows:** Salesforce's declarative automation engine. Flow types:

- Screen Flow: presents a UI to the user (multi-step forms, wizards)
- Record-Triggered Flow: fires when a record is created, updated, or deleted (before or after save)
- Scheduled Path Flow: fires on a defined schedule for records matching criteria
- Auto-launched Flow: called programmatically from other automations or APIs

**Approval Processes:** multi-step workflows that require one or more approvers to sign off before a record proceeds. Each approval step can be assigned to a specific user, a queue, or the record owner's manager.

---

### Topic 7: Reports and Dashboards (13% of exam)

**Report Formats:** tabular (flat list), summary (groupings and subtotals), matrix (two-dimension cross-tab), joined (multiple report type blocks).

**Dashboard Components:** chart, table, metric, gauge, Visualforce page. Max 20 components per dashboard.

**Running User:** determines data visibility for all viewers. Static running user = everyone sees the same data. Dynamic dashboard = each viewer sees their own data.

**Report Scheduling:** reports can be scheduled to run and be emailed automatically.

**Folder Permissions:** Edit and View access to report and dashboard folders is controlled separately from record access.

---

### Topic 8: Security and Access (14% of exam)

See Module 13 Reading Guide for detailed coverage. Key high-priority points for exam:

- FLS overrides page layout
- OWD is the most restrictive baseline; sharing only opens access
- Role hierarchy grants upward visibility; has nothing to do with profile or object permissions
- Setup Audit Trail: 180 days, setup configuration changes only
- Field History Tracking: 18 months default; 10 years with Salesforce Shield
- Manual sharing: the record owner can share a specific record with a specific user

---

## Part 2: SAP S/4HANA Essentials Exam Review

### SAP Organizational Structure Summary

| Element | Purpose | Key Parent |
|---------|---------|------------|
| Client | Top-level tenant | (none) |
| Company Code | Legal entity for financial accounting | Client |
| Plant | Physical location for production/storage | Company Code |
| Storage Location | Sub-area of a plant for inventory | Plant |
| Sales Organization | Sales responsibility unit | Company Code |
| Distribution Channel | How goods reach customers | Sales Organization |
| Division | Product line grouping | Client |
| Purchasing Organization | Procurement negotiation unit | Client or Company Code |
| Controlling Area | Internal cost management unit | Client |

---

### Financial Accounting (FI) Summary

**G/L Accounts:** the chart of accounts defines all G/L accounts. Balance sheet accounts and P&L accounts. Every posting creates a balanced accounting document (debits = credits).

**Document Types:** classify postings by origin (SA = G/L, KR = Vendor Invoice, DZ = Customer Payment). Each document type has a number range.

**Posting Keys:** define whether a line item is a debit or credit and which account type can be posted. Know: 40 = Debit G/L, 50 = Credit G/L, 31 = Vendor Credit, 21 = Vendor Debit.

**Fiscal Year Variant:** defines the fiscal year structure (calendar year vs. non-calendar). A company code is assigned to a fiscal year variant.

**Special G/L Transactions:** for down payments, bills of exchange, and other items that need to be tracked separately from normal open items but still affect the sub-ledger.

---

### Materials Management (MM) Summary

**Procurement cycle:** PR → PO → GR (movement type 101) → Invoice Verification (MIRO) → Payment (F-53).

**Material Master views:** Basic Data, Purchasing, Accounting, MRP, Storage, and others. Different organizational levels access different views.

**Inventory Valuation:** standard price vs. moving average price. Standard price: cost is fixed; variances posted to variance accounts. Moving average price: cost updates with each GR based on the current value.

**Special Procurement Types:** subcontracting (vendor assembles components), consignment (inventory on-site not yet owned), and third-party processing (vendor ships directly to customer).

---

### Sales and Distribution (SD) Summary

**Condition technique:** the pricing framework. Condition types (PR00 = base price, K007 = customer discount, MWST = tax) are organized in Condition Tables and accessed via Access Sequences. Pricing Procedures define the calculation sequence.

**Availability Check:** during sales order creation, SAP checks whether the requested quantity can be delivered by the requested date. Configured via Checking Group on the material master and Checking Rule in SD.

**Output Determination:** how SAP decides what documents to print, email, or transmit. Output Types (e.g., order confirmation, delivery note, invoice) use the same condition technique as pricing.

---

### Authorization Concept Summary

Hierarchy from bottom to top:

**Authorization Field:** a parameter that can be controlled (e.g., activity 01=Create, 02=Change, 03=Display; company code value).

**Authorization Object:** a named set of authorization fields that together control a specific capability (e.g., F_BKPF_BUK = financial document posting by company code).

**Authorization:** a specific combination of field values for an authorization object (e.g., F_BKPF_BUK with ACTVT=01,02,03 and BUKRS=1000,2000).

**Authorization Profile:** a collection of authorizations. Generated automatically by PFCG Profile Generator.

**Role (Single):** contains a menu of transaction codes plus one authorization profile.

**Role (Composite):** contains multiple single roles.

**User Master:** holds the user's assigned roles; the profiles are resolved from the roles.

---

### SAP BI Summary

**Reporting Options:** live S/4HANA Fiori tiles (operational, real-time), SAP BW/4HANA (data warehouse, complex analytics), SAP Analytics Cloud (cloud BI, planning, prediction), Crystal Reports (formatted document output).

**BW/4HANA Flow:** S/4HANA → Extractor → aDSO → CompositeProvider → SAC/BEX query → End user.

**SAP Analytics Cloud:** three capabilities — Business Intelligence, Augmented Analytics (Smart Predict, Smart Insights), Planning.

---

### Integration Summary

**IDoc:** Control Record (envelope) + Data Records (content) + Status Records (processing history). Message types: ORDERS (PO), INVOIC (Invoice), MATMAS (Material Master).

**RFC Types:** sRFC (sync, waits), aRFC (async, no response), tRFC (exactly-once, TID-based), bgRFC (modern successor to tRFC).

**SAP Integration Suite components:** Cloud Integration (iFlow designer), API Management, Event Mesh, Open Connectors.

**OData:** RESTful API standard; SAP S/4HANA exposes 1,000+ OData services via API Business Hub.

---

### ASAP Phases Quick Reference

| Phase | Name | Primary Deliverable |
|-------|------|---------------------|
| 1 | Project Preparation | Project Charter, system landscape |
| 2 | Business Blueprint | Business Blueprint document (to-be processes) |
| 3 | Realization | Configured SAP system, tested interfaces |
| 4 | Final Preparation | Trained users, migrated data, Go/No-Go |
| 5 | Go-Live and Support | Live production system, hypercare |

---

## Part 3: Cross-Platform Synthesis

### Common Exam Traps

**Trap 1:** Confusing the SAP Role with the Salesforce Role. In SAP, a role is a bundle of transaction codes and authorizations. In Salesforce, a role is purely a record-sharing mechanism in the role hierarchy — it has nothing to do with object or field permissions.

**Trap 2:** Confusing Salesforce Field-Level Security with page layout visibility. FLS wins. Always.

**Trap 3:** Confusing IDoc and BAPI. IDocs are asynchronous document messages. BAPIs are synchronous function module interfaces to business objects. They are different mechanisms used for different purposes.

**Trap 4:** Thinking the Salesforce Administrator exam tests coding. The Admin exam is declarative — click-based administration. If an answer choice involves Apex code, it is almost certainly wrong.

**Trap 5:** Confusing "Change Data Capture" and "Platform Events." CDC is automatic — Salesforce generates events when records change. Platform Events must be explicitly published.

---

## Part 4: Capstone Preparation

### What the Capstone Tests

The capstone assignment synthesizes all course content into a realistic business scenario. You will be asked to make and justify technical and business decisions across all topic areas:

- Which Salesforce objects and security model to implement
- Which SAP modules are relevant to the scenario
- How Salesforce and SAP should be integrated
- What reporting architecture serves the business's needs
- How the implementation should be structured (methodology, timeline, change management)
- What the five-year TCO looks like

Strong capstone submissions demonstrate: correct application of technical concepts, awareness of trade-offs, specific recommendations rather than vague options, and acknowledgment of risks.

### Capstone Success Tips

**Be specific.** "Use Salesforce reports" is not an answer. "Use a matrix report with rep on rows and quarter on columns, sourced from the Opportunities with Products report type" is an answer.

**Show trade-off awareness.** Every recommendation has a downside. Acknowledging it — "This approach provides the fastest time-to-value but creates technical debt that will need to be addressed in Phase 2" — demonstrates professional judgment.

**Use the terminology.** If the question is about SAP security, use "authorization object," "PFCG," and "composite role" — not generic terms like "user settings."

**Structure your response.** Use headings for each topic area. Graders reviewing long submissions appreciate clear organization.

---

## Key Terms — Master Glossary (Module 16 Review)

This glossary consolidates the most exam-critical terms from all modules.

**ASAP:** Accelerated SAP — five-phase SAP implementation methodology.

**Authorization Object (SAP):** a named set of controllable business capabilities with associated fields.

**Blueprint:** the Phase 2 ASAP deliverable documenting to-be processes.

**Bucket Field (Salesforce):** an in-report virtual field that groups values into named categories.

**BAPI:** stable, published SAP interface to a business object; runs as an RFC.

**CDC (Change Data Capture):** Salesforce feature that automatically publishes events when records change.

**Company Code:** the primary legal entity in SAP Financial Accounting.

**Composite Role (SAP):** a container grouping multiple single roles.

**CRM Analytics:** Salesforce's advanced analytics platform with its own data store.

**Dead Letter Queue:** a holding queue for integration messages that fail all retry attempts.

**ETL:** Extract, Transform, Load — the three phases of data movement.

**FLS (Field-Level Security):** Salesforce control that determines whether a field is visible and editable.

**IDoc:** SAP's Intermediate Document format for asynchronous data exchange.

**KPI:** a measurable metric tied to a business objective with a target and time horizon.

**Matching Rule (Salesforce):** defines criteria for identifying duplicate records.

**Named Credential:** a Salesforce configuration for securely storing API endpoint URLs and credentials.

**OData:** OASIS standard for RESTful APIs; extensively used in SAP S/4HANA.

**OWD (Organization-Wide Default):** the baseline record-sharing level in Salesforce.

**PFCG:** SAP transaction for creating and maintaining roles.

**Platform Events:** Salesforce's publish-subscribe event framework for real-time integration.

**RFC (Remote Function Call):** SAP's network protocol for calling function modules remotely.

**Running User:** the user whose access determines Salesforce dashboard data visibility.

**SAP Activate:** SAP's current Agile implementation methodology for S/4HANA.

**SAP Analytics Cloud:** SAP's cloud-native BI, planning, and predictive analytics platform.

**SAP BW/4HANA:** SAP's enterprise data warehouse on the HANA in-memory database.

**SAP GRC:** Governance, Risk, and Compliance — SAP's platform for SoD management.

**Setup Audit Trail:** Salesforce log of all configuration changes; retains 180 days.

**SoD (Segregation of Duties):** no single individual controls a complete business process end-to-end.

**SU53:** SAP transaction displaying the last failed authorization check for a user.

**SPRO/IMG:** SAP's customizing framework used during the Realization phase.

**tRFC:** Transactional RFC — guarantees exactly-once execution using a Transaction ID.

**TCO (Total Cost of Ownership):** complete lifecycle cost including license, implementation, integration, and support.

---

## Study Questions

1. A Salesforce user with the Standard User profile is trying to edit the "Contract Value" field on an Opportunity. The field is on the page layout but not visible. Where do you look first to diagnose the issue?

2. What is the difference between a Master-Detail relationship and a Lookup relationship in Salesforce? Give one consequence of each that is significant for a Salesforce Administrator.

3. Explain what happens during Lead Conversion in Salesforce. What objects are created, and what setting must the administrator configure for custom Lead fields to transfer?

4. What is the difference between an Authorization Object and a Role in SAP? What connects them?

5. In SAP's P2P cycle, what is the significance of the Goods Receipt posting (movement type 101)? What downstream impact does it have in Financial Accounting?

6. A company needs to synchronize 100,000 Account records from SAP to Salesforce nightly. They also need a real-time inventory check from SAP when a sales rep is building a quote. Name the appropriate Salesforce API for each use case and explain why.

7. What is the difference between a Dynamic Dashboard and a Static Dashboard in Salesforce? When would each be appropriate?

8. Describe the ADKAR model and apply it to a scenario where employees know how to use a new system but are still using their old spreadsheets 30 days after go-live.

9. What is the Go/No-Go decision and what criteria should be evaluated before proceeding with a production go-live?

10. A company's five-year Salesforce TCO is $3.8 million. Their current CRM spreadsheet system costs $25,000 per year in software and $40,000 per year in staff overhead. Build an argument for whether the Salesforce investment is justified.

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
