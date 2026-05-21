# Reading Guide: Module 03 - CI/CD Concepts – Jenkins, GitHub Actions, GitLab CI

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 03 - CI/CD Concepts – Jenkins, GitHub Actions, GitLab CI**! This module examines the three most common CI/CD platforms in enterprise DevSecOps environments and how each is configured to enforce security gates. You will learn how GitHub Actions YAML workflows, Jenkins declarative pipelines, and GitLab CI `.gitlab-ci.yml` files structure jobs, steps, and security scan stages. Understanding runner environments, trigger events, and pipeline security gates across these platforms is directly tested on the CDP certification exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **GitHub Actions**: A native CI/CD and workflow automation platform integrated directly into GitHub repositories. Workflows are defined in YAML files under `.github/workflows/` and are triggered by repository events (push, pull_request, schedule). GitHub Actions is widely used in DevSecOps pipelines because security scanning steps can be added as reusable actions from the GitHub Marketplace.

* **YAML syntax**: The human-readable data serialization format used to define CI/CD pipeline configurations across GitHub Actions, GitLab CI, and Kubernetes manifests. In pipeline files, YAML structures jobs, steps, environment variables, and trigger conditions using indentation-based hierarchy — errors in indentation cause pipeline failures, making YAML linting (`yamllint`) an important pipeline quality check.

* **Runner environments**: The operating system and tool context in which pipeline jobs execute. GitHub Actions offers ubuntu-latest, windows-latest, and macos-latest hosted runners; GitLab CI uses Docker-based runners; Jenkins uses agent nodes. The runner environment determines which tools (Docker, scanners, compilers) are available without installation steps.

* **Steps**: Individual sequential tasks within a CI/CD job, each running a shell command or reusable action. In a security-focused pipeline, steps might include: checkout code, run linter, run SAST scan, build Docker image, run SCA scan, upload results. Each step's exit code determines whether the pipeline continues or fails.

* **Jobs**: Logical groupings of steps that run on a single runner. Multiple jobs can run in parallel (e.g., a `lint` job and a `sast` job simultaneously) or sequentially with `needs:` dependencies. Separating security checks into distinct jobs allows parallel execution and clearer failure attribution.

* **Trigger events**: The repository or schedule conditions that cause a pipeline run to start. In DevSecOps, security scans are typically triggered on `pull_request` (to gate merges) and `push` to protected branches. Understanding trigger scoping prevents security checks from being inadvertently skipped.

---

### 2. Certification Exam Tips

* **Pipeline File Location**: Know the canonical locations — GitHub Actions: `.github/workflows/*.yml`; GitLab CI: `.gitlab-ci.yml` at repository root; Jenkins: `Jenkinsfile` at repository root. The CDP exam tests whether you can identify the correct configuration file for each platform.
* **Security Stage Placement**: The standard DevSecOps pipeline order is: lint → SAST → build → SCA → container scan → DAST → deploy. Know why each security stage is placed where it is and what it would mean to move it later in the pipeline.
* **Reusable Actions vs. Shell Commands**: GitHub Actions allows calling pre-built marketplace actions (e.g., `actions/checkout@v4`, `github/codeql-action/analyze@v3`) as single steps. The CDP exam may ask about the security implications of using third-party actions (supply chain risk) versus inline shell scripts.
* **Study Resource**: The [GitHub Actions Workflow Syntax reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) documents every available keyword (`on`, `jobs`, `steps`, `uses`, `run`, `env`, `secrets`) — review this alongside the freeCodeCamp video for the complete picture.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [GitHub Actions Workflow Syntax documentation](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) — the official reference for all YAML keywords used in GitHub Actions workflow files. Focus on the `on`, `jobs`, `steps`, `uses`, and `secrets` sections.
* **Required Video**: Watch the GitHub Actions workflow segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates writing, triggering, and reading results from GitHub Actions pipeline runs with security scan steps included.

---

### Lab & Command Integration

In this week's hands-on lab, you will build and trigger a working CI/CD pipeline by:

* **Write a GitHub Actions workflow script using YAML**: Create a `.github/workflows/ci.yml` file with at least three jobs: lint, test, and a placeholder security scan step triggered on `pull_request`.
* **Configure runner triggers on git push events**: Add a second workflow triggered on `push` to `main` that runs a build step, demonstrating the difference between push-triggered and pull-request-triggered pipeline behavior.
* **Verify build execution logs**: Push a commit, navigate to the Actions tab in GitHub, and read the step-by-step execution logs to identify which steps passed, which failed, and what output each step produced.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how each concept maps to a specific YAML keyword or pipeline concept.
* [ ] Read the GitHub Actions Workflow Syntax reference at [https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
* [ ] Watch the GitHub Actions segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the workflow YAML creation and trigger testing in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
