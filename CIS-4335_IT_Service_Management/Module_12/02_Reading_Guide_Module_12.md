# Reading Guide: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

Release and Deployment Management is the ITIL 4 practice responsible for making new and changed services and features available for use. It sits at one of the most consequential transition points in any IT organization — the boundary between development and production. Understanding this practice means understanding not just the mechanics of deploying software, but the planning, risk management, communication, and review disciplines that determine whether deployments succeed.

Use this guide alongside the Module 12 video lecture and ITIL 4 Foundation study resources.

---

## Purpose of Release and Deployment Management

ITIL 4 defines the purpose of Release and Deployment Management as:

> To make new and changed services and features available for use.

Three aspects of this purpose deserve careful attention.

**"New and changed"** — The practice covers both entirely new services being launched for the first time and modifications to existing services. Both carry risk. New services risk poor user adoption or undetected design flaws. Changed services risk breaking established functionality that users depend on.

**"Services and features"** — The practice is not limited to application code. A release may include infrastructure changes, configuration changes, documentation updates, or access permission changes. Any change that makes a new or modified capability available to users falls within scope.

**"Available for use"** — The goal is not deployment itself but usability. A deployment that is technically complete but leaves users unable to access the new functionality has not met the purpose of this practice.

---

## Release Planning

A release is a version of a service or service component that is made available for use. Release planning is the process of deciding what will be included in a release, how it will be deployed, who will approve and execute it, and what success criteria will determine whether the release has achieved its goals.

### Release Contents

Releases typically bundle multiple related changes together. The rationale for bundling is efficiency — deploying multiple changes at once is often less disruptive than deploying them separately. However, bundling increases complexity. A problem after a bundled release is harder to diagnose because multiple changes are potential sources.

### Release Versioning

A version control scheme helps all parties understand the history of a release. Common schemes include semantic versioning (major.minor.patch) and date-based versioning. The CMDB should record the version of every deployed configuration item so that the current state of the production environment is always known.

### Approval and Authorization

Before a release reaches production, it must pass through an approval process. In ITIL 4, this connects to Change Management — most releases require change authorization. The approval process validates that the release has been tested, that the deployment plan is sound, and that a rollback plan exists.

---

## Deployment Approaches

The choice of deployment approach is one of the most significant decisions in release planning. Each approach carries different risk, speed, and complexity trade-offs.

### Big Bang Deployment

| Attribute | Detail |
|---|---|
| Description | Full release deployed to all users and environments simultaneously |
| Risk | Highest — all users affected by any problem |
| Complexity | Lowest — no parallel version management required |
| Rollback | Complex and time-consuming |
| Best for | Small, low-risk changes; organizations without parallel environment capability |

A big bang deployment replaces the old version entirely in a single operation. The advantage is simplicity. The disadvantage is exposure: if something goes wrong, there is no unaffected user population, and rollback requires reversing the entire deployment.

### Phased Deployment

| Attribute | Detail |
|---|---|
| Description | Staged rollout to successive user groups or regions |
| Risk | Contained per phase — problems affect only the current phase population |
| Complexity | Medium — version management across phases required |
| Rollback | Affects only current phase population |
| Best for | Large user bases; geographically distributed services |

Phased deployment reduces risk by limiting exposure at each stage. The organization learns from each phase and can address problems before expanding the rollout. The challenge is managing the period when different user populations are on different versions — this creates support complexity and may cause compatibility problems.

### Canary Deployment

| Attribute | Detail |
|---|---|
| Description | Small percentage of production traffic routed to new version |
| Risk | Minimal — tiny initial exposure in production |
| Complexity | High — traffic routing infrastructure required |
| Rollback | Fast — redirect canary traffic back to stable version |
| Best for | High-traffic services; performance-sensitive applications |

The canary approach uses real production traffic as its validation signal. Automated monitoring watches the canary population for anomalies — elevated error rates, increased latency, business metric drops. If anomalies are detected, the canary is rolled back. If healthy, the percentage is increased. This gives the organization a production-validated signal rather than a test environment approximation.

### Blue-Green Deployment

| Attribute | Detail |
|---|---|
| Description | Two identical production environments with traffic switched via load balancer |
| Risk | Minimal — traffic can be instantly redirected to prior environment |
| Complexity | High — duplicate infrastructure cost; database synchronization challenge |
| Rollback | Near-instantaneous — DNS or load balancer switch |
| Best for | High-availability applications; cloud environments |

Blue-green deployments decouple the deployment act from the traffic switch. The new version can be fully deployed, tested, and validated in the inactive environment before any user is affected. The cutover is the single high-stakes moment, and even that can be reversed in seconds.

---

## Deployment Automation

### The Deployment Pipeline

A deployment pipeline automates the sequence of steps required to move a change from source code to production. A well-designed pipeline includes:

1. Source code commit triggers the pipeline
2. Automated build compiles and packages the release
3. Automated tests (unit, integration, regression) validate functionality
4. Deployment to staging environment for final validation
5. Approval gate for human authorization to proceed to production
6. Automated production deployment
7. Post-deployment smoke tests verify production health

