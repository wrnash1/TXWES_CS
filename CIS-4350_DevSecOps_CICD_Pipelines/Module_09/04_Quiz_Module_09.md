# Quiz: Module 09 - Secrets Management – HashiCorp Vault and AWS Secrets Manager

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Why should API keys and database passwords never be hardcoded in Git source files?

* A) Git's compression algorithm corrupts binary data such as keys during storage
* B) Once pushed, secrets are saved in repository history and can be exposed to unauthorized parties even if the file is later deleted or overwritten
* C) Hardcoded secrets increase code execution time because the interpreter must parse them on startup
* D) Hardcoded secrets cause Git merge conflicts that cannot be automatically resolved
* **Correct Answer:** B) Git histories are persistent; once a secret is committed, it remains in the repository history — in all clones, forks, and cached copies — and can be extracted even after the file is modified or deleted.
* **Distractor Analysis:**
  * *Why B is correct:* Git stores every version of every file in its object database. A secret committed in version 1 and deleted in version 2 is still fully recoverable by checking out version 1 or reading the object pack. Attackers routinely scan public GitHub repositories and their full histories for exposed credentials.
  * *Why A is incorrect:* Git does not corrupt data during storage. Its SHA-1/SHA-256 content-addressable model ensures exact byte preservation of all committed content.
  * *Why C is incorrect:* Hardcoded credentials have no measurable impact on code execution time. The risk is exposure and unauthorized access, not performance.
  * *Why D is incorrect:* Hardcoded strings do not cause Git merge conflicts any more than other code. The risk is credential exposure through repository access, not version control mechanics.

---

**Question 2**
Which of the following most accurately describes HashiCorp Vault's dynamic secrets capability?

* A) Vault stores a fixed, pre-configured password for each service and returns the same value on every request
* B) Vault generates short-lived, unique credentials on demand (such as a temporary database username and password) that automatically expire after a configured time-to-live, eliminating long-lived static credentials
* C) Vault encrypts static environment variable files at rest on the CI/CD runner's filesystem
* D) Vault scans Git repository history to identify and automatically rotate any exposed credentials it detects
* **Correct Answer:** B) Vault's dynamic secrets engine generates credentials on demand with a short TTL — if the credential is leaked, it expires and becomes useless without any manual rotation step.
* **Distractor Analysis:**
  * *Why B is correct:* Vault's database secrets engine, for example, creates a unique PostgreSQL user with a randomly generated password for each requesting application or pipeline job. The credential expires at TTL, reducing the blast radius of any leak to the TTL window rather than indefinitely.
  * *Why A is incorrect:* Returning the same static password on every request is the traditional secrets manager pattern (AWS Secrets Manager with manual rotation). Vault's dynamic secrets capability specifically avoids static, long-lived credentials.
  * *Why C is incorrect:* Encrypting environment variable files on disk is a function of secrets injection at rest (e.g., encrypted Kubernetes Secrets). Vault's dynamic secrets is about generating fresh credentials on demand, not encrypting existing files.
  * *Why D is incorrect:* Scanning repositories for exposed credentials is the function of secret scanning tools like Gitleaks or TruffleHog. Vault does not scan code repositories.

---

**Question 3**
A CI/CD pipeline needs to authenticate to AWS to deploy infrastructure. Which approach best follows DevSecOps secrets management principles?

