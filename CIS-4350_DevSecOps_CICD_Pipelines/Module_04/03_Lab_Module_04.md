# Lab Activity: Module 04 - Containerization: Docker Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Write a secure Dockerfile following all six production best practices from Module 04.
- Identify and remediate security flaws in an existing insecure Dockerfile.
- Run a container image scan with Trivy and interpret the results.
- Integrate Dockerfile linting and image scanning into a GitHub Actions pipeline.

---

## Prerequisites

Before beginning this lab, confirm the following:

- Docker Desktop is installed and running locally (`docker --version` returns a result).
- You have completed the Module 04 video and reading guide.
- You have the lab repository from Module 02/03 available on GitHub.
- Trivy is installed locally OR you will use the GitHub Actions integration for Part 2.

To install Trivy on macOS:

```bash
brew install aquasecurity/trivy/trivy
```

To install Trivy on Linux:

```bash
sudo apt-get install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update && sudo apt-get install trivy
```

---

## Part 1: Write a Secure Dockerfile (35 points)

### Part 1 Background

This part requires you to write a production-ready Dockerfile for a Python Flask application following all six secure Dockerfile best practices from the Module 04 reading guide. This is the required Dockerfile specification from the course lab requirements.

### Part 1 Application Context

You are containerizing a Python Flask web application. The source code lives in a `src/` directory. The entry point is `src/app.py`. The application listens on port 8080.

### Part 1 Instructions

**Step 1: Write the complete secure Dockerfile.**

Create a file named `Dockerfile` in your lab repository root. The Dockerfile must satisfy all requirements below:

Requirements:

- Uses a two-stage multi-stage build.
- Stage 1 (named `builder`): Uses `python:3.11-slim` as the base, copies `requirements.txt`, installs dependencies with `pip install --no-cache-dir`.
- Stage 2 (production): Uses `python:3.11-slim` as the base (minimal, not `ubuntu:latest`).
- Creates a non-root system group and user (`appgroup`, `appuser`) in Stage 2.
- Copies installed packages from Stage 1 into Stage 2 using `COPY --from=builder`.
- Copies only the `src/` directory into the image — not the entire repository.
- Sets `WORKDIR` to `/app`.
- Changes ownership of `/app` to the non-root user.
- Switches to the non-root user with `USER appuser` before the CMD instruction.
- Uses exec form (not shell form) for CMD.
- Exposes only port 8080.

The completed Dockerfile must follow this structure:

```dockerfile
# Stage 1: Dependency installation
FROM python:3.11-slim AS builder
# ... complete this stage

# Stage 2: Production image
FROM python:3.11-slim
# ... complete this stage — must include non-root user, selective COPY, USER directive
```

**Step 2: Build the image and verify it runs as non-root.**

```bash
docker build -t secure-flask-app:lab04 .

# Verify the running user is not root
docker run --rm secure-flask-app:lab04 whoami
```

The `whoami` output must show `appuser`, not `root`.

**Step 3: Inspect the image layers.**

```bash
docker history secure-flask-app:lab04
```

Review the layer history and confirm that no secrets or .env files appear in the build steps. Record the output.

### Part 1 Deliverable

Submit: your complete `Dockerfile`, the output of `docker build`, the output of `docker run ... whoami`, and the output of `docker history`.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Multi-stage build with correctly named builder stage | 6 |
| Production stage uses python:3.11-slim (not ubuntu:latest or :latest tag) | 4 |
| Non-root user created and USER directive applied before CMD | 8 |
| Only src/ directory copied (not entire repository) | 4 |
| Exec form CMD used correctly | 4 |
| whoami output confirms non-root execution | 5 |
| docker history shows no secrets in layer steps | 4 |

---

## Part 2: Insecure Dockerfile Analysis and Remediation (25 points)

### Part 2 Background

Analyzing vulnerable Dockerfiles and writing remediated versions is a tested skill on the DevSecOps Professional exam.

### Part 2 Insecure Dockerfile

Review the following Dockerfile:

```dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    git \
    vim \
    build-essential

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENV DB_PASSWORD=mypassword123
ENV API_KEY=sk-prod-1234567890abcdef

EXPOSE 22
EXPOSE 8080
EXPOSE 3306

CMD python3 app.py
```

### Part 2 Instructions

