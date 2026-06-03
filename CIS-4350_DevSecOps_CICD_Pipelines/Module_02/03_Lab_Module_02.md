# Lab 02 — Version Control Security: Signed Commits, Branch Protection, and Secrets Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will configure GPG commit signing, set up branch protection rules on GitHub, implement a pre-commit hook configuration for secrets scanning, and practice the full secrets remediation workflow including history cleaning.

**Estimated Time:** 90–120 minutes

**Difficulty:** Intermediate

---

## Prerequisites

- Git 2.34+ installed (`git --version`)
- GPG installed (`gpg --version`)
- GitHub account with a test repository
- Python 3.8+ for the pre-commit framework (`python --version`)
- Docker (optional, for gitleaks container)

---

## Part 1 — GPG Commit Signing (30 minutes)

### Part 1 Objective

Configure your local Git to sign all commits with a GPG key and verify that GitHub displays the "Verified" badge.

### Step 1.1 — Generate a GPG Key

```bash
gpg --full-generate-key
```

When prompted:

- Key type: RSA and RSA (option 1)
- Key size: 4096
- Expiration: 0 (does not expire — acceptable for course use)
- Name: Your full name
- Email: Your GitHub-registered email address (critical — must match)
- Comment: Leave blank
- Passphrase: Choose a passphrase and remember it

### Step 1.2 — Retrieve Your Key ID

```bash
gpg --list-secret-keys --keyid-format=long
```

Expected output:

```text
sec   rsa4096/A1B2C3D4E5F6G7H8 2024-01-15 [SC]
      FINGERPRINT...
uid   [ultimate] Your Name <you@example.com>
```

Note the 16-character key ID after `rsa4096/`.

### Step 1.3 — Export Public Key and Add to GitHub

```bash
gpg --armor --export A1B2C3D4E5F6G7H8
```

Copy the full output (including `-----BEGIN PGP PUBLIC KEY BLOCK-----` headers). In GitHub: Settings > SSH and GPG keys > New GPG key. Paste and save.

### Step 1.4 — Configure Git to Sign All Commits

```bash
git config --global user.signingkey A1B2C3D4E5F6G7H8
git config --global commit.gpgsign true
git config --global tag.gpgSign true
```

### Step 1.5 — Make a Signed Commit and Verify

```bash
mkdir ~/lab02-signing && cd ~/lab02-signing
git init
git checkout -b main
echo "# Lab 02 Signing Demo" > README.md
git add README.md
git commit -m "Initial commit with GPG signing"
git log --show-signature -1
```

The output should include `gpg: Good signature from "Your Name <you@example.com>"`.

### Step 1.6 — Push and Verify on GitHub

Push the repository to GitHub and navigate to the commits page. Verify the "Verified" green badge appears on your commit.

---

## Part 2 — Branch Protection Rules (20 minutes)

### Part 2 Objective

Configure branch protection rules to require signed commits, code review, and CI status checks.

### Step 2.1 — Create a GitHub Repository

Create a new public repository called `lab02-branch-protection` on GitHub.

### Step 2.2 — Configure Branch Protection via GitHub UI

Navigate to Settings > Branches > Add branch protection rule. Set branch name pattern to `main`.

Enable the following:

- Require a pull request before merging
- Required number of approvals: 1
- Dismiss stale pull request approvals when new commits are pushed
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Require signed commits
- Do not allow bypassing the above settings

Click "Create" to save.

### Step 2.3 — Test Protection via Direct Push Attempt

```bash
cd ~/lab02-signing
git remote add origin https://github.com/YOUR_USERNAME/lab02-branch-protection.git
git push -u origin main
```

Create a second commit directly and attempt a direct push:

```bash
echo "Direct push test" >> README.md
git add README.md
git commit -m "Attempt direct push to main"
git push origin main
```

If branch protection is configured correctly, this push will be rejected with an error message. Record the exact error message in your lab report.

### Step 2.4 — Use a Pull Request Workflow

```bash
git checkout -b feature/add-content
echo "## About This Project" >> README.md
git add README.md
git commit -m "Add about section"
git push origin feature/add-content
```

Open a pull request on GitHub and observe that the status checks requirement is shown (even if no checks are configured yet, the requirement will display).

---

