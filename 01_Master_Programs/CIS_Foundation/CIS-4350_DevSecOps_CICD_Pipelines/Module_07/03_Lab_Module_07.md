# Lab 07 — Application Security Testing: Semgrep, OWASP ZAP, and SBOM

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will run Semgrep SAST scans on a vulnerable Python application, run OWASP ZAP in baseline scan mode against OWASP Juice Shop (a deliberately vulnerable application), run OWASP Dependency-Check with a CVSS quality gate, generate an SBOM with Syft, and integrate all four into a GitHub Actions pipeline.

**Estimated Time:** 90–120 minutes

**Difficulty:** Intermediate

---

## Prerequisites

- Docker Desktop running
- Python 3.8+ installed
- Git and GitHub account
- Semgrep CLI (`pip install semgrep`)
- Syft installed (binary download or `brew install syft`)

---

## Part 1 — SAST with Semgrep (20 minutes)

### Part 1 Objective

Scan a vulnerable Python web application with Semgrep and interpret OWASP Top 10 findings.

### Step 1.1 — Prepare the Vulnerable Application

```bash
mkdir ~/lab07-appsec && cd ~/lab07-appsec
git init && git checkout -b main
mkdir src
```

Create `src/vulnerable_app.py`:

```python
# src/vulnerable_app.py
# Deliberately vulnerable application for security testing

import sqlite3
import subprocess
import yaml
import pickle
import hashlib
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/search")
def search():
    # VULN: Reflected XSS — user input rendered without escaping
    term = request.args.get("q", "")
    return render_template_string(f"<h1>Results for: {term}</h1>")

@app.route("/user")
def get_user():
    # VULN: SQL injection — string concatenation
    uid = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + uid)
    return str(cursor.fetchall())

@app.route("/run")
def run_cmd():
    # VULN: Command injection — shell=True with user input
    cmd = request.args.get("cmd", "")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

@app.route("/load")
def load_data():
    # VULN: Unsafe deserialization
    data = request.get_data()
    obj = pickle.loads(data)
    return str(obj)

@app.route("/config")
def load_config():
    # VULN: Unsafe YAML load
    config_data = request.get_data(as_text=True)
    config = yaml.load(config_data)
    return str(config)

def hash_password(password):
    # VULN: Weak hashing — MD5
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
```

Create `requirements.txt`:

```text
flask==3.0.3
pyyaml==5.3.1
```

### Step 1.2 — Run Semgrep with OWASP Top 10 Rules

```bash
semgrep --config p/owasp-top-ten src/ \
  --text \
  2>&1 | tee semgrep-owasp.txt
```

### Step 1.3 — Run Semgrep with Python-Specific Rules

```bash
semgrep --config p/python src/ \
  --text \
  2>&1 | tee semgrep-python.txt
```

### Step 1.4 — Generate SARIF Output

```bash
semgrep --config p/owasp-top-ten --config p/python \
  --sarif src/ > semgrep.sarif
```

### Step 1.5 — Record Findings

In your lab report, create a table listing every Semgrep finding with rule ID, severity, file, line, and a brief description. You should find at least 5 distinct findings. Map each finding to its corresponding OWASP Top 10 category.

---

## Part 2 — DAST with OWASP ZAP Against Juice Shop (30 minutes)

### Part 2 Objective

Run ZAP baseline scan against OWASP Juice Shop and interpret DAST findings.

### Step 2.1 — Start OWASP Juice Shop

```bash
docker run -d --name juiceshop \
  -p 3000:3000 \
  bkimminich/juice-shop
```

Wait about 30 seconds for Juice Shop to start, then verify:

```bash
curl -s http://localhost:3000 | head -5
```

### Step 2.2 — Run ZAP Baseline Scan

```bash
docker run --rm \
  --network host \
  -v "$(pwd):/zap/wrk:rw" \
  owasp/zap2docker-stable:latest \
  zap-baseline.py \
  -t http://localhost:3000 \
  -r zap-report.html \
  -J zap-report.json \
  -I
```

The `-I` flag ignores the exit code for this baseline run so we can examine results without a CI failure. The scan takes approximately 2–5 minutes.

