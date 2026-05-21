# Reading Guide: Module 12 - Kubernetes Security – RBAC, Network Policies, Pod Security

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 12 - Kubernetes Security – RBAC, Network Policies, Pod Security**! This module covers Kubernetes-specific security controls that govern what containers can do once they are running inside a cluster. You will learn how Role-Based Access Control (RBAC) enforces least-privilege access to the Kubernetes API, how Network Policies restrict pod-to-pod communication to only what is explicitly permitted, and how Pod Security Standards (PSS) control container behavior within namespaces. These controls work alongside the container image scanning and secrets management covered in previous modules to build a defense-in-depth Kubernetes security posture. All three topics are heavily weighted on the CDP exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Container base images**: The foundation layer of a container image, specified in the `FROM` instruction of a Dockerfile. Security-hardened base images (Alpine Linux, Google distroless, Red Hat UBI minimal) contain only the minimum OS components needed to run the application, reducing the package surface area available to an attacker who compromises a pod. Choosing a minimal base image is the first container security decision and affects all subsequent image scans.

* **Image scanning (Trivy)**: The pre-deployment pipeline stage that scans built container images for CVEs in OS packages and application libraries. In a Kubernetes CI/CD pipeline, a Trivy scan job must pass before the image is pushed to the registry and referenced in a Kubernetes deployment manifest. Image scanning catches OS and runtime-level CVEs that SAST and SCA cannot see.

* **Rootless containers**: Containers configured to run all processes as non-root users, enforced by the `runAsNonRoot: true` and `runAsUser: <non-zero UID>` settings in a pod's `securityContext`. Running processes as root inside a container is a critical misconfiguration that can enable privilege escalation and container escape. Kubernetes' Restricted Pod Security Standard requires rootless execution.

* **Registry configurations**: The access control and security settings of the container image registry (GitHub Container Registry, Docker Hub, AWS ECR, Google Artifact Registry) that control who can push images, whether image scanning is enforced at push time, and whether images must be signed before they are pullable by Kubernetes nodes.

---

### 2. Certification Exam Tips

* **RBAC Least Privilege**: The CDP exam tests RBAC configuration deeply. Know that ClusterRoles grant cluster-wide permissions while Roles are namespace-scoped. The principle of least privilege in RBAC means service accounts should only be granted the specific verb+resource permissions needed (e.g., `get` and `list` on `pods` in a specific namespace), never wildcard (`*`) verbs or resources.
* **Network Policy Default Deny**: By default, Kubernetes allows all pod-to-pod communication. A best-practice Kubernetes security configuration adds a default-deny NetworkPolicy to each namespace, then adds explicit allow policies for only the required communication paths. The CDP exam tests knowledge of this default-deny pattern.
* **Pod Security Standards**: Know the three PSS levels: Privileged (no restrictions), Baseline (prevents known privilege escalations), and Restricted (hardened; requires non-root, read-only filesystem, no host namespaces). The exam tests which PSS level applies to which namespace type (system vs. application).
* **Study Resource**: The [Kubernetes RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) and [Network Policies documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/) are the authoritative references — review both alongside the Pod Security Standards docs for comprehensive CDP exam coverage.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [Kubernetes RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) and the [Kubernetes Network Policies documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — the official Kubernetes references for the two most heavily tested Kubernetes security mechanisms on the CDP exam. Focus on Role vs. ClusterRole, RoleBinding vs. ClusterRoleBinding, and the NetworkPolicy `podSelector` and `policyTypes` fields.
* **Required Video**: Watch the Kubernetes security segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — covers running Trivy container scans, configuring pod security contexts, and integrating image scanning into a pipeline that deploys to a Kubernetes cluster.

---

### Lab & Command Integration

In this week's hands-on lab, you will apply Kubernetes security controls by:

* **Run Trivy container scan**: Execute `trivy image --exit-code 1 --severity HIGH,CRITICAL <image>` against a locally built image and record the findings, noting CVE identifiers, affected packages, and fixed versions.
* **Identify high vulnerability counts**: Compare scan results from two base images — a full Ubuntu base versus an Alpine base — and document the difference in total CVE count to illustrate the security benefit of minimal base images.
* **Refactor Dockerfile to use Alpine base image**: Update the `FROM` instruction to use `node:18-alpine` or `python:3.11-alpine`, rebuild the image, re-run the Trivy scan, and verify that the CRITICAL and HIGH finding counts are significantly reduced.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how RBAC, Network Policies, and Pod Security Standards work together as defense-in-depth Kubernetes controls.
* [ ] Read the Kubernetes RBAC documentation at [https://kubernetes.io/docs/reference/access-authn-authz/rbac/](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
* [ ] Read the Kubernetes Network Policies documentation at [https://kubernetes.io/docs/concepts/services-networking/network-policies/](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
* [ ] Watch the Kubernetes security segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the Trivy base image comparison and Alpine refactor in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
