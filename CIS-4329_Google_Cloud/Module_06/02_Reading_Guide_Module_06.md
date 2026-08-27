# Reading Guide: Module 06 — Google Kubernetes Engine (GKE)

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This reading guide covers Google Kubernetes Engine — GCP's managed Kubernetes
platform. GKE is a key ACE exam topic, with questions spanning cluster types,
workload deployment, autoscaling, and networking within Kubernetes.

**Estimated Reading Time:** 55–65 minutes

---

## Section 1 — Kubernetes Fundamentals

### 1.1 Core Objects

| Object | Description |
|---|---|
| Pod | Smallest deployable unit; one or more containers sharing network/storage |
| Deployment | Manages pod replicas; handles rolling updates and rollbacks |
| ReplicaSet | Ensures a specified number of pod replicas are running |
| StatefulSet | Like a Deployment but for stateful apps; stable pod names and storage |
| DaemonSet | Runs one pod per node; used for monitoring agents, log collectors |
| Job | Runs a pod to completion; for batch workloads |
| CronJob | Runs a Job on a schedule |
| Service | Stable networking endpoint for a set of pods |
| Ingress | HTTP/HTTPS routing to multiple services based on host/path |
| ConfigMap | Non-sensitive configuration data for pods |
| Secret | Sensitive data (credentials, tokens) for pods |
| Namespace | Logical isolation scope within a cluster |
| PersistentVolume | A piece of storage in the cluster |
| PersistentVolumeClaim | A request for storage by a pod |

### 1.2 Pod Lifecycle

Pods go through these phases:

- **Pending**: Accepted by the cluster; waiting to be scheduled
- **Running**: At least one container is running
- **Succeeded**: All containers completed successfully
- **Failed**: At least one container exited with non-zero status
- **Unknown**: Pod state cannot be determined

Pods do not self-heal. Deployments and ReplicaSets watch for failed pods and
create replacements. Do not run a single unmanaged pod in production.

### 1.3 Labels and Selectors

Labels are key-value metadata attached to objects. Selectors filter objects
by their labels. Services use selectors to find the pods they route traffic to.

```yaml
# Pod with labels
metadata:
  labels:
    app: web-app
    env: production
    version: v2

# Service selecting those pods
spec:
  selector:
    app: web-app
    env: production
```

---

## Section 2 — GKE Cluster Types

### 2.1 Standard vs. Autopilot

| Feature | Standard | Autopilot |
|---|---|---|
| Node management | User-managed | Google-managed |
| Billing unit | Per node (VM) | Per pod CPU/memory request |
| Machine type choice | User selects | Google optimizes |
| Privileged containers | Allowed (configurable) | Not allowed by default |
| SSH to nodes | Allowed | Not allowed |
| Node pool customization | Full | None |
| Best for | Control, custom configs | Simplicity, variable workloads |

### 2.2 Zonal vs. Regional Clusters

| Feature | Zonal | Regional |
|---|---|---|
| Control plane zones | 1 | 3 |
| Control plane SLA | No SLA (best effort) | 99.95% |
| Node zones | 1 zone default (multi-zone optional) | Spread across 3+ zones |
| Cost | Lower | Higher (3x control plane replicas) |
| Best for | Dev/test | Production |

### 2.3 Private Clusters

In a private cluster, nodes do not have external IP addresses. The control
plane is in a Google-managed VPC. Communication between the control plane and
nodes happens over VPC peering.

Benefits:

- Nodes are not directly reachable from the internet
- Better security posture for production workloads

```bash
# Create a private Standard cluster
gcloud container clusters create my-private-cluster \
  --region=us-central1 \
  --enable-private-nodes \
  --enable-private-endpoint \
  --master-ipv4-cidr=172.16.0.32/28 \
  --network=custom-vpc \
  --subnetwork=gke-subnet
```

---

## Section 3 — Node Pools

### 3.1 Node Pool Configuration

```bash
# Add a node pool to an existing cluster
gcloud container node-pools create high-memory-pool \
  --cluster=my-cluster \
  --region=us-central1 \
  --machine-type=n2-highmem-4 \
  --num-nodes=3 \
  --node-labels=workload=high-memory

# List node pools
gcloud container node-pools list \
  --cluster=my-cluster \
  --region=us-central1

# Delete a node pool
gcloud container node-pools delete old-pool \
  --cluster=my-cluster \
  --region=us-central1
```

### 3.2 Node Upgrades

GKE can automatically upgrade nodes to new Kubernetes versions. The upgrade
strategy:

- **Surge upgrade** (default): Adds extra nodes, migrates pods, removes old
  nodes. Minimal disruption.
- **Blue/green upgrade**: Creates a parallel new node pool, migrates all pods,
  deletes old pool.

### 3.3 Node Taints and Tolerations

Taints prevent pods from being scheduled on nodes unless the pod has a matching
toleration.

```bash
# Apply a taint to a node pool (at creation)
gcloud container node-pools create gpu-pool \
  --cluster=my-cluster \
  --region=us-central1 \
  --machine-type=a2-highgpu-1g \
  --node-taints=gpu=true:NoSchedule
```

```yaml
# Pod toleration to allow scheduling on tainted nodes
spec:
  tolerations:
    - key: "gpu"
      operator: "Equal"
      value: "true"
      effect: "NoSchedule"
```

---

## Section 4 — Services and Networking

### 4.1 Service Types

| Type | External access | Use case |
|---|---|---|
| ClusterIP | No | Internal microservice communication |
| NodePort | Via node IPs | Dev/test; not for production external |
| LoadBalancer | Via GCP External LB | External TCP/UDP services |
| ExternalName | Via DNS CNAME | Route cluster traffic to external service |

