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

---

### Question 11

(5 points)

A material master record in SAP MM contains multiple views. Which view stores the MRP type, reorder point, safety stock level, and lot size parameters used by the planning run?

- A) Sales view — because MRP planning data flows from customer orders
- B) Accounting view — because inventory value and valuation class are stored there
- C) MRP view — because all planning-relevant parameters for the material are configured in the MRP tabs of the material master
- D) Warehouse Management view — because safety stock and bin locations are managed together

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* SAP material master records have multiple views (tabs), each serving a different module. The MRP views (MRP 1–4) store all planning-relevant parameters: MRP type (reorder point, MRP, consumption-based), lot-sizing procedure, reorder point quantity, safety stock, and planned delivery time.
  - *Why A is incorrect:* The Sales views store customer-facing data like sales unit, delivering plant, and delivery tolerances — not MRP planning parameters.
  - *Why B is incorrect:* The Accounting view stores the valuation class and inventory price (standard or moving average); it does not contain MRP planning parameters.
  - *Why D is incorrect:* Warehouse Management views store warehouse-specific data like bin type and special movement indicators; safety stock is an MRP parameter stored in the MRP views.

---

### Question 12

(5 points)

A company uses **Standard Price** valuation for a raw material. The standard price is $50/unit. A new shipment arrives at an actual purchase price of $58/unit. How does SAP record this goods receipt?

- A) SAP records the inventory at $58 and updates the standard price to $58 for all future receipts
- B) SAP records the inventory at $50 (standard price) and posts the $8/unit difference to a price variance account
- C) SAP blocks the goods receipt until the purchase order price is corrected to match the standard price
- D) SAP averages $50 and $58 and updates the inventory value to $54/unit

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* With Standard Price valuation (price indicator "S"), inventory is always recorded at the predetermined standard price. Any difference between actual purchase price and standard price is posted to a Price Difference account, enabling variance analysis.
  - *Why A is incorrect:* Standard Price does not self-update from goods receipts; the standard price can only be changed through a deliberate price update transaction (MR21), not automatically.
  - *Why C is incorrect:* SAP does not block goods receipts due to price discrepancies with standard price; the discrepancy is simply posted to the variance account.
  - *Why D is incorrect:* Averaging the standard price with the actual price describes behavior closer to Moving Average Price valuation, not Standard Price valuation.

---

### Question 13

(5 points)

In SAP Supply Chain Management, what is the purpose of the **GR/IR clearing account**?

- A) It is the cost center account used to allocate goods receipt costs to the appropriate department
- B) It is a balance sheet clearing account that records the obligation to pay for goods received but not yet invoiced, and is cleared when the matching vendor invoice is posted
- C) It is the General Ledger account that stores cumulative purchase order values for budget control
- D) It is a vendor-specific account that tracks all open purchase orders for each supplier

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The GR/IR (Goods Receipt / Invoice Receipt) clearing account bridges the timing difference between receiving goods (which creates a debit to inventory and credit to GR/IR) and receiving the vendor invoice (which debits GR/IR and credits vendor payable). At month-end, any non-zero balance represents goods received but not yet invoiced, or invoices received without a corresponding goods receipt.
  - *Why A is incorrect:* Cost center allocation is a CO function; the GR/IR account is an FI clearing account, not a CO cost allocation vehicle.
  - *Why C is incorrect:* Cumulative purchase order budget tracking is handled through commitment management in SAP, not the GR/IR clearing account.
  - *Why D is incorrect:* Vendor-specific balances are tracked in the vendor sub-ledger (FI-AP); the GR/IR account is a balance sheet clearing account, not a vendor account.

---

### Question 14

(5 points)

A distribution company wants to minimize inventory holding costs while ensuring they never run out of their top-selling product during the 14-day supplier lead time. Which two SAP MRP parameters most directly address this requirement?

