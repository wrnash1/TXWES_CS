# Lab: Module 12 — ERP Integration and Middleware

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

**Title:** Integration Architecture Design and Salesforce API Exploration

**Estimated Time:** 90–120 minutes

**Format:** Individual work with written deliverables

**Tools Required:** Salesforce Developer Edition org (free at developer.salesforce.com), web browser, text editor or Word processor

**Submission:** Upload completed lab report (PDF or DOCX) to the LMS by the module due date.

---

## Learning Objectives

By completing this lab you will be able to:

- Identify the appropriate integration technology for a given business scenario
- Navigate the Salesforce Setup area to locate API configuration settings
- Construct a basic integration architecture diagram for a Salesforce-to-SAP scenario
- Evaluate the trade-offs between integration approaches using a structured decision framework

---

## Lab Background

Westridge Manufacturing is a mid-sized industrial equipment company. Their technology landscape includes:

- Salesforce Sales Cloud for CRM (opportunities, accounts, contacts)
- SAP S/4HANA for finance, procurement, and inventory management
- A legacy order management system (OMS) running on-premises that does not have modern APIs
- A cloud data warehouse (Snowflake) for analytics

The CIS team has asked you — as a junior integration architect — to assess four integration scenarios and recommend an approach for each, then implement and document configuration settings in Salesforce for secure API access.

---

## Part 1: Integration Scenario Analysis (40 points)

For each of the four scenarios below, complete the analysis table. You must identify the integration pattern, the recommended technology, the data direction, and provide a one-paragraph justification.

### Scenario A: Sales Order Flow

When a sales opportunity is marked "Closed Won" in Salesforce, a corresponding sales order must be created in SAP S/4HANA within 15 minutes. The sales order needs the account number, opportunity line items, requested delivery date, and shipping address.

**Analysis Table — Scenario A**

Fill in each row:

| Field | Your Answer |
|-------|-------------|
| Integration pattern (point-to-point, hub-spoke, event-driven, API-led) | |
| Data direction | Salesforce → SAP |
| Recommended Salesforce technology | |
| Recommended SAP technology | |
| Synchronous or asynchronous? | |
| Middleware required? (Yes/No and why) | |

**Justification paragraph (5–7 sentences):** Explain why you chose these technologies, how the 15-minute SLA influences your decision, and what would happen if SAP were temporarily unavailable.

---

### Scenario B: Inventory Availability Check

Before a sales rep submits a quote in Salesforce, the system must display current inventory levels from SAP for each product on the quote. The rep needs to see inventory in real time before confirming availability to the customer.

**Analysis Table — Scenario B**

| Field | Your Answer |
|-------|-------------|
| Integration pattern | |
| Data direction | SAP → Salesforce (real-time lookup) |
| Recommended Salesforce technology | |
| Recommended SAP technology | |
| Synchronous or asynchronous? | |
| Middleware required? (Yes/No and why) | |

**Justification paragraph (5–7 sentences):** Explain the implications of the real-time requirement, and discuss the risk of a synchronous call to SAP failing mid-quote.

---

### Scenario C: Nightly Account Master Sync

Every night, the SAP customer master (up to 50,000 records) must be synchronized to Salesforce Accounts. Records that exist in SAP but not in Salesforce should be created. Records that differ should be updated. Records that no longer exist in SAP should be marked inactive in Salesforce.

**Analysis Table — Scenario C**

| Field | Your Answer |
|-------|-------------|
| Integration pattern | |
| Data direction | SAP → Salesforce |
| Recommended Salesforce technology | |
| Recommended SAP technology | |
| Synchronous or asynchronous? | |
| Middleware required? (Yes/No and why) | |

**Justification paragraph (5–7 sentences):** Justify the technology choice given the volume, explain what "upsert" means and why it is the right operation here, and describe what a dead letter queue would be used for in this scenario.

---

### Scenario D: Legacy OMS Integration

The legacy OMS does not have an API. It can produce a delimited flat file every two hours containing new and updated orders. Salesforce needs to reflect the order status (Submitted, In Fulfillment, Shipped, Delivered) on each Opportunity.

**Analysis Table — Scenario D**

| Field | Your Answer |
|-------|-------------|
| Integration pattern | |
| Data direction | OMS → Salesforce |
| Recommended approach (file-based ETL, API, etc.) | |
| Recommended Salesforce technology | |
| Frequency | Every 2 hours |
| Key transformation needed | |

**Justification paragraph (5–7 sentences):** Explain why a file-based ETL approach is appropriate, what transformation steps are needed to map OMS status codes to Salesforce opportunity stages, and how you would handle records in the file that do not match any Salesforce Opportunity.

---

## Part 2: Salesforce Setup Exploration (30 points)

Log in to your Salesforce Developer Edition org. Navigate to Setup (gear icon in the upper right, then Setup).

