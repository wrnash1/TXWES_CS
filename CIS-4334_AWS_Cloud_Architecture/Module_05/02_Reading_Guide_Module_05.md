# Reading Guide: Module 05 - VPC: Subnets, Route Tables, Security Groups, NACLs

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Introduction

VPC is the foundational networking service for AWS. Every resource you deploy in AWS runs inside a VPC or connects to one. The SAA-C03 exam tests VPC architecture at multiple levels: CIDR design, routing, firewall configuration, and connectivity. This reading guide provides the complete reference tables, CIDR planning methodology, security control comparisons, and connectivity decision frameworks needed for exam scenario questions.

---

## Section 1: VPC and Subnet Design

### 1.1 VPC CIDR Planning

VPC CIDR blocks must follow these constraints:

- Size range: /16 (65,536 IP addresses) to /28 (16 IP addresses)
- RFC 1918 private ranges recommended: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- CIDR blocks cannot be modified after VPC creation (you can add secondary CIDR blocks but not change the primary)
- Peered VPCs cannot have overlapping CIDR blocks
- On-premises networks connected via VPN or Direct Connect must not overlap with VPC CIDRs

AWS reserves 5 IP addresses per subnet:

- .0 — Network address
- .1 — VPC router
- .2 — Amazon DNS server
- .3 — Reserved for future use
- .255 — Broadcast address (not used by AWS, but reserved)

For a /24 subnet (256 total), 251 IP addresses are usable by resources.

### 1.2 Three-Tier Architecture CIDR Plan

A production-ready three-tier VPC CIDR layout for a deployment across two AZs:

```text
VPC CIDR: 10.0.0.0/16  (65,536 IPs)

Tier 1 — Public (ALB, NAT Gateway, bastion host):
  10.0.1.0/24   (251 usable) — us-east-1a
  10.0.2.0/24   (251 usable) — us-east-1b
  10.0.3.0/24   (251 usable) — us-east-1c (if three AZs)

Tier 2 — Private (EC2 application tier):
  10.0.11.0/24  (251 usable) — us-east-1a
  10.0.12.0/24  (251 usable) — us-east-1b
  10.0.13.0/24  (251 usable) — us-east-1c

Tier 3 — Isolated (RDS, ElastiCache):
  10.0.21.0/24  (251 usable) — us-east-1a
  10.0.22.0/24  (251 usable) — us-east-1b
  10.0.23.0/24  (251 usable) — us-east-1c

Reserved for future use: 10.0.100.0/22 through 10.0.255.0/24
```

Gap numbering (1, 11, 21) makes it visually obvious which tier a subnet belongs to and leaves room for expansion within each tier range.

### 1.3 Public vs. Private vs. Isolated Subnets

| Subnet Type | Route to Internet | Has Public IPs | Resources | Example |
|---|---|---|---|---|
| Public | Route to Internet Gateway | Yes | ALB, NAT GW, Bastion | 10.0.1.0/24 |
| Private | Route to NAT Gateway (outbound only) | No | EC2 app servers, ECS tasks | 10.0.11.0/24 |
| Isolated | No internet route | No | RDS, ElastiCache, internal services | 10.0.21.0/24 |

The subnet type is determined entirely by the route table attached to it — not by any flag on the subnet itself. A subnet becomes public by having a route to an Internet Gateway. Remove that route and it becomes private.

---

## Section 2: Internet Gateway and NAT Gateway

### 2.1 Internet Gateway

- One per VPC; horizontally scaled and highly available by design
- No charge for the gateway; charges apply for data transfer out
- Required for: resources with public IPs receiving inbound connections, and as the exit point for NAT Gateway outbound traffic
- To make a subnet public: attach Internet Gateway to VPC, add route `0.0.0.0/0` -> IGW to subnet route table, assign public IP to resource

### 2.2 NAT Gateway

