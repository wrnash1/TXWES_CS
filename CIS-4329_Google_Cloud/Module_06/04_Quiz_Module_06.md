# Quiz: Module 06 — Google Kubernetes Engine (GKE)

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
This quiz covers GKE cluster types, node pools, Kubernetes workloads, Services,
Ingress, autoscaling, and Helm.

---

## Question 1

A development team wants to deploy containerized applications on GKE. They do
not want to manage node provisioning, scaling, or maintenance. Billing should
be based on actual pod resource consumption rather than node capacity.
Which GKE cluster mode should they use?

- A) Standard cluster with node pool autoscaling
- B) Autopilot cluster
- C) Zonal Standard cluster with fixed node count
- D) Standard cluster with preemptible nodes

**Correct Answer:** B

**Explanation:** GKE Autopilot manages node provisioning, scaling, and
maintenance on behalf of the user. Billing is based on pod CPU and memory
requests rather than node VM costs. This is exactly the model the question
describes. Standard clusters (options A, C, D) require the user to manage node
pools even when autoscaling is enabled, and bill per node regardless of pod
utilization.

---

## Question 2

You need to run a pod only on nodes in a specific GKE node pool that has GPUs.
The node pool was created with the taint `gpu=true:NoSchedule`. What must
the pod spec include to be scheduled on those nodes?

- A) A node affinity rule specifying the node pool name
- B) A toleration matching `gpu=true:NoSchedule`
- C) A resource request for GPU units
- D) A label `nodePool: gpu-pool` on the pod

**Correct Answer:** B

**Explanation:** Taints on nodes prevent pods from being scheduled unless the
pod has a matching toleration. The taint `gpu=true:NoSchedule` requires a
toleration with key=`gpu`, value=`true`, effect=`NoSchedule`. Without this
toleration, the scheduler ignores those nodes. Node affinity (option A) is for
preference-based scheduling, not hard restrictions via taints.

---

## Question 3

Your GKE cluster has 10 pods running. The Horizontal Pod Autoscaler scales
the deployment to 20 pods due to high CPU. The 10 new pods stay in Pending
state. What is the most likely cause and what resolves it automatically?

- A) The pods are misconfigured; a cluster administrator must fix the YAML
- B) The node pool has reached its maximum node count; you must manually
     add nodes
- C) The Cluster Autoscaler detects the pending pods and adds nodes to the
     pool, up to the configured maximum
- D) The HPA and Cluster Autoscaler cannot run simultaneously

**Correct Answer:** C

**Explanation:** When pods cannot be scheduled because no node has sufficient
resources, the Cluster Autoscaler detects the pending pods and adds new nodes to
the node pool (up to the configured maximum). The HPA and Cluster Autoscaler
are designed to work together — HPA creates more pods, CA provides the nodes
to run them. If the maximum node count is already reached, CA cannot add more
nodes, but that is a configuration limit, not the "most likely" cause described.

---

## Question 4

A microservices application has three services deployed on GKE: `frontend`,
`api`, and `admin`. You want to expose all three over HTTP from a single
external IP address, routing based on path:
`/api/*` → api service, `/admin/*` → admin service, `/` → frontend. What
Kubernetes resource achieves this most efficiently?

- A) Three separate LoadBalancer services, each with a different external IP
- B) Three NodePort services with a custom nginx proxy VM
- C) One Ingress resource with path-based routing rules
- D) One ClusterIP service with port forwarding

**Correct Answer:** C

**Explanation:** An Ingress resource defines HTTP/HTTPS routing rules based on
hostname and path, routing to multiple backend services through a single GCP
Application Load Balancer with one external IP. This is more efficient and
cost-effective than creating three separate LoadBalancer services (option A),
each of which provisions a separate GCP load balancer.

---

## Question 5

What is the key command to configure kubectl to communicate with a GKE cluster
after the cluster is created?

- A) `kubectl config set-context GKE_CLUSTER_NAME`
- B) `gcloud container clusters get-credentials CLUSTER_NAME --region REGION`
- C) `kubectl apply -f cluster-credentials.yaml`
- D) `gcloud auth configure-docker`

**Correct Answer:** B

**Explanation:** `gcloud container clusters get-credentials` fetches the cluster
credentials from the GKE API and writes them to the kubectl configuration file
(`~/.kube/config`). This configures the current kubectl context to point to
the specified GKE cluster. `kubectl config` (option A) manipulates existing
kubeconfig entries but cannot fetch new GKE credentials.

