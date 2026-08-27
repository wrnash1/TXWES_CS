# Quiz: Module 08 – Estimation: Story Points and Planning Poker

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Story points are a unit of measure for estimating what?

- A) The exact number of hours required to complete a user story
- B) The relative effort, complexity, and uncertainty of a user story
- C) The business value of a user story ranked by the Product Owner
- D) The number of tasks needed to implement a user story

Correct Answer: B — Story points measure the relative effort, complexity, and uncertainty of a user story, not absolute duration. They are relative to other stories on the same team's scale.

Distractor Analysis:

- Why A is incorrect: Story points deliberately avoid committing to exact hours because software duration estimates are notoriously inaccurate for complex work.
- Why C is incorrect: Business value is the Product Owner's domain; story point estimates belong to the Developers and measure effort, not value.
- Why D is incorrect: The number of tasks is a task-level decomposition activity (Sprint Planning), not what story points measure.

---

## Question 2

Why does Planning Poker use the Fibonacci sequence (1, 2, 3, 5, 8, 13, 21) rather than a simple 1–10 scale?

- A) Fibonacci numbers are internationally standardized for Agile estimation
- B) The increasing gaps prevent false precision, forcing teams to acknowledge uncertainty in larger estimates
- C) Fibonacci numbers are easier to remember than sequential numbers
- D) The Scrum Guide mandates the Fibonacci scale for all story point estimates

Correct Answer: B — The growing gaps between Fibonacci numbers prevent teams from choosing between, for example, 8 and 9 when they cannot realistically distinguish that level of precision. The larger gaps at higher values reflect the greater uncertainty inherent in larger work items.

Distractor Analysis:

- Why A is incorrect: There is no international standardization for Fibonacci in Agile; it is a widely adopted practice, not a standard.
- Why C is incorrect: Memorability is not the reason for the Fibonacci scale in estimation contexts.
- Why D is incorrect: The Scrum Guide does not mandate story points or any specific estimation scale.

---

## Question 3

In Planning Poker, why do all participants reveal their cards simultaneously rather than one at a time?

- A) Simultaneous reveal is a Scrum Guide requirement for all estimation activities
- B) Simultaneous reveal ensures the highest estimate always wins
- C) Simultaneous reveal prevents anchoring bias — the tendency for later estimators to be influenced by the first number revealed
- D) Simultaneous reveal speeds up the session by eliminating discussion

Correct Answer: C — Anchoring bias is a well-documented cognitive phenomenon where people's estimates cluster around the first number they hear. Simultaneous reveal ensures each team member's independent assessment is preserved before any discussion occurs.

Distractor Analysis:

- Why A is incorrect: The Scrum Guide does not describe Planning Poker; it is a practice, not a Scrum rule.
- Why B is incorrect: The goal is honest consensus, not a specific outcome favoring high or low estimates.
- Why D is incorrect: Simultaneous reveal actually enables more valuable discussion by surfacing divergent estimates that need exploration.

---

## Question 4

Who is responsible for estimating the size of Product Backlog items in Scrum?

- A) The Product Owner, based on business complexity
- B) The Scrum Master, based on historical velocity data
- C) The Developers, based on their technical understanding of the work
- D) The project manager, based on the project schedule requirements

Correct Answer: C — The Scrum Guide is explicit: the Developers who will do the work add size estimates to Product Backlog items. No one else can override or replace their estimates.

Distractor Analysis:

- Why A is incorrect: The Product Owner manages value and ordering; they do not estimate technical effort.
- Why B is incorrect: The Scrum Master coaches and facilitates; they do not estimate work on behalf of the Developers.
- Why D is incorrect: Project manager is not a Scrum accountability; and even in non-Scrum contexts, having someone other than the implementers estimate produces less accurate results.

---

## Question 5

A team's velocity over the last four Sprints has been 28, 32, 30, and 34 story points. What is the most appropriate use of this data for Sprint 5 planning?

- A) The team must commit to exactly 31 story points (the average) in Sprint 5
- B) The team uses the velocity range (28–34) as a guideline for how many story points to select, not as a hard commitment
- C) The team should ignore velocity and commit to as many story points as the Product Owner requests
- D) The team must increase their velocity each Sprint, so Sprint 5 must target at least 35 points

Correct Answer: B — Velocity is a trailing indicator used as a planning guideline, not a hard commitment or a target. The range of 28–34 suggests the team can reasonably plan for approximately 30–32 story points while acknowledging variability.

Distractor Analysis:

