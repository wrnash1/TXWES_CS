# Quiz: Module 06 - Supply Chain Management Integrations

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

What is the function of Material Requirements Planning (MRP) in an ERP system?

* A) To design user interface screens for the procurement module
* B) To calculate what materials are needed, in what quantities, and by what dates to meet production and sales schedules
* C) To monitor database server performance metrics
* D) To compile and deploy custom ABAP programs to the ERP system

* **Correct Answer:** B) MRP uses inventory data, sales orders, and bills of materials to schedule component purchases and production orders dynamically.
* **Distractor Analysis:**
  * *Why B is correct:* MRP is a planning algorithm that nets demand against available inventory and open orders to generate procurement proposals — it is the engine that keeps supply and demand in balance.
  * *Why A is incorrect:* UI screen design is a development activity handled by the Fiori/UI team, not MRP.
  * *Why C is incorrect:* Database performance monitoring is a Basis/infrastructure task unrelated to materials planning.
  * *Why D is incorrect:* Deploying custom ABAP programs is a development and transport management activity, not a supply chain planning function.

---

### Question 2

Which of the following best describes **vendor records** in an ERP Supply Chain Management context?

* A) Records that store warehouse bin locations and storage section assignments for physical inventory
* B) Master data records containing all supplier information — name, bank account, payment terms, and tax data — required before any purchase transaction can be processed
* C) Log entries created each time a goods movement occurs in the warehouse management system
* D) Configuration tables that define the reorder point levels and safety stock quantities for each material

* **Correct Answer:** B) Vendor master records are the foundational master data required for all purchasing transactions; they store the supplier's commercial, banking, and purchasing condition data.
* **Distractor Analysis:**
  * *Why B is correct:* In SAP MM, a vendor master record (created in transaction XK01) must exist before a purchase order can reference that vendor. It stores general data, company-code data, and purchasing-organization data.
  * *Why A is incorrect:* Warehouse bin and storage section assignments are part of the Warehouse Management (WM) storage bin master, not vendor records.
  * *Why C is incorrect:* Goods movement log entries are material documents created by transactions like MIGO; they reference vendors but are not vendor master records themselves.
  * *Why D is incorrect:* Reorder points and safety stock quantities are stored in the material master (MRP views), not in vendor records.

---

### Question 3

A warehouse receives a shipment of 500 units from a vendor. Before the goods can be used in production or sold to customers, which SAP transaction records the physical arrival of inventory?

* A) MIRO — Invoice Verification, to post the vendor's bill
* B) ME21N — Create Purchase Order, to document the procurement agreement
* C) MIGO — Goods Receipt, to record the physical arrival of materials into unrestricted stock
* D) MD01 — MRP Planning Run, to recalculate future procurement needs

* **Correct Answer:** C) MIGO is the SAP transaction used to post a Goods Receipt, which records inventory entering the warehouse and triggers the financial posting to the inventory asset account.
* **Distractor Analysis:**
  * *Why C is correct:* Posting a Goods Receipt in MIGO increases stock quantity, creates a material document, and posts a financial document debiting the inventory account and crediting the GR/IR clearing account.
  * *Why A is incorrect:* MIRO processes the vendor invoice after goods are received; it comes after the goods receipt in the procure-to-pay sequence.
  * *Why B is incorrect:* ME21N creates the purchase order before goods arrive; it represents the procurement agreement, not the physical receipt of goods.
  * *Why D is incorrect:* MD01 runs the MRP planning algorithm to generate future procurement proposals; it does not record actual physical inventory movements.

---

### Question 4

An ERP system shows that safety stock for a critical component is at risk of falling below the reorder point within 5 days due to unexpectedly high production demand. Which automated SCM response should the ERP system generate?

* A) A depreciation posting to reduce the asset value of the component on the balance sheet
* B) A purchase requisition recommending procurement of additional stock to restore inventory levels above the safety threshold
* C) A three-way match variance report flagging the discrepancy between the sales order and the production plan
* D) A cost center allocation transferring the material cost to the relevant profit center

* **Correct Answer:** B) When MRP detects that projected stock will fall below the reorder point, it automatically generates a purchase requisition as a procurement proposal for the planner to review and convert to a purchase order.
* **Distractor Analysis:**
  * *Why B is correct:* MRP's core output is procurement proposals (purchase requisitions for external procurement, planned orders for internal production) that close the gap between demand and available supply.
  * *Why A is incorrect:* Asset depreciation is a financial accounting activity with no connection to inventory replenishment.
  * *Why C is incorrect:* A three-way match variance report is an AP payment control, not a supply planning response to low stock.
  * *Why D is incorrect:* Cost center allocation is a management accounting (CO) activity that assigns costs for reporting; it does not replenish physical inventory.

---

### Question 5

A manufacturing company receives components from three vendors. One vendor consistently delivers late, causing production line stoppages. Which ERP capability would help the procurement team identify and address this pattern?

* A) Asset accounting depreciation schedules tracking equipment wear on the production line
* B) Vendor evaluation scoring in the ERP system that tracks on-time delivery performance, quality rejection rates, and pricing compliance per vendor
* C) A cost center budget variance report showing overspending in the production department
* D) A General Ledger account balance report showing total payments made to each vendor

* **Correct Answer:** B) ERP vendor evaluation modules track delivery reliability, quality, and pricing performance per supplier, giving procurement teams data to renegotiate contracts, diversify supply, or qualify alternative vendors.
* **Distractor Analysis:**
  * *Why B is correct:* SAP's vendor evaluation (transaction ME61) scores vendors on criteria including on-time delivery, invoice accuracy, and quality — creating a data-driven basis for supplier management decisions.
  * *Why A is incorrect:* Asset depreciation schedules track equipment value reduction; they do not measure supplier delivery performance.
  * *Why C is incorrect:* A production cost center variance report shows budget overruns but does not identify which vendor caused the production stoppage.
  * *Why D is incorrect:* A GL account balance shows total payment amounts but does not track delivery timeliness or quality performance per vendor.
