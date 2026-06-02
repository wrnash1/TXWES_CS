# Reading Guide: Module 05 - Container Orchestration Security: Kubernetes

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 05 introduces Kubernetes container orchestration from a security perspective. Kubernetes is the dominant platform for deploying containerized applications at scale in enterprise DevSecOps environments. Its RBAC model, Security Contexts, Network Policies, and API server security configuration are all heavily tested on the DevSecOps Professional exam. Module 12 covers Kubernetes security in greater depth; this module establishes the foundational concepts.

---

## Section 1: High-Yield Glossary

**Kubernetes (K8s)** — An open-source container orchestration system that automates the deployment, scaling, and management of containerized applications across clusters of machines.

**Pod** — The smallest deployable unit in Kubernetes. A pod contains one or more containers that share a network namespace and storage. Security configurations are applied at the pod and container level.

**Namespace** — A logical partition within a Kubernetes cluster that isolates resources. RBAC Roles and Network Policies are namespace-scoped.

**Control plane** — The Kubernetes components that manage the cluster: API server, etcd, scheduler, and controller manager. The control plane must be hardened and isolated from workload nodes.

**API server** — The central Kubernetes component that processes all REST API requests. Every kubectl command, CI/CD deployment, and controller operation passes through the API server. Its security directly determines cluster security.

**etcd** — The distributed key-value store that holds all Kubernetes cluster state: pod definitions, Secrets, ConfigMaps, RBAC policies, and certificates. Must be encrypted at rest and access-restricted.

**ServiceAccount** — A Kubernetes object representing an identity for processes running in a pod. Pods use ServiceAccounts to authenticate to the Kubernetes API server. CI/CD systems use ServiceAccounts for deployment credentials.

**RBAC (Role-Based Access Control)** — The Kubernetes authorization model. Controls what actions a subject (user, group, or service account) can perform on which API resources.

**Role** — A namespaced Kubernetes RBAC object that defines a set of permissions (allowed API resources and verbs) within a specific namespace.

**ClusterRole** — A cluster-scoped Kubernetes RBAC object that defines permissions across all namespaces and for cluster-level resources.

**RoleBinding** — A Kubernetes object that grants the permissions defined in a Role to a subject within a specific namespace.

**ClusterRoleBinding** — A Kubernetes object that grants a ClusterRole to a subject at the cluster level (all namespaces).

**cluster-admin** — The most privileged built-in ClusterRole in Kubernetes, granting full control over all resources in the cluster. Should never be granted to automated CI/CD service accounts.

**Security Context** — A Kubernetes pod or container specification field that applies Linux security settings: running user/group, read-only root filesystem, capability dropping, seccomp profiles, and privilege escalation prevention.

**seccompProfile** — A Security Context field that enables Linux seccomp (secure computing mode) to filter allowed system calls. `RuntimeDefault` uses the container runtime's default seccomp profile.

**allowPrivilegeEscalation** — A Security Context container field. When set to `false`, prevents the container process from gaining additional privileges through setuid/setgid binaries or Linux capabilities.

**readOnlyRootFilesystem** — A Security Context container field. When set to `true`, mounts the container's root filesystem read-only, preventing filesystem writes by a compromised process.

**Network Policy** — A Kubernetes object that controls ingress and egress traffic between pods. Network Policies are additive (default-allow by default; require explicit default-deny to enforce zero-trust).

**Default-deny Network Policy** — A Network Policy with an empty `podSelector: {}` that selects all pods in a namespace and denies all ingress and egress. Required to enforce network segmentation. Additional policies then explicitly allow required traffic.

**Admission controller** — A Kubernetes component that intercepts API server requests before objects are persisted, enabling policy enforcement: blocking pods that run as root, requiring image scanning results, enforcing resource limits.

**PodSecurityAdmission** — A built-in Kubernetes admission controller (GA in K8s 1.25+) that enforces Pod Security Standards (Privileged, Baseline, Restricted) at the namespace level.

---

## Section 2: Kubernetes RBAC Model Reference

| RBAC Object | Scope | Purpose |
|---|---|---|
| Role | Namespace | Defines permissions (resources + verbs) within one namespace |
| ClusterRole | Cluster-wide | Defines permissions across all namespaces or for cluster resources |
| RoleBinding | Namespace | Grants a Role or ClusterRole to a subject in one namespace |
| ClusterRoleBinding | Cluster-wide | Grants a ClusterRole to a subject across all namespaces |

### RBAC Verb Reference

| Verb | Description |
|---|---|
| get | Read a single named resource |
| list | List all resources of a type |
| watch | Watch for changes to resources |
| create | Create a new resource |
| update | Replace an existing resource |
| patch | Partially modify an existing resource |
| delete | Delete a resource |
| * | All verbs (wildcard — avoid in least-privilege configurations) |

### Principle of Least Privilege for Service Accounts

- CI/CD deployment accounts should have only `update` and `patch` on `deployments`, and `get`/`list` on `pods` — not `cluster-admin`.
- Application pods should have no ServiceAccount token mounted unless they explicitly need to call the Kubernetes API.
- Set `automountServiceAccountToken: false` on pods that do not need cluster API access.

---

## Section 3: Security Context Reference

