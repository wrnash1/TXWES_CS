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
