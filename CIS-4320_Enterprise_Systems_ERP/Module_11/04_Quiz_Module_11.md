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

---

### Question 11

(5 points)

A manufacturing engineer needs to verify which finished products use a specific bearing component (material BEAR-6205) before making a design change that would alter the bearing's dimensions. Which SAP PP transaction provides this information?

- A) CS11 — Multi-Level BOM Explosion displays the bearing's own sub-components
- B) CS15 — Where-Used List shows all BOMs that contain the specified component as a line item
- C) CS03 — Display BOM shows the bearing's own BOM structure
- D) MD04 — Stock/Requirements List shows the bearing's supply and demand elements

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* CS15 is the Where-Used List. It takes a component material number as input and returns all BOMs (at one or multiple levels) that include that component. This is exactly the reverse-lookup needed before a design change — the engineer can see every parent product that would be affected.
  - *Why A is incorrect:* CS11 explodes a finished product's BOM downward to show all sub-components at every level. It answers "what does this product contain?" not "what products contain this component?" CS11 requires the parent material as input, not a component.
  - *Why C is incorrect:* CS03 displays a single BOM for a specific material. If the bearing has its own BOM (if it is itself assembled from sub-components), CS03 would show those sub-components. It does not show which parent products use the bearing.
  - *Why D is incorrect:* MD04 shows MRP planning elements — open orders, requirements, and stock balance over time — for a single material. It does not reveal BOM parentage or show which products the bearing is a component of.

---

### Question 12

(5 points)

A production planner sets the lot size rule for material FG-WING-005 to "FX" (Fixed Lot Size) with a fixed quantity of 50 units. MRP calculates a net requirement of 68 units for a given week. How many units will MRP propose in the Planned Order, and what is the consequence?

- A) 68 units — MRP always matches the exact net requirement regardless of lot size rule
- B) 50 units — MRP proposes one lot of 50 units, leaving an uncovered shortage of 18 units
- C) 100 units — MRP rounds up to the next full lot and proposes two lots of 50 units
- D) 68 units rounded to 70 — MRP rounds to the nearest multiple of the fixed lot size

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* With a Fixed Lot Size (FX) rule, MRP will propose multiples of the fixed quantity until the net requirement is covered. One lot of 50 does not cover 68 — so MRP proposes two lots of 50 = 100 units. The 32-unit surplus will appear as excess inventory on the available quantity timeline in MD04.
  - *Why A is incorrect:* EX (Exact Lot Size) is the rule that matches the exact net requirement. FX (Fixed Lot Size) forces the order quantity to a predefined fixed amount or a multiple thereof — it does not match the net requirement precisely.
  - *Why B is incorrect:* MRP with FX lot size will not leave a shortage uncovered. It will generate sufficient lots to satisfy the net requirement, even if that means ordering more than exactly needed. Leaving a shortage uncovered would defeat the purpose of MRP.
  - *Why D is incorrect:* Rounding to the nearest multiple is not standard FX behavior. FX always rounds up (not to nearest) to ensure the requirement is fully covered. A rule that could round down would risk leaving demand uncovered.

---

### Question 13

(5 points)

A Work Center (machine WC-LATHE-03) has a capacity of 8 hours per day and runs 5 days per week. A Production Order operation on this Work Center has a standard machine time of 3.5 hours. The order was confirmed (CO11N) with an actual machine time of 4.8 hours. What is the variance, and where does it ultimately flow after order settlement (KO88)?

