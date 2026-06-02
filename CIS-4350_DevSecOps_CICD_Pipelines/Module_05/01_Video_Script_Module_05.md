# Video Script: Module 05 - Container Orchestration Security: Kubernetes

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 05 — Container Orchestration Security: Kubernetes"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. In Module 04 we secured individual Docker containers. Now we're scaling up: when you have hundreds or thousands of containers running across multiple hosts, you need an orchestration platform. That platform is Kubernetes — the dominant container orchestration system in enterprise DevSecOps environments.

Kubernetes introduces a new security model with its own attack surface. By the end of this video you'll understand the Kubernetes architecture from a security perspective, explain the RBAC model, configure Security Contexts, understand Network Policies, and know how to secure the Kubernetes API server. Kubernetes security has its own dedicated module later in this course (Module 12) — here we're building the foundational concepts."

---

### [01:30 - 06:00] Kubernetes Architecture and Security Model

**Visual:** Kubernetes architecture diagram — control plane (API server, etcd, scheduler, controller manager) and worker nodes (kubelet, kube-proxy, pods)

**Audio:**

"Let's start with the Kubernetes architecture and its security implications.

The Kubernetes control plane consists of four components. The API server is the central control point — every interaction with Kubernetes (kubectl commands, CI/CD deployments, pod scheduling) goes through the API server. This makes it the highest-value attack target in a Kubernetes cluster. The API server must be protected with authentication, authorization (RBAC), and network access controls.

etcd is the key-value store that holds all cluster state — pod definitions, secrets, service configurations, certificates. etcd stores Kubernetes Secrets in base64 encoding by default, which is not encryption. Encryption at rest for etcd must be explicitly configured. Compromising etcd is equivalent to compromising the entire cluster.

The scheduler assigns pods to nodes. The controller manager runs control loops that maintain desired state (e.g., ensuring the right number of pod replicas are running).

Worker nodes run the actual workloads. Each worker node has a kubelet — the agent that communicates with the API server and manages pods on the node. The kubelet has a local API that must be secured against unauthorized access.

From a DevSecOps pipeline perspective, the CI/CD system interacts with the Kubernetes API server to deploy workloads. This means the CI/CD system needs credentials to authenticate to the Kubernetes API — and those credentials must be tightly scoped using RBAC."

---

### [06:00 - 11:00] Kubernetes RBAC Model

**Visual:** RBAC diagram — Subject (User/ServiceAccount) → RoleBinding → Role → Resources/Verbs

**Audio:**

"Role-Based Access Control — RBAC — is the authorization model in Kubernetes. Understanding RBAC is one of the highest-priority Kubernetes topics on the DevSecOps Professional exam.

RBAC in Kubernetes has four key objects: Role, ClusterRole, RoleBinding, and ClusterRoleBinding.

A **Role** defines a set of permissions within a specific namespace. Permissions specify what API resources (pods, services, deployments) can be accessed and what verbs (get, list, watch, create, update, delete) are allowed.

A **ClusterRole** defines permissions across the entire cluster, not limited to a namespace. ClusterRoles are used for cluster-wide resources like nodes, persistent volumes, and namespaces themselves.

A **RoleBinding** grants the permissions defined in a Role to a subject (a user, group, or service account) within a specific namespace.

A **ClusterRoleBinding** grants a ClusterRole to a subject cluster-wide.

**[SHOW CODE]**

Here is an RBAC configuration for a CI/CD deployment service account — the principle of least privilege applied to Kubernetes:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ci-deployer
  namespace: production

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: deployment-manager
  namespace: production
rules:
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "update", "patch"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: ci-deployer-binding
  namespace: production
subjects:
  - kind: ServiceAccount
    name: ci-deployer
    namespace: production
roleRef:
  kind: Role
  name: deployment-manager
  apiGroup: rbac.authorization.k8s.io
```

This creates a service account `ci-deployer` that can only update deployments and read pods in the `production` namespace. It cannot create new resources, access secrets, delete deployments, or touch any other namespace. This is the correct least-privilege model for a CI/CD deployment credential.

The most dangerous RBAC misconfiguration — and the one most frequently tested on exams — is granting `cluster-admin` to a service account. `cluster-admin` has full control of the entire cluster. A compromised CI/CD credential with `cluster-admin` is a full cluster compromise."

---

### [11:00 - 16:00] Security Contexts and Pod Security

**Visual:** Pod specification YAML with securityContext highlighted

**Audio:**

"Security Contexts in Kubernetes apply the same principle we used in Docker — running as non-root, dropping capabilities, read-only filesystems — but at the pod and container specification level.

**[SHOW CODE]**

Here is a pod specification with a comprehensive Security Context:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
  namespace: production
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
      image: myapp:1.2.3
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
          add:
            - NET_BIND_SERVICE
      resources:
        limits:
          memory: "256Mi"
          cpu: "500m"
        requests:
          memory: "128Mi"
          cpu: "250m"
      volumeMounts:
        - name: tmp-dir
          mountPath: /tmp

  volumes:
    - name: tmp-dir
      emptyDir: {}
```

Let me walk through the security fields.

`runAsNonRoot: true` — Kubernetes will refuse to start the pod if the container image runs as root. This is an admission control check.

`runAsUser: 1001` — enforces that the process runs as UID 1001, not root.

`allowPrivilegeEscalation: false` — prevents the container process from gaining more privileges than it starts with (e.g., via setuid binaries).

`readOnlyRootFilesystem: true` — mounts the container's root filesystem read-only. The `tmp-dir` volume mount provides a writable temporary directory for applications that need to write files.

`capabilities: drop: [ALL]` — drops all Linux capabilities. `add: [NET_BIND_SERVICE]` adds back only what is needed.

`seccompProfile: RuntimeDefault` — enables the default seccomp (system call filtering) profile, blocking a large set of dangerous system calls.

Resource limits (`memory` and `cpu`) prevent denial-of-service attacks where a compromised container consumes all node resources."

---

### [16:00 - 20:00] Network Policies and API Server Security

**Visual:** Kubernetes Network Policy diagram showing allowed and denied traffic paths

**Audio:**

"By default, Kubernetes allows all pod-to-pod communication within the cluster — any pod can reach any other pod on any port. This flat network model means that if an attacker compromises one pod, they can reach all other pods in the cluster. Network Policies change this.

**[SHOW CODE]**

A Network Policy that implements a default-deny posture and then allows only specific traffic:

```yaml
# Default deny all ingress and egress
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

---
# Allow frontend pods to reach backend pods on port 8080
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
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

The first policy selects all pods in the `production` namespace and denies all ingress and egress by default. The second policy explicitly allows frontend pods to reach backend pods on port 8080. Any other traffic — backend to database on an unspecified port, compromised pod to external internet — is blocked.

For API server security: the Kubernetes API server should not be exposed to the public internet. Access should be restricted to management networks and CI/CD systems via firewall rules. Audit logging should be enabled to record all API server requests for forensic purposes."

---

### [20:00 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know the four RBAC objects — Role, ClusterRole, RoleBinding, ClusterRoleBinding — and how they combine to grant permissions. Know that `cluster-admin` is the most dangerous RBAC assignment. Know Security Context fields: `runAsNonRoot`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, and capability dropping. Know that Kubernetes Network Policies are deny-by-default additive rules — you must explicitly start with a default-deny policy.

Modules 12 covers Kubernetes security in depth. Complete the lab and quiz for this module before moving on to Module 06."
