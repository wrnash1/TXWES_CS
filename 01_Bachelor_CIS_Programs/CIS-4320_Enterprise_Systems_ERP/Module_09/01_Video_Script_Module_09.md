# Video Script: Module 09 — SAP Financial Accounting (FI Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

## SEGMENT 1 — Introduction: Financial Accounting as the ERP Spine (0:00–2:30)

Welcome back. I'm Professor Nash, and this is Module 9 of CIS-4320 Enterprise Systems and ERP.

Starting this module, we shift from the Salesforce CRM world into the SAP ERP world. For the next four modules — 9 through 12 — we go deep on SAP S/4HANA functional modules. This content maps directly to the SAP S/4HANA Essentials certification.

We begin with the Financial Accounting module — SAP FI. Why start here? Because every business transaction in an ERP system ultimately produces a financial impact that must be recorded. Buying raw materials, making a sale, paying an employee, building a product — all of it lands in FI. If you understand SAP FI, you understand the financial backbone that connects every other ERP module.

Today's topics: the Chart of Accounts, General Ledger postings, Accounts Payable, Accounts Receivable, bank reconciliation, and financial statement generation in SAP. All six areas appear on the SAP S/4HANA Essentials exam.

[SHOW SCREEN: SAP S/4HANA Fiori Launchpad — Finance section showing tiles: General Ledger, Accounts Payable, Accounts Receivable, Bank Accounting, Financial Closing]

---

## SEGMENT 2 — Organizational Structures in SAP FI (2:30–5:30)

Before posting a single transaction, you must understand the organizational structures that define where financial data belongs.

The most important SAP FI organizational unit is the **Company Code**. A Company Code is a legally independent entity that produces its own balance sheet and income statement. A multinational corporation might have dozens of Company Codes — one per subsidiary per country. Transaction OX02 displays and configures Company Codes.

[SHOW SCREEN: SAP transaction OX02 — Company Code table with columns: Company Code, Company Name, City, Country, Currency]

Below the Company Code, the **Business Area** is an optional division for internal segment reporting — think product lines or regional divisions that cut across legal entities.

The **Controlling Area** links SAP FI to the Controlling (CO) module. One Controlling Area can span multiple Company Codes, enabling unified internal cost reporting across a corporate group.

The **Chart of Accounts** is assigned at the Company Code level. It is the master list of every G/L account used by the company. Let's look at that next.

---

## SEGMENT 3 — Chart of Accounts and General Ledger Postings (5:30–10:00)

The Chart of Accounts defines all General Ledger accounts available for posting. Every financial transaction must post to at least one G/L account.

[SHOW SCREEN: SAP transaction FS00 — G/L Account master record: G/L Account Number, Account Group, Account Type (Balance Sheet or P&L), Short Description, Currency, Field Status Group]

G/L accounts are organized into **Account Groups** that define the number range and field requirements for each account type. A typical numbering convention:

- 1xxxxx — Current and Non-Current Assets
- 2xxxxx — Liabilities
- 3xxxxx — Equity
- 4xxxxx — Revenue
- 5xxxxx — Cost of Goods Sold
- 6xxxxx — Operating Expenses
- 7xxxxx — Other Income and Expense

The Account Type determines year-end behavior. **Balance Sheet accounts** carry their balance forward — cash, receivables, payables, inventory, fixed assets. **P&L accounts** are reset to zero at fiscal year-end when net income is transferred to retained earnings via the year-end closing program.

Now let me show you a G/L journal entry. Transaction **FB50** is the G/L account document entry screen.

[SHOW SCREEN: SAP FB50 — G/L account document screen showing Document Date, Posting Date, Document Type, Currency, and line item table with G/L Account, D/C indicator, Amount, Cost Center]

Every FI document must balance — total debits must equal total credits. SAP enforces this at save time. An unbalanced document cannot be posted. The system will display an error showing the imbalance amount.

Key document header fields:

- **Document Date** — the date of the original business transaction
- **Posting Date** — the date that determines which accounting period is updated; it can differ from Document Date
- **Document Type** — classifies the journal entry: SA (G/L document), KR (vendor invoice), DR (customer invoice), ZP (payment run)
- **Posting Period** — derived from the Posting Date; the period must be open in the **Fiscal Year Variant**

