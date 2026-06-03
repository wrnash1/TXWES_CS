# Lab 08 — Supply Chain Security: SCA, SBOM, Code Signing, and SLSA

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will run Snyk SCA scanning with license and vulnerability checks, generate both CycloneDX and SPDX SBOMs, simulate a dependency confusion attack in a safe sandbox, sign a container image with cosign using keyless signing, and generate a SLSA provenance attestation in GitHub Actions.

**Estimated Time:** 90–120 minutes

**Difficulty:** Intermediate–Advanced

---

## Prerequisites

- Docker Desktop running
- Python 3.8+ installed
- Snyk CLI (`npm install -g snyk` or binary download; free account at snyk.io)
- Syft installed (binary download or `brew install syft`)
- cosign installed (`brew install cosign` or binary download)
- GitHub account with Actions enabled
- Git configured from Lab 02

---

## Part 1 — SCA with Snyk (25 minutes)

### Part 1 Objective

Run Snyk SCA including vulnerability and license scanning against a Python application.

### Step 1.1 — Prepare the Project

```bash
mkdir ~/lab08-supply-chain && cd ~/lab08-supply-chain
git init && git checkout -b main
```

Create `requirements.txt` with mixed dependencies:

```text
flask==2.0.1
requests==2.18.0
pyyaml==5.3.1
cryptography==3.4.8
pillow==9.0.0
django==3.2.0
```

Create a minimal `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Lab 08 Supply Chain Demo"
```

### Step 1.2 — Authenticate Snyk

```bash
snyk auth
# Follow the browser authentication flow
```

### Step 1.3 — Run Snyk Vulnerability Scan

```bash
snyk test \
  --file=requirements.txt \
  --package-manager=pip \
  --severity-threshold=high \
  --json > snyk-vuln-results.json

# Human-readable output
snyk test \
  --file=requirements.txt \
  --package-manager=pip \
  --severity-threshold=medium \
  2>&1 | tee snyk-vuln-report.txt
```

### Step 1.4 — Run Snyk License Check

```bash
snyk test \
  --file=requirements.txt \
  --package-manager=pip \
  --all-projects \
  2>&1 | tee snyk-license-report.txt
```

Review the license report and note:

- Which packages have permissive licenses (MIT, BSD, Apache-2.0)?
- Are there any copyleft licenses (GPL, LGPL)?

### Step 1.5 — Record SCA Findings

In your lab report, create a table:

| Package | Version | CVEs Found | Highest CVSS | License |
|---|---|---|---|---|
| flask | 2.0.1 | | | |
| requests | 2.18.0 | | | |
| pyyaml | 5.3.1 | | | |
| cryptography | 3.4.8 | | | |
| pillow | 9.0.0 | | | |
| django | 3.2.0 | | | |

---

## Part 2 — SBOM Generation (20 minutes)

### Part 2 Objective

Generate CycloneDX and SPDX SBOMs and inspect their contents.

### Step 2.1 — Create a Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]
```

### Step 2.2 — Build the Image

```bash
docker build -t lab08-app:latest .
```

### Step 2.3 — Generate CycloneDX SBOM

```bash
syft lab08-app:latest \
  --source-name lab08-app \
  --source-version 1.0.0 \
  -o cyclonedx-json=sbom-cyclonedx.json

# Inspect component count
python3 -c "
import json
with open('sbom-cyclonedx.json') as f:
    sbom = json.load(f)
components = sbom.get('components', [])
print(f'CycloneDX version: {sbom[\"specVersion\"]}')
print(f'Total components: {len(components)}')
libs = [c for c in components if c.get('type') == 'library']
print(f'Library components: {len(libs)}')
"
```

### Step 2.4 — Generate SPDX SBOM

```bash
syft lab08-app:latest \
  --source-name lab08-app \
  -o spdx-json=sbom-spdx.json

python3 -c "
import json
with open('sbom-spdx.json') as f:
    sbom = json.load(f)
packages = sbom.get('packages', [])
print(f'SPDX version: {sbom.get(\"spdxVersion\")}')
print(f'Total packages: {len(packages)}')
"
```

### Step 2.5 — Scan SBOM with Grype

```bash
grype sbom:sbom-cyclonedx.json \
  --fail-on high \
  --output table \
  2>&1 | tee grype-results.txt

