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

---

### Question 11 (5 points)

A Dockerfile begins with `FROM ubuntu:latest`. Why is this considered a security anti-pattern?

- A) Ubuntu images are not compatible with Linux container runtimes
- B) The `latest` tag is mutable — a future build may silently pull a different, potentially vulnerable image version
- C) Ubuntu base images do not support multi-stage builds
- D) The `latest` tag always points to an end-of-life Ubuntu release

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Ubuntu images are fully compatible with Linux container runtimes — compatibility is not the concern.
  - C) Multi-stage builds work with any base image including Ubuntu.
  - D) `latest` typically points to the newest release, not an EOL version — the problem is mutability, not the specific version.

---

### Question 12 (5 points)

What does the `USER` instruction in a Dockerfile accomplish, and at which stage of a multi-stage build should it appear?

- A) It sets the username for Git commit attribution; it should appear in the build stage
- B) It sets the OS user that runs the container process; it should appear in the final stage just before CMD/ENTRYPOINT
- C) It grants the specified user sudo access inside the container
- D) It creates a new OS user account in the image; it must appear before any RUN instruction

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `USER` is a container runtime directive — it has nothing to do with Git.
  - C) `USER` switches the running user — it does not grant elevated privileges; switching to a non-root user removes privileges.
  - D) `USER` can reference a user that was already created earlier with `RUN useradd` — but the instruction itself does not create the account, and placement in the final stage is the security best practice.

---

### Question 13 (5 points)

Which Trivy scan target type would you use to detect vulnerabilities in a Terraform configuration file before it is deployed?

- A) `trivy image`
- B) `trivy fs`
- C) `trivy repo`
- D) `trivy config`

- **Correct Answer:** D
- **Distractor Analysis:**
  - A) `trivy image` scans container image layers for OS and library CVEs — not IaC files.
  - B) `trivy fs` scans a local filesystem for application dependencies and secrets — not IaC misconfigurations.
  - C) `trivy repo` scans a remote Git repository for vulnerabilities — not specifically IaC config files.

---

### Question 14 (5 points)

A container runs with `--security-opt seccomp=unconfined`. What is the security implication?

- A) The container can only execute system calls explicitly allowed in the default seccomp profile
- B) The container can make any system call to the Linux kernel, bypassing the default seccomp filter
- C) The container is prevented from loading kernel modules
- D) The container's network stack is isolated from all other containers

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `unconfined` means the opposite — no seccomp filtering at all.
  - C) Kernel module loading is controlled by the `SYS_MODULE` capability, not by seccomp configuration.
  - D) Network isolation is controlled by network namespaces and CNI plugins, not seccomp.

---

### Question 15 (5 points)

In a Docker Compose file, which configuration correctly mounts a volume as read-only?

- A) `volumes: - ./data:/app/data:ro`
- B) `volumes: - ./data:/app/data --read-only`
- C) `read_only: true` under the service definition
- D) `volumes: - ./data:/app/data:immutable`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The `:ro` suffix is the correct syntax for read-only volume mounts in Compose; `--read-only` is a `docker run` flag, not valid in volume syntax.
  - C) `read_only: true` at the service level makes the entire container filesystem read-only, but individual volume mounts use the `:ro` suffix on the volume path.
  - D) `immutable` is not a valid Docker volume mount option.

---

### Question 16 (5 points)

What is the purpose of generating a container SBOM with Syft and attesting it with cosign?

- A) To compress the image layers before pushing to a registry
- B) To create a signed, verifiable inventory of all packages in the image that can be audited for compliance and queried when new CVEs are disclosed
- C) To replace Trivy scanning — an attested SBOM eliminates the need for periodic rescans
- D) To encrypt the image layers so only authorized users can pull the image

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Syft and cosign perform attestation, not compression — image layer compression is handled by the registry or build tooling.
  - C) An SBOM is a point-in-time inventory; Trivy can scan the SBOM, but new CVEs require rescanning — the SBOM does not eliminate the need for ongoing scanning.
  - D) Image encryption is a separate concern handled by registry-level features or Docker Content Trust — not by Syft or cosign.

---

### Question 17 (5 points)

Which of the following correctly describes how `COPY --chown=appuser:appgroup` improves container security?

- A) It prevents the copied files from being readable by any process inside the container
- B) It ensures files are owned by a non-root user, so the application process does not need root access to read or write them
- C) It automatically runs a virus scan on the copied files before adding them to the image layer
- D) It signs the copied files with the image's cosign key

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `--chown` sets ownership, not access restrictions — the specified user and group still need read/write permissions.
  - C) `--chown` is a file ownership directive with no scanning capability.
  - D) Signing is a separate operation performed after the image is built, not during the COPY instruction.

---

### Question 18 (5 points)

A Docker image scan reveals that 90% of the detected CVEs are in packages installed by `RUN apt-get install -y build-essential`. These packages are only needed during compilation, not at runtime. What Dockerfile change eliminates these CVEs from the production image?

- A) Add `RUN apt-get remove build-essential` after the compilation step
- B) Use a multi-stage build: install and compile in a builder stage, then copy only the compiled binary into a minimal runtime image
- C) Pin the build-essential package to a specific version that has no CVEs
- D) Use `--no-cache` on the `docker build` command to prevent the packages from being stored

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `apt-get remove` may not cleanly remove all files and dependencies — and removed packages may still appear in lower image layers that Trivy scans.
  - C) Pinning to a CVE-free version of build-essential is impractical — the packages still have CVEs and are unnecessary at runtime.
  - D) `--no-cache` prevents Docker layer caching but does not affect which packages are present in the final image.

---

### Question 19 (5 points)

What is the function of the Grype tool in a container security pipeline?

- A) Grype is a container runtime monitor that detects anomalous system calls at execution time
- B) Grype is a vulnerability scanner that matches SBOM components against a CVE database, similar to Trivy
- C) Grype is a policy engine for enforcing Kubernetes admission control rules
- D) Grype generates and signs SBOMs for container images

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Runtime monitoring of system calls is performed by tools like Falco, not Grype.
  - C) Kubernetes admission control is handled by tools like OPA/Gatekeeper or Kyverno, not Grype.
  - D) SBOM generation is the role of Syft; Grype is Anchore's vulnerability scanner that consumes SBOMs or scans images directly.

---

### Question 20 (5 points)

In a Docker build, `RUN pip install -r requirements.txt` installs packages as root by default. Which sequence of Dockerfile instructions correctly creates a non-root user and installs packages as that user?

- A) `USER appuser` → `RUN pip install -r requirements.txt` → `RUN useradd -r appuser`
- B) `RUN useradd -r -s /bin/false appuser` → `RUN pip install -r requirements.txt` → `USER appuser`
- C) `RUN useradd -r -s /bin/false appuser` → `USER appuser` → `RUN pip install -r requirements.txt`
- D) `USER appuser` → `RUN useradd -r -s /bin/false appuser` → `RUN pip install -r requirements.txt`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `USER appuser` before `useradd` fails because the user does not exist yet.
  - C) Installing pip packages as a non-root `appuser` will fail unless the install location is owned by that user — root installation followed by user switch is the correct pattern for system packages.
  - D) `USER` before `useradd` fails for the same reason as A — the user must be created first.
