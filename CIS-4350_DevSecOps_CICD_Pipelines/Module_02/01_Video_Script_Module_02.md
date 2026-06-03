# Video Script: Module 02 — Version Control Security and Git Best Practices

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–1:30)

[SLIDE: Module 02 title card]

Welcome back. In Module 01 we established the DevSecOps philosophy and toolchain landscape. In Module 02 we get hands-on with the first security layer in any pipeline: version control. Git is the universal foundation of modern software development, and it is also the first place where security either holds or breaks down.

By the end of this module you'll understand branching strategies and when to use each, how to sign commits with GPG keys, how to configure branch protection rules, how to use git hooks as automated security gates, and how to detect and prevent secrets from entering your repositories.

---

### SEGMENT 2 — Why Version Control Security Matters (1:30–4:00)

[SLIDE: Headline: "600,000 secrets found in public GitHub repos — GitGuardian 2023"]

Version control is where all software begins its journey. A security weakness here propagates forward into every subsequent stage of the pipeline. Let me give you three concrete failure modes.

First, secrets exposure. The GitGuardian State of Secrets Sprawl report consistently finds hundreds of thousands of API keys, passwords, and tokens committed to public GitHub repositories every year. Once a secret is committed — even if immediately deleted — it exists in the Git history forever unless the history is rewritten. And history rewriting is painful, error-prone, and disruptive.

Second, insecure branching. Without protected branches, any contributor can push directly to main, bypassing code review and all automated checks. A single unreviewed push can introduce a critical vulnerability.

Third, unsigned commits. Without GPG-signed commits, there is no cryptographic guarantee that a commit was actually made by the person whose name appears on it. An attacker who gains brief access to a developer's machine can make commits impersonating that developer.

These three problems have concrete solutions: secrets scanning, branch protection, and signed commits. Let's explore each.

---

### SEGMENT 3 — Branching Strategies (4:00–8:00)

[SLIDE: GitFlow diagram vs. trunk-based development diagram]

The branching strategy your team uses has direct security implications. Let's compare the two most common approaches.

GitFlow, introduced by Vincent Driessen in 2010, uses long-lived branches: main, develop, feature, release, and hotfix. The model looks like this:

```text
main
 └── develop
      ├── feature/login-page
      ├── feature/payment-api
      └── release/v1.2
           └── hotfix/critical-xss-fix
```

GitFlow provides clear separation of concerns and supports complex release schedules. The security implication: long-lived feature branches accumulate drift from main. A branch open for three weeks may miss critical security patches applied to develop. Additionally, GitFlow's complexity creates more merge points — each merge is an opportunity for conflict resolution errors that introduce bugs.

Trunk-based development, by contrast, has developers commit directly to main or merge short-lived feature branches — typically less than two days old — into main multiple times per day. There are no long-lived branches except release tags.

```text
main (trunk)
 ├── short-lived: feature/add-oauth (1 day)
 ├── short-lived: fix/sql-injection (4 hours)
 └── tag: v1.2.0
```

Trunk-based development has better security hygiene: security patches reach all developers immediately, there is no branch drift, and the CI pipeline runs on every commit to main. It requires feature flags to hide incomplete features from production, but the security and velocity benefits are significant.

For this course, we'll work with a simplified GitFlow for exercises to match what you'll encounter in enterprise environments, but we'll note the trunk-based advantages throughout.

---

### SEGMENT 4 — Signed Commits with GPG (8:00–11:00)

[SLIDE: GPG key verification badge on GitHub commit]

A signed commit uses a GPG (GNU Privacy Guard) key to create a cryptographic signature proving that the commit was made by a specific person with possession of the private key. GitHub and GitLab display a "Verified" badge on signed commits.

Here is how to set up GPG signing:

```bash
# Generate a GPG key
gpg --full-generate-key
# Select RSA and RSA, 4096 bits, no expiry for course purposes

# List your keys to get the key ID
gpg --list-secret-keys --keyid-format=long

# Export the public key for GitHub
gpg --armor --export YOUR_KEY_ID

# Configure Git to use your key
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true

# Make a signed commit
git commit -S -m "Add signed commit example"
```

Once you paste your public key into GitHub at Settings > SSH and GPG Keys, every signed commit will show the "Verified" badge. Unsigned commits will show "Unverified."

For organizations, the next step is requiring signed commits via branch protection rules. When required signing is enabled, any push containing unsigned commits is rejected by GitHub, regardless of the branch protection bypass permissions.

---

### SEGMENT 5 — Protected Branches (11:00–14:00)

[SLIDE: GitHub branch protection settings screenshot mockup]

Branch protection rules are enforced server-side by the Git hosting platform. GitHub calls them "Branch protection rules" and "Rulesets." GitLab calls them "Protected branches." The controls available include:

Require pull request reviews before merging. This enforces code review and prevents direct pushes to the protected branch. You can require one, two, or more approvals. You can also require review from code owners — people designated as responsible for specific files or directories via a CODEOWNERS file.

