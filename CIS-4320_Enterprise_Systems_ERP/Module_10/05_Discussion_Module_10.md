# Discussion Forum: Module 10 — SAP Materials Management (MM Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

---

## Overview

This forum applies SAP MM concepts to realistic business scenarios involving procurement controls, inventory valuation decisions, and purchasing process failures. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175–225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Reference at least one specific SAP MM object, transaction code, or concept (Plant, Material Master, Purchase Requisition, Purchase Order, MIGO, MIRO, three-way match, GR/IR, Movement Type, Valuation Class, etc.) by name
- Apply at least one MM process or control principle from Module 10 to the scenario
- Make a concrete recommendation or analysis grounded in the scenario details

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must do one of the following:

- Identify a financial reporting or inventory accuracy risk your classmate did not mention
- Connect the scenario to a different SAP MM or FI transaction your classmate did not address
- Describe how the MM process failure in the scenario would affect a downstream ERP module (FI accounts payable, PP production planning, SD order fulfillment, or a Salesforce CRM integration)

---

## Scenarios

### Scenario A: The Rogue Purchase Order

A manufacturing plant manager at an industrial equipment company has been bypassing the company's SAP procurement process for two years. Instead of creating Purchase Requisitions and having them approved through SAP, he contacts vendors directly by phone, places verbal orders, and then instructs the receiving dock team to receive the goods in SAP against hastily created Purchase Orders that he creates himself after the fact — post-dating the PO to appear as if it preceded the delivery.

The company's internal audit team discovers the pattern when reconciling the GR/IR Clearing Account. They find 34 Purchase Orders where the PO creation date is after the Goods Receipt date. The total value of these back-dated POs is $1.2 million over 24 months.

**Your task:** Explain why the GR/IR Clearing Account analysis was able to detect this pattern. What is the financial risk to the company from purchases made without approved Purchase Requisitions and properly issued POs? What SAP MM configuration controls — such as purchase order tolerance checks, approval workflows, or GR-to-PO linkage requirements — should have been in place to prevent this from occurring? Reference at least one specific SAP concept or transaction.

### Scenario B: The Invoice Flood

A regional food distributor processes approximately 2,400 vendor invoices per month through SAP MM. Their AP team of three people manually reviews every MIRO posting for accuracy before approving payment. The team spends an average of 8 minutes per invoice on manual review. Over 60% of invoices match the PO and GR exactly and require no investigation.

A new ERP consultant recommends enabling MIRO tolerance-based auto-posting: invoices with price variances below 2% and quantity variances within 0.5 units would post automatically without manual review. Only invoices outside these tolerances would require human attention.

**Your task:** Evaluate this recommendation. What is the current time cost of the all-manual review process? How does MIRO three-way match work, and what does enabling tolerance-based auto-posting actually change about the matching logic? What financial control risks exist if tolerances are set too broadly, and what governance safeguards would you recommend alongside the automation? Provide a numerical analysis as part of your response.

### Scenario C: The Inventory Valuation Conflict

A chemical manufacturing company is migrating from a legacy inventory system to SAP S/4HANA. They produce 85 different materials: 40 are bulk commodity chemicals purchased from external suppliers (prices fluctuate 15–30% per quarter), 30 are proprietary formulated compounds manufactured in-house (complex BOM, labor-intensive, stable internal cost), and 15 are specialty imported reagents with highly volatile pricing.

The SAP implementation team proposes using Standard Price (S) for all 85 materials to simplify configuration. The company's controller pushes back, arguing that Standard Price is inappropriate for materials with highly volatile market prices.

**Your task:** Explain the difference between Standard Price (S) and Moving Average Price (V) in the SAP Material Master. Why is the implementation team's proposal to use Standard Price for all materials problematic for the 40 commodity chemicals and 15 specialty reagents? What would happen to the Price Difference account if volatile materials are valued at Standard Price during a period of significant price fluctuation? What configuration approach would you recommend for each of the three material categories, and why?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter at top of post |
| Specific SAP MM object, transaction, or concept named and applied | 2 | SAP term used correctly in scenario context |
| MM process or control principle applied correctly | 1 | Principle named and applied to the scenario |
| Concrete recommendation or analysis | 1 | Specific and grounded — not generic ERP commentary |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, substantive extension | 2 | Adds financial risk, inventory risk, or downstream module connection |
| Peer response 2: 60+ words, substantive extension | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario A describes one of the most common audit findings in SAP MM environments: purchase orders created after the goods receipt. In a properly configured SAP system, a GR cannot be posted without referencing a valid, approved PO. The system enforces the sequence. But when configuration is lax — or when someone with sufficient authorization creates POs retroactively — the sequence breaks down. The GR/IR Clearing Account becomes the forensic trail. Any time a PO date is later than the GR date for the same line item, something went wrong in the procurement process. Internal audit teams routinely run this query as a standard fraud detection procedure. Learning to recognize what a clean GR/IR balance means — and what an anomalous one reveals — is one of the most practical skills you will take from this module.
