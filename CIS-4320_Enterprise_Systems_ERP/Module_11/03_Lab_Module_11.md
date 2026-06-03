# Lab Activity: Module 11 — SAP Production Planning (PP Module)

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: SAP S/4HANA Essentials

---

## Lab Overview

This lab develops your ability to analyze Bill of Materials structures, trace MRP calculation logic, map the Production Order lifecycle, interpret accounting entries for production transactions, and diagnose PP-to-MM-to-FI integration flows. All work is analytical and scenario-based using the Precision Aero Components company scenario below.

**Estimated Time:** 90 minutes

**Submission:** Upload to Canvas under "Lab 11 -- SAP Production Planning."

---

## Learning Objectives

By completing this lab you will be able to:

- Identify the correct SAP PP transaction code for each master data and execution activity
- Trace MRP calculation logic from gross requirement through procurement proposal
- Map the Production Order status lifecycle and identify allowed activities at each status
- Construct journal entries for Goods Issue, Goods Receipt, and Order Settlement
- Analyze a PP-to-MM-to-FI integration flow and identify the module handoff points

---

## Scenario Background

**Company:** Precision Aero Components, Inc. (PAC)

**Industry:** Aerospace and defense subcontracting — precision-machined structural parts

**SAP Environment:** SAP S/4HANA, single plant (Plant 1000 — Dallas Manufacturing), one Company Code (PAC1)

**Product:** FG-AILERON-200 — a finished aluminum aileron bracket assembly produced for a commercial aviation customer

**Bill of Materials for FG-AILERON-200 (Base Quantity: 1 unit):**

| Item | Component | Description | Quantity | UOM |
|---|---|---|---|---|
| 10 | ALU-BAR-6061 | Aluminum Bar Stock 6061-T6 | 3.2 | kg |
| 20 | BOLT-M10-SS | Stainless Steel Bolt Set M10 | 8 | EA |
| 30 | SEAL-RING-12 | Rubber Seal Ring 12mm | 4 | EA |
| 40 | SA-BRACKET-CORE | Sub-assembly: Core Bracket Frame | 1 | EA |

**BOM for SA-BRACKET-CORE (Base Quantity: 1 unit):**

| Item | Component | Description | Quantity | UOM |
|---|---|---|---|---|
| 10 | STL-PLATE-4MM | Steel Plate 4mm | 0.9 | kg |
| 20 | RIVET-5MM | Aluminum Rivet 5mm | 12 | EA |
| 30 | WELD-WIRE-308 | Welding Wire 308L | 0.05 | kg |

**Routing for FG-AILERON-200:**

| Op | Description | Work Center | Setup Time | Machine Time | Labor Time |
|---|---|---|---|---|---|
| 10 | Cut to Length | CNC-SAW-02 | 20 min | 4 min/unit | — |
| 20 | CNC Mill Profile | CNC-MILL-07 | 30 min | 12 min/unit | — |
| 30 | Weld Sub-Assembly | WELD-CELL-01 | 15 min | — | 25 min/unit |
| 40 | Deburr and Clean | CLEAN-02 | — | — | 8 min/unit |
| 50 | Quality Inspection | QA-AERO | 10 min | — | 10 min/unit |

**Material Master MRP Settings for FG-AILERON-200:**

- MRP Type: PD (standard MRP)
- Lot Size: EX (exact lot size)
- In-House Production Time: 5 calendar days
- Safety Stock: 10 units

---

## Part A: Transaction Code Mapping (20 points)

### A-1: Master Data Transactions

For each PP master data activity below, provide the correct SAP transaction code and a one-sentence description of what that transaction does. Use the transaction codes from the Module 11 reading guide.

| Activity | Transaction Code | One-Sentence Description |
|---|---|---|
| Create the BOM for FG-AILERON-200 | | |
| Display the multi-level BOM explosion for FG-AILERON-200 to see SA-BRACKET-CORE components | | |
| Display the Work Center CNC-MILL-07 to review its capacity and cost rates | | |
| Create the Routing for FG-AILERON-200 | | |
| Find all finished goods that use ALU-BAR-6061 as a BOM component | | |

### A-2: Planning and Execution Transactions

For each PP planning and execution activity below, provide the correct transaction code.