* A) Store AWS access key and secret key as plaintext in the repository's `.env` file and reference them in the workflow
* B) Hardcode the AWS credentials directly in the workflow YAML file as string literals for simplicity
* C) Configure the CI platform (GitHub Actions) to use OIDC federation with AWS IAM to exchange a short-lived OIDC token for temporary AWS credentials — no long-lived keys stored anywhere
* D) Email the AWS credentials to all developers on the team so they can configure them locally if the pipeline fails
* **Correct Answer:** C) OIDC federation allows the CI platform to authenticate to AWS using a signed JWT issued by GitHub, which AWS IAM exchanges for temporary STS credentials — eliminating the need to store any long-lived AWS keys.
* **Distractor Analysis:**
  * *Why C is correct:* GitHub Actions OIDC + AWS IAM role trust is the modern, keyless approach. The pipeline receives temporary credentials (valid for 15 minutes to 1 hour) scoped to exactly the permissions needed. No secret is ever stored, committed, or rotated manually.
  * *Why A is incorrect:* Storing credentials in a `.env` file in the repository is a critical security failure — the file will be committed to Git and exposed in repository history, forks, and CI logs.
  * *Why B is incorrect:* Hardcoding credentials in workflow YAML commits them to the repository in plaintext, making them accessible to anyone with repository read access and persisting them in Git history.
  * *Why D is incorrect:* Distributing credentials via email creates uncontrolled copies, violates the principle of least privilege, and provides no audit trail or automatic expiration.

---

**Question 4**
A secret scanning tool (Gitleaks) detects an AWS access key pattern in a pull request diff. The developer claims it is a test key that has already been deleted from AWS. What is the correct DevSecOps response?

* A) Approve the PR and merge it since the key is already deleted and no longer works
* B) Block the merge, have the developer remove the key from the commit (using `git commit --amend` or interactive rebase), confirm the key is truly revoked in AWS, and run the secret scan again to verify the finding is gone before merging
* C) Add the detected pattern to the scanner's suppression list so future scans don't flag this pattern
* D) Accept the merge but immediately rotate all AWS keys in the account as a precaution
* **Correct Answer:** B) Even if the key is revoked, it should not enter the repository history. The commit must be rewritten to remove the credential, the scan must re-pass, and revocation in AWS must be confirmed before the PR is merged.
* **Distractor Analysis:**
  * *Why B is correct:* A revoked key is less dangerous but still represents a policy violation and a precedent that credentials belong in source code. Rewriting the commit (via `git commit --amend` or interactive rebase) keeps the repository history clean and prevents the pattern from normalizing credential commits.
  * *Why A is incorrect:* Merging a PR with a committed credential — even a revoked one — stores it permanently in the main branch history, normalizes the bad practice, and could cause confusion in future security audits.
  * *Why C is incorrect:* Adding the AWS key pattern to the suppression list would prevent all future AWS key detections of the same format, creating a dangerous blindspot in the scanner's coverage.
  * *Why D is incorrect:* Rotating all AWS keys is a disproportionate response and does not address the root issue: the credential pattern in the commit history. The specific key should be confirmed revoked and removed from the commit.

---

**Question 5**
A DevSecOps team wants to prevent developers from accidentally committing secrets to the repository in the first place. Which combination of controls provides the most comprehensive prevention?

* A) Display a reminder in the team's Slack channel each Monday asking developers not to commit secrets
* B) Combine a local pre-commit hook (running Gitleaks on staged files before commit) with a CI pipeline stage (running Gitleaks on the full diff of each pull request) so secrets are caught both locally and server-side
* C) Configure the Git repository to store all files as binary blobs, making it impossible to inspect them for text patterns
* D) Require all developers to use a password manager for their personal passwords, reducing the likelihood of confusing credentials with code
* **Correct Answer:** B) Defense in depth using both a local pre-commit hook (earliest gate, catches before commit creation) and a CI pipeline scanner (authoritative server-side gate, catches anything that bypassed the local hook) provides comprehensive, automated coverage.
* **Distractor Analysis:**
  * *Why B is correct:* The pre-commit hook stops most accidental commits before they happen; the CI gate catches anything that slipped through (e.g., a developer who skipped hooks with `--no-verify`). Together they create a defense-in-depth approach where no single bypass point eliminates protection.
  * *Why A is incorrect:* Slack reminders are an awareness mechanism, not a technical control. They do not prevent any commits and are easily ignored or missed.
  * *Why C is incorrect:* Storing files as binary blobs would break all text editors, IDEs, code review tools, and diff functionality — it is operationally destructive and does not prevent secrets from being embedded in binary representations.
  * *Why D is incorrect:* Personal password managers address how developers store their own credentials but do not prevent developers from accidentally embedding API keys, tokens, or other programmatic credentials in source code during development.
