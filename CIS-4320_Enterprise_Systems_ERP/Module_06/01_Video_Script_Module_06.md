# Video Script: Module 06 - Supply Chain Management Integrations

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22-24 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### [00:00 - 01:30] Opening

Professor Nash on camera. Title card: "Module 06 - Supply Chain Management Integrations."

"Welcome back to CIS-4320. In Module 05 we covered the financial core of ERP. Now we move to the operational backbone: Supply Chain Management.

For any company that buys, makes, or moves physical goods — a manufacturer, a distributor, a retailer — supply chain is where ERP delivers some of its most direct business value. Getting the right materials to the right place at the right time, at the right cost, with minimal waste — that is the supply chain management mission. ERP systems execute this mission through a tightly integrated set of modules that span procurement, inventory management, production planning, and materials requirements planning.

Today we cover SAP Materials Management (MM), the Procure-to-Pay process, inventory management, MRP, warehouse management, and how supply chain integrates with financial modules. These are high-frequency topics on the SAP Associate exam."

---

### [01:30 - 05:30] Materials Management Overview

Cut to slide: "SAP MM — The Procurement Engine."

"SAP Materials Management — abbreviated MM — is the primary SAP module for supply chain. MM handles three core functions: procurement management, inventory management, and warehouse management.

Procurement management encompasses everything from determining what to buy, to issuing purchase orders, to receiving goods, to paying vendors. This is the Procure-to-Pay process we introduced in Module 05 in the context of the three-way match.

Inventory management tracks the quantity and value of materials held in storage locations across the organization. Every goods movement — a receipt, an issue to production, a transfer between locations, a return to vendor — is recorded as a material document. The material document is the record of what happened; the financial document is the record of the accounting impact.

Warehouse management handles the physical locations within a warehouse: aisles, shelves, bins. Warehouse management is an optional layer on top of inventory management, used by companies with complex warehouse operations. SAP's Extended Warehouse Management (EWM) is the advanced warehouse solution for high-complexity distribution centers.

[SHOW DIAGRAM: Three concentric circles or nested boxes. Outer layer: 'MM — Materials Management.' Middle layer: 'Inventory Management — tracks quantities and values.' Inner layer: 'Warehouse Management / EWM — tracks physical bin locations within the warehouse.' Arrows showing data flows between layers.]

The master data that drives all MM processes is stored in two places: the vendor master (we covered this in Module 05) and the material master. The material master is one of the most important objects in SAP — it contains every piece of information about a product: description, unit of measure, procurement parameters, costing data, quality management rules, and storage requirements."

---

### [05:30 - 09:30] Material Requirements Planning

Cut to slide: "MRP — The Demand Engine."

"Material Requirements Planning — MRP — is the planning algorithm at the heart of supply chain ERP. MRP answers three fundamental questions: What do we need? How much do we need? When do we need it?

MRP takes as inputs: the sales demand (open sales orders and forecast), the current inventory levels, the bills of materials (what components go into each finished product), the production orders (what we are already making), and the purchasing proposals (what we have already ordered). It processes all of these together to calculate net requirements — the additional materials that need to be procured or produced to meet demand.

The output of an MRP run is procurement proposals: purchase requisitions for materials to be bought externally, and planned production orders for materials to be made internally.

[SHOW DIAGRAM: An MRP input/output diagram. Left side (Inputs): Sales Orders/Forecast, Current Stock, Bills of Materials, Open POs, Open Production Orders. Arrow pointing right to 'MRP Planning Run (MD01).' Right side (Outputs): Purchase Requisitions (for external procurement), Planned Orders (for internal production). Below the output, a note: 'Planner reviews proposals and converts to Purchase Orders or Production Orders.']

The MRP run is executed by a planner using SAP transaction MD01 for mass planning or MD02 for single material planning. After the run, the planner reviews the proposals, makes adjustments based on judgment (minimum order quantities, supplier constraints, etc.), and converts the proposals to executable purchase orders or production orders.

Exam tip: MRP is not automatic. It generates proposals that a human planner reviews and approves. Fully automated ERP that creates purchase orders without human review is an advanced pattern called autonomous procurement, not standard MRP."

---

### [09:30 - 13:00] The Procure-to-Pay Process End-to-End

Cut to slide: "P2P — Procure-to-Pay End-to-End."

"Let me walk through the complete Procure-to-Pay process in SAP so you can see how MM and FI work together.

Step one: Purchase Requisition. A need is identified — either manually by a department or automatically by MRP. The purchase requisition (PR) is an internal document requesting that procurement buy something. It is not sent to a vendor.

Step two: Purchase Order. The purchasing department reviews the requisition, selects a vendor, and creates a Purchase Order (PO) using SAP transaction ME21N. The PO is an external document sent to the vendor. It commits the company to buy at the agreed price.

Step three: Goods Receipt. The vendor ships the goods. The warehouse records the physical arrival using SAP transaction MIGO (Goods Receipt). This increases the inventory balance and posts an accounting entry: Debit Inventory, Credit GR/IR Clearing (a transit account).

Step four: Invoice Verification. The vendor sends their invoice. The AP clerk enters it using SAP transaction MIRO. SAP executes the three-way match against the PO and GR. If it passes, the invoice is cleared for payment: Debit GR/IR Clearing, Credit Vendor AP.

