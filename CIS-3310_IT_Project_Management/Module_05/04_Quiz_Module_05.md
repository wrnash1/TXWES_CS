# Quiz: Module 05 - Cost Management – Budgeting and EVM
## Course: CIS-3310_IT_Project_Management (CompTIA Project+ / PMI CAPM)

---

**Question 1**
What is the definition of the Critical Path in project scheduling?
*   A) The path containing the most complex tasks
*   B) The longest path of dependent activities that determines the shortest possible project duration
*   C) The path with the highest cost
*   D) The sequence of non-dependent milestones
*   **Correct Answer:** B) The critical path is the longest sequence of dependent activities through the network diagram; any delay to tasks on this path directly delays the project end date.
*   **Distractor Analysis:**
    *   *Why B is correct:* The critical path has zero total float. The project's minimum duration equals the total duration of the critical path. This is the most tested CPM definition on Project+ and CAPM.
    *   *Why A is incorrect:* Complexity is not a defining attribute of the critical path; a simple task with a long duration can be critical, while a complex task with plenty of float is not.
    *   *Why C is incorrect:* The critical path is defined by time (duration/float), not by cost. The most expensive path and the critical path are often different.
    *   *Why D is incorrect:* Critical path activities are dependent on each other by definition. Non-dependent milestones describe activities with no predecessors or successors, which is the opposite of a sequenced critical path.

---

**Question 2**
Which of the following best defines the **Backward Pass (Late Start/Finish)** in Critical Path Method calculations?
*   A) A right-to-left calculation through the network diagram that determines the latest an activity can start and finish without delaying the project end date.
*   B) A left-to-right calculation that determines the earliest an activity can start and finish given its predecessors.
*   C) A technique that adds resources to critical path tasks to compress the project schedule while increasing cost.
*   D) A method of estimating activity durations using the average of optimistic, most likely, and pessimistic estimates.
*   **Correct Answer:** A) A right-to-left calculation through the network diagram that determines the latest an activity can start and finish without delaying the project end date.
*   **Distractor Analysis:**
    *   *Why A is correct:* The backward pass calculates Late Finish (LF) and Late Start (LS) for every activity. Combined with the forward pass results, it enables float calculation. LS = LF - Duration.
    *   *Why B is incorrect:* That description defines the forward pass, which computes Early Start (ES) and Early Finish (EF), working left-to-right through the network.
    *   *Why C is incorrect:* Adding resources to critical path tasks to compress the schedule describes "crashing," a schedule compression technique, not the backward pass.
    *   *Why D is incorrect:* Averaging optimistic, most likely, and pessimistic estimates describes the three-point (PERT) estimating technique, which is a duration estimation method, not a CPM calculation pass.

---

**Question 3**
A project has the following activities: A(3 days)→B(4 days)→C(2 days) and A(3 days)→D(6 days)→C(2 days). What is the critical path duration?
*   A) 9 days (path A-B-C)
*   B) 11 days (path A-D-C)
*   C) 6 days (activity D alone)
*   D) 5 days (activities A and C only)
*   **Correct Answer:** B) 11 days — the path A→D→C has a total duration of 3 + 6 + 2 = 11 days, which is longer than A→B→C (3 + 4 + 2 = 9 days).
*   **Distractor Analysis:**
    *   *Why B is correct:* The critical path is the longest path. Adding the durations: A→D→C = 3+6+2 = 11 days. A→B→C = 3+4+2 = 9 days. Therefore, A→D→C is critical with 11 days total.
    *   *Why A is incorrect:* Path A-B-C (9 days) is not the longest path. Activities B and D share float relative to D's path; B has 2 days of float.
    *   *Why C is incorrect:* Activity D has a duration of 6 days, but the critical path includes all activities on the longest sequence, not a single activity in isolation.
    *   *Why D is incorrect:* Including only A and C ignores the sequential activities in between. You must sum the entire path including intermediate activities.

---

**Question 4**
During project execution, the earned value (EV) is $40,000, the planned value (PV) is $50,000, and the actual cost (AC) is $45,000. What is the Schedule Variance (SV)?
*   A) SV = −$10,000 (behind schedule)
*   B) SV = +$5,000 (ahead of schedule)
*   C) SV = −$5,000 (over budget)
*   D) SV = +$10,000 (under budget)
*   **Correct Answer:** A) SV = EV − PV = $40,000 − $50,000 = −$10,000. A negative SV means the project is behind schedule—less work has been completed than was planned.
*   **Distractor Analysis:**
    *   *Why A is correct:* Schedule Variance (SV) = EV - PV. A negative result indicates the project is behind its planned progress. Note that SV measures schedule performance in dollar terms, not days.
    *   *Why B is incorrect:* SV = $40,000 − $50,000 = −$10,000, not +$5,000. A positive SV would indicate ahead-of-schedule performance.
    *   *Why C is incorrect:* Cost Variance (CV) = EV − AC = $40,000 − $45,000 = −$5,000 (over budget). That calculates CV, not SV—this answer mixes up the two formulas.
    *   *Why D is incorrect:* A positive value of $10,000 would result from reversing the SV formula (PV − EV), which is incorrect.

---

**Question 5**
A project has a Budget at Completion (BAC) of $200,000 and a Cost Performance Index (CPI) of 0.80. Using the EAC = BAC/CPI formula, what is the Estimate at Completion?
*   A) $160,000
*   B) $200,000
*   C) $250,000
*   D) $240,000
*   **Correct Answer:** C) EAC = BAC / CPI = $200,000 / 0.80 = $250,000. A CPI below 1.0 means the project is over budget, so the revised total cost forecast is higher than the original budget.
*   **Distractor Analysis:**
    *   *Why C is correct:* The EAC formula EAC = BAC/CPI gives the forecasted total project cost based on current spending efficiency. With CPI = 0.80 (spending $1.25 per $1.00 of work), the final cost is projected to exceed the original budget.
    *   *Why A is incorrect:* $160,000 = $200,000 × 0.80, which incorrectly multiplies rather than divides. That would give a lower forecast, which contradicts an over-budget situation.
    *   *Why B is incorrect:* $200,000 is the original BAC; the EAC adjusts for actual performance and will differ from BAC whenever CPI ≠ 1.0.
    *   *Why D is incorrect:* $240,000 does not result from the standard EAC = BAC/CPI formula; it may come from a different (incorrect) calculation approach.
