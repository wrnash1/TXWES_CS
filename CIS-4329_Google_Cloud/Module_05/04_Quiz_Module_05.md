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

---

### Question 11 (5 points)

You create a custom VPC in auto mode. What subnets are automatically
provisioned?

- A) No subnets — auto mode requires you to create all subnets manually
- B) One subnet per GCP region, each with a pre-defined IP range from
   `10.128.0.0/9`
- C) One subnet in the default region selected during VPC creation
- D) One subnet per zone in the default region

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Auto mode specifically auto-creates subnets; that behavior is the defining characteristic of auto mode versus custom mode.
  - C) Auto mode creates one subnet per region across all GCP regions simultaneously, not just the default region.
  - D) Subnets are regional resources, not zonal; one subnet per region is created, covering all zones within that region automatically.

---

### Question 12 (5 points)

A VM in subnet `10.0.1.0/24` needs to communicate with a VM in subnet
`10.0.2.0/24` within the same custom VPC. No firewall rules have been
configured. Will communication succeed?

- A) Yes — VMs within the same VPC can always communicate freely regardless
   of firewall rules
- B) No — the default implied deny-all ingress rule blocks all traffic;
   an explicit allow rule between the subnets must be created
- C) Yes — subnets in the same VPC use route-based communication that bypasses
   firewall rules
- D) No — VMs on different subnets require VPC peering to communicate

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) In a custom VPC with no rules added, the implied deny-all ingress rule at priority 65535 blocks all inbound traffic, including traffic from other subnets in the same VPC.
  - C) Firewall rules apply to all traffic entering a VM's network interface, regardless of whether the source is another subnet in the same VPC; routes determine the path but firewalls still filter.
  - D) VPC peering connects separate VPCs; subnets within the same VPC do not require peering — they only need a firewall allow rule for the desired traffic.

---

### Question 13 (5 points)

What is the primary difference between Partner Interconnect and Dedicated
Interconnect?

- A) Partner Interconnect uses encryption; Dedicated Interconnect does not
- B) Partner Interconnect connects to Google's network through a supported
   service provider; Dedicated Interconnect requires a physical connection
   directly from the customer's facility to a Google colocation facility
- C) Dedicated Interconnect supports up to 1 Gbps; Partner Interconnect
   supports up to 100 Gbps
- D) Partner Interconnect is only available in the United States

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Neither type of Interconnect provides encryption by default; both carry traffic over private physical circuits. Cloud VPN can be layered on top for encryption if needed.
  - C) Dedicated Interconnect supports 10 Gbps or 100 Gbps per circuit; Partner Interconnect supports 50 Mbps to 50 Gbps through the partner's network. The bandwidth figures in option C are reversed.
  - D) Partner Interconnect is available globally through supported service providers in many countries, not only the US.

---

### Question 14 (5 points)

A GCP project has the default VPC. The default VPC includes a firewall rule
`default-allow-internal`. What traffic does this rule permit?

- A) All traffic between any VMs in any GCP project
- B) All protocols and ports between VMs on the same default VPC
- C) Only TCP:22 (SSH) and TCP:3389 (RDP) between VMs on the default VPC
- D) ICMP only between VMs on the default VPC

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `default-allow-internal` applies only within the same VPC network; it does not permit traffic between different projects or different VPCs.
  - C) `default-allow-internal` allows all protocols and all ports between instances on the default VPC; SSH and RDP are covered by `default-allow-ssh` and `default-allow-rdp` respectively.
  - D) ICMP-only would describe a much more restrictive rule; `default-allow-internal` permits TCP, UDP, and ICMP on all ports within the VPC.

---

### Question 15 (5 points)

You need to allow a Cloud Run service (no external IP, serverless) to
access a private Redis instance (Memorystore) in a VPC. What networking
component enables this?

- A) Cloud NAT configured on the VPC subnet
- B) A Serverless VPC Access connector attached to the Cloud Run service
- C) VPC peering between the serverless network and the customer VPC
- D) A Cloud VPN tunnel between the Cloud Run region and the VPC

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud NAT provides outbound internet access for VMs without external IPs; it does not route traffic from serverless services to private VPC resources.
  - C) VPC peering connects two VPCs together; serverless services like Cloud Run do not reside in a customer-controlled VPC and cannot be a peer in a standard VPC peering relationship.
  - D) Cloud VPN connects on-premises networks or other clouds to a GCP VPC; it is not the mechanism for connecting serverless services to private VPC resources within the same GCP project.

---

### Question 16 (5 points)

