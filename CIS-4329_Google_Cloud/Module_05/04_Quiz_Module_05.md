# Quiz — Module 05

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Virtual Private Cloud (VPC) — Networking Fundamentals

### 10 Questions | 10 Points Each | Total: 100 Points

---

## Question 1

A developer on your team is unable to connect to a new Compute Engine VM on port 22 (SSH). The VM has a public IP address and is running in a custom VPC with no preconfigured firewall rules. What is the most likely cause and the correct fix?

A. The VM's operating system SSH service is not running; reboot the VM to restore it.

B. There is no ingress firewall rule in the VPC allowing TCP port 22 from the developer's source IP; create one targeting the VM's network tag.

C. The VM does not have a network tag assigned, so all SSH connections are globally blocked regardless of firewall rules.

D. Custom VPCs block all external traffic by default; you must contact Google Support to unlock SSH access.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: While it is theoretically possible for the SSH daemon to be stopped, the most common and expected cause of a new VM being unreachable on port 22 in a custom VPC is the absence of a firewall rule. Custom VPCs have no default SSH allow rule — unlike the default VPC, which does.
- Why C is incorrect: The absence of a network tag does not block SSH connections in isolation. Firewall rules can target all instances or use tags. The underlying cause is the absence of an ingress allow rule for port 22, not the absence of a tag.
- Why D is incorrect: Custom VPCs do not require Google Support to enable SSH access. The implied deny-all ingress rule is a configuration baseline, and you add your own explicit allow rules. No special unlocking procedure is needed.

---

## Question 2

Your organization has two GCP VPC networks: `vpc-production` and `vpc-analytics`. You configure VPC peering between them. You also configure VPC peering between `vpc-analytics` and a third network, `vpc-data-lake`. Can VMs in `vpc-production` communicate with VMs in `vpc-data-lake` through `vpc-analytics`?

A. Yes, because VPC peering is transitive — traffic flows through any connected network automatically.

B. Yes, but only if you add a custom static route in `vpc-analytics` pointing to `vpc-data-lake`.

C. No, because VPC peering is non-transitive — `vpc-production` needs a direct peering with `vpc-data-lake` to reach it.

D. No, because the VPCs have overlapping subnet CIDR ranges, which GCP always prevents from communicating.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: GCP VPC peering is explicitly and permanently non-transitive. This is a documented architectural constraint, not a configurable option. Traffic does not flow through an intermediate peered VPC under any circumstances.
- Why B is incorrect: Adding a custom static route in `vpc-analytics` does not enable transitive communication. GCP's routing architecture blocks peered VPCs from serving as transit paths regardless of any route configuration changes.
- Why D is incorrect: The question does not indicate that the VPCs have overlapping CIDRs, and the question is asking about the correct reason for the connectivity limitation. The correct reason is non-transitivity, not CIDR overlap. (Overlapping CIDRs would prevent peering from being established at all, which is a separate scenario.)

---

## Question 3

You need to allow internet traffic on port 443 (HTTPS) to reach only the web-tier VMs in your VPC. Your web-tier VMs all have the network tag `https-server`. Which firewall rule configuration is most appropriate?

A. Create an ingress rule allowing TCP:443 from `0.0.0.0/0`, targeting all instances in the VPC with no tag filter.

B. Create an ingress rule allowing TCP:443 from `0.0.0.0/0`, with a target tag of `https-server`.

C. Create an egress rule allowing TCP:443 from `0.0.0.0/0`, with a target tag of `https-server`.

D. Delete the implied deny-all ingress rule and create a custom allow rule for TCP:443 on all instances.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Applying an ingress rule for TCP:443 to all instances in the VPC would open port 443 on every VM — including database VMs, internal microservices, and administrative systems. This violates the principle of least exposure and creates unnecessary attack surface.
- Why C is incorrect: An egress rule controls traffic flowing outbound from the VMs, not inbound internet traffic arriving at VMs from the internet. Allowing inbound HTTPS connections requires an ingress rule, not an egress rule.
- Why D is incorrect: The implied deny-all ingress rule cannot be deleted or disabled. It is a permanent baseline in every GCP VPC and exists at the lowest priority (65535). You add explicit allow rules on top of it — you cannot remove the baseline.

---

## Question 4

Your company's on-premises data center needs to access GCP resources in your VPC using private IP addresses. The connection must be encrypted in transit, and the expected maximum bandwidth requirement is approximately 500 Mbps. Which connectivity option is most appropriate?

