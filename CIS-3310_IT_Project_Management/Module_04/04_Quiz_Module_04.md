# Quiz: Module 04 - Schedule Management – Gantt Charts and CPM
## Course: CIS-3310_IT_Project_Management (CompTIA Project+ / PMI CAPM)

---

**Question 1**
Which dependency type describes a scenario where Task B cannot start until Task A has completed?
*   A) Start-to-Start (SS)
*   B) Finish-to-Start (FS)
*   C) Finish-to-Finish (FF)
*   D) Start-to-Finish (SF)
*   **Correct Answer:** B) Finish-to-Start is the most common scheduling linkage; the predecessor activity must end before the successor activity can begin.
*   **Distractor Analysis:**
    *   *Why B is correct:* FS is the default dependency type in most project schedules. Example: "Testing (B) cannot start until Development (A) finishes."
    *   *Why A is incorrect:* Start-to-Start means B cannot *start* until A *starts*—both activities begin around the same time, but B cannot initiate before A does.
    *   *Why C is incorrect:* Finish-to-Finish means B cannot *finish* until A *finishes*—both may run concurrently but B must wait for A to complete before B can complete.
    *   *Why D is incorrect:* Start-to-Finish (the rarest type) means B cannot *finish* until A *starts*—almost never used in practice.

---

**Question 2**
Which of the following best defines **Dependency Types (Finish-to-Start, FS)** in project schedule management?
*   A) The four logical relationships between activities (FS, SS, FF, SF) that define in what order tasks must be performed relative to each other.
*   B) A risk response strategy that involves reducing the probability or impact of a negative risk event before it occurs.
*   C) A cost management technique that compares earned value against actual costs to measure budget efficiency.
*   D) The process of assigning human and material resources to each activity in the project schedule.
*   **Correct Answer:** A) The four logical relationships between activities (FS, SS, FF, SF) that define in what order tasks must be performed relative to each other.
*   **Distractor Analysis:**
    *   *Why A is correct:* Dependency types define the precedence relationships that drive the network diagram and ultimately determine the critical path. All four types—FS, SS, FF, and SF—are tested on the exam.
    *   *Why B is incorrect:* Reducing probability or impact of a risk describes the "mitigate" risk response strategy, which belongs to Risk Management, not schedule dependency management.
    *   *Why C is incorrect:* Comparing earned value against actual costs describes the Cost Performance Index (CPI), a concept from Earned Value Management and Cost Management.
    *   *Why D is incorrect:* Assigning resources to activities describes resource management or the resource loading process, not dependency types.

---

**Question 3**
A project manager needs to compress the project schedule because the delivery date has moved up by two weeks. She decides to overlap the testing phase with the last week of development. Which schedule compression technique is she using?
*   A) Crashing
*   B) Resource leveling
*   C) Fast-tracking
*   D) Schedule baselining
*   **Correct Answer:** C) Fast-tracking is a schedule compression technique where activities normally done in sequence are performed in parallel or with overlap, increasing risk.
*   **Distractor Analysis:**
    *   *Why C is correct:* Overlapping tasks that were planned sequentially is the definition of fast-tracking. It reduces schedule duration but increases the risk of rework because later tasks begin before earlier tasks are fully complete.
    *   *Why A is incorrect:* Crashing compresses the schedule by adding more resources (e.g., overtime, additional staff) to critical path activities; it increases cost, not just risk.
    *   *Why B is incorrect:* Resource leveling adjusts the schedule to resolve resource over-allocation conflicts; it typically extends the schedule rather than compressing it.
    *   *Why D is incorrect:* Schedule baselining locks in the approved schedule for comparison and control; it does not compress the schedule.

---

**Question 4**
On a Gantt chart, how is a milestone typically represented?
*   A) A horizontal bar spanning the entire project duration
*   B) A vertical line separating project phases
*   C) A diamond shape with zero duration
*   D) A shaded rectangle indicating the critical path
*   **Correct Answer:** C) Milestones are represented as diamond shapes with zero duration on a Gantt chart, marking significant points or events in the project.
*   **Distractor Analysis:**
    *   *Why C is correct:* A milestone has no duration—it represents a point in time (e.g., "Design approved," "System go-live"). The diamond symbol is the universal convention in Gantt charts and is tested on the Project+ exam.
    *   *Why A is incorrect:* A horizontal bar spanning the full duration would represent the project summary bar, not a milestone.
    *   *Why B is incorrect:* Vertical lines are sometimes used to mark the current date on a Gantt chart, but they do not represent milestones.
    *   *Why D is incorrect:* Critical path activities may be highlighted differently (often in red), but the milestone symbol is specifically a diamond, not a shaded rectangle.

---

**Question 5**
In schedule management, what does **lag time** refer to?
*   A) The amount of time a successor activity can start before its predecessor finishes
*   B) A deliberate waiting period inserted between the end of a predecessor activity and the start of a successor activity
*   C) The total amount of time a non-critical activity can be delayed without delaying the project end date
*   D) The estimated duration assigned to each activity during schedule planning
*   **Correct Answer:** B) Lag time is a deliberate delay applied to a dependency relationship—the successor cannot begin until a specified amount of time has passed after the predecessor finishes.
*   **Distractor Analysis:**
    *   *Why B is correct:* Lag adds a wait period to a dependency. For example, after pouring concrete (A), you must wait 3 days (lag = +3 days) before installing tiles (B). Lag extends the schedule.
    *   *Why A is incorrect:* That definition describes lead time, which is the opposite—allowing a successor to start before its predecessor is done (represented as negative lag). Lead compresses the schedule.
    *   *Why C is incorrect:* The ability to delay a task without affecting the project end date describes float (slack), a CPM concept, not lag time.
    *   *Why D is incorrect:* Estimated duration is assigned during activity duration estimating; it is not the same as lag, which modifies the relationship between two activities.
