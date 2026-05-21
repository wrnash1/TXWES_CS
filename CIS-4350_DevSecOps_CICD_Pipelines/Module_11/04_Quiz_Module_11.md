# Quiz: Module 11 - Container Image Scanning – Trivy and Grype

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Why should API keys and database passwords never be hardcoded in Git source files or embedded in Docker image layers?

* A) Git's compression reduces performance when storing binary secrets, slowing clone operations
* B) Secrets embedded in image layers are retrievable from the image history even if later deleted in a subsequent layer; secrets in Git history persist across clones and forks indefinitely
* C) Hardcoded secrets cause container startup to fail because Docker validates all environment values at build time
* D) Hardcoded secrets in source files cause linting tools to report formatting warnings that block the CI pipeline
* **Correct Answer:** B) Image layers and Git commits are both permanent and content-addressable — a secret "deleted" in a later layer or commit is still fully recoverable from the earlier layer or commit object.
* **Distractor Analysis:**
  * *Why B is correct:* Docker's layered filesystem preserves all layer data regardless of later `RUN rm` commands. Similarly, `git log` and pack file extraction can recover any previously committed content. The correct approach is to never write secrets to either artifact.
  * *Why A is incorrect:* Git stores all content — binary or text — with equal efficiency using content-addressed pack files. Secret data does not cause meaningful performance degradation.
  * *Why C is incorrect:* Docker does not validate environment variable values at build time or startup for security purposes. Containers with hardcoded secrets start normally — the risk is exposure, not startup failure.
  * *Why D is incorrect:* Linting tools check code style and syntax; they do not inspect the semantic content of string values for credentials. Secret scanning tools (not linters) detect credential patterns.

---

**Question 2**
Which of the following most accurately describes what a container image scanner like Trivy does?

* A) It analyzes the application's Python or JavaScript source code for insecure function calls and injection vulnerabilities before the image is built
* B) It scans the filesystem layers of a built container image, inventorying all installed OS packages and application libraries against vulnerability databases to identify CVEs in the exact versions present in the image
* C) It monitors a running container's system call patterns at runtime to detect exploitation attempts and anomalous behavior
* D) It validates that a Kubernetes pod's YAML manifest complies with the cluster's admission control policies before the pod is scheduled
* **Correct Answer:** B) Container image scanners analyze the actual installed software in a built image — OS packages (apt, rpm), language runtimes, and application dependencies — finding CVEs in the specific versions present, including packages not listed in source dependency manifests.
* **Distractor Analysis:**
  * *Why B is correct:* Trivy decompresses image layers, reads package manager databases (dpkg, rpm, pip, npm) from the layer filesystem, and cross-references installed versions against the NVD, GitHub Advisory Database, and OS vendor advisories.
  * *Why A is incorrect:* Source code analysis is SAST's function. Container image scanning analyzes the packaged image, not the source files. SAST runs before the build; image scanning runs after the build.
  * *Why C is incorrect:* Monitoring running container system calls at runtime is the function of runtime security tools like Falco or seccomp profiles. Image scanning is a pre-deployment static analysis activity.
  * *Why D is incorrect:* Validating pod manifests against admission policies is the function of Kubernetes admission controllers (OPA Gatekeeper, Kyverno). Trivy operates on image artifacts, not Kubernetes manifests.

---

**Question 3**
A team uses the command `trivy image --exit-code 1 --severity CRITICAL myapp:latest` in their CI pipeline. What does this command do, and what happens when Trivy finds a CRITICAL CVE?

* A) Trivy scans only the image metadata (tag and digest) for known-bad signatures and exits with code 1 if the image is on a blocklist
* B) Trivy scans all OS and application packages in `myapp:latest` for CVEs; if any CRITICAL severity vulnerability is found, the command exits with code 1, causing the pipeline step to fail and blocking the image push
* C) Trivy scans only CRITICAL severity CVEs and skips all other severities to improve scan performance; exit code 1 indicates the scan completed successfully
* D) Trivy modifies the image by patching CRITICAL CVEs automatically and exits with code 1 to indicate patches were applied
* **Correct Answer:** B) `--exit-code 1` tells Trivy to exit with a non-zero code when findings at or above `--severity CRITICAL` are detected, which causes the CI pipeline step to fail — preventing the image push job from running.
* **Distractor Analysis:**
  * *Why B is correct:* In a CI/CD pipeline, a non-zero exit code from any step causes the job to fail. By design, `--exit-code 1 --severity CRITICAL` makes Trivy behave as a security gate: the build passes only when no CRITICAL CVEs are present in the image's installed packages.
  * *Why A is incorrect:* Trivy performs full CVE analysis of all installed packages within the image layers, not just metadata inspection. Exit code 1 indicates findings, not a blocklist match.
  * *Why C is incorrect:* `--severity CRITICAL` filters the output report to show only CRITICAL findings but does not skip scanning other severity levels. Exit code 1 indicates findings exist, not successful completion.
  * *Why D is incorrect:* Trivy is a read-only scanning tool; it does not modify images or apply patches. Remediation requires rebuilding the image with a patched base image or updated packages.

