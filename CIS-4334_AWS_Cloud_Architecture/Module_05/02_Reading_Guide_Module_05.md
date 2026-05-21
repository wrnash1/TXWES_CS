# Reading Guide: Module 05 - VPC – Subnets, Route Tables, Security Groups, NACLs
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 05 - VPC – Subnets, Route Tables, Security Groups, and Network ACLs**! Amazon Virtual Private Cloud (VPC) is the networking foundation for virtually every AWS deployment. This module covers how to design isolated virtual networks with public and private subnets, how traffic is routed using route tables and gateways, and how to apply layered network security with Security Groups and Network ACLs. VPC design and troubleshooting questions are among the most common scenario-based questions on the SAA-C03 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **VPC (Virtual Private Cloud)**: A logically isolated virtual network in the AWS cloud that you control. You define the IP address range (CIDR block, e.g., 10.0.0.0/16), create subnets, configure route tables, and attach gateways. Each VPC is confined to a single Region but can span all AZs within that Region. VPCs are the networking boundary for EC2, RDS, Lambda, and most other compute and database services.

*   **Public vs. Private Subnets**: A subnet is a range of IP addresses within a VPC (e.g., 10.0.1.0/24). A public subnet has a route table entry pointing 0.0.0.0/0 (all internet traffic) to an Internet Gateway, enabling resources with public IPs to communicate directly with the internet. A private subnet has no such route; resources in private subnets can only reach the internet via a NAT Gateway (for outbound-only) or not at all. Databases and application servers typically belong in private subnets; load balancers and bastion hosts in public subnets.

*   **Internet Gateway (IGW)**: A horizontally scaled, redundant, and highly available VPC component that allows communication between VPC resources and the public internet. An IGW must be attached to the VPC and referenced in the subnet's route table for resources in that subnet to have internet access. Without an IGW attachment, no subnet in the VPC can reach the internet.

*   **Route Tables**: A set of rules (routes) that determine where network traffic is directed within and out of a VPC. Every subnet is associated with exactly one route table (the main route table by default). A route consists of a destination CIDR and a target (IGW, NAT Gateway, VPC Peering connection, etc.). The most specific matching route (longest prefix) is used.

*   **Security Groups vs. Network ACLs (NACLs)**: Security Groups are stateful instance-level firewalls — return traffic for an allowed inbound connection is automatically allowed outbound without an explicit rule. NACLs are stateless subnet-level firewalls — you must explicitly allow both inbound and outbound traffic, including ephemeral ports for return traffic. Security Groups only allow (no explicit deny); NACLs support both allow and deny rules evaluated in numbered order (lowest number first). NACLs are applied at the subnet boundary; Security Groups are applied to individual ENIs (EC2 instances).

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** VPC is tested in Design Secure Architectures (30%) and Design Resilient Architectures (26%). Network connectivity troubleshooting and HA subnet design questions are very common.

*   **Public Subnet Checklist:** For an EC2 instance in a public subnet to be reachable from the internet, you need ALL of: (1) IGW attached to the VPC, (2) route table with 0.0.0.0/0 → IGW, (3) public IP or Elastic IP assigned to the instance, and (4) Security Group allowing inbound traffic on the required port. Missing any one of these is a common exam trap.

*   **NAT Gateway vs. Internet Gateway:** A NAT Gateway allows private subnet resources to initiate outbound connections to the internet (e.g., to download patches) but does not allow inbound connections from the internet. An IGW supports bidirectional traffic. The exam will test which gateway to use based on whether inbound or outbound-only internet access is required.

*   **Security Group vs. NACL Exam Trap:** Security Groups are stateful (allow return traffic automatically); NACLs are stateless (require explicit inbound AND outbound rules). When a question mentions "blocking a specific IP address," NACLs can deny; Security Groups cannot deny — they only allow. Use NACLs for IP blocking.

*   **VPC Peering:** VPC Peering connects two VPCs with non-overlapping CIDR ranges for private routing between them. It is non-transitive — if VPC A peers with B and B peers with C, A cannot reach C through B. For transitive routing between many VPCs, use AWS Transit Gateway.

*   **Study Resource:** The VPC User Guide covers all subnet, routing, and security configuration: [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/index.html). The "Security in your VPC" chapter is directly exam-relevant.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the VPC chapter in the AWS Solutions Architect study materials and the [Amazon VPC FAQs page](https://aws.amazon.com/vpc/faqs/). Review the [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) for the "AWS Security Best Practices" whitepaper's network security sections.

*   **Required Video:** Watch the VPC module in the official course playlist, focusing on the step-by-step architecture of a multi-tier VPC with public and private subnets, IGW, NAT Gateway, and the layered Security Group / NACL security model: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create a VPC with public and private subnets:** Use the VPC wizard or CLI to create a VPC (10.0.0.0/16) with a public subnet (10.0.1.0/24) and private subnet (10.0.2.0/24) in two AZs, attach an Internet Gateway, and configure route tables appropriately.

*   **Deploy a NAT Gateway for private subnet outbound access:** Create a NAT Gateway in the public subnet, allocate an Elastic IP, and update the private subnet route table to add 0.0.0.0/0 → NAT Gateway. Test outbound internet connectivity from a private EC2 instance.

*   **Configure Security Group and NACL rules:** Create a Security Group allowing HTTP (port 80) inbound from 0.0.0.0/0 for a web server. Create a NACL rule explicitly denying a specific test IP address range. Verify that the NACL deny overrides the Security Group allow for the denied source IP.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Review VPC networking concepts at [https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
- [ ] Review Security Groups vs. NACLs comparison at [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html).
- [ ] Watch the VPC video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab building a multi-tier VPC with public/private subnets, IGW, NAT Gateway, Security Groups, and NACLs.
- [ ] Proceed to the weekly quiz.
