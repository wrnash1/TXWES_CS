# Video Script: Module 04 — Container Security with Docker

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–1:30)

[SLIDE: Module 04 title card]

Welcome to Module 04. Containers have fundamentally changed how applications are built and deployed. Docker is the dominant container runtime, and understanding its security model is essential for any DevSecOps practitioner. In this module we'll work through Docker architecture, secure Dockerfile practices, image scanning with Trivy and Snyk, running containers as non-root users, read-only filesystems, Docker Content Trust for image signing, and container registry security.

By the end of this module you'll be able to write security-hardened Dockerfiles, scan images for vulnerabilities before pushing them to a registry, configure containers to run with minimal privilege, and integrate container scanning into your CI pipeline from Module 03.

---

### SEGMENT 2 — Docker Architecture and the Threat Model (1:30–5:00)

[SLIDE: Docker architecture diagram — daemon, client, registry, containers]

Docker uses a client-server architecture. The Docker client sends commands to the Docker daemon, which manages images, containers, networks, and volumes. Images are pulled from and pushed to registries.

The Docker threat model has five attack surfaces.

The host OS is the first surface. The Docker daemon runs as root on the host. If an attacker can escape the container namespace — a container escape — they have root on the host.

The Docker daemon itself is the second surface. The daemon socket at `/var/run/docker.sock` is effectively root access to the host. Never mount the Docker socket into a container.

The container image is the third surface. Images built from base images containing known CVEs in OS packages or application libraries can be exploited after deployment.

The container runtime is the fourth surface. Running containers as root inside the container, without read-only filesystem, with elevated Linux capabilities, or with access to the host network namespace all expand the attack surface.

The registry is the fifth surface. If an attacker can push a malicious image to your registry or perform a man-in-the-middle attack to substitute an image, they control your application.

Each of these surfaces has specific controls. Let's work through them.

---

### SEGMENT 3 — Dockerfile Security Best Practices (5:00–9:00)

[SLIDE: Insecure Dockerfile vs. Secure Dockerfile side by side]

The Dockerfile is the blueprint for your container image. Security decisions made here affect every container deployed from the image. Let's compare a typical insecure Dockerfile to a hardened one.

Here is an insecure Dockerfile:

```dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python3", "app.py"]
```

The problems with this Dockerfile:

First, `ubuntu:latest` is a floating tag. The exact image you get today differs from what you get in six months. And Ubuntu is a large general-purpose OS — most of its packages are irrelevant to your application, adding attack surface.

Second, the application runs as root. If someone exploits a vulnerability in your application, they have root inside the container.

Third, the entire build context is copied with `COPY . /app`, which may include `.env` files, test data, or other sensitive artifacts.

Here is the hardened version:

```dockerfile
# Stage 1: Build
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim AS runtime
WORKDIR /app

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy only installed packages from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appuser src/ .

# Switch to non-root user
USER appuser

EXPOSE 8080

# Use exec form to ensure signals are handled correctly
CMD ["/home/appuser/.local/bin/python", "app.py"]
```

Key improvements: multi-stage build (build tools not in production image), non-root user, explicit version pinning (`python:3.12-slim`), minimal copy with `--chown`, and exec form CMD.

---

### SEGMENT 4 — Multi-Stage Builds and Minimal Base Images (9:00–11:30)

[SLIDE: Multi-stage build diagram showing layers dropped between stages]

Multi-stage builds are one of the most powerful Docker security techniques. The build stage installs compilers, development libraries, and build tools. The final runtime stage copies only the compiled artifacts — no build tools, no source code, no package managers in the final image.

For Python applications, distroless images from Google represent the most minimal option. They contain only the runtime and its dependencies — no shell, no package manager, no unnecessary OS utilities:

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t /app/packages

FROM gcr.io/distroless/python3-debian12
WORKDIR /app
COPY --from=builder /app/packages /app/packages
COPY src/ .
ENV PYTHONPATH=/app/packages
CMD ["app.py"]
```

The distroless image has no shell (`/bin/sh`) and no package manager. An attacker who exploits your application cannot easily install tools or run interactive commands. This dramatically limits post-exploitation capability.

For organizations not ready for distroless, `python:3.12-slim` is a reasonable intermediate choice — it's a Debian slim image containing only what Python needs, reducing the package surface significantly compared to `ubuntu:latest`.

---

### SEGMENT 5 — Image Scanning with Trivy (11:30–14:30)

[SLIDE: Trivy scan output]

Trivy, developed by Aqua Security, is the leading open-source container image scanner. It checks OS packages, language libraries (Python packages, Node modules, Ruby gems, etc.), and IaC files in a single scan.

Running Trivy in CI:

```bash
# Scan a local image
trivy image --severity HIGH,CRITICAL myapp:latest

