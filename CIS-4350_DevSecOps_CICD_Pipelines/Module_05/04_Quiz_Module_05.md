# Quiz: Module 05 - Container Orchestration Security: Kubernetes

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

A CI/CD system needs to update Kubernetes Deployments in the `staging` namespace as part of automated releases. Which RBAC configuration correctly implements the principle of least privilege?

- A) Grant the CI/CD service account the built-in `cluster-admin` ClusterRole to ensure it can always complete deployments
- B) Create a Role in the `staging` namespace with `update` and `patch` verbs on `deployments`, and bind it to the service account with a RoleBinding
- C) Create a ClusterRole with full read-write access to all resources and bind it to the service account with a ClusterRoleBinding
- D) Give the CI/CD service account direct SSH access to the Kubernetes API server host

#### Q1 Correct Answer

B — A namespace-scoped Role with only `update` and `patch` on `deployments`, bound via a RoleBinding, grants exactly the permissions needed for automated deployments — nothing more. The service account cannot read secrets, create new resources, modify other namespaces, or perform any cluster-level operations.

#### Q1 Distractor Analysis

- *Why A is incorrect:* `cluster-admin` grants full control of the entire cluster. A compromised CI/CD credential with `cluster-admin` is equivalent to a full cluster breach.
- *Why C is incorrect:* A ClusterRole with full read-write access grants permissions across all namespaces, far beyond what is needed to deploy to one namespace.
- *Why D is incorrect:* SSH access to the API server host bypasses all RBAC controls and is not an appropriate authentication method for CI/CD systems.

---

### Question 2

What does the Kubernetes Security Context field `allowPrivilegeEscalation: false` prevent?

- A) The pod from creating child processes that run with a different user ID
- B) The container process from gaining more privileges than it started with, such as through setuid binaries
- C) The pod from being scheduled on a node with elevated privileges
- D) The container image from being updated to a newer version during runtime

#### Q2 Correct Answer

B — `allowPrivilegeEscalation: false` sets the `no_new_privs` bit on the container process. This prevents the process from gaining elevated privileges through mechanisms like setuid binaries or capabilities that would otherwise allow privilege escalation inside the container.

#### Q2 Distractor Analysis

- *Why A is incorrect:* Child process user IDs are controlled by `runAsUser` and `runAsNonRoot`. `allowPrivilegeEscalation` specifically addresses privilege escalation via setuid mechanisms.
- *Why C is incorrect:* Node scheduling decisions are made by the scheduler. `allowPrivilegeEscalation` applies to the container process after scheduling, not to the scheduling decision itself.
- *Why D is incorrect:* Image version immutability is enforced by image pull policies (`imagePullPolicy: IfNotPresent`) and image digest pinning, not by Security Context.

---

### Question 3

A Kubernetes cluster has no Network Policies configured. An attacker compromises a pod running the frontend application. What can the attacker do from within that compromised pod?

- A) Nothing — Kubernetes automatically blocks all traffic between pods in different namespaces
- B) Reach any other pod in the cluster on any port, because Kubernetes defaults to allow-all pod-to-pod communication
- C) Only reach pods in the same namespace, because Kubernetes uses namespaces as network isolation boundaries
- D) Only reach pods that have explicitly declared the compromised pod as a dependency in their deployment manifest

#### Q3 Correct Answer

B — Without Network Policies, Kubernetes has a flat network model where all pods can communicate with all other pods on any port, regardless of namespace. An attacker in the frontend pod can probe and connect to database pods, internal APIs, monitoring systems, and any other service in the cluster.

#### Q3 Distractor Analysis

- *Why A is incorrect:* Kubernetes namespaces are logical organization units, not network isolation boundaries. They do not restrict pod-to-pod traffic by default.
- *Why C is incorrect:* This is a common misconception. Kubernetes namespaces do not provide network isolation. A pod in namespace A can reach pods in namespace B without any special configuration.
- *Why D is incorrect:* Kubernetes deployment manifests define application configuration, not network access control. There is no "dependency declaration" that restricts network access.

---

### Question 4

A DevSecOps team applies the following NetworkPolicy to the `production` namespace. What is the effect on pod-to-pod traffic?

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

