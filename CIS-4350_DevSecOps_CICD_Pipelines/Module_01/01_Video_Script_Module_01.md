# Video Script: Module 01 — Introduction to DevSecOps

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Welcome and Course Orientation (0:00–2:00)

[SLIDE: Course title card with Texas Wesleyan branding]

Welcome to CIS-4350 — DevSecOps and CI/CD Pipelines. I'm Professor Nash, and over the next nine modules we're going to build a thorough, practical understanding of how modern software teams integrate security directly into the development and delivery process.

Before we dive into the technical content, let me set the stage. This course aligns with the DevSecOps Professional certification, sometimes abbreviated DSOE. The skills you develop here are directly applicable to real-world job roles including DevSecOps Engineer, Platform Security Engineer, and Site Reliability Engineer with a security focus.

By the end of this module you will be able to define DevSecOps, explain the shift-left principle, describe the DevSecOps lifecycle, identify major tools in the DevSecOps toolchain, and articulate the cultural changes required for successful adoption.

Let's get started.

---

### SEGMENT 2 — What Is DevOps and Why Did It Emerge? (2:00–5:00)

[SLIDE: Traditional Waterfall vs. Agile vs. DevOps timeline]

To understand DevSecOps we first need to understand DevOps. In the traditional software development world — sometimes called the waterfall model — development teams and operations teams were completely separate. Developers wrote code, threw it "over the wall" to operations, and operations tried to deploy it. Security was an afterthought, a gate at the very end, often called a "penetration test before release."

This created three fundamental problems.

First, slow delivery. A release cycle could take six months to a year. By the time software shipped, requirements had already changed.

Second, instability. Operations teams were not involved in design decisions, so infrastructure assumptions were often wrong. Deployments failed regularly.

Third, late-breaking security defects. When security testing happened only at the end, vulnerabilities discovered late were enormously expensive to fix. The NIST study on cost-of-defect repair showed that a bug found in production costs 30 times more to fix than one found during design.

DevOps emerged in the late 2000s — the term was popularized at the Agile conference in 2008 — as a cultural and technical movement to break down these silos. The Three Ways of DevOps, as described by Gene Kim in the book The Phoenix Project, are Flow, Feedback, and Continual Learning. Flow means work moves efficiently left to right. Feedback means problems surface quickly. Continual learning means teams improve continuously.

DevOps gave us CI/CD — Continuous Integration and Continuous Delivery — which we'll explore deeply in Module 03. But DevOps in its early form still treated security as a separate concern. That's where DevSecOps comes in.

---

### SEGMENT 3 — Shift-Left Security (5:00–9:00)

[SLIDE: SDLC diagram with security touchpoints at every stage]

The phrase "shift left" refers to moving security earlier in the software development lifecycle. Picture a timeline going left to right: Plan, Code, Build, Test, Release, Deploy, Operate, Monitor. In the old model, security lived all the way to the right — at release or even in production. Shift-left means we move security activities to the far left — into planning and coding — where defects are cheapest to find and fix.

Let me give you a concrete example. Suppose a developer writes code that constructs a SQL query by concatenating user input directly — a classic SQL injection vulnerability. In a traditional model this might not be caught until a penetration tester runs sqlmap against the production environment months later. In a shift-left DevSecOps model, a Static Application Security Testing tool — SAST — would flag this in the developer's IDE before the code is even committed to version control.

The four dimensions of shift-left are as follows.

**People** — Developers are trained in secure coding practices. Security is not a separate team's responsibility; it is everyone's responsibility.

**Process** — Security reviews happen at every stage: threat modeling in design, code review in development, automated scanning in CI, compliance checks in deployment.

**Technology** — Automated tools are embedded into the pipeline so security gates run without human intervention on every code change.

**Measurement** — Teams track security metrics alongside performance metrics. Mean Time to Remediate vulnerabilities, vulnerability density per thousand lines of code, and pipeline security gate pass rates are all first-class metrics.

The shift-left principle is foundational to everything we'll do in this course. Keep it in mind as we explore each tool and technique.

---

### SEGMENT 4 — The DevSecOps Lifecycle (9:00–13:00)

[SLIDE: Infinity loop diagram — Plan, Code, Build, Test, Release, Deploy, Operate, Monitor]

