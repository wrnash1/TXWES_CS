# Quiz: Module 08 – Estimation: Story Points and Planning Poker

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

Why do Agile teams use story points instead of hours to estimate the size of Product Backlog items?

* A) Story points are required by the Scrum Guide and must be used in all Scrum projects.
* B) Story points allow the team to express relative complexity, effort, and uncertainty without committing to specific time durations.
* C) Story points make it easier for management to track individual Developer productivity.
* D) Story points can be converted directly to salary calculations for team members.

Correct Answer: B) Story points capture the relative size of work in terms of complexity, effort, and risk — freeing the team from the false precision of hour-based estimates.

Distractor Analysis:

* *Why B is correct:* Relative estimation with story points acknowledges that software complexity is uncertain and varies by developer. A point estimate expresses "how big is this compared to that story?" without locking in a time promise.
* *Why A is incorrect:* The Scrum Guide does not mention story points. They are a widely adopted complementary practice, not a Scrum requirement.
* *Why C is incorrect:* Using story points to track individual productivity is an anti-pattern. Story points are a team-level planning tool, not an individual performance measure.
* *Why D is incorrect:* Story points have no monetary conversion. Tying estimates to compensation would create perverse incentives to inflate estimates.

---

### Question 2

Which of the following is the most accurate definition of Planning Poker?

* A) A card game played by the Product Owner to assign priorities to backlog items before Sprint Planning.
* B) A consensus-based estimation technique where Developers independently select point values, reveal them simultaneously, and discuss until they reach agreement.
* C) A technique where the most experienced Developer announces an estimate and the team adopts it without discussion.
* D) An optional sprint retrospective activity used to vote on which process improvements to implement.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* Planning Poker's core mechanism is simultaneous reveal — everyone shows their card at the same time to prevent anchoring bias. Discussion follows when estimates diverge significantly, leading to consensus.
* *Why A is incorrect:* Planning Poker is used by the Developers to estimate effort — it is not a Product Owner prioritization tool.
* *Why C is incorrect:* Having one person announce an estimate before others reveals theirs is exactly the anchoring bias that Planning Poker is designed to prevent.
* *Why D is incorrect:* Planning Poker is an estimation technique used in backlog refinement and Sprint Planning — not a retrospective voting tool.

---

### Question 3

After three Sprints, a team completed 18, 22, and 20 story points respectively. What is their average velocity, and approximately how many story points should they commit to in Sprint 4?

* A) Average velocity is 22; they should commit to 30 points in Sprint 4.
* B) Average velocity is 20; they should commit to approximately 20 points in Sprint 4.
* C) Average velocity is 18; they should commit to 10 points in Sprint 4 to be safe.
* D) Velocity cannot be calculated with only three Sprints; they should ask the Product Owner to set the commitment.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* Average velocity = (18 + 22 + 20) / 3 = 20. The team should use their historical velocity as the forecast for the next Sprint — committing to approximately 20 points.
* *Why A is incorrect:* 22 is the highest single Sprint result, not the average. Committing to 30 points exceeds their demonstrated capacity and sets an unrealistic expectation.
* *Why C is incorrect:* 18 is the lowest Sprint result. Using the lowest value alone is overly conservative and wastes the team's capacity. Average velocity is the standard planning input.
* *Why D is incorrect:* Three Sprints is a sufficient baseline to establish a velocity trend. The Product Owner does not set the team's capacity commitment — the Developers do.

---

### Question 4

A manager asks the Scrum Master to use velocity data to rank three development teams and identify the highest-performing team. What should the Scrum Master do?

* A) Compile the velocity rankings and share them with management as requested.
* B) Ask the Product Owner to perform the ranking instead, since velocity relates to product delivery.
* C) Explain that velocity is a team-specific planning tool and is not valid for cross-team comparisons or performance ranking.
* D) Add velocity tracking to the Sprint Retrospective agenda so teams can compete to improve their scores.

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* Velocity is calibrated per team, per context, and per point scale — different teams use points differently. Comparing velocities across teams is meaningless and creates pressure to inflate estimates rather than estimate accurately.
* *Why A is incorrect:* Compiling cross-team velocity rankings misuses the metric and undermines the safety needed for accurate estimation. The Scrum Master should coach against this, not comply.
* *Why B is incorrect:* Redirecting the request to the Product Owner does not solve the problem. The Scrum Master is accountable for coaching the organization on correct Scrum and Agile metrics usage.
* *Why D is incorrect:* Turning velocity into a competition incentivizes teams to overestimate story points rather than estimate honestly — a classic Agile anti-pattern called "velocity gaming."

---

### Question 5

During Planning Poker, the team's estimates for a story are: 3, 3, 3, 13, 3. What is the recommended next step?

* A) Average all estimates (total 25 ÷ 5 = 5) and use 5 as the final estimate without discussion.
* B) Accept the majority estimate of 3 points immediately, since four of five Developers agree.
* C) Ask the Developer who estimated 13 to explain their reasoning, then re-estimate after discussion.
* D) Discard the 13 as an outlier and proceed with 3 points without any discussion.

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* Outlier estimates in Planning Poker are the most valuable signals — they reveal hidden complexity, risk, or misunderstanding. Surfacing and discussing them is the entire point of the technique before re-estimating.
* *Why A is incorrect:* Averaging estimates skips the discussion that uncovers why estimates diverged. Averaging also produces a number (5) that no Developer actually believes represents the story's size.
* *Why B is incorrect:* Taking the majority vote without discussion is majority rules, not consensus. Planning Poker's goal is for the team to reach shared understanding through discussion of divergent perspectives.
* *Why D is incorrect:* Discarding outliers silences the Developer with the most concern about complexity or risk — exactly the information the team needs to estimate accurately.
