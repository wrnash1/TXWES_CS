# Reading Guide: Module 09 — SAP Financial Accounting (FI Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

## Introduction

SAP Financial Accounting (FI) is the module that records, manages, and reports all financial transactions for a legal entity. It is the system of record for external financial reporting — balance sheet, income statement, and cash flow — and the foundation for all other ERP module integrations. This reading guide covers organizational structures, chart of accounts design, the four FI sub-modules (GL, AP, AR, Bank Accounting), and the transaction codes tested on the SAP S/4HANA Essentials exam.

---

## Section 1 — Core Glossary

**Company Code**
The central SAP FI organizational unit representing a legally independent entity that produces its own balance sheet and income statement. All financial postings belong to a Company Code. Transaction OX02 manages Company Codes.

**Chart of Accounts**
The master list of all General Ledger accounts available for posting within a Company Code. Each G/L account has a number, description, account type, and field status group. Transaction FS00 maintains G/L account master data.

**General Ledger (G/L)**
The central accounting ledger where all financial transactions are recorded. Every FI posting creates a G/L document that updates G/L account balances. The G/L is the source for all financial reports.

**Document Principle**
The SAP rule that every financial transaction creates an immutable document with a unique document number. Documents cannot be deleted — only reversed with a counter-posting. This principle ensures a complete and auditable financial record.

**Posting Date**
The date that determines which accounting period a transaction is recorded in. Distinct from Document Date (the date of the original business transaction). Posting Date drives period-end reporting.

**Fiscal Year Variant**
The configuration that defines a company's financial year structure — calendar year (Jan–Dec) or a non-calendar variant (e.g., Jul–Jun). Determines the 12 posting periods and special periods for year-end adjustments.

**Vendor Master**
The master data record for a vendor (supplier). Contains name, address, payment terms, bank details for electronic payment, and the AP Reconciliation Account. Transaction FK03 displays Vendor Master data.

**Customer Master**
The master data record for a customer. Contains name, address, credit limit, payment terms, and the AR Reconciliation Account. Transaction FD03 displays Customer Master data.

**Reconciliation Account**
A G/L account that aggregates all transactions posted to a sub-ledger (AP or AR). When a vendor invoice is posted to a vendor's account, SAP simultaneously updates the AP Reconciliation Account in the G/L — keeping the sub-ledger and G/L in sync automatically.

**Open Item Management**
An account setting that tracks each posted item (invoice) as an individual "open item" until it is cleared by a matching payment. Used on all AR and AP accounts. Enables exact tracking of which invoices are paid and which are outstanding.

**Payment Terms**
The agreement between a company and a vendor or customer defining when payment is due and whether early payment discounts apply. Examples: Net 30 (full amount due in 30 days), 2/10 Net 30 (2% discount if paid within 10 days; otherwise full amount due in 30 days). SAP calculates due dates automatically.

**Automatic Payment Program (F110)**
The SAP transaction that automates vendor payment processing. Scans all open AP items, determines which are due based on terms and proposed payment date, groups payments by vendor, and generates electronic payment files. Eliminates manual check writing.

**Dunning**
The automated process of sending payment reminders to overdue customers. Transaction F150 runs the dunning program. Dunning levels escalate from polite reminders (level 1) to final notices (level 4).

**Financial Statement Version**
A hierarchical mapping of G/L accounts to financial statement line items. Configures how G/L account balances are grouped and labeled in the Balance Sheet and Income Statement reports.

**Financial Closing Cockpit (FCCX)**
The SAP S/4HANA tool that manages the month-end and year-end close process as a checklist-driven workflow with task assignments, dependencies, and status tracking.

---

## Section 2 — SAP FI Organizational Structure

```text
CLIENT (SAP System Level)
    |
    +-- COMPANY CODE 1000 (US Legal Entity)
    |       |
    |       +-- Chart of Accounts: CAUS
    |       +-- Fiscal Year Variant: K4 (Calendar Year)
    |       +-- Controlling Area: CO-NA
    |
    +-- COMPANY CODE 2000 (Germany Legal Entity)
            |
            +-- Chart of Accounts: CADE
            +-- Fiscal Year Variant: K4
            +-- Controlling Area: CO-EU
```

