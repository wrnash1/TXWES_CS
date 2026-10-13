# Video Script: Module 10 — Earned Value Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Production Notes

- Slides: Use clean slide deck with formula callouts highlighted in yellow
- Screen recording: Show spreadsheet calculations live during Segment 6
- Graphics: Timeline bar chart with PV/EV/AC overlays
- Tone: Conversational but precise — students should feel comfortable with math

---

## Segment 1 — Introduction and Why EVM Matters (0:00–2:30)

[SHOW SLIDE: Title — "Module 10: Earned Value Management"]

Welcome back to CIS-3310 IT Project Management. I'm Professor Nash, and today we are tackling one of the most important — and, I will admit, one of the most initially intimidating — topics in the entire Project+ exam: Earned Value Management, or EVM.

[PAUSE — 2 seconds]

Here is the honest truth about EVM. Most students see a wall of formulas and immediately go into panic mode. SPI, CPI, EAC, ETC — it looks like alphabet soup. But by the end of this module, you are going to see that every single formula is telling one simple story: how is my project doing right now compared to where it was supposed to be?

That is all EVM does. It answers that question with math instead of gut feelings.

[SHOW SLIDE: "Why EVM? — The Problem with Status Reports"]

Think about a typical project status meeting. The project manager says, "We have spent $400,000 so far and we are halfway done." Does that tell you whether the project is on track? Not really. You need to know what you were supposed to have accomplished by now. You need to know what that completed work is actually worth. EVM gives you a structured, objective way to answer both questions simultaneously.

[PAUSE — 2 seconds]

EVM originated in the U.S. Department of Defense in the 1960s, and it became a contractual requirement for large government projects. Today it is standard practice in IT project management, construction, aerospace, and any domain where budgets and schedules need rigorous monitoring.

[SHOW SLIDE: "EVM Is Heavily Tested on Project+"]

From a certification standpoint, CompTIA Project+ (exam code PK0-005) tests EVM in two ways. First, scenario questions where you calculate a value and interpret what it means. Second, conceptual questions about what each metric tells a project manager. We will practice both types today.

---

## Segment 2 — The Three Foundation Metrics: PV, EV, AC (2:30–7:00)

[SHOW SLIDE: "The Three Building Blocks of EVM"]

Every EVM formula is built from three base measurements. Learn these three, and everything else follows naturally.

[SHOW SLIDE: "Planned Value (PV)"]

The first is Planned Value, abbreviated PV. PV is also called the Budgeted Cost of Work Scheduled, or BCWS. PV answers the question: how much work did we plan to accomplish by this point in time, and what was that work budgeted to cost?

[PAUSE — 2 seconds]

For example, imagine you are managing a software development project with a total budget of $200,000. You planned to complete 40% of the work by the end of month three. Your PV at month three is `$200,000 × 0.40 = $80,000`. That eighty thousand dollars is what you planned to have accomplished in terms of budgeted cost.

[SHOW SLIDE: "Earned Value (EV)"]

The second metric is Earned Value, abbreviated EV. EV is also called the Budgeted Cost of Work Performed, or BCWP. EV answers the question: how much of the budget have we actually earned based on the work we have really completed?

[PAUSE — 2 seconds]

This is the trickiest concept for new students. EV is not how much money you have spent. It is the budgeted value of work you have actually finished. If your project is only 30% complete — not the 40% you planned — then your EV is `$200,000 × 0.30 = $60,000`. You have only earned $60,000 worth of work, even if you spent more than that to get there.

[SHOW SLIDE: "Actual Cost (AC)"]

The third metric is Actual Cost, abbreviated AC. AC is also called Actual Cost of Work Performed, or ACWP. AC is simply: how much money have we actually spent so far?

[PAUSE — 2 seconds]

AC is the easiest to understand — it is your real expenditure from the accounting system. Let us say your system shows you have spent $75,000 by month three. That is your AC: $75,000.

[SHOW SLIDE: "Our Running Example — Three Values Side by Side"]

Let me put these three together:

- PV = $80,000 (planned to finish 40%)
- EV = $60,000 (only finished 30%)
- AC = $75,000 (actually spent this amount)

[PAUSE — 3 seconds]

