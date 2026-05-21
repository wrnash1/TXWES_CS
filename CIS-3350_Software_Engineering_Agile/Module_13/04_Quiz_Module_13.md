# Quiz: Module 13 – Continuous Integration and DevOps Basics

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

What is the primary goal of Continuous Integration (CI)?

* A) To automatically deploy every code change to production servers without human approval
* B) To automatically build and test code changes each time a developer commits, detecting integration failures early
* C) To replace the Sprint Review by providing automated stakeholder notifications of completed features
* D) To generate project status reports for management by analyzing commit frequency

Correct Answer: B) CI automatically verifies new changes by triggering build and test pipelines on each commit, catching failures while they are small and easy to fix.

Distractor Analysis:

* *Why B is correct:* Martin Fowler's definition of CI centers on frequent integration to a shared mainline with automated verification — reducing the cost and risk of merging divergent code branches.
* *Why A is incorrect:* Automatically deploying to production without human approval is Continuous Deployment — a separate, more advanced practice that builds on top of CI.
* *Why C is incorrect:* CI has no direct relationship to the Sprint Review. Sprint Review is a Scrum event for stakeholder inspection of the Increment; CI is a technical engineering practice.
* *Why D is incorrect:* CI is a quality and integration practice, not a management reporting tool. Commit frequency analysis is an observability metric, not CI's primary purpose.

---

### Question 2

Which of the following best describes the difference between Continuous Delivery and Continuous Deployment?

* A) Continuous Delivery requires manual testing; Continuous Deployment uses automated testing only.
* B) In Continuous Delivery, the software is always in a deployable state but production release requires a manual decision; in Continuous Deployment, every passing build is automatically released to production.
* C) Continuous Deployment applies only to mobile apps; Continuous Delivery applies to web services.
* D) Continuous Delivery deploys to production; Continuous Deployment deploys only to staging environments.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* The key distinction is the final step: Continuous Delivery means the release decision is made by a human; Continuous Deployment means the release is fully automated when all pipeline stages pass.
* *Why A is incorrect:* Both practices rely on automated testing. The difference is in the production deployment trigger, not the testing method.
* *Why C is incorrect:* Both practices apply to any software type — web, mobile, APIs, or embedded systems. The distinction is about deployment automation, not application type.
* *Why D is incorrect:* This reverses the definitions. Continuous Delivery keeps software staging-ready with human-controlled production release; Continuous Deployment automates the production release.

---

### Question 3

A Scrum Team's Definition of Done includes: "All automated unit and integration tests pass" and "Code is merged to the main branch." Which practice most directly enforces these two conditions for every code change?

* A) Sprint Retrospective — where the team reviews whether tests were run
* B) Continuous Integration — where automated pipelines verify build and test status on every commit
* C) Sprint Review — where stakeholders manually verify that tests have been run
* D) Product Backlog refinement — where the Product Owner confirms test coverage before items are selected

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* CI pipelines run automatically on every commit and block merges to the main branch if tests fail — making DoD verification objective and continuous rather than manual and end-of-Sprint.
* *Why A is incorrect:* The Sprint Retrospective is a process reflection event; it cannot enforce technical standards on individual commits.
* *Why C is incorrect:* Sprint Reviews inspect the product Increment with stakeholders. Stakeholders do not verify CI pipeline results — that is an automated technical process.
* *Why D is incorrect:* Backlog refinement prepares items for selection; the Product Owner does not verify test coverage on individual commits.

---

### Question 4

A development team commits code to a feature branch for three weeks, merging to the main branch only at Sprint end. They then spend two days resolving merge conflicts and test failures. What practice would most directly prevent this problem?

* A) Extending the Sprint to five weeks to allow more time for integration
* B) Having the Scrum Master review and approve all commits before they are merged
* C) Practicing Continuous Integration by committing to the shared main branch multiple times per day and running automated tests on each commit
* D) Asking the Product Owner to reduce the number of stories in each Sprint to reduce merge complexity

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* The described problem is "big batch integration" — the longer branches diverge, the more conflicts accumulate. CI requires frequent integration (multiple times daily) to keep branches short-lived and conflicts small.
* *Why A is incorrect:* A longer Sprint simply delays the same large merge problem — it does not eliminate it.
* *Why B is incorrect:* The Scrum Master does not approve code commits. Adding a human gate to every commit slows delivery and does not address the root cause of infrequent integration.
* *Why D is incorrect:* Reducing Sprint scope does not address the integration frequency problem. Fewer stories but still merged once at Sprint end produces the same three-week divergence issue.

---

### Question 5

A Scrum Team wants to improve their DevOps maturity. They currently deploy manually to production twice a year. Which sequence best describes the incremental path toward Continuous Deployment?

* A) Skip directly to Continuous Deployment to maximize automation benefits immediately.
* B) Establish CI (automated build and test on commit) first, then Continuous Delivery (always deployable to staging), then Continuous Deployment (automatic production release).
* C) Implement Continuous Deployment first, then add automated testing to the pipeline retroactively.
* D) Replace Scrum Sprint Reviews with automated deployment notifications, then automate testing.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* CI/CD maturity is built incrementally. Without CI (reliable automated tests on every commit), Continuous Delivery is fragile. Without Continuous Delivery (always deployable to staging), Continuous Deployment is unsafe. Each level must be established before the next.
* *Why A is incorrect:* Skipping to Continuous Deployment without automated test coverage would deploy broken code to production automatically — a high-risk approach for teams starting from manual deployments.
* *Why C is incorrect:* Deploying to production automatically before tests are in place guarantees production incidents. Testing must precede automated production release.
* *Why D is incorrect:* Sprint Reviews are a Scrum event for stakeholder product inspection — they are not equivalent to deployment notifications. Replacing them does not establish CI/CD maturity.
