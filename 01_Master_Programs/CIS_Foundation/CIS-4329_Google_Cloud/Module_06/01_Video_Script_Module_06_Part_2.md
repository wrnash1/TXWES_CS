# Video Script: Module 06 — Google Kubernetes Engine (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Recap and Agenda (1 minute)

Welcome back. In Part 1 we covered GKE cluster types, node pools, and workload
deployment. In Part 2 we cover:

- Kubernetes Services and Ingress
- Helm package manager
- Horizontal Pod Autoscaler
- Cluster autoscaling
- gcloud and kubectl CLI walkthrough
- ACE exam strategy for GKE

---

## Segment 2 — Kubernetes Services (3 minutes)

### Why Services?

Pods are ephemeral — their IPs change every time they are replaced. A Service
provides a stable IP address and DNS name that routes traffic to a set of pods
matching a label selector.

### Service Types

#### ClusterIP (default)

Exposes the service on a stable internal IP within the cluster. Accessible only
from within the cluster. Use for internal microservice-to-microservice
communication.

#### NodePort

Exposes the service on a static port on every node's external IP. Accessible
from outside the cluster via `NODE_IP:NODE_PORT`. Rarely used in production.

#### LoadBalancer

Provisions a GCP External Network Load Balancer and assigns an external IP.
Each LoadBalancer service creates a separate GCP load balancer — expensive if
you have many services.

#### ExternalName

Maps the service to an external DNS name. Used for routing cluster traffic to
external services.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-svc
spec:
  type: LoadBalancer
  selector:
    app: web-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

```bash
# Apply the service
kubectl apply -f service.yaml

# Check the external IP (wait for LB provisioning)
kubectl get service web-app-svc --watch
```

### Ingress

An Ingress resource provides HTTP/HTTPS routing to multiple services based on
hostname and path. One Ingress creates a single GCP Application Load Balancer
that routes to multiple backend services — much more efficient than multiple
LoadBalancer services.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations:
    kubernetes.io/ingress.class: "gce"
spec:
  rules:
    - host: www.example.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-svc
                port:
                  number: 80
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-app-svc
                port:
                  number: 80
```

**ACE Exam Tip:** Use Ingress (one LB, path-based routing) instead of multiple
LoadBalancer services when you have several HTTP services. LoadBalancer services
are appropriate for non-HTTP protocols like TCP databases.

---

## Segment 3 — Helm (2 minutes)

### What is Helm?

Helm is the package manager for Kubernetes. A Helm **chart** is a pre-packaged,
configurable Kubernetes application. Instead of writing and maintaining dozens
of YAML files, you install a chart with a single command.

```bash
# Add the bitnami Helm repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Install nginx using Helm
helm install my-nginx bitnami/nginx \
  --namespace web \
  --create-namespace \
  --set service.type=LoadBalancer

# List installed releases
helm list --all-namespaces

# Upgrade a release
helm upgrade my-nginx bitnami/nginx \
  --set replicaCount=3

# Uninstall a release
helm uninstall my-nginx --namespace web
```

Helm is widely used for deploying off-the-shelf software (databases, monitoring
tools, ingress controllers) onto GKE clusters.

---

## Segment 4 — Autoscaling in GKE (3 minutes)

### Horizontal Pod Autoscaler (HPA)

The HPA automatically adjusts the number of pod replicas in a Deployment or
ReplicaSet based on observed metrics.

Default metric: CPU utilization relative to resource requests. Custom metrics
via the Metrics Server or Cloud Monitoring adapter are also supported.

```bash
# Create an HPA for the web-app deployment
kubectl autoscale deployment web-app \
  --cpu-percent=70 \
  --min=2 \
  --max=10

# View HPA status
kubectl get hpa
kubectl describe hpa web-app
```

Or as YAML:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Vertical Pod Autoscaler (VPA)

The VPA automatically adjusts the CPU and memory requests and limits for
containers based on actual usage. Useful when you are unsure of the right
resource requests for a workload.

### Cluster Autoscaler

The Cluster Autoscaler (CA) adds or removes nodes from a node pool when:

- Pods cannot be scheduled due to insufficient resources (scale up)
- Nodes are underutilized and pods can be rescheduled elsewhere (scale down)

The CA and HPA work together: the HPA creates more pods when load increases;
the CA adds more nodes when there is no room for those pods.

---

## Segment 5 — gcloud and kubectl Walkthrough (4 minutes)

### Cluster Management with gcloud

```bash
# Create an Autopilot cluster
gcloud container clusters create-auto lab06-autopilot \
  --region=us-central1

# Create a Standard regional cluster
gcloud container clusters create lab06-standard \
  --region=us-central1 \
  --num-nodes=2 \
  --machine-type=e2-medium \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=5

# List clusters
gcloud container clusters list

# Get credentials (configure kubectl)
gcloud container clusters get-credentials lab06-standard \
  --region=us-central1

# Describe a cluster
gcloud container clusters describe lab06-standard \
  --region=us-central1

# Upgrade a cluster's control plane
gcloud container clusters upgrade lab06-standard \
  --region=us-central1 \
  --master

# Delete a cluster
gcloud container clusters delete lab06-standard \
  --region=us-central1
```

### kubectl Essentials

```bash
# View cluster info
kubectl cluster-info

# List nodes
kubectl get nodes -o wide

# List all resources in a namespace
kubectl get all -n default

# Apply a manifest
kubectl apply -f manifest.yaml

# Delete resources from a manifest
kubectl delete -f manifest.yaml

# Scale a deployment
kubectl scale deployment web-app --replicas=5

# View logs for a pod
kubectl logs POD_NAME

# Stream logs
kubectl logs -f POD_NAME

# Execute a command inside a pod
kubectl exec -it POD_NAME -- /bin/bash

# Roll back a deployment
kubectl rollout undo deployment/web-app

# View rollout history
kubectl rollout history deployment/web-app

# Port-forward for local testing
kubectl port-forward service/web-app-svc 8080:80
```

---

## Segment 6 — ACE Exam Tips for GKE (1 minute)

Key GKE patterns on the ACE exam:

- **Standard vs. Autopilot**: Autopilot manages nodes; Standard you manage them.
  Autopilot bills per pod request; Standard bills per node.
- **Zonal vs. regional cluster**: Regional = 99.95% SLA, control plane replicated.
  Production should use regional clusters.
- **Service types**: ClusterIP for internal; LoadBalancer for external TCP/UDP;
  Ingress for HTTP/HTTPS multi-service routing.
- **HPA vs. VPA vs. Cluster Autoscaler**: HPA scales pods horizontally. VPA
  resizes pod resources. CA scales nodes. All three can work together.
- **kubectl get credentials**: `gcloud container clusters get-credentials`
  is the command to configure kubectl for a GKE cluster.
- **Node pool operations**: Adding a node pool does not restart the cluster.
  Deleting a node pool drains and removes nodes.

---

## Summary — Module 06

Across both parts we covered:

- Kubernetes core objects: Pod, Deployment, Service, ConfigMap, Secret
- GKE cluster architecture: Google-managed control plane
- Standard vs. Autopilot and when to use each
- Zonal vs. regional clusters and SLA differences
- Node pools: multi-pool designs, taints and tolerations
- Services: ClusterIP, NodePort, LoadBalancer, ExternalName
- Ingress: path-based HTTP routing with a single load balancer
- Helm: chart-based package management
- HPA, VPA, and Cluster Autoscaler working together
- gcloud and kubectl CLI workflows

The lab will have you create a GKE cluster, deploy an application, configure
a Service and Ingress, and set up an HPA.

---

End of Part 2 — Module 06

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/kubernetes-engine/docs