**Step 1: Identify all security problems.**

List every security flaw in the Dockerfile above. For each flaw, state the specific line or instruction, the security problem it creates, and which best practice from Module 04 it violates. You must identify at least six distinct flaws.

**Step 2: Write the remediated Dockerfile.**

Rewrite the complete Dockerfile with all identified flaws corrected. Apply all six secure Dockerfile best practices from the reading guide.

**Step 3: Explain the layer secret problem.**

The original Dockerfile sets `ENV DB_PASSWORD=mypassword123`. In 3-4 sentences, explain why removing this ENV line in a new Dockerfile revision still does not protect the password if the original image was ever built and the layers are available. Describe the technically correct way to handle runtime secrets.

### Part 2 Deliverable

Submit: your list of security flaws with analysis, your remediated Dockerfile, and your layer secret explanation.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| At least 6 security flaws identified with accurate analysis | 12 |
| Remediated Dockerfile applies all six best practices | 9 |
| Layer secret explanation is technically accurate | 4 |

---

## Part 3: Container Image Scanning with Trivy (25 points)

### Part 3 Background

Container image scanning detects CVEs in base image packages and runtime dependencies before the image is deployed to production.

### Part 3 Instructions

**Step 1: Scan the insecure base image.**

Run Trivy against the `ubuntu:latest` base image to see its CVE exposure:

```bash
trivy image ubuntu:latest --severity CRITICAL,HIGH
```

Record the total number of CRITICAL and HIGH CVEs found.

**Step 2: Scan your secure image from Part 1.**

```bash
trivy image secure-flask-app:lab04 --severity CRITICAL,HIGH
```

Record the total number of CRITICAL and HIGH CVEs found. Compare it to the ubuntu:latest result.

**Step 3: Test the pipeline gate behavior.**

Run Trivy with the exit-code flag:

```bash
trivy image --exit-code 1 --severity CRITICAL,HIGH secure-flask-app:lab04
echo "Exit code: $?"
```

Record the exit code. Explain what this exit code means for a CI/CD pipeline job.

**Step 4: Add Trivy to your GitHub Actions pipeline.**

Add a Trivy scanning step to your `full-pipeline.yml` from Module 03 within the `security-scan` job:

```yaml
- name: Build Docker image
  run: docker build -t myapp:${{ github.sha }} .

- name: Scan image with Trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: myapp:${{ github.sha }}
    format: sarif
    output: trivy-results.sarif
    severity: CRITICAL,HIGH
    exit-code: '1'

- name: Upload scan results to GitHub Security
  uses: github/codeql-action/upload-sarif@v3
  if: always()
  with:
    sarif_file: trivy-results.sarif
```

Push this change and provide a screenshot of the Trivy step in the Actions log.

### Part 3 Deliverable

Submit: Trivy output for `ubuntu:latest`, Trivy output for your secure image, exit code analysis, updated pipeline YAML with Trivy step, and a screenshot from the GitHub Actions log.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| Both Trivy scans completed and output recorded | 8 |
| CVE count comparison between ubuntu:latest and slim image is documented | 5 |
| Exit code interpretation is technically accurate | 4 |
| Pipeline YAML correctly integrates Trivy with exit-code and SARIF upload | 8 |

---

## Part 4: Dockerfile Security Concepts (15 points)

### Part 4 Instructions

Answer each of the following questions in 2-4 sentences. Use precise technical terminology.

**Question A:** Explain why exec form CMD (`CMD ["python", "app.py"]`) is preferred over shell form CMD (`CMD python app.py`) from a security perspective. What specific risk does shell form introduce?

**Question B:** A developer argues that their application must run as root inside the container because it needs to bind to port 80. Explain the security risk of running as root and provide an alternative approach that allows binding to a privileged port without running the application as root.

**Question C:** Explain the difference between a `python:3.11-slim` base image and a `python:3.11` (full Debian) base image from an attack surface perspective. How does this relate to the shift-left security principle?

### Part 4 Deliverable

Submit written answers to all three questions. Label each answer with the corresponding question letter.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Question A answer is technically accurate (exec vs. shell form risks) | 5 |
| Question B answer identifies root risk and proposes a valid alternative | 5 |
| Question C answer correctly relates base image size to attack surface | 5 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (04) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