Just from these three numbers you can already tell something is wrong. You planned $80,000 worth of work but only got $60,000 worth done, and you spent $75,000 to do it. You are behind schedule and over budget. The variance formulas will quantify exactly how far off you are.

---

## Segment 3 — Variance Metrics: SV and CV (7:00–10:30)

[SHOW SLIDE: "Schedule Variance and Cost Variance"]

Now we move to the variance metrics. These tell you how far off track you are in dollar terms.

[SHOW SLIDE: "Schedule Variance Formula"]

Schedule Variance, or SV, measures how far ahead or behind schedule you are expressed in dollars. The formula is `SV = EV - PV`.

[PAUSE — 2 seconds]

In our example: `SV = $60,000 - $80,000 = -$20,000`. The negative sign tells you the project is behind schedule. A positive SV means ahead of schedule. An SV of zero means perfectly on schedule.

[SHOW SLIDE: "Cost Variance Formula"]

Cost Variance, or CV, measures how far over or under budget you are. The formula is `CV = EV - AC`.

[PAUSE — 2 seconds]

In our example: `CV = $60,000 - $75,000 = -$15,000`. Negative CV means over budget. Positive CV means under budget. Zero means exactly on budget.

[SHOW SLIDE: "The Universal Sign Rule — Negative Is Bad"]

Here is your memory anchor for all EVM variances: negative is bad, positive is good. When EV is less than PV, you have not done as much as planned — that is behind schedule. When EV is less than AC, you paid more than the work is worth — that is over budget.

[PAUSE — 2 seconds]

This works because EV is always in the first position of the subtraction. EV minus something: if EV is the smaller number, the result is negative, meaning bad. Write that down right now and put it on a sticky note.

[SHOW SLIDE: "Variance Summary Table"]

| Metric | Formula | Positive Means | Negative Means |
|--------|---------|----------------|----------------|
| SV | `EV - PV` | Ahead of schedule | Behind schedule |
| CV | `EV - AC` | Under budget | Over budget |

---

## Segment 4 — Performance Indices: SPI and CPI (10:30–14:00)

[SHOW SLIDE: "From Variances to Efficiency Ratios"]

Variances are great for communicating the dollar impact, but they are hard to compare across projects of different sizes. A $20,000 schedule variance on a $100,000 project is a crisis. The same variance on a $10 million project is almost noise. That is where performance indices come in — they give you a ratio, a percentage of efficiency that scales across any project size.

[SHOW SLIDE: "Schedule Performance Index"]

The Schedule Performance Index, or SPI, tells you what percentage of planned work you are actually accomplishing. The formula is `SPI = EV / PV`.

[PAUSE — 2 seconds]

In our example: `SPI = $60,000 / $80,000 = 0.75`. An SPI of 0.75 means you are getting 75 cents of work done for every dollar of work you planned. You are operating at 75% schedule efficiency.

[SHOW SLIDE: "Cost Performance Index"]

The Cost Performance Index, or CPI, tells you how efficiently you are spending money. The formula is `CPI = EV / AC`.

[PAUSE — 2 seconds]

In our example: `CPI = $60,000 / $75,000 = 0.80`. A CPI of 0.80 means you are getting only 80 cents of earned value for every dollar you spend. You are at 80% cost efficiency.

[SHOW SLIDE: "Index Interpretation — The 1.0 Rule"]

The rule for all indices: below 1.0 is bad, above 1.0 is good, exactly 1.0 is perfect.

- SPI less than 1.0 — behind schedule
- SPI greater than 1.0 — ahead of schedule
- CPI less than 1.0 — over budget
- CPI greater than 1.0 — under budget

[PAUSE — 2 seconds]

CPI is considered the most important single EVM metric because research on large government and commercial projects shows that a project's CPI tends to stabilize after the 20% completion mark. If your CPI is 0.80 at 20% done, the odds of recovering to 1.0 by the end are very low. This is why project sponsors pay close attention to early CPI readings rather than waiting until the project is 80% complete.

[SHOW SLIDE: "When to Use Variances vs. Indices"]

Use variances when you need to communicate the dollar impact to stakeholders — "we are $15,000 over budget" is concrete. Use indices when you need to compare efficiency across projects or feed forecasting formulas. Both show up on the Project+ exam.

---

## Segment 5 — Forecasting: EAC, ETC, and VAC (14:00–18:00)

