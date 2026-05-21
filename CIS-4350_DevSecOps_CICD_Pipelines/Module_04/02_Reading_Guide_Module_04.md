# Reading Guide: Module 04 - Containerization – Docker Security

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 04 - Containerization – Docker Security**! This module covers Docker as both a deployment technology and a security surface that must be managed within a DevSecOps pipeline. You will learn how Dockerfile instructions affect the attack surface of a container image, why multi-stage builds reduce vulnerability exposure, how Docker layer caching interacts with security scanning, and how images are built and pushed securely within CI/CD workflows. These container security concepts are core to the CDP exam and to modern cloud-native deployments.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Dockerfile syntax**: The set of instructions (`FROM`, `RUN`, `COPY`, `USER`, `EXPOSE`, `ENTRYPOINT`) used to define how a container image is built layer by layer. Security-relevant Dockerfile practices include using minimal base images, avoiding running as root (`USER nonroot`), copying only necessary files, and not embedding secrets in `RUN` or `ENV` instructions.

* **Container layers**: Each `RUN`, `COPY`, or `ADD` instruction in a Dockerfile creates a new read-only layer in the image. Once a layer is written, its contents persist in the image — including any files that are later deleted in subsequent layers. This means secrets accidentally written to a `RUN` layer and then deleted are still recoverable from the image history, making layer-aware secret hygiene critical.

* **Caching strategies**: Docker's layer cache reuses previously built layers when inputs have not changed, speeding up builds. In a CI/CD pipeline, cache strategy affects both build speed and security: placing frequently changing instructions (like `COPY . .`) late in the Dockerfile maximizes cache hits, while placing dependency installation (`RUN pip install`) early ensures stable layers are cached and only rebuilt when `requirements.txt` changes.

* **Building images in pipelines**: The process of running `docker build` within a CI/CD job to produce a tagged image artifact. Pipeline-integrated builds ensure every image is built from a known, version-controlled Dockerfile, scanned for vulnerabilities before being pushed to a registry, and tagged with a meaningful version (commit SHA or semantic version) for traceability.

---

### 2. Certification Exam Tips

* **Multi-Stage Build Security**: The CDP exam frequently tests multi-stage builds. Know that `FROM builder AS build` followed by `FROM gcr.io/distroless/base` with a `COPY --from=build` copies only the compiled artifact into a minimal final image, eliminating build tools (compilers, package managers) from the deployed image and drastically reducing the vulnerability footprint.
* **Non-Root User**: Running containers as root is a critical security misconfiguration. The CDP exam expects you to know that `USER nonroot` (or `USER 1001`) in a Dockerfile prevents privilege escalation if the container is compromised, and that Kubernetes Pod Security Standards also enforce non-root execution.
* **Secret in Build Layer**: Know that `ENV SECRET=value` and `RUN curl -H "Authorization: $TOKEN"` both embed sensitive values into image layers visible via `docker history`. The correct pattern is to inject secrets at runtime via environment variables or a secrets manager, never at build time.
* **Study Resource**: The [Docker Security Best Practices documentation](https://docs.docker.com/develop/security-best-practices/) covers image hardening, rootless Docker, content trust, and registry security — all topics appearing on the CDP exam.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [Docker Security Best Practices guide](https://docs.docker.com/develop/security-best-practices/) — official Docker documentation covering image hardening, non-root users, multi-stage builds, secret management, and registry authentication. Focus on image build security and the sections on least-privilege container execution.
* **Required Video**: Watch the Docker containerization segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates writing Dockerfiles, building images within a CI pipeline, and pushing images to a registry as a pipeline artifact.

---

### Lab & Command Integration

In this week's hands-on lab, you will apply Docker security principles by:

* **Build package directories**: Structure a sample application with a multi-stage Dockerfile — a build stage that compiles or installs dependencies, and a final stage using a minimal base image that copies only the runtime artifact.
* **Configure build artifact outputs inside pipelines**: Add a `docker build` and `docker push` step to a GitHub Actions workflow, using GitHub Actions secrets to supply registry credentials rather than hardcoding them in the workflow file.
* **Upload build packages to mock registries**: Tag and push the built image to GitHub Container Registry (ghcr.io) using the `GITHUB_TOKEN` secret for authentication, then verify the image appears in the repository's Packages section.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how each Dockerfile concept affects container security posture.
* [ ] Read the Docker Security Best Practices guide at [https://docs.docker.com/develop/security-best-practices/](https://docs.docker.com/develop/security-best-practices/).
* [ ] Watch the Docker containerization segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the multi-stage Dockerfile and pipeline build step in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
