# Reading Guide: Module 01 - DevOps Fundamentals and the DevSecOps Mindset

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Welcome to Module 01. This module establishes the cultural and technical foundations of DevSecOps: what it means to embed security into every stage of the software delivery lifecycle rather than treating it as a final checkpoint. You will explore the evolution from traditional waterfall development through DevOps and into DevSecOps, understanding why integrating security earlier — "shifting left" — dramatically reduces the cost and risk of vulnerabilities. These foundational concepts underpin every subsequent module and are heavily tested on the DevSecOps Professional certification exam.

---

## Section 1: High-Yield Glossary

Review these definitions carefully. The DevSecOps Professional exam expects you to recognize and apply these concepts in scenario-based questions.

**DevSecOps** — A software engineering culture and practice that integrates security controls, testing, and responsibilities into every phase of the DevOps CI/CD pipeline. Rather than a separate security review at the end of development, DevSecOps makes security a shared responsibility among developers, operations engineers, and security professionals from the first commit onward.

**Shift-left security** — The practice of moving security activities — such as code analysis, dependency scanning, and threat modeling — earlier in the software development lifecycle (SDLC). By catching vulnerabilities during development rather than post-deployment, teams reduce remediation cost and prevent security debt from accumulating.

**CI/CD pipeline** — Continuous Integration and Continuous Delivery (or Deployment). A series of automated steps that take source code from a developer's commit through build, test, security scanning, and deployment to production. The pipeline is the enforcement point for DevSecOps controls.

**Pipeline automation** — The use of CI/CD tooling (GitHub Actions, Jenkins, GitLab CI) to automatically trigger build, test, and security-gate steps upon each code commit. Automating security checks within the pipeline ensures consistent, repeatable enforcement without relying on manual human review for every change.

**Feedback loop** — The time elapsed between when a developer introduces a vulnerability and when they receive notification of it. Shorter feedback loops are a core DevSecOps goal because they reduce context-switching cost and make remediation faster and cheaper.

**Security gate** — An automated check within the CI/CD pipeline that must pass before the pipeline proceeds to the next stage. A failed security gate — such as a SAST scan finding a critical vulnerability — blocks the build or merge until the issue is resolved.

**Shared responsibility model** — The DevSecOps principle that security is owned by all roles: developers own secure code, operations owns secure infrastructure, and security teams own tooling, policy, and training. No single team is the sole security owner.

**Security champion** — A developer within a product team who receives additional security training and serves as a first point of contact for security questions, bridging the gap between the development team and the dedicated security team.

**SAST (Static Application Security Testing)** — Analysis of source code, bytecode, or binaries without executing the application. SAST tools identify vulnerability patterns in code at the earliest possible pipeline stage — commit or pull request.

**DAST (Dynamic Application Security Testing)** — Testing a running application by sending crafted HTTP requests and observing responses. DAST finds runtime vulnerabilities that cannot be detected without execution. Applied at the staging stage of the pipeline.

**SCA (Software Composition Analysis)** — Scanning open-source dependencies and third-party libraries for known CVEs and license compliance issues. Applied at the build stage when dependencies are downloaded.

**IaC (Infrastructure as Code)** — Managing infrastructure configuration (servers, networks, cloud resources) through machine-readable configuration files rather than manual setup. Terraform, Pulumi, and AWS CloudFormation are common IaC tools. IaC files can be scanned for security misconfigurations before provisioning.

**CVE (Common Vulnerabilities and Exposures)** — A standardized identifier for publicly known security vulnerabilities maintained in the National Vulnerability Database (NVD). CVE identifiers (e.g., CVE-2021-44228) are used by SCA and container scanning tools to flag vulnerable components.

**Security debt** — Accumulated security vulnerabilities and misconfigurations that have not been remediated. Like technical debt, security debt grows over time and becomes increasingly expensive to address.

---

## Section 2: The Software Development Lifecycle and Security Placement

Understanding where each security activity belongs in the SDLC is one of the most heavily tested topics on the DevSecOps Professional exam. The table below maps SDLC phases to the appropriate security activities and tools.

| SDLC Phase | Security Activity | Representative Tools |
|---|---|---|
| Requirements / Design | Threat modeling | STRIDE, OWASP Threat Dragon |
| Coding | Pre-commit secrets scan | Gitleaks, truffleHog |
| Code review / Pull request | SAST | Semgrep, SonarQube, Checkmarx |
| Build | SCA (dependency scan) | Snyk, OWASP Dependency-Check, Grype |
| Container build | Image scanning | Trivy, Grype, Clair |
| Staging / Integration test | DAST | OWASP ZAP, Burp Suite Enterprise |
| IaC provisioning | IaC misconfiguration scan | Checkov, tfsec, Terrascan |
| Production | Runtime monitoring | Falco, AWS GuardDuty |

---

## Section 3: CI/CD Pipeline Stage Comparison

The following table compares the three most commonly tested pipeline security categories on the DevSecOps Professional exam.

| Dimension | SAST | DAST | SCA |
|---|---|---|---|
| Full name | Static Application Security Testing | Dynamic Application Security Testing | Software Composition Analysis |
| Requires running app | No | Yes | No |
| Primary target | First-party source code | Running application endpoints | Third-party dependencies |
| Pipeline stage | Commit / Pull request | Staging | Build |
| Finds | Insecure code patterns, injection flaws | Runtime flaws, auth bypasses, config errors | Known CVEs in libraries |
| False positive rate | Higher (no runtime context) | Lower (real execution) | Low (CVE database matches) |
| Representative tools | Semgrep, SonarQube, Checkmarx | OWASP ZAP, Burp Suite Enterprise | Snyk, OWASP Dependency-Check |

---

