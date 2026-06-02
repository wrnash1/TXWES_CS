# Quiz: Module 05 - Financial Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### Question 1

Which ERP module records all financial transactions and serves as the primary data source for balance sheets and income statements?

- A) Material Management (MM)
- B) General Ledger (FI-GL)
- C) Sales and Distribution (SD)
- D) Human Capital Management (HCM)

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The General Ledger is the central repository for all financial transactions; every sub-ledger (AP, AR, Asset Accounting) posts summarized journal entries to the GL, which produces the financial statements used by management and external auditors.
- *Why A is incorrect:* Materials Management tracks inventory procurement and warehouse stock; it posts goods-receipt financial events to the GL but does not contain the GL itself.
- *Why C is incorrect:* Sales and Distribution manages order-to-cash processes; billing documents post revenue to the GL, but SD is not the GL module.
- *Why D is incorrect:* Human Capital Management handles employee records and payroll; payroll costs post to the GL, but HCM is not the General Ledger module.

---

### Question 2

Which of the following best describes **asset accounting** in an ERP financial module?

- A) The process of reconciling vendor invoices against purchase orders before approving payment
- B) A module that tracks the acquisition, depreciation, and disposal of fixed assets like buildings and equipment on the balance sheet
- C) The function that allocates operating costs to internal profit centers and cost centers for management reporting
- D) The sub-ledger that manages money owed by customers and tracks collection of outstanding invoices

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In SAP, FI-AA manages fixed asset master records, calculates depreciation using configurable methods (straight-line, declining balance), and posts period-end depreciation to the GL automatically.
- *Why A is incorrect:* Reconciling vendor invoices against purchase orders describes the three-way match process in Accounts Payable (FI-AP), not asset accounting.
- *Why C is incorrect:* Allocating costs to profit centers and cost centers describes the Controlling (CO) module, not asset accounting.
- *Why D is incorrect:* Managing money owed by customers describes Accounts Receivable (FI-AR), not asset accounting.

---

### Question 3

SAP's Accounts Payable module uses a three-way match before releasing vendor payments. Which three documents are compared in this process?

- A) Customer Invoice, Sales Order, and Delivery Note
- B) Purchase Order, Goods Receipt, and Vendor Invoice
- C) Cost Center Plan, Actual Posting, and Variance Report
- D) Asset Acquisition Document, Depreciation Run, and Disposal Document

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The three-way match compares the Purchase Order (agreed price/quantity), the Goods Receipt (what was actually received), and the Vendor Invoice (what the vendor is charging) before payment is approved.
- *Why A is incorrect:* These documents belong to the Sales and Distribution (SD) order-to-cash process on the revenue side, not the procure-to-pay process in AP.
- *Why C is incorrect:* These describe CO (Controlling) variance analysis activities, not AP payment verification.
- *Why D is incorrect:* These describe the asset accounting lifecycle events, not the three-way match in Accounts Payable.

---

### Question 4

A company's financial controller needs to see which product lines and geographic regions are generating profit versus operating at a loss, using data not visible in the external General Ledger. Which ERP module provides this internal management reporting?

- A) Accounts Payable (FI-AP)
- B) Accounts Receivable (FI-AR)
- C) Controlling (CO)
- D) Asset Accounting (FI-AA)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The Controlling (CO) module allocates revenues and costs to profit centers, cost centers, and internal orders, enabling management reporting by dimension that the external GL's legal entity view cannot deliver.
- *Why A is incorrect:* Accounts Payable tracks what the company owes vendors; it does not provide product-line or regional profitability analysis.
- *Why B is incorrect:* Accounts Receivable tracks money owed by customers; it does not allocate costs and revenues to internal management dimensions.
- *Why D is incorrect:* Asset Accounting tracks fixed asset values and depreciation; it does not produce product-level or regional profit-and-loss reports.

---

### Question 5

At month-end close, an SAP finance team needs to record the decrease in value of the company's fleet of delivery vehicles for the current period. Which automated ERP process handles this?

- A) Three-way match validation in Accounts Payable
- B) Dunning run in Accounts Receivable to send overdue payment notices
- C) Depreciation run in Asset Accounting posting periodic asset value reductions to the General Ledger
- D) Payroll posting run in Human Capital Management

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* SAP's AFAB transaction (depreciation run) calculates depreciation for all active asset master records using their assigned depreciation method and posts the resulting journal entries automatically.
- *Why A is incorrect:* The three-way match is a payment approval control in AP; it does not reduce asset values on the balance sheet.
- *Why B is incorrect:* A dunning run sends payment reminders to overdue customers in AR; it has no effect on asset valuations.
- *Why D is incorrect:* A payroll posting run records employee wage costs in the GL; it does not process vehicle depreciation.

---

### Question 6

A vendor sends an invoice to Crestview Manufacturing for 300 units of raw material at $15 each ($4,500 total). The SAP system shows the corresponding Purchase Order was for 300 units at $15 each, but the Goods Receipt only recorded 250 units received. What does SAP do with this invoice?

