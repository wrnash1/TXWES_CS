# Video Script: Module 10 — SAP Materials Management (MM Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Salesforce Administrator / SAP S/4HANA Essentials

---

## SEGMENT 1 — Introduction: What MM Does and Why It Matters (0:00–2:30)

Welcome back. I'm Professor Nash, and this is Module 10 of CIS-4320 Enterprise Systems and ERP.

In Module 9 we covered the financial side of SAP — the FI module, where every transaction ultimately lands in the General Ledger. Now we look at the operational engine that generates most of those transactions: the Materials Management module, or SAP MM.

SAP MM manages everything a company does to acquire goods and materials — from recognizing that you need something, to placing an order with a vendor, to receiving the goods, to paying the invoice. This is the Procure-to-Pay cycle, and it is one of the most important business processes in any manufacturing, distribution, or retail company.

For the SAP S/4HANA Essentials exam, MM is one of the highest-weighted topic areas. Today we cover: the MM organizational structures, Material Master and Vendor Master, the full Procure-to-Pay cycle (Purchase Requisition → Purchase Order → Goods Receipt → Invoice Verification), and how MM integrates with FI for automatic financial postings.

[SHOW SCREEN: SAP Fiori Launchpad — Materials Management section showing tiles: Purchase Requisitions, Purchase Orders, Goods Movements, Invoice Verification, Material Master]

---

## SEGMENT 2 — MM Organizational Structures (2:30–5:00)

SAP MM has its own organizational hierarchy that sits under the FI Company Code.

The **Plant** is the central MM organizational unit. A Plant represents a physical location where materials are produced, stored, or distributed — a factory, a warehouse, a distribution center. All material movements, stock levels, and production activities belong to a Plant.

[SHOW SCREEN: SAP transaction OX10 — Plant configuration showing: Plant Code, Plant Name, Address, Company Code Assignment]

A Plant always belongs to one Company Code. Multiple Plants can belong to the same Company Code — for example, a manufacturer might have Plants in Dallas, Houston, and San Antonio, all assigned to the same legal entity.

The **Storage Location** is a physical storage area within a Plant — a specific warehouse section, a raw materials bin, a finished goods shelf. Stock quantities are tracked at the Storage Location level.

The **Purchasing Organization** manages vendor relationships and negotiates purchasing conditions. It can be set up at the Company Code level (one Purchasing Org per company) or at the Plant level (each Plant negotiates its own vendor terms).

The **Purchasing Group** is the individual buyer or team responsible for purchasing specific material categories — the buyer who handles raw steel, the buyer who handles office supplies, the buyer who handles IT equipment.

---

## SEGMENT 3 — Material Master and Vendor Master (5:00–9:00)

Before you can purchase anything in SAP MM, two master data records must exist: the Material Master and the Vendor Master.

The **Material Master** is the central repository for all information about a material — anything the company buys, produces, stores, or sells.

[SHOW SCREEN: SAP transaction MM03 — Material Master display showing multiple tabs: Basic Data 1, General Plant Data/Storage, MRP 1, Purchasing, Accounting 1, Sales]

The Material Master is organized into **views** — tabs in the SAP interface — each maintained by a different organizational area:

- **Basic Data 1** — Material Number, Description, Base Unit of Measure, Material Group, Industry Sector
- **Purchasing view** — Purchasing Group, order unit, Goods Receipt processing time
- **MRP views (MRP 1, MRP 2)** — planning parameters: MRP type, lot size, reorder point, lead time
- **Accounting 1** — Valuation Class (links material to G/L accounts), price control (Standard or Moving Average), current standard cost or moving average price
- **Plant Data/Storage** — Storage Location, unit of issue, shelf life

The key field for financial integration is the **Valuation Class** on the Accounting view. When goods are received or issued, SAP uses the Valuation Class to automatically determine which G/L accounts to post to — no manual account selection required.

