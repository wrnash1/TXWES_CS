# Lab Activity: Module 09 — SAP Financial Accounting (FI Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

This lab applies SAP FI concepts through scenario-based analysis and transaction tracing. You will map business events to SAP FI transactions, construct journal entries, trace the Accounts Payable and Accounts Receivable process flows, and analyze a bank reconciliation exception. No live SAP system is required — all work is analytical based on the Module 09 content.

**Estimated Time:** 90–110 minutes

**Submission:** Upload a single PDF to Canvas under "Lab 09 — SAP Financial Accounting."

---

## Learning Objectives

By completing this lab you will be able to:

- Map business financial events to the correct SAP FI transaction codes
- Construct double-entry journal entries for vendor invoices, customer invoices, and payments
- Trace the complete AP Procure-to-Pay financial flow from invoice posting through payment clearing
- Trace the AR Order-to-Cash financial flow from invoice posting through customer payment
- Analyze an aging report and recommend appropriate follow-up actions
- Explain the bank reconciliation process and identify common exception scenarios

---

## Company Background

**Company:** Ridgeline Industrial Supply Co.

**Industry:** B2B wholesale distribution — industrial components and safety equipment

**SAP System:** SAP S/4HANA 2023 (Cloud Public Edition)

**Company Code:** 1100 (Ridgeline US Operations)

**Fiscal Year:** Calendar year (January–December)

**Chart of Accounts:** RIUS (Ridgeline Industrial US)

The Controller at Ridgeline has asked you to analyze four open accounting situations from the current month (June 2026).

---

## Part A — Transaction Code and Object Mapping (20 points)

### A-1: Business Event to Transaction Code

For each business event at Ridgeline, identify the correct SAP FI transaction code and the SAP object that is created or updated.

| Business Event | SAP Transaction Code | SAP Object Created or Updated |
|---|---|---|
| The accounting team receives an invoice from Apex Welding Supplies for $18,500 and needs to post it in SAP | | |
| A controller needs to view all open and cleared invoices for the Apex Welding Supplies vendor account | | |
| Ridgeline sends an invoice to Cornerstone Manufacturing for $42,000 for delivered safety equipment | | |
| Ridgeline's accountant runs the weekly payment processing for all vendor invoices due this week | | |
| Cornerstone Manufacturing's account is 35 days overdue; the credit manager wants to send a payment reminder | | |
| The Controller needs a complete list of all vendor invoices due in the next 30 days, grouped by age | | |
| The Controller imports the June bank statement from Ridgeline's bank to match against G/L entries | | |
| The Controller needs to generate the Balance Sheet and Income Statement for June 2026 | | |

---

## Part B — Journal Entry Construction (30 points)

### B-1: Vendor Invoice Posting

Ridgeline receives the following invoice from Apex Welding Supplies on June 5, 2026:

- Invoice number: AWP-20260605
- Invoice date: June 5, 2026
- Posting date: June 5, 2026
- Goods: 200 units of industrial welding masks at $92.50 each
- Total: $18,500
- Payment terms: Net 30
- Cost assignment: Cost Center 4200 (Warehouse Operations)

Construct the complete SAP FI journal entry that transaction FB60 would create. Include:

- Document Type
- All account line items with account names, debit/credit designation, and amounts
- Cost Center assignment
- Due date (show calculation)

Verify your entry balances (total debits = total credits).

### B-2: Vendor Payment Posting

On July 3, 2026 (within payment terms), Ridgeline pays the Apex Welding Supplies invoice via ACH bank transfer. The Automatic Payment Program (F110) runs and processes the payment.

Construct the journal entry that F110 posts to clear this payment. Show:

- All account line items with debit/credit designation and amounts
- Which open item is cleared by this posting
- The net effect on the AP Reconciliation Account balance

### B-3: Customer Invoice and Incoming Payment

On June 10, 2026, Ridgeline delivers $42,000 of safety equipment to Cornerstone Manufacturing and issues an invoice (payment terms: Net 30).

On July 8, 2026, Cornerstone makes the full payment.

Construct two separate journal entries:

1. The June 10 customer invoice posting (FB70)
2. The July 8 incoming payment posting (F-28) that clears the open AR item

For each entry: list account names, debit/credit designation, and amounts. Verify each entry balances.

---

## Part C — Aging Report Analysis (25 points)

### C-1: AP Aging Analysis

Ridgeline's AP aging report (S_ALR_87012103) as of June 30, 2026 shows the following open vendor invoices:

| Vendor | Invoice Date | Amount | Payment Terms | Days Outstanding |
|---|---|---|---|---|
| Apex Welding Supplies | June 5 | $18,500 | Net 30 | 25 days |
| Pinnacle Safety Corp | May 8 | $31,200 | Net 30 | 53 days |
| Industrial Metals LLC | May 15 | $9,750 | 2/10 Net 30 | 46 days |
| Harbor Components | April 22 | $22,400 | Net 45 | 69 days |
| Atlas Equipment Co | June 18 | $14,100 | Net 30 | 12 days |

Answer the following questions:

1. Which invoices are currently past due? Show your calculation for each.
2. Which invoice represents the most significant cash discount opportunity that has already been lost? Explain.
3. Harbor Components is 24 days past their Net 45 terms. What risk does this create for Ridgeline's vendor relationship, and what action should the AP team take immediately?
4. The Controller wants to prioritize this week's payment run to protect vendor relationships while conserving cash. Which two invoices would you recommend paying first and why?

### C-2: AR Aging Analysis

Ridgeline's AR aging report (S_ALR_87012178) as of June 30, 2026 shows:

| Customer | Invoice Date | Amount | Payment Terms | Days Outstanding |
|---|---|---|---|---|
| Cornerstone Manufacturing | June 10 | $42,000 | Net 30 | 20 days |
| Bridgecross Industrial | April 30 | $28,500 | Net 30 | 61 days |
| Southland Fabricators | March 15 | $16,800 | Net 30 | 107 days |
| Westgate Construction | June 1 | $11,400 | Net 30 | 29 days |
| Northfield Systems | May 5 | $34,200 | Net 30 | 56 days |

Answer the following questions:

1. Calculate the total outstanding AR balance and the percentage that is more than 60 days overdue.
2. Southland Fabricators has been outstanding 107 days on a $16,800 invoice. What dunning level should be in effect for this account? What does that dunning level typically mean in terms of escalation?
3. Bridgecross Industrial (61 days) and Northfield Systems (56 days) are both significantly overdue. The credit manager proposes placing a credit hold on both accounts. What does a credit hold mean in an ERP system, and how would it be configured in SAP FI?
4. What is the total forecasted cash inflow if all invoices due within 30 days are collected on time?

---

## Part D — Bank Reconciliation Exception Analysis (25 points)

### D-1: Reconciliation Scenario

Ridgeline's June 30 bank statement shows a closing balance of $847,320. The G/L bank account (G/L 100100) shows a balance of $812,940 as of June 30. The reconciliation team imports the electronic bank statement using transaction FEBAN.

The auto-matching process resolves most transactions, but the following five items remain unmatched:

**Unmatched Bank Items (amounts received by the bank but not in G/L):**

1. Deposit of $22,500 received June 28 — reference: REF-45821
2. Deposit of $14,200 received June 29 — no reference number
3. Bank service fee charge of $285 — June 30

**Unmatched G/L Items (amounts in G/L but not yet on bank statement):**

4. Check issued to Harbor Components for $22,400 — issued June 27, not yet cleared at bank
5. ACH payment to Pinnacle Safety Corp for $31,200 — initiated June 30, not yet settled

For each unmatched item:

- Identify whether it is a timing difference (legitimate outstanding item) or a posting error requiring investigation
- Describe the action the accounting team should take in SAP to resolve it
- Identify the SAP transaction code applicable to the resolution action

### D-2: Reconciliation Proof

After all adjustments, prepare a formal bank reconciliation proof showing:

- Bank statement balance (starting point)
- Adjustments for outstanding checks and deposits in transit
- Adjusted bank balance

- G/L balance (starting point)
- Adjustments for unrecorded bank items
- Adjusted G/L balance