A. Assign public IP addresses to all GCP VMs and connect over the public internet using TLS at the application layer.

B. Configure Cloud VPN with HA VPN tunnels that encrypt traffic using IPsec over the public internet.

C. Provision a Dedicated Interconnect for a private, direct physical fiber connection to Google's network.

D. Use VPC peering between your on-premises network and the GCP VPC.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Routing traffic over the public internet using application-layer TLS does not create an encrypted network tunnel, does not use private IPs between sites, and exposes your GCP resources to public internet discovery and scanning.
- Why C is incorrect: Dedicated Interconnect provides 10 Gbps or 100 Gbps circuits and is designed for organizations with very high bandwidth requirements. At 500 Mbps, Cloud VPN is the appropriate and more cost-effective choice. Dedicated Interconnect would be significantly over-engineered and more expensive for this bandwidth level.
- Why D is incorrect: VPC peering connects two GCP VPC networks to each other over Google's internal network. It cannot connect an on-premises data center to a GCP VPC. On-premises connectivity requires Cloud VPN or Cloud Interconnect.

---

## Question 5

A VM in your VPC has an external IP address and a default route pointing to the internet gateway. The VM cannot reach the internet. Which firewall issue is most likely causing the problem?

A. There is no egress firewall rule explicitly allowing outbound traffic, and the implied default egress is deny-all.

B. There is no ingress firewall rule allowing return traffic from the internet, which blocks replies from reaching the VM.

C. The VM's internal IP is not within the subnet's CIDR range, preventing the route table from forwarding traffic.

D. The external IP address is ephemeral and expired after 60 minutes, blocking all outbound connections.

Correct Answer: A

Distractor Analysis:

- Why B is incorrect: GCP firewall rules are stateful. If outbound traffic is allowed, the corresponding inbound reply packets for established connections are automatically permitted without a separate ingress rule. You do not need an ingress rule for return traffic from an outbound-initiated connection.
- Why C is incorrect: GCP automatically assigns VM internal IPs from the subnet CIDR during creation. It is not possible to create a VM with an IP address outside its subnet's CIDR range through normal GCP operations.
- Why D is incorrect: Ephemeral external IPs do not expire on a timer during the VM's lifetime. They persist as long as the VM is running. They are released only when the VM is stopped or deleted, not based on a time duration.

---

## Question 6

A security engineer wants to ensure that only Compute Engine VMs running as a specific service account (`web-sa@project.iam.gserviceaccount.com`) can accept database connections on port 5432. Which firewall rule target is most appropriate?

A. Target all instances in the VPC and restrict the source range to the web tier subnet CIDR.

B. Target instances by network tag `web-tier` and create a corresponding firewall rule using that tag.

C. Target instances by the service account `web-sa@project.iam.gserviceaccount.com` as the target in the firewall rule.

D. Target instances by hostname using a DNS-based firewall rule for the service account's email address.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Targeting all instances allows any VM to accept database connections, not just the web-tier service VMs. Restricting by source CIDR limits the origin but does not restrict which VMs can receive the connection.
- Why B is incorrect: Network tags can be applied by any user who has permission to modify VM metadata, which includes the VM owner. This is less secure than service account targeting because a malicious or compromised VM user could add the tag to a VM they control.
- Why D is incorrect: GCP firewall rules do not support DNS-based or hostname-based targeting. Firewall rules operate on IP addresses, IP ranges, network tags, and service accounts — not on hostnames or DNS names.

---

## Question 7

You have a VM with no external IP address. The VM needs to call the Cloud Storage API to read data from a bucket. The VM cannot connect to the API. What is the most likely cause and the simplest fix?

A. The VM's service account does not have `roles/storage.objectViewer` on the bucket — grant the role.

B. Private Google Access is not enabled on the VM's subnet — enable it so VMs without external IPs can reach Google APIs.

C. The VM's firewall rules do not allow egress on port 443 to `storage.googleapis.com` — add an egress rule.

D. The VM needs a static external IP address before it can call any Google API.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: While an IAM role is also needed to access the bucket, the scenario describes a connectivity failure, not a permission failure. Private Google Access controls whether VMs without external IPs can reach Google API endpoints at the network level. The IAM role would only matter after the network path is established.
- Why C is incorrect: The implied default in a VPC is allow-all egress. A specific egress firewall rule for port 443 is not needed unless the VPC has a custom deny egress rule. The issue is Private Google Access routing, not a firewall rule.
- Why D is incorrect: VMs without external IPs are a security best practice, not a limitation. Private Google Access exists specifically to allow VMs without external IPs to reach Google APIs through Google's internal network. A static external IP is not required.

