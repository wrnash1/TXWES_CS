# Discussion Forum: Module 06 - Supply Chain Management Integrations

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

---

## Overview

This forum applies Module 06 supply chain concepts to realistic business scenarios involving procurement controls, MRP planning decisions, and inventory management trade-offs. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175-225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Reference at least one specific SAP MM transaction code or process (MIGO, MIRO, ME21N, ME61, MD01, three-way match, etc.)
- Name a specific supply chain concept from Module 06 (MRP, reorder point, safety stock, GR/IR clearing, vendor evaluation, etc.)
- Make a concrete recommendation or analysis grounded in the scenario

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must:

- Add a supply chain risk or consequence your classmate did not mention
- Connect the scenario to a specific financial journal entry or inventory valuation impact
- Or describe how the supply chain control your classmate referenced would appear in a Salesforce Order Management context

---

## Scenarios

### Scenario A: The Bypass Request

A mid-size electronics manufacturer runs MRP weekly using SAP transaction MD01. After each MRP run, the materials planner reviews 80 to 100 procurement proposals and converts acceptable ones to purchase orders. The VP of Operations complains that this weekly cycle is too slow — by the time purchase orders are sent to vendors, some critical components are already below safety stock. She proposes that the company configure SAP to automatically convert all MRP proposals to purchase orders without planner review, and send them directly to vendors.

**Your task:** What risks would fully automated PO creation introduce? What is the appropriate role of the human planner in reviewing MRP proposals before they become purchase orders? Rather than bypassing the review step entirely, what process improvement could reduce the planning cycle from weekly to a shorter interval while preserving procurement controls? Reference at least one specific SAP concept or transaction in your answer.

### Scenario B: The Valuation Mismatch

A building materials distributor implemented SAP with Moving Average Price (MAP) for all inventory. Six months in, the company acquires a large lot of lumber at a price 35% below their current MAP because of a distressed seller. After the goods receipt is posted in MIGO, the MAP drops sharply. The CFO receives the monthly balance sheet and is alarmed that inventory values fell significantly even though the physical quantity increased. He asks the controller to "fix the inventory value back to where it was."

**Your task:** Explain why the MAP drop is not an error — it is the correct behavior of the Moving Average Price method. What journal entry did SAP post when the goods receipt was recorded? Why would "correcting" the MAP back to the prior value misrepresent the actual cost of the inventory? Under what circumstances would Standard Price have been the better valuation choice for this company, and what would have happened differently at the time of the low-price receipt?

### Scenario C: The Vendor Reliability Crisis

A food packaging manufacturer has three approved vendors for a critical sealing film. Vendor A supplies 60% of volume and has been consistently on time. Vendor B supplies 30% and has had two late deliveries in the last quarter. Vendor C supplies 10% and has had four late deliveries plus two quality rejections resulting in goods returns in the last six months. The procurement manager has not taken any formal action because "the vendors always eventually deliver." Last week, Vendor C's late shipment caused a 2-day production stoppage that cost the company $85,000 in lost output.

**Your task:** How should SAP's vendor evaluation functionality (transaction ME61) have been used before the production stoppage occurred? What score criteria would have identified Vendor C as high-risk? What formal procurement actions should the procurement manager now take in SAP based on the evaluation data? How does the three-way match in accounts payable relate to the quality rejection events described above?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter |
| Specific SAP transaction code or process named and applied | 2 | Transaction code or named process used correctly in scenario context |
| Supply chain concept referenced correctly | 1 | MRP, safety stock, valuation method, vendor evaluation, or GR/IR named and applied |
| Concrete recommendation or analysis | 1 | Specific and grounded in scenario |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, adds supply chain risk or financial impact | 2 | Substantive extension |
| Peer response 2: 60+ words, adds supply chain risk or financial impact | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario C is the one that frustrates me most when I see it in real companies. Vendor evaluation data exists in the system — SAP ME61 can score every supplier on delivery, quality, and pricing automatically. But the scores sit there unused while procurement managers explain away late deliveries as one-off events. The $85,000 production stoppage in this scenario is not bad luck. It is the predictable outcome of ignoring data the ERP system provided. One of ERP's most underutilized capabilities is turning operational transaction data into supplier intelligence. Use it.
