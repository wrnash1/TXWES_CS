# Quiz: Module 09 — SAP Financial Accounting (FI Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

### Question 1

In SAP Financial Accounting, which organizational unit represents a legally independent entity that produces its own balance sheet and income statement?

- A) Controlling Area — the unit that manages internal cost reporting across the enterprise
- B) Business Area — the optional division used for internal segment reporting
- C) Company Code — the central SAP FI organizational unit representing a legal entity with independent financial statements
- D) Chart of Accounts — the master list of all G/L accounts used by the organization

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The Company Code is the foundational organizational unit in SAP FI. Every financial posting belongs to a Company Code. A multinational company might have one Company Code per subsidiary per country, each with its own balance sheet and income statement. Transaction OX02 manages Company Codes.
- *Why A is incorrect:* The Controlling Area is the link between FI and the CO module for internal cost reporting. It does not produce external financial statements and can span multiple Company Codes.
- *Why B is incorrect:* Business Areas are optional internal reporting divisions — they do not represent legally independent entities and do not produce standalone legal financial statements.
- *Why D is incorrect:* The Chart of Accounts is a configuration object — the list of available G/L accounts. It is assigned to a Company Code but is not itself an organizational unit.

---

### Question 2

An accountant at a manufacturing company receives a vendor invoice for $24,000 of raw materials received last week. Which SAP FI transaction code should the accountant use to post this invoice, and what is the resulting journal entry?

- A) FB70 — Debit Revenue, Credit Accounts Receivable
- B) F110 — Debit Accounts Payable, Credit Bank Account
- C) FB60 — Debit Raw Materials Expense (or Inventory), Credit Accounts Payable
- D) F-28 — Debit Bank Account, Credit Accounts Receivable

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* FB60 is the SAP transaction for entering a vendor invoice. The accounting entry is: Debit the expense or asset account (raw materials purchased) and Credit Accounts Payable (the liability created). This is the standard AP invoice entry in SAP FI.
- *Why A is incorrect:* FB70 is for customer invoices, not vendor invoices. The accounts in Option A (Revenue and AR) describe a sales transaction, not a purchase.
- *Why B is incorrect:* F110 is the Automatic Payment Program — it processes payments for already-posted invoices. It does not post the initial vendor invoice. The accounts described (AP and Bank) represent a payment, not an invoice entry.
- *Why D is incorrect:* F-28 is for posting incoming payments from customers — it clears open AR items. It has nothing to do with vendor invoice posting.

---

### Question 3

A company's AP team wants to automatically pay all vendor invoices that are due within the next seven days, generating ACH transfers for each eligible vendor without manual check writing. Which SAP FI transaction handles this?

- A) FB60 — the vendor invoice entry transaction that creates open items
- B) FBL1N — the vendor line item display that shows all open and cleared items
- C) F110 — the Automatic Payment Program that selects due invoices and generates payment files
- D) FEBAN — the electronic bank statement processing transaction

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* F110 is the SAP Automatic Payment Program. The AP team defines a payment run date, company code, payment methods, and the "next payment date." F110 then scans all open vendor invoices, determines which are due based on payment terms, groups payments by vendor and bank, and generates electronic payment files — all without manual intervention.
- *Why A is incorrect:* FB60 creates invoice records — it does not process payments. Posting an invoice creates an open AP item; F110 is what pays it.
- *Why B is incorrect:* FBL1N displays vendor line items for reporting and review. It is a display-only transaction and does not initiate any payments.
- *Why D is incorrect:* FEBAN processes incoming bank statements to reconcile the G/L with the bank's records. It is a bank reconciliation tool, not a payment processing tool.

---

### Question 4

In SAP FI, what does "Open Item Management" mean when applied to an Accounts Receivable account?

