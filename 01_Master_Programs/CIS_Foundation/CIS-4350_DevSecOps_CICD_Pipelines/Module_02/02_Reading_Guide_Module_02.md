# Reading Guide: Module 02 — Version Control Security and Git Best Practices

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4350 &BULL; DEVSECOPS & CI/CD SECURITY AUTOMATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

## 9. Supplemental Resources

**1. [GitHub Docs — About secret scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning)**
Official GitHub documentation covering push protection, partner patterns, and how to configure secret scanning for public and private repositories. Essential reference for the secrets management portions of this module.

**2. [pre-commit framework documentation](https://pre-commit.com/)**
The official documentation for the pre-commit framework, including all available hooks, configuration syntax, and integration with CI. Covers hook management, versioning, and CI mode (`pre-commit run --all-files`).

**3. [git-filter-repo documentation and usage guide](https://github.com/newren/git-filter-repo)**
The recommended tool for rewriting Git history to remove accidentally committed secrets. Covers all major use cases including path removal, content replacement, and handling force-push coordination with collaborators.

---

Reading Guide — Module 02 | CIS-4350 | Texas Wesleyan University | Professor Nash
