# Lab Activity: Module 05 - Container Orchestration Security: Kubernetes

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Write Kubernetes RBAC configurations implementing least-privilege service accounts.
- Configure Security Contexts for pods following all six key security fields.
- Write Network Policies implementing default-deny with explicit allowlists.
- Analyze Kubernetes manifest files for security misconfigurations.

---

## Prerequisites

Before beginning this lab, confirm the following:

- You have a Kubernetes environment available: minikube, kind, Docker Desktop Kubernetes, or a cloud cluster.
- `kubectl` is installed and configured (`kubectl version` returns a result).
- You have completed the Module 05 video and reading guide.

To install minikube (macOS/Linux):

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start
```

---

## Part 1: RBAC Configuration for CI/CD Service Account (30 points)

### Part 1 Background

A CI/CD system needs to update deployments in the `production` namespace as part of automated deployments. This part requires you to write the minimal RBAC configuration — a ServiceAccount, Role, and RoleBinding — that grants only the required permissions.

### Part 1 Instructions

**Step 1: Create the production namespace.**

```bash
kubectl create namespace production
```

**Step 2: Write the RBAC configuration.**

Create a file named `ci-rbac.yaml`. The configuration must include:

- A `ServiceAccount` named `ci-deployer` in the `production` namespace.
- A `Role` named `deployment-manager` in the `production` namespace granting:
  - `update` and `patch` verbs on `deployments` in the `apps` API group.
  - `get` and `list` verbs on `pods` in the core API group.
  - No other permissions — not `create`, not `delete`, not access to `secrets`.
- A `RoleBinding` named `ci-deployer-binding` that binds `ci-deployer` ServiceAccount to the `deployment-manager` Role, both in the `production` namespace.

Apply the configuration:

```bash
kubectl apply -f ci-rbac.yaml
```

**Step 3: Verify the permissions using kubectl auth can-i.**

```bash
# This should return "yes"
kubectl auth can-i update deployments --namespace production --as system:serviceaccount:production:ci-deployer

# This should return "no"
kubectl auth can-i get secrets --namespace production --as system:serviceaccount:production:ci-deployer

# This should return "no"
kubectl auth can-i create deployments --namespace production --as system:serviceaccount:production:ci-deployer
```

Record all three outputs.

**Step 4: Analyze the cluster-admin risk.**

In 3-4 sentences, explain what would happen if the CI/CD pipeline's service account had `cluster-admin` privileges and the CI/CD system was compromised by a supply chain attack. What resources could the attacker access or modify?

### Part 1 Deliverable

Submit: your complete `ci-rbac.yaml` file, the three `kubectl auth can-i` outputs, and your cluster-admin risk analysis.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| ServiceAccount, Role, and RoleBinding are correctly defined | 12 |
| Role grants only the specified verbs (no excess permissions) | 8 |
| All three auth can-i checks produce the expected output | 6 |
| cluster-admin risk analysis is technically accurate | 4 |

---

## Part 2: Pod Security Context Configuration (30 points)

### Part 2 Background

Security Contexts enforce least-privilege execution at the Kubernetes pod level. This part requires writing a secure pod specification that applies all key Security Context settings.

### Part 2 Instructions

**Step 1: Write a secure pod manifest.**

Create a file named `secure-pod.yaml`. The pod specification must include all of the following Security Context settings:

Pod-level security context:

- `runAsNonRoot: true`
- `runAsUser: 1001`
- `fsGroup: 1001`
- `seccompProfile.type: RuntimeDefault`

Container-level security context:

- `allowPrivilegeEscalation: false`
- `readOnlyRootFilesystem: true`
- `capabilities.drop: [ALL]`

Additional requirements:

- The pod must define resource limits for memory (256Mi) and CPU (500m).
- The pod must use an `emptyDir` volume mounted at `/tmp` to provide writable temporary storage.
- The pod should use a real, minimal image (e.g., `busybox:1.36` or `alpine:3.19`) for the lab.
- The container command should sleep to keep the pod running: `["sleep", "3600"]`.

Apply and verify:

```bash
kubectl apply -f secure-pod.yaml -n production
kubectl get pod secure-app -n production
kubectl describe pod secure-app -n production
```

**Step 2: Attempt to write to the root filesystem (expected to fail).**

```bash
kubectl exec -n production secure-app -- sh -c "echo test > /test.txt"
```

The command should fail with a read-only filesystem error. Record the output.

**Step 3: Verify the running user.**

```bash
kubectl exec -n production secure-app -- id
```

The output should show UID 1001, not 0. Record the output.

**Step 4: Analyze a misconfigured pod manifest.**

Review the following pod specification and identify all Security Context violations:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: insecure-app
spec:
  containers:
    - name: app
      image: myapp:latest
      securityContext:
        allowPrivilegeEscalation: true
        runAsUser: 0
      env:
        - name: DB_PASSWORD
          value: "plaintextpassword"
```

