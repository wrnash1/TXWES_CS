# Lab Activity: Module 12 — Kubernetes Security: RBAC, Network Policies, and Pod Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Create least-privilege RBAC manifests for a CI/CD deployment service account.
- Write and apply a default-deny Network Policy and allowlist policies.
- Apply a hardened Security Context to a container Deployment.
- Configure a namespace with PodSecurity enforcement labels.
- Integrate Checkov Kubernetes manifest scanning into a GitHub Actions pipeline.

---

## Prerequisites

Before beginning this lab, confirm the following:

- `kubectl` is installed and configured to access a local cluster (minikube, kind, or Docker Desktop Kubernetes).
- Checkov is installed (`checkov --version`). Install with `pip install checkov`.
- You have a GitHub repository from earlier modules.
- You have completed the Module 12 video and reading guide.

---

## Part 1: RBAC — Least-Privilege CI/CD Service Account (25 points)

### Part 1 Background

The goal of this part is to create a dedicated service account for a hypothetical CI/CD deployment job and verify it has only the minimum required permissions. You will use `kubectl auth can-i` to confirm allowed and denied operations.

### Part 1 Instructions

**Step 1: Create the namespace and service account.**

Create a file named `rbac-lab.yaml` with the following content:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: lab-prod

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ci-deployer
  namespace: lab-prod
```

Apply it:

```bash
kubectl apply -f rbac-lab.yaml
```

**Step 2: Create the Role.**

Add to `rbac-lab.yaml` a Role named `deployment-writer` in the `lab-prod` namespace. The role must grant `get`, `list`, `create`, `update`, and `patch` verbs on the following resources:

- `deployments` in the `apps` API group
- `services` and `configmaps` in the core API group (`""`)

The role must NOT grant access to `secrets`.

**Step 3: Create the RoleBinding.**

Add a RoleBinding that binds `deployment-writer` to the `ci-deployer` ServiceAccount in `lab-prod`.

**Step 4: Verify permissions with `kubectl auth can-i`.**

Run the following commands and record each result (yes/no):

```bash
kubectl auth can-i create deployments --namespace=lab-prod \
  --as=system:serviceaccount:lab-prod:ci-deployer

kubectl auth can-i patch services --namespace=lab-prod \
  --as=system:serviceaccount:lab-prod:ci-deployer

kubectl auth can-i get secrets --namespace=lab-prod \
  --as=system:serviceaccount:lab-prod:ci-deployer

kubectl auth can-i create deployments --namespace=default \
  --as=system:serviceaccount:lab-prod:ci-deployer
```

The first two should return `yes`. The last two should return `no`. Record all four results.

### Part 1 Deliverable

Submit: the complete `rbac-lab.yaml` manifest and the four `kubectl auth can-i` output lines with a one-sentence explanation of why the `secrets` check and the `default` namespace check return `no`.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Role correctly grants the required verbs on the correct resources | 8 |
| Role does not grant access to Secrets | 4 |
| RoleBinding correctly binds to the ServiceAccount | 5 |
| All four `auth can-i` results are recorded and accurate | 5 |
| Explanation of `no` results is technically correct | 3 |

---

## Part 2: Network Policy — Default Deny and Allowlist (25 points)

### Part 2 Background

This part implements the micro-segmentation model: a default-deny policy for a namespace, followed by specific allow rules that permit only the required traffic flows.

### Part 2 Instructions

**Step 1: Deploy test pods.**

Apply the following pod manifest to create three labeled pods in `lab-prod`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
  namespace: lab-prod
  labels:
    app: frontend
spec:
  containers:
    - name: frontend
      image: nginx:alpine

---
apiVersion: v1
kind: Pod
metadata:
  name: api
  namespace: lab-prod
  labels:
    app: api
spec:
  containers:
    - name: api
      image: nginx:alpine

---
apiVersion: v1
kind: Pod
metadata:
  name: database
  namespace: lab-prod
  labels:
    app: database
spec:
  containers:
    - name: database
      image: nginx:alpine
```

**Step 2: Verify open communication before applying policies.**

Run a connectivity test from frontend to api (port 80) before any Network Policy is applied:

```bash
kubectl exec -n lab-prod frontend -- wget -qO- --timeout=3 http://api.lab-prod.svc.cluster.local/
```

Record the result (success or timeout).

**Step 3: Apply the default-deny policy.**

Create `netpol-lab.yaml` with a NetworkPolicy named `default-deny-all` in `lab-prod` that denies all ingress and egress. Use `podSelector: {}` and list both `Ingress` and `Egress` in `policyTypes` with no rules.

Apply it and re-run the connectivity test from Step 2. Record the result (should now be timeout).

**Step 4: Add allowlist policies.**

Add two more NetworkPolicy objects to `netpol-lab.yaml`:

- Allow ingress to `app: api` from `app: frontend` on port 80
- Allow ingress to `app: database` from `app: api` on port 80

Apply and run these tests:

```bash
kubectl exec -n lab-prod frontend -- wget -qO- --timeout=3 http://api.lab-prod.svc.cluster.local/
kubectl exec -n lab-prod api -- wget -qO- --timeout=3 http://database.lab-prod.svc.cluster.local/
kubectl exec -n lab-prod frontend -- wget -qO- --timeout=3 http://database.lab-prod.svc.cluster.local/
```

Record all three results. Frontend-to-API and API-to-database should succeed. Frontend-to-database should time out.