- Why A is incorrect: Committing to exactly the average ignores natural Sprint-to-Sprint variability and treats velocity as a precise prediction rather than a guide.
- Why C is incorrect: The Developers determine their own capacity; Product Owner requests do not override the team's capacity assessment.
- Why D is incorrect: Requiring velocity to increase each Sprint treats it as a performance target, which leads to estimate inflation and destroys its planning value.

---

## Question 6

Velocity is team-specific. What does this mean in practice?

- A) Each Developer on the team has their own individual velocity score
- B) Velocity is measured in team-hours per Sprint, specific to the team's work schedule
- C) A team's story point scale is calibrated to their own experience; comparing velocity across different teams is meaningless
- D) Velocity is only valid for teams that have been working together for more than six months

Correct Answer: C — Story point scales are calibrated through a team's shared estimation experience. One team's "5 points" may represent more or less work than another team's "5 points," making cross-team velocity comparisons invalid.

Distractor Analysis:

- Why A is incorrect: Velocity is a team-level measure, not an individual one. Individual Developer performance is not measured by story points.
- Why B is incorrect: Velocity is measured in story points per Sprint, not team-hours.
- Why D is incorrect: The Scrum Guide places no minimum tenure requirement on velocity measurement; it becomes useful after a few Sprints of calibration.

---

## Question 7

During Planning Poker, one Developer plays the infinity card for a user story. What does this signal?

- A) The Developer disagrees with the story's business value and refuses to estimate it
- B) The story is too large or too unclear to estimate; it needs to be split or refined before it can be selected for a Sprint
- C) The Developer believes the story will take infinitely long to complete and should be removed from the backlog
- D) The infinity card indicates the highest possible estimate, equivalent to 100 story points

Correct Answer: B — The infinity card signals that the story cannot be meaningfully estimated in its current form — it is either too large (an epic) or too unclear. It is a prompt for decomposition or refinement, not a rejection of the story.

Distractor Analysis:

- Why A is incorrect: The infinity card is not a value judgment; it is a sizing signal related to decomposition needs, not business value disagreement.
- Why C is incorrect: Playing the infinity card does not mean the story should be removed; it means it needs to be broken down before it is sprint-ready.
- Why D is incorrect: The infinity card is a qualitative signal about story size, not a numeric estimate equivalent to 100 points.

---

## Question 8

A manager observes that Team A has a velocity of 45 story points per Sprint and Team B has a velocity of 28 story points per Sprint. The manager concludes that Team A is 60% more productive. What is wrong with this conclusion?

- A) Nothing — velocity is a direct productivity measure and the comparison is valid
- B) The comparison is invalid because story point scales are team-specific and cannot be compared across teams
- C) The comparison is valid only if both teams have the same number of Developers
- D) The comparison is invalid because Sprint 5 must include a velocity reset

Correct Answer: B — Story point scales are calibrated independently by each team based on their own shared experience. Team A's "45 story points" may represent less actual work than Team B's "28 story points" if Team A estimates generously and Team B estimates conservatively.

Distractor Analysis:

- Why A is incorrect: Velocity is explicitly not a productivity metric — it is a team-specific capacity planning tool.
- Why C is incorrect: Team size affects absolute output but does not make cross-team velocity comparisons valid; the fundamental problem is the non-standard scale.
- Why D is incorrect: "Velocity reset" is not a Scrum concept; there is no prescribed mechanism for resetting velocity.

---

## Question 9

What is the most important outcome of a Planning Poker session, according to Agile estimation principles?

- A) Achieving unanimous agreement on a single story point number for every story
- B) Generating a complete story point estimate for every item in the Product Backlog
- C) Surfacing different perspectives and reaching a shared understanding of the work that informs planning decisions
- D) Producing hour-level estimates that can be converted to a project schedule

Correct Answer: C — The most valuable outcome of Planning Poker is the discussion that surfaces divergent knowledge, hidden assumptions, and technical risks. The numbers themselves are secondary to the team understanding the work.

Distractor Analysis:

- Why A is incorrect: Unanimous agreement on the first round often means the team is anchoring or rushing rather than genuinely exploring the work.
- Why B is incorrect: Estimating every item in the entire backlog at once is wasteful; only items close to being Sprint-ready need detailed estimates.
- Why D is incorrect: Converting story points to hours re-introduces false precision and violates the purpose of relative estimation.

---

## Question 10

Does the Scrum Guide require teams to use story points for Product Backlog estimation?

- A) Yes — the Scrum Guide mandates story points as the standard unit for PBI estimation
- B) Yes — but only for teams using two-week or longer Sprints
- C) No — the Scrum Guide says Developers add size estimates but does not prescribe the format or unit
- D) No — the Scrum Guide prohibits numerical estimates and requires descriptive sizing only

