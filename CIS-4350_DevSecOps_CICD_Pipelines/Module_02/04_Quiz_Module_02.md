# Quiz: Module 02 — Version Control Security and Git Best Practices

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Submit answers through the Canvas quiz interface.

---

## Question 1

Which branching strategy is most likely to minimize security patch propagation delay across all developers?

- A) GitFlow with long-lived feature branches
- B) Trunk-based development with short-lived branches
- C) Release branching with quarterly merges
- D) Forking workflow with upstream sync once per sprint

### Q1 — Correct Answer: B

### Q1 — Distractor Analysis

- A) GitFlow's long-lived branches create drift — security patches merged to develop may not reach feature branches for days or weeks.
- C) Quarterly merges create extreme drift and are incompatible with continuous security patching.
- D) Forking with sprint-level sync creates the same drift problem as infrequent feature branch merges.

---

## Question 2

A developer commits code with `git commit --no-verify`. What security control does this bypass?

- A) Branch protection rules on the remote server
- B) GPG commit signature requirement
- C) Client-side pre-commit and commit-msg hooks
- D) CI pipeline status check requirements

### Q2 — Correct Answer: C

### Q2 — Distractor Analysis

- A) Branch protection rules are server-side and cannot be bypassed by client-side git flags.
- B) GPG signing is configured globally in git config — `--no-verify` does not affect it.
- D) CI pipeline status checks run on the server after a push — `--no-verify` only affects local hooks.

---

## Question 3

What is the primary advantage of managing git hooks via the pre-commit framework rather than placing scripts directly in `.git/hooks/`?

- A) The pre-commit framework runs faster than native git hooks
- B) Hook configuration is version-controlled and shared across all team members automatically
- C) The pre-commit framework bypasses branch protection rules
- D) Native `.git/hooks/` scripts cannot run secrets scanning tools

### Q3 — Correct Answer: B

### Q3 — Distractor Analysis

- A) Performance difference is negligible — this is not the primary advantage.
- C) The pre-commit framework does not interact with branch protection rules at all.
- D) Native git hooks can run any executable — the limitation is sharing and versioning, not capability.

---

## Question 4

You discover that an AWS access key was committed to a public GitHub repository 3 days ago. After running git-filter-repo to remove it from history, what is the most critical next step?

- A) Create a new branch to separate the clean history from the old history
- B) Immediately rotate and revoke the compromised AWS access key
- C) Change the repository visibility from public to private
- D) Notify all team members to run `git pull` to get the clean history

### Q4 — Correct Answer: B

### Q4 — Distractor Analysis

- A) Branching does not address the fact that the secret was already exposed and may have been used.
- C) Making the repo private does not revoke the already-exposed credential.
- D) Team notification is necessary but secondary — the credential is already compromised and must be rotated immediately.

---

## Question 5

Which file must you commit to a repository to document required environment variables without exposing their values?

- A) `.env`
- B) `.env.secret`
- C) `.env.example`
- D) `env_config.json`

### Q5 — Correct Answer: C

### Q5 — Distractor Analysis

- A) `.env` contains actual secret values and must never be committed.
- B) `.env.secret` is not a standard pattern and the name implies it contains secrets.
- D) A JSON config file is not the standard pattern and may accidentally contain real values.

---

## Question 6

What does a GPG-signed commit prove that an unsigned commit does not?

- A) That the code is free of security vulnerabilities
- B) That the commit passed all CI pipeline checks
- C) That the commit was made by someone possessing a specific private key
- D) That the commit message follows the team's convention

### Q6 — Correct Answer: C

### Q6 — Distractor Analysis

- A) GPG signing proves authorship only — it makes no claim about code quality or security.
- B) CI pipeline checks are separate from commit signing — the two are independent.
- D) Commit message conventions are enforced by commit-msg hooks, not GPG signing.

---

## Question 7

Which GitHub feature automatically revokes secrets such as AWS access keys when they are detected in a public repository, in coordination with the cloud provider?

- A) Dependabot
- B) GitHub Advanced Security secret scanning partner patterns
- C) GitHub Actions security hardening
- D) CodeQL analysis

### Q7 — Correct Answer: B

### Q7 — Distractor Analysis

- A) Dependabot monitors dependency vulnerabilities (CVEs), not secrets in source code.
- C) GitHub Actions security hardening relates to workflow permissions, not secret detection.
- D) CodeQL is a SAST tool for code vulnerabilities, not credential scanning.

