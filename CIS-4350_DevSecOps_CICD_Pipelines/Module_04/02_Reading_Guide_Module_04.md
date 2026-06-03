# Reading Guide: Module 04 — Container Security with Docker

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Describe Docker's five-surface threat model
- Write a production-hardened Dockerfile using multi-stage builds and non-root users
- Compare minimal base image options and their security trade-offs
- Use Trivy and Snyk to scan container images in CI pipelines with blocking gates
- Apply runtime security flags to minimize container privilege
- Configure Docker Content Trust and registry security controls

---

## Section 1 — Docker Architecture and Threat Model

### 1.1 Docker Components

| Component | Description | Security Relevance |
|---|---|---|
| Docker Client | CLI sending commands to daemon | Must use TLS for remote daemon |
| Docker Daemon | Process managing containers/images | Runs as root; high-value target |
| Docker Socket | `/var/run/docker.sock` | Root-equivalent access; never mount in containers |
| Container Runtime | runc or containerd | Namespace isolation; escape = host compromise |
| Image Registry | Docker Hub, ECR, GCR, ACR | Supply chain; scan images at push |
| Container | Isolated process using host kernel | Namespace + cgroups = not a VM |

### 1.2 Container vs. VM Isolation

Containers share the host OS kernel. They use Linux namespaces (PID, network, mount, IPC, UTS, user) for isolation and cgroups for resource limits. This is fundamentally weaker isolation than a hypervisor VM.

Security implication: a kernel vulnerability exploitable from inside a container can be used to escape to the host. VMs require a hypervisor vulnerability plus a guest OS vulnerability for the same effect.

### 1.3 Five Attack Surfaces

| Surface | Example Attack | Primary Control |
|---|---|---|
| Host OS | Kernel exploit enabling container escape | Keep host kernel patched |
| Docker Daemon | Exploit via exposed Docker API | Never expose daemon to network; use TLS |
| Docker Socket | Mount socket into container for host escape | Never mount `/var/run/docker.sock` |
| Container Image | CVE in base image OS package exploited at runtime | Image scanning + minimal base images |
| Registry | Push malicious image; image substitution MITM | DCT/cosign image signing; registry access control |

---

## Section 2 — Dockerfile Security Best Practices

### 2.1 Insecure vs. Hardened Dockerfile Comparison

| Practice | Insecure | Hardened |
|---|---|---|
| Base image | `FROM ubuntu:latest` | `FROM python:3.12-slim` or distroless |
| Tag pinning | Floating `:latest` tag | Pinned version or SHA digest |
| Build isolation | Single-stage (build tools in runtime image) | Multi-stage build |
| User | Default root | `RUN useradd -r appuser && USER appuser` |
| Copy scope | `COPY . /app` (everything) | `COPY --chown=appuser src/ /app/` |
| CMD form | Shell form: `CMD python app.py` | Exec form: `CMD ["python", "app.py"]` |
| Secret handling | ARG/ENV for secrets | BuildKit secrets (`--mount=type=secret`) |
| Image size | Large — all packages | Minimal — only runtime dependencies |

### 2.2 Multi-Stage Build Pattern

```dockerfile
# ============================================================
# Stage 1: Dependency installer (discarded after build)
# ============================================================
FROM python:3.12-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ============================================================
# Stage 2: Production runtime image
# ============================================================
FROM python:3.12-slim AS runtime

LABEL org.opencontainers.image.source="https://github.com/org/repo"
LABEL org.opencontainers.image.description="Production API service"

# Create non-root system user
RUN groupadd -r appuser --gid=1001 \
    && useradd -r --uid=1001 -g appuser appuser

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Copy application source — not test files, not .env
COPY --chown=appuser:appuser src/ .

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

CMD ["/home/appuser/.local/bin/gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
```

### 2.3 Base Image Selection

