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

---

### Question 11

(5 points)

In SAP FI, which transaction code is used to display all open and cleared line items for a specific vendor account?

- A) FD03 — Display Customer Master
- B) FB60 — Enter Vendor Invoice
- C) FBL1N — Vendor Line Item Display
- D) F110 — Automatic Payment Program

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* FBL1N is the Vendor Line Item Display transaction. It shows all posted documents (invoices, credit memos, payments) for a vendor, filterable by open items, cleared items, or all items. It is the primary transaction for reviewing a vendor's payment history and outstanding balances.
  - *Why A is incorrect:* FD03 displays the Customer Master record — it shows customer master data, not vendor line items.
  - *Why B is incorrect:* FB60 is used to enter (create) a new vendor invoice. It does not display existing vendor transactions.
  - *Why D is incorrect:* F110 is the Automatic Payment Program that generates payment runs. It does not display individual vendor line items.

---

### Question 12

(5 points)

A G/L accountant discovers that a journal entry was posted to the wrong G/L account. The Posting Date was in the current open period. Which SAP FI approach is the correct way to correct this error?

- A) Delete the incorrect posting directly from the database using a developer SQL statement
- B) Use FB08 to reverse the incorrect document, then re-post with FB50 using the correct G/L account
- C) Change the G/L account field directly in the posted document using the document change function
- D) Post a new document crediting the wrong account and debiting the correct account — without reversing the original

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* SAP FI maintains a complete, immutable audit trail. Incorrect postings are corrected by reversing the original document (FB08 creates a mirror-image reversal document) and then posting the correct entry (FB50 for manual journal entries). This preserves the full history of both the error and the correction.
  - *Why A is incorrect:* Direct database manipulation in a production SAP system is a catastrophic control violation — it bypasses all audit trail mechanisms and would be detected immediately by auditors. SAP records are never corrected at the database level.
  - *Why C is incorrect:* SAP prevents changes to most fields in posted accounting documents. The G/L account on a posted line item cannot be changed after posting — it is part of the immutable audit record.
  - *Why D is incorrect:* While posting a correcting entry (without a formal reversal) is technically possible, it leaves the incorrect original document open and clutters the audit trail. The standard SAP practice is a formal reversal using FB08 to create a clean, traceable correction.

---

### Question 13

(5 points)

Which of the following correctly describes the **Chart of Accounts** in SAP FI and its relationship to Company Codes?

- A) Each Company Code must have its own unique Chart of Accounts; sharing is not permitted
- B) A Chart of Accounts is the master list of all G/L accounts; multiple Company Codes can share the same Chart of Accounts, but each Company Code activates only the accounts it needs
- C) The Chart of Accounts is identical to the Financial Statement Version used to generate reports
- D) A Chart of Accounts is assigned at the Controlling Area level and applies equally to all Company Codes

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A Chart of Accounts (e.g., INT — International Chart of Accounts) is a master list of G/L account numbers and descriptions. Multiple Company Codes in the same Client can share one Chart of Accounts, which standardizes account numbering across subsidiaries while allowing each Company Code to activate only the accounts it uses.
  - *Why A is incorrect:* SAP supports shared Charts of Accounts across Company Codes — this is a common configuration in multinational companies to standardize financial reporting.
  - *Why C is incorrect:* A Financial Statement Version defines how G/L accounts are grouped and displayed in printed financial statements. It is a separate configuration object from the Chart of Accounts, which is the underlying account master list.
  - *Why D is incorrect:* Charts of Accounts are assigned to Company Codes (in FI), not to Controlling Areas (in CO). While a Controlling Area can span multiple Company Codes, the Chart of Accounts assignment is at the Company Code level.

---

### Question 14

(5 points)

A company's vendor payment terms include a 3% early payment discount if paid within 15 days. The AP team notices that they are consistently missing the discount window because invoices sit in approval queues for 12 days before being posted. What is the business impact of this process inefficiency?

