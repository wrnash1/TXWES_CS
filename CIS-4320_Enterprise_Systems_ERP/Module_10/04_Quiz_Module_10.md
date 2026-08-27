# Quiz: Module 10 — SAP Materials Management (MM Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

### Question 1

In SAP MM, which organizational unit represents a physical location — such as a factory, warehouse, or distribution center — where materials are produced, stored, or distributed, and to which all inventory balances are assigned?

- A) Purchasing Organization — the unit that negotiates vendor contracts and manages purchasing conditions
- B) Storage Location — the physical bin area within the larger facility
- C) Plant — the central MM organizational unit representing a physical production or storage location
- D) Company Code — the legal entity that owns all financial transactions

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The Plant is the central operational unit in SAP MM. Every inventory balance, purchase order, production order, and goods movement belongs to a specific Plant. A Plant is always assigned to exactly one Company Code.
- *Why A is incorrect:* The Purchasing Organization manages vendor relationships and negotiations. It is a procurement unit, not a physical location, and does not hold inventory balances.
- *Why B is incorrect:* A Storage Location is a subdivision within a Plant — a specific warehouse area or bin location. Stock quantities are tracked at the Plant/Storage Location level, but the Storage Location cannot exist independently of a Plant.
- *Why D is incorrect:* Company Code is the SAP FI legal entity unit. It is the financial parent of one or more Plants but does not itself represent a physical operational location.

---

### Question 2

A purchasing agent at a manufacturing company creates a document in SAP requesting that 1,000 units of steel rod be ordered from a vendor, specifying the quantity needed, the required delivery date, and the cost center to charge. This document has no legal standing with the vendor and requires approval before any commitment is made. Which SAP MM document is this?

- A) Purchase Order — the legally binding commitment to purchase from the vendor
- B) Purchase Requisition — the internal request document that initiates the procurement process
- C) Vendor Invoice — the vendor's billing document requesting payment
- D) Goods Receipt — the record of materials physically received from the vendor

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A Purchase Requisition (ME51N) is an internal document — it expresses a need to purchase but has no legal effect on the vendor. It must be approved and then converted into a Purchase Order before any vendor commitment is made.
- *Why A is incorrect:* A Purchase Order (ME21N) is the legally binding commitment to a specific vendor. It includes vendor name, price, and delivery terms — information that a Purchase Requisition does not contain. A PO is created after the PR is approved.
- *Why C is incorrect:* A Vendor Invoice is received from the vendor after goods are delivered. It is the vendor's request for payment — it comes after both the PO and the GR in the P2P cycle.
- *Why D is incorrect:* A Goods Receipt (MIGO) is posted when physical delivery occurs. It creates a stock entry and an accounting document — it is an operational confirmation, not a request to purchase.

---

### Question 3

When a Goods Receipt is posted in SAP MM using transaction MIGO with Movement Type 101, which accounting entry does SAP automatically generate?

- A) Debit Accounts Payable / Credit Bank Account
- B) Debit GR/IR Clearing Account / Credit Inventory Account
- C) Debit Inventory Account / Credit GR/IR Clearing Account
- D) Debit Expense Account / Credit Accounts Payable

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* When goods are received, inventory increases (Debit Inventory) and an obligation to pay is recognized through the GR/IR Clearing Account (Credit GR/IR). The GR/IR is a balance sheet liability that sits between the goods receipt and the vendor invoice. SAP determines the inventory account automatically from the Material Master Valuation Class.
- *Why A is incorrect:* Debit AP / Credit Bank describes a vendor payment posting (F110). Payment occurs much later in the P2P cycle — after the invoice has been posted and is due.
- *Why B is incorrect:* This entry reverses the correct direction. At GR, inventory increases (debit) and GR/IR is credited as an obligation. Debiting GR/IR at GR would reverse the logic of the clearing account.
- *Why D is incorrect:* Debit Expense / Credit AP describes a service invoice posting or an expense that is consumed immediately. For a stock material goods receipt, inventory (an asset) is debited, not an expense — the expense occurs later when the material is consumed (Goods Issue).

---

### Question 4

A vendor sends an invoice for 500 units at $52.00 each ($26,000 total). The Purchase Order specified 500 units at $50.00 each ($25,000 total). The Goods Receipt confirmed all 500 units were received. When the AP team posts this invoice in MIRO, what happens?

