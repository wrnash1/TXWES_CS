# Discussion Forum: Module 11 — SAP Production Planning (PP Module)

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

---

## Overview

This forum applies SAP PP concepts to realistic manufacturing planning and execution scenarios. You will analyze a BOM structure failure, an MRP planning breakdown, and a Production Order costing problem. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175–225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Reference at least one specific SAP PP object, transaction code, or concept (BOM, Routing, Work Center, MRP, MD04, Planned Order, Production Order, BOM explosion, lot size, safety stock, CRTD/REL/TECO/CLSD status, CO11N, KO88, production variance, Movement Type 261/101, etc.) by name
- Apply at least one PP process or control principle from Module 11 to the scenario
- Make a concrete recommendation or analysis grounded in the scenario details

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must do one of the following:

- Identify a production costing, inventory accuracy, or scheduling risk your classmate did not mention
- Connect the scenario to a different SAP PP or MM transaction your classmate did not address
- Describe how the PP process failure in the scenario would affect a downstream ERP module (MM materials supply, FI cost accounting, CO variance analysis, or a Salesforce CRM customer commitment)

---

## Scenarios

### Scenario A: The Missing Sub-Assembly

A consumer electronics manufacturer uses SAP PP to plan production of a finished circuit board assembly (FG-CB-900). The BOM for FG-CB-900 has been in production for two years. Six months ago, the engineering team redesigned one of the sub-assemblies — SA-POWER-MODULE — replacing a legacy capacitor with a new higher-specification part (CAP-NEW-22UF) and removing the old one (CAP-OLD-10UF).

The engineering change was approved and the new CAP-NEW-22UF was added to the vendor catalog and Material Master. However, the BOM for SA-POWER-MODULE was never updated in SAP. It still lists CAP-OLD-10UF as a component.

For six months, MRP has been generating Purchase Requisitions for CAP-OLD-10UF, which is no longer needed. CAP-NEW-22UF has been procured manually outside of MRP, creating unplanned inventory. The shop floor has been manually substituting the components during production — no formal SAP posting reflects the actual materials consumed.

**Your task:** Explain what PP master data should have been updated when the engineering change was approved. What are the risks to production cost accuracy and inventory management when actual components consumed differ from what the BOM specifies? What happens to the production variance (viewable after KO88 settlement) when unauthorized component substitutions are made without updating the BOM? What is your recommendation to correct the current state?

### Scenario B: The MRP Overproduction Spiral

A specialty chemical company runs MRP every Monday morning using regenerative planning (MD01). Their finished product FG-SOLV-440 has the following Material Master settings: MRP Type PD, Lot Size FX (fixed lot size of 500 units), Safety Stock 200 units.

Current state on Monday morning: Gross requirement for the week is 300 units. Current warehouse stock is 450 units (well above safety stock). The planner opens MD04 for FG-SOLV-440 and is surprised to see MRP has generated a Planned Order for 500 units.

The production manager is frustrated: "We have 450 units on hand and only need 300 this week. Why is SAP telling us to produce 500 more? Our warehouse is already overstocked and our Work Centers are at 95% capacity. If we run this order we will hit 650 units of finished stock with nowhere to put it."

**Your task:** Explain exactly why MRP generated a Planned Order for 500 units given the FX lot size configuration and current stock position. Is this technically correct SAP behavior? What is the business problem with using a fixed lot size for a product with variable weekly demand? What change to the Material Master MRP settings would you recommend to prevent unnecessary production proposals in weeks where existing stock already covers demand? Use specific MRP Type or Lot Size configuration terms in your answer.

### Scenario C: The Invisible Variance

A precision machining company produces industrial pump housings (FG-PUMP-H200). Each unit has a standard cost of $1,850, calculated from the Routing (machine time × Work Center rate) and BOM (material quantities × standard material prices). The company runs 40-unit Production Orders monthly.

For the past three months, the monthly KO88 settlement consistently shows an unfavorable production variance of $8,000–$12,000 per order. The standard cost is $1,850 × 40 = $74,000 per order; actual costs are running $82,000–$86,000. Management is aware of the variance but no one has investigated it.

The production controller finally reviews the Production Order detail in CO03 and finds: actual machine time on Operation 20 (Boring Mill — Work Center BORE-MILL-01) is consistently 40% higher than the standard time defined in the Routing. The Work Center BORE-MILL-01 has a cost rate of $185/hour. The standard Routing time for Operation 20 is 12 minutes/unit (8 hours per 40-unit order); actual confirmed time via CO11N is consistently 16–17 minutes/unit (about 11 hours per order).

**Your task:** Calculate the expected cost impact of the 40% machine time overrun on a 40-unit order using the $185/hour Work Center rate. Does your calculation explain the observed variance range ($8,000–$12,000)? What are two possible root causes for the persistent machine time overrun — one operational and one master data related? What corrective action should the company take in SAP, and which transaction would be used to update the Routing standard values if the longer time is now the new standard?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter at top of post |
| Specific SAP PP object, transaction, or concept named and applied | 2 | SAP term used correctly in scenario context |
| PP process or control principle applied correctly | 1 | Principle named and applied to the scenario |
| Concrete recommendation or analysis | 1 | Specific and grounded — not generic ERP commentary |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, substantive extension | 2 | Adds costing risk, inventory risk, or downstream module connection |
| Peer response 2: 60+ words, substantive extension | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario C describes one of the most common and most ignored problems in SAP PP implementations: the stale Routing. When a company implements SAP, engineers set standard values for Routing operations based on the production process at that moment. Over time, machines age, processes change, operators are replaced, and actual production times drift away from the standard. But no one updates the Routing — because updating master data requires paperwork, approvals, and effort that production teams often deprioritize.

The result is a chronic unfavorable variance that everyone sees on the KO88 settlement report every month and no one investigates. Management learns to expect a variance and treats it as normal. The variance is not normal. It is a signal: either the process has changed and the standard is wrong, or the process is inefficient and needs to be fixed. In either case, the standard values in the Routing must reflect reality. An unrealistic Routing produces misleading planned costs, unreliable production scheduling, and variance reports that no longer carry useful information. Learning to read a Production Order costing analysis — comparing planned Routing times to actual confirmed times — is one of the most valuable analytical skills in manufacturing ERP work.

