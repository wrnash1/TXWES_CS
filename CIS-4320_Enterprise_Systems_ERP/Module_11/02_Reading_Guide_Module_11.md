# Reading Guide: Module 11 — SAP Production Planning (PP Module)

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4320 &BULL; ENTERPRISE SYSTEMS & ERP ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

## Introduction

SAP Production Planning (PP) is the module that manages the complete manufacturing process — from defining product structure and production methods through planning material needs and executing production on the shop floor. PP integrates tightly with MM (material supply), FI (cost postings), and CO (variance analysis). This reading guide covers the five core PP topics tested on the SAP S/4HANA Essentials exam: Bill of Materials, Work Centers, Routings, MRP, and Production Orders.

---

## Section 1 — Core Glossary

**Bill of Materials (BOM)**
A structured list of all components, sub-assemblies, and raw materials required to produce one unit of a finished product, with quantities for each component. The BOM defines the material inputs to production. Transactions CS01 (create), CS03 (display), CS11 (multi-level explosion).

**Single-Level BOM**
Shows only the immediate children of a finished product. Sub-assemblies appear as single line items without showing their own components.

**Multi-Level BOM**
Explodes all levels of the product structure — finished product, sub-assemblies, and raw materials. Used by MRP to calculate total requirements across the entire product hierarchy.

**Base Quantity**
The quantity of the finished product the BOM is defined for — typically 1 unit. All component quantities are proportional to the base quantity. MRP scales all requirements by multiplying the BOM quantities by the planned production quantity.

**Work Center**
The PP representation of a machine, workstation, or production team where manufacturing operations are performed. Contains capacity data (available hours), scheduling data (setup and run times), and costing data (activity type rates). Transactions CR01 (create), CR03 (display).

**Routing**
The ordered sequence of production operations required to manufacture a product. Each operation references a Work Center and defines standard processing times. Routings drive scheduling, capacity planning, and production costing. Transactions CA01 (create), CA03 (display).

**Operation**
A numbered step in a Routing. Operations are numbered in increments of 10 (10, 20, 30...) to allow insertions. Each operation specifies: Work Center, control key, standard values (setup time, machine time, labor time).

**Standard Values**
The planned time parameters for each Routing operation: setup time (per lot), machine time (per unit or per lot), labor time (per unit). Used for scheduling and as the basis for production cost calculation.

**MRP (Material Requirements Planning)**
The SAP planning engine that calculates what materials need to be procured or produced, in what quantities, and by when — based on demand requirements, current stock levels, and open procurement or production orders. MRP transactions: MD01 (plant-level run), MD02 (single material), MD04 (Stock/Requirements List).

**Independent Requirement**
A demand for a finished product that originates externally — from a sales order or a planned independent requirement (forecast). Independent requirements drive MRP calculations at the finished goods level.

**Dependent Requirement**
A demand for a component or raw material that is derived by exploding the BOM of a finished product. Generated automatically by MRP when it explodes the BOM to calculate component needs.

**Planned Order**
A procurement proposal generated by MRP for in-house manufactured materials. A Planned Order is a system suggestion — it must be converted to a Production Order before manufacturing can begin.

**Purchase Requisition (PP-generated)**
A procurement proposal generated by MRP for externally procured materials. Flows directly to SAP MM where a buyer converts it to a Purchase Order. This is the PP-to-MM integration handoff.

**Lot Size**
The rule in the Material Master MRP view that determines how MRP rounds order quantities. Common lot sizes: EX (exact lot size — order exactly what is needed), FX (fixed lot size — always order the same quantity), MB (minimum lot size — never order less than a minimum amount).

**Safety Stock**
A buffer quantity of material maintained to protect against supply delays or unexpected demand spikes. Defined in the Material Master MRP 2 view. MRP treats safety stock as a minimum inventory floor — if stock drops below safety stock, a replenishment order is generated.

**Production Order**
The formal shop floor authorization to manufacture a specific quantity of a material by a specific date. Created by converting a Planned Order (CO40) or directly (CO01). Contains the BOM components, Routing operations, scheduled dates, and cost plan.