- A) MIRO posts the invoice for $25,000 (the PO amount) and ignores the extra $1,000 automatically
- B) MIRO detects a price variance of $1,000 and posts the GR/IR at PO price, Accounts Payable at invoice price, and the $1,000 difference to a Price Difference account
- C) MIRO rejects the invoice entirely and requires a new PO to be created at the higher price before any posting can occur
- D) MIRO posts the invoice for $26,000 and automatically updates the PO price to $52.00 for future orders

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* MIRO's three-way match detects the $1,000 price difference. The GR/IR account is debited for the PO-price value ($25,000) to clear the GR obligation. Accounts Payable is credited for the full invoice amount ($26,000). The $1,000 difference posts to a Price Difference or variance account. Depending on tolerance configuration, the invoice may post automatically or be blocked for manual review.
- *Why A is incorrect:* SAP does not silently ignore price differences. Every dollar must be accounted for under the double-entry principle. MIRO captures the variance and posts it to the correct account.
- *Why C is incorrect:* MIRO does not reject invoices that differ from the PO price — it posts the variance. A new PO is not required. The resolution might involve a PO price change (ME22N) or accepting the variance, but the invoice is not rejected outright.
- *Why D is incorrect:* MIRO does not automatically update the PO price. Purchase Order prices are changed only by the buyer using ME22N after an explicit decision. Automatic price updates from invoices would bypass procurement controls.

---

### Question 5

The GR/IR Clearing Account in SAP MM serves as a temporary holding account between two events. Which two events does it bridge, and what is the expected balance of this account when both events are complete for a given purchase?

- A) It bridges the Purchase Requisition and the Purchase Order; the balance should equal the total PO value outstanding
- B) It bridges the Goods Receipt and the Invoice Verification; the balance should be zero when both events are posted for the same quantity and value
- C) It bridges the Vendor Payment and the Bank Transfer; the balance should equal the total payments awaiting bank confirmation
- D) It bridges the Material Issue and the Production Order; the balance should equal the cost of materials consumed in production

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* GR/IR is credited at the Goods Receipt (obligation created: goods received but not yet invoiced) and debited at Invoice Verification (MIRO). When both events are posted for the same quantity and value, the GR/IR nets to zero. An open GR/IR balance indicates either a GR without a matching invoice (accrued liability) or an invoice without a matching GR.
- *Why A is incorrect:* The GR/IR account is not involved in Purchase Requisitions or Purchase Orders. PRs and POs create commitment records but generate no financial postings until goods are physically received.
- *Why C is incorrect:* The account bridging vendor payments and bank transfers is the Payment Clearing account used in FI-AP — not the GR/IR account. GR/IR is purely a procurement-to-invoice bridge.
- *Why D is incorrect:* The accounting entry for materials issued to a Production Order involves debiting a production cost account and crediting Inventory — no GR/IR account is involved in goods issues.

---

### Question 6

Which SAP MM transaction code is used to post all types of inventory movements — including Goods Receipts for Purchase Orders, Goods Issues to production orders, and transfer postings between storage locations?

- A) ME21N — Create Purchase Order
- B) MIRO — Logistics Invoice Verification
- C) MB52 — Warehouse Stocks of Material
- D) MIGO — Goods Movement

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* MIGO is the universal goods movement transaction in SAP MM. It handles all inventory movements through the selection of the appropriate Movement Type: 101 (GR for PO), 201 (GI to Cost Center), 261 (GI to Production Order), 301 (Plant Transfer), and many others.
- *Why A is incorrect:* ME21N creates Purchase Orders — it is a procurement document transaction, not a goods movement transaction. Creating a PO does not update inventory.
- *Why B is incorrect:* MIRO posts vendor invoices using three-way match logic. It creates an accounting document (GR/IR and AP) but does not move physical stock or update inventory quantities.
- *Why C is incorrect:* MB52 is a reporting transaction that displays current warehouse stock levels by material and storage location. It is read-only and does not post any movements.

---

### Question 7

A Material Master record has Price Control set to "V" (Moving Average Price). The current moving average price is $100.00 per unit and there are 200 units in stock. The company receives a new shipment of 100 units at an actual purchase price of $112.00 per unit. What is the new moving average price after this goods receipt?

