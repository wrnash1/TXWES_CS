# Quiz: Module 09 – Kanban and Lean Principles

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Which organization and decade gave rise to the Lean manufacturing principles later adapted for software development?

- A) General Motors in the 1980s
- B) Toyota in the 1950s and 1960s
- C) Microsoft in the 1990s
- D) Ford Motor Company in the 1940s

Correct Answer: B — The Toyota Production System, developed by Taiichi Ohno and Shigeo Shingo at Toyota in the 1950s and 1960s, is the origin of Lean thinking. Mary and Tom Poppendieck translated these principles into software development terms in their 2003 book.

Distractor Analysis:

- Why A is incorrect: General Motors was not the origin of Lean; Toyota developed the Production System as a competitive response to resource constraints in post-war Japan.
- Why C is incorrect: Microsoft is where David Anderson adapted Kanban for software in the early 2000s, but that is a Kanban application, not the origin of Lean principles.
- Why D is incorrect: Ford's assembly line was a push-based mass production system — almost the opposite of Lean's pull-based, waste-eliminating philosophy.

---

## Question 2

Lean Principle 4 — Establish Pull — states that work should enter the system only when there is capacity to handle it. Which Scrum practice most directly embodies this principle?

- A) The Product Owner orders the Product Backlog by business value
- B) Developers pull work from the Product Backlog during Sprint Planning rather than having work assigned to them
- C) The Scrum Master removes impediments from the team's path
- D) The Definition of Done sets quality standards for Increment completion

Correct Answer: B — Sprint Planning is a pull mechanism: Developers select how much work they can handle from the Product Backlog based on their own capacity assessment, rather than having a manager push work onto them. The Scrum Guide reinforces that only Developers can determine how much they can take on.

Distractor Analysis:

- Why A is incorrect: Product Backlog ordering relates to Lean Principle 1 (Identify Value) — prioritizing customer value — not to the pull mechanism of work intake.
- Why C is incorrect: Impediment removal supports flow (Principle 3) but is not a pull mechanism for work intake.
- Why D is incorrect: The Definition of Done relates to quality and reducing partially done work waste, but it is not a pull mechanism.

---

## Question 3

According to Little's Law, what is the relationship between WIP, throughput, and cycle time?

- A) Cycle Time = Throughput × WIP
- B) Throughput = WIP × Cycle Time
- C) Cycle Time = WIP / Throughput
- D) WIP = Throughput / Cycle Time

Correct Answer: C — Little's Law states: Average Cycle Time = WIP / Throughput. This means that if throughput is held constant and WIP is reduced, cycle time decreases proportionally. This is the mathematical justification for WIP limits in Kanban.

Distractor Analysis:

- Why A is incorrect: This rearrangement inverts the relationship incorrectly — multiplying throughput by WIP does not yield cycle time.
- Why B is incorrect: This form calculates throughput, not cycle time, and is not the standard expression of the law.
- Why D is incorrect: This form calculates WIP from the other two variables but is not the primary expression used to justify WIP limit benefits.

---

## Question 4

Which of the following is the defining practice that distinguishes Kanban from other workflow management approaches?

- A) Visualizing work on a board
- B) Holding daily team meetings to coordinate work
- C) Limiting the number of work items allowed in each workflow stage simultaneously
- D) Assigning a dedicated team lead to each workflow column

Correct Answer: C — WIP limits are the defining practice of Kanban. While many methods use task boards, Kanban's unique contribution is the explicit numerical limit on how many items can be in any stage at once, which forces teams to finish work before starting new work.

Distractor Analysis:

- Why A is incorrect: Visualization is a Kanban core practice, but many methods use task boards. WIP limits are what make Kanban specifically Kanban.
- Why B is incorrect: Daily meetings are associated with Scrum's Daily Scrum, not Kanban. Kanban prescribes no required meetings or cadences.
- Why D is incorrect: Kanban prescribes no roles. Assigning team leads to columns is not a Kanban practice.

---

## Question 5

A software team notices that code written two months ago has never been integrated, tested, or deployed because the team keeps starting new features before finishing existing ones. Which Lean waste category best describes this situation?

- A) Defects
- B) Relearning
- C) Partially done work
- D) Extra features

Correct Answer: C — Partially done work is the Lean waste category for code that has been written but not moved through to a deliverable state. It represents sunk effort with no value yet delivered to the customer.

Distractor Analysis:

- Why A is incorrect: Defects refer to bugs and specification errors that require rework, not to unintegrated work. The scenario describes work that may be correct but is simply stalled.
- Why B is incorrect: Relearning refers to solving the same problem multiple times due to poor knowledge transfer — distinct from accumulation of unfinished work.
- Why D is incorrect: Extra features describes building functionality users did not request. The waste here is in the unfinished state of the work, not the features' existence.

---

## Question 6

A team is using Kanban and their Development column has a WIP limit of 4. Currently 4 items are in Development. A new high-priority item arrives. What should the team do?

- A) Increase the WIP limit temporarily to 5 to accommodate the high-priority item
- B) Immediately move an existing Development item to Done to create capacity
- C) Stop starting new work and focus on moving one of the current Development items forward before pulling in the new item
- D) Add the new item to Development anyway because WIP limits are guidelines, not rules

