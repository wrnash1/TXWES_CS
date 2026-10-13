# Discussion Forum: Module 15 — Software Project Metrics and Velocity Tracking

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Overview

This discussion asks you to apply metrics concepts to realistic professional scenarios. Write your initial post responding to one scenario, then respond substantively to at least two classmates who chose different scenarios.

---

## Professor Nash Note

Metrics are one of the most politically charged topics in software development because they sit at the intersection of measurement and trust. When a manager asks "what is your team's velocity?" the question may be sincere curiosity, disguised performance pressure, or an attempt to compare teams. The technical answer is the same in all three cases, but the implications are very different. The best responses in this discussion will engage with the human and organizational dynamics behind the metrics question — not just the math. Ask yourself: who benefits from this metric being tracked this way, and who is harmed?

---

## Scenario A: The Velocity Pressure

A software company's leadership team has started publishing a weekly dashboard showing the velocity of every Scrum Team in the engineering department. The stated purpose is "transparency and continuous improvement." Teams are listed by name with their last three Sprint velocities visible to all employees and leadership.

In the three Sprints since the dashboard went live, the product team's Scrum Master has noticed: two teams have inflated their estimates (stories that were previously estimated at 5 points are now consistently estimated at 8); one team reports stories as done before the Definition of Done is fully met; and all teams are reluctant to take on stories that are ambiguous or risky because those stories are harder to complete by Sprint end.

The Scrum Master raises the concern with the VP of Engineering: "This dashboard is measuring the wrong thing and changing the wrong behavior." The VP responds: "We need visibility into team performance. What's the alternative?"

How would you advise the Scrum Master to respond to the VP? What specific behaviors does the dashboard create, and why are they harmful? What alternative approach to organizational transparency would you recommend? Your post should be 175–225 words.

### Sample Response — Scenario A

The VP's instinct — wanting visibility into engineering performance — is reasonable. The implementation is harmful because velocity is a team-internal forecasting tool, not a cross-team performance indicator. Publishing velocities across teams creates a competition that velocities cannot support: different teams estimate on different scales, work on different complexity, and operate in different contexts. Comparing them is meaningless and predictably produces exactly the behaviors observed.

The inflation pattern is the most important harm to name. When teams inflate estimates to look productive on the dashboard, every downstream use of velocity — Sprint planning, release forecasting, capacity planning — becomes unreliable. The metric that was supposed to provide transparency now provides noise with the appearance of signal.

The alternative I would recommend to the VP: measure outcomes, not activity. Business metrics that reflect delivery — features released per quarter, lead time from feature request to production, defect escape rate — measure what actually matters. These metrics are harder to game because they are anchored in customer-visible results rather than in an internal estimation scale that teams control. Teams can also self-report their own velocity for internal use without leadership comparisons being published. Separating internal team forecasting tools from organizational performance visibility eliminates the incentive to optimize for the dashboard.

---

## Scenario B: The Burndown That Won't Budge

The EdgeSync team is in Sprint 5. On Day 7 of their 10-day Sprint, the burndown shows 26 remaining story points out of an original 40. The ideal line at Day 7 would be 12 points. The Scrum Master asks the developers what is happening. The responses are: "I finished my story but it's not tested yet." "My story is done technically but it needs a design review." "I have two stories in code review but they haven't been merged yet." "My story is 85 percent done but the API integration is blocked."

The Daily Scrum has been running efficiently — 15 minutes, everyone shares updates, impediments are raised. But the burndown is not changing.

What is the root cause of the burndown problem? Is the Daily Scrum effective given the evidence? What should the Scrum Master recommend the team change — about how they work, not just how they report? Your post should be 175–225 words.

### Sample Response — Scenario B

The root cause is that the team is confusing individual task completion with story completion. Every developer's update describes work that is "done from my perspective" — tested, code reviewed, merged, integrated — but not done in the sense that the story meets the Definition of Done. The burndown reflects the Definition of Done, not individual work completion. Stories that are waiting for code review, design approval, or API integration are not done. They are stalled.