[SHOW SLIDE: "Forecasting — Using EVM to Look Forward"]

So far we have been looking backward: how did we do up to this point? The real power of EVM is using those performance metrics to predict where the project will end up. These are called the forecasting metrics.

[SHOW SLIDE: "Budget at Completion — BAC"]

Before we can forecast, we need one more piece of data: the Budget at Completion, or BAC. BAC is simply the total authorized budget for the entire project. In our running example, BAC = $200,000. You always know BAC at project start — it does not change unless there is a formal approved scope change.

[SHOW SLIDE: "Estimate at Completion — Three Formulas"]

The Estimate at Completion, or EAC, predicts how much the total project will cost when finished. There are three EAC formulas the Project+ exam may test. You need all three.

[PAUSE — 3 seconds]

Formula 1 — EAC based on current CPI (the most common): `EAC = BAC / CPI`

This assumes the current cost efficiency rate will continue for the rest of the project. Use this when there is no reason to believe future performance will differ from past performance.

In our example: `EAC = $200,000 / 0.80 = $250,000`. The project is now forecasted to cost $250,000 instead of the original $200,000 budget.

[PAUSE — 2 seconds]

Formula 2 — EAC using a new bottom-up estimate: `EAC = AC + ETC`

Use this when the project team has generated a fresh, detailed estimate for the remaining work. You add actual spending to date to the new estimate for what remains.

[PAUSE — 2 seconds]

Formula 3 — EAC assuming remaining work proceeds at planned rate: `EAC = AC + (BAC - EV)`

This is the most optimistic formula. It treats past overruns as sunk costs and assumes future work will proceed exactly as originally planned. Use it when the cause of the overrun was a one-time event that will not repeat.

[SHOW SLIDE: "Estimate to Complete — ETC"]

The Estimate to Complete, or ETC, answers: how much more money do we need to finish the remaining work? The formula is `ETC = EAC - AC`.

[PAUSE — 2 seconds]

Using our Formula 1 EAC: `ETC = $250,000 - $75,000 = $175,000`. You need $175,000 more to complete the project.

[SHOW SLIDE: "Variance at Completion — VAC"]

The Variance at Completion, or VAC, predicts the final cost overrun or savings at project completion. The formula is `VAC = BAC - EAC`.

[PAUSE — 2 seconds]

In our example: `VAC = $200,000 - $250,000 = -$50,000`. A negative VAC means a $50,000 forecasted cost overrun. A positive VAC would mean a forecasted cost savings. On the Project+ exam, negative VAC is always a red flag requiring management attention.

[SHOW SLIDE: "Complete EVM Formula Reference"]

| Metric | Formula | What It Tells You |
|--------|---------|-------------------|
| SV | `EV - PV` | Schedule status in dollars |
| CV | `EV - AC` | Cost status in dollars |
| SPI | `EV / PV` | Schedule efficiency ratio |
| CPI | `EV / AC` | Cost efficiency ratio |
| EAC (CPI method) | `BAC / CPI` | Forecasted total cost |
| EAC (new estimate) | `AC + ETC` | Forecasted total cost with fresh estimate |
| EAC (planned rate) | `AC + (BAC - EV)` | Optimistic forecast |
| ETC | `EAC - AC` | Remaining cost to finish |
| VAC | `BAC - EAC` | Forecasted over/under at completion |

---

## Segment 6 — Worked Example and Exam Strategy (18:00–22:30)

[SHOW SLIDE: "Full Worked Example — Highland IT Upgrade Project"]

Let us work a complete exam-style EVM problem from scratch. This mirrors exactly the type of scenario question you will see on both the module quiz and the CompTIA Project+ exam.

[PAUSE — 3 seconds]

Scenario: The Highland IT Upgrade project has a total budget of $500,000 and a 10-month schedule. After 5 months, the project team has completed 45% of the total scope. The original schedule called for 50% completion at this point in time. The accounting system shows $240,000 has been spent.

[SHOW SLIDE: "Step 1 — Identify PV, EV, AC, BAC"]

Step 1 is always to extract and label the three base values plus BAC.

- BAC = $500,000
- PV = `$500,000 × 0.50 = $250,000` (planned 50% completion)
- EV = `$500,000 × 0.45 = $225,000` (actual 45% completion)
- AC = $240,000 (given by accounting system)

