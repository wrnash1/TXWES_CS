# Quiz: Module 05 — Kubernetes Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Submit answers through the Canvas quiz interface.

---

## Question 1

What is the functional difference between a Kubernetes `Role` and a `ClusterRole`?

- A) A Role applies to all namespaces; a ClusterRole applies only to one namespace
- B) A Role applies only within a specific namespace; a ClusterRole applies across the entire cluster
- C) A Role grants read-only permissions; a ClusterRole grants write permissions
- D) Roles and ClusterRoles are identical — the naming is historical

### Q1 — Correct Answer: B

### Q1 — Distractor Analysis

- A) This reverses the correct definitions — Role is namespace-scoped, ClusterRole is cluster-wide.
- C) Both Role and ClusterRole can define any combination of verbs — the scope, not the permission type, is the difference.
- D) They are meaningfully different in scope — the distinction has real security implications.

---

## Question 2

A ServiceAccount is configured with `automountServiceAccountToken: false`. What security benefit does this provide?

- A) It prevents the ServiceAccount from being used in any RBAC binding
- B) It prevents the service account token from being automatically mounted into pods, reducing credential exposure
- C) It disables network egress for pods using this ServiceAccount
- D) It requires manual approval before pods can be scheduled using this ServiceAccount

### Q2 — Correct Answer: B

### Q2 — Distractor Analysis

- A) The ServiceAccount can still be used in RBAC bindings — token mounting and RBAC usage are independent.
- C) Network egress is controlled by Network Policies, not ServiceAccount configuration.
- D) Pod scheduling approval is not a feature of ServiceAccount configuration.

---

## Question 3

Which Pod Security Admission profile requires that all containers drop ALL Linux capabilities and run as a non-root user?

- A) Privileged
- B) Baseline
- C) Restricted
- D) Default

### Q3 — Correct Answer: C

### Q3 — Distractor Analysis

- A) Privileged allows all capabilities and root — it is the least-restrictive profile.
- B) Baseline blocks the most dangerous configurations but does not require non-root or capability drops.
- D) There is no "Default" PSA profile — the three profiles are Privileged, Baseline, and Restricted.

---

## Question 4

A Kubernetes NetworkPolicy is created with `podSelector: {}` and `policyTypes: [Ingress]` but no `ingress` rules defined. What is the effect?

- A) All ingress traffic is allowed to all pods in the namespace
- B) All ingress traffic is blocked to all pods in the namespace (default-deny ingress)
- C) Ingress traffic is allowed only from within the same namespace
- D) The policy is invalid and has no effect

### Q4 — Correct Answer: B

### Q4 — Distractor Analysis

- A) The absence of ingress rules means no traffic is permitted — the opposite of the stated option.
- C) Same-namespace allowance requires explicit podSelector rules — an empty policy denies all.
- D) The policy is valid YAML and is enforced — empty ingress rules means nothing is allowed.

---

## Question 5

OPA Gatekeeper uses two resource types to implement custom Kubernetes policies. What are they?

- A) PolicyRule and PolicyBinding
- B) AdmissionPolicy and AdmissionController
- C) ConstraintTemplate and Constraint
- D) RuleSet and RuleBinding

### Q5 — Correct Answer: C

### Q5 — Distractor Analysis

- A) PolicyRule is a subfield of Kubernetes RBAC Role objects — not a Gatekeeper resource.
- B) AdmissionPolicy is a Kubernetes 1.30 alpha feature, not OPA Gatekeeper terminology.
- D) RuleSet and RuleBinding are not Gatekeeper resources — they do not exist in this context.

---

## Question 6

Falco detects a security incident by monitoring which data source?

- A) Kubernetes API audit logs only
- B) Container image contents and dependency vulnerability databases
- C) Linux kernel syscalls via eBPF or kernel module
- D) Network packet captures at the cluster ingress

### Q6 — Correct Answer: C

### Q6 — Distractor Analysis

- A) Falco can consume audit logs as a data source but its primary detection mechanism is kernel syscall monitoring.
- B) Image content scanning is performed by tools like Trivy — Falco detects runtime behavior, not image contents.
- D) Network packet capture at ingress is performed by tools like Sysdig or network monitoring systems — Falco operates at the syscall level.

---

## Question 7

Which kube-bench tool is used to automate assessment of Kubernetes cluster hardening?

- A) kubectl audit
- B) kube-bench
- C) kube-hunter
- D) kubesec

### Q7 — Correct Answer: B

### Q7 — Distractor Analysis

- A) `kubectl audit` is not a real kubectl subcommand — audit log analysis requires separate tooling.
- C) kube-hunter performs active penetration testing against a cluster — it finds exploitable weaknesses, not configuration benchmark compliance.
- D) kubesec scores Kubernetes resource security — it does not automate CIS benchmark checks against cluster configuration.

---

## Question 8

A pod running in Kubernetes is compromised. The pod's ServiceAccount has the `cluster-admin` ClusterRole bound to it. What is the worst-case impact?

