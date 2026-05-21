# Quiz: Module 12 - Kubernetes Security – RBAC, Network Policies, Pod Security

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Which base image choice minimizes the vulnerability footprint of a container deployed to a Kubernetes cluster?

* A) Ubuntu Desktop 22.04 — includes a full desktop environment for debugging convenience
* B) Alpine Linux (minimal) — a ~5MB distribution with musl libc, BusyBox, and no unnecessary packages
* C) Windows Server Core — provides full .NET Framework and COM support for enterprise applications
* D) Debian Bullseye (full install) — includes all standard Debian packages for maximum compatibility
* **Correct Answer:** B) Alpine is a lightweight Linux distribution containing minimal binaries, reducing the CVE attack surface and the number of packages an attacker can exploit if they compromise the pod.
* **Distractor Analysis:**
  * *Why B is correct:* Alpine's minimal footprint means fewer installed packages, which means fewer CVEs in a Trivy scan. The distroless base image approach (Google distroless, Chainguard) goes even further — no shell or package manager — but Alpine is the standard minimal base for most workloads.
  * *Why A is incorrect:* Ubuntu Desktop includes a graphical interface, office tools, and hundreds of additional packages with no relevance to server workloads — dramatically increasing the CVE surface without any security benefit.
  * *Why C is incorrect:* Windows Server Core is appropriate only for Windows-native .NET workloads. For most Linux-based applications running in Kubernetes, it provides no benefit and a far larger attack surface than Linux minimal images.
  * *Why D is incorrect:* A full Debian install includes thousands of packages that have no place in a production container — each package is a potential CVE. Minimal images (slim, alpine, distroless) are always preferred for security.

---

**Question 2**
Which of the following most accurately describes container image scanning with Trivy in the context of a Kubernetes deployment pipeline?

* A) A runtime monitoring tool that watches Kubernetes pod system calls and alerts on anomalous behavior during execution
* B) A pre-deployment analysis step that scans the built container image's installed OS packages and application libraries against CVE databases, blocking the image push if critical vulnerabilities are found
* C) A Kubernetes admission controller that validates pod YAML manifests against RBAC policies before pods are scheduled on nodes
* D) A network traffic analyzer that inspects inter-pod HTTP requests for SQL injection or XSS payloads at runtime
* **Correct Answer:** B) Container image scanning with Trivy runs in the CI pipeline after the image is built and before it is pushed, inventorying all packages in the image layers and checking for known CVEs.
* **Distractor Analysis:**
  * *Why B is correct:* Trivy performs static analysis of image layers — it reads package databases from the image filesystem (apt lists, pip metadata, npm lock files) and cross-references installed versions against NVD, OSV, and vendor advisories. The `--exit-code 1` flag makes it a blocking pipeline gate.
  * *Why A is incorrect:* Runtime system call monitoring is the function of tools like Falco, which uses eBPF/seccomp to detect anomalous container behavior during execution. Trivy is a pre-deployment scanning tool.
  * *Why C is incorrect:* Kubernetes admission controllers (OPA Gatekeeper, Kyverno) validate resource manifests at API submission time. Trivy operates on container image artifacts, not Kubernetes YAML manifests.
  * *Why D is incorrect:* Runtime network traffic analysis for injection attacks is a web application firewall or service mesh function. Trivy does not analyze HTTP traffic.

---

**Question 3**
A Kubernetes security audit finds that all service accounts in a namespace have been granted a `ClusterRoleBinding` to the `cluster-admin` ClusterRole. Why is this a critical misconfiguration, and what is the correct remediation?

* A) `cluster-admin` bindings slow down Kubernetes API server response times; fix by creating a separate API server for high-privilege service accounts
* B) Granting `cluster-admin` to all service accounts violates least privilege — a compromised pod can use its service account token to take full control of the entire cluster; fix by creating namespace-scoped Roles with only the specific verbs and resources each service account needs
* C) `cluster-admin` ClusterRoleBindings are not supported in Kubernetes versions above 1.20; fix by upgrading to the new RBAC model
* D) `cluster-admin` access causes pod-to-pod network traffic to bypass NetworkPolicy rules; fix by adding default-deny NetworkPolicies to each namespace
* **Correct Answer:** B) `cluster-admin` grants unrestricted access to every resource in the cluster. If any pod with a `cluster-admin`-bound service account is compromised, the attacker gains full cluster control — read secrets, deploy arbitrary workloads, delete namespaces.
* **Distractor Analysis:**
  * *Why B is correct:* Kubernetes RBAC least privilege means each service account should have only the specific permissions it needs — for example, `get` and `list` on `pods` in a single namespace for a monitoring service. Fine-grained namespace-scoped Roles replace the overpermissive ClusterRoleBinding.
  * *Why A is incorrect:* RBAC role bindings have no measurable effect on API server response times. This is a security concern, not a performance issue.
  * *Why C is incorrect:* `ClusterRoleBinding` to `cluster-admin` is fully supported in all Kubernetes versions; the issue is the security misconfiguration of over-permissioning, not a version compatibility problem.
  * *Why D is incorrect:* RBAC and NetworkPolicies are independent control planes — RBAC governs Kubernetes API access, while NetworkPolicies govern pod network communication. An RBAC misconfiguration does not affect NetworkPolicy enforcement.

