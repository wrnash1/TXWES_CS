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
