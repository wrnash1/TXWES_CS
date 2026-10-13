# Lab Activity: Module 06 - Supply Chain Management Integrations

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab develops your ability to trace the Procure-to-Pay process through SAP MM, analyze MRP net requirements calculations, classify goods movements by financial impact, and evaluate inventory valuation methods in a manufacturing context. All work is analytical and scenario-based.

**Estimated Time:** 90 minutes

**Submission:** Upload to Canvas under "Lab 06 — Supply Chain Management Integrations."

---

## Learning Objectives

By completing this lab you will be able to:

- Trace each step of the Procure-to-Pay process and identify the SAP transaction and document created at each step
- Apply the MRP net requirements formula to calculate procurement proposals
- Classify goods movement types by their effect on stock quantity and financial postings
- Compare Standard Price and Moving Average Price valuation outcomes for the same goods receipt
- Analyze cross-module integration triggers between MM, FI, SD, and PP

---

## Scenario Background

**Company:** Hartwell Industrial Components

**Industry:** Contract metal fabrication — produces structural steel assemblies for commercial construction

**Size:** 480 employees, $95 million revenue

**ERP:** SAP S/4HANA, implemented 18 months ago

**Supply chain team:** Purchasing manager, 2 buyers, 2 warehouse clerks, 1 materials planner

Hartwell has been live on SAP for a year and a half. The materials planner has identified three problem areas she wants help analyzing before the next MRP run.

---

## Part A: Procure-to-Pay Process Tracing (30 points)

### A-1: P2P Step Identification

Hartwell's purchasing team is procuring a shipment of raw steel coil from a new vendor. The following events occur in sequence. For each event, identify: (1) the SAP transaction code used, (2) the SAP document created, and (3) the financial journal entry posted (if any).

| Event | SAP Transaction | Document Created | Journal Entry (Dr / Cr) |
|---|---|---|---|
| The MRP run determines that 20 coils of raw steel are needed within 14 days and generates an internal request to the purchasing department | | | |
| The purchasing manager selects the vendor and issues the formal commitment to buy 20 coils at $1,800 each | | | |
| The vendor ships the coils; the warehouse receives and counts all 20 coils and records their arrival in SAP | | | |
| The vendor's invoice arrives for 20 coils at $1,800 each ($36,000); SAP compares it to the PO and GR | | | |
| The three-way match passes; the automatic payment run pays the vendor | | | |

### A-2: GR/IR Clearing Account Analysis

The GR/IR clearing account is a transit account that bridges the goods receipt and invoice verification steps.

Answer the following questions in complete sentences:

1. What is the balance in the GR/IR clearing account immediately after the goods receipt is posted for the 20 steel coils (before the invoice is processed)?

2. What happens to the GR/IR clearing account balance after the vendor invoice is verified and approved?

3. What does a non-zero GR/IR clearing account balance at month-end indicate? Name two possible causes.

---

## Part B: MRP Net Requirements Calculations (25 points)

### B-1: Net Requirements Formula Application

The Hartwell materials planner provides you with the following data for three materials going into the next MRP run. Apply the MRP net requirements formula to each material and determine whether a procurement proposal should be generated.

**MRP Formula:**

```text
Net Requirement = Gross Requirement
                  minus Current Available Stock
                  minus Open Purchase Orders (scheduled receipts)
                  minus Open Production Orders (scheduled receipts)

If Net Requirement > 0: Generate procurement proposal
If Net Requirement <= 0: No action required
```

**Material Data:**

| Material | Gross Requirement | Current Stock | Open POs | Open Prod. Orders | Net Requirement | Action |
|---|---|---|---|---|---|---|
| Steel Bracket A12 | 800 units | 300 units | 200 units | 0 units | | |
| Weld Rod WR-05 | 1,200 units | 1,500 units | 0 units | 0 units | | |
| Bolt Assembly BA-7 | 2,500 units | 400 units | 500 units | 300 units | | |

Show your calculation for each material and state whether a procurement proposal is generated.

### B-2: MRP Planning Strategy Selection

Hartwell produces two product families with very different demand patterns. For each product family, recommend the appropriate MRP planning strategy (Make to Order, Make to Stock, or Assemble to Order) and explain your reasoning in 2-3 sentences per product.

**Product Family 1 — Standard Angle Iron:** A commodity item sold in large volumes to repeat customers. Demand is relatively predictable and Hartwell maintains finished goods inventory to ship same-day.

**Product Family 2 — Custom Fabricated Frames:** Engineered-to-order assemblies built to customer specifications. Each order requires a unique cut list and weld sequence that cannot be prepared in advance.

---

## Part C: Goods Movements and Inventory Valuation (25 points)

### C-1: Movement Type Classification

For each warehouse event at Hartwell, identify the SAP goods movement type (from the standard movement types: 101, 201, 261, 311, 501, 551, 601), describe the effect on stock quantity, and identify the financial posting.

| Warehouse Event | Movement Type | Stock Effect | Financial Posting |
|---|---|---|---|
| Raw steel coils received against a purchase order | | | |
| Steel brackets issued to a production order for fabrication | | | |
| Finished assemblies shipped to a customer via a delivery | | | |
| Defective weld rod written off after quality inspection | | | |
| Materials transferred from the main warehouse to the on-site staging area (different storage location, same plant) | | | |
| Raw material received without a purchase order due to an emergency drop shipment | | | |

