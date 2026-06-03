# Lab 01 — DevSecOps Toolchain Mapping and Pipeline Design

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will build a conceptual DevSecOps toolchain map, install and run two foundational tools (gitleaks and Trivy), and design a basic security-integrated CI pipeline in YAML. No cloud account is required. All tools run locally via Docker or native binary.

**Estimated Time:** 90 minutes

**Difficulty:** Introductory

---

## Prerequisites

- Git installed and configured (`git --version`)
- Docker Desktop installed and running (`docker version`)
- A text editor (VS Code recommended)
- A GitHub account (free tier is sufficient)

---

## Part 1 — Toolchain Mapping Exercise (20 minutes)

### Objective

Map DevSecOps tools to the correct lifecycle phase. This exercise builds the mental model you'll need throughout the course.

### Step 1.1 — Create Your Toolchain Map

Create a new directory and file:

```bash
mkdir ~/devsecops-lab01 && cd ~/devsecops-lab01
touch toolchain_map.md
```

### Step 1.2 — Fill in the Toolchain Map

Open `toolchain_map.md` and complete the following table. Use the Module 01 reading guide, your notes, or credible web sources. The first two rows are completed as examples.

```markdown
# DevSecOps Toolchain Map — [Your Name]

| Lifecycle Phase | Activity | Tool(s) | Category |
|---|---|---|---|
| Plan | Threat modeling | STRIDE, MS Threat Modeling Tool | Threat Modeling |
| Code | Secret scanning in IDE | gitleaks, Snyk IDE | Secrets Detection |
| Build | | | |
| Build | | | |
| Test | | | |
| Release | | | |
| Deploy | | | |
| Operate | | | |
| Monitor | | | |
```

Fill in at least two tools for each remaining phase. You should have a minimum of 16 rows when complete.

### Step 1.3 — Deliverable Check

Your completed `toolchain_map.md` must include at minimum:

- Two rows for Build (one SAST, one dependency scan)
- One row for Test (DAST)
- One row for Release (SBOM)
- Two rows for Deploy (IaC scan + container scan)
- One row for Operate (runtime security)
- One row for Monitor (SIEM or log aggregation)

---

## Part 2 — Secrets Scanning with gitleaks (25 minutes)

### Part 2 Objective

Experience firsthand how secrets scanning prevents credential exposure in version control.

### Step 2.1 — Create a Test Repository

```bash
cd ~/devsecops-lab01
git init secrets-demo
cd secrets-demo
git checkout -b main
```

### Step 2.2 — Create a File with an Intentional Fake Secret

```bash
cat > config.py << 'EOF'
# Application configuration
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
# WARNING: Never commit real credentials — this is a demonstration only
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
EOF
```

```bash
git add config.py
git commit -m "Add application configuration"
```

### Step 2.3 — Run gitleaks via Docker

```bash
docker run --rm -v "$(pwd):/repo" \
  zricethezav/gitleaks:latest \
  detect --source /repo --verbose
```

### Step 2.4 — Observe Output

gitleaks will report findings similar to:

```text
Finding:     AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
Secret:      AKIAIOSFODNN7EXAMPLE
RuleID:      aws-access-token
Entropy:     3.58
File:        config.py
Line:        5
Commit:      [sha]
```

### Step 2.5 — Remediate and Re-scan

Remove the secrets from `config.py`, replacing them with environment variable references:

```python
import os
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
```

Commit the fix, then re-run gitleaks. Confirm zero findings.

```bash
git add config.py
git commit -m "Remove hardcoded credentials, use environment variables"
docker run --rm -v "$(pwd):/repo" \
  zricethezav/gitleaks:latest \
  detect --source /repo --verbose
```

### Expected Result

gitleaks reports: `leaks found: 0`

---

## Part 3 — Container Image Scanning with Trivy (25 minutes)

### Part 3 Objective

Scan a publicly available Docker image for known CVEs and interpret the severity report.

