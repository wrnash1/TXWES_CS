# Reading Guide: Module 02 - Version Control with Git and GitHub

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 02 - Version Control with Git and GitHub**! This module covers Git as the foundation of every modern CI/CD pipeline. You will learn how Git branching strategies, commit hooks, and repository configurations directly affect pipeline security and code quality. Understanding how automation runners are triggered by Git events — pushes, pull requests, tags — and how pre-commit hooks enforce linting and security checks before code enters the shared repository is essential for the CDP exam and for building secure pipelines in practice.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Automation runners**: Compute environments (GitHub-hosted or self-hosted) that execute CI/CD pipeline jobs when triggered by a Git event. Runners check out the repository, install dependencies, and execute each defined step — including security scans — in an isolated environment, ensuring builds are reproducible and tamper-resistant.

* **Local commit hooks**: Scripts stored in a repository's `.git/hooks/` directory that execute automatically at specific Git lifecycle points (pre-commit, commit-msg, pre-push). In DevSecOps, pre-commit hooks run linters, secret scanners, and unit tests locally before code even leaves the developer's machine, providing the earliest possible shift-left security gate.

* **Git triggers**: Event-driven conditions in CI/CD workflow files (e.g., `on: push`, `on: pull_request`, `on: release`) that define when a pipeline run is initiated. Correctly scoping triggers prevents unnecessary builds while ensuring security gates fire on every relevant code change.

* **Linting steps**: Automated code quality checks that analyze source files for syntax errors, style violations, and common anti-patterns using tools like ESLint, Flake8, or Pylint. In a DevSecOps pipeline, linting is typically the first job in the CI workflow, failing fast on formatting issues before costlier security scans run.

---

### 2. Certification Exam Tips

* **Hook vs. Pipeline Gate**: The CDP exam distinguishes between local git hooks (run on the developer's machine, bypassable with `--no-verify`) and remote pipeline gates (enforced by the CI server, not bypassable by developers). Know that pipeline gates are the authoritative security enforcement point.
* **Branch Protection Rules**: GitHub branch protection rules (require status checks, require reviews, restrict who can push) are a key DevSecOps control. The exam tests knowledge of how these rules enforce security gates before code merges to main.
* **Trigger Scoping**: Know the difference between `push` triggers (runs on every commit to any branch) and `pull_request` triggers (runs when a PR is opened or updated). Security scans are most commonly gated on `pull_request` to prevent merging unscanned code.
* **Study Resource**: The [GitHub Actions documentation](https://docs.github.com/en/actions) provides the official reference for workflow syntax, trigger events, and runner configuration — essential reading for CDP exam workflow questions.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [GitHub Actions Quickstart Guide](https://docs.github.com/en/actions/quickstart) — the official GitHub documentation explaining workflow files, trigger events, jobs, and steps. This is the authoritative reference for YAML pipeline syntax used on the CDP exam.
* **Required Video**: Watch the Git and CI/CD fundamentals segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — covers Git branching, commit workflows, and how GitHub Actions workflows are structured and triggered.

---

### Lab & Command Integration

In this week's hands-on lab, you will apply version control and CI concepts by:

* **Configure a local git pre-commit hook running code linters**: Write a `.git/hooks/pre-commit` shell script that invokes a linter (e.g., `flake8` or `eslint`) and exits with a non-zero code on violations to block the commit.
* **Analyze lint configuration files**: Examine `.flake8`, `.eslintrc`, or `pyproject.toml` lint configuration files to understand how rules are enabled, disabled, and scoped to specific directories.
* **Test local commit constraints**: Intentionally introduce a style violation and verify the pre-commit hook blocks the commit; then fix the violation and confirm the commit succeeds.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how each concept connects to pipeline automation.
* [ ] Read the GitHub Actions Quickstart at [https://docs.github.com/en/actions/quickstart](https://docs.github.com/en/actions/quickstart).
* [ ] Watch the Git and CI/CD segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the pre-commit hook configuration in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
