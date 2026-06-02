# Video Script: Module 04 - Containerization: Docker Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 04 — Containerization: Docker Security"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. We have covered the DevSecOps culture, Git workflows, and multi-stage CI/CD pipelines. Now we're going to get into one of the most important infrastructure topics in modern DevSecOps: Docker and container security.

Containers are everywhere. If you are working in DevSecOps today, you are almost certainly building, securing, and scanning Docker images. By the end of this video you'll understand the Docker security model, be able to write a secure Dockerfile using production best practices, explain the attack surface of container images, and describe how container image scanning fits into the CI/CD pipeline."

---

### [01:30 - 06:00] The Docker Security Model

**Visual:** Diagram — Docker architecture: host kernel, Docker daemon, containers, namespaces, cgroups

**Audio:**

"Let's start with how Docker security actually works at the kernel level, because this is the foundation for everything else.

Docker containers are not virtual machines. A container shares the host operating system kernel. The isolation between containers — and between containers and the host — is provided by two Linux kernel features: namespaces and control groups (cgroups).

Namespaces isolate what a container can see: its own process tree (PID namespace), its own network interfaces (network namespace), its own filesystem view (mount namespace), and its own hostname (UTS namespace). From inside the container, it looks like a standalone system. But the kernel calls are all going to the same shared kernel.

Control groups limit what a container can use: CPU, memory, I/O. They prevent a runaway container from starving other containers or the host of resources.

This architecture has a critical security implication: a vulnerability in the Linux kernel could potentially be exploited from inside a container to escape to the host. This is called a container breakout. Container breakouts are rare but documented — CVE-2019-5736 (runc vulnerability) and CVE-2022-0492 (cgroups escape) are historical examples.

The Docker daemon itself runs as root by default. A compromised Docker daemon has root access to the host. This is why the exam tests Docker daemon access control and rootless Docker as a hardening measure.

Understanding this kernel-shared architecture tells us why container image hardening matters: a smaller, more minimal image reduces the attack surface available to exploit inside the container."

---

### [06:00 - 12:00] Secure Dockerfile Best Practices

**Visual:** Side-by-side comparison — insecure Dockerfile vs. secure Dockerfile

**Audio:**

"Now let's look at how to write a production-secure Dockerfile. This is directly tested on the DevSecOps Professional exam and required in this module's lab.

**[SHOW CODE]**

Here is an insecure Dockerfile — the kind you should never use in production:

```dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
```

Let me count the problems: `ubuntu:latest` is a mutable, massive base image with hundreds of packages that are potential attack surface. Running as root (no `USER` directive). Copying the entire repository into the image (potentially including test files, .env files, Git history). Using `latest` means the build is not reproducible.

Now here is the same application with a secure Dockerfile:

```dockerfile
# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /build

# Copy only dependency manifest first (layer caching optimization)
COPY requirements.txt .

# Install dependencies into a prefix directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Production image
FROM python:3.11-slim

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup -s /sbin/nologin appuser

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy only the application source code, not tests or dev files
COPY src/ ./src/

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose only the required port
EXPOSE 8080

# Use exec form (not shell form) to handle signals correctly
CMD ["python3", "-m", "src.main"]
```

Let me walk through every security decision here.

Multi-stage build: the `builder` stage installs dependencies using pip. The final `python:3.11-slim` stage copies only the installed packages and application code — not the build tools, not pip, not any build artifacts. This dramatically reduces image size and attack surface.

`python:3.11-slim`: a minimal base image. Not `ubuntu:latest` with 500 packages. Not `:latest` — a pinned version so the build is reproducible and we know exactly what base image CVEs we're dealing with.

Non-root user: `groupadd` creates a system group, `useradd` creates a system user with no login shell. `USER appuser` switches to that user before the CMD runs. If the container is compromised, the attacker runs as `appuser` — no root, no sudo, no ability to write to system directories.

`COPY src/ ./src/` — we copy only the application source, not the entire repository. This prevents test files, configuration templates, or accidentally included secrets from ending up in the image.