- A) 1.3-hour favorable variance; flows to a WIP account in FI
- B) 1.3-hour unfavorable variance; the machine time overrun increases actual production cost and flows to the Production Variance account in FI at KO88
- C) 1.3-hour unfavorable variance; the variance is absorbed into the standard cost of the finished product
- D) No variance — actual time is recorded for information only; standard cost never changes

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Actual machine time (4.8 hrs) exceeds standard (3.5 hrs) by 1.3 hours — this is an unfavorable time variance. The additional hours are charged to the Production Order at the Work Center's cost rate (per hour). At KO88 settlement, actual costs exceed standard costs, and the difference posts to the Production Variance account in FI/CO.
  - *Why A is incorrect:* A favorable variance means actual cost is less than standard (actual time is shorter than planned). Here actual time exceeds standard — this is unfavorable, not favorable.
  - *Why C is incorrect:* Production variances are never absorbed into the standard cost of the finished product. Standard cost remains fixed until a cost estimate is released. Variances are posted separately to FI variance accounts to preserve the integrity of standard costing.
  - *Why D is incorrect:* Actual times confirmed on a Production Order are valued using the Work Center's cost rates and posted to the Production Order as actual costs. They affect the order's actual cost accumulation and therefore the settlement variance — they are not informational only.

---

### Question 14

(5 points)

During a production planning review, the planner sees that several Planned Orders in MD04 have a "Firming" indicator set. What does a firmed Planned Order mean, and why would a planner firm a Planned Order?

- A) A firmed Planned Order has been converted to a Production Order and sent to the shop floor for execution
- B) A firmed Planned Order is protected from being changed or deleted by the next MRP run — the planner has manually confirmed this order quantity and date
- C) A firmed Planned Order indicates the order has been approved by the Plant Manager and cannot be modified
- D) A firmed Planned Order has been assigned to a specific Work Center and cannot be rescheduled

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Firming a Planned Order (setting the Firming indicator in MD04 or MD05) prevents MRP from rescheduling, changing the quantity, or deleting the order during the next MRP run. Planners firm orders when they have made manual adjustments or coordinated with vendors/shop floor on specific dates and quantities that should not be overwritten by automatic planning.
  - *Why A is incorrect:* Converting a Planned Order to a Production Order is a separate action (CO40). Converting creates an entirely new Production Order document — the Planned Order disappears and is replaced by the Production Order. Firming does not convert the order.
  - *Why C is incorrect:* There is no standard "Plant Manager approval" status associated with firming in SAP PP. Firming is a planning tool controlled by the production planner, not an approval workflow step.
  - *Why D is incorrect:* Work Center assignment is part of the Routing — operations are assigned to Work Centers in the Routing definition. Firming the Planned Order does not assign it to a specific Work Center or affect rescheduling from a capacity perspective independently.

---

### Question 15

(5 points)

A production scheduler needs to understand whether Work Center WC-MILL-02 is overloaded for the next two weeks based on all open Production Orders that have operations assigned to it. Which SAP PP transaction provides a graphical or tabular view of work center load versus available capacity?

- A) MD04 — Stock/Requirements List shows capacity for all materials planned on the Work Center
- B) CM01 — Work Center Capacity Load displays planned load versus available capacity over a time horizon
- C) CO03 — Display Production Order shows the scheduled dates for operations on that Work Center
- D) COOIS — Production Order Information System lists all open Production Orders but not capacity load

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* CM01 (Capacity Planning — Work Center View) shows the capacity load on a specific Work Center: the total planned work (in hours) from all Production Order operations scheduled on that Work Center compared to its available capacity (daily or weekly hours). It is the primary capacity leveling and overload detection tool in SAP PP.
  - *Why A is incorrect:* MD04 is material-centric — it shows supply and demand for a single material. It does not aggregate Work Center load across multiple Production Orders or compare planned hours to capacity availability.
  - *Why C is incorrect:* CO03 shows the details of a single Production Order including its scheduled operation dates and the Work Center assigned to each operation. However, it shows only that one order — it cannot aggregate load across all orders on a given Work Center.
  - *Why D is incorrect:* COOIS (Production Order Information System) is a reporting tool that lists Production Orders with their status, dates, and quantities. While it can filter by Work Center, it does not display a capacity load chart or compare planned load to available capacity.

---

### Question 16

(5 points)

Transaction CO11N is used to confirm a production operation. Which of the following data elements is captured during a production confirmation in SAP PP?

