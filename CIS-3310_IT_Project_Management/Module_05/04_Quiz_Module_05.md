# Quiz: Module 05 – Cost Management: Budgeting and EVM

**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

What is the definition of the Critical Path in project scheduling?

- A) The path containing the most complex tasks
- B) The longest path of dependent activities that determines the shortest possible project duration
- C) The path with the highest cost
- D) The sequence of non-dependent milestones

Correct Answer: B) The critical path is the longest sequence of dependent activities through the network diagram; any delay to tasks on this path directly delays the project end date.

Distractor Analysis:

- *Why B is correct:* The critical path has zero total float. The project's minimum duration equals the total duration of the critical path. This is the most tested CPM definition on Project+ and CAPM.
- *Why A is incorrect:* Complexity is not a defining attribute of the critical path; a simple long-duration task can be critical, while a complex short-duration task is not.
- *Why C is incorrect:* The critical path is defined by time (duration/float), not by cost. The most expensive path and the critical path are often different.
- *Why D is incorrect:* Critical path activities are dependent on each other by definition. Non-dependent milestones would have no float relationship to the critical path.

---

## Question 2

Which of the following best defines the Backward Pass (Late Start/Finish) in Critical Path Method calculations?

- A) A right-to-left calculation through the network diagram that determines the latest an activity can start and finish without delaying the project end date.
- B) A left-to-right calculation that determines the earliest an activity can start and finish given its predecessors.
- C) A technique that adds resources to critical path tasks to compress the project schedule while increasing cost.
- D) A method of estimating activity durations using the average of optimistic, most likely, and pessimistic estimates.

Correct Answer: A) A right-to-left calculation through the network diagram that determines the latest an activity can start and finish without delaying the project end date.

Distractor Analysis:

- *Why A is correct:* The backward pass calculates Late Finish (LF) and Late Start (LS) for every activity. Combined with the forward pass, it enables float calculation. LS = LF - Duration + 1.
- *Why B is incorrect:* That description defines the forward pass, which computes Early Start (ES) and Early Finish (EF) moving left-to-right through the network.
- *Why C is incorrect:* Adding resources to critical path tasks describes "crashing," a schedule compression technique, not the backward pass.
- *Why D is incorrect:* Averaging optimistic, most likely, and pessimistic estimates describes PERT estimating, not a CPM calculation pass.

---

## Question 3

A project has the following activities: A(3 days) → B(4 days) → C(2 days) and A(3 days) → D(6 days) → C(2 days). What is the critical path duration?

- A) 9 days (path A-B-C)
- B) 11 days (path A-D-C)
- C) 6 days (activity D alone)
- D) 5 days (activities A and C only)

Correct Answer: B) 11 days — the path A → D → C has a total duration of 3 + 6 + 2 = 11 days, which is longer than A → B → C (3 + 4 + 2 = 9 days).

Distractor Analysis:

- *Why B is correct:* The critical path is the longest path. A → D → C = 3+6+2 = 11 days. A → B → C = 3+4+2 = 9 days. Therefore A → D → C is critical.
- *Why A is incorrect:* Path A-B-C (9 days) is not the longest path. Activity B has 2 days of float.
- *Why C is incorrect:* Activity D alone is 6 days, but the critical path includes all activities on the longest sequence.
- *Why D is incorrect:* Summing only A and C ignores the intermediate activities that are required to complete the path.

---

## Question 4

During project execution, the earned value (EV) is $40,000, the planned value (PV) is $50,000, and the actual cost (AC) is $45,000. What is the Schedule Variance (SV)?

- A) SV = -$10,000 (behind schedule)
- B) SV = +$5,000 (ahead of schedule)
- C) SV = -$5,000 (over budget)
- D) SV = +$10,000 (under budget)

Correct Answer: A) SV = EV - PV = $40,000 - $50,000 = -$10,000. A negative SV means the project is behind schedule.

Distractor Analysis:

- *Why A is correct:* Schedule Variance (SV) = EV - PV. A negative result indicates the project is behind its planned progress. SV measures schedule performance in dollar terms, not days.
- *Why B is incorrect:* SV = $40,000 - $50,000 = -$10,000, not +$5,000. A positive SV would indicate ahead-of-schedule performance.
- *Why C is incorrect:* Cost Variance (CV) = EV - AC = $40,000 - $45,000 = -$5,000 (over budget). That calculates CV, not SV — this answer mixes up the two formulas.
- *Why D is incorrect:* +$10,000 would result from reversing the SV formula (PV - EV), which is incorrect.

