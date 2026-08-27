# Quiz: Module 10 — Earned Value Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Question 1

A project has a Budget at Completion of $500,000. At the current status date, the project team has completed 40% of the total scope. The project was planned to be 50% complete by this date. What is the Earned Value (EV)?

- A) $250,000
- B) $200,000
- C) $150,000
- D) $300,000

**Correct Answer: B**

EV is calculated as `BAC × actual % complete = $500,000 × 0.40 = $200,000`. EV reflects the budgeted value of work actually accomplished, not the planned value or the amount spent.

Distractor Analysis:

- **Why B is correct:** EV always uses the actual completion percentage multiplied by BAC. The project is 40% done, so it has earned 40% of the total budget in value: `$500,000 × 0.40 = $200,000`.
- **Why A is incorrect:** $250,000 is the PV — `$500,000 × 0.50` using the planned 50% completion. PV and EV are different metrics that use different percentages.
- **Why C is incorrect:** $150,000 would correspond to 30% completion. No data supports this value. Confusing planned and actual percentages is the most common EVM calculation error.
- **Why D is incorrect:** $300,000 would correspond to 60% completion. There is no 60% figure in this problem. Students who arrive here have likely inverted a percentage or used the wrong base.

---

## Question 2

A project reports the following EVM data: `EV = $120,000`, `PV = $150,000`, `AC = $130,000`. What are the Schedule Variance and Cost Variance, and what do they indicate?

- A) SV = +$30,000 (ahead of schedule); CV = -$10,000 (over budget)
- B) SV = -$30,000 (behind schedule); CV = -$10,000 (over budget)
- C) SV = -$30,000 (behind schedule); CV = +$10,000 (under budget)
- D) SV = +$20,000 (ahead of schedule); CV = +$10,000 (under budget)

**Correct Answer: B**

`SV = EV - PV = $120,000 - $150,000 = -$30,000` (behind schedule). `CV = EV - AC = $120,000 - $130,000 = -$10,000` (over budget). Both variances are negative, indicating the project is both behind schedule and over budget.

Distractor Analysis:

- **Why B is correct:** Applying `SV = EV - PV` gives a negative result because EV ($120K) is less than PV ($150K) — behind schedule. Applying `CV = EV - AC` gives a negative result because EV ($120K) is less than AC ($130K) — over budget. Both formulas place EV in the minuend position.
- **Why A is incorrect:** This reverses the SV sign. SV = -$30,000 is behind schedule, not ahead. Getting the sign wrong on variance questions is the most common EVM exam error.
- **Why C is incorrect:** The CV sign is wrong. EV ($120K) is less than AC ($130K), making CV negative (over budget), not positive. Under-budget would require EV to exceed AC.
- **Why D is incorrect:** Both values are computed incorrectly. This answer likely results from subtracting in reverse order for both formulas. Always place EV first in the subtraction.

---

## Question 3

A project has `SPI = 0.85` and `CPI = 1.10`. Which statement best describes the project's status?

- A) Behind schedule and over budget
- B) Ahead of schedule and under budget
- C) Behind schedule and under budget
- D) Ahead of schedule and over budget

**Correct Answer: C**

SPI of 0.85 is below 1.0, indicating behind-schedule performance. CPI of 1.10 is above 1.0, indicating under-budget (cost-efficient) performance. The project has a schedule problem but a cost advantage.

Distractor Analysis:

- **Why C is correct:** SPI < 1.0 always means behind schedule. CPI > 1.0 always means under budget (more efficient than planned). The combination is not contradictory — a project can be slow but spending less than budgeted per unit of work.
- **Why A is incorrect:** The cost characterization is wrong. CPI = 1.10 means the project is getting $1.10 of value per dollar spent — that is under budget, not over budget.
- **Why B is incorrect:** The schedule characterization is wrong. SPI = 0.85 means only 85 cents of planned work is being accomplished per dollar of planned work — that is behind schedule, not ahead.
- **Why D is incorrect:** Both characterizations are wrong. This answer applies the index rules in reverse for both metrics. Review the threshold rule: above 1.0 is good, below 1.0 is bad.

