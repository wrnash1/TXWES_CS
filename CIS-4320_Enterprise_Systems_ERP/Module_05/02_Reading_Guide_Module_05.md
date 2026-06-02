# Reading Guide: Module 05 - Financial Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

The financial management module is the core of every ERP system. Regardless of what other modules a company implements, finance is always included — because every business activity ultimately has a financial dimension. This module covers the key financial sub-modules in SAP S/4HANA: General Ledger (FI-GL), Accounts Payable (FI-AP), Accounts Receivable (FI-AR), Asset Accounting (FI-AA), and Controlling (CO). Understanding these modules equips you to answer financial process questions on the SAP Certified Associate exam and provides context for how financial processes connect to Salesforce Order-to-Cash scenarios.

---

## Section 1: High-Yield Glossary

**General Ledger (FI-GL)**
The central accounting repository that records all financial transactions as journal entries organized by account. Every sub-ledger (AP, AR, AA) posts summarized totals to the GL automatically. The GL produces the company's external financial statements: Balance Sheet, Income Statement, and Cash Flow Statement.

**Chart of Accounts**
The complete list of financial accounts used by a company, organized by type: assets, liabilities, equity, revenue, and expenses. Every financial posting must reference an account in the chart of accounts. SAP allows multiple charts of accounts for companies that report under different accounting standards.

**Journal Entry**
The fundamental unit of financial recording. A journal entry always has at least one debit and one credit, and the two sides must balance. Example: when a vendor invoice is posted, the system debits an expense account and credits the Accounts Payable liability account.

**Accounts Payable (FI-AP)**
The sub-ledger that manages money owed to vendors. AP tracks open vendor invoices, enforces the three-way match payment control, executes the automatic payment run, and posts cleared payments to the General Ledger.

**Three-Way Match**
A payment control mechanism in Accounts Payable that compares three documents before approving a vendor invoice for payment: the Purchase Order (agreed price and quantity), the Goods Receipt (what was physically received), and the Vendor Invoice (what the vendor is charging). Discrepancies block the invoice for review, preventing unauthorized payments.

**Accounts Receivable (FI-AR)**
The sub-ledger that manages money owed by customers. AR tracks open customer invoices, applies received payments against open invoices (clearing), and executes the dunning process to collect overdue balances.

**Dunning**
The automated process of generating collection notices for overdue customer invoices. SAP supports multiple dunning levels with progressively escalating notice types (reminder, warning, final notice, credit hold).

**Asset Accounting (FI-AA)**
The sub-module that tracks the full lifecycle of fixed assets: acquisition cost, depreciation calculations, net book value, and disposal. Every fixed asset has a master record. The depreciation run (SAP transaction AFAB) calculates and posts periodic depreciation automatically.

**Depreciation**
The systematic reduction in a fixed asset's book value over its useful life, reflecting consumption of the asset's economic benefit. Common methods include straight-line (equal annual amounts) and declining balance (higher amounts early in life).

**Net Book Value (NBV)**
The current carrying value of a fixed asset on the Balance Sheet. NBV = Acquisition Cost − Accumulated Depreciation.

**Controlling (CO)**
SAP's internal management accounting module. CO provides financial reporting by internal dimension (cost center, profit center, product line) that is not visible in the external General Ledger. CO is used for budgeting, profitability analysis, and cost management.

**Cost Center**
An organizational unit that accumulates costs but is not directly measured on profit. Examples: IT department, HR department, facilities management. Cost center accounting tracks how much each department spends.

**Profit Center**
An organizational unit that tracks both revenues and costs, enabling internal profitability measurement. Examples: a product line, a geographic region, a business unit.

**Period-End Close**
The monthly process of finalizing all financial transactions for a period, running automated processes (depreciation, allocations), reconciling sub-ledgers to the General Ledger, and producing financial statements. The period is then locked to prevent backdated postings.

**Parallel Ledgers**
SAP S/4HANA's New General Ledger supports maintaining parallel accounting books for different reporting standards (e.g., US GAAP and IFRS) in the same system simultaneously, with different valuation rules applied to each.

---

## Section 2: SAP Financial Module Architecture

### Sub-Ledger to General Ledger Flow

```text
[Vendor Invoice Posted in FI-AP]
          |
   Automatic GL Posting:
   Dr: Expense Account / Goods Received
   Cr: Accounts Payable (Vendor)
          |
[Customer Billing in SD → FI-AR]
          |
   Automatic GL Posting:
   Dr: Accounts Receivable (Customer)
   Cr: Revenue Account
          |
[Depreciation Run in FI-AA]
          |
   Automatic GL Posting:
   Dr: Depreciation Expense
   Cr: Accumulated Depreciation
          |
[Payroll Run in HCM]
          |
   Automatic GL Posting:
   Dr: Salary Expense, Benefits Expense
   Cr: Cash / Bank / Accruals
          |
      [General Ledger (FI-GL)]
          |
   Produces: Balance Sheet, Income Statement, Cash Flow
```

