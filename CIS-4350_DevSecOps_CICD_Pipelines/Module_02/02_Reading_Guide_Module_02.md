# Reading Guide: Module 02 — Version Control Security and Git Best Practices

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Compare GitFlow and trunk-based development branching strategies and their security trade-offs
- Configure GPG-signed commits and explain their role in supply chain integrity
- Implement branch protection rules that enforce CI security gates
- Write and manage git hooks using the pre-commit framework
- Scan repository history for secrets using gitleaks and truffleHog
- Configure a comprehensive `.gitignore` to prevent sensitive file exposure

---

## Section 1 — Branching Strategies and Security Implications

### 1.1 GitFlow

GitFlow organizes work around five branch types:

| Branch | Purpose | Lifetime |
|---|---|---|
| main | Production-ready code | Permanent |
| develop | Integration branch | Permanent |
| feature/* | New features | Days to weeks |
| release/* | Release preparation | Days |
| hotfix/* | Emergency production fixes | Hours to days |

Security concerns with GitFlow:

- Long-lived feature branches accumulate drift, missing security patches merged to develop
- Merge complexity increases — each merge point is a conflict risk
- Multiple integration points mean security scans must run on each branch, increasing CI cost
- Hotfix branches may bypass normal review processes under pressure

### 1.2 Trunk-Based Development

Trunk-based development uses a single long-lived branch (main or trunk). All developers merge short-lived branches (under 2 days) or commit directly. Features not ready for release are hidden behind feature flags.

Security advantages:

- Security patches reach all developers within hours
- No branch drift — everyone works from the same base
- Simpler merge history reduces conflict-resolution bugs
- CI pipeline always reflects current production-bound code

Security requirements for trunk-based development:

- Mandatory CI status checks on every merge to main
- Feature flags to decouple deployment from release
- Robust automated test coverage to catch regressions fast

### 1.3 Branching Strategy Comparison

| Dimension | GitFlow | Trunk-Based |
|---|---|---|
| Branch longevity | Weeks | Hours to 2 days |
| Merge complexity | High | Low |
| Security patch latency | Days to weeks | Hours |
| CI integration | Per-branch | Every commit to trunk |
| Release cadence fit | Scheduled (monthly/quarterly) | Continuous |
| Feature flag requirement | Optional | Required for incomplete features |
| Best for | Enterprise with scheduled releases | Startups, SaaS, continuous delivery |

---

## Section 2 — GPG-Signed Commits

### 2.1 Why Sign Commits

A Git commit contains the author name and email as plain text — anyone can set `git config user.name` to any value. Without signatures, there is no cryptographic proof of authorship. A supply chain attacker who briefly compromises a developer's workstation can impersonate them.

GPG-signed commits provide:

- Cryptographic non-repudiation — the commit was made by someone with the private key
- "Verified" badge in GitHub/GitLab, making unsigned commits visually identifiable
- Enforcement via branch protection — platforms can reject unsigned commits

### 2.2 GPG Setup Reference

```bash
# Step 1: Generate key (RSA 4096, no passphrase expiry for lab use)
gpg --full-generate-key

# Step 2: Get key ID
gpg --list-secret-keys --keyid-format=long
# Output: sec   rsa4096/ABCD1234EFGH5678

# Step 3: Export public key for GitHub
gpg --armor --export ABCD1234EFGH5678

# Step 4: Configure Git globally
git config --global user.signingkey ABCD1234EFGH5678
git config --global commit.gpgsign true
git config --global tag.gpgSign true

# Step 5: Verify a signed commit
git log --show-signature -1
```

### 2.3 SSH Signing (Modern Alternative)

GitHub also supports SSH key signing as of 2022, which many developers find simpler since they already manage SSH keys:

```bash
# Configure SSH signing
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

---

## Section 3 — Branch Protection Rules

### 3.1 GitHub Branch Protection Controls

| Control | Security Purpose |
|---|---|
| Require pull request before merging | Enforces code review, prevents direct push |
| Required number of approvals | Ensures multiple reviewers; minimum 2 for sensitive branches |
| Dismiss stale reviews | Invalidates approvals after new commits |
| Require review from Code Owners | Ensures domain experts review relevant changes |
| Require status checks to pass | CI pipeline must be green before merge |
| Require branches to be up to date | Prevents stale-branch merges that bypass security fixes |
| Require signed commits | Enforces GPG/SSH signatures |
| Restrict who can push | Limits direct-push to designated users |
| Do not allow bypassing | Prevents admin override — essential for compliance |

### 3.2 CODEOWNERS File

The CODEOWNERS file maps file patterns to responsible teams or individuals. When a PR touches those files, the designated owners are automatically required as reviewers:

```gitignore
# CODEOWNERS
# Security-sensitive paths require security team review
/infra/          @org/security-team
/auth/           @org/security-team @org/backend-team
*.tf             @org/platform-team @org/security-team
Dockerfile       @org/platform-team
.github/         @org/devops-team
```

### 3.3 GitLab Protected Branches

GitLab uses "Protected Branches" under Settings > Repository. Key settings:

- Allowed to merge: Developers, Maintainers, or No One
- Allowed to push and merge: Maintainers or No One (use for main)
- Require approval: Linked to Approval Rules
- Code owner approval: Tied to CODEOWNERS file

---

## Section 4 — Git Hooks

### 4.1 Hook Types and Security Use Cases

| Hook | Trigger | Security Use |
|---|---|---|
| pre-commit | Before commit recorded | Secrets scan, lint, credential check |
| commit-msg | After commit message written | Enforce commit message policy (e.g., ticket reference) |
| pre-push | Before push to remote | Run full test suite, SAST scan |
| post-receive | Server-side, after push received | Trigger CI, notify SIEM |
| pre-receive | Server-side, before push accepted | Block direct pushes to protected branches |

### 4.2 The pre-commit Framework

Manual `.git/hooks/` scripts are not version-controlled and must be manually installed by each developer. The pre-commit framework solves this with a configuration file committed to the repo:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
        name: Detect secrets with gitleaks

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: detect-private-key
      - id: check-added-large-files
        args: [--maxkb=500]
      - id: check-json
      - id: check-yaml
      - id: no-commit-to-branch
        args: [--branch, main, --branch, develop]

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: [-lll, --recursive, .]
```

Install and use:

```bash
# Install the framework
pip install pre-commit

# Install hooks defined in .pre-commit-config.yaml
pre-commit install

# Run manually against all files
pre-commit run --all-files

# Update hook versions
pre-commit autoupdate
```

### 4.3 Bypassing Hooks — A Risk to Document

Hooks can be bypassed with `git commit --no-verify`. This is necessary in some legitimate scenarios (emergency hotfixes, broken hook environment) but creates risk. Best practices:

- Log all `--no-verify` usage via a server-side pre-receive hook
- Require post-bypass justification in the commit message or PR description
- Run the same scans in CI so the server-side pipeline catches what hooks missed

---

## Section 5 — Secrets Scanning

### 5.1 Tool Comparison: gitleaks vs. truffleHog

| Feature | gitleaks | truffleHog |
|---|---|---|
| Detection method | Regex pattern matching | Regex + entropy analysis |
| Pre-commit support | Yes (protect --staged) | Limited |
| CI integration | Yes (detect command) | Yes (git scan) |
| GitHub Actions | Official action available | Community action |
| Verified-only mode | No | Yes (--only-verified) |
| Custom rules | Yes (TOML config) | Yes |
| Output formats | JSON, SARIF, CSV | JSON |
| License | MIT | AGPL-3.0 |

### 5.2 gitleaks Configuration

Custom rules extend gitleaks beyond its built-in patterns:

```toml
# .gitleaks.toml
title = "Custom Gitleaks Configuration"

[[rules]]
id = "internal-api-key"
description = "Internal API key pattern"
regex = '''(?i)internal[_-]?api[_-]?key\s*=\s*['"][A-Za-z0-9]{32,}['"]'''
severity = "CRITICAL"
tags = ["api", "internal"]

[allowlist]
description = "Allowlist for known false positives"
regexes = [
  '''EXAMPLE_KEY''',
  '''TEST_SECRET'''
]
paths = [
  '''docs/''',
  '''tests/fixtures/'''
]
```

### 5.3 GitHub Native Secret Scanning

For repositories on GitHub, enable secret scanning under Settings > Security:

- Secret scanning alerts notify repository admins when patterns are detected
- Push protection blocks pushes containing detected secrets in real time
- Partner patterns: 200+ token types from providers including AWS, Azure, Google, Stripe, Twilio are automatically revoked when detected in public repos

---

## Section 6 — .gitignore Best Practices

### 6.1 What to Always Ignore

```gitignore
# Secrets and credentials
.env
.env.*
!.env.example
*.pem
*.key
*.p12
*.pfx
secrets/
credentials.json
service-account.json
*_credentials.json

# Cloud provider credentials
.aws/
.azure/
.gcp/
kubeconfig

# IDE and OS files
.vscode/settings.json
.idea/
*.swp
.DS_Store
Thumbs.db

# Build artifacts
dist/
build/
target/
*.class
node_modules/
.venv/
__pycache__/
```

### 6.2 The .env.example Pattern

Never commit `.env` but always commit `.env.example` with placeholder values to document required environment variables:

```bash
# .env.example — commit this file
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
AWS_ACCESS_KEY_ID=your-key-id-here
AWS_SECRET_ACCESS_KEY=your-secret-here
JWT_SECRET=your-jwt-secret-here
```

---

## Exam Tips for DSOE Certification

- Know the difference between GitFlow (long-lived branches) and trunk-based development (short-lived, feature flags).
- GPG signing provides cryptographic non-repudiation — not just identity; it proves possession of a private key.
- Branch protection rules are server-side enforced — pre-commit hooks are client-side and can be bypassed.
- The pre-commit framework version-controls hook configuration, ensuring all developers run the same checks.
- gitleaks uses regex patterns; truffleHog adds entropy analysis for unknown secret formats.
- GitHub native secret scanning includes push protection — it blocks the push before the secret enters the repo.
- `.gitignore` prevents staging; it does not remove already-committed files from history.
- To remove a secret from Git history: `git filter-repo` or BFG Repo Cleaner, followed by a force push and credential rotation.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| GitFlow | Branching model with long-lived feature, develop, release, and hotfix branches |
| Trunk-Based Development | All developers integrate to main frequently; branches live less than 2 days |
| GPG | GNU Privacy Guard — cryptographic key management for signing |
| Signed Commit | Git commit with a cryptographic signature proving authorship |
| Branch Protection | Server-side rules preventing direct pushes and enforcing review/CI |
| CODEOWNERS | File mapping paths to required reviewers |
| pre-commit | Python framework for managing client-side git hooks |
| gitleaks | Open-source secrets scanning tool for git repositories |
| truffleHog | Secrets scanner with entropy-based detection |
| .gitignore | File specifying paths Git should not track |
| Push Protection | GitHub feature blocking pushes containing detected secrets |
| Feature Flag | Runtime toggle hiding incomplete features from end users |

---

Reading Guide — Module 02 | CIS-4350 | Texas Wesleyan University | Professor Nash
