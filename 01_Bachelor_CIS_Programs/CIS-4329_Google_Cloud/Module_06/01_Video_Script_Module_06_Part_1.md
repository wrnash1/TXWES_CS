# Video Script: Module 06 — Google Kubernetes Engine (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Introduction (1 minute)

Welcome to Module 06. This module covers Google Kubernetes Engine — GCP's
managed Kubernetes platform and one of the most important services in the
modern cloud landscape.

Google invented Kubernetes in 2014 based on its internal Borg system, and
GKE is widely considered the most mature managed Kubernetes offering available.

In Part 1 we cover Kubernetes and GKE concepts, cluster types, node pools,
and workload deployment. In Part 2 we cover services, Ingress, Helm, cluster
autoscaling, and gcloud and kubectl CLI workflows.

---

## Segment 2 — Kubernetes Concepts Review (3 minutes)

### What is Kubernetes?

Kubernetes is an open-source container orchestration platform. It automates
the deployment, scaling, and management of containerized applications.

Key Kubernetes objects:

- **Pod**: The smallest deployable unit. Contains one or more containers
  sharing network and storage. Pods are ephemeral — they can be created,
  killed, and replaced at any time.
- **Deployment**: Manages a set of identical pod replicas. Handles rolling
  updates and rollbacks. This is how you deploy stateless applications.
- **Service**: Provides stable networking for a set of pods. Abstracts the
  ephemeral pod IPs with a stable endpoint.
- **ConfigMap**: Stores non-sensitive configuration data (environment variables,
  config files) that pods can consume.
- **Secret**: Stores sensitive data (passwords, tokens, keys) for pods.
- **Namespace**: Virtual cluster within a cluster. Provides scope for names
  and resource quotas.
- **Node**: A worker machine in the cluster. Can be a VM (in GKE) or a
  bare-metal machine.

### GKE Architecture

In a GKE cluster:

- **Control plane** (master): Managed by Google. Runs the Kubernetes API server,
  scheduler, controller manager, and etcd. You do not manage the control plane
  in GKE — Google handles updates, patches, and HA.
- **Worker nodes**: Compute Engine VMs in a node pool. You manage the machine
  type, count, and configuration.

---

## Segment 3 — GKE Cluster Types (4 minutes)

### Standard Clusters

In a Standard cluster, you manage the node pools — you choose machine types,
node counts, autoscaling settings, and update schedules. Google manages the
control plane.

You have full flexibility over:

- Node machine types (any Compute Engine type)
- Node operating system (Container-Optimized OS, Ubuntu, Windows)
- Custom node configurations
- Node pool autoscaling settings

Standard clusters are billed for the VMs in the node pools plus a cluster
management fee.

### Autopilot Clusters

GKE Autopilot is a managed cluster mode where Google manages both the control
plane AND the worker nodes. You deploy workloads; Google handles everything else.

In Autopilot:

- You do not manage node pools, machine types, or node counts
- Google automatically provisions and scales nodes based on pod resource requests
- Billing is per pod CPU and memory request — not per node
- Security hardening is applied automatically (e.g., no privileged pods,
  no SSH to nodes)

When to use Autopilot:

- Teams that want to focus on workload development, not cluster operations
- Variable workloads where node utilization would otherwise be low
- When security defaults are acceptable and preferred

When to use Standard:

- Workloads requiring custom node configurations or privileged containers
- GPU/TPU workloads
- When precise control over node fleet is needed

**ACE Exam Tip:** The ACE exam frequently tests Standard vs. Autopilot. Key
differentiators: Autopilot manages nodes, Standard you manage nodes. Autopilot
bills per pod resource, Standard bills per node. Autopilot is more restricted
(no privileged containers by default).

### Cluster Modes: Zonal vs. Regional

- **Zonal cluster**: Control plane in one zone; nodes in one zone or multiple
  zones. If the control plane zone goes down, the cluster is unavailable.
- **Regional cluster**: Control plane replicated across 3 zones. Nodes spread
  across zones. 99.95% SLA. Recommended for production.

```bash
# Create a regional Autopilot cluster
gcloud container clusters create-auto lab06-autopilot \
  --region=us-central1

# Create a regional Standard cluster
gcloud container clusters create lab06-standard \
  --region=us-central1 \
  --num-nodes=2 \
  --machine-type=e2-medium
```

---

## Segment 4 — Node Pools (3 minutes)

### What is a Node Pool?

A node pool is a group of nodes in a GKE Standard cluster that share the same
configuration (machine type, disk, OS, labels, taints). A cluster can have
multiple node pools for different workload types.

Example node pool structure:

- **Default pool**: e2-standard-4, general workloads
- **GPU pool**: a2-highgpu-1g, ML inference workloads
- **High-memory pool**: n2-highmem-8, in-memory database workloads

### Taints and Tolerations

**Taints** are applied to nodes to repel pods that do not explicitly tolerate
them. **Tolerations** are applied to pods to allow them to be scheduled on
tainted nodes.

Example: Taint the GPU node pool with `gpu=true:NoSchedule`. Only pods with
the matching toleration will be scheduled on those nodes. Regular application
pods stay on the general pool.

### Node Pool Autoscaling

GKE node pool autoscaling adds or removes nodes based on pending pod resource
requests:

```bash
# Create a node pool with autoscaling
gcloud container node-pools create general-pool \
  --cluster=lab06-standard \
  --region=us-central1 \
  --machine-type=e2-medium \
  --num-nodes=2 \
  --min-nodes=1 \
  --max-nodes=5 \
  --enable-autoscaling
```

---

## Segment 5 — Deploying Workloads (2 minutes)

### Deployment YAML

The standard way to deploy applications to Kubernetes is with YAML manifest
files applied via `kubectl`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
        - name: web
          image: nginx:stable
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "250m"
              memory: "256Mi"
```

**ACE Exam Tip:** Resource requests and limits are critical for GKE Autopilot
billing and for the cluster autoscaler. Always specify requests — they tell the
scheduler how much capacity a pod needs.

### Applying Manifests

```bash
# Apply a manifest
kubectl apply -f deployment.yaml

# Check deployment status
kubectl rollout status deployment/web-app

# List pods
kubectl get pods -o wide

# Describe a pod
kubectl describe pod POD_NAME
```

---

## Summary — Part 1

In Part 1 we covered:

- Kubernetes core objects: Pod, Deployment, Service, ConfigMap, Secret
- GKE architecture: Google-managed control plane, user-managed worker nodes
- Standard vs. Autopilot cluster types and when to use each
- Zonal vs. regional clusters and their SLA implications
- Node pools: multi-pool configurations, taints and tolerations
- Node pool autoscaling
- Deployment YAML structure and resource requests

In Part 2 we cover Services, Ingress, Helm, Cluster Autoscaler, Horizontal
Pod Autoscaler, and hands-on gcloud and kubectl workflows.

See you in Part 2.

---

End of Part 1 — Module 06

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/kubernetes-engine/docs
