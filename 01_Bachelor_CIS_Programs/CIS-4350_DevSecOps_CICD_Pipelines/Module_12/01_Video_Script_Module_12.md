# Video Script: Module 12 — Kubernetes Security: RBAC, Network Policies, and Pod Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–2:00)

Welcome back to CIS-4350. I'm Professor Nash. In Module 11 we scanned container images for vulnerabilities before they reach the cluster. In this module we look at how to secure what runs inside the cluster: access control to the Kubernetes API, network traffic between pods, security constraints on containers themselves, and automated policy scanning of Kubernetes manifests in your CI/CD pipeline.

Kubernetes is a powerful orchestration platform, and that power creates a large attack surface if it is left at default settings. The default Kubernetes cluster allows containers to run as root, allows pods in any namespace to talk to pods in any other namespace, and allows any service account to call most Kubernetes API endpoints. In a DevSecOps program, we close those gaps systematically using four controls: Role-Based Access Control, Network Policies, Security Contexts, and the PodSecurity admission controller.

By the end of this module you will understand Kubernetes RBAC and how to create least-privilege service accounts for CI/CD pipelines, how to write Network Policies to implement default-deny segmentation, how to apply Security Contexts to harden container runtime behavior, how the PodSecurity admission controller enforces security standards at the namespace level, and how to scan Kubernetes manifests in CI using Checkov.

---

### SEGMENT 2 — Kubernetes RBAC (2:00–7:00)

Role-Based Access Control in Kubernetes is the primary mechanism for controlling who can do what to Kubernetes API resources. RBAC has four object types: Role, ClusterRole, RoleBinding, and ClusterRoleBinding.

A Role defines a set of permissions within a single namespace. A ClusterRole defines permissions across the entire cluster. A RoleBinding grants a Role or ClusterRole to a subject — a user, group, or service account — within a namespace. A ClusterRoleBinding grants a ClusterRole cluster-wide.

In a CI/CD context, the most important application of RBAC is creating a least-privilege service account for your deployment pipeline. Your pipeline should have exactly the permissions it needs to deploy your application and nothing more.

Here is a complete RBAC configuration for a CI/CD deployment service account:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ci-deployer
  namespace: app-prod

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: deployment-writer
  namespace: app-prod
