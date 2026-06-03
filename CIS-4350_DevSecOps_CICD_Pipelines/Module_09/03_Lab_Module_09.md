# Lab Activity: Module 09 - Secrets Management: HashiCorp Vault and AWS Secrets Manager

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Detect secrets in Git history using Gitleaks.
- Configure a pre-commit hook that prevents secrets from being committed.
- Integrate secrets scanning into a GitHub Actions pipeline.
- Analyze Docker image layer exposure and apply BuildKit secret mounts.
- Explain the OIDC federation pattern for cloud credential management in CI/CD.

---

## Prerequisites

Before beginning this lab, confirm the following:

- Git is installed and you have a GitHub account.
- Docker is installed and BuildKit is available (`DOCKER_BUILDKIT=1`).
- Gitleaks is installed (`gitleaks version`) or you can install it from the Gitleaks GitHub releases page.
- You have completed the Module 09 video and reading guide.

---

## Part 1: Secrets Detection with Gitleaks (30 points)

### Part 1 Background

Gitleaks scans Git history and staged changes for known secret patterns. This part walks through detecting intentionally planted secrets and configuring a pre-commit hook to prevent future commits.

### Part 1 Instructions

**Step 1: Create a test repository with planted secrets.**

```bash
mkdir lab09-secrets && cd lab09-secrets
git init
```

Create a file `config.py` with these intentionally insecure values:

```python
DATABASE_URL = "postgresql://admin:SuperSecret123@db.example.com/myapp"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ012345"
```

Commit this file:

```bash
git add config.py
git commit -m "add config"
```

Then create a second commit that removes the secrets:

```bash
echo "# secrets removed" > config.py
git add config.py
git commit -m "remove secrets"
```

**Step 2: Run Gitleaks to scan the full repository history.**

```bash
gitleaks detect --source . --verbose
```

Record the complete Gitleaks output. Note which secrets were detected, which commits they were found in, and the line numbers.

**Step 3: Configure a Gitleaks pre-commit hook.**

Create a `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks:
      - id: gitleaks
```

Install pre-commit and activate the hooks:

```bash
pip install pre-commit
pre-commit install
```

Attempt to stage and commit a new file containing a secret to verify the hook fires:

```bash
echo 'SECRET_KEY = "sk-proj-testkey12345"' > test_secret.py
git add test_secret.py
git commit -m "this should be blocked"
```

Record the pre-commit hook output and the exit code.

**Step 4: Explain the `fetch-depth: 0` requirement.**

In 2-3 sentences, explain why a GitHub Actions workflow that runs `actions/checkout@v4` without `fetch-depth: 0` would miss the secrets you committed in Step 1, and what the default checkout behavior is.

### Part 1 Deliverable

Submit: the Gitleaks detect output showing all findings, a screenshot of the blocked commit from the pre-commit hook, and the written explanation of `fetch-depth: 0`.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Gitleaks output shows all four planted secrets with commit and line references | 12 |
| Pre-commit hook correctly blocks the test commit and output is captured | 10 |
| Explanation of `fetch-depth: 0` is technically accurate | 8 |

---

## Part 2: GitHub Actions Secrets Scanning Integration (25 points)

### Part 2 Background

Secrets scanning must be part of the CI/CD pipeline to catch secrets introduced despite local hook protections — for example, from contributors who do not have the hook installed or from direct pushes.

### Part 2 Instructions

**Step 1: Add a secrets scanning job to your existing GitHub Actions pipeline.**

In your `full-pipeline.yml`, add a `secrets-scan` job that runs before the build job. The job must check out the code with `fetch-depth: 0`, run `gitleaks/gitleaks-action@v2`, and use `secrets.GITHUB_TOKEN` for the `GITHUB_TOKEN` environment variable.

**Step 2: Push the lab09 repository to GitHub and trigger the pipeline.**

The repository should contain the `config.py` file with planted secrets from Part 1 (re-add it to test the pipeline gate).

Add `config.py` back with the secret values and push to a feature branch. Record the pipeline job output showing Gitleaks findings.

**Step 3: Create a Gitleaks baseline file.**

For production pipelines, known false positives can be baselined to prevent blocking on findings that have been reviewed and accepted. Generate a baseline:

```bash
gitleaks detect --source . --baseline-path .gitleaks-baseline.json --report-path .gitleaks-baseline.json
```

