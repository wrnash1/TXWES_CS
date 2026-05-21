# Quiz: Module 04 - Containerization – Docker Security

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Why should pipelines upload validated builds to a secure artifact registry?

* A) To delete local source files and free up developer disk space
* B) To maintain single, unalterable build versions that can be deployed repeatably across target environments
* C) To run automated tests faster by using cached build layers
* D) To bypass software license checks during deployment
* **Correct Answer:** B) Registry repositories host ready-to-deploy, version-controlled binaries, ensuring environment consistency.
* **Distractor Analysis:**
  * *Why B is correct:* A container registry stores a specific, immutable image digest; every deployment pulls the exact same artifact, preventing "works on my machine" inconsistencies and ensuring only scanned, approved images reach production.
  * *Why A is incorrect:* Pushing to a registry does not affect local source files; it makes a build artifact available remotely.
  * *Why C is incorrect:* Layer caching speeds up builds locally; the registry stores finished images, not build caches.
  * *Why D is incorrect:* License compliance is enforced by SCA scanning during the build, not by using a registry.

---

**Question 2**
Which of the following most accurately describes version tagging in a Docker-based CI/CD pipeline?

* A) The process of labeling a container image with a meaningful identifier (such as a Git commit SHA or semantic version) so each build is uniquely traceable and deployments are reproducible
* B) A Git operation that marks a specific commit in the repository history to indicate a release point
* C) A Kubernetes label applied to Pod specifications to control which nodes a container runs on
* D) A Docker Compose option that pins a service to a specific network subnet for security isolation
* **Correct Answer:** A) Tagging container images with commit SHAs or semantic versions links every running container back to the exact source code and pipeline run that produced it, enabling precise rollback and audit trails.
* **Distractor Analysis:**
  * *Why A is correct:* In a CI/CD pipeline, `docker build -t myapp:$GITHUB_SHA` tags the image with the triggering commit SHA; this makes it possible to trace any running container back to its exact build and source revision.
  * *Why B is incorrect:* Git tags mark commits in source history; image version tags annotate container images in a registry. These are related concepts but operate on different artifacts.
  * *Why C is incorrect:* Kubernetes node selector labels control scheduling placement; they are not related to container image versioning.
  * *Why D is incorrect:* Docker Compose network settings control container networking; they are unrelated to image version identification.

---

**Question 3**
A Dockerfile contains the instruction `RUN pip install -r requirements.txt` followed later by `COPY . .`. A developer modifies only a Python source file. What happens to the `pip install` layer in the next build?

* A) Docker re-runs the `pip install` step because any file change invalidates the entire cache
* B) Docker uses the cached `pip install` layer because `requirements.txt` has not changed, and only re-executes steps from the modified `COPY . .` instruction onward
* C) Docker skips all layers and performs a full image rebuild from the base image
* D) Docker deletes the existing image and pulls a fresh copy of the base image before rebuilding
* **Correct Answer:** B) Docker's layer cache reuses the `pip install` layer because neither `requirements.txt` nor earlier instructions changed; only the `COPY . .` layer and anything after it are rebuilt.
* **Distractor Analysis:**
  * *Why B is correct:* Docker invalidates a layer only when its instruction or its inputs change. Since `requirements.txt` is unchanged, the `RUN pip install` layer is served from cache, dramatically speeding up the build.
  * *Why A is incorrect:* Docker does not invalidate the entire cache on any file change; it invalidates only from the first changed layer onward.
  * *Why C is incorrect:* A full rebuild from the base image only occurs if the `FROM` instruction changes or if `--no-cache` is passed explicitly.
  * *Why D is incorrect:* Docker does not delete images or re-pull base images simply because a source file changed; it uses incremental layer rebuilding.

---

**Question 4**
A security review finds that a production Docker container is running all processes as the root user. Why is this a security misconfiguration, and what is the correct fix?

* A) Running as root causes the container to use more memory; fix by reducing the container's CPU limit
* B) Running as root means that if the container process is compromised, the attacker has root-level access within the container and may be able to escape to the host; fix by adding `USER nonroot` to the Dockerfile
* C) Running as root prevents the container from connecting to external networks; fix by adding a network policy
* D) Running as root causes Docker image scans to fail with a false-positive critical vulnerability; fix by suppressing the scanner rule
* **Correct Answer:** B) A root process inside a container that is exploited gives the attacker elevated privileges that may be used for container escape or host compromise; the fix is to create a non-root user in the Dockerfile and switch to it with `USER`.
* **Distractor Analysis:**
  * *Why B is correct:* Containers share the host kernel; a root process inside a container that exploits a kernel vulnerability can break container isolation. Adding `USER 1001` or `USER nonroot` enforces least privilege at the process level.
  * *Why A is incorrect:* Process user context has no direct relationship to memory or CPU consumption; this is not a performance concern.
  * *Why C is incorrect:* Container network connectivity is controlled by Docker network settings and Kubernetes network policies, not by the process user.
  * *Why D is incorrect:* Running as root is a genuine security vulnerability, not a false positive; suppressing the finding would leave the misconfiguration unresolved.

---

**Question 5**
A developer accidentally embeds an AWS access key in a Dockerfile using `ENV AWS_SECRET_KEY=AKIAIOSFODNN7EXAMPLE`. The layer is later removed in a subsequent build. Why does this not fully resolve the security risk, and what is the correct remediation?

* A) The `ENV` instruction only stores the key temporarily during build; it is not retained in the final image, so no remediation is needed
* B) The layer containing the secret is still present in the image history and can be extracted with `docker history --no-trunc`; the correct fix is to never embed secrets in Dockerfile instructions and instead inject them at runtime via a secrets manager or CI environment variable
* C) The risk is resolved automatically when the image is pushed to a private registry with access controls
* D) Docker automatically encrypts all `ENV` values in the image manifest, so the secret cannot be read even if the image is pulled
* **Correct Answer:** B) Docker image layers are immutable; deleting a file or unsetting an ENV in a later layer does not remove the data from the earlier layer, which remains accessible in the image history.
* **Distractor Analysis:**
  * *Why B is correct:* `docker history --no-trunc` and image layer extraction tools can recover values from any layer in the image, including those "removed" by later instructions. Secrets must never enter a Dockerfile; use `--secret` mount at build time or runtime environment injection instead.
  * *Why A is incorrect:* `ENV` instructions write values into the image layer permanently; they are not temporary and persist in the image manifest and history.
  * *Why C is incorrect:* A private registry controls who can pull the image but does not prevent authorized users (or attackers who gain registry access) from reading layer contents including the embedded secret.
  * *Why D is incorrect:* Docker does not encrypt `ENV` values in image layers or manifests; they are stored as plaintext and are readable by anyone with access to the image.