The DevSecOps lifecycle extends the classic DevOps infinity loop by adding security activities at each phase. Let's walk through each phase and describe what security looks like there.

**Plan** — Threat modeling occurs here. Teams use frameworks like STRIDE — Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege — to systematically identify potential threats against the system being designed. Security requirements are written alongside functional requirements.

**Code** — Developers use IDE plugins from tools like SonarLint, Semgrep, or Snyk to get real-time security feedback while writing code. Pre-commit hooks prevent secrets from being committed to version control. Peer code review includes security-focused checklists.

**Build** — The CI server compiles code and runs unit tests, but also triggers SAST scans, dependency vulnerability scans, and license compliance checks. A build that introduces a critical vulnerability fails the pipeline.

**Test** — Automated integration and functional tests run alongside Dynamic Application Security Testing, or DAST, which fires HTTP requests at a running application to find runtime vulnerabilities like XSS and CSRF.

**Release** — Security sign-off is automated wherever possible. Release gates check that all security scans passed, that compliance policies are satisfied, and that the Software Bill of Materials is generated and stored.

**Deploy** — Infrastructure is provisioned from code — Infrastructure as Code — and that code is also scanned for misconfigurations. Container images are scanned before being pushed to registries and again before being deployed to Kubernetes clusters.

**Operate** — Runtime security monitoring watches for anomalous behavior in production. Tools like Falco alert on unexpected syscalls from containers.

**Monitor** — Security logs feed into SIEM systems. Vulnerability management platforms track open findings and their remediation status. Compliance dashboards provide continuous audit evidence.

This lifecycle is the backbone of this course. Each subsequent module zooms in on one or more phases.

---

### SEGMENT 5 — Security as Code (13:00–16:00)

[SLIDE: Code snippet of a policy file]

One of the most powerful concepts in DevSecOps is Security as Code — treating security policies, configurations, and controls as versioned, testable code rather than as documents or manual checklists.

Consider a compliance requirement that says all S3 buckets must have public access blocked. In a traditional model, a security engineer manually reviews the AWS console periodically. In a Security as Code model, this policy is written as a machine-executable rule:

```python
# Example: OPA Rego policy for S3 public access
deny[msg] {
    resource := input.resource.aws_s3_bucket[_]
    resource.config.acl == "public-read"
    msg := sprintf("S3 bucket %v must not be public", [resource.address])
}
```

This policy runs automatically in the CI pipeline every time infrastructure code changes. If a developer accidentally sets a bucket to public, the pipeline fails immediately with a clear error message. No human reviewer needed.

Security as Code has four major benefits. It makes security repeatable — the same check runs every time. It makes security auditable — the Git history shows every policy change. It makes security fast — policies execute in seconds. And it makes security collaborative — developers can propose changes to policies through pull requests, just like application code.

The tools that implement Security as Code include Open Policy Agent for general policy enforcement, HashiCorp Sentinel for Terraform policies, tfsec and checkov for Infrastructure as Code scanning, and Conftest for testing configurations against OPA policies. We'll use all of these in later modules.

---

### SEGMENT 6 — DevSecOps Toolchain Overview (16:00–19:00)

[SLIDE: Toolchain diagram organized by lifecycle phase]

The DevSecOps toolchain is large. Let me give you a high-level map so you know what we're covering across the course.

**Source Control Security** — GitHub, GitLab, Bitbucket. Branch protection, signed commits, secret scanning. Covered in Module 02.

**CI/CD Platforms** — GitHub Actions, GitLab CI, Jenkins. Pipeline as code, security gates. Covered in Module 03.

**SAST — Static Analysis** — SonarQube, Semgrep, Checkmarx, Veracode. Analyze source code without running it. Covered in Module 07.

**DAST — Dynamic Analysis** — OWASP ZAP, Burp Suite Enterprise. Test running applications. Covered in Module 07.

**Dependency Scanning** — OWASP Dependency-Check, Snyk, Dependabot. Find vulnerabilities in open-source libraries. Covered in Module 07.

**Container Security** — Docker Scout, Trivy, Snyk Container, Anchore. Scan container images. Covered in Module 04.