All postings to the General Ledger from sub-ledgers are automatic and happen in real time when the originating transaction is posted.

### SAP Financial Module Codes Reference

| Module Code | Full Name | Primary Function |
|---|---|---|
| FI | Financial Accounting | External financial reporting |
| FI-GL | General Ledger | Central journal; financial statements |
| FI-AP | Accounts Payable | Vendor invoice management, payments |
| FI-AR | Accounts Receivable | Customer billing, collections |
| FI-AA | Asset Accounting | Fixed asset lifecycle, depreciation |
| FI-TR | Treasury | Cash management, bank reconciliation |
| CO | Controlling | Internal management accounting |
| CO-CCA | Cost Center Accounting | Departmental cost tracking |
| CO-PCA | Profit Center Accounting | Business unit profitability |
| CO-OPA | Internal Orders | Project/campaign cost tracking |
| CO-PC | Product Costing | Standard cost calculation |

---

## Section 3: The Three-Way Match — Detailed Flow

The three-way match is one of the most tested concepts on the SAP Associate exam. Understand it thoroughly.

### Three-Way Match Process Flow

```text
Step 1: Purchase Order (ME21N)
        Company orders 200 units @ $25 each = $5,000
                    |
Step 2: Goods Receipt (MIGO)
        Warehouse receives 200 units
        GL Posting: Dr Inventory $5,000 / Cr GR/IR Clearing $5,000
                    |
Step 3: Invoice Receipt (MIRO)
        Vendor invoices for 200 units @ $25 each = $5,000
        System checks: Invoice vs. PO vs. GR
                    |
        [XOR: Does invoice match PO and GR within tolerance?]
               |                        |
             YES                        NO
               |                        |
    Invoice approved               Invoice blocked
    GL: Dr GR/IR $5,000         Work item created for AP team
        Cr Vendor AP $5,000     AP team investigates and resolves
                    |
Step 4: Payment Run (F110)
        System generates payment to vendor
        GL: Dr Vendor AP $5,000 / Cr Bank $5,000
```

### Three-Way Match Failure Scenarios

| Discrepancy Type | Example | System Response |
|---|---|---|
| Price discrepancy | Invoice @ $27, PO @ $25 | Invoice blocked, price variance work item |
| Quantity discrepancy | Invoice 220 units, GR 200 units | Invoice blocked, quantity variance work item |
| Goods not received | Invoice before GR | Invoice blocked, goods receipt expected |
| Duplicate invoice | Same invoice number already posted | Invoice blocked, duplicate detected |

---

## Section 4: Asset Accounting — Depreciation Methods

| Method | Calculation | Best Used For |
|---|---|---|
| Straight-Line | Cost ÷ Useful Life = same amount per year | Buildings, furniture, long-life equipment |
| Declining Balance | NBV × fixed percentage = decreasing amount per year | Technology equipment, vehicles |
| Units of Production | Cost ÷ Total Units × Units Produced this period | Manufacturing equipment with measurable output |
| Sum-of-Years Digits | Accelerated method; front-loaded depreciation | Tax depreciation in some jurisdictions |

### Asset Lifecycle in SAP

```text
[Asset Acquisition] → Asset master record created
        |              Acquisition posting to FI-AA and GL
        |
[Monthly Depreciation Run (AFAB)]
        |              Calculates depreciation per method
        |              Posts: Dr Depreciation Expense
        |                     Cr Accumulated Depreciation
        |
[Asset Disposal / Retirement]
               Removes NBV from balance sheet
               Calculates gain or loss on disposal
               Final posting to GL
```

---

## Section 5: Financial Module Comparison — SAP vs. Oracle vs. Salesforce

| Financial Function | SAP S/4HANA | Oracle Cloud ERP | Salesforce |
|---|---|---|---|
| General Ledger | FI-GL (New GL with parallel ledgers) | Oracle Financials GL | Not applicable (no native GL) |
| Accounts Payable | FI-AP with three-way match | Oracle Payables | Not applicable |
| Accounts Receivable | FI-AR with dunning | Oracle Receivables | Revenue Cloud / Billing (add-on) |
| Fixed Asset Management | FI-AA with AFAB depreciation run | Oracle Fixed Assets | Not applicable |
| Management Accounting | CO module (cost/profit centers) | Oracle Costing | Not applicable |
| Reporting | SAP Analytics Cloud / SAP Fiori | Oracle OTBI / Analytics | Salesforce Reports and Dashboards |
| Intercompany Consolidation | SAP Group Reporting (S/4HANA) | Oracle Consolidation | Not applicable |

