# Lab 05 — Kubernetes Security: RBAC, Pod Security, and Network Policies

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will deploy a local Kubernetes cluster using kind (Kubernetes in Docker), configure RBAC with least-privilege service accounts, apply Pod Security Admission to enforce the Restricted profile, implement Network Policies using default-deny with selective allow, and run kube-bench to assess cluster hardening status against the CIS benchmark.

**Estimated Time:** 90–120 minutes

**Difficulty:** Intermediate–Advanced

---

## Prerequisites

- Docker Desktop running
- kind installed (`go install sigs.k8s.io/kind@latest` or binary download)
- kubectl installed
- Helm 3 installed (for Falco deployment, optional)
- `jq` installed for JSON parsing

---

## Part 1 — Cluster Setup and RBAC Configuration (30 minutes)

### Part 1 Objective

Create a multi-node kind cluster and configure RBAC with least-privilege service accounts.

### Step 1.1 — Create a kind Cluster

```bash
cat > kind-config.yaml << 'EOF'
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
name: lab05
nodes:
  - role: control-plane
  - role: worker
  - role: worker
EOF

kind create cluster --config kind-config.yaml
kubectl cluster-info --context kind-lab05
```

### Step 1.2 — Create Namespaces

```bash
kubectl create namespace production
kubectl create namespace development
```

### Step 1.3 — Deploy a Sample Application

```bash
cat > sample-app.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
  namespace: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api-service
  template:
    metadata:
      labels:
        app: api-service
        version: "1.0"
        team: platform
    spec:
      containers:
        - name: api
          image: nginx:1.25-alpine
          ports:
            - containerPort: 80
EOF

kubectl apply -f sample-app.yaml
kubectl get pods -n production
```

### Step 1.4 — Create a Least-Privilege ServiceAccount

```bash
cat > rbac-setup.yaml << 'EOF'
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-service-account
  namespace: production
automountServiceAccountToken: false
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: api-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: api-reader-binding
  namespace: production
subjects:
  - kind: ServiceAccount
    name: api-service-account
    namespace: production
roleRef:
  kind: Role
  name: api-reader
  apiGroup: rbac.authorization.k8s.io
EOF

kubectl apply -f rbac-setup.yaml
```

### Step 1.5 — Verify RBAC Permissions

```bash
# Confirm allowed actions
kubectl auth can-i get configmaps \
  --as=system:serviceaccount:production:api-service-account \
  -n production

# Confirm denied actions (should return "no")
kubectl auth can-i delete pods \
  --as=system:serviceaccount:production:api-service-account \
  -n production

kubectl auth can-i get secrets \
  --as=system:serviceaccount:production:api-service-account \
  -n production
```

Record the output of all three commands in your lab report.

---

## Part 2 — Pod Security Admission (25 minutes)

### Part 2 Objective

Enforce the Restricted Pod Security profile on the production namespace and observe rejection of non-compliant pods.

### Step 2.1 — Label the Production Namespace

```bash
kubectl label namespace production \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/enforce-version=latest \
  pod-security.kubernetes.io/warn=restricted \
  pod-security.kubernetes.io/audit=restricted

kubectl get namespace production --show-labels
```

### Step 2.2 — Attempt to Deploy a Privileged Pod

Create `privileged-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: privileged-test
  namespace: production
spec:
  containers:
    - name: test
      image: nginx:1.25-alpine
      securityContext:
        privileged: true
```

```bash
kubectl apply -f privileged-pod.yaml
```

The pod should be rejected with an error like:
`Error from server (Forbidden): pods "privileged-test" is forbidden: violates PodSecurity "restricted:latest": privileged`

### Step 2.3 — Deploy a Compliant Pod

Create `compliant-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: compliant-app
  namespace: production
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: nginx:1.25-alpine
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
        readOnlyRootFilesystem: true
      volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: run
          mountPath: /var/run
        - name: cache
          mountPath: /var/cache/nginx
  volumes:
    - name: tmp
      emptyDir: {}
    - name: run
      emptyDir: {}
    - name: cache
      emptyDir: {}
```