- A) Missing the discount window has no financial impact — vendors always accept the discounted amount regardless of payment timing
- B) Each missed discount represents a direct cash cost equal to 3% of the invoice amount — for high-volume payables this can amount to hundreds of thousands of dollars annually in forgone savings
- C) Late payment always triggers automatic penalty charges in SAP equal to the missed discount percentage
- D) The missed discount appears as a GL variance that inflates the company's cost of goods sold on the income statement

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Early payment discounts (cash discounts) are a significant source of working capital value. A 3% discount on a $1M annual payables volume equals $30,000 in foregone savings. Missing discount windows due to slow approval processes is a measurable business impact of AP inefficiency.
  - *Why A is incorrect:* Payment terms are contractual — vendors do not offer the discounted amount after the discount window expires. The full invoice amount is due after the discount period.
  - *Why C is incorrect:* SAP does not automatically charge a penalty equal to the missed discount. Late payment penalties (if any) are separate contractual terms and must be manually negotiated and configured — they are not automatic SAP behavior.
  - *Why D is incorrect:* A missed discount does not inflate COGS. The invoice is recorded at full face value when the discount is not taken. The impact is an opportunity cost (foregone savings), not an additional expense posting.

---

### Question 15

(5 points)

A controller runs an AR Aging Report using transaction S_ALR_87012178. The report shows $1,200,000 in the "Over 90 Days" bucket. What is the most appropriate immediate next step using SAP FI functionality?

- A) Run F.01 to generate the Balance Sheet and confirm the AR balance matches the aging total
- B) Run F150 (Dunning Run) to send Level 3 or Level 4 escalated payment reminders to all customers in the over-90-day bucket
- C) Run F110 (Automatic Payment Program) to automatically collect the overdue balances from customers' bank accounts
- D) Run AFAB (Depreciation Run) to write off the overdue receivables as uncollectible

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Customers with balances over 90 days past due have already missed multiple dunning cycles. The correct SAP response is to run F150 with the appropriate dunning level to escalate collection pressure — potentially triggering final demand letters, credit holds, or handoff to collections.
  - *Why A is incorrect:* F.01 generates financial statements. While it is useful for verifying that the Balance Sheet AR balance matches the aging, it is a reporting tool — it does not initiate any collection action.
  - *Why C is incorrect:* F110 is the vendor payment program that pays out to vendors. Companies cannot use SAP to automatically debit customers' bank accounts without explicit direct debit mandate agreements, which are a separate configuration.
  - *Why D is incorrect:* AFAB is the asset depreciation run — it has no function in accounts receivable or write-off processing. AR write-offs are processed through manual journal entries, not AFAB.

---

### Question 16

(5 points)

In SAP FI, a **clearing document** is created when which of the following events occurs?

- A) When a vendor invoice is entered using FB60, creating an open liability
- B) When an outgoing payment (F110) matches and settles an open vendor invoice, removing it from the open items list
- C) When the depreciation run (AFAB) posts period depreciation to the asset accounts
- D) When a customer invoice is created using FB70, creating an open receivable

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Clearing occurs when an open item (e.g., a vendor invoice) is matched and settled by a corresponding document (the payment). The clearing document records this settlement and marks both the invoice and the payment as cleared — removing them from the open items display and confirming the liability is extinguished.
  - *Why A is incorrect:* Entering a vendor invoice (FB60) creates an open item — the starting point of the AP lifecycle. The clearing event happens later when the invoice is paid.
  - *Why C is incorrect:* The depreciation run posts depreciation journal entries to asset and expense accounts. It does not create clearing documents — clearing is specific to the open item management context in AP and AR.
  - *Why D is incorrect:* Entering a customer invoice (FB70) creates an open AR item — analogous to the vendor invoice on the AP side. Clearing happens when the customer's payment is received and matched against the open invoice.

---

### Question 17

(5 points)

A company uses SAP S/4HANA's Universal Journal (ACDOCA table). What is the primary architectural benefit of the Universal Journal compared to the traditional SAP ECC financial architecture?

- A) The Universal Journal stores only summarized period balances, reducing storage requirements significantly
- B) The Universal Journal consolidates FI, CO, ML (Material Ledger), and AA (Asset Accounting) into a single line-item table, eliminating the need for periodic FI-CO reconciliation and enabling real-time multidimensional reporting
- C) The Universal Journal replaces the Chart of Accounts with a flat account structure that requires no configuration
- D) The Universal Journal prevents any manual journal entries, ensuring all postings originate from source transactions

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The ACDOCA Universal Journal table in SAP S/4HANA unifies financial and management accounting into a single line-item store. In SAP ECC, FI and CO maintained separate ledgers that required periodic reconciliation. In S/4HANA, every business transaction creates one Universal Journal entry that simultaneously satisfies FI and CO reporting requirements — eliminating the reconciliation step.
  - *Why A is incorrect:* The Universal Journal stores individual line items (not summarized balances), which actually increases granularity and storage compared to summarized period tables in ECC. The performance benefit comes from HANA's in-memory processing, not from storing less data.
  - *Why C is incorrect:* The Universal Journal does not change the Chart of Accounts concept. Companies still configure and maintain a Chart of Accounts; the Universal Journal changes the underlying data architecture, not the account master configuration.
  - *Why D is incorrect:* Manual journal entries (FB50) are still supported in S/4HANA. The Universal Journal does not restrict the source of postings; it unifies where all postings are stored.