### Step 2.3 — Examine the HTML Report

Open `zap-report.html` in your browser. Navigate to the Alerts section and record:

- Total number of alerts by risk level (High, Medium, Low, Informational)
- Names of any High-risk alerts
- Names of any Medium-risk alerts

### Step 2.4 — Run ZAP API Scan (Optional Extension)

Juice Shop exposes a REST API. Run the API scan:

```bash
docker run --rm \
  --network host \
  -v "$(pwd):/zap/wrk:rw" \
  owasp/zap2docker-stable:latest \
  zap-api-scan.py \
  -t http://localhost:3000/api/ \
  -f openapi \
  -r zap-api-report.html \
  -J zap-api-report.json \
  -I
```

### Step 2.5 — Stop Juice Shop

```bash
docker stop juiceshop && docker rm juiceshop
```

---

## Part 3 — Dependency Scanning with OWASP Dependency-Check (15 minutes)

### Part 3 Objective

Run Dependency-Check against the requirements file and enforce a CVSS quality gate.

### Step 3.1 — Run Dependency-Check via Docker

```bash
mkdir reports
docker run --rm \
  -v "$(pwd):/src" \
  -v "$(pwd)/reports:/report" \
  owasp/dependency-check:latest \
  --project lab07-app \
  --scan /src/requirements.txt \
  --format HTML \
  --format JSON \
  --out /report \
  --enableRetired \
  2>&1 | tee depcheck-run.txt
```

### Step 3.2 — Review the HTML Report

Open `reports/dependency-check-report.html`. Note:

- How many dependencies were scanned
- How many CVEs were found
- Which libraries have Critical/High findings
- The CVSS scores of the top findings

### Step 3.3 — Test the Quality Gate

Re-run with `--failOnCVSS 7`:

```bash
docker run --rm \
  -v "$(pwd):/src" \
  -v "$(pwd)/reports:/report" \
  owasp/dependency-check:latest \
  --project lab07-app \
  --scan /src/requirements.txt \
  --format JSON \
  --out /report \
  --failOnCVSS 7
echo "Exit code: $?"
```

The exit code should be non-zero (1) because `pyyaml==5.3.1` has a CVSS >= 7.0 finding. Record the exact exit code.

---

## Part 4 — SBOM Generation with Syft (15 minutes)

### Part 4 Objective

Generate a CycloneDX SBOM for the application directory and a container image.

### Step 4.1 — Build the Application Image

Create a minimal `Dockerfile`:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
CMD ["python", "vulnerable_app.py"]
```

```bash
docker build -t lab07-app:latest .
```

### Step 4.2 — Generate SBOM for the Container Image

```bash
syft lab07-app:latest -o cyclonedx-json=sbom-cyclonedx.json
syft lab07-app:latest -o spdx-json=sbom-spdx.json
```

### Step 4.3 — Inspect the SBOM

```bash
# Count components in the SBOM
python3 -c "
import json
with open('sbom-cyclonedx.json') as f:
    sbom = json.load(f)
print(f'SBOM format: {sbom.get(\"bomFormat\", \"unknown\")}')
print(f'Spec version: {sbom.get(\"specVersion\", \"unknown\")}')
print(f'Component count: {len(sbom.get(\"components\", []))}')
"
```

### Step 4.4 — Scan the SBOM with Grype

```bash
grype sbom:sbom-cyclonedx.json --fail-on high
echo "Grype exit code: $?"
```

---

## Part 5 — Complete AppSec Pipeline in GitHub Actions (10 minutes)

### Part 5 Objective

Write the GitHub Actions workflow integrating all four tools as security gates.

Create `.github/workflows/appsec.yml`:

```yaml
name: Application Security Testing Pipeline

on:
  pull_request:
    branches: [main]

permissions:
  contents: read
  security-events: write

