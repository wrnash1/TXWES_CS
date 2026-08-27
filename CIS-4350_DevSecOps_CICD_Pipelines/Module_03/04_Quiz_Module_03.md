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

---

### Question 11 (5 points)

Which GitHub Actions configuration correctly restricts the auto-generated `GITHUB_TOKEN` to read-only access across an entire workflow while allowing a single job to write security scan results?

- A) Set `permissions: read-all` at the workflow level and override with `permissions: security-events: write` in the specific job
- B) Set `permissions: write-all` at the workflow level and remove permissions from all other jobs
- C) Remove the `permissions` block entirely — GitHub Actions defaults to read-only
- D) Set `permissions: contents: read` per job in every job definition

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `write-all` grants broad write access to all scopes — this violates least-privilege and is the opposite of the goal.
  - C) The default is write-all in many repository configurations, not read-only; explicit `read-all` or scoped permissions are required.
  - D) Setting per-job permissions is redundant and error-prone; a workflow-level default with targeted job-level overrides is the recommended pattern.

---

### Question 12 (5 points)

A CI pipeline runs OWASP Dependency-Check with `--failOnCVSS 9.0`. A build includes a dependency with a CVE scored 8.9. What happens?

- A) The pipeline fails because 8.9 is close to the threshold
- B) The pipeline passes because 8.9 is below the 9.0 threshold
- C) The pipeline fails because any CVE above 7.0 automatically triggers failure
- D) Dependency-Check ignores scores below 9.5 by default

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The threshold is a hard numeric cutoff — 8.9 does not meet or exceed 9.0.
  - C) The 7.0 threshold is a separate, stricter configuration choice — it does not apply unless explicitly set.
  - D) Dependency-Check has no built-in 9.5 default; the default is to report all CVEs without failing unless `--failOnCVSS` is configured.

---

### Question 13 (5 points)

In GitHub Actions, what does `if: always()` on a step accomplish?

- A) It ensures the step runs on every branch, not just the default branch
- B) It makes the step run even if a previous step in the same job failed
- C) It runs the step only when the workflow was triggered manually
- D) It prevents the step from being skipped when the job uses a matrix strategy

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Branch filtering is controlled by the `on.push.branches` or `on.pull_request.branches` trigger configuration, not `if: always()`.
  - C) Manual triggers use `workflow_dispatch`; `always()` has nothing to do with trigger type.
  - D) Matrix strategy skipping is not what `always()` addresses — it applies to step execution within a single job instance.

---

### Question 14 (5 points)

Which of the following correctly describes the security concern with using `pull_request_target` instead of `pull_request` as a GitHub Actions trigger?

- A) `pull_request_target` cannot trigger scans against the PR branch, making it useless for security testing
- B) `pull_request_target` runs with write permissions and secrets access in the base repo context, allowing a malicious fork PR to exfiltrate secrets
- C) `pull_request_target` requires branch protection rules to be disabled before it can run
- D) `pull_request_target` only supports manual approval workflows and cannot run automated scans

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `pull_request_target` can access the PR branch code but the security concern is the opposite — too much access, not too little.
  - C) `pull_request_target` has no dependency on branch protection configuration.
  - D) `pull_request_target` supports full automated workflows — the risk is that it provides secrets to code from untrusted forks.

---

### Question 15 (5 points)

A GitLab CI pipeline uses `artifacts: reports: sast:` to expose scan results. What does this accomplish?

- A) It automatically remediates all SAST findings before the next stage runs
- B) It makes scan results visible in the GitLab Security Dashboard and Merge Request widget
- C) It uploads SARIF files to the GitHub Security tab
- D) It stores scan results in a separate protected branch for audit purposes

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) GitLab CI does not auto-remediate vulnerabilities — the artifact report only surfaces findings in the UI.
  - C) The GitHub Security tab is a GitHub-specific feature; GitLab uses its own Security Dashboard, not GitHub's tab.
  - D) Artifacts are stored in GitLab's artifact storage, not in a Git branch.