## Section 4: The Cost of Late Detection

One of the most frequently tested DevSecOps Professional exam topics is the economic justification for shift-left security. Key points to know:

- IBM Systems Sciences Institute research shows that the relative cost to fix a defect increases by a factor of 5-10x for each phase it progresses uncaught through the SDLC.
- A vulnerability fixed at the coding phase may cost $80 in developer time.
- The same vulnerability found in production testing may cost $1,500 in developer time plus operations time.
- The same vulnerability found after a production breach may cost millions in incident response, regulatory fines, and reputation damage.
- These multipliers justify the investment in automated pipeline security controls even when those controls occasionally produce false positives.

---

## Section 5: DevSecOps vs. Traditional Security Models

| Dimension | Traditional (Waterfall/Siloed) | DevSecOps |
|---|---|---|
| Security timing | Post-development, pre-release gate | Continuous, at every pipeline stage |
| Security ownership | Dedicated security team only | Shared: Dev + Ops + Security |
| Feedback loop | Weeks to months | Minutes to hours |
| Security testing method | Manual penetration test | Automated pipeline scans + manual where needed |
| Vulnerability discovery point | Staging or production | Commit or pull request |
| Release velocity impact | Security is bottleneck | Security is automated, minimal velocity impact |
| Cost of remediation | High (late discovery) | Low (early discovery) |

---

## Section 6: Docker Security Best Practices Reference

While Docker security is covered in depth in Module 04, these foundational practices appear in exam questions starting in Module 01 as context for DevSecOps pipeline design.

- Use minimal base images (Alpine, distroless) to reduce the attack surface.
- Never run containers as root; use `USER` directive in Dockerfile to specify a non-root user.
- Use multi-stage builds to exclude build-time dependencies from the final image.
- Pin dependency versions in the Dockerfile rather than using `latest` tags.
- Scan images with Trivy or Grype before pushing to a registry.
- Store secrets in environment variables injected at runtime, never in the image.

---

## Section 7: Kubernetes RBAC Model Reference

Kubernetes Role-Based Access Control (RBAC) is covered in depth in Module 12, but understanding the basic model is tested in foundational questions from Module 01 onward.

- RBAC controls which users and service accounts can perform which actions on which Kubernetes resources.
- Key objects: Role (namespace-scoped), ClusterRole (cluster-scoped), RoleBinding, ClusterRoleBinding.
- Principle of least privilege: grant only the permissions required for a specific function.
- Service accounts should not have cluster-admin privileges unless absolutely required.

---

## Section 8: Secrets Rotation Reference

Secrets rotation — periodically replacing credentials to limit the damage window of a compromised secret — is a cross-cutting concern tested throughout the DevSecOps Professional exam.

- Static credentials (hardcoded in code or config files) should never be used in production.
- Secrets should be stored in dedicated secrets management systems: HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault.
- Rotation intervals depend on secret sensitivity: database passwords every 30-90 days; API keys on compromise detection.
- Automated rotation reduces the operational burden and eliminates the human error risk of manual rotation.
- Audit logs of secret access provide forensic evidence in the event of a breach.

---

## Section 9: Required Reading

Complete the following before attempting the quiz.

- Read the OWASP DevSecOps Guideline introduction at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/). Focus on the sections covering pipeline integration and the placement of security controls at each CI/CD stage.

---

## Section 10: DevSecOps Professional Exam Tips

The following tips are based on the DevSecOps Professional (DSOE) exam objectives and common question patterns.

1. **Shift-left scenario questions** — When the exam presents a scenario where a vulnerability is discovered late (in staging or production) and asks what process change would have prevented it, the answer almost always involves adding the relevant automated scan (SAST, SCA, or secrets scanner) at an earlier pipeline stage.

2. **Culture vs. tools** — Exam questions may ask which statement best describes the DevSecOps mindset. Prioritize answers about shared responsibility and continuous security over answers that focus solely on tool selection.

3. **SDLC phase placement** — Know exactly which tool belongs at which SDLC phase. The exam frequently tests this with "which stage should X scan run at" questions.

4. **Feedback loop optimization** — Questions about improving developer productivity in a DevSecOps context often have answers involving shortening the feedback loop — automated PR checks, inline scan results, or IDE plugins.

5. **Business justification** — The exam tests whether you can articulate the ROI of DevSecOps in economic terms. Know the cost multiplier argument for early detection.

6. **Shared responsibility boundaries** — Know which team owns which responsibility: developers own secure coding practices and dependency choices, operations owns infrastructure configuration, security teams own tooling selection and policy.

7. **Security gate vs. security advisory** — Know the difference: a gate blocks the pipeline (mandatory), an advisory reports findings without blocking (informational). Exam questions test when each is appropriate.

8. **Pre-commit vs. CI pipeline scans** — Pre-commit hooks run locally before the commit is created (earliest). CI pipeline scans run after a push to the remote (later but catches what pre-commit misses or is bypassed).

---

## Section 11: Study Checklist

Work through this checklist before attempting the quiz and lab.

- [ ] Define DevSecOps in your own words, distinguishing it from DevOps.
- [ ] Explain the shift-left principle with a specific cost-of-remediation example.
- [ ] List the three pillars of DevSecOps (People, Process, Technology) with one example under each.
- [ ] Map SAST, DAST, SCA, and secrets scanning to their correct pipeline stages.
- [ ] Explain the shared responsibility model: who owns what in DevSecOps.
- [ ] Read the OWASP DevSecOps Guideline introduction at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
- [ ] Complete the SDLC security mapping table in your notes.
- [ ] Review the SAST vs. DAST vs. SCA comparison table until you can reconstruct it from memory.
- [ ] Complete the Module 01 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
