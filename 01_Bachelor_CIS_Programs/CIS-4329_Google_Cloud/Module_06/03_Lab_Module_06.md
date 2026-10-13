# Lab: Module 06 — Google Kubernetes Engine (GKE)

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Lab Overview

In this lab you will create a GKE cluster, deploy a containerized application,
expose it with a Service and Ingress, configure the Horizontal Pod Autoscaler,
and observe Cluster Autoscaler behavior.

**Estimated Time:** 90 minutes

**Prerequisites:**

- Active GCP project with billing enabled
- Kubernetes Engine API enabled
- Container Registry or Artifact Registry API enabled
- Cloud Shell access with kubectl pre-installed

**Learning Objectives:**

By the end of this lab you will be able to:

1. Create a GKE Standard regional cluster
2. Configure kubectl to connect to the cluster
3. Deploy an application using kubectl and YAML manifests
4. Expose the application via a LoadBalancer Service and Ingress
5. Configure and observe the Horizontal Pod Autoscaler
6. Add a node pool and use taints and tolerations

---

## Part 1 — Create a GKE Cluster (15 minutes)

### Step 1.1 — Enable APIs and Set Environment

```bash
gcloud services enable container.googleapis.com

export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
export CLUSTER=lab06-cluster
```

### Step 1.2 — Create a Regional Standard Cluster

```bash
gcloud container clusters create $CLUSTER \
  --region=$REGION \
  --num-nodes=2 \
  --machine-type=e2-medium \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=4 \
  --release-channel=regular

# Monitor cluster creation (takes 3-5 minutes)
gcloud container clusters list
```

### Step 1.3 — Configure kubectl

```bash
# Get credentials for kubectl
gcloud container clusters get-credentials $CLUSTER \
  --region=$REGION

# Verify connection
kubectl cluster-info
kubectl get nodes -o wide
```

---

## Part 2 — Deploy an Application (20 minutes)

### Step 2.1 — Create Deployment Manifest

```bash
cat > deployment.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-app
  labels:
    app: hello-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-app
  template:
    metadata:
      labels:
        app: hello-app
    spec:
      containers:
        - name: hello-app
          image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: "100m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "128Mi"
EOF
```

### Step 2.2 — Apply the Deployment

```bash
kubectl apply -f deployment.yaml

# Monitor rollout
kubectl rollout status deployment/hello-app

# List pods
kubectl get pods -o wide

# Describe one pod
POD_NAME=$(kubectl get pods -l app=hello-app -o jsonpath='{.items[0].metadata.name}')
kubectl describe pod $POD_NAME
```

### Step 2.3 — Create a LoadBalancer Service

```bash
cat > service-lb.yaml << 'EOF'
apiVersion: v1
kind: Service
metadata:
  name: hello-app-svc
spec:
  type: LoadBalancer
  selector:
    app: hello-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
EOF

kubectl apply -f service-lb.yaml

# Wait for the external IP (1-3 minutes)
kubectl get service hello-app-svc --watch
```

### Step 2.4 — Test the Service

```bash
LB_IP=$(kubectl get service hello-app-svc \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo "Service IP: $LB_IP"

# Test the application
curl http://$LB_IP

# Run multiple requests to see load balancing
for i in {1..5}; do curl -s http://$LB_IP; done
```

---

## Part 3 — Deploy a Second Service and Ingress (20 minutes)

### Step 3.1 — Deploy a Second Application

```bash
cat > deployment-v2.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-app-v2
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-app-v2
  template:
    metadata:
      labels:
        app: hello-app-v2
    spec:
      containers:
        - name: hello-app-v2
          image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: "100m"
              memory: "64Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: hello-app-v2-svc
spec:
  type: NodePort
  selector:
    app: hello-app-v2
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
EOF

kubectl apply -f deployment-v2.yaml

# Convert first service to NodePort for Ingress
kubectl patch service hello-app-svc -p '{"spec":{"type":"NodePort"}}'
```

### Step 3.2 — Create an Ingress

```bash
cat > ingress.yaml << 'EOF'
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-ingress
  annotations:
    kubernetes.io/ingress.class: "gce"
spec:
  defaultBackend:
    service:
      name: hello-app-svc
      port:
        number: 80
  rules:
    - http:
        paths:
          - path: /v2
            pathType: Prefix
            backend:
              service:
                name: hello-app-v2-svc
                port:
                  number: 80
EOF

kubectl apply -f ingress.yaml

# Wait for the ingress to get an external IP (5-10 minutes)
kubectl get ingress hello-ingress --watch
```

### Step 3.3 — Test Path-Based Routing

```bash
INGRESS_IP=$(kubectl get ingress hello-ingress \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

# Test default route (v1)
curl http://$INGRESS_IP

# Test v2 path
curl http://$INGRESS_IP/v2
```

---

## Part 4 — Horizontal Pod Autoscaler (15 minutes)

### Step 4.1 — Create an HPA

```bash
kubectl autoscale deployment hello-app \
  --cpu-percent=50 \
  --min=2 \
  --max=8

# View HPA status
kubectl get hpa
kubectl describe hpa hello-app
```

### Step 4.2 — Generate Load to Trigger Scaling

```bash
# Open a separate Cloud Shell tab and run this load generator
# (or run in background with &)
kubectl run load-generator \
  --image=busybox:stable \
  --restart=Never \
  --command -- /bin/sh -c \
  "while true; do wget -q -O- http://hello-app-svc; done" &

# In the first tab, watch HPA and pods scale
watch -n5 kubectl get hpa hello-app
kubectl get pods -l app=hello-app --watch
```

### Step 4.3 — Stop the Load

