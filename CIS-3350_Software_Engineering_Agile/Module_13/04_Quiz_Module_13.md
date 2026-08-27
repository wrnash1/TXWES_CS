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

### Question 11 (5 points)

A CI pipeline's static analysis stage fails because a developer used a deprecated API function. The developer argues: "The function still works — this is a false positive." What is the most accurate technical response?

- A) Static analysis results are advisory only; the developer can override them if the code compiles successfully
- B) Static analysis checks code quality patterns without running the code; deprecated API warnings indicate future breakage risk that the developer should address before merging
- C) Static analysis is only relevant for security vulnerabilities, not API usage patterns
- D) The pipeline should skip static analysis when the build stage passes to avoid slowing the team down

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: If the Definition of Done includes "all CI checks pass," then a static analysis failure means the story is not done — it is not advisory.
  - Why C is incorrect: Static analysis tools cover a broad range of issues including deprecated APIs, code style, complexity metrics, and security patterns — not only security.
  - Why D is incorrect: Skipping static analysis removes a quality signal that catches problems when they are cheapest to fix; it does not make the team faster in any meaningful sprint-over-sprint sense.

---

### Question 12 (5 points)

A team uses Continuous Delivery with a manual release gate. The Product Owner asks: "Why does the deployment still require my approval if the pipeline is automated?" What is the most accurate explanation?

- A) Regulatory requirements prohibit fully automated deployments for any software that handles user data
- B) Continuous Delivery ensures software is technically releasable after every pipeline run, but the timing of when to release to users is a business decision reserved for the Product Owner
- C) The pipeline cannot deploy to production without the Product Owner's technical credentials
- D) The manual gate is required by the Scrum Guide, which states the Product Owner must approve each Increment before release

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Regulatory constraints may apply in specific industries, but this is not the defining reason for the manual gate in Continuous Delivery — the gate is a deliberate design choice, not a universal rule.
  - Why C is incorrect: The manual gate is a process decision, not a technical credential requirement. Deployment pipelines are configured to require approval, not credentials.
  - Why D is incorrect: The Scrum Guide does not prescribe how releases are managed or who must approve deployments; the Guide is intentionally silent on engineering practices.

---

### Question 13 (5 points)

Which of the following best describes the primary role of integration tests in a CI pipeline, as distinct from unit tests?

- A) Integration tests verify that individual functions return the correct values for given inputs
- B) Integration tests verify that multiple components — such as the application and its database — work correctly together
- C) Integration tests replace E2E tests in teams that do not have a staging environment
- D) Integration tests run faster than unit tests because they test fewer lines of code

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Verifying individual function outputs is the role of unit tests, not integration tests.
  - Why C is incorrect: Integration tests and E2E tests serve different purposes; integration tests verify component interactions while E2E tests simulate full user workflows. They are complementary, not interchangeable.
  - Why D is incorrect: Integration tests run slower than unit tests because they involve real dependencies (databases, APIs, file systems) rather than isolated, in-memory logic.

---

### Question 14 (5 points)

A Scrum team's pipeline takes 45 minutes to run. The Product Owner proposes: "We should only run the full pipeline on the last day of the Sprint to save time." What is the primary risk of this approach?

- A) The pipeline will take longer on the last day because more code changes will be batched together
- B) Defects introduced early in the Sprint will not be discovered until Sprint end, when the context is lost and fixing them consumes the Sprint Review buffer
- C) Running the pipeline less frequently will cause the static analysis stage to produce more warnings
- D) The canary deployment will not function correctly with infrequent pipeline runs

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: While batching more changes can slow a pipeline, the primary risk described is about defect discovery timing, not pipeline duration.
  - Why C is incorrect: Static analysis warning counts are not affected by pipeline run frequency; they reflect code quality at the time of each run.
  - Why D is incorrect: Canary deployment is a production release strategy unrelated to how often the CI pipeline runs during development.

---

### Question 15 (5 points)

In DevOps culture, what does "shift left" mean in the context of quality assurance?

- A) Moving the QA team from the right side of the org chart to a position reporting to the development lead
- B) Performing quality checks earlier in the development process — during development rather than after code is complete — so defects are found when they are cheapest to fix
- C) Shifting all test writing responsibility from developers to a dedicated QA engineer
- D) Deploying to production earlier in the Sprint to collect real user feedback sooner

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: "Shift left" is a metaphor about where in the timeline quality activities occur, not about organizational reporting structures.
  - Why C is incorrect: Shifting left means developers take more quality responsibility — writing tests earlier — not delegating test writing to a separate role.
  - Why D is incorrect: Early production deployment is a release strategy decision, not what the "shift left" principle describes.

---

### Question 16 (5 points)