Correct Answer: C — The 2020 Scrum Guide states that Developers add size estimates to Product Backlog items but does not mandate story points, Fibonacci scales, Planning Poker, or any specific estimation technique. These are widely adopted practices, not Scrum rules.

Distractor Analysis:

- Why A is incorrect: This is a common misconception. The Scrum Guide is deliberately minimal on estimation technique.
- Why B is incorrect: The Scrum Guide makes no Sprint-length-based distinction about estimation format.
- Why D is incorrect: The Scrum Guide does not prohibit numerical estimates; it simply does not prescribe any format.

---

### Question 11 (5 points)

A Developer plays the "?" card during Planning Poker. What does this signal?

- A) The Developer disagrees with the story's priority and refuses to estimate it
- B) The Developer does not have enough information or clarity about the story to provide a meaningful estimate
- C) The Developer estimates the story at zero effort
- D) The Developer believes the story should be removed from the Product Backlog

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — The "?" card is about information gaps, not value disagreement; priority is the Product Owner's domain, not the reason for a "?" card.
  - C) Incorrect — Zero effort is represented by the "0" card; "?" means insufficient information to estimate, not negligible effort.
  - D) Incorrect — The "?" card does not signal that a story should be removed; it prompts a refinement conversation before the story can be estimated.

---

### Question 12 (5 points)

A team's Sprint 1 velocity is unusually low because it was their first Sprint and they were calibrating their estimates. What is the best practice for using this Sprint 1 velocity in future planning?

- A) Use Sprint 1 velocity as the baseline and require all future Sprints to exceed it
- B) Discard Sprint 1 data entirely and start tracking velocity from Sprint 2
- C) Include Sprint 1 data but note its anomalous nature; after 3–4 Sprints, the average will smooth out early calibration variance
- D) Replace Sprint 1 velocity with a standardized industry average for teams of the same size

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — Requiring future Sprints to exceed Sprint 1 treats velocity as a target rather than a measurement, which is an anti-pattern.
  - B) Incorrect — Completely discarding data is wasteful; the team can note the context and include it in a broader average after more data points are available.
  - D) Incorrect — Industry averages are meaningless for team-specific story point scales; velocity is only valid within the team's own calibrated scale.

---

### Question 13 (5 points)

What is "estimate inflation" in the context of Agile velocity, and why is it harmful?

- A) Estimating stories at higher points to make the team appear more productive — this inflates velocity numbers, making them unreliable for capacity planning
- B) Adding inflation factors to estimates to account for meeting time and interruptions
- C) Increasing estimates for non-functional requirements that are harder to measure
- D) Using T-shirt sizes instead of Fibonacci numbers to get larger estimate values

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Incorrect — Accounting for meeting time and interruptions in capacity calculations is legitimate practice, not estimate inflation.
  - C) Incorrect — Adjusting estimates for hard-to-measure non-functional work is reasonable sizing; it is not inflation.
  - D) Incorrect — Using T-shirt sizes is an alternative estimation scale, not an inflation technique.

---

### Question 14 (5 points)

A team has been using story points for 12 Sprints. A new Developer joins the team. How should the new Developer's estimates be handled in the next Planning Poker session?

- A) The new Developer should not participate in estimation until they have completed at least three Sprints
- B) The new Developer participates fully; their independent perspective may surface assumptions the rest of the team has normalized
- C) The new Developer's estimates should be averaged with the team's to reduce noise
- D) The Scrum Master should assign the new Developer's estimates based on past velocity data

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Excluding new team members from estimation is not prescribed by any Agile practice and wastes a valuable perspective.
  - C) Incorrect — All estimates are revealed and discussed; averaging without discussion skips the most valuable part of Planning Poker.
  - D) Incorrect — The Scrum Master does not estimate on behalf of Developers; the new Developer estimates from their own understanding.

---

### Question 15 (5 points)

Which of the following scenarios best illustrates the correct use of velocity in Sprint Planning?

- A) "Our velocity target is 50 points, so we must select stories totaling exactly 50 points."
- B) "Our last three Sprints averaged 32 points, so we'll plan to take on approximately 30–34 points this Sprint."
- C) "Our velocity was 45 last Sprint, so we must beat 45 this Sprint to show improvement."
- D) "We'll take as many stories as the Product Owner requests and use velocity to prove we delivered them."

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Velocity is a guide, not a target; requiring exactly 50 points creates artificial pressure.
  - C) Incorrect — Velocity should not be used as a performance bar to beat each Sprint; this leads to estimate gaming.
  - D) Incorrect — The Developers determine how much to take on; velocity measures what was accomplished, not what was requested.

