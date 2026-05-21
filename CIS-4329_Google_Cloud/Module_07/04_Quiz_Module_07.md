# Quiz: Module 07 – Kubernetes Engine (GKE): Cluster Management
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your team wants to deploy a containerized microservice on GKE. They want Google to fully manage all infrastructure including node provisioning, scaling, and upgrades. Your team should only need to define and deploy pods. Which GKE mode should you use?

A) GKE Standard with node auto-upgrade enabled
B) GKE Autopilot
C) GKE Standard with Cluster Autoscaler enabled
D) Anthos GKE on-premises

*   **Correct Answer:** B) GKE Autopilot
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GKE Standard with auto-upgrade still requires you to configure and manage node pools, choose machine types, and set minimum/maximum node counts — your team retains node-level responsibility.
    *   *Why C is incorrect:* Cluster Autoscaler in Standard mode scales the number of nodes in existing node pools but does not remove the need to define and manage those node pools in the first place.
    *   *Why D is incorrect:* Anthos GKE on-premises runs Kubernetes on your own data center hardware — it provides no Google-managed infrastructure and is the opposite of what is described.

---

**Question 2**
You have deployed an application on GKE. The application processes user requests, and you want it to automatically add more pod replicas when CPU utilization exceeds 70%, and remove replicas when utilization drops back below that threshold. Which Kubernetes resource implements this behavior?

A) Cluster Autoscaler configured on the node pool
B) Horizontal Pod Autoscaler (HPA) targeting the application's Deployment
C) A Kubernetes CronJob that runs a scaling script every 5 minutes
D) A Managed Instance Group with CPU-based autoscaling attached to the cluster

*   **Correct Answer:** B) Horizontal Pod Autoscaler (HPA) targeting the application's Deployment
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cluster Autoscaler scales the number of nodes (VMs) in a node pool when there is insufficient capacity to schedule pods — it does not scale the number of pod replicas based on CPU utilization.
    *   *Why C is incorrect:* A CronJob runs a task on a time schedule — it has no awareness of real-time CPU metrics and is not the correct mechanism for reactive autoscaling.
    *   *Why D is incorrect:* Managed Instance Groups are a Compute Engine concept that manage raw VMs — they have no integration with Kubernetes pod scheduling or Deployment replicas.

---

**Question 3**
You need to give a pod running in your GKE cluster access to a Cloud Storage bucket so it can read and write objects. Following security best practices, which approach should you use?

A) Download a Service Account key JSON file and mount it as a Kubernetes Secret in the pod.
B) Grant `roles/storage.objectAdmin` to the Compute Engine default Service Account used by the cluster nodes.
C) Use Workload Identity to link a Kubernetes Service Account to a GCP Service Account with `roles/storage.objectAdmin` on the bucket.
D) Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in the pod spec to point to the cluster's built-in credentials.

*   **Correct Answer:** C) Use Workload Identity to link a Kubernetes Service Account to a GCP Service Account with `roles/storage.objectAdmin` on the bucket.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Mounting a Service Account key JSON file as a Secret is a security anti-pattern — if the Secret is exposed or the pod is compromised, the long-lived key can be exfiltrated. Workload Identity provides short-lived, automatically rotated credentials.
    *   *Why B is incorrect:* Granting a broad role to the node's default Service Account gives every pod on every node in the cluster that access — violating least privilege. Workload Identity scopes credentials to individual pods.
    *   *Why D is incorrect:* There is no built-in cluster credentials file that pods can reference via `GOOGLE_APPLICATION_CREDENTIALS`; this would require the same key file approach described in option A.

---

**Question 4**
You perform a rolling update to your GKE Deployment and the new version contains a critical bug. Users are reporting errors. You need to restore the previous working version as quickly as possible. Which command accomplishes this?

A) `kubectl delete deployment my-app && kubectl apply -f old-deployment.yaml`
B) `kubectl rollout undo deployment/my-app`
C) `gcloud container clusters upgrade my-cluster --rollback`
D) `kubectl scale deployment my-app --replicas=0` then re-apply the old manifest

*   **Correct Answer:** B) `kubectl rollout undo deployment/my-app`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deleting the Deployment and reapplying an old manifest causes complete downtime during the deletion window and requires you to have the old YAML readily available — `rollout undo` achieves an instant rollback with zero downtime.
    *   *Why C is incorrect:* `gcloud container clusters upgrade` manages cluster control plane and node version upgrades — it has nothing to do with rolling back an application Deployment.
    *   *Why D is incorrect:* Scaling to zero replicas takes the application completely offline before the old version is restored, causing unnecessary downtime that a rolling rollback avoids.

---

**Question 5**
You want to expose your GKE application to external internet traffic with path-based routing: requests to `/api` should go to one backend service and requests to `/web` should go to another. Which Kubernetes resource and corresponding GCP resource combination achieves this?

A) Two separate LoadBalancer Services — one for `/api` and one for `/web`.
B) A Kubernetes Ingress resource, which provisions a Global HTTP(S) Load Balancer with URL map rules.
C) A NodePort Service combined with a Cloud VPN tunnel for external access.
D) A ClusterIP Service exposed externally by adding an external IP address directly to the Service spec.

*   **Correct Answer:** B) A Kubernetes Ingress resource, which provisions a Global HTTP(S) Load Balancer with URL map rules.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* LoadBalancer Services each get their own L4 external IP and cannot perform path-based routing — each service handles its own port but has no knowledge of URL paths.
    *   *Why C is incorrect:* NodePort Services expose a port on each cluster node but are not designed for production external traffic routing; Cloud VPN is for private network connectivity, not public HTTP access.
    *   *Why D is incorrect:* ClusterIP Services are internal-only by design; assigning an external IP directly to a ClusterIP Service is not a supported GKE pattern and provides no HTTP path-routing capability.
