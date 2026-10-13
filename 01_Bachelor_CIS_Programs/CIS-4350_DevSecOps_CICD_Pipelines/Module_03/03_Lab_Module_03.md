# Lab 03 — Building a Security-Integrated CI Pipeline with GitHub Actions

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will build a complete GitHub Actions CI pipeline that integrates secrets scanning, SAST with Semgrep, and dependency vulnerability scanning as enforced security gates. You will observe pipeline failures triggered by security findings, remediate the findings, and confirm the pipeline passes.

**Estimated Time:** 90–120 minutes

**Difficulty:** Intermediate

---

## Prerequisites

- GitHub account
- Git configured with GPG signing from Lab 02
- Python 3.8+ installed locally
- A text editor (VS Code recommended)

---

## Part 1 — Repository Setup with Intentional Vulnerabilities (15 minutes)

### Part 1 Objective

Create a Python web application with deliberate security vulnerabilities to demonstrate pipeline security gate behavior.

### Step 1.1 — Initialize the Repository

```bash
mkdir ~/lab03-ci-pipeline && cd ~/lab03-ci-pipeline
git init
git checkout -b main
```

### Step 1.2 — Create a Vulnerable Python Application

```bash
mkdir src tests
```

Create `src/app.py` with deliberate vulnerabilities:

```python
# src/app.py
# WARNING: This file contains intentional vulnerabilities for lab purposes only
import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    # VULNERABILITY 1: SQL Injection — string concatenation in SQL query
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id  # SQL injection
    cursor.execute(query)
    return str(cursor.fetchall())

@app.route("/run")
def run_command():
    # VULNERABILITY 2: Command injection — unsanitized shell=True
    cmd = request.args.get("cmd")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    app.run(debug=True)  # VULNERABILITY 3: Debug mode in production
```

### Step 1.3 — Create a Requirements File with a Known Vulnerable Dependency

```bash
cat > requirements.txt << 'EOF'
flask==2.0.1
requests==2.18.0
pyyaml==5.3.1
EOF
```

Note: These are older versions that have known CVEs for demonstration purposes.

### Step 1.4 — Create a Minimal Test File

```python
# tests/test_app.py
def test_placeholder():
    """Placeholder test — real tests would cover application logic."""
    assert True
```

### Step 1.5 — Create a Basic Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
EXPOSE 8080
CMD ["python", "app.py"]
```

---

## Part 2 — Write the Security-Integrated Pipeline (30 minutes)

### Part 2 Objective

Write a complete GitHub Actions workflow with security gates that will detect the vulnerabilities you introduced in Part 1.

### Step 2.1 — Create the Workflow Directory and File

```bash
mkdir -p .github/workflows
```

Create `.github/workflows/secure-ci.yml`:

```yaml
name: Secure CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

permissions:
  contents: read
  security-events: write

env:
  PYTHON_VERSION: "3.12"

jobs:
  secrets-scan:
    name: Secrets Detection
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run gitleaks secrets scan
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ env.PYTHON_VERSION }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run unit tests with coverage
        run: pytest tests/ --tb=short --cov=src --cov-report=xml

  sast-semgrep:
    name: SAST — Semgrep
    runs-on: ubuntu-latest
    needs: unit-tests
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4

      - name: Run Semgrep SAST scan
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/owasp-top-ten
            p/python
            p/flask
          generateSarif: "1"

      - name: Upload Semgrep SARIF to GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: semgrep.sarif

  dependency-scan:
    name: Dependency Vulnerability Scan
    runs-on: ubuntu-latest
    needs: unit-tests
    steps:
      - uses: actions/checkout@v4

      - name: Run OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: lab03-app
          path: .
          format: SARIF
          out: dep-check-results/
          args: >-
            --failOnCVSS 7
            --enableRetired
            --scan requirements.txt

      - name: Upload Dependency-Check SARIF
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: dep-check-results/dependency-check-report.sarif

  security-summary:
    name: Security Gate Summary
    runs-on: ubuntu-latest
    needs: [secrets-scan, sast-semgrep, dependency-scan]
    if: always()
    steps:
      - name: Check all security gates passed
        run: |
          echo "Secrets scan: ${{ needs.secrets-scan.result }}"
          echo "SAST scan: ${{ needs.sast-semgrep.result }}"
          echo "Dependency scan: ${{ needs.dependency-scan.result }}"
          if [[ "${{ needs.secrets-scan.result }}" == "failure" || \
                "${{ needs.sast-semgrep.result }}" == "failure" || \
                "${{ needs.dependency-scan.result }}" == "failure" ]]; then
            echo "PIPELINE FAILED: One or more security gates did not pass."
            exit 1
          fi
          echo "All security gates passed."
