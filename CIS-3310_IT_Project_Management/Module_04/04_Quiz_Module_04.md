# Quiz: Module 04 – Schedule Management: Gantt Charts and CPM

**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

Which dependency type describes a scenario where Task B cannot start until Task A has completed?

- A) Start-to-Start (SS)
- B) Finish-to-Start (FS)
- C) Finish-to-Finish (FF)
- D) Start-to-Finish (SF)

Correct Answer: B) Finish-to-Start is the most common scheduling linkage; the predecessor must end before the successor can begin.

Distractor Analysis:

- *Why B is correct:* FS is the default dependency type in most project schedules. Example: "Testing cannot start until Development finishes."
- *Why A is incorrect:* Start-to-Start means B cannot start until A starts — both begin around the same time, but B cannot initiate before A does.
- *Why C is incorrect:* Finish-to-Finish means B cannot finish until A finishes — both may run concurrently but B must wait for A to complete before B can complete.
- *Why D is incorrect:* Start-to-Finish (the rarest type) means B cannot finish until A starts — almost never used in practice.

---

## Question 2

Which of the following best defines the four logical dependency types (FS, SS, FF, SF) in project schedule management?

- A) The four logical relationships between activities that define in what order tasks must be performed relative to each other.
- B) A risk response strategy that involves reducing the probability or impact of a negative risk event before it occurs.
- C) A cost management technique that compares earned value against actual costs to measure budget efficiency.
- D) The process of assigning human and material resources to each activity in the project schedule.

Correct Answer: A) The four logical relationships between activities that define in what order tasks must be performed relative to each other.

Distractor Analysis:

- *Why A is correct:* Dependency types define the precedence relationships that drive the network diagram and ultimately determine the critical path. All four types are tested on the exam.
- *Why B is incorrect:* Reducing probability or impact of a risk describes the "mitigate" risk response strategy, which belongs to Risk Management.
- *Why C is incorrect:* Comparing earned value against actual costs describes the Cost Performance Index (CPI), a concept from Earned Value Management.
- *Why D is incorrect:* Assigning resources to activities describes resource management, not dependency types.

---

## Question 3

A project manager needs to compress the project schedule because the delivery date has moved up by two weeks. She decides to overlap the testing phase with the last week of development. Which schedule compression technique is she using?

- A) Crashing
- B) Resource leveling
- C) Fast-tracking
- D) Schedule baselining

Correct Answer: C) Fast-tracking is a schedule compression technique where activities normally done in sequence are performed in parallel or with overlap, increasing risk.

Distractor Analysis:

- *Why C is correct:* Overlapping tasks that were planned sequentially is the definition of fast-tracking. It reduces schedule duration but increases the risk of rework because later tasks begin before earlier tasks are fully complete.
- *Why A is incorrect:* Crashing compresses the schedule by adding more resources to critical path activities; it increases cost, not just risk.
- *Why B is incorrect:* Resource leveling adjusts the schedule to resolve resource over-allocation conflicts; it typically extends the schedule rather than compressing it.
- *Why D is incorrect:* Schedule baselining locks in the approved schedule for comparison and control; it does not compress the schedule.

---

## Question 4

On a Gantt chart, how is a milestone typically represented?

- A) A horizontal bar spanning the entire project duration
- B) A vertical line separating project phases
- C) A diamond shape with zero duration
- D) A shaded rectangle indicating the critical path

Correct Answer: C) Milestones are represented as diamond shapes with zero duration on a Gantt chart, marking significant points or events in the project.

Distractor Analysis:

- *Why C is correct:* A milestone has no duration — it represents a point in time (e.g., "Design approved," "System go-live"). The diamond symbol is the universal convention in Gantt charts and is tested on the Project+ exam.
- *Why A is incorrect:* A horizontal bar spanning the full duration represents the project summary bar, not a milestone.
- *Why B is incorrect:* Vertical lines are sometimes used to mark the current date on a Gantt chart, but they do not represent milestones.
- *Why D is incorrect:* Critical path activities may be highlighted differently, but the milestone symbol is specifically a diamond, not a shaded rectangle.

---

## Question 5

In schedule management, what does lag time refer to?

- A) The amount of time a successor activity can start before its predecessor finishes
- B) A deliberate waiting period inserted between the end of a predecessor activity and the start of a successor activity
- C) The total amount of time a non-critical activity can be delayed without delaying the project end date
- D) The estimated duration assigned to each activity during schedule planning