### SAP FI Sub-Module Overview

| Sub-Module | Code | Scope |
|---|---|---|
| General Ledger | FI-GL | All G/L postings, financial statements, period close |
| Accounts Payable | FI-AP | Vendor invoices, payments, vendor master, aging |
| Accounts Receivable | FI-AR | Customer invoices, incoming payments, customer master, dunning |
| Bank Accounting | FI-BL | Bank statement import, bank reconciliation, cash management |
| Fixed Assets | FI-AA | Asset master, depreciation, acquisition, disposal |
| Special Purpose Ledger | FI-SL | Parallel reporting ledgers for different accounting standards |

---

## Section 3 — Chart of Accounts Structure

### Standard G/L Account Number Ranges

| Range | Account Type | Examples |
|---|---|---|
| 1xxxxx | Current Assets | Cash, AR, Inventory, Prepaid Expenses |
| 1xxxxx (non-current) | Fixed Assets | Buildings, Equipment, Accumulated Depreciation |
| 2xxxxx | Liabilities | AP, Accrued Liabilities, Long-Term Debt |
| 3xxxxx | Equity | Common Stock, Retained Earnings |
| 4xxxxx | Revenue | Product Revenue, Service Revenue |
| 5xxxxx | Cost of Goods Sold | Materials, Direct Labor, Manufacturing Overhead |
| 6xxxxx | Operating Expenses | Salaries, Rent, Utilities, Depreciation |
| 7xxxxx | Other Income and Expense | Interest Income, Interest Expense, Gain on Sale |

### G/L Account Type Comparison

| Account Type | Year-End Treatment | Examples |
|---|---|---|
| Balance Sheet | Balance carried forward to next year | Cash, AR, AP, Inventory, Equity |
| P&L (Income Statement) | Balance reset to zero; net income closed to Retained Earnings | Revenue, COGS, Operating Expenses |

---

## Section 4 — G/L Document Structure

### FI Document Header Fields

| Field | Description | Exam Relevance |
|---|---|---|
| Document Number | Auto-generated unique ID per posting | Immutable; referenced in reversals |
| Company Code | Legal entity this posting belongs to | All postings are Company Code-specific |
| Document Date | Date of the original business event | May differ from Posting Date |
| Posting Date | Date used to determine accounting period | Drives which period is updated |
| Document Type | Classification of transaction (SA, KR, DR, ZP) | Determines number range and account type rules |
| Currency | Transaction currency | SAP stores amounts in both local and foreign currency |
| Reference | External reference number (invoice number, contract) | Used for clearing and matching |

### Document Type Reference

| Document Type | Description | Typical Use |
|---|---|---|
| SA | G/L account document | Manual journal entries, accruals, corrections |
| KR | Vendor invoice | AP invoice posting (FB60) |
| KZ | Vendor payment | AP payment clearing |
| DR | Customer invoice | AR invoice posting (FB70) |
| DZ | Customer payment | AR incoming payment clearing |
| ZP | Payment program document | F110 automatic payment run output |

---

## Section 5 — Accounts Payable Process Flow

```text
[Vendor Invoice Received]
        |
        v
[Post Vendor Invoice — FB60]
  Dr: Expense / Asset Account
  Cr: Accounts Payable (Reconciliation Account)
  Open Item created on Vendor account
        |
        v
[Invoice Verification and Approval]
  Three-way match in MM (optional): PO + GR + Invoice
        |
        v
[Automatic Payment Program — F110]
  Selects due invoices based on Payment Terms
  Groups payments by Vendor and Bank
  Generates payment file (ACH / Check / Wire)
        |
        v
[Payment Posted]
  Dr: Accounts Payable (clears open item)
  Cr: Bank Clearing Account
        |
        v
[Bank Transfer Executed]
  Dr: Bank Clearing Account
  Cr: Bank Account (when bank confirms)
```

### AP Key Transaction Codes

