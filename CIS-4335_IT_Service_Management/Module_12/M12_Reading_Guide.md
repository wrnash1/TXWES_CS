# Reading Guide: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

This reading guide accompanies the Module 12 video lecture. Use it before watching to prime your thinking, and again afterward to consolidate key concepts. Margin notes, self-quiz responses, and highlighted vocabulary will strengthen retention for the ITIL 4 Foundation exam.

**Estimated reading and reflection time:** 90–120 minutes

---

## Learning Objectives

After completing this module, you will be able to:

1. Define Release and Deployment Management and articulate its purpose within ITIL 4.
2. Distinguish between a release and a deployment.
3. Compare big bang, phased, and canary deployment strategies.
4. Explain the components of an effective release plan and release note.
5. Describe the role of CI/CD automation in modern release management.
6. Conduct a post-implementation review using a structured framework.
7. Map Release and Deployment Management to the ITIL 4 Service Value Chain.

---

## Section 1: Foundations of Release and Deployment Management

### 1.1 Purpose and Scope

ITIL 4 defines Release and Deployment Management as the practice that "makes new or changed services and features available for use." This deceptively simple statement encompasses a broad operational domain.

The practice exists because moving changes from a controlled development environment to a live production environment is inherently risky. Production environments differ from test environments in scale, data complexity, user behavior patterns, and interconnected dependencies. Even thoroughly tested releases can behave unexpectedly when millions of real transactions flow through them.

**Reflection prompt:** Think of a software update on your phone or laptop that caused unexpected problems. What could better release management have prevented?

### 1.2 Release vs. Deployment

These two terms are often conflated but have distinct meanings in ITIL.

A **release** is a version of a service or service component that is available for deployment. It represents a logical grouping — perhaps a sprint's worth of features, a security patch bundle, or a complete new module. The release has been through development, testing, and approval before it is considered ready.

A **deployment** is the act of placing a specific release into an environment. The same release may be deployed to a staging environment first, then to a pilot group, and finally to full production. Each of those is a separate deployment event.

This distinction matters because:

- Release governance (what gets bundled and approved) is separate from deployment execution (how and when it lands).
- An organization might maintain multiple active release streams while conducting deployments at different frequencies.

### 1.3 Relationship to Change Enablement

Change Enablement governs whether a change is authorized. Release and Deployment Management governs how authorized changes reach production. In practice, a change request references one or more release packages. The change record provides the "permission slip"; the release record provides the "instruction manual."

---

## Section 2: Release Planning

### 2.1 Release Calendar

A release calendar is a forward-looking schedule showing planned releases across all teams, applications, and environments. Its primary value is **conflict avoidance** — ensuring that two teams do not deploy to the same shared infrastructure simultaneously, and that deployments do not land during business-critical periods such as quarter-end financial closes or peak e-commerce seasons.

**Key elements of a release calendar:**

- Target deployment date and maintenance window time.
- Environment(s) affected (staging, UAT, production).
- Owner and release manager contact.
- Change request reference number.
- Freeze periods (dates when no changes are permitted).

Most organizations also define **code freezes** — periods where only emergency or critical security patches can be released. Common freeze windows include the weeks surrounding major holidays or fiscal year-end processing.

### 2.2 Release Notes

Release notes are the formal communication artifact of a release. They bridge the technical details of what changed with the operational context of how that affects support teams, end users, and auditors.

**Standard release note sections:**

- **Release identifier:** Version number, release name, date.
- **Change request references:** Links to the authorizing change records.
- **Scope summary:** High-level description of what is new, changed, or fixed.
- **Components affected:** Specific services, servers, databases, or software versions.
- **Pre-deployment prerequisites:** Steps that must occur before deployment begins (e.g., database backups, configuration exports).
- **Deployment steps:** Step-by-step procedure with estimated durations.
- **Validation criteria:** Tests that confirm successful deployment.
- **Rollback procedure:** Steps to revert if validation fails.
- **Known issues:** Any defects or limitations in this release that will be addressed in a future release.
- **Support contacts:** Who to call if problems arise post-deployment.

Well-written release notes double as audit evidence, proving that deployments were planned and controlled.

### 2.3 Go/No-Go Review

The go/no-go review is a pre-deployment checkpoint where stakeholders confirm that all conditions for a safe deployment are met. It is not a technical test — testing was completed earlier. It is a structured human decision point.

**Typical go/no-go criteria:**

- All acceptance tests passed with no open critical defects.
- Release notes distributed to operations, help desk, and business owners.
- Rollback plan reviewed and understood by deployment team.
- Maintenance window confirmed with infrastructure and networking teams.
- On-call engineers briefed and available during and after deployment.
- Backup or snapshot of current production state completed.

If any criterion is not met, the responsible party must either resolve the gap immediately or the release is postponed.

---

## Section 3: Deployment Strategies

### 3.1 Choosing a Strategy

