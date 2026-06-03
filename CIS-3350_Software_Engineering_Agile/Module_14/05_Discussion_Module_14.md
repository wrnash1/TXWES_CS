# Discussion Forum: Module 14 — Scaled Agile: SAFe and LeSS Overview

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Overview

This discussion asks you to apply scaling framework concepts to realistic organizational scenarios. Write your initial post responding to one scenario, then respond substantively to at least two classmates who chose different scenarios.

---

## Professor Nash Note

Scaling is where Agile idealism meets organizational reality. Every organization that adopts SAFe or LeSS is trying to solve real coordination problems, and both frameworks represent genuine thinking about how to do that. The best responses in this discussion will resist the temptation to declare one framework universally superior. Instead, engage with the specific organizational context: what is the root cause of the coordination problem? What does the proposed framework actually address — and what does it leave unresolved? Think about the human side: which organizational structures benefit from scaling frameworks, and which problems cannot be solved by adding more meetings and roles?

---

## Scenario A: The Component Team Crisis

GlobalBank has twelve development teams building their core banking platform. Each team owns a component: authentication, transaction processing, account management, reporting, notifications, and so on. Teams frequently block each other — the Notification team cannot complete a story without a new API endpoint from the Transaction team, which itself needs schema changes from the Account Management team.

The organization's CTO has proposed adopting SAFe. She argues that PI Planning will force the teams to surface these dependencies early and coordinate before Sprint work begins. A senior architect objects: "PI Planning doesn't fix the architecture. We have twelve component teams because the system was designed with tight component coupling. Adding planning ceremonies will not eliminate the handoffs — it will just schedule them more formally."

Who has the stronger argument? What does PI Planning actually address in this scenario, and what does it leave unresolved? If you were the Agile consultant, what would you recommend the organization do before or alongside the SAFe adoption? Your post should be 175–225 words.

### Sample Response — Scenario A

The architect has the stronger technical argument, and the CTO has the stronger organizational argument — and both are right simultaneously. PI Planning will improve coordination visibility. It will surface the dependency between the Notification team and the Transaction team before Sprint work begins rather than in the middle of a Sprint. That is a genuine improvement. But it does not eliminate the dependency itself. After PI Planning, the Notification team still has to wait for the Transaction team's API endpoint. The handoff is now scheduled — but it still exists.

The architect is correct that the root cause is architectural coupling. Twelve component teams exist because the system was built as twelve tightly coupled components. SAFe's coordination machinery manages that coupling; it does not remove it. Two years of PI Planning will still involve twelve teams negotiating API contracts at each PI if the architecture remains componentized.

My recommendation before the SAFe adoption: assess whether any component teams can be converted to feature teams — cross-functional teams that own a customer-facing capability end-to-end rather than a technical layer. Even converting three or four of the twelve to feature teams would reduce the most frequent dependency chains. Then adopt SAFe for the remaining coordination challenges. SAFe is most effective when team structure and architecture have already minimized coupling. Used alone as an overlay on a componentized system, it schedules the problem without solving it.

---

## Scenario B: The LeSS Adoption Resistance

A 200-person software company is considering LeSS for their flagship enterprise product. Currently, eight teams build the product with eight independent Product Owners and eight separate backlogs. The leadership team has identified that customer-facing features frequently require coordinating across four or five teams because no single team owns a complete user workflow.

A proposed LeSS adoption would consolidate to one Product Owner and one shared backlog. Two Product Owners whose roles would be eliminated in the consolidation have objected vigorously. Their argument: "We understand our domain deeply. A single Product Owner cannot maintain the depth of knowledge we have about our respective areas. We will end up with a less-informed prioritization process."

Is their concern valid? What does LeSS's model of one Product Owner actually require of that person, and how does LeSS address the concern about deep domain knowledge? What would you tell the departing Product Owners about how their expertise fits in the new model? Your post should be 175–225 words.

### Sample Response — Scenario B

The departing Product Owners' concern is technically valid and practically manageable. One person genuinely cannot maintain the depth of domain knowledge that eight specialists currently hold. The concern is real — the question is whether LeSS's design addresses it adequately.