- A) All traffic to pods matching the empty `podSelector` (which selects no pods) is blocked — other pods are unaffected
- B) All ingress and egress traffic for all pods in the `production` namespace is denied, because empty `podSelector` selects all pods
- C) Only external traffic from outside the cluster is blocked — internal pod-to-pod traffic is unaffected
- D) The policy has no effect because at least one pod must be explicitly named in the `podSelector` for a NetworkPolicy to apply

#### Q4 Correct Answer

B — An empty `podSelector: {}` selects ALL pods in the namespace. This is the standard pattern for implementing default-deny in Kubernetes. After applying this policy, all ingress and egress for every pod in the namespace is denied until explicitly permitted by additional Network Policies.

#### Q4 Distractor Analysis

- *Why A is incorrect:* Empty `podSelector: {}` is not "no pods" — it is "all pods". This is a counter-intuitive but critical Kubernetes behavior to know for the exam.
- *Why C is incorrect:* Network Policies apply to all traffic, including internal pod-to-pod traffic. External traffic filtering is a separate concern handled by ingress controllers and firewall rules.
- *Why D is incorrect:* An empty `podSelector` is a valid selector that matches all pods. Explicit pod names are not required.

---

### Question 5

Where does Kubernetes store all cluster state, including Secrets, and what is the default security concern with this storage?

- A) In a PostgreSQL database on the control plane node, encrypted with AES-256 by default
- B) In etcd, where Secrets are stored as base64-encoded data (not encrypted) by default
- C) In the container image registry, encrypted with the registry's TLS certificate
- D) In each worker node's local filesystem, encrypted with the node's disk encryption key

#### Q5 Correct Answer

B — Kubernetes stores all cluster state in etcd. Kubernetes Secrets are stored as base64-encoded values, which is encoding (not encryption) and is trivially reversible. Encryption at rest requires explicitly configuring an EncryptionConfiguration with an encryption provider (AES-GCM, AES-CBC, or KMS integration).

#### Q5 Distractor Analysis

- *Why A is incorrect:* Kubernetes uses etcd, not PostgreSQL, for cluster state storage. There is no default AES-256 encryption.
- *Why C is incorrect:* Container image registries store images, not cluster state or secrets.
- *Why D is incorrect:* Cluster state is centralized in etcd on the control plane, not distributed across worker node filesystems.

---

### Question 6

Which Kubernetes object would you use to grant a service account the ability to list nodes across all namespaces?

- A) A Role bound to the service account via a RoleBinding in the `default` namespace
- B) A ClusterRole bound to the service account via a ClusterRoleBinding
- C) A Role bound to the service account via a ClusterRoleBinding
- D) A RoleBinding that grants cluster-wide permissions by referencing the `kube-system` namespace

#### Q6 Correct Answer

B — Nodes are cluster-scoped resources (not namespace-scoped). Granting permissions on cluster-scoped resources requires a ClusterRole. To bind it to a service account cluster-wide, a ClusterRoleBinding is required.

#### Q6 Distractor Analysis

- *Why A is incorrect:* A Role is namespace-scoped and cannot grant permissions on cluster-level resources like nodes.
- *Why C is incorrect:* While a ClusterRoleBinding can reference a Role or ClusterRole, a Role scoped to one namespace cannot grant permissions on cluster-level resources like nodes. A ClusterRole is required.
- *Why D is incorrect:* Namespacing a RoleBinding to `kube-system` does not confer cluster-wide permissions. Cluster-wide permissions require a ClusterRoleBinding.

---

### Question 7

A pod specification sets `readOnlyRootFilesystem: true`. The application needs to write log files. What is the correct solution?

- A) Remove `readOnlyRootFilesystem: true` to allow the application to write logs
- B) Mount an `emptyDir` volume at the application's log directory path to provide a writable location while keeping the root filesystem read-only
- C) Run the container as root so it has permission to write to the read-only filesystem
- D) Use a ConfigMap to store log output, which bypasses the read-only filesystem restriction

#### Q7 Correct Answer

B — An `emptyDir` volume is a temporary directory backed by the node's local storage. Mounting it at the log directory path provides a writable location while the rest of the filesystem remains read-only. This is the standard Kubernetes pattern for applications with `readOnlyRootFilesystem: true`.