---

## Question 6

You deploy a GKE cluster with the control plane in a single zone. A zone
outage occurs. What is the impact on workloads running in the cluster?

- A) Pods continue running because they are on worker nodes in healthy zones
- B) The cluster API server is unavailable; existing pods continue running but
     no new pods can be scheduled and no management operations are possible
- C) All pods are immediately terminated because the control plane is down
- D) GKE automatically migrates the control plane to a healthy zone

**Correct Answer:** B

**Explanation:** In a zonal cluster, the control plane runs in a single zone.
If that zone fails, the Kubernetes API server is unreachable — you cannot
deploy, scale, or delete workloads. However, pods already running on worker
nodes in healthy zones continue to run because they do not need the API server
for normal operation. This is why regional clusters (with control plane in 3
zones) are recommended for production.

---

## Question 7

A ClusterIP service is created for a database pod. A developer reports that
they cannot connect to the database from outside the cluster. What is the
expected behavior and how should they access it?

- A) ClusterIP services are not routable; the database should be exposed
     as a LoadBalancer service
- B) ClusterIP services are only accessible within the cluster; to access
     from outside, use port-forward for dev/test or a LoadBalancer/Ingress
     for production
- C) ClusterIP services require a firewall rule to be opened externally
- D) The service is misconfigured; all GKE services are externally accessible

**Correct Answer:** B

**Explanation:** ClusterIP is the default service type and provides a stable
internal IP accessible only from within the cluster. This is the correct
type for a database that should not be externally accessible. For development
and testing, `kubectl port-forward` can tunnel cluster traffic to a local port.
For production external access, a LoadBalancer service or Ingress is needed —
though exposing a database externally is rarely advisable.

---

## Question 8

What is the purpose of specifying `resources.requests.cpu` in a pod spec?

- A) It caps the maximum CPU the container can use
- B) It tells the Kubernetes scheduler how much CPU capacity the pod needs
     to be placed on a node with sufficient resources
- C) It creates a CPU billing alert in Cloud Monitoring
- D) It reserves a dedicated CPU core on the host node

**Correct Answer:** B

**Explanation:** Resource requests inform the Kubernetes scheduler of the
minimum resources a pod needs. The scheduler uses requests to find a node with
enough available capacity. Requests also affect HPA scaling (the target
utilization is calculated relative to requests) and Cluster Autoscaler decisions.
Resource limits (option A) cap maximum usage. Requests do not reserve dedicated
hardware — they are hints to the scheduler.

---

## Question 9

Your team uses Helm to manage a third-party monitoring stack on GKE. A new
version of the Helm chart is released with configuration changes. You want
to upgrade the deployment but must be able to roll back immediately if
something breaks. What Helm command performs the upgrade?

- A) `helm install monitoring bitnami/prometheus --replace`
- B) `helm upgrade monitoring bitnami/prometheus`
- C) `kubectl apply -f prometheus-chart.yaml`
- D) `helm delete monitoring && helm install monitoring bitnami/prometheus`

**Correct Answer:** B

**Explanation:** `helm upgrade` upgrades an existing release to a new chart
version or configuration. Helm tracks release history automatically, so if
the upgrade causes issues, you can immediately roll back with
`helm rollback monitoring [REVISION]`. Option D (delete and reinstall) loses
the release history and creates downtime.

---

## Question 10

A GKE Autopilot cluster is being considered for a security-sensitive
production workload. Which statement about Autopilot's security model
is accurate?

- A) Autopilot provides weaker security than Standard clusters because you
     cannot configure node-level settings
- B) Autopilot enforces security hardening automatically — privileged containers
     are not allowed and node SSH access is restricted
- C) Autopilot clusters do not support Workload Identity Federation
- D) Autopilot clusters require manual firewall rule configuration to restrict
     inter-pod traffic

**Correct Answer:** B

**Explanation:** GKE Autopilot enforces security hardening as part of its
managed model. Privileged containers are rejected by default, host namespaces
cannot be shared, and SSH access to nodes is not permitted. These restrictions
are consistent and cannot be accidentally loosened by a misconfigured deployment.
This can actually be a security advantage over Standard clusters where teams
might enable privileged containers inadvertently.

---

End of Quiz — Module 06

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
