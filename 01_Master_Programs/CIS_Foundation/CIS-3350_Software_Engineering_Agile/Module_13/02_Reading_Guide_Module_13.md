# Reading Guide: Module 13 — Continuous Integration and DevOps Basics

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3350 &BULL; SOFTWARE ENGINEERING & AGILE METHODOLOGIES</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Continuous Integration and DevOps practices are the technical infrastructure that makes Scrum's "potentially releasable Increment every Sprint" promise achievable in practice. Without automated build-test-deploy pipelines, delivering a high-quality Increment in one to two weeks is nearly impossible at scale. This module covers the core concepts of CI, Continuous Delivery, deployment strategies, and the relationship between DevOps culture and Scrum team effectiveness.

---

## 1. Continuous Integration

### Definition and Core Practice

Continuous Integration is the practice of merging developer code changes into a shared repository frequently — at minimum, daily — and automatically verifying each integration with a build and test run.

The problem CI solves: when developers work in long-lived feature branches, they accumulate integration risk. When those branches merge simultaneously at the end of a Sprint, conflicting changes, broken dependencies, and unexpected interactions consume significant Sprint capacity. CI eliminates integration risk by making integration a continuous, automated activity.

### CI Pipeline Stages

| Stage | Purpose | Failure Means |
|-------|---------|---------------|
| Commit trigger | Starts pipeline on every push to shared branch | N/A — trigger event |
| Build | Compiles or assembles the application | Code cannot compile — no further stages run |
| Unit tests | Runs automated unit tests from TDD | A unit of logic has regressed |
| Static analysis / lint | Checks code quality, style, security patterns | Code quality standard violated |
| Integration tests | Tests code against real dependencies | Integration behavior has broken |
| Artifact creation | Produces deployable package | Build output unavailable for deployment |

### CI Culture Requirements

The pipeline is only effective when the team treats a broken build as an immediate priority. CI culture requires:

- Developers push code at least once daily — not once at Sprint end
- A red pipeline is an emergency, not a to-do item
- The developer who broke the build fixes it before others push new changes
- Test coverage must be sufficient for the pipeline to serve as a quality signal

---

## 2. Continuous Delivery and Continuous Deployment

### Continuous Delivery

Continuous Delivery extends CI so that every successful pipeline run produces a release candidate — software that has been built, tested, and deployed to a staging environment. The software is always in a releasable state. A human decision (typically the Product Owner) is the only gate between staging and production.

Continuous Delivery supports Scrum's Sprint model: the Increment is potentially releasable at Sprint end because the pipeline has verified it and staged it. The Product Owner decides when — not whether — to release.

### Continuous Deployment

Continuous Deployment removes the human gate. Every successful pipeline run deploys automatically to production. This requires extremely high confidence in automated test coverage and monitoring.

### Comparison

| Term | Automated To | Human Gate Before Production |
|------|-------------|------------------------------|
| Continuous Integration | Build + tests | Yes — always |
| Continuous Delivery | Staging environment | Yes — release decision |
| Continuous Deployment | Production | No — fully automated |

---

## 3. Deployment Strategies

### Blue-Green Deployment

Blue-green deployment maintains two identical production environments. One environment (blue) is live. The new version is deployed to the inactive environment (green) and tested. A router switch redirects traffic from blue to green. The original blue environment remains as an instant rollback.

Benefits: zero-downtime deployment, instant rollback capability.

Costs: maintaining two complete production environments, cost of double infrastructure.

Best fit: teams that need a guaranteed rollback option and can afford duplicate environments.

### Canary Deployment

Canary deployment routes a small percentage of production traffic — typically one to five percent — to the new version. The team monitors error rates, performance, and user behavior on the canary segment. The percentage increases gradually as metrics confirm stability. Problems cause the canary to roll back to zero.

Benefits: real-world validation before full rollout, reveals load-related problems that staging environments miss.

Costs: complexity of running two software versions simultaneously, especially when database schemas or APIs differ between versions.

Best fit: teams releasing features that need validation under real production load, or changes to high-risk components.

### Traditional Big-Bang Deployment (Anti-Pattern)

Traditional deployments push all changes to all users at once, often after a long development cycle. There is no rollback mechanism beyond a full re-deployment of the previous version. Risk is highest when the change volume is largest. Neither blue-green nor canary deployment is appropriate when the release cycle is six months long — they require frequent, small releases to be effective.

---

## 4. DevOps Principles

DevOps is a cultural and organizational approach that removes the separation between development teams (who build software) and operations teams (who run it in production). The core principle is "you build it, you run it" — the team that writes the code is responsible for its behavior in production.

DevOps supports Scrum because:

- Scrum teams are cross-functional — they should own the full lifecycle of what they build
- Operations concerns (reliability, monitoring, incident response) are part of the Definition of Done
- Short feedback loops from production behavior inform Sprint planning and backlog refinement

---

## 5. CI/CD and the Scrum Definition of Done

The Definition of Done is the commitment that defines what "done" means for an Increment. In teams with CI/CD pipelines, the DoD commonly includes:

- All CI checks pass (build, unit tests, static analysis, integration tests)
- Artifact deployed to staging environment
- Integration tests pass in staging
- No critical defects introduced by the Increment

These criteria make "potentially releasable" a verifiable claim rather than an optimistic one. If a Story passes all pipeline checks and deploys cleanly to staging, the Increment meets its quality commitment. If the pipeline is red, the Increment is not done by definition.

---

## 6. Velocity and CI/CD Investment

Teams without CI/CD pipelines spend Sprint capacity on:

- Manual test runs before Sprint Review
- Debugging integration conflicts during the final days of the Sprint
- Fixing defects discovered late because there was no automated quality gate

Teams with mature CI/CD pipelines redirect that capacity to feature development. The initial investment in building the pipeline — estimated at two to four Sprints for a new team — is typically recovered within the following four to six Sprints through reduced defect rates and eliminated manual testing overhead.

---

## 7. PSM I Exam Tips

Tip 1: The PSM I does not test CI/CD implementation details. It tests why technical practices like CI/CD matter for Scrum's goal of a potentially releasable Increment and how they relate to the Scrum values of transparency and inspection.

Tip 2: Transparency is the Scrum pillar most directly supported by CI. A green pipeline is a transparent quality signal visible to the entire Scrum Team. Without CI, the Increment's quality is only visible at Sprint Review — too late for meaningful inspection.

Tip 3: Continuous Delivery is the practice most aligned with Scrum. The Product Owner retains the release decision. Continuous Deployment removes that decision — a difference exam questions may exploit.

Tip 4: Blue-green and canary deployment are exam-relevant because they represent choices about how to manage deployment risk. Blue-green favors rollback speed. Canary favors pre-full-release validation.

Tip 5: The Definition of Done is the mechanism connecting CI/CD to Scrum. When the DoD includes pipeline criteria, the team's quality claim for each Increment is backed by automated evidence, not assertion.

Tip 6: DevOps culture aligns with Scrum's cross-functional team model. A Scrum Team that includes operations responsibilities in its DoD and owns production reliability embodies both Scrum and DevOps principles.

Tip 7: "Integration hell" — the cost of delayed merging — is a form of technical debt that CI prevents. Scrum's Retrospective is the event where the team surfaces and plans the reduction of integration-related waste.

Tip 8: The Agile Manifesto's Principle 9 — continuous attention to technical excellence — applies to pipeline quality as much as to design quality. A broken, ignored CI pipeline is the infrastructure equivalent of a God Object.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 13 topics:

**1. "Continuous Integration" — Martin Fowler**
<https://martinfowler.com/articles/continuousIntegration.html>
The definitive free article on Continuous Integration by Martin Fowler, one of the Agile Manifesto signatories. Covers the full set of CI practices including daily integration, automated build, self-testing builds, and the cultural practices required for CI to succeed. Essential background for the lab's pipeline analysis tasks.

**2. "Deployment Strategies" — The Twelve-Factor App**
<https://12factor.net>
A free methodology guide for building software-as-a-service applications, directly relevant to DevOps and CI/CD practices. Covers environment parity, release/run stages, and disposable processes — the foundational ideas behind blue-green and canary deployment strategies.

**3. "What is DevOps?" — Atlassian**
<https://www.atlassian.com/devops>
A free comprehensive guide to DevOps culture, practices, and tooling from Atlassian. Covers the "you build it, you run it" principle, CI/CD pipelines, monitoring, and the relationship between DevOps and Agile teams. Includes a clear comparison of Continuous Integration, Continuous Delivery, and Continuous Deployment.

---

## 8. Study Checklist

- [ ] Define Continuous Integration and explain what the pipeline automates
- [ ] Name the stages of a typical CI pipeline and what each one verifies
- [ ] Distinguish Continuous Delivery from Continuous Deployment
- [ ] Explain blue-green deployment and identify its primary benefit and cost
- [ ] Explain canary deployment and identify what risk it is designed to validate
- [ ] Describe what DevOps culture means for a Scrum Team
- [ ] Connect CI/CD pipeline criteria to the Definition of Done
- [ ] Explain why a broken build is an emergency in CI culture
- [ ] Complete this module's Lab and Quiz

---
