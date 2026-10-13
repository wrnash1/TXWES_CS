# Video Script: Module 08 – Estimation: Story Points and Planning Poker

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Estimated Duration:** 21 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Show Planning Poker card deck and a live estimation round as a visual demonstration

---

## Section 1 — Welcome and Why We Estimate [00:00–03:30]

"Welcome to Module 8. We have covered how to write good user stories. Today we tackle the question every team faces when they look at a list of user stories: how much work is this?

Estimation in Agile is fundamentally different from estimation in Waterfall. In Waterfall, estimates are used to create project schedules — to predict with precision when specific features will be complete. The problem is that software estimation is notoriously inaccurate when predicting absolute durations. Studies have consistently shown that developers and project managers overestimate their accuracy when predicting how long software work will take.

Agile teams use estimation differently: to understand relative complexity, to make Sprint Planning decisions, and to observe velocity over time as a capacity planning tool. We are not trying to predict the future perfectly — we are trying to make reasonable decisions today with the information we have.

By the end of this module you will be able to:

- Explain what story points measure and why they differ from hour estimates
- Facilitate a Planning Poker estimation session
- Use the Fibonacci sequence as an estimation scale
- Understand velocity and use it for Sprint capacity planning
- Avoid the most common estimation mistakes in Agile teams"

---

## Section 2 — Story Points vs. Hour Estimates [03:30–09:00]

"Story points are units of measure for expressing an estimate of the overall effort required to fully implement a Product Backlog item or any other piece of work. The key word is 'relative.' Story points measure size relative to other stories — not absolute duration.

[SHOW DIAGRAM: T-shirt size comparison — Small = 1 pt, Medium = 3 pts, Large = 8 pts, Extra Large = 13 pts — showing relative sizes visually]

Let me explain why relative estimation works better than absolute estimation for software development.

Suppose I ask you to estimate how long it will take to drive from Fort Worth to Dallas. You might say 35 minutes on a good day, or 75 minutes in rush hour traffic. Your estimate varies because external factors — traffic, weather, road construction — significantly affect duration, and you know this from experience.

Now suppose I ask: is it longer to drive from Fort Worth to Dallas or from Dallas to Houston? You immediately know Houston is much farther — maybe two and a half times as far. Your relative comparison is accurate and stable even though your absolute time estimates would vary widely.

Software works the same way. A Developer asked 'how many hours will this login feature take?' faces enormous uncertainty — it depends on the codebase, the tools, whether dependencies are in place, whether there are unexpected complications. But the same Developer asked 'is this login feature more or less complex than the password reset feature we built last Sprint?' can answer that question reliably.

Story points capture this relative complexity, effort, and uncertainty. A 5-point story is roughly twice as complex as a 3-point story. A 13-point story is notably more complex than an 8-point story.

PSM I Exam Tip: The Scrum Guide does not mandate story points. The Guide says Developers add size estimates to Product Backlog items but does not specify the unit. Story points are widely used in practice, but teams also use T-shirt sizes, ideal days, or any other relative scale. Questions about story points test your understanding of the concept, not the Scrum Guide's requirement.

Why the Fibonacci sequence? The most common story point scale uses Fibonacci numbers: 1, 2, 3, 5, 8, 13, 21. There is a practical reason for this. When the gap between consecutive estimates grows, it forces an honest conversation about uncertainty. If you are choosing between 8 and 13, that 5-point gap reflects significant uncertainty about the work. If you were using a 1–10 scale, the choice between 8 and 9 would create false precision. The Fibonacci sequence's growing gaps prevent false precision in high-complexity estimates."

---

## Section 3 — Planning Poker: The Process [09:00–15:00]

"Planning Poker is the most common technique for generating story point estimates in Agile teams. It combines the wisdom of the crowd with a structured process that prevents anchoring bias.

[SHOW DIAGRAM: Planning Poker session — Product Owner at whiteboard, 6 Developers each holding a card face-down, with a user story visible]

Here is how Planning Poker works step by step.

Step 1: The facilitator (usually the Scrum Master, though anyone can facilitate) presents a user story to the team. The Product Owner reads the story and answers clarifying questions. The Developers discuss the story until they feel they understand it well enough to estimate.

