# Quiz: Module 04 - Containerization: Docker Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

What is the primary security purpose of using a non-root user in a Docker container?

- A) To allow the container to communicate with other containers on the same Docker network
- B) To limit the damage an attacker can do if they achieve code execution inside the container, since the process lacks root privileges
- C) To enable the container to bind to privileged ports (below 1024) without requiring additional configuration
- D) To allow multiple containers to share the same user credentials for inter-service authentication

#### Q1 Correct Answer

B — If an attacker exploits a vulnerability in the containerized application, they execute code as the limited non-root user. They cannot write to system directories, install packages, modify system configurations, or perform other root-level operations.

#### Q1 Distractor Analysis

- *Why A is incorrect:* Container network communication is controlled by Docker networking configuration (bridges, overlay networks), not by the user the container runs as.
- *Why C is incorrect:* Non-root users cannot bind to privileged ports by default. Running as non-root actually prevents privileged port binding without the `NET_BIND_SERVICE` capability.
- *Why D is incorrect:* Container-to-container authentication uses service accounts, API tokens, or mTLS — not shared OS users.

---

### Question 2

A developer writes the following Dockerfile instructions in sequence. What is the security problem with this approach?

```dockerfile
RUN echo "DB_PASS=secret123" > /app/.env
# ... additional build steps ...
RUN rm /app/.env
```

- A) The `RUN` instruction cannot execute shell commands — it is for package installation only
- B) The `.env` file is written to an image layer and persists in the image history even after the subsequent deletion, making the secret recoverable
- C) Docker automatically encrypts any file containing the string "PASS", making the delete step redundant
- D) The `RUN rm` instruction will fail because Docker mounts all files read-only during the build process

#### Q2 Correct Answer

B — Each Dockerfile `RUN` instruction creates a new image layer. The `.env` file is written to layer N and exists permanently in that layer. The `RUN rm` creates a new layer N+1 that hides the file in the final filesystem view, but layer N still exists in the image and can be inspected with `docker history` or extracted using image inspection tools.

#### Q2 Distractor Analysis

- *Why A is incorrect:* `RUN` executes shell commands in the container environment during build. It is not restricted to package installation.
- *Why C is incorrect:* Docker does not automatically encrypt file contents based on filenames. No such automatic protection exists.
- *Why D is incorrect:* The build-time filesystem is writable. `RUN rm` executes successfully — the problem is that the deletion creates a new layer without removing the data from the previous layer.

---

### Question 3

Which Dockerfile instruction pattern correctly implements a multi-stage build for a Python application?

- A) Using `FROM python:3.11-slim` twice in the same Dockerfile without any inter-stage data transfer
- B) Using `FROM python:3.11-slim AS builder` for the first stage and `COPY --from=builder /install /usr/local` in the second stage to transfer only installed packages
- C) Using `RUN pip install` in the first stage and `RUN pip install` again in the second stage to ensure both stages have dependencies
- D) Using `COPY --from=0 /app /app` to copy the entire first stage filesystem into the second stage

#### Q3 Correct Answer

B — The builder stage installs dependencies into an isolated prefix (`/install`). The production stage starts fresh from the base image and copies only the installed packages — not pip, not build tools, not any build artifacts. This is the correct multi-stage pattern.

#### Q3 Distractor Analysis

- *Why A is incorrect:* Using the same base image twice without `COPY --from=builder` provides no benefit — it just creates two independent stages with no data transfer.
- *Why C is incorrect:* Running pip install in both stages defeats the purpose of multi-stage builds. The final image still contains pip and all build tools.
- *Why D is incorrect:* `COPY --from=0 /app /app` copies the entire `/app` directory from stage 0 — including build tools, source files, and any temporary artifacts. This is not a minimal, secure copy.

---

### Question 4

A Trivy container scan is run with the following command. What happens if the image contains a CRITICAL severity CVE?

```bash
trivy image --exit-code 1 --severity CRITICAL,HIGH myapp:latest
```