Require status checks to pass before merging. This ties your CI pipeline to branch protection. If the CI pipeline fails — including security scan stages — the pull request cannot be merged. This is the critical connection between pipeline security gates and version control governance.

Require signed commits. As discussed, this enforces GPG signatures.

Restrict who can push to matching branches. Limits direct pushes to administrators or specific users or teams.

Do not allow bypassing the above settings. Prevents administrators from overriding protection rules — important for compliance environments where even admins must follow process.

Here is a minimal GitHub Ruleset configuration expressed as JSON for API automation:

```json
{
  "name": "main-protection",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/main"],
      "exclude": []
    }
  },
  "rules": [
    { "type": "required_signatures" },
    { "type": "pull_request",
      "parameters": { "required_approving_review_count": 2 } },
    { "type": "required_status_checks",
      "parameters": {
        "required_status_checks": [
          { "context": "secrets-scan" },
          { "context": "sast-scan" }
        ]
      }
    }
  ]
}
```

---

### SEGMENT 6 — Git Hooks for Security (14:00–17:00)

[SLIDE: Git hook lifecycle diagram]

Git hooks are scripts that run automatically at specific points in the Git workflow. The hooks most relevant to security are pre-commit and commit-msg.

The pre-commit hook runs before the commit is recorded. If it exits with a non-zero status, the commit is aborted. This makes it a perfect place to run secrets scanning, linting, and simple security checks.

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running pre-commit security checks..."

# Check for secrets using gitleaks
if command -v gitleaks &>/dev/null; then
  gitleaks protect --staged --verbose
  if [ $? -ne 0 ]; then
    echo "BLOCKED: Potential secrets detected. Fix before committing."
    exit 1
  fi
fi

# Check for TODO/FIXME with security implications
if git diff --cached | grep -i "password\s*=\s*['\"]"; then
  echo "BLOCKED: Hardcoded password pattern detected."
  exit 1
fi

echo "Pre-commit checks passed."
exit 0
```

The pre-commit Python framework simplifies hook management across teams. Instead of manually placing scripts in `.git/hooks/`, teams define hooks in a `.pre-commit-config.yaml` file that developers install with `pre-commit install`. The configuration is version-controlled, so all team members run the same hooks.

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: detect-private-key
      - id: check-json
      - id: check-yaml
      - id: trailing-whitespace
```

---

### SEGMENT 7 — Secrets Scanning in Repositories (17:00–20:00)

[SLIDE: gitleaks vs. truffleHog feature comparison]

Even with pre-commit hooks, secrets sometimes slip into repositories — perhaps from a developer who bypassed hooks with `git commit --no-verify`, or from a time before hooks were in place. Repository-wide secrets scanning addresses this.

Two leading open-source tools are gitleaks and truffleHog.

gitleaks scans the full Git history for patterns matching known secret formats — AWS keys, GitHub tokens, Stripe API keys, and hundreds more. It can run as a CI step, scanning every push:

```bash
# Scan the entire repo history
gitleaks detect --source . --verbose --report-path gitleaks-report.json

# Scan only staged changes (pre-commit mode)
gitleaks protect --staged --verbose
```

truffleHog has similar capabilities with the addition of entropy-based detection — it looks for high-entropy strings that may be secrets even if they don't match a known pattern:

```bash
# Scan a GitHub repository
trufflehog github --repo https://github.com/org/repo --only-verified
```

GitHub Advanced Security includes native secret scanning that alerts repository administrators when a secret matching a known pattern is pushed. Many secret providers — AWS, GitHub, Stripe, Slack — have partnered with GitHub to automatically revoke tokens when they're detected in public repositories.

The `.gitignore` file is the first line of defense against accidental commits. Always gitignore your `.env` files, credential files, and private keys. A well-configured `.gitignore` for a Python project looks like:

```gitignore
# Environment and secrets
.env
.env.*
*.pem
*.key
*_rsa
*_rsa.pub
secrets.json
credentials.json

# Python artifacts
__pycache__/
*.pyc
.venv/
dist/
build/
```

---

### SEGMENT 8 — Module Summary and Looking Ahead (20:00–22:00)

[SLIDE: Module 02 key takeaways]

Let's recap. Version control is the foundation of your security posture. The key practices are:

Choose your branching strategy deliberately — trunk-based development offers security advantages through reduced branch drift and immediate patch propagation.

Sign commits with GPG keys to provide cryptographic proof of authorship.

Configure branch protection rules to require code review, passing CI status checks, and signed commits.

Use git hooks — especially pre-commit hooks managed via the pre-commit framework — to catch secrets and policy violations before they enter the repository.

Scan repository history with gitleaks or truffleHog to detect secrets that bypassed earlier controls.

Use a comprehensive `.gitignore` to prevent sensitive files from ever being staged.

In Module 03 we'll build on this foundation by constructing full CI pipelines in GitHub Actions and GitLab CI, adding SAST and dependency scanning stages as security gates. See you there.

---

*[END OF SCRIPT — Module 02]*