---

## Question 8

A CODEOWNERS file serves which security purpose?

- A) It lists all files that should be added to `.gitignore`
- B) It maps file paths to required reviewers, ensuring security-sensitive code always gets expert review
- C) It defines which GPG keys are authorized to sign commits
- D) It specifies which branches are protected from direct pushes

### Q8 — Correct Answer: B

### Q8 — Distractor Analysis

- A) `.gitignore` has no relationship to CODEOWNERS — they are entirely separate files.
- C) GPG key authorization is configured in platform settings, not CODEOWNERS.
- D) Branch protection rules handle push restrictions, not CODEOWNERS.

---

## Question 9

truffleHog's entropy-based detection capability solves which limitation of regex-only secrets scanners like gitleaks?

- A) Entropy detection is faster than regex matching for large repositories
- B) Entropy detection can identify high-entropy strings that may be secrets even without a matching known pattern
- C) Entropy detection eliminates false positives entirely
- D) Entropy detection works on binary files while regex scanning only works on text

### Q9 — Correct Answer: B

### Q9 — Distractor Analysis

- A) Entropy analysis is computationally more expensive than regex, not faster.
- C) Entropy detection actually tends to produce more false positives than regex-based detection.
- D) Both tools operate primarily on text content in Git objects — binary file handling is unrelated to entropy detection.

---

## Question 10

Which statement about the `--no-allow-bypass` branch protection setting in GitHub is correct?

- A) It prevents external contributors from forking the repository
- B) It prevents repository administrators from overriding the branch protection rules
- C) It disables all CI/CD pipelines for the protected branch
- D) It requires two-factor authentication for all push operations

### Q10 — Correct Answer: B

### Q10 — Distractor Analysis

- A) Forking controls are separate repository-level settings unrelated to branch protection bypass.
- C) Branch protection does not affect CI/CD pipeline execution — pipelines still run.
- D) Two-factor authentication is an account-level security setting, not a branch protection parameter.

---

Quiz — Module 02 | CIS-4350 | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

A team stores Infrastructure as Code in a monorepo. They want to ensure that only the platform security team can approve changes to Terraform files. Which file and mechanism accomplish this?

- A) `.gitignore` with a `*.tf` entry to exclude Terraform files from indexing
- B) A `CODEOWNERS` file with `*.tf @org/platform-security-team`
- C) A branch protection rule that blocks all pushes containing `.tf` files
- D) A pre-commit hook that rejects commits touching Terraform files

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `.gitignore` prevents files from being tracked by Git — it does not control who can review them.
  - C) Branch protection can restrict pushes broadly but cannot filter by file type — CODEOWNERS is the correct mechanism for file-based review requirements.
  - D) A pre-commit hook could warn but would not enforce a review requirement — it runs client-side and can be bypassed.

---

### Question 12 (5 points)

When using `git filter-repo` to remove a secret from repository history, what must happen to remote copies of the repository?

- A) Nothing — git filter-repo automatically pushes the cleaned history to all remotes
- B) The remote must be force-pushed with the cleaned history, and all collaborators must re-clone or rebase
- C) The remote repository must be deleted and recreated from scratch
- D) Running `git gc --prune=now` on the remote server is sufficient to remove the secret

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `git filter-repo` only modifies local history — it does not push to remotes automatically.
  - C) Recreating the repository is one option but is more disruptive than necessary; a force push with collaborator re-clone achieves the same result.
  - D) `git gc` compacts objects locally but does not rewrite history or affect what is stored on the remote server.

---

### Question 13 (5 points)

What is the primary security purpose of enabling "Dismiss stale pull request approvals when new commits are pushed" in GitHub branch protection?

- A) It automatically closes pull requests that have not been updated in 30 days
- B) It prevents a PR from being merged with an approval that was given before a potentially dangerous new commit was added
- C) It reduces the number of required approvers when PRs are updated frequently
- D) It triggers a new CI pipeline run whenever a new approval is submitted

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) This setting does not close PRs — it only invalidates approvals.
  - C) The setting does not change the required approval count — it requires those approvals to be re-earned after new commits.
  - D) CI pipeline triggers are driven by push events, not approval events; these are independent settings.

---

### Question 14 (5 points)