The following Security Context settings should be applied to all production pods.

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    fsGroup: 1001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: [ALL]
```

| Field | Value | Security Effect |
|---|---|---|
| `runAsNonRoot` | `true` | Blocks pod start if image runs as root |
| `runAsUser` | non-zero UID | Enforces non-root UID for process |
| `allowPrivilegeEscalation` | `false` | Prevents setuid privilege gain |
| `readOnlyRootFilesystem` | `true` | Blocks filesystem writes by compromised process |
| `capabilities.drop` | `[ALL]` | Removes all Linux capabilities |
| `seccompProfile.type` | `RuntimeDefault` | Filters dangerous system calls |

---

## Section 4: Kubernetes vs. Docker Security Model Comparison

| Dimension | Docker (standalone) | Kubernetes |
|---|---|---|
| Access control | Docker daemon socket (root equivalent) | RBAC on API server |
| Secrets management | Docker Secrets (Swarm) or env vars | Kubernetes Secrets (base64, optionally encrypted) |
| Network isolation | Docker network bridges | Network Policies (namespace-scoped) |
| Non-root enforcement | USER directive in Dockerfile | `runAsNonRoot` in Security Context |
| Capability dropping | `--cap-drop ALL` at runtime | `capabilities.drop: [ALL]` in Security Context |
| Audit logging | Docker daemon logs | Kubernetes API server audit logs |
| Policy enforcement | Limited (manual) | Admission controllers, OPA Gatekeeper |

---

## Section 5: Network Policy Reference

### Default-Deny Pattern

Applying a default-deny NetworkPolicy to a namespace blocks all traffic. All required connections must then be explicitly permitted.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

### Allowlist Addition Pattern

After applying default-deny, add explicit allow policies for each required traffic path.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-to-db
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: api
      ports:
        - protocol: TCP
          port: 5432
```

---

## Section 6: CI/CD Pipeline Stage Comparison — Kubernetes Security Controls

| Pipeline Stage | Kubernetes Security Control | Tool / Method |
|---|---|---|
| Container build | Image scanning | Trivy, Grype |
| Pre-deployment | Kubernetes manifest scanning | Checkov, kubesec, kube-score |
| Deployment | Admission controller enforcement | OPA Gatekeeper, Kyverno |
| Runtime | Security Context enforcement | PodSecurityAdmission |
| Runtime | Network policy enforcement | Calico, Cilium, WeaveNet |
| Runtime monitoring | Container behavior anomaly detection | Falco |

---

## Section 7: Kubernetes API Server Security Reference

- Enable RBAC authentication (`--authorization-mode=RBAC`).
- Enable audit logging (`--audit-log-path`, `--audit-policy-file`).
- Restrict API server network access to management and CI/CD networks via firewall rules.
- Disable anonymous authentication (`--anonymous-auth=false`).
- Use TLS for all API server communications.
- Encrypt etcd at rest using the EncryptionConfiguration API.

---

## Section 8: SAST vs. DAST vs. SCA Comparison

| Dimension | SAST | DAST | SCA |
|---|---|---|---|
| Kubernetes equivalent | Manifest linting (kubesec) | Runtime security testing (Falco) | Image dependency scanning (Trivy) |
| Requires running cluster | No | Yes | No |
| Pipeline stage | Pre-deployment | Post-deployment | Pre-deployment |

---

## Section 9: DevSecOps Professional Exam Tips

1. **RBAC objects and their scope** — Know that Roles and RoleBindings are namespaced; ClusterRoles and ClusterRoleBindings are cluster-scoped. The exam frequently presents scenarios where a Role is used where a ClusterRole is needed (or vice versa).

2. **cluster-admin risk** — The exam tests that granting `cluster-admin` to a service account (especially a CI/CD service account) is a critical misconfiguration. Know the least-privilege alternative.

3. **Security Context vs. Dockerfile** — Both enforce non-root execution. `USER` in Dockerfile is image-level. `runAsNonRoot` in Security Context is cluster-enforcement. Both are needed: the Dockerfile sets the default; the Security Context enforces the policy.

4. **Default-deny Network Policy requirement** — Know that Kubernetes does NOT default to deny-all. You must explicitly create a NetworkPolicy with empty `podSelector: {}` to achieve default-deny. Without it, all pods can reach all other pods.

5. **etcd encryption** — Know that Kubernetes Secrets are stored in etcd as base64-encoded data (not encrypted) by default. Encryption at rest requires explicit EncryptionConfiguration. The exam tests this as a common misconfiguration.

6. **automountServiceAccountToken** — Pods automatically mount a ServiceAccount token that can be used to call the Kubernetes API. Set `automountServiceAccountToken: false` for pods that don't need cluster API access.

7. **readOnlyRootFilesystem + emptyDir** — Know that `readOnlyRootFilesystem: true` prevents all filesystem writes. Applications that need writable temp space use a `volumeMount` pointing to an `emptyDir` volume.

8. **Admission controller role** — Admission controllers (OPA Gatekeeper, Kyverno, PodSecurityAdmission) enforce policy at the API server level, preventing non-compliant pods from being created. They are the Kubernetes equivalent of a security gate.

---

## Section 10: Study Checklist

- [ ] List the four Kubernetes RBAC objects and their scope (namespace vs. cluster).
- [ ] Write a minimal RBAC configuration for a CI/CD deployment service account from memory.
- [ ] Explain what `cluster-admin` grants and why it should not be used for service accounts.
- [ ] List five Security Context fields and their security effects.
- [ ] Explain the default-deny Network Policy pattern and why it is required.
- [ ] Explain the difference between base64 encoding and encryption for Kubernetes Secrets.
- [ ] Describe the role of admission controllers in Kubernetes security policy enforcement.
- [ ] Read the OWASP DevSecOps Guideline Kubernetes security section at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
- [ ] Complete the Module 05 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