```

### Step 2.2 — Create CODEOWNERS to Protect the Pipeline

```bash
mkdir -p .github
cat > .github/CODEOWNERS << 'EOF'
# Pipeline configuration requires security team review
.github/workflows/   @YOUR_USERNAME
EOF
```

---

## Part 3 — Push and Observe Pipeline Failures (20 minutes)

### Part 3 Objective

Push the vulnerable application to GitHub and observe how each security gate fires.

### Step 3.1 — Create the Repository on GitHub

Create a new public repository called `lab03-ci-pipeline` on GitHub.

### Step 3.2 — Push the Code

```bash
git add .
git commit -m "Initial commit: vulnerable app for CI pipeline demo"
git remote add origin https://github.com/YOUR_USERNAME/lab03-ci-pipeline.git
git push -u origin main
```

### Step 3.3 — Observe the Pipeline

Navigate to the Actions tab in your GitHub repository. Watch the pipeline jobs execute. You should see:

- Semgrep SAST flagging the SQL injection (SQL string concatenation) and command injection (`shell=True`)
- Dependency-Check flagging known CVEs in `flask==2.0.1`, `requests==2.18.0`, and `pyyaml==5.3.1`

Take screenshots of the failing jobs. Record which Semgrep rule IDs fired and which CVE IDs were found by Dependency-Check.

### Step 3.4 — Review Findings in the Security Tab

Navigate to Security > Code scanning alerts and Security > Dependency alerts. These are populated from the SARIF uploads.

---

## Part 4 — Remediate and Confirm Green Pipeline (25 minutes)

### Part 4 Objective

Fix the vulnerabilities so the pipeline passes all security gates.

### Step 4.1 — Fix the Application Code

```python
# src/app.py — remediated version
import sqlite3
import subprocess
import shlex
from flask import Flask, request

app = Flask(__name__)

ALLOWED_COMMANDS = {"uptime", "date", "hostname"}

@app.route("/user")
def get_user():
    # FIX 1: Parameterized query prevents SQL injection
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return str(cursor.fetchall())

@app.route("/run")
def run_command():
    # FIX 2: Allowlist + no shell=True prevents command injection
    cmd = request.args.get("cmd")
    if cmd not in ALLOWED_COMMANDS:
        return "Command not allowed", 403
    result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    # FIX 3: Debug mode disabled
    app.run(debug=False)
```

### Step 4.2 — Update Dependencies to Non-Vulnerable Versions

```bash
cat > requirements.txt << 'EOF'
flask==3.0.3
requests==2.32.3
pyyaml==6.0.1
pytest==8.2.0
pytest-cov==5.0.0
EOF
```

### Step 4.3 — Commit and Push the Fix

```bash
git add src/app.py requirements.txt
git commit -m "Security fixes: parameterized queries, no shell=True, update deps"
git push origin main
```

### Step 4.4 — Confirm All Gates Pass

Return to the Actions tab and confirm the pipeline is green. Take a screenshot of all jobs passing.

---

## Deliverables

Submit the following on Canvas:

1. Screenshot of failing pipeline showing Semgrep findings (Part 3, Step 3.3)
2. Screenshot of failing pipeline showing Dependency-Check CVEs (Part 3, Step 3.3)
3. Screenshot of Security tab showing code scanning alerts (Part 3, Step 3.4)
4. Completed `secure-ci.yml` workflow file (Part 2)
5. Screenshot of fully green pipeline after remediation (Part 4, Step 4.4)
6. Written reflection (minimum 150 words): What was the developer experience of discovering these vulnerabilities through the pipeline vs. discovering them in a code review? What would have happened if these vulnerabilities reached production?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Failing pipeline screenshot — Semgrep findings | 15 |
| Failing pipeline screenshot — Dependency-Check CVEs | 15 |
| Security tab screenshot with alerts | 10 |
| Workflow YAML — complete, syntactically correct | 25 |
| Green pipeline screenshot after remediation | 20 |
| Reflection — substantive, 150+ words | 15 |
| Total | 100 |

---

## Part 9 — Challenge Exercise

### Challenge 1: Implement a Reusable Security Workflow

Refactor the pipeline from this lab into a reusable workflow that can be called by multiple application repositories.

1. Create a new GitHub repository named `security-workflows` in your account.
2. Create `.github/workflows/sast-gate.yml` inside it with the following structure — the workflow should accept an `language` input and a `fail_threshold` input (default `7`), run Semgrep with the appropriate ruleset, and upload SARIF results:

```yaml
on:
  workflow_call:
    inputs:
      language:
        required: true
        type: string
      fail_threshold:
        required: false
        type: string
        default: '7'
```

3. In your `lab03` application repository, replace the inline Semgrep job with a call to the reusable workflow using `uses: YOUR_USERNAME/security-workflows/.github/workflows/sast-gate.yml@main`.
4. Verify the pipeline still produces SARIF output in the Security tab of the calling repository.

### Challenge 2: Tune Quality Gates with a Suppression File

Add an OWASP Dependency-Check suppression file to handle a known false positive without lowering the global CVSS threshold.

1. Identify one finding from your Dependency-Check SARIF report that you determine to be a false positive or accepted risk (note its CVE ID).
2. Create a `dependency-check-suppressions.xml` file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<suppressions xmlns="https://jeremylong.github.io/DependencyCheck/dependency-suppression.1.3.xsd">
  <suppress>
    <notes>Accepted risk — CVE does not apply to our usage pattern. Reviewed [date].</notes>
    <cve>CVE-YYYY-NNNNN</cve>
  </suppress>
</suppressions>
```

1. Pass the suppression file to Dependency-Check in your workflow using `--suppression dependency-check-suppressions.xml`.
2. Confirm the previously flagged CVE no longer causes a gate failure while other Critical CVEs still fail the build.

### Reflection Questions

1. Your reusable workflow is pinned at `@main`. A security engineer pushes an update to `sast-gate.yml` that tightens the CVSS threshold from 7 to 6. All consuming repositories inherit this change on their next run. What are the benefits and risks of this coupling? How would you mitigate the risks while preserving the governance benefit?
2. A developer argues that suppression files undermine the point of security gates because anyone can suppress any finding. How would you design a process around suppression file changes to maintain security governance — what branch protection rules, reviewer requirements, and documentation standards would you require?

---

Lab 03 | CIS-4350 | Texas Wesleyan University | Professor Nash
