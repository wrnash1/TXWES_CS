# Reading Guide: Module 04 - Containerization: Docker Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 04 covers Docker container security — one of the highest-weight topics on the DevSecOps Professional exam. Modern DevSecOps pipelines build, scan, and deploy container images. Understanding the Docker security model, secure Dockerfile construction, image scanning tools, and container runtime hardening is essential for both the exam and real-world DevSecOps practice.

---

## Section 1: High-Yield Glossary

**Container** — A lightweight, isolated process that shares the host OS kernel but has its own filesystem, network, and process tree views via Linux namespaces. Containers are not virtual machines — they share the kernel.

**Docker image** — A read-only, layered filesystem snapshot used to create containers. Each Dockerfile instruction (RUN, COPY, ADD) creates a new layer. Image layers are cached and reused across builds.

**Dockerfile** — A text file containing sequential instructions for building a Docker image. Security best practices in the Dockerfile directly determine the attack surface of every container spawned from the image.

**Linux namespace** — A kernel feature that isolates a container's view of system resources. Types used by Docker: PID (process tree), net (network interfaces), mnt (filesystem mounts), uts (hostname), user (user IDs).

**Control group (cgroup)** — A Linux kernel feature that limits and accounts for resource usage (CPU, memory, disk I/O) by a container. Used by Docker to enforce resource limits.

**Container breakout** — A vulnerability that allows a process inside a container to escape its namespace isolation and gain access to the host system or other containers. A rare but high-severity class of vulnerability.

**Multi-stage build** — A Dockerfile pattern using multiple `FROM` instructions, where intermediate stages handle compilation or dependency installation and the final stage copies only the necessary artifacts. Reduces image size and attack surface by excluding build tools.

**Base image** — The image specified in the `FROM` instruction that forms the foundation of a Dockerfile build. The security posture of the base image directly affects the final image's vulnerability exposure.

**Distroless image** — A minimal container base image maintained by Google that contains only the application runtime and its dependencies — no shell, no package manager, no standard Unix utilities. Dramatically reduces attack surface.

**Non-root container** — A container whose main process runs as a user other than root (UID 0). Non-root containers limit the damage an attacker can do if they achieve code execution inside the container.

**Image layer** — A delta of filesystem changes produced by one Dockerfile instruction. Layers are cached and stacked to form the final image. Sensitive data written to a layer (even if deleted in a later layer) persists in the image's history.

**Trivy** — An open-source container image and filesystem vulnerability scanner from Aqua Security. Scans OS packages, language runtime dependencies, and misconfigurations. Primary container scanning tool for DevSecOps pipelines.

**Grype** — An open-source container and filesystem vulnerability scanner from Anchore. Similar capability to Trivy; often used as a second opinion scanner or preferred in Anchore-ecosystem environments.

**Hadolint** — An open-source Dockerfile linter that checks Dockerfile instructions against security and best-practice rules. Run at the pre-build stage of the CI pipeline.

**SARIF (Static Analysis Results Interchange Format)** — A JSON-based standard format for static analysis tool output. GitHub, GitLab, and other platforms consume SARIF files to display security findings in the repository's security dashboard.

**Container registry** — A service for storing and distributing Docker images. Examples: Docker Hub, Amazon ECR, Google Artifact Registry, self-hosted Harbor. Images should be scanned before pushing to production registries.

**Read-only filesystem** — A container runtime flag (`--read-only` in Docker run) that mounts the container's root filesystem as read-only, preventing an attacker from writing malicious files to the container's filesystem.

**Capability dropping** — The practice of removing Linux capabilities from a container (`--cap-drop ALL`) to restrict what privileged operations the container process can perform. Principle of least privilege applied to containers.

**Rootless Docker** — A Docker configuration where the Docker daemon runs as a non-root user, reducing the risk that a compromised daemon leads to host root compromise.

---

## Section 2: Docker Security Model vs. VM Security Model

| Dimension | Docker Container | Virtual Machine |
|---|---|---|
| Kernel sharing | Shares host OS kernel | Has its own isolated kernel |
| Isolation mechanism | Linux namespaces + cgroups | Hypervisor hardware virtualization |
| Isolation strength | Weaker (shared kernel) | Stronger (full OS isolation) |
| Startup time | Milliseconds | Seconds to minutes |
| Resource overhead | Minimal | Significant (full OS per VM) |
| Container escape risk | Yes (kernel vulnerability) | More difficult (hypervisor boundary) |
| Use case in DevSecOps | Application packaging, CI runners | High-security isolation requirements |

---

## Section 3: Secure Dockerfile Best Practices Reference

The following six practices are the most heavily tested Docker security topics on the DevSecOps Professional exam.

| Practice | Insecure Pattern | Secure Pattern | Security Reason |
|---|---|---|---|
| Base image selection | `FROM ubuntu:latest` | `FROM python:3.11-slim` or distroless | Minimal images have fewer packages and smaller CVE exposure |
| Image version pinning | `FROM node:latest` | `FROM node:20.11.0-alpine3.19` | Pinned versions are reproducible and CVE-trackable |
| Non-root user | No USER directive (runs as root) | `RUN useradd -r appuser` then `USER appuser` | Limits attacker capabilities on container compromise |
| Multi-stage build | Single stage with build tools | `FROM ... AS builder`, then `FROM ... COPY --from=builder` | Excludes build tools and source from production image |
| Selective COPY | `COPY . /app` | `COPY src/ /app/src/` | Prevents .env files, tests, secrets from entering image |
| CMD form | `CMD python app.py` (shell form) | `CMD ["python", "app.py"]` (exec form) | Exec form handles signals correctly; no shell injection |

---

## Section 4: Docker Image Layer Security

A critical concept tested on the exam: **data written to any image layer persists in the image history, even if deleted in a later layer.**

