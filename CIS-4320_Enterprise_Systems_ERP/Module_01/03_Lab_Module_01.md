# Lab Activity: Module 01 - Enterprise Systems Concepts

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab develops your ability to analyze real enterprise scenarios, identify functional silo problems, and map business processes to appropriate ERP modules. You will produce three deliverables: a silo analysis diagram, an ERP module mapping table, and a written integration justification. All work is conceptual and document-based — no software installation or terminal commands are required.

**Estimated Time:** 90 minutes

**Submission:** Upload your completed lab document to the Canvas assignment portal by the module due date.

---

## Learning Objectives

By completing this lab you will be able to:

- Identify functional silos in a described business scenario and articulate the specific problems they cause
- Map business functions to the correct SAP module or Salesforce object
- Explain the data flow through an integrated ERP system for a given business transaction
- Justify an ERP investment using the three core business drivers: data consistency, process efficiency, and regulatory compliance

---

## Scenario Background

**Company:** RidgeLine Industrial Supply
**Industry:** Industrial distribution (tools, fasteners, safety equipment)
**Size:** 320 employees, $85 million annual revenue
**Locations:** Fort Worth headquarters, Dallas warehouse, Houston distribution center

RidgeLine currently operates with the following disconnected systems:

- **Sales team:** Tracks customer quotes and orders in a shared Google Sheet. Updates are manual. No automated inventory check.
- **Warehouse (Fort Worth and Dallas):** Each location tracks inventory in its own spreadsheet. The two locations do not share data.
- **Finance:** Uses QuickBooks for accounts payable, accounts receivable, and general ledger. Customer data is re-entered manually from the Sales team's spreadsheet.
- **HR:** Keeps employee records in a filing cabinet and a local Excel workbook. Payroll is processed by a third-party payroll service using manually prepared reports.
- **Purchasing:** Vendor contracts are stored as PDF files in a shared drive folder. Purchase orders are created in Word documents and emailed to vendors.

---

## Part A: Silo Analysis (30 points)

### A-1: Identify the Silos

Review the RidgeLine scenario above. In the table below, identify each functional silo, describe the data it contains, and explain one specific business problem caused by its isolation from other departments.

Complete this table in your lab document:

| Department | System Used | Data Stored | Specific Problem Caused by Isolation |
|---|---|---|---|
| Sales | | | |
| Warehouse — Fort Worth | | | |
| Warehouse — Dallas | | | |
| Finance | | | |
| HR | | | |
| Purchasing | | | |

**Guidance:** For the "Specific Problem" column, describe a realistic scenario — for example, "A customer calls to check if an order has shipped; the sales rep cannot see warehouse inventory and must call the warehouse manually, causing a 2-hour delay."

### A-2: Silo Diagram

Draw (by hand or using a simple diagram tool) a visual representation of RidgeLine's current architecture showing:

- Each department as a separate box
- The data each box contains
- The manual handoff points between departments (label each handoff with the method used: phone call, email, manual re-entry, etc.)
- At least three places where data discrepancies could arise

Attach your diagram as an image or describe it in detail in your lab document.

### A-3: Business Impact Analysis

In 150-200 words, describe the cumulative business impact of RidgeLine's silo architecture. Address:

- How many manual re-entry points exist in a typical order-to-cash cycle (customer order to final payment receipt)?
- What types of errors are most likely to occur?
- How would these problems affect customer satisfaction and financial reporting accuracy?

---

## Part B: ERP Module Mapping (30 points)

### B-1: Module Matching Table

RidgeLine has decided to implement SAP S/4HANA. Match each current RidgeLine business function to the correct SAP module. Use the module codes covered in the reading guide and video lecture.

Complete this table:

| RidgeLine Business Function | SAP Module Code | SAP Module Full Name | Key Benefit of Replacing Current Tool |
|---|---|---|---|
| General Ledger and financial statements | | | |
| Accounts payable — vendor invoice processing | | | |
| Accounts receivable — customer billing | | | |
| Inventory management across both warehouses | | | |
| Purchase order creation and vendor management | | | |
| Customer order entry and order fulfillment | | | |
| Employee records and payroll | | | |
| Internal cost reporting by product line | | | |

### B-2: Shared Database Benefits

Choose three of the module pairings you identified in B-1. For each pair, write 2-3 sentences explaining how having both modules share a single database eliminates a specific problem that exists in RidgeLine's current silo architecture.

Example format:

> When the [Module A] and [Module B] share a single database, [specific data element] entered in [Module A] is immediately visible in [Module B], eliminating [specific manual step or error] that currently occurs in RidgeLine's process.

---

## Part C: Integration Architecture (25 points)

### C-1: Transaction Data Flow

Walk through the following business scenario and describe the data flow through the integrated SAP system at each step. Identify which SAP module handles each step and what data record is created.

**Scenario:** A customer calls RidgeLine and places an order for 50 boxes of safety gloves. RidgeLine's warehouse picks and ships the order. The vendor invoice for the gloves arrives. Finance pays the vendor.

