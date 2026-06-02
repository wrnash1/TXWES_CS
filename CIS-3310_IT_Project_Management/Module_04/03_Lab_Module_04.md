# Lab Activity: Module 04 – Schedule Management: Gantt Charts and CPM

**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005)
**Total Points:** 100
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Lab Overview

In this lab you will apply Module 04 schedule management concepts through three hands-on exercises: network diagram construction and critical path analysis, forward and backward pass calculations, and schedule compression decision-making. All work is done on paper or in a word processor — no scheduling software is required.

Submit all deliverables as a single PDF or Word document to the Canvas assignment portal. Show all calculations clearly.

---

## Scenario Background

Oakdale Medical Center (a fictional organization) is implementing a new patient portal system. The project manager has identified the following activities from the WBS:

| ID | Activity Name | Duration | Predecessors |
|---|---|---|---|
| A | Requirements Workshop | 5 days | None |
| B | Vendor Selection | 8 days | A |
| C | System Design | 6 days | A |
| D | Database Configuration | 4 days | B |
| E | Application Development | 10 days | C |
| F | Integration Testing | 5 days | D, E |
| G | User Acceptance Testing | 4 days | F |
| H | Staff Training | 3 days | G |
| I | Go-Live and Cutover | 2 days | G |
| J | Project Closure | 1 day | H, I |

---

## Part 1: Network Diagram and Critical Path

### Part 1 Objective

Construct the project network diagram, identify all paths, and determine the critical path and project duration.

### Part 1 Instructions

Complete the following steps and show all work.

#### Step 1 — Draw the Network Diagram

Draw an Activity-on-Node (AON) network diagram showing all 10 activities and their dependencies. Use boxes for activities and arrows for dependencies. Label each box with the Activity ID and Duration.

You may draw this by hand and photograph it, or use a simple table/text format if drawing is not feasible.

#### Step 2 — List All Paths

List every path through the network from Activity A to Activity J. Write each path as a sequence of Activity IDs and calculate the total duration of each path.

| Path | Activity Sequence | Total Duration |
|---|---|---|
| Path 1 | | |
| Path 2 | | |
| Path 3 | | |
| Path 4 | | |

#### Step 3 — Identify the Critical Path

State which path(s) are the critical path and explain why. What is the project duration?

**Part 1 Point Value:** 30 points

Grading breakdown:

- Network diagram (10 pts): All 10 activities shown with correct dependencies
- Path listing (10 pts): All paths correctly identified with accurate total durations
- Critical path identification (10 pts): Correct critical path stated with correct project duration and explanation

---

## Part 2: Forward and Backward Pass Calculations

### Part 2 Objective

Perform forward and backward pass calculations for all ten activities, then calculate total float for each activity.

### Part 2 Instructions

Complete the following table using the formulas from the Module 04 Reading Guide.

Use Day 1 as the Early Start for Activity A (ES of A = 1).

Forward Pass formulas:

- EF = ES + Duration - 1
- ES of successor = EF of predecessor + 1
- When multiple predecessors, ES = largest EF of predecessors + 1

Backward Pass formulas:

- LF of last activity = EF of last activity
- LS = LF - Duration + 1
- LF of predecessor = LS of successor - 1
- When multiple successors, LF = smallest LS of successors - 1

Float formula: Total Float = LS - ES

| ID | Duration | ES | EF | LS | LF | Total Float | Critical? |
|---|---|---|---|---|---|---|---|
| A | 5 | | | | | | |
| B | 8 | | | | | | |
| C | 6 | | | | | | |
| D | 4 | | | | | | |
| E | 10 | | | | | | |
| F | 5 | | | | | | |
| G | 4 | | | | | | |
| H | 3 | | | | | | |
| I | 2 | | | | | | |
| J | 1 | | | | | | |

After completing the table, answer the following questions:

Question A: Which activity has the most total float? How many days can it be delayed without affecting the project end date?

Question B: Activity C has float available. If the design team uses 3 days of float on Activity C, how does that affect the float remaining for Activity E? Explain your reasoning.

Question C: The project sponsor asks whether the project can be done in 33 days. Based on your calculations, is this possible without compressing the schedule? What is the actual project duration?

**Part 2 Point Value:** 40 points

Grading breakdown:

- Completed calculation table (25 pts): All ES, EF, LS, LF, and float values correct; critical path marked accurately
- Question A (5 pts): Correct activity identified; correct float value stated
- Question B (5 pts): Demonstrates understanding that float on a path is shared
- Question C (5 pts): Correct project duration stated with clear reasoning

---

## Part 3: Schedule Compression Decision

### Part 3 Objective

Evaluate two schedule compression options and recommend the best approach based on cost, risk, and feasibility.

### Part 3 Instructions

The Oakdale Medical Center project sponsor has announced that the go-live date has been moved up by 5 days due to a regulatory deadline. The current critical path duration must be reduced by 5 days.

The project manager has identified two options:

#### Option 1 — Crash Activity E (Application Development)

Adding a second developer to Application Development would reduce its duration from 10 days to 7 days. The additional developer costs $3,500.

#### Option 2 — Fast-Track Activities E and F

Begin Integration Testing (F) after the first 7 days of Application Development (E) are complete, overlapping the last 3 days of Development with the first 3 days of Testing. This adds no direct cost but creates a risk that integration issues discovered during testing may require reworking the last 3 days of development.

Write a 200–300 word analysis addressing the following questions:

1. Does each option achieve the required 5-day reduction? Show your reasoning with the revised path calculations.
2. What are the cost and risk trade-offs of each option?
3. Which option would you recommend and why? Reference at least two schedule management concepts from Module 04 in your recommendation.

**Part 3 Point Value:** 30 points

Grading breakdown:

- Duration analysis for each option (10 pts): Correct calculation showing whether each option achieves the 5-day reduction
- Trade-off analysis (10 pts): Accurate description of cost and risk for each option
- Recommendation (10 pts): Clear, justified recommendation using Module 04 terminology

---

## Deliverables Summary

Compile the following into one submission document:

1. Network diagram and path analysis with critical path identified (Part 1)
2. Completed forward/backward pass table with three question responses (Part 2)
3. Schedule compression analysis and recommendation (Part 3)

Submit as a single PDF or Word document to the Canvas Module 04 Lab assignment. Show all calculations clearly — partial credit is available for correct process with arithmetic errors.

---

## Grading Rubric Summary

| Section | Points | Key Criteria |
|---|---|---|
| Part 1: Network Diagram and Critical Path | 30 | Correct dependencies, all paths listed, correct critical path |
| Part 2: Forward and Backward Pass | 40 | All 10 rows calculated correctly; float questions answered |
| Part 3: Schedule Compression | 30 | Correct duration math; trade-off analysis; justified recommendation |
| **Total** | **100** | |