---

### Question 16 (5 points)

Two Developers estimate a story at 3 points and 13 points respectively. What is the most valuable next step in the Planning Poker session?

- A) Average the two estimates (8 points) and move on to save time
- B) The facilitator chooses the lower estimate to maintain project schedule confidence
- C) Ask both the 3-point and 13-point estimators to explain their reasoning, as the divergence likely reveals different assumptions about scope or technical risk
- D) Discard both estimates and re-start the round from scratch

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — Averaging without discussion discards the most valuable outcome of divergent estimates: the surfacing of hidden assumptions.
  - B) Incorrect — The facilitator does not choose estimates; consensus is reached through team discussion, not facilitated selection.
  - D) Incorrect — Re-starting from scratch is unnecessary; the divergence is information, not an error to discard.

---

### Question 17 (5 points)

A Scrum Team switches from story points to T-shirt sizes (S, M, L, XL) midway through their product development. What happens to their historical velocity data?

- A) Historical velocity data can be directly compared to the new scale if the team maps each T-shirt size to a number
- B) Historical velocity data becomes incomparable to future data because the two scales are calibrated differently; the team effectively resets its velocity baseline
- C) The Scrum Master is responsible for converting all historical data to the new scale
- D) Nothing changes because velocity is not a Scrum framework element anyway

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Mapping S→3, M→5 etc. is arbitrary; the calibration of the original scale was built through team experience, not a conversion formula.
  - C) Incorrect — The Scrum Master does not own velocity data or scale conversions; and such a conversion would produce invalid comparisons.
  - D) Incorrect — While velocity is not in the Scrum Guide, it is still a tool the team relies on for planning; changing scales does affect its usefulness even if it has no formal Scrum status.

---

### Question 18 (5 points)

Which of the following best describes the T-shirt sizing estimation scale's most appropriate use case?

- A) For detailed Sprint Planning where accurate point totals are needed to match team capacity
- B) For early roadmap and product vision conversations where rough relative sizing is sufficient and a number feels too precise
- C) For tracking velocity across multiple Scrum Teams in a scaled Agile program
- D) For estimating tasks within a Sprint Backlog when Developers need sub-story granularity

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Sprint Planning requires precise enough estimates to match team capacity; T-shirt sizes lack the granularity needed for this.
  - C) Incorrect — Cross-team velocity tracking is problematic regardless of scale; T-shirt sizes do not solve the cross-team comparison problem.
  - D) Incorrect — Sprint Backlog tasks are typically estimated in hours, not T-shirt sizes; T-shirt sizes are too coarse for task-level granularity.

---

### Question 19 (5 points)

What distinguishes "complexity" from "effort" as factors in a story point estimate?

- A) Complexity refers to the number of lines of code; effort refers to the number of hours required
- B) Complexity is how technically difficult the work is (e.g., a novel algorithm); effort is how much work is involved regardless of difficulty (e.g., a straightforward but time-consuming data migration)
- C) Complexity is estimated by the Product Owner; effort is estimated by the Developers
- D) Complexity and effort are identical concepts; story points measure only one of them at a time

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Lines of code and hours are absolute measures that story points deliberately avoid; the distinction is conceptual, not metric.
  - C) Incorrect — Both complexity and effort are assessed by the Developers; the Product Owner does not contribute to technical effort estimates.
  - D) Incorrect — Story points capture complexity, effort, and uncertainty as a combined assessment; they are distinct but related dimensions of work size.

---

### Question 20 (5 points)

A Product Owner asks to participate in Planning Poker by playing their own cards alongside the Developers. How should the Scrum Master respond?

- A) Allow it — the Product Owner has business knowledge that improves estimates
- B) Refuse — the Product Owner is forbidden from attending estimation sessions by the Scrum Guide
- C) Allow the Product Owner to attend and answer questions, but note that their estimation cards should not be used to determine the final estimate, as estimates belong to the Developers
- D) Allow it only if the Product Owner agrees to match the Developers' average estimate

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — While Product Owner attendance is valuable for answering questions, allowing their cards to influence the final estimate conflates product knowledge with technical effort assessment.
  - B) Incorrect — The Scrum Guide does not prohibit Product Owner attendance at estimation; it assigns estimate ownership to Developers but does not exclude others from the room.
  - D) Incorrect — Matching the average defeats the purpose; the Product Owner's role in estimation is to provide context, not to match Developer estimates.