- A) Approve the full invoice for $4,500 because the purchase order authorized that amount
- B) Block the invoice because the vendor is billing for 300 units but only 250 units were received — the quantity discrepancy prevents the three-way match from passing
- C) Automatically correct the invoice to $3,750 and post it without notifying the AP clerk
- D) Delete the invoice and create a credit memo to the vendor

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The three-way match fails because the invoice quantity (300) does not match the goods receipt quantity (250). SAP blocks the invoice and creates a work item for the AP team. The correct resolution is either to post a partial receipt for the remaining 50 units (if they arrive) or negotiate a revised invoice with the vendor.
- *Why A is incorrect:* The PO authorizes the purchase but the three-way match also requires the goods to have been physically received. Paying for undelivered goods would be an unauthorized overpayment.
- *Why C is incorrect:* SAP does not silently modify invoices; any discrepancy requires human review and resolution before payment proceeds.
- *Why D is incorrect:* Deleting the invoice and issuing a credit memo would eliminate the legitimate portion of the invoice; the correct action is to investigate the discrepancy and resolve it.

---

### Question 7

A company has just implemented SAP S/4HANA. The CFO asks why the company now needs a separate "Controlling" (CO) module if they already have the General Ledger in FI. Which response correctly explains the distinction?

- A) The CO module is only required for companies with more than 1,000 employees; smaller companies can use FI alone for all reporting
- B) FI provides legally required external financial reporting by legal entity; CO provides internal management reporting by cost center, profit center, and product line that is not visible in the external GL — both are needed for a complete financial management picture
- C) CO replaces FI entirely in SAP S/4HANA; FI is a legacy module no longer required
- D) The CO module handles accounts payable; FI handles accounts receivable — they divide the financial workload between them

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* FI and CO serve fundamentally different audiences and purposes. FI produces legally mandated external financial statements; CO provides management information for internal decisions about profitability, cost control, and budgeting by internal dimension.
- *Why A is incorrect:* CO is relevant for organizations of all sizes that need internal management reporting; there is no employee-count threshold.
- *Why C is incorrect:* FI and CO coexist in SAP S/4HANA; CO did not replace FI. In fact, SAP S/4HANA's New General Ledger integration made FI and CO even more tightly connected.
- *Why D is incorrect:* Both AP and AR are in the FI module; CO has nothing to do with payables or receivables — it handles internal cost and profitability reporting.

---

### Question 8

Which SAP module would a company use to track the cost of running a specific marketing campaign, separate from the department's general overhead costs?

- A) FI-AR — because marketing generates revenue that flows through accounts receivable
- B) CO-OPA (Internal Orders) — because an internal order tracks costs for a specific, time-bounded initiative like a campaign
- C) FI-AA — because the campaign materials are capitalized as fixed assets
- D) FI-AP — because all campaign costs are paid to external vendors through accounts payable

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Internal Orders (CO-OPA) are designed for tracking costs related to specific initiatives — marketing campaigns, small projects, maintenance jobs — that are distinct from the ongoing operational costs of a department's cost center.
- *Why A is incorrect:* FI-AR tracks customer receivables; while a campaign may generate future revenue, the cost tracking function belongs to CO, not AR.
- *Why C is incorrect:* FI-AA manages physical fixed assets; marketing campaign costs are typically operational expenses, not capitalized assets (unless specific qualifying criteria are met).
- *Why D is incorrect:* FI-AP processes the payment to vendors, but the cost object assignment (which cost center or internal order bears the cost) is determined by the CO configuration, not AP.

---

### Question 9

A customer's invoice of $12,500 is 45 days past due. The company's SAP system is configured with three dunning levels: Level 1 at 30 days overdue (reminder), Level 2 at 45 days (warning), Level 3 at 60 days (credit hold). Which SAP module and process executes the collection notice automatically?

- A) FI-AP — the automatic payment run identifies overdue invoices and generates notices
- B) FI-AR — the dunning run identifies overdue customer invoices and generates the appropriate level dunning notice based on the overdue period
- C) CO-CCA — the cost center accounting variance report flags overdue receivables
- D) FI-AA — the asset accounting module monitors payment obligations for capitalized contracts

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The dunning process is an FI-AR function. The dunning run evaluates all open customer invoices, calculates the overdue period, and applies the configured dunning level to generate the appropriate notice — Level 2 (warning) in this case.
- *Why A is incorrect:* FI-AP manages payments to vendors; it does not generate collection notices. The automatic payment run (F110) releases payments to vendors, not dunning notices to customers.
- *Why C is incorrect:* CO-CCA tracks departmental spending; it has no function related to customer payment collection.
- *Why D is incorrect:* FI-AA manages physical fixed asset accounting; it does not monitor customer payment obligations.

---

### Question 10

A fixed asset (manufacturing equipment) was purchased for $180,000 with a 10-year useful life using straight-line depreciation. After 4 years, what is the net book value of the asset?

- A) $180,000 — the original acquisition cost never changes on the balance sheet
- B) $108,000 — calculated as $180,000 minus 4 years of depreciation at $18,000/year
- C) $0 — assets are fully depreciated when placed into service under accelerated methods
- D) $144,000 — calculated as 80% of original cost after 4 years under declining balance

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Straight-line depreciation: $180,000 ÷ 10 years = $18,000 per year. After 4 years: 4 × $18,000 = $72,000 accumulated depreciation. NBV = $180,000 − $72,000 = $108,000. This is the standard straight-line calculation tested on SAP financial accounting concepts.
- *Why A is incorrect:* The acquisition cost is the gross asset value but the balance sheet also shows accumulated depreciation; the net book value decreases each period as depreciation is posted.
- *Why C is incorrect:* Full depreciation at placement describes certain accelerated tax depreciation methods; the scenario specifies straight-line over 10 years.
- *Why D is incorrect:* 80% of original cost ($144,000) corresponds to 2 years of straight-line depreciation (not 4 years), and the calculation described does not match the declining balance method formula.
