# Video Script: Module 08 - Feasibility Analysis and Cost-Benefit Analysis

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 22 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.

---

## Section 1: Welcome and Module Overview [00:00 - 03:00]

Welcome to Module 08. I am Professor Nash. Today we are covering feasibility analysis and cost-benefit analysis — the tools BAs use to evaluate whether a proposed system is worth building before a single line of code is written.

[SHOW DIAGRAM: Title slide — "Module 08: Feasibility Analysis and Cost-Benefit Analysis" with BABOK KA 2 and KA 4 labels and IIBA ECBA badge]

Feasibility analysis answers the question: can and should we build this? It examines the proposed solution from four angles — technical, economic, operational, and legal. Cost-benefit analysis answers the financial version of that question: do the projected benefits justify the costs, and by how much?

These are not just academic exercises. In real organizations, poorly conducted feasibility analysis leads to projects that fail not because they were built wrong but because no one seriously asked whether they should be built at all. The BA's responsibility in needs assessment — covered in BABOK KA 2 — includes evaluating solution viability before committing organizational resources.

---

## Section 2: The Four Dimensions of Feasibility [03:00 - 10:00]

[SHOW DIAGRAM: Four-quadrant grid labeled with the four feasibility dimensions — Technical (top left), Economic (top right), Operational (bottom left), Legal/Ethical (bottom right) — each quadrant listing 2–3 key evaluation questions]

Feasibility analysis examines a proposed solution from four distinct perspectives. All four must be assessed — a project that passes three and fails one is still infeasible.

Technical feasibility asks: can we build this? Does the required technology exist? Does the organization have — or can it acquire — the expertise to develop, deploy, and maintain the system? Does the proposed solution integrate with existing systems without creating unacceptable technical risk? Technical feasibility failures happen when organizations propose systems that require technology no one on the team understands, or integration with legacy systems whose interfaces are undocumented.

Economic feasibility asks: is it worth building? Do the projected benefits exceed the projected costs, and does the return justify the investment? This is where cost-benefit analysis lives. A project with a negative Net Present Value — where costs exceed benefits in present-day terms — fails economic feasibility. A project where the payback period exceeds the system's useful life is also a red flag.

Operational feasibility asks: will it work in practice? Will users adopt it? Does it fit the organization's workflows, culture, and capacity to change? A technically excellent system that users refuse to use delivers zero business value. Operational feasibility includes change management assessment — how much organizational change is required, and is the organization capable of managing it?

Legal and ethical feasibility asks: are there regulatory, legal, contractual, or ethical constraints on the proposed solution? Data privacy regulations, industry compliance requirements, intellectual property concerns, and organizational policies all fall under this dimension. A proposed system that would violate HIPAA, GDPR, or an existing vendor contract fails legal feasibility.

> IIBA ECBA Exam Tip: The exam tests the ability to match a scenario to the correct feasibility dimension. Key mapping: Skills or technology gap = Technical. Cost exceeds benefit = Economic. User resistance or adoption risk = Operational. Regulatory violation = Legal. Practice this mapping with scenarios until it is automatic.

---

## Section 3: Cost-Benefit Analysis [10:00 - 16:00]

[SHOW DIAGRAM: Cost-benefit analysis framework table — rows for Development Costs, Operating Costs, Total Costs; Tangible Benefits, Intangible Benefits, Total Benefits; and calculated metrics ROI, Payback Period, NPV — with sample values filled in for a hypothetical system]

Cost-benefit analysis quantifies the economic case for a system. Let me cover the three key metrics the ECBA exam tests.

Return on Investment — ROI — measures the net benefit as a percentage of total cost. The formula is: ROI equals Net Benefit divided by Total Cost, multiplied by 100%. Net Benefit equals Total Benefits minus Total Costs. An ROI of 40% means the project returns $0.40 in net benefit for every $1.00 invested. Higher ROI is better. A positive ROI means the project covers its own costs and generates surplus value.

Payback Period measures how long it takes for cumulative benefits to equal cumulative costs. The formula is: Payback Period equals Total Cost divided by Annual Net Benefit. If a project costs $300,000 and generates $75,000 per year in net benefits, the payback period is four years. This tells decision makers when they will break even. Shorter payback periods are preferable when the organization needs to recover investment quickly.

Net Present Value — NPV — accounts for the time value of money. A dollar received three years from now is worth less than a dollar received today, because today's dollar can be invested to generate returns. NPV discounts all future cash flows to their present-day equivalent using a discount rate — typically the organization's cost of capital. A positive NPV means the project creates value. A negative NPV means it destroys value relative to the discount rate.

[SHOW DIAGRAM: NPV calculation example — Year 0 through Year 4, showing initial investment as a negative value, annual benefit values, discount factors at 8%, and discounted cash flows summing to a positive NPV]

> IIBA ECBA Exam Tip: Know the definitions and formulas for all three metrics. ROI = percentage return on investment. Payback Period = time to break even. NPV = present-day value of future net benefits. The exam will present a number and ask you to identify which metric it represents. A percentage = ROI. A time measurement in years = Payback Period. A dollar amount with a positive or negative sign = NPV.

---

## Section 4: Tangible vs. Intangible Benefits and Costs [16:00 - 19:30]

Cost-benefit analysis works best with tangible, quantifiable benefits and costs. But real projects always include intangible elements that resist easy quantification. BAs must identify both.

Tangible benefits are measurable in dollars: reduced labor costs, eliminated process steps, increased transaction throughput, reduced error rates that translate to fewer costly corrections. These can be directly entered into the financial model.

Intangible benefits are real but harder to quantify: improved customer satisfaction, higher employee morale, better competitive positioning, reduced reputational risk. These should be documented and described qualitatively even when they cannot be precisely valued.

Similarly, costs come in two categories. Development costs are one-time: hardware, software licenses, development labor, testing, training, and deployment. Operating costs are ongoing: maintenance, support, subscription fees, and periodic upgrades. A complete cost model includes both.

Total Cost of Ownership — TCO — captures the full life-cycle cost of a system including both development and operating costs over the expected useful life. Decision makers who only look at development costs and ignore operating costs routinely underestimate total investment.

---

## Section 5: Lab Preview and Closing [19:30 - 22:00]

This week's lab gives you practice conducting a complete feasibility analysis and building a cost-benefit model. You will evaluate a proposed system from all four feasibility dimensions and calculate ROI, payback period, and NPV from a provided data set.

Three exam reminders. First: match the scenario to the correct feasibility dimension — technical means can we build it, economic means is it worth it, operational means will it work in practice, legal means is it allowed. Second: positive NPV means the project creates value; negative NPV means it destroys value. Third: ROI is a percentage; payback period is a time measurement in years.

---

## Module 08 Complete

Next: Module 09 - System Design: Logical vs. Physical Design

### Additional Resources

- iiba.org — BABOK Guide v3 KA 2: Needs Assessment — feasibility analysis context
- iiba.org — ECBA exam blueprint weighting information