The Daily Scrum is technically running efficiently but is not effective. Fifteen minutes, everyone talks — but the team is not surfacing and acting on the right information. The Daily Scrum's purpose is to inspect progress toward the Sprint Goal and adapt. Four developers with stories stuck in handoffs is a pattern that should have triggered a swarm response several days earlier. An effective Daily Scrum would have prompted someone to ask "what can I do to unblock your code review?" on Day 3, not Day 7.

The recommended change is about how the team works, not how they report: define explicit WIP limits on the number of stories in code review and testing simultaneously, and adopt a swarm model where team members prioritize completing in-progress stories over starting new ones. The Daily Scrum question should shift from "what did I work on yesterday?" to "what is blocking stories from reaching Done, and how do we remove that blocker today?"

---

## Scenario C: The Metric Misfit

A Scrum Team at FinanceApp has been tracking velocity and Sprint Burndown successfully for two years. A new CTO joins and announces a new engineering excellence initiative. The initiative adds the following metrics, tracked weekly and reported to leadership: number of commits per developer per day, lines of code added per week per team, test coverage percentage, number of open bugs per team, and time spent in meetings per developer.

Three months into the initiative, the team's Scrum Master observes: developers are making more frequent but smaller commits (splitting work to increase commit count); two senior developers who primarily do architecture review and pair programming score poorly despite being highly valued by peers; the team has written hundreds of new tests that cover trivial code paths to raise the coverage number; and the team spends more time preparing metric reports than they did before.

What metric anti-patterns are present in this initiative? For each metric, diagnose whether it is measuring activity or outcomes. What would you tell the CTO about the initiative's effects, and what would you recommend replacing it with? Your post should be 175–225 words.

### Sample Response — Scenario C

Five metrics are being tracked; five anti-patterns are present. Commits per developer measures activity and is trivially gameable — as the team demonstrates by splitting work. Lines of code measures activity inversely to code quality: the best engineering is often removing code, not adding it. Test coverage percentage without quality controls measures test quantity, not test effectiveness — a test suite that passes trivially is worthless. Open bugs per team creates an incentive to avoid logging bugs or to close them before they are genuinely resolved. Time in meetings is a proxy for collaboration that penalizes senior contributors whose value often comes from discussion, review, and mentoring — exactly what the architecture team exemplifies.

Every metric in this initiative measures activity. Not one measures business outcome. Shipped features, lead time, defect escape rate to production, and customer-reported issues are outcome metrics. They are harder to game because they are anchored in real-world results.

What I would tell the CTO: this initiative is measuring what is easy to count rather than what matters. The behaviors it has produced — commit splitting, trivial test writing, report preparation — are the signature of metrics that serve reporting rather than improvement. The initiative is consuming the team's capacity to deliver actual value. I would recommend replacing it with three outcome metrics and inviting the teams to select them collaboratively, so the metrics serve the teams' self-understanding rather than organizational performance theater.

---

## Peer Response Guidelines

Your reply to a classmate must be at least 75 words and should do at least one of the following:

- Challenge their diagnosis of the metric problem with a counter-argument or alternative interpretation
- Extend their argument by connecting to a Scrum event or Scrum value they did not address
- Identify a practical risk in their recommended alternative metric approach
- Ask a focused follow-up question about how their recommendation would be implemented or communicated

Avoid replies that simply agree or restate the classmate's argument.

---

## Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario understanding | 2 | Response accurately identifies the core metric misuse or anti-pattern in the scenario |
| Module concept application | 3 | At least two specific metric concepts correctly named and applied |
| Reasoning quality | 2 | Arguments connect metric choices to team behavior and organizational outcomes |
| Peer responses | 2 | Two substantive peer replies of 75+ words each that advance the discussion |
| Writing quality | 1 | Complete sentences, organized paragraphs, professional tone |
| **Total** | **10** | |
