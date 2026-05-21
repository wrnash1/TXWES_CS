# Quiz: Module 12 - Network Virtualization and SDN
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
An enterprise data center needs to run 50 virtual machines with maximum performance, security isolation between VMs, and no dependency on a host operating system. Which hypervisor type meets these requirements?
A) Type 2 hypervisor — runs as an application on a standard Windows or Linux host OS, providing easy VM management through the host's interface
B) Type 1 hypervisor — runs directly on the physical hardware with no host OS, providing native hardware access for maximum VM performance and isolation
C) A container engine (Docker) — runs application containers that share the host OS kernel, providing lightweight workload isolation
D) A Type 2 hypervisor with hardware-assisted virtualization enabled in BIOS to compensate for the performance overhead of running on a host OS
*   **Correct Answer:** B) Type 1 hypervisor — runs directly on the physical hardware with no host OS, providing native hardware access for maximum VM performance and isolation
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Type 2 hypervisor runs on top of a host OS — this adds overhead and creates a dependency on the host OS for security and stability. In enterprise data centers, Type 2 is used for development/testing, not production workloads requiring maximum performance.
    *   *Why C is incorrect:* Containers (Docker) share the host OS kernel — they provide process-level isolation, not full VM isolation with separate OS instances. They do not meet the requirement for complete VM isolation and do not run full operating systems per workload.
    *   *Why D is incorrect:* Hardware-assisted virtualization (VT-x/AMD-V) reduces Type 2 overhead but does not eliminate the fundamental performance penalty of running through a host OS. Type 1 remains the correct choice for enterprise production environments regardless of BIOS settings.

---

**Question 2**
A network architect is designing a data center that needs to support 20,000 isolated tenant networks for a cloud provider. Each tenant requires complete Layer 2 isolation from other tenants. The existing physical network uses standard IP routing. Which overlay technology provides the required scale?
A) 802.1Q VLANs — support up to 4,094 unique VLAN IDs using a 12-bit VLAN identifier in the frame header
B) 802.1ad (QinQ) double-tagging — nests a customer VLAN tag inside a provider VLAN tag, extending capacity to approximately 4,094 × 4,094 combinations
C) VXLAN — uses a 24-bit VNID supporting over 16 million virtual network segments, encapsulated in UDP for transport across Layer 3 networks
D) MPLS VPN — uses label-switching paths to create isolated Layer 3 VPNs between carrier sites over a shared backbone
*   **Correct Answer:** C) VXLAN — uses a 24-bit VNID supporting over 16 million virtual network segments, encapsulated in UDP for transport across Layer 3 networks
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 802.1Q supports a maximum of 4,094 usable VLAN IDs — far short of the 20,000 isolated networks required. This is precisely the scaling limitation that VXLAN was designed to overcome.
    *   *Why B is incorrect:* QinQ (802.1ad) theoretically extends VLAN capacity, but practical implementations are limited by provider VLAN space and vendor support. More importantly, QinQ remains a Layer 2 technology that cannot cross Layer 3 boundaries without additional tunneling, making it unsuitable for modern cloud data centers.
    *   *Why D is incorrect:* MPLS VPNs create Layer 3 isolation between sites in a carrier network — they do not create the Layer 2 tenant isolation within a data center required for VM-to-VM communication within each tenant's virtual network. MPLS is a WAN/carrier technology, not a data center overlay.

---

**Question 3**
A network engineer is describing the SDN architecture to a colleague. They explain that one component makes all routing and forwarding decisions for the entire network, while another component simply forwards packets according to programmed rules. Which terms correctly identify these two components?
A) The management plane makes all forwarding decisions; the control plane monitors and reports network statistics
B) The control plane makes routing and forwarding decisions; the data plane forwards packets according to the rules the control plane programs
C) The data plane makes routing decisions using its routing table; the control plane enforces security policies on forwarded traffic
D) The forwarding plane sets routing policies via CLI; the management plane executes packet forwarding in hardware
*   **Correct Answer:** B) The control plane makes routing and forwarding decisions; the data plane forwards packets according to the rules the control plane programs
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The management plane is the interface used to configure and monitor network devices (CLI, SNMP, APIs) — it does not make packet forwarding decisions. The control plane makes routing decisions; the data plane forwards packets.
    *   *Why C is incorrect:* This reverses the roles. The data plane is purely a forwarding engine — it does not make routing decisions. The control plane (centralized in the SDN controller) determines routing logic. Security policy enforcement can be part of the control plane's programming, not the data plane's autonomous decision-making.
    *   *Why D is incorrect:* CLI configuration is a management plane function, not a forwarding plane function. The forwarding plane (data plane) executes packet forwarding — it does not set policies. This answer mislabels both planes and conflates management tasks with forwarding.

