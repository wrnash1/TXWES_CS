# Video Script: Module 11 — SAP Production Planning (PP Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

## SEGMENT 1 — Introduction: The Manufacturing Engine (0:00–2:30)

Welcome back. I'm Professor Nash, and this is Module 11 of CIS-4320 Enterprise Systems and ERP.

In Module 10 we covered how SAP MM manages the procurement of materials from external vendors. In this module we look at what happens to those materials once they are inside the factory: the SAP Production Planning module — SAP PP.

PP is the manufacturing brain of SAP ERP. It handles everything from defining how a product is built — the Bill of Materials and Routing — to planning how much to produce and when — Material Requirements Planning — to executing that plan on the factory floor through Production Orders. If you work in manufacturing, engineering, supply chain, or operations, PP is where your career intersects with ERP.

Today's topics: Bill of Materials (BOM), Work Centers, Routings, Material Requirements Planning (MRP), Production Orders, and Shop Floor Control. These are all tested on the SAP S/4HANA Essentials exam.

[SHOW SCREEN: SAP Fiori Launchpad — Production Planning section showing tiles: Material Requirements Planning, Production Orders, Bill of Materials, Work Centers, Routing]

---

## SEGMENT 2 — Bill of Materials (2:30–6:00)

The Bill of Materials is the foundation of production planning. It answers a deceptively simple question: what do I need to make this product?

A **Bill of Materials (BOM)** is a structured list of all the components, sub-assemblies, and raw materials required to manufacture one unit of a finished product, along with the quantity of each component needed.

[SHOW SCREEN: SAP transaction CS03 — Display BOM for material FG-BRACKET-001: Header showing Finished Good material, valid-from date. Item list showing: Item 1 — Titanium Bar Stock (TIT-BAR-001), 2.5 kg; Item 2 — Steel Bolt Set (BOLT-M8), 12 units; Item 3 — Rubber Gasket (GASK-12), 4 units; Item 4 — Sub-assembly SA-BRACKET-FRAME, 1 unit]

The BOM has two key levels:

**Single-level BOM** — shows only the immediate components of the finished product. If the finished product contains a sub-assembly, the single-level BOM shows the sub-assembly as one component — not what the sub-assembly is made of.

**Multi-level BOM** — explodes all levels: the finished product, its sub-assemblies, and the raw materials within each sub-assembly. This is what MRP uses to calculate total material requirements across all levels.

Transaction **CS01** creates a BOM. Transaction **CS03** displays it. Transaction **CS11** shows the multi-level BOM explosion.

BOM categories in SAP: Production BOM (for manufacturing), Sales Order BOM (customer-specific variants), WM BOM (warehouse management picking list).

The **Base Quantity** is the quantity of the finished product that the BOM is defined for — typically 1 unit. If the base quantity is 1 bracket and the BOM shows 2.5 kg of titanium, then producing 400 brackets requires 1,000 kg of titanium. MRP performs this multiplication automatically.

---

## SEGMENT 3 — Work Centers (6:00–8:30)

A Work Center is where production operations are performed. It is the PP representation of a machine, a workstation, a production line, or a team.

[SHOW SCREEN: SAP transaction CR03 — Display Work Center showing: Work Center ID, Work Center Category, Plant, Capacity, Available Capacity (hours per shift), Costing Data (activity type and rates)]

Work Centers contain:

- **Capacity data** — how many hours per day is this work center available? One shift = 8 hours. Two shifts = 16 hours. This drives capacity planning.
- **Scheduling data** — setup time, processing time formula, teardown time. Used by the Routing to calculate how long each operation takes.
- **Costing data** — the cost rates associated with using this work center. When a Production Order is confirmed, the system multiplies the actual time used by the cost rate to calculate the production cost.

The Work Center is the link between PP's operational world and CO's cost accounting world. Every minute of machine or labor time used in production is costed through the Work Center's activity rates.

Transaction **CR01** creates a Work Center. Transaction **CR03** displays it.

---

## SEGMENT 4 — Routing (8:30–11:00)

If the BOM answers "what do I need," the Routing answers "how do I make it — step by step."

A **Routing** is the sequence of production operations required to manufacture a product, specifying which Work Center performs each operation and how long each step takes.

[SHOW SCREEN: SAP transaction CA03 — Display Routing for material FG-BRACKET-001: Operation list showing: Operation 10 — Cut to Length (Work Center: CNC-SAW-01, Setup 15 min, Machine time 2 min/unit); Operation 20 — Mill Profile (Work Center: CNC-MILL-03, Setup 20 min, Machine time 8 min/unit); Operation 30 — Deburr and Clean (Work Center: CLEAN-01, Labor time 3 min/unit); Operation 40 — Quality Inspection (Work Center: QA-INSPECT, Setup 5 min, Inspection time 5 min/unit)]

Key Routing concepts:

- **Operations** are numbered in increments of 10 (10, 20, 30...) to allow insertions without renumbering.
- **Standard Values** — setup time, machine time, labor time — define the time required per unit or per lot at each operation. These feed into scheduling and costing.
- **Control Key** determines whether an operation must be confirmed, whether it is a milestone operation, and whether a PP order for sub-assembly components should be triggered.
- **In-house Production Time** — the total lead time from start to finish of production, calculated by summing all routing operation times plus queue times between operations. This is a key field on the Material Master MRP view.

Transaction **CA01** creates a Routing. Transaction **CA03** displays it. Transaction **CA60** reports on where a Routing is used.

---

## SEGMENT 5 — Material Requirements Planning (11:00–15:30)

MRP is the computational engine that answers the question every production planner faces every day: "What do I need to order or produce, in what quantity, and by when?"