Step five: Payment. The automatic payment run (F110) pays the vendor. Debit Vendor AP, Credit Bank.

[SHOW DIAGRAM: A horizontal flow showing all five steps as connected boxes. Below each step: the SAP transaction code (ME51N → ME21N → MIGO → MIRO → F110) and the SAP document created (Requisition → Purchase Order → Material Document + FI Document → Invoice Document → Payment Document).]

Notice how each step produces both a logistics document AND a financial document. That integration between MM and FI is the core architecture of SAP's procure-to-pay process."

---

### [13:00 - 16:30] Inventory Management and Valuation

Cut to slide: "Inventory — Quantity and Value."

"Inventory management in SAP MM tracks two dimensions simultaneously: quantity and value.

Quantity tracking means knowing how many units are in each storage location. When a goods receipt is posted, the stock quantity at that location increases. When goods are issued to a production order, the quantity decreases. Every movement is logged as a material document.

Value tracking means knowing the financial value of the inventory. SAP supports two primary inventory valuation methods: Standard Price and Moving Average Price.

With Standard Price, each material has a fixed predetermined cost. Any difference between the standard price and the actual purchase price is posted to a price variance account. Standard price is common in manufacturing environments where cost stability is important for product costing.

With Moving Average Price, SAP recalculates the average unit price with each new goods receipt, blending the new receipt price with the existing stock value. Moving average price is common for trading companies where purchased goods are resold without further transformation.

[SHOW DIAGRAM: Two side-by-side examples. Left (Standard Price): Material standard price = $10. Received 100 units at $11 each. Inventory posting: Debit Inventory $1,000 (100 × $10 standard), Debit Price Variance $100, Credit Vendor AP $1,100. Right (Moving Average Price): Existing 50 units @ $10. Received 100 units @ $11. New MAP = (50×$10 + 100×$11)/150 = $10.67. New inventory value = 150 × $10.67.]

Physical inventory counting is another key MM process. At least annually (and more frequently for cycle counting programs), the physical stock is counted and reconciled against SAP's perpetual inventory records. Any differences are posted as inventory adjustments."

---

### [16:30 - 19:30] Vendor Evaluation and SCM Integration

Cut to slide: "Vendor Management and SCM Integration."

"A critical but often underappreciated SCM capability in SAP is vendor evaluation. The vendor evaluation module tracks supplier performance across three dimensions: delivery reliability, quality, and pricing compliance.

For each vendor, SAP can calculate an overall vendor score based on configurable weighting of these criteria. A vendor who consistently delivers on time and at the agreed price receives a high score. A vendor with frequent late deliveries or quality rejections receives a low score. This data drives procurement decisions — high-scoring vendors are preferred for future orders; chronically low-scoring vendors are candidates for disqualification or renegotiation.

[SHOW DIAGRAM: A vendor scorecard table showing three vendors. Vendor A: Delivery 92%, Quality 98%, Pricing 99% → Overall Score 96. Vendor B: Delivery 78%, Quality 95%, Pricing 97% → Overall Score 87. Vendor C: Delivery 61%, Quality 88%, Pricing 94% → Overall Score 74. Decision arrows: Vendor A = Preferred, Vendor B = Monitor, Vendor C = Corrective Action Required.]

Supply chain management also integrates with Sales and Distribution (SD) for demand planning, with Production Planning (PP) for manufacturing execution, and with Quality Management (QM) for incoming goods inspections. The integration across all these modules is what gives ERP its power — a sales order in SD triggers MRP in MM which generates a production order in PP which consumes materials from MM inventory — all automatically, all with financial postings to FI.

This is the full integration story: supply chain is not a standalone process. It is embedded in the operational and financial fabric of the enterprise."

---

### [19:30 - 21:30] Module Summary and Exam Tips

Cut to slide: "Module 06 Key Takeaways."

"Key takeaways for Module 06:

One: SAP Materials Management (MM) covers procurement, inventory management, and warehouse management.

Two: MRP — Material Requirements Planning — calculates what to buy or produce based on demand, inventory, and bills of materials. Its outputs are purchase requisitions and planned production orders that humans review and approve.

Three: The Procure-to-Pay process flows through Purchase Requisition → Purchase Order → Goods Receipt → Invoice Verification → Payment. Each step produces both a logistics document and a financial document.

Four: Inventory management tracks both quantity and value. Valuation methods are Standard Price (fixed predetermined cost) and Moving Average Price (recalculated with each receipt).

Five: Vendor evaluation scores supplier performance on delivery, quality, and pricing to support procurement decisions.

Six: SCM integrates with FI (financial postings), SD (demand), and PP (production) — the integration is the value.

Exam tips: SAP transaction codes for the P2P process are frequently tested on the SAP Associate exam. Know: ME21N (Purchase Order), MIGO (Goods Receipt), MIRO (Invoice), F110 (Payment Run). Also know MD01 for MRP. For the distinction between purchase requisition and purchase order — the PR is internal, the PO is external and vendor-facing."

---

### [End Card]

Text on screen:

- Complete Reading Guide 06
- Complete Lab 06 (Procure-to-Pay Scenario Analysis)
- Complete Quiz 06 (10 questions)
- Post to Discussion Forum 06 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com — search "Salesforce Order Management"