jobs:
  semgrep:
    name: SAST — Semgrep
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/owasp-top-ten
            p/python
          generateSarif: "1"
      - uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: semgrep.sarif

  dependency-check:
    name: Dependency Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dependency-check/Dependency-Check_Action@main
        with:
          project: lab07-app
          path: .
          format: SARIF
          out: reports/
          args: --failOnCVSS 7 --enableRetired
      - uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: reports/dependency-check-report.sarif

  sbom:
    name: SBOM Generation
    runs-on: ubuntu-latest
    needs: dependency-check
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t lab07-app:${{ github.sha }} .
      - uses: anchore/sbom-action@v0
        with:
          image: lab07-app:${{ github.sha }}
          format: cyclonedx-json
          output-file: sbom.json
      - uses: actions/upload-artifact@v4
        with:
          name: sbom-${{ github.sha }}
          path: sbom.json
```

---

## Deliverables

Submit the following on Canvas:

1. Semgrep findings table — rule ID, severity, file, line, OWASP category (Part 1, Step 1.5)
2. `zap-report.html` or screenshot of ZAP alerts summary (Part 2, Step 2.3)
3. `reports/dependency-check-report.html` (Part 3, Step 3.2)
4. Screenshot showing exit code from `--failOnCVSS 7` run (Part 3, Step 3.3)
5. SBOM component count output from Python inspection (Part 4, Step 4.3)
6. Completed `.github/workflows/appsec.yml` (Part 5)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Semgrep findings table — 5+ findings with OWASP mapping | 20 |
| ZAP HTML report or screenshot — alert counts recorded | 20 |
| Dependency-Check HTML report submitted | 15 |
| Quality gate exit code screenshot | 10 |
| SBOM component count output | 10 |
| GitHub Actions workflow — syntactically correct, 3 jobs | 25 |
| Total | 100 |

---

## Part 9 — Challenge Exercise

### Challenge 1: Run an Authenticated ZAP Scan

Configure OWASP ZAP to scan the DVWA application using a logged-in session so protected pages are also tested.

1. Start DVWA in Docker: `docker run -p 80:80 vulnerables/web-dvwa`
2. Use the ZAP Automation Framework to configure an authenticated scan. Create a `zap-auth-plan.yaml` file that includes a `scriptBasedAuthentication` or `formBasedAuthentication` job targeting `http://localhost/login.php` with credentials `admin:password`.
3. Run the authenticated scan and compare the alert count to your unauthenticated baseline scan from Part 2. Record how many additional alerts were found when ZAP had access to authenticated endpoints.
4. Identify one authenticated-only finding (e.g., CSRF, IDOR, or session management issue) and document the alert name, risk level, and affected URL in your lab report.

### Challenge 2: Generate a VEX Document for a False-Positive CVE

Produce a Vulnerability Exploitability Exchange (VEX) document that marks a specific CVE in your SBOM as `not_affected`.

1. From the Grype scan output in Part 4, identify one CVE that you can argue is not exploitable in your specific application context (for example, a CVE in a crypto library for a hash function your application does not call).
2. Create a `vex.cdx.json` CycloneDX VEX document with status `not_affected` and justification `component_not_present` or `protected_by_mitigating_control`:

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "version": 1,
  "vulnerabilities": [
    {
      "id": "CVE-YYYY-NNNNN",
      "affects": [{"ref": "pkg:pypi/PACKAGE@VERSION"}],
      "analysis": {
        "state": "not_affected",
        "justification": "component_not_present",
        "detail": "The vulnerable function is not called by this application."
      }
    }
  ]
}
```

1. Run Grype with your VEX document: `grype sbom:sbom.json --vex vex.cdx.json` and verify the CVE is suppressed from the output.
2. Document the CVE, the justification used, and the technical rationale for why it is not exploitable.

### Reflection Questions

1. You ran both SAST (Semgrep) and DAST (ZAP) against the same vulnerable application. Make a table comparing the findings: which vulnerabilities did SAST catch that DAST missed, and vice versa? What does this tell you about why both tool types are required in a complete DevSecOps pipeline?
2. Your SBOM shows 847 transitive dependencies. A new CVE is published for one of them. Describe the end-to-end process your team would follow — from CVE publication to verified fix in production — including which tools trigger alerts, how exploitability is assessed, how the fix is prioritized and deployed, and how the resolution is documented.

---

Lab 07 | CIS-4350 | Texas Wesleyan University | Professor Nash