**Production Order Status**
The lifecycle state of a Production Order. Standard statuses: CRTD (Created), REL (Released to shop floor), CONF (Confirmed — operations reported), TECO (Technically Complete), CLSD (Closed and settled).

**Order Confirmation (CO11N)**
The transaction used by shop floor workers or supervisors to report actual quantities produced, scrap generated, and actual times used at each Routing operation.

**Order Settlement (KO88)**
The transaction that closes a Production Order financially by comparing actual costs to standard costs and posting any variance to FI variance accounts.

**Production Variance**
The difference between the actual cost of production (actual materials consumed + actual machine and labor times × Work Center rates) and the standard cost of the finished goods produced. Unfavorable variances indicate higher-than-planned production costs.

---

## Section 2 — PP Organizational and Master Data Hierarchy

```text
PLANT (PP Operational Unit)
  |
  +-- MATERIAL MASTER (MRP views)
  |       MRP Type, Lot Size, Safety Stock
  |       In-House Production Time
  |
  +-- BILL OF MATERIALS (CS01)
  |       Component 1: quantity, unit
  |       Component 2: quantity, unit
  |       Sub-assembly: quantity (with its own BOM)
  |
  +-- WORK CENTER (CR01)
  |       Capacity (hours/shift)
  |       Cost Rates (per activity type)
  |       Scheduling Parameters
  |
  +-- ROUTING (CA01)
          Operation 10: Work Center A, 15 min setup, 2 min/unit
          Operation 20: Work Center B, 10 min setup, 8 min/unit
          Operation 30: Work Center C, 5 min setup, 3 min/unit
```

---

## Section 3 — BOM Structure Reference

### BOM Header Fields

| Field | Description |
|---|---|
| Material | The finished product or assembly this BOM defines |
| Plant | The plant where this BOM is valid |
| BOM Usage | Purpose: 1=Production, 5=Sales, 6=Costing |
| Valid From | Date from which BOM is active |
| Base Quantity | Quantity of the finished product the BOM is defined for |

### BOM Item Fields

| Field | Description |
|---|---|
| Item Number | Sequential identifier for the component |
| Component | Material number of the required part |
| Quantity | Amount of the component needed per base quantity |
| Unit of Measure | Unit for the quantity (kg, EA, L, m) |
| Item Category | L=Stock item (from inventory), N=Non-stock, R=Variable size |
| Scrap % | Expected scrap allowance for this component |

### Single-Level vs. Multi-Level BOM

```text
SINGLE-LEVEL BOM for FG-BRACKET-001 (1 unit):
  - TIT-BAR-001 (Titanium Bar Stock): 2.5 kg
  - BOLT-M8 (Bolt Set): 12 EA
  - SA-FRAME (Sub-assembly Frame): 1 EA   <-- shown as 1 unit, not exploded

MULTI-LEVEL BOM EXPLOSION:
  FG-BRACKET-001 (1 unit)
    TIT-BAR-001: 2.5 kg
    BOLT-M8: 12 EA
    SA-FRAME (1 EA)
      STL-PLATE-001 (Steel Plate): 0.8 kg   <-- sub-assembly components shown
      WELD-ROD-003: 0.1 kg
      RIVET-4MM: 8 EA
```

---

## Section 4 — MRP Logic and Calculation

### MRP Calculation Steps

| Step | Description | SAP Action |
|---|---|---|
| 1 — Gross Requirement | Total demand from independent requirements | Read sales orders and PIRs |
| 2 — Available Stock | Current warehouse stock + open orders | Read inventory and open POs/PRs/Prod Orders |
| 3 — Net Requirement | Gross Requirement minus Available Stock | Calculate shortage quantity |
| 4 — Lot Sizing | Apply lot size rule to net requirement | Round to fixed lot, minimum lot, or exact |
| 5 — Procurement Proposal | Generate Planned Order (produced) or PR (purchased) | Create MRP elements in MD04 |
| 6 — Scheduling | Calculate start and finish dates using lead times | Apply production/delivery times |
| 7 — BOM Explosion | Cascade requirements to sub-assembly and component level | Generate dependent requirements |