- Deployed per AZ in a public subnet
- Has one Elastic IP address
- Allows outbound internet connections from private subnet resources
- Does not allow unsolicited inbound connections from the internet
- Managed service — AWS patches and maintains; no management overhead
- Charges: hourly usage fee + per-GB data processing fee
- High availability: deploy one NAT GW per AZ; configure each AZ's private subnets to use their local NAT GW

Route table configuration for private subnets using NAT Gateway:

| Destination | Target |
|---|---|
| 10.0.0.0/16 | local |
| 0.0.0.0/0 | nat-xxxxxxxxxxxxxxxxx (NAT Gateway in same AZ) |

### 2.3 Egress-Only Internet Gateway

For IPv6, the equivalent of a NAT Gateway is an Egress-Only Internet Gateway. IPv6 addresses are always public, so the Egress-Only IGW allows outbound IPv6 connections from private resources without allowing inbound connections. There is no IPv6 equivalent of NAT (address translation is not used with IPv6).

---

## Section 3: Security Groups vs. Network ACLs

### 3.1 Feature Comparison

| Feature | Security Group | Network ACL |
|---|---|---|
| Operates at | ENI (instance) level | Subnet level |
| State | Stateful — return traffic auto-allowed | Stateless — must explicitly allow return traffic |
| Rule types | Allow only | Allow and Deny |
| Rule evaluation | All rules evaluated simultaneously | Rules evaluated in numeric order; first match applies |
| Applies to | Individual instances/ENIs | All traffic entering/leaving a subnet |
| Default (new SG) | Deny all inbound, allow all outbound | N/A |
| Default NACL | N/A | Allow all inbound and outbound |
| Best for | Granular instance-level control | Broad subnet-level blocking; explicit deny rules |

### 3.2 Security Group Rule Design

Security groups use the principle of implicit deny — everything not explicitly allowed is denied. Rules must be explicitly written for desired traffic.

A typical three-tier security group design:

**SG-ALB (public ALB):**

- Inbound: TCP 443 from 0.0.0.0/0 (HTTPS from internet)
- Inbound: TCP 80 from 0.0.0.0/0 (HTTP redirect)
- Outbound: TCP 80 to SG-WebServer (to web tier)

**SG-WebServer (EC2 web tier):**

- Inbound: TCP 80 from SG-ALB (only from ALB)
- Outbound: TCP 8080 to SG-AppServer (to app tier)

**SG-AppServer (EC2 app tier):**

- Inbound: TCP 8080 from SG-WebServer (only from web tier)
- Outbound: TCP 5432 to SG-Database (to database)

**SG-Database (RDS):**

- Inbound: TCP 5432 from SG-AppServer (only from app tier)
- Outbound: none needed (stateful — response traffic auto-allowed)

This design enforces strict east-west traffic control using security group references rather than IP CIDR ranges. It is more resilient to IP changes than CIDR-based rules.

### 3.3 Network ACL Rule Design

NACLs require both inbound and outbound rules because they are stateless.

Example NACL for a public subnet:

| Rule | Type | Protocol | Port | Source | Action |
|---|---|---|---|---|---|
| 100 | Inbound | TCP | 443 | 0.0.0.0/0 | Allow |
| 110 | Inbound | TCP | 80 | 0.0.0.0/0 | Allow |
| 120 | Inbound | TCP | 1024-65535 | 0.0.0.0/0 | Allow (ephemeral ports for return traffic) |
| 90 | Inbound | All | All | 203.0.113.0/24 | Deny (specific bad actor CIDR) |
| * | Inbound | All | All | 0.0.0.0/0 | Deny (default) |
| 100 | Outbound | TCP | 443 | 0.0.0.0/0 | Allow |
| 110 | Outbound | TCP | 1024-65535 | 0.0.0.0/0 | Allow (ephemeral response ports) |
| * | Outbound | All | All | 0.0.0.0/0 | Deny (default) |

The deny rule for 203.0.113.0/24 at rule number 90 (lower than the allow rules) ensures that traffic from that CIDR is blocked before the allow rules are reached.

---

## Section 4: VPC Connectivity Options