Correct Answer: B) Lag time is a deliberate delay applied to a dependency relationship — the successor cannot begin until a specified amount of time has passed after the predecessor finishes.

Distractor Analysis:

- *Why B is correct:* Lag adds a wait period to a dependency. For example, after pouring concrete (A), you must wait 3 days (lag = +3 days) before installing tiles (B). Lag extends the schedule.
- *Why A is incorrect:* That definition describes lead time — allowing a successor to start before its predecessor is done (represented as negative lag). Lead compresses the schedule.
- *Why C is incorrect:* The ability to delay a task without affecting the project end date describes total float (slack), a CPM concept, not lag time.
- *Why D is incorrect:* Estimated duration is assigned during activity duration estimating; it is not the same as lag, which modifies the relationship between two activities.

---

## Question 6

A project has the following activities: A(4 days) → B(3 days) → E(4 days) and A(4 days) → C(7 days) → E(4 days). What is the critical path duration?

- A) 11 days (path A-B-E)
- B) 15 days (path A-C-E)
- C) 7 days (Activity C alone)
- D) 8 days (Activities A and E only)

Correct Answer: B) 15 days — the path A → C → E has a total duration of 4 + 7 + 4 = 15 days, which is longer than A → B → E (4 + 3 + 4 = 11 days).

Distractor Analysis:

- *Why B is correct:* The critical path is the longest path. A → C → E = 4 + 7 + 4 = 15 days. A → B → E = 4 + 3 + 4 = 11 days. Therefore A → C → E is critical with 15 days total duration.
- *Why A is incorrect:* Path A-B-E (11 days) is shorter. Activity B has 4 days of float relative to Activity C's path.
- *Why C is incorrect:* The critical path includes all activities on the longest sequence, not a single activity in isolation.
- *Why D is incorrect:* Summing only A and E ignores the intermediate activities. You must add the full path including all activities between start and finish.

---

## Question 7

Activity D has an Early Start of Day 10, a Late Start of Day 14, an Early Finish of Day 13, and a Late Finish of Day 17. What is the total float for Activity D, and is it on the critical path?

- A) Float = 4 days; not on the critical path
- B) Float = 0 days; on the critical path
- C) Float = 3 days; not on the critical path
- D) Float = 4 days; on the critical path

Correct Answer: A) Float = 4 days; not on the critical path — Total Float = LS - ES = 14 - 10 = 4 days.

Distractor Analysis:

- *Why A is correct:* Total Float = LS - ES = 14 - 10 = 4. Also verifiable as LF - EF = 17 - 13 = 4. Because float is greater than zero, Activity D is not on the critical path.
- *Why B is incorrect:* Zero float would mean LS = ES (or LF = EF). Here LS (14) does not equal ES (10), so float is not zero and D is not critical.
- *Why C is incorrect:* 3 days would require LS - ES = 3, which means LS = 13. But LS is 14, giving a difference of 4, not 3.
- *Why D is incorrect:* The float calculation of 4 days is correct, but a non-zero float means the activity is NOT on the critical path. Critical path activities have zero float by definition.

---

## Question 8

The project manager wants to shorten the schedule by adding overtime for the development team on critical path tasks. Which schedule compression technique is this?

- A) Fast-tracking
- B) Resource leveling
- C) Crashing
- D) Schedule compression baselining

Correct Answer: C) Crashing — adding resources (overtime counts as additional capacity) to critical path activities to reduce their duration.

Distractor Analysis:

- *Why C is correct:* Crashing means adding resources — people, equipment, or hours — to critical path activities. Overtime is a classic form of crashing. It reduces duration but increases cost.
- *Why A is incorrect:* Fast-tracking overlaps sequential activities. Adding overtime to a single task does not involve overlapping it with another task — it is crashing.
- *Why B is incorrect:* Resource leveling resolves over-allocation by adjusting timing, typically extending the schedule. It does not add resources or compress duration.
- *Why D is incorrect:* "Schedule compression baselining" is not a PMI-defined term. Baselining refers to locking an approved schedule, not compressing it.

---

## Question 9

A software project uses PERT three-point estimating for Activity Z. The optimistic estimate is 4 days, the most likely estimate is 7 days, and the pessimistic estimate is 16 days. What is the PERT expected duration?

- A) 7.0 days
- B) 8.0 days
- C) 9.0 days
- D) 10.5 days