---

**Question 4**
A company wants to replace its aging dedicated hardware firewall appliances, load balancers, and WAN optimizers with software instances running on standard x86 servers in their data center. This will reduce hardware refresh costs and allow rapid deployment of new security services. Which technology model describes this approach?
A) SDN (Software-Defined Networking) — centralizes the control plane in a software controller to program forwarding behavior across the network
B) NFV (Network Functions Virtualization) — replaces dedicated network hardware appliances with software-based virtual network functions running on standard servers
C) IaaS (Infrastructure as a Service) — migrates on-premises hardware to cloud-hosted virtual machines managed by a third-party provider
D) Type 1 hypervisor deployment — installs a bare-metal hypervisor on existing hardware to consolidate multiple network appliances onto fewer physical hosts
*   **Correct Answer:** B) NFV (Network Functions Virtualization) — replaces dedicated network hardware appliances with software-based virtual network functions running on standard servers
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SDN separates the control plane from the data plane to centralize routing intelligence — it does not specifically address replacing hardware appliances with software. SDN is about programmable network control, not hardware replacement with software equivalents.
    *   *Why C is incorrect:* IaaS moves workloads to a third-party cloud provider's infrastructure — the company in the scenario is keeping equipment in their own data center. IaaS does not describe running network functions as software on on-premises servers.
    *   *Why D is incorrect:* Installing a Type 1 hypervisor consolidates servers but does not specifically describe replacing network appliance functions with virtual equivalents. NFV specifically refers to virtualizing network functions (firewall, load balancer, WAN optimizer) — the hypervisor is just the platform NFV runs on, not the solution itself.

---

**Question 5**
A security team is reviewing the virtual networking configuration of a VMware ESXi host running 12 production VMs. They identify three security concerns: (1) VMs from different security zones share the same virtual switch port group without VLAN separation, (2) management traffic to the ESXi host uses the same vSwitch as VM traffic, (3) a compromised VM could potentially send crafted frames to escape its VLAN. Which combination of controls addresses all three concerns?
A) Create separate virtual switches (vSwitches) for VM traffic and management traffic, assign each security zone's VMs to separate VLAN-tagged port groups, and enable the security policy settings on the vSwitch to block forged MAC transmits and promiscuous mode.
B) Migrate all VMs to a Type 2 hypervisor, configure host-based firewalls on each VM, and deploy an IDS sensor on the physical network uplink.
C) Configure EtherChannel between the ESXi host and the physical switch to increase bandwidth, assign all VMs to VLAN 1, and enable BPDU Guard on the ESXi host's uplink ports.
D) Deploy a dedicated physical firewall between each VM and the virtual switch, configure static ARP entries on all VMs, and enable SNMP monitoring on the ESXi management interface.
*   **Correct Answer:** A) Create separate virtual switches (vSwitches) for VM traffic and management traffic, assign each security zone's VMs to separate VLAN-tagged port groups, and enable the security policy settings on the vSwitch to block forged MAC transmits and promiscuous mode.
*   **Distractor Analysis:**
    *   *Why A is correct:* Separate vSwitches isolate management traffic from VM traffic (requirement 2); VLAN-tagged port groups segment VMs by security zone at Layer 2 (requirement 1); disabling forged MAC transmits and promiscuous mode on the vSwitch security policy prevents VMs from crafting frames to spoof other VMs' MAC addresses or sniff all traffic (requirement 3).
    *   *Why B is incorrect:* Moving to a Type 2 hypervisor degrades performance and security compared to Type 1 — this is a regression. Host-based firewalls on VMs don't address the vSwitch-level VLAN segmentation gaps. An external IDS detects attacks after traffic leaves the host but cannot control intra-host vSwitch traffic between VMs.
    *   *Why C is incorrect:* EtherChannel improves uplink bandwidth but doesn't address security zone separation. Assigning all VMs to VLAN 1 eliminates isolation entirely — the opposite of what is needed. BPDU Guard on ESXi uplinks is a physical switch feature, not a VMware configuration, and doesn't address the three identified concerns.
    *   *Why D is incorrect:* Physical firewalls between each VM and the virtual switch is architecturally impractical — all inter-VM traffic within the host never leaves the physical host, so external firewalls cannot intercept it. Static ARP entries mitigate ARP poisoning on specific hosts but do not provide VLAN segmentation or prevent MAC spoofing at scale. SNMP monitoring provides visibility but no access control.
