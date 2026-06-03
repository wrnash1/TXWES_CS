# Quiz: Module 03 — Continuous Integration and Security Gates

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Submit answers through the Canvas quiz interface.

---

## Question 1

In a GitHub Actions workflow, which keyword declares that one job must complete successfully before another job begins?

- A) `depends`
- B) `after`
- C) `needs`
- D) `requires`

### Q1 — Correct Answer: C

### Q1 — Distractor Analysis

- A) `depends` is not a valid GitHub Actions keyword — it is used in other orchestration tools but not here.
- B) `after` is not a GitHub Actions workflow keyword.
- D) `requires` is not a valid GitHub Actions keyword, though it sounds intuitive.

---

## Question 2

What is the purpose of the `permissions: contents: read` setting at the top of a GitHub Actions workflow?

- A) It restricts which branches the workflow can check out
- B) It limits the GITHUB_TOKEN to read-only repository access, following the principle of least privilege
- C) It prevents the workflow from running on pull requests from forks
- D) It requires code review approval before the workflow can run

### Q2 — Correct Answer: B

### Q2 — Distractor Analysis

- A) Branch checkout permissions are controlled by `ref` in the checkout step, not the `permissions` block.
- C) Fork pull request behavior is controlled by workflow trigger configuration, not the `permissions` block.
- D) Required reviewers are a branch protection feature, not a workflow-level permission.

---

## Question 3

A CVSS quality gate is configured with `--failOnCVSS 7`. Which vulnerability scores cause the pipeline to fail?

- A) Only scores of exactly 7.0
- B) Scores of 7.0 and above (High and Critical)
- C) Scores below 7.0 (Low and Medium)
- D) All scores including 0.0

### Q3 — Correct Answer: B

### Q3 — Distractor Analysis

- A) The threshold applies to 7.0 and above, not exactly 7.0 — it is a minimum threshold, not an exact match.
- C) The gate fails on scores at or above the threshold, not below it.
- D) Scores of 0.0 are "None" severity and would not trigger a failure gate set at 7.0.

---

## Question 4

What is SARIF and why is it important in DevSecOps pipelines?

- A) A secret management format for storing API keys in CI/CD environments
- B) A JSON schema standard for security tool output, enabling platform-agnostic result consumption
- C) A branching strategy that separates security fixes from feature development
- D) A type of signed container image that has been verified by a trusted registry

### Q4 — Correct Answer: B

### Q4 — Distractor Analysis

- A) SARIF has nothing to do with secret management — it is a reporting format for scan results.
- C) SARIF is not a branching strategy — it is a data format standard.
- D) Signed container images use Docker Content Trust or Sigstore, not SARIF.

---

## Question 5

Your team uses GitHub Actions. A developer modifies `.github/workflows/secure-ci.yml` to remove the Semgrep security scan job. What control prevents this change from being merged without security team review?

- A) Branch protection requiring signed commits
- B) A CODEOWNERS entry mapping `.github/workflows/` to the security team
- C) The `permissions: security-events: write` setting in the workflow
- D) The gitleaks pre-commit hook

### Q5 — Correct Answer: B

### Q5 — Distractor Analysis

- A) Signed commits prove authorship but do not require a specific reviewer for pipeline file changes.
- C) `security-events: write` is a permission for uploading SARIF results — it does not control who can modify the workflow file.
- D) The gitleaks pre-commit hook scans for secrets in code — it does not enforce reviewer requirements.

---

## Question 6

In GitLab CI, the `include: template: Security/SAST.gitlab-ci.yml` directive provides which benefit?

- A) It creates a dedicated SAST runner with more CPU resources
- B) It imports GitLab's pre-configured SAST job definitions for multiple language analyzers
- C) It scans the `.gitlab-ci.yml` file itself for security misconfigurations
- D) It requires security team approval before the SAST job runs

### Q6 — Correct Answer: B

### Q6 — Distractor Analysis

- A) The `include` directive imports configuration — it does not provision additional compute resources.
- C) The SAST template scans application source code, not the CI configuration file.
- D) Job approval gates are configured separately in GitLab's approval rules, not via the include directive.

---

## Question 7

Which trigger configuration ensures a full security scan suite runs on every pull request to the main branch but only a fast secrets scan runs on feature branch pushes?

- A) Configure two separate workflow files with different `on` trigger blocks
- B) Use a single workflow with `if` conditions or path filters per job
- C) Run only the full suite on all triggers — partial scanning creates gaps
- D) Schedule security scans nightly instead of on push events

### Q7 — Correct Answer: A

### Q7 — Distractor Analysis

- B) While `if` conditions can work, separate workflow files provide clearer separation and are the recommended pattern for significantly different scan scopes.
- C) Running the full suite on every feature branch push creates a slow developer feedback loop and is not recommended.
- D) Nightly scheduling misses the shift-left goal of giving developers immediate feedback on their changes.

---

## Question 8

Pinning a GitHub Actions action to a commit SHA (rather than a tag like `@v4`) provides which security benefit?

- A) It speeds up the action because the runner does not need to resolve the tag
- B) It prevents supply chain attacks where an attacker updates a mutable tag to point to malicious code
- C) It grants the action elevated permissions to access repository secrets
- D) It ensures the action runs only on pull requests, not on direct pushes

### Q8 — Correct Answer: B

### Q8 — Distractor Analysis

- A) Tag resolution vs. SHA resolution has negligible performance difference — this is not the security rationale.
- C) Action permissions are controlled by the `permissions` block, not by how the action is versioned.
- D) SHA pinning does not restrict the trigger type — that is controlled by the `on` block.

---

## Question 9

What is the primary security purpose of a reusable GitHub Actions workflow shared from a central `security-workflows` repository?

- A) Reusable workflows run faster because they share compute resources across repositories
- B) Reusable workflows allow teams to skip security scans on low-risk branches
- C) Centralized security gates prevent individual teams from modifying or disabling scan configurations
- D) Reusable workflows automatically rotate secrets used by scanning tools

### Q9 — Correct Answer: C

### Q9 — Distractor Analysis

- A) Reusable workflows do not share compute — each invocation provisions its own runner.
- B) Reusable workflows enforce security gates consistently — they do not provide a mechanism to skip scans.
- D) Secret rotation is the responsibility of secrets management tools like Vault, not CI workflow configuration.

---

## Question 10

In the five-layer CI pipeline model (Source, Build, Test, Scan, Report), which layer is the primary enforcement point for security quality gates?

- A) Source
- B) Build
- C) Scan
- D) Report

### Q10 — Correct Answer: C

### Q10 — Distractor Analysis

- A) The Source layer checks out code and validates credentials — it does not run security analysis tools.
- B) The Build layer compiles code and installs dependencies — security scanning does not typically occur here.
- D) The Report layer publishes results but is typically non-blocking — it does not enforce pass/fail gates.

---

Quiz — Module 03 | CIS-4350 | Texas Wesleyan University | Professor Nash