Correct Answer: B) 8.0 days — PERT formula: (O + 4M + P) / 6 = (4 + 28 + 16) / 6 = 48 / 6 = 8.0 days.

Distractor Analysis:

- *Why B is correct:* (4 + 4×7 + 16) / 6 = (4 + 28 + 16) / 6 = 48 / 6 = 8.0 days. The factor of 4 applied to the most likely estimate weights the middle value more heavily.
- *Why A is incorrect:* 7.0 is the most likely (M) estimate alone — using only M ignores the optimistic and pessimistic estimates entirely.
- *Why C is incorrect:* 9.0 would result from a simple average: (4 + 7 + 16) / 3 = 27 / 3 = 9. The PERT formula weights M by a factor of 4, producing a different result.
- *Why D is incorrect:* 10.5 does not match any standard PERT or averaging formula applied to these three values.

---

## Question 10

Free float differs from total float in which key way?

- A) Free float measures how long a project can be delayed; total float measures how long an activity can be delayed.
- B) Free float is the delay an activity can absorb without delaying any successor's early start; total float is the delay an activity can absorb without delaying the project end date.
- C) Free float applies only to critical path activities; total float applies only to non-critical activities.
- D) Free float and total float are calculated using the same formula and produce identical results for every activity.

Correct Answer: B) Free float is the delay an activity can absorb without delaying any successor's early start; total float is the delay without delaying the project end date.

Distractor Analysis:

- *Why B is correct:* Total float measures slack relative to the project end date. Free float measures slack relative to the next activity. Free float is always less than or equal to total float. An activity can consume its free float without impacting any successor, but consuming total float will reduce float elsewhere on the path.
- *Why A is incorrect:* Neither float type measures project-level delays — both measure activity-level scheduling flexibility. Total float is not a project delay metric.
- *Why C is incorrect:* Critical path activities have zero total float and zero free float. Both types of float apply to non-critical activities, not the other way around.
- *Why D is incorrect:* Free float and total float use different formulas and produce equal values only when an activity has a single successor with no other predecessors feeding into it.

---

## Question 11

A project network diagram has the following paths with these durations: Path A = 22 days, Path B = 18 days, Path C = 25 days, Path D = 19 days. What is the minimum project duration and which path is critical?

- A) Minimum duration = 18 days; Path B is critical.
- B) Minimum duration = 25 days; Path C is critical.
- C) Minimum duration = 22 days; Path A is critical.
- D) Minimum duration = 19 days; Path D is critical.

**Correct Answer:** B) Minimum duration = 25 days; Path C is critical.

**Distractor Analysis:**

- *Why B is correct:* The critical path is the LONGEST path through the network, and it determines the earliest the project can finish. The project cannot complete until all paths are complete; therefore the minimum project duration equals the longest path — 25 days on Path C.
- *Why A is incorrect:* 18 days is the shortest path, which has the most float — the opposite of a critical path.
- *Why C is incorrect:* Path A at 22 days is longer than B and D but shorter than C. It is not the critical path.
- *Why D is incorrect:* Path D at 19 days has 6 days of float relative to the critical path (25 - 19 = 6). It is not critical.

---

## Question 12

An activity has an Early Start (ES) of Day 5, Early Finish (EF) of Day 12, Late Start (LS) of Day 9, and Late Finish (LF) of Day 16. What is the total float, and is this activity on the critical path?

- A) Total float = 0; this activity IS on the critical path.
- B) Total float = 4; this activity is NOT on the critical path.
- C) Total float = 7; this activity is NOT on the critical path.
- D) Total float = 3; this activity is NOT on the critical path.

**Correct Answer:** B) Total float = 4; this activity is NOT on the critical path.

**Distractor Analysis:**

- *Why B is correct:* Total float = LS - ES = 9 - 5 = 4 (or equivalently LF - EF = 16 - 12 = 4). Since total float > 0, the activity is not on the critical path. Critical path activities always have zero total float.
- *Why A is incorrect:* A total float of 0 would require LS = ES, which is not the case here (LS=9, ES=5, difference=4).
- *Why C is incorrect:* 7 does not match any valid float calculation using the values given.
- *Why D is incorrect:* 3 does not result from LS - ES (9-5=4) or LF - EF (16-12=4).

---

## Question 13

