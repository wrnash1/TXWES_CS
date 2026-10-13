# Lab 04 — Container Security: Hardening Dockerfiles and Scanning Images

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will harden an insecure Dockerfile using multi-stage builds and non-root users, scan container images with Trivy to identify and compare vulnerabilities between insecure and hardened images, add a container scanning gate to your GitHub Actions pipeline from Lab 03, and practice signing container images with cosign.

**Estimated Time:** 90–120 minutes

**Difficulty:** Intermediate

---

## Prerequisites

- Docker Desktop installed and running
- GitHub account with the Lab 03 repository
- Trivy installed or available via Docker
- cosign installed (`brew install cosign` on macOS; binary download on Windows/Linux)
- Git configured from Lab 02

---

## Part 1 — Build and Scan an Insecure Image (20 minutes)

### Part 1 Objective

Establish a baseline vulnerability count for an insecure image, then compare it to a hardened image.

### Step 1.1 — Create the Insecure Dockerfile

```bash
mkdir ~/lab04-container && cd ~/lab04-container
git init && git checkout -b main
```

Create `Dockerfile.insecure`:

```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip curl wget
COPY . /app
WORKDIR /app
RUN pip3 install flask==2.0.1 requests==2.18.0
EXPOSE 80
CMD python3 app.py
```

Create a minimal `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from insecure container"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```

### Step 1.2 — Build the Insecure Image

```bash
docker build -f Dockerfile.insecure -t myapp:insecure .
```

### Step 1.3 — Scan the Insecure Image with Trivy

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image \
  --severity HIGH,CRITICAL \
  --format table \
  myapp:insecure 2>&1 | tee trivy-insecure.txt
```

Record the total number of HIGH and CRITICAL findings.

---

## Part 2 — Build a Hardened Image (30 minutes)

### Part 2 Objective

Create a production-hardened Dockerfile and demonstrate the reduction in vulnerabilities.

### Step 2.1 — Create the Hardened Dockerfile

Create `Dockerfile`:

```dockerfile
# Stage 1: Dependency builder
FROM python:3.12-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Production runtime
FROM python:3.12-slim AS runtime

LABEL org.opencontainers.image.description="Lab 04 hardened image"

# Create non-root user
RUN groupadd -r appuser --gid=1001 \
    && useradd -r --uid=1001 -g appuser appuser

WORKDIR /app

# Copy only installed dependencies from builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Copy only application source — not test files, not .env
COPY --chown=appuser:appuser app.py .

# Switch to non-root user before runtime
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/')"

CMD ["python3", "app.py"]
```

Create `requirements.txt` with current safe versions:

```text
flask==3.0.3
```

Update `app.py` for the hardened image:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from hardened container"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
```

Create `.dockerignore`:

```gitignore
.env
.env.*
.git/
tests/
*.md
__pycache__/
Dockerfile.insecure
trivy-*.txt
```

### Step 2.2 — Build the Hardened Image

```bash
docker build -t myapp:hardened .
```

### Step 2.3 — Verify Non-Root User

```bash
# Confirm the container runs as non-root
docker run --rm myapp:hardened id
```

Expected output: `uid=1001(appuser) gid=1001(appuser) groups=1001(appuser)`

### Step 2.4 — Scan the Hardened Image

```bash
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image \
  --severity HIGH,CRITICAL \
  --format table \
  myapp:hardened 2>&1 | tee trivy-hardened.txt
```

### Step 2.5 — Compare Results

Create a comparison table in your lab report:

| Metric | Insecure Image | Hardened Image |
|---|---|---|
| Base image | ubuntu:20.04 | python:3.12-slim |
| HIGH findings | (your count) | (your count) |
| CRITICAL findings | (your count) | (your count) |
| Runs as root | Yes | No |
| Build tools in image | Yes | No (multi-stage) |

---

## Part 3 — Runtime Security Controls (20 minutes)

### Part 3 Objective

Apply Docker runtime security flags and observe their effect on container behavior.

### Step 3.1 — Run with Minimal Privileges

```bash
docker run --rm \
  --user 1001:1001 \
  --read-only \
  --tmpfs /tmp:noexec,nosuid \
  --cap-drop ALL \
  --no-new-privileges \
  --memory 256m \
  --cpus 0.5 \
  -p 127.0.0.1:8080:8080 \
  myapp:hardened
```

In a second terminal, confirm the app is accessible:

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
```

### Step 3.2 — Test Read-Only Filesystem

With the container running from Step 3.1, attempt to write to the filesystem:

```bash
# Get the container ID
CONTAINER_ID=$(docker ps --filter "ancestor=myapp:hardened" -q)

