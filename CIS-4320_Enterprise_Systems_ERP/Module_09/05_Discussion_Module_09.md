# Discussion Forum: Module 09 — SAP Financial Accounting (FI Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

---

## Overview

This forum applies SAP FI concepts to realistic business scenarios involving financial data integrity, month-end close pressure, and ERP configuration decisions. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175–225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Reference at least one specific SAP FI object, transaction code, or concept (Company Code, G/L account, Reconciliation Account, Document Type, FB60, F110, F.01, Dunning, Open Item Management, etc.) by name
- Apply at least one accounting principle (double-entry, matching principle, period cut-off, etc.) to the scenario
- Make a concrete recommendation or analysis grounded in the scenario details

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must do one of the following:

- Identify a financial reporting risk or audit consequence your classmate did not mention
- Connect the scenario to a different SAP FI transaction or object your classmate did not address
- Describe how the problem in the scenario would affect an upstream or downstream ERP module (MM, SD, CO, or a Salesforce CRM integration)

---

## Scenarios

### Scenario A: The Posting Date Problem

A regional distribution company runs SAP S/4HANA. At the end of each month, the accounts payable team receives a stack of vendor invoices that arrived in the last three business days of the month. Under pressure from the controller to close the books quickly, the AP team posts all late-arriving invoices using a Posting Date in the new month rather than the month they represent — even though the goods were received and the expense was incurred in the prior month.

The finance director discovers this practice during a quarterly audit. The prior month's income statement is understated by $380,000 in expenses. The next month's income statement will be overstated by the same amount because those expenses will post there instead.

**Your task:** Explain the accounting principle this practice violates and why it matters for financial statement accuracy. What is the specific SAP FI field that controls which period a transaction is recorded in? How should the AP team handle late-arriving vendor invoices correctly in SAP — is there a way to keep the current period open a few extra days for late postings while closing it to routine new transactions? Reference at least one specific SAP concept or transaction.

### Scenario B: The Dunning Failure

A wholesale auto parts company has $2.3 million in total accounts receivable. Their SAP AR aging report shows that $890,000 — 39% of total AR — is more than 60 days overdue. When the new credit manager joins and reviews the situation, she discovers that Dunning has never been configured in their SAP FI system. The company has been manually emailing overdue customers whenever a credit analyst remembers to do so — which is inconsistent and undocumented. Several customers with balances over 90 days claim they never received a reminder. The company has written off $145,000 in bad debt over the past year.

**Your task:** What is the financial risk of $890,000 in overdue AR at a wholesale distribution company? Explain how SAP Dunning (transaction F150) works and how configuring it correctly would have prevented the current situation. What dunning levels would you configure for this company, and what escalation actions would you attach to the highest level? How does a well-functioning dunning process connect to the company's bad debt write-off rate?

### Scenario C: The Chart of Accounts Expansion

A mid-sized construction company uses SAP S/4HANA and currently has one Chart of Accounts shared across two Company Codes: their US operations and a Canadian subsidiary acquired 18 months ago. The US Controller complains that Canadian revenue and expense accounts are mixing into US financial reports. The Canadian Controller complains that the account numbers used in Canada do not align with Canadian GAAP reporting requirements. Both controllers want to know if the company should create a separate Chart of Accounts for Canada or continue sharing the current one.

**Your task:** Explain the relationship between a Chart of Accounts and a Company Code in SAP FI. Is it possible for two Company Codes to share one Chart of Accounts while producing separate financial statements? If so, how does SAP ensure separation of Company Code data even when the Chart of Accounts is shared? What configuration recommendation would you make — shared Chart of Accounts or separate — and what are the trade-offs of each approach?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter at top of post |
| Specific SAP FI object, transaction, or concept named and applied | 2 | SAP term used correctly in scenario context |
| Accounting principle applied correctly | 1 | Principle named and applied to the scenario |
| Concrete recommendation or analysis | 1 | Specific and grounded — not generic ERP commentary |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, substantive extension | 2 | Adds financial risk, audit consequence, or module connection |
| Peer response 2: 60+ words, substantive extension | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario A is not hypothetical. I have seen this in real implementations at multiple companies. The pressure to close the books fast creates a temptation to manipulate Posting Dates — pushing December expenses into January to make December look better, or pulling January revenue into December to hit a year-end target. In SAP, the Posting Date field is the mechanism that controls when a transaction is recorded. The system allows any date to be entered. The control is not technical — it is procedural. And when the procedure breaks down under month-end pressure, the financial statements become unreliable. The SAP S/4HANA Essentials exam expects you to understand not just what Posting Date does technically, but why it matters financially and how it can be misused. That is the difference between knowing the system and understanding the business.
