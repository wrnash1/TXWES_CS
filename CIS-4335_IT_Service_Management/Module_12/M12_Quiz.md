# Quiz: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

An organization is deploying a new customer-facing web portal. The deployment team plans to route 3% of production traffic to the new version while 97% continues to use the current version. Monitoring will track error rates and response times for 48 hours before expanding the rollout. Which deployment strategy is described?

A. Big bang deployment

B. Blue/green deployment

C. Canary deployment

D. Phased deployment

**Correct Answer: C**

**Distractor Analysis:**

- **A (Big bang)** is wrong because big bang replaces all users simultaneously — there is no controlled small-percentage routing.
- **B (Blue/green)** is wrong because blue/green switches 100% of traffic between two environments at once. It does not route a small percentage.
- **C (Canary)** is correct. The defining characteristic is routing a small percentage of real production traffic to the new version to detect issues before full rollout. The 3% figure and monitoring window are classic canary pattern elements.
- **D (Phased)** is the most tempting distractor. Phased deployment also rolls out incrementally but is typically organized by user group, geography, or department — not by a live traffic percentage split on the same infrastructure.

---

**Question 2**

Which document provides step-by-step deployment procedures, rollback instructions, validation criteria, and support contacts for a specific release?

A. Service Level Agreement

B. Release notes

C. Change advisory board minutes

D. Service catalog entry

**Correct Answer: B**

**Distractor Analysis:**

- **A (SLA)** is wrong. An SLA defines the agreed service level targets between provider and customer — it does not contain deployment procedures.
- **B (Release notes)** is correct. Release notes are the primary release artifact combining scope description, technical steps, validation tests, rollback instructions, and contact information.
- **C (CAB minutes)** is wrong. CAB minutes record the change authorization discussion and decision — they reference the release but do not contain deployment procedures.
- **D (Service catalog)** is wrong. The service catalog describes services available to users — not how to deploy them.

---

**Question 3**

A large bank must migrate its core banking database to a new schema. The migration is irreversible once begun, and two versions of the application cannot coexist against different schema versions. Which deployment strategy is most appropriate?

A. Canary deployment

B. Phased deployment by region

C. Big bang deployment during a maintenance window

D. Feature flag deployment

**Correct Answer: C**

**Distractor Analysis:**

- **A (Canary)** is wrong. Canary requires two versions to run simultaneously against the same infrastructure. If the schema change is irreversible and version-incompatible, canary is not viable.
- **B (Phased by region)** is wrong for the same reason — regional phases would require different application versions against different database schemas, which the scenario explicitly excludes.
- **C (Big bang)** is correct. When a simultaneous cutover is required by technical constraints (irreversible migration, single schema), big bang during a controlled maintenance window is the appropriate choice.
- **D (Feature flag)** is wrong. Feature flags control visibility of application features at the code level — they do not help with database schema incompatibility between versions.

---

**Question 4**

In ITIL 4, what is the primary distinction between a "release" and a "deployment"?

A. A release is authorized by the Change Advisory Board; a deployment is authorized by the Release Manager.

B. A release is a logical bundle of changes that has been tested and approved; a deployment is the act of placing that release into a specific environment.

C. A release applies only to software; a deployment applies to both software and hardware.

D. A release is created by developers; a deployment is created by operations teams.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Both release and deployment records can involve CAB or Change Manager authorization depending on the organization's process. The distinction is not about who authorizes but about what the artifact represents.
- **B** is correct. ITIL 4 defines the release as the logical package (what is being moved) and deployment as the act (how and when it moves to an environment). The same release may result in multiple deployments.
- **C** is wrong. Both releases and deployments can encompass hardware, software, configurations, and documentation — ITIL 4 does not restrict either term to a single domain.
- **D** is wrong. Release management and deployment management both involve both development and operations teams. The distinction is not about team ownership.

---

**Question 5**

Which DORA metric measures the percentage of deployments that cause a degradation in service requiring remediation?

A. Deployment frequency

B. Lead time for changes

C. Change failure rate

D. Mean time to restore

**Correct Answer: C**

**Distractor Analysis:**

- **A (Deployment frequency)** measures how often deployments occur — a volume metric, not a quality metric.
- **B (Lead time for changes)** measures the elapsed time from code commit to production deployment — a speed metric.
- **C (Change failure rate)** is correct. It directly measures deployment quality — what percentage of changes required rollback, hotfix, or other remediation.
- **D (Mean time to restore)** measures how quickly service is restored after a failure — a recovery metric. It is related but measures response, not the rate of failures.

---

**Question 6**

What is the primary purpose of a post-implementation review (PIR) in Release and Deployment Management?

A. To re-authorize changes that were deployed without Change Advisory Board approval.