- A) $100.00 — the moving average price does not change until a physical inventory count is conducted
- B) $112.00 — the new price always replaces the old price with moving average pricing
- C) $104.00 — calculated as total value divided by total quantity after the new receipt
- D) $106.00 — the average of the old price ($100) and the new price ($112)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Moving Average Price = (Existing stock value + New receipt value) / (Existing quantity + New quantity). Existing value: 200 units × $100 = $20,000. New receipt value: 100 units × $112 = $11,200. Total value: $31,200. Total quantity: 300 units. New MAP = $31,200 / 300 = $104.00.
- *Why A is incorrect:* Moving Average Price is recalculated automatically with every goods receipt in SAP — no physical count is required. That is the defining characteristic of price control V.
- *Why B is incorrect:* Moving Average Price is a weighted average of all receipts, not a replacement of the old price. Simply replacing with the new price would ignore the value already in stock.
- *Why D is incorrect:* A simple average of $100 and $112 = $106 ignores the quantity weights. The correct calculation must weight each price by the quantity it represents.

---

### Question 8

A company purchases IT equipment (laptops) for direct consumption by employees — the laptops will never enter warehouse stock. The buyer creates a Purchase Order in SAP MM. Which Account Assignment Category should be used on the PO line item?

- A) No account assignment — stock items do not require an account assignment category
- B) K — Account Assignment to Cost Center, so the expense is charged directly to the department's cost center at goods receipt
- C) M — Account Assignment to Project, so the laptop cost is capitalized as a project asset
- D) A — Account Assignment to Fixed Asset, only valid for items that depreciate over 10+ years

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Account Assignment Category K (Cost Center) is used when goods are purchased for direct consumption — not into stock. At goods receipt, the expense posts directly to the specified cost center rather than to an inventory account. This is correct for IT equipment, office supplies, and maintenance items consumed directly by a department.
- *Why A is incorrect:* "No account assignment" means the item is received into stock (inventory). Since these laptops are going directly to employees and not into a warehouse, they should not be received into stock.
- *Why C is incorrect:* Account Assignment M is used for project-related purchases charged to a WBS element in the Project System module. IT laptops for general employee use are typically an operating expense, not a project cost.
- *Why D is incorrect:* Account Assignment A (Fixed Asset) is used when purchasing items that will be capitalized as fixed assets and depreciated over their useful life. While some high-value laptops may be capitalized as assets, the scenario specifies direct consumption — making K (Cost Center) the more appropriate answer.

---

### Question 9

The three-way match in SAP MM invoice verification (MIRO) compares which three documents?

- A) Purchase Requisition, Purchase Order, and Vendor Master
- B) Purchase Order, Goods Receipt, and Vendor Invoice
- C) Material Master, Vendor Master, and Purchase Order
- D) Goods Receipt, Payment Run, and Bank Statement

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Three-way match verifies that: (1) the vendor invoice price and terms match the Purchase Order, (2) the vendor invoice quantity does not exceed the Goods Receipt quantity. This three-way check — PO, GR, Invoice — is the core AP control in a procurement-integrated environment. MIRO enforces this automatically.
- *Why A is incorrect:* The Purchase Requisition is an internal document with no vendor-facing legal standing. It is not part of the three-way match. The Vendor Master provides vendor data but is not a transactional document matched against the invoice.
- *Why C is incorrect:* Material Master and Vendor Master are configuration and reference data — they are not transactional documents compared in the invoice matching process. The three-way match involves three transactional events, not master data records.
- *Why D is incorrect:* Payment Run (F110) and Bank Statement (FEBAN) are FI payment processes that happen after the invoice is already posted and approved. They are not part of the three-way match validation.

---

### Question 10

A materials controller reviews the open GR/IR Clearing Account balance at month-end and finds $180,000 in credits with no matching debits. What does this balance indicate, and what action should the controller take?

