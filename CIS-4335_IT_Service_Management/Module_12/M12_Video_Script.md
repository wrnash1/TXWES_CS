# Video Script: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Slide 1: Introduction (0:00–0:45)

Welcome back to CIS-4335 IT Service Management. I'm Professor Nash, and this is Module 12: Release and Deployment Management.

In this video we cover one of the most operationally significant practices in the ITIL 4 framework — how organizations move tested, approved changes from development or staging environments into live production. This is where planning meets execution, and where errors can ripple out to thousands of end users in seconds.

By the end of this lesson you will be able to describe the purpose of Release and Deployment Management, compare deployment strategies, explain the role of automation, and articulate what a post-implementation review accomplishes.

---

## Slide 2: What Is Release and Deployment Management? (0:45–2:00)

ITIL 4 defines Release and Deployment Management as the practice responsible for making new or changed services and features available for use.

Notice the careful language: "available for use." The practice is not just about pushing code. It is about ensuring that:

- The right version of a service component reaches the right environment.
- Users and support staff are informed and prepared.
- Rollback mechanisms exist if something goes wrong.
- Evidence of a successful deployment is captured.

This practice sits in the Service Management practice group and works hand-in-hand with Change Enablement, which governs authorization, and with Deployment Management at the technical layer.

A **release** is a collection of one or more changes to an IT service that are built, tested, and deployed together. A **deployment** is the physical or virtual act of moving that release to the target environment.

Think of a release as the packaged gift and the deployment as delivering it to the recipient's door.

---

## Slide 3: The Release Planning Process (2:00–4:30)

Effective release planning prevents the chaos that occurs when changes are deployed in an uncoordinated fashion. Planning answers four questions:

- **What** is being released?
- **When** will it be deployed?
- **Who** is responsible for each step?
- **How** will success be measured?

### Release Schedule

Most mature organizations maintain a release calendar or release schedule — a forward-looking view of all planned releases across environments and business units. The calendar helps avoid conflicts, such as two teams deploying to the same database cluster on the same night.

### Release Notes

Before any deployment, a release note document is prepared. Release notes serve multiple audiences:

- **Operations teams** need to know what changed technically.
- **Help Desk teams** need to know what new symptoms or errors might appear.
- **End users** may receive simplified release notes explaining new features.
- **Auditors** need traceability — evidence that what was deployed matches what was approved.

A good release note includes: version number, change request references, list of components changed, known issues, rollback instructions, and contact information for the deployment lead.

### Go/No-Go Decision

Immediately before deployment, a structured go/no-go review is conducted. Participants include representatives from development, testing, operations, and often the business. If any critical acceptance criteria are unmet, the release is held and rescheduled.

---

## Slide 4: Deployment Approaches — Big Bang (4:30–6:15)

There are three primary deployment approaches in industry. Each involves trade-offs between speed, risk, and operational complexity.

### Big Bang Deployment

In a big bang deployment, the new version replaces the old version for all users simultaneously at a defined cutover time.

**Advantages:**

- Simple to coordinate — one deployment event.
- No need to maintain two versions simultaneously.
- Clear before/after boundary for support teams.

**Disadvantages:**

- Maximum blast radius. If something goes wrong, all users are affected immediately.
- Rollback must happen quickly or downtime accumulates.
- Requires high confidence in testing coverage.

Big bang deployments are often scheduled during maintenance windows — typically late at night or over weekends — to minimize user impact. They remain common for monolithic applications, database schema changes, and on-premises infrastructure upgrades where parallel operation is impractical.

---

## Slide 5: Deployment Approaches — Phased and Canary (6:15–8:30)

### Phased Deployment

A phased deployment rolls the new version out incrementally — by region, user group, department, or server cluster — over a defined schedule.

**Advantages:**

- Problems are caught early, affecting only the first cohort.
- Feedback from early adopters informs support readiness.
- Rollback scope is smaller if issues surface.

**Disadvantages:**

- Two versions run simultaneously, which complicates data migrations and API compatibility.
- Extended deployment window increases coordination overhead.
- Some users receive the new version much later than others.

Phased deployment is common for SaaS platforms, enterprise software rollouts across global offices, and mobile application updates.

### Canary Deployment

A canary deployment is a specialized form of phased deployment where a small percentage of traffic or users — often 1–5% — is routed to the new version while the majority remains on the stable version. Engineers monitor error rates, latency, and business metrics closely. If the canary performs well, the percentage gradually increases until full rollout.

The name comes from the historical practice of coal miners using canaries to detect toxic gases — the canary signals danger before the whole workforce is affected.

