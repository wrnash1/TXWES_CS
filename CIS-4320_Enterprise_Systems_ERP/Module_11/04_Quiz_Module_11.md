# Quiz: Module 11 — SAP Production Planning (PP Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

### Question 1

A manufacturing engineer at an aerospace company creates a structured list in SAP that defines all components, sub-assemblies, and raw materials required to produce one unit of a finished bracket assembly, including the quantity of each component needed. Which SAP PP object has the engineer created?

- A) Routing — the ordered sequence of production operations specifying which Work Center performs each step
- B) Work Center — the PP representation of a machine or workstation where operations are performed
- C) Bill of Materials — the structured component list defining what materials are needed to produce the finished product
- D) Production Order — the formal shop floor authorization to manufacture a specific quantity by a specific date

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The Bill of Materials (BOM) answers the question "what do I need to make this product?" It is the complete structured list of components, sub-assemblies, and raw materials with quantities, defined for a specific base quantity of the finished product. Created with transaction CS01.
- *Why A is incorrect:* A Routing answers "how do I make it" — it defines the sequence of operations (steps), the Work Center performing each step, and the processing times. A Routing is about process sequence, not material components.
- *Why B is incorrect:* A Work Center is a single production resource (machine, team, or workstation) with capacity, scheduling, and cost rate data. It is referenced by Routing operations but is not a list of material components.
- *Why D is incorrect:* A Production Order is a shop floor execution document created to manufacture a specific quantity. When created, it copies the BOM and Routing into the order — but the Production Order itself is not the master data component list; it consumes the BOM.

---

### Question 2

A production planner displays a BOM for a finished product and sees it contains four line items: three raw materials and one sub-assembly component listed as a single line with quantity 1. The sub-assembly's own components are not visible. Which type of BOM display is the planner using?

- A) Multi-level BOM explosion — all levels of the product structure are shown including sub-assembly components
- B) Where-used list — shows all finished products that contain this component
- C) Single-level BOM — shows only the immediate children of the finished product without exploding sub-assemblies
- D) Production BOM — the BOM category used for manufacturing as opposed to sales or costing

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* A single-level BOM (displayed via CS03) shows only the immediate children of the parent material. Sub-assemblies appear as single line items — their own components are not shown. The planner sees the sub-assembly as "1 EA" without any further breakdown.
- *Why A is incorrect:* A multi-level BOM explosion (CS11) would show the sub-assembly AND all of its components below it in the hierarchy. If the planner could see what the sub-assembly is made of, it would be a multi-level display.
- *Why B is incorrect:* A where-used list (CS15) is the reverse lookup — it shows which parent products use a given component. That is the opposite direction from what the planner is doing.
- *Why D is incorrect:* Production BOM is the BOM usage category (Usage 1), which distinguishes it from a Sales Order BOM or Costing BOM. BOM usage category is separate from single-level vs. multi-level display — a Production BOM can be displayed either way.

---

### Question 3

An MRP run at Plant 1000 calculates the following for material FG-BRACKET-001: Gross Requirement = 80 units. Current stock = 25 units. Safety Stock = 10 units. Open Production Orders = 0 units. The lot size rule is EX (exact lot size). What quantity will MRP propose in the Planned Order?

- A) 80 units — MRP always orders the gross requirement regardless of current stock
- B) 55 units — MRP subtracts only current stock from gross requirement without considering safety stock
- C) 65 units — MRP nets against available stock (current stock minus safety stock) to maintain the safety stock floor
- D) 45 units — MRP subtracts both current stock and safety stock twice from the gross requirement

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Net Requirement = Gross Requirement minus Available Stock. Available Stock for MRP netting = Current Stock minus Safety Stock = 25 minus 10 = 15 units. Net Requirement = 80 minus 15 = 65 units. With EX lot size, MRP proposes exactly 65 units. Safety stock acts as an inventory floor — MRP plans to replenish down to safety stock level, not below it.
- *Why A is incorrect:* MRP subtracts available stock from gross requirements before proposing an order. Ordering 80 units when 25 are already in stock would result in 45 units of excess inventory (ignoring safety stock), which is waste.
- *Why B is incorrect:* Subtracting only current stock (80 minus 25 = 55) ignores safety stock. Since safety stock is defined as a buffer floor, MRP treats it as unavailable for demand coverage — available stock = 25 minus 10 = 15, not 25.
- *Why D is incorrect:* Safety stock is subtracted once from current stock to determine available stock. It is not subtracted twice or independently added to the order quantity in a separate step.

---

### Question 4

For which type of material does SAP MRP generate a Planned Order as the procurement proposal, and for which type does it generate a Purchase Requisition?