A project manager needs to compress the schedule by 5 days. Adding two more developers to the critical path activities would cost an additional $12,000 and reduce duration by 5 days. Overlapping the testing phase with the final development phase would save 5 days at no additional cost but increases the risk of rework. What compression techniques are described, respectively?

- A) Fast-tracking; crashing
- B) Crashing; fast-tracking
- C) Resource leveling; fast-tracking
- D) Crashing; resource smoothing

**Correct Answer:** B) Crashing; fast-tracking

**Distractor Analysis:**

- *Why B is correct:* Adding resources (developers) to shorten duration at increased cost = crashing. Overlapping phases that would normally be sequential = fast-tracking. Both are schedule compression techniques; crashing increases cost, fast-tracking increases risk.
- *Why A is incorrect:* The descriptions are reversed. Adding resources is crashing, not fast-tracking. Overlapping phases is fast-tracking, not crashing.
- *Why C is incorrect:* Resource leveling resolves resource over-allocation by delaying activities — it does not compress the schedule. It is not described here.
- *Why D is incorrect:* Resource smoothing adjusts activity timing within float limits to smooth resource demand — it is not a compression technique and does not shorten the critical path.

---

## Question 14

Which type of activity dependency is described by: "The successor activity cannot START until the predecessor activity has FINISHED"?

- A) Start-to-Start (SS)
- B) Finish-to-Finish (FF)
- C) Finish-to-Start (FS)
- D) Start-to-Finish (SF)

**Correct Answer:** C) Finish-to-Start (FS)

**Distractor Analysis:**

- *Why C is correct:* Finish-to-Start (FS) is the most common dependency type. The successor cannot begin until the predecessor is complete. Example: software must be coded (predecessor finishes) before it can be tested (successor starts).
- *Why A is incorrect:* Start-to-Start means both activities can begin simultaneously or the successor starts after the predecessor starts — the finish of the predecessor is not the trigger.
- *Why B is incorrect:* Finish-to-Finish means both activities must finish together — the successor cannot finish until the predecessor finishes, but they may overlap.
- *Why D is incorrect:* Start-to-Finish is the rarest dependency type: the successor cannot finish until the predecessor starts. It is almost never used in standard project management.

---

## Question 15

Which scheduling tool provides a VISUAL representation of project activities against a calendar timeline, showing start and end dates as horizontal bars?

- A) Network Diagram (PDM)
- B) Resource Breakdown Structure
- C) Gantt Chart
- D) PERT Chart

**Correct Answer:** C) Gantt Chart

**Distractor Analysis:**

- *Why C is correct:* A Gantt chart displays activities as horizontal bars on a calendar timeline. It is the most widely used project communication tool and is standard on the Project+ exam.
- *Why A is incorrect:* A network diagram (PDM) shows activity relationships and dependencies but does not display activities against a calendar. It is used for critical path analysis, not schedule communication.
- *Why B is incorrect:* A Resource Breakdown Structure is a hierarchical chart showing resource categories — not a schedule tool.
- *Why D is incorrect:* A PERT chart is a network diagram variation that also shows probabilistic time estimates — not a calendar-based bar chart.

---

## Question 16

Using the PERT three-point estimating formula, calculate the expected duration for an activity with Optimistic = 4 days, Most Likely = 8 days, and Pessimistic = 18 days.

- A) 8.0 days
- B) 9.0 days
- C) 8.67 days
- D) 10.0 days

**Correct Answer:** B) 9.0 days

**Distractor Analysis:**

- *Why B is correct:* Expected Duration = (O + 4M + P) / 6 = (4 + 4×8 + 18) / 6 = (4 + 32 + 18) / 6 = 54 / 6 = 9.0 days.
- *Why A is incorrect:* 8.0 is the most likely estimate alone, not the PERT weighted average.
- *Why C is incorrect:* 8.67 would result from a simple triangular average (O + M + P) / 3 = (4 + 8 + 18) / 3 = 30 / 3 = 10 — not even 8.67. This may reflect an arithmetic error in a different formula variant.
- *Why D is incorrect:* 10.0 is the simple average (O + M + P) / 3 = 30 / 3 = 10. The PERT formula weights M by a factor of 4, producing a different (and more accurate) result.

---

## Question 17

A project manager wants to represent that Activity B can start two days after Activity A starts (not after it finishes). Which dependency type with what modifier should be used?