List every security problem and the correct remediation for each.

### Part 2 Deliverable

Submit: your `secure-pod.yaml`, the read-only filesystem error output, the `id` output confirming UID 1001, and your insecure pod analysis.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| secure-pod.yaml applies all required pod-level security context fields | 8 |
| secure-pod.yaml applies all required container-level security context fields | 8 |
| Read-only filesystem error is documented | 4 |
| UID verification shows 1001 | 4 |
| Insecure pod analysis identifies all problems with correct remediations | 6 |

---

## Part 3: Network Policy — Default Deny and Allowlist (25 points)

### Part 3 Background

Kubernetes does not enforce network isolation by default. This part implements the default-deny pattern followed by explicit allowlist policies.

### Part 3 Instructions

**Step 1: Write the default-deny Network Policy.**

Create a file named `network-policies.yaml`. The first policy must select all pods in the `production` namespace and deny all ingress and egress traffic.

**Step 2: Add an allowlist policy.**

In the same `network-policies.yaml` file, add a second Network Policy that allows:

- Ingress to pods labeled `app: backend` on TCP port 8080 from pods labeled `app: frontend`.
- No other ingress or egress is permitted unless separately defined.

**Step 3: Apply the policies.**

```bash
kubectl apply -f network-policies.yaml -n production
kubectl get networkpolicies -n production
```

Record the output showing both policies applied.

**Step 4: Explain the default-allow problem.**

In 3-4 sentences, explain why Kubernetes' default-allow network model is a security risk in a production cluster. Specifically, describe what an attacker who compromises one pod can do in a cluster without Network Policies, and how the default-deny pattern limits the blast radius of a pod compromise.

### Part 3 Deliverable

Submit: your `network-policies.yaml` file, the `kubectl get networkpolicies` output, and your default-allow risk explanation.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| Default-deny policy is correctly structured and selects all pods | 8 |
| Allowlist policy correctly permits only the specified traffic | 8 |
| kubectl output shows both policies applied | 4 |
| Default-allow risk explanation is technically accurate | 5 |

---

## Part 4: Reflection on Kubernetes vs. Docker Security (15 points)

### Part 4 Instructions

Write a 200-250 word reflection addressing the following:

Module 04 covered Docker container security: non-root users via the `USER` Dockerfile directive, capability dropping at runtime with `--cap-drop ALL`, and resource limits. Module 05 covers the same concepts but in Kubernetes Security Context: `runAsNonRoot`, `capabilities.drop: [ALL]`, and resource limits in the pod spec.

1. Explain why both levels of enforcement are necessary — why is it insufficient to rely solely on the Dockerfile `USER` directive without also enforcing `runAsNonRoot: true` in the Security Context?
2. Explain the defense-in-depth argument for having security controls at both the image level (Dockerfile) and the orchestration level (Security Context).
3. Identify one Kubernetes-specific security control that has no Docker equivalent for standalone containers, and explain what protection it provides.

### Part 4 Deliverable

Submit your written reflection (200-250 words) as part of your combined submission document.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Explanation of why both Dockerfile and Security Context controls are needed | 6 |
| Defense-in-depth argument is technically sound | 5 |
| Kubernetes-specific control identified correctly with accurate explanation | 4 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (05) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
