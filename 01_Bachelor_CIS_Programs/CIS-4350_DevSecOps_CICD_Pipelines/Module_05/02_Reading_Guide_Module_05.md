# Reading Guide: Module 05 — Kubernetes Security

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4350 &BULL; DEVSECOPS & CI/CD SECURITY AUTOMATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Describe Kubernetes control plane components and their security implications
- Write RBAC Roles, ClusterRoles, and bindings following least-privilege principles
- Configure Pod Security Admission profiles on namespaces
- Write Network Policies implementing default-deny with selective allow
- Deploy OPA Gatekeeper ConstraintTemplates and Constraints for custom policy enforcement
- Interpret Falco alert output and understand kube-bench CIS benchmark reports

---

## Section 1 — Kubernetes Architecture Security Review

### 1.1 Control Plane Components

| Component | Function | Key Security Concern |
|---|---|---|
| kube-apiserver | All cluster operations go through it | Expose only via TLS; audit log all requests |
| etcd | Stores all cluster state, including secrets | Encrypt at rest; restrict access to apiserver only |
| kube-scheduler | Assigns pods to nodes | Limit to authenticated API access |
| kube-controller-manager | Runs control loops | Restrict SA token auto-mount |
| cloud-controller-manager | Cloud provider integration | Least-privilege IAM role |

### 1.2 Node Components

| Component | Function | Key Security Concern |
|---|---|---|
| kubelet | Node agent executing pod specs | Authenticate with TLS client certs; restrict anonymous access |
| containerd / CRI-O | Container runtime | Use rootless mode where possible |
| kube-proxy | Manages iptables/eBPF rules | No external exposure needed |

### 1.3 Default Insecure Configurations to Remediate

- Anonymous authentication to the API server (`--anonymous-auth=false`)
- Unauthenticated kubelet API (`--authentication-token-webhook=true`)
- etcd without encryption at rest
- Default service account with automounted token in all pods
- No audit logging on the API server
- Flat network (no Network Policies)

---

## Section 2 — RBAC Deep Dive

### 2.1 RBAC Resource Hierarchy

```text
ClusterRole / Role (defines permissions)
    ↓ bound to ↓
ClusterRoleBinding / RoleBinding (binds to subject)
    ↓ for subject ↓
User / Group / ServiceAccount
```

### 2.2 RBAC Principle of Least Privilege

| Anti-Pattern | Risk | Correct Approach |
|---|---|---|
| `cluster-admin` for app service accounts | Full cluster compromise if SA token stolen | Create minimal Role with only required verbs |
| `get/list/watch` on Secrets cluster-wide | Exposes all secrets | Namespace-scoped Role for specific secret names |
| Wildcard verbs: `verbs: ["*"]` | Allows create/delete/escalate | Enumerate exactly required verbs |
| Wildcard resources: `resources: ["*"]` | Broad access | Enumerate exactly required resources |
| No RBAC at all (ABAC legacy) | Flat authorization | Migrate to RBAC |

### 2.3 Minimal ServiceAccount Pattern

```yaml
# Dedicated ServiceAccount per application
apiVersion: v1
kind: ServiceAccount
metadata:
  name: payments-service
  namespace: production
automountServiceAccountToken: false   # Disable unless API access needed
---
# Role with exactly required permissions
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: payments-config-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    resourceNames: ["payments-config"]  # Named resource restriction
    verbs: ["get"]
---
# Bind role to ServiceAccount
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: payments-config-binding
  namespace: production
subjects:
  - kind: ServiceAccount
    name: payments-service
    namespace: production
roleRef:
  kind: Role
  name: payments-config-reader
  apiGroup: rbac.authorization.k8s.io
```

### 2.4 Auditing RBAC with kubectl

```bash
# List all ClusterRoleBindings — find who has cluster-admin
kubectl get clusterrolebindings -o wide

# Check effective permissions for a ServiceAccount
kubectl auth can-i --list \
  --as=system:serviceaccount:production:payments-service

# Check if a specific action is permitted
kubectl auth can-i delete pods \
  --as=system:serviceaccount:production:payments-service \
  -n production
```

