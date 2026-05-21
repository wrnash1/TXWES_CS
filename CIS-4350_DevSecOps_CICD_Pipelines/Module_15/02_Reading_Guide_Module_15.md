# Reading Guide: Module 15 - Security Metrics and Dashboards in CI/CD

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 15 - Security Metrics and Dashboards in CI/CD**! This module covers how to measure, visualize, and communicate the security posture of a DevSecOps program using pipeline metrics, vulnerability trend data, and compliance dashboards. Security metrics close the feedback loop: they tell engineering and leadership whether the DevSecOps pipeline is actually reducing risk over time, and they provide the evidence base for compliance audits. You will learn the key DevSecOps metrics (MTTR, vulnerability backlog trends, pipeline gate pass rates) and how audit logs, signed commits, and build log validation support regulatory compliance. These topics appear on the CDP exam and are critical for program maturity assessment.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Compliance as Code**: The practice of expressing security and regulatory compliance requirements as executable, version-controlled policy code (Rego, OPA Gatekeeper Constraints, Conftest policies) that is enforced automatically in CI/CD pipelines and Kubernetes admission control. Compliance as Code transforms audit evidence from point-in-time snapshots into continuous, machine-verifiable assertions that every deployment met defined requirements.

* **Pipeline audit logs**: Immutable, structured records of every CI/CD pipeline execution — including trigger event, commit SHA, scan results, approval decisions, and deployment targets. Pipeline audit logs are the primary evidentiary artifact for DevSecOps compliance audits, proving that security gates ran and passed on every production deployment. Stored in tamper-evident centralized logging, they satisfy SOC 2, PCI-DSS, and ISO 27001 evidence requirements.

* **Signed commits**: Git commits that are cryptographically signed with a developer's GPG or SSH key, creating a verifiable chain of custody from source code change to production deployment. In a DevSecOps pipeline, requiring signed commits (enforced via branch protection rules) ensures that every commit in the production branch is attributable to a verified developer identity — supporting non-repudiation and supply chain integrity.

* **Build logs validation**: The process of verifying that pipeline build logs are complete, unmodified, and accurately reflect the steps that executed during a build. In compliance contexts, build log validation confirms that no pipeline steps were skipped, that scan tools ran to completion, and that exit codes accurately reflect scan outcomes — preventing log tampering that could falsely indicate a clean build.

---

### 2. Certification Exam Tips

* **Key DevSecOps Metrics**: The CDP exam tests knowledge of security metrics: Mean Time to Remediate (MTTR) CVEs, vulnerability backlog count and trend, pipeline gate failure rate, percentage of builds with CRITICAL findings, DAST finding resolution rate, secrets scan detection rate. Know what each metric measures and what an improving trend looks like.
* **DORA Metrics and Security**: DORA metrics (Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR) originally measured DevOps performance. In DevSecOps, Change Failure Rate includes security-caused rollbacks and Change Lead Time includes security review time. The CDP exam may ask how security gates affect DORA metric trends.
* **Audit Trail Requirements**: Know which artifacts constitute an audit trail for a regulated deployment: signed commit (developer identity), SAST scan result with pass/fail status, code review approval record, pipeline run ID, image digest pushed, and deployment timestamp. Together these prove the complete chain of custody from code change to production.
* **Study Resource**: The [OWASP DevSecOps Guideline — Metrics and Dashboards section](https://owasp.org/www-project-devsecops-guideline/) provides guidance on which security metrics to collect, how to visualize them, and how pipeline data feeds compliance reporting — directly relevant to CDP exam maturity and measurement questions.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/) section on security metrics and dashboards — covers which metrics meaningfully measure DevSecOps program effectiveness, how to build security dashboards from pipeline data, and how audit log data maps to compliance framework requirements.
* **Required Video**: Watch the compliance, audit, and metrics segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates verifying signed git commits, auditing pipeline logs for control compliance, and the structure of release approval workflows that generate compliant audit trails.

---

### Lab & Command Integration

In this week's hands-on lab, you will implement compliance measurement and audit controls by:

* **Verify signed git commits indicators**: Configure a GitHub repository to require commit signing, use `git log --show-signature` to verify signed commits are present, and confirm that the branch protection rule blocks unsigned commits from being merged to `main`.
* **Audit pipeline logs for control compliance checks**: Review a GitHub Actions workflow run's complete log output and identify: (a) which security scan steps ran, (b) their exit codes, (c) whether all required steps executed, and (d) whether any steps were skipped — documenting findings as a mock audit evidence record.
* **Draft release approval forms**: Based on the pipeline audit log from a successful build, fill out a mock release approval checklist documenting: pipeline run ID, commit SHA, SAST result, SCA result, container scan result, reviewer identity, approval timestamp, and deployed image digest.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how pipeline audit logs, signed commits, and compliance metrics together form a DevSecOps audit trail.
* [ ] Read the OWASP DevSecOps Guideline at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
* [ ] Watch the compliance and metrics segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the signed commit verification, pipeline log audit, and release approval form in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