---

## Question 4

A project's total budget (BAC) is $600,000. The current CPI is 0.75. Using the CPI-based forecast method, what is the Estimate at Completion (EAC)?

- A) $450,000
- B) $800,000
- C) $150,000
- D) $600,000

**Correct Answer: B**

`EAC = BAC / CPI = $600,000 / 0.75 = $800,000`. When CPI is below 1.0, EAC will always exceed BAC, indicating a forecasted cost overrun.

Distractor Analysis:

- **Why B is correct:** `EAC = BAC / CPI` is the CPI-trend formula. Dividing $600,000 by 0.75 gives $800,000. A CPI of 0.75 means the project is spending $1.33 for every $1.00 of value — the overrun compounds across the remaining work.
- **Why A is incorrect:** $450,000 = `$600,000 × 0.75`. This multiplies instead of divides. When CPI is below 1.0, dividing produces a larger number (the overrun forecast), not a smaller one.
- **Why C is incorrect:** $150,000 cannot be derived from any standard EVM formula using this data. This may result from subtracting rather than dividing.
- **Why D is incorrect:** $600,000 is BAC — the original budget, not the revised forecast. EAC equals BAC only when CPI is exactly 1.0. A CPI of 0.75 guarantees EAC will be higher than BAC.

---

## Question 5

After calculating EAC, a project manager needs to determine how much additional funding is required to complete the remaining work. The project has spent $180,000 so far and the EAC is $320,000. Which metric answers this question, and what is its value?

- A) VAC = $140,000
- B) ETC = $140,000
- C) VAC = -$140,000
- D) ETC = $500,000

**Correct Answer: B**

ETC (Estimate to Complete) is the cost needed to finish remaining work. `ETC = EAC - AC = $320,000 - $180,000 = $140,000`. ETC is the "how much more do we need" metric.

Distractor Analysis:

- **Why B is correct:** ETC measures remaining cost, not total cost or variance. `ETC = EAC - AC = $320,000 - $180,000 = $140,000`. This is the additional funding required to complete the project from its current state.
- **Why A is incorrect:** $140,000 labeled as VAC applies the correct arithmetic but the wrong metric. VAC = `BAC - EAC`, which requires BAC. Without BAC, VAC cannot be calculated from the data given. The question asks for additional funding needed, which is ETC.
- **Why C is incorrect:** This uses VAC with a negative sign, suggesting an overrun interpretation — but VAC requires BAC, which is not provided here. The negative sign also misapplies the formula.
- **Why D is incorrect:** $500,000 = `$180,000 + $320,000` — this adds AC and EAC, which has no meaning in EVM. ETC subtracts AC from EAC to find the remaining portion.

---

## Question 6

A project manager is preparing a status report and needs to communicate whether the project will come in over or under its original budget at completion. Which EVM metric specifically forecasts the final budget surplus or deficit?

- A) CV (Cost Variance)
- B) ETC (Estimate to Complete)
- C) CPI (Cost Performance Index)
- D) VAC (Variance at Completion)

**Correct Answer: D**

VAC (Variance at Completion) is the metric that forecasts the projected budget surplus or deficit at project end. Formula: `VAC = BAC - EAC`. A negative VAC indicates a projected overrun; a positive VAC indicates projected savings.

Distractor Analysis:

- **Why D is correct:** VAC is specifically designed to answer the "will we come in over or under budget at the end?" question. It compares the original budget (BAC) to the current forecast (EAC) and expresses the difference.
- **Why A is incorrect:** CV measures current cost performance — how over or under budget the project is at this moment. CV does not project forward to project completion.
- **Why B is incorrect:** ETC measures how much additional money is needed to finish. It is a remaining-cost estimate, not a variance from the original budget target.
- **Why C is incorrect:** CPI is an efficiency ratio that measures past cost performance. While CPI feeds the EAC calculation, it does not directly express a dollar surplus or deficit at completion.

---

## Question 7

A project team is 60% complete on a project with a BAC of $900,000. The project has spent $600,000. What is the Cost Variance (CV), and what does it tell the project manager?

