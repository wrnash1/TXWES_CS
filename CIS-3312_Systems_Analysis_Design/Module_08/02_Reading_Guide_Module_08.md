# Reading Guide: Module 08 - Feasibility Analysis and Cost-Benefit Analysis

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 08 covers feasibility analysis and cost-benefit analysis — the tools BAs use to evaluate whether a proposed system or solution is viable before resources are committed. Feasibility analysis examines the solution from four dimensions: technical, economic, operational, and legal. Cost-benefit analysis quantifies the financial return using metrics including ROI, payback period, and NPV. Both techniques appear in BABOK Guide v3 KA 2 (Needs Assessment) and are tested on the IIBA ECBA exam.

---

## 1. Core Vocabulary

### 1.1 Feasibility Analysis

Feasibility analysis is a structured evaluation of whether a proposed solution can be built, is worth building, will be adopted by users, and is legally permissible. It is conducted during the needs assessment phase before detailed requirements analysis begins. A feasibility study informs the go/no-go decision at project initiation.

### 1.2 Technical Feasibility

Technical feasibility evaluates whether the required technology exists, whether the organization has or can acquire the skills and infrastructure to build and operate the system, and whether the proposed solution integrates with existing systems. A system that requires capabilities no vendor or internal team can deliver within project constraints fails technical feasibility.

### 1.3 Economic Feasibility

Economic feasibility evaluates whether the projected benefits justify the costs. It is the primary financial evaluation of a proposed system. Economic feasibility is determined through cost-benefit analysis — if the benefits outweigh the costs (positive ROI, acceptable payback period, positive NPV), the system is economically feasible.

### 1.4 Operational Feasibility

Operational feasibility evaluates whether the proposed system will be adopted and successfully used in the organizational environment. It considers user readiness, workflow fit, change management requirements, and cultural factors. A system that is technically and economically feasible but operationally infeasible — because users will not use it — delivers no value.

### 1.5 Legal and Ethical Feasibility

Legal and ethical feasibility evaluates whether the proposed system complies with applicable laws, regulations, contracts, and organizational policies. Relevant constraints include data privacy regulations (HIPAA, GDPR), industry-specific compliance requirements, intellectual property restrictions, and contractual obligations.

### 1.6 Cost-Benefit Analysis (CBA)

Cost-benefit analysis is a financial modeling technique that quantifies and compares the projected costs and benefits of a proposed system over its useful life. CBA produces metrics — ROI, payback period, NPV — that enable decision makers to assess whether and when the investment will pay off.

### 1.7 Return on Investment (ROI)

ROI measures net benefit as a percentage of total cost. Formula: ROI = (Net Benefit / Total Cost) x 100%. Net Benefit = Total Benefits - Total Costs. A positive ROI means benefits exceed costs. ROI is expressed as a percentage.

### 1.8 Payback Period

Payback period is the time required for cumulative benefits to equal cumulative costs (break-even point). Formula: Payback Period = Total Cost / Annual Net Benefit. Expressed in years or months. A shorter payback period means faster recovery of investment.

### 1.9 Net Present Value (NPV)

NPV is the sum of all future project cash flows (benefits minus costs) discounted to present-day value using a discount rate. Formula: NPV = sum of [Cash Flow(t) / (1 + r)^t] for each year t. Positive NPV means the project creates value; negative NPV means it destroys value. NPV accounts for the time value of money.

### 1.10 Total Cost of Ownership (TCO)

TCO is the full life-cycle cost of a system, including one-time development costs (hardware, software, development labor, testing, training, deployment) and ongoing operating costs (maintenance, support, subscriptions, upgrades) over the expected useful life.

### 1.11 Tangible vs. Intangible Benefits

Tangible benefits are directly measurable in financial terms (cost savings, revenue increases, error reduction with quantifiable cost impact). Intangible benefits are real but difficult to quantify (improved customer satisfaction, competitive advantage, employee morale). Both should be documented in a feasibility study.

---

## 2. Four Dimensions of Feasibility

| Dimension | Question | Failure Example |
|---|---|---|
| Technical | Can we build it with available technology and skills? | Required AI capability unavailable from any vendor within timeline |
| Economic | Do benefits justify costs? | Project NPV is negative; costs exceed benefits over useful life |
| Operational | Will users adopt it and does it fit workflows? | Users resist new system; projected adoption rate of 30% |
| Legal/Ethical | Does it comply with regulations and policies? | System stores patient data in a way that violates HIPAA |

---

## 3. Cost-Benefit Analysis Metrics

| Metric | Formula | Unit | Interpretation |
|---|---|---|---|
| ROI | (Net Benefit / Total Cost) x 100% | Percentage | Higher = better return per dollar invested |
| Payback Period | Total Cost / Annual Net Benefit | Years (or months) | Shorter = faster break-even |
| NPV | Sum of discounted net cash flows | Dollars | Positive = creates value; Negative = destroys value |