echo "Grype exit code: $?"
```

---

## Part 3 — Dependency Confusion Simulation (15 minutes)

### Part 3 Objective

Understand the dependency confusion attack by simulating it safely with a local registry.

### Step 3.1 — Understand the Attack Scenario

In this simulation you will:

1. Create a "private" package in a local directory
2. Create a "public" (malicious) package with the same name but higher version
3. Observe how pip resolves the conflict

### Step 3.2 — Create a Mock Private Package

```bash
mkdir -p private_packages/company-utils/src
cat > private_packages/company-utils/setup.py << 'EOF'
from setuptools import setup
setup(
    name="company-utils",
    version="1.0.0",
    description="Safe internal package - version 1.0.0"
)
EOF
```

### Step 3.3 — Create a Mock "Malicious" Public Package

```bash
mkdir -p public_packages/company-utils/src
cat > public_packages/company-utils/setup.py << 'EOF'
from setuptools import setup
setup(
    name="company-utils",
    version="9.9.9",
    description="SIMULATED MALICIOUS PACKAGE - version 9.9.9"
)
EOF
```

### Step 3.4 — Simulate Resolution

```bash
# Install from "private" registry first
pip install private_packages/company-utils/ \
  --no-index --find-links private_packages/ \
  --quiet

python3 -c "import company_utils; print(f'Installed version: checking...')" 2>/dev/null || \
  pip show company-utils | grep Version

# Now simulate what happens when public "malicious" package exists
pip install public_packages/company-utils/ \
  --no-index --find-links public_packages/ \
  --quiet

pip show company-utils | grep Version
```

The second install overwrites with the higher version — this is the confusion attack.

### Step 3.5 — Document Prevention

In your lab report, describe the three most important controls that would prevent this in a production environment, citing specific configurations from the reading guide.

---

## Part 4 — Container Image Signing with cosign (20 minutes)

### Part 4 Objective

Sign a container image using cosign with key-based signing and verify the signature.

### Step 4.1 — Generate a cosign Key Pair

```bash
cosign generate-key-pair
# Creates cosign.key (private) and cosign.pub (public)
# Set a passphrase when prompted
```

### Step 4.2 — Push Image to a Registry

For this lab, use Docker Hub (create a free account if needed) or GitHub Container Registry:

```bash
# Tag for GHCR
docker tag lab08-app:latest ghcr.io/YOUR_USERNAME/lab08-app:v1.0.0
docker push ghcr.io/YOUR_USERNAME/lab08-app:v1.0.0
```

### Step 4.3 — Sign the Image

```bash
cosign sign --key cosign.key \
  ghcr.io/YOUR_USERNAME/lab08-app:v1.0.0
```

Enter your key passphrase when prompted. The signature is stored alongside the image in the registry.

### Step 4.4 — Verify the Signature

```bash
cosign verify \
  --key cosign.pub \
  ghcr.io/YOUR_USERNAME/lab08-app:v1.0.0 \
  | python3 -m json.tool
```

The output will show the verified signature payload. Take a screenshot.

### Step 4.5 — Attempt to Verify Tampered Image

```bash
# Pull and retag to simulate tampering
docker pull nginx:alpine
docker tag nginx:alpine ghcr.io/YOUR_USERNAME/lab08-app:v1.0.0-tampered
docker push ghcr.io/YOUR_USERNAME/lab08-app:v1.0.0-tampered

# Attempt to verify with original signature (should fail)
cosign verify \
  --key cosign.pub \
  ghcr.io/YOUR_USERNAME/lab08-app:v1.0.0-tampered \
  2>&1 || echo "Verification FAILED — image was tampered with"
```

---

## Deliverables

Submit the following on Canvas:

1. Snyk SCA findings table with CVEs and licenses per package (Part 1, Step 1.5)
2. CycloneDX SBOM component count output (Part 2, Step 2.3)
3. SPDX SBOM package count output (Part 2, Step 2.4)
4. `grype-results.txt` (Part 2, Step 2.5)
5. Written dependency confusion prevention plan — 3 controls with configurations (Part 3, Step 3.5)
6. Screenshot of cosign verify output showing successful signature verification (Part 4, Step 4.4)
7. Screenshot of cosign verify failure on tampered image (Part 4, Step 4.5)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Snyk findings table — accurate CVE and license data | 20 |
| Both SBOM component counts recorded | 10 |
| Grype results file submitted | 10 |
| Dependency confusion prevention plan — 3 controls | 20 |
| cosign verify success screenshot | 20 |
| cosign verify failure screenshot | 20 |
| Total | 100 |

---

Lab 08 | CIS-4350 | Texas Wesleyan University | Professor Nash
