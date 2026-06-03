# Video Script: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation
**Estimated Duration:** 22–25 minutes
**Recorded by:** Professor Nash

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.
- [PAUSE] cues indicate natural break points for student note-taking.

---

## Section 1: Welcome and Module Overview [00:00 - 02:30]

Welcome to Module 12. I am Professor Nash. Today we are covering Release and Deployment Management — one of the most operationally visible practices in the ITIL 4 framework. If you have ever wondered how software updates reach production without breaking everything, or how enterprises roll back a failed change at 2 AM, this module answers those questions.

[SHOW DIAGRAM: Title slide — "Module 12: Release and Deployment Management" with ITIL 4 SVS label and ITIL 4 Foundation certification badge]

Release and Deployment Management is defined in ITIL 4 as the practice that makes new and changed services and features available for use. It is the hand-off point between development and operations — the place where tested, approved changes become real services that real users depend on.

By the end of this module you will be able to: define the purpose of Release and Deployment Management, distinguish the four major deployment approaches, explain rollback planning and post-implementation review, and connect this practice to the ITIL 4 Service Value Chain.

---

## Section 2: Purpose and Scope [02:30 - 06:00]

[SHOW DIAGRAM: ITIL 4 Service Value Chain with "Obtain/Build" and "Deliver and Support" stages highlighted, with Release Management bridging the two]

ITIL 4 defines the purpose of Release and Deployment Management as:

> To make new and changed services and features available for use.

That sounds simple. But embedded in it are several important responsibilities.

First: release planning. A release is a version of a service or service component that is made available for use. Not every change is a release — a hotfix applied to a single server may be a change, not a formal release. A release typically bundles multiple related changes together. Planning a release means defining what is included, who approves it, what the deployment sequence is, and what success looks like.

[PAUSE]

Second: deployment. Deployment is the activity of making a release available in an environment. Environments matter here. You might deploy a release to a test environment, then a staging environment, then production. Each environment serves a different purpose and carries different stakes.

Third: communication. Releases must be accompanied by release notes — documentation that tells the people operating and using the service what has changed, what the impact is, and what to do if something goes wrong.

---

## Section 3: Deployment Approaches [06:00 - 14:00]

This is the most tested section of Release and Deployment Management on the ITIL 4 Foundation exam. There are four primary deployment approaches, and you need to be able to distinguish them.

[SHOW DIAGRAM: Four-panel comparison grid — Big Bang, Phased, Canary, Blue-Green — each with a simple flow diagram showing how traffic or users transition to the new release]

### Big Bang Deployment

In a big bang deployment, the new release is deployed to all users or all environments simultaneously. The old version is replaced in a single operation. This approach is simple and avoids the complexity of running two versions in parallel, but it carries the highest risk. If something goes wrong, everyone is affected immediately. Big bang deployments are appropriate for small, low-risk changes, or for organizations with limited infrastructure to support parallel environments.

[PAUSE]

### Phased Deployment

In a phased deployment, the release is rolled out incrementally — first to one region, then another; first to one user group, then the next. Each phase validates the release in a real environment before expanding the rollout. Risk is contained because a problem in phase one affects only the phase one population. Phased deployments require careful planning to manage the period when different users are on different versions — version incompatibility and split support can become challenges.

### Canary Deployment

A canary deployment routes a small percentage of real production traffic to the new release — perhaps 1%, 5%, or 10%. The rest of the traffic continues to use the old version. Operations teams monitor error rates, latency, and business metrics on the canary population. If the new version performs well, the percentage is gradually increased until the full rollout is complete. If problems appear, the canary population is redirected back to the old version with minimal overall impact.

The name comes from the historical practice of sending canaries into coal mines — the canary's sensitivity to toxic gases gave miners early warning before conditions became dangerous. The canary release population provides the same early warning in production.

[PAUSE]

### Blue-Green Deployment

In a blue-green deployment, two identical production environments — called blue and green — are maintained simultaneously. At any time, one environment (say, blue) is live and serving all traffic. When a new release is ready, it is deployed to the inactive environment (green). Once testing confirms the green environment is healthy, a load balancer or DNS cutover switches all traffic from blue to green in a single, near-instantaneous operation. If problems are detected, the same switch redirects traffic back to blue — a rollback that takes seconds rather than hours.