- A) $180,000 in vendor invoices have been posted but no goods have been received — the invoices must be reversed immediately
- B) $180,000 in goods have been received but the corresponding vendor invoices have not yet been posted — this is an accrued liability that should be reviewed and accrued in the financial statements
- C) $180,000 in payments have been made but the bank has not yet cleared them — no action is needed until the next bank statement
- D) $180,000 of inventory has been issued to production orders but the production orders have not yet been confirmed — the production team must confirm their orders

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A credit balance in GR/IR means goods have been received (GR posted = credit to GR/IR) but the vendor invoices have not yet arrived or been posted (no debit to clear the GR/IR). This is a normal month-end situation for in-transit invoices. The controller should review the open items, confirm the goods were legitimately received, and accrue the liability in the financial statements if the period is closing.
- *Why A is incorrect:* This describes the opposite scenario — a debit balance in GR/IR (invoices posted, no GR). A credit balance in GR/IR means the GR was posted first and the invoice has not yet followed.
- *Why C is incorrect:* Uncleared bank payments are tracked in the FI Bank Accounting sub-module through bank clearing accounts — not in the GR/IR account. The GR/IR account is strictly a procurement-to-invoice bridge.
- *Why D is incorrect:* Goods issues to production orders post to production cost accounts and inventory — not to the GR/IR account. Production order confirmation is a PP module activity unrelated to GR/IR balance management.

---

### Question 11

A purchasing manager creates a Purchase Order in SAP using transaction ME21N for 200 laptop computers. Which MM document type is most appropriate for this standard external procurement of stock materials from a vendor?

- A) NB — Standard Purchase Order, used for one-time external procurement of goods or services from a vendor
- B) UB — Stock Transport Order, used to transfer materials between two plants within the same company
- C) FO — Framework Order, used for blanket agreements with an open value or quantity over a period of time
- D) RFQ — Request for Quotation, used to solicit pricing from potential vendors before committing to a purchase

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Document type NB (Normal Order) is the standard Purchase Order type in SAP MM for external procurement. It commits the company to purchase a specific quantity at a specific price from a named vendor and triggers the full P2P cycle: GR, invoice verification, and payment.
- *Why B is incorrect:* UB (Stock Transport Order) is an inter-plant transfer document — it moves stock between two SAP plants using Movement Type 351/101. No vendor is involved and no vendor invoice is expected.
- *Why C is incorrect:* FO (Framework Order) is used for blanket purchasing agreements where a total value is agreed upfront and individual releases are drawn against it over time. It is not used for a one-time discrete quantity purchase.
- *Why D is incorrect:* An RFQ (transaction ME41) is a pre-purchase document that requests pricing from vendors. It has no legal commitment and does not trigger goods receipt or payment — it must be converted into a Purchase Order after vendor selection.

---

### Question 12

A company uses standard price control (Price Control "S") for a finished goods material. The standard price is set at $200.00 per unit. The company receives 50 units from production at an actual cost of $195.00 per unit. What accounting entry does SAP generate at Goods Receipt, and where does the cost difference go?

- A) Debit Inventory $10,000 / Credit GR/IR $10,000 — no variance because standard price absorbs all cost differences
- B) Debit Inventory $9,750 / Credit Price Difference $9,750 — actual cost is used because SAP always values GR at actual cost
- C) Debit Inventory $10,000 (at standard price) / Credit Production Cost Account $9,750 / Credit Price Difference Account $250 — the $250 favorable variance posts to a price difference account
- D) Debit Inventory $10,000 (at standard price) / Credit Stock Account $9,750 / Debit Price Difference Account $250 — the $250 favorable variance reduces the inventory value immediately

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* With Price Control "S," inventory is always valued at the standard price regardless of actual cost. The 50 units enter stock at 50 × $200 = $10,000. The production order actual cost was 50 × $195 = $9,750. The $250 favorable variance (standard > actual) posts to a Price Difference account. This allows cost controllers to monitor production efficiency variances.
- *Why A is incorrect:* Standard price does not "absorb" cost differences silently — the variance is explicitly posted to a Price Difference account and is visible in cost center and product cost reporting.
- *Why B is incorrect:* Moving Average Price (Price Control "V") values GR at actual cost. Standard Price ("S") always uses the frozen standard, regardless of actual receipts.
- *Why D is incorrect:* With standard price, the inventory account is debited at standard price and the offset credits the production cost account at actual cost. A favorable variance is a credit to Price Difference, not a debit that reduces inventory.

---

### Question 13