- A) Trivy prints a warning message and exits with code 0, allowing the pipeline step to succeed
- B) Trivy exits with code 1, causing the CI/CD pipeline step to fail and blocking the image from being pushed
- C) Trivy automatically removes the vulnerable package from the image and rebuilds it
- D) Trivy sends a notification email to the repository owner but does not affect the pipeline execution

#### Q4 Correct Answer

B — The `--exit-code 1` flag instructs Trivy to exit with a non-zero code when findings at the specified severity level are found. A non-zero exit code causes the CI/CD pipeline step to fail, which blocks downstream jobs (like pushing the image to a registry) from running.

#### Q4 Distractor Analysis

- *Why A is incorrect:* Without `--exit-code 1`, Trivy exits with 0 (success) regardless of findings. The flag changes this behavior so findings cause a non-zero exit.
- *Why C is incorrect:* Trivy is a scanner, not a remediation tool. It cannot modify images or remove packages.
- *Why D is incorrect:* Trivy does not send notifications. Notification of scan failures is handled by the CI/CD platform (GitHub Actions, Jenkins) based on job failure status.

---

### Question 5

What distinguishes a distroless container base image from a `slim` base image in terms of security?

- A) Distroless images contain only the application runtime with no shell, package manager, or standard utilities, providing the smallest possible attack surface
- B) Distroless images run as root by default, which is more secure because it allows the container to manage its own filesystem
- C) Distroless images include a hardened shell that cannot execute arbitrary commands
- D) Distroless images automatically update themselves with security patches, unlike slim images that must be rebuilt

#### Q5 Correct Answer

A — Distroless images contain only the application runtime (e.g., Python interpreter, Java JRE) and its direct dependencies. There is no shell, no `apt`, no `curl`, no standard Unix utilities. This means many attack techniques that require executing shell commands inside the container are not possible.

#### Q5 Distractor Analysis

- *Why B is incorrect:* Distroless images do not run as root by default. Running as root would be the opposite of a security improvement. Non-root is a security best practice regardless of image type.
- *Why C is incorrect:* Distroless images have no shell at all — not a hardened one. The absence of a shell is the security property, not a hardened version of one.
- *Why D is incorrect:* No base image automatically updates itself at runtime. Container images must be rebuilt and redeployed with updated base images to get security patches.

---

### Question 6

Which of the following Docker `CMD` instruction forms is preferred for security and correct signal handling?

- A) `CMD python app.py` (shell form)
- B) `CMD ["/bin/sh", "-c", "python app.py"]` (explicit shell invocation)
- C) `CMD ["python", "app.py"]` (exec form)
- D) `ENTRYPOINT python app.py` (shell form entrypoint)

#### Q6 Correct Answer

C — Exec form passes the command directly to the OS without shell interpretation. The process receives signals (SIGTERM, SIGKILL) directly, enabling graceful shutdown. Shell form wraps the command in `/bin/sh -c`, creating an extra process that may not propagate signals to the application, leading to ungraceful container termination.

#### Q6 Distractor Analysis

- *Why A is incorrect:* Shell form creates a shell process as PID 1, which may not propagate SIGTERM to the actual application process. This can cause containers to hang during shutdown.
- *Why B is incorrect:* Explicitly invoking `/bin/sh -c` has the same problem as shell form — the shell becomes PID 1 and signal propagation may be unreliable.
- *Why D is incorrect:* Shell form ENTRYPOINT has the same signal propagation issue as shell form CMD.

---

### Question 7

A security team audits a production Dockerfile and finds that `EXPOSE 22`, `EXPOSE 3306`, and `EXPOSE 8080` are all declared. The application only serves web traffic on port 8080. What is the security concern?

- A) Exposing multiple ports causes Docker to create multiple container instances automatically
- B) Exposing SSH (port 22) and MySQL (port 3306) in a web application container violates the principle of least privilege and suggests unnecessary services may be present in the image
- C) The `EXPOSE` instruction automatically opens firewall rules on the host, creating network-level vulnerabilities
- D) Docker limits containers to a maximum of two exposed ports, so the third EXPOSE instruction will fail

#### Q7 Correct Answer

B — `EXPOSE 22` suggests SSH may be installed in the container. `EXPOSE 3306` suggests a MySQL server may be running. Neither belongs in an application container. The principle of least privilege applied to containers means exposing only the ports the application actually uses, and installing only the services the application needs.