Correct Answer: C — When a WIP limit is reached, the correct Kanban response is to stop starting and start finishing. The team should work to complete or advance an existing item before pulling in the new one. This is the core behavioral discipline WIP limits are designed to enforce.

Distractor Analysis:

- Why A is incorrect: Routinely raising WIP limits to accommodate urgent items defeats the purpose of the limit. If the limit is constantly overridden, it provides no flow benefit.
- Why B is incorrect: Items cannot be arbitrarily moved to Done unless the work is actually complete. Moving an unfinished item to Done to create WIP capacity violates honest workflow management.
- Why D is incorrect: WIP limits are explicit policies, not flexible suggestions. Treating them as optional removes the discipline that makes Kanban's flow improvements possible.

---

## Question 7

Which of the following is a fundamental difference between Scrum and Kanban regarding how new work is accepted?

- A) Scrum requires story points for all new work; Kanban prohibits story points
- B) In Scrum, new items can be added to the current Sprint at any time; in Kanban, new items must wait for the next cycle
- C) In Scrum, new items are protected from entering the current Sprint scope; in Kanban, new items can be pulled in at any time within WIP limits
- D) Scrum and Kanban both accept new work on the same weekly schedule

Correct Answer: C — Scrum's Sprint scope is protected; changes that would endanger the Sprint Goal are not added mid-Sprint and new items go to the Product Backlog for a future Sprint. Kanban has no protected Sprint; new items can be pulled into the workflow whenever WIP limits permit.

Distractor Analysis:

- Why A is incorrect: The Scrum Guide does not mandate story points, and Kanban does not prohibit them. Both frameworks are estimation-agnostic.
- Why B is incorrect: This reverses the correct behavior. It is Kanban — not Scrum — that allows new items to enter at any time within limits.
- Why D is incorrect: Neither framework prescribes weekly work acceptance. Scrum accepts new items at Sprint boundaries; Kanban accepts them on demand within WIP limits.

---

## Question 8

What does a cumulative flow diagram (CFD) reveal when a band for a specific column becomes noticeably wider over time?

- A) The team is increasing throughput in that column
- B) Work items are accumulating in that column faster than they are leaving it, indicating a bottleneck
- C) The team has reduced WIP in that column successfully
- D) Cycle time for items passing through that column is decreasing

Correct Answer: B — A widening band in a CFD indicates that items are entering a column faster than they are exiting it. This is the visual signature of a bottleneck — work piling up because of a constraint downstream or a capacity problem in that stage.

Distractor Analysis:

- Why A is incorrect: A widening band means items are accumulating, not moving through faster. Higher throughput would keep the band narrow.
- Why C is incorrect: A widening band shows WIP increasing in that column, which is the opposite of successful WIP reduction.
- Why D is incorrect: A widening band indicates items spending more time in the column, meaning cycle time is increasing, not decreasing.

---

## Question 9

Which team type does Kanban fit best, according to the Scrum vs. Kanban comparison?

- A) A product team building new features against a quarterly roadmap with bi-weekly stakeholder demos
- B) An operations or support team handling continuous, unpredictable incoming work with service level agreements
- C) A team that needs fixed Sprint Goals and committed iteration deliverables
- D) A cross-functional team coordinating frontend, backend, and data engineering work on new features

Correct Answer: B — Kanban is optimized for teams with continuous, unpredictable incoming work — operations, support, or maintenance teams. These teams cannot batch work into two-week Sprints because items arrive unpredictably and often have short resolution windows.

Distractor Analysis:

- Why A is incorrect: Bi-weekly stakeholder demos and quarterly roadmaps describe a product development cadence that maps to Scrum's Sprint Review and Sprint cycle, not Kanban's continuous flow.
- Why C is incorrect: Fixed Sprint Goals and committed iteration deliverables are Scrum concepts. Kanban has no iteration commitment mechanism.
- Why D is incorrect: Coordination between frontend, backend, and data engineering on new features describes a feature development context well suited to Scrum's cross-functional team model.

---

## Question 10

Scrumban is best described as which of the following?

- A) An official Scrum.org framework that replaces both Scrum and Kanban
- B) A hybrid approach where teams combine Scrum's structural elements with Kanban's flow-based practices
- C) A Kanban variant that adds mandatory Sprint Retrospectives and a Product Owner role
- D) A derogatory term for teams that fail to implement either Scrum or Kanban correctly

Correct Answer: B — Scrumban is an informal hybrid in which teams retain Scrum's structure (Sprints, events, roles) while incorporating Kanban's flow practices (WIP limits, cycle time tracking, cumulative flow diagrams). It is not an official Scrum.org framework, but the Scrum Guide permits teams to use Kanban tools within a Scrum context.

Distractor Analysis:

- Why A is incorrect: Scrumban is not an official Scrum.org framework and does not replace either Scrum or Kanban. It is a practitioner-evolved hybrid.
- Why C is incorrect: Scrumban adds Kanban practices to an existing Scrum foundation, not the other way around. It does not impose Scrum roles on Kanban teams.
- Why D is incorrect: Scrumban is a recognized, legitimate hybrid configuration used by many mature teams. It is not a failure mode or a pejorative term.

---
