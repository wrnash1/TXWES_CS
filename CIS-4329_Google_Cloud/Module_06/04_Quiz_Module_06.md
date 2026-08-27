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

---

### Question 11 (5 points)

You need to upgrade the Kubernetes version on a GKE Standard cluster's node
pool with zero downtime. What is the correct approach?

- A) Delete the node pool and recreate it with the new version
- B) Use `gcloud container clusters upgrade` which performs a rolling node
   upgrade, draining and replacing one node at a time
- C) Manually SSH into each node and run `apt-get upgrade`
- D) Upgrade the control plane first, then set the node pool to auto-upgrade
   and wait for the next maintenance window

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Deleting and recreating the node pool causes all pods on that pool to be evicted simultaneously, causing downtime for workloads that don't have replicas on other pools.
  - C) Node VMs are managed by GKE and should not be modified manually via SSH; this approach would cause configuration drift and is not supported.
  - D) While auto-upgrade is a valid long-term strategy, the question asks about performing a node upgrade; `gcloud container clusters upgrade` is the immediate command-driven approach that performs the rolling drain-and-replace.

---

### Question 12 (5 points)

A pod spec sets `resources.limits.memory: 512Mi` but does not set
`resources.requests.memory`. What value does Kubernetes use for the memory
request when scheduling this pod?

- A) 0 — the pod has no memory reservation for scheduling purposes
- B) 512Mi — when only a limit is specified, the request defaults to the
   same value as the limit
- C) 256Mi — Kubernetes uses half the limit as the default request
- D) The pod fails to schedule because requests are mandatory

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Without an explicit request, Kubernetes does not default to 0; it uses the limit value to prevent pods from being scheduled on nodes that cannot satisfy even the limit.
  - C) Kubernetes does not apply a half-limit heuristic; it uses the exact limit value as the default request when no request is specified.
  - D) Requests are not mandatory fields; Kubernetes handles missing requests by defaulting them to the limit value (or using LimitRange defaults if configured).

---

### Question 13 (5 points)

Which GKE feature automatically identifies and removes nodes that have
been consistently underutilized, reducing cluster costs?

- A) Horizontal Pod Autoscaler (HPA)
- B) Vertical Pod Autoscaler (VPA)
- C) Cluster Autoscaler scale-down
- D) Node auto-repair

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) HPA adjusts pod replica counts based on metrics; it does not manage nodes.
  - B) VPA adjusts the CPU and memory requests/limits of individual pods; it does not remove nodes.
  - D) Node auto-repair detects and replaces nodes that fail health checks; it addresses node health, not cost optimization through scale-down.

---

### Question 14 (5 points)

A GKE private cluster has `--enable-private-nodes` set. What is the security
implication for the worker nodes?

- A) Worker nodes have no external IP addresses and cannot be reached directly
   from the internet
- B) Worker nodes use private encryption keys that rotate automatically
- C) Worker nodes can only be managed by users in the same GCP organization
- D) Worker nodes have no access to the Kubernetes API server

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `--enable-private-nodes` refers to network IP assignment, not encryption key management.
  - C) Access to manage nodes is controlled by IAM roles, not private cluster status; private clusters restrict network-level reachability, not IAM-based management.
  - D) Worker nodes in a private cluster still communicate with the API server via private IP through the internal VPC network; they do not lose API access.

---

### Question 15 (5 points)

What does the `kubectl rollout undo deployment/my-app` command do?

- A) Deletes the deployment and all its pods permanently
- B) Rolls the deployment back to the previous revision, replacing pods
   with the prior container image and configuration
- C) Pauses the current rollout and waits for manual approval
- D) Scales the deployment down to zero replicas

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `kubectl delete deployment` is the command that removes a deployment; `rollout undo` preserves the deployment and reverts its configuration.
  - C) `kubectl rollout pause` pauses a rollout; `rollout undo` actively replaces the current revision with the previous one.
  - D) `kubectl scale deployment my-app --replicas=0` scales to zero; `rollout undo` maintains the current replica count but changes the pod template back to the previous revision.

---

### Question 16 (5 points)