Both adjusted balances should agree. Show your arithmetic.

---

## Submission Instructions

1. Compile all responses into a single clearly labeled PDF.
2. Journal entries must be formatted in debit/credit table format — not prose.
3. Calculations must be shown — not just answers.
4. Name your file: `Lab09_LastName_FirstName.pdf`
5. Upload to Canvas under "Lab 09 — SAP Financial Accounting."
6. Deadline: See course schedule. Late submissions lose 10 points per day.

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Company Financial Close Simulation

A holding company (ParentCo, Company Code 1000) has two subsidiaries: ManufactureCo (Company Code 1100, Germany) and DistributeCo (Company Code 1200, US). During June, the following intercompany transactions occurred: ManufactureCo sold $180,000 of finished goods to DistributeCo; DistributeCo has not yet paid. Both companies share the same Chart of Accounts (INT).

1. Write the journal entry for ManufactureCo (Company Code 1100) recording the intercompany sale. Specify the G/L accounts (use account number ranges from the Reading Guide), the SAP transaction code used, and whether the posting creates an open item.
2. Write the journal entry for DistributeCo (Company Code 1200) recording the intercompany purchase receipt. Specify accounts, transaction code, and the resulting open item status.
3. Explain the two steps required at month-end consolidation to eliminate this intercompany transaction from ParentCo's consolidated financial statements. Name the specific accounts eliminated and the eliminating journal entry.
4. Identify which SAP tool (FI-LC or SAP Group Reporting) would automate step 3 and describe what configuration would be needed to identify this transaction as intercompany at the time of posting.

### Challenge 2: AP Process Audit and Control Assessment

A company's internal audit team is reviewing the Accounts Payable process for Segregation of Duties (SOD) compliance. The AP team of four people currently operates as follows: Person A creates vendor master records AND enters invoices. Person B approves invoices AND runs the F110 payment program. Person C handles bank reconciliation AND also has access to FB60. Person D has view-only access to all AP transactions.

1. Identify every SOD conflict in the described process. For each conflict, explain the specific fraud scenario it enables (what could go wrong if one person controls both functions).
2. Redesign the role assignments for the four-person team to eliminate all SOD conflicts while keeping the team at four people. Specify exactly which SAP transactions each person should be authorized to run in your redesigned model.
3. Define two automated preventive controls (system-enforced) and two detective controls (monitoring/reporting) that SAP FI can provide to strengthen AP fraud prevention beyond role separation alone.
4. Write a one-paragraph risk assessment memo (75-100 words) for the CFO summarizing the highest-risk SOD violation you identified and the business impact if it went undetected for 12 months.

### Reflection Questions

1. In the multi-company scenario, the intercompany sale created an AR in ManufactureCo and an AP in DistributeCo — both legitimate postings at the entity level. Why does consolidation require eliminating both, and what would the consolidated income statement show if the elimination was not performed?
2. The SOD redesign required you to separate vendor master creation from invoice entry. In a company with only two AP staff, this separation may not be feasible. What compensating controls could a two-person AP team implement to reduce fraud risk without full role separation?

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Transaction code and object mapping | 20 | All 8 events mapped to correct transaction code and SAP object |
| B-1: Vendor invoice journal entry | 10 | Correct document type; correct accounts; correct D/C; cost center included; due date calculated; entry balances |
| B-2: Vendor payment journal entry | 10 | Correct clearing entry; open item identified; AP reconciliation account impact described |
| B-3: Customer invoice and payment journal entries | 10 | Both entries correct; accounts named; D/C correct; both entries balance |
| C-1: AP aging analysis | 13 | Past due invoices identified with calculation; discount opportunity named; vendor risk described; payment priority recommendation justified |
| C-2: AR aging analysis | 12 | Total and overdue percentage calculated; dunning level identified; credit hold explained; forecasted collections calculated |
| D-1: Reconciliation exception analysis | 15 | Each item correctly classified; resolution action described; transaction code identified |
| D-2: Reconciliation proof | 10 | Both adjusted balances calculated correctly and agree |
| **Total** | **100** | |