```bash
kubectl apply -f compliant-pod.yaml
kubectl get pod compliant-app -n production
```

---

## Part 3 — Network Policies (25 minutes)

### Part 3 Objective

Implement default-deny network policies and verify that only explicitly allowed traffic is permitted.

### Step 3.1 — Verify Current Connectivity (Pre-Policy)

```bash
# Get IP of compliant-app pod
POD_IP=$(kubectl get pod compliant-app -n production -o jsonpath='{.status.podIP}')
echo "Pod IP: $POD_IP"

# Launch a test pod and attempt to connect
kubectl run test-curl -n production \
  --image=curlimages/curl:latest \
  --restart=Never \
  --rm -it -- \
  curl --connect-timeout 3 http://$POD_IP/
```

Note whether the connection succeeds (it should before network policy is applied).

### Step 3.2 — Apply Default-Deny Policies

```bash
cat > default-deny.yaml << 'EOF'
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
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
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
EOF

kubectl apply -f default-deny.yaml
```

### Step 3.3 — Verify Connectivity is Blocked

```bash
kubectl run test-curl2 -n production \
  --image=curlimages/curl:latest \
  --restart=Never \
  --rm -it -- \
  curl --connect-timeout 3 http://$POD_IP/ || echo "Connection blocked as expected"
```

### Step 3.4 — Apply a Selective Allow Policy

```bash
cat > allow-api.yaml << 'EOF'
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-test-to-app
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: compliant-app
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              role: tester
      ports:
        - port: 80
EOF

kubectl apply -f allow-api.yaml

# Label the test pod and retry
kubectl run test-curl3 -n production \
  --image=curlimages/curl:latest \
  --labels="role=tester" \
  --restart=Never \
  --rm -it -- \
  curl --connect-timeout 3 http://$POD_IP/
```

---

## Part 4 — kube-bench CIS Benchmark Assessment (15 minutes)

### Part 4 Objective

Run kube-bench against the kind cluster and interpret the CIS benchmark results.

### Step 4.1 — Run kube-bench

```bash
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml
kubectl wait --for=condition=complete job/kube-bench --timeout=300s
kubectl logs job/kube-bench > kube-bench-results.txt
cat kube-bench-results.txt | head -100
```

### Step 4.2 — Count Findings by Category

```bash
grep -c "PASS" kube-bench-results.txt
grep -c "FAIL" kube-bench-results.txt
grep -c "WARN" kube-bench-results.txt
```

### Step 4.3 — Identify Top 3 FAIL Items

Review `kube-bench-results.txt` and identify the three highest-severity FAIL items. For each, note:

- The CIS check number
- The check description
- The remediation guidance provided by kube-bench

Record these in your lab report. Note: some findings are expected for a development kind cluster.

---

## Deliverables

Submit the following on Canvas:

1. Output of three `kubectl auth can-i` commands showing allowed and denied actions (Part 1, Step 1.5)
2. Screenshot of privileged pod rejection by PSA (Part 2, Step 2.2)
3. Screenshot of compliant pod running successfully (Part 2, Step 2.3)
4. Screenshot showing connectivity blocked by default-deny policy (Part 3, Step 3.3)
5. Screenshot showing selective allow restoring connectivity (Part 3, Step 3.4)
6. `kube-bench-results.txt` (Part 4, Step 4.1)
7. Written analysis of top 3 FAIL items with remediation steps (Part 4, Step 4.3 — minimum 150 words)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| RBAC auth can-i output — 3 commands with correct results | 15 |
| PSA rejection screenshot | 15 |
| Compliant pod running screenshot | 10 |
| Network policy block + allow screenshots | 20 |
| kube-bench results file submitted | 15 |
| Written analysis of 3 FAIL items | 25 |
| Total | 100 |

---

Lab 05 | CIS-4350 | Texas Wesleyan University | Professor Nash