- A) The attacker can only access resources in the pod's namespace
- B) The attacker gains full administrative control over the entire Kubernetes cluster
- C) The attacker can only read resources — `cluster-admin` does not grant write permissions
- D) The attacker is limited to read access on nodes in the pod's availability zone

### Q8 — Correct Answer: B

### Q8 — Distractor Analysis

- A) `cluster-admin` is cluster-wide — it is not limited to the pod's namespace.
- C) `cluster-admin` grants all verbs on all resources — including create, delete, update, and escalate.
- D) `cluster-admin` grants full cluster control — availability zones are irrelevant to RBAC scope.

---

## Question 9

Which CNI plugins support the enforcement of Kubernetes Network Policies? Select the most complete correct answer.

- A) Flannel only
- B) Flannel and Weave
- C) Calico, Cilium, and Weave (but not Flannel)
- D) All CNI plugins enforce Network Policies by default

### Q9 — Correct Answer: C

### Q9 — Distractor Analysis

- A) Flannel does not support Network Policy enforcement — this is a well-known limitation.
- B) Flannel does not enforce Network Policies — only Weave in this pair does.
- D) Network Policy enforcement is not universal — it requires a CNI plugin that specifically implements it.

---

## Question 10

Pod Security Admission is configured on a namespace with the label `pod-security.kubernetes.io/warn: restricted`. What happens when a non-compliant pod is created?

- A) The pod is rejected at admission and cannot be created
- B) The pod is created but a warning is shown to the user; it is not blocked
- C) The pod is created but is immediately terminated at runtime
- D) The pod is quarantined in a separate namespace for review

### Q10 — Correct Answer: B

### Q10 — Distractor Analysis

- A) Rejection at admission requires the `enforce` label — `warn` allows creation with a warning.
- C) PSA operates at admission time — it does not terminate running pods.
- D) Pod quarantining is not a built-in Kubernetes PSA behavior.

---

Quiz — Module 05 | CIS-4350 | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

A Kubernetes deployment manifest includes `securityContext: privileged: true`. What risk does this introduce?

- A) The pod can only communicate with other privileged pods in the cluster
- B) The container runs with nearly all Linux capabilities and access to the host kernel, making container escape significantly easier
- C) The pod bypasses NetworkPolicy rules and can reach any IP in the cluster
- D) The container is scheduled to run on dedicated nodes reserved for privileged workloads

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Privileged mode grants kernel access, not restricted network communication — it does not limit pod-to-pod communication.
  - C) `privileged: true` affects the Linux security context of the container process — it does not bypass Kubernetes NetworkPolicy enforcement, which operates at the network layer.
  - D) Node scheduling for privileged pods is not automatic — it requires taint/toleration configuration.

---

### Question 12 (5 points)

A Kubernetes Namespace has Pod Security Admission configured with `pod-security.kubernetes.io/enforce: restricted`. A developer deploys a pod that does not set `runAsNonRoot: true`. What occurs?

- A) The pod is created with a warning but runs successfully
- B) The pod is rejected at admission and cannot be created
- C) The pod is created but is automatically patched to add `runAsNonRoot: true`
- D) The pod is created but flagged in the audit log for review

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The `warn` mode produces a warning without rejection; `enforce` mode rejects the pod.
  - C) PSA does not mutate pods — it only validates and admits or rejects.
  - D) Audit logging is a separate feature; the `enforce` mode actively blocks non-compliant pods.

---

### Question 13 (5 points)

In Kubernetes RBAC, what is the difference between a `RoleBinding` and a `ClusterRoleBinding`?

- A) A RoleBinding can reference ClusterRoles but only grants permissions within a single namespace; a ClusterRoleBinding grants cluster-wide access
- B) A RoleBinding requires a ServiceAccount; a ClusterRoleBinding can reference user accounts
- C) A RoleBinding is deprecated in Kubernetes 1.25+ and replaced by ClusterRoleBinding
- D) A RoleBinding grants read-only access; a ClusterRoleBinding grants read-write access

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Both RoleBinding and ClusterRoleBinding can reference ServiceAccounts, Users, and Groups as subjects.
  - C) RoleBinding is not deprecated — it remains the correct mechanism for namespace-scoped permission grants.
  - D) The distinction is scope (namespace vs. cluster-wide), not permission level (read vs. write).

---

### Question 14 (5 points)

kubesec scores a Kubernetes Deployment manifest. Which of the following manifest changes would most likely increase the kubesec score?

- A) Increasing the number of replicas from 1 to 3
- B) Adding `securityContext: readOnlyRootFilesystem: true` and `runAsNonRoot: true`
- C) Adding resource limits for CPU and memory
- D) Adding a liveness probe and readiness probe

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Replica count is an availability concern, not a security configuration — kubesec does not score it.
  - C) Resource limits are an operational best practice but kubesec's primary focus is security context and privilege configurations.
  - D) Liveness and readiness probes improve reliability — they are not security controls scored by kubesec.

