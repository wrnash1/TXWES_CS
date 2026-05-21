# Reading Guide: Module 05 - Financial Management Modules

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 05 - Financial Management Modules**! The financial accounting and controlling modules are the heart of every ERP system — virtually every business transaction ultimately posts to the General Ledger. This module covers the core FI (Financial Accounting) and CO (Controlling) modules in SAP, explaining how debits and credits flow through accounts payable, accounts receivable, asset management, and cost accounting.

These concepts are central to the SAP Certified Associate (Finance) exam and also provide context for understanding how Salesforce Revenue Cloud and CPQ (Configure-Price-Quote) connect CRM sales activities to financial outcomes.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **General Ledger (GL)**: The master financial record of all monetary transactions in the organization, organized by account code. Every business event — a purchase order, a customer payment, a payroll run — ultimately creates a journal entry in the General Ledger. The GL is the source of the balance sheet and income statement.
* **Accounts Payable (AP)**: The sub-ledger and process that manages money the company owes to vendors and suppliers. AP processes vendor invoices, validates them against purchase orders and goods receipts (the three-way match), and schedules payments.
* **Accounts Receivable (AR)**: The sub-ledger and process that manages money owed to the company by customers. AR generates customer invoices from sales orders, tracks payment due dates, processes incoming payments, and manages collections for overdue accounts.
* **Asset accounting**: The module that tracks the financial value of fixed assets (buildings, machinery, vehicles, IT equipment) over their useful life, applying depreciation schedules to reduce book value and produce accurate balance sheet valuations.
* **Cost accounting (CO)**: The controlling function that tracks costs and revenues by internal cost centers, profit centers, and projects. CO data enables management reporting — showing which products, regions, or departments are profitable — that the external GL alone cannot provide.
* **Financial reporting**: The process of producing period-end financial statements (balance sheet, income statement, cash flow statement) from ERP data. ERP systems automate period-end closing and consolidation, replacing manual spreadsheet-based processes.

---

### 2. Certification Exam Tips

* **SAP FI/CO focus:** Know the three-way match concept: SAP automatically compares the Purchase Order (MM), the Goods Receipt (MM-WM), and the Vendor Invoice (FI-AP) before allowing payment. If values do not match within tolerance, the invoice is blocked. This is one of SAP's most frequently tested concepts.
* **Chart of Accounts:** In SAP, every company code is assigned a Chart of Accounts — the complete list of GL account numbers and their definitions. Know that the Chart of Accounts is defined at the client level and shared across company codes, while account master records have both client-level and company-code-level segments.
* **Salesforce relevance:** Salesforce Revenue Cloud connects CRM opportunity and order management directly to ERP financial systems. Salesforce itself does not run a General Ledger, but exam questions may ask how Salesforce data flows to financial systems through integration.
* **Period-end close:** SAP's month-end close sequence runs in a specific order: post all open items → run depreciation → allocate costs (CO) → reconcile FI-CO → run financial statements. Exam questions may test the correct sequence.
* **Study Resource:** Explore the SAP Learning Hub overview of FI module concepts at [openSAP Financial Accounting](https://open.sap.com) — free course units covering General Ledger, AP, AR, and asset accounting in S/4HANA.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Review the [openSAP platform](https://open.sap.com) for free Financial Accounting in SAP S/4HANA course materials covering the GL, AP, AR, and asset accounting modules.
* **Required Video:** Watch the video lecture on **Financial Management Modules** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Examine General Ledger double-entry transaction links**: Given a sample purchase order scenario, trace the complete journal entry chain — from purchase order creation through goods receipt to invoice payment — and identify which GL accounts are debited and credited at each step.
* **Map account matching rules**: Document the three-way match process for a vendor invoice, showing what data SAP compares between the PO, GR, and invoice, and what tolerance percentage triggers a payment block.
* **Draft financial report templates**: Design a simple balance sheet layout identifying which GL account types (assets, liabilities, equity) appear in each section, and explain how ERP automation replaces manual spreadsheet consolidation at period end.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to explain where each sub-ledger (AP, AR, AA) posts to in the General Ledger.
* [ ] Review [openSAP](https://open.sap.com) for free SAP Financial Accounting course content.
* [ ] Watch the video lecture on **Financial Management Modules** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab three-way match trace and balance sheet layout exercise.
* [ ] Proceed to the weekly quiz.