- A) CV = +$60,000; the project is under budget
- B) CV = -$60,000; the project is over budget
- C) CV = -$60,000; the project is ahead of schedule
- D) CV = +$540,000; the project is under budget

**Correct Answer: B**

EV = `$900,000 × 0.60 = $540,000`. `CV = EV - AC = $540,000 - $600,000 = -$60,000`. The negative result means the project is over budget — it spent $600,000 to accomplish work worth only $540,000.

Distractor Analysis:

- **Why B is correct:** First calculate EV from BAC and actual completion: `$900,000 × 0.60 = $540,000`. Then `CV = $540,000 - $600,000 = -$60,000`. Negative CV always means over budget. The project paid $600K for work worth $540K.
- **Why A is incorrect:** A positive $60,000 would require EV to exceed AC. Here EV ($540K) is less than AC ($600K), making CV negative. Additionally, CV measures cost status, not schedule status.
- **Why C is incorrect:** The magnitude is correct but the interpretation is wrong. CV measures cost performance, not schedule performance. "Ahead of schedule" is indicated by SV or SPI, not CV.
- **Why D is incorrect:** $540,000 is the EV, not the CV. CV is the difference between EV and AC, not EV itself.

---

## Question 8

Which EAC formula should a project manager use when past cost overruns were caused by a one-time, non-recurring event and future work is expected to proceed at the originally planned efficiency rate?

- A) `EAC = BAC / CPI`
- B) `EAC = AC + ETC`
- C) `EAC = AC + (BAC - EV)`
- D) `EAC = EV / SPI`

**Correct Answer: C**

When past overruns are non-recurring and remaining work is expected to proceed at the planned rate, the correct formula is `EAC = AC + (BAC - EV)`. This formula takes actual spending to date and adds the remaining planned work (BAC minus EV) at the original budgeted rate.

Distractor Analysis:

- **Why C is correct:** This formula treats sunk costs (AC) as given and assumes remaining work will proceed exactly as planned. `BAC - EV` represents the remaining planned work value, and adding it to AC projects a total cost that corrects past overruns without compounding them into the future.
- **Why A is incorrect:** `BAC / CPI` assumes the current cost efficiency trend continues for all remaining work. This formula is appropriate when overruns are systemic and will persist — the opposite of the scenario described.
- **Why B is incorrect:** `AC + ETC` is used when the project team provides a fresh bottom-up estimate for remaining work. The scenario does not mention a new estimate — it states future work will proceed at the planned rate.
- **Why D is incorrect:** `EV / SPI` is not a standard EVM formula. It would produce a value numerically equivalent to PV but does not represent any recognized EAC calculation method.

---

## Question 9

A project has `BAC = $1,000,000`, `EV = $400,000`, and `AC = $500,000`. What is the To-Complete Performance Index (TCPI) if the project manager must finish within the original budget?

- A) 0.80
- B) 1.20
- C) 2.00
- D) 0.67

**Correct Answer: B**

`TCPI = (BAC - EV) / (BAC - AC) = ($1,000,000 - $400,000) / ($1,000,000 - $500,000) = $600,000 / $500,000 = 1.20`. A TCPI of 1.20 means the team must work 20% more efficiently than they have been to finish within the original budget.

Distractor Analysis:

- **Why B is correct:** TCPI (to BAC) = remaining work / remaining budget = `(BAC - EV) / (BAC - AC) = $600,000 / $500,000 = 1.20`. The team has $600,000 of work remaining but only $500,000 of budget left — they must improve efficiency by 20%.
- **Why A is incorrect:** 0.80 is the current CPI (`EV / AC = $400K / $500K`). CPI measures past efficiency; TCPI measures the efficiency required going forward. These are different metrics with different purposes.
- **Why C is incorrect:** 2.00 would require the remaining work to be double the remaining budget. Double-check whether the TCPI numerator and denominator are correctly placed. No data in this problem yields 2.00 using a standard formula.
- **Why D is incorrect:** 0.67 = `$400,000 / $600,000`, which is neither CPI nor TCPI using the correct formulas. Verify that both TCPI components — remaining work and remaining budget — are calculated by subtracting from BAC, not from each other.