A Kubernetes ConfigMap is updated to change an environment variable that
a running pod reads at startup. What must happen for the running pod to
pick up the new value?

- A) The pod automatically restarts and reads the new value within 30 seconds
- B) The ConfigMap update propagates to running pods instantly via the kubelet
- C) The pod must be deleted and recreated (or the deployment rolled out) for
   the new environment variable value to take effect
- D) Running `kubectl apply -f configmap.yaml` triggers a rolling restart of
   all pods that reference the ConfigMap

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Pods do not auto-restart when a ConfigMap changes; environment variable values are injected at pod startup and are not live-reloaded.
  - B) While ConfigMap data mounted as volumes can update within seconds (the kubelet syncs the volume), environment variables sourced from ConfigMaps are set at container creation time and do not update in running containers.
  - D) `kubectl apply` updates the ConfigMap resource but does not trigger a rollout; you must explicitly run `kubectl rollout restart deployment/my-app` to cycle pods.

---

### Question 17 (5 points)

You want to run a database pod on GKE that requires a dedicated persistent
volume. The pod must always be rescheduled to the same volume even if the
pod is deleted and recreated. Which Kubernetes resource manages this
persistent storage binding?

- A) ConfigMap
- B) PersistentVolumeClaim (PVC)
- C) Secret
- D) StorageClass only — no claim is needed

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) ConfigMaps store configuration data (key-value pairs, config files); they do not manage persistent block storage volumes.
  - C) Secrets store sensitive data such as passwords and API keys; they do not manage persistent disk volumes.
  - D) A StorageClass defines the type and parameters of storage to provision; a PersistentVolumeClaim (PVC) is the actual binding between a pod and a persistent volume — both are needed together.

---

### Question 18 (5 points)

In GKE, what is Workload Identity used for?

- A) Assigning a Kubernetes username to each developer for `kubectl` access
- B) Allowing pods to authenticate to GCP APIs (such as Cloud Storage or
   BigQuery) using a GCP IAM service account without storing JSON key files
   in the cluster
- C) Enabling pods to communicate with other pods using mTLS certificates
- D) Creating network identity policies to control pod-to-pod traffic

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Developer kubectl access is managed via `gcloud container clusters get-credentials` and IAM RBAC bindings, not Workload Identity.
  - C) Mutual TLS for pod-to-pod communication is handled by a service mesh such as Anthos Service Mesh (Istio); Workload Identity is for GCP API authentication.
  - D) Network policies control pod-to-pod traffic at the IP layer; Workload Identity handles IAM authentication for GCP API calls, not network routing.

---

### Question 19 (5 points)

A GKE Standard cluster node pool is created with `--disk-size=50GB`. After
several months, application logs fill the node disk to 90% capacity. What
is the recommended approach to increase disk space without recreating all
pods?

- A) SSH into each node and resize the disk using the OS disk utility
- B) Add a new node pool with a larger disk size, migrate pods to the new
   pool using taints and node selectors, then delete the old pool
- C) Edit the existing node pool to increase the disk size — GKE supports
   online node pool disk resizing
- D) Attach an additional persistent disk to each node via the Compute Engine
   console

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Node VM disks should not be manually modified; changes would be overwritten during node repairs or upgrades, and manual resizing is not a supported GKE operation.
  - C) GKE does not support online disk resizing for existing node pool nodes; a new node pool with the desired configuration is the standard migration path.
  - D) Attaching additional disks to GKE nodes is not a supported mechanism for expanding node disk space; the node disk is a single managed persistent disk configured at pool creation.

---

### Question 20 (5 points)

Which command lists all pods across all namespaces in a GKE cluster?

- A) `kubectl get pods`
- B) `kubectl get pods --all-namespaces`
- C) `gcloud container pods list --all`
- D) `kubectl describe pods --namespace=*`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `kubectl get pods` without a namespace flag lists pods only in the current namespace context (usually `default`).
  - C) `gcloud container` does not have a `pods list` subcommand; pod management is done through `kubectl`, not the gcloud CLI.
  - D) `--namespace=*` is not valid kubectl syntax; the correct flag for cross-namespace listing is `--all-namespaces` (or its shorthand `-A`).