- A) Planned Orders for externally purchased materials; Purchase Requisitions for in-house manufactured materials
- B) Planned Orders for in-house manufactured materials; Purchase Requisitions for externally purchased materials
- C) Both Planned Orders and Purchase Requisitions are generated for all materials — the planner chooses which to use
- D) Planned Orders for all materials at the component level; Purchase Requisitions only for finished goods

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* MRP generates Planned Orders for materials with in-house production (the MRP Type is PD and the material is set up for in-house production). Planned Orders must be converted to Production Orders before manufacturing begins. For externally procured materials, MRP generates Purchase Requisitions that flow to MM where a buyer converts them to Purchase Orders.
- *Why A is incorrect:* This reverses the correct logic. Purchase Requisitions flow to vendors through MM purchasing — they represent external procurement. Planned Orders are internal manufacturing proposals.
- *Why C is incorrect:* The type of procurement proposal MRP generates is determined by the material's procurement type in the Material Master MRP view (in-house production vs. external procurement) — it is not a planner choice made during each MRP run.
- *Why D is incorrect:* The level in the BOM (finished goods vs. component) does not determine the procurement proposal type. A component can be either manufactured in-house (Planned Order) or purchased externally (Purchase Requisition) depending on its procurement type setting.

---

### Question 5

A production planner opens transaction MD04 and reviews the Stock/Requirements List for material ALU-BAR-6061. The list shows a line where the Available Quantity column displays a negative number. What does this indicate, and what action should the planner take?

- A) The material has been over-received; the planner should reverse the excess Goods Receipt
- B) There is a material shortage on that date — demand exceeds available supply, and the planner should create or expedite a procurement proposal to cover the shortage
- C) The material has been issued to a Production Order; a negative balance is normal and requires no action
- D) The MRP run encountered an error; the negative balance will correct itself when MRP is re-run

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In MD04, the Available Quantity column shows the running balance of supply minus demand over time. A negative available quantity means that at that date, demand (requirements) exceeds supply (stock + open orders). This is a shortage situation that requires the planner to create a new procurement proposal or expedite an existing one to cover the gap.
- *Why A is incorrect:* An over-receipt would result in a higher-than-expected positive balance, not a negative one. Negative available quantity reflects a supply shortage, not an inventory surplus.
- *Why C is incorrect:* Issuing materials to a Production Order reduces inventory but does not cause negative available quantity in MD04 by itself — the issue is planned and reflected in the MRP element. A negative balance means more demand is planned than supply available.
- *Why D is incorrect:* MD04 reflects the current MRP plan. A negative balance is a genuine shortage signal from the planning engine, not a calculation error. Re-running MRP with the same inputs will reproduce the same shortage.

---

### Question 6

A Production Order at a manufacturing plant has status REL (Released). The shop floor supervisor posts the Goods Issue to withdraw raw materials from inventory for this order using MIGO Movement Type 261. Which accounting entry does SAP generate?

- A) Debit Finished Goods Inventory / Credit Production Order (WIP)
- B) Debit Production Order (WIP) / Credit Raw Materials Inventory
- C) Debit Raw Materials Inventory / Credit Accounts Payable
- D) Debit Variance Account / Credit Production Order (WIP)

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* When raw materials are issued to a Production Order (Movement Type 261), the components leave inventory (Credit Raw Materials Inventory — inventory decreases) and the cost is charged to the Production Order as Work in Progress (Debit Production Order WIP). The Production Order accumulates actual costs until settlement.
- *Why A is incorrect:* Debiting Finished Goods Inventory and crediting the Production Order is the entry for the Goods Receipt from the Production Order (Movement Type 101) — when the finished product enters stock after manufacturing is complete. That is the opposite end of the production cycle.
- *Why C is incorrect:* Debiting Raw Materials Inventory and crediting Accounts Payable is the vendor invoice posting (MIRO). Materials were received from a vendor in a prior step. The Goods Issue to the Production Order pulls from existing inventory — no vendor transaction is involved.
- *Why D is incorrect:* Debiting a Variance Account and crediting the Production Order is part of the Order Settlement posting (KO88) — which happens at the end of the production cycle when actual costs are compared to standard costs. It does not occur at the Goods Issue step.

---

### Question 7

A Production Order for 100 units of a finished product has status TECO (Technically Complete). A quality inspector discovers that 5 additional units need to be reworked and wants to post a Goods Issue for more raw materials to the order. What will happen when the inspector attempts this posting?

- A) The Goods Issue will post successfully because TECO orders can receive additional material postings for rework
- B) The system will prompt the inspector to create a new Production Order for the rework quantity
- C) The Goods Issue posting will be blocked — TECO status prevents further goods movements and confirmations
- D) The system will automatically downgrade the order to REL status to allow the rework posting

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* TECO (Technically Complete) status signals that production is finished and the order is closed from a manufacturing standpoint. No further goods movements (Goods Issues or Goods Receipts) or operation confirmations are allowed. The order is locked for operational activities — only financial settlement (KO88) can follow.
- *Why A is incorrect:* TECO specifically blocks further goods movements. This is a deliberate control — it prevents unplanned material consumption after the order is considered finished, which would distort actual costs and inventory.
- *Why B is incorrect:* SAP does not automatically prompt for a new Production Order. The inspector would need to manually reverse the TECO status (if authorized) or create a separate rework order. The system does not create new orders automatically.
- *Why D is incorrect:* SAP does not automatically downgrade order status. Status changes are deliberate actions performed by authorized users. An automatic downgrade would undermine the control purpose of TECO status.

---

### Question 8

