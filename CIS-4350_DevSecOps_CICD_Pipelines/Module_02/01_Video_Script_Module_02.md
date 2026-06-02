# Video Script: Module 02 - Version Control with Git and GitHub

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 02 — Version Control with Git and GitHub"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. In Module 01 we covered the DevSecOps mindset — the why. Now we're going to cover the foundation that makes every DevSecOps pipeline possible: version control with Git and GitHub.

Every security automation we will study in this course — SAST scans, SCA checks, secrets scanning, container builds — is triggered by a Git event. You cannot understand DevSecOps pipeline automation without understanding Git deeply. By the end of this video you'll be able to describe the Git workflow for a secure development team, configure branch protection rules, implement pre-commit hooks for secrets detection, and write a basic GitHub Actions workflow triggered on pull request."

---

### [01:30 - 05:30] Git Security Fundamentals

**Visual:** Diagram of Git object model — commits, trees, blobs

**Audio:**

"Let's start with what Git is and why it matters for security. Git is a distributed version control system. Every developer has a complete copy of the repository history. Every commit is a cryptographically addressed object — Git uses SHA-1 hashing to identify every commit, tree, and blob in the repository. This means Git history is tamper-evident: if you alter a past commit, all downstream commit hashes change, which is detectable.

From a security standpoint, this matters in two ways. First, Git history is forensically valuable — you can trace exactly when a vulnerability was introduced, who introduced it, and what other changes came with it. Second, Git history is permanent — if a secret is committed and pushed to a remote repository, even deleting it in a subsequent commit leaves it in history. Anyone who cloned the repository before the deletion already has it. This is why pre-commit secrets scanning is so critical: once a secret is in Git history, the only correct remediation is to rotate the credential and do a full history rewrite, which is expensive and disruptive.

The core Git workflow in a DevSecOps context is: developer creates a feature branch, makes commits, opens a pull request, automated pipeline checks run, a reviewer approves, and the branch merges into main. Each of these steps has security implications we will cover today."

---

### [05:30 - 10:00] Branch Protection and Security Gates

**Visual:** GitHub repository settings screen showing branch protection configuration

**Audio:**

"Branch protection rules are the foundation of pipeline-enforced security on GitHub. Let's walk through the key settings.

Navigate to your repository Settings, then Branches, then Add a branch protection rule for your main branch.

The first critical setting is 'Require status checks to pass before merging.' This is what makes your CI/CD security scans mandatory — not optional. You list the specific pipeline job names that must succeed: your SAST scan job, your SCA dependency check, your secrets scanner. If any of these jobs fail, the merge button is grayed out and GitHub prevents the merge.

The second setting is 'Require a pull request before merging.' This prevents anyone — including repository administrators — from pushing directly to main without going through the PR and automated check process. Direct pushes to main bypass all pipeline security checks. This rule closes that gap.

'Require signed commits' is a best practice for regulated environments. GPG-signed commits cryptographically verify that a commit was actually made by the claimed author. This prevents commit author spoofing.

'Require linear history' forces all merges to use squash or rebase strategies, keeping the history readable and traceable.

These rules together form a policy layer on top of your pipeline. The pipeline does the automated security checking; the branch protection rules enforce that the pipeline must be satisfied before code can reach main."

---

### [10:00 - 15:00] Pre-Commit Hooks: The Earliest Shift-Left Gate

**Visual:** Terminal showing pre-commit hook installation and execution

**Audio:**

"Now let's look at pre-commit hooks — the earliest possible shift-left security control. A pre-commit hook is a shell script stored in `.git/hooks/pre-commit` that executes when the developer runs `git commit`, before the commit object is created. If the hook exits with a non-zero code, the commit is aborted.

**[SHOW CODE]**

You can install the `pre-commit` framework, which manages hook configurations declaratively:

```bash
pip install pre-commit
```

Then create a `.pre-commit-config.yaml` file in your repository root:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
        name: Detect secrets with Gitleaks

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: detect-private-key
```

Install the hooks into the local Git repository:

```bash
pre-commit install
```

Now every `git commit` automatically runs Gitleaks and the standard hooks. A developer trying to commit a file containing an AWS access key pattern, a private key header, or a high-entropy string matching a known credential format will see the commit blocked with a clear error message.

The critical limitation: pre-commit hooks run on the developer's local machine and can be bypassed with `git commit --no-verify`. This is why you also need the same secrets scan in your CI pipeline as a server-side, bypass-resistant gate. Defense in depth: local hook for early feedback, CI pipeline hook for enforcement."

---

### [15:00 - 20:00] GitHub Actions: Writing a Secure CI Workflow

**Visual:** GitHub Actions workflow YAML in code editor

**Audio:**

"GitHub Actions is GitHub's built-in CI/CD automation system. Workflows are defined in YAML files stored in `.github/workflows/`. They are triggered by Git events — push, pull request, schedule, or manual dispatch.

**[SHOW CODE]**

Here is a production-quality GitHub Actions workflow that runs security checks on every pull request targeting main:

```yaml
name: Security Checks on PR

on:
  pull_request:
    branches:
      - main

permissions:
  contents: read
  security-events: write

jobs:
  secrets-scan:
    name: Secrets Detection
    runs-on: ubuntu-latest
    steps:
      - name: Checkout full history
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Gitleaks secrets scan
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  sast-scan:
    name: Static Analysis
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Semgrep SAST
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/owasp-top-ten

  dependency-scan:
    name: Dependency Vulnerability Check
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'my-app'
          path: '.'
          format: 'SARIF'
          out: 'reports'
```

Let me explain the key security design decisions in this workflow.

`permissions: contents: read` — the principle of least privilege applied to GitHub Actions. The workflow only needs to read the code. Scoping permissions prevents a compromised action from writing back to the repository.

`fetch-depth: 0` in the Gitleaks step fetches the full Git history, not just the latest commit. This is critical for secrets scanning — Gitleaks needs to scan all commits in the PR, not just the final state, because a secret could have been added and then deleted within the PR's commit history while still existing in that history.

`on: pull_request` with `branches: [main]` — this fires on every PR opened against or updated for the main branch. No code merges to main without these checks passing."

---

### [20:00 - 22:30] Exam Alignment and Key Takeaways

**Visual:** Exam objective bullets on screen

**Audio:**

"For the DevSecOps Professional exam, here is what you must know from this module.

Know the Git workflow: feature branch, commit, pull request, pipeline checks, review, merge. Know that direct pushes to main bypass pipeline controls and must be blocked by branch protection rules.

Know the difference between pre-commit hooks and CI pipeline scans: hooks run locally and can be bypassed with --no-verify; CI pipeline scans are server-side and cannot be bypassed for PR merging purposes.

Know the `pull_request` trigger in GitHub Actions and why it is the correct trigger for security gate workflows — it fires before merge, allowing you to block insecure code.

Know the `permissions` block — least privilege applied to workflow tokens. Know that `fetch-depth: 0` is required for full-history secrets scanning.

In the next module we will expand from GitHub Actions to the broader CI/CD landscape: Jenkins and GitLab CI. Complete the lab — which includes writing a real GitHub Actions workflow with security gates — before moving on."

---

### [22:30 - End] Closing

**Visual:** Instructor on camera

**Audio:**

"Module 02 complete. Git history is permanent — secrets committed and pushed must be rotated. Branch protection rules make pipeline checks mandatory. Pre-commit hooks provide the earliest shift-left feedback but must be paired with CI pipeline enforcement. GitHub Actions workflows use YAML, trigger on Git events, and should follow least-privilege permissions.

See you in Module 03."