---

## Question 5

A project has a Budget at Completion (BAC) of $200,000 and a Cost Performance Index (CPI) of 0.80. Using the EAC = BAC/CPI formula, what is the Estimate at Completion?

- A) $160,000
- B) $200,000
- C) $250,000
- D) $240,000

Correct Answer: C) EAC = BAC / CPI = $200,000 / 0.80 = $250,000. A CPI below 1.0 means the project is over budget, so the revised total cost forecast is higher than the original budget.

Distractor Analysis:

- *Why C is correct:* EAC = BAC / CPI = $200,000 / 0.80 = $250,000. With CPI = 0.80 (spending $1.25 per $1.00 of work), the final cost is projected to exceed the original budget.
- *Why A is incorrect:* $160,000 = $200,000 × 0.80, which incorrectly multiplies rather than divides. That would give a lower forecast, contradicting an over-budget situation.
- *Why B is incorrect:* $200,000 is the original BAC; the EAC adjusts for actual performance and will differ from BAC whenever CPI ≠ 1.0.
- *Why D is incorrect:* $240,000 does not result from the standard EAC = BAC/CPI formula with these values.

---

## Question 6

A project manager is setting aside $18,000 in the budget to cover identified risks documented in the Risk Register. What type of reserve is this, and is it part of the Cost Baseline?

- A) Management Reserve; not part of the Cost Baseline
- B) Contingency Reserve; part of the Cost Baseline
- C) Contingency Reserve; not part of the Cost Baseline
- D) Management Reserve; part of the Cost Baseline

Correct Answer: B) Contingency Reserve; part of the Cost Baseline.

Distractor Analysis:

- *Why B is correct:* Contingency reserves are budgeted for identified risks (known unknowns) documented in the Risk Register. They are part of the Cost Baseline and are controlled by the PM. Management reserves are NOT part of the baseline.
- *Why A is incorrect:* Management Reserves are for unknown unknowns — completely unforeseen events. Funds for identified risks are Contingency Reserves, and they ARE part of the Cost Baseline.
- *Why C is incorrect:* The type is correctly identified as Contingency Reserve, but Contingency Reserves are included in the Cost Baseline (unlike Management Reserves).
- *Why D is incorrect:* These are Contingency Reserves (tied to identified risks), not Management Reserves. Management Reserves are unplanned and excluded from the baseline.

---

## Question 7

A project has a BAC of $400,000, an EV of $160,000, and an AC of $200,000. What is the CPI, and what does it indicate?

- A) CPI = 1.25; the project is under budget
- B) CPI = 0.80; the project is over budget
- C) CPI = 0.80; the project is behind schedule
- D) CPI = 1.25; the project is ahead of schedule

Correct Answer: B) CPI = EV/AC = $160,000 / $200,000 = 0.80; the project is over budget (getting only $0.80 of value for every $1.00 spent).

Distractor Analysis:

- *Why B is correct:* CPI = EV / AC = 160,000 / 200,000 = 0.80. CPI < 1.0 means over budget — the team is spending more than the value of work it is producing.
- *Why A is incorrect:* 1.25 would result from inverting the formula (AC / EV instead of EV / AC). A CPI of 1.25 would indicate under budget, not over budget.
- *Why C is incorrect:* CPI measures cost performance, not schedule performance. "Behind schedule" is indicated by SPI, not CPI.
- *Why D is incorrect:* CPI = 1.25 would require EV > AC. Here EV ($160,000) is less than AC ($200,000), so CPI < 1.0.

---

## Question 8

At Month 9 of a 12-month project, the BAC is $300,000, AC is $220,000, and EAC = $330,000. What is the Variance at Completion (VAC)?

- A) VAC = +$30,000 (projected under budget)
- B) VAC = -$30,000 (projected over budget)
- C) VAC = +$110,000 (remaining budget)
- D) VAC = -$80,000 (amount over budget)

Correct Answer: B) VAC = BAC - EAC = $300,000 - $330,000 = -$30,000 (projected to finish $30,000 over budget).

Distractor Analysis:

- *Why B is correct:* VAC = BAC - EAC = $300,000 - $330,000 = -$30,000. A negative VAC means the project is projected to finish over the original budget.
- *Why A is incorrect:* A positive $30,000 would require BAC > EAC. Here EAC ($330,000) exceeds BAC ($300,000), so VAC is negative.
- *Why C is incorrect:* $110,000 = EAC - AC = $330,000 - $220,000, which is actually the ETC (Estimate to Complete), not the VAC.
- *Why D is incorrect:* -$80,000 does not result from the VAC = BAC - EAC formula with these values.

