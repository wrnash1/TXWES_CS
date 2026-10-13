# Discussion Forum: Module 07 — Application Security Testing in CI/CD

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Discussion Overview

Post your original response to one scenario below (minimum 175 words). Then reply substantively to at least two classmates' posts (minimum 75 words each). Original posts due Sunday 11:59 PM; peer replies due Tuesday 11:59 PM.

Professor Nash note: Application security testing is a domain with genuine expert disagreement about trade-offs — especially between SAST false positive rates, DAST pipeline integration challenges, and the coverage gap that exists even when all three testing types are in place. I want to see you engage with these real tensions rather than presenting idealized solutions.

---

## Scenario 1 — The SAST False Positive Crisis

Your organization deploys Semgrep with the `p/owasp-top-ten` rule set across 15 microservices. In the first two weeks, developers report that 68% of Semgrep findings are false positives — code that is flagged as SQL injection or XSS but is not actually vulnerable in context. Developer sentiment toward the security scanning program is turning negative. Three teams have started adding `nosemgrep` comments to everything flagged without reviewing the finding.

Diagnose what went wrong and propose a recovery plan. What factors typically cause high false positive rates in SAST tools? What is the difference between a false positive and an accepted risk, and how does your response differ for each? How do you tune Semgrep rule sets to reduce noise without creating blind spots? What process changes would you implement to ensure that `nosemgrep` suppressions receive appropriate review? Reference specific Semgrep configuration options and suppression practices from the reading guide.

### Scenario 1 — Peer Response Prompt

Your classmate proposed specific tuning steps. Do their proposed tuning changes reduce false positives or do they create security blind spots? What evidence would you want to see before accepting their proposal?

---

## Scenario 2 — DAST in a Microservices Environment

You are tasked with implementing DAST scanning across a microservices application that has 23 individual services, each with its own REST API. All services are deployed together in a staging Kubernetes cluster. A complete OWASP ZAP full scan of all 23 services takes 4 hours — far too long for a pull request pipeline. The security team insists that DAST is a requirement for compliance.

Design a practical DAST strategy for this environment. Which services should get full scans vs. baseline scans, and on what criteria? How do you integrate DAST into the pipeline without blocking developers for 4 hours? Consider scheduled DAST vs. PR-triggered DAST, risk-based scan scope selection, parallel scanning, and the trade-off between scan coverage and pipeline speed. Reference the ZAP scan modes from this module and propose specific GitHub Actions trigger configurations. What compliance evidence does this approach generate, and is it sufficient to satisfy a SOC 2 or PCI-DSS auditor?

### Scenario 2 — Peer Response Prompt

Your classmate proposed a risk-based approach to which services get full scans. What is the risk of their selection criteria? Is there a service type that their criteria would incorrectly exclude from full scanning?

---

## Scenario 3 — The Log4Shell Response

In December 2021, the Log4Shell vulnerability (CVE-2021-44228 — CVSS 10.0) was disclosed. Organizations using Apache Log4j in Java applications needed to identify and patch within hours. Organizations with mature DevSecOps programs responded in hours; those without took days or weeks.

Analyze how a mature SBOM program would have improved the Log4Shell response. If every release since 2019 had an associated CycloneDX SBOM, what exact steps would your incident response team take within the first 2 hours of disclosure? Compare this to the response at an organization without SBOMs — how do they determine which applications are affected? What dependency scanning tools would have caught this in the pipeline before deployment, and why did many organizations deploying Log4j not catch it? (Hint: consider the difference between direct and transitive dependencies.) Reference Syft, Grype, and OWASP Dependency-Check from this module.

### Scenario 3 — Peer Response Prompt

Your classmate described an SBOM-based response process. How long does their described process actually take for an organization with 500 applications? What is the bottleneck in their process?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Original post addresses all parts of the chosen scenario | 3 |
| Specific tools, configurations, or pipeline patterns cited | 2 |
| Trade-offs and real-world constraints acknowledged | 2 |
| Peer reply 1 — substantive challenge or extension | 1.5 |
| Peer reply 2 — substantive challenge or extension | 1.5 |
| Total | 10 |

---

Discussion — Module 07 | CIS-4350 | Texas Wesleyan University | Professor Nash