**Key requirement:** Canary deployments require feature flags or traffic routing infrastructure — tools like Kubernetes ingress controllers, AWS CodeDeploy, or LaunchDarkly.

---

## Slide 6: Deployment Automation (8:30–10:45)

Manual deployments are slow, error-prone, and hard to reproduce. Modern ITSM environments invest heavily in deployment automation.

### CI/CD Pipelines

**Continuous Integration (CI)** means developers regularly merge code changes into a shared repository, triggering automated builds and tests.

**Continuous Delivery (CD)** extends CI so that every successfully tested build is ready for deployment with minimal human intervention.

**Continuous Deployment** takes CD one step further — approved builds are automatically pushed to production without manual gates.

In ITIL 4 terms, CI/CD pipelines are an **enabling technology** for Release and Deployment Management. They do not replace the practice — governance, documentation, and human judgment remain essential — but they dramatically reduce lead time and defect rates.

### Deployment Automation Tools

Common tools include:

- **Jenkins** — open-source automation server; triggers build-test-deploy pipelines.
- **GitLab CI/CD** — integrated into the GitLab source control platform.
- **GitHub Actions** — event-driven workflows tied to repository events.
- **Ansible / Puppet / Chef** — infrastructure-as-code tools for environment configuration.
- **ArgoCD / Flux** — GitOps tools for Kubernetes-based deployments.

### Immutable Infrastructure

An important modern pattern is **immutable infrastructure**: rather than patching running servers, a new server image is built and deployed, and the old one is terminated. This eliminates configuration drift and makes rollback as simple as redeploying the prior image.

---

## Slide 7: Post-Implementation Review (10:45–13:00)

Deployment does not end when the release goes live. A **post-implementation review (PIR)** is conducted after sufficient stabilization time — typically 24–72 hours for significant releases — to evaluate whether the deployment met its objectives.

### PIR Agenda

A structured PIR addresses:

- Did the deployment complete on schedule?
- Were the acceptance criteria met?
- Were any incidents or problems triggered by the release?
- Were stakeholders adequately informed?
- Was the rollback plan tested (even if not used)?
- What lessons should be captured for future releases?

### Outputs

PIR outputs feed back into the Continual Improvement practice. Common outputs include:

- Updated runbooks or deployment checklists.
- Identified training needs for support staff.
- Metrics such as deployment frequency, lead time for changes, and change failure rate.

These last three are part of the **DORA metrics** (DevOps Research and Assessment), which are increasingly referenced in ITIL 4 discussions because they provide quantitative evidence of release and deployment maturity.

---

## Slide 8: Release and Deployment in the ITIL 4 SVS (13:00–14:30)

Release and Deployment Management does not operate in isolation. Within the ITIL 4 Service Value System:

- **Change Enablement** authorizes the release.
- **Service Validation and Testing** certifies it is ready.
- **Deployment Management** handles the technical execution.
- **Service Configuration Management** updates the CMDB with new component versions.
- **IT Asset Management** tracks license and software asset changes.

The **Service Value Chain** activity most associated with this practice is **Deploy and Transition**, which transforms approved changes into live value for customers.

Feedback loops are also essential. Incidents raised after deployment link back to the release record, providing evidence for root cause analysis and trend identification.

---

## Slide 9: Key Terms Summary (14:30–15:30)

Let us review the key vocabulary from this module:

- **Release** — a set of changes bundled and deployed together.
- **Deployment** — the act of moving a release to a target environment.
- **Release notes** — documentation of what changed, for whom, and how to roll back.
- **Big bang deployment** — simultaneous cutover for all users.
- **Phased deployment** — incremental rollout by group or region.
- **Canary deployment** — small-percentage traffic routing to test new version.
- **CI/CD pipeline** — automated build, test, and deploy workflow.
- **Immutable infrastructure** — deploy new images rather than patch live servers.
- **Post-implementation review** — structured evaluation after go-live.
- **DORA metrics** — deployment frequency, lead time, change failure rate, mean time to restore.

---

## Slide 10: Closing and Preview (15:30–16:00)

That wraps up Module 12. You now have a solid grounding in how organizations plan, execute, and evaluate releases in a disciplined, ITIL-aligned way.

In Module 13 we shift focus to IT Asset Management — tracking the hardware, software, and configuration items that power your services across their entire lifecycle.

Complete the reading guide, lab, and quiz before moving on. I'll see you in Module 13.

---

*End of Module 12 Video Script — approximately 230 lines*