The **Fiscal Year Variant** defines the company's financial year structure. Some companies use a calendar year (January–December). Others use a non-calendar fiscal year — a university might run July–June. SAP accommodates both.

**Cost Objects** — cost centers, profit centers, internal orders — can be added to G/L line items to enable management reporting by organizational unit. Posting to a cost center means the expense is visible in the CO module for budget vs. actual analysis.

---

## SEGMENT 4 — Accounts Payable (10:00–13:30)

Accounts Payable in SAP FI manages all financial transactions with vendors — companies you purchase from.

The vendor record is the **Vendor Master** (transaction FK03). It stores the vendor name, address, payment terms, bank account details for electronic payment, and the **Reconciliation Account** — the G/L account to which all AP transactions for this vendor are aggregated for balance sheet reporting.

[SHOW SCREEN: SAP FK03 — Vendor Master display: General Data tab showing Name, Address; Company Code Data tab showing Payment Terms, Reconciliation Account; Purchasing Data tab showing Currency, Incoterms]

When a vendor invoice arrives, transaction **FB60** posts:

- Debit: Expense or Asset account
- Credit: Accounts Payable (the reconciliation account)

[SHOW SCREEN: SAP FB60 — Enter Vendor Invoice screen with Vendor field, Invoice Date, Posting Date, Amount, Tax Code, and line items with expense accounts]

**Payment Terms** control due date calculation. Net 30 means the invoice is due 30 days after the invoice date. 2/10 Net 30 means a 2% discount is available if paid within 10 days; otherwise full amount is due in 30 days. SAP calculates all due dates automatically from the terms on the Vendor Master.

The **Automatic Payment Program** — transaction **F110** — is one of the most critical SAP FI transactions. It scans all open vendor invoices, identifies which are due for payment based on terms and the proposed payment run date, groups payments by vendor and bank, and generates a payment file (ACH, check, wire transfer). No manual check writing. No risk of paying the same invoice twice. F110 is the engine behind high-volume corporate payments.

[SHOW SCREEN: SAP F110 — Automatic Payment Program parameters screen: Payment Run Date, Identification, Company Code, Payment Methods, Next Posting Date]

The **AP Aging Report** (transaction S_ALR_87012103) shows all open vendor invoices grouped by age: not yet due, 1–30 days overdue, 31–60 days, 61–90 days, over 90 days. Cash management teams use this daily.

---

## SEGMENT 5 — Accounts Receivable (13:30–17:00)

Accounts Receivable manages money that customers owe you — invoices issued and not yet paid.

The **Customer Master** (transaction FD03) mirrors the Vendor Master on the receivables side: customer name, address, credit limit, payment terms, bank details for direct debit, and the AR reconciliation account.

When you issue a customer invoice, transaction **FB70** posts:

- Debit: Accounts Receivable
- Credit: Revenue account

[SHOW SCREEN: SAP FB70 — Enter Customer Invoice screen with Customer field, Invoice Date, Amount, and revenue account line items]

When the customer pays, transaction **F-28** (Incoming Payment) clears the open item:

- Debit: Bank account
- Credit: Accounts Receivable — clears the open AR item

**Open Item Management** is a foundational SAP concept. When AR and AP accounts use open item management, every posted invoice creates an "open item" that remains visible in the system until a matching payment clears it. This allows exact tracking of which invoices are paid and which are outstanding. Transaction **FBL5N** displays all customer line items — open and cleared — for any customer.

[SHOW SCREEN: SAP FBL5N — Customer Line Item Display showing columns: Document Number, Invoice Date, Due Date, Amount, Clearing Date, Status (Open/Cleared)]

The **AR Aging Report** (transaction S_ALR_87012178) groups open customer items by age. This is the tool the collections team uses to identify overdue accounts.