The **Vendor Master** in MM (transaction XK03 or MK03) contains the purchasing-specific data for each vendor: currency, payment terms, Incoterms (shipping responsibility terms), purchasing organization assignment, and which materials or material groups the vendor supplies. This is the same Vendor Master we saw in FI (FK03) — SAP shares the master data across modules, with each module adding its own views.

---

## SEGMENT 4 — The Procure-to-Pay Cycle (9:00–15:00)

The Procure-to-Pay (P2P) cycle is the complete business process from identifying a purchasing need to paying the vendor. In SAP MM, this cycle has four main steps.

[SHOW SCREEN: P2P flow diagram — four boxes left to right: Purchase Requisition → Purchase Order → Goods Receipt → Invoice Verification, with FI GL Posting shown as a parallel track below]

### Step 1: Purchase Requisition (PR)

A Purchase Requisition is an internal request to purchase something. It is created by the person who needs the material — a production planner, a warehouse manager, or an automated MRP run.

Transaction **ME51N** creates a Purchase Requisition. Key fields: Material Number, Quantity, Delivery Date, Plant, Cost Object (cost center or WBS element).

[SHOW SCREEN: SAP ME51N — Create Purchase Requisition with line items: Material, Quantity, Delivery Date, Plant, Cost Center]

A Purchase Requisition is an internal document — it has no legal standing with the vendor. It must be approved (optional) and then converted into a Purchase Order before the vendor is involved.

### Step 2: Purchase Order (PO)

The Purchase Order is the legal commitment to buy from a specific vendor. Transaction **ME21N** creates a Purchase Order. The buyer selects the vendor, confirms the price from an existing **Info Record** or negotiated **Contract**, and assigns the PO to the correct Purchasing Organization and Plant.

[SHOW SCREEN: SAP ME21N — Create Purchase Order showing: Vendor, Purchasing Organization, PO Date, line items: Material, Quantity, Price, Delivery Date, Plant, Storage Location]

Key PO concepts:

- **PO Line Item** — each material being purchased is a separate line item with its own quantity, price, and delivery date
- **Account Assignment Category** — defines how the goods will be used: stock item (K = cost center, no account assignment for stock), asset purchase (A = fixed asset), project purchase (P = WBS element)
- **Info Record** — a record (ME11) that stores the vendor-material price relationship: the last price, standard price, and any price scales for volume discounts

The PO creates a commitment in SAP — the spending is authorized but not yet financially posted.

### Step 3: Goods Receipt (GR)

When the vendor delivers the goods, the receiving team posts a Goods Receipt. Transaction **MIGO** (Goods Movement) is the primary GR transaction.

[SHOW SCREEN: SAP MIGO — Goods Receipt against Purchase Order showing: PO Number reference, Material, Quantity Received, Storage Location, Movement Type 101]

The Goods Receipt uses **Movement Type 101** (Goods Receipt for PO into stock). This posting:

- Increases the stock quantity in the inventory records
- Creates a Material Document (stock movement record)
- Creates an Accounting Document with the automatic G/L entries:
  - Debit: Inventory / Stock account (from Material Master Valuation Class)
  - Credit: Goods Receipt/Invoice Receipt (GR/IR) Clearing Account

The GR/IR Clearing Account is one of the most important concepts in SAP MM. It is a liability account that sits between the goods receipt and the invoice. The credit at GR represents the obligation to pay for goods received but not yet invoiced. The GR/IR account is cleared when the matching invoice is posted.

### Step 4: Invoice Verification

When the vendor invoice arrives, the accounts payable team posts it using transaction **MIRO** (Logistics Invoice Verification). MIRO performs the **three-way match**: it compares the vendor invoice to the Purchase Order and the Goods Receipt.

[SHOW SCREEN: SAP MIRO — Enter Incoming Invoice showing: PO Number reference, Vendor Invoice Number, Invoice Date, Amount, line items auto-populated from PO]

If the quantities and amounts on the invoice match the PO and GR, the posting occurs automatically:

- Debit: GR/IR Clearing Account (clears the GR liability)
- Credit: Accounts Payable (creates the payment obligation)