# Attempt to write to root filesystem (should fail)
docker exec $CONTAINER_ID touch /test-file
```

Expected: `touch: cannot touch '/test-file': Read-only file system`

### Step 3.3 — Confirm Temp Write Works

```bash
docker exec $CONTAINER_ID touch /tmp/test-file
docker exec $CONTAINER_ID ls /tmp/
```

Writing to `/tmp` should succeed because of the `--tmpfs /tmp` mount.

---

## Part 4 — Add Container Scanning to the CI Pipeline (20 minutes)

### Part 4 Objective

Integrate Trivy scanning into the GitHub Actions pipeline from Lab 03.

### Step 4.1 — Update the Pipeline File

Open `.github/workflows/secure-ci.yml` from Lab 03 and add the following job after the existing `dependency-scan` job:

```yaml
  container-scan:
    name: Container Image Scan — Trivy
    runs-on: ubuntu-latest
    needs: unit-tests
    permissions:
      contents: read
      security-events: write
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build container image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Scan image with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: sarif
          output: trivy-results.sarif
          severity: HIGH,CRITICAL
          exit-code: "1"

      - name: Upload Trivy SARIF results
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: trivy-results.sarif
```

Also update the `security-summary` job's `needs` array:

```yaml
  security-summary:
    needs: [secrets-scan, sast-semgrep, dependency-scan, container-scan]
```

### Step 4.2 — Commit the Hardened Dockerfile and Pipeline

```bash
git add Dockerfile requirements.txt app.py .dockerignore .github/
git commit -m "Add hardened Dockerfile and container scan to CI pipeline"
git push origin main
```

### Step 4.3 — Observe the Container Scan Job

Navigate to the Actions tab and observe the `Container Image Scan — Trivy` job. With the hardened image and updated dependencies, the scan should pass.

---

## Deliverables

Submit the following on Canvas:

1. `trivy-insecure.txt` and `trivy-hardened.txt` scan output files (Part 1 and Part 2)
2. Completed comparison table showing finding counts for both images (Part 2, Step 2.5)
3. Screenshot showing `id` output proving non-root execution (Part 2, Step 2.3)
4. Screenshot showing read-only filesystem rejection and successful `/tmp` write (Part 3)
5. Completed `Dockerfile` (hardened, multi-stage, non-root)
6. Screenshot of green CI pipeline including the `container-scan` job (Part 4)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Both Trivy scan files submitted and showing meaningful difference | 20 |
| Comparison table — accurate counts | 10 |
| Non-root ID screenshot | 10 |
| Read-only filesystem + tmpfs screenshots | 15 |
| Hardened Dockerfile — multi-stage, non-root, no floating tags | 25 |
| Green CI pipeline with container scan job | 20 |
| Total | 100 |

---

## Part 9 — Challenge Exercise

### Challenge 1: Generate and Attest a Container SBOM

Produce a signed Software Bill of Materials for your hardened image using Syft and cosign, then verify the attestation.

1. Install Syft: `curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin`
2. Generate an SBOM in CycloneDX JSON format: `syft app:latest -o cyclonedx-json > sbom.cdx.json`
3. Install cosign and perform a keyless attestation of the SBOM against the image pushed to a registry (GitHub Container Registry or Docker Hub):

```bash
cosign attest --predicate sbom.cdx.json \
  --type cyclonedx \
  ghcr.io/YOUR_USERNAME/lab04-app:latest
```

1. Verify the attestation: `cosign verify-attestation --type cyclonedx ghcr.io/YOUR_USERNAME/lab04-app:latest`
2. Add a CI pipeline step that fails if the image in the registry does not have a valid cosign attestation before it is deployed.

### Challenge 2: Scan a Running Container with Falco

Use Falco to detect a suspicious command executed inside a running container.

1. Run Falco in a Docker container alongside your application container using the Docker socket:

```bash
docker run --rm -it \
  --privileged \
  -v /var/run/docker.sock:/host/var/run/docker.sock \
  -v /dev:/host/dev \
  -v /proc:/host/proc:ro \
  falcosecurity/falco:latest
```

1. In a separate terminal, exec into your running application container and run a command that Falco's default rules consider suspicious (e.g., `cat /etc/shadow` or `apt-get`): `docker exec -it <container_id> cat /etc/shadow`
2. Observe Falco's alert output in the first terminal. Record the rule name, priority, and output fields.
3. Write a custom Falco rule in a `falco_rules.local.yaml` file that generates a CRITICAL alert when any process named `wget` or `curl` runs inside a container whose image name starts with `lab04-app`.

### Reflection Questions

1. Your hardened image uses `gcr.io/distroless/python3` as the runtime base. A security engineer flags that distroless images make it impossible to exec into a running container for incident investigation. How would you design a production debugging workflow that maintains security hardening while still allowing authorized engineers to investigate live containers?
2. You generated an SBOM and cosign attestation for image `app:v1.2.3`. Three months later, a new CVE is disclosed that affects a library in that image. The attestation is still valid. Explain why a valid cosign attestation does not mean the image is currently secure, and describe the ongoing scanning process required after attestation.

---

Lab 04 | CIS-4350 | Texas Wesleyan University | Professor Nash
