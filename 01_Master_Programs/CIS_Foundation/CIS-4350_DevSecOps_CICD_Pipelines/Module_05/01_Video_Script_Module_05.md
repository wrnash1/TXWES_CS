# Video Script: Module 05 — Kubernetes Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–1:30)

[SLIDE: Module 05 title card]

Welcome to Module 05. In Module 04 we secured individual Docker containers. In this module we scale up to Kubernetes — the dominant container orchestration platform — and learn how to apply security controls at the cluster level.

Kubernetes introduces new attack surface: the API server, etcd, RBAC permissions, pod scheduling, network communication between pods, secrets storage, and admission control. Each of these is an area where misconfiguration creates critical vulnerabilities.

By the end of this module you'll understand Kubernetes RBAC, Pod Security Admission, network policies, secrets management, admission controllers including OPA Gatekeeper, runtime security with Falco, and the CIS Kubernetes Benchmark.

---

### SEGMENT 2 — Kubernetes Architecture and Security Surface (1:30–4:30)

[SLIDE: Kubernetes control plane and node architecture]

Kubernetes has two types of components: control plane and worker nodes.

The control plane includes the API server — the central management endpoint; etcd — the key-value store holding all cluster state including secrets; the scheduler — assigns pods to nodes; and the controller manager — maintains desired state.

Worker nodes run the kubelet — the node agent; the container runtime (containerd or CRI-O); and kube-proxy — network routing.

The security attack surface breaks down into four areas.

Control plane security: The API server is the single point of control for the entire cluster. Unauthorized access to the API server is a complete cluster compromise. etcd contains all secrets in base64 encoding by default — encryption at rest is required for any regulated environment.

Workload security: Pods running with excessive privileges, host namespace access, or as root can escape to the node.

Network security: By default, all pods can communicate with all other pods. This is a flat network model that violates the principle of least privilege.

Secrets security: Kubernetes Secrets are base64-encoded, not encrypted. They must be protected with RBAC and optionally with external secret management.

---

### SEGMENT 3 — RBAC in Kubernetes (4:30–8:00)

[SLIDE: RBAC entities diagram — Subject, Role, RoleBinding]

Role-Based Access Control is the primary authorization mechanism in Kubernetes. RBAC has four resources: Role, ClusterRole, RoleBinding, and ClusterRoleBinding.

A Role defines a set of permissions within a specific namespace. A ClusterRole defines permissions cluster-wide. A RoleBinding grants a Role to a subject (user, group, or ServiceAccount) within a namespace. A ClusterRoleBinding grants a ClusterRole cluster-wide.

Here's a minimal Role for a developer who needs read-only access to pods and logs in the `production` namespace:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
```

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developer-pod-reader
  namespace: production
subjects:
  - kind: User
    name: alice@company.com
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

The most common RBAC mistake is using the `cluster-admin` ClusterRole for service accounts that don't need it. `cluster-admin` is effectively root on the cluster. Use it only for cluster administrators.

ServiceAccount RBAC is especially important because ServiceAccounts are mounted into pods by default. A pod with an overly permissive ServiceAccount can manipulate the Kubernetes API on behalf of an attacker who compromises the pod.

```yaml
# Disable automounting for service accounts that don't need API access
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-service
  namespace: production
automountServiceAccountToken: false
```

---

### SEGMENT 4 — Pod Security Admission (8:00–11:00)

[SLIDE: Pod Security Admission profile levels — Privileged, Baseline, Restricted]

Pod Security Admission (PSA), introduced in Kubernetes 1.23 and stable in 1.25, replaces the deprecated PodSecurityPolicy. PSA enforces security standards at the namespace level using three profiles.

Privileged: No restrictions. Pods can run as root, use host namespaces, and escalate privileges. Only for system namespaces like `kube-system`.

Baseline: Prevents the most dangerous configurations. Disallows: host namespaces (`hostPID`, `hostIPC`, `hostNetwork`), privileged containers, host path volumes that aren't read-only, and several other high-risk settings.

Restricted: Implements current pod security best practices. Requires non-root user, drops all capabilities, requires seccomp profile, disallows privilege escalation.

Enable PSA by labeling namespaces:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/audit: restricted
```

With `enforce: restricted`, any pod that violates the Restricted profile will be rejected at admission. The `warn` label lets non-conforming pods through but generates a warning. The `audit` label logs violations to the audit log. Use `warn` and `audit` before `enforce` during migration to identify which workloads need remediation.