| Activity | Transaction Code |
|---|---|
| Run MRP for all materials at Plant 1000 | |
| View the Stock/Requirements List for ALU-BAR-6061 to check current demand and supply | |
| Enter the demand plan — 200 units of FG-AILERON-200 needed by July 31 | |
| Convert a Planned Order for FG-AILERON-200 into a Production Order | |
| Confirm that Operation 20 (CNC Mill Profile) is complete on Production Order 1000042 | |
| Post Goods Issue of ALU-BAR-6061 to Production Order 1000042 | |
| Post Goods Receipt of finished FG-AILERON-200 units from Production Order 1000042 | |
| Settle Production Order 1000042 to transfer variances to FI | |

---

## Part B: BOM Analysis and MRP Calculation (30 points)

### B-1: BOM Structure Analysis

Answer the following questions about the PAC BOM structure.

1. PAC's planner runs transaction CS03 on FG-AILERON-200 and sees four line items: ALU-BAR-6061, BOLT-M10-SS, SEAL-RING-12, and SA-BRACKET-CORE. Is this a single-level or multi-level BOM display? Explain how you know.

2. The planner then runs CS11. What additional information appears that was not visible in CS03? List the specific components that would now appear for the first time.

3. PAC receives a sales order for 50 units of FG-AILERON-200. Using the multi-level BOM, calculate the total quantities of each raw material required to fill this order. Show your calculations.

| Component | BOM Qty (per FG unit) | Required for 50 units |
|---|---|---|
| ALU-BAR-6061 | | |
| BOLT-M10-SS | | |
| SEAL-RING-12 | | |
| STL-PLATE-4MM | | |
| RIVET-5MM | | |
| WELD-WIRE-308 | | |

### B-2: MRP Calculation

PAC's planner reviews MD04 for FG-AILERON-200 on June 1. The following data is available:

- Gross Requirement (from sales order): 50 units, needed by June 20
- Current warehouse stock: 18 units
- Safety Stock: 10 units
- Open Production Orders (not yet delivered): 0 units
- MRP Type: PD | Lot Size: EX | In-House Production Time: 5 days

Answer the following MRP calculation questions:

1. Calculate the Available Stock that MRP will use in its net requirement calculation. (Hint: Available Stock = Current Stock minus Safety Stock for PD type with safety stock defined.)

2. Calculate the Net Requirement. Show your formula.

3. Given the EX (exact) lot size rule, what quantity will MRP propose in the Planned Order?

4. Working backward from the June 20 requirement date and using the 5-day In-House Production Time, what will be the scheduled start date of the Planned Order?

5. MRP explodes the BOM to calculate dependent requirements. What transaction code would the planner check to see if ALU-BAR-6061 has sufficient supply to cover the dependent requirement generated for this production run?

6. For ALU-BAR-6061 (an externally purchased material), what type of procurement proposal does MRP generate — a Planned Order or a Purchase Requisition? Explain why.

---

## Part C: Production Order Lifecycle (25 points)

### C-1: Status Sequence Analysis

The Production Order for 50 units of FG-AILERON-200 (Order 1000042) was created on June 3 and is progressing through its lifecycle. For each status below, answer the questions.

**Status: CRTD (Created)**

1. What two master data objects did SAP automatically copy into Production Order 1000042 when it was created?
2. What financial action did SAP take in MM when the order reached CRTD status?
3. Can the shop floor begin production at CRTD status? What must happen first?

**Status: REL (Released)**

4. What goods movement is now allowed that was blocked at CRTD status?
5. What transaction and Movement Type does the warehouse team use to withdraw ALU-BAR-6061 from inventory for this order?

**Status: CONF (Confirmed)**

6. The CNC-MILL-07 operator completes Operation 20 and reports 50 units produced, 0 scrap, actual machine time of 620 minutes (versus planned 12 min × 50 = 600 minutes). What transaction does the operator use to record this?
7. The 20-minute overrun on CNC-MILL-07 will affect what on the Production Order? (Choose: scheduled dates / planned cost / actual cost accumulation)

**Status: TECO (Technically Complete)**

8. After the Goods Receipt of 50 completed FG-AILERON-200 units is posted, the planner sets the order to TECO. What two activities are now blocked that were previously allowed?

**Status: CLSD (Closed)**