| Image | Size | Shell | Package Manager | Security Use Case |
|---|---|---|---|---|
| `ubuntu:22.04` | ~70MB | Yes | apt | General purpose; high attack surface |
| `debian:bookworm-slim` | ~75MB | Yes | apt | Reduced surface vs. full Debian |
| `python:3.12-slim` | ~130MB | Yes | apt + pip | Python apps; good balance |
| `python:3.12-alpine` | ~50MB | sh | apk | Minimal; musl libc compat issues |
| `gcr.io/distroless/python3` | ~50MB | No | None | Maximum security; no shell |
| `scratch` | 0 | No | None | Static binaries (Go, Rust) only |

### 2.4 .dockerignore File

The `.dockerignore` file prevents sensitive files from entering the build context:

```gitignore
# .dockerignore
.env
.env.*
.git/
.github/
tests/
docs/
*.md
*.log
node_modules/
__pycache__/
.pytest_cache/
.coverage
dist/
build/
```

---

## Section 3 — Container Image Scanning

### 3.1 Trivy Scan Modes

| Mode | Command | Scans |
|---|---|---|
| Image scan | `trivy image myapp:latest` | OS packages, language libs |
| Filesystem scan | `trivy fs .` | Files in directory |
| Repository scan | `trivy repo github.com/org/repo` | Remote repository |
| Config scan | `trivy config .` | IaC misconfigurations |
| SBOM generation | `trivy sbom myapp:latest` | Software bill of materials |

### 3.2 Trivy Output Formats

```bash
# Table (default — human readable)
trivy image python:3.8-slim

# JSON (for programmatic processing)
trivy image --format json --output report.json python:3.8-slim

# SARIF (for GitHub/GitLab Security tab)
trivy image --format sarif --output trivy.sarif python:3.8-slim

# CycloneDX (SBOM format)
trivy image --format cyclonedx --output sbom.json python:3.8-slim
```

### 3.3 Snyk Container Scanning

Snyk offers both a CLI and GitHub Actions integration with additional features including base image upgrade recommendations:

```bash
# CLI scan
snyk container test myapp:latest

# With Snyk-suggested base image upgrade
snyk container test myapp:latest --file=Dockerfile

# In GitHub Actions
- name: Snyk Container scan
  uses: snyk/actions/docker@master
  with:
    image: myapp:${{ github.sha }}
    args: --file=Dockerfile --severity-threshold=high
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

### 3.4 Scan Severity Thresholds for CI Gates

| Severity | CVSS Range | Recommended Gate Action |
|---|---|---|
| Critical | 9.0–10.0 | Always block |
| High | 7.0–8.9 | Block (after grace period) |
| Medium | 4.0–6.9 | Warn; create ticket |
| Low | 0.1–3.9 | Report only |

---

## Section 4 — Runtime Security Controls

### 4.1 Docker Run Security Flags

```bash
docker run \
  --user 1001:1001 \           # Run as non-root UID/GID
  --read-only \                # Read-only root filesystem
  --tmpfs /tmp:noexec,nosuid \ # Writable temp; no execute, no setuid
  --cap-drop ALL \             # Drop all Linux capabilities
  --cap-add NET_BIND_SERVICE \ # Add back only what's needed
  --no-new-privileges \        # Prevent privilege escalation
  --security-opt seccomp=default.json \ # Restrict syscalls
  --memory 512m \              # Resource limit
  --cpus 1.0 \                 # CPU limit
  --pids-limit 100 \           # Process limit
  myapp:latest
```

### 4.2 Linux Capabilities Reference

| Capability | What It Allows | Risk if Granted |
|---|---|---|
| `SYS_ADMIN` | Mount filesystems, many admin ops | Near-root; avoid in containers |
| `NET_ADMIN` | Configure network interfaces | Network manipulation |
| `NET_RAW` | Raw socket access | Packet sniffing, ARP spoofing |
| `SYS_PTRACE` | Process tracing | Inspect other processes' memory |
| `DAC_OVERRIDE` | Bypass file permission checks | Read any file on system |
| `NET_BIND_SERVICE` | Bind to ports < 1024 | Low risk; needed for HTTP/HTTPS on standard ports |

Best practice: `--cap-drop ALL` then add back only what your application requires.

### 4.3 Docker Compose Security

```yaml
# docker-compose.yml — hardened service definition
services:
  api:
    image: myapp:v1.2.3
    user: "1001:1001"
    read_only: true
    tmpfs:
      - /tmp:noexec,nosuid
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    security_opt:
      - no-new-privileges:true
    mem_limit: 512m
    cpus: 1.0
    pids_limit: 100
    environment:
      - DATABASE_URL
    secrets:
      - db_password
    networks:
      - internal
    ports:
      - "127.0.0.1:8080:8080"  # Bind to localhost only