---

## 4. Development Costs vs. Operating Costs

| Cost Category | Examples |
|---|---|
| Development (one-time) | Hardware purchase, software licenses, development labor, testing, training, deployment, data migration |
| Operating (ongoing) | Annual maintenance, technical support, subscription renewals, periodic upgrades, user support |

---

## 5. Tangible vs. Intangible Benefits

| Benefit Type | Examples | How to Document |
|---|---|---|
| Tangible | Reduced labor hours, eliminated paper processing, fewer data entry errors, faster transaction processing | Quantify in dollars; include in financial model |
| Intangible | Improved customer satisfaction, competitive differentiation, employee morale, reduced reputational risk | Describe qualitatively; include as supporting rationale |

---

## 6. Feasibility Analysis in the BABOK Framework

Feasibility analysis is primarily conducted as part of BABOK KA 2: Needs Assessment. The BA identifies the problem or opportunity, determines the current state, defines the desired future state, and assesses the feasibility of proposed solutions before selecting the recommended approach. Feasibility findings inform the Business Case — the formal document that captures the justification for undertaking a project.

---

## 7. Common CBA Pitfalls

BAs who conduct cost-benefit analysis should be aware of common errors that undermine the analysis:

Optimism bias: systematically underestimating costs and overestimating benefits. Mitigation: use conservative (pessimistic) scenarios in addition to expected scenarios.

Omitting operating costs: modeling only development costs while ignoring ongoing maintenance, support, and upgrade costs. Mitigation: use TCO rather than development cost alone.

Ignoring intangible costs: change management, productivity dip during transition, user training time. Mitigation: document and estimate these even approximately.

Ignoring intangible benefits: treating only quantifiable benefits as valid. Mitigation: document and describe qualitative benefits as supporting evidence.

Incorrect discount rate: using an inappropriate discount rate in NPV calculations. Mitigation: use the organization's published cost of capital or hurdle rate.

---

## 8. Certification Exam Tips

1. The exam tests the ability to match a scenario description to the correct feasibility dimension. Practice this mapping: skills or technology gap = Technical; cost exceeds benefit = Economic; user resistance or adoption concern = Operational; regulatory or legal constraint = Legal. One scenario, one dimension — identify it immediately.

2. ROI, payback period, and NPV definitions are tested in detail. Know: ROI is a percentage. Payback period is a time measurement. NPV is a dollar amount with a positive or negative sign. If the exam presents a number and asks which metric it represents, the unit is the giveaway.

3. NPV positive means the project creates value (benefits exceed costs at the discount rate). NPV negative means the project destroys value (costs exceed benefits). This is directly tested — do not confuse negative NPV with a budget variance or cost overrun.

4. Payback period formula is Payback = Total Cost / Annual Net Benefit. If the exam presents a scenario with total cost and annual benefit, calculate and select the matching year. Practice this calculation until it takes less than 30 seconds.

5. ROI formula is (Net Benefit / Total Cost) x 100%. Net Benefit = Total Benefits - Total Costs. Be careful: Total Benefits does not equal Net Benefit. You must subtract costs first.

6. Operational feasibility includes user adoption, workflow fit, and change management. A question about strong user resistance or cultural objections to a new system is testing operational feasibility — not technical or economic.

7. The Business Case is the primary deliverable that captures the results of feasibility analysis. BABOK KA 2 positions the Business Case as the output of needs assessment. The exam may ask which deliverable documents the justification for a project.

8. Total Cost of Ownership differs from development cost. TCO includes ongoing operating costs across the full useful life. A project with low development cost but high annual operating cost may have poor TCO even if the initial investment seems affordable.

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, KA 2: Needs Assessment — Assess Capability Gaps and Recommend Actions tasks
- BABOK Guide v3, Chapter 10 (Techniques) — Business Cases; Financial Analysis

Supplemental reading:

- Any standard corporate finance reference covering NPV, IRR, payback period, and ROI formulas
- Project Management Institute PMBOK Guide — Business Case section for additional context

---

## 10. Study Checklist

- [ ] Name all four feasibility dimensions and give one example of a failure in each.
- [ ] Calculate ROI from a provided cost and benefit scenario.
- [ ] Calculate payback period from a provided cost and annual benefit.
- [ ] Explain NPV in your own words, including the role of the discount rate.
- [ ] Distinguish tangible benefits from intangible benefits with two examples of each.
- [ ] Explain the difference between development cost and TCO.
- [ ] Identify the BABOK knowledge area where feasibility analysis is primarily located.
- [ ] Watch the Module 08 video lecture.
- [ ] Complete the Module 08 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.
