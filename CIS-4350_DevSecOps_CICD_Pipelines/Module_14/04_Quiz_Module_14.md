# Quiz: Module 14 - Threat Modeling in DevSecOps

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the primary goal of chaos engineering in a DevSecOps program?

* A) To intentionally write disorganized, undocumented code in order to test the team's debugging skills under pressure
* B) To proactively inject controlled failures into production or staging systems to discover weaknesses in resilience and security controls before an unplanned outage exposes them
* C) To reduce network bandwidth consumption by periodically shutting down non-critical services during off-peak hours
* D) To test whether security team members can bypass network firewalls using unconventional attack techniques
* **Correct Answer:** B) Chaos engineering validates that clusters, authentication systems, and security controls degrade gracefully and auto-recover from controlled failures — discovering weaknesses in a safe, controlled experiment rather than during a real incident.
* **Distractor Analysis:**
  * *Why B is correct:* Chaos engineering experiments (inspired by Netflix's Chaos Monkey) deliberately terminate instances, inject latency, and simulate resource exhaustion to validate that resilience mechanisms work as designed. From a security perspective, this includes verifying that fallback authentication paths are secure, secrets rotation fires on node failure, and access control remains enforced during degraded states.
  * *Why A is incorrect:* Writing disorganized code is a code quality problem, not an engineering discipline. Chaos engineering operates on running infrastructure, not on code quality or documentation.
  * *Why C is incorrect:* Shutting down services to save bandwidth describes capacity management, not chaos engineering. Chaos experiments are scientific: they have hypotheses, defined blast radii, and clear rollback procedures.
  * *Why D is incorrect:* Security team members attempting to bypass firewalls describes penetration testing or red team exercises, not chaos engineering. Chaos engineering focuses on infrastructure resilience, not adversarial security testing.

---

**Question 2**
Which of the following most accurately describes resilience testing in the context of DevSecOps security controls?

* A) The process of testing whether an application's UI remains visually consistent when browser font sizes are changed
* B) Systematic validation that security controls — authentication, secrets delivery, authorization enforcement — continue to function correctly and fail safely when underlying infrastructure components fail or degrade
* C) The practice of testing application performance under high user load to determine the maximum transaction throughput
* D) A code review process where a senior developer systematically validates that all functions handle null input without crashing
* **Correct Answer:** B) Security resilience testing validates that security controls do not introduce single points of failure — for example, testing what happens to access control when the identity provider is temporarily unavailable.
* **Distractor Analysis:**
  * *Why B is correct:* A security control that fails open (grants access when unavailable) is just as dangerous as one that is misconfigured. Resilience testing of security controls verifies that they fail closed (deny access when degraded) and recover automatically without requiring manual intervention.
  * *Why A is incorrect:* UI visual consistency across font sizes is a front-end compatibility or accessibility testing concern. Resilience testing focuses on infrastructure failure modes, not presentation layer behavior.
  * *Why C is incorrect:* Load testing determines maximum throughput and performance limits — this is performance engineering. Resilience testing focuses on failure mode behavior and recovery, not peak capacity.
  * *Why D is incorrect:* Null input handling is a unit testing or defensive programming concern within a code review. Resilience testing operates at the infrastructure and system level, testing how the overall system responds to component failures.

---

**Question 3**
A threat model for a web application's login system identifies the threat: "An attacker submits a forged JWT with a modified payload claiming to be an administrator." Which STRIDE threat category does this represent, and what mitigation addresses it?

* A) Denial of Service — mitigated by rate limiting JWT validation requests to prevent token exhaustion attacks
* B) Elevation of Privilege — mitigated by cryptographically verifying the JWT signature using the signing key on the server side before trusting any claims in the payload
* C) Information Disclosure — mitigated by encrypting the JWT payload using AES-256 so the attacker cannot read role claims
* D) Tampering — mitigated by requiring all JWT tokens to expire within 24 hours to limit the window of exploitation
* **Correct Answer:** B) Forging a JWT to claim elevated privileges is an Elevation of Privilege attack. The mitigation is server-side signature verification — a token signed with the wrong key or a modified payload will fail verification and be rejected.
* **Distractor Analysis:**
  * *Why B is correct:* JWT signature verification ensures that only tokens signed by the trusted private key are accepted. An attacker who modifies the payload (to change a `role` claim from `user` to `admin`) will produce a token with an invalid signature, which the server rejects. Using RS256 or ES256 (asymmetric signing) is more secure than HS256 (shared secret).
  * *Why A is incorrect:* Rate limiting addresses Denial of Service by limiting request frequency; it does not prevent a single forged token from being accepted if signature verification is not enforced.
  * *Why C is incorrect:* Encrypting the JWT payload (JWE) addresses Information Disclosure by hiding the claim contents. However, encryption alone does not prevent forgery — an attacker could still submit a crafted token with a new encrypted payload if they have the encryption key.
  * *Why D is incorrect:* Token expiration limits the time window for a leaked, legitimate token to be misused. It does not prevent a forged token (which an attacker creates themselves, potentially with any expiry they choose) from being accepted if signature verification is missing.