## Part 3 — Pre-Commit Framework for Secrets Prevention (30 minutes)

### Part 3 Objective

Install the pre-commit framework and configure it to automatically detect secrets before they enter the repository.

### Step 3.1 — Install pre-commit

```bash
pip install pre-commit
pre-commit --version
```

### Step 3.2 — Create a Pre-Commit Configuration

```bash
mkdir ~/lab02-hooks && cd ~/lab02-hooks
git init
git checkout -b main
```

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
        name: Detect secrets (gitleaks)

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: detect-private-key
        name: Detect private keys
      - id: check-added-large-files
        args: [--maxkb=1024]
      - id: check-json
      - id: check-yaml
      - id: no-commit-to-branch
        args: [--branch, main]
      - id: trailing-whitespace
      - id: end-of-file-fixer
```

### Step 3.3 — Install the Hooks

```bash
pre-commit install
```

You should see: `pre-commit installed at .git/hooks/pre-commit`

### Step 3.4 — Test Secret Detection

Create a file with a fake secret:

```bash
cat > config.py << 'EOF'
# This is a test file for the lab
DATABASE_HOST = "localhost"
# Fake AWS key for testing -- DO NOT USE IN REAL CODE
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
EOF
```

Attempt to commit:

```bash
git add config.py
git commit -m "Test secret detection"
```

The pre-commit hook should block the commit and display the gitleaks finding. Record the output.

### Step 3.5 — Remediate and Confirm Pass

```bash
cat > config.py << 'EOF'
import os

# Secrets loaded from environment variables only
DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
EOF
```

Also create `.env.example`:

```bash
cat > .env.example << 'EOF'
DATABASE_HOST=localhost
AWS_ACCESS_KEY_ID=your-key-id-here
AWS_SECRET_ACCESS_KEY=your-secret-here
EOF
```

Create `.gitignore`:

```gitignore
.env
.env.*
!.env.example
*.pem
*.key
```

```bash
git add .pre-commit-config.yaml config.py .env.example .gitignore
git commit -m "Add pre-commit config, remediate secrets, add env template"
```

All hooks should pass. Record the output.

---

## Part 4 — Secrets Remediation in Git History (20 minutes)

### Part 4 Objective

Practice removing a secret that was accidentally committed to Git history.

### Step 4.1 — Simulate an Accidental Secret Commit

```bash
# Temporarily disable hooks for this simulation
echo "SLACK_TOKEN=xoxb-example-token-12345678" > slack_config.py
git add slack_config.py
git commit --no-verify -m "Add Slack integration config"
```

Verify the secret is in history:

```bash
git log --oneline
git show HEAD:slack_config.py
```

### Step 4.2 — Remove the Secret Using git-filter-repo

```bash
pip install git-filter-repo

# Remove the file from all history
git filter-repo --path slack_config.py --invert-paths --force
```

### Step 4.3 — Verify Removal

```bash
git log --oneline
git show HEAD:slack_config.py 2>&1
```

The file should no longer exist in the repository history. Record the git log output before and after.

### Step 4.4 — Document the Incident

In your lab report, answer: In a real scenario after removing a secret from Git history, what other steps must you take? (Hint: consider the secret itself, not just the repository.)

---

## Deliverables

Submit the following on Canvas:

1. Screenshot showing "Verified" badge on a signed commit in GitHub (Part 1, Step 1.6)
2. Screenshot of the direct push rejection error message (Part 2, Step 2.3)
3. Screenshot of gitleaks blocking the commit with fake AWS credentials (Part 3, Step 3.4)
4. Screenshot of all pre-commit hooks passing after remediation (Part 3, Step 3.5)
5. Git log output before and after git-filter-repo removal (Part 4, Steps 4.1 and 4.3)
6. Written answer: what steps must follow secret removal from Git history (Part 4, Step 4.4 — minimum 100 words)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Signed commit with Verified badge screenshot | 20 |
| Branch protection rejection screenshot with error text | 15 |
| gitleaks block screenshot | 20 |
| All hooks passing after remediation screenshot | 15 |
| git-filter-repo before/after log output | 15 |
| Incident response write-up (100+ words) | 15 |
| Total | 100 |

---

Lab 02 | CIS-4350 | Texas Wesleyan University | Professor Nash