---

### Question 18

(5 points)

A company runs the F110 Automatic Payment Program. After the payment run completes, which accounting entry is posted for a vendor invoice of $15,000 that is cleared?

- A) Debit Accounts Payable $15,000 / Credit Bank Account $15,000
- B) Debit Bank Account $15,000 / Credit Accounts Payable $15,000
- C) Debit Expense Account $15,000 / Credit Cash $15,000
- D) Debit Accounts Receivable $15,000 / Credit Revenue $15,000

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* When F110 clears a vendor invoice, it debits (reduces) the Accounts Payable liability (extinguishing the obligation) and credits (reduces) the Bank Account (cash paid out). This clears the open AP item and records the outflow of cash.
  - *Why B is incorrect:* This entry reverses the correct debits and credits — it would increase AP and decrease the bank, which is the wrong direction. A payment reduces AP (debit) and reduces cash (credit).
  - *Why C is incorrect:* The expense was already recorded when the invoice was posted (FB60). The payment entry does not re-record the expense; it settles the liability already on the books.
  - *Why D is incorrect:* Accounts Receivable and Revenue are customer-side accounts (FI-AR). Vendor payments are processed through Accounts Payable — the vendor owes nothing to the company; the company owes money to the vendor.

---

### Question 19

(5 points)

A company has payment terms with a supplier of "Net 60." SAP's cash discount base date is configured as the invoice date. The invoice is dated August 1. On what date will SAP's F110 Automatic Payment Program first consider this invoice eligible for payment?

- A) August 1 — immediately upon invoice receipt
- B) August 31 — one month after the invoice date
- C) September 30 — exactly 60 days after the August 1 invoice date
- D) October 1 — SAP adds one day buffer to all payment terms

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* "Net 60" means the full invoice amount is due 60 days from the base date. With cash discount base date = invoice date (August 1), the due date is August 1 + 60 days = September 30. F110 will include this invoice in the payment run on or after September 30.
  - *Why A is incorrect:* Payment terms define a grace period before the amount is due. F110 respects the due date — it does not pay invoices immediately upon receipt unless specifically configured to do so.
  - *Why B is incorrect:* August 31 is 30 days from August 1, which would correspond to Net 30 terms, not Net 60.
  - *Why D is incorrect:* SAP calculates due dates mathematically based on configured payment terms. There is no automatic one-day buffer added by the system.

---

### Question 20

(5 points)

A Finance Director wants to understand the difference between the **AP Aging Report** (S_ALR_87012103) and the **Vendor Line Item Display** (FBL1N). Which statement correctly distinguishes these two reports?

- A) AP Aging shows invoices in time buckets (current, 1-30 days, 31-60 days, etc.) for a snapshot view of outstanding payables by age; FBL1N shows all individual document-level transactions for a specific vendor in chronological detail
- B) AP Aging shows only cleared invoices; FBL1N shows only open invoices
- C) AP Aging requires input of a specific vendor number; FBL1N can run across all vendors simultaneously
- D) AP Aging is a CO report; FBL1N is an FI report — they use different data sources

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* The AP Aging Report groups open payables into time buckets for a portfolio-level view of payment obligations by age — useful for cash flow planning and identifying overdue invoices. FBL1N provides document-level drill-down for a specific vendor (or multiple vendors), showing every individual invoice, credit memo, and payment in chronological order.
  - *Why B is incorrect:* The AP Aging Report shows open items (not cleared — those are paid). FBL1N can show open items, cleared items, or all items depending on the selection criteria the user applies.
  - *Why C is incorrect:* The AP Aging Report can run across all vendors or be filtered by vendor range. FBL1N also accepts vendor ranges or specific vendors. Neither report is limited to a single vendor.
  - *Why D is incorrect:* Both AP Aging and FBL1N are FI reports drawing from the same FI posting data. Neither is a CO report. They are both in the FI-AP reporting area of SAP.