---

**Question 4**
A CI/CD pipeline builds a Docker image using `FROM ubuntu:20.04` as the base. A Trivy scan finds 47 CVEs — 3 CRITICAL, 12 HIGH — primarily in OS packages installed by default in Ubuntu 20.04. What is the most effective remediation strategy?

* A) Add `RUN apt-get upgrade -y` to the Dockerfile to update all packages, then re-scan to verify the CRITICAL and HIGH findings are resolved
* B) Change the base image to a minimal alternative (`FROM ubuntu:22.04` with security updates, or `FROM gcr.io/distroless/base-debian12`) to reduce the installed package surface area, then rebuild and re-scan
* C) Suppress all 47 CVEs in the Trivy configuration file so the scan passes and the image can be pushed to the registry
* D) Deploy the image despite the findings, then apply OS patches to running containers after deployment using `docker exec` commands
* **Correct Answer:** B) Switching to a newer, actively maintained base image with security patches applied — or to a minimal/distroless image with far fewer installed packages — reduces both the vulnerability count and the attack surface of every container deployed from this image.
* **Distractor Analysis:**
  * *Why B is correct:* Ubuntu 20.04 is approaching end-of-life and has accumulated unpatched OS CVEs. Moving to Ubuntu 22.04 (with current security updates) or a distroless image eliminates most OS-level CVEs. Combining with `--no-install-recommends` and removing unused packages further minimizes the footprint.
  * *Why A is incorrect:* `apt-get upgrade -y` in the Dockerfile updates packages at image build time, but this is fragile — the same Dockerfile rebuilt a month later may have new CVEs if the base image adds new packages. Pinning to a minimal, known-good base image is more robust.
  * *Why C is incorrect:* Suppressing 47 findings hides real vulnerabilities without fixing them. The containers would still ship vulnerable OS packages, leaving them exploitable.
  * *Why D is incorrect:* Patching running containers with `docker exec` violates the immutable infrastructure principle — patched containers are no longer in a known, version-controlled state, and the patches are lost on container restart. The correct approach is to rebuild the image.

---

**Question 5**
A DevSecOps team wants to ensure that no container image with CRITICAL vulnerabilities is ever pushed to their production registry. Which combination of pipeline controls enforces this requirement end-to-end?

* A) Add a Trivy scan step in the CI pipeline that runs after the image push, reviewing findings as an advisory report
* B) Configure the CI pipeline to run `trivy image --exit-code 1 --severity CRITICAL` before the push step, so the push job only runs if the scan passes; additionally configure the registry to reject image pushes lacking a valid vulnerability scan attestation signed by the CI system
* C) Manually review Trivy reports once per week and remove images that fail from the registry as part of a routine hygiene process
* D) Configure Trivy to scan only the final image stage in multi-stage builds, skipping intermediate builder stages, and accept all findings as informational
* **Correct Answer:** B) Defense in depth: the pipeline gate prevents pushing vulnerable images, and the registry policy rejects unsigned or unscanned images, ensuring no image bypasses both controls.
* **Distractor Analysis:**
  * *Why B is correct:* The pipeline `--exit-code 1` gate is the primary automated control. Registry-level admission (using tools like Cosign image signing and a policy engine) provides a secondary enforcement layer — even if someone tries to push an image directly to the registry outside the pipeline, the policy rejects it without a valid scan attestation signature.
  * *Why A is incorrect:* Running the scan after the push means vulnerable images have already entered the registry and could be deployed before the finding is reviewed. Advisory post-push scanning does not prevent vulnerable images from reaching the registry.
  * *Why C is incorrect:* Weekly manual review is reactive and delayed; vulnerable images could be deployed to production during the window between the push and the review. Automated gates are required for consistent enforcement.
  * *Why D is incorrect:* Treating all findings as informational removes the blocking enforcement that prevents vulnerable images from being pushed. A non-blocking scan provides visibility but not prevention.