Salesforce does not have a native financial accounting module. Its Revenue Cloud and Billing products handle subscription billing and revenue recognition in SaaS business models, but they integrate with external ERP systems for GL posting rather than maintaining a full General Ledger.

---

## Section 6: Controlling Module — Internal vs. External Reporting

### FI vs. CO: The Core Distinction

| Dimension | FI (Financial Accounting) | CO (Controlling) |
|---|---|---|
| Audience | External: investors, auditors, regulators | Internal: managers, business unit leaders |
| Standard | GAAP, IFRS, legal requirements | Company-defined internal reporting structure |
| Reporting unit | Legal entity (company code) | Cost center, profit center, product line, project |
| Period | Calendar or fiscal year | Flexible period matching management cycles |
| Mandatory | Yes (legally required) | No (management decision) |

### Cost Center vs. Profit Center

| Dimension | Cost Center | Profit Center |
|---|---|---|
| Tracks | Costs only | Revenues and costs |
| Purpose | Departmental spending control | Business unit profitability |
| Examples | IT Dept, HR Dept, Facilities | Product Division, Geographic Region |
| SAP Object | KOSTL (cost center) | PRCTR (profit center) |

---

## Section 7: Month-End Close Sequence

A standard SAP month-end close follows this sequence:

1. Post all transactions for the period (invoices, receipts, time entries)
2. Run depreciation (AFAB) for all active assets
3. Execute overhead cost allocations from cost centers to cost objects
4. Run raw material price variance calculations (if applicable)
5. Reconcile sub-ledger balances to General Ledger totals
6. Perform intercompany matching and elimination (if multi-entity)
7. Generate draft financial statements for management review
8. Make any required adjusting entries
9. Lock the closed period (prevent backdated postings)
10. Issue final financial statements

ERP automation typically reduces close time from 10+ days to 3-5 days by automating steps 2, 3, and 5.

---

## Section 8: Certification Exam Tips

1. **The three-way match documents are: Purchase Order, Goods Receipt, Vendor Invoice.** This is directly tested. Know the three documents, what each verifies, and what happens when a discrepancy is found.

2. **FI is external reporting; CO is internal management accounting.** When asked which SAP module produces profitability by product line or region, the answer is CO — the General Ledger alone cannot produce this view.

3. **Depreciation is automatic in SAP through the AFAB transaction.** If a question asks how SAP handles monthly asset depreciation, the answer is the automated depreciation run.

4. **The dunning process is in FI-AR.** Dunning generates collection notices for overdue customer balances automatically; it is an AR function, not an AP function.

5. **FI sub-ledgers post to the GL automatically.** When a vendor invoice is posted in FI-AP, the GL journal entry is created simultaneously. No manual GL entry is needed.

6. **Salesforce does not have a native General Ledger.** Salesforce Revenue Cloud handles billing and revenue recognition for SaaS models but posts to an external ERP for accounting. If asked about GL management, the answer is SAP or Oracle — not Salesforce.

7. **Cost centers accumulate costs; profit centers track revenues and costs.** The distinction is tested in both CO configuration and management reporting questions.

8. **Period locking prevents backdated postings.** After the period-end close is complete, SAP locks the closed period so no additional postings can be made, ensuring financial statement integrity.

---

## Section 9: Required Trailhead and Study Resources

Complete before attempting the quiz:

- **Salesforce Trailhead — Revenue Cloud Basics**
  URL: trailhead.salesforce.com — search "Revenue Cloud Basics"
  Covers how Salesforce handles billing and revenue management — provides context for how CRM connects to financial processes.

- **Salesforce Trailhead — Financial Services Cloud Basics**
  URL: trailhead.salesforce.com — search "Financial Services Cloud Basics"
  Relevant for understanding Salesforce's financial services industry positioning.

---

## Section 10: Study Checklist

- Memorize the SAP FI module codes and their functions from Section 2.
- Trace through the three-way match flow in Section 3. Know the three documents and what happens on failure.
- Study the depreciation methods table in Section 4. Know which method is most commonly used for buildings versus technology equipment.
- Review the FI vs. CO distinction in Section 6. Be able to explain the difference in your own words.
- Trace the month-end close sequence in Section 7. Know the order and which steps are automated by ERP.
- Complete the Salesforce Trailhead "Revenue Cloud Basics" module.
- Watch the Module 05 video lecture.
- Complete Lab 05.
- Post to Discussion Forum 05 by Wednesday at 11:59 PM.
- Complete Quiz 05 (10 questions).
