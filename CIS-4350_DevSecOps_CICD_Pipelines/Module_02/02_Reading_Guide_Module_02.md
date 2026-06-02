# Reading Guide: Module 02 - Version Control with Git and GitHub

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 02 establishes version control as the triggering mechanism for all DevSecOps pipeline automation. Every SAST scan, SCA check, secrets detection run, and container build in subsequent modules is initiated by a Git event. This reading guide covers Git security fundamentals, branch protection configuration, pre-commit hooks, and GitHub Actions workflow design — all of which appear on the DevSecOps Professional certification exam.

---

## Section 1: High-Yield Glossary

**Git** — A distributed version control system where every developer has a complete copy of the repository and its history. Commits are identified by SHA hashes, making history tamper-evident.

**Repository** — A Git-tracked directory containing project source code, configuration files, and the complete commit history. Repositories may be local (on a developer's machine) or remote (on GitHub, GitLab, Bitbucket).

**Branch** — A lightweight pointer to a specific commit. Feature branches allow developers to work on changes in isolation from the main codebase. In DevSecOps, the main branch is protected and receives code only through reviewed, pipeline-checked pull requests.

**Pull request (PR)** — A request to merge a feature branch into the main branch. The PR is the standard checkpoint for automated security scanning: pipeline jobs run against the PR's changes, and branch protection rules can require those jobs to pass before merging is allowed.

**Pre-commit hook** — A shell script stored in `.git/hooks/pre-commit` that executes before `git commit` finalizes. If the script exits non-zero, the commit is aborted. Pre-commit hooks provide the earliest shift-left security gate — on the developer's local machine before code reaches the remote repository.

**Branch protection rule** — A GitHub repository setting that enforces policies on a protected branch. Key policies include: require status checks to pass before merging, require a pull request before merging (no direct pushes), require signed commits, and require a minimum number of approving reviews.

**GitHub Actions** — GitHub's built-in CI/CD automation platform. Workflows are defined in YAML files under `.github/workflows/` and are triggered by Git events (push, pull_request, schedule, workflow_dispatch).

**Workflow** — A GitHub Actions automation definition. Each workflow has a trigger (on:), one or more jobs, and each job contains sequential steps. Multiple jobs in a workflow run in parallel by default unless dependencies are defined with `needs:`.

**Runner** — The compute environment where a GitHub Actions job executes. GitHub provides hosted runners (ubuntu-latest, windows-latest, macos-latest). Organizations can also run self-hosted runners on their own infrastructure for compliance or performance reasons.

**Status check** — A pass/fail result posted to a pull request by a CI/CD job. Branch protection rules can require specific status checks to pass before a PR can be merged, making them the enforcement mechanism for pipeline security gates.

**Gitleaks** — An open-source secrets detection tool that scans Git repositories and commit history for hardcoded credentials using regex patterns and entropy analysis. Used in both pre-commit hooks and CI pipelines.

**GITHUB_TOKEN** — An automatically generated token available to GitHub Actions workflows. It has scoped permissions to the current repository. Best practice is to restrict its permissions to only what the workflow requires using the `permissions:` block.

**Signed commit** — A Git commit that includes a GPG cryptographic signature verifying the committer's identity. Signed commits prevent commit author spoofing and provide non-repudiation for code changes.

**fetch-depth** — A parameter in `actions/checkout` controlling how many commits of history are fetched. Setting `fetch-depth: 0` fetches the complete history, which is required for secrets scanners to check all commits in a PR rather than just the current file state.

---

## Section 2: Git Security Workflow Reference

The following table maps the standard Git collaborative workflow to the security concern and control at each step.

| Workflow Step | Security Concern | DevSecOps Control |
|---|---|---|
| Developer writes code locally | Hardcoded credentials, insecure patterns | IDE security plugins (e.g., Semgrep IDE) |
| git add / git commit | Secret in staged file | Pre-commit hook (Gitleaks, detect-private-key) |
| git push to remote branch | Secret bypasses local hook | CI pipeline secrets scan on push |
| Pull request opened | Insecure code, vulnerable deps | SAST + SCA pipeline jobs as required status checks |
| Code review | Logic flaws, architecture risk | Human security review (security champion) |
| Merge to main | Policy enforcement | Branch protection required status checks |
| Release tag | Artifact provenance | Signed tags, SBOM generation |

---

## Section 3: Branch Protection Configuration Reference

The following settings should be applied to the main (or master) branch of any production repository in a DevSecOps environment.

| Setting | Purpose | Risk if Disabled |
|---|---|---|
| Require pull request before merging | Forces all changes through the PR and review process | Developers can push directly to main, bypassing all pipeline checks |
| Require status checks to pass | Makes CI/CD security scan jobs mandatory | Pipeline failures are informational only; broken or insecure code can merge |
| Require branches to be up to date | PR must include latest main before merging | Security fixes merged to main are not present when PR is checked |
| Require signed commits | Verifies committer identity cryptographically | Commit author can be spoofed |
| Require linear history | Enforces squash or rebase merges | Complex merge commits obscure the history of individual changes |
| Include administrators | Protection rules apply to admins too | Admins can bypass security gates |

---

## Section 4: GitHub Actions Workflow Structure Reference

A GitHub Actions workflow file has the following structure:

```yaml
name:            # Workflow display name in the GitHub UI
on:              # Trigger events (push, pull_request, schedule, etc.)
permissions:     # Token permissions — use least privilege
env:             # Workflow-level environment variables
jobs:
  job-name:
    runs-on:     # Runner OS (ubuntu-latest, windows-latest, macos-latest)
    steps:
      - name:    # Step display name
        uses:    # Pre-built Action from the Actions Marketplace
        with:    # Input parameters for the Action
        run:     # Shell command to execute directly
        env:     # Step-level environment variables
```

Key security design rules for workflow files:

- Set `permissions:` to the minimum required scope. Default to `contents: read`.
- Never print secrets to the workflow log with `echo` or `run: env`.
- Pin Actions to a specific commit SHA rather than a mutable tag when security is critical.
- Use `GITHUB_TOKEN` rather than personal access tokens where possible.
- Store all credentials and API keys in GitHub Secrets, never in the workflow YAML file.

---

## Section 5: CI/CD Pipeline Stage Comparison

| Dimension | Pre-commit Hook | CI Pipeline Job | Branch Protection Rule |
|---|---|---|---|
| Execution location | Developer's local machine | GitHub-hosted or self-hosted runner | GitHub server-side policy |
| Can be bypassed? | Yes (--no-verify) | No (for PR merge blocking) | No (enforced by GitHub) |
| Trigger | git commit | Push or pull_request event | PR merge attempt |
| Latency | Immediate (seconds) | 1-5 minutes typically | Enforced after CI completes |
| Purpose | Earliest feedback | Automated security gate | Policy enforcement |

---

## Section 6: SAST vs. DAST vs. SCA Comparison

| Dimension | SAST | DAST | SCA |
|---|---|---|---|
| Full name | Static Application Security Testing | Dynamic Application Security Testing | Software Composition Analysis |
| Requires running application | No | Yes | No |
| Primary target | First-party source code | Running application endpoints | Third-party dependencies |
| Pipeline stage | Commit / Pull request | Staging | Build |
| Finds | Insecure code patterns, injection flaws | Runtime flaws, auth issues, config errors | Known CVEs in libraries |
| Representative tools | Semgrep, SonarQube, Checkmarx | OWASP ZAP, Burp Suite Enterprise | Snyk, OWASP Dependency-Check, Grype |

---

## Section 7: Docker Security Best Practices Reference

These practices appear in exam questions across multiple modules.

- Use minimal base images such as Alpine or distroless to reduce attack surface.
- Never run containers as root. Use the `USER` directive in the Dockerfile.
- Use multi-stage builds to exclude build tools and source code from the final image.
- Pin base image versions with a digest rather than a mutable tag.
- Scan images with Trivy or Grype before pushing to a registry.
- Store all secrets in environment variables injected at runtime, never baked into image layers.

---

## Section 8: Secrets Rotation Reference

- Static credentials hardcoded in code or config files must never be used in production.
- Secrets belong in dedicated management systems: HashiCorp Vault, AWS Secrets Manager, GitHub Secrets.
- Rotation intervals: database passwords every 30-90 days; API keys on compromise or periodically.
- If a secret is committed to Git history, rotating it is mandatory — the old value is permanently accessible in history.
- Automated rotation via secrets management platforms eliminates the human error risk of manual rotation.

---

## Section 9: Required Reading

Complete the following before attempting the quiz.

- Read the OWASP DevSecOps Guideline section on secrets management and secure coding at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).

