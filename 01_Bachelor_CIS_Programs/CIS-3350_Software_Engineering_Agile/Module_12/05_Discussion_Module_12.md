# Discussion Forum: Module 12 — Test-Driven Development and BDD

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Overview

This discussion asks you to apply TDD and BDD concepts to realistic professional scenarios. Write your initial post responding to one scenario, then respond substantively to at least two classmates who chose different scenarios.

---

## Professor Nash Note

TDD and BDD are discipline problems as much as they are technical problems. Every developer I have met who resisted TDD gave the same objection: "Writing the test first takes longer." What they were really saying is: "I have never experienced what happens to a codebase after six months of TDD compared to six months without it." The best responses in this discussion will engage with the human side — why teams abandon the discipline, what organizational conditions make it harder, and how Scrum events create the structure for the conversation to happen. Think about what the Definition of Done really means when your team chooses to skip the tests.

---

## Scenario A: The Test-First Resistance

A Scrum team of six developers is adopting TDD for the first time. By Sprint 3, three developers are following the Red-Green-Refactor cycle consistently. The other three are writing tests after their implementation code — or not writing tests at all for "simple" methods. In the Sprint Retrospective, the three resisters argue: "TDD slows us down. We are missing Sprint goals because we spend too much time on tests before we even know if the feature design is right. We should write the code first, get it working, and then write tests to document what we built."

The Scrum Master asks the team to examine the evidence: in the last three Sprints, 70 percent of defects found during Sprint Review were in code written by developers who did not follow TDD. Code written TDD-style has required fewer bug fixes in subsequent Sprints. Story points completed per Sprint are slightly lower for TDD stories in the first two Sprints but equal by Sprint 3.

How would you respond to the resisters' argument? Address the specific claim that "TDD slows us down." What does the retrospective evidence suggest about short-term cost versus long-term benefit? How does TDD connect to the team's Definition of Done, and what should the Scrum Master do if the team decides TDD is optional? Your post should be 175–225 words.

### Sample Response — Scenario A

The resisters' argument is accurate about the short term and wrong about the medium term. TDD does slow initial code writing — the discipline of writing the failing test first, then writing only enough code to pass, then refactoring requires more intentionality than writing code until it seems to work. But the retrospective evidence answers the argument directly: 70 percent of defects are in code without TDD, and velocity equalizes by Sprint 3. The cost is front-loaded; the benefit compounds.

The claim that "writing tests documents what we built" is the misconception at the core of their resistance. Tests written after implementation verify existing behavior — they do not drive design. TDD's second benefit is design feedback: if a unit is hard to test, it is usually hard to change. Post-implementation tests do not reveal that signal.

The Definition of Done is the correct mechanism to resolve this team disagreement. If the team's DoD includes "unit tests written for all new code" or "all CI checks pass," a developer who ships untested code has not completed their work by definition — the Story is not done. The Scrum Master's role is not to enforce TDD technically but to facilitate the team's agreement that a DoD with TDD criteria is non-negotiable once agreed, and that exemptions for "simple" methods are how the standard erodes Sprint by Sprint.

---

## Scenario B: The BDD Breakdown

A product team at FinEdge is attempting BDD for the first time. The Product Owner writes acceptance criteria in user stories. A QA analyst writes Gherkin scenarios after reading the stories. Developers receive the Gherkin files and implement the features. At the Sprint Review, the Product Owner sees the demos and raises three issues: the interest calculation feature works correctly according to the test scenarios, but it calculates interest based on a 365-day year when the Product Owner expected a 360-day banking year; the early withdrawal scenario passes all tests but does not match how early withdrawal actually works in the target market; the error message for an invalid account number is technically tested but is not the message the compliance team approved.

The QA analyst says: "All of my scenarios pass. This is a requirements problem, not a test problem." The Product Owner says: "This is a testing problem — the tests did not catch the real requirements." The Scrum Master says: "This is a collaboration problem."

Who is right, and why? What does this scenario reveal about how BDD is supposed to work compared to how the team used it? What should have happened during Sprint refinement? Your post should be 175–225 words.

### Sample Response — Scenario B