**Kubernetes Security** — Falco, OPA Gatekeeper, kube-bench. Runtime and policy enforcement. Covered in Module 05.

**Infrastructure as Code Security** — tfsec, checkov, Terrascan. Scan Terraform, CloudFormation, Kubernetes manifests. Covered in Module 06.

**Secrets Management** — HashiCorp Vault, AWS Secrets Manager, Azure Key Vault. Never hardcode secrets. Covered in Module 09.

**Software Composition Analysis** — Snyk, Black Duck, FOSSA. License and vulnerability tracking. Covered in Module 08.

**SBOM** — Syft, CycloneDX, SPDX. Generate software bill of materials. Covered in Module 08.

That is eleven tool categories across eight modules. You don't need to memorize every tool today — we'll build familiarity as we work through each module in detail.

---

### SEGMENT 7 — Cultural and Organizational Change (19:00–21:30)

[SLIDE: Conway's Law diagram]

Technology is only part of the DevSecOps story. Culture is equally important, and honestly harder to change than any tool.

Conway's Law states that organizations design systems that mirror their communication structures. If your organization has separate Development, Security, and Operations teams that rarely talk to each other, your software architecture will reflect those boundaries — and security will always be siloed.

DevSecOps requires what practitioners call a "security champions" model. In this model, each development team has one or two members with extra security training who serve as liaisons to the central security team. Security champions help their colleagues understand security issues, triage findings from automated tools, and propagate security culture throughout the organization.

The CALMS framework — Culture, Automation, Lean, Measurement, and Sharing — provides a useful lens for DevSecOps adoption. Culture means shared ownership of security outcomes. Automation means replacing manual gates with automated controls. Lean means eliminating waste in security processes. Measurement means tracking security KPIs. Sharing means making security knowledge available to all teams.

Organizational change is gradual. Start by embedding one security tool into an existing pipeline. Demonstrate value quickly — show that automated SAST found a real vulnerability faster than a manual review would have. Build momentum from there.

---

### SEGMENT 8 — ROI of DevSecOps (21:30–23:00)

[SLIDE: Cost comparison chart — fix cost at different SDLC stages]

Let's close with the business case. Why should organizations invest in DevSecOps?

The IBM Systems Sciences Institute data is frequently cited: fixing a defect in the design phase costs $1; in development, $10; in integration testing, $100; in production, $1,000. Security defects follow the same exponential cost curve.

Beyond defect cost, consider breach costs. The IBM Cost of a Data Breach Report 2023 found the average breach cost $4.45 million. Organizations with mature DevSecOps practices had lower breach rates and lower breach costs.

Regulatory compliance is another driver. GDPR, HIPAA, PCI-DSS, SOC 2 — all require evidence of security controls. DevSecOps generates that evidence automatically as a byproduct of the pipeline.

Finally, consider developer productivity. Counterintuitively, embedding security earlier makes developers faster, not slower. When a security finding surfaces in the IDE before commit, it takes minutes to fix. When it surfaces in a quarterly penetration test, it requires a sprint of rework, meetings, and patch releases.

The ROI case for DevSecOps is compelling on every dimension: cost of defects, cost of breaches, compliance, and developer velocity.

---

### SEGMENT 9 — Module Summary and Looking Ahead (23:00–24:00)

[SLIDE: Module 01 key takeaways]

Let's recap the key takeaways from Module 01.

DevOps broke down silos between development and operations. DevSecOps extends that by integrating security into every stage of the lifecycle.

Shift-left security means finding and fixing vulnerabilities earlier, where they are cheapest to remediate.

The DevSecOps lifecycle — Plan, Code, Build, Test, Release, Deploy, Operate, Monitor — has security activities at every stage.

Security as Code treats policies and controls as versioned, testable artifacts.

The DevSecOps toolchain spans source control, CI/CD, SAST, DAST, container security, IaC security, secrets management, and SCA.

Cultural change — through security champions, CALMS, and shared ownership — is as important as any tool.

The business case is strong: lower defect costs, lower breach costs, better compliance posture, and faster developer velocity.

In Module 02 we'll get hands-on with version control security — signed commits, branch protection, git hooks, and secrets scanning. See you there.

---

*[END OF SCRIPT — Module 01]*