### Step 3.1 — Pull a Deliberately Vulnerable Image

```bash
docker pull python:3.8-slim
```

### Step 3.2 — Scan the Image with Trivy

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image \
  --severity HIGH,CRITICAL \
  python:3.8-slim
```

### Step 3.3 — Interpret the Output

Trivy produces a table like:

```text
python:3.8-slim (debian 11.x)
Total: 42 (HIGH: 38, CRITICAL: 4)

┌──────────────────┬───────────────┬──────────┬────────────────────────┐
│ Library          │ Vulnerability │ Severity │ Installed / Fixed Ver  │
├──────────────────┼───────────────┼──────────┼────────────────────────┤
│ libssl1.1        │ CVE-2023-xxxx │ CRITICAL │ 1.1.1n / 1.1.1t        │
└──────────────────┴───────────────┴──────────┴────────────────────────┘
```

### Step 3.4 — Compare to a Newer Image

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image \
  --severity HIGH,CRITICAL \
  python:3.12-slim
```

Record the difference in HIGH and CRITICAL counts between the two scans in your lab report.

### Step 3.5 — Export Scan Results as JSON

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$(pwd):/output" \
  aquasec/trivy:latest image \
  --format json \
  --output /output/trivy-report.json \
  python:3.8-slim
```

---

## Part 4 — Design a Basic Secure CI Pipeline (20 minutes)

### Part 4 Objective

Write a GitHub Actions workflow YAML that integrates gitleaks and Trivy as security gates.

### Step 4.1 — Create the Workflow File

```bash
cd ~/devsecops-lab01
mkdir -p .github/workflows
touch .github/workflows/devsecops-pipeline.yml
```

### Step 4.2 — Write the Pipeline

Paste the following into `devsecops-pipeline.yml`:

```yaml
name: DevSecOps Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  secrets-scan:
    name: Secrets Detection
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  container-scan:
    name: Container Image Scan
    runs-on: ubuntu-latest
    needs: secrets-scan
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t app:${{ github.sha }} .

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}
          format: sarif
          output: trivy-results.sarif
          severity: CRITICAL,HIGH
          exit-code: "1"

      - name: Upload Trivy results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: trivy-results.sarif
```

### Step 4.3 — Add a Minimal Dockerfile

```bash
cat > Dockerfile << 'EOF'
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true
CMD ["python", "-m", "http.server", "8080"]
EOF
```

### Step 4.4 — Commit and Push to GitHub

Push the repository to GitHub and observe the Actions tab to see your pipeline execute.

```bash
git add .github/ Dockerfile
git commit -m "Add DevSecOps CI pipeline with gitleaks and Trivy"
git remote add origin https://github.com/YOUR_USERNAME/devsecops-lab01.git
git push -u origin main
```

---

## Deliverables

Submit the following on Canvas:

1. `toolchain_map.md` — Completed with 16+ rows (Part 1)
2. Screenshot of gitleaks finding the fake AWS credential (Part 2, Step 2.3)
3. Screenshot of gitleaks reporting zero findings after remediation (Part 2, Step 2.5)
4. Screenshot comparing Trivy HIGH/CRITICAL counts for python:3.8-slim vs python:3.12-slim (Part 3, Step 3.4)
5. `devsecops-pipeline.yml` — Your completed workflow file (Part 4)
6. Lab reflection (minimum 150 words): What surprised you about the number of vulnerabilities in a "standard" base image? How does this change your perspective on container image selection?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Toolchain map — completeness (16+ rows, correct phases) | 20 |
| gitleaks — secret detected and screenshot provided | 15 |
| gitleaks — remediation confirmed with zero findings | 15 |
| Trivy — both images scanned, count comparison recorded | 20 |
| Pipeline YAML — syntactically correct, both jobs present | 20 |
| Lab reflection — substantive, minimum 150 words | 10 |
| **Total** | **100** |

---

Lab 01 | CIS-4350 | Texas Wesleyan University | Professor Nash
