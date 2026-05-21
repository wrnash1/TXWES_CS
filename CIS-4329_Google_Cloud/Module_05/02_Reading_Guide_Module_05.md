# Reading Guide: Module 05 – Virtual Private Cloud (VPC): Networking Fundamentals
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 05 – Virtual Private Cloud (VPC): Networking Fundamentals**! A VPC network is the foundation of every GCP deployment. This module covers VPC architecture, subnets, firewall rules, routes, VPC peering, and Cloud VPN. The ACE exam tests networking heavily — especially firewall rule behavior, the difference between GCP's global VPCs and AWS-style regional VPCs, and how to connect on-premises networks to GCP.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **VPC Network**: In GCP, a VPC network is a **global** resource — it spans all regions automatically. This is fundamentally different from AWS, where VPCs are regional. However, **subnets are regional**: each subnet is associated with one region and has one primary IPv4 CIDR range.

*   **Firewall Rules**: GCP firewall rules are defined at the VPC network level but enforced at the VM instance level. Rules are **stateful** — if an inbound connection is allowed, the corresponding outbound reply is automatically permitted without a separate rule. Every VPC has an implied deny-all ingress and allow-all egress rule that cannot be deleted.

*   **Network Tags**: String labels applied to VM instances (e.g., `web-server`, `db-backend`). Firewall rules can target VMs by network tag instead of by IP address, making rules more portable and easier to manage as the fleet changes. A VM inherits all firewall rules that reference any of its tags.

*   **Routes**: Every VPC has a default route (`0.0.0.0/0`) pointing to the default internet gateway. Routes can also direct traffic to VPN tunnels, interconnects, or other VPC networks via VPC peering. Custom static routes override the default for specific destination CIDRs.

*   **VPC Peering**: Connects two VPC networks so VMs in each can communicate using internal IP addresses without traversing the public internet. Peering is non-transitive — if VPC A peers with VPC B, and VPC B peers with VPC C, VPC A cannot reach VPC C through VPC B without a direct peering.

*   **Cloud VPN / Cloud Interconnect**: Cloud VPN creates an encrypted IPsec tunnel over the public internet between your on-premises network and a GCP VPC. Cloud Interconnect (Dedicated or Partner) provides a private, high-bandwidth physical connection. Use VPN for lower-bandwidth or cost-sensitive hybrid connectivity; use Interconnect for high-throughput, low-latency requirements.

---

### 2. Certification Exam Tips

*   **GCP VPCs are global, subnets are regional**: This is a top ACE exam trap. When a question says "your VPC spans multiple regions," that is normal GCP behavior — not a special configuration. Subnets define the IP address space within a specific region.

*   **Firewall rules are stateful**: You only need to allow the inbound direction for a service; reply traffic is automatically allowed. The exam may try to trick you into creating both inbound and outbound rules for a simple web server — only the inbound rule is needed.

*   **Least-privilege firewall rule targeting**: Prefer network tags over IP ranges when the set of target VMs changes over time. The exam favors tag-based rules for their operational flexibility.

*   **VPC peering is non-transitive**: If a question describes three VPCs and asks whether VM-A can reach VM-C, check whether A↔C have a direct peering. A peering between A↔B and B↔C does not give A access to C.

*   **Study Resource**: The freeCodeCamp ACE course covers VPC networking, firewall rules, and hybrid connectivity with diagrams: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Supplement with the official VPC overview documentation for precise terminology on routes and peering.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the VPC network overview including subnet behavior, firewall rules, and routes: [VPC Network Overview](https://cloud.google.com/vpc/docs/vpc). Pay attention to the "Firewall rules" and "Routes" sections.
*   **Required Reading**: Review Cloud VPN and how IPsec tunnels connect on-premises networks to GCP: [Cloud VPN Overview](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
*   **Required Video**: Watch the VPC networking segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Networking chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a custom VPC, add subnets, configure firewall rules with network tags, and verify connectivity. Key commands to practice:

*   `gcloud compute networks create my-vpc --subnet-mode=custom` — creates a custom VPC
*   `gcloud compute networks subnets create my-subnet --network=my-vpc --region=us-central1 --range=10.0.0.0/24` — creates a subnet
*   `gcloud compute firewall-rules create allow-http --network=my-vpc --allow=tcp:80 --target-tags=web-server` — creates a tag-based firewall rule
*   `gcloud compute instances add-tags VM_NAME --tags=web-server` — applies a network tag to a VM

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [VPC Network Overview](https://cloud.google.com/vpc/docs/vpc) documentation page.
- [ ] Read the [Cloud VPN Overview](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview) documentation page.
- [ ] Watch the VPC Networking segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a custom VPC, configure subnets and firewall rules with tags.
- [ ] Proceed to the weekly quiz.