- A) The account balance is always visible to external auditors without restriction
- B) Every posted customer invoice creates an individual open item that remains visible until it is cleared by a matching incoming payment
- C) The account is open for posting by any user in any company code without authorization restrictions
- D) The account balance is recalculated and opened fresh at the start of each new fiscal year

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Open Item Management means each posted document (invoice) creates an "open item" on the account. The item remains open and visible in FBL5N until a matching payment is posted that clears it. This enables exact tracking of which invoices are paid and which remain outstanding — the foundation of AR management.
- *Why A is incorrect:* Open Item Management is an accounting data management concept, not an access control setting. It has nothing to do with auditor visibility or authorization.
- *Why C is incorrect:* Account access control is managed by SAP authorization objects and roles — entirely separate from the accounting concept of open item management.
- *Why D is incorrect:* Balance sheet accounts carry balances forward at year-end. P&L accounts are reset at year-end. Neither of these year-end behaviors describes open item management, which is about individual document-level tracking.

---

### Question 5

A customer's invoice has been outstanding for 65 days. The payment terms were Net 30. The credit manager wants SAP to automatically send an escalating payment reminder to the customer. Which SAP FI transaction initiates this process?

- A) FB70 — to re-post the invoice with an updated due date
- B) FBL5N — to display the customer's open line items for manual review
- C) F150 — the dunning run that generates automated payment reminders at escalating levels
- D) F110 — the automatic payment program that settles overdue customer balances

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* F150 is the SAP dunning run transaction. It reviews all open AR items, identifies which customers have overdue balances, and generates dunning letters at escalating levels of urgency. Level 1 is a friendly reminder; level 4 is a final notice before legal or collections action. This is the standard SAP AR collections automation tool.
- *Why A is incorrect:* FB70 posts a new customer invoice — it does not send reminders for existing invoices. Re-posting an already-issued invoice would create a duplicate billing.
- *Why B is incorrect:* FBL5N displays customer line items for manual review. It is a reporting transaction; it does not trigger any automated communication to customers.
- *Why D is incorrect:* F110 is the vendor payment program — it pays vendors, not customers. You do not "pay" overdue AR; you collect it. F110 has no role in AR collections.

---

### Question 6

An accountant posts a vendor invoice on June 28 with a Document Date of June 28 and a Posting Date of July 1. In which accounting period will this invoice appear?

- A) June — because the Document Date is June 28
- B) July — because the Posting Date is July 1
- C) Both June and July — SAP splits the entry across both periods proportionally
- D) Neither — SAP rejects entries where Document Date and Posting Date are in different months

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The Posting Date is the field that determines which accounting period a transaction is recorded in. Document Date is the date of the original business event and is used for reference. Since the Posting Date is July 1, SAP records this transaction in Period 7 (July), not Period 6 (June).
- *Why A is incorrect:* The Document Date does not determine the accounting period. Only the Posting Date drives period assignment. This distinction is a frequently tested concept because it is counterintuitive — the "real" date of the transaction and the "accounting" date are separate fields.
- *Why C is incorrect:* SAP does not split transactions across periods. Each document has a single Posting Date and therefore belongs to a single accounting period.
- *Why D is incorrect:* SAP does not reject documents where Document Date and Posting Date differ. Different-period dates are a common and legitimate accounting practice — for example, posting December invoices received in January with a January Posting Date to keep December closed.

---

### Question 7

Which SAP FI transaction is used to import an electronic bank statement and automatically match bank transactions to open G/L items?

- A) FF67 — Manual Bank Statement Entry
- B) F110 — Automatic Payment Program
- C) FEBAN — Electronic Bank Statement Processing
- D) S_ALR_87012301 — G/L Trial Balance

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* FEBAN is the SAP transaction for processing electronic bank statements. It imports the bank's transaction file, attempts to automatically match each line to an open G/L item (vendor payment, customer receipt), and flags unmatched items for manual review. Large organizations process hundreds of bank transactions daily through FEBAN.
- *Why A is incorrect:* FF67 is for manually entering bank statement data when a paper statement is received and no electronic file is available. It does not perform automatic matching.
- *Why B is incorrect:* F110 generates outgoing vendor payments — it does not process incoming bank statements or perform bank reconciliation.
- *Why D is incorrect:* S_ALR_87012301 is the G/L Trial Balance report — a read-only report showing G/L account balances. It does not import bank data or perform reconciliation.

