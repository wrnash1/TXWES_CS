# Discussion Forum: Module 05 - Financial Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

---

## Overview

This forum applies Module 05 financial module concepts to realistic business scenarios. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175-225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Name at least one specific SAP financial sub-module (FI-GL, FI-AP, FI-AR, FI-AA, or CO) and explain its role in the scenario
- Reference a specific financial control or process (three-way match, dunning, depreciation run, period lock, etc.)
- Make a concrete recommendation or analysis grounded in the scenario

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must:

- Add a financial risk or consequence your classmate did not mention
- Connect the scenario to a specific journal entry or GL impact
- Or describe how the control your classmate referenced would appear in a Salesforce revenue management context

---

## Scenarios

### Scenario A: The Approval Shortcut

A regional construction company processes approximately 400 vendor invoices per month. After implementing SAP FI-AP with the three-way match, the AP manager complains that 35% of invoices are being blocked for review because the purchasing team frequently orders materials with a verbal approval and creates the purchase order retroactively after the goods arrive — sometimes with different quantities or prices than what was actually ordered. The operations team argues that the three-way match is "slowing down the business" and asks the AP manager to configure SAP to simply approve all invoices without the three-way match.

**Your task:** Why is disabling the three-way match a dangerous financial decision, even if it does speed up payment processing? What is the root cause of the 35% block rate — and is it actually caused by the three-way match, or by the ordering process upstream? What SAP-based process improvement (not involving removing the three-way match) would reduce the block rate while preserving the financial control?

### Scenario B: The Depreciation Discovery

A university's facilities department has been managing 120 buildings and major equipment items on a spreadsheet since 2008. Some assets have been in service for 15+ years with no depreciation calculated because "nobody updated the spreadsheet." The university is implementing SAP FI-AA and the project team must load the asset master records and calculate the accumulated depreciation for all assets retroactively. The CFO is concerned that the balance sheet will show a significant prior-period adjustment when the correct accumulated depreciation is recorded.

**Your task:** Explain why correct depreciation recording matters for the Balance Sheet and Income Statement. What is the process for loading historical assets into SAP FI-AA (conceptually — not SAP transaction codes)? Why is prior-period depreciation correction necessary even if it causes a one-time balance sheet adjustment? What governance improvement would SAP provide going forward to prevent this from happening again?

### Scenario C: The Profitability Mystery

A $240 million diversified manufacturing company has been on SAP for 3 years with FI (General Ledger, AP, AR) active. The CEO asks the CFO: "We made $18 million in operating profit this year. But I know our three product divisions have very different margins. Which one is making money and which is losing money?" The CFO cannot answer because the company never implemented the CO (Controlling) module — all costs are posted to the General Ledger by account type but not by product division. The company's external auditor confirms the financial statements are accurate.

**Your task:** Why are the financial statements accurate yet unable to answer the CEO's question? Explain the difference between FI (external reporting) and CO (internal management reporting). If the company implemented CO Profit Center Accounting for their three product divisions, describe what data would need to be configured or loaded to produce the product-line profitability view. What business risk does the absence of this information create for the company's strategy?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter |
| Specific SAP sub-module named and applied | 2 | Module code or name used correctly in scenario context |
| Financial control or process referenced correctly | 1 | Three-way match, dunning, depreciation run, period lock, or CO reporting named and applied |
| Concrete recommendation or analysis | 1 | Specific and grounded in scenario |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, adds financial risk or GL impact | 2 | Substantive extension |
| Peer response 2: 60+ words, adds financial risk or GL impact | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario C is a problem I have seen repeatedly in real companies. They implement the financial accounting module perfectly, pass their audit, and then discover that they cannot answer the most basic management question: which part of our business is profitable? The distinction between FI (external reporting) and CO (internal management reporting) is not just academic — it is the difference between a company that can make evidence-based strategic decisions and one that is flying blind. This is exactly the kind of business intelligence gap that ERP implementations are supposed to close.