### Part 2 Deliverable

Submit: the complete `netpol-lab.yaml` manifest, the four connectivity test results (before deny, after deny, after allowlist x3), and a two-sentence explanation of why the frontend-to-database test still fails even after adding the allowlist policies.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Default-deny policy uses correct `podSelector: {}` syntax with no rules | 8 |
| Allowlist policies correctly reference labels and ports | 8 |
| All four connectivity test results are recorded | 5 |
| Explanation of frontend-to-database failure is technically correct | 4 |

---

## Part 3: Security Context Hardening (25 points)

### Part 3 Background

This part applies a hardened Security Context to a Deployment and verifies that the runtime constraints are enforced. You will observe what happens when an application tries to write to a read-only filesystem without an emptyDir volume, then fix it.

### Part 3 Instructions

**Step 1: Deploy without Security Context.**

Create `deployment-lab.yaml` with a basic Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  namespace: lab-prod
spec:
  replicas: 1
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: webapp
          image: nginx:alpine
          ports:
            - containerPort: 80
```

Apply and confirm the pod starts successfully. Record the pod status.

**Step 2: Add Security Context fields.**

Update the Deployment to add the following fields:

- Pod-level `securityContext`: `runAsNonRoot: true`, `runAsUser: 1000`
- Container-level `securityContext`: `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, `capabilities.drop: [ALL]`

Apply the updated manifest. Observe whether the pod starts successfully. Record the pod status and any error messages from `kubectl describe pod`.

The nginx image requires write access to `/var/cache/nginx`, `/var/run`, and `/tmp`. The pod will fail with `readOnlyRootFilesystem: true` without emptyDir volumes for these paths.

**Step 3: Add emptyDir volumes.**

Update the Deployment to add `emptyDir` volume mounts for `/var/cache/nginx`, `/var/run`, and `/tmp`. Apply and confirm the pod starts and is Running.

**Step 4: Verify Security Context enforcement.**

Run the following commands against the running pod and record the output:

```bash
kubectl exec -n lab-prod deploy/webapp -- id
kubectl exec -n lab-prod deploy/webapp -- touch /testfile
kubectl exec -n lab-prod deploy/webapp -- touch /tmp/testfile
```

The `id` command should show a non-root UID. The write to `/testfile` (root of the filesystem) should fail. The write to `/tmp/testfile` should succeed because `/tmp` is an emptyDir volume.

### Part 3 Deliverable

Submit: the final `deployment-lab.yaml` with all Security Context fields and emptyDir volumes, the pod status from each step, the three `kubectl exec` outputs with explanation of each result, and a two-sentence explanation of why `emptyDir` volumes are required with `readOnlyRootFilesystem: true`.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| All five Security Context fields are correctly applied | 10 |
| Three emptyDir volumes are correctly mounted | 6 |
| Pod status progression (fail then pass) is recorded | 5 |
| `kubectl exec` outputs demonstrate correct enforcement | 4 |

---

## Part 4: Checkov Kubernetes Manifest Scanning in CI (25 points)

### Part 4 Background

This part integrates Checkov Kubernetes manifest scanning into a GitHub Actions pipeline, catching Security Context and RBAC misconfigurations before manifests are applied to the cluster.

### Part 4 Instructions

**Step 1: Run Checkov locally on the insecure deployment from Step 1 of Part 3.**

```bash
checkov -f deployment-lab.yaml --framework kubernetes
```

Record the check IDs that fail and the corresponding policy descriptions.

**Step 2: Run Checkov on the hardened deployment from Step 3 of Part 3.**

```bash
checkov -f deployment-lab.yaml --framework kubernetes
```

Record how many checks pass versus fail. Document any checks that still fail and explain why.

**Step 3: Add a Kubernetes manifest scan job to your GitHub Actions pipeline.**

In `full-pipeline.yml`, add a `k8s-scan` job with the following requirements:

- Runs on `ubuntu-latest`
- Checks out code with `actions/checkout@v4`
- Uses `bridgecrewio/checkov-action@master` with `directory: k8s/`, `framework: kubernetes`, `output_format: sarif`, `output_file_path: checkov-k8s.sarif`, `soft_fail: false`
- Uploads the SARIF file using `github/codeql-action/upload-sarif@v3` with `if: always()`

**Step 4: Create a `k8s/` directory in your repository.**

Place an intentionally non-compliant Deployment manifest (missing Security Context fields) in `k8s/deployment.yaml`. Push to a feature branch. Observe the `k8s-scan` job failing in the Actions tab.

**Step 5: Update the manifest with the hardened Security Context.**

Push the corrected manifest and observe the `k8s-scan` job passing.

**Step 6: Screenshot both pipeline states.**

Capture the failing scan output showing CKV_K8S_* check failures and the passing scan.

### Part 4 Deliverable

Submit: the Checkov local output tables from Steps 1 and 2, the complete `k8s-scan` job YAML, screenshots of the failing and passing pipeline runs, and a one-paragraph explanation of why `soft_fail: false` is the correct setting for a Kubernetes manifest scan gate in production.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Checkov local output tables are complete and accurate | 6 |
| Pipeline job YAML includes all required parameters | 8 |
| Screenshot shows failing pipeline with CKV_K8S_* findings | 6 |
| Screenshot shows passing pipeline after manifest correction | 3 |
| `soft_fail: false` explanation is technically correct | 2 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (12) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
