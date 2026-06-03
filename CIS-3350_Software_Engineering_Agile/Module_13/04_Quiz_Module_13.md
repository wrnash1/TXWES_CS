# Quiz: Module 13 — Continuous Integration and DevOps Basics

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A Scrum team pushes all code changes to the main branch on the last day of the Sprint, resulting in integration conflicts that consume two days of debugging. Which CI practice would most directly prevent this problem?

- A) Canary deployment — to route a small percentage of users to the new code before full release
- B) Daily integration — each developer merges to the main branch at least once per day throughout the Sprint
- C) Blue-green deployment — to maintain two identical environments so the old version can be restored
- D) Static analysis — to detect code quality issues before the merge

Correct Answer: B — Continuous Integration requires frequent integration — at minimum daily. When developers merge only at Sprint end, they accumulate integration risk. Daily integration surfaces conflicts immediately when they are small and specific rather than compounded.

Distractor Analysis:

- Why A is incorrect: Canary deployment is a production release strategy, not a developer workflow practice. It does not address integration conflicts between developer branches during the Sprint.
- Why C is incorrect: Blue-green deployment manages the switch between deployed versions in production — it does not prevent merge conflicts during development.
- Why D is incorrect: Static analysis detects code style and quality issues in individual files. It does not detect integration conflicts between changes made by different developers.

---

## Question 2

Which of the following best distinguishes Continuous Delivery from Continuous Deployment?

- A) Continuous Delivery deploys only to development environments; Continuous Deployment deploys to staging
- B) Continuous Delivery requires all tests to pass before deployment; Continuous Deployment does not require tests
- C) Continuous Delivery keeps a human release decision before production; Continuous Deployment automates the final deployment to production
- D) Continuous Delivery uses canary deployment; Continuous Deployment uses blue-green deployment

Correct Answer: C — Continuous Delivery ensures software is always in a releasable state with a human gate before production. Continuous Deployment removes that gate — every successful pipeline run deploys to production automatically.

Distractor Analysis:

- Why A is incorrect: Both Continuous Delivery and Continuous Deployment deploy beyond development environments. The distinction is about the production gate, not the environment scope.
- Why B is incorrect: Both practices require passing automated tests. The distinction is not about test requirements but about who or what makes the final release decision.
- Why D is incorrect: Both Continuous Delivery and Continuous Deployment can use either blue-green or canary deployment strategies. Deployment strategies are independent choices from the delivery model.

---

## Question 3

A CI pipeline has been red for three days because a developer's change broke two integration tests. Other developers are pushing new code anyway, bypassing the failed checks. What is the most significant risk of this behavior?

- A) The pipeline will take longer to run because more code changes are queued
- B) The team loses the ability to use the pipeline as a reliable quality signal, and defects become invisible until Sprint Review
- C) The static analysis stage will produce more warnings
- D) The canary deployment percentage will increase too quickly

Correct Answer: B — A CI pipeline's value is as a quality gate that makes defects visible immediately. When developers push past a broken pipeline, the signal becomes noise — new defects introduced after the breakage are invisible until they reach Sprint Review or production.

Distractor Analysis:

- Why A is incorrect: Pipeline execution time is a performance concern, not the primary risk of bypassing a failed check. The risk is a quality one, not a scheduling one.
- Why C is incorrect: Static analysis warnings are a code quality concern unrelated to the behavioral consequence of bypassing a broken pipeline.
- Why D is incorrect: Canary deployment percentage is a production release decision entirely separate from CI pipeline behavior during development.

---

## Question 4

The test pyramid places unit tests at the base, integration tests in the middle, and end-to-end (E2E) tests at the top. Which of the following correctly explains why E2E tests should be the smallest layer?

- A) E2E tests are less accurate than unit tests at finding bugs
- B) E2E tests are slow to run, brittle when UI changes occur, and expensive to maintain — making a large E2E suite a pipeline performance and stability liability
- C) E2E tests can only run in production environments, not in CI pipelines
- D) E2E tests require Continuous Deployment to function correctly