9. What transaction settles the Production Order and what does settlement calculate?
10. If actual costs on Order 1000042 were $48,200 and the standard cost of 50 units of FG-AILERON-200 is $950 per unit ($47,500 total), what is the production variance? Is it favorable or unfavorable?

### C-2: Scenario — Partial Confirmation

PAC's shop floor supervisor posts a partial confirmation for Operation 20: reports 30 units complete out of 50. The remaining 20 units have not been confirmed.

1. Can PAC post a Goods Receipt for the 30 completed units at this point, or must all 50 units be confirmed first?
2. What does the partial confirmation mean for the actual cost accumulation on the Production Order — is cost proportional to confirmed quantity?
3. If the remaining 20 units are later scrapped due to a material defect, how should the supervisor handle the final confirmation? What quantity fields are populated?

---

## Part D: Accounting Entries and Integration Analysis (25 points)

### D-1: Journal Entries

For each production transaction below, write the complete journal entry (Debit and Credit accounts, amounts). Use the BOM quantities and standard costs provided.

**Standard cost data:**

- Standard cost of ALU-BAR-6061: $8.50/kg
- Standard cost of BOLT-M10-SS: $0.75/EA
- Standard cost of SEAL-RING-12: $1.20/EA
- Standard cost of SA-BRACKET-CORE sub-assembly: $22.00/EA
- Standard cost of FG-AILERON-200 (finished unit): $950.00/EA

**Transaction 1 — Goods Issue (MIGO, Movement Type 261)**

PAC posts the Goods Issue of ALU-BAR-6061 for the full order quantity (50 units × 3.2 kg = 160 kg). Write the journal entry.

| | Account | Amount |
|---|---|---|
| Debit | | |
| Credit | | |

**Transaction 2 — Goods Receipt (MIGO, Movement Type 101)**

PAC completes production and posts the Goods Receipt for 50 units of FG-AILERON-200 at standard cost ($950 × 50 = $47,500). Write the journal entry.

| | Account | Amount |
|---|---|---|
| Debit | | |
| Credit | |

**Transaction 3 — Order Settlement (KO88) — Unfavorable Variance**

After all postings, actual costs on Order 1000042 total $48,800. Standard cost of goods produced is $47,500. Write the settlement journal entry to close the Production Order.

| | Account | Amount |
|---|---|---|
| Debit | | |
| Credit | | |

### D-2: Integration Flow Analysis

Trace the PP-to-MM-to-FI integration for the PAC FG-AILERON-200 production run. Answer each question in one to two sentences.

1. When MRP ran and generated a Purchase Requisition for ALU-BAR-6061, which SAP module was responsible for converting that PR to a Purchase Order? What transaction code did the buyer use?

2. When ALU-BAR-6061 was received from the vendor (Goods Receipt in MM), what accounting entry was generated in FI? Which account serves as the temporary bridge between the GR and the vendor invoice?

3. When the Production Order issued ALU-BAR-6061 from inventory (Movement Type 261), what happened to the MM inventory balance and what happened to the Production Order in CO?

4. When the Production Order posted the Goods Receipt for 50 units of FG-AILERON-200 (Movement Type 101), which FI account increased? Which account was reduced?

5. When KO88 settled the Production Order and posted the $1,300 unfavorable variance, to which module did the variance flow, and what management report would a controller use to analyze production variances across all orders?

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Master data transaction codes | 10 | 5 transaction codes correct with accurate descriptions |
| A-2: Planning and execution transaction codes | 10 | 8 transaction codes correct |
| B-1: BOM analysis — structure type and explosion | 12 | Single vs. multi-level identified correctly; CS11 components listed; quantity table calculated correctly |
| B-2: MRP calculation steps | 18 | Available stock, net requirement, lot size, start date, procurement proposal type — all correct with formulas shown |
| C-1: Production Order lifecycle questions 1–10 | 20 | All 10 lifecycle questions answered correctly with SAP terminology |
| C-2: Partial confirmation scenario | 5 | All 3 partial confirmation questions answered accurately |
| D-1: Journal entries — 3 transactions | 12 | All 3 entries correct (debit/credit accounts and amounts) |
| D-2: Integration flow analysis — 5 questions | 13 | All 5 integration questions answered with correct module references |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile all responses into a single document.
2. Name your file: `Lab11_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 11 -- SAP Production Planning."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day.
