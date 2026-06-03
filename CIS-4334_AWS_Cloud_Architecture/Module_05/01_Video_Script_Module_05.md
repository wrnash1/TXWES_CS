# Video Script: Module 05 - VPC: Subnets, Route Tables, Security Groups, NACLs

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome back. I am Professor Nash and this is Module 05: VPC — Subnets, Route Tables, Security Groups, and Network ACLs.

The Virtual Private Cloud is your private network in AWS. Everything you run in AWS lives inside a VPC or connects to one. Understanding VPC architecture is foundational to the SAA-C03 exam — network design questions appear in every domain because security, performance, and resilience all depend on how your network is structured.

By the end of this module you will be able to:

- Design a VPC with correct CIDR block allocation for a three-tier architecture
- Configure public and private subnets with the correct routing
- Explain the difference between Security Groups and Network ACLs and apply each correctly
- Configure an Internet Gateway, NAT Gateway, and route tables
- Design VPC peering and VPC Endpoints for connectivity
- Identify when to use Transit Gateway for multi-VPC networking

---

## [01:30 - 06:30] VPC Fundamentals and CIDR Planning

[SHOW DIAGRAM]

A VPC is a logically isolated section of the AWS cloud where you launch your resources. When you create a VPC, you define a CIDR block — a range of IP addresses that all resources in the VPC will use. CIDR stands for Classless Inter-Domain Routing. A CIDR block like `10.0.0.0/16` means the first 16 bits are fixed (the network address) and the remaining 16 bits are available for hosts — giving you 65,536 IP addresses.

VPC CIDR ranges must be between /16 (65,536 addresses) and /28 (16 addresses). For production use, /16 gives you the most flexibility to create subnets. RFC 1918 private ranges are recommended: `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`. Avoid using CIDR ranges that overlap with your on-premises network or other VPCs you need to peer with — overlapping CIDRs prevent peering.

Now let me show you how to plan a three-tier architecture CIDR layout. Suppose your VPC is `10.0.0.0/16`. You need three tiers — public (web), private (application), and isolated (database) — across two Availability Zones. You divide the /16 into /24 subnets (256 addresses each, but AWS reserves 5 per subnet so 251 usable).

[SHOW DIAGRAM]

```text
VPC: 10.0.0.0/16

Public subnets (ALB, NAT Gateway, bastion):
  10.0.1.0/24  — AZ us-east-1a
  10.0.2.0/24  — AZ us-east-1b

Private subnets (EC2 application tier):
  10.0.11.0/24 — AZ us-east-1a
  10.0.12.0/24 — AZ us-east-1b

Isolated subnets (RDS database tier):
  10.0.21.0/24 — AZ us-east-1a
  10.0.22.0/24 — AZ us-east-1b
```

Why this layout? Separating subnet ranges by function makes security group rules, route table configuration, and firewall rules much cleaner. Putting databases in subnets with no route to the internet adds a network-level barrier beyond security groups.

AWS reserves five IP addresses in every subnet: the network address, the VPC router address, the DNS resolver address, a future use address, and the broadcast address. For a /24 subnet (256 total), you have 251 usable addresses.

---

## [06:30 - 11:00] Internet Gateway, NAT Gateway, and Route Tables

[SHOW DIAGRAM]

For resources to communicate with the internet, three things must be in place: an Internet Gateway, a route table entry pointing to it, and a public IP address (Elastic IP or auto-assigned public IP) on the resource.

An **Internet Gateway** is a horizontally scaled, redundant, highly available VPC component that allows communication between your VPC and the internet. You attach one Internet Gateway per VPC. There is no charge for the gateway itself — you pay for data transfer.

A subnet is "public" if its route table has a route sending `0.0.0.0/0` (all internet traffic) to the Internet Gateway. Resources in a public subnet with public IP addresses can receive inbound connections from the internet.

A subnet is "private" if its route table has no route to an Internet Gateway. Resources in private subnets cannot receive inbound connections from the internet — but they also cannot make outbound connections by default.

**NAT Gateway** allows resources in private subnets to make outbound connections to the internet (for software updates, API calls to third-party services) while preventing inbound connections initiated from the internet. You place the NAT Gateway in a public subnet. The private subnet's route table points `0.0.0.0/0` to the NAT Gateway. The NAT Gateway has an Elastic IP address it uses for outbound connections.

[SHOW DIAGRAM]

Outbound flow from a private EC2 instance:

```text
EC2 in private subnet
  -> NAT Gateway (in public subnet)
  -> Internet Gateway
  -> Internet
```

Important exam points about NAT Gateway:

- NAT Gateway is deployed per AZ — for high availability, deploy one NAT Gateway per AZ and configure each AZ's private subnets to use that AZ's NAT Gateway
- NAT Gateway is managed by AWS — no patching or management required
- Charges apply per hour and per GB of data processed

Route table design:

- Public subnet route table: local route (VPC CIDR → local) plus `0.0.0.0/0` → Internet Gateway
- Private subnet route table: local route plus `0.0.0.0/0` → NAT Gateway
- Isolated/database subnet route table: local route only — no internet route

---

## [11:00 - 16:00] Security Groups and Network ACLs

[SHOW DIAGRAM]

Security Groups and Network ACLs are both firewall mechanisms in VPC, but they work differently and at different levels. Understanding the distinction is one of the most tested VPC concepts on the SAA-C03 exam.

**Security Groups** operate at the instance (ENI) level. They are stateful — if you allow an inbound connection, the response traffic is automatically allowed outbound regardless of outbound rules. You only write rules for the traffic you want to allow. Security groups use only allow rules — there is no explicit deny capability.

