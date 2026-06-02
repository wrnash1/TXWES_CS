# Reading Guide: Module 06 - Supply Chain Management Integrations

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

Supply Chain Management (SCM) is the operational engine of any company that sources, makes, or moves physical goods. ERP's most visible value proposition for manufacturers and distributors is the real-time visibility and coordination that SCM modules provide. When a sales order is entered in SD, the MRP engine in MM immediately sees the demand, checks inventory, and generates procurement or production proposals — all without a phone call, email, or spreadsheet. This module covers SAP MM, MRP, the Procure-to-Pay process, inventory valuation, and supply chain integration architecture.

---

## Section 1: High-Yield Glossary

**Materials Management (SAP MM)**
The SAP module responsible for procurement, inventory management, and warehouse management. MM is the operational backbone of supply chain in SAP, managing the full lifecycle of materials from purchase requisition through vendor payment.

**Material Master**
The central master data record for every product or raw material in SAP. The material master contains procurement parameters, inventory management settings, costing data, quality inspection rules, and storage location information. Every goods movement references a material master record.

**Vendor Master**
The central master data record for every supplier. The vendor master contains commercial data (address, payment terms, bank details) and purchasing data (ordering currency, delivery tolerance). No purchase order can be created without a valid vendor master record.

**Bill of Materials (BOM)**
A structured list of all components required to produce a finished product, including quantities and unit of measure. SAP uses the BOM as input to MRP — when demand exists for a finished product, MRP explodes the BOM to determine what components must be procured or produced.

**Material Requirements Planning (MRP)**
The planning algorithm that calculates net material requirements by comparing demand (sales orders, forecasts, production orders) against available supply (current stock, open POs, open production orders) and generates procurement and production proposals. SAP MRP transaction: MD01 (mass run), MD02 (single material).

**Purchase Requisition (PR)**
An internal SAP document requesting that the purchasing department procure a material or service. A PR is not sent to vendors; it is an authorization request within the company. Created manually or automatically by MRP.

**Purchase Order (PO)**
An external SAP document issued to a vendor confirming the commitment to buy a material or service at an agreed price and delivery date. The PO is the legal offer in the procurement contract. SAP transaction: ME21N.

**Goods Receipt (GR)**
The SAP transaction (MIGO) that records the physical arrival of goods at the warehouse. Posting a goods receipt increases the inventory quantity and posts a financial entry: Debit Inventory Account, Credit GR/IR Clearing Account.

**GR/IR Clearing Account**
A balance sheet transit account that represents goods received but not yet invoiced. When a goods receipt is posted, the GR/IR account is credited. When the vendor invoice is processed, the GR/IR account is debited, clearing the transit balance. The account should have a zero balance after full invoice posting.

**Goods Issue**
The SAP transaction that records materials leaving the warehouse for a specific purpose — issued to a production order, delivered to a customer, scrapped. Posting a goods issue decreases inventory quantity and posts the relevant financial entry.

**Standard Price**
An inventory valuation method where each material is valued at a predetermined standard cost. Differences between the standard price and actual purchase price are posted to a price variance account. Common in manufacturing environments.

**Moving Average Price (MAP)**
An inventory valuation method where the average unit cost is recalculated with each goods receipt. The new average blends the cost of existing stock with the cost of new receipts. Common in trading and distribution environments.

**Vendor Evaluation**
SAP functionality that scores vendors on delivery reliability, quality performance, and pricing compliance. Scores are used to rank preferred suppliers and identify underperforming vendors requiring corrective action.

**Reorder Point**
The inventory level at which a procurement proposal is automatically triggered by MRP. The reorder point is configured in the material master and accounts for expected demand during the procurement lead time plus safety stock.

**Safety Stock**
The minimum inventory buffer maintained to absorb demand variability and supply uncertainty. Safety stock prevents stockout conditions when demand spikes or supply is delayed. Configured in the material master MRP views.

**Lead Time**
The time from placing a purchase order to receiving the goods at the warehouse. Lead time is a critical input to MRP calculations — MRP must place orders early enough for goods to arrive before stock reaches zero.

---

## Section 2: Procure-to-Pay (P2P) Process Reference

### Complete P2P Flow

```text
[Demand Identified]
(MRP proposal or manual request)
          |
[Purchase Requisition (ME51N)]
 Internal document, not sent to vendor
          |
[Requisition Approval]
 Manager approves within SAP workflow
          |
[Purchase Order (ME21N)]
 External document sent to vendor
 Financial commitment created
          |
[Vendor Ships Goods]
          |
[Goods Receipt (MIGO)]
 GL: Dr Inventory / Cr GR/IR Clearing
 Stock quantity increases
          |
[Invoice Verification (MIRO)]
 Three-way match: PO + GR + Invoice
          |
 [XOR: Match passes?]
        |              |
      YES             NO
        |              |
 Invoice approved   Invoice blocked
 GL: Dr GR/IR /     Work item for AP
     Cr Vendor AP
        |
[Automatic Payment Run (F110)]
 GL: Dr Vendor AP / Cr Bank
```