rules:
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "create", "update", "patch"]
  - apiGroups: [""]
    resources: ["services", "configmaps"]
    verbs: ["get", "list", "create", "update", "patch"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: ci-deployer-binding
  namespace: app-prod
subjects:
  - kind: ServiceAccount
    name: ci-deployer
    namespace: app-prod
roleRef:
  kind: Role
  name: deployment-writer
  apiGroup: rbac.authorization.k8s.io
```

This service account can update Deployments, Services, and ConfigMaps in the `app-prod` namespace. It cannot read Secrets, cannot access other namespaces, and cannot modify RBAC objects themselves. This is the principle of least privilege applied to Kubernetes access control.

The most dangerous RBAC misconfiguration is granting `cluster-admin` to a CI/CD service account "because it is easier." Cluster-admin grants full control over the entire cluster including creating new RBAC objects — which an attacker who compromises the pipeline can use to escalate privileges further. Always use a Role scoped to the deployment namespace rather than a ClusterRole.

A second common mistake is using the `default` service account. Every pod in a namespace runs as the `default` service account unless otherwise specified. If your application pods and your CI/CD pipeline both use `default`, your application pods inherit pipeline permissions — or vice versa. Always create dedicated service accounts for each workload type.

---

### SEGMENT 3 — Kubernetes Network Policies (7:00–12:00)

By default, all pods in a Kubernetes cluster can communicate with all other pods across all namespaces. This means a compromised pod in a development namespace can potentially reach a database pod in a production namespace. Network Policies are Kubernetes resources that define allowed traffic flows — everything not explicitly allowed is denied when a policy applies to a pod.

The foundational pattern is a default-deny policy. Here is a default-deny-all Network Policy for a namespace:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: app-prod
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

The empty `podSelector: {}` matches all pods in the namespace. Listing both `Ingress` and `Egress` in `policyTypes` with no rules means no ingress or egress traffic is allowed unless a more specific policy permits it.

After applying the default-deny policy, you add specific allow policies. Here is a policy that allows the frontend to reach the API service:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-api
  namespace: app-prod
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

And a policy that allows the API to reach the database on port 5432:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-to-database
  namespace: app-prod
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

This three-policy set creates explicit micro-segmentation: frontend can reach API on 8080, API can reach database on 5432, and nothing else is permitted. A compromised frontend pod cannot make direct database connections — the network layer enforces the boundary.

One important nuance: Network Policies are enforced by the CNI plugin (Container Network Interface). Not all CNI plugins support Network Policies. Calico, Cilium, and Weave Net support them. Flannel does not. If you apply Network Policies on a cluster with a CNI that ignores them, the policies silently have no effect.

---

### SEGMENT 4 — Security Contexts (12:00–16:00)

Security Contexts configure the runtime security settings for a pod or container. They implement the principle of least privilege at the process level: containers should run with the minimum capabilities required to do their job.

Here is a hardened Security Context applied to a container:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-api
  namespace: app-prod
spec:
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000
      containers:
        - name: payment-api
          image: payment-api:v1.2.3
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
          volumeMounts:
            - name: tmp-dir
              mountPath: /tmp
      volumes:
        - name: tmp-dir
          emptyDir: {}
```

Let me walk through each field.

`runAsNonRoot: true` — the container will not start if the image's process runs as UID 0 (root). This is enforced by the kubelet before the container starts.

`runAsUser: 1000` — explicitly sets the UID. Prevents the container from running as root even if the image does not specify a USER instruction.

`allowPrivilegeEscalation: false` — prevents the process from gaining more privileges than it started with. Specifically, this sets the `no_new_privs` flag, which prevents SUID binaries from elevating privilege.

`readOnlyRootFilesystem: true` — the container filesystem is mounted read-only. The process cannot write to its own filesystem. This is the most effective single control against fileless malware that writes scripts to disk. When you set this, any application that needs to write temporary files must use an `emptyDir` volume, as shown in the volumes section.

`capabilities.drop: ALL` — removes all Linux capabilities from the container. By default, containers retain a small set of capabilities including `NET_BIND_SERVICE`, `CHOWN`, and `SETUID`. Dropping all capabilities removes the ability to perform privileged operations even as root. If your application needs a specific capability — for example, binding to a port below 1024 — you add it back explicitly with `capabilities.add`.

---

### SEGMENT 5 — PodSecurity Admission Controller (16:00–19:00)

Manually applying Security Contexts to every Deployment is error-prone — a developer might forget and deploy a container running as root. The PodSecurity admission controller enforces security standards at the namespace level, automatically rejecting pods that do not meet the configured standard.

PodSecurity defines three profiles:

`privileged` — no restrictions. Used for system namespaces like `kube-system`.

`baseline` — prevents the most dangerous privilege escalations. Blocks host network access, hostPID, hostIPC, privileged containers, and dangerous capabilities. This is the minimum standard for application workloads.

`restricted` — enforces the full Security Context hardening: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, and dropping all capabilities. This is the standard for production application namespaces.

You configure PodSecurity using namespace labels:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: app-prod
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/audit: restricted
```

The `enforce` label causes pods that violate the profile to be rejected at admission — the deployment fails. The `warn` label allows the pod but returns a warning. The `audit` label logs violations to the audit log without blocking. A common migration pattern is to set `warn` first to identify non-compliant workloads before switching to `enforce`.

---

### SEGMENT 6 — Checkov Kubernetes Scanning in CI (19:00–22:00)

Just as Checkov scans Terraform HCL for IaC misconfigurations, it scans Kubernetes YAML manifests for security policy violations. The same misconfigurations we just discussed — missing Security Contexts, overly permissive RBAC, absent Network Policies — are detectable by Checkov before the manifests reach the cluster.

Here is a GitHub Actions job that scans Kubernetes manifests with Checkov:

```yaml
k8s-scan:
  runs-on: ubuntu-latest
  needs: build
  permissions:
    security-events: write
    contents: read
  steps:
    - uses: actions/checkout@v4

    - name: Run Checkov on Kubernetes manifests
      uses: bridgecrewio/checkov-action@master
      with:
        directory: k8s/
        framework: kubernetes
        output_format: sarif
        output_file_path: checkov-k8s.sarif
        soft_fail: false

    - name: Upload Checkov results to GitHub Code Scanning
      uses: github/codeql-action/upload-sarif@v3
      if: always()
      with:
        sarif_file: checkov-k8s.sarif
```

Key Checkov checks for Kubernetes manifests include:

`CKV_K8S_6` — Do not admit containers that wish to share the host process ID namespace.

`CKV_K8S_8` — Use `readOnlyRootFilesystem: true`.

`CKV_K8S_15` — Containers should not run as root.

`CKV_K8S_20` — Containers should not allow privilege escalation.

`CKV_K8S_28` — Do not admit containers with added capabilities.

`CKV_K8S_30` — Do not admit root containers.

`CKV_K8S_37` — Minimize the admission of containers with added capabilities.

These checks translate your Security Context requirements into automated policy gates in the CI pipeline, catching misconfigurations before they are ever deployed to the cluster.

---

### SEGMENT 7 — Wrap-Up (22:00–24:00)

Kubernetes security is a layered discipline. RBAC controls who can call the Kubernetes API — least-privilege service accounts for CI/CD pipelines, scoped Roles rather than cluster-admin. Network Policies control how pods communicate — default-deny-all plus explicit allow rules creates the micro-segmentation model. Security Contexts control how containers run — no root, no privilege escalation, read-only filesystem, no capabilities. PodSecurity enforces those Security Context standards across namespaces automatically. And Checkov scans your manifests in CI before they ever reach the cluster.

None of these controls is sufficient alone. A cluster with RBAC but no Network Policies allows lateral movement between pods. A cluster with Network Policies but containers running as root is vulnerable to container escape. Defense in depth requires all layers working together.

In the next module we cover Compliance as Code — how to use Open Policy Agent and Rego to express your organization's security and compliance requirements as executable policies that your pipeline and Kubernetes admission controller enforce automatically.

See you there.

---

### PRODUCTION NOTES

- Screen share: `kubectl apply` of RBAC manifests and `kubectl auth can-i` verification
- Demo: Applying default-deny NetworkPolicy and showing blocked cross-pod communication
- Screen share: Security Context fields in a Deployment manifest
- Demo: PodSecurity namespace label enforcement rejecting a root container
- Screen share: Checkov GitHub Actions job with CKV_K8S_* findings in Code Scanning
- Slide: RBAC object type hierarchy (ServiceAccount → RoleBinding → Role)
- Slide: Network Policy allow-list model diagram
- Slide: Security Context field reference table