---

## Question 9

Which cost estimating technique is most appropriate when the project sponsor needs a quick, rough estimate and the project has only a high-level scope description with no WBS?

- A) Bottom-up estimating
- B) Parametric estimating
- C) Analogous (top-down) estimating
- D) Definitive estimating

Correct Answer: C) Analogous (top-down) estimating — uses historical data from similar projects to produce a fast, high-level estimate when detailed scope information is not yet available.

Distractor Analysis:

- *Why C is correct:* Analogous estimating is the fastest technique and requires only a high-level scope comparison to a similar prior project. It produces a ROM estimate appropriate for early feasibility analysis.
- *Why A is incorrect:* Bottom-up estimating requires a complete WBS with detailed work packages — precisely what is not available in this scenario. It is the most accurate but also the most time-consuming technique.
- *Why B is incorrect:* Parametric estimating requires reliable unit-rate data (cost per server, hours per module). Without a WBS or detailed scope, there is no basis for applying unit rates.
- *Why D is incorrect:* Definitive estimating is synonymous with bottom-up estimating in many contexts — it requires complete scope detail and is inappropriate at the high-level stage described.

---

## Question 10

A project's current CPI is 0.92 and SPI is 1.05. Which statement best describes the project's status?

- A) The project is under budget and behind schedule
- B) The project is over budget and ahead of schedule
- C) The project is under budget and ahead of schedule
- D) The project is over budget and behind schedule

Correct Answer: B) The project is over budget and ahead of schedule — CPI < 1.0 indicates over budget; SPI > 1.0 indicates ahead of schedule.

Distractor Analysis:

- *Why B is correct:* CPI = 0.92 means for every $1.00 spent, only $0.92 of work is produced (over budget). SPI = 1.05 means 105% of planned work has been completed (ahead of schedule). These two conditions can coexist.
- *Why A is incorrect:* Under budget requires CPI > 1.0. A CPI of 0.92 is below 1.0, indicating over budget, not under budget.
- *Why C is incorrect:* CPI = 0.92 is over budget (not under). The SPI interpretation of ahead of schedule is correct, but the cost interpretation is wrong.
- *Why D is incorrect:* SPI = 1.05 indicates ahead of schedule (not behind). The cost interpretation of over budget is correct, but the schedule interpretation is wrong.

---

## Question 11

A project has a Budget at Completion (BAC) of $200,000, Planned Value (PV) of $80,000, Earned Value (EV) of $70,000, and Actual Cost (AC) of $85,000. What is the Schedule Variance (SV)?

- A) -$15,000 (behind schedule)
- B) +$10,000 (ahead of schedule)
- C) -$10,000 (behind schedule)
- D) +$15,000 (ahead of schedule)

**Correct Answer:** C) -$10,000 (behind schedule)

**Distractor Analysis:**

- *Why C is correct:* SV = EV - PV = $70,000 - $80,000 = -$10,000. A negative SV means the project has earned less value than planned — it is behind schedule.
- *Why A is incorrect:* -$15,000 would result from CV = EV - AC = $70,000 - $85,000 = -$15,000. That is the Cost Variance, not Schedule Variance.
- *Why B is incorrect:* A positive SV would require EV > PV. Here EV ($70,000) < PV ($80,000), so SV is negative.
- *Why D is incorrect:* $15,000 positive is the CV in absolute terms but with the wrong sign; it also uses the wrong formula for SV.

---

## Question 12

Using the same values from Question 11 (BAC=$200,000, EV=$70,000, AC=$85,000), what is the Cost Performance Index (CPI)?

- A) 1.21
- B) 0.88
- C) 0.82
- D) 1.14

**Correct Answer:** C) 0.82

**Distractor Analysis:**

- *Why C is correct:* CPI = EV / AC = $70,000 / $85,000 = 0.824, rounded to 0.82. A CPI below 1.0 means the project is getting less than $1.00 of value for every $1.00 spent — it is over budget.
- *Why A is incorrect:* 1.21 would indicate under budget performance; it does not result from any standard EVM formula using these values.
- *Why B is incorrect:* 0.88 = SPI = EV / PV = $70,000 / $80,000. This is the Schedule Performance Index, not the CPI.
- *Why D is incorrect:* 1.14 = AC / EV = $85,000 / $70,000 — the formula is inverted. CPI = EV / AC, not AC / EV.

