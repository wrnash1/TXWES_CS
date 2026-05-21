# Quiz: Module 05 - Container Orchestration Security – Kubernetes

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the primary security benefit of using multi-stage builds in a Dockerfile for a Kubernetes deployment?

* A) It allows the container to listen on multiple network ports simultaneously
* B) It produces a minimal final image containing only the runtime artifact, without build tools that could be used by an attacker who compromises the pod
* C) It automatically encrypts all data written to the container's filesystem at rest
* D) It eliminates the need for a base image, making the container completely isolated from the host OS

* **Correct Answer:** B) Multi-stage builds allow compiler tools to run in early stages, copying only the final binary to a lean deployment image, reducing the attack surface available inside a running pod.
* **Distractor Analysis:**
  * *Why B is correct:* When a pod is compromised, an attacker uses tools already present in the container (bash, curl, apt) to pivot. A distroless or Alpine final stage eliminates those tools, making post-exploitation significantly harder.
  * *Why A is incorrect:* Port exposure is controlled by `EXPOSE` instructions and Kubernetes Service definitions; multi-stage builds have no effect on port multiplexing.
  * *Why C is incorrect:* Multi-stage builds affect image composition, not filesystem encryption. Encryption at rest is handled by the container runtime or storage class, not the Dockerfile build process.
  * *Why D is incorrect:* Even distroless images use a minimal base image (`FROM gcr.io/distroless/base`); there is always a base layer. The `FROM scratch` pattern creates a truly baseless image but is only usable for statically compiled binaries.

---

**Question 2**
Which of the following most accurately describes the Dockerfile syntax instruction `FROM node:18-alpine AS builder`?

* A) It imports an external npm package named `node` and aliases it as `builder` for use in subsequent steps
* B) It begins a named multi-stage build stage using the `node:18-alpine` image as the base, allowing later stages to copy artifacts from this stage with `COPY --from=builder`
* C) It defines a Kubernetes init container that runs before the main application container starts in a pod
* D) It sets the container's runtime user to a non-root account named `builder` for least-privilege execution
* **Correct Answer:** B) The `AS builder` alias names this build stage so that a subsequent `FROM` stage can selectively copy only the compiled output using `COPY --from=builder /app/dist /app/dist`.
* **Distractor Analysis:**
  * *Why B is correct:* Multi-stage build syntax uses `FROM image AS name` to label a stage; `COPY --from=name` in a later stage references only the artifacts from that named stage, keeping the final image minimal.
  * *Why A is incorrect:* `FROM` is a Dockerfile instruction, not a package import mechanism. npm packages are installed with `RUN npm install`, not `FROM`.
  * *Why C is incorrect:* Kubernetes init containers are defined in Pod specifications under `initContainers:`; they are not defined inside a Dockerfile.
  * *Why D is incorrect:* The runtime user is set with the `USER` instruction; `AS builder` is purely a stage naming mechanism and has no effect on process permissions.

---

**Question 3**
A Kubernetes cluster enforces the "Restricted" Pod Security Standard profile. Which of the following container configurations would be blocked by this policy?

* A) A container using a read-only root filesystem with `securityContext.readOnlyRootFilesystem: true`
* B) A container running as a specific non-root UID with `runAsUser: 1001` and `runAsNonRoot: true`
* C) A container running as root (`runAsUser: 0`) without a `securityContext` defined
* D) A container with resource limits defined for CPU and memory in the pod spec
* **Correct Answer:** C) The Kubernetes Restricted profile explicitly prohibits containers from running as root and requires `runAsNonRoot: true` and a non-zero UID; a container without these security context settings would be blocked.
* **Distractor Analysis:**
  * *Why C is correct:* The Restricted profile requires `runAsNonRoot: true`, disallows privilege escalation, requires a read-only root filesystem, and demands explicit seccomp profiles. Running as root violates the most basic Restricted requirement.
  * *Why A is incorrect:* A read-only root filesystem is required by the Restricted profile, not prohibited — this configuration would be allowed and encouraged.
  * *Why B is incorrect:* Running as a non-root UID satisfies the Restricted profile's `runAsNonRoot: true` requirement; this configuration would be permitted.
  * *Why D is incorrect:* Defining resource limits is a best practice and is required by the Restricted profile (to prevent resource exhaustion); it would not be blocked.

---

**Question 4**
In a CI/CD pipeline that builds and deploys container images to Kubernetes, a security scan discovers a critical CVE in the base image. The pipeline is configured with a security gate that fails the build on critical findings. What is the correct DevSecOps response?

* A) Suppress the CVE finding in the scanner configuration and re-run the pipeline so the deployment can proceed on schedule
* B) Override the pipeline gate manually and deploy the image, planning to update the base image in the next sprint
* C) Update the `FROM` instruction in the Dockerfile to a patched base image version, rebuild, re-scan, and deploy only after the scan passes with no critical findings
* D) Add a Kubernetes network policy to block all ingress traffic to the affected pods as a permanent mitigation
* **Correct Answer:** C) The correct DevSecOps response is to update the base image to a version with the CVE patched, rebuild the image, and allow the pipeline's security gate to validate the fix before deployment.
* **Distractor Analysis:**
  * *Why C is correct:* Updating the base image and re-scanning is the root-cause fix. The pipeline gate exists precisely for this scenario — it should be respected, not bypassed, to maintain security assurance.
  * *Why A is incorrect:* Suppressing a critical CVE removes visibility of the risk without fixing it; this is a security antipattern that defeats the purpose of scanning.
  * *Why B is incorrect:* Manually overriding the pipeline gate breaks the security assurance chain and sets a precedent for bypassing controls. Deferring a critical vulnerability to the next sprint is an unacceptable risk posture.
  * *Why D is incorrect:* A network policy restricts traffic to the pod but does not address the exploitable CVE within the container image. This is a compensating control, not a remediation.

---

**Question 5**
A DevSecOps team wants every container image deployed to their Kubernetes cluster to have been built and scanned by the CI pipeline — not manually built and pushed by developers. Which combination of controls enforces this requirement?

* A) Require developers to sign a policy acknowledging they will not push manual images, and rely on periodic audit reviews
* B) Configure the container registry to accept pushes only from the CI service account, and configure Kubernetes admission control to reject images without a valid pipeline scan signature
* C) Enable Docker Content Trust on developer workstations to prevent unsigned pushes to the registry
* D) Add a comment to the `Jenkinsfile` documenting that manual pushes are prohibited, and monitor the registry for anomalies
* **Correct Answer:** B) Restricting registry write access to the CI service account prevents manual pushes, while admission control (e.g., Cosign + policy controller) rejects unsigned or unscanned images from being deployed to the cluster.
* **Distractor Analysis:**
  * *Why B is correct:* This is a defense-in-depth approach: the registry access control prevents unauthorized pushes, and the Kubernetes admission webhook enforces that only pipeline-signed images are scheduled — no manual image can bypass both controls.
  * *Why A is incorrect:* Policy acknowledgements and periodic audits are detective and administrative controls; they do not technically prevent a developer from pushing a manual image.
  * *Why C is incorrect:* Docker Content Trust on developer workstations controls signing on push from those machines but does not prevent a developer from pushing a manually built, unsigned image to a registry that accepts unsigned content.
  * *Why D is incorrect:* Documentation and monitoring are advisory and detective controls; they do not enforce the requirement at the technical enforcement layer.
