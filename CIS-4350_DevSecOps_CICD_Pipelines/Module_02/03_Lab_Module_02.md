# Lab Activity: Module 02 - Version Control with Git and GitHub

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Configure a Git repository with a pre-commit hook that runs secrets detection before every commit.
- Write a GitHub Actions workflow triggered on push to main that checks out code and runs tests.
- Explain the security purpose of each workflow step and pipeline design decision.
- Identify branch protection settings that enforce pipeline status checks as merge requirements.

---

## Prerequisites

Before beginning this lab, confirm the following:

- You have Git installed locally (`git --version` returns a result).
- You have a GitHub account and can create a public or private repository.
- You have Python 3.8 or later installed locally (`python --version` or `python3 --version`).
- You have completed the Module 02 video and reading guide.

---

## Part 1: Configure a Local Pre-Commit Hook (25 points)

### Part 1 Background

Pre-commit hooks are the earliest shift-left control in the DevSecOps pipeline. This part walks you through installing and verifying a secrets-detection pre-commit hook in a real Git repository.

### Part 1 Instructions

**Step 1: Create a test repository.**

```bash
mkdir devsecops-lab02
cd devsecops-lab02
git init
git checkout -b main
```

**Step 2: Install the pre-commit framework.**

```bash
pip install pre-commit
```

**Step 3: Create the hook configuration file.**

Create a file named `.pre-commit-config.yaml` in the repository root with the following content:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: detect-private-key
        name: Block private key files
      - id: check-yaml
        name: Validate YAML syntax
      - id: end-of-file-fixer
        name: Ensure files end with newline
      - id: trailing-whitespace
        name: Remove trailing whitespace
```

**Step 4: Install hooks into the repository.**

```bash
pre-commit install
```

Confirm the installation succeeded. The output should include: `pre-commit installed at .git/hooks/pre-commit`

**Step 5: Create a test file with a simulated private key and attempt to commit it.**

```bash
cat > test_secret.txt << 'EOF'
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2a2rwplBQLzHPZe5
-----END RSA PRIVATE KEY-----
EOF

git add test_secret.txt
git commit -m "test: attempt to commit simulated private key"
```

The commit should be blocked. Record the exact error message output.

**Step 6: Remove the simulated secret and commit the clean file.**

```bash
echo "no secrets here" > test_secret.txt
git add test_secret.txt
git commit -m "test: clean file commits successfully"
```

Confirm this commit succeeds.

### Part 1 Deliverable

Submit a document containing: a screenshot or copy of the blocked commit output from Step 5, a screenshot or copy of the successful commit output from Step 6, and a 3-4 sentence explanation of why pre-commit hooks must be paired with a CI pipeline secrets scan for full protection.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| `.pre-commit-config.yaml` is correctly structured and submitted | 5 |
| Blocked commit output is shown with the correct error | 8 |
| Successful clean commit output is shown | 7 |
| Explanation of hook + CI pipeline defense-in-depth is technically accurate | 5 |

---

## Part 2: Write a GitHub Actions Workflow (40 points)

### Part 2 Background

GitHub Actions workflows are the automation engine for DevSecOps pipelines. This part requires you to write a complete workflow that runs on push to main, checks out code, sets up a Python environment, installs dependencies, and runs tests. This is the required workflow specification from the course lab requirements.

### Part 2 Instructions

**Step 1: Create the workflow directory in your lab repository.**

```bash
mkdir -p .github/workflows
```

**Step 2: Write the complete workflow file.**

Create `.github/workflows/ci.yml` with a workflow that satisfies all of the following requirements:

- Triggers on push to the `main` branch.
- Has a single job named `build-and-test` running on `ubuntu-latest`.
- Step 1: Checks out the repository code using `actions/checkout@v4`.
- Step 2: Sets up Python 3.11 using `actions/setup-python@v5`.
- Step 3: Installs dependencies from `requirements.txt` using `pip install -r requirements.txt`.
- Step 4: Runs tests using `pytest tests/`.
- Sets `permissions: contents: read` at the workflow level.

The completed workflow must follow this structure:

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

permissions:
  contents: read

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      # Step 1: Checkout
      # Step 2: Python setup
      # Step 3: Install deps
      # Step 4: Run tests
```

