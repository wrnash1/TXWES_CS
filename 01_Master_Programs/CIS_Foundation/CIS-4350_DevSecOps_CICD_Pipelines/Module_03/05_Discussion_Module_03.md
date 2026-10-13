# Discussion Forum: Module 03 — Continuous Integration and Security Gates

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Discussion Overview

Post your original response to one scenario below (minimum 175 words). Then reply substantively to at least two classmates' posts (minimum 75 words each). Original posts due Sunday 11:59 PM; peer replies due Tuesday 11:59 PM.

Professor Nash note: I am listening for evidence that you understand the tension between pipeline strictness and developer velocity. A pipeline so strict that developers work around it is not more secure — it may be less secure. Think carefully about the phased adoption approach, the role of quality gates as guardrails not blockers, and the organizational dynamics that make or break pipeline security programs.

---

## Scenario 1 — The Pipeline That Cried Wolf

Your organization's newly deployed CI pipeline has been running for 30 days. Security scan jobs are configured to fail the build on any CVSS 4.0+ finding. The result: 94% of all pipeline runs fail. Developers have started regularly using `git commit --no-verify` locally and pushing with `--force` to bypass branch protection. The security team is proud of how strict the pipeline is. The development VP is furious.

Analyze what went wrong and propose a concrete remediation plan. Your plan must address the quality gate threshold configuration, how you will reduce the backlog of open findings to a manageable level, how you will restore developer trust in the pipeline, and what metrics you will track to measure improvement. Reference the phased adoption approach from the reading guide. What is the minimum effective gate that provides real security value without causing alert fatigue? How would you present this change to both the security team and the development VP?

### Scenario 1 — Peer Response Prompt

Your classmate proposed a quality gate threshold. Do you agree with their minimum effective gate? Is there a scenario where their proposed threshold would still allow critical vulnerabilities to reach production?

---

## Scenario 2 — The Contractor's Pipeline Backdoor

During a security audit, you discover that a third-party contractor who was given write access to your GitHub repository six months ago modified `.github/workflows/secure-ci.yml` to add `continue-on-error: true` to all security scan jobs before their engagement ended. As a result, the pipeline has been showing green for six months regardless of security findings. Hundreds of pull requests have been merged during this time.

Describe your immediate response, your investigation process, and the long-term preventive controls you would implement. How do you assess the scope of potential damage — what is the worst-case scenario for what may have been introduced during the six months the gate was disabled? Reference the CODEOWNERS and reusable workflow controls from this module. What organizational process failure allowed this to happen, and how does pipeline-as-code create attack surface that traditional manual security gates do not?

### Scenario 2 — Peer Response Prompt

Your classmate described an incident response process. What step did they miss or underweight? Consider the supply chain implications — if vulnerabilities entered production during those six months, what is the downstream impact?

---

## Scenario 3 — GitLab vs. GitHub Actions for a Regulated Client

You are a DevSecOps consultant advising a healthcare company that must comply with HIPAA. They are currently using Jenkins (self-hosted) and considering a migration to either GitHub Actions (cloud-hosted) or GitLab CI (self-hosted GitLab). Their CISO has three requirements: (1) all CI/CD execution must occur in their own data center or a FedRAMP-authorized environment, (2) scan results must never leave their infrastructure, and (3) the solution must support the full security scan suite — SAST, dependency scanning, DAST, and container scanning — out of the box or with minimal custom configuration.

Evaluate GitHub Actions, GitLab CI (self-hosted), and Jenkins for this client against all three requirements. Which do you recommend and why? What are the trade-offs? If you recommend GitLab self-hosted, what specific security templates would you use and what do they provide out of the box? If you recommend GitHub Actions, how would you address the data residency concern? Be specific — do not simply say one is "better."

### Scenario 3 — Peer Response Prompt

Your classmate made a recommendation. Would you trust their recommendation for a HIPAA-regulated environment? What due diligence step did they not mention that a real consultant would perform before making a platform recommendation?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Original post addresses all parts of the chosen scenario | 3 |
| Specific technical configurations, tools, or pipeline concepts cited | 2 |
| Trade-offs and real-world constraints acknowledged | 2 |
| Peer reply 1 — substantive challenge or extension | 1.5 |
| Peer reply 2 — substantive challenge or extension | 1.5 |
| Total | 10 |

---

Discussion — Module 03 | CIS-4350 | Texas Wesleyan University | Professor Nash