The pipeline enforces consistency. Every release travels through the same stages in the same sequence. Manual steps introduce variation; automation eliminates it.

### Infrastructure as Code

Infrastructure as Code (IaC) treats environment configuration as version-controlled code. Tools like Terraform, Ansible, and Chef provision and configure servers, networks, and cloud resources from code definitions. IaC ensures that the test environment matches the production environment — a common source of deployment failures when environments diverge.

### The ITIL 4 "Optimize and Automate" Guiding Principle

The ITIL 4 guiding principle "Optimize and Automate" specifically supports deployment automation. The principle advises organizations to first optimize a process — eliminating unnecessary steps, removing waste — and then automate what remains. Automating a broken process makes it fail faster and more consistently. Automation's value is realized only when the underlying process is sound.

---

## Release Notes

Release notes are the communication artifact that accompanies every release. They serve multiple audiences simultaneously.

### For End Users

End users need to know: What has changed in the service I use? Are there new features I should be aware of? Are there known limitations in this version?

### For Operations and Support Staff

Operations staff need to know: What was deployed and when? What configuration items changed? What dependencies were modified? What do I do if something breaks?

### For the Change and Release Record

The release notes form part of the change record — the documentation that enables any future investigation to understand exactly what was deployed to production and when. Accurate release notes are essential for incident investigation and problem management.

### Release Notes Contents

A complete release note document includes:

- Release version and date
- Summary of changes included (features, fixes, configuration changes)
- Known issues and limitations
- Prerequisites and dependencies
- Manual steps required before, during, or after deployment
- Rollback instructions
- Post-deployment verification steps
- Support contact information

---

## Rollback Planning

A rollback plan is a documented procedure for returning a service to its previous state when a deployment fails or causes unacceptable problems. The rollback plan is not optional — it is a required component of any deployment plan.

### Rollback Triggers

The rollback plan must define the conditions that trigger a rollback decision. Common triggers include:

- Error rates exceeding a defined threshold in post-deployment monitoring
- Critical incidents reported within a defined window after deployment
- Failed post-deployment smoke tests
- Business metric drops that cannot be explained by other factors

### Rollback Complexity

Not all rollbacks are equal in complexity.

**Application code rollbacks** are generally straightforward — redeploy the previous version of the application package.

**Configuration rollbacks** require restoring the previous configuration state — possible if configuration is managed in version control.

**Database schema rollbacks** are the most complex. When a new release adds or alters database tables, columns, or constraints, reversing those schema changes while preserving data integrity requires careful scripting. Some schema changes — like deleting a column — cannot be reversed without data loss. Forward-only migrations should be planned with this in mind.

**Infrastructure rollbacks** in cloud environments may involve restoring previous IaC state — possible but requiring automation to execute quickly under pressure.

---

## Post-Implementation Review

A post-implementation review (PIR) is a structured evaluation conducted after a release has reached production and stabilized. The PIR typically occurs one to two weeks after deployment, once any immediate post-deployment incidents have been resolved.

### PIR Objectives

- Assess whether the release achieved its intended outcomes
- Identify any incidents caused by the release
- Evaluate the quality of the deployment plan and release notes
- Validate that the rollback plan was viable and accurate
- Capture lessons learned for future releases

### PIR Outputs

The PIR produces a written record that includes findings and recommendations. These recommendations become inputs to the Continual Improvement Register — ITIL 4's mechanism for tracking and prioritizing improvement actions. Problems identified in a PIR may also trigger formal Problem Management investigations if root causes have not been identified.

### PIR and the Service Value Chain

The PIR closes the loop between deployment activity and organizational learning. Without it, organizations repeat the same mistakes across release after release. With it, each release makes the next release slightly more reliable.

---

## Key Terms for the ITIL 4 Foundation Exam

| Term | Definition |
|---|---|
| Release | A version of a service or service component made available for use |
| Deployment | The activity of moving a release to an environment |
| Big bang deployment | Simultaneous full rollout to all users or environments |
| Phased deployment | Staged rollout to successive user groups or regions |
| Canary deployment | Small percentage of production traffic routed to new version |
| Blue-green deployment | Two identical production environments with traffic switch |
| Release notes | Documentation accompanying a release for multiple audiences |
| Rollback | Returning a service to its previous state after a failed deployment |
| Post-implementation review | Structured evaluation after a release reaches production |
| Deployment pipeline | Automated sequence of steps from code commit to production |

---

## Study Questions

Answer these questions in your own words to verify comprehension before attempting the Module 12 quiz.

1. What is the stated purpose of Release and Deployment Management in ITIL 4?

2. What distinguishes a canary deployment from a phased deployment?

3. Why are database schema changes treated as the most complex aspect of rollback planning?

4. What are the three audiences served by release notes, and what does each audience need to know?

5. What is the relationship between the PIR and Continual Improvement in ITIL 4?

6. A company is deploying a critical e-commerce platform update on a major sales day. They need near-instantaneous rollback capability if problems occur. Which deployment approach is most appropriate and why?

7. What does the ITIL 4 guiding principle "Optimize and Automate" say about the sequence of optimization and automation?