---

## Section 10: DevSecOps Professional Exam Tips

1. **Pre-commit vs. CI pipeline** — Know that pre-commit hooks run locally and can be bypassed with `--no-verify`. CI pipeline scans are server-side and cannot be bypassed for branch protection purposes. Both are needed; they complement each other.

2. **fetch-depth: 0** — This GitHub Actions checkout parameter appears in exam questions about secrets scanning. Full history is required to scan every commit in a PR, not just the latest file state.

3. **permissions block** — Know that GitHub Actions workflows should use `permissions: contents: read` by default. Overly permissive tokens (write-all) are a common exam distractor representing a security misconfiguration.

4. **Branch protection required status checks** — Know that listing a job name under required status checks makes it mandatory for merging. If the job is not listed, it is optional regardless of its pass/fail result.

5. **pull_request trigger** — Know that `on: pull_request` fires when a PR is opened, updated (synchronized), or reopened. It does not fire on direct pushes. This is the correct trigger for merge-blocking security gates.

6. **Secret rotation after exposure** — The exam tests that when a secret is found in Git history, the first action is to rotate the credential immediately — not simply delete the file in a new commit.

7. **Defense in depth for secrets** — Know that best practice combines a pre-commit hook (early feedback) with a CI pipeline scan (enforcement) because the hook can be bypassed. Neither alone is sufficient.

8. **Signed commits vs. 2FA** — Know the difference: signed commits verify commit authorship cryptographically; two-factor authentication verifies user login. Both are security controls but at different points.

---

## Section 11: Study Checklist

Work through this checklist before attempting the quiz and lab.

- [ ] Explain why Git history permanence makes pre-commit secrets scanning critical.
- [ ] List five branch protection rule settings and the risk each addresses.
- [ ] Explain the difference between a pre-commit hook and a CI pipeline secrets scan.
- [ ] Write (from memory or notes) the YAML structure of a GitHub Actions workflow with at least two jobs.
- [ ] Explain what `fetch-depth: 0` does and why it matters for secrets scanning.
- [ ] Explain the `permissions:` block and what `contents: read` means.
- [ ] Identify the correct trigger for a security gate that must pass before a PR can merge.
- [ ] Read the OWASP DevSecOps Guideline secrets management section at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
- [ ] Complete the Module 02 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