- A) Finish-to-Start with a 2-day lag
- B) Start-to-Start with a 2-day lag
- C) Start-to-Start with a 2-day lead
- D) Finish-to-Finish with a 2-day lag

**Correct Answer:** B) Start-to-Start with a 2-day lag

**Distractor Analysis:**

- *Why B is correct:* Start-to-Start with a lag means "B can start 2 days AFTER A starts." The lag delays the successor relative to its dependency trigger. SS + 2-day lag = B starts on Day 3 if A starts on Day 1.
- *Why A is incorrect:* Finish-to-Start means B cannot start until A finishes — a different relationship that requires A to be complete before B begins.
- *Why C is incorrect:* A lead compresses the schedule (negative lag). A 2-day lead on SS would mean B starts 2 days BEFORE A starts — the opposite direction.
- *Why D is incorrect:* Finish-to-Finish with lag means B cannot finish until 2 days after A finishes — a completion dependency, not a start dependency.

---

## Question 18

What is the primary risk associated with fast-tracking a project schedule?

- A) Increased labor costs due to overtime pay
- B) Increased scope because more work is performed in parallel
- C) Increased probability of rework because activities that would normally be sequential are performed in parallel, and the outputs of earlier activities may change
- D) Decreased team morale because fast-tracking increases workload

**Correct Answer:** C) Increased probability of rework because activities that would normally be sequential are performed in parallel, and the outputs of earlier activities may change.

**Distractor Analysis:**

- *Why C is correct:* Fast-tracking's primary risk is rework. If Activity A is still in progress when Activity B starts using A's preliminary output, and A's output subsequently changes, B's work may need to be redone. This is the trade-off the PM accepts when fast-tracking.
- *Why A is incorrect:* Increased labor costs describe crashing, not fast-tracking. Fast-tracking typically does not require additional resources.
- *Why B is incorrect:* Fast-tracking does not add scope — it changes the timing/sequence of existing scope. The work to be done stays the same.
- *Why D is incorrect:* Team morale impacts are possible side effects of compression but are not the primary identified risk of fast-tracking in PMI literature.

---

## Question 19

An activity has a duration of 10 days and its predecessor must finish before it can start. The predecessor finishes on Day 15. There is also a 3-day lag requirement between the two activities. On which day does the successor's Early Start fall?

- A) Day 15
- B) Day 16
- C) Day 18
- D) Day 19

**Correct Answer:** D) Day 19

**Distractor Analysis:**

- *Why D is correct:* The successor has a Finish-to-Start dependency with a 3-day lag. The predecessor finishes on Day 15. The lag adds 3 days: Early Start of successor = Day 15 + 3 + 1 = Day 19 (the successor cannot start until Day 19, which is 3 days after the predecessor's finish).
- *Why A is incorrect:* Day 15 would be the ES with no lag — the immediate next possible start after the predecessor finishes, ignoring the required delay.
- *Why B is incorrect:* Day 16 would be the ES with a standard FS (no lag) — the day after the predecessor finishes.
- *Why C is incorrect:* Day 18 applies only a 2-day lag instead of 3.

---

## Question 20

A project manager is told she must deliver the project two weeks earlier than the current schedule allows. She can add contractors to critical path tasks (at $5,000 extra) or overlap the system testing phase with the final build phase (which increases defect risk). What factor should MOST influence her choice between crashing and fast-tracking?

- A) The preference of the development team
- B) The organization's risk tolerance and the availability of budget for additional contractors
- C) The number of remaining activities on the critical path
- D) Whether the project has been approved by the Change Control Board

**Correct Answer:** B) The organization's risk tolerance and the availability of budget for additional contractors.

**Distractor Analysis:**

- *Why B is correct:* Choosing between crashing and fast-tracking is a cost-vs-risk trade-off. If the organization can absorb additional cost, crashing is safer. If budget is constrained, fast-tracking may be necessary despite higher rework risk. The PM must evaluate both factors to make a justified recommendation.
- *Why A is incorrect:* Team preference is a factor in implementation but should not be the primary decision driver for a compression strategy that affects the project's cost and risk profile.
- *Why C is incorrect:* The number of remaining critical path activities affects how much compression is possible, but it does not determine which technique to use. The cost/risk trade-off is the primary decision factor.
- *Why D is incorrect:* CCB approval will be needed to implement either option, but the PM's recommendation must be built on cost and risk analysis first — CCB approval is the outcome of the process, not the input to the decision.