A procurement team is setting up a new material in SAP. They need to maintain purchasing-specific data such as the purchasing group responsible, planned delivery time, and vendor-specific order unit. Which Material Master organizational view contains this data?

- A) Basic Data 1 — contains the material description, base unit of measure, and material group
- B) Purchasing view — contains purchasing-relevant data including purchasing group, order unit, and GR processing time
- C) MRP 1 view — contains MRP type, lot-size procedure, and reorder point for demand planning
- D) Accounting 1 view — contains price control, standard price, and valuation class for financial integration

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The Purchasing view (organizational level: Plant) stores all procurement-relevant configuration for a material: responsible purchasing group, planned delivery time, minimum order quantity, order unit, and GR processing time. This data drives how the system creates and processes purchase orders for this material.
- *Why A is incorrect:* Basic Data 1 holds general descriptive data that is valid across all organizational levels — material description, base unit of measure, division, and material group. It contains no purchasing-specific fields.
- *Why C is incorrect:* MRP 1 contains planning parameters — MRP type (e.g., MRP, consumption-based), lot-size procedure, reorder point, and safety stock. These drive automatic procurement proposals but are not the purchasing configuration view.
- *Why D is incorrect:* Accounting 1 holds financial valuation data — price control (S or V), current standard or moving average price, and valuation class. Valuation class links the material to the G/L accounts used in automatic account determination.

---

### Question 14

An SAP vendor master record for a supplier contains data at three organizational levels. An accounts payable clerk needs to maintain the vendor's payment terms, bank account details, and reconciliation account. Which organizational level of the vendor master contains this financial accounting data?

- A) Client level — general data such as vendor name, address, and communication details valid across the entire SAP system
- B) Company Code level — accounting-relevant data including reconciliation account, payment terms, and bank details, valid per legal entity
- C) Purchasing Organization level — procurement-relevant data including incoterms, order currency, and pricing conditions
- D) Plant level — inventory and logistics data specific to a receiving plant

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The Company Code segment of the vendor master stores all FI-AP-relevant data: the reconciliation account (which links the vendor sub-ledger to the G/L), payment terms, payment methods, dunning data, and bank account details. This data is maintained separately per Company Code so that a multinational vendor can have different payment arrangements with each legal entity.
- *Why A is incorrect:* Client-level (General Data) contains vendor name, search terms, address, telephone, and tax numbers — data that is the same regardless of which company code or purchasing organization is using the vendor.
- *Why C is incorrect:* The Purchasing Organization segment stores procurement-specific terms: order currency, incoterms, minimum order value, and schema group for pricing conditions. This data is not used by accounts payable for payment processing.
- *Why D is incorrect:* The vendor master does not have a Plant-level segment. Plant-level vendor relationships are managed through info records (ME11), not the vendor master itself.

---

### Question 15

A company has implemented the three-way match in SAP MIRO. The Purchase Order specifies 100 units at $50.00 each. The Goods Receipt confirms 80 units received. The vendor submits an invoice for 100 units at $50.00. When the AP team posts the invoice in MIRO, what will most likely happen?

- A) MIRO posts the full invoice of $5,000 because the PO was created for 100 units
- B) MIRO posts $4,000 and automatically creates a credit memo to the vendor for the remaining $1,000
- C) MIRO detects a quantity variance: only 80 units were received, so the invoice is blocked for the 20-unit overbill ($1,000) pending a further goods receipt or invoice reduction
- D) MIRO rejects the entire invoice and requires the vendor to resubmit for 80 units only

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Three-way match compares invoice quantity against the GR quantity. Since only 80 units have been received and the vendor is billing for 100, MIRO detects a quantity variance of 20 units ($1,000). Depending on tolerance configuration, the invoice may be posted with a payment block or partially posted for the matched quantity — the overbilled portion is held until a further GR is posted or the invoice is corrected.
- *Why A is incorrect:* MIRO enforces the GR quantity ceiling — it does not allow payment for goods not yet received. Paying for un-received goods would bypass the internal control purpose of three-way match.
- *Why B is incorrect:* MIRO does not automatically generate vendor credit memos. A credit memo must be manually requested from the vendor or created via a separate MIRO transaction using the "Credit Memo" document type.
- *Why D is incorrect:* MIRO does not reject invoices outright for quantity variances within configurable tolerance limits. It blocks or flags the variance for review — the invoice document is still created in the system.