Security group rules reference:

- Protocol (TCP, UDP, ICMP)
- Port range
- Source or destination (CIDR, another security group, or prefix list)

The ability to reference another security group as a source is very powerful. If you have a web tier security group and an app tier security group, you can configure the app tier to allow inbound TCP on port 8080 only from the web tier security group. This means only resources with the web tier security group attached can reach the app tier on that port — regardless of IP address.

**Network ACLs** operate at the subnet level. They are stateless — inbound and outbound rules are evaluated independently. If you allow inbound TCP on port 443, you must also allow outbound TCP on the ephemeral port range (1024-65535) for the response traffic to return. NACLs support both allow and deny rules evaluated in numeric order — the lowest numbered rule that matches is applied. Rule numbers typically increment by 10 or 100.

[SHOW DIAGRAM]

Security Group vs. Network ACL comparison:

| Feature | Security Group | Network ACL |
|---|---|---|
| Level | Instance (ENI) | Subnet |
| Stateful | Yes | No |
| Rule types | Allow only | Allow and Deny |
| Rule evaluation | All rules evaluated, most permissive wins | Rules evaluated in order by number |
| Default behavior | Deny all inbound, allow all outbound | Allow all inbound and outbound |
| Use case | Primary instance-level firewall | Additional subnet-level layer; explicit denials |

The exam frequently asks: if you want to block a specific IP address from reaching your web servers, should you use a security group or a NACL? The answer is NACL — security groups cannot create explicit deny rules. If you want to block IP address 203.0.113.5 from reaching your entire subnet, add a NACL deny rule with a low rule number before the allow rules.

---

## [16:00 - 19:30] VPC Connectivity Options

[SHOW DIAGRAM]

Beyond basic internet connectivity, VPCs have several connectivity options you must know for the exam.

**VPC Peering** allows two VPCs to communicate using private IP addresses as if they were in the same network. Peering can be within the same account, across accounts, or across Regions (inter-region peering). Key limitations: peering is non-transitive — if VPC A peers with VPC B and VPC B peers with VPC C, VPC A cannot communicate with VPC C through VPC B. Each pair requires a direct peering connection. Also, CIDR blocks of peered VPCs cannot overlap.

**Transit Gateway** solves the scaling problem with VPC peering. Instead of a mesh of peer connections between N VPCs (requiring N(N-1)/2 connections), each VPC attaches to a single Transit Gateway hub. The TGW routes traffic between all attached VPCs and can also connect to VPNs and Direct Connect. Transit Gateway supports transitive routing — VPC A can reach VPC C through the TGW without a direct connection. For the exam: if you see more than three or four VPCs that all need to communicate with each other, or if you need transitive routing, Transit Gateway is the answer.

**VPC Endpoints** allow resources in your VPC to access AWS services privately without using the internet:

- Gateway Endpoints: for S3 and DynamoDB. Free. Configured in the route table.
- Interface Endpoints (AWS PrivateLink): for most other AWS services (SSM, CloudWatch, SQS, SNS, etc.). Uses Elastic Network Interface with private IP. Has an hourly charge.

**AWS Site-to-Site VPN** connects your on-premises network to a VPC over an encrypted IPsec tunnel over the public internet. Easy to set up, lower cost, but limited bandwidth and subject to internet latency and reliability.

**AWS Direct Connect** is a dedicated private network connection between your on-premises data center and AWS. Bypasses the public internet entirely. Provides consistent, dedicated bandwidth and lower latency than VPN. Higher cost and longer setup time (weeks to months for physical circuit provisioning).

---

## [19:30 - 22:00] Bastion Hosts and VPC Flow Logs

**Bastion Host (Jump Server)** is an EC2 instance in a public subnet that provides a secure entry point for administrators to SSH or RDP into instances in private subnets. Instead of exposing all private EC2 instances with public IPs, you expose only the bastion host. Security group rules: bastion host allows SSH from specific admin IP ranges; private instances allow SSH only from the bastion host security group. For the exam: the modern alternative to a bastion host is AWS Systems Manager Session Manager, which provides shell access without SSH, without a public IP, and without a bastion host entirely.

**VPC Flow Logs** capture information about IP traffic flowing through your VPC network interfaces. Flow logs can be published to CloudWatch Logs or S3. They record source and destination IP, protocol, port, action (ACCEPT or REJECT), and packet/byte counts. Flow logs are essential for security analysis, troubleshooting connectivity issues, and compliance auditing. They are not real-time — there is a delay of several minutes. For the exam: if a scenario asks how to diagnose whether a security group is rejecting traffic, VPC Flow Logs is the answer.

---

## [22:00 - 24:00] Module Summary

VPC CIDR planning: use /16 for production VPCs; allocate /24 subnets by tier and AZ; avoid overlapping with on-premises ranges.

Public vs. private subnets: public subnets have a route to Internet Gateway; private subnets use NAT Gateway for outbound internet access; isolated subnets have no internet route.

Security Groups are stateful, instance-level, allow-only. NACLs are stateless, subnet-level, support allow and deny with ordered rules.

VPC connectivity: peering for small numbers of VPCs (non-transitive); Transit Gateway for hub-and-spoke multi-VPC; VPN for encrypted internet-based on-premises connectivity; Direct Connect for dedicated private on-premises connectivity.

In the lab this week you will design a complete VPC CIDR block layout for a three-tier architecture. In the Reading Guide you have complete subnet planning tables, security group vs. NACL reference, and connectivity option comparisons.

For your certification study: <aws.amazon.com/certification>

---

End of Module 05 Video Script