Fill in all four steps completely. Each step must have a `name:` field and either a `uses:` or `run:` field.

**Step 3: Create a minimal requirements.txt and test file so the workflow can execute.**

```bash
echo "pytest==7.4.0" > requirements.txt

mkdir -p tests
cat > tests/test_hello.py << 'EOF'
def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "devsecops".upper() == "DEVSECOPS"
EOF
```

**Step 4: Push to GitHub and verify the workflow runs.**

Create a repository on GitHub, add it as a remote, and push:

```bash
git remote add origin https://github.com/YOUR_USERNAME/devsecops-lab02.git
git add .
git commit -m "feat: add CI workflow, tests, and pre-commit config"
git push -u origin main
```

Navigate to the Actions tab in your GitHub repository and confirm the workflow runs and all steps pass.

### Part 2 Deliverable

Submit: your complete `.github/workflows/ci.yml` file, a screenshot of the successful workflow run in the GitHub Actions tab showing all steps passed, and a 2-3 sentence explanation of what the `permissions: contents: read` setting does and why it is a security best practice.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Workflow YAML is syntactically correct and complete with all four steps | 15 |
| Workflow triggers correctly on push to main | 5 |
| All four steps use correct action names and parameters | 10 |
| Screenshot shows successful workflow run with all steps green | 5 |
| Permissions explanation is technically accurate | 5 |

---

## Part 3: Branch Protection Analysis (20 points)

### Part 3 Background

Branch protection rules enforce that pipeline security checks must pass before code can merge. This part asks you to configure and document branch protection settings, then analyze their security impact.

### Part 3 Instructions

**Step 1: Enable branch protection on your lab repository.**

In your GitHub repository, navigate to Settings, then Branches. Add a branch protection rule for the `main` branch. Enable the following settings:

- Require a pull request before merging
- Require status checks to pass before merging (add your `build-and-test` job as a required check)
- Require branches to be up to date before merging
- Do not allow bypassing the above settings

**Step 2: Test the protection.**

Attempt to push a commit directly to main from the command line. Record what happens.

**Step 3: Document the analysis.**

Answer the following questions in writing:

1. What error or behavior did you observe when attempting a direct push to main?
2. Why does requiring the `build-and-test` status check to pass make the CI workflow a mandatory security gate rather than an optional advisory?
3. What is the risk of NOT checking "Do not allow bypassing the above settings"? Who could bypass the rules, and how does this undermine the DevSecOps shared responsibility model?

### Part 3 Deliverable

Submit: a screenshot of your branch protection rule configuration, a screenshot or description of the direct-push rejection, and written answers to the three analysis questions.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| Branch protection rule is correctly configured (screenshot) | 6 |
| Direct push rejection is documented | 4 |
| Three analysis questions answered with technical accuracy | 10 |

---

## Part 4: Reflection on Shift-Left Enforcement (15 points)

### Part 4 Instructions

Write a 200-250 word reflection addressing the following:

The pre-commit hook you configured in Part 1 and the CI workflow you wrote in Part 2 both serve shift-left security goals, but they operate at different points in the Git workflow and have different bypass characteristics.

1. Explain the specific shift-left role of each control: what stage does the pre-commit hook operate at, and what stage does the CI pipeline operate at?
2. Describe the bypass vector for each: how could a developer skip the pre-commit hook, and why is the CI pipeline not subject to the same bypass?
3. Explain why the combination of both controls implements defense-in-depth rather than redundancy.

### Part 4 Deliverable

Submit your written reflection (200-250 words) as part of your combined submission document.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Shift-left stage of each control is correctly identified | 5 |
| Bypass vector for each is accurately described | 5 |
| Defense-in-depth argument is technically sound | 5 |

---

## Submission Instructions

Combine all four parts into a single PDF or Word document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (02) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