Transaction KO88 settles a Production Order that manufactured 200 units of a finished product. The actual production cost accumulated on the order is $42,500. The standard cost of the 200 units produced is $40,000 ($200 per unit × 200 units). What type of variance exists, and what is the accounting entry posted by KO88?

- A) Favorable variance of $2,500 — Debit Production Order (close WIP) / Credit Variance Account (favorable)
- B) Unfavorable variance of $2,500 — Debit Variance Account (unfavorable) / Credit Production Order (close WIP)
- C) No variance — KO88 always posts actual cost to standard cost with no difference
- D) Unfavorable variance of $2,500 — Debit Finished Goods Inventory / Credit Variance Account

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Actual cost ($42,500) exceeds standard cost ($40,000) by $2,500 — this is an unfavorable variance because production cost more than planned. KO88 posts: Debit Variance Account (unfavorable) for $2,500 to record the excess cost in FI; Credit Production Order (WIP) to close the $2,500 remaining balance on the order. The order WIP balance goes to zero.
- *Why A is incorrect:* A favorable variance occurs when actual cost is less than standard cost. Here actual ($42,500) exceeds standard ($40,000) — the variance is unfavorable. Also, the debit/credit direction is reversed: for an unfavorable variance, the variance account is debited (expense), not credited.
- *Why C is incorrect:* Production variances are extremely common in manufacturing. Differences in actual vs. planned material consumption, scrap, machine time overruns, and labor time variations routinely produce variances. KO88 always compares and posts the difference.
- *Why D is incorrect:* KO88 does not debit Finished Goods Inventory — that posting already occurred at Goods Receipt when the finished product entered stock. KO88 only clears the remaining WIP balance on the Production Order by posting the variance to FI accounts.

---

### Question 9

A production planner needs to check whether the scheduled operations on a Production Order have been reported as complete and whether actual times have been logged for each step. Which transaction and document status should the planner review?

- A) MD04 — Stock/Requirements List; check the Available Quantity column for the finished product
- B) CO03 — Display Production Order; review the Operations tab and check operation status and actual times
- C) CS11 — Multi-level BOM explosion; verify component quantities consumed at each level
- D) CR03 — Display Work Center; check the capacity utilization report for actual hours used

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* CO03 (Display Production Order) shows the complete Production Order including the Operations tab where each Routing operation is listed with its planned and actual times, confirmation status, yield quantities, and scrap. This is the correct transaction to verify whether operations have been confirmed and actual times recorded.
- *Why A is incorrect:* MD04 shows supply and demand elements for a material over time — it shows whether a Production Order exists and its scheduled dates, but does not show operation-level confirmation details or actual times logged at each Routing step.
- *Why C is incorrect:* CS11 is the multi-level BOM explosion — it shows material components across all BOM levels. It provides no information about Production Order execution, operation confirmations, or actual production times.
- *Why D is incorrect:* CR03 displays the Work Center master data — capacity definition, cost rates, and scheduling parameters. While a capacity report from the Work Center perspective might show hours loaded, the planner's specific need is to check confirmation status on a particular Production Order, which requires CO03.

---

### Question 10

SAP PP integrates tightly with MM and FI throughout the production process. Which of the following correctly describes the sequence of integration events when a Production Order for a purchased raw material is executed from MRP through order settlement?

- A) MRP generates a Purchase Order → MM posts the Goods Receipt → PP creates the Production Order → FI posts the variance at order creation
- B) MRP generates a Purchase Requisition → MM buyer converts it to a Purchase Order → MM posts the vendor Goods Receipt → PP issues materials to the Production Order → PP posts the finished goods Goods Receipt → FI receives the variance at order settlement
- C) PP creates the Production Order → MRP runs to calculate components → MM generates Purchase Orders automatically → FI posts all transactions simultaneously at month-end
- D) MRP generates a Planned Order → PP converts it to a Purchase Order → MM verifies the vendor invoice → FI posts inventory at the time of the MRP run

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* This is the correct PP-MM-FI integration sequence. MRP generates a PR (not a PO) for purchased materials → MM buyer converts PR to PO (ME21N) → MM posts vendor Goods Receipt (MIGO 101 for PO) → PP issues components to the Production Order (MIGO 261) → PP posts finished goods GR (MIGO 101 for production order) → KO88 settlement flows production variances to FI. Each step belongs to the correct module in the correct sequence.
- *Why A is incorrect:* MRP does not generate Purchase Orders — it generates Purchase Requisitions. POs are created by buyers in MM. Also, FI variance posting occurs at order settlement (after production is complete), not at order creation.
- *Why C is incorrect:* Production Orders are created after MRP runs, not before. MRP calculates component requirements based on existing demand, not after the Production Order exists. MM does not generate Purchase Orders automatically from MRP — buyers must convert PRs. FI postings occur in real time as each transaction is posted, not at month-end.
- *Why D is incorrect:* A Planned Order (for in-house production) is converted to a Production Order (CO40), not a Purchase Order. Purchase Orders are for externally procured materials. Also, FI inventory postings occur at Goods Receipt time, not during the MRP run — MRP creates no financial postings.
