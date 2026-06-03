# Quiz: Module 05 — Virtual Private Cloud Networking

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
This quiz covers VPC architecture, subnets, firewall rules, VPC peering,
Shared VPC, hybrid connectivity, load balancing, and Cloud Armor.

---

## Question 1

Which statement correctly describes the scope of a GCP VPC network?

- A) A VPC is scoped to a single zone and must be replicated to other zones
- B) A VPC is scoped to a single region and subnets automatically span all
     zones within that region
- C) A VPC is a global resource; subnets within it are regional
- D) A VPC is scoped to a single project and cannot span multiple regions

**Correct Answer:** C

**Explanation:** GCP VPCs are global resources — a single VPC can have subnets
in any or all GCP regions simultaneously. The subnets themselves are regional
resources. This is unique to GCP compared to AWS and Azure, where VPCs are
region-scoped. This global nature allows a VM in us-central1 to communicate
privately with a VM in europe-west1 on the same VPC.

---

## Question 2

You have two firewall rules on the same VPC targeting the same VM:

- Rule A: ALLOW TCP:22, priority 800
- Rule B: DENY TCP:22, priority 1000

What is the effective behavior when someone tries to SSH to that VM?

- A) DENY — the deny rule overrides the allow rule
- B) ALLOW — the allow rule wins because lower priority number wins
- C) DENY — when rules conflict, deny always wins regardless of priority
- D) ALLOW — the most recently created rule takes precedence

**Correct Answer:** B

**Explanation:** In GCP firewall rules, lower priority number means higher
priority. Rule A with priority 800 is evaluated before Rule B with priority
1000. Since Rule A allows TCP:22, traffic is permitted and Rule B is never
reached. GCP does not have a "deny always wins" tie-breaker — it strictly uses
numeric priority.

---

## Question 3

Your organization has three GCP VPCs: VPC-Alpha, VPC-Beta, and VPC-Gamma.
You configure VPC peering between Alpha and Beta, and between Beta and Gamma.
A VM in VPC-Alpha tries to connect to a VM in VPC-Gamma using its private IP.
What happens?

- A) The connection succeeds because Beta acts as a transit network
- B) The connection fails because VPC peering is non-transitive
- C) The connection succeeds if you enable transitive peering in the console
- D) The connection succeeds if the IP ranges do not overlap

**Correct Answer:** B

**Explanation:** GCP VPC peering is non-transitive. Alpha peers with Beta and
Beta peers with Gamma, but that does not give Alpha any access to Gamma. To
allow Alpha-Gamma communication, you must explicitly create a peering
relationship between Alpha and Gamma. There is no "transitive peering" setting
in GCP.

---

## Question 4

A large enterprise wants multiple project teams to deploy GCP resources into a
centrally managed network. The network team should own firewall rules and
subnets, while each project team manages only their own VMs. Which GCP feature
best implements this model?

- A) VPC peering between each team's project and the network team's project
- B) Shared VPC with the network team's project as the host project
- C) Giving the network team `roles/owner` on all project teams' projects
- D) Creating a separate VPC in each project and using static routes to connect

**Correct Answer:** B

**Explanation:** Shared VPC is designed exactly for this use case. The host
project owns the VPC, subnets, firewall rules, and routes. Service projects
(the individual team projects) can deploy VMs into the host VPC's subnets
without being able to modify the network configuration. This provides
centralized network governance with decentralized resource ownership.

---

## Question 5

A company needs to connect its on-premises data center to GCP. The connection
requires a consistent 5 Gbps bandwidth with low latency, and the company's
security policy prohibits traffic from traversing the public internet.
Which connectivity option should they choose?

- A) Cloud VPN with static routing
- B) Cloud VPN with HA VPN
- C) Dedicated Interconnect
- D) Direct SSH tunnels over the internet

**Correct Answer:** C

**Explanation:** Dedicated Interconnect provides a physical circuit (10 Gbps
or 100 Gbps) between the company's network and Google's network. Traffic never
traverses the public internet. Cloud VPN (options A and B) uses IPsec encryption
over the internet, which violates the security policy. Partner Interconnect
would also work but Dedicated Interconnect is the direct answer for 5+ Gbps
with no internet transit.