### MRP Type Reference

| MRP Type Code | Description | Use Case |
|---|---|---|
| PD | MRP (standard demand-driven) | Finished goods and components with predictable demand |
| VB | Reorder Point Planning (manual) | Slow-moving materials; planner sets reorder point manually |
| VM | Reorder Point Planning (automatic) | Automatic reorder point based on historical consumption |
| ND | No Planning | Materials excluded from MRP; managed manually |

### Material Master MRP Key Fields

| Field | View | Description |
|---|---|---|
| MRP Type | MRP 1 | Planning method (PD, VB, VM, ND) |
| Lot Size | MRP 1 | Order quantity rounding rule (EX, FX, MB, etc.) |
| Minimum Lot Size | MRP 1 | Minimum order quantity under MB lot sizing |
| Reorder Point | MRP 1 | Stock level that triggers a replenishment (VB type only) |
| Safety Stock | MRP 2 | Buffer inventory floor; MRP replenishes if stock falls below |
| Planned Delivery Time | MRP 2 | External procurement lead time in calendar days |
| In-House Production Time | MRP 2 | Manufacturing lead time in calendar days |
| Scheduling Margin Key | MRP 2 | Float times before and after production for scheduling buffer |

---

## Section 5 — Production Order Lifecycle

```text
[PLANNED ORDER created by MRP]
         |
         | CO40: Convert Planned Order to Production Order
         | or CO01: Create Production Order directly
         v
[CRTD — CREATED]
  BOM components reserved in MM
  Routing operations scheduled
  Planned cost calculated
         |
         | Release order (CO02 or automatic)
         v
[REL — RELEASED]
  Shop floor can begin production
  Goods Issue allowed (MIGO 261)
         |
         | Post Goods Issue: components withdrawn from inventory
         | Operations confirmed (CO11N): actual times reported
         v
[CONF — CONFIRMED]
  Actual times logged
  Actual costs accumulating on order
         |
         | Post Goods Receipt: finished goods enter inventory (MIGO 101)
         v
[TECO — TECHNICALLY COMPLETE]
  Production finished
  No more goods movements or confirmations
         |
         | KO88: Order Settlement
         v
[CLSD — CLOSED]
  Actual vs. standard cost variance posted to FI
  Order archived
```

---

## Section 6 — Production Order Accounting Entries

| Event | Transaction | Debit | Credit |
|---|---|---|---|
| Goods Issue to Prod Order | MIGO (261) | Production Order (WIP) | Raw Materials Inventory |
| Goods Receipt from Prod Order | MIGO (101) | Finished Goods Inventory | Production Order (WIP) |
| Order Settlement — favorable | KO88 | Production Order (close WIP) | Variance Account (favorable) |
| Order Settlement — unfavorable | KO88 | Variance Account (unfavorable) | Production Order (close WIP) |

---

## Section 7 — PP to MM to FI Integration Flow

```text
[DEMAND MANAGEMENT — MD61]
  Planned Independent Requirements entered
         |
         v
[MRP RUN — MD01]
  BOM exploded to component level
  Net requirements calculated
         |
  In-house materials: Planned Orders
  Purchased materials: Purchase Requisitions
         |              |
         v              v
[PRODUCTION          [MM PROCUREMENT]
 ORDER — CO01]        PR → PO (ME21N)
         |              Goods Receipt (MIGO 101)
  GI: MIGO 261          Invoice (MIRO)
  Components consumed    Payment (F110)
         |
  GR: MIGO 101
  Finished goods in stock
         |
  KO88 Settlement
         |
         v
[FI POSTING]
  Variance account updated
  Inventory asset updated
  WIP cleared to zero
```

---

## Section 8 — Transaction Code Master Reference