Blue-green deployments are resource-intensive because you maintain two full production environments. But the rollback speed they enable is unmatched. They are widely used in high-availability cloud environments.

[SHOW DIAGRAM: Blue-Green architecture diagram — two environment boxes (Blue: v1.0, Green: v1.1), load balancer on top, arrows showing traffic flowing to Blue, then cutover arrow to Green, then rollback arrow back to Blue]

---

## Section 4: Deployment Automation and Pipeline [14:00 - 17:30]

Modern release and deployment practices depend heavily on automation. Deployment automation reduces human error, increases deployment speed, and enables consistent repeatable processes across environments.

[SHOW DIAGRAM: CI/CD pipeline — Code Commit → Build → Automated Tests → Staging Deploy → Approval Gate → Production Deploy → Post-Deploy Verification]

A deployment pipeline is a sequence of automated stages that moves a change from source code to production. In the context of ITIL 4, the pipeline is where deployment automation lives. Key stages include: automated build, automated testing, staged deployment, approval gates, production deployment, and post-deployment verification.

Deployment automation tools — such as Jenkins, GitHub Actions, Azure DevOps, or GitLab CI — execute the pipeline steps. Infrastructure as Code tools — such as Terraform and Ansible — ensure environments are provisioned consistently. Container orchestration platforms — such as Kubernetes — enable blue-green and canary deployments at scale.

[PAUSE]

The ITIL 4 principle of "Optimize and Automate" applies directly here. Manual deployment processes are slow, error-prone, and inconsistent. Automating the repeatable parts of deployment frees IT staff to focus on judgment-intensive work like release approvals and post-implementation analysis.

---

## Section 5: Release Notes and Rollback Planning [17:30 - 20:00]

### Release Notes

Release notes are documentation that accompanies a release. Good release notes serve multiple audiences: end users who need to know what changed in the service they use, operations staff who need to know what was deployed and what dependencies changed, and the change advisory process that needs a record of what was released and when.

A complete set of release notes includes: the release version and date, a summary of changes included, any known issues or limitations, instructions for any manual steps required, rollback instructions, and contact information for support.

[PAUSE]

### Rollback Planning

Every deployment plan must include a rollback plan. A rollback is the process of returning a service to its previous state when a deployment fails or causes problems. The rollback plan answers three questions: How will we detect that a rollback is needed? How will we execute the rollback? How long will rollback take?

Blue-green deployments make rollback near-instant. Big bang deployments may require complex data migration reversals. For database schema changes, rollback can be the most complex part of the entire deployment — schemas are harder to reverse than application code. This is why database migrations require special attention in release planning.

---

## Section 6: Post-Implementation Review [20:00 - 22:00]

A post-implementation review (PIR) is a structured evaluation conducted after a release has been deployed to production. Its purpose is to assess whether the release achieved its intended outcomes, identify any problems that occurred during or after deployment, and capture lessons learned.

A PIR typically examines: Did the deployment go as planned? Were any incidents caused by the release? Were the release notes accurate and complete? Was the rollback plan tested and viable? What would we do differently next time?

The PIR feeds directly into Continual Improvement. Problems found during PIR become inputs to change management, problem management, and future release planning. Without the PIR step, organizations repeat the same deployment mistakes across every release.

[SHOW DIAGRAM: Improvement cycle — Release → PIR → Lessons Learned → Release Process Improvement → Next Release]

---

## Section 7: Exam Reminders and Lab Preview [22:00 - End]

Three key exam reminders. First: Know the four deployment approaches and their trade-offs — big bang, phased, canary, blue-green. Second: Understand that rollback planning is mandatory, not optional. Third: The PIR is the connection between individual releases and organizational learning.

This week's lab puts you in the role of a release manager planning a production deployment for a fictional healthcare IT system. You will select a deployment approach, draft release notes, write a rollback plan, and complete a post-implementation review template.

---

## Module 12 Complete

Next: Module 13 — IT Asset Management

### Additional Resources

- axelos.com — ITIL 4 Foundation study materials and practice exams
- itil4.axelos.com — ITIL 4 SVS and practice reference sheets
- martinfowler.com — Deployment pipeline patterns and blue-green deployment overview