---

## Section 3 — Pod Security Admission

### 3.1 PSA Profile Comparison

| Check | Privileged | Baseline | Restricted |
|---|---|---|---|
| hostNetwork / hostPID / hostIPC | Allowed | Blocked | Blocked |
| Privileged containers | Allowed | Blocked | Blocked |
| Host path volumes | Allowed | Blocked (most) | Blocked |
| runAsRoot | Allowed | Allowed | Must be false |
| Capabilities (all) | Allowed | CAP_SYS_ADMIN+ blocked | Must drop ALL |
| Privilege escalation | Allowed | Allowed | Must be false |
| seccomp profile | Allowed | Allowed | Must be RuntimeDefault or Localhost |
| Volume types | All | Most | Limited set only |

### 3.2 Namespace Labels for PSA

```yaml
# Dry run — warn mode first (does not block)
metadata:
  labels:
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/warn-version: latest

# Graduated enforcement
metadata:
  labels:
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/enforce: baseline   # Enforce at baseline first
```

### 3.3 Compliant Pod Spec for Restricted Profile

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    runAsGroup: 1001
    fsGroup: 1001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: myapp:v1.2.3@sha256:abc123...
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
        readOnlyRootFilesystem: true
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

---

## Section 4 — Network Policies

### 4.1 Default-Deny Pattern

```yaml
# Apply this to every application namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-egress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Egress
```

### 4.2 Three-Tier Application Network Policy

```yaml
# Allow ingress-controller → frontend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ingress-to-frontend
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: frontend
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: ingress-nginx
      ports:
        - port: 8080
---
# Allow frontend → API
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-api
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: api
  ingress:
    - from:
        - podSelector:
            matchLabels:
              tier: frontend
      ports:
        - port: 8080
---
# Allow API → database
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-to-db
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: database
  ingress:
    - from:
        - podSelector:
            matchLabels:
              tier: api
      ports:
        - port: 5432
```

### 4.3 DNS Egress Policy

Pods need DNS resolution. Always include an egress rule to allow port 53:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns-egress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Egress
  egress:
    - ports:
        - port: 53
          protocol: UDP
        - port: 53
          protocol: TCP
```

---

## Section 5 — Admission Controllers and OPA Gatekeeper

### 5.1 Built-in Admission Controllers to Enable

| Controller | Purpose |
|---|---|
| NodeRestriction | Limits kubelet to modify only its own node/pods |
| PodSecurity | Enforces Pod Security Admission profiles |
| LimitRanger | Enforces resource limits in namespaces |
| ResourceQuota | Limits total resources per namespace |
| ServiceAccount | Automates SA token injection (also enables disabling it) |

### 5.2 OPA Gatekeeper Policy Catalog

Common Gatekeeper policies for production clusters:

| Policy | Description |
|---|---|
| k8srequiredlabels | Require specific labels on all pods |
| k8scontainerlimits | Require CPU/memory limits on all containers |
| k8sallowedrepos | Restrict image pull to approved registries only |
| k8snolatestimage | Block `:latest` tag on container images |
| k8sreadonlyrootfs | Require readOnlyRootFilesystem on all containers |
| k8sblockloadbalancer | Prevent LoadBalancer services in certain namespaces |

### 5.3 Approved Registry Policy Example

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8sallowedrepos
spec:
  crd:
    spec:
      names:
        kind: K8sAllowedRepos
      validation:
        openAPIV3Schema:
          properties:
            repos:
              type: array
              items:
                type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8sallowedrepos
        violation[{"msg": msg}] {
          container := input.review.object.spec.containers[_]
          not strings.any_prefix_match(
            container.image,
            input.parameters.repos
          )
          msg := sprintf("Image '%v' not from approved registry", [container.image])
        }
---
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sAllowedRepos
metadata:
  name: approved-registries
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
  parameters:
    repos:
      - "registry.company.com/"
      - "gcr.io/distroless/"
```

---

## Section 6 — Runtime Security and CIS Benchmark

### 6.1 Falco Rule Anatomy