---

### Question 16

Which of the following correctly describes the automatic account determination process that SAP uses when posting a Goods Receipt (Movement Type 101) for a purchase order line item?

- A) SAP prompts the user to manually select the inventory and GR/IR G/L accounts at the time of posting
- B) SAP derives the G/L accounts automatically using the material's Valuation Class (from the Accounting view of the Material Master) combined with the Movement Type and the account determination configuration in OBYC
- C) SAP always posts to a fixed default inventory account and a fixed GR/IR account defined at the Company Code level, regardless of material type
- D) SAP uses the Purchasing Organization's account assignment group to look up the G/L accounts in the vendor master

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* SAP's automatic account determination (configured in transaction OBYC) works by combining the Movement Type's transaction key (e.g., BSX for stock, WRX for GR/IR) with the material's Valuation Class. Different Valuation Classes (raw material, finished goods, trading goods) can map to different G/L accounts, enabling granular financial reporting without manual account selection at posting time.
- *Why A is incorrect:* Manual account selection is not part of standard MM goods movements. SAP's automatic account determination is a core design principle — requiring manual entry would introduce human error and defeat the system's integration purpose.
- *Why C is incorrect:* Different materials (raw materials vs. finished goods vs. consumables) are typically mapped to different inventory accounts via their Valuation Class. A single fixed account at Company Code level would prevent differentiated financial reporting by material category.
- *Why D is incorrect:* The vendor master's account assignment group is used in FI-SD revenue account determination for customer billing — not for MM inventory and GR/IR account determination on goods receipts.

---

### Question 17

A production planner configures MRP for a raw material with MRP Type "PD" (MRP with planned independent requirements). Demand is 200 units in week 3. Current stock is 50 units. Safety stock is 20 units. Lot size procedure is "EX" (Exact Lot Size). What planned order quantity will MRP generate?

- A) 200 units — MRP ignores current stock and always orders the full demand quantity
- B) 150 units — MRP calculates net requirement as demand minus available stock (200 − 50 = 150), then orders the exact net requirement
- C) 170 units — MRP calculates net requirement as demand minus available stock plus safety stock (200 − 50 + 20 = 170), then orders the exact net requirement
- D) 220 units — MRP adds safety stock to the demand quantity regardless of current stock levels

**Correct Answer:** C

**Explanation via Distractor Analysis:**

- *Why C is correct:* MRP net requirement = Demand − Available Stock + Safety Stock. Available stock after safety stock reserve = 50 − 20 = 30 units usable. Net requirement = 200 − 30 = 170 units. With EX (Exact Lot Size), SAP generates a planned order for exactly 170 units. Safety stock is a floor — MRP plans to replenish it, not consume it.
- *Why A is incorrect:* MRP always offsets demand against available stock before generating a planned order. Ordering the full demand quantity would result in excess stock equal to the current on-hand balance.
- *Why B is incorrect:* This calculation ignores safety stock. MRP treats safety stock as a minimum inventory floor and plans to maintain it, so the net requirement must include coverage of the safety stock requirement.
- *Why D is incorrect:* MRP does not simply add safety stock to demand. Safety stock is already held in inventory (or planned to be held) — it is part of the net requirements calculation, not an additive overhead on the demand quantity.

---

### Question 18

A pharmaceutical company uses SAP MM batch management to track lots of a regulated ingredient. When a batch is received via Goods Receipt (MIGO), a quality inspection lot is automatically created and the batch is placed in "Quality Inspection" stock. Which MM configuration element triggers the automatic quality inspection at goods receipt?