- A) Vendor name, invoice number, and payment terms for the raw materials consumed
- B) Yield quantity (units produced), scrap quantity, actual machine time, actual labor time, and the operation being confirmed
- C) Customer name, sales order number, and delivery date for the finished product
- D) Cost center, GL account, and cost element for the variance posting

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* CO11N captures the actual execution data for a production operation: how many good units were produced (yield), how many were scrapped, and the actual times (machine hours, labor hours) compared to the planned times from the Routing. This data feeds actual cost calculations and shop floor progress tracking.
  - *Why A is incorrect:* Vendor invoice data belongs to MM (MIRO) — it records how much was paid to a vendor for purchased materials. Production confirmation is internal to the manufacturing execution process and has no connection to vendor invoices.
  - *Why C is incorrect:* Customer and sales order data belongs to SD (Sales and Distribution). While a Production Order may have been triggered by a Sales Order in a Make-to-Order environment, the production confirmation itself does not capture customer or delivery information.
  - *Why D is incorrect:* Cost center, GL account, and cost element assignments are configured in the PP/CO master data (Work Center cost rates, cost elements). They are determined automatically by SAP based on confirmation data — the shop floor operator does not enter them manually during CO11N.

---

### Question 17

(5 points)

A company manufactures a product using a multi-level BOM. Level 0 is the finished product; Level 1 contains two sub-assemblies (SA-A and SA-B); Level 2 contains the raw materials for each sub-assembly. MRP runs for the Level 0 finished product and generates Planned Orders. What happens to the demand for Level 1 sub-assemblies and Level 2 raw materials?

- A) MRP only plans Level 0 — sub-assemblies and raw materials must be planned in separate manual MRP runs
- B) MRP automatically explodes the BOM downward, generating dependent requirements at Level 1 and Level 2 simultaneously in a single planning run
- C) MRP generates Planned Orders only for Level 1; a second MRP run is needed to generate requirements for Level 2 raw materials
- D) Level 2 raw materials are planned by MM, not PP — PP only manages production of finished and semi-finished goods

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* SAP MRP performs a full multi-level BOM explosion in a single planning run. When demand for the finished product (Level 0) is planned, MRP automatically derives dependent requirements for all sub-assemblies and raw materials at every BOM level. This is one of MRP's core capabilities — a single MD01 or MD02 run covers the entire product structure.
  - *Why A is incorrect:* Separate MRP runs per BOM level would defeat the purpose of an integrated planning system. SAP MRP was designed specifically to handle multi-level structures in one execution — planners do not need to manually cascade requirements through each level.
  - *Why C is incorrect:* A single MRP run cascades through all BOM levels simultaneously. There is no need for a second run to reach Level 2 materials. The explosion is recursive — each level's Planned Orders create dependent requirements for the level below.
  - *Why D is incorrect:* Both MM (for externally purchased raw materials) and PP (for in-house manufactured sub-assemblies) are involved in MRP. The distinction is the procurement proposal type: raw materials get Purchase Requisitions routed to MM; in-house sub-assemblies get Planned Orders converted in PP. Both happen in the same MRP run.

---

### Question 18

(5 points)

A plant controller wants to review production efficiency across all Production Orders that were settled in June 2026, comparing actual production costs to standard costs and summarizing variance by variance category (input price variance, quantity variance, lot size variance). Which SAP report or transaction is most appropriate?

- A) MD05 — MRP List shows the last MRP run results including planned versus actual requirements
- B) COOIS — Production Order Information System provides a list of orders but not variance category detail
- C) CO1P / KKBC_ORD — Production Order Cost Report shows actual vs. standard costs and variance categories per order
- D) KO88 — Settlement transaction can be executed in simulation mode to show variance previews

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* The Production Order Cost Report (accessible via CO03 → Costs tab, or KKBC_ORD for summary across orders) shows the actual costs accumulated on each order versus the standard cost of production, with variance broken down into categories: input price variance (material cost difference), quantity variance (more or less material used than planned), and lot size variance. This is the controller's primary production variance analysis tool.
  - *Why A is incorrect:* MD05 is the MRP List — it shows a snapshot of the last MRP planning run for a material (planned orders, purchase requisitions, dates). It contains no cost or variance information.
  - *Why B is incorrect:* COOIS provides a configurable list of Production Orders with status, dates, quantities, and basic cost data. It is useful for operational tracking but does not provide the detailed variance category breakdown the controller needs.
  - *Why D is incorrect:* KO88 is the settlement execution transaction — it posts the settlement, not a variance analysis report. While KO88 can be run in test mode to preview settlement results, it is a posting transaction, not a cost analysis tool for reviewing multiple settled orders.