A pod that satisfies the Restricted profile looks like:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: myapp:v1.2.3
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
        readOnlyRootFilesystem: true
      volumeMounts:
        - name: tmp
          mountPath: /tmp
  volumes:
    - name: tmp
      emptyDir: {}
```

---

### SEGMENT 5 — Network Policies (11:00–13:30)

[SLIDE: Network policy ingress/egress diagram]

By default, all pods in a Kubernetes cluster can reach all other pods on any port. This flat network model means that if an attacker compromises one pod, they can reach every other pod in the cluster.

Network Policies define how pods can communicate. They are the firewall rules for pod-to-pod traffic.

A default-deny policy blocks all ingress and egress traffic for a namespace:

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

Then selectively allow only required communication:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-api
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

Network Policies require a CNI plugin that supports them — Calico, Cilium, and Weave are common examples. The default Flannel CNI does not enforce Network Policies.

---

### SEGMENT 6 — Admission Controllers and OPA Gatekeeper (13:30–17:00)

[SLIDE: Kubernetes admission controller flow diagram]

Admission controllers are plugins that intercept API requests after authentication and authorization but before persistence in etcd. They can mutate requests or validate them, rejecting requests that violate policy.

Two types: Mutating Admission Controllers modify the incoming object (e.g., inject a sidecar container). Validating Admission Controllers accept or reject based on policy.

OPA Gatekeeper is a validating admission webhook that uses Rego policies (same language as OPA) to enforce custom policies on Kubernetes objects. It extends PSA capabilities with organization-specific policies.

A ConstraintTemplate defines a reusable policy type:

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredLabels
      validation:
        openAPIV3Schema:
          properties:
            labels:
              type: array
              items:
                type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredlabels
        violation[{"msg": msg}] {
          provided := {label | input.review.object.metadata.labels[label]}
          required := {label | label := input.parameters.labels[_]}
          missing := required - provided
          count(missing) > 0
          msg := sprintf("Missing required labels: %v", [missing])
        }
```

A Constraint instantiates the policy:

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredLabels
metadata:
  name: require-app-label
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
  parameters:
    labels: ["app", "version", "team"]
```

---

### SEGMENT 7 — Runtime Security with Falco and CIS Benchmark (17:00–20:30)

[SLIDE: Falco alert output]

Falco is an open-source runtime security tool from Sysdig (now CNCF). It monitors the Linux kernel via eBPF or kernel module, detecting anomalous container behavior and generating alerts.

Falco rules define suspicious behavior. Built-in rules detect events like:

```yaml
- rule: Terminal shell in container
  desc: A shell was spawned by a non-shell program in a container
  condition: >
    spawned_process and container
    and shell_procs and proc.pname exists
    and not proc.pname in (shell_binaries)
  output: >
    Shell spawned in container (user=%user.name container=%container.name
    shell=%proc.name parent=%proc.pname)
  priority: WARNING
```

Falco integrates with SIEM systems, Slack, PagerDuty, and Kubernetes audit logs for alerting.

The CIS Kubernetes Benchmark provides prescriptive hardening guidance for Kubernetes clusters. kube-bench is an open-source tool that automates CIS benchmark checks:

```bash
# Run kube-bench on a node
kube-bench run --targets node

# Run against the control plane
kube-bench run --targets master

# Output in JSON for integration
kube-bench run --json > kube-bench-results.json
```

kube-bench reports pass, fail, and warn for each CIS check, organized by section (API server, etcd, scheduler, controller manager, RBAC, etc.).

---

### SEGMENT 8 — Module Summary and Looking Ahead (20:30–22:00)

[SLIDE: Module 05 key takeaways]

Module 05 summary.

Kubernetes RBAC controls who can do what to which resources. Avoid `cluster-admin` for service accounts; disable automounting tokens for pods that don't need API access.

Pod Security Admission enforces security profiles at the namespace level. Use `warn` and `audit` before `enforce` to identify non-compliant workloads.

Network Policies implement default-deny with selective allow — the Kubernetes equivalent of firewall rules.

OPA Gatekeeper extends PSA with custom organization policies enforced at admission.

Falco provides runtime threat detection by monitoring kernel syscalls and container behavior.

kube-bench automates CIS Kubernetes Benchmark checks to assess and track cluster hardening status.

In Module 06 we move to Infrastructure as Code security — Terraform scanning with tfsec and checkov, policy as code with OPA and Sentinel, and immutable infrastructure principles. See you there.

---

*[END OF SCRIPT — Module 05]*