- A) Standard Price and Moving Average Price
- B) Safety Stock and Planned Delivery Time
- C) Vendor Evaluation Score and Payment Terms
- D) Goods Issue movement type and delivery confirmation

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Safety Stock sets the minimum inventory buffer that triggers replenishment before a stockout occurs. Planned Delivery Time tells MRP how many days to expect between creating a purchase order and receiving the goods, ensuring orders are placed far enough in advance to maintain the safety buffer during the lead time.
  - *Why A is incorrect:* Standard Price and Moving Average Price are inventory valuation methods that affect financial reporting, not stock level planning or replenishment timing.
  - *Why C is incorrect:* Vendor evaluation scores and payment terms are procurement management parameters; they do not directly control when MRP triggers replenishment proposals.
  - *Why D is incorrect:* Goods issue movement type determines how stock reductions are posted financially; delivery confirmation is an operational logistics step. Neither directly controls safety stock levels or replenishment lead time calculations.

---

### Question 15

(5 points)

Which SAP module integration is triggered when a finished goods delivery is posted for a customer order in the SD module?

- A) SD posts to FI-AP, creating a vendor payment obligation for the customer order
- B) SD triggers MM-IM Goods Issue (movement type 601), reducing finished goods inventory and creating a COGS posting in FI
- C) SD triggers PP to start a new production order for the delivered quantity to replenish stock
- D) SD posts to CO-CCA, allocating the delivery cost to the shipping department cost center

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Posting a customer delivery in SD triggers movement type 601 in MM-IM, which reduces the finished goods inventory balance and creates the cost of goods sold (COGS) journal entry in FI — the classic SD-MM-FI integration chain.
  - *Why A is incorrect:* FI-AP is the vendor payables module; a customer delivery creates a receivable (FI-AR), not a payable.
  - *Why C is incorrect:* MRP-driven replenishment is triggered by the sales order demand (not the delivery posting), and even then it generates a planned order for human review — not an automatic new production order.
  - *Why D is incorrect:* While shipping costs may be allocated to a cost center in CO, the primary financial impact of a goods issue is the inventory reduction and COGS posting in MM-IM and FI, not a cost center allocation.

---

### Question 16

(5 points)

What distinguishes **Make-to-Order (MTO)** production planning from **Make-to-Stock (MTS)** in SAP?

- A) MTO produces goods in advance of customer orders and stores them in finished goods inventory; MTS produces only in direct response to individual customer orders
- B) MTO links each production order directly to a specific customer sales order, with costs and stock tracked at the sales order level; MTS produces to replenish generic finished goods stock without a specific customer assignment
- C) MTO is used only for services, not physical goods; MTS is used only for discrete manufacturing
- D) MTO requires a purchase order from the vendor; MTS requires a production order from the plant

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In Make-to-Order, each production order is a direct response to a specific sales order, and finished goods are earmarked for that customer. Cost tracking and special stock handling differ from MTS. In Make-to-Stock, production fills generic finished goods inventory that can be consumed by any future customer order.
  - *Why A is incorrect:* This reverses the definitions. MTS produces in advance of orders; MTO produces in response to orders.
  - *Why C is incorrect:* Both MTO and MTS apply to physical manufactured goods. Services typically use different planning strategies entirely.
  - *Why D is incorrect:* Both MTO and MTS can involve purchase orders for components; the distinction is about whether production is tied to a specific customer order, not about purchasing behavior.

---

### Question 17

(5 points)

A procurement manager wants to automatically generate a purchase order every time a purchase requisition is created and has been approved. Which SAP functionality enables this automatic PO creation?

- A) MIGO automatic release
- B) Source List with automatic purchase order creation flag enabled in the material and vendor master
- C) MRP automatic payment run
- D) MIRO automatic three-way match bypass

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* SAP supports automatic PO creation from approved purchase requisitions when a source list entry exists for the material/vendor combination and the automatic PO creation indicator is set. This reduces manual effort in high-volume, low-risk procurement scenarios.
  - *Why A is incorrect:* MIGO is the goods receipt transaction; it does not have a function for automatically creating purchase orders from requisitions.
  - *Why C is incorrect:* The MRP payment run does not exist as an SAP transaction; F110 is the AP payment run, and it processes vendor payments, not procurement document creation.
  - *Why D is incorrect:* MIRO is used for invoice verification; there is no "automatic bypass" of the three-way match — bypassing it would eliminate a critical financial control.

