# Quiz: Module 05 - Financial Management Modules

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Which ERP module records all financial transactions and serves as the primary data source for balance sheets and income statements?

* A) Material Management (MM)
* B) General Ledger (FI-GL)
* C) Sales and Distribution (SD)
* D) Human Capital Management (HCM)

* **Correct Answer:** B) The General Ledger is the central repository that maps all accounts, balances debits and credits, and produces the financial statements used by management and external auditors.
* **Distractor Analysis:**
  * *Why B is correct:* Every sub-ledger (AP, AR, Asset Accounting) ultimately posts summarized journal entries to the General Ledger, which is the single source of truth for all financial reporting.
  * *Why A is incorrect:* Material Management tracks inventory procurement and warehouse stock; it posts goods-receipt financial events to the GL but does not contain the GL itself.
  * *Why C is incorrect:* Sales and Distribution manages order-to-cash processes; billing documents post revenue to the GL, but SD is not the GL module.
  * *Why D is incorrect:* Human Capital Management handles employee records, payroll, and HR processes; payroll costs post to the GL, but HCM is not the General Ledger module.

---

### Question 2

Which of the following best describes **asset accounting** in an ERP financial module?

* A) The process of reconciling vendor invoices against purchase orders before approving payment
* B) A module that tracks the acquisition, depreciation, and disposal of fixed assets like buildings and equipment on the balance sheet
* C) The function that allocates operating costs to internal profit centers and cost centers for management reporting
* D) The sub-ledger that manages money owed by customers and tracks collection of outstanding invoices

* **Correct Answer:** B) Asset accounting tracks the full lifecycle of fixed assets — acquisition cost, annual depreciation, net book value, and eventual disposal — ensuring accurate balance sheet valuations.
* **Distractor Analysis:**
  * *Why B is correct:* In SAP, the FI-AA (Asset Accounting) sub-module manages fixed asset master records, calculates depreciation using configurable methods (straight-line, declining balance), and posts period-end depreciation to the GL automatically.
  * *Why A is incorrect:* Reconciling vendor invoices against purchase orders describes the three-way match process in Accounts Payable (FI-AP), not asset accounting.
  * *Why C is incorrect:* Allocating costs to profit centers and cost centers describes the CO (Controlling) module, not asset accounting.
  * *Why D is incorrect:* Managing money owed by customers describes Accounts Receivable (FI-AR), not asset accounting.

---

### Question 3

SAP's Accounts Payable module uses a three-way match before releasing vendor payments. Which three documents are compared in this process?

* A) Customer Invoice, Sales Order, and Delivery Note
* B) Purchase Order, Goods Receipt, and Vendor Invoice
* C) Cost Center Plan, Actual Posting, and Variance Report
* D) Asset Acquisition Document, Depreciation Run, and Disposal Document

* **Correct Answer:** B) The three-way match compares the Purchase Order (agreed price and quantity), the Goods Receipt (what was actually received), and the Vendor Invoice (what the vendor is charging) before payment is approved.
* **Distractor Analysis:**
  * *Why B is correct:* SAP FI-AP automatically compares PO price and quantity, GR quantity, and vendor invoice amount. If differences exceed the configured tolerance, the invoice is blocked for manual review, preventing overpayment.
  * *Why A is incorrect:* These documents belong to the Sales and Distribution (SD) order-to-cash process on the revenue side, not the procure-to-pay process in AP.
  * *Why C is incorrect:* These describe CO (Controlling) variance analysis activities, not AP payment verification.
  * *Why D is incorrect:* These describe the asset accounting lifecycle events, not the three-way match used in Accounts Payable.

---

### Question 4

A company's financial controller needs to see which product lines and geographic regions are generating profit versus operating at a loss, using data not visible in the external General Ledger. Which ERP module provides this internal management reporting?

* A) Accounts Payable (FI-AP)
* B) Accounts Receivable (FI-AR)
* C) Controlling (CO)
* D) Asset Accounting (FI-AA)

* **Correct Answer:** C) The Controlling (CO) module allocates revenues and costs to profit centers, cost centers, and internal orders, enabling management reporting that is not required for external financial statements.
* **Distractor Analysis:**
  * *Why C is correct:* CO (SAP's management accounting module) provides the internal view of financial performance by dimension — product line, region, project — that the external GL's legal entity view cannot deliver.
  * *Why A is incorrect:* Accounts Payable tracks what the company owes vendors; it does not provide product-line or regional profitability analysis.
  * *Why B is incorrect:* Accounts Receivable tracks money owed by customers; it does not allocate costs and revenues to internal management dimensions.
  * *Why D is incorrect:* Asset Accounting tracks fixed asset values and depreciation; it does not produce product-level or regional profit-and-loss reports.

---

### Question 5

At month-end close, an SAP finance team needs to record the decrease in value of the company's fleet of delivery vehicles for the current period. Which automated ERP process handles this?

* A) Three-way match validation in Accounts Payable
* B) Dunning run in Accounts Receivable to send overdue payment notices
* C) Depreciation run in Asset Accounting posting periodic asset value reductions to the General Ledger
* D) Payroll posting run in Human Capital Management

* **Correct Answer:** C) The depreciation run in SAP Asset Accounting calculates and posts the periodic decrease in asset book value to the configured depreciation expense accounts in the General Ledger.
* **Distractor Analysis:**
  * *Why C is correct:* SAP's AFAB transaction (depreciation run) calculates depreciation for all active asset master records using their assigned depreciation method and posts the resulting journal entries automatically, eliminating manual spreadsheet calculations.
  * *Why A is incorrect:* The three-way match is a payment approval control in AP; it does not reduce asset values on the balance sheet.
  * *Why B is incorrect:* A dunning run sends payment reminders to overdue customers in AR; it has no effect on asset valuations.
  * *Why D is incorrect:* A payroll posting run records employee wage costs in the GL; it does not process vehicle depreciation.