```yaml
- rule: Write below root
  desc: An attempt to write to any file directly below / or /etc
  condition: >
    open_write and container
    and (fd.name startswith /etc or fd.directory = /)
    and not proc.name in (known_root_files_writers)
  output: >
    File below / or /etc opened for writing
    (user=%user.name target=%fd.name command=%proc.cmdline
    container=%container.name image=%container.image.repository)
  priority: ERROR
  tags: [filesystem, mitre_persistence]
```

### 6.2 Falco Integration Targets

```yaml
# falco.yaml output section
json_output: true
json_include_output_property: true

grpc:
  enabled: true
  bind_address: "0.0.0.0:5060"

program_output:
  enabled: true
  keep_alive: false
  program: "jq '{text: .output}' | curl -d @- -X POST https://hooks.slack.com/YOUR_WEBHOOK"
```

### 6.3 kube-bench CIS Check Categories

| Category | CIS Section | Key Checks |
|---|---|---|
| Control Plane | 1.x | API server TLS, audit log, anonymous auth |
| etcd | 2.x | Encryption at rest, TLS, client auth |
| Control Plane Config | 3.x | Scheduler, controller manager flags |
| Worker Node | 4.x | kubelet flags, node authentication |
| Kubernetes Policies | 5.x | RBAC, pod security policies, network policies |

---

## Exam Tips for DSOE Certification

- Role vs. ClusterRole: Role is namespace-scoped; ClusterRole is cluster-wide.
- RoleBinding can bind a ClusterRole but limits its scope to the binding's namespace.
- PSA replaces PodSecurityPolicy (deprecated in 1.21, removed in 1.25).
- PSA `enforce` mode rejects non-compliant pods at admission. Use `warn` first.
- Network Policies require a compatible CNI (Calico, Cilium) — Flannel does not enforce them.
- `podSelector: {}` with no `ingress` or `egress` defined blocks all traffic (default-deny).
- OPA Gatekeeper uses ConstraintTemplate (policy schema) + Constraint (policy instance).
- Falco monitors kernel syscalls via eBPF — it detects runtime threats not caught by admission controls.
- kube-bench automates CIS Kubernetes Benchmark checks — use it to assess cluster hardening status.
- `automountServiceAccountToken: false` prevents unnecessary API credential exposure in pods.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| RBAC | Role-Based Access Control — Kubernetes authorization mechanism |
| ServiceAccount | Kubernetes identity for workloads |
| Pod Security Admission (PSA) | Namespace-level pod security enforcement (replaces PSP) |
| Network Policy | Kubernetes resource defining allowed pod-to-pod communication |
| Admission Controller | Plugin intercepting API requests before persistence |
| OPA Gatekeeper | Kubernetes admission webhook using Rego policies |
| ConstraintTemplate | Gatekeeper resource defining a policy type schema |
| Constraint | Gatekeeper resource instantiating a policy from a template |
| Falco | Open-source runtime security tool monitoring kernel syscalls |
| kube-bench | Tool automating CIS Kubernetes Benchmark checks |
| etcd | Key-value store for all Kubernetes cluster state |
| CNI | Container Network Interface — plugin providing pod networking |

---

## 9. Supplemental Resources

**1. [Kubernetes RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)**
Official Kubernetes documentation covering Roles, ClusterRoles, RoleBindings, ClusterRoleBindings, ServiceAccounts, and RBAC best practices. Includes worked examples for common permission patterns and the principle of least privilege.

**2. [OPA Gatekeeper policy library](https://open-policy-agent.github.io/gatekeeper-library/website/)**
A curated library of pre-built OPA Gatekeeper ConstraintTemplates and Constraints covering pod security, allowed registries, resource limits, and more. Use this as a reference when designing admission control policies for real clusters.

**3. [Falco rules documentation and default rules reference](https://falco.org/docs/rules/)**
Official Falco documentation for writing and customizing detection rules, including all available fields, macros, and lists. Covers integration with Kubernetes audit logs, gRPC output, and alerting integrations with Slack and PagerDuty.

---

Reading Guide — Module 05 | CIS-4350 | Texas Wesleyan University | Professor Nash
