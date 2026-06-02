# Quiz: Module 06 - Supply Chain Management Integrations

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### Question 1

What is the function of Material Requirements Planning (MRP) in an ERP system?

- A) To design user interface screens for the procurement module
- B) To calculate what materials are needed, in what quantities, and by what dates to meet production and sales schedules
- C) To monitor database server performance metrics
- D) To compile and deploy custom ABAP programs to the ERP system

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* MRP is a planning algorithm that nets demand against available inventory and open orders to generate procurement proposals — it is the engine that keeps supply and demand in balance.
- *Why A is incorrect:* UI screen design is a development activity handled by the Fiori/UI team, not MRP.
- *Why C is incorrect:* Database performance monitoring is a Basis/infrastructure task unrelated to materials planning.
- *Why D is incorrect:* Deploying custom ABAP programs is a development and transport management activity, not a supply chain planning function.

---

### Question 2

Which of the following best describes **vendor records** in an ERP Supply Chain Management context?

- A) Records that store warehouse bin locations and storage section assignments for physical inventory
- B) Master data records containing all supplier information — name, bank account, payment terms, and tax data — required before any purchase transaction can be processed
- C) Log entries created each time a goods movement occurs in the warehouse management system
- D) Configuration tables that define the reorder point levels and safety stock quantities for each material

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In SAP MM, a vendor master record must exist before a purchase order can reference that vendor. It stores general data, company-code data, and purchasing-organization data.
- *Why A is incorrect:* Warehouse bin and storage section assignments are part of the Warehouse Management storage bin master, not vendor records.
- *Why C is incorrect:* Goods movement log entries are material documents created by transactions like MIGO; they reference vendors but are not vendor master records themselves.
- *Why D is incorrect:* Reorder points and safety stock quantities are stored in the material master (MRP views), not in vendor records.

---

### Question 3

A warehouse receives a shipment of 500 units from a vendor. Before the goods can be used in production or sold to customers, which SAP transaction records the physical arrival of inventory?

- A) MIRO — Invoice Verification, to post the vendor's bill
- B) ME21N — Create Purchase Order, to document the procurement agreement
- C) MIGO — Goods Receipt, to record the physical arrival of materials into unrestricted stock
- D) MD01 — MRP Planning Run, to recalculate future procurement needs

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Posting a Goods Receipt in MIGO increases stock quantity, creates a material document, and posts a financial document debiting the inventory account and crediting the GR/IR clearing account.
- *Why A is incorrect:* MIRO processes the vendor invoice after goods are received; it comes after the goods receipt in the procure-to-pay sequence.
- *Why B is incorrect:* ME21N creates the purchase order before goods arrive; it represents the procurement agreement, not the physical receipt of goods.
- *Why D is incorrect:* MD01 runs the MRP planning algorithm to generate future procurement proposals; it does not record actual physical inventory movements.

---

### Question 4

An ERP system shows that safety stock for a critical component is at risk of falling below the reorder point within 5 days due to unexpectedly high production demand. Which automated SCM response should the ERP system generate?

- A) A depreciation posting to reduce the asset value of the component on the balance sheet
- B) A purchase requisition recommending procurement of additional stock to restore inventory levels above the safety threshold
- C) A three-way match variance report flagging the discrepancy between the sales order and the production plan
- D) A cost center allocation transferring the material cost to the relevant profit center

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* MRP's core output is procurement proposals (purchase requisitions for external procurement, planned orders for internal production) that close the gap between demand and available supply.
- *Why A is incorrect:* Asset depreciation is a financial accounting activity with no connection to inventory replenishment.
- *Why C is incorrect:* A three-way match variance report is an AP payment control, not a supply planning response to low stock.
- *Why D is incorrect:* Cost center allocation is a management accounting activity that assigns costs for reporting; it does not replenish physical inventory.

---

### Question 5

A manufacturing company receives components from three vendors. One vendor consistently delivers late, causing production line stoppages. Which ERP capability would help the procurement team identify and address this pattern?

- A) Asset accounting depreciation schedules tracking equipment wear on the production line
- B) Vendor evaluation scoring in the ERP system that tracks on-time delivery performance, quality rejection rates, and pricing compliance per vendor
- C) A cost center budget variance report showing overspending in the production department
- D) A General Ledger account balance report showing total payments made to each vendor

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* SAP's vendor evaluation (transaction ME61) scores vendors on criteria including on-time delivery, invoice accuracy, and quality — creating a data-driven basis for supplier management decisions.
- *Why A is incorrect:* Asset depreciation schedules track equipment value reduction; they do not measure supplier delivery performance.
- *Why C is incorrect:* A production cost center variance report shows budget overruns but does not identify which vendor caused the production stoppage.
- *Why D is incorrect:* A GL account balance shows total payment amounts but does not track delivery timeliness or quality performance per vendor.

---

### Question 6

In the SAP Procure-to-Pay process, what is the correct sequence of steps from demand identification to vendor payment?