---

## Question 13

A project manager wants to estimate the total cost at completion using the assumption that all remaining work will be performed at the BUDGETED cost rate (current variances are considered atypical). Which EAC formula should she use?

- A) EAC = BAC / CPI
- B) EAC = AC + ETC
- C) EAC = AC + (BAC - EV)
- D) EAC = AC + [(BAC - EV) / CPI]

**Correct Answer:** C) EAC = AC + (BAC - EV)

**Distractor Analysis:**

- *Why C is correct:* EAC = AC + (BAC - EV) assumes the remaining work (BAC - EV = ETC) will be completed at the original budgeted rate. This formula is used when the current variance is believed to be a one-time event that will not recur.
- *Why A is incorrect:* EAC = BAC / CPI assumes the current CPI will continue for all remaining work. This is the formula for the "typical" variance assumption — the opposite of what the question describes.
- *Why B is incorrect:* EAC = AC + ETC is the generic formula, not a specific EAC variant. It requires a separately estimated ETC value rather than using a formula-based ETC.
- *Why D is incorrect:* EAC = AC + [(BAC - EV) / CPI] assumes the current CPI AND SPI will both persist for remaining work. This is the most pessimistic EAC formula.

---

## Question 14

The project sponsor asks the project manager what it will cost to complete the remaining work if performance continues at the current rate. Which EVM metric should the PM report?

- A) VAC (Variance at Completion)
- B) ETC (Estimate to Complete)
- C) EAC (Estimate at Completion)
- D) TCPI (To-Complete Performance Index)

**Correct Answer:** B) ETC (Estimate to Complete)

**Distractor Analysis:**

- *Why B is correct:* ETC is the expected cost to complete ALL remaining project work from the current point. The question asks specifically what it will cost from now to completion — that is ETC = EAC - AC.
- *Why A is incorrect:* VAC (Variance at Completion = BAC - EAC) tells you how far over or under budget the project is expected to finish — not what it costs to finish the remaining work.
- *Why C is incorrect:* EAC is the expected total cost at the END of the project (including what has already been spent). The sponsor is asking only about the remaining cost, not the total.
- *Why D is incorrect:* TCPI is an efficiency ratio showing what CPI is needed going forward to meet the original BAC or EAC target. It is a performance target, not a cost forecast.

---

## Question 15

What does the To-Complete Performance Index (TCPI) measure?

- A) The cost efficiency achieved so far on the project
- B) The CPI required for all remaining work to stay within the approved budget
- C) The total amount of budget remaining at the current time
- D) The schedule efficiency required to hit the planned completion date

**Correct Answer:** B) The CPI required for all remaining work to stay within the approved budget.

**Distractor Analysis:**

- *Why B is correct:* TCPI = (BAC - EV) / (BAC - AC). It answers the question: "To finish within budget, how efficiently must we perform the remaining work?" A TCPI > 1.0 means the team must work more efficiently than it has been — often a red flag.
- *Why A is incorrect:* CPI measures cost efficiency achieved to date, not what is needed going forward.
- *Why C is incorrect:* Budget remaining = BAC - AC is a simpler calculation that does not account for earned value or required future performance.
- *Why D is incorrect:* TCPI is a cost metric, not a schedule metric. Schedule efficiency is measured by SPI and related formulas.

---

## Question 16

Which of the following best describes "contingency reserve" in project cost management?

- A) Funds held by senior management for unplanned changes outside the project scope
- B) Budget set aside for known risks that have been identified and assigned a probability of occurrence
- C) The difference between the project's BAC and its current EAC
- D) Funds used to cover cost overruns discovered during project closure

**Correct Answer:** B) Budget set aside for known risks that have been identified and assigned a probability of occurrence.

**Distractor Analysis:**

- *Why B is correct:* Contingency reserve is planned reserve allocated for "known unknowns" — risks identified in the Risk Register. It is included in the Cost Baseline and controlled by the project manager.
- *Why A is incorrect:* Funds held by senior management for unplanned or out-of-scope events describe management reserve — which is NOT part of the Cost Baseline.
- *Why C is incorrect:* The difference between BAC and EAC is Variance at Completion (VAC) — a performance metric, not a reserve definition.
- *Why D is incorrect:* Contingency reserve is planned before project execution, not discovered at closure. Using reserve at closure may be appropriate, but that is not its definition.