#### Q7 Distractor Analysis

- *Why A is incorrect:* `EXPOSE` is documentation metadata. It does not create additional container instances.
- *Why C is incorrect:* `EXPOSE` does not configure firewall rules or host networking. It is metadata indicating which ports the container listens on. Actual port publishing requires `-p` or `-P` flags at runtime.
- *Why D is incorrect:* There is no Docker limit on the number of exposed ports per container.

---

### Question 8

A DevSecOps engineer wants to scan a Dockerfile for security misconfigurations before building the image. Which tool is designed for this specific task?

- A) Trivy (using `trivy image` mode)
- B) Hadolint (Dockerfile linter)
- C) Grype (using `grype dir:.` mode)
- D) Semgrep (using OWASP rule set)

#### Q8 Correct Answer

B — Hadolint is a Dockerfile-specific linter that analyzes Dockerfile instructions against security and best-practice rules: detecting `FROM :latest` usage, missing USER directives, shell form CMD, unnecessary packages, and other misconfigurations. It runs before the image is built.

#### Q8 Distractor Analysis

- *Why A is incorrect:* `trivy image` requires a built image to scan. It scans for CVEs in packages within the image, not Dockerfile instruction patterns.
- *Why C is incorrect:* `grype dir:.` scans the filesystem for vulnerable packages but does not analyze Dockerfile instruction security patterns.
- *Why D is incorrect:* Semgrep analyzes application source code for coding vulnerability patterns. It is not designed for Dockerfile security analysis.

---

### Question 9

Which of the following `docker run` flags implements the principle of least privilege for container capabilities?

- A) `--privileged` — grants the container access to all Linux capabilities and host devices
- B) `--cap-drop ALL --cap-add NET_BIND_SERVICE` — removes all capabilities and adds back only what is needed
- C) `--user root` — runs the container as root, which has access to all capabilities by default
- D) `--network host` — gives the container access to the host network stack

#### Q9 Correct Answer

B — `--cap-drop ALL` removes every Linux capability from the container. `--cap-add NET_BIND_SERVICE` adds back only the specific capability required (binding to privileged ports). This implements least privilege: the container has exactly the capabilities it needs and nothing more.

#### Q9 Distractor Analysis

- *Why A is incorrect:* `--privileged` grants maximum capabilities — the opposite of least privilege. Privileged containers can access all host devices and bypass most container isolation.
- *Why C is incorrect:* Running as root (UID 0) grants all capabilities by default. This violates least privilege and maximizes the impact of a container compromise.
- *Why D is incorrect:* `--network host` bypasses network namespace isolation, giving the container direct access to the host network interfaces. This is the opposite of least privilege for networking.

---

### Question 10

A CI/CD pipeline builds a Docker image, scans it with Trivy, and if the scan passes, pushes the image to a container registry. What critical security control is missing between the Trivy scan step and the registry push step?

- A) A manual approval gate requiring a security engineer to review Trivy results before the push proceeds
- B) A Hadolint Dockerfile lint step should run before the build to catch misconfigurations before image creation
- C) The image should be tagged with a content-addressable digest after scanning so the exact scanned image is pushed — not a potentially rebuilt version
- D) A DAST scan should run against the registry to verify the image is stored securely

#### Q10 Correct Answer

B — Hadolint should run against the Dockerfile before the build step, not after. By placing Hadolint in the pre-build pipeline stage, Dockerfile misconfigurations are caught before compute time is spent building a vulnerable image. The correct order is: lint Dockerfile, build image, scan image, push image.

#### Q10 Distractor Analysis

- *Why A is incorrect:* Manual approval gates for every image push do not scale in a DevSecOps pipeline. Automated scanning with enforced thresholds is the correct model for routine deployments.
- *Why C is incorrect:* While image digest tagging is a best practice for reproducibility, it is not the "missing control" in this specific scenario. The described pipeline already scans before pushing.
- *Why D is incorrect:* DAST scans test running applications for runtime vulnerabilities, not registry storage security. Scanning the registry with DAST is not a container security control.