Step 2: Each Developer privately selects a card from their Planning Poker deck. The deck contains cards with Fibonacci numbers (1, 2, 3, 5, 8, 13, 21) plus a '?' card (for 'I don't understand this story enough to estimate') and an infinity card (for 'this story is too large to estimate — it needs to be split').

Step 3: On the facilitator's signal, all Developers reveal their cards simultaneously. Simultaneous reveal is critical — if one Developer reveals first, they anchor everyone else's estimate. Simultaneous revelation prevents anchoring bias.

Step 4: If all cards show the same number (or adjacent numbers), the estimate is recorded and the team moves to the next story. If there is significant divergence — say, one Developer chose 3 and another chose 13 — the team discusses the reasoning behind the outlier estimates.

PSM I Exam Tip: The most valuable part of Planning Poker is the discussion that follows divergent estimates, not the numbers themselves. A Developer who estimates 3 may be thinking of a simple implementation path that others missed. A Developer who estimates 13 may be aware of a technical dependency that others overlooked. These conversations surface knowledge that improves the team's shared understanding.

Step 5: After discussing the outliers, all Developers re-estimate with a new card. This continues until the team reaches consensus or an acceptable range.

The goal is not to achieve perfect consensus — it is to achieve a shared understanding of the work that is good enough for Sprint Planning decisions. Planning Poker should be productive and time-boxed; it is not a mechanism for endless debate."

---

## Section 4 — Velocity and Capacity Planning [15:00–19:00]

"Velocity is the sum of story points completed — meeting the Definition of Done — across a Sprint. It is a measure of how much work a specific team can accomplish in a Sprint of a given length.

[SHOW DIAGRAM: Bar chart showing Sprint velocity over 8 Sprints — values varying from 28 to 38 points with an average trendline around 33]

Velocity is used for Sprint capacity planning: if a team's average velocity over the last three Sprints is 32 story points, Sprint Planning can use 32 as a rough guide for how many story points to select.

Important velocity caveats that PSM I tests:

First, velocity is team-specific. You cannot compare the velocity of Team A to Team B. Their story point scales are calibrated to their own shared experience, not to an industry standard. A '5' at Team A may represent more or less work than a '5' at Team B.

Second, velocity is a trailing indicator. It tells you what the team accomplished last Sprint, not what they will accomplish next Sprint. Team composition changes, holidays, and complexity spikes all affect velocity.

Third, velocity should not be used as a performance metric. If a team's velocity is used to evaluate or pressure them, they will inflate estimates to hit a higher number — a phenomenon called 'velocity gaming.' The result is inflated estimates that no longer reflect reality, destroying the planning value of velocity.

Fourth, the Scrum Guide does not use the word 'velocity.' This is a commonly used Agile practice term, not a Scrum framework element. On the PSM I exam, questions about velocity fall under the category of 'useful practices' rather than Scrum rules.

PSM I Exam Tip: When a manager demands that a team increase their velocity, the Scrum-aligned response is to explain that velocity is not a target — it is a historical measurement. The way to increase team output is to address impediments, improve quality (technical debt reduction), and allow the team to build sustainable capacity over time."

---

## Section 5 — Estimation Anti-Patterns [19:00–21:00]

"Let me close with the most common estimation mistakes that undermine the value of story points and Planning Poker.

Anti-pattern 1: Anchoring. One person announces their estimate before everyone else decides. Everyone converges on that number rather than estimating independently. Simultaneous reveal in Planning Poker prevents this.

Anti-pattern 2: Pressure-based estimation. A manager or Product Owner reacts negatively to high estimates, causing Developers to lower their estimates to avoid conflict. Estimates must be owned by the Developers; external pressure corrupts their accuracy.

Anti-pattern 3: Converting story points to hours for reporting. Once you convert story points to hours in a management report, you reintroduce all the precision problems that story points were designed to avoid. Story points are for the team's internal capacity planning, not for external time-based commitments.

Anti-pattern 4: Estimating without understanding. Teams that estimate quickly without reading and discussing the story produce meaningless numbers. The conversation is the value, not the card.

Anti-pattern 5: Using velocity as a productivity metric. If velocity becomes a goal rather than a measurement, it loses its diagnostic value. Teams should be encouraged to refine their estimation accuracy, not to maximize velocity.

In Module 9 we shift from Scrum-specific practices to Kanban and Lean principles — the broader family of Agile approaches. See you there."

---

## End Card

- Next module: Module 09 – Kanban and Lean Principles
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