**Dunning** is the automated customer payment reminder process. Transaction **F150** runs the dunning program: it reviews all open AR items, calculates which are overdue, and generates dunning letters at escalating levels. Level 1 is a polite payment reminder. Level 4 is a final notice before referral to collections or legal. Each level can be configured with different message text and follow-up actions.

---

## SEGMENT 6 — Bank Reconciliation and Financial Statements (17:00–21:00)

Every company must reconcile what the bank shows against what the accounting system shows. SAP FI handles this through the Bank Accounting sub-module.

The bank reconciliation process in SAP:

1. Import the bank statement — manually via transaction **FF67** or electronically via **FEBAN** (Electronic Bank Statement).
2. SAP attempts automatic matching of each bank line to an open G/L item (a vendor payment sent, a customer payment received).
3. Matched items are automatically cleared. Unmatched items are flagged for manual review.
4. After processing, the G/L bank account balance must equal the bank statement closing balance.

[SHOW SCREEN: SAP FEBAN — Electronic Bank Statement Processing screen showing bank transactions listed with status: Automatically Cleared, Manually Cleared, Unprocessed]

Large companies import bank statements daily for each bank account. SAP's matching algorithms recognize payment references and amounts, clearing most items automatically. Manual review is needed only for exceptions — payments that arrived without an invoice reference, or deposits that do not match any open AR item.

Now, financial statements. Transaction **F.01** runs the Financial Statements report.

[SHOW SCREEN: SAP F.01 — Financial Statements selection screen: Company Code, Financial Statement Version, Fiscal Year, Reporting Period]

The **Financial Statement Version** is a hierarchical mapping of G/L accounts to financial statement line items. The FI administrator configures which G/L accounts roll into "Cash and Cash Equivalents," which roll into "Trade Receivables," which roll into "Revenue from Product Sales," and so on. The report then uses live G/L balances to populate each line.

Standard financial reports in SAP FI:

- **Balance Sheet** — assets, liabilities, and equity at a point in time
- **Income Statement** — revenue minus expenses for a period
- **Trial Balance** — all G/L account balances (transaction S_ALR_87012301)

The **Financial Closing Cockpit** (transaction FCCX) in SAP S/4HANA is the month-end and year-end close management tool. It presents a checklist of close activities — post accruals, depreciate fixed assets, reconcile intercompany, generate financial statements — in the correct sequence, with status tracking for each step and team member assignment.

---

## SEGMENT 7 — Transaction Code Reference and Exam Summary (21:00–23:30)

Here is your SAP FI transaction code reference for the exam.

**Organizational Configuration:**

- OX02 — Display Company Codes
- FS00 — G/L Account Master Data Maintenance
- OBA7 — Document Types

**General Ledger:**

- FB50 — Enter G/L Account Document (journal entry)
- S_ALR_87012301 — G/L Trial Balance

**Accounts Payable:**

- FK03 — Display Vendor Master
- FB60 — Enter Vendor Invoice
- F110 — Automatic Payment Program
- S_ALR_87012103 — AP Aging Report

**Accounts Receivable:**

- FD03 — Display Customer Master
- FB70 — Enter Customer Invoice
- F-28 — Incoming Payment (clear AR)
- FBL5N — Customer Line Item Display
- F150 — Dunning Run
- S_ALR_87012178 — AR Aging Report

**Bank Accounting:**

- FF67 — Manual Bank Statement Entry
- FEBAN — Electronic Bank Statement Processing

**Financial Reporting:**

- F.01 — Financial Statements (Balance Sheet and P&L)
- FCCX — Financial Closing Cockpit

For the SAP exam: know what each transaction does, not the menu path. Scenario-based questions will describe a business event — "a vendor invoice was received" — and you need to identify the correct transaction code (FB60) and the resulting accounting entry (Dr Expense / Cr AP).

The lab this week takes you through the complete Procure-to-Pay financial flow: entering a vendor invoice (FB60), running the payment program (F110), and viewing the impact on the Trial Balance (S_ALR_87012301). Use the SAP Learning Hub free trial or the course-provided sandbox.

Module 10 covers Materials Management — the MM module that drives the purchasing side of the same Procure-to-Pay process we started in FI today.

---

*End of Script — Module 09*
