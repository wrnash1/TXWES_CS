# Video Script: Module 10 — AWS Networking and VPC Design

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

---

### SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4334. I'm Professor Nash. Today we cover AWS networking and VPC design — the module that ties every other AWS service together. Without a properly designed VPC, nothing in AWS is secure or properly isolated.

This module is one of the most architecture-intensive topics on the SAA-C03 exam. You will see multi-diagram scenario questions that ask you to trace traffic flows, identify routing gaps, and design connectivity between VPCs and on-premises networks.

By the end of this module you will be able to design a multi-tier VPC with public and private subnets, explain Internet Gateway versus NAT Gateway routing, choose between VPC Peering, Transit Gateway, and PrivateLink for different connectivity requirements, configure Route 53 routing policies for failover, latency, and weighted distribution, and understand the security layers — security groups and NACLs — that protect resources within a VPC.

Let's start at the foundation — the VPC itself.

---

### SEGMENT 2 — VPC Architecture (1:30–5:30)

[SHOW DIAGRAM: A VPC with CIDR 10.0.0.0/16 spanning all AZs in a region. Inside the VPC: two public subnets (10.0.1.0/24 in AZ-A, 10.0.2.0/24 in AZ-B) and two private subnets (10.0.3.0/24 in AZ-A, 10.0.4.0/24 in AZ-B). Internet Gateway attached to VPC. NAT Gateway in public subnet AZ-A. Route tables shown for public and private subnets with arrows to IGW and NAT GW respectively.]

A Virtual Private Cloud — VPC — is a logically isolated section of the AWS cloud where you define your own virtual network. You control the IP address range, subnets, route tables, and network gateways. Every VPC is region-scoped — it spans all Availability Zones in that region.

You define the IP address range for a VPC using a CIDR block. AWS allows VPC CIDR sizes from /16 (65,536 IPs) to /28 (16 IPs). The standard enterprise practice is to use a /16 for the VPC and then subdivide it into /24 subnets, providing 256 IPs per subnet (minus 5 reserved by AWS). Choose a CIDR range from the RFC 1918 private address space: 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16.

**Public subnets** are subnets with a route to an Internet Gateway in their route table. Resources in public subnets can receive inbound connections from the internet and send outbound traffic to the internet. Load balancers, NAT Gateways, and bastion hosts are placed in public subnets.

**Private subnets** have no route to the Internet Gateway. Resources in private subnets cannot be reached directly from the internet. Application servers, databases, and caches are placed in private subnets. Private subnet resources can still reach the internet through a NAT Gateway for outbound-only connectivity — software updates, API calls to external services.

The standard multi-tier VPC architecture across 3 AZs has 9 subnets: 3 public (one per AZ for load balancers and NAT Gateways), 3 private application tier (one per AZ for EC2 Auto Scaling), and 3 private data tier (one per AZ for RDS and ElastiCache). Each AZ can independently serve traffic if the others fail.

---

### SEGMENT 3 — Internet Gateway and NAT Gateway (5:30–8:30)

[SHOW DIAGRAM: Traffic flow comparison — Left: public subnet instance with IGW. Arrow shows bidirectional traffic between instance and internet via IGW. Right: private subnet instance with NAT Gateway in public subnet. Arrow shows instance → NAT GW → IGW → internet (one direction only, with annotation "Internet cannot initiate inbound connections to private instance")]

**Internet Gateway (IGW)** is a horizontally scaled, redundant, highly available VPC component that enables bidirectional communication between the VPC and the internet. Attaching an IGW to a VPC and adding `0.0.0.0/0 → IGW` to a subnet's route table makes that subnet public. The IGW performs Network Address Translation between public IP addresses and private IP addresses for instances with assigned public IPs or Elastic IPs.

**NAT Gateway** enables instances in private subnets to initiate outbound connections to the internet while preventing the internet from initiating inbound connections to those instances. The NAT Gateway is placed in a public subnet and has an Elastic IP address. The private subnet's route table sends `0.0.0.0/0` to the NAT Gateway, which translates the source IP and forwards the request to the IGW.

AWS manages NAT Gateways — they are fully managed, scale automatically up to 45 Gbps, and are highly available within a single AZ. Because a NAT Gateway is in one AZ, best practice is to deploy one NAT Gateway per AZ. If you have private subnets in us-east-1a, us-east-1b, and us-east-1c, deploy three NAT Gateways (one per AZ) and configure each AZ's private subnet to route to the local NAT Gateway. This prevents cross-AZ traffic charges and ensures AZ independence.