---

## Question 6

You need to deploy a globally distributed web application that serves users in
North America, Europe, and Asia. The application uses HTTPS, needs SSL
termination at the edge, and must be protected against DDoS attacks.
Which load balancer type should you use?

- A) External Passthrough Network Load Balancer (regional)
- B) Internal Application Load Balancer
- C) External Application Load Balancer (global)
- D) External Regional Application Load Balancer

**Correct Answer:** C

**Explanation:** The External Application Load Balancer (global) is the correct
choice. It is a Layer 7 load balancer with a global Anycast IP that serves
traffic from Google's edge PoPs closest to users worldwide. It handles HTTPS
with SSL termination at the edge and integrates with Cloud Armor for DDoS
protection. The regional options do not serve global users from edge PoPs.
Internal load balancers are not accessible from the internet.

---

## Question 7

A firewall rule uses `target-tags=web-server` to apply to specific VMs.
A developer accidentally adds the `web-server` tag to a database VM.
What is the security implication, and how could this risk be mitigated?

- A) No risk — tags only affect outbound traffic
- B) The database VM would now be exposed to the same inbound traffic allowed
     for web servers; use service account-based targeting instead of tags to
     mitigate
- C) Tags cannot be accidentally assigned — they require an IAM permission
     not held by developers
- D) The database VM would lose its database firewall rules automatically

**Correct Answer:** B

**Explanation:** Network tags are simple strings that can be added or removed by
anyone with `compute.instances.setTags` permission (included in `roles/compute.instanceAdmin`).
Adding the wrong tag to a VM incorrectly exposes it to the associated firewall
rules. Using service account-based targeting instead of tags mitigates this
risk because changing a VM's service account requires a separate, more
privileged IAM action.

---

## Question 8

Which two IP ranges must be permitted in your ingress firewall rules to allow
GCP load balancer health checks to reach your backend VMs?

- A) 10.0.0.0/8 and 172.16.0.0/12 (private RFC 1918 ranges)
- B) 35.191.0.0/16 and 130.211.0.0/22 (GCP health checker ranges)
- C) 0.0.0.0/0 (allow all internet)
- D) The external IP of the load balancer only

**Correct Answer:** B

**Explanation:** GCP health checkers send probes from the ranges 35.191.0.0/16
and 130.211.0.0/22. If these ranges are not permitted in the ingress firewall
rules on the appropriate port, the health checker cannot reach the VM, the VM
is marked unhealthy, and the load balancer stops sending traffic to it.

---

## Question 9

Private Google Access is enabled on a subnet. What does this allow?

- A) VMs in the subnet can access private services in other GCP projects
- B) VMs in the subnet without external IPs can still reach Google APIs and
     services such as Cloud Storage and BigQuery
- C) The subnet is made private and no external IPs can be assigned to VMs
- D) VMs in the subnet can access on-premises resources via Cloud VPN

**Correct Answer:** B

**Explanation:** Private Google Access allows VM instances in a subnet to
communicate with Google APIs and services (Cloud Storage, BigQuery, Pub/Sub,
etc.) using only their internal IP address — no external IP required. Without
Private Google Access, a VM with no external IP cannot reach Google's public
API endpoints.

---

## Question 10

An engineer creates a new custom-mode VPC. No firewall rules have been added.
A VM is deployed in the VPC and assigned an external IP. Another user tries
to SSH to the VM from the internet. What happens?

- A) The SSH connection succeeds because GCP allows SSH by default
- B) The SSH connection fails because the custom VPC has an implied deny all
     ingress rule at priority 65535 and no explicit allow rule for SSH
- C) The SSH connection succeeds if the VM has a valid external IP address
- D) The SSH connection fails because custom VPCs do not support external IPs

**Correct Answer:** B

**Explanation:** Every GCP VPC has an implied deny all ingress rule at
priority 65535. In a custom-mode VPC, there are no automatically created
firewall rules (unlike the default VPC). Without an explicit rule allowing
TCP:22, all inbound traffic — including SSH — is blocked by the implied deny.
The engineer must create a firewall rule explicitly allowing SSH.

---

End of Quiz — Module 05

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
