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