`CMD ["python3", "-m", "src.main"]` — exec form, not shell form. Exec form passes signals directly to the process, enabling clean shutdown. Shell form wraps the command in `/bin/sh -c`, creating an extra process and potentially exposing shell injection vectors."

---

### [12:00 - 17:00] Container Image Attack Surface and Scanning

**Visual:** Trivy scan output showing CVEs in a container image

**Audio:**

"Even a perfectly written Dockerfile can result in a vulnerable image if the base image itself contains packages with known CVEs. This is where container image scanning comes in.

Container image scanning tools analyze every layer of a Docker image against vulnerability databases, identifying OS packages, system libraries, and language runtime dependencies that have known CVEs.

The two tools you need to know for the exam are Trivy and Grype.

**[SHOW CODE]**

Trivy is an open-source scanner from Aqua Security. Install and run it locally:

```bash
# Install Trivy
brew install aquasecurity/trivy/trivy

# Scan a local image
trivy image myapp:latest

# Scan and fail if any CRITICAL or HIGH CVEs are found
trivy image --exit-code 1 --severity CRITICAL,HIGH myapp:latest

# Output results in JSON format for pipeline integration
trivy image --format json --output trivy-results.json myapp:latest
```

The `--exit-code 1` flag is critical for pipeline integration: when Trivy finds a vulnerability at or above the specified severity threshold, it exits with code 1, causing the pipeline step to fail and blocking the image from being pushed.

Here is how to integrate Trivy into a GitHub Actions pipeline:

```yaml
- name: Scan container image with Trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: myapp:latest
    format: sarif
    output: trivy-results.sarif
    severity: CRITICAL,HIGH
    exit-code: '1'

- name: Upload Trivy results to GitHub Security
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: trivy-results.sarif
```

Uploading results in SARIF format to GitHub Security displays the findings directly in the repository's Security tab, integrated with the code review workflow.

Grype, from Anchore, is the other major open-source scanner. Its syntax is similar:

```bash
# Install Grype
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin

# Scan image
grype myapp:latest

# Fail on CRITICAL findings
grype myapp:latest --fail-on critical
```

For the exam: know that both Trivy and Grype scan base image layers and application dependencies. Know that `--exit-code 1` / `--fail-on` flags are what make scanners into pipeline security gates rather than informational reports."

---

### [17:00 - 20:30] Container Security in the CI/CD Pipeline

**Visual:** CI/CD pipeline diagram with container build and scan steps highlighted

**Audio:**

"Let's place container security controls in the context of the full CI/CD pipeline we discussed in Module 03.

The container-related security steps occur in this order within the pipeline:

First, during the build stage, the Dockerfile itself is scanned for security misconfigurations — tools like Hadolint analyze Dockerfile syntax against security rules: running as root, using `latest` tags, adding unnecessary capabilities.

Second, after the Docker image is built, it is scanned with Trivy or Grype before being pushed to any registry. If the scan finds critical CVEs, the push is blocked.

Third, the approved image is pushed to a private container registry — Docker Hub private, Amazon ECR, Google Artifact Registry, or a self-hosted Harbor instance.

Fourth, in production, the running container should have read-only filesystem (`--read-only`), dropped capabilities (`--cap-drop ALL`), no new privileges (`--security-opt no-new-privileges`), and memory and CPU limits to prevent resource exhaustion attacks.

**[SHOW CODE]**

Dockerfile linting with Hadolint in a GitHub Actions pipeline:

```yaml
- name: Lint Dockerfile with Hadolint
  uses: hadolint/hadolint-action@v3.1.0
  with:
    dockerfile: Dockerfile
    failure-threshold: warning
```

The exam tests the order: lint Dockerfile, build image, scan image, push to registry. Never push an unscanned image."

---

### [20:30 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know the Docker security model — namespace and cgroup isolation, kernel sharing, and why this differs from VM isolation. Know the six secure Dockerfile practices: minimal base image, non-root user, multi-stage build, pinned versions, selective COPY, exec form CMD. Know Trivy and Grype as the primary container scanning tools and that `--exit-code 1` makes them pipeline gates. Know Hadolint for Dockerfile linting.

Complete the lab, which requires writing a secure multi-stage Dockerfile. See you in Module 05."
