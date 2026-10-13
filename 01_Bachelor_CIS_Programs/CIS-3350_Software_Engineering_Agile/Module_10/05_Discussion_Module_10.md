# Discussion Forum: Module 10 — Test-Driven Development (TDD)

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Overview

This discussion asks you to apply TDD concepts to realistic professional scenarios. Write your initial post responding to one scenario, then respond substantively to at least two classmates who chose different scenarios.

---

## Professor Nash Note

Test-Driven Development is one of those practices that sounds simple in theory and feels uncomfortable in practice — at least at first. I want you to think carefully about the human and organizational side of TDD, not just the mechanics. The best responses will move beyond "TDD is good because tests catch bugs" to examine trade-offs, team dynamics, and the realistic conditions under which TDD creates or destroys value. There are no purely right or wrong answers here — strong reasoning and evidence from the module matter more than taking a particular position.

---

## Scenario A: The Resistant Team

A mid-sized software company has just hired you as a senior developer. During your first week, you discover that the team writes no automated tests. When you suggest adopting TDD, two teammates push back. The first says: "We ship features faster without tests — writing tests first slows us down." The second says: "Our codebase is too messy to add tests now. We'd have to refactor everything before TDD could even work."

Both teammates have valid points rooted in real experience. How would you respond to each objection? What evidence or reasoning from the module supports your position? What would you propose as a realistic first step toward TDD adoption that doesn't derail the team's Sprint commitments?

### Sample Response — Scenario A

The first teammate's concern about speed is understandable and reflects a real phenomenon: TDD does slow teams down initially, typically by fifteen to thirty percent during the learning period. However, the module distinguishes between short-term velocity and long-term throughput. Teams that skip tests pay a compounding tax in debugging time, production incidents, and the fear-driven reluctance to refactor code that becomes harder to maintain with every Sprint. The correct response isn't to argue that TDD is always faster — it's to acknowledge the real cost and then explain why the long-term investment is worth making.

The second teammate raises a structural concern about legacy code. This is also valid: applying TDD to untested legacy code requires a different approach than greenfield development. A realistic strategy is the "strangler fig" pattern — rather than retrofitting tests onto existing code all at once, the team writes tests for every new feature or bug fix going forward. Over time, the tested surface area grows and the legacy code gradually becomes surrounded by tests. This respects the current Sprint pace while moving toward a more sustainable foundation.

As a practical first step, I would propose a team agreement: for one Sprint, every new feature must be built using TDD. Existing code is not touched. This creates real experience with the process without the daunting task of retrofitting everything. After the Sprint, the team reflects empirically on what went well and what was difficult — which aligns directly with Scrum's inspect-and-adapt philosophy and the Sprint Retrospective.

---

## Scenario B: The Coverage Debate

Your Scrum team has just adopted a policy requiring 80% code coverage before any feature branch can be merged. Three weeks in, you notice that several developers are writing tests that call every function but make no assertions — just enough to hit the coverage threshold without actually verifying behavior. The CI pipeline shows green, coverage is at 84%, but you found a critical bug in production that the tests completely missed.

How do you explain what went wrong to a Product Owner who doesn't have a technical background? What does this situation reveal about the relationship between coverage metrics and test quality? What changes would you propose to the team's Definition of Done to prevent this from recurring?

### Sample Response — Scenario B

To explain the situation to a non-technical Product Owner, I would use an analogy: imagine a checklist for a restaurant kitchen that requires inspectors to visit every station — stove, prep area, refrigerator — but doesn't require them to actually check whether the food is safe. The inspector visits every station and the checklist shows 100% complete, but the restaurant can still make customers sick because visiting a station and verifying its safety are two completely different things. That's what happened with our coverage requirement: the tests touched every function but verified nothing.

The root cause is a common misconception that the module addresses directly: code coverage measures execution, not correctness. An 84% coverage number tells us that 84% of lines were run — nothing more. A test with no assertions can achieve full coverage while testing absolutely nothing.

This situation reveals a fundamental flaw in using coverage as the sole quality gate. Coverage is a useful signal for identifying dead code paths, but it cannot replace meaningful assertions. The Definition of Done change I would propose has two parts. First, add a requirement that every test must include at least one assertion that verifies a specific behavioral outcome — not just that the function ran without throwing an error. Second, introduce peer code review of the test file alongside the production code file as a required step before merge. A reviewer who reads a test with no assertions should flag it before it reaches the CI pipeline. Coverage remains useful as a floor, but the quality of assertions determines whether that floor actually protects the team.

---

## Scenario C: TDD and the Sprint Timeline

During Sprint Planning, your team estimates a user story at five story points. Midway through the Sprint, the developer assigned to the story reports that they have spent two days writing tests and implementing the feature with TDD, but only have two days left and the feature is roughly sixty percent complete. They estimate they need four more days to finish properly.

The Scrum Master asks the team how TDD affected this situation and whether the story was correctly estimated. The Product Owner asks whether the developer should skip the remaining tests to finish the feature in time. How do you assess what went wrong during planning? How do you respond to the Product Owner's suggestion to skip tests? What does this situation reveal about how Scrum teams should account for TDD in their estimations?

### Sample Response — Scenario C

The planning failure here is an estimation problem, not a TDD problem. When a team adopts TDD but estimates stories based on "how long it takes to write the code," they are systematically underestimating because they have mentally excluded test-writing time from the estimate. Story points should reflect the total effort required to produce a Done Increment — and for a team with TDD in their Definition of Done, that includes writing tests. The team's velocity should be calibrated against stories completed with TDD, not against stories completed without it. If the team has been estimating without accounting for testing, their historical velocity is inflated relative to their actual Done capacity.

Regarding the Product Owner's suggestion to skip the remaining tests: this is a meaningful conversation about the Definition of Done, and the Scrum Master should facilitate it transparently. The Definition of Done is not optional — it defines what "Done" means for this team. Delivering code without tests that the team agreed should be present doesn't produce a Done Increment; it produces something that looks done but carries hidden technical debt and regression risk. The honest options are to reduce scope within the Sprint (do fewer things fully Done), carry the story into the next Sprint, or have a team conversation about temporarily relaxing the DoD — understanding that technical debt created today costs more to resolve later.

This situation is also valuable retrospective material. The team should examine whether five-point stories consistently require more than five points of effort when TDD is applied, which would indicate the need to recalibrate velocity or re-estimate this story size. The Retrospective is precisely the venue for this kind of process improvement conversation.

---

## Peer Response Guidelines

When responding to a classmate, your reply must be at least 60 words and should do at least one of the following:

- Challenge an assumption in their argument with a counter-example or alternative perspective
- Extend their reasoning by connecting it to a concept from the module they did not mention
- Share a practical observation about how their proposed solution would play out in a real team context
- Ask a focused follow-up question that pushes the discussion deeper

Avoid replies that only agree or restate what your classmate said.

---

## Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario understanding | 2 | Response demonstrates accurate understanding of the scenario's core tension |
| Module concept application | 3 | At least two specific module concepts (red-green-refactor, FIRST, mocking, coverage, etc.) correctly applied |
| Reasoning quality | 2 | Arguments are logical, evidence-based, and acknowledge trade-offs rather than presenting one-sided conclusions |
| Peer responses | 2 | Two substantive peer replies of 60+ words each that advance the discussion |
| Writing quality | 1 | Complete sentences, organized paragraphs, professional tone |
| **Total** | **10** | |
