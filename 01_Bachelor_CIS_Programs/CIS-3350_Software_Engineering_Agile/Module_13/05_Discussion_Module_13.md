# Discussion Forum: Module 13 — Continuous Integration and DevOps Basics

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

## Overview

This discussion asks you to apply CI/CD concepts to realistic professional scenarios. Write your initial post responding to one scenario, then respond substantively to at least two classmates who chose different scenarios.

---

## Professor Nash Note

CI/CD is one of those engineering topics that sounds purely technical but has deep organizational and process implications. The best responses in this discussion will go beyond "set up a pipeline" to examine the human side: why teams resist automated gates, how CI/CD changes team culture and communication, and what the real trade-offs are when moving fast with automation. Think about the Scrum values — courage, transparency, commitment — and how they show up in CI/CD decisions.

---

## Scenario A: The Long-Running Test Suite

Your Scrum team has a CI pipeline that takes 45 minutes to complete. Developers have started pushing code less frequently — sometimes holding commits for two or three days — because waiting 45 minutes for feedback is too disruptive. During the most recent Sprint Retrospective, the team identified two problems: integration bugs are being discovered later in the Sprint because commits are batched, and the pipeline is becoming a bottleneck during the last two days of the Sprint when everyone is pushing final work.

The Scrum Master asks the team to improve CI feedback time. One developer proposes parallelizing the test suite across multiple runners. Another suggests splitting the pipeline into a "fast" stage (unit tests, lint — 5 minutes) and a "slow" stage (integration tests, E2E — 40 minutes) that runs asynchronously.

What are the trade-offs of each proposed solution? Which would you recommend, and why? What change would you also make to team behavior — not just pipeline configuration — to address the root cause? Your post should be 175–225 words.

### Sample Response — Scenario A

Both proposed solutions have merit, but they address different layers of the problem. Parallelizing the test suite across multiple runners is a pure infrastructure solution — it reduces total elapsed time by running tests concurrently. If the 40-minute integration suite can be split across four runners, the wall-clock time drops to about ten minutes. The trade-off is cost — running four simultaneous runners is four times more expensive — and the complexity of managing test isolation across parallel environments. Tests that share state or write to a shared database can produce race conditions when parallelized.

The staged pipeline approach is more architecturally sound for development workflow. Separating a five-minute fast stage from a forty-minute slow stage means developers get immediate feedback on syntax errors, style violations, and unit test failures in five minutes. The slow integration tests run asynchronously and can notify the team if they fail without blocking the developer's next commit. The trade-off is that integration failures become known after the fact rather than before merge — which requires team discipline to treat integration failures as a blocking priority rather than something to address later.

My recommendation is a combination: implement the staged pipeline immediately for workflow improvement, and use runner parallelization for the integration tests specifically, targeting a fifteen-minute complete pipeline time. The behavioral change the team also needs to make is to treat a red pipeline as an interruption-level priority — not something to queue behind other work. Restoring a culture where a broken build is everyone's problem is as important as the technical improvements.

---

## Scenario B: The Deployment Strategy Decision

Your team is preparing to release a major update to a high-traffic e-commerce checkout page. The new version includes a redesigned checkout flow and a new payment provider integration. Two team members have competing recommendations.

The first recommends blue-green deployment because the team can test the new checkout in a completely isolated environment, flip the switch, and immediately roll back if anything goes wrong. The second recommends canary deployment, pointing out that the new payment provider has never been tested under real production load and a 5 percent canary would reveal any load-related issues before the full rollout.

There are complications: the new checkout uses a slightly different database schema than the old checkout, and both versions need to run simultaneously during any transition period. The team has strong monitoring on error rates and payment conversion rates. What recommendation would you make and why? What database strategy would address the schema compatibility concern? Your post should be 175–225 words.

### Sample Response — Scenario B

This scenario presents a genuine tension between the two strategies, and the right answer depends on the database schema concern more than anything else. Blue-green deployment is ideal when the old and new environments are truly independent — but when they share a database with an incompatible schema, the "instant switch" is not actually instant. If the blue version is still processing requests in-flight during the switch, those requests will fail when they encounter a schema that was changed for the green version.

The fact that the team has strong monitoring on error rates and conversion rates strongly favors canary deployment for this specific release. The canary percentage can start at one percent — exposing only the smallest fraction of real traffic to the new payment provider integration — and increase gradually as the monitoring confirms stable error rates and equivalent conversion.

For the database schema, the recommended pattern is an expand-and-contract migration. In the expand phase, add the new columns or tables needed by the new checkout version without removing anything the old version uses. Both versions can now run against the same schema simultaneously. During the canary rollout, the new version uses the new columns; the old version continues using the old ones. Once the canary reaches 100 percent and the old version is decommissioned, run the contract phase to clean up the deprecated schema elements. This approach makes the schema change backwards-compatible across the transition window.

---

## Scenario C: The Broken Build Culture

You join a team that has a CI pipeline, but it is frequently broken — sometimes for days at a time. When you ask about it, you hear: "Oh, the build has been red for a week, but we know it's just that flaky integration test. We just push anyway." The branch protection rules are configured so that administrators can bypass the required checks, and senior developers routinely override the gate when they are under deadline pressure.

The result is that the team has CI/CD infrastructure but not CI/CD culture. The pipeline exists but provides no real quality guarantee. The Definition of Done says "all CI checks pass" but that criterion is effectively ignored. How do you diagnose the root causes of this situation? What specific changes — both technical and organizational — would you propose? How does this connect to Scrum values and the Definition of Done? Your post should be 175–225 words.

### Sample Response — Scenario C

The situation describes a broken feedback loop, and the root causes are layered. The technical root cause is the flaky integration test — a test that fails intermittently for reasons unrelated to the code being tested. Flaky tests are damaging to CI culture because they teach the team that a red build might not mean anything. Once developers learn to ignore the pipeline, it loses its authority as a quality gate and becomes background noise.

The organizational root cause is the bypass policy. When administrators can override branch protection — and do so regularly under deadline pressure — the message to the team is that the pipeline is optional when things are urgent. But urgency is exactly the wrong time to skip quality checks. This is the courage value in Scrum: the team must have the courage to slow down and fix the build rather than shipping untested changes.

My proposed changes have two layers. Technically: quarantine the flaky test immediately — tag it as skipped with a tracking issue so it does not block the pipeline while being investigated. A quarantined test is better than an ignored gate. Organizationally: remove the bypass permission for administrators. If no one can override the gate, the team is forced to address build failures rather than work around them. Connect this directly to the Definition of Done: if the DoD says CI must pass, and CI is optional in practice, the team has two options — fix the pipeline or change the DoD. Running with a contradictory DoD is the least defensible option.

---

## Peer Response Guidelines

Your reply to a classmate must be at least 75 words and should do at least one of the following:

- Challenge an assumption or propose a different technical approach with reasoning
- Extend their argument by connecting to a pipeline stage, strategy, or Scrum concept they did not address
- Identify a practical risk in their proposed solution that they did not mention
- Ask a specific follow-up question about implementation details or trade-offs

Avoid replies that simply agree or restate the classmate's argument.

---

## Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario understanding | 2 | Response accurately identifies the core technical and organizational tension in the scenario |
| Module concept application | 3 | At least two specific CI/CD concepts correctly applied |
| Reasoning quality | 2 | Arguments are logical, acknowledge trade-offs, and connect technical solutions to team behavior |
| Peer responses | 2 | Two substantive peer replies of 75+ words each that advance the discussion |
| Writing quality | 1 | Complete sentences, organized paragraphs, professional tone |
| **Total** | **10** | |