On the exam: instances in a public subnet can receive inbound traffic from the internet. Instances in a private subnet with a NAT Gateway can initiate outbound traffic but cannot receive inbound connections from the internet. NAT Gateways are AZ-specific.

---

### SEGMENT 4 — VPC Peering and Transit Gateway (8:30–12:00)

[SHOW DIAGRAM: Left side — Three VPCs each connected to each other with double-headed arrows labeled "VPC Peering." Labels show "3 VPCs = 3 peering connections." Text annotation: "10 VPCs = 45 peering connections." Right side — Six VPCs all connected to a central Transit Gateway hub with single arrows. Label: "Transit Gateway = hub-and-spoke, 1 attachment per VPC."]

When you need to connect multiple VPCs, you have two primary options.

**VPC Peering** establishes a private, direct network connection between two VPCs. Traffic between peered VPCs uses the AWS private network and never traverses the public internet. VPC Peering can connect VPCs in the same account, different accounts, or different regions (inter-region VPC Peering).

The critical limitation of VPC Peering is that it is non-transitive. If VPC-A is peered with VPC-B, and VPC-B is peered with VPC-C, VPC-A cannot communicate with VPC-C through VPC-B. You must establish a direct peering connection between VPC-A and VPC-C. This limitation makes VPC Peering impractical at scale — connecting 10 VPCs in a full mesh requires 45 peering connections.

**Transit Gateway (TGW)** solves the scalability problem. Transit Gateway is a regional network hub that acts as a central router for all VPCs and on-premises networks. Each VPC attaches to the TGW once, and routing between all attached networks is managed by TGW route tables. Adding a new VPC requires only one TGW attachment.

Transit Gateway supports thousands of VPC attachments, cross-account sharing via AWS Resource Access Manager, inter-region peering between Transit Gateways, and integration with AWS VPN and AWS Direct Connect for on-premises connectivity. TGW is the correct answer for any scenario involving multiple VPCs that all need to communicate — it is the enterprise hub-and-spoke networking model for AWS.

On the exam: if you see 3 or fewer VPCs that need to communicate → VPC Peering may work. If you see 4 or more VPCs, or a hub that all VPCs need to reach (like a shared services VPC with DNS, monitoring, or security scanning) → Transit Gateway.

---

### SEGMENT 5 — PrivateLink and VPC Endpoints (12:00–14:30)

[SHOW DIAGRAM: Consumer VPC and Provider VPC. Without PrivateLink: traffic path goes Consumer EC2 → IGW → Internet → IGW → Provider ALB (passes through public internet). With PrivateLink: traffic path shows Consumer EC2 → Interface VPC Endpoint (ENI in consumer VPC) → PrivateLink → Provider NLB (stays entirely within AWS network, never touching internet).]

**AWS PrivateLink** enables you to privately access AWS services or services hosted by other AWS customers without sending traffic over the public internet. PrivateLink creates an Interface VPC Endpoint — an Elastic Network Interface in your VPC — that routes traffic to the target service through the AWS private network.

VPC Endpoints come in two types. **Interface Endpoints** (powered by PrivateLink) create ENIs in your subnets and provide private connectivity to AWS services like S3, DynamoDB, SQS, SNS, and hundreds of other services, as well as marketplace and partner services. Interface endpoints have an hourly cost and a per-GB data processing charge.

**Gateway Endpoints** are specifically for S3 and DynamoDB. A Gateway Endpoint adds an entry to your route table that routes traffic destined for the service through the endpoint instead of the internet. Gateway endpoints have no additional cost — they are free. If you need to access S3 or DynamoDB from a private subnet without going through a NAT Gateway, use a Gateway Endpoint. This eliminates NAT Gateway data processing charges and internet traffic for S3 and DynamoDB access.

On the exam: private access to S3 from a private EC2 instance without NAT Gateway → S3 Gateway Endpoint. Private access to other AWS services (SQS, Secrets Manager, SSM) from a private subnet → Interface VPC Endpoint.

---

### SEGMENT 6 — Route 53 Routing Policies (14:30–18:00)

[SHOW DIAGRAM: Route 53 logo at center with six routing policy types branching out as labeled boxes: Simple, Weighted, Latency-Based, Failover, Geolocation, Geoproximity. Each box has a one-line description.]