```bash
# Delete the load generator pod
kubectl delete pod load-generator

# Watch pods scale back down (takes several minutes due to cooldown)
kubectl get hpa hello-app --watch
```

---

## Part 5 — Add a Node Pool (10 minutes)

### Step 5.1 — Create a New Node Pool with a Taint

```bash
gcloud container node-pools create batch-pool \
  --cluster=$CLUSTER \
  --region=$REGION \
  --machine-type=e2-small \
  --num-nodes=1 \
  --node-taints=workload=batch:NoSchedule

# Verify the new pool
gcloud container node-pools list \
  --cluster=$CLUSTER \
  --region=$REGION
```

### Step 5.2 — Deploy a Pod with a Toleration

```bash
cat > batch-job.yaml << 'EOF'
apiVersion: batch/v1
kind: Job
metadata:
  name: batch-test-job
spec:
  template:
    spec:
      tolerations:
        - key: "workload"
          operator: "Equal"
          value: "batch"
          effect: "NoSchedule"
      containers:
        - name: batch-worker
          image: busybox:stable
          command: ["/bin/sh", "-c", "echo 'Batch job complete'; sleep 30"]
      restartPolicy: Never
  backoffLimit: 1
EOF

kubectl apply -f batch-job.yaml

# Watch the job run to completion on the batch-pool nodes
kubectl get jobs
kubectl get pods --watch
```

---

## Lab Deliverables

Submit a lab report containing:

1. Output of `kubectl get nodes -o wide` showing all cluster nodes.
2. Output of `kubectl get pods -o wide` after deploying both applications.
3. Output showing the LoadBalancer service external IP and a successful `curl`.
4. Output of `kubectl get ingress hello-ingress` showing the Ingress IP.
5. Screenshot of `kubectl get hpa hello-app` showing CPU load above the
   threshold and replica count increasing.
6. Output of `gcloud container node-pools list` showing both node pools.
7. Answers to the lab questions.

**Lab Questions:**

1. Explain the difference between a Service of type LoadBalancer and an
   Ingress resource. When would you use each?
2. What is the purpose of resource requests in a pod spec? How do they affect
   both the HPA and the Cluster Autoscaler?
3. You deploy an application on a GKE Standard cluster and the HPA scales the
   pods from 3 to 10 replicas. However, 4 of the new pods stay in Pending
   state. What likely happened and what will resolve it automatically?
4. What is the difference between a GKE regional cluster and a zonal cluster
   in terms of control plane availability?
5. A pod must only run on nodes in the `batch-pool` node pool. Describe the
   configuration needed on both the node pool and the pod.

---

## Cleanup

```bash
# Delete Kubernetes resources
kubectl delete -f ingress.yaml
kubectl delete -f deployment-v2.yaml
kubectl delete -f service-lb.yaml
kubectl delete -f deployment.yaml
kubectl delete hpa hello-app

# Delete node pool
gcloud container node-pools delete batch-pool \
  --cluster=$CLUSTER \
  --region=$REGION --quiet

# Delete the cluster
gcloud container clusters delete $CLUSTER \
  --region=$REGION --quiet
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Workload Identity Configuration

Configure Workload Identity on the GKE cluster so a pod can call the Cloud
Storage API without a JSON key file.

1. Enable Workload Identity on the cluster (if not already enabled):

```bash
gcloud container clusters update $CLUSTER \
  --region=$REGION \
  --workload-pool=$PROJECT_ID.svc.id.goog
```

1. Create a GCP service account for the workload and grant it Storage Viewer:

```bash
gcloud iam service-accounts create gke-wi-demo \
  --display-name="GKE Workload Identity Demo"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:gke-wi-demo@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

1. Create a Kubernetes service account and bind it to the GCP service account:

```bash
kubectl create serviceaccount wi-ksa --namespace=default

gcloud iam service-accounts add-iam-policy-binding \
  gke-wi-demo@$PROJECT_ID.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:$PROJECT_ID.svc.id.goog[default/wi-ksa]"

kubectl annotate serviceaccount wi-ksa \
  --namespace=default \
  iam.gke.io/gcp-service-account=gke-wi-demo@$PROJECT_ID.iam.gserviceaccount.com
```

1. Deploy a test pod using the Kubernetes service account and verify it can
   list Cloud Storage buckets:

```bash
kubectl run wi-test --image=google/cloud-sdk:slim \
  --serviceaccount=wi-ksa \
  --restart=Never \
  --command -- gcloud storage buckets list
kubectl logs wi-test
```

### Challenge 2: PodDisruptionBudget for Zero-Downtime Maintenance

Create a PodDisruptionBudget (PDB) that ensures at least 2 replicas of
the `hello-app` deployment remain available during a node drain.

1. Create the PDB:

```bash
cat <<'EOF' | kubectl apply -f -
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: hello-app-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: hello-app
EOF
```

1. Scale the deployment to 3 replicas and drain one node to observe the PDB
   in action:

```bash
kubectl scale deployment hello-app --replicas=3
NODE=$(kubectl get nodes -o name | head -1 | cut -d/ -f2)
kubectl drain $NODE --ignore-daemonsets --delete-emptydir-data
```

1. Observe that the drain respects the PDB and only evicts pods when 2+
   replicas remain available. Uncordon the node afterward:

```bash
kubectl uncordon $NODE
```

### Reflection Questions

1. In the Workload Identity setup you annotated a Kubernetes service account
   with a GCP service account email. Why does this eliminate the need for a
   JSON key file mounted as a Kubernetes Secret, and what security benefit does
   that provide?
2. The PodDisruptionBudget you created specifies `minAvailable: 2`. During the
   node drain, if all 3 replicas are on the same node, what will happen and why
   does distributing pods across nodes matter for PDB effectiveness?

---

End of Lab — Module 06

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