### C-2: Inventory Valuation Comparison

Hartwell is deciding whether to use Standard Price or Moving Average Price for their raw steel inventory. The following scenario applies to both methods.

**Scenario Data:**

- Current stock: 50 coils valued at $1,600 each (total: $80,000)
- New goods receipt: 100 coils purchased at $1,850 each (total: $185,000)

Complete both valuation calculations:

**Standard Price Calculation (standard price = $1,600):**

Show the journal entry for the goods receipt. Identify what happens to the $250-per-coil price variance.

**Moving Average Price Calculation:**

Calculate the new Moving Average Price after the receipt. Show the formula. State the new total inventory value and new per-unit MAP.

**Analysis (3-5 sentences):** Based on your calculations, explain which valuation method would produce more stable financial reporting for Hartwell and which would better reflect current market costs. Under what business conditions would each method be preferred?

---

## Part D: Cross-Module Integration Analysis (20 points)

### D-1: Integration Trigger Mapping

For each business event at Hartwell, identify the originating SAP module, the receiving SAP module, the trigger that initiates the data flow, and the data exchanged.

| Business Event | Originating Module | Receiving Module | Trigger | Data Exchanged |
|---|---|---|---|---|
| A customer places a large order for steel assemblies; MRP needs to know about this demand | | | | |
| Hartwell posts a goods receipt for raw steel; the financial team needs the inventory value updated | | | | |
| A production order is released to the shop floor; raw materials must be consumed from inventory | | | | |
| A vendor invoice is approved and cleared; the accounts payable sub-ledger must be updated | | | | |

### D-2: Integration Architecture Reflection

The Hartwell operations manager says: "I don't understand why we need all these different modules. Can't we just have one system that tracks everything?" In 150-200 words, explain why the modular architecture of SAP is actually the source of its integration power rather than a limitation. Use at least two specific cross-module data flows from Hartwell's scenario to support your answer.

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: P2P step identification | 15 | All 5 steps with correct transaction codes, documents, and journal entries |
| A-2: GR/IR clearing account analysis | 15 | Correct balance descriptions and two causes of non-zero month-end balance |
| B-1: Net requirements calculations | 15 | All three materials calculated correctly with pass/fail determination |
| B-2: Planning strategy selection | 10 | Correct strategy for each product family with valid reasoning |
| C-1: Movement type classification | 15 | All six events mapped to correct movement type, stock effect, and financial posting |
| C-2: Inventory valuation comparison | 10 | Both calculations correct; 3-5 sentence analysis addresses stability vs. market cost trade-off |
| D-1: Integration trigger mapping | 10 | All four integration points correctly mapped with trigger and data exchanged |
| D-2: Integration architecture reflection | 10 | 150-200 words; modular integration concept explained; two specific data flows cited |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile all responses into a single document.
2. Name your file: `Lab06_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 06 — Supply Chain Management Integrations."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day.

---

## Part 9 — Challenge Exercise

### Challenge 1: MRP Master Data Configuration Design

A contract electronics manufacturer is implementing SAP MM. They produce three product categories: (1) standard circuit boards (high volume, predictable demand, 20+ vendors available), (2) custom ASIC chips (made-to-order, single-source vendor, 12-week lead time), and (3) passive components (very high volume, commodity, safety stock approach). You are configuring the material master MRP views.

1. For each product category, specify the recommended MRP type (reorder point, MRP, consumption-based, make-to-order), lot-sizing procedure, and safety stock strategy. Justify each choice with reference to the product's demand characteristics.
2. For the custom ASIC chips, calculate the required reorder point given: average weekly consumption = 50 units, planned delivery time = 84 days (12 weeks), safety stock = 2 weeks of average consumption.
3. Design the source list configuration for the standard circuit boards: identify what information would be stored for each of the 20+ vendors, and explain how SAP uses the source list during automatic purchase order creation.
4. Explain why using Moving Average Price (rather than Standard Price) is more appropriate for the passive components category, and describe one scenario where Standard Price would be preferred even for high-volume commodities.

### Challenge 2: Supply Chain Disruption Response Planning

An automotive parts supplier experiences a sudden shortage of a critical steel alloy due to a supplier bankruptcy. The company has 15 days of stock remaining for the alloy, three alternative suppliers (none pre-qualified), and production commitments to three major customers in the next 30 days.

1. Define the immediate (0-48 hour) actions the supply chain team should take in the ERP system, specifying which SAP transactions are involved and what data must be updated.
2. Map the cross-module impacts of the shortage on SD (customer commitments), PP (production scheduling), FI (accruals for premium sourcing costs), and MM (emergency procurement). For each module, identify one specific document or configuration that must be created or changed.
3. Design a vendor qualification checklist with six criteria for emergency supplier approval. For each criterion, explain why it matters in a 48-hour qualification scenario versus a standard 3-month qualification process.

### Reflection Questions

1. MRP is often described as a "push" planning system — it schedules production based on forecasted demand. How does this create risk in volatile demand environments, and what more advanced planning approach (think beyond standard MRP) would address this limitation?
2. The supply chain disruption scenario required cross-module coordination between SD, PP, MM, and FI. In a company without integrated ERP, how would this same disruption be managed, and what specific information gaps would make the response slower and less accurate?