Amazon Route 53 is AWS's DNS service. Beyond basic DNS resolution, Route 53 supports advanced routing policies that control how traffic is distributed across resources. The SAA-C03 exam tests routing policy selection heavily.

**Simple Routing** is the default. A single DNS record points to one or more resources. If multiple values are returned, the client selects one randomly. No health checks or intelligent routing. Use for basic single-region deployments.

**Weighted Routing** distributes traffic across multiple resources based on assigned weights. If you have two endpoints with weights of 80 and 20, Route 53 sends 80% of traffic to the first and 20% to the second. Use this for gradual blue-green deployments (shift traffic from the old version to the new one incrementally) and A/B testing.

**Latency-Based Routing** routes traffic to the AWS Region with the lowest network latency for the requesting user. Route 53 measures latency from the user's location to each configured region and returns the DNS record for the region with the lowest measured latency. Use this for global applications serving users in multiple regions.

**Failover Routing** routes traffic to a primary resource and automatically fails over to a secondary resource if the primary becomes unhealthy. Route 53 uses health checks to monitor the primary resource. When the health check fails, Route 53 automatically begins returning the secondary resource's address. The combination of active-passive failover.

**Geolocation Routing** routes traffic based on the geographic location of the user — specifically the country or continent of origin. Use this for content localization (returning different content based on country), legal compliance (blocking traffic from specific countries), or regional differentiation.

**Geoproximity Routing** routes traffic based on geographic proximity to resources, with an optional bias that expands or shrinks the geographic area that routes to each resource. Use this when you want to route users to the geographically closest resource but need fine-tuned control over the routing boundaries.

On the exam: "Blue-green deployment, shift traffic gradually" → Weighted. "Route to lowest latency region" → Latency-Based. "Active-passive DR, automatic failover" → Failover. "Route based on country of origin" → Geolocation.

---

### SEGMENT 7 — Security Groups and NACLs (18:00–20:30)

[SHOW DIAGRAM: VPC with a security group boundary around an EC2 instance (labeled "Stateful — return traffic automatic") and a NACL boundary around the subnet (labeled "Stateless — must explicitly allow both inbound and outbound"). Arrows show inbound request and return traffic with annotation for each layer.]

Every VPC has two network security layers: Security Groups and Network Access Control Lists (NACLs).

**Security Groups** operate at the instance level (attached to an ENI). They are stateful — when you allow inbound traffic on a port, the return traffic is automatically allowed regardless of outbound rules. Security groups support allow rules only; there are no deny rules. All traffic is implicitly denied by default unless an allow rule exists. Changes to security group rules take effect immediately.

**Network ACLs** operate at the subnet level and are stateless — you must explicitly allow both inbound and outbound traffic for any given communication. NACLs support both allow and deny rules and evaluate rules in numbered order (lowest number first). You can use NACLs to block specific IP addresses or CIDR ranges at the subnet level, something that security groups cannot do.

The key exam comparison: Security Groups are stateful (return traffic automatic), operate at the instance level, allow rules only. NACLs are stateless (must explicitly configure both directions), operate at the subnet level, support both allow and deny rules, evaluated in order.

If a scenario asks how to block a specific IP address at the network level, the answer is a NACL deny rule. Security groups cannot block specific IPs because they have no deny rules.

---

### SEGMENT 8 — Summary and Exam Tips (20:30–22:00)

Here are the key exam takeaways for Module 10.

VPC architecture: public subnets have a route to the Internet Gateway; private subnets do not. Place load balancers and NAT Gateways in public subnets. Place application servers, databases, and caches in private subnets.

Internet Gateway: bidirectional; enables public subnets to communicate with the internet. NAT Gateway: outbound-only; enables private subnets to initiate internet connections. Deploy one NAT Gateway per AZ.

VPC Peering: non-transitive, works for small numbers of VPCs. Transit Gateway: hub-and-spoke, required for many VPCs, cross-account, or on-premises integration at scale.

VPC Endpoints: Gateway Endpoints for S3 and DynamoDB (free, route table based). Interface Endpoints via PrivateLink for all other AWS services (paid).

Route 53: Weighted for blue-green deployments and A/B testing. Latency-based for lowest-latency global routing. Failover for active-passive DR. Geolocation for country-based routing.

Security Groups: stateful, instance-level, allow only. NACLs: stateless, subnet-level, allow and deny. Use NACLs to block specific IP addresses.

Module 11 covers IAM and security architecture. I'll see you there.

---

*End of Module 10 Video Script*

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