A Scrum team adopts Continuous Deployment and finds that every code push automatically deploys to production. Two weeks later, the Product Owner complains: "I showed a stakeholder a feature yesterday but today it looks completely different." What process gap does this reveal?

- A) The team's pipeline does not include a static analysis stage
- B) Continuous Deployment does not include a human release decision, so the Product Owner must be informed of production changes through another mechanism such as deployment notifications or feature flags
- C) The team needs to switch to Continuous Delivery to prevent unauthorized deployments
- D) The Scrum Guide prohibits Continuous Deployment because it bypasses the Sprint Review

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Static analysis checks code quality patterns; it has no connection to the Product Owner's awareness of production changes.
  - Why C is incorrect: Switching to Continuous Delivery is one option, but the scenario reveals a communication gap, not necessarily that Continuous Deployment is wrong for this team. Feature flags and deployment notifications are also valid solutions.
  - Why D is incorrect: The Scrum Guide does not address Continuous Deployment or prescribe any particular release model.

---

### Question 17 (5 points)

Which of the following is the most significant advantage of canary deployment over blue-green deployment for a team releasing a machine learning model update?

- A) Canary deployment eliminates the need for a staging environment
- B) Canary deployment allows the team to measure model accuracy against real user behavior on a small population before exposing all users to potential prediction errors
- C) Canary deployment is cheaper because it requires only one production environment
- D) Canary deployment provides a faster rollback than blue-green because fewer users are affected

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Canary deployment does not eliminate staging; both strategies use staging environments for pre-production verification.
  - Why C is incorrect: Canary deployment requires running two software versions simultaneously on the same infrastructure, which adds operational complexity; it is not necessarily cheaper than blue-green.
  - Why D is incorrect: Blue-green provides the fastest rollback — a single router switch returns all traffic to the previous environment. Canary rollback is faster to decide but still requires routing changes and monitoring to confirm stability.

---

### Question 18 (5 points)

A team's CI pipeline runs successfully but the deployment to staging fails because of a missing environment variable. The Scrum Master says: "The pipeline is green — this story is done." Is this correct?

- A) Yes — if the pipeline passes all test stages, the story meets the Definition of Done regardless of staging deployment
- B) No — if the team's Definition of Done includes "deployed to staging," a staging deployment failure means the story is not done despite passing pipeline tests
- C) Yes — environment configuration is an operations concern, not a development concern, so it does not affect story completeness
- D) No — the Scrum Guide requires all stories to be deployed to production before being marked done

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Definition of Done defines what "done" means — if staging deployment is a criterion, passing pipeline tests alone is insufficient.
  - Why C is incorrect: In DevOps culture, environment configuration is the development team's responsibility. The separation of dev and ops concerns is the anti-pattern DevOps addresses.
  - Why D is incorrect: The Scrum Guide does not require production deployment as part of done. The DoD is defined by the Scrum Team and may or may not include production deployment.

---

### Question 19 (5 points)

Which Lean waste category does the practice of running CI with daily integrations most directly reduce?

- A) Extra features — by preventing developers from building unnecessary functionality
- B) Defects — by detecting regressions immediately after the code change that introduced them, when they are cheapest to fix
- C) Task switching — by limiting developers to one integration per day
- D) Relearning — by documenting each integration in the pipeline run history

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: CI does not constrain feature scope; it verifies code quality. Preventing extra features is the responsibility of backlog management and the Product Owner.
  - Why C is incorrect: Daily integration does not limit task switching; developers can still multitask. CI addresses defect detection timing, not developer work habits.
  - Why D is incorrect: Pipeline run history is a transparency artifact, but the primary waste category CI targets is defects — bugs found late that require expensive rework.

---

### Question 20 (5 points)

A Scrum team has a CI pipeline but no deployment automation — they deploy manually to production by copying files via FTP after each Sprint. Which DevOps practice would most directly improve this?

- A) Adding more unit tests to the pipeline to catch additional defects before manual deployment
- B) Implementing Continuous Delivery so that every successful pipeline run automatically deploys to a staging environment, reducing manual steps and the risk of human error during deployment
- C) Switching from Scrum to Kanban to enable more frequent deployment windows
- D) Asking the operations team to take over the manual deployment process to free up developer time

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: More unit tests improve defect detection but do not address the manual deployment risk or inefficiency — the problem is the deployment process, not test coverage.
  - Why C is incorrect: The delivery method (Scrum vs. Kanban) does not determine whether deployments are automated; automated deployment is an engineering practice, not a framework choice.
  - Why D is incorrect: Delegating manual deployment to a separate operations team is the pre-DevOps model that DevOps was designed to replace; it increases handoff waste rather than eliminating it.

---
