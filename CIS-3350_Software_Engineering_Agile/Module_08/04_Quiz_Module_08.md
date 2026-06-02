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