---

## Question 8

An architect designs an environment with three VPCs: `corp-vpc`, `dev-vpc`, and `shared-services-vpc`. They configure VPC peering between `corp-vpc` and `shared-services-vpc`, and between `dev-vpc` and `shared-services-vpc`. VMs in `shared-services-vpc` can communicate with both other VPCs. What is true about communication between `corp-vpc` and `dev-vpc`?

A. VMs in `corp-vpc` can communicate with VMs in `dev-vpc` because they both peer with `shared-services-vpc`.

B. VMs in `corp-vpc` cannot communicate with VMs in `dev-vpc` unless a direct peering is created between them.

C. VMs in `corp-vpc` can communicate with VMs in `dev-vpc` if a custom route is added to `shared-services-vpc`.

D. VMs in `corp-vpc` can communicate with VMs in `dev-vpc` if the `shared-services-vpc` admin configures route advertisement.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: VPC peering is non-transitive. A peering between `corp-vpc` and `shared-services-vpc`, and between `dev-vpc` and `shared-services-vpc`, does not create any path between `corp-vpc` and `dev-vpc`. They need a direct peer.
- Why C is incorrect: Adding custom routes to `shared-services-vpc` does not enable transitive traffic flow between the other two VPCs. GCP's VPC peering architecture is designed to prevent transit routing through an intermediate peered VPC regardless of route configuration.
- Why D is incorrect: Route advertisement in GCP VPC peering affects whether routes are exchanged between the peered pair. It does not create transitive routing paths through the advertising VPC. `corp-vpc` and `dev-vpc` would still need a direct peering.

---

## Question 9

You are creating a firewall rule to allow SSH access to VMs in a production VPC. You want to use Google's Identity-Aware Proxy (IAP) service for secure browser-based SSH so that VMs do not need external IP addresses. What source IP range should the firewall rule use to allow IAP-tunneled SSH connections?

A. `0.0.0.0/0` — allow SSH from anywhere on the internet

B. `35.235.240.0/20` — the IP range used by Google's IAP service

C. The CIDR range of the production subnet only

D. The external IP address of each developer's workstation

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Using `0.0.0.0/0` as the source for SSH exposes port 22 to the entire internet, which is a significant security risk even in hardened environments. The purpose of using IAP is to restrict SSH access to the Google IAP service IP range, not to open it to everyone.
- Why C is incorrect: Restricting SSH to the subnet CIDR would only allow SSH connections originating from inside the same subnet. IAP-tunneled connections originate from Google's IAP servers, which are not in your subnet.
- Why D is incorrect: Developer workstations change IP addresses (working remotely, VPNs, coffee shops), making per-workstation IP allowlisting operationally impractical and requiring constant updates. IAP handles authentication so you do not need to manage source IPs.

---

## Question 10

Which statement most accurately describes the difference between the default VPC and a custom VPC created with `--subnet-mode=custom` in GCP?

A. The default VPC has no firewall rules; a custom VPC is pre-populated with rules that allow SSH and HTTP by default.

B. The default VPC automatically creates one subnet per region with predefined CIDR ranges and includes pre-configured firewall rules allowing SSH, RDP, and ICMP from anywhere; a custom VPC starts with no subnets and no firewall rules beyond the implied defaults.

C. A custom VPC is regional; the default VPC is global.

D. The default VPC and custom VPCs are functionally identical — the only difference is the name assigned at creation time.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: This reverses the reality. The default VPC does have pre-configured firewall rules. A new custom VPC has no custom firewall rules — only the two implied defaults (deny-all ingress and allow-all egress) that exist in every VPC.
- Why C is incorrect: Both the default VPC and custom VPCs are global resources in GCP. All GCP VPCs span all regions regardless of how they are created. The scope difference between them is about subnet creation mode, not network geographic scope.
- Why D is incorrect: The default VPC and custom VPCs are meaningfully different in their initial configuration. The default VPC comes with auto-created subnets in every region and pre-configured firewall rules. A custom VPC starts empty. These differences are operationally significant for production environments.

---

End of Quiz — Module 05

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