---

## Question 10

An IT project has the following status: `SPI = 0.92`, `CPI = 0.88`. The project sponsor asks whether the project will recover. Based on EVM research on CPI stability, what is the most accurate statement the project manager can make?

- A) The project will likely recover because SPI is close to 1.0
- B) Because CPI has stabilized below 1.0, a significant cost recovery is statistically unlikely without major corrective action
- C) The project is in good shape because both indices are positive numbers
- D) CPI is irrelevant once the project passes the 50% completion mark

**Correct Answer: B**

Research on completed projects shows that CPI stabilizes after approximately 20% completion and rarely improves significantly. A CPI of 0.88 that has stabilized is a reliable predictor of a final cost overrun. Without major corrective action (scope reduction, resource reallocation, or schedule extension), recovery is unlikely.

Distractor Analysis:

- **Why B is correct:** This reflects the empirical finding that CPI tends to stabilize after 20% project completion. A CPI of 0.88 means the project is getting only 88 cents of value per dollar spent. If this efficiency level persists, `EAC = BAC / 0.88`, which is approximately 14% over budget at completion.
- **Why A is incorrect:** SPI proximity to 1.0 addresses schedule, not cost. The sponsor's question about recovery almost certainly concerns whether the project will come in within budget. SPI does not answer cost recovery questions.
- **Why C is incorrect:** Being a positive number is not the same as performing well. Indices of 0.92 and 0.88 are both below 1.0, indicating below-target performance on both dimensions — this is not "good shape."
- **Why D is incorrect:** CPI becomes more reliable and meaningful as the project progresses. It is most informative and most predictive after the 20% completion mark — the opposite of what this distractor claims.

---

## Question 11

A project has BAC = $600,000 and is 50% complete at the midpoint. The team has spent $360,000 so far. What is the current CPI, and what does it indicate?

- A) CPI = 0.83; the project is over budget.
- B) CPI = 1.20; the project is under budget.
- C) CPI = 1.00; the project is exactly on budget.
- D) CPI = 0.50; the project has spent its full budget prematurely.

**Correct Answer:** A) CPI = 0.83; the project is over budget.

**Distractor Analysis:**

- *Why A is correct:* EV = BAC × % complete = $600,000 × 0.50 = $300,000. CPI = EV / AC = $300,000 / $360,000 = 0.833. A CPI below 1.0 means the team is getting less than $1.00 of value for every $1.00 spent — the project is over budget.
- *Why B is incorrect:* A CPI of 1.20 would require EV > AC ($300K / AC = 1.20 → AC = $250K). The project has spent $360K, far more than $250K.
- *Why C is incorrect:* CPI = 1.00 would require EV = AC = $300K. The actual cost is $360K, not $300K.
- *Why D is incorrect:* CPI = 0.50 would require AC = $600K (the full BAC). The project has spent $360K, not the full budget.

---

## Question 12

Using the same project from Question 11 (BAC = $600,000, EV = $300,000, AC = $360,000), calculate the Estimate at Completion (EAC) using the formula that assumes the current CPI will continue.

- A) $660,000
- B) $720,000
- C) $630,000
- D) $600,000

**Correct Answer:** B) $720,000

**Distractor Analysis:**

- *Why B is correct:* EAC = BAC / CPI = $600,000 / 0.833 = $720,096, rounded to $720,000. This assumes the efficiency problem continues for all remaining work.
- *Why A is incorrect:* $660,000 = AC + (BAC - EV) = $360,000 + $300,000 — this uses the "atypical variance" formula, not the "CPI continues" formula.
- *Why C is incorrect:* $630,000 does not result from any standard EAC formula using these inputs.
- *Why D is incorrect:* $600,000 is the original BAC. EAC equals BAC only when CPI = 1.0. Since CPI = 0.833, the project is projected to overrun.

---

## Question 13

A project manager reports PV = $500,000, EV = $520,000, and AC = $490,000. Which statement accurately describes this project?