If there is a difference — the vendor billed more than the PO price, or invoiced for more units than were received — MIRO generates a **price variance** or **quantity variance** and may block the invoice for payment pending resolution. This variance checking is the core value of three-way matching.

---

## SEGMENT 5 — Inventory Valuation and Additional MM Concepts (15:00–18:30)

Let me cover a few additional MM concepts that appear on the SAP exam.

**Goods Issue** — when materials are withdrawn from inventory for production or for consumption. Transaction MIGO with Movement Type 201 (Goods Issue to Cost Center) or 261 (Goods Issue to Production Order). The G/L posting:

- Debit: Consumption expense (from Valuation Class)
- Credit: Inventory account

**Inventory Valuation Methods** — SAP supports two price controls in the Material Master:

- **Standard Price (S)** — all goods movements at a fixed standard cost. Variances between actual cost and standard cost are posted to a Price Difference account.
- **Moving Average Price (V)** — price recalculated with every goods receipt based on actual purchase price. Used for materials where price fluctuates regularly.

**Special Stock Types** — SAP MM tracks special stock categories separately from regular stock:

- **Consignment Stock** — vendor-owned material stored at the customer site; payment triggered only when consumed
- **Sales Order Stock** — stock reserved for a specific customer order
- **Project Stock** — stock assigned to a specific project (WBS element)

**Stock Transport Order (STO)** — used when transferring materials between two Plants within the same Company Code. Creates both a goods issue at the sending Plant and a goods receipt at the receiving Plant.

---

## SEGMENT 6 — MM to FI Integration Summary (18:30–21:00)

SAP MM generates financial postings automatically at two key moments: the Goods Receipt and the Invoice Verification. No accountant manually posts these entries — the MM transactions trigger them.

[SHOW SCREEN: P2P accounting flow diagram showing three events: GR → Dr Inventory / Cr GR/IR. MIRO → Dr GR/IR / Cr AP. F110 Payment → Dr AP / Cr Bank]

Let me walk through the full accounting flow for one purchase:

Event 1 — Goods Receipt (MIGO, Movement Type 101):

- Debit: Raw Materials Inventory $10,000
- Credit: GR/IR Clearing Account $10,000

Event 2 — Invoice Verification (MIRO):

- Debit: GR/IR Clearing Account $10,000 (closes the liability from GR)
- Credit: Accounts Payable $10,000 (creates the payment obligation)

Event 3 — Vendor Payment (F110 Automatic Payment):

- Debit: Accounts Payable $10,000
- Credit: Bank $10,000

After these three events, the GR/IR account nets to zero, inventory is on the books at $10,000, and the vendor has been paid. The entire financial record is created by the operational MM transactions — no separate manual FI entries required. This automatic financial integration is one of the most powerful features of SAP ERP.

---

## SEGMENT 7 — Transaction Code Reference and Summary (21:00–23:30)

Here is your SAP MM transaction code reference for the exam.

Master Data:

- **MM01 / MM03** — Create / Display Material Master
- **XK01 / XK03** — Create / Display Vendor Master (MM/FI combined view)
- **ME11** — Create Purchasing Info Record

Procurement:

- **ME51N** — Create Purchase Requisition
- **ME21N** — Create Purchase Order
- **ME23N** — Display Purchase Order

Goods Movements:

- **MIGO** — Goods Movement (GR, GI, Transfer Posting)

Invoice Verification:

- **MIRO** — Logistics Invoice Verification (three-way match)
- **MIR7** — Park Vendor Invoice (save without posting)

Reporting:

- **ME2M** — Purchase Orders by Material
- **MB52** — Warehouse Stocks of Material
- **ME80FN** — General Analysis of Purchasing Documents

Key concepts to remember for the exam: the GR/IR Clearing Account bridges the Goods Receipt and Invoice posting. Three-way match (PO + GR + Invoice) is verified by MIRO. Movement Type 101 is Goods Receipt. The Valuation Class in the Material Master drives automatic G/L account determination. Module 11 covers SAP PP — Production Planning — where the MM materials we just set up become inputs to the manufacturing process.

---

*End of Script — Module 10*