---

### Question 18

(5 points)

A company has 90 days of raw material inventory on hand but only 7 days of sales demand to cover. Which supply chain performance metric would flag this situation, and what business problem does it indicate?

- A) On-Time Delivery Rate — indicates the supplier is delivering too early
- B) Days Inventory Outstanding (DIO) — an extremely high DIO indicates excess cash tied up in inventory, increasing carrying costs and risk of obsolescence
- C) Fill Rate — indicates that 83 days of inventory cannot be matched to customer orders
- D) Purchase Order Cycle Time — indicates the procurement team is creating orders too frequently

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Days Inventory Outstanding (also called Days of Inventory on Hand) measures how long inventory sits before being consumed. A DIO of 90 days when sales demand is 7 days indicates dramatically over-purchased inventory — tying up working capital, increasing warehouse costs, and creating obsolescence risk.
  - *Why A is incorrect:* On-Time Delivery Rate measures whether suppliers deliver on the promised date, not inventory levels relative to demand.
  - *Why C is incorrect:* Fill Rate measures the percentage of customer orders fulfilled from available stock; it does not directly measure excess inventory levels.
  - *Why D is incorrect:* Purchase Order Cycle Time measures how long it takes to create and send a purchase order; it does not measure inventory excess relative to demand.

---

### Question 19

(5 points)

In SAP Materials Management, which document type is created when a company confirms that goods ordered on a purchase order have physically arrived at the warehouse?

- A) Purchase Requisition
- B) Purchase Order
- C) Material Document (Goods Receipt)
- D) Vendor Invoice Document

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* A Material Document (created by MIGO transaction, movement type 101) is the SAP record of goods physically received. It updates inventory quantity, creates the GR/IR clearing account entry, and triggers a corresponding FI accounting document.
  - *Why A is incorrect:* A Purchase Requisition is created before the purchase order as an internal request to procure; it precedes the physical receipt of goods.
  - *Why B is incorrect:* A Purchase Order is the legal commitment to the vendor; it is created before goods arrive, not at the time of receipt.
  - *Why D is incorrect:* A Vendor Invoice Document (created by MIRO) is posted when the vendor's bill arrives; it comes after the goods receipt in the P2P sequence.

---

### Question 20

(5 points)

A company's ERP system has reorder point planning configured for a component. The reorder point is set at 200 units. Current stock is 180 units, with an open purchase order for 300 units already confirmed. Should MRP generate a new purchase requisition?

- A) Yes — current stock (180) is below the reorder point (200), so MRP always generates a new requisition regardless of existing open purchase orders
- B) No — MRP considers available stock plus open purchase orders (180 + 300 = 480 units), which exceeds the reorder point, so no additional procurement is needed
- C) Yes — MRP ignores open purchase orders when calculating net requirements
- D) No — once a reorder point is set, MRP never generates new requisitions until the open PO is received

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* SAP MRP calculates net requirements by netting current stock plus open purchase orders and production orders against demand. With 180 on hand and 300 on order, total available = 480 — well above the 200 reorder point. No new procurement proposal is needed.
  - *Why A is incorrect:* MRP does not ignore existing open orders; considering all supply-side commitments is a core MRP calculation principle.
  - *Why C is incorrect:* Ignoring open purchase orders would create duplicate procurement and excess inventory — the opposite of MRP's purpose. MRP always includes all planned and confirmed supply orders in its calculation.
  - *Why D is incorrect:* Having an open PO does not permanently disable MRP planning. MRP continuously recalculates and would generate a new proposal if stock fell below requirements after the open PO is received and consumed.