### 4.2 Ingress

Ingress is a Kubernetes API object that manages external HTTP/HTTPS access to
services. GKE creates a GCP Application Load Balancer when an Ingress is applied.

GKE Ingress annotations:

```yaml
metadata:
  annotations:
    kubernetes.io/ingress.class: "gce"                # External LB
    kubernetes.io/ingress.class: "gce-internal"       # Internal LB
    networking.gke.io/managed-certificates: "my-cert" # Managed SSL cert
    kubernetes.io/ingress.global-static-ip-name: "web-ip"  # Static IP
```

### 4.3 Container-Native Load Balancing

GKE supports Network Endpoint Groups (NEGs), which allow the GCP load balancer
to send traffic directly to pod IPs instead of node IPs. Benefits:

- Reduced latency (fewer hops)
- More precise health checking at the pod level
- Required for HTTP/2, gRPC, and WebSockets with Ingress

---

## Section 5 — Autoscaling

### 5.1 Horizontal Pod Autoscaler (HPA)

Scales the number of pod replicas based on CPU/memory utilization or custom
metrics.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 60
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
```

### 5.2 Vertical Pod Autoscaler (VPA)

Adjusts CPU and memory requests/limits based on actual historical usage.
Not compatible with HPA on the same metric simultaneously.

### 5.3 Cluster Autoscaler

Scales node pools based on pod scheduling demand:

- **Scale up**: Triggered when pods are Pending due to insufficient node capacity
- **Scale down**: Triggered when a node is underutilized and its pods can fit
  on other nodes

```bash
# Enable autoscaling on an existing node pool
gcloud container clusters update my-cluster \
  --region=us-central1 \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=10 \
  --node-pool=default-pool
```

---

## Section 6 — Helm

### 6.1 Helm Concepts

| Term | Description |
|---|---|
| Chart | Package of Kubernetes resources and templates |
| Repository | Collection of charts hosted at a URL |
| Release | An instance of a chart deployed to a cluster |
| Values | Configuration parameters that customize a chart's resources |

### 6.2 Common Helm Commands

```bash
# Add a repository
helm repo add stable https://charts.helm.sh/stable
helm repo update

# Search for charts
helm search repo nginx

# Install a chart
helm install my-release bitnami/nginx \
  --namespace prod \
  --create-namespace \
  --values custom-values.yaml

# List releases
helm list -A

# View release notes and configuration
helm status my-release

# Upgrade a release
helm upgrade my-release bitnami/nginx \
  --set replicaCount=5

# Roll back to a previous revision
helm rollback my-release 1

# Uninstall
helm uninstall my-release
```

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| Pod | Smallest deployable Kubernetes unit |
| Deployment | Controller managing replicated pods with rolling update support |
| Service | Stable networking endpoint routing to a pod selector |
| Ingress | HTTP/HTTPS routing to multiple services; creates a GCP ALB |
| Node pool | Group of nodes with identical configuration in a GKE cluster |
| Taint | Node attribute repelling pods without matching tolerations |
| Toleration | Pod attribute allowing scheduling on tainted nodes |
| HPA | Horizontal Pod Autoscaler — scales replica count |
| VPA | Vertical Pod Autoscaler — adjusts CPU/memory requests |
| Cluster Autoscaler | Scales node count based on pod scheduling demand |
| Standard cluster | GKE mode where users manage node pools |
| Autopilot cluster | GKE mode where Google manages node pools; bills per pod |
| Regional cluster | GKE cluster with control plane replicated across 3 zones |
| Helm | Kubernetes package manager using charts and releases |
| NEG | Network Endpoint Group — direct pod-level load balancing |
| Private cluster | Cluster where nodes have no external IPs |

---

## ACE Exam Focus Areas — Module 06

- Explain the difference between Standard and Autopilot GKE cluster modes.
- Describe the billing model difference (per node vs. per pod request).
- Choose zonal vs. regional cluster for a described availability requirement.
- Explain when to use ClusterIP, LoadBalancer, and Ingress service types.
- Describe HPA, VPA, and Cluster Autoscaler and how they interact.
- Identify the command to configure kubectl for a GKE cluster.
- Explain node pool taints and pod tolerations.
- Describe private clusters and their security benefit.

---

## Further Reading

- GKE overview: cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview
- Autopilot: cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview
- Node pools: cloud.google.com/kubernetes-engine/docs/concepts/node-pools
- Autoscaling: cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler
- Ingress: cloud.google.com/kubernetes-engine/docs/concepts/ingress
- Helm: helm.sh/docs

## 9. Supplemental Resources

**1. Google Cloud Documentation — GKE Autopilot Overview**
<https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview>
Official guide to GKE Autopilot covering its managed node model, security
defaults, billing by pod resource requests, and comparison with Standard
clusters. Key reading for ACE exam questions on GKE cluster mode selection.

**2. Google Cloud Skills Boost — Kubernetes Engine: Qwik Start**
<https://www.cloudskillsboost.google/focuses/878>
Hands-on lab deploying a containerized application to GKE, creating a
Service, and scaling the deployment. Covers the core `kubectl` commands
tested on the ACE exam.

**3. Kubernetes Documentation — Concepts Overview**
<https://kubernetes.io/docs/concepts/>
The official Kubernetes documentation for core objects: Pods, Deployments,
Services, Ingress, ConfigMaps, Secrets, and PersistentVolumeClaims. GKE
is fully Kubernetes-conformant, so upstream docs apply directly.