### SAP P2P Transaction Codes

| Step | Transaction Code | Document Created |
|---|---|---|
| Create Purchase Requisition | ME51N | Purchase Requisition |
| Display/Change Requisition | ME52N | (updates PR) |
| Create Purchase Order | ME21N | Purchase Order |
| Display Purchase Order | ME23N | (view only) |
| Post Goods Receipt | MIGO | Material Document + FI Document |
| Enter Vendor Invoice | MIRO | Invoice Document + FI Document |
| Run Automatic Payments | F110 | Payment Document |
| Display Material Document | MB03 | (view only) |

---

## Section 3: MRP Logic — Detailed Flow

### MRP Input/Output Model

| Input | Description | SAP Source |
|---|---|---|
| Gross requirements | Demand from sales orders and forecasts | Sales orders (SD), demand planning |
| Current stock | Available inventory by material and plant | Inventory management (MM-IM) |
| Open purchase orders | Orders already placed with vendors | Purchase orders (MM-PUR) |
| Open production orders | Manufacturing orders in progress | Production planning (PP) |
| Bill of materials | Component list for each finished product | BOM (CS module) |
| Planning parameters | Lead times, safety stock, reorder points | Material master (MM) |

### MRP Net Requirements Calculation

```text
Gross Requirement (demand)
  minus: Current Available Stock
  minus: Open Purchase Orders (scheduled receipt)
  minus: Open Production Orders (scheduled receipt)
  equals: NET REQUIREMENT

If Net Requirement > 0:
  → Generate Purchase Requisition (for external procurement)
  → Generate Planned Order (for internal production)
```

### MRP Planning Strategies

| Strategy | Description | Best Used For |
|---|---|---|
| MTO (Make to Order) | Production starts only when a customer order is received | Custom/configured products |
| MTS (Make to Stock) | Production runs based on forecast to build inventory in advance | Standard high-volume products |
| Assemble to Order | Standard subassemblies built to stock; final assembly triggered by order | Configurable products with common subassemblies |

---

## Section 4: Inventory Management — Goods Movements

| Movement Type | Description | Stock Effect | Financial Posting |
|---|---|---|---|
| 101 | Goods Receipt for Purchase Order | Stock increases | Dr Inventory, Cr GR/IR Clearing |
| 201 | Goods Issue to Cost Center | Stock decreases | Dr Cost Center Expense, Cr Inventory |
| 261 | Goods Issue to Production Order | Stock decreases | Dr WIP/Production, Cr Inventory |
| 311 | Transfer Posting: Storage Location to Storage Location | No net change | No financial posting |
| 501 | Receipt without Purchase Order | Stock increases | Dr Inventory, Cr Inventory Adjustment |
| 551 | Scrapping — write-off | Stock decreases | Dr Scrap Expense, Cr Inventory |
| 601 | Goods Issue for Delivery to Customer (SD) | Stock decreases | Dr COGS, Cr Inventory |

These movement type codes are referenced in SAP MIGO and are useful for understanding what financial impacts different warehouse operations create.

---

## Section 5: Supply Chain Integration Architecture

### MM Integration with Other Modules

```text
[Sales and Distribution (SD)]
  Sales Order demand
          |
          v
[Materials Management (MM)]
  MRP calculates net requirements
          |
    +-----+------+
    |             |
    v             v
[Purchase     [Production
 Order         Planning (PP)]
 (External)]   Production Order
    |             |
    v             v
[Goods        [Goods Issue
 Receipt]      to Production]
    |             |
    v             v
[FI-AP        [FI-GL
 Invoice       Inventory
 Processing]   Valuation]
```

### Cross-Module Integration Points

| Integration | From Module | To Module | Trigger | Data Exchanged |
|---|---|---|---|---|
| Sales order to MRP | SD | MM | Sales order created | Material, quantity, delivery date |
| MRP to Purchase Requisition | MM-MRP | MM-PUR | MRP run | Material, quantity, need date |
| Goods Receipt to FI | MM-IM | FI-GL | MIGO posting | Inventory value, GR/IR posting |
| Invoice to FI | MM-LIV | FI-AP | MIRO posting | Invoice amount, vendor payable |
| Delivery to Inventory | SD | MM-IM | Goods Issue (601) | Stock quantity reduction |
| Production Order consumption | PP | MM-IM | Goods Issue (261) | Component quantity reduction |