B. To evaluate whether the release achieved its objectives and to capture lessons learned for continuous improvement.

C. To assign blame for any incidents caused by the deployment.

D. To update the service catalog with new features delivered by the release.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. PIRs do not re-authorize changes after the fact. Unauthorized changes would be handled through the Change Enablement process.
- **B** is correct. The PIR is a structured retrospective focused on whether outcomes matched intentions and what improvements should be captured. It feeds the Continual Improvement practice.
- **C** is wrong. A well-conducted PIR is blameless — focused on systemic improvement, not individual fault-finding. This is aligned with both ITIL values and modern DevOps culture.
- **D** is wrong. While service catalog updates may result from a release, updating the catalog is not the purpose of the PIR.

---

**Question 7**

An organization has implemented a CI/CD pipeline where every code change that passes automated testing is automatically deployed to production without a manual approval gate. Which term describes this practice?

A. Continuous Integration

B. Continuous Delivery

C. Continuous Deployment

D. Infrastructure as Code

**Correct Answer: C**

**Distractor Analysis:**

- **A (CI)** is wrong. Continuous Integration means merging code frequently and running automated tests — it does not include automated production deployment.
- **B (Continuous Delivery)** is the most common distractor. Continuous Delivery means every passing build is *ready* for production deployment, but a human must still approve the production push. The question states no manual gate — so Delivery does not apply.
- **C (Continuous Deployment)** is correct. When approved builds are automatically deployed to production without manual intervention, that is Continuous Deployment.
- **D (IaC)** is wrong. Infrastructure as Code defines infrastructure in code files — it is an enabling practice for automation but does not describe the deployment trigger model.

---

**Question 8**

A company maintains two identical production environments. The new version is deployed to Environment B and tested while Environment A serves all live traffic. When testing is complete, the router switches 100% of traffic to Environment B. What deployment strategy is this?

A. Canary deployment

B. Blue/green deployment

C. Phased deployment

D. Rolling deployment

**Correct Answer: B**

**Distractor Analysis:**

- **A (Canary)** is wrong. Canary splits live traffic by percentage — the environments are not two full parallel setups, and traffic is not switched 100% at once.
- **B (Blue/green)** is correct. Two full, parallel environments where traffic is switched completely from one to the other is the defining characteristic of blue/green deployment.
- **C (Phased)** is wrong. Phased deployment gradually expands user groups — it does not involve two parallel full production environments with a traffic switch.
- **D (Rolling)** is wrong. A rolling deployment replaces instances one at a time in the same environment — not across two full parallel environments.

---

**Question 9**

Which ITIL 4 Service Value Chain activity is most directly associated with Release and Deployment Management?

A. Plan

B. Engage

C. Deploy and Transition

D. Improve

**Correct Answer: C**

**Distractor Analysis:**

- **A (Plan)** contributes to release planning activities but is not the primary activity associated with this practice.
- **B (Engage)** involves interaction with stakeholders about needs and requirements — not the act of releasing.
- **C (Deploy and Transition)** is correct. ITIL 4 explicitly identifies Deploy and Transition as the Service Value Chain activity where Release and Deployment Management makes its primary contribution.
- **D (Improve)** is relevant to post-implementation review output but is not the primary activity of the practice itself.

---

**Question 10**

During a go/no-go review, the deployment team discovers that two regression test cases were skipped due to a test environment issue. The tests were last run successfully 10 days ago. The maintenance window opens in 15 minutes. What is the most appropriate action aligned with ITIL 4 principles?

A. Proceed — the tests passed 10 days ago, which is sufficient evidence.

B. Cancel the deployment — any skipped tests require a full re-run before proceeding.

C. Conduct a risk assessment: evaluate what the tests cover, how critical those areas are to this release, and decide whether to proceed, hold, or proceed with heightened post-deployment monitoring.

D. Remove the skipped tests from the test suite so they do not block future deployments.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is wrong. Ten days is a meaningful gap given that changes have occurred since those tests ran. Automatically proceeding without assessing the risk is inconsistent with ITIL principles of risk management.
- **B** is wrong. Requiring perfect test completion in all circumstances is overly rigid and ignores context — particularly the regulatory deadline in such scenarios. ITIL 4 values pragmatic judgment.
- **C** is correct. ITIL 4's guiding principles of "think and work holistically" and "progress iteratively with feedback" support a risk-based decision. The manager should assess test coverage relevance, apply judgment, and potentially proceed with enhanced monitoring — not blindly cancel or blindly proceed.
- **D** is wrong. Removing tests to avoid failures is a dangerous anti-pattern that reduces quality assurance coverage over time.

---

*End of Module 12 Quiz — 10 questions with distractor analysis*