### 4.1 Connectivity Option Comparison

| Option | Use Case | Transitive | Cost | Bandwidth |
|---|---|---|---|---|
| VPC Peering | Connect 2 VPCs privately | No | Low (data transfer) | Up to 25 Gbps |
| Transit Gateway | Hub-and-spoke for many VPCs | Yes | Hourly + data processing | Up to 50 Gbps per attachment |
| Site-to-Site VPN | On-premises to VPC over internet | N/A | Per hour + data | Up to 1.25 Gbps |
| Direct Connect | On-premises to VPC over private circuit | N/A | Port hours + data | 1-100 Gbps |
| Gateway VPC Endpoint | S3 and DynamoDB access | N/A | Free | Not applicable |
| Interface VPC Endpoint | Other AWS services via PrivateLink | N/A | Hourly + data | Not applicable |

### 4.2 VPC Peering Constraints

- Cannot use overlapping CIDR blocks
- Non-transitive: if A peers with B and B peers with C, A cannot reach C through B
- Inter-region peering is supported but incurs inter-region data transfer costs
- No transitive routing through a peered VPC's Internet Gateway, NAT Gateway, or VPN
- Maximum 125 peering connections per VPC (default limit, can be increased)

When you have more than 3-4 VPCs or need transitive routing, migrate to Transit Gateway.

### 4.3 Transit Gateway

Transit Gateway acts as a hub router. Key capabilities:

- Each VPC, VPN, and Direct Connect attaches to TGW
- Route tables on TGW control which attachments can communicate
- Supports route propagation from VPN and Direct Connect
- Supports multicast
- Can be shared across accounts via AWS Resource Access Manager
- Supports multiple route tables for network segmentation (e.g., prod VPCs cannot route to dev VPCs)

### 4.4 VPN vs. Direct Connect Decision

| Factor | Site-to-Site VPN | Direct Connect |
|---|---|---|
| Setup time | Minutes to hours | Weeks to months |
| Connection type | Encrypted over public internet | Dedicated private circuit |
| Reliability | Internet-dependent; variable latency | Consistent, dedicated bandwidth |
| Cost | Low (hourly + data) | High (port + cross-connect + data) |
| Bandwidth | Up to 1.25 Gbps per tunnel | 1 Gbps or 10 Gbps ports |
| Best for | Quick setup, budget-constrained, lower throughput | High throughput, consistent latency, compliance |

For the exam: if the scenario mentions consistent latency, dedicated bandwidth, or large data migration with a predictable throughput requirement, Direct Connect is correct. If the scenario mentions quick setup, backup connectivity, or lower cost, VPN is correct.

---

## Section 5: VPC Flow Logs

VPC Flow Logs capture IP traffic metadata at the VPC, subnet, or ENI level. Flow log records include:

- Source and destination IP address and port
- Protocol
- Packets and bytes transferred
- Action: ACCEPT or REJECT
- Log status: OK, NODATA, SKIPDATA

Flow logs are published to CloudWatch Logs or S3. They do not capture real-time traffic — there is typically a 5-15 minute delay. They do not capture DNS queries (use Route 53 DNS query logs for that), or traffic to/from the instance metadata service (169.254.169.254), or DHCP traffic.

Use VPC Flow Logs for:

- Diagnosing over-permissive or under-permissive security groups
- Forensic analysis after a security incident
- Monitoring for unusual traffic patterns
- Compliance requirements to log all network activity

---

## Section 6: SAA-C03 Exam Tips for Module 05

**Exam Tip 1 — Public subnet definition:**
A subnet is public only if its route table has a `0.0.0.0/0` route pointing to an Internet Gateway AND resources have public IP addresses. Both conditions must be met. Adding a public IP without the route (or a route without a public IP) does not make the resource reachable from the internet.

**Exam Tip 2 — NAT Gateway per AZ for high availability:**
A single NAT Gateway in one AZ is a single point of failure for private subnet outbound traffic. For high availability, deploy one NAT Gateway per AZ and configure each AZ's private subnets to route through their local NAT Gateway.