[SHOW SCREEN: MRP logic diagram showing three inputs: Independent Requirements (planned production quantities from demand plan), Dependent Requirements (BOM explosion — components needed), Current Stock and Open POs/PRs. Output: Planned Orders and Purchase Requisitions]

MRP in SAP works by:

1. Reading the **Demand Program** — independent requirements from sales orders, forecasts, or the Demand Management module (MD61).
2. **Exploding the BOM** — for every finished product requirement, calculating how many of each component is needed (quantity × BOM component quantity).
3. **Netting** — subtracting current stock and open purchase orders or production orders from the gross requirement to determine the net requirement.
4. **Lot Sizing** — applying the lot size rule from the Material Master MRP view to determine order quantities (exact lot size, fixed lot size, minimum lot size, economic order quantity).
5. **Generating Procurement Proposals** — creating Planned Orders for in-house manufactured materials and Purchase Requisitions for externally procured materials.

[SHOW SCREEN: SAP transaction MD04 — Stock/Requirements List for TIT-BAR-001 showing: Date, MRP Element (ProdOrd, PurRqs, Stock), Quantity, Available Quantity]

The **Stock/Requirements List** (transaction MD04) is the production planner's primary daily tool. It shows every demand, every supply, and the resulting available stock balance — forward in time — for a single material. If available quantity goes negative on any date, there is a material shortage that must be resolved.

The **MRP Run** is executed at the Plant level (transaction **MD01**) or for a single material (transaction **MD02**). SAP offers two MRP modes:

- **Regenerative Planning** — recalculates everything for all materials in the plant. Used for the weekly or nightly full planning run.
- **Net Change Planning** — recalculates only materials where something has changed since the last MRP run. Much faster; used for intraday updates.

Key Material Master MRP fields:

- **MRP Type** — controls how the material is planned: MRP (PD), reorder point (VB), consumption-based (VM), or manual (ND)
- **Lot Size** — how to round or batch order quantities
- **Planned Delivery Time** — external procurement lead time (days from PO to GR)
- **In-House Production Time** — manufacturing lead time (days from production start to completion)
- **Safety Stock** — buffer quantity to protect against supply or demand variability

---

## SEGMENT 6 — Production Orders and Shop Floor Control (15:30–20:00)

Once MRP has generated Planned Orders, the production supervisor converts them to Production Orders and the shop floor executes the plan.

[SHOW SCREEN: SAP transaction CO01 — Create Production Order showing: Material, Order Type, Plant, Order Quantity, Basic Start Date, Basic Finish Date. Status field showing: REL (Released)]

A **Production Order** is the formal authorization to manufacture a specific quantity of a material by a specific date. When a Production Order is created, SAP:

- Copies the BOM and Routing into the order
- Calculates scheduled start and finish dates for each operation
- Reserves the required component materials (creates reservations in MM)
- Calculates the planned production cost based on Routing times and Work Center rates

The Production Order lifecycle follows these statuses:

- **CRTD (Created)** — order exists but is not yet released to the shop floor
- **REL (Released)** — order is authorized to start; goods issues can be posted
- **CONF (Confirmed)** — operations have been reported as complete; times and quantities are logged
- **TECO (Technically Complete)** — production is finished; no more postings
- **CLSD (Closed)** — order is settled; all costs transferred to the finished goods stock or variance accounts

[SHOW SCREEN: SAP transaction CO11N — Production Order Confirmation screen showing: Order Number, Operation, Confirmation Date, Yield Quantity, Scrap Quantity, Activity times: Machine Time, Labor Time]

The **Goods Issue** to the Production Order (MIGO, Movement Type 261) withdraws the required component materials from inventory. SAP posts:

- Debit: Production Order (WIP — work in progress)
- Credit: Inventory (component materials consumed)

The **Goods Receipt** from the Production Order (MIGO, Movement Type 101 for production) posts the finished goods into inventory:

- Debit: Finished Goods Inventory
- Credit: Production Order (reduces WIP)

**Order Settlement** — after the order is technically complete, transaction **KO88** settles the Production Order. It compares the actual costs incurred (materials consumed, machine time, labor time) to the standard cost of the finished goods produced. The difference is the production variance:

- If actual cost > standard cost: an unfavorable variance is posted to a variance account
- If actual cost < standard cost: a favorable variance is posted

Production variances are visible to management in the Controlling (CO) module and are a key signal of manufacturing efficiency.

---

## SEGMENT 7 — PP to MM and FI Integration Summary (20:00–22:30)

SAP PP is deeply integrated with MM and FI. Let me trace the complete flow.

When MRP runs and generates a Purchase Requisition for a raw material, that PR flows directly to MM where a buyer converts it to a Purchase Order. The MM Goods Receipt increases inventory and posts to FI. When the Production Order consumes those materials, MIGO Movement Type 261 reduces MM inventory and posts a cost to the Production Order in CO.

When finished goods are produced and received into inventory, FI records the inventory asset. When the order settles, cost variances flow to FI as variance accounts.

The key integration points:

- MRP generates PRs in MM for purchased materials
- Goods Issues from inventory to Production Orders reduce MM stock and post to CO via Work Center cost rates
- Goods Receipts from Production Orders increase MM finished goods inventory
- Order Settlement transfers production variances to FI

For the SAP S/4HANA exam: know the BOM transaction codes (CS01/CS03), Routing transaction codes (CA01/CA03), MRP run (MD01), Stock/Requirements List (MD04), Production Order creation (CO01), confirmation (CO11N), and settlement (KO88). Know the Production Order status sequence: CRTD, REL, CONF, TECO, CLSD.

Module 12 covers SAP Sales and Distribution — the SD module — which is the customer-facing counterpart to the PP manufacturing and MM procurement modules we have covered in Modules 10 and 11.

---

*End of Script — Module 11*