- A) Over budget and behind schedule
- B) Under budget and behind schedule
- C) Under budget and ahead of schedule
- D) Over budget and ahead of schedule

**Correct Answer:** C) Under budget and ahead of schedule

**Distractor Analysis:**

- *Why C is correct:* SV = EV - PV = $520,000 - $500,000 = +$20,000 (ahead of schedule, positive). CV = EV - AC = $520,000 - $490,000 = +$30,000 (under budget, positive). Both are favorable.
- *Why A is incorrect:* Both variances are positive — over budget and behind schedule would require negative CV and negative SV.
- *Why B is incorrect:* SV is positive (+$20K), indicating ahead of schedule — not behind.
- *Why D is incorrect:* CV is positive (+$30K), indicating under budget — not over budget.

---

## Question 14

What does Earned Value (EV) represent in EVM?

- A) The total amount of money the project has spent to date
- B) The amount of work that was planned to be done by a specific point in time, expressed in dollars
- C) The budgeted value of the work actually completed to date
- D) The difference between the project budget and the actual cost

**Correct Answer:** C) The budgeted value of the work actually completed to date.

**Distractor Analysis:**

- *Why C is correct:* EV = BAC × % work actually complete. It represents what the completed work was supposed to cost according to the original plan. EV is the bridge between schedule (what was done) and cost (what was budgeted for it).
- *Why A is incorrect:* Money spent to date is Actual Cost (AC). AC measures spending, not value earned from completed work.
- *Why B is incorrect:* The amount of work planned to be done by a given time is Planned Value (PV), not EV. PV is the schedule baseline value.
- *Why D is incorrect:* The difference between budget and actual cost is the Cost Variance (CV = EV - AC) — not EV itself.

---

## Question 15

At project completion, the final EAC is $850,000 for a project with BAC = $800,000. What is the Variance at Completion (VAC)?

- A) +$50,000 (under budget)
- B) -$50,000 (over budget)
- C) $800,000
- D) 0.94 (the CPI at completion)

**Correct Answer:** B) -$50,000 (over budget)

**Distractor Analysis:**

- *Why B is correct:* VAC = BAC - EAC = $800,000 - $850,000 = -$50,000. Negative VAC means the project finished over budget by $50,000.
- *Why A is incorrect:* A positive VAC would require EAC < BAC. Since EAC ($850K) > BAC ($800K), VAC is negative.
- *Why C is incorrect:* $800,000 is the BAC — not the VAC. The VAC is the difference between them.
- *Why D is incorrect:* 0.94 looks like a CPI-type ratio. VAC is always expressed in dollars, not as an index.

---

## Question 16

A project manager wants to forecast the remaining cost of work using the ETC formula that assumes future work will be done at the original budgeted efficiency. Which formula applies?

- A) ETC = EAC - AC
- B) ETC = (BAC - EV) / CPI
- C) ETC = BAC - EV
- D) ETC = AC + BAC

**Correct Answer:** C) ETC = BAC - EV

**Distractor Analysis:**

- *Why C is correct:* ETC = BAC - EV represents the remaining work valued at the original budgeted rate. It assumes the current variances are atypical and future work will proceed as planned — the "optimistic" ETC formula.
- *Why A is incorrect:* ETC = EAC - AC is the generic ETC formula. It calculates remaining cost as total expected cost minus what has already been spent, but requires EAC to be known separately and does not specify any performance assumption.
- *Why B is incorrect:* ETC = (BAC - EV) / CPI adjusts the remaining work for the current CPI — this assumes the efficiency problem will continue, not that future work will be done at budgeted rates.
- *Why D is incorrect:* AC + BAC is not a valid EVM formula. It would sum past spending with the total budget — a meaningless combination.

---

## Question 17

Which of the following correctly describes when to use the EAC formula EAC = AC + [(BAC - EV) / (CPI × SPI)]?

- A) When future work is expected to be completed at the original budgeted rate
- B) When both schedule and cost performance are expected to continue at current rates and both indexes are influencing the outcome
- C) When the project sponsor has approved a revised cost baseline
- D) When the current cost variance is believed to be a one-time exception