**Exam Tip 3 — Security groups cannot explicitly deny:**
Security groups only support Allow rules. If you need to block a specific IP address or CIDR, use a Network ACL Deny rule. The exam frequently asks this — the answer is always NACL for explicit deny.

**Exam Tip 4 — NACL is stateless:**
When configuring a NACL, you must allow both the inbound request and the outbound response (ephemeral ports 1024-65535). Forgetting outbound ephemeral port rules is the most common NACL misconfiguration trap on the exam.

**Exam Tip 5 — VPC peering is non-transitive:**
VPC A can peer with VPC B. VPC B can peer with VPC C. But VPC A cannot reach VPC C through VPC B — you need a direct A-to-C peering connection. If a scenario has many VPCs that all need to communicate, Transit Gateway is the scalable solution.

**Exam Tip 6 — VPC endpoint types:**
Gateway VPC Endpoints (free) support only S3 and DynamoDB. Interface VPC Endpoints (have an hourly cost) support most other AWS services. Know the distinction and know that Gateway endpoints use route table entries while Interface endpoints use private IP addresses in your subnet.

**Exam Tip 7 — CIDR overlap prevents peering:**
Overlapping CIDR blocks prevent VPC peering and cause routing ambiguity with VPN/Direct Connect. Always plan CIDR blocks to avoid overlap across all connected networks including on-premises.

**Exam Tip 8 — Flow Logs diagnose connectivity issues:**
If a scenario asks how to determine why traffic to an EC2 instance is being rejected or why a security group rule is not working as expected, VPC Flow Logs is the diagnostic tool.

---

## Section 7: Key CLI Commands for Module 05

Describe VPCs in your account:

```bash
aws ec2 describe-vpcs \
  --query "Vpcs[*].{ID:VpcId,CIDR:CidrBlock,Default:IsDefault}" \
  --output table
```

Describe subnets in a VPC:

```bash
aws ec2 describe-subnets \
  --filters Name=vpc-id,Values=vpc-xxxxxxxxxxxxxxxxx \
  --query "Subnets[*].{ID:SubnetId,CIDR:CidrBlock,AZ:AvailabilityZone,Public:MapPublicIpOnLaunch}" \
  --output table
```

Describe route tables for a VPC:

```bash
aws ec2 describe-route-tables \
  --filters Name=vpc-id,Values=vpc-xxxxxxxxxxxxxxxxx \
  --output json
```

Describe security groups:

```bash
aws ec2 describe-security-groups \
  --filters Name=vpc-id,Values=vpc-xxxxxxxxxxxxxxxxx \
  --output table
```

Describe Network ACLs:

```bash
aws ec2 describe-network-acls \
  --filters Name=vpc-id,Values=vpc-xxxxxxxxxxxxxxxxx \
  --output json
```

---

## Section 8: Study Checklist

- [ ] Design a /16 VPC CIDR layout with three tiers and two AZs from scratch without referencing notes
- [ ] Explain the five IP addresses reserved per subnet and why they are reserved
- [ ] Draw the routing required to make a subnet public (what routes must exist in the route table?)
- [ ] Explain NAT Gateway high-availability architecture (how many NAT Gateways, where, and why?)
- [ ] Compare Security Groups and Network ACLs on all five features in the Section 3 table without looking
- [ ] Write out the NACL rules needed to allow HTTPS inbound and its return traffic outbound
- [ ] Explain why VPC peering is non-transitive and when Transit Gateway is the better solution
- [ ] Distinguish between a Gateway VPC Endpoint and an Interface VPC Endpoint
- [ ] Describe what VPC Flow Logs capture and what they do NOT capture
- [ ] Run the CLI commands in Section 7 and record the output
- [ ] Complete the Module 05 quiz with a score of at least 80 percent
- [ ] Post your initial response in the Module 05 discussion forum by the Wednesday deadline

---

## References

All certification study materials and exam registration: <aws.amazon.com/certification>