LeSS's answer is that the Product Owner is a prioritization authority and domain ambassador, not an expert in every technical and product detail. The Product Owner owns the ordering of the backlog and ensures the team understands the business value of each item. Deep domain knowledge about specific areas lives in the teams — who interact with customers, conduct discovery, and develop domain expertise over time.

For organizations with deeply specialized domains, LeSS allows the Product Owner to be supported by Area Product Owners in the LeSS Huge configuration. Each Area PO works in a Requirement Area — a large domain slice — and the overall PO coordinates across areas. This directly addresses the domain knowledge concern: the area POs provide depth, and the overall PO provides strategic coherence and final prioritization authority.

The departing Product Owners' expertise does not disappear — it shifts. In LeSS, they would likely become Area Product Owners, team members with domain expertise who work closely with feature teams on their requirement area, or subject matter experts embedded in teams. Their knowledge is more valuable than their title, and the LeSS model can absorb that knowledge with the right role design.

---

## Scenario C: The Stalled Scaling Adoption

MidWest Insurance adopted SAFe eighteen months ago across three ARTs totaling twenty-one teams. At the most recent quarterly leadership review, the following data was presented:

- PI Objective completion rate: 48 percent (down from 62 percent at PI 1)
- Average days from feature request to production: 94 days (same as before SAFe)
- Number of SAFe ceremonies per week per team: 6 (up from 2 before SAFe)
- Developer satisfaction survey: 34 percent satisfied (down from 71 percent before SAFe)

The program leader says: "We have the framework in place. We just need more discipline in following it." A senior Scrum Master says: "The ceremonies are not the problem. We adopted SAFe as an organizational overlay without changing the underlying team structure or product ownership model. We have three ARTs that are still fundamentally component teams with shared dependencies."

What is your assessment of the senior Scrum Master's diagnosis? What does the data suggest about how well empiricism is functioning in this organization? What would you recommend the organization do — not just add or remove — to address the situation? Your post should be 175–225 words.

### Sample Response — Scenario C

The senior Scrum Master's diagnosis is correct, and the data supports it conclusively. A 48 percent PI Objective completion rate means more than half of what the ARTs plan is not delivered — not a discipline problem, a structural one. Discipline improves execution of the right plan; it cannot fix a fundamentally wrong structure. The 94-day lead time, unchanged from pre-SAFe, means the organization is doing more ceremonies and delivering at the same speed. That is the most damning data point — the only outcome that changed is developer satisfaction, which went down.

The empiricism picture is clear: Transparency may have improved through the ceremony structure, but Adaptation is failing. The Inspect and Adapt events are apparently not producing structural changes — the ARTs are inspecting and then recommitting to the same structure. The declining PI Objective completion rate suggests the organization is inspecting evidence that the plan was wrong and then making similarly over-ambitious plans next PI.

My recommendation: stop adding SAFe fidelity and start examining team structure. Which of the twenty-one teams have the most cross-team dependencies? Map those dependencies against the architecture. If three teams account for 70 percent of the dependency delays, the question is whether those three teams can be restructured into one or two feature teams. SAFe works well when it sits on top of a genuinely cross-functional team structure. As an overlay on component teams with architectural coupling, it produces exactly the data MidWest Insurance is reporting.

---

## Peer Response Guidelines

Your reply to a classmate must be at least 75 words and should do at least one of the following:

- Challenge their framework recommendation with a scenario-specific counter-argument
- Extend their argument by addressing an organizational consequence they did not discuss
- Identify a risk in their proposed adoption approach that they did not acknowledge
- Ask a specific follow-up question about how their recommendation would affect team structure or Product Ownership

Avoid replies that simply agree or restate the classmate's argument.

---

## Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario understanding | 2 | Response accurately identifies the core scaling tension in the scenario |
| Module concept application | 3 | At least two specific SAFe or LeSS concepts correctly named and applied |
| Reasoning quality | 2 | Arguments acknowledge trade-offs and connect scaling choices to organizational outcomes |
| Peer responses | 2 | Two substantive peer replies of 75+ words each that advance the discussion |
| Writing quality | 1 | Complete sentences, organized paragraphs, professional tone |
| **Total** | **10** | |