- A) The Material Master MRP 1 view — the reorder point triggers inspection when stock falls below minimum
- B) The Quality Management (QM) view of the Material Master — the QM Procurement Active indicator triggers an automatic inspection lot creation at GR for the plant
- C) The Purchasing Info Record — the vendor evaluation score below a threshold triggers mandatory quality inspection
- D) The Goods Receipt document type in MIGO — selecting movement type 103 instead of 101 routes stock to inspection automatically

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Activating the QM Procurement indicator in the QM view of the Material Master (at Plant level) enables the quality management integration for procurement. When a GR is posted for this material/plant combination, SAP Quality Management automatically creates an inspection lot and places the received quantity in restricted (Quality Inspection) stock until the inspection is completed and a usage decision is made.
- *Why A is incorrect:* The MRP 1 view controls replenishment planning parameters. The reorder point triggers procurement proposals — it has no connection to quality inspection lot generation.
- *Why C is incorrect:* Purchasing Info Records store vendor-material pricing and delivery data. Vendor evaluation scores affect vendor selection and reporting, but they do not automatically block stock or trigger inspection lots at goods receipt.
- *Why D is incorrect:* Movement Type 101 is the standard GR for Purchase Order movement. Movement Type 103 posts to "GR Blocked Stock" — a holding area for items under dispute or pending verification, not quality inspection stock. Inspection lot creation is driven by QM master data, not movement type selection.

---

### Question 19

Which of the following correctly describes how SAP MM integrates with SAP FI (Financial Accounting) at the time of Invoice Verification posting in MIRO?

- A) MIRO creates only a logistics document; the FI accounting document is created separately by the finance team in transaction FB60
- B) MIRO automatically creates a linked FI accounting document in the same posting transaction — debiting the GR/IR clearing account and crediting the Accounts Payable sub-ledger (vendor account), with simultaneous update to the G/L reconciliation account
- C) MIRO posts the invoice amount directly to the vendor's bank account and creates a FI payment document automatically
- D) MIRO updates only the purchase order history; the Accounts Payable balance is updated when the payment run (F110) is executed

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Invoice Verification in MIRO is a fully integrated transaction. When posted, it simultaneously creates: (1) a Material document (logistics) updating PO history and GR/IR, and (2) an FI accounting document debiting the GR/IR clearing account and crediting the vendor's sub-ledger AP account. The vendor sub-ledger credit simultaneously updates the G/L reconciliation account. This real-time integration is the core of SAP's logistics-finance integration.
- *Why A is incorrect:* MIRO creates the FI accounting document automatically in the same posting — no separate FB60 entry is needed or appropriate. FB60 is used for invoices with no purchase order reference (direct FI posting), which bypasses three-way match.
- *Why C is incorrect:* MIRO creates an open item in Accounts Payable — it does not trigger a bank payment. Payment is a separate step executed by the automatic payment run (transaction F110) or a manual payment (F-53), which occurs after invoice posting and approval.
- *Why D is incorrect:* PO history is updated at MIRO, but so is the FI Accounts Payable balance — immediately, not deferred until F110. F110 converts the open AP item to a cleared payment document and generates the bank transfer instruction.

---

### Question 20

A storage location in SAP MM represents a physical subdivision within a Plant. A warehouse manager needs to transfer 500 units of a component from Storage Location 0001 (main warehouse) to Storage Location 0002 (production staging area) within the same plant. Which movement type in MIGO accomplishes this, and what is the financial impact?

- A) Movement Type 101 — Goods Receipt to Purchase Order; creates a vendor liability in Accounts Payable
- B) Movement Type 201 — Goods Issue to Cost Center; expenses the material immediately to the staging area's cost center
- C) Movement Type 311 — Transfer Posting between storage locations within the same plant; no financial accounting document is generated because no valuation change occurs
- D) Movement Type 351 — Stock Transport Order; requires an inter-plant purchase order and generates an inter-company billing document

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Movement Type 311 transfers stock between two storage locations within the same Plant. Because the material stays within the same plant and valuation area, no value change occurs and no FI accounting document is generated. Only the MM inventory quantities are updated — 500 units deducted from SLoc 0001 and added to SLoc 0002. This is a purely logistical movement.
- *Why A is incorrect:* Movement Type 101 is used for goods receipts against Purchase Orders. It creates inventory (debit) and GR/IR (credit) financial postings — it is not used for internal stock transfers.
- *Why B is incorrect:* Movement Type 201 is a goods issue that removes material from stock and charges it to a cost center as an expense. This would permanently consume the 500 units from inventory — not transfer them to a staging area for later use in production.
- *Why D is incorrect:* Movement Type 351 is used for Stock Transport Orders between two different Plants. It requires an inter-plant STO purchase order, involves two separate plants (and potentially two company codes), and may generate inter-company financial documents. It is not appropriate for a movement within a single plant.