There is no universally superior deployment strategy. The right choice depends on:

- The nature and risk level of the change.
- The architectural characteristics of the application (monolithic vs. microservices).
- The availability requirements of the service (can it tolerate downtime?).
- The organization's rollback capabilities.
- The maturity of the team's tooling and monitoring.

Understanding the trade-offs is essential for both ITIL practitioners and the ITIL 4 Foundation exam.

### 3.2 Big Bang Deployment

In a big bang deployment, the old version is replaced by the new version in a single, simultaneous cutover for all users and all infrastructure components.

**When to use big bang:**

- The change requires a shared data migration that cannot coexist with the old schema.
- The application is monolithic and cannot be partially updated.
- The deployment window is scheduled during a period of near-zero usage.

**Risk mitigation for big bang:**

- Full regression test suite completed.
- Database backup taken immediately before cutover.
- Rollback procedure rehearsed in a staging environment.
- Extended on-call coverage for 48–72 hours post-deployment.

**Exam tip:** Big bang carries the highest simultaneous risk but the lowest operational complexity. Phased strategies spread risk over time but increase complexity.

### 3.3 Phased Deployment

Phased deployment releases the new version to a subset of users or infrastructure, then progressively expands the rollout based on monitoring results and feedback.

**Phase structure example:**

- **Phase 1 (Pilot):** 5% of users, internal staff or power users.
- **Phase 2 (Early Adopters):** 20% of users, one geographic region.
- **Phase 3 (General Availability):** 100% of users.

**API compatibility challenge:** When two versions of an application run simultaneously, APIs must support both old and new clients. This requires versioned APIs or backward-compatible changes — a significant engineering constraint.

**Database migrations** present another challenge: schema changes must be backward-compatible during the phased window, which often means a two-step migration (add new columns while old ones remain, then remove old columns after full rollout).

### 3.4 Canary Deployment

Canary deployment is a traffic-based variant of phased deployment. Rather than assigning users to old/new versions, a routing layer directs a small percentage of all requests to the new version while the remainder hit the stable version.

**Infrastructure requirements:**

- Load balancer or service mesh capable of weighted routing (e.g., Nginx, Istio, AWS ALB).
- Observability tooling to compare error rates, latency, and business KPIs across versions simultaneously.
- Feature flag or version-labeling mechanism.

**Automated rollback:** Advanced teams configure automated canary analysis — if the new version's error rate exceeds a threshold compared to the stable version, the canary is automatically retracted without human intervention. Tools like Argo Rollouts and Spinnaker support this.

**Name origin:** In 19th-century coal mining, miners carried caged canaries into tunnels. Canaries are more sensitive to carbon monoxide than humans, so a dead canary warned miners to evacuate before the toxic levels became fatal to people. In software, the "canary" — a small percentage of production traffic — is the early warning system.

### 3.5 Blue/Green Deployment (Supplemental)

Though not always covered in ITIL Foundation scope, blue/green deployment is worth knowing. Two identical production environments — "blue" (current) and "green" (new) — are maintained. After testing green, the router switches 100% of traffic from blue to green. Rollback is instant: switch traffic back to blue. The main disadvantage is the cost of maintaining two full production environments.

---

## Section 4: Deployment Automation

### 4.1 Why Automate?

Manual deployment processes have three fundamental weaknesses:

1. **Human error:** Missing a step, executing steps out of order, or misreading configuration values.
2. **Inconsistency:** Different engineers follow the same procedure slightly differently, producing different outcomes.
3. **Speed:** Manual processes are slow, which limits deployment frequency and creates pressure to batch many changes into large, risky releases.

Automation addresses all three: scripts execute identically every time, in the correct sequence, at machine speed.

### 4.2 CI/CD Pipeline Architecture

A CI/CD pipeline is an automated workflow that moves code from a developer's workstation to production through a series of validated stages:

**Stage 1 — Source Control:** Developer commits code. Pipeline is triggered.

**Stage 2 — Build:** Code is compiled, dependencies resolved, artifacts created.

**Stage 3 — Unit Tests:** Automated tests verify individual functions and components.

**Stage 4 — Integration Tests:** Tests verify that components interact correctly.

**Stage 5 — Security Scan:** Static analysis (SAST) and dependency vulnerability checks.

**Stage 6 — Deploy to Staging:** Artifact deployed to a staging environment identical to production.

**Stage 7 — Acceptance Tests:** Automated end-to-end tests run against staging.

**Stage 8 — Manual Gate (optional):** Human approval required before production deployment (Continuous Delivery stops here until a human acts; Continuous Deployment skips this gate).

**Stage 9 — Deploy to Production:** Automated deployment to production using approved strategy.

**Stage 10 — Post-Deploy Monitoring:** Automated health checks; alerts triggered if baselines are breached.

### 4.3 Infrastructure as Code