**Correct Answer:** B) When both schedule and cost performance are expected to continue at current rates and both indexes are influencing the outcome.

**Distractor Analysis:**

- *Why B is correct:* This composite EAC formula — dividing remaining work by both CPI and SPI — reflects projects where schedule pressure is compressing the time available to do remaining work and both performance inefficiencies are expected to persist.
- *Why A is incorrect:* Future work at the original rate describes EAC = AC + (BAC - EV), not the composite formula.
- *Why C is incorrect:* Sponsor approval of a revised baseline triggers a rebaselined BAC, not a specific EAC formula variant.
- *Why D is incorrect:* A one-time exception describes EAC = AC + (BAC - EV) — the formula that assumes the variance will not recur.

---

## Question 18

A project has a TCPI of 0.85. What does this mean?

- A) The team must work 15% more efficiently than it has been in order to meet the budget.
- B) The team can afford to work at 85% of its past efficiency and still meet the budget target.
- C) The project is 85% complete.
- D) The project is 15% over budget.

**Correct Answer:** B) The team can afford to work at 85% of its past efficiency and still meet the budget target.

**Distractor Analysis:**

- *Why B is correct:* A TCPI < 1.0 means the remaining budget is MORE than the remaining work requires. The team can deliver the rest of the project at only 85% of the efficiency required and still stay within budget — this is a favorable position.
- *Why A is incorrect:* Having to work more efficiently than before describes TCPI > 1.0. A TCPI of 0.85 is favorable, not a warning sign.
- *Why C is incorrect:* TCPI is a cost efficiency ratio, not a completion percentage. Percent complete is measured separately.
- *Why D is incorrect:* Being 15% over budget would be reflected in CPI (approximately 0.87) and VAC — not in TCPI. A TCPI of 0.85 is actually favorable news.

---

## Question 19

Which of the following is the BEST description of Planned Value (PV)?

- A) The total budget authorized for the project
- B) The budgeted cost of the work that was scheduled to be done by a specific point in time
- C) The actual cost incurred to date for all work performed
- D) The efficiency ratio of earned value to planned value

**Correct Answer:** B) The budgeted cost of the work that was scheduled to be done by a specific point in time.

**Distractor Analysis:**

- *Why B is correct:* PV is the schedule baseline expressed in dollars. At any point in time, PV answers: "According to the plan, how much work should have been completed and what should it have cost?" PV increases over time as planned work accumulates.
- *Why A is incorrect:* The total budget authorized for the project is the BAC (Budget at Completion) — PV at the end of the project equals BAC.
- *Why C is incorrect:* Actual cost to date is AC — what has actually been spent, regardless of how much work was planned or completed.
- *Why D is incorrect:* The efficiency ratio of EV to PV is the Schedule Performance Index (SPI), not PV itself.

---

## Question 20

A project is 75% complete, has a BAC of $400,000, a CPI of 0.95, and AC of $315,000. What is the Estimate to Complete (ETC) using the formula ETC = (BAC - EV) / CPI?

- A) $85,000
- B) $105,263
- C) $100,000
- D) $78,947

**Correct Answer:** B) $105,263

**Distractor Analysis:**

- *Why B is correct:* EV = BAC × % complete = $400,000 × 0.75 = $300,000. Remaining work = BAC - EV = $400,000 - $300,000 = $100,000. ETC = $100,000 / 0.95 = $105,263. This ETC assumes the current CPI inefficiency will continue for the remaining work.
- *Why A is incorrect:* $85,000 = AC - EV = $315,000 - $300,000 = $15,000 — no, that is CV. $400,000 - $315,000 = $85,000 is the simple remaining budget (BAC - AC), not ETC.
- *Why C is incorrect:* $100,000 = BAC - EV, which is the remaining work at the budgeted rate (the atypical variance ETC formula). It does not apply the CPI adjustment as the question requires.
- *Why D is incorrect:* $78,947 = EV / CPI = $300,000 / 3.8 — this does not correspond to any standard ETC formula using the given values.