Which gitleaks mode should be used in a pre-commit hook to scan only the files staged for the current commit, rather than the entire repository history?

- A) `gitleaks detect --source .`
- B) `gitleaks protect --staged`
- C) `gitleaks git --all`
- D) `gitleaks scan --head-only`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `detect --source .` scans the working directory or full repo, not just staged changes.
  - C) `--all` scans the full history — this is the slowest option and inappropriate for per-commit hooks.
  - D) `--head-only` is not a valid gitleaks flag.

---

### Question 15 (5 points)

An organization requires that all commits to their main branch include a Jira ticket reference (e.g., `JIRA-1234`) in the commit message. Which git hook type enforces this?

- A) pre-commit
- B) pre-push
- C) commit-msg
- D) post-commit

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) The pre-commit hook fires before the message is written — the message does not yet exist to validate.
  - B) pre-push fires before a push to a remote — by then many commits may already exist locally without a valid message.
  - D) post-commit fires after the commit is complete — the commit already exists and cannot be blocked.

---

### Question 16 (5 points)

Which of the following is NOT a valid reason to use trunk-based development over GitFlow?

- A) Security patches reach all developers faster with shorter branch lifetimes
- B) It eliminates the need for automated testing because fewer branches exist
- C) It simplifies merge history, reducing conflict-resolution bugs
- D) CI pipeline results always reflect current production-bound code

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) This is a genuine security advantage of trunk-based development — shorter branches mean fewer days of drift.
  - C) Simpler merge history is a real advantage that reduces the chance of human error during conflict resolution.
  - D) CI running on every main commit is a core benefit of trunk-based development.

---

### Question 17 (5 points)

SSH key signing for Git commits (introduced in Git 2.34) differs from GPG signing in which way?

- A) SSH signing does not provide non-repudiation — it only encrypts the commit content
- B) SSH signing uses the developer's existing SSH key pair, eliminating the need to manage a separate GPG key
- C) SSH-signed commits are not supported by GitHub's "Verified" badge system
- D) SSH signing requires a hardware security key (YubiKey) and cannot be done with a software key

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) SSH signing does provide non-repudiation through asymmetric cryptography — the same principle as GPG.
  - C) GitHub supports SSH-signed commits and displays the "Verified" badge for them since 2022.
  - D) SSH signing works with any SSH key pair, including software-generated keys — a hardware key is optional.

---

### Question 18 (5 points)

A `.gitignore` file contains the following entry: `!.env.example`. What does the `!` prefix mean in this context?

- A) It is a comment indicating that `.env.example` should not be used in production
- B) It negates the previous ignore rule, re-including `.env.example` so it is tracked by Git
- C) It marks `.env.example` as a required file that will cause an error if missing
- D) It encrypts `.env.example` before adding it to the repository

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Comments in `.gitignore` use `#`, not `!`.
  - C) `.gitignore` has no mechanism to require files — it only controls exclusion.
  - D) `.gitignore` is a text pattern file with no encryption capability.

---

### Question 19 (5 points)

GitHub's secret scanning "push protection" feature operates at which point in the developer workflow?

- A) During a CI pipeline run after the push is accepted
- B) During a nightly scheduled scan of all repository contents
- C) At the moment of the `git push`, before the commits are accepted by the server
- D) When a pull request is opened for review

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Push protection is a pre-receive mechanism — it blocks the push before commits are stored, not after.
  - B) Nightly scanning exists as a separate feature; push protection operates in real time at push time.
  - D) Pull request scanning is a separate check; push protection fires during the push itself, regardless of whether a PR is involved.

---

### Question 20 (5 points)

A developer's machine is compromised and an attacker uses `git config user.name` and `git config user.email` to impersonate a senior engineer before committing malicious code. Which control specifically prevents this attack?

- A) Branch protection requiring at least two code reviewers
- B) Mandatory GPG or SSH commit signing with keys stored in a hardware security module
- C) A pre-commit hook that validates the committer's email against an allowlist
- D) Enabling two-factor authentication on the GitHub account

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Two reviewers check the code content but cannot detect identity impersonation if the commit appears to come from a legitimate author.
  - C) A pre-commit hook runs on the attacker's compromised machine and can be bypassed with `--no-verify`; it also cannot verify key possession.
  - D) 2FA protects the GitHub web/API login session but does not protect commit authorship in the local Git client.
