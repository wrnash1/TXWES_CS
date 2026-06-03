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
