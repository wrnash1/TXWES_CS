# Video Script: Module 13 — Continuous Integration and DevOps Basics

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Estimated Duration:** 20 minutes

**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Pipeline diagrams should show sequential stages with pass/fail gates; deployment diagrams show environment progression

---

## Section 1 — Welcome and Why CI/CD Matters for Scrum Teams [00:00–03:00]

"Welcome to Module 13. We have spent the last two modules on technical practices — design patterns and test-driven development. Now we are going to look at the infrastructure that holds all of those practices together: Continuous Integration and the foundations of DevOps.

If TDD is the discipline that ensures individual units of code are correct, CI is the infrastructure that ensures the entire codebase stays correct as the team integrates their work. These two practices are meant to be used together, and neither is fully effective without the other.

Here is the problem CI solves. Imagine a Sprint team of five developers. Each developer works on a different feature for several days. At the end of the Sprint, they all try to merge their code. The result is frequently called integration hell — conflicting changes, broken dependencies, features that work individually but fail together. The team spends the last two days of the Sprint debugging merges instead of delivering value.

CI eliminates integration hell by making integration a continuous, automated activity. Code is integrated frequently — at least daily — and an automated pipeline verifies that the integrated codebase still builds and passes all tests after every merge.

By the end of this module you will be able to:

- Define Continuous Integration, Continuous Delivery, and Continuous Deployment and distinguish them
- Describe the stages of a CI pipeline and what each stage verifies
- Explain deployment strategies including blue-green and canary deployments
- Connect CI/CD practices to Scrum's goal of a potentially releasable Increment every Sprint
- Identify the relationship between CI/CD and the Definition of Done"

---

## Section 2 — Continuous Integration: The Pipeline [03:00–08:00]

"Let me define the terms precisely, because CI, CD, and Continuous Deployment are often used interchangeably when they mean different things.

Continuous Integration is the practice of integrating code changes into a shared repository frequently — at least daily — and verifying each integration with an automated build and test run. The key word is automated. If a developer has to manually run tests before pushing, CI is not happening.

[SHOW DIAGRAM: CI pipeline stages — commit trigger → build → unit tests → static analysis/lint → integration tests → artifact creation]

A typical CI pipeline has several stages. The commit trigger: every time a developer pushes code to the shared repository, the pipeline starts automatically. The build stage: the code is compiled or assembled. If the code cannot even build, nothing else matters. The unit test stage: the automated unit tests — written with TDD — run against the freshly built code. Static analysis and lint: tools check for code style violations, security vulnerabilities, and common code quality issues. Integration tests: the code is tested against other components it depends on — databases, APIs, external services. Finally, if all stages pass, the pipeline produces an artifact — a deployable package.

The pipeline is a quality gate. If any stage fails, the pipeline stops and notifies the team immediately. The developer who caused the failure is responsible for fixing it before anyone else pushes new changes. This is the culture dimension of CI: a broken build is an emergency, not a to-do item for later.

PSM I Exam Tip: CI connects directly to Scrum's transparency principle. The pipeline makes the health of the codebase visible to everyone in real time. A green pipeline means the Increment is potentially releasable. A red pipeline means it is not. You cannot inspect what you cannot see."

---

## Section 3 — Continuous Delivery and Continuous Deployment [08:00–12:00]

"CI ensures the code is always in a buildable, testable state. Continuous Delivery extends that further — it ensures the code is always in a releasable state. Let me explain the distinction.

[SHOW DIAGRAM: CI/CD pipeline extended — CI stages → staging environment → manual release gate → production; and CD without gate → production]

With Continuous Delivery, every successful CI pipeline run produces a release candidate — software that has been built, tested, and deployed to a staging environment that mirrors production. A human decision — typically the Product Owner or release manager — is the only gate between staging and production. The software is ready to release at any moment. The question is when, not whether.

Continuous Deployment removes the human gate entirely. Every successful pipeline run deploys to production automatically. This is the most aggressive form of CD and requires extremely high confidence in the automated test coverage and monitoring.

