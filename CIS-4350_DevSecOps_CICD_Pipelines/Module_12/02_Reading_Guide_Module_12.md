# Reading Guide: Module 12 — Kubernetes Security: RBAC, Network Policies, and Pod Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 12 covers Kubernetes cluster security — the controls that govern who can call the Kubernetes API, how pods communicate with each other, and what a container process is permitted to do at runtime. Securing a Kubernetes cluster requires four complementary controls: Role-Based Access Control (RBAC), Network Policies, Security Contexts, and the PodSecurity admission controller. This module also covers how to scan Kubernetes manifests in CI using Checkov to catch misconfigurations before they reach the cluster.

---

## Section 1: High-Yield Glossary

**Role-Based Access Control (RBAC)** — A Kubernetes access control mechanism that grants permissions to API resources based on roles assigned to subjects (users, groups, service accounts).

**Role** — A namespaced RBAC object that defines a set of permissions (verbs on API resources) within a single namespace.

**ClusterRole** — An RBAC object that defines permissions cluster-wide, or grants permissions to cluster-scoped resources. Can also be bound within a namespace via RoleBinding.

**RoleBinding** — Grants a Role or ClusterRole to a subject within a specific namespace.

**ClusterRoleBinding** — Grants a ClusterRole to a subject across the entire cluster.

**ServiceAccount** — A Kubernetes identity for processes running in pods. Used by CI/CD pipeline jobs and application workloads to authenticate to the Kubernetes API.

**Least privilege (RBAC)** — The principle that a service account should have exactly the permissions needed for its function and nothing more. For CI/CD pipelines: Deployments, Services, ConfigMaps in the deployment namespace only.

**`cluster-admin`** — The built-in Kubernetes ClusterRole that grants full control over all resources. Should never be assigned to CI/CD service accounts or application workloads.

**Network Policy** — A Kubernetes resource that defines allowed ingress and egress traffic for pods matching a `podSelector`. Traffic not explicitly allowed is denied when a policy applies.

**Default-deny policy** — A Network Policy with an empty `podSelector: {}` and `policyTypes: [Ingress, Egress]` but no rules, which blocks all traffic to and from all pods in the namespace.

**CNI plugin** — Container Network Interface plugin, which implements Network Policy enforcement. Calico, Cilium, and Weave Net enforce Network Policies; Flannel does not.

**Security Context** — Fields in a pod or container spec that configure runtime security properties: UID, root prevention, privilege escalation, filesystem mutability, and Linux capabilities.

**`runAsNonRoot: true`** — Security Context field that prevents the kubelet from starting the container if the process would run as UID 0.

**`allowPrivilegeEscalation: false`** — Security Context field that sets the `no_new_privs` flag, preventing SUID binaries from escalating privileges.

**`readOnlyRootFilesystem: true`** — Security Context field that mounts the container filesystem read-only, preventing runtime writes and fileless malware.

**`capabilities.drop: ALL`** — Security Context field that removes all Linux capabilities from the container. The most restrictive capability setting.

**`emptyDir` volume** — A temporary volume type that provides a writable scratch directory for containers with `readOnlyRootFilesystem: true`. Data is deleted when the pod terminates.

**PodSecurity admission controller** — A Kubernetes admission controller that enforces one of three security profiles (privileged, baseline, restricted) for pods in a namespace, based on namespace labels.

**PodSecurity profiles** — Three levels: `privileged` (no restrictions), `baseline` (blocks most dangerous privilege escalations), `restricted` (enforces full Security Context hardening including `runAsNonRoot` and `allowPrivilegeEscalation: false`).

**PodSecurity modes** — Three enforcement modes applied via namespace labels: `enforce` (reject non-compliant pods), `warn` (allow but return warning), `audit` (log violation, do not block).

**CKV_K8S_*** — Checkov check IDs for Kubernetes manifest policy violations. Examples: CKV_K8S_6 (hostPID), CKV_K8S_8 (readOnlyRootFilesystem), CKV_K8S_15 (non-root), CKV_K8S_20 (no privilege escalation).

---

## Section 2: RBAC Object Hierarchy

