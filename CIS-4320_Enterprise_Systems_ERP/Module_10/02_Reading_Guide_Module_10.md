# Reading Guide: Module 10 — SAP Materials Management (MM Module)

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

SAP Materials Management (MM) is the module that manages the complete procurement and inventory process — from recognizing a need through paying the vendor. MM is tightly integrated with FI (automatic financial postings), PP (production material supply), and SD (customer order fulfillment). This reading guide covers MM organizational structures, master data, the full Procure-to-Pay cycle, inventory valuation, and the key transaction codes tested on the SAP S/4HANA Essentials exam.

---

## Section 1 — Core Glossary

**Plant**
The central MM organizational unit representing a physical location where materials are produced, stored, or distributed. A Plant belongs to exactly one Company Code. All inventory balances, purchase orders, and production orders are Plant-specific.

**Storage Location**
A physical storage area within a Plant. Stock quantities are tracked at the Plant/Storage Location level. Examples: Raw Materials Warehouse, Finished Goods Area, Quality Inspection Zone.

**Purchasing Organization**
The organizational unit responsible for negotiating purchasing conditions and managing vendor relationships. Can be at the Company Code level (enterprise-wide purchasing) or Plant level (plant-specific purchasing).

**Purchasing Group**
An individual buyer or buyer team responsible for a specific material category. Purchasing Groups are assigned to Purchase Orders and used for reporting and workflow routing.

**Material Master**
The central data record for any material the company buys, produces, stores, or sells. Organized into views maintained by different departments: Basic Data, Purchasing, MRP, Accounting, Sales. Transaction MM01 creates; MM03 displays.

**Valuation Class**
A field in the Material Master Accounting view that links a material to G/L accounts. When goods are received or issued, SAP uses the Valuation Class to determine which G/L accounts to post to automatically — no manual account selection required.

**Price Control**
The method used to value inventory movements in the Material Master. Two options: Standard Price (S) — fixed cost; variances posted to Price Difference account. Moving Average Price (V) — recalculated with each goods receipt based on actual purchase price.

**Vendor Master**
The master data record for a vendor. In MM, the relevant views are: General Data (name, address), Company Code Data (payment terms, reconciliation account), and Purchasing Data (currency, Incoterms, purchasing organization). Transactions XK01 (create), XK03 (display).

**Purchase Requisition (PR)**
An internal document requesting authorization to purchase materials or services. Created manually (ME51N) or automatically by MRP. Has no legal standing with vendors. Must be converted to a Purchase Order.

**Purchase Order (PO)**
The legal commitment to purchase from a specific vendor. Contains vendor, material, quantity, price, delivery date, and plant. Created with ME21N. Drives the three-way match process.

**Purchasing Info Record**
A record (ME11) that stores the vendor-material price relationship: the last negotiated price, standard price, and price scales for quantity discounts. Used to auto-populate PO prices.

**Goods Receipt (GR)**
The physical receipt of materials from a vendor. Posted in SAP using transaction MIGO with Movement Type 101. Increases inventory stock and posts the GR/IR accounting entry.

**Movement Type**
A three-digit SAP code that classifies every inventory movement and determines the resulting G/L postings. Key movement types: 101 (GR for PO), 102 (GR reversal), 201 (GI to Cost Center), 261 (GI to Production Order), 301 (Plant-to-Plant transfer).

**GR/IR Clearing Account**
The Goods Receipt / Invoice Receipt clearing account. A balance sheet liability account that bridges the gap between when goods are received (GR) and when the vendor invoice is posted (IR). Credited at GR; debited at MIRO. Should net to zero when all open PO items are invoiced.

**MIRO (Logistics Invoice Verification)**
The SAP transaction for posting vendor invoices in the MM context. Performs three-way match: compares invoice to PO and GR. Posts: Debit GR/IR / Credit Accounts Payable. Generates a variance if price or quantity does not match.

**Three-Way Match**
The verification that a vendor invoice matches: (1) the approved Purchase Order (price and terms), (2) the Goods Receipt (quantity actually received). Any discrepancy generates a variance and may block payment.

**MRP (Material Requirements Planning)**
The SAP planning engine (in PP and MM) that analyzes production requirements, current stock levels, and open purchase orders to automatically generate Purchase Requisitions for materials that need to be replenished.

---

## Section 2 — MM Organizational Structure

```text
CLIENT
  |
  +-- COMPANY CODE 1000
          |
          +-- PLANT 1000 (Main Factory — Dallas)
          |       |
          |       +-- Storage Location 0001 (Raw Materials)
          |       +-- Storage Location 0002 (Finished Goods)
          |       +-- Storage Location 0003 (Quality Inspection)
          |
          +-- PLANT 1100 (Distribution Center — Houston)
                  |
                  +-- Storage Location 0001 (Inbound Dock)
                  +-- Storage Location 0002 (Outbound Staging)
```

### MM Organizational Unit Comparison