- A) Purchase Order → Goods Receipt → Purchase Requisition → Invoice Verification → Payment Run
- B) Purchase Requisition → Purchase Order → Goods Receipt → Invoice Verification → Payment Run
- C) Invoice Verification → Purchase Order → Goods Receipt → Purchase Requisition → Payment Run
- D) Purchase Order → Purchase Requisition → Invoice Verification → Goods Receipt → Payment Run

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The P2P sequence is: internal requisition (PR) → external commitment (PO) → physical receipt (GR) → billing verification (MIRO) → payment (F110). Each step depends on the prior step existing in SAP.
- *Why A is incorrect:* A Purchase Requisition must exist before a Purchase Order can be created; the order shown reverses this dependency.
- *Why C is incorrect:* Invoice Verification cannot occur before the goods are received; SAP's three-way match requires both the PO and GR to already exist.
- *Why D is incorrect:* A Purchase Requisition is the internal authorization step that precedes the Purchase Order; creating the PO before the PR is not the standard SAP P2P workflow.

---

### Question 7

A company receives 200 units of raw material at $15 per unit using the **Moving Average Price** valuation method. Before this receipt, they held 100 units at a moving average of $12 each. What is the new Moving Average Price per unit after the goods receipt is posted?

- A) $12.00 — the existing average is not affected by new receipts
- B) $13.50 — calculated as the simple average of $12 and $15
- C) $14.00 — calculated as the weighted average: (100 × $12 + 200 × $15) ÷ 300
- D) $15.00 — the new receipt price replaces the old average entirely

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Moving Average Price is a weighted average: (existing stock value + new receipt value) ÷ total units. (100 × $12 + 200 × $15) ÷ 300 = ($1,200 + $3,000) ÷ 300 = $4,200 ÷ 300 = $14.00.
- *Why A is incorrect:* Moving Average Price recalculates with every goods receipt; it does not remain fixed at the prior average.
- *Why B is incorrect:* A simple average of the two prices ($12 + $15) ÷ 2 = $13.50 ignores the difference in quantities; the weighted average is required.
- *Why D is incorrect:* Replacing the prior average with the new price describes Standard Price behavior, not Moving Average Price.

---

### Question 8

Which SAP goods movement type is used when finished goods are issued to a customer as part of a sales delivery, and what is the financial posting?

- A) Movement type 101 — Debit GR/IR Clearing, Credit Inventory
- B) Movement type 261 — Debit WIP/Production, Credit Inventory
- C) Movement type 551 — Debit Scrap Expense, Credit Inventory
- D) Movement type 601 — Debit Cost of Goods Sold, Credit Inventory

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* Movement type 601 is the Goods Issue for a customer delivery triggered by the SD module. It reduces finished goods inventory and posts the cost of the delivered goods to the COGS account on the income statement.
- *Why A is incorrect:* Movement type 101 is a Goods Receipt for a Purchase Order; it increases inventory and is used when receiving from a vendor, not issuing to a customer.
- *Why B is incorrect:* Movement type 261 issues materials to a production order — it records components consumed in manufacturing, not finished goods shipped to a customer.
- *Why C is incorrect:* Movement type 551 is a scrap write-off for damaged or defective materials; it has no connection to customer deliveries.

---

### Question 9

MRP generates procurement proposals after a planning run. What is the correct description of an MRP output, and what must happen before those proposals become firm purchase orders?

- A) MRP automatically creates approved purchase orders and sends them to vendors without human review
- B) MRP generates purchase requisitions and planned orders that a human materials planner reviews, adjusts if needed, and converts to purchase orders or production orders
- C) MRP generates vendor invoices that the AP team must verify before procurement can begin
- D) MRP updates the General Ledger directly with the projected cost of future procurement

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* MRP outputs are proposals, not firm commitments. The planner reviews the proposals for feasibility, applies judgment about minimum order quantities or supplier constraints, and manually converts acceptable proposals to executable orders.
- *Why A is incorrect:* Fully automated PO creation without human review describes autonomous procurement, an advanced pattern beyond standard MRP. Standard MRP always produces proposals requiring planner review.
- *Why C is incorrect:* MRP produces procurement proposals — purchase requisitions and planned orders — not vendor invoices. Invoices are created by vendors after goods are shipped.
- *Why D is incorrect:* MRP is a planning tool that generates logistics proposals; it does not post financial entries to the General Ledger. GL postings occur when actual goods receipts and invoices are processed.

---

### Question 10

A sales order is entered in the SAP SD module for 500 finished assemblies. No finished goods are in stock. Describe the correct sequence of cross-module events that SAP triggers to fulfill this order, naming the modules involved.

- A) SD creates the sales order → MM-MRP calculates the shortage → MM-PUR creates a purchase requisition → PP creates a production order → MM-IM records goods issue to the production order → SD posts the customer delivery
- B) FI posts a revenue accrual → SD creates the billing document → MM issues the materials → PP starts production without a production order
- C) SD creates the sales order → FI posts the revenue → MM receives raw materials → SD ships the goods without production involvement
- D) PP creates the production order first → SD enters the sales order after production completes → MM records the goods receipt

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* This is the standard Make-to-Order integration chain in SAP: the SD sales order creates demand visible to MRP (MM), which generates a purchase requisition for components and a planned production order (PP). Once components are received and issued to production (MM-IM), the finished goods are delivered against the SD order.
- *Why B is incorrect:* Revenue should not be recognized before goods are delivered; posting revenue at order entry violates accrual accounting principles. Additionally, production cannot be skipped for manufactured goods.
- *Why C is incorrect:* This sequence omits the production planning step entirely. For manufactured goods, PP must create and execute a production order before finished goods exist to ship.
- *Why D is incorrect:* In a customer-demand-driven environment, the sales order must exist before production begins. Starting production before a customer order exists describes Make-to-Stock planning, not Make-to-Order, and the sequence described is reversed.