| Object | Scope | Purpose |
|---|---|---|
| ServiceAccount | Namespace | Identity for pod processes and CI/CD jobs |
| Role | Namespace | Permission set for resources in one namespace |
| ClusterRole | Cluster | Permission set for cluster-wide or all-namespace access |
| RoleBinding | Namespace | Assigns a Role or ClusterRole to a subject within a namespace |
| ClusterRoleBinding | Cluster | Assigns a ClusterRole to a subject across the entire cluster |

---

## Section 3: RBAC Verbs Reference

| Verb | HTTP Method | Description |
|---|---|---|
| `get` | GET | Read a single resource |
| `list` | GET (collection) | Read all resources of a type |
| `create` | POST | Create a new resource |
| `update` | PUT | Replace an existing resource |
| `patch` | PATCH | Partially update a resource |
| `delete` | DELETE | Remove a resource |
| `watch` | GET (stream) | Watch for resource changes |

For a CI/CD deployment service account, the minimum verbs needed are `get`, `list`, `create`, `update`, and `patch` on Deployments, Services, and ConfigMaps in the deployment namespace.

---

## Section 4: Network Policy Design Patterns

| Pattern | Purpose | Key Field |
|---|---|---|
| Default deny all | Block all traffic; allowlist from scratch | `podSelector: {}` with no rules |
| Allow specific ingress | Permit traffic from labeled pods to this pod | `ingress.from.podSelector` |
| Allow namespace ingress | Permit traffic from a specific namespace | `ingress.from.namespaceSelector` |
| Allow external egress | Permit pods to reach external services | `egress.to` with `ipBlock` |
| Allow DNS egress | Permit pods to resolve DNS (UDP 53) | `egress.ports.port: 53, protocol: UDP` |

Note: A default-deny policy that blocks egress will also block DNS resolution. Always add an explicit DNS egress allow policy when applying default-deny-egress.

---

## Section 5: Security Context Fields Reference

| Field | Level | Effect |
|---|---|---|
| `runAsNonRoot: true` | Pod or container | Kubelet rejects container if UID = 0 |
| `runAsUser: 1000` | Pod or container | Sets process UID explicitly |
| `fsGroup: 2000` | Pod | Sets GID for volume ownership |
| `allowPrivilegeEscalation: false` | Container | Sets `no_new_privs`; blocks SUID escalation |
| `readOnlyRootFilesystem: true` | Container | Mounts container FS read-only |
| `capabilities.drop: [ALL]` | Container | Removes all Linux capabilities |
| `capabilities.add: [NET_BIND_SERVICE]` | Container | Adds back specific capabilities after dropping all |
| `privileged: false` | Container | Prevents privileged container mode |
| `seccompProfile.type: RuntimeDefault` | Pod | Applies default seccomp syscall filter |

---

## Section 6: PodSecurity Profiles Comparison

| Control | Privileged | Baseline | Restricted |
|---|---|---|---|
| Host namespaces (hostPID, hostIPC, hostNetwork) | Allowed | Blocked | Blocked |
| Privileged containers | Allowed | Blocked | Blocked |
| HostPath volumes | Allowed | Blocked | Blocked |
| Dangerous capabilities (SYS_ADMIN, NET_ADMIN) | Allowed | Blocked | Blocked |
| runAsNonRoot required | No | No | Yes |
| allowPrivilegeEscalation: false required | No | No | Yes |
| Seccomp profile required | No | No | RuntimeDefault or Localhost |
| Drop all capabilities required | No | No | Yes |

---

## Section 7: Checkov Kubernetes Check IDs

| Check ID | Policy | Remediation |
|---|---|---|
| CKV_K8S_6 | hostPID: false | Remove `hostPID: true` from pod spec |
| CKV_K8S_8 | readOnlyRootFilesystem: true | Add `readOnlyRootFilesystem: true` to container securityContext |
| CKV_K8S_11 | CPU limits set | Add `resources.limits.cpu` |
| CKV_K8S_12 | CPU requests set | Add `resources.requests.cpu` |
| CKV_K8S_13 | Memory limits set | Add `resources.limits.memory` |
| CKV_K8S_14 | Memory requests set | Add `resources.requests.memory` |
| CKV_K8S_15 | Non-root container | Add `runAsNonRoot: true` to securityContext |
| CKV_K8S_20 | allowPrivilegeEscalation: false | Add `allowPrivilegeEscalation: false` to securityContext |
| CKV_K8S_28 | No added capabilities | Remove `capabilities.add` entries |
| CKV_K8S_30 | Non-root user | Set `runAsUser` to non-zero value |
| CKV_K8S_37 | Minimize capability additions | Only add capabilities that are strictly required |