---

### Question 16 (5 points)

What problem does "alert fatigue" create in the context of CI security gates?

- A) It causes pipelines to run slower due to the large number of alerts being processed
- B) Developers begin ignoring or suppressing all findings when there are too many low-quality alerts, causing real issues to be missed
- C) It increases cloud compute costs because each alert triggers a separate pipeline run
- D) It prevents SARIF results from being uploaded to the GitHub Security tab

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Alert volume does not affect pipeline execution speed in a meaningful way.
  - C) Alerts from a scan tool do not trigger separate pipeline runs — they are part of the same run.
  - D) SARIF upload success is independent of alert count or quality.

---

### Question 17 (5 points)

In a GitHub Actions workflow, an action is pinned as `uses: actions/checkout@1e31de5234b9f8995739874a8ce0492dc87873e2`. What is the security implication compared to `uses: actions/checkout@v4`?

- A) The SHA-pinned version always uses an older, less secure codebase
- B) Tags like `v4` are mutable and can be redirected by a compromised maintainer; a commit SHA is immutable
- C) SHA pinning prevents the action from being cached, increasing pipeline runtime
- D) SHA pinning requires a special organization-level permission to use

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) SHA pinning locks a specific commit — it does not imply the code is older; it is the same code the tag pointed to at that time.
  - C) GitHub Actions runner caching operates on the action code content, not on whether a tag or SHA reference is used.
  - D) SHA pinning is available to all workflows regardless of organization settings.

---

### Question 18 (5 points)

Which configuration in a GitHub Actions workflow causes the workflow to fail if any job exits with a non-zero status code, even if subsequent jobs use `if: always()`?

- A) `continue-on-error: false` at the workflow level
- B) Each job exits with a non-zero code by default; the overall workflow status reflects the worst job status
- C) Setting `fail-fast: true` in the strategy block
- D) Adding `exit 1` at the end of every run step

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `continue-on-error` is a job-level setting that allows subsequent jobs to run despite failure — but the overall workflow status still reflects the failing job.
  - C) `fail-fast: true` applies to matrix strategies — it cancels remaining matrix jobs when one fails, but it does not affect workflow-level status reporting.
  - D) `exit 1` in every step is redundant; any non-zero exit from any step already fails the job by default.

---

### Question 19 (5 points)

A reusable workflow is defined in a repository called `org/security-workflows`. A consuming repository calls it with `uses: org/security-workflows/.github/workflows/sast.yml@main`. What is the primary governance benefit?

- A) The consuming repository's developers can modify the sast.yml file directly from their own repository
- B) The security team can update scanning rules and thresholds in one place and all consuming repositories inherit the change automatically
- C) The reusable workflow runs on the security team's private runners, reducing compute costs for application teams
- D) The calling repository's secrets are automatically shared with the reusable workflow

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Consuming repositories cannot modify files in `org/security-workflows` — that is the point of centralized governance.
  - C) Runner provisioning is independent of workflow reuse — the called workflow uses the caller's runner unless explicitly configured otherwise.
  - D) Secrets are NOT automatically shared with reusable workflows — they must be explicitly passed via `secrets: inherit` or individual `secrets:` mappings.

---

### Question 20 (5 points)

What is the primary purpose of uploading SARIF results to the GitHub Security tab in a CI pipeline?

- A) To trigger Dependabot to automatically create pull requests fixing the detected vulnerabilities
- B) To make static analysis and scan findings visible across repositories in a unified interface for triage and tracking
- C) To satisfy a GitHub Advanced Security license requirement for public repositories
- D) To convert SARIF results into GitHub Issues automatically

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Dependabot is triggered by dependency graph analysis, not SARIF uploads.
  - C) SARIF upload for public repositories is available in the free tier — a GitHub Advanced Security license is required for private repositories, not public ones.
  - D) SARIF upload populates the Security tab code scanning alerts view, not GitHub Issues.