#### Q7 Distractor Analysis

- *Why A is incorrect:* Removing the security control to accommodate a writable log path is unnecessary and reduces security. The correct solution maintains the security control while accommodating the requirement.
- *Why C is incorrect:* Root privileges do not override a `readOnlyRootFilesystem: true` setting. The filesystem is read-only regardless of the running user's UID.
- *Why D is incorrect:* ConfigMaps are Kubernetes configuration objects, not log storage systems. Application processes cannot write to ConfigMaps during runtime.

---

### Question 8

What is the primary security risk of not setting `automountServiceAccountToken: false` on pods that do not need to call the Kubernetes API?

- A) The pod will fail to start because Kubernetes requires all pods to have an explicitly configured service account
- B) Every container in the pod has a ServiceAccount token mounted at a known path, which a compromised process could use to call the Kubernetes API with the pod's RBAC permissions
- C) The pod's network traffic will be automatically encrypted using the ServiceAccount token as a TLS certificate
- D) The ServiceAccount token is shared with all pods in the namespace, creating a single point of token compromise

#### Q8 Correct Answer

B — By default, Kubernetes mounts the pod's ServiceAccount token at `/var/run/secrets/kubernetes.io/serviceaccount/token` inside every container. If the application is compromised, the attacker can read this token and use it to make authenticated API server calls, potentially reading secrets or modifying other resources depending on the ServiceAccount's RBAC permissions.

#### Q8 Distractor Analysis

- *Why A is incorrect:* Pods do not require explicitly configured service accounts. They use the `default` service account if none is specified.
- *Why C is incorrect:* ServiceAccount tokens are bearer tokens for Kubernetes API authentication, not TLS certificates. They have no role in encrypting pod network traffic.
- *Why D is incorrect:* Each pod gets its own ServiceAccount token. Tokens are not shared between pods.

---

### Question 9

Which admission controller enforces Pod Security Standards (Privileged, Baseline, Restricted) at the namespace level in Kubernetes 1.25 and later?

- A) NetworkPolicy admission controller
- B) PodSecurityAdmission
- C) ResourceQuota admission controller
- D) LimitRanger admission controller

#### Q9 Correct Answer

B — PodSecurityAdmission (GA in Kubernetes 1.25) replaced the deprecated PodSecurityPolicy and enforces standardized security profiles at the namespace level. The `Restricted` profile enforces non-root execution, read-only filesystem, capability dropping, and other security settings.

#### Q9 Distractor Analysis

- *Why A is incorrect:* There is no "NetworkPolicy admission controller" as a named component. NetworkPolicies are enforced by the CNI plugin, not an admission controller.
- *Why C is incorrect:* ResourceQuota limits resource consumption (CPU, memory, pod count) per namespace. It does not enforce pod security settings.
- *Why D is incorrect:* LimitRanger sets default resource requests and limits for pods in a namespace. It does not enforce security settings like non-root execution.

---

### Question 10

A DevSecOps engineer wants to add Kubernetes manifest scanning to the CI/CD pipeline before any manifests are applied to the cluster. Which tool is designed for this purpose?

- A) Falco — which monitors running containers for anomalous behavior
- B) Checkov — which scans Kubernetes YAML manifests for security misconfigurations before deployment
- C) Trivy — which scans container images for CVEs after they are built
- D) Hadolint — which lints Dockerfile instructions for security violations

#### Q10 Correct Answer

B — Checkov is a static analysis tool for Infrastructure as Code that scans Kubernetes YAML manifests for misconfigurations: missing Security Contexts, exposed services, missing resource limits, and RBAC over-permissions. It runs in the CI/CD pipeline before `kubectl apply`, making it a shift-left control for Kubernetes security.

#### Q10 Distractor Analysis

- *Why A is incorrect:* Falco is a runtime security tool that monitors container system calls for anomalous behavior. It runs after deployment, not before.
- *Why C is incorrect:* Trivy scans container images for CVEs. While Trivy also has some manifest scanning capability, Checkov is the purpose-built IaC/manifest scanner.
- *Why D is incorrect:* Hadolint scans Dockerfile instructions for security violations. It analyzes Dockerfiles, not Kubernetes YAML manifests.
