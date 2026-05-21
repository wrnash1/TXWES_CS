# Reading Guide: Module 13 – Continuous Integration and DevOps Basics

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Introduction

Welcome to **Module 13 – Continuous Integration and DevOps Basics**! Continuous Integration (CI) and DevOps practices are the technical infrastructure that makes Scrum's "potentially releasable Increment every Sprint" promise achievable in practice. Without automated build-test-deploy pipelines, delivering a high-quality Increment in 1–2 weeks is nearly impossible at scale.

The PSM I expects understanding of how CI/CD practices support Scrum's empirical pillars — particularly how automation enables the team to inspect and adapt rapidly. This module bridges Scrum theory and the DevOps engineering practices that enable it.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Continuous Integration (CI):** A software engineering practice in which developers integrate their code changes into a shared mainline branch frequently — ideally multiple times per day. Each integration triggers an automated build and test run that quickly detects compilation failures and test regressions. CI reduces the "integration hell" of merging long-lived feature branches.

* **Continuous Delivery (CD):** An extension of CI that automatically deploys all code changes that pass automated tests to a staging environment, keeping the software in a deployable state at all times. The release to production may require a manual approval step but the artifact is always ready.

* **Continuous Deployment:** An advanced practice where every change that passes all automated tests is automatically deployed to production without any manual intervention. It requires extremely high automated test coverage and robust monitoring to detect production issues quickly.

* **CI/CD pipeline:** The automated sequence of steps that code changes move through from commit to deployment — typically including: source control, automated build, unit tests, integration tests, code quality checks, staging deployment, and production release. Pipelines are defined as code (YAML or similar) and run on CI servers such as GitHub Actions, GitLab CI, or Jenkins.

* **Infrastructure as Code (IaC):** The practice of managing and provisioning computing infrastructure (servers, networks, databases) through machine-readable configuration files rather than manual processes. Tools like Terraform and Ansible enable teams to version-control and reproduce environments consistently — a core DevOps enabler.

---

### 2. Certification Exam Tips

* **PSM I Focus — CI supports the Definition of Done:** A Scrum Team's Definition of Done commonly includes "all automated tests pass" and "code integrated to main branch." CI enforces these conditions automatically for every commit, making the Definition of Done verifiable and objective rather than manual.
* **Scenario Trap — CI vs. Continuous Deployment:** Questions sometimes blur CI, Continuous Delivery, and Continuous Deployment. Know the distinctions: CI = automatic build + test on commit; Continuous Delivery = always deployable to staging; Continuous Deployment = automatically deployed to production. Each is a superset of the previous.
* **DevOps and Scrum complement each other:** DevOps is not a replacement for Scrum. DevOps provides the technical pipeline; Scrum provides the organizational framework. A Scrum Team with DevOps practices delivers higher-quality Increments more reliably than one without them.
* **The "Done" Increment requires CI:** If a Scrum Team's Definition of Done requires passing a full automated test suite and integration into a shared build, then CI is not optional — it is the mechanism by which the DoD is verified at scale.
* **Study Resource:** [The Twelve-Factor App methodology](https://12factor.net/) provides free, concise principles for building software-as-a-service apps that are inherently CI/CD compatible. Also read [GitHub Actions quickstart](https://docs.github.com/en/actions/quickstart) for a hands-on CI pipeline example.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** [Continuous Integration — Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html) — the seminal free article that defines CI, its practices, and its relationship to automated testing and Agile teams.
* **Required Video:** [CI/CD Pipeline Explained in Simple Terms – TechWorld with Nana](https://www.youtube.com/watch?v=0y6nzovAF14) — visual walkthrough of a complete CI/CD pipeline from code commit to production deployment. (~11 min)

---

### Lab & Command Integration

In this week's hands-on lab, you will:

* **Create a local CI simulation:** Write a shell script that runs linting (flake8 or equivalent), executes the pytest test suite, and reports pass/fail status — simulating what a CI server does on each commit.
* **Map a CI/CD pipeline:** Using a provided application description, draw a pipeline diagram with at least five stages (commit, build, unit test, integration test, staging deploy) and label the tool that would handle each stage.
* **Identify pipeline failures:** Review three provided CI pipeline logs and identify the stage at which each pipeline failed, the most likely cause, and the corrective action the development team should take.

---

### 3. Study Checklist

* [ ] Read the Martin Fowler Continuous Integration article.
* [ ] Be able to distinguish CI, Continuous Delivery, and Continuous Deployment without notes.
* [ ] Understand how CI enforces the automated testing requirement in a Scrum Definition of Done.
* [ ] Watch the required video and trace a code change from commit through to deployment in the pipeline shown.
* [ ] Proceed to the weekly hands-on lab activity.
