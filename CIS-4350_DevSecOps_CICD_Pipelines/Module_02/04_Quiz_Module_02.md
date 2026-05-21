# Quiz: Module 02 - Version Control with Git and GitHub

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the primary function of a linter tool in a Continuous Integration pipeline?

* A) To compile source code into executable binaries
* B) To analyze source code for programmatic errors, code smells, and style guide violations
* C) To host REST APIs for external service consumers
* D) To decrypt database connection strings at runtime
* **Correct Answer:** B) Linters check code syntax and styling against standard formats (e.g., PEP 8 for Python), catching basic errors early.
* **Distractor Analysis:**
  * *Why B is correct:* Linters perform static analysis of source text against configurable rule sets, flagging style violations, unused variables, and common anti-patterns without executing the code.
  * *Why A is incorrect:* Compilation converts source code to executable artifacts; linting is a separate analysis step that does not produce binaries.
  * *Why C is incorrect:* API hosting is an application runtime concern, unrelated to code quality analysis in a CI pipeline.
  * *Why D is incorrect:* Decrypting credentials is a secrets management concern; linters analyze code structure and style only.

---

**Question 2**
Which of the following most accurately describes an automation runner in a CI/CD pipeline?

* A) A developer who manually reviews code before it is merged to the main branch
* B) A compute environment that executes pipeline jobs — checking out code, running tests, and performing security scans — when triggered by a Git event
* C) A database server that stores build artifacts and deployment logs for audit purposes
* D) A Git branch protection rule that requires a minimum number of approving reviews before merging
* **Correct Answer:** B) Automation runners are the execution environments (GitHub-hosted or self-hosted VMs/containers) that carry out every step defined in a CI/CD workflow when triggered by events like push or pull_request.
* **Distractor Analysis:**
  * *Why B is correct:* Runners check out the repository, install tools, and execute each workflow step in isolation — including linting, testing, and security scanning — without human intervention.
  * *Why A is incorrect:* A human reviewer is a manual quality gate, not an automation runner. Runners execute automated steps, not human reviews.
  * *Why C is incorrect:* Artifact storage is a separate concern (handled by registries or artifact stores); runners execute steps but are not storage systems.
  * *Why D is incorrect:* Branch protection rules are repository configuration policies; they constrain what can be merged but are not execution environments.

---

**Question 3**
A developer wants to prevent accidentally committing files containing hardcoded credentials to a Git repository. Which approach provides the earliest shift-left enforcement?

* A) Configure a GitHub Actions workflow to scan for secrets on every pull request
* B) Add a pre-commit hook that runs a secrets scanner (e.g., Gitleaks) before each local commit is finalized
* C) Set up a weekly scheduled CI job that scans the entire repository history for exposed secrets
* D) Enable branch protection rules requiring two reviewers to approve all pull requests
* **Correct Answer:** B) A pre-commit hook runs on the developer's machine before the commit is even created, preventing the secret from ever entering the repository or its history.
* **Distractor Analysis:**
  * *Why B is correct:* Pre-commit hooks are the earliest possible gate — they fire before `git commit` finalizes, meaning the secret never reaches the local commit object, let alone the remote repository.
  * *Why A is incorrect:* A pull request scan catches secrets after they have already been committed and pushed to a remote branch; the secret is already in Git history at that point.
  * *Why C is incorrect:* A weekly scheduled scan is reactive and delayed; secrets may have been exposed for days before detection.
  * *Why D is incorrect:* Human reviewers may miss embedded secrets in large diffs; automated scanning is more reliable and consistent.

---

**Question 4**
In a GitHub Actions workflow, what is the effect of setting `on: pull_request` as the trigger for a security scan job?

* A) The security scan runs once per day on a scheduled timer regardless of code changes
* B) The security scan runs only when a pull request is opened, updated, or synchronized against the target branch
* C) The security scan runs on every push to every branch in the repository
* D) The security scan runs only after a release is published to the GitHub Releases page
* **Correct Answer:** B) The `pull_request` trigger fires when a PR is opened or receives new commits, making it the standard gate for blocking insecure code from merging into the main branch.
* **Distractor Analysis:**
  * *Why B is correct:* The `on: pull_request` event fires on PR open, synchronize (new commits pushed), and reopen actions — providing automated security validation before any merge is allowed.
  * *Why A is incorrect:* Scheduled triggers use `on: schedule` with a cron expression; `pull_request` is event-driven, not time-driven.
  * *Why C is incorrect:* The `on: push` trigger fires on all branch pushes; `on: pull_request` is scoped specifically to PR lifecycle events.
  * *Why D is incorrect:* Release-triggered workflows use `on: release`; that event fires after a release is published, not during code review.

---

**Question 5**
A DevSecOps team wants to ensure no code merges to the `main` branch unless all CI checks — including SAST and linting — have passed. Which GitHub configuration enforces this policy?

* A) Adding a `.gitignore` file that excludes test output directories from the repository
* B) Enabling branch protection rules on `main` with required status checks that must pass before merging
* C) Setting the default branch to `main` in the repository settings
* D) Tagging all passing commits with a semantic version number using `git tag`
* **Correct Answer:** B) GitHub branch protection rules with required status checks prevent any pull request from being merged until all specified CI jobs — including security scans — report a passing status.
* **Distractor Analysis:**
  * *Why B is correct:* Branch protection's "Require status checks to pass before merging" setting directly enforces that pipeline jobs (SAST, linting, tests) must succeed — if any fail, the merge button is disabled.
  * *Why A is incorrect:* `.gitignore` controls which files Git tracks; it has no effect on merge permissions or CI enforcement.
  * *Why C is incorrect:* Setting the default branch only affects which branch is shown first in the UI and used for clone operations; it does not add any protection or CI enforcement.
  * *Why D is incorrect:* Semantic version tags are a release management practice; they do not enforce CI checks or prevent insecure code from being merged.