| Transaction | Description |
|---|---|
| FK03 | Display Vendor Master |
| FB60 | Enter Vendor Invoice |
| FB65 | Enter Vendor Credit Memo |
| MIRO | Invoice Verification (MM-linked; three-way match) |
| F110 | Automatic Payment Program |
| FBL1N | Vendor Line Item Display (open and cleared items) |
| S_ALR_87012103 | AP Aging Report |

---

## Section 6 — Accounts Receivable Process Flow

```text
[Customer Order Fulfilled / Service Delivered]
        |
        v
[Post Customer Invoice — FB70]
  Dr: Accounts Receivable (Reconciliation Account)
  Cr: Revenue Account
  Open Item created on Customer account
        |
        v
[Invoice Sent to Customer]
        |
  Customer pays within terms? --- No ---> [Dunning — F150]
        |                                  Level 1: Reminder
        Yes                                Level 2: Notice
        |                                  Level 3: Final Notice
        v                                  Level 4: Referral
[Incoming Payment — F-28]
  Dr: Bank Account
  Cr: Accounts Receivable (clears open item)
```

### AR Key Transaction Codes

| Transaction | Description |
|---|---|
| FD03 | Display Customer Master |
| FB70 | Enter Customer Invoice |
| FB75 | Enter Customer Credit Memo |
| F-28 | Post Incoming Payment |
| FBL5N | Customer Line Item Display |
| S_ALR_87012178 | AR Aging Report |
| F150 | Dunning Run |

---

## Section 7 — Bank Reconciliation Process

### Bank Reconciliation Steps

| Step | Description | Transaction |
|---|---|---|
| 1 | Receive bank statement (paper or electronic file) | — |
| 2 | Import electronic bank statement | FEBAN |
| 3 | Manual bank statement entry (if paper) | FF67 |
| 4 | SAP auto-matches bank lines to open G/L items | Automatic in FEBAN |
| 5 | Review unmatched items; post manually | FEBAN |
| 6 | Verify G/L bank account balance equals bank statement balance | S_ALR_87012301 |

### Bank Reconciliation Accounting

| Event | Debit | Credit |
|---|---|---|
| Vendor payment cleared by bank | AP Clearing Account | Bank Account |
| Customer payment received at bank | Bank Account | AR Clearing Account |
| Bank fee charged | Bank Fee Expense | Bank Account |
| Interest earned | Bank Account | Interest Income |

---

## Section 8 — Financial Statement Generation

### Transaction F.01 Parameters

| Parameter | Description |
|---|---|
| Company Code | Which legal entity to report |
| Financial Statement Version | The account grouping hierarchy for the report |
| Fiscal Year | Which year to report |
| Reporting Period | Which period (month) through which to report |
| Comparison Period | Prior year or prior period for variance comparison |

### Financial Statement Version Hierarchy Example

```text
BALANCE SHEET
  Assets
    Current Assets
      Cash and Cash Equivalents   [G/L 100000-109999]
      Accounts Receivable         [G/L 110000-119999]
      Inventory                   [G/L 130000-139999]
    Non-Current Assets
      Property, Plant, Equipment  [G/L 200000-249999]
  Liabilities
    Current Liabilities
      Accounts Payable            [G/L 310000-319999]
      Accrued Liabilities         [G/L 320000-329999]
  Equity
    Retained Earnings             [G/L 400000-400999]

INCOME STATEMENT
  Revenue                         [G/L 500000-509999]
  Cost of Goods Sold              [G/L 600000-609999]
  Operating Expenses              [G/L 700000-799999]
  Net Income = Revenue - COGS - OpEx
```

---

## Section 9 — Transaction Code Master Reference