| Transaction | Description |
|---|---|
| CS01 / CS03 | Create / Display Bill of Materials |
| CS11 | Display Multi-Level BOM Explosion |
| CS15 | Where-Used List for a Component |
| CR01 / CR03 | Create / Display Work Center |
| CA01 / CA03 | Create / Display Routing |
| CA60 | Where-Used List for Routing |
| MD61 | Create Planned Independent Requirements (demand plan) |
| MD01 | MRP Run (Plant Level) |
| MD02 | MRP Run (Single Material) |
| MD04 | Stock/Requirements List |
| MD05 | MRP List (last MRP run result snapshot) |
| CO01 | Create Production Order |
| CO02 / CO03 | Change / Display Production Order |
| CO40 | Convert Planned Order to Production Order |
| CO11N | Production Order Confirmation |
| MIGO (261) | Goods Issue to Production Order |
| MIGO (101) | Goods Receipt from Production Order |
| KO88 | Production Order Settlement |
| COOIS | Production Order Information System (reporting) |

---

## Section 9 — Exam Tips

> **Exam Tip 1 — BOM and Routing are the two PP master data pillars.** BOM = what materials are needed. Routing = how the product is made (which machines, in what sequence, for how long). Both must exist before a Production Order can be created.

> **Exam Tip 2 — MRP generates Planned Orders and Purchase Requisitions.** For in-house produced materials: Planned Orders. For externally purchased materials: Purchase Requisitions. Know the difference and where each flows next.

> **Exam Tip 3 — MD04 is the production planner's daily tool.** The Stock/Requirements List shows every MRP element — demands, supplies, and available stock balance — over time for one material. A negative available quantity means a shortage requiring action.

> **Exam Tip 4 — Production Order status sequence.** CRTD (created) → REL (released) → CONF (confirmed) → TECO (technically complete) → CLSD (closed). Know what activities are allowed and blocked at each status.

> **Exam Tip 5 — Movement Type 261 is goods issue to a Production Order.** Movement Type 101 for production is goods receipt from a Production Order into finished goods inventory. Know both movement types and the resulting accounting entries.

> **Exam Tip 6 — Order Settlement compares actual to standard cost.** KO88 settles the Production Order. The difference between actual production cost and standard cost is the production variance. Unfavorable variances indicate manufacturing inefficiency.

---

## Section 10 — Study Checklist

- Review the PP master data hierarchy diagram in Section 2.
- Memorize the BOM field table and understand single-level vs. multi-level BOM differences.
- Trace the MRP calculation steps in Section 4 and understand what each step produces.
- Study the Material Master MRP key fields table in Section 4.
- Review the Production Order lifecycle in Section 5 — know all five statuses.
- Study the accounting entries table in Section 6.
- Trace the PP-to-MM-to-FI integration flow in Section 7.
- Memorize the transaction code master reference in Section 8.
- Watch the Module 11 video lecture.
- Complete Lab 11.
- Post to Discussion Forum 11 by Wednesday at 11:59 PM.
- Complete Quiz 11.

---

## 9. Supplemental Resources

**1. SAP Learning — Manufacturing with SAP S/4HANA**
<https://learning.sap.com/learning-journeys/plan-and-manufacture-with-sap-s-4hana>
Official SAP learning journey covering the complete Production Planning process: BOM and Routing master data, MRP planning run, Production Order creation and execution, Goods Issue and Goods Receipt, and order settlement with variance analysis. Maps directly to the transaction codes (CS01, MD01, CO01, CO11N, KO88) tested in this module's quiz and Lab 11.

**2. APICS — Manufacturing Planning and Control for Supply Chain Management**
<https://www.ascm.org/learning-development/certifications-credentials/cpim/>
The ASCM CPIM certification covers Manufacturing Resource Planning (MRP II) theory, BOM structures, capacity requirements planning, and production scheduling — the conceptual foundation underlying SAP PP configuration decisions. Particularly relevant to MRP netting logic, lot sizing rules, and Make-to-Order vs. Make-to-Stock environments covered in this module.

**3. SAP Help Portal — Production Orders in SAP S/4HANA**
<https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/production-planning>
Official SAP documentation for Production Planning. Covers Production Order lifecycle management (statuses CRTD through CLSD), operation confirmation, movement types for Goods Issue and Goods Receipt, and the PP-MM-FI-CO integration points — essential reference for understanding the accounting entries and integration flows analyzed in Lab 11.