---

## Question 17

A project manager reports an SPI of 0.78 to the steering committee. Which of the following plain-language translations is CORRECT?

- A) The project is spending 78 cents for every dollar of work completed — it is under budget.
- B) The project has completed only 78% of the work that was planned to be done by this point in time — it is behind schedule.
- C) The project will cost 78% more than originally planned by the time it finishes.
- D) The project has delivered 78% of the total planned scope.

**Correct Answer:** B) The project has completed only 78% of the work that was planned to be done by this point in time — it is behind schedule.

**Distractor Analysis:**

- *Why B is correct:* SPI = EV / PV. An SPI of 0.78 means only $0.78 of planned work has been completed for every $1.00 of work that should have been done — the project is behind schedule.
- *Why A is incorrect:* That description matches CPI (cost efficiency), not SPI. Spending per dollar of work completed is a cost metric, not a schedule metric.
- *Why C is incorrect:* A cost overrun percentage describes a cost variance metric, not SPI.
- *Why D is incorrect:* SPI at a point in time compares EV to PV at that moment — it does not represent the percentage of total planned scope delivered. Total scope progress would be measured differently (percent complete).

---

## Question 18

Which estimating technique produces the MOST accurate cost estimate and requires a complete, detailed WBS?

- A) Analogous estimating
- B) Parametric estimating
- C) Rough Order of Magnitude (ROM)
- D) Bottom-up estimating

**Correct Answer:** D) Bottom-up estimating

**Distractor Analysis:**

- *Why D is correct:* Bottom-up estimating requires every work package in the WBS to be individually estimated, then summed. It is the most time-consuming but also the most accurate technique.
- *Why A is incorrect:* Analogous estimating uses historical data from similar past projects — it is fast but least accurate, typically used in early project phases.
- *Why B is incorrect:* Parametric estimating multiplies a unit rate by a quantity metric (e.g., $50/hour × 200 hours). It is more accurate than analogous but less accurate than bottom-up because it relies on standard unit rates that may not match the specific work package.
- *Why C is incorrect:* ROM (Rough Order of Magnitude) is the roughest estimate, with an accuracy range of -25% to +75%. It is used for initial budget requests, not for detailed project planning.

---

## Question 19

A project's BAC is $500,000 and the current EAC is $575,000. What is the Variance at Completion (VAC), and what does it mean?

- A) VAC = +$75,000; the project is projected to finish under budget.
- B) VAC = -$75,000; the project is projected to finish over budget by $75,000.
- C) VAC = $575,000; the project's revised total budget.
- D) VAC = 0.87; the CPI needed to bring the project back on budget.

**Correct Answer:** B) VAC = -$75,000; the project is projected to finish over budget by $75,000.

**Distractor Analysis:**

- *Why B is correct:* VAC = BAC - EAC = $500,000 - $575,000 = -$75,000. A negative VAC means the project is projected to overrun its original budget.
- *Why A is incorrect:* A positive VAC would require EAC < BAC. Since EAC > BAC here, VAC is negative (over budget, not under).
- *Why C is incorrect:* $575,000 is the EAC itself — not the VAC. VAC is the difference between BAC and EAC, not EAC itself.
- *Why D is incorrect:* 0.87 is a ratio — it looks like a TCPI or CPI value, not VAC. VAC is expressed in dollars, not as a ratio.

---

## Question 20

A project manager is preparing a cost performance report and calculates that EV = $120,000, AC = $130,000, PV = $115,000. Which statement is TRUE about this project?

- A) The project is under budget and ahead of schedule.
- B) The project is over budget and behind schedule.
- C) The project is over budget and ahead of schedule.
- D) The project is under budget and behind schedule.

**Correct Answer:** C) The project is over budget and ahead of schedule.

**Distractor Analysis:**

- *Why C is correct:* CV = EV - AC = $120,000 - $130,000 = -$10,000 (over budget, since negative). SV = EV - PV = $120,000 - $115,000 = +$5,000 (ahead of schedule, since positive). Both conditions can coexist.
- *Why A is incorrect:* CV is negative ($120K - $130K = -$10K), indicating over budget, not under budget.
- *Why B is incorrect:* SV is positive ($120K - $115K = +$5K), indicating ahead of schedule, not behind.
- *Why D is incorrect:* Under budget requires CV > 0 (EV > AC). Here EV < AC, so the project is over budget.