### Task 2.1: Locate the API Settings

In Setup, use the Quick Find box to search for "API." Locate the "API" node under the Integrations section.

Document the following (screenshot or written description):

1. What is the current API version shown in your org?

2. Is the SOAP API endpoint listed? Write it out.

3. Is the REST API enabled in your org? How can you confirm?

---

### Task 2.2: Create a Connected App

In Setup, navigate to App Manager. Click "New Connected App."

Fill in the following settings:

- Connected App Name: `CIS4320_Integration_Lab`
- API Name: (auto-populated)
- Contact Email: your TXWES email address
- Enable OAuth Settings: checked
- Callback URL: `https://login.salesforce.com/services/oauth2/callback`
- Selected OAuth Scopes: Add "Manage user data via APIs (api)" and "Perform requests at any time (refresh_token, offline_access)"

Save the Connected App. After saving, record:

1. The Consumer Key (also called Client ID) — first 20 characters only (do not submit the full key in a shared document).

2. What is the "Require Secret for Web Server Flow" toggle used for?

3. Under the Connected App, find the "Manage" button and describe what IP relaxation settings are available.

---

### Task 2.3: Explore Named Credentials

In Setup, search for "Named Credentials." Review the Named Credentials page.

Answer these questions:

1. What problem does a Named Credential solve compared to storing API endpoint URLs and credentials directly in Apex code?

2. What authentication protocols does Named Credential support? List at least three.

3. Create a mock Named Credential (you do not need a real endpoint):
   - Label: `SAP_S4HANA_Dev`
   - Name: (auto-populated)
   - URL: `https://sap-dev.example.com`
   - Authentication Protocol: Password Authentication
   - Username: `integration_user`
   - Password: (any mock value)

Screenshot the saved Named Credential record (or describe the fields visible after saving).

---

### Task 2.4: Review API Usage

Navigate to Setup > System Overview. Scroll to the API Usage section.

1. What is your org's daily API limit?

2. How many API calls have been made today?

3. If an integration was consuming 80% of the daily API limit by 2 PM, what strategies would you recommend to reduce API consumption? (List at least three.)

---

## Part 3: Integration Architecture Diagram (30 points)

Draw (by hand, on paper, or using a free tool such as draw.io, Lucidchart free tier, or PowerPoint) an integration architecture diagram for the following scenario.

**Scenario:** Westridge Manufacturing wants to implement the sales order flow from Scenario A (Part 1) using MuleSoft as middleware.

**Required diagram elements:**

- Salesforce Sales Cloud box (source)
- MuleSoft Anypoint Platform box (middleware)
- SAP S/4HANA box (target)
- Snowflake Data Warehouse box (analytics consumer)
- Arrow showing Platform Event published from Salesforce to MuleSoft
- Arrow showing API call from MuleSoft to SAP
- Arrow showing confirmation written back from MuleSoft to Salesforce
- Arrow showing order data replicated to Snowflake
- Labels on each arrow indicating the technology (REST API, OData, Bulk API, etc.)
- A "Dead Letter Queue" element showing where failed messages go
- A legend explaining each symbol used

**Diagram quality checklist (self-assess before submitting):**

- All systems are labeled
- All arrows have direction and technology label
- DLQ is shown and labeled
- Legend is present
- Diagram fits on one page

---

## Submission Checklist

Before submitting, verify:

- Part 1: All four scenarios have completed analysis tables and justification paragraphs
- Part 2: All four tasks are documented with screenshots or written descriptions
- Part 3: Integration architecture diagram is included as an image or embedded graphic
- Document is saved as PDF or DOCX
- Your name, student ID, and the date are on the cover page

---

## Grading Rubric

| Section | Points | Criteria |
|---------|--------|----------|
| Part 1 — Scenario A analysis and justification | 10 | Technology choice is correct and justified; SLA consideration addressed |
| Part 1 — Scenario B analysis and justification | 10 | Real-time requirement recognized; synchronous implications discussed |
| Part 1 — Scenario C analysis and justification | 10 | Bulk API identified; upsert explained; DLQ discussed |
| Part 1 — Scenario D analysis and justification | 10 | File-based ETL justified; transformation steps identified |
| Part 2 — Setup exploration tasks | 30 | Each task fully documented with accurate information |
| Part 3 — Architecture diagram | 30 | All required elements present; technically accurate; clearly labeled |
| **Total** | **100** | |

---

## Extension Activity (Optional, ungraded)

If you want to go further: use the Salesforce Workbench tool (workbench.developerforce.com) to execute a live REST API query against your Developer Edition org. Log in with OAuth, navigate to REST Explorer, and execute a `GET /services/data/v62.0/sobjects/` call. Document what the response contains and what it tells you about your org's data model.

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