| Unit | Level | Scope |
|---|---|---|
| Company Code | Financial | Legal entity; owns balance sheet |
| Plant | Operational | Physical location; owns inventory |
| Storage Location | Physical | Storage area within plant |
| Purchasing Organization | Procurement | Negotiates vendor terms |
| Purchasing Group | Buyer | Responsible for material category |

---

## Section 3 — Material Master View Reference

| View | Maintained By | Key Fields |
|---|---|---|
| Basic Data 1 | Central/Master Data team | Material Number, Description, Base UoM, Material Group |
| Purchasing | Purchasing | Purchasing Group, Order Unit, GR Processing Time |
| MRP 1 | Production Planning | MRP Type, Lot Size Procedure, Reorder Point |
| MRP 2 | Production Planning | Planned Delivery Time, Safety Stock, Scheduling Margin |
| Accounting 1 | Finance/Controlling | Valuation Class, Price Control (S/V), Standard/Moving Avg Price |
| Plant Data/Storage | Warehouse | Storage Location, Hazardous Material Info, Shelf Life |
| Sales | Sales | Sales Unit, Item Category Group, Delivering Plant |

### Price Control Comparison

| Method | Code | How Price Is Set | Variance Posting | Best For |
|---|---|---|---|---|
| Standard Price | S | Fixed cost set at start of period | Price Difference account | Finished goods, semi-finished goods |
| Moving Average Price | V | Recalculated at each goods receipt | Absorbed into stock value | Raw materials, trading goods |

---

## Section 4 — Procure-to-Pay Cycle

### Complete P2P Process Flow

```text
[NEED IDENTIFIED]
  Manual: User recognizes shortage
  Automatic: MRP run generates planned orders
        |
        v
[PURCHASE REQUISITION — ME51N]
  Internal request document
  Fields: Material, Quantity, Delivery Date, Plant, Cost Object
  No legal standing; may require approval
        |
  Approved PR
        |
        v
[PURCHASE ORDER — ME21N]
  Legal commitment to vendor
  Vendor + Material + Qty + Price + Delivery Date
  References PR; sourced from Info Record or Contract
  Account Assignment Category determines G/L target
        |
  PO sent to vendor
        |
        v
[GOODS RECEIPT — MIGO, Movement Type 101]
  Physical delivery from vendor
  Verifies quantity and quality
  Posts Material Document (inventory record)
  Posts Accounting Document:
    Dr: Inventory / Stock Account
    Cr: GR/IR Clearing Account
        |
        v
[INVOICE VERIFICATION — MIRO]
  Vendor invoice received
  Three-way match: Invoice vs. PO vs. GR
  If match: Posts Accounting Document:
    Dr: GR/IR Clearing Account
    Cr: Accounts Payable
  If variance: Invoice blocked; purchasing resolves
        |
        v
[VENDOR PAYMENT — F110 (FI)]
  Automatic Payment Program selects due invoices
  Posts:
    Dr: Accounts Payable
    Cr: Bank
```

---

## Section 5 — Key Accounting Entries in the P2P Cycle

| Event | Transaction | Debit | Credit |
|---|---|---|---|
| Goods Receipt | MIGO (101) | Inventory / Stock Account | GR/IR Clearing Account |
| Invoice Verification (matched) | MIRO | GR/IR Clearing Account | Accounts Payable |
| Invoice Variance (price diff) | MIRO | GR/IR Clearing Account + Price Difference | Accounts Payable |
| Vendor Payment | F110 | Accounts Payable | Bank Account |
| Goods Issue to Production | MIGO (261) | Production Order / Cost Object | Inventory Account |
| Goods Issue to Cost Center | MIGO (201) | Cost Center Expense | Inventory Account |
| Return to Vendor | MIGO (122) | GR/IR Clearing Account | Inventory Account |

---

## Section 6 — Movement Type Reference

| Movement Type | Description | Direction |
|---|---|---|
| 101 | Goods Receipt for Purchase Order | Into stock (from vendor) |
| 102 | Reversal of GR for PO | Out of stock (GR correction) |
| 122 | Return to Vendor | Out of stock (return delivery) |
| 201 | Goods Issue to Cost Center | Out of stock (consumption) |
| 261 | Goods Issue to Production Order | Out of stock (into manufacturing) |
| 301 | Transfer Posting Plant to Plant (one-step) | Between plants |
| 311 | Transfer Posting Storage Location to Storage Location | Within plant |
| 561 | Initial Stock Entry (opening balance) | Into stock (no PO reference) |

---

## Section 7 — Three-Way Match Logic

### Match Scenarios

| Scenario | PO Price | GR Quantity | Invoice | Result |
|---|---|---|---|---|
| Perfect match | $100/unit | 500 units | $50,000 | Posts automatically; no variance |
| Price variance | $100/unit | 500 units | $52,500 | Price difference of $2,500; may block invoice |
| Quantity variance | $100/unit | 500 units | $55,000 (550 units) | 50 units not received; partial payment only |
| Under-delivery | $100/unit | 450 units (of 500) | $45,000 | Posts for received quantity; remaining 50 open |

### Tolerance Keys in MIRO