Example of the mistake:

```dockerfile
RUN echo "SECRET_KEY=abc123" > /app/.env
# ... some steps ...
RUN rm /app/.env   # This does NOT remove the data from image history
```

Anyone who pulls this image and inspects its layers with `docker history` or `docker image inspect` can retrieve the `.env` file from the layer where it was created.

Correct pattern: never write secrets to image layers at all. Pass secrets at runtime via environment variables or volume mounts. Use BuildKit secret mounts for build-time secrets:

```dockerfile
RUN --mount=type=secret,id=mysecret cat /run/secrets/mysecret
```

BuildKit secret mounts are not persisted in image layers.

---

## Section 5: Container Image Scanning Reference

| Dimension | Trivy | Grype |
|---|---|---|
| Maintainer | Aqua Security | Anchore |
| License | Apache 2.0 | Apache 2.0 |
| Scans | OS packages, language deps, IaC, secrets | OS packages, language deps |
| Database | Continuously updated (offline mode available) | Continuously updated (offline mode available) |
| Output formats | Table, JSON, SARIF, CycloneDX | Table, JSON, SARIF |
| Pipeline exit code | `--exit-code 1` | `--fail-on critical` |
| GitHub Actions integration | `aquasecurity/trivy-action` | `anchore/scan-action` |

---

## Section 6: CI/CD Pipeline Stage Comparison — Container Security Placement

| Pipeline Stage | Container Security Control | Tool |
|---|---|---|
| Pre-build | Dockerfile lint | Hadolint |
| After image build | Image vulnerability scan | Trivy or Grype |
| Before registry push | Scan threshold enforcement (exit-code 1) | Trivy or Grype |
| Registry storage | Continuous registry scanning | ECR scan-on-push, Harbor |
| Runtime (Kubernetes) | Admission controller image policy | OPA Gatekeeper, Kyverno |
| Runtime monitoring | Container runtime anomaly detection | Falco |

---

## Section 7: Docker Runtime Security Hardening Reference

When running containers in production, these runtime flags implement the principle of least privilege.

```bash
docker run \
  --read-only \
  --cap-drop ALL \
  --cap-add NET_BIND_SERVICE \
  --security-opt no-new-privileges \
  --memory 256m \
  --cpus 0.5 \
  --user 1001:1001 \
  myapp:latest
```

- `--read-only` — mounts root filesystem read-only; attacker cannot write to container filesystem.
- `--cap-drop ALL` — removes all Linux capabilities from the container.
- `--cap-add NET_BIND_SERVICE` — adds back only the specific capability needed (binding to privileged ports). Add only what is required.
- `--security-opt no-new-privileges` — prevents the container process from gaining additional privileges via setuid/setgid binaries.
- `--memory` and `--cpus` — resource limits preventing denial-of-service conditions.
- `--user` — runs container process as a specific non-root UID/GID.

---

## Section 8: SAST vs. DAST vs. SCA Comparison

| Dimension | SAST | DAST | SCA |
|---|---|---|---|
| Requires running application | No | Yes | No |
| Primary target | First-party source code | Running application endpoints | Third-party dependencies |
| Pipeline stage | Commit / Pull request | Staging | Build |
| Docker-specific equivalent | Dockerfile linting (Hadolint) | Container DAST (running container) | Image layer scanning (Trivy/Grype) |

---

## Section 9: DevSecOps Professional Exam Tips

1. **Non-root user directive** — Know that `USER appuser` in a Dockerfile switches the running process to a non-root user. Know that this directive must come after the user is created with `useradd` or `adduser`, and must appear before the `CMD` instruction.

2. **Multi-stage build purpose** — The primary security purpose of multi-stage builds is to exclude build-time tools (compilers, package managers) from the final image, reducing attack surface. Size reduction is a secondary benefit.

3. **Layer persistence** — Know that deleting a file in a later Dockerfile layer does NOT remove it from image history. Secrets must never be written to layers, even temporarily.

4. **Trivy --exit-code 1** — This flag makes Trivy a pipeline gate. Without it, Trivy reports findings but the pipeline step succeeds regardless. Know that `--severity CRITICAL,HIGH` limits failures to high-severity findings only.

5. **exec form vs. shell form CMD** — The exam tests this distinction. Exec form `CMD ["python", "app.py"]` receives signals directly. Shell form `CMD python app.py` wraps in `/bin/sh -c` and may not propagate SIGTERM properly, leading to ungraceful container shutdown.

6. **Distroless images** — Know that distroless images have no shell (`/bin/sh` does not exist), making interactive exec into the container for debugging impossible — but also making many attack techniques that rely on shell execution impossible.

7. **Container breakout** — Know the concept: a vulnerability allowing escape from container namespaces to the host. Know that this is more likely when containers run as root and that non-root + capability dropping reduces breakout risk.

8. **Registry scan-on-push** — Know that cloud registries like Amazon ECR and Google Artifact Registry support scanning images on push, providing a registry-level enforcement layer even if a CI pipeline scan is bypassed.

---

## Section 10: Study Checklist

- [ ] Explain the difference between container isolation (namespaces/cgroups) and VM isolation (hypervisor).
- [ ] List the six secure Dockerfile practices and the security reason for each.
- [ ] Explain why deleting a secret in a later Dockerfile layer does not remove it from the image.
- [ ] Write a multi-stage Dockerfile from memory for a Python application.
- [ ] Explain the difference between Trivy's table output mode and its pipeline gate mode (`--exit-code 1`).
- [ ] List the four Docker runtime hardening flags and what each does.
- [ ] Explain what a distroless base image is and its security trade-off.
- [ ] Read the OWASP DevSecOps Guideline container security section at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
- [ ] Complete the Module 04 lab activity (secure multi-stage Dockerfile).
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
