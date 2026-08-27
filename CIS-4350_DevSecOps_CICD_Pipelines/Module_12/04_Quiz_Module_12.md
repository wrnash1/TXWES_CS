# Quiz: Module 12 — Kubernetes Security: RBAC, Network Policies, and Pod Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

A CI/CD pipeline service account needs to update Deployments and Services in the `app-prod` namespace but must not be able to read Secrets or access any other namespace. Which RBAC configuration correctly implements this?

- A) Create a ClusterRole with permissions on Deployments and Services, then create a ClusterRoleBinding to the service account
- B) Create a Role in `app-prod` with permissions on Deployments and Services, then create a RoleBinding in `app-prod` to the service account
- C) Create a Role in `app-prod` with permissions on Deployments, Services, and Secrets, then suppress Secrets access with a deny rule
- D) Assign the built-in `edit` ClusterRole to the service account via a ClusterRoleBinding scoped to `app-prod`

#### Q1 Correct Answer

B — A Role is namespaced and can only grant permissions within its namespace. A RoleBinding binds it to the service account within that same namespace. This creates a precisely scoped grant: the service account can manage Deployments and Services in `app-prod` only. No cross-namespace access is possible because the Role and RoleBinding are both namespaced to `app-prod`.

#### Q1 Distractor Analysis

- *Why A is incorrect:* A ClusterRoleBinding grants the ClusterRole across the entire cluster. Even scoped to Deployments and Services, the service account would have that access in every namespace — violating the namespace isolation requirement.
- *Why C is incorrect:* Kubernetes RBAC is additive only. There are no deny rules in Kubernetes RBAC. You cannot grant Secrets access and then deny it. The correct approach is to simply not include Secrets in the Role's resource list.
- *Why D is incorrect:* The built-in `edit` ClusterRole grants broad permissions including Secrets read access. Binding it via ClusterRoleBinding would give cluster-wide access. Even binding it via RoleBinding (which would scope it to the namespace) would still grant Secrets access, violating the requirement.

---

### Question 2

A Kubernetes cluster has a NetworkPolicy with the following spec applied to the `payments` namespace:

```yaml
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

What is the effect of this policy?

- A) All ingress to all pods in `payments` is blocked; egress from all pods is still allowed because no egress rules are specified
- B) All ingress and egress to and from all pods in `payments` is blocked; no traffic is permitted unless a more specific NetworkPolicy allows it
- C) The policy has no effect because `podSelector: {}` matches no pods
- D) All egress from all pods in `payments` is blocked; ingress is still allowed because the policy does not include ingress rules

#### Q2 Correct Answer

B — `podSelector: {}` matches all pods in the namespace (empty selector = all). Listing both `Ingress` and `Egress` in `policyTypes` with no `ingress` or `egress` rule sections means no traffic is permitted. This is the default-deny-all pattern. Any subsequent NetworkPolicy that selects specific pods and defines ingress/egress rules will add specific allow flows on top of this baseline.

#### Q2 Distractor Analysis

- *Why A is incorrect:* `podSelector: {}` matches all pods, not no pods. And listing `Egress` in `policyTypes` with no egress rules means egress is blocked — not allowed by default.
- *Why C is incorrect:* `podSelector: {}` is an empty selector, which in Kubernetes NetworkPolicy semantics matches all pods in the namespace — the opposite of matching no pods.
- *Why D is incorrect:* Both `Ingress` and `Egress` are listed in `policyTypes`, so both are controlled by this policy. Without rules, both are blocked.

---

### Question 3

After applying a default-deny-all NetworkPolicy to a namespace, application pods begin failing DNS resolution — they cannot look up service names. What is the most likely cause and fix?

- A) The CoreDNS pods are in a different namespace and need a ClusterRole to serve the blocked namespace; add a ClusterRoleBinding for CoreDNS
- B) The default-deny-egress policy blocks UDP port 53 traffic from pods to the CoreDNS service; add an explicit egress NetworkPolicy allowing UDP port 53 to the kube-dns namespace
- C) Kubernetes NetworkPolicy does not affect DNS traffic; the DNS failure is caused by a misconfigured CoreDNS ConfigMap that must be repaired separately
- D) The default-deny policy blocks ingress to CoreDNS pods; apply `podSelector: {}` with a rule allowing port 53 ingress from all pods

#### Q3 Correct Answer

B — DNS resolution requires pods to make egress connections on UDP port 53 to the CoreDNS service, which typically runs in the `kube-system` namespace. A default-deny-egress policy blocks this traffic. The fix is an explicit egress NetworkPolicy on the application namespace pods that allows UDP (and TCP for large DNS responses) port 53, typically scoped to `namespaceSelector` matching `kube-system`.

#### Q3 Distractor Analysis

- *Why A is incorrect:* RBAC controls Kubernetes API access, not network traffic. DNS resolution is a network-layer operation unrelated to RBAC or ClusterRoles.
- *Why C is incorrect:* NetworkPolicy does affect DNS traffic. DNS uses UDP/TCP port 53. A default-deny-egress policy will block DNS queries from pods in the namespace.
- *Why D is incorrect:* The failure is an egress problem from the application pods, not an ingress problem into CoreDNS. Allowing ingress to CoreDNS does not fix the inability of application pods to send outbound DNS queries.

---

### Question 4

Which Security Context field specifically prevents a process from gaining more privileges than it started with, even if a SUID binary is executed inside the container?

- A) `runAsNonRoot: true`
- B) `capabilities.drop: [ALL]`
- C) `readOnlyRootFilesystem: true`
- D) `allowPrivilegeEscalation: false`

#### Q4 Correct Answer

D — `allowPrivilegeEscalation: false` sets the `no_new_privs` flag at the kernel level. This flag prevents any process in the container from gaining additional privileges beyond what it started with — even via SUID (Set User ID) or SGID binaries that would normally allow privilege escalation. This is distinct from `runAsNonRoot`, which prevents the initial process from running as root but does not prevent a non-root process from escalating to root via a SUID binary.

#### Q4 Distractor Analysis

- *Why A is incorrect:* `runAsNonRoot: true` prevents the initial process from starting as UID 0. It does not prevent privilege escalation via SUID binaries. A container starting as UID 1000 could still escalate to root via a SUID binary without `allowPrivilegeEscalation: false`.
- *Why B is incorrect:* `capabilities.drop: [ALL]` removes Linux capabilities, which limits specific privileged operations. But dropping capabilities is a different mechanism from the `no_new_privs` flag. Both are needed for full hardening.
- *Why C is incorrect:* `readOnlyRootFilesystem: true` prevents filesystem writes. It does not affect privilege escalation via in-memory execution.

---

### Question 5

A container with `readOnlyRootFilesystem: true` fails to start with the error: `nginx: [emerg] mkdir() "/var/cache/nginx/client_temp" failed (30: Read-only file system)`. What is the correct fix?

- A) Remove `readOnlyRootFilesystem: true` because nginx requires a writable filesystem
- B) Add `emptyDir: {}` volumes mounted at `/var/cache/nginx` and other paths nginx writes to, providing writable scratch space without removing the root filesystem restriction
- C) Change `readOnlyRootFilesystem: true` to `readOnlyRootFilesystem: false` at the container level while keeping it `true` at the pod level
- D) Add `capabilities.add: [DAC_OVERRIDE]` to allow the process to write to read-only directories

#### Q5 Correct Answer

B — `emptyDir` volumes are ephemeral volumes backed by node storage that provide a writable directory for the duration of the pod's lifetime. Mounting `emptyDir` volumes at the specific paths nginx needs to write (e.g., `/var/cache/nginx`, `/var/run`, `/tmp`) allows nginx to function normally while keeping the root filesystem read-only. This is the correct pattern for running any application that needs writable scratch space with `readOnlyRootFilesystem: true`.

#### Q5 Distractor Analysis

- *Why A is incorrect:* Removing `readOnlyRootFilesystem: true` eliminates a key security control without a security-equivalent replacement. The correct response is to add writable volumes for specific paths, not to remove the constraint.
- *Why C is incorrect:* `readOnlyRootFilesystem` is a container-level field only — there is no pod-level equivalent. Setting it at the pod level is not valid YAML for Kubernetes.
- *Why D is incorrect:* `DAC_OVERRIDE` (Discretionary Access Control Override) is a Linux capability that allows bypassing file permission checks. This would allow the container to write to arbitrary paths owned by other users, not to fix a read-only filesystem mount. It would also re-introduce a capability that was dropped for security.

---

### Question 6

A platform team wants to enforce that all pods in the `app-prod` namespace must meet the `restricted` PodSecurity profile but wants to avoid immediately breaking existing workloads during the migration. What is the correct sequence of namespace labels to apply?

- A) Apply `enforce: restricted` immediately — this is the only way to validate that workloads are compliant
- B) Apply `warn: restricted` and `audit: restricted` first to identify non-compliant pods without breaking them, then switch to `enforce: restricted` after workloads are updated
- C) Apply `enforce: baseline`, then `enforce: restricted` — migrating through the intermediate profile first reduces breakage risk
- D) Apply `audit: restricted` to the cluster-level PodSecurity configuration, which propagates to all namespaces automatically

#### Q6 Correct Answer

B — The `warn` mode surfaces non-compliance as warnings in kubectl output when pods are created or updated, without rejecting them. The `audit` mode logs violations to the audit log. Together, `warn` and `audit` allow the team to discover which existing workloads violate the `restricted` profile and fix them proactively. Once all workloads are compliant, switching to `enforce` has no impact because there are no remaining violations.

#### Q6 Distractor Analysis

- *Why A is incorrect:* Applying `enforce: restricted` immediately rejects all non-compliant pod creation and update operations, including rolling deployments. This can cause production outages if existing workloads are not yet compliant.
- *Why C is incorrect:* While `baseline` is less strict than `restricted`, jumping through an intermediate `enforce: baseline` level still risks breaking workloads that violate baseline restrictions. Using `warn` mode at the target profile level is the safer migration path.
- *Why D is incorrect:* PodSecurity configuration is applied at the namespace level via labels, not at a cluster level that propagates automatically. The `kube-system` namespace uses `privileged` profile by default and would be incorrect to inherit a `restricted` setting.

---

### Question 7

Checkov reports `CKV_K8S_20: Containers should not allow privilege escalation` for a Deployment manifest. What specific field in the manifest is missing or incorrectly configured?

- A) `securityContext.runAsNonRoot: true` is missing from the container spec
- B) `securityContext.allowPrivilegeEscalation: false` is missing from the container spec
- C) `securityContext.capabilities.drop: [ALL]` is missing from the container spec
- D) `securityContext.readOnlyRootFilesystem: true` is missing from the container spec

#### Q7 Correct Answer

B — CKV_K8S_20 checks specifically for the presence of `allowPrivilegeEscalation: false` in the container's `securityContext`. The check fails if the field is absent (the default is `allowPrivilegeEscalation: true`) or if it is explicitly set to `true`. The remediation is to add `allowPrivilegeEscalation: false` to the container's security context.

#### Q7 Distractor Analysis

- *Why A is incorrect:* CKV_K8S_15 checks for `runAsNonRoot: true`. CKV_K8S_20 specifically checks for `allowPrivilegeEscalation: false`. These are separate checks with separate check IDs.
- *Why C is incorrect:* CKV_K8S_28 and CKV_K8S_37 check for capability management. CKV_K8S_20 specifically targets the `allowPrivilegeEscalation` field.
- *Why D is incorrect:* CKV_K8S_8 checks for `readOnlyRootFilesystem: true`. Each security context field has its own dedicated Checkov check ID.

---

### Question 8

A DevSecOps engineer runs `kubectl auth can-i get secrets --namespace=app-prod --as=system:serviceaccount:app-prod:ci-deployer` and receives `yes`. The CI/CD pipeline service account should not have access to Secrets. What is the most likely cause?

- A) The `ci-deployer` service account is in the wrong namespace and accidentally inherits the `default` service account's permissions
- B) The `ci-deployer` RoleBinding is bound to a Role or ClusterRole that includes `secrets` in its resource list, or the service account has an additional RoleBinding or ClusterRoleBinding that grants Secrets access
- C) The `get` verb on Secrets is automatically granted to all service accounts in Kubernetes by default
- D) The namespace labels include `pod-security.kubernetes.io/enforce: restricted`, which inadvertently grants Secrets access to pipeline service accounts

#### Q8 Correct Answer

B — The most likely cause is that the Role bound to `ci-deployer` includes `secrets` in its resource list, or there is an additional binding (a second RoleBinding or a ClusterRoleBinding) that grants Secrets access. You can diagnose this with `kubectl get rolebindings,clusterrolebindings -n app-prod -o yaml | grep -A 20 ci-deployer` to find all bindings for the service account and inspect the referenced roles.

#### Q8 Distractor Analysis

- *Why A is incorrect:* Service accounts do not inherit each other's permissions. The `default` service account has minimal permissions by default. Being in a namespace does not cause permission inheritance.
- *Why C is incorrect:* Kubernetes does not automatically grant `get` on Secrets to service accounts. The default service account has very limited API access. Secret access must be explicitly granted via RBAC.
- *Why D is incorrect:* PodSecurity namespace labels control which pods can run in the namespace based on their security context. They have no effect on API access control or RBAC permissions.

---

### Question 9

A Kubernetes NetworkPolicy applies to pods labeled `app: database` in the `app-prod` namespace. It defines ingress from pods labeled `app: api` on port 5432. A pod labeled `app: api` in the `monitoring` namespace cannot reach the database pods, even though the company's architecture requires it. What change to the NetworkPolicy would permit this cross-namespace traffic?

- A) Add a `namespaceSelector` matching the `monitoring` namespace alongside the existing `podSelector: {matchLabels: {app: api}}` in the ingress `from` block
- B) Create a ClusterRoleBinding that grants the `monitoring` namespace service account access to the `app-prod` namespace
- C) Add the `monitoring` namespace to the existing `podSelector` using a comma-separated list of namespace names
- D) Set the NetworkPolicy's `podSelector: {}` to apply to all pods in `app-prod`, which will automatically allow cross-namespace traffic

#### Q9 Correct Answer

A — A NetworkPolicy ingress `from` entry can combine `podSelector` and `namespaceSelector`. To allow traffic from pods labeled `app: api` specifically in the `monitoring` namespace, the `from` entry should include a `namespaceSelector` matching the namespace label (e.g., `kubernetes.io/metadata.name: monitoring`) along with a `podSelector` matching `app: api`. Without the `namespaceSelector`, the policy only permits traffic from pods labeled `app: api` in the same namespace (`app-prod`).

#### Q9 Distractor Analysis

- *Why B is incorrect:* RBAC controls Kubernetes API access, not network traffic between pods. ClusterRoleBindings have no effect on whether pods can make TCP connections to each other.
- *Why C is incorrect:* `podSelector` uses label selectors, not namespace names. Namespace names cannot be listed in a `podSelector`. Namespace filtering uses `namespaceSelector` separately.
- *Why D is incorrect:* `podSelector: {}` expands the scope of which pods the policy applies to (protects), but it does not change the `from` (allowed sources) section. The policy would still only allow traffic from pods in the same namespace unless `namespaceSelector` is added.

---

### Question 10

A security team wants to use Checkov to scan Kubernetes manifests in a GitHub Actions pipeline and ensure the pipeline fails when any check violation is found, while still uploading findings to GitHub Code Scanning for visibility. Which pipeline configuration achieves this?

- A) Set `soft_fail: true` in the Checkov action so it reports all findings without failing, then add a separate step that reads the SARIF file and fails the job if any findings exist
- B) Set `soft_fail: false` in the Checkov action so it exits non-zero on violations, and add a SARIF upload step with `if: always()` so findings are uploaded even when Checkov fails
- C) Set `soft_fail: false` and do not add a SARIF upload step, because the pipeline failure itself notifies the team of violations
- D) Set `soft_fail: true` and add a SARIF upload step without `if: always()`, because `soft_fail: true` guarantees findings are uploaded before the step exits

#### Q10 Correct Answer

B — `soft_fail: false` causes Checkov to exit with a non-zero code when any check fails, which fails the GitHub Actions job. This is the pipeline gate. The SARIF upload step with `if: always()` ensures the findings file is uploaded to GitHub Code Scanning regardless of whether the Checkov step passed or failed — the same pattern used for Trivy in Module 11. Without `if: always()`, a failing Checkov step would cause GitHub Actions to skip the SARIF upload, making the findings invisible in the Code Scanning tab.

#### Q10 Distractor Analysis

- *Why A is incorrect:* With `soft_fail: true`, Checkov always exits with code 0 regardless of findings. The pipeline would never fail. Adding a separate step to parse the SARIF file is unnecessarily complex when `soft_fail: false` provides the correct behavior directly.
- *Why C is incorrect:* Without a SARIF upload, findings are only visible in raw job logs. GitHub Code Scanning provides structured finding tracking, PR annotations, and dismissal workflows that are lost without the upload step.
- *Why D is incorrect:* With `soft_fail: true`, the Checkov step always succeeds, so `if: always()` is not needed to preserve the upload. But `soft_fail: true` also means the pipeline never fails on violations, which defeats the purpose of a security gate.

---

#### Q11

A Kubernetes NetworkPolicy is applied to the `payments` namespace with a `podSelector: {}` and no ingress or egress rules. What is the effect of this policy?

- A) The policy has no effect because it selects no specific pods
- B) All pods in the `payments` namespace are denied all ingress and egress traffic by default
- C) All pods in the cluster are denied all ingress and egress traffic
- D) Pods in the `payments` namespace can receive traffic but cannot initiate outbound connections

#### Q11 Correct Answer

B — A `podSelector: {}` (empty selector) selects all pods in the namespace where the policy is applied. A NetworkPolicy with no ingress rules denies all ingress traffic to selected pods, and a policy with no egress rules denies all egress traffic. This is the standard default-deny pattern. It applies only within the namespace where the policy is created, not cluster-wide.

#### Q11 Distractor Analysis

- *Why A is incorrect:* An empty `podSelector: {}` does not mean "no pods" — it means "all pods in this namespace." This is the standard Kubernetes selector behavior where an empty selector matches everything in scope.
- *Why C is incorrect:* NetworkPolicies are namespace-scoped. A policy in the `payments` namespace only affects pods in that namespace, not pods in other namespaces.
- *Why D is incorrect:* If no egress rules are specified in a NetworkPolicy that selects pods, egress is also denied (not permitted). The default-deny applies to both ingress and egress when the respective rule sets are absent.

---

#### Q12

A developer creates a ServiceAccount named `ci-deployer` for a GitHub Actions pipeline. The pipeline needs to `kubectl apply` manifests to a specific namespace. Which RBAC manifest correctly implements least-privilege access?

- A) A ClusterRoleBinding binding `ci-deployer` to `cluster-admin`
- B) A RoleBinding in the target namespace binding `ci-deployer` to a Role that grants `create`, `update`, `patch`, and `delete` on `deployments`, `services`, and `configmaps`
- C) A ClusterRole with `verbs: ["*"]` bound to `ci-deployer` via a RoleBinding in the target namespace
- D) A RoleBinding in `kube-system` granting `ci-deployer` the built-in `admin` ClusterRole

#### Q12 Correct Answer

B — Least-privilege RBAC for a CI/CD deployer means scoping permissions to the specific namespace, specific resources, and specific verbs required. A namespace-scoped Role with explicit verbs on the required resource types, bound via a RoleBinding in the target namespace, is the correct pattern. No cluster-wide permissions are needed for a namespace-scoped deployment.

#### Q12 Distractor Analysis

- *Why A is incorrect:* `cluster-admin` grants unrestricted access to all resources in all namespaces. Binding a CI/CD pipeline service account to `cluster-admin` violates least privilege and creates a high-impact compromise path if the pipeline is exploited.
- *Why C is incorrect:* A ClusterRole with `verbs: ["*"]` grants all verbs on the specified resources. Using wildcard verbs is an overpermission — the role should enumerate only the verbs actually needed.
- *Why D is incorrect:* Binding in `kube-system` grants elevated permissions in the control plane namespace. RoleBindings must be in the namespace where the permissions are needed — the target application namespace, not `kube-system`.

---

#### Q13

A pod specification sets `securityContext.runAsNonRoot: true` but does not set `runAsUser`. The container image's `USER` instruction sets `USER 0` (root). What happens when Kubernetes admits this pod?

- A) Kubernetes ignores `runAsNonRoot` if the image has a `USER` instruction — the image USER directive takes precedence
- B) Kubernetes admission fails with an error because `runAsNonRoot: true` requires the container to run as a non-root user, but the image's `USER 0` specifies root
- C) The container starts as root but Kubernetes restricts its system calls at runtime
- D) `runAsNonRoot: true` only applies if `runAsUser` is explicitly set in the pod spec — without `runAsUser`, it has no effect

#### Q13 Correct Answer

B — `runAsNonRoot: true` causes the Kubernetes admission controller to check the effective user ID of the container. If the image's `USER` directive specifies UID 0 (root) and no `runAsUser` override is provided in the pod spec, the pod will be rejected at admission with a message indicating the container must not run as root.

#### Q13 Distractor Analysis

- *Why A is incorrect:* The pod security context overrides or constrains the image's USER directive. `runAsNonRoot: true` is a hard constraint that is enforced by the admission controller regardless of what the Dockerfile specifies.
- *Why C is incorrect:* `runAsNonRoot` is an admission-time enforcement, not a runtime syscall filter. It prevents the pod from starting rather than restricting system calls after startup. Syscall restrictions are handled by seccomp profiles.
- *Why D is incorrect:* `runAsNonRoot: true` is effective without an explicit `runAsUser`. It instructs Kubernetes to verify that the effective UID is not 0, using the image's USER instruction as the source if `runAsUser` is absent.

---

#### Q14

Which PodSecurity admission mode should be applied first when migrating an existing cluster to the `restricted` profile, and why?

- A) `enforce` — immediately rejecting non-compliant pods ensures the migration is complete before any new deployments
- B) `warn` — the admission controller logs warnings for non-compliant pods without rejecting them, allowing teams to identify and fix violations without causing outages
- C) `audit` — the admission controller records violations in the audit log only, with no user-visible warnings, providing the most non-disruptive first pass
- D) Either `warn` or `audit` must be combined with `enforce` from the start — using either alone is not a valid migration strategy

#### Q14 Correct Answer

B — The recommended PodSecurity migration pattern is to start with `warn` mode so that violations surface as visible warnings in `kubectl apply` output without blocking deployments. This lets teams see which workloads need remediation without causing production outages. After fixing violations, switch to `enforce`. `audit` mode is also useful but produces no user-visible output.

#### Q14 Distractor Analysis

- *Why A is incorrect:* Starting with `enforce` on an existing cluster will immediately reject all non-compliant pods, potentially blocking deployments and causing service disruptions before teams have had a chance to remediate violations.
- *Why C is incorrect:* While `audit` is non-disruptive, it only writes to audit logs that many teams do not actively monitor. `warn` mode produces visible warnings in `kubectl apply` output that developers encounter in their normal workflow, making violations harder to miss.
- *Why D is incorrect:* Using `warn` or `audit` alone is a valid first step in the migration strategy. Combining them with `enforce` from the start would create the same disruption risk as starting with `enforce` directly.

---

#### Q15

A Checkov scan of a Kubernetes Deployment manifest fails with check `CKV_K8S_30`. This check ID corresponds to which security context configuration?

- A) The container is running with `privileged: true`
- B) The container has not set `readOnlyRootFilesystem: true`
- C) The container is missing `allowPrivilegeEscalation: false`
- D) The container is missing resource limits for CPU and memory

#### Q15 Correct Answer

C — `CKV_K8S_30` checks that `securityContext.allowPrivilegeEscalation` is explicitly set to `false`. Without this setting, a container process could gain additional privileges via setuid binaries or kernel mechanisms. This is a key Kubernetes security context hardening requirement.

#### Q15 Distractor Analysis

- *Why A is incorrect:* Privileged container checks use a different Checkov check ID. `CKV_K8S_16` checks for `privileged: true` specifically.
- *Why B is incorrect:* Read-only root filesystem is checked by `CKV_K8S_22`. Each security context attribute maps to its own check ID in Checkov.
- *Why D is incorrect:* Resource limits checks use `CKV_K8S_11` (CPU limits) and `CKV_K8S_13` (memory limits). Checkov maps each distinct misconfiguration to a unique check ID.

---

#### Q16

A Kubernetes cluster uses Flannel as the CNI plugin. A security engineer applies a NetworkPolicy requiring that the `frontend` pods can only communicate with the `backend` pods on port 8080. After applying the policy, the `frontend` pods can still reach all pods in the cluster. What is the most likely cause?

- A) The NetworkPolicy YAML has a syntax error that caused it to be silently ignored
- B) Flannel does not enforce NetworkPolicies — it is a CNI plugin focused on overlay networking rather than policy enforcement
- C) NetworkPolicies require a PodSecurityPolicy to be active before they are enforced
- D) The NetworkPolicy was applied to the wrong namespace

#### Q16 Correct Answer

B — Flannel is a CNI plugin that provides overlay networking but does not implement the Kubernetes NetworkPolicy enforcement API. NetworkPolicies are only enforced when a CNI plugin with policy support is installed — such as Calico, Cilium, or Weave Net. With Flannel, NetworkPolicy objects can be created but are silently ignored, giving a false sense of security.

#### Q16 Distractor Analysis

- *Why A is incorrect:* Kubernetes validates NetworkPolicy YAML at admission time and will reject manifests with syntax errors. A silently accepted but syntactically invalid policy is not the typical failure mode.
- *Why C is incorrect:* NetworkPolicy enforcement has no dependency on PodSecurityPolicy. These are independent Kubernetes security mechanisms.
- *Why D is incorrect:* While a namespace mismatch would also cause a policy to have no effect on the target pods, the scenario specifies the policy was applied correctly and the described behavior matches the known behavior of Flannel specifically.

---

#### Q17

A Kubernetes Deployment runs a web application container. The security team wants to prevent the container from writing to its own filesystem at runtime (except for a specific `/tmp` directory needed by the application). Which combination of security context settings achieves this?

- A) Set `readOnlyRootFilesystem: true` on the container and mount an `emptyDir` volume at `/tmp`
- B) Set `privileged: false` and `allowPrivilegeEscalation: false` — these settings prevent all filesystem writes
- C) Set `runAsNonRoot: true` — non-root processes cannot write to system directories
- D) Apply a NetworkPolicy restricting egress to prevent data exfiltration via the filesystem

#### Q17 Correct Answer

A — `readOnlyRootFilesystem: true` makes the container's root filesystem read-only. Applications that require a writable temporary directory can mount an `emptyDir` volume at `/tmp`, which provides a writable in-memory or ephemeral disk location without making the entire filesystem writable.

#### Q17 Distractor Analysis

- *Why B is incorrect:* `privileged: false` and `allowPrivilegeEscalation: false` restrict privilege escalation but do not make the filesystem read-only. A non-privileged process can still write to the container filesystem unless `readOnlyRootFilesystem: true` is set.
- *Why C is incorrect:* `runAsNonRoot: true` prevents running as UID 0 but does not prevent writes to directories that are writable by the application's UID. Many application-owned directories would still be writable.
- *Why D is incorrect:* NetworkPolicies control network traffic, not filesystem access. They do not prevent processes inside the container from writing to the local filesystem.

---

#### Q18

A team is writing Kubernetes RBAC manifests for three service accounts: `ci-deploy` (needs to deploy to `staging` namespace), `monitoring` (needs to read pods and metrics across all namespaces), and `log-shipper` (needs to read pod logs in all namespaces). Which combination of Role/ClusterRole resources is correct?

- A) Three Roles — all in the `staging` namespace
- B) A Role for `ci-deploy` in `staging`; ClusterRoles for `monitoring` and `log-shipper` because they need cross-namespace read access
- C) Three ClusterRoles — ClusterRoles can be bound to specific namespaces using RoleBindings
- D) A ClusterRole for all three, bound via ClusterRoleBindings to grant the broadest access

#### Q18 Correct Answer

B — `ci-deploy` only needs namespace-scoped access in `staging`, so a Role in that namespace with a RoleBinding is correct. `monitoring` and `log-shipper` need to read resources across all namespaces, which requires ClusterRoles. These ClusterRoles can be bound via ClusterRoleBindings for cluster-wide access.

#### Q18 Distractor Analysis

- *Why A is incorrect:* Roles in the `staging` namespace cannot grant access to pods in other namespaces. `monitoring` and `log-shipper` have cluster-wide read requirements that cannot be satisfied by namespace-scoped Roles.
- *Why C is incorrect:* While ClusterRoles can be bound in a specific namespace via RoleBindings, using ClusterRoles for all three introduces unnecessary cluster-wide permission definitions. For `ci-deploy`, a namespace-scoped Role is the correct least-privilege choice and is simpler to audit.
- *Why D is incorrect:* ClusterRoleBindings grant cluster-wide access. Using ClusterRoleBindings for all three service accounts would grant `ci-deploy` the ability to deploy across all namespaces, violating least privilege.

---

#### Q19

A security engineer runs `kube-bench` against a cluster control plane node and sees FAIL results for benchmark 1.2.1 (`--anonymous-auth=false`) and 1.2.7 (`--authorization-mode` not including RBAC). What risk do these two findings represent?

- A) Anonymous access to the API server allows unauthenticated requests to reach the Kubernetes API, and a missing RBAC authorization mode means all authenticated requests may be permitted without policy checks
- B) These findings indicate the cluster nodes cannot communicate with each other over the network
- C) Anonymous auth is only a risk if the cluster is internet-exposed; authorization mode findings only apply to worker nodes
- D) These are informational findings — kube-bench CIS checks are advisory only and do not represent real attack vectors

#### Q19 Correct Answer

A — `--anonymous-auth=false` is required to prevent unauthenticated requests to the Kubernetes API server. Without this setting, anonymous users can make API calls that may be permitted by RBAC if the `system:anonymous` or `system:unauthenticated` groups have any bound roles. Without RBAC in the authorization chain, the API server may fall back to AlwaysAllow mode, granting every authenticated request unrestricted access.

#### Q19 Distractor Analysis

- *Why B is incorrect:* These flags control authentication and authorization for the API server, not network connectivity between nodes. Node-to-node communication is handled by the CNI plugin and is unrelated to these API server flags.
- *Why C is incorrect:* Anonymous auth is a risk regardless of whether the cluster is internet-exposed — internal attackers or compromised pods could exploit anonymous API access. Authorization mode findings apply to the control plane API server, not worker nodes specifically.
- *Why D is incorrect:* kube-bench implements the CIS Kubernetes Benchmark, which is the industry-standard security baseline for Kubernetes clusters. These findings represent real attack vectors that have been exploited in cloud environment compromises.

---

#### Q20

A developer argues that setting resource limits (`resources.limits.cpu` and `resources.limits.memory`) on Kubernetes pods is a performance concern, not a security concern, and therefore should not be enforced by a security gate. What is the DevSecOps counterargument?

- A) Resource limits have no security value — the developer is correct that this is purely a performance and availability concern
- B) Resource limits prevent a compromised or misbehaving container from consuming all node resources (CPU and memory), which is a denial-of-service attack vector that can make other workloads on the node unavailable
- C) Resource limits prevent containers from writing to persistent volumes, which is a security concern
- D) Resource limits are required by the Kubernetes NetworkPolicy API and must be set before NetworkPolicies are enforced

#### Q20 Correct Answer

B — Resource limits are a security control because they bound the blast radius of a compromised container. Without limits, a single container can consume all available CPU and memory on a node, starving other pods and potentially causing node instability. This is a denial-of-service risk that an attacker with container execution can exploit intentionally. The CIS Kubernetes Benchmark and Checkov both flag missing resource limits as security misconfigurations.

#### Q20 Distractor Analysis

- *Why A is incorrect:* Resource limits have clear security value beyond performance. The CIS Kubernetes Benchmark specifically requires resource limits as a security control, which is why Checkov maps `CKV_K8S_11` and `CKV_K8S_13` to resource limit enforcement.
- *Why C is incorrect:* Resource limits govern CPU and memory allocation, not filesystem access. Persistent volume write access is controlled by volume permissions and security contexts, not resource limits.
- *Why D is incorrect:* NetworkPolicy enforcement depends on the CNI plugin, not on resource limits. These are completely independent Kubernetes features with no dependency relationship.

---

Quiz — Module 12 | CIS-4350 | Texas Wesleyan University | Professor Nash