---

**Question 4**
A Kubernetes NetworkPolicy is applied to a namespace with the following specification: `podSelector: {}` and `policyTypes: [Ingress, Egress]` with no `ingress` or `egress` rules defined. What is the effect of this policy?

* A) No effect — a NetworkPolicy with an empty `podSelector` matches no pods, so no traffic is affected
* B) All ingress and egress traffic to and from all pods in the namespace is denied by default, because no allow rules are defined and the policy selects all pods
* C) All ingress traffic is denied, but all egress traffic is permitted because `Egress` is listed without explicit deny rules
* D) The policy enables cluster-admin access for the namespace's service accounts, overriding existing RBAC bindings
* **Correct Answer:** B) An empty `podSelector: {}` selects all pods in the namespace. With `policyTypes: [Ingress, Egress]` and no allow rules, this creates a default-deny-all policy — all incoming and outgoing traffic is blocked unless overridden by another NetworkPolicy with explicit allow rules.
* **Distractor Analysis:**
  * *Why B is correct:* In Kubernetes NetworkPolicy, an empty `podSelector` (`{}`) means "select all pods in this namespace." Listing a `policyType` with no corresponding rules creates an implicit deny for that traffic direction. This is the standard implementation of a default-deny posture, followed by explicit allow policies for required communication paths.
  * *Why A is incorrect:* An empty `podSelector: {}` does not match "no pods" — it matches "all pods in the namespace." This is a critical distinction in Kubernetes NetworkPolicy syntax.
  * *Why C is incorrect:* NetworkPolicy does not distinguish between permitting egress by default when listed in `policyTypes`. Listing `Egress` in `policyTypes` without egress rules means all egress is denied (default deny), not permitted.
  * *Why D is incorrect:* NetworkPolicy controls pod network communication. It has no relationship to RBAC or service account permissions. These are entirely separate Kubernetes control mechanisms.

---

**Question 5**
A pod specification includes the following security context: `securityContext: { runAsRoot: true, privileged: true, allowPrivilegeEscalation: true }`. A Kubernetes cluster enforcing the Restricted Pod Security Standard rejects this pod. Which corrected security context configuration would satisfy the Restricted PSS requirements?

* A) `securityContext: { runAsNonRoot: true, runAsUser: 1001, allowPrivilegeEscalation: false, readOnlyRootFilesystem: true, seccompProfile: { type: RuntimeDefault } }`
* B) `securityContext: { runAsRoot: false, privileged: false }` — removing the explicit `true` values is sufficient to satisfy the Restricted profile
* C) `securityContext: { capabilities: { add: ["NET_ADMIN", "SYS_PTRACE"] } }` — adding named capabilities satisfies the Restricted profile's explicit permission model
* D) Remove the `securityContext` block entirely — pods without a defined security context are automatically assigned the Restricted profile settings by Kubernetes
* **Correct Answer:** A) The Restricted PSS requires `runAsNonRoot: true`, a non-zero `runAsUser`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, and a seccomp profile — all specified in option A.
* **Distractor Analysis:**
  * *Why A is correct:* The Kubernetes Restricted Pod Security Standard mandates each of these settings. Together they enforce least-privilege execution: the container process cannot escalate to root, cannot write to the root filesystem (preventing modification of system files), and is subject to a system-call filter via the seccomp profile.
  * *Why B is incorrect:* Simply setting boolean values to `false` is not sufficient. The Restricted profile requires explicit presence of specific security context fields (`runAsNonRoot: true`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, seccomp). A missing field is treated as a violation, not as a permissive default.
  * *Why C is incorrect:* The Restricted profile requires dropping ALL capabilities and permits no capability additions. Adding `NET_ADMIN` or `SYS_PTRACE` explicitly violates the Restricted profile by granting elevated privileges.
  * *Why D is incorrect:* Kubernetes does not automatically assign Restricted profile security context settings to pods that lack a `securityContext`. A missing `securityContext` means Kubernetes applies no security constraints, which is equivalent to running with the Privileged profile defaults.
