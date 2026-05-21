# Reading Guide: Module 07 – Kubernetes Engine (GKE): Cluster Management
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 07 – Kubernetes Engine (GKE): Cluster Management**! Google Kubernetes Engine is GCP's managed Kubernetes service. This module covers cluster creation and configuration, node pools, workload deployment, services and ingress, autoscaling, and the difference between GKE Standard and Autopilot modes. The ACE exam tests your ability to select the right GKE configuration for a given scenario and understand how GKE integrates with other GCP services like IAM, Cloud Logging, and load balancers.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Cluster**: The top-level GKE resource. A cluster consists of a control plane (managed by Google) and one or more node pools. The control plane runs the Kubernetes API server, scheduler, and etcd. In Standard mode you pay for nodes; in Autopilot mode you pay per pod resource request.

*   **Node Pool**: A group of Compute Engine VMs within a cluster that share the same machine type, disk configuration, and labels. A cluster can have multiple node pools — for example, a general-purpose pool for web workloads and a high-memory pool for analytics jobs.

*   **Pod**: The smallest deployable unit in Kubernetes. A pod wraps one or more containers and shares a network namespace and storage volumes. Pods are ephemeral — when they crash, the Deployment controller creates a replacement.

*   **Deployment**: A Kubernetes controller that manages a desired number of identical pod replicas. Deployments support rolling updates (gradually replacing old pods with new ones) and rollbacks. Use `kubectl rollout undo deployment/NAME` to revert a failed update.

*   **Service**: A stable network endpoint that exposes a set of pods. `ClusterIP` services are internal-only. `NodePort` services expose a port on every node. `LoadBalancer` services provision a GCP External Load Balancer automatically. `ExternalName` services map to an external DNS name.

*   **Horizontal Pod Autoscaler (HPA)**: Automatically scales the number of pod replicas based on observed CPU utilization or custom metrics. HPA works with Deployments and ReplicaSets. Cluster Autoscaler separately scales the number of nodes in a node pool when pods cannot be scheduled due to insufficient capacity.

---

### 2. Certification Exam Tips

*   **GKE Standard vs. Autopilot**: The ACE exam will describe a scenario and ask which mode is appropriate. Key signals: if the question mentions managing node pools, selecting machine types, or needing DaemonSets — Standard. If it mentions paying only for pod resources, no node management, or Google handles all infrastructure — Autopilot.

*   **`kubectl` is required for GKE workload management**: Know that `gcloud container clusters get-credentials CLUSTER_NAME --region=REGION` populates `~/.kube/config` so `kubectl` commands work. Then use `kubectl apply -f deployment.yaml`, `kubectl get pods`, `kubectl describe pod POD_NAME`, and `kubectl logs POD_NAME`.

*   **LoadBalancer Service creates a Cloud Load Balancer**: When you create a Kubernetes Service of type `LoadBalancer` in GKE, GCP automatically provisions a Regional External TCP Load Balancer. For HTTP(S) with path-based routing, use an Ingress resource, which provisions a Global HTTP(S) Load Balancer.

*   **Workload Identity for GKE IAM**: The recommended way to give GKE pods access to GCP APIs (like Cloud Storage or Pub/Sub) is Workload Identity — it links a Kubernetes Service Account to a GCP Service Account without needing key files. The ACE exam favors Workload Identity over manually mounting Service Account key JSON files.

*   **Study Resource**: The freeCodeCamp ACE course covers GKE cluster setup, workload deployment, and services: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Supplement with the official GKE quickstart for hands-on familiarity with cluster creation commands.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review GKE cluster architecture including control plane, node pools, and the difference between Standard and Autopilot modes: [GKE Cluster Architecture](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).
*   **Required Reading**: Review how Kubernetes Services of type LoadBalancer and Ingress interact with GCP load balancers: [GKE Services and Ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/service).
*   **Required Video**: Watch the GKE segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Kubernetes Engine chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a GKE cluster, deploy a containerized application, and expose it with a LoadBalancer Service. Key commands to practice:

*   `gcloud container clusters create my-cluster --region=us-central1 --num-nodes=2` — creates a regional GKE cluster
*   `gcloud container clusters get-credentials my-cluster --region=us-central1` — configures kubectl credentials
*   `kubectl apply -f deployment.yaml` — deploys workloads from a manifest file
*   `kubectl get services` — lists Services and their external IP addresses

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [GKE Cluster Architecture](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) documentation page.
- [ ] Read the [GKE Services and Ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/service) documentation page.
- [ ] Watch the GKE segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a cluster, deploy a workload, expose it as a LoadBalancer Service.
- [ ] Proceed to the weekly quiz.