For Scrum teams, the relevant concept is Continuous Delivery. The Scrum Guide says the Sprint produces a potentially releasable Increment — meaning the decision to release belongs to the Product Owner, not to a technical readiness process. If the team's CI/CD pipeline is configured for Continuous Delivery, the Product Owner can release at any Sprint Review or at any point during the Sprint when a feature is complete.

PSM I Exam Tip: Do not confuse Continuous Delivery with Continuous Deployment. The difference is whether a human gate exists before production. Continuous Delivery keeps the human decision. Continuous Deployment automates it away."

---

## Section 4 — Deployment Strategies [12:00–17:00]

"Once a team has a working CI/CD pipeline, they still have to make decisions about how to deploy changes to production. Two deployment strategies appear frequently in modern engineering teams.

[SHOW DIAGRAM: Blue-Green deployment — live traffic on blue environment; green environment prepared with new version; traffic switches at go-live; blue kept as rollback]

Blue-green deployment: the team maintains two identical production environments — blue and green. At any given time, one environment is live and serving users. The new version is deployed to the inactive environment and tested there. When ready, a router switch redirects all traffic from the live environment to the newly deployed one. The old environment remains intact as an instant rollback option if something goes wrong. The primary benefit is zero-downtime deployment and an instant rollback mechanism. The primary cost is maintaining two complete production environments simultaneously.

[SHOW DIAGRAM: Canary deployment — 100% traffic on v1; 5% routed to v2 (canary); monitoring; gradual ramp 5%→25%→50%→100%]

Canary deployment: a small percentage of production traffic — often one to five percent — is routed to the new version while the rest continues to receive the old version. The team monitors error rates, performance metrics, and user behavior on the canary segment. If the metrics are healthy, the percentage increases gradually. If problems appear, the canary percentage drops back to zero. The primary benefit is real-world validation before full rollout — the team can catch load-related problems or unexpected behavior that staging environments do not reveal. The primary cost is the complexity of running two versions of the software simultaneously, especially when database schemas or APIs are involved.

PSM I Exam Tip: The exam may present scenarios involving risk-averse deployments or teams that need to validate behavior under real load. Blue-green favors speed of rollback. Canary favors validation of real-world behavior. Both are preferable to a traditional big-bang deployment where all users receive the new version simultaneously with no rollback plan."

---

## Section 5 — CI/CD, Scrum, and the Definition of Done [17:00–20:00]

"Let me connect everything we have covered back to Scrum.

[SHOW DIAGRAM: Sprint cycle with CI/CD embedded — developers push code → CI pipeline runs → green pipeline = potentially releasable Increment → Sprint Review → Product Owner release decision]

The Scrum Guide's Definition of Done is a formal commitment that defines the quality standards an Increment must meet to be considered done. In teams with a working CI/CD pipeline, the DoD almost always includes pipeline-related criteria: all CI checks pass, the artifact is deployed to the staging environment, integration tests pass in the staging environment. These criteria are not optional polish — they are the mechanism by which 'potentially releasable' becomes a real claim rather than an optimistic one.

The relationship between CI/CD and velocity is also important for Scrum teams to understand. Teams that lack CI/CD spend significant Sprint capacity on manual testing, manual integration, and debugging merge conflicts. Teams with mature CI/CD pipelines eliminate most of that waste. The investment in building the pipeline is paid back in velocity within a few Sprints.

DevOps as a practice extends CI/CD beyond the pipeline to a cultural orientation: development and operations teams work together rather than throwing software over a wall. In Scrum terms, this means the team that builds the software is responsible for its reliability in production — not a separate operations team. This cultural shift is what makes the 'you build it, you run it' principle possible, and it is why Scrum teams that adopt DevOps practices deliver more reliably Sprint over Sprint.

In Module 14 we will look at how Scrum scales — how organizations apply Scrum principles when the work requires more than one team. See you there."

---

## End Card

- Next module: Module 14 – Scaled Agile: SAFe and LeSS Overview
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