---

## Section 6: SCM Module Comparison — SAP vs. Oracle vs. Salesforce

| SCM Function | SAP S/4HANA | Oracle Cloud SCM | Salesforce |
|---|---|---|---|
| Procurement | MM — Purchasing (ME21N, F110) | Oracle Procurement Cloud | Not applicable |
| Inventory Management | MM — Inventory (MIGO) | Oracle Inventory Management | Not applicable |
| Warehouse Management | EWM (Extended Warehouse Mgmt) | Oracle WMS Cloud | Not applicable |
| Material Requirements Planning | MRP (MD01) | Oracle Planning Central | Not applicable |
| Production Planning | PP (CO01) | Oracle Manufacturing | Not applicable |
| Demand Planning | IBP (Integrated Business Planning) | Oracle Demand Management | Not applicable |
| Order Management | SD — Sales Orders (VA01) | Oracle Order Management | Salesforce Order Management |
| Vendor Performance | ME61 (Vendor Evaluation) | Oracle Supplier Qualification | Not applicable |

Salesforce's role in supply chain is primarily in order management (connecting sales pipeline to order fulfillment) and supplier portal solutions, not in core procurement or inventory management.

---

## Section 7: Inventory Valuation Comparison

| Dimension | Standard Price | Moving Average Price |
|---|---|---|
| Unit cost method | Predetermined fixed cost | Weighted average, recalculated each receipt |
| Price variance treatment | Separate variance account | Absorbed into inventory value |
| Best for | Manufacturing with stable BOMs | Trading, distribution |
| Balance sheet stability | High (cost is fixed) | Can fluctuate with market prices |
| Management reporting | Clear variance analysis | Reflects actual market costs |
| SAP price indicator | S (Standard) | V (Moving Average) |

---

## Section 8: Certification Exam Tips

1. **Know the P2P transaction codes.** ME21N (Purchase Order), MIGO (Goods Receipt), MIRO (Invoice), F110 (Payment Run), MD01 (MRP) are high-frequency on the SAP Associate exam.

2. **Purchase Requisition is internal; Purchase Order is external.** A PR requests procurement internally; a PO is a legal commitment sent to a vendor. If asked which document is sent to the vendor, the answer is PO.

3. **MRP outputs are proposals, not firm orders.** MRP generates purchase requisitions and planned orders that a human planner reviews and converts. MRP does not place purchase orders automatically.

4. **The GR/IR clearing account is the transit bridge between goods receipt and invoice.** It should net to zero after all invoices for received goods are posted.

5. **Safety stock prevents stockouts; reorder point triggers replenishment.** Know what each parameter means in the MRP context.

6. **Standard Price posts variances; Moving Average Price absorbs them.** On valuation questions, identify what happens to the difference between the actual purchase price and the standard price.

7. **Vendor evaluation is in MM — transaction ME61.** When a scenario asks how to identify underperforming suppliers, the answer involves vendor evaluation scoring.

8. **MM and FI are tightly integrated.** Every goods movement in MM produces a corresponding financial document in FI. This automatic dual-document posting is a core ERP architecture concept.

---

## Section 9: Required Trailhead and Study Resources

Complete before attempting the quiz:

- **Salesforce Trailhead — Salesforce Order Management**
  URL: trailhead.salesforce.com — search "Salesforce Order Management Basics"
  Covers how Salesforce handles order fulfillment — relevant for understanding CRM-SCM integration.

- **Salesforce Trailhead — Manufacturing Cloud Basics**
  URL: trailhead.salesforce.com — search "Manufacturing Cloud Basics"
  Covers Salesforce's industry cloud for manufacturing — relevant for understanding how CRM connects to supply chain planning.

---

## Section 10: Study Checklist

- Memorize the P2P transaction codes and the document each creates.
- Trace through the P2P flow diagram in Section 2 without looking at labels.
- Study the MRP net requirements formula in Section 3. Practice applying it with a simple example.
- Review the goods movement types in Section 4. Know which movements increase vs. decrease stock.
- Study the cross-module integration table in Section 5. Know what triggers data flow between MM and FI.
- Review the inventory valuation comparison in Section 7. Know when Standard vs. Moving Average is used.
- Complete the Salesforce Trailhead "Salesforce Order Management Basics" module.
- Watch the Module 06 video lecture.
- Complete Lab 06.
- Post to Discussion Forum 06 by Wednesday at 11:59 PM.
- Complete Quiz 06 (10 questions).
