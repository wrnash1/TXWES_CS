# Quiz: Module 05 – Virtual Private Cloud (VPC): Networking Fundamentals
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
A developer on your team is unable to connect to a new Compute Engine VM on port 22 (SSH). The VM has a public IP address and is running in your custom VPC. What is the most likely cause, and what is the correct fix?

A) The VM's operating system SSH service is not running; reboot the VM to restore it.
B) There is no ingress firewall rule in the VPC allowing TCP port 22 from the developer's source IP; create one targeting the VM's network tag.
C) The VM does not have a network tag assigned, so all SSH connections are blocked by default.
D) VPC networks block all external traffic by default; you must configure a Cloud Armor security policy to allow SSH.

*   **Correct Answer:** B) There is no ingress firewall rule in the VPC allowing TCP port 22 from the developer's source IP; create one targeting the VM's network tag.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While an SSH service could theoretically be stopped, the most common cause of an unreachable new VM is the absence of a firewall rule — the VPC's implied default is deny-all ingress, so no inbound port is open without an explicit allow rule.
    *   *Why C is incorrect:* The absence of a network tag does not by itself block SSH; it simply means no tag-based firewall rules apply. The underlying deny-all ingress default still blocks port 22 regardless of tags.
    *   *Why D is incorrect:* Cloud Armor is a web application firewall for HTTP(S) load balancers — it is not used to control SSH access to individual VMs. Firewall rules are the correct mechanism.

---

**Question 2**
Your organization has two GCP VPC networks: `vpc-production` and `vpc-analytics`. You configure VPC peering between them. VMs in `vpc-production` can now communicate with VMs in `vpc-analytics`. You also configure VPC peering between `vpc-analytics` and a third network, `vpc-data-lake`. Can VMs in `vpc-production` reach VMs in `vpc-data-lake` through `vpc-analytics`?

A) Yes, because VPC peering is transitive — traffic flows through any connected network.
B) Yes, but only if you add a custom static route in `vpc-analytics` pointing to `vpc-data-lake`.
C) No, because VPC peering is non-transitive — `vpc-production` needs a direct peering with `vpc-data-lake` to communicate with it.
D) No, because peered VPCs cannot have overlapping subnet CIDR ranges, which prevents any transitive routing.

*   **Correct Answer:** C) No, because VPC peering is non-transitive — `vpc-production` needs a direct peering with `vpc-data-lake` to communicate with it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GCP VPC peering is explicitly non-transitive. This is a documented limitation and a frequent ACE exam topic — traffic does not flow through an intermediate peered network.
    *   *Why B is incorrect:* Adding a custom static route in `vpc-analytics` does not enable transitive peering; GCP's routing architecture prevents peered networks from using each other as transit paths regardless of route configuration.
    *   *Why D is incorrect:* While overlapping CIDRs do prevent peering, that is a separate issue. The question describes a valid topology; the answer is that non-transitive peering is the reason `vpc-production` cannot reach `vpc-data-lake`.

---

**Question 3**
You need to allow internet traffic on port 443 (HTTPS) to reach only the web-tier VMs in your VPC. Your web-tier VMs all have the network tag `https-server`. Which firewall rule configuration is most appropriate?

A) Create an ingress rule allowing TCP:443 from `0.0.0.0/0`, targeting all instances in the VPC with no tag filter.
B) Create an ingress rule allowing TCP:443 from `0.0.0.0/0`, with a target tag of `https-server`.
C) Create an egress rule allowing TCP:443 from `0.0.0.0/0`, with a target tag of `https-server`.
D) Disable the implied deny-all ingress rule and create a custom allow rule for TCP:443.

*   **Correct Answer:** B) Create an ingress rule allowing TCP:443 from `0.0.0.0/0`, with a target tag of `https-server`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Targeting all instances with no tag filter opens port 443 on every VM in the VPC — including database VMs and internal services — which violates the principle of least exposure.
    *   *Why C is incorrect:* An egress rule controls outbound traffic leaving VMs, not inbound internet traffic arriving at VMs. Allowing inbound HTTPS requires an ingress rule.
    *   *Why D is incorrect:* The implied deny-all ingress rule cannot be deleted or disabled; it is a permanent baseline. You add explicit allow rules on top of it — you never remove the baseline deny.

---

**Question 4**
Your company's on-premises data center needs to securely access GCP resources in your VPC using private IP addresses. The connection must be encrypted, and the expected bandwidth is approximately 500 Mbps. Which connectivity option is most appropriate?

A) Assign public IP addresses to all GCP VMs and connect over the public internet using TLS.
B) Configure Cloud VPN with HA VPN tunnels over the public internet using IPsec encryption.
C) Provision a Dedicated Interconnect for a private, direct physical connection to Google's network.
D) Use VPC peering between your on-premises network and the GCP VPC.

*   **Correct Answer:** B) Configure Cloud VPN with HA VPN tunnels over the public internet using IPsec encryption.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Routing traffic over the public internet with TLS does not use private IPs and does not create an encrypted tunnel at the network level; it also exposes GCP resources to public internet scanning.
    *   *Why C is incorrect:* Dedicated Interconnect provides 10 Gbps or 100 Gbps circuits and is appropriate for very high bandwidth requirements (multi-gigabit); at 500 Mbps, Cloud VPN is the more cost-appropriate choice.
    *   *Why D is incorrect:* VPC peering connects two GCP VPC networks to each other — it cannot be used to connect an on-premises data center to a GCP VPC.

---

**Question 5**
A new VM in your VPC cannot reach the internet, even though it has an external IP address. The VPC has a default route pointing to the internet gateway. Which firewall rule issue is most likely causing the problem?

A) There is no egress firewall rule explicitly allowing outbound traffic, and the default egress rule is deny-all.
B) There is no ingress firewall rule allowing return traffic from the internet to the VM's external IP.
C) The VM's internal IP is not in the subnet's CIDR range, so the route table cannot forward traffic.
D) The external IP address is ephemeral and expires after 60 minutes, blocking outbound connections.

*   **Correct Answer:** A) There is no egress firewall rule explicitly allowing outbound traffic, and the default egress rule is deny-all.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* GCP firewall rules are stateful — if outbound traffic is allowed, the corresponding inbound reply packets are automatically permitted without a separate ingress rule.
    *   *Why C is incorrect:* GCP automatically assigns VM internal IPs from the subnet CIDR at creation time; a VM cannot be created with an IP outside its subnet range.
    *   *Why D is incorrect:* Ephemeral external IPs do not expire on a timer during a VM's lifetime; they are released only when the VM is stopped or deleted, not after a fixed duration.