secrets:
  db_password:
    external: true
```

---

## Section 5 — Docker Content Trust and Registry Security

### 5.1 Docker Content Trust (DCT)

```bash
# Enable DCT for all Docker operations
export DOCKER_CONTENT_TRUST=1

# Push signs the image with your Notary key
docker push myregistry.io/myapp:v1.2.3

# Pull validates signature before downloading
docker pull myregistry.io/myapp:v1.2.3

# Verify image signature
docker trust inspect myregistry.io/myapp:v1.2.3
```

### 5.2 Sigstore / cosign (Modern Alternative)

cosign is the modern image signing tool from the Sigstore project, now preferred over DCT:

```bash
# Generate a key pair
cosign generate-key-pair

# Sign an image
cosign sign --key cosign.key myregistry.io/myapp:v1.2.3

# Verify before deployment
cosign verify --key cosign.pub myregistry.io/myapp:v1.2.3

# Keyless signing (uses GitHub Actions OIDC)
cosign sign myregistry.io/myapp:v1.2.3
```

### 5.3 Registry Security Controls

| Control | AWS ECR | GCR / Artifact Registry | Azure ACR | Docker Hub |
|---|---|---|---|---|
| Vulnerability scanning | Enhanced scanning (Trivy) | Artifact Analysis | Microsoft Defender | Docker Scout |
| Image signing | cosign / DCT | Binary Authorization | Notation | DCT |
| Private registries | Yes (IAM) | Yes (IAM) | Yes (RBAC) | Paid tier |
| Tag immutability | Yes | Yes | Yes | Limited |
| Pull-through cache | Yes | Yes | Yes | No |
| Geo-replication | Yes | Yes | Yes | No |

---

## Exam Tips for DSOE Certification

- Know the five Docker attack surfaces: host OS, daemon, socket, image, registry.
- Mounting `/var/run/docker.sock` into a container gives the container root access to the host.
- Multi-stage builds reduce image size and attack surface by excluding build tools from the final image.
- `--cap-drop ALL` + `--cap-add <only-needed>` is the least-privilege approach to Linux capabilities.
- `--no-new-privileges` prevents setuid binaries from escalating privileges.
- `--read-only` combined with `--tmpfs /tmp` is the standard way to use read-only containers with a writable temp directory.
- Trivy scans OS packages AND language libraries; `--exit-code 1` makes it a blocking CI gate.
- DCT uses Notary; cosign uses Sigstore. Both sign images for supply chain integrity.
- Distroless images have no shell and no package manager — maximum attack surface reduction.
- `.dockerignore` prevents `.env` files and other secrets from entering the build context.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| Docker Daemon | Background process managing containers and images; runs as root |
| Docker Socket | Unix socket for daemon communication; root-equivalent access |
| Multi-Stage Build | Dockerfile using multiple FROM stages; final image contains only runtime artifacts |
| Distroless | Google's minimal container images containing only runtime, no shell or package manager |
| Trivy | Open-source image scanner by Aqua Security |
| cosign | Sigstore tool for container image signing |
| Docker Content Trust | DCT — Notary-based image signing framework |
| Linux Capabilities | Fine-grained root privilege subdivision |
| `--no-new-privileges` | Docker flag preventing privilege escalation via setuid |
| SBOM | Software Bill of Materials — inventory of all image components |
| `.dockerignore` | File excluding paths from Docker build context |

---

Reading Guide — Module 04 | CIS-4350 | Texas Wesleyan University | Professor Nash