The Scrum Master is correct, and the failure is a collaboration failure that created a testing failure and a requirements failure downstream. BDD is not a documentation format — it is a conversation protocol. The three amigos model (Product Owner, developer, QA) is designed to surface ambiguity before implementation begins, not to generate test files that one role hands to another.

The 360-versus-365-day interest calculation is the clearest example. That ambiguity exists in the domain, not in the code. A QA analyst writing scenarios from a user story alone has no mechanism to catch it because the story does not specify it and the analyst may not know banking calendar conventions. A three-amigos conversation during refinement, with a developer asking "which day-count convention applies?" would have surfaced the question before a single line of implementation code was written.

The passing tests are not wrong — they correctly test the behavior that was specified. The specification was incomplete because BDD's collaborative process was skipped. The team implemented a waterfall workflow — write requirements, write tests, write code — and called it BDD because the tests use Gherkin syntax. BDD is not a syntax. It is a shared understanding built through conversation, and the conversation must happen before the scenario is written. The team should add a refinement checkpoint: no scenario is written without the three-amigos review, and scenarios are accepted into the Sprint only when all three roles agree they are complete.

---

## Scenario C: The Definition of Done Drift

The Velocity team has a Definition of Done that includes: "Unit tests written," "Integration tests passing," "Code reviewed by one peer," and "CI pipeline green." In Sprint 7, the team is under pressure to deliver a major feature before a client demonstration. With two days left in the Sprint, two user stories are complete by all DoD criteria except the integration tests, which are failing because a dependency service is down in the test environment. The team lead says: "These features work — we tested them manually. The integration tests are failing because of the test environment, not our code. Let's ship them and fix the test environment next Sprint."

Three team members agree. Two team members object. The Scrum Master does not override the decision — the team votes to ship.

In the following Sprint, the dependency service comes back online and the integration tests reveal two actual defects in the features that were shipped. The client demo goes poorly.

Analyze what went wrong from a TDD and Definition of Done perspective. What should the Scrum Master have done when the team was considering bypassing the DoD? What does this scenario illustrate about the purpose of automated tests versus manual testing? Your post should be 175–225 words.

### Sample Response — Scenario C

The team made a decision they were not authorized to make — they unilaterally lowered the quality standard of their Definition of Done under deadline pressure. The Definition of Done is a Scrum artifact, and while the team owns it, it cannot be selectively suspended for individual Stories. A Story that does not meet the Definition of Done is not done. Shipping it anyway does not change the DoD — it creates undeclared technical debt with a warranty that "we think it works."

The Scrum Master's error was framing the decision as the team's to make by vote. The Scrum Master is accountable for the Scrum Team's effectiveness, which includes protecting the validity of the DoD as a quality guarantee. The correct action was to clearly state that the Stories are not done, move them to the next Sprint, and help the team communicate to stakeholders that the demo scope is smaller than planned. That is a harder conversation than shipping — and it is the Scrum value of courage.

The scenario illustrates the critical difference between manual testing and automated integration testing. Manual testing confirmed behavior under known, happy-path conditions in the moment. The integration tests, when run against the real dependency, discovered defects that manual testing missed — defects in edge cases the human tester did not think to exercise. Automated tests do not replace judgment, but they execute consistently across every scenario they encode, every time, without deadline pressure.

---

## Peer Response Guidelines

Your reply to a classmate must be at least 75 words and should do at least one of the following:

- Challenge an assumption or propose a different approach with reasoning
- Extend their argument by connecting to a Scrum event or artifact they did not address
- Identify a practical risk in their proposed solution that they did not mention
- Ask a specific follow-up question about how their recommendation would affect the team's Definition of Done or Sprint velocity

Avoid replies that simply agree or restate the classmate's argument.

---

## Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario understanding | 2 | Response accurately identifies the core TDD or BDD failure in the scenario |
| Module concept application | 2 | At least two specific TDD or BDD concepts correctly named and applied |
| Reasoning quality | 2 | Arguments connect testing practices to Sprint-level and business outcomes |
| Peer responses | 3 | Two substantive peer replies of 75+ words each that advance the discussion |
| Writing quality | 1 | Complete sentences, organized paragraphs, professional tone |
| **Total** | **10** | |
