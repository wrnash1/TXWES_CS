# Quiz: Module 02 - Version Control with Git and GitHub

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

What is the primary security purpose of a pre-commit hook in a DevSecOps workflow?

- A) To compile source code into a deployable artifact before it is committed
- B) To detect and block commits containing hardcoded secrets or insecure patterns before they enter Git history
- C) To push the committed code automatically to the remote repository and trigger CI/CD pipelines
- D) To enforce code style formatting rules so all developers follow the same indentation standard

#### Q1 Correct Answer

B — Pre-commit hooks run on the developer's local machine before `git commit` finalizes. If the hook detects a secret or insecure pattern and exits non-zero, the commit is aborted and the content never enters Git history.

#### Q1 Distractor Analysis

- *Why A is incorrect:* Compilation is a build-stage concern. Pre-commit hooks run analysis against staged files, not compilation.
- *Why C is incorrect:* Pushing to remote and triggering pipelines happens after the commit is created. Pre-commit hooks run before the commit exists.
- *Why D is incorrect:* While some pre-commit hooks do enforce style, the primary security purpose is detecting vulnerabilities and secrets — not formatting.

---

### Question 2

A developer discovers that a teammate bypassed the pre-commit secrets hook using `git commit --no-verify` and pushed an API key to a feature branch on GitHub. What is the correct immediate response?

- A) Delete the feature branch — this removes the API key from GitHub
- B) Rotate the compromised API key immediately, then remove it from the branch and rewrite history
- C) Add a comment to the commit explaining the key is no longer valid
- D) Enable two-factor authentication on the developer's GitHub account

#### Q2 Correct Answer

B — Once a secret is pushed to any remote branch, it must be treated as compromised regardless of whether the branch is deleted. Rotation is the only safe remediation. History rewrite removes the secret from the repository.

#### Q2 Distractor Analysis

- *Why A is incorrect:* Deleting a branch does not delete the objects from GitHub's backend. Anyone who cloned or forked the repository before deletion may already have the key.
- *Why C is incorrect:* Adding a comment does not revoke the credential. The key remains valid and accessible in history until rotated.
- *Why D is incorrect:* 2FA protects account login but does not revoke an already-exposed API key or prevent its misuse.

---

### Question 3

In a GitHub Actions workflow, what does setting `fetch-depth: 0` on the `actions/checkout` step accomplish?

- A) It limits the checkout to only the files changed in the current pull request, improving performance
- B) It fetches the complete Git history, enabling secrets scanners to inspect all commits in the pull request rather than just the latest file state
- C) It forces the workflow to run on a fresh runner with no cached data from previous workflow runs
- D) It disables shallow cloning and downloads all repository branches including remote-tracking branches

#### Q3 Correct Answer

B — By default, `actions/checkout` performs a shallow clone (depth 1), fetching only the latest commit. `fetch-depth: 0` fetches the full history, which secrets scanners like Gitleaks require to check every commit in the PR — a secret added in commit 1 and deleted in commit 3 is still accessible in history.

#### Q3 Distractor Analysis

- *Why A is incorrect:* Limiting to only changed files would be a different parameter. `fetch-depth: 0` fetches more history, not less.
- *Why C is incorrect:* Runner cache behavior is controlled by the `cache:` action, not `fetch-depth`.
- *Why D is incorrect:* `fetch-depth: 0` fetches the full history of the checked-out branch; fetching all remote branches requires additional configuration.

---

### Question 4

A GitHub Actions workflow is configured with `on: pull_request` targeting the main branch. When exactly does this workflow trigger?

- A) Once per day on a scheduled timer, regardless of code activity
- B) Every time any developer pushes commits to any branch in the repository
- C) When a pull request targeting main is opened, updated with new commits, or reopened
- D) Only when a pull request is approved by a required reviewer and is ready to merge

#### Q4 Correct Answer

C — The `pull_request` event fires on PR open, synchronize (new commits pushed to the PR branch), and reopen actions. This makes it the standard trigger for security checks that must pass before merging.

#### Q4 Distractor Analysis

- *Why A is incorrect:* Scheduled triggers use `on: schedule` with a cron expression. `pull_request` is event-driven, not time-driven.
- *Why B is incorrect:* The `on: push` trigger fires on all branch pushes. `on: pull_request` is scoped to PR lifecycle events, not all pushes.
- *Why D is incorrect:* Pull request approval is a separate human action. The `pull_request` event does not wait for reviewer approval — it fires immediately on PR open or update.

---

### Question 5

Which GitHub branch protection setting most directly enforces that CI pipeline security scan jobs must succeed before a pull request can merge?

- A) Require signed commits
- B) Require status checks to pass before merging, with the security scan job names listed as required checks
- C) Require a minimum number of approving reviews
- D) Restrict who can push to the branch

#### Q5 Correct Answer

B — Listing specific CI job names as required status checks means GitHub will not enable the merge button until those jobs have reported a passing result. This is the mechanism that makes automated pipeline scans mandatory rather than advisory.

#### Q5 Distractor Analysis

- *Why A is incorrect:* Signed commits verify committer identity cryptographically. They do not enforce CI job results.
- *Why C is incorrect:* Required reviews enforce human approval. They do not enforce automated pipeline job results.
- *Why D is incorrect:* Restricting push access prevents direct pushes to the branch but does not enforce pipeline status checks on PRs.

---

### Question 6

A team wants to prevent any developer — including repository administrators — from bypassing branch protection rules and pushing directly to main. Which setting achieves this?