---

### Question 8

A controller needs to generate a formal Balance Sheet and Income Statement for Company Code 1100 for the period ending June 30, 2026. Which SAP FI transaction is used?

- A) FB50 — to post the closing journal entries that finalize June balances
- B) FCCX — the Financial Closing Cockpit for managing the close checklist
- C) F.01 — the Financial Statements transaction that generates the Balance Sheet and P&L from G/L balances
- D) FS00 — to display the G/L account master data used in the financial statements

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* F.01 is the SAP Financial Statements transaction. The controller selects the Company Code, Financial Statement Version, fiscal year, and reporting period, and SAP generates a formatted Balance Sheet and Income Statement drawn from current G/L account balances.
- *Why A is incorrect:* FB50 is for posting manual journal entries. Closing journal entries may be posted with FB50, but generating the financial statements requires F.01 after posting is complete.
- *Why B is incorrect:* FCCX is the Financial Closing Cockpit — a project management tool for tracking the sequence of close activities. It manages who does what in what order, but it does not generate the financial statements itself.
- *Why D is incorrect:* FS00 maintains G/L account master data — names, types, field status groups. It is a configuration and reference tool, not a financial reporting transaction.

---

### Question 9

A vendor's invoice has payment terms of "2/10 Net 30." The invoice date is June 1 and the invoice amount is $50,000. The company pays on June 8. What is the correct payment amount?

- A) $50,000 — the full amount is always due regardless of when payment is made
- B) $49,000 — a 2% discount is taken because payment is made within 10 days
- C) $45,000 — a 10% discount applies because payment is made within 30 days
- D) $48,500 — a 3% discount applies because payment is made within the grace period

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* "2/10 Net 30" means: take a 2% early payment discount if paid within 10 days; otherwise pay the full amount within 30 days. June 8 is 7 days after the June 1 invoice date — within the 10-day discount window. Discount amount = $50,000 × 2% = $1,000. Payment = $50,000 − $1,000 = $49,000.
- *Why A is incorrect:* $50,000 would be correct only if paying after the 10-day discount window but within 30 days. Paying on June 8 (day 7) qualifies for the early payment discount.
- *Why C is incorrect:* $45,000 would imply a 10% discount, which is not part of the "2/10 Net 30" terms. The "10" in the term refers to 10 days — not 10 percent.
- *Why D is incorrect:* $48,500 would imply a 3% discount, which is not defined in these payment terms. There is no "grace period" discount category in standard SAP payment terms — only the cash discount and the net amount.

---

### Question 10

In SAP FI, the Reconciliation Account on a Vendor Master record serves which purpose?

- A) It stores the vendor's bank account number used for ACH payment transfers
- B) It is the G/L account that automatically receives the credit when a vendor invoice is posted, keeping the AP sub-ledger and General Ledger synchronized
- C) It defines the payment terms that determine when the vendor invoice is due
- D) It is the internal cost center account used to track vendor spending by department

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The Reconciliation Account is the G/L account that aggregates all transactions posted to the AP sub-ledger for a vendor. When FB60 posts a vendor invoice, SAP simultaneously credits the vendor's individual account in the AP sub-ledger AND the Reconciliation Account in the G/L — keeping both in sync automatically. You cannot post directly to a Reconciliation Account with a manual journal entry.
- *Why A is incorrect:* The vendor's bank account number is stored in the vendor's Company Code banking data (a separate tab in FK03). It is used for electronic payment execution by F110 but is not the Reconciliation Account.
- *Why C is incorrect:* Payment terms are stored in the vendor's Company Code data and are used to calculate due dates and cash discount windows. They are not the Reconciliation Account.
- *Why D is incorrect:* Cost centers are CO module objects used for internal cost allocation. They are assigned at the line-item level of individual transactions, not at the Vendor Master level. The Reconciliation Account is a G/L account — a balance sheet liability account, not a cost center.