For each numbered step below, identify the SAP module involved and the SAP document created:

1. Sales representative enters the customer's order into the system
2. System checks whether 50 boxes are available in inventory
3. Warehouse picks and ships the 50 boxes; inventory is reduced
4. System generates the invoice to send to the customer
5. Customer's account is updated to show an outstanding receivable
6. Vendor invoice for the gloves arrives and is processed for payment
7. Payment is sent to the vendor and the outstanding payable is cleared

### C-2: Integration Justification

RidgeLine's CFO is skeptical of the SAP investment, asking: "We've managed fine with spreadsheets for 15 years. Why do we need to spend $2 million on a new system?"

Write a 200-250 word response from the perspective of a consultant making the business case. Your response must address:

- At least two specific examples of how the current architecture creates financial risk or reporting inaccuracy
- The three core business drivers for ERP (data consistency, process efficiency, regulatory compliance)
- One concrete operational improvement that would result from ERP implementation

---

## Part D: Reflection (15 points)

### D-1: Certification Connection

In 100-150 words, explain how the concepts in this lab connect to what is tested on either the Salesforce Certified Associate exam or the SAP Certified Associate exam. Identify at least one specific concept from today's lab that you expect to see on a certification exam question.

### D-2: Personal Application

In 100-150 words, describe a real or hypothetical scenario from an industry you are interested in working in after graduation. Describe how functional silos could create a business problem in that industry and how an enterprise system could solve it.

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Silo identification table | 10 | All 6 rows completed with accurate systems, data, and realistic problems |
| A-2: Silo diagram | 10 | Visual shows all departments, data, handoffs, and at least 3 discrepancy points |
| A-3: Business impact analysis | 10 | 150-200 words; addresses re-entry points, error types, and customer/financial impact |
| B-1: Module matching table | 20 | All 8 rows matched to correct SAP module code and full name; benefit described |
| B-2: Shared database benefits | 10 | 3 pairs chosen; each explanation is specific to RidgeLine scenario, 2-3 sentences |
| C-1: Transaction data flow | 15 | All 7 steps identified with correct module and document name |
| C-2: Integration justification | 10 | 200-250 words; 2 financial risks, 3 drivers, 1 operational improvement |
| D-1: Certification connection | 8 | 100-150 words; identifies specific certifiable concept |
| D-2: Personal application | 7 | 100-150 words; realistic industry scenario with silo problem and ERP solution |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile your responses into a single document (Word, PDF, or Google Doc).
2. Name your file: `Lab01_LastName_FirstName.pdf`
3. Upload to the Canvas assignment portal under "Lab 01 — Enterprise Systems Concepts."
4. Deadline: See the course schedule in Canvas.

Late submissions lose 10 points per day unless an extension is approved in advance by Professor Nash.

---

## Part 9 — Challenge Exercise

### Challenge 1: Greenfield ERP Vendor Selection Matrix

You have been hired as an ERP consultant for a 500-employee food-and-beverage manufacturer. The CEO wants to evaluate SAP S/4HANA, Oracle Cloud ERP, and Microsoft Dynamics 365. Build a structured vendor comparison:

1. Create a weighted scoring matrix with at least six evaluation criteria (e.g., total cost of ownership, industry-specific functionality, implementation timeline, integration ecosystem, vendor support model, upgrade cadence). Assign a weight (must total 100%) to each criterion based on what matters most to a food manufacturer.
2. Score each of the three vendors on each criterion from 1–5 and calculate a weighted total score. Document your scoring rationale for each cell.
3. Write a 100-word executive summary recommending one vendor and justifying the choice using the weighted results.
4. Identify one criterion where your scoring was most uncertain and explain what additional information you would need to finalize that score.

### Challenge 2: Integration Failure Post-Mortem

A retail company went live with SAP S/4HANA six months ago but kept Salesforce CRM on a separate, unintegrated system. Sales representatives are creating orders in Salesforce that are not flowing to SAP, causing fulfillment delays and duplicate invoices.

1. Draw a data flow diagram showing what should happen (Opportunity close → SAP Sales Order) versus what is currently happening (manual workaround steps the team invented).
2. Identify three specific data fields (e.g., customer ID, order total, requested delivery date) that are at risk of mismatching between the two systems given the current manual process.
3. Propose a middleware integration solution (name a specific tool such as MuleSoft or SAP Integration Suite) and describe the two most critical data mappings it must handle.
4. Estimate the business cost of the current failure in terms of time, accuracy, and customer experience — use specific numbers based on reasonable assumptions.

### Reflection Questions

1. In the vendor selection matrix, which criterion had the biggest impact on the final ranking? Would a different industry (e.g., financial services instead of food manufacturing) change that weighting significantly, and why?
2. The integration failure scenario is a real pattern seen in many ERP go-lives. What organizational or project management decision most likely caused the integration to be left out of the initial scope, and what should the project manager have done differently during the planning phase?