- A) Set the repository to private so only team members have access
- B) Enable "Do not allow bypassing the above settings" (or "Include administrators") in the branch protection rule
- C) Require all developers to use SSH keys instead of HTTPS for Git authentication
- D) Enable two-factor authentication for all organization members

#### Q6 Correct Answer

B — By default, repository administrators can bypass branch protection rules. The "Include administrators" or "Do not allow bypassing" option applies the rules to everyone including admins, eliminating this privileged bypass path.

#### Q6 Distractor Analysis

- *Why A is incorrect:* Repository visibility (public vs. private) controls who can see the code. It does not change who can bypass branch protection rules.
- *Why C is incorrect:* SSH vs. HTTPS is an authentication method for Git operations. It does not affect branch protection bypass capabilities.
- *Why D is incorrect:* 2FA strengthens account login security but does not affect the ability to bypass branch protection rules after authentication.

---

### Question 7

A GitHub Actions workflow posts a failing SAST scan result to a pull request, but the developer is still able to merge the PR. What is the most likely cause?

- A) The SAST scan found only informational findings, which GitHub automatically ignores
- B) The SAST job name is not listed as a required status check in the branch protection rules
- C) The workflow is using `on: push` instead of `on: pull_request` as its trigger
- D) The developer used `git commit --no-verify` to skip the pre-commit hooks

#### Q7 Correct Answer

B — A CI job result is only a merge blocker if its job name is listed under required status checks in the branch protection rule. Without that listing, the failing result is visible but does not prevent merging.

#### Q7 Distractor Analysis

- *Why A is incorrect:* GitHub does not automatically classify SAST findings by severity. All status check results — pass or fail — are shown. The issue is whether the check is required, not the finding severity.
- *Why C is incorrect:* If the workflow uses `on: push`, the scan runs on the push to the feature branch, not on the PR. This is a separate problem (wrong trigger) but does not explain why a failing check can be bypassed.
- *Why D is incorrect:* `--no-verify` bypasses pre-commit hooks on the local machine. It has no effect on CI pipeline jobs running on GitHub runners.

---

### Question 8

Which of the following is a correct security practice when storing credentials needed by a GitHub Actions workflow?

- A) Hardcode the credential in the workflow YAML file and mark it with a comment indicating it is sensitive
- B) Store the credential as a GitHub Secret and reference it using `${{ secrets.SECRET_NAME }}` in the workflow
- C) Base64-encode the credential and store it in a public environment variable in the workflow YAML
- D) Store the credential in a `.env` file committed to the repository and load it at runtime

#### Q8 Correct Answer

B — GitHub Secrets are encrypted at rest and masked in workflow logs. The `${{ secrets.SECRET_NAME }}` syntax injects the value at runtime without exposing it in the YAML file or in log output.

#### Q8 Distractor Analysis

- *Why A is incorrect:* Hardcoding credentials in the workflow YAML makes them visible to anyone with read access to the repository — including in public repositories, the entire internet.
- *Why C is incorrect:* Base64 encoding is not encryption. Encoded values can be decoded trivially. Storing them in public environment variables exposes them in the workflow YAML.
- *Why D is incorrect:* Committing a `.env` file to the repository exposes credentials in Git history and to anyone with repository access.

---

### Question 9

What does the `permissions: contents: read` block in a GitHub Actions workflow accomplish?

- A) It grants the workflow read access to all repositories in the GitHub organization
- B) It restricts the workflow's GITHUB_TOKEN to read-only access on the current repository, following the principle of least privilege
- C) It allows the workflow to read encrypted secrets stored in GitHub Secrets
- D) It gives the workflow permission to read environment variables defined in the repository settings

#### Q9 Correct Answer

B — The `permissions:` block scopes the automatically-generated `GITHUB_TOKEN` for that workflow run. Setting `contents: read` grants only repository content read access, preventing a compromised or malicious action from writing to the repository, creating releases, or modifying settings.

#### Q9 Distractor Analysis

- *Why A is incorrect:* `permissions:` scopes the token for the current repository only. Cross-repository access requires a personal access token or GitHub App token with separate configuration.
- *Why C is incorrect:* Access to GitHub Secrets is controlled separately by the secrets configuration, not by the `permissions:` block.
- *Why D is incorrect:* Environment variable access is not controlled by the `permissions:` block. Secrets access and variable access have separate configuration mechanisms.

---

### Question 10

A DevSecOps team is reviewing their GitHub Actions workflow and notices the following trigger configuration. What security gap does this create?

```yaml
on:
  push:
    branches:
      - main
```

- A) The workflow runs too frequently, creating unnecessary compute costs and noise in the Actions log
- B) The workflow runs only after code has already been merged to main, meaning insecure code can reach main before being scanned
- C) The workflow cannot access GitHub Secrets because push triggers are restricted from secrets access
- D) The workflow will fail because push triggers require a `paths:` filter to be valid

#### Q10 Correct Answer

B — A `push` to main trigger fires after the merge has already occurred. Any vulnerability the scan finds is already in the main branch. The correct DevSecOps pattern is `on: pull_request` so the scan runs before merge and can block insecure code from entering main.

#### Q10 Distractor Analysis

- *Why A is incorrect:* Workflow frequency and compute cost are operational concerns, not security gaps. The core issue is timing — post-merge vs. pre-merge.
- *Why C is incorrect:* GitHub Secrets are accessible to workflows triggered by push events. There is no restriction based on trigger type for secrets access (with appropriate configuration).
- *Why D is incorrect:* `paths:` is an optional filter for push triggers. A push trigger without `paths:` is valid and fires on all pushes to the specified branch.