---

### Question 19

(5 points)

In a Make-to-Order (MTO) production environment, a Production Order is created directly from a Sales Order line item. How does this differ from a Make-to-Stock (MTS) Production Order, and what is the key consequence for inventory and cost flow?

- A) MTO and MTS Production Orders are identical — the only difference is that MTO orders are created manually while MTS orders are created by MRP
- B) In MTO, the Production Order is linked to a specific Sales Order and the finished goods produced go directly to the Sales Order; inventory is not built to stock, and costs are settled to the Sales Order rather than to a stock account
- C) In MTO, finished goods are posted to stock and then allocated to the Sales Order at the time of delivery — the production cost flows through inventory exactly as in MTS
- D) MTO Production Orders skip the Goods Receipt step — finished goods are delivered directly to the customer without entering SAP inventory

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* In Make-to-Order, the Production Order carries the Sales Order as an account assignment. The finished goods produced are posted against the Sales Order (they may appear in stock but are valuated and attributed to that specific Sales Order — not generic stock). Settlement flows to the Sales Order cost object, enabling exact cost and margin tracking per customer order.
  - *Why A is incorrect:* MTO and MTS Production Orders differ in more than creation method. The fundamental difference is account assignment: MTO orders are assigned to Sales Orders; MTS orders are assigned to cost centers or profit centers. This affects settlement, inventory valuation, and cost traceability.
  - *Why C is incorrect:* In true MTO, finished goods produced are earmarked for the specific Sales Order at the time of production. They are not available for any other Sales Order allocation. The accounting and settlement logic differs from MTS because costs trace to the individual customer order.
  - *Why D is incorrect:* MTO Production Orders do post a Goods Receipt — the finished product enters SAP inventory as a valuated stock item (though earmarked for the specific Sales Order). The Goods Issue to the Sales Order delivery then removes it from inventory in the normal SD delivery process.

---

### Question 20

(5 points)

A plant has 200 active Production Orders in various statuses. The Production Planning manager wants a single report listing all REL (Released) orders that are past their scheduled finish date (overdue), with the open quantity remaining and the responsible Work Center for the final operation. Which transaction is most appropriate?

- A) MD04 — Stock/Requirements List filtered by order status and date
- B) CS11 — BOM explosion filtered by order finish date
- C) COOIS — Production Order Information System with filters on status REL, finish date less than today, and output layout including open quantity and Work Center
- D) CO03 — Display Production Order iterated manually for all 200 orders

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* COOIS (Production Order Information System) is specifically designed for this type of cross-order reporting. The planner can filter by order status (REL), finish date (less than or equal to today), and configure the output layout to include remaining quantity and the Work Center of the last operation. COOIS is the standard SAP PP reporting cockpit for shop floor management.
  - *Why A is incorrect:* MD04 is material-centric — it shows planning elements for one material at a time. It cannot aggregate all overdue Production Orders across all materials in a single report filtered by status and finish date.
  - *Why B is incorrect:* CS11 is the multi-level BOM explosion — it shows product structure, not Production Order execution status. It has no concept of order finish dates, order status, or remaining production quantities.
  - *Why D is incorrect:* CO03 displays a single Production Order. Reviewing 200 orders individually is operationally impossible for a daily management review. COOIS exists precisely to avoid this — it provides mass reporting across all orders with flexible filtering.