Infrastructure as Code (IaC) means defining infrastructure — servers, networks, load balancers, databases — in version-controlled configuration files rather than through manual UI actions.

**Benefits for release management:**

- Environments are reproducible: staging is guaranteed to match production.
- Changes to infrastructure are reviewed and approved like code changes.
- Rollback means reverting an IaC file, not manually reconfiguring servers.

**Common IaC tools:** Terraform, AWS CloudFormation, Pulumi, Bicep (Azure).

---

## Section 5: Post-Implementation Review

### 5.1 Purpose

The post-implementation review (PIR) closes the release lifecycle loop. It asks: did the release deliver what was intended, and what can we learn?

Without a PIR, organizations cannot improve. Problems get repeated, successes go uncelebrated, and lessons remain locked in individual memories rather than captured in documentation.

### 5.2 Timing

PIRs should be conducted:

- 24–72 hours after deployment for high-impact releases (enough time to see early issues but close enough that participants remember details).
- Within one sprint cycle for routine releases.
- Immediately following any release that caused an incident.

### 5.3 PIR Framework

**Questions to address:**

1. Did the deployment complete within the scheduled maintenance window?
2. Were all acceptance criteria met at go-live?
3. Were any incidents or problems triggered within 72 hours post-deployment?
4. Were the help desk and operations teams adequately prepared?
5. Was user communication timely and accurate?
6. Were rollback procedures tested (even as a dry run)?
7. What were the actual vs. estimated deployment durations?
8. What should be done differently next time?

**Output artifacts:**

- PIR report shared with Change Enablement for change record closure.
- Updated deployment runbook with corrected steps or timings.
- Incident tickets linked to the release record.
- Metrics submitted to the Continual Improvement register.

### 5.4 DORA Metrics Connection

The DORA (DevOps Research and Assessment) research program identified four key metrics that predict software delivery performance:

- **Deployment frequency:** How often the organization successfully releases to production.
- **Lead time for changes:** Time from code commit to production deployment.
- **Change failure rate:** Percentage of deployments that cause a degradation requiring remediation.
- **Mean time to restore (MTTR):** Time to recover from a failure in production.

PIR data feeds directly into change failure rate and MTTR calculations. Organizations that conduct rigorous PIRs accumulate the data needed to demonstrate improvement over time.

---

## Section 6: ITIL 4 Context

### 6.1 Practice Group

Release and Deployment Management is categorized in the **Service Management** practice group within ITIL 4.

### 6.2 Service Value Chain Placement

This practice primarily supports the **Deploy and Transition** activity of the Service Value Chain. It also contributes to **Design and Transition** (planning) and **Obtain/Build** (automation infrastructure).

### 6.3 Guiding Principle Connections

Several ITIL 4 Guiding Principles are particularly relevant:

- **Progress iteratively with feedback:** Phased and canary deployments embody this principle.
- **Keep it simple and practical:** Release notes and runbooks should be as concise as needed — no longer.
- **Optimize and automate:** CI/CD pipelines are the operational expression of this principle.
- **Collaborate and promote visibility:** Release calendars, go/no-go reviews, and PIRs all depend on cross-functional collaboration.

---

## Key Vocabulary

Review these terms before the quiz:

- **Release** — bundled set of changes ready for deployment.
- **Deployment** — act of placing a release into a target environment.
- **Release calendar** — forward-looking schedule of planned releases.
- **Release notes** — documentation artifact covering scope, steps, rollback, and contacts.
- **Go/no-go review** — pre-deployment decision checkpoint.
- **Big bang deployment** — simultaneous cutover for all users.
- **Phased deployment** — incremental rollout by user group or region.
- **Canary deployment** — small traffic percentage routed to new version.
- **Blue/green deployment** — two identical environments; traffic switch for cutover.
- **CI/CD pipeline** — automated build-test-deploy workflow.
- **Infrastructure as Code (IaC)** — version-controlled infrastructure definitions.
- **Post-implementation review (PIR)** — structured evaluation after go-live.
- **DORA metrics** — deployment frequency, lead time, change failure rate, MTTR.
- **Immutable infrastructure** — deploy new images; never patch running servers.
- **Code freeze** — period when only emergency changes are permitted.

---

## Self-Check Questions

Answer these in your own words before reviewing the answer key in class:

1. What is the difference between a release and a deployment?
2. Why would an organization choose a phased deployment over a big bang deployment?
3. What infrastructure is required to implement canary deployments?
4. What are the four DORA metrics and why do they matter to Release Management?
5. How does the post-implementation review connect to Continual Improvement?

---

## Connections to Other Modules

- **Module 8 (Change Enablement):** Change authorization is a prerequisite for release deployment.
- **Module 13 (IT Asset Management):** Deployed components must be reflected in the CMDB.
- **Module 15 (DevOps and ITIL):** CI/CD and DevOps practices align directly with deployment automation.

---

*End of Module 12 Reading Guide — approximately 250 lines*