---

## Section 8: CI/CD Pipeline RBAC Anti-Patterns

| Anti-Pattern | Risk | Correct Pattern |
|---|---|---|
| `cluster-admin` for CI/CD service account | Full cluster compromise if pipeline is breached | Scoped Role for deployment namespace only |
| Using `default` service account for pipeline | Application pods inherit pipeline permissions | Dedicated `ci-deployer` ServiceAccount |
| ClusterRoleBinding for deployment access | Pipeline can access all namespaces | RoleBinding in deployment namespace only |
| Hardcoded kubeconfig in pipeline secrets | Credential rotation requires secret update | OIDC federation with short-lived tokens |
| Granting Secrets `get` permission to pipeline | Pipeline can exfiltrate all secrets | Exclude Secrets from deployment Role |

---

## Section 9: DevSecOps Professional Exam Tips

1. **RBAC object scope** — Know that Role and RoleBinding are namespaced; ClusterRole and ClusterRoleBinding are cluster-scoped. A RoleBinding can bind a ClusterRole within a namespace — it does not make the ClusterRole cluster-wide.

2. **Empty podSelector** — Know that `podSelector: {}` in a NetworkPolicy matches all pods in the namespace. A NetworkPolicy with `podSelector: {}` and no rules (no `ingress` or `egress` sections) is the default-deny pattern.

3. **CNI requirement** — Know that Network Policies require a CNI plugin that implements them. Flannel does not; Calico and Cilium do. A common trick question: Network Policies are silently ignored on clusters with non-supporting CNIs.

4. **`readOnlyRootFilesystem` and `emptyDir`** — Know that setting `readOnlyRootFilesystem: true` requires adding `emptyDir` volume mounts for any path the application needs to write (e.g., `/tmp`). Forgetting this causes application startup failures.

5. **PodSecurity enforce vs. warn** — Know the difference: `enforce` rejects pods at admission; `warn` allows the pod but surfaces a warning to `kubectl`; `audit` logs the violation without blocking. The migration pattern is `warn` first, then `enforce` after non-compliant workloads are fixed.

6. **`allowPrivilegeEscalation: false`** — Know that this field sets the `no_new_privs` flag at the kernel level. It is independent of whether the container runs as root. A non-root container without this flag can still escalate via SUID binaries.

7. **Checkov `--framework kubernetes`** — Know that Checkov scans Kubernetes YAML manifests with `--framework kubernetes`. The check IDs use the `CKV_K8S_*` prefix. `soft_fail: false` causes the pipeline to fail on any check violation.

8. **Network Policy DNS egress** — Know that applying a default-deny-egress policy without an explicit UDP 53 allow rule will break DNS resolution inside pods. This is a common misconfiguration that causes application failures after adding Network Policies.

---

## Section 10: Required Reading

- Review the Kubernetes RBAC documentation at [https://kubernetes.io/docs/reference/access-authn-authz/rbac/](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

---

## Section 11: Study Checklist

- [ ] Explain the difference between Role and ClusterRole, and when to use each.
- [ ] Write an RBAC manifest for a least-privilege CI/CD service account.
- [ ] Explain why `cluster-admin` is dangerous for CI/CD service accounts.
- [ ] Describe the default-deny Network Policy pattern using `podSelector: {}`.
- [ ] Name two CNI plugins that support Network Policies and one that does not.
- [ ] List the five key Security Context fields for container hardening.
- [ ] Explain what `emptyDir` is and why it is required with `readOnlyRootFilesystem: true`.
- [ ] Explain the three PodSecurity profiles and their differences.
- [ ] Describe the PodSecurity migration pattern using `warn` before `enforce`.
- [ ] Name three `CKV_K8S_*` check IDs and the Security Context fields they enforce.
- [ ] Complete the Module 12 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