# Exit with non-zero code if HIGH or CRITICAL found (CI gate)
trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:latest

# Output in JSON for integration
trivy image --format json --output trivy-report.json myapp:latest

# Output in SARIF for GitHub Security tab
trivy image --format sarif --output trivy.sarif myapp:latest
```

In a GitHub Actions pipeline, the Trivy action integrates cleanly:

```yaml
- name: Build image
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

The `exit-code: "1"` is what makes this a blocking gate — if HIGH or CRITICAL vulnerabilities are found, the job fails, and the image is not pushed to the registry.

---

### SEGMENT 6 — Non-Root Containers and Capabilities (14:30–17:00)

[SLIDE: Linux capabilities diagram]

Running a container as root (`USER root`) means that if an attacker exploits a vulnerability in your application, they have root inside the container. With certain misconfigurations — like privileged mode or mounted host volumes — root inside the container can become root on the host.

The fix is simple: always create and use a non-root user. We saw this in the Dockerfile example. At runtime, you can also enforce non-root using Docker security options:

```bash
docker run \
  --user 1001:1001 \
  --read-only \
  --tmpfs /tmp \
  --cap-drop ALL \
  --cap-add NET_BIND_SERVICE \
  --no-new-privileges \
  myapp:latest
```

Let me explain each flag.

`--user 1001:1001` — run as UID/GID 1001, not root.

`--read-only` — mount the root filesystem as read-only. The application cannot write files outside of explicitly declared writable directories.

`--tmpfs /tmp` — provide a writable in-memory temporary directory. Required by many applications but does not persist between restarts.

`--cap-drop ALL` — drop all Linux capabilities. Capabilities like `NET_RAW`, `SYS_ADMIN`, `SYS_PTRACE` are dangerous if an attacker gains container access.

`--cap-add NET_BIND_SERVICE` — add back only the specific capability needed (in this case, binding to ports below 1024 — though it's better to use port 8080+ and avoid this entirely).

`--no-new-privileges` — prevents the process from gaining additional privileges via setuid binaries.

---

### SEGMENT 7 — Docker Content Trust and Registry Security (17:00–20:00)

[SLIDE: Docker Content Trust signing diagram]

Docker Content Trust (DCT) uses the Notary framework to sign images. When DCT is enabled, Docker only pulls images that have a valid signature from a trusted publisher.

```bash
# Enable DCT globally
export DOCKER_CONTENT_TRUST=1

# Push a signed image (prompts for signing keys)
docker push myregistry.io/myapp:v1.2.3

# Pull — will be verified against signature
docker pull myregistry.io/myapp:v1.2.3
```

For registry security, the key controls are:

Image signing with DCT or Sigstore/cosign ensures images were not tampered with in transit or storage.

Registry access control via role-based permissions prevents unauthorized users from pushing images.

Image scanning at push time — AWS ECR, Google Artifact Registry, and Azure Container Registry all support automatic scanning on image push.

Image tag immutability prevents a production image tag from being overwritten — once `v1.2.3` is pushed, no one can push a different image under that tag.

Pull-through cache with scanning combines performance and security — images are cached locally and scanned before being served to build systems.

---

### SEGMENT 8 — Module Summary and Looking Ahead (20:00–22:00)

[SLIDE: Module 04 key takeaways]

Module 04 in review.

Docker's threat model spans five surfaces: host OS, daemon, image, runtime, and registry.

Hardened Dockerfiles use multi-stage builds, minimal base images (slim or distroless), non-root users, explicit version pins, and minimal COPY scope.

Trivy scans container images for OS package CVEs and language library vulnerabilities. In CI, `--exit-code 1` makes it a blocking gate.

Runtime security flags — `--read-only`, `--cap-drop ALL`, `--no-new-privileges`, `--user` — minimize privilege at container runtime.

Docker Content Trust and Sigstore/cosign provide image signing for supply chain integrity.

Registry security includes access control, scanning at push, and tag immutability.

In Module 05 we scale up — Kubernetes security: RBAC, Pod Security Admission, network policies, and runtime threat detection with Falco. See you there.

---

*[END OF SCRIPT — Module 04]*