SAP can be configured to automatically post invoices with small variances (within a tolerance percentage) without blocking them. Tolerances above the configured threshold block the invoice for manual review. This prevents small rounding differences from creating manual work while ensuring large discrepancies are investigated.

---

## Section 8 — Special Procurement Types

| Type | Description | Key Characteristic |
|---|---|---|
| Standard Purchase | Buy from external vendor | Regular P2P cycle |
| Consignment | Vendor stock stored at company premises | Liability triggered only when consumed (MIGO 411) |
| Subcontracting | Company provides components; vendor assembles | Components issued to vendor with PO |
| Stock Transport Order | Transfer between plants | Treated as internal purchase |
| Service Procurement | Purchase services, not goods | Service Entry Sheet (ML81N) instead of GR |

---

## Section 9 — Transaction Code Master Reference

| Transaction | Description |
|---|---|
| MM01 / MM03 | Create / Display Material Master |
| XK01 / XK03 | Create / Display Vendor Master (all views) |
| MK01 / MK03 | Create / Display Vendor Master (purchasing view only) |
| ME11 | Create Purchasing Info Record |
| ME51N | Create Purchase Requisition |
| ME52N / ME53N | Change / Display Purchase Requisition |
| ME21N | Create Purchase Order |
| ME22N / ME23N | Change / Display Purchase Order |
| MIGO | Goods Movement (GR, GI, Transfer) |
| MIRO | Logistics Invoice Verification |
| MIR7 | Park Vendor Invoice |
| ME2M | Purchase Orders by Material |
| MB52 | Warehouse Stocks of Material |
| MB51 | Material Document List |
| ME80FN | General Purchasing Analysis |

---

## Section 10 — Exam Tips

> **Exam Tip 1 — Plant is the central MM unit.** Everything in MM belongs to a Plant: stock, purchase orders, production orders. A Plant belongs to exactly one Company Code. Multiple Plants can share one Company Code.

> **Exam Tip 2 — GR/IR is the bridge account.** Goods Receipt credits GR/IR; Invoice Verification debits GR/IR. When both events are complete, GR/IR nets to zero. An open GR/IR balance means either a GR without an invoice (accrued liability) or an invoice without a GR (advance billing).

> **Exam Tip 3 — MIGO is the goods movement transaction.** All inventory movements go through MIGO with the appropriate Movement Type. Know 101 (GR for PO), 201 (GI to Cost Center), 261 (GI to Production Order).

> **Exam Tip 4 — MIRO performs three-way match.** Invoice vs. PO vs. GR. Variances can be within tolerance (auto-post) or outside tolerance (invoice blocked). This is the core AP control in an MM environment.

> **Exam Tip 5 — Valuation Class drives automatic G/L posting.** The Material Master Accounting view Valuation Class determines which G/L accounts are updated for any movement. This is how SAP avoids manual account selection for every goods movement.

> **Exam Tip 6 — Purchase Requisition is internal; Purchase Order is external.** A PR has no legal effect. A PO is a legal commitment to a vendor. Know the transaction codes: ME51N (PR), ME21N (PO).

---

## Section 11 — Study Checklist

- Review the MM organizational structure diagram in Section 2.
- Memorize the Material Master view table and what each view contains (Section 3).
- Trace the complete P2P process flow in Section 4 without looking at labels.
- Study the accounting entries table in Section 5 — know which accounts are debited and credited at each P2P step.
- Memorize the key Movement Types in Section 6.
- Review the three-way match scenarios in Section 7.
- Memorize the transaction code master reference in Section 9.
- Complete the Module 10 SAP exercises (sandbox or Learning Hub).
- Watch the Module 10 video lecture.
- Complete Lab 10.
- Post to Discussion Forum 10 by Wednesday at 11:59 PM.
- Complete Quiz 10.

---

## 9. Supplemental Resources

**1. SAP Learning — Sourcing and Procurement with SAP S/4HANA**
<https://learning.sap.com/learning-journeys/source-and-procure-with-sap-s-4hana>
Official SAP learning journey covering the end-to-end Procure-to-Pay process: purchase requisitions, purchase orders, goods receipts, MIRO invoice verification, and automatic payment. Maps directly to the transaction codes (ME51N, ME21N, MIGO, MIRO, F110) and three-way match logic tested in this module's quiz and Lab 10.

**2. ASCM — Certified in Planning and Inventory Management (CPIM) Body of Knowledge**
<https://www.ascm.org/learning-development/certifications-credentials/cpim/>
The ASCM (formerly APICS) CPIM certification body of knowledge covers MRP logic, inventory valuation methods (standard price vs. moving average), reorder point planning, and safety stock calculation — the inventory management theory underlying SAP MM configuration decisions covered in this module.

**3. SAP Help Portal — Inventory Management and Physical Inventory**
<https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/inventory-management>
Official SAP product documentation for Inventory Management. Covers movement types, material documents, valuation classes, and G/L account determination via the Account Determination framework (OBYC) — essential reference for understanding how SAP MM posting logic works and how Valuation Class maps to G/L accounts.