Explain in 2-3 sentences what a secrets scanning baseline is, when it is appropriate to use one, and what the risk is of an overly broad baseline.

### Part 2 Deliverable

Submit: the updated pipeline YAML with the secrets-scan job, a screenshot of the pipeline failure showing Gitleaks findings, and the written baseline explanation.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Pipeline YAML correctly adds secrets-scan job with `fetch-depth: 0` and Gitleaks action | 10 |
| Screenshot shows pipeline failure with Gitleaks findings | 8 |
| Baseline explanation is technically accurate and addresses the false-positive tradeoff | 7 |

---

## Part 3: Docker Image Layer Secret Exposure (25 points)

### Part 3 Background

Secrets baked into Docker images during build steps are recoverable from image layer history, even if the secret is deleted in a subsequent layer. This part demonstrates the vulnerability and the BuildKit fix.

### Part 3 Instructions

**Step 1: Create an insecure Dockerfile that bakes a secret into a layer.**

```dockerfile
FROM python:3.11-slim
ARG REGISTRY_TOKEN
RUN pip install --extra-index-url https://user:${REGISTRY_TOKEN}@pypi.internal.example.com myapp
```

Build it with a dummy token:

```bash
docker build --build-arg REGISTRY_TOKEN=supersecrettoken -t lab09-insecure .
```

Inspect the layer history to show the exposed secret:

```bash
docker history lab09-insecure --no-trunc
```

Record the command output showing where the token appears in the layer history.

**Step 2: Fix the Dockerfile using BuildKit secret mounts.**

Rewrite the Dockerfile to use BuildKit's `--mount=type=secret` syntax:

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11-slim
RUN --mount=type=secret,id=registry_token \
    REGISTRY_TOKEN=$(cat /run/secrets/registry_token) && \
    pip install --extra-index-url https://user:${REGISTRY_TOKEN}@pypi.internal.example.com myapp
```

Build using BuildKit:

```bash
DOCKER_BUILDKIT=1 docker build \
    --secret id=registry_token,src=./registry_token.txt \
    -t lab09-secure .
```

Run `docker history lab09-secure --no-trunc` on the secure image and compare the output to the insecure image.

**Step 3: Write the comparison analysis.**

In 100-150 words, explain: why the `ARG` approach exposes the secret in layer history even though the secret was not written to any file, what the BuildKit secret mount does differently at the layer level, and why this matters for images pushed to a container registry.

### Part 3 Deliverable

Submit: the insecure `docker history` output showing the exposed token, the secure `docker history` output showing no token, and the written comparison analysis.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| Insecure docker history output correctly shows the token in a layer | 8 |
| Secure docker history output confirms no token in any layer | 8 |
| Written analysis accurately explains the layer persistence mechanism and BuildKit fix | 9 |

---

## Part 4: Secrets Management Concepts (20 points)

### Part 4 Instructions

Answer each question in 3-5 sentences using precise secrets management and DevSecOps terminology.

**Question A:** A developer discovers that their team's AWS access key was committed to a public GitHub repository six months ago. The key has since been removed from the repository in a subsequent commit. The developer argues that since the secret is no longer in the current version of the file, there is no security risk. Explain why this reasoning is incorrect, what the correct remediation steps are (in order), and how secrets scanning tools detect this type of historical exposure.

**Question B:** Your organization is evaluating whether to use GitHub Secrets (CI/CD platform secrets) or HashiCorp Vault AppRole for injecting database credentials into a GitHub Actions deployment pipeline. Identify two specific security capabilities that Vault provides that GitHub Secrets cannot, and describe a use case where GitHub Secrets is a sufficient and appropriate choice.

**Question C:** Explain what OIDC federation is in the context of a GitHub Actions pipeline deploying to AWS, and describe specifically what happens during the authentication exchange — what does GitHub issue, what does AWS verify, and what does the pipeline receive. Explain what long-lived credential risk OIDC federation eliminates.

### Part 4 Deliverable

Submit written answers to all three questions. Label each answer with the question letter.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Question A correctly explains Git history persistence and gives correct remediation order | 7 |
| Question B identifies two accurate Vault advantages and correctly characterizes the GitHub Secrets use case | 6 |
| Question C accurately explains OIDC federation exchange and identifies the eliminated risk | 7 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (09) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
