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