An organization policy sets `constraints/compute.restrictVpcPeering` to deny
all VPC peering requests in the organization. A developer in a project within
that organization tries to create a VPC peering connection. What happens?

- A) The peering succeeds if the developer has `roles/compute.networkAdmin`
- B) The peering request is blocked by the organization policy regardless of
   the developer's IAM role
- C) The policy only applies to the organization node, not to individual
   projects
- D) The developer can override the organization policy by setting a
   project-level policy to allow peering

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Organization Policy constraints operate independently of IAM; even a user with `roles/owner` cannot perform actions blocked by an Organization Policy.
  - C) Organization Policy constraints applied at the Organization node cascade down to all folders and projects in the organization.
  - D) Project-level policies can only make constraints more restrictive than the parent; they cannot override a deny set at the Organization level.

---

### Question 17 (5 points)

Which GCP networking feature automatically assigns outbound public IP
addresses to VMs that have no external IP, allowing them to make outbound
internet connections while remaining unreachable from the internet?

- A) Private Google Access
- B) Cloud NAT
- C) External Load Balancer with VIP
- D) Shared VPC with a public subnet

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Private Google Access allows VMs without external IPs to reach Google APIs and GCP services (like Cloud Storage), but it does not provide general internet access to arbitrary public destinations.
  - C) An External Load Balancer provides inbound internet connectivity to backend VMs; it does not enable outbound internet access for VMs with no external IP.
  - D) Shared VPC is a network governance feature for sharing subnets across projects; it does not automatically provide outbound internet connectivity to VMs without external IPs.

---

### Question 18 (5 points)

A firewall rule uses `--source-ranges=35.191.0.0/16,130.211.0.0/22` and
`--target-tags=http-server`. What is this rule's purpose?

- A) It blocks load balancer traffic from reaching the tagged VMs
- B) It allows health check probes from GCP load balancers to reach VMs
   tagged `http-server`
- C) It allows all internet traffic on all ports to VMs tagged `http-server`
- D) It allows VMs tagged `http-server` to send traffic to the internet

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) This is an ingress allow rule (the ranges `35.191.0.0/16` and `130.211.0.0/22` are the GCP health checker source ranges); it permits traffic, not blocks it.
  - C) The source ranges `35.191.0.0/16` and `130.211.0.0/22` are specifically Google's health check probe ranges, not the entire internet; the rule is narrowly scoped to those two address blocks.
  - D) A rule specifying `--source-ranges` applies to ingress traffic coming from those ranges; egress rules use `--destination-ranges`.

---

### Question 19 (5 points)

You configure Cloud Armor with a security policy that includes:

- Rule 1 priority 100: Allow requests from `203.0.113.0/24`
- Rule 2 priority 500: Deny SQL injection (preconfigured WAF rule)
- Default rule: Allow all

A request arrives from `203.0.113.5` containing a SQL injection payload.
What action is taken?

- A) The request is allowed because Rule 1 matches first at priority 100
- B) The request is denied because the WAF rule detects SQL injection
- C) The default rule allows the request because the WAF rule only applies to
   non-allowed IPs
- D) Both rules match and the result is undefined behavior

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud Armor evaluates rules in priority order; Rule 1 at priority 100 is evaluated before Rule 2 at priority 500. Because the source IP matches Rule 1 (allow), the allow action is applied and evaluation stops before reaching the WAF rule.
  - C) Cloud Armor does not have a concept of "non-allowed IPs" that bypasses further evaluation; it strictly evaluates rules in numeric priority order and stops at the first match.
  - D) Cloud Armor's behavior is well-defined: the first matching rule wins; there is no undefined behavior when multiple rules could match.

---

### Question 20 (5 points)

What is the purpose of a VPC flow log, and which resource must it be enabled
on?

- A) VPC flow logs record DNS query activity; enabled on the VPC network
- B) VPC flow logs record a sample of network flows to and from VM network
   interfaces; enabled on individual subnets
- C) VPC flow logs record firewall rule evaluation decisions; enabled on
   individual firewall rules
- D) VPC flow logs record all API calls in the project; enabled on the
   project's audit log configuration

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) DNS query logging is a separate feature of Cloud DNS private zones; VPC flow logs record network packet flows, not DNS queries.
  - C) Firewall rule evaluation decisions are recorded in firewall logs (a separate feature enabled per firewall rule), not VPC flow logs.
  - D) API call logging is handled by Cloud Audit Logs; VPC flow logs are specifically for network traffic metadata at the subnet level.