| Transaction | Module | Description |
|---|---|---|
| OX02 | FI Config | Display/configure Company Codes |
| FS00 | FI-GL | G/L Account master data |
| FB50 | FI-GL | Enter G/L Account document (journal entry) |
| S_ALR_87012301 | FI-GL | G/L Trial Balance |
| F.01 | FI-GL | Financial Statements (Balance Sheet and P&L) |
| FCCX | FI-GL | Financial Closing Cockpit |
| FK03 | FI-AP | Display Vendor Master |
| FB60 | FI-AP | Enter Vendor Invoice |
| F110 | FI-AP | Automatic Payment Program |
| FBL1N | FI-AP | Vendor Line Item Display |
| S_ALR_87012103 | FI-AP | AP Aging Report |
| FD03 | FI-AR | Display Customer Master |
| FB70 | FI-AR | Enter Customer Invoice |
| F-28 | FI-AR | Post Incoming Payment |
| FBL5N | FI-AR | Customer Line Item Display |
| F150 | FI-AR | Dunning Run |
| S_ALR_87012178 | FI-AR | AR Aging Report |
| FF67 | FI-BL | Manual Bank Statement Entry |
| FEBAN | FI-BL | Electronic Bank Statement Processing |

---

## Section 10 — Exam Tips

> **Exam Tip 1 — Company Code is the central FI unit.** Every financial posting belongs to a Company Code. A Company Code represents a legally independent entity with its own balance sheet. Multiple Company Codes can share a Chart of Accounts and Controlling Area.

> **Exam Tip 2 — Posting Date vs. Document Date.** Posting Date determines which accounting period is updated. Document Date is the date of the original business event. They can be different — for example, a December invoice processed in January has a Document Date in December and a Posting Date in January.

> **Exam Tip 3 — Reconciliation Accounts.** AP and AR use reconciliation accounts to keep sub-ledger and G/L in sync automatically. You cannot post directly to a reconciliation account in a manual journal entry — SAP prevents this. Postings must go through the vendor or customer sub-ledger.

> **Exam Tip 4 — F110 is the Automatic Payment Program.** When a scenario describes paying multiple vendor invoices automatically, the answer is F110. Know that it selects invoices based on due dates, generates payment files, and posts the clearing entry automatically.

> **Exam Tip 5 — Open Item Management.** AR and AP accounts use open item management. Each invoice is an open item until cleared by a payment. FBL5N shows customer open items. FBL1N shows vendor open items. These are the go-to transactions for answering "which invoices are unpaid?"

> **Exam Tip 6 — Dunning is automated AR follow-up.** F150 is the dunning run. It sends escalating payment reminders to overdue customers. Know that dunning levels exist and escalate — this is often tested in a scenario about reducing overdue AR.

---

## Section 11 — Study Checklist

- Review the SAP FI organizational structure diagram in Section 2.
- Memorize G/L account number ranges and which account type (Balance Sheet vs. P&L) each range represents.
- Trace the AP process flow in Section 5 and match each step to its transaction code.
- Trace the AR process flow in Section 6 and match each step to its transaction code.
- Study the bank reconciliation steps table in Section 7.
- Review the Financial Statement Version hierarchy in Section 8.
- Memorize the transaction code master reference in Section 9.
- Complete the Module 09 SAP Learning Hub or sandbox exercises.
- Watch the Module 09 video lecture.
- Complete Lab 09.
- Post to Discussion Forum 09 by Wednesday at 11:59 PM.
- Complete Quiz 09.

---

## 9. Supplemental Resources

**1. SAP Learning — Financial Accounting with SAP S/4HANA: Business Processes**
<https://learning.sap.com/learning-journeys/run-financial-accounting-with-sap-s-4hana>
Official SAP learning journey covering the complete FI module: G/L, AP, AR, and asset accounting. Maps directly to the transaction codes (FB60, F110, F150, FEBAN) and process flows tested in this module's quiz and Lab 09.

**2. SAP Help Portal — SAP S/4HANA Finance Transaction Code Reference**
<https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/sts/2022/en-US/index.html>
Official SAP product documentation. The FI section provides detailed explanation of each transaction code's purpose, prerequisites, and output — the authoritative reference for the transaction code master table in Section 9.

**3. AICPA — Revenue Recognition and Financial Reporting Standards (ASC 606 / IFRS 15)**
<https://www.aicpa.org/resources/article/revenue-recognition>
Resource covering how revenue recognition standards affect how ERP systems must be configured to comply with ASC 606 and IFRS 15. Relevant to the financial statement generation content in this module and the compliance themes in Module 15.