[SHOW SLIDE: "Step 2 — Calculate Variances"]

Step 2: Calculate SV and CV.

- `SV = EV - PV = $225,000 - $250,000 = -$25,000` — behind schedule
- `CV = EV - AC = $225,000 - $240,000 = -$15,000` — over budget

[SHOW SLIDE: "Step 3 — Calculate Indices"]

Step 3: Calculate SPI and CPI.

- `SPI = EV / PV = $225,000 / $250,000 = 0.90`
- `CPI = EV / AC = $225,000 / $240,000 = 0.9375` (approximately 0.94)

[SHOW SLIDE: "Step 4 — Forecast EAC, ETC, VAC"]

Step 4: Forecast using CPI method.

- `EAC = BAC / CPI = $500,000 / 0.9375 = $533,333`
- `ETC = EAC - AC = $533,333 - $240,000 = $293,333`
- `VAC = BAC - EAC = $500,000 - $533,333 = -$33,333`

[PAUSE — 3 seconds]

Interpretation: The project is slightly behind schedule (SPI of 0.90 means operating at 90% schedule efficiency) and slightly over budget (CPI of 0.94 means getting 94 cents of value per dollar spent). If current cost efficiency continues, the project will overspend its budget by approximately $33,333.

[SHOW SLIDE: "Three Exam Strategies for EVM Questions"]

Let me give you three strategies for handling EVM questions on the exam.

First: always extract PV, EV, and AC before computing anything. Label them. If the question gives percentages, multiply by BAC to convert to dollars before applying any formula.

Second: apply the sign rules mechanically. Negative variance always means bad. Index below 1.0 always means bad. If you calculate an index above 1.0 but the scenario describes a struggling project, check whether you have EV and AC in the right positions.

Third: when a question asks for EAC and specifies an assumption — "assuming current efficiency continues" points to `BAC / CPI`; "assuming remaining work at planned rate" points to `AC + (BAC - EV)`; "using a new estimate" points to `AC + ETC`.

[SHOW SLIDE: "Common Exam Traps to Avoid"]

Watch out for these four common exam traps.

Trap one: Confusing EV with AC. AC is money spent. EV is money earned based on completed work. They are never the same unless you are exactly on budget.

Trap two: Using the wrong EAC formula when the question specifies a future-performance assumption.

Trap three: Forgetting that SV is expressed in dollars, not time units. SPI is the ratio version.

Trap four: Calculating ETC as the remaining time or remaining scope percentage instead of remaining cost.

---

## Segment 7 — Closing Summary (22:30–24:00)

[SHOW SLIDE: "Module 10 Key Takeaways"]

Let us bring everything together. Earned Value Management is a performance measurement system that integrates scope, schedule, and cost into a single objective view of project health.

The three foundation metrics are Planned Value, Earned Value, and Actual Cost. From these, you derive Schedule Variance (`EV - PV`), Cost Variance (`EV - AC`), Schedule Performance Index (`EV / PV`), and Cost Performance Index (`EV / AC`). The forecasting metrics — EAC, ETC, and VAC — use current performance data to predict final project outcomes.

[PAUSE — 2 seconds]

The single most important principle: negative variances and indices below 1.0 are warning signals. CPI is the most predictive single metric — once it stabilizes after 20% completion, it rarely improves significantly.

[SHOW SLIDE: "Coming Up — Module 11: Risk Management"]

In Module 11 we shift to risk management — how to systematically identify, analyze, and respond to threats and opportunities on your project. Risk management connects directly to the cost and schedule performance we studied today; unmanaged risks are one of the primary drivers of poor CPI and SPI.

[PAUSE — 2 seconds]

Before you move on: complete the reading guide, work through the lab spreadsheet exercise, take the quiz, and post your discussion response. The discussion prompt asks you to interpret a real EVM scenario and make a managerial recommendation — connect your numbers to an action, not just a calculation.

I will see you in Module 11. You now know EVM. Practice the formulas until they are automatic.

[SHOW SLIDE: End card — Texas Wesleyan University | CIS-3310 | Professor Nash]

---

*End of Module 10 Video Script*

*Total estimated runtime: 22–24 minutes*