---

### Question 15 (5 points)

A Kubernetes NetworkPolicy `policyTypes: [Egress]` is applied to a namespace with no `egress` rules defined. What is the result for pods in that namespace?

- A) Pods can reach any external destination — the policy has no effect without rules
- B) All outgoing traffic from pods in the namespace is blocked
- C) Only DNS traffic (port 53) is allowed — Kubernetes automatically adds a DNS egress exception
- D) Traffic to the Kubernetes API server is still allowed — control-plane traffic is exempt

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Defining the policy type with no rules creates a default-deny — the policy does have effect.
  - C) Kubernetes does not automatically add DNS exceptions — DNS will break unless an explicit egress rule allows port 53.
  - D) No traffic is automatically exempt in a default-deny egress policy — API server access must be explicitly allowed.

---

### Question 16 (5 points)

Which Falco rule condition would trigger an alert when a process other than `httpd` or `nginx` opens a network socket inside a container?

- A) `evt.type = open and not proc.name in (httpd, nginx)`
- B) `evt.type in (connect, accept) and not proc.name in (httpd, nginx) and container.id != host`
- C) `syscall.type = socket and container.privileged = false`
- D) `fd.type = ipv4 and container.name startswith prod`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `open` is a file open syscall — network socket operations use `connect` or `accept`.
  - C) `syscall.type` is not a valid Falco field name — the correct field is `evt.type`. Also, `container.privileged` is not the right filter for this use case.
  - D) This condition is too narrow — it only matches IPv4 connections in containers named `prod*` and does not filter by process name.

---

### Question 17 (5 points)

The CIS Kubernetes Benchmark recommends setting `--anonymous-auth=false` on the kubelet. What attack does this prevent?

- A) It prevents unauthenticated requests to the kubelet API, which could allow an attacker to list pods, exec into containers, or retrieve secrets from the node
- B) It prevents anonymous users from creating new namespaces in the cluster
- C) It disables the ability to run `kubectl exec` against any pod on the node
- D) It prevents the kubelet from registering with the API server without a valid TLS certificate

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Namespace creation is controlled by RBAC on the Kubernetes API server, not the kubelet configuration.
  - C) `kubectl exec` is proxied through the API server, which enforces authentication regardless of the kubelet setting.
  - D) Kubelet-to-API-server TLS is controlled by `--tls-cert-file` and `--tls-private-key-file`, not `--anonymous-auth`.

---

### Question 18 (5 points)

A developer needs to grant a pod read access to Secrets in only the `payments` namespace. Which combination of resources is correct?

- A) ClusterRole with `secrets: get,list` + ClusterRoleBinding to the pod's ServiceAccount
- B) Role with `secrets: get,list` in the `payments` namespace + RoleBinding in the `payments` namespace to the pod's ServiceAccount
- C) ClusterRole with `secrets: get,list` + RoleBinding in the `payments` namespace to the pod's ServiceAccount
- D) Role with `secrets: get,list` in `kube-system` + RoleBinding in `payments` to the pod's ServiceAccount

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) A ClusterRoleBinding with a ClusterRole grants access to secrets in all namespaces — violating least privilege.
  - B) This is valid but less conventional than C — using a ClusterRole for reusable permission definitions paired with a namespace-scoped RoleBinding is the recommended pattern.
  - D) A Role defined in `kube-system` cannot be bound to grant access in a different namespace — Role scope is local to its namespace.

---

### Question 19 (5 points)

What does `etcd` encryption at rest protect against?

- A) Unauthorized reads of Kubernetes API resources by users without RBAC access
- B) Physical theft or unauthorized access to the etcd storage volume, exposing Secrets in plaintext
- C) Network interception of etcd cluster replication traffic between nodes
- D) Unauthorized writes to etcd by compromised worker nodes

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) RBAC enforces access control for API requests — encryption at rest protects data stored on disk, not live API access.
  - C) Encryption in transit for etcd traffic is handled by TLS/mTLS between etcd peers — this is separate from encryption at rest.
  - D) Write access control to etcd is handled by etcd's client authentication and RBAC — encryption at rest does not prevent writes from authorized clients.

---

### Question 20 (5 points)

An OPA Gatekeeper ConstraintTemplate policy denies pods that do not set `readOnlyRootFilesystem: true`. A developer deploys an init container that requires a writable filesystem. What is the most appropriate response?

- A) Delete the Gatekeeper ConstraintTemplate — it is too restrictive for real workloads
- B) Add a namespace-level label to disable Gatekeeper for that namespace
- C) Update the Constraint to add an exemption for the specific init container image or namespace, with documented justification
- D) Use `--no-verify` in the kubectl command to bypass admission control

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Removing the policy for all workloads because one workload needs an exception defeats the purpose of the policy.
  - B) Disabling Gatekeeper for an entire namespace removes protection from all workloads in that namespace.
  - D) `--no-verify` is a git flag — kubectl does not have a bypass flag for admission webhooks.