---

**Question 4**
During a threat modeling session for a CI/CD pipeline, the team identifies the following threat: "A malicious actor gains write access to the pipeline's GitHub Actions workflow YAML file and inserts a step that exfiltrates secrets from the runner's environment." Which mitigation best addresses this threat?

* A) Encrypt all secrets stored in GitHub Actions Secrets with an additional application-layer AES key managed by the team
* B) Enable branch protection rules on the repository requiring code owner review and approval for any changes to files in `.github/workflows/`, combined with CODEOWNERS enforcement and required status checks
* C) Move all CI/CD pipeline definitions to a private repository that only the security team can read
* D) Add a pipeline step at the end of every workflow that deletes all environment variables from the runner after the job completes
* **Correct Answer:** B) Branch protection with CODEOWNERS review on workflow files prevents unauthorized modification of pipeline definitions — a change to `.github/workflows/` requires explicit approval from designated owners before it can be merged.
* **Distractor Analysis:**
  * *Why B is correct:* CODEOWNERS allows the team to designate specific reviewers who must approve changes to security-sensitive files. Branch protection's required reviews and status checks ensure no workflow change can be merged without human review by authorized personnel, directly mitigating the threat of unauthorized pipeline modification.
  * *Why A is incorrect:* Double-encrypting secrets stored in GitHub Actions Secrets does not prevent a malicious workflow step from reading those secrets at runtime — GitHub injects secrets as environment variables when the job runs, so a malicious step executes with the same access as a legitimate step.
  * *Why C is incorrect:* Moving pipeline definitions to a private repository does not prevent the threat if the attacker has write access to that private repository. Access control alone does not enforce review requirements.
  * *Why D is incorrect:* Deleting environment variables at the end of the workflow does not prevent a malicious step earlier in the workflow from exfiltrating them. The exfiltration would already have occurred before the cleanup step runs.

---

**Question 5**
A team performs a threat model of their container deployment pipeline using a Data Flow Diagram. They identify a trust boundary crossing where the CI/CD runner pushes a built Docker image to a container registry that is then pulled by Kubernetes nodes. Which threat and mitigation pair is most relevant to this trust boundary?

* A) Threat: The registry runs out of disk space and cannot store new images. Mitigation: Implement registry garbage collection to remove old images periodically.
* B) Threat: A compromised CI system or supply chain attack inserts malicious code into an image that Kubernetes then deploys. Mitigation: Implement image signing (Cosign) in the CI pipeline and configure Kubernetes to verify image signatures via an admission webhook before allowing pods to run.
* C) Threat: Network latency between the registry and Kubernetes nodes slows pod startup times. Mitigation: Deploy a registry mirror within the same cloud region as the Kubernetes cluster.
* D) Threat: Kubernetes nodes pull images too frequently, increasing registry bandwidth costs. Mitigation: Set `imagePullPolicy: IfNotPresent` on all pod specifications to use locally cached images.
* **Correct Answer:** B) The trust boundary between CI and the registry, and between the registry and Kubernetes, is a supply chain attack surface. Image signing in the CI pipeline and signature verification at Kubernetes admission enforces that only pipeline-built, verified images are deployed.
* **Distractor Analysis:**
  * *Why B is correct:* This trust boundary is where a supply chain attack (SolarWinds-style) would inject a malicious image into the deployment path. Image signing with Cosign creates a cryptographic attestation that the image was produced by the authorized CI system; Kubernetes admission verification ensures only signed, trusted images are scheduled.
  * *Why A is incorrect:* Registry disk capacity is an operational availability concern, not a security threat at a trust boundary. Disk management does not address integrity or authenticity of images.
  * *Why C is incorrect:* Network latency is a performance concern. Trust boundaries in threat modeling focus on security properties (authentication, integrity, authorization), not network performance.
  * *Why D is incorrect:* Image pull frequency and bandwidth cost are operational optimization concerns. `imagePullPolicy: IfNotPresent` actually reduces security by allowing stale cached images to run without pulling updated, patched versions.
