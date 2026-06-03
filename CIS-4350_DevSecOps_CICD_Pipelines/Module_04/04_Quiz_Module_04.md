# Quiz: Module 04 — Container Security with Docker

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Submit answers through the Canvas quiz interface.

---

## Question 1

Why is mounting `/var/run/docker.sock` into a container considered a critical security risk?

- A) It causes the container to use the host network namespace
- B) It gives the container the ability to manage Docker itself, effectively providing root access to the host
- C) It prevents the container from being scanned by image scanning tools
- D) It disables the read-only filesystem feature of the container

### Q1 — Correct Answer: B

### Q1 — Distractor Analysis

- A) Host network access is controlled by `--network host`, not the Docker socket.
- C) Image scanning occurs at the image layer level and is not affected by socket mounts at runtime.
- D) Read-only filesystem is a separate runtime flag — socket mounts do not affect it.

---

## Question 2

What is the primary security benefit of a multi-stage Docker build?

- A) Multi-stage builds make images run faster because fewer layers are loaded
- B) Multi-stage builds allow the production image to exclude build tools, compilers, and source code
- C) Multi-stage builds automatically scan each stage for vulnerabilities
- D) Multi-stage builds ensure the container always runs as a non-root user

### Q2 — Correct Answer: B

### Q2 — Distractor Analysis

- A) Performance may be affected, but security attack surface reduction is the primary benefit.
- C) Multi-stage builds do not perform scanning — that is handled by separate tools like Trivy.
- D) Non-root user configuration is a separate `USER` directive and is independent of multi-stage builds.

---

## Question 3

A container is run with `--cap-drop ALL --cap-add NET_BIND_SERVICE`. What does this configuration achieve?

- A) The container can access the host network but cannot bind to any ports
- B) The container drops all Linux capabilities except the ability to bind to ports below 1024
- C) The container is prevented from using any network connections
- D) The container is granted full root capabilities for network operations

### Q3 — Correct Answer: B

### Q3 — Distractor Analysis

- A) `NET_BIND_SERVICE` is specifically about port binding below 1024, not host network access.
- C) `--cap-drop ALL` removes privileged capabilities — normal network operations using unprivileged ports are still available.
- D) Adding back `NET_BIND_SERVICE` is highly targeted — it is far from full root network capabilities.

---

## Question 4

Which base image option provides the smallest attack surface and eliminates the ability for an attacker to run an interactive shell inside the container?

- A) `ubuntu:22.04`
- B) `python:3.12-alpine`
- C) `python:3.12-slim`
- D) `gcr.io/distroless/python3`

### Q4 — Correct Answer: D

### Q4 — Distractor Analysis

- A) Ubuntu is a full-featured OS with a shell, package manager, and many utilities — largest attack surface.
- B) Alpine has a shell (`/bin/sh`) and the `apk` package manager — it has a shell, unlike distroless.
- C) Slim images have a shell and package manager — they reduce size but do not eliminate shell access.

---

## Question 5

In a Trivy CI gate configured with `exit-code: "1"` and `severity: HIGH,CRITICAL`, what happens if only Medium severity vulnerabilities are found?

- A) The pipeline fails because any vulnerability should block progression
- B) The pipeline passes because only HIGH and CRITICAL trigger the exit code
- C) The pipeline pauses and waits for manual approval
- D) Trivy generates a warning but does not produce a SARIF file

### Q5 — Correct Answer: B

### Q5 — Distractor Analysis

- A) The severity filter is explicit — Medium findings do not trigger the configured exit code.
- C) Pipeline pause for manual approval is a separate feature not related to Trivy's exit code setting.
- D) SARIF output is independent of the severity filter and exit code — it is generated regardless.

---

## Question 6

What is the `.dockerignore` file's role in container security?

- A) It specifies which ports the container is allowed to expose
- B) It prevents sensitive files such as `.env` and private keys from entering the Docker build context
- C) It lists container images that should not be pulled from external registries
- D) It configures which capabilities are dropped when the container runs

### Q6 — Correct Answer: B

### Q6 — Distractor Analysis

- A) Exposed ports are declared with the `EXPOSE` instruction, not `.dockerignore`.
- C) `.dockerignore` is a build-time file — it has no effect on image pulls from registries.
- D) Runtime security flags like `--cap-drop` are set in the `docker run` command or Compose file, not `.dockerignore`.

---

## Question 7

Which Docker runtime flag prevents setuid binaries inside a container from escalating the process's privileges?

- A) `--read-only`
- B) `--cap-drop ALL`
- C) `--no-new-privileges`
- D) `--user 1001:1001`

### Q7 — Correct Answer: C

### Q7 — Distractor Analysis

- A) `--read-only` makes the filesystem immutable but does not prevent setuid escalation.
- B) `--cap-drop ALL` removes Linux capabilities but a setuid root binary can still elevate if `--no-new-privileges` is not set.
- D) `--user` sets the initial user — but setuid binaries owned by root can still escalate unless `--no-new-privileges` is also used.

---

## Question 8

cosign is preferred over Docker Content Trust (DCT) for modern container image signing because:

- A) cosign signs images faster due to a more efficient cryptographic algorithm
- B) cosign integrates with Sigstore's transparency log, supports keyless signing via OIDC, and is the CNCF-endorsed standard
- C) cosign is built into Docker Desktop and requires no additional installation
- D) cosign automatically scans images for CVEs as part of the signing process

### Q8 — Correct Answer: B

### Q8 — Distractor Analysis

- A) Signing speed is not a meaningful differentiator between the two approaches.
- C) cosign requires separate installation — it is not built into Docker Desktop.
- D) cosign handles signing and verification only — CVE scanning is a separate function performed by Trivy or similar tools.

---

## Question 9

A Dockerfile contains `CMD python3 app.py` (shell form). Why is `CMD ["python3", "app.py"]` (exec form) preferred from a security and reliability perspective?

- A) Exec form runs faster because it bypasses the OS shell
- B) Exec form ensures the process receives OS signals directly and does not launch a shell interpreter as PID 1
- C) Exec form automatically enables read-only filesystem mode
- D) Exec form is required for multi-stage builds to work correctly

### Q9 — Correct Answer: B

### Q9 — Distractor Analysis

- A) Performance difference is negligible — signal handling and PID 1 are the meaningful reasons.
- C) Read-only filesystem is a runtime flag — CMD form has no effect on it.
- D) Multi-stage builds work correctly with either CMD form — exec form is not a requirement.

---

## Question 10

Which registry feature prevents a production image tag (e.g., `v1.2.3`) from being overwritten by a subsequent push of a different image using the same tag?

- A) Vulnerability scanning at push
- B) Tag immutability
- C) Image signing
- D) Pull-through cache

### Q10 — Correct Answer: B

### Q10 — Distractor Analysis

- A) Vulnerability scanning detects CVEs — it does not prevent tag overwrites.
- C) Image signing verifies authenticity — it does not prevent tags from being overwritten by the key holder.
- D) Pull-through cache improves performance and reduces external dependency — it does not enforce tag uniqueness.

---

Quiz — Module 04 | CIS-4350 | Texas Wesleyan University | Professor Nash