Correct Answer: B — E2E tests simulate full user workflows through the UI and system layers. They are inherently slow, sensitive to UI changes, and expensive to maintain. A pipeline with hundreds of E2E tests runs slowly and breaks frequently for non-code reasons — undermining CI's fast feedback value.

Distractor Analysis:

- Why A is incorrect: E2E tests provide broad coverage of integrated behavior. Accuracy is not the issue — cost, speed, and brittleness are.
- Why C is incorrect: E2E tests run in CI staging environments. They are not restricted to production.
- Why D is incorrect: E2E tests are independent of the deployment model. They run in the pipeline regardless of whether the team practices Continuous Deployment or Continuous Delivery.

---

## Question 5

A Scrum team is releasing a major update to their checkout page. A junior developer asks: "Should we use blue-green or canary deployment?" The release includes a new payment provider integration that has never been tested under real production load. Which deployment strategy best addresses this specific risk?

- A) Blue-green — because it provides an instant rollback if the payment provider integration fails
- B) Canary — because it validates the new payment provider under real production traffic before full rollout
- C) Big-bang deployment — because full deployment reveals load issues fastest
- D) Blue-green — because it allows both versions of the checkout to serve traffic simultaneously

Correct Answer: B — Canary deployment routes a small percentage of real users to the new version. This directly validates whether the new payment provider integration handles real production load correctly — a risk that staging environments cannot fully replicate. Issues can be caught at 1 percent traffic before being exposed to all users.

Distractor Analysis:

- Why A is incorrect: Blue-green provides instant rollback but does not validate load behavior before full exposure. After a blue-green switch, 100 percent of users hit the new payment provider simultaneously.
- Why C is incorrect: Big-bang deployment exposes all users to the risk simultaneously. Finding the problem is fast; the impact is maximum.
- Why D is incorrect: Blue-green does not serve traffic on both environments simultaneously — that is the defining characteristic of canary deployment, not blue-green.

---

## Question 6

A team's Definition of Done includes "all CI checks pass." At the end of Sprint 9, two user stories are not passing the integration test stage because a test environment dependency is unavailable. The team lead proposes shipping the stories anyway because "the code works." What is the correct Scrum response?

- A) The team should vote to ship if a majority agrees the code is functionally correct
- B) The Scrum Master should override the team's decision and block the release
- C) The stories do not meet the Definition of Done and should not be included in the Sprint's Increment
- D) The Product Owner can waive the DoD criterion for this Sprint if the business need is urgent

Correct Answer: C — The Definition of Done is a formal commitment. A Story that does not meet all DoD criteria is not done. The correct action is to move the unfinished Stories to the next Sprint rather than ship an Increment that does not meet its quality commitment.

Distractor Analysis:

- Why A is incorrect: The team does not have the authority to suspend the Definition of Done by vote for individual Stories. The DoD is a team-level quality standard, not a per-story negotiation.
- Why B is incorrect: The Scrum Master facilitates the team's adherence to Scrum but does not have override authority. The Scrum Master's role is to make the situation transparent and help the team understand the implications.
- Why D is incorrect: The Product Owner may influence the DoD over time through team agreement, but cannot unilaterally waive DoD criteria for a Sprint. The DoD is a team commitment, not a Product Owner permission to grant or revoke.

---

## Question 7

Which Scrum pillar is most directly supported by a CI pipeline that makes the build status visible to the entire team at all times?

- A) Adaptation — because the team can adapt their code when the pipeline is red
- B) Inspection — because the pipeline provides continuous inspection of the Increment's quality
- C) Transparency — because the pipeline makes the current quality state of the codebase visible to all stakeholders
- D) Commitment — because developers commit to keeping the pipeline green

Correct Answer: C — Transparency is the pillar that requires work and progress to be visible. A CI pipeline with a public green/red status makes the current releasability of the Increment visible to the entire Scrum Team and stakeholders in real time. Without CI, quality is only visible at Sprint Review.

Distractor Analysis:

- Why A is incorrect: Adaptation is the pillar that describes responding to what inspection reveals. While adaptation may follow a red pipeline, the pipeline itself primarily addresses transparency.
- Why B is incorrect: The Scrum Guide defines Inspection as reviewing Scrum artifacts and Sprint progress during Scrum events. The CI pipeline is a technical practice, not a Scrum event. It most directly supports Transparency.
- Why D is incorrect: Commitment is a Scrum value, not one of the three pillars of empiricism. The pillars are Transparency, Inspection, and Adaptation.

---

## Question 8

Blue-green deployment is ideal for which type of release situation?

- A) Releases where the new version needs to be validated under real production load before reaching all users
- B) Releases where an instant rollback mechanism is required and the team can afford to run two production environments
- C) Releases where the team wants to gradually increase the percentage of users on the new version
- D) Releases where the team does not have strong production monitoring

Correct Answer: B — Blue-green deployment's primary benefit is the instant rollback: the previous environment (blue) remains intact after the switch to green. If the release reveals a critical issue, traffic switches back to blue in seconds. The cost is maintaining two complete production environments simultaneously.

Distractor Analysis:

- Why A is incorrect: Validating behavior under real production load before full exposure is the benefit of canary deployment, not blue-green. Blue-green exposes all users to the new version at the moment of the switch.
- Why C is incorrect: Gradually increasing the percentage of users is canary deployment. Blue-green switches 100 percent of traffic at once.
- Why D is incorrect: Both blue-green and canary deployment benefit from strong monitoring. Blue-green without monitoring does not help identify problems after the switch — it only provides the rollback mechanism.

---

## Question 9

A developer argues: "Our team already does manual testing at the end of each Sprint before the demo. Why do we need a CI pipeline — it's redundant?" What is the most effective technical counter-argument?

- A) CI pipelines are required by the Scrum Guide for any team delivering a potentially releasable Increment
- B) Manual testing at Sprint end verifies behavior at a single point in time; CI pipelines detect regressions continuously throughout the Sprint, when the cost of fixing them is lowest
- C) Manual testing is less accurate than automated testing because humans make mistakes
- D) CI pipelines eliminate the need for Sprint Reviews because stakeholders can inspect the pipeline directly

Correct Answer: B — The fundamental advantage of CI over end-of-Sprint manual testing is timing. CI detects regressions immediately after the code change that caused them — when the developer who wrote the code is still working in that area. End-of-Sprint testing detects regressions days or weeks later, when the context is lost and the fix is more expensive.

Distractor Analysis:

- Why A is incorrect: The Scrum Guide does not prescribe CI pipelines or any specific engineering practice. The Guide is intentionally silent on technical practices, which are the team's responsibility to choose.
- Why C is incorrect: While automated tests execute consistently, the argument does not address the specific redundancy concern — it would apply equally to any testing approach.
- Why D is incorrect: CI pipelines do not replace Sprint Reviews. Sprint Review is a Scrum event where stakeholders inspect the Increment and provide feedback — an entirely different purpose from automated quality verification.

---

## Question 10

DevOps culture aligns with Scrum's model of cross-functional teams in what specific way?

- A) DevOps requires developers and Product Owners to pair on writing deployment scripts
- B) DevOps assigns a dedicated operations role to each Scrum Team to manage production deployments
- C) DevOps removes the separation between development and operations accountability — the team that builds the software is responsible for its production reliability
- D) DevOps replaces the Sprint Retrospective with a production incident review

Correct Answer: C — The DevOps principle of "you build it, you run it" means the development team owns production reliability, not a separate operations team. This aligns directly with Scrum's cross-functional team model: all skills needed to create a done Increment, including operations ownership, belong within the team.

Distractor Analysis:

- Why A is incorrect: DevOps does not prescribe Product Owner involvement in deployment scripts. DevOps addresses the organizational boundary between development and operations teams.
- Why B is incorrect: Adding a dedicated operations role to each team is closer to traditional operations thinking than DevOps. DevOps moves operations skills into the development team, not alongside it.
- Why D is incorrect: DevOps does not modify or replace Scrum events. Sprint Retrospectives remain the team's mechanism for continuous improvement regardless of DevOps adoption.

---
