# Quiz: Module 10 — AWS Networking and VPC Design

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A solutions architect creates a VPC with the CIDR 10.0.0.0/16 and creates a subnet with the CIDR 10.0.1.0/24. The subnet is labeled "public" in the AWS console. A developer launches an EC2 instance in this subnet but the instance cannot communicate with the internet. What is the MOST LIKELY cause?

A. The subnet CIDR is too small to support internet routing

B. The subnet does not have a route to an Internet Gateway in its route table

C. The EC2 instance needs a NAT Gateway to access the internet

D. The VPC CIDR overlaps with a public IP address range

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The /24 CIDR size (256 addresses) has no bearing on internet routing. A subnet's internet connectivity is determined entirely by its route table, not its size.
- B is correct. A subnet is "public" only when its route table contains a route `0.0.0.0/0 → Internet Gateway`. Without this route, the subnet has no path to the internet regardless of its name in the console. The console label "public" is just a name tag — it does not configure routing.
- C is incorrect. NAT Gateways are for private subnet resources that need outbound-only internet access. A public subnet resource (with a public IP) uses the Internet Gateway directly, not a NAT Gateway.
- D is incorrect. The 10.0.0.0/16 range is RFC 1918 private address space and does not conflict with public routing. CIDR overlap becomes a problem when peering VPCs, not for internet connectivity.

---

### Question 2

A company has 12 VPCs in us-east-1. All VPCs need to communicate with a central Shared Services VPC that hosts DNS and security services. Connectivity between non-Shared-Services VPCs is not required. What is the MOST appropriate connectivity solution?

A. Establish VPC Peering connections between all 12 VPCs

B. Use Transit Gateway with the Shared Services VPC as a hub; configure TGW routing so non-hub VPCs cannot route to each other

C. Enable VPC Sharing for all VPCs using AWS Resource Access Manager

D. Use Direct Connect to route all VPC traffic through the on-premises network

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. 12 VPCs in a full mesh require 66 peering connections. Additionally, VPC Peering is non-transitive — if 12 VPCs all need to reach the Shared Services VPC but not each other, you need 11 peering connections (one per spoke). But managing 11 peering connections and route tables is complex, and future additions require new connections. Transit Gateway scales better.
- B is correct. Transit Gateway's hub-and-spoke model is designed for this exact pattern. Attach each VPC to TGW. Configure TGW route tables so that spoke VPCs only have routes to the Shared Services VPC, not to each other. Each new VPC only requires one TGW attachment.
- C is incorrect. VPC Sharing (via RAM) allows resources in different accounts to be deployed into the same VPC subnets. It does not solve the routing problem between 12 separate VPCs.
- D is incorrect. Routing VPC-to-VPC traffic through on-premises network introduces unnecessary latency, increases Direct Connect bandwidth consumption, and adds dependency on on-premises infrastructure for internal cloud communication.

---

### Question 3

An EC2 instance in a private subnet needs to access an Amazon S3 bucket to download configuration files. A security requirement states that traffic must not leave the AWS network. The current configuration routes all private subnet traffic through a NAT Gateway. What change minimizes cost while satisfying the security requirement?

A. Add a public IP address to the EC2 instance so it can connect directly to S3

B. Create an S3 Gateway Endpoint and add it to the private subnet's route table

C. Create an S3 Interface Endpoint in the private subnet

D. Move the EC2 instance to a public subnet

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Instances in a private subnet cannot have public IP addresses routed through an Internet Gateway. Adding a public IP does not change private subnet routing. This also violates the security requirement.
- B is correct. An S3 Gateway Endpoint routes S3-bound traffic directly from the VPC to S3 through AWS's private network, bypassing the NAT Gateway entirely. Gateway Endpoints for S3 and DynamoDB are free — no hourly cost, no data processing charge. This both satisfies the security requirement and reduces NAT Gateway data processing costs.
- C is incorrect. An S3 Interface Endpoint (PrivateLink) also keeps traffic off the public internet but incurs hourly costs and per-GB data processing charges. The Gateway Endpoint is free and is the preferred solution for S3 access from private subnets.
- D is incorrect. Moving the instance to a public subnet would remove it from the secure private tier and expose it to inbound internet traffic, creating a security risk.

---

### Question 4

A network administrator wants to block all inbound traffic from a specific IP address (198.51.100.1) to instances in a specific subnet. Security groups on the instances currently allow inbound HTTP traffic from all IP addresses. What is the CORRECT approach?

A. Add a deny rule to the security group for 198.51.100.1

B. Remove the existing security group rule that allows HTTP traffic from all addresses

C. Add a deny rule to the subnet's Network Access Control List for 198.51.100.1

D. Move the instances to a private subnet with no public IP addresses

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Security groups support allow rules only. There is no way to create a deny rule in a security group. All traffic not explicitly allowed is implicitly denied, but you cannot explicitly deny a specific IP address while continuing to allow all others.
- B is incorrect. Removing the HTTP allow rule would block traffic from all IP addresses, not just the specific malicious IP. This is too broad and would break legitimate traffic.
- C is correct. Network Access Control Lists support both allow and deny rules. Adding a NACL rule with a lower rule number that denies inbound traffic from 198.51.100.1 on any port (or HTTP specifically) blocks traffic from that IP at the subnet boundary before it reaches the security group or the instance.
- D is incorrect. Moving to a private subnet removes the public IP addresses but does not precisely block a specific IP — it blocks all inbound internet traffic. This is overly broad if the application needs to be publicly accessible.

---

### Question 5

A company runs a web application across two AWS Regions: us-east-1 (primary) and eu-west-1 (disaster recovery). Route 53 should serve all traffic to the us-east-1 endpoint under normal conditions and automatically route to eu-west-1 only when the primary is down. Which Route 53 routing policy implements this behavior?

A. Weighted Routing with us-east-1 at weight 100 and eu-west-1 at weight 0

B. Latency-Based Routing with health checks on both records

C. Failover Routing with us-east-1 as Primary and eu-west-1 as Secondary

D. Geolocation Routing routing US traffic to us-east-1 and European traffic to eu-west-1

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Weighted Routing with eu-west-1 at weight 0 means zero traffic goes to eu-west-1 — it does not serve as a failover. Route 53 Weighted Routing does not automatically reroute based on health; a weight of 0 simply means the record is never returned.
- B is incorrect. Latency-Based Routing routes users to the lowest-latency region, which would split traffic between us-east-1 and eu-west-1 based on geographic location — not implement active-passive failover.
- C is correct. Route 53 Failover Routing is the active-passive DR pattern. The primary record (us-east-1) receives all traffic. A health check monitors the primary endpoint. If the health check fails, Route 53 automatically returns the secondary record (eu-west-1) to clients. When the primary recovers and passes health checks, Route 53 automatically switches back.
- D is incorrect. Geolocation Routing routes based on the user's country, not on the health of the primary endpoint. Both endpoints would remain active simultaneously, and there would be no automatic failover if us-east-1 went down for European or other users.

---

### Question 6

A company's application tier EC2 instances are in a private subnet. The private subnet's route table has two routes: `10.0.0.0/16 → local` and `0.0.0.0/0 → nat-gateway-id`. A developer reports that the application instances cannot reach `169.254.169.254` to retrieve EC2 instance metadata. What is the cause?

A. The NAT Gateway blocks access to the instance metadata service

B. `169.254.169.254` is a link-local address accessible within the subnet without any routing configuration

C. The security group on the EC2 instances must allow outbound traffic to 169.254.169.254

D. A NAT Gateway is required to access the EC2 metadata service from private subnets

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The EC2 instance metadata service at `169.254.169.254` is a link-local address accessible at the instance level without leaving the subnet. It does not go through the NAT Gateway or any external route.
- B is correct. `169.254.169.254` is the EC2 Instance Metadata Service (IMDS) endpoint. It is a link-local address that is accessible to every EC2 instance regardless of subnet type or route table configuration. No route to this address is needed in the route table — it is always locally accessible.
- C is incorrect. Security groups do not block outbound traffic to IMDS by default. The default security group has an outbound allow-all rule. Even with a restrictive security group, IMDS is accessible because it does not traverse the security group in the traditional sense — it is a local hypervisor service.
- D is incorrect. The developer's report is likely not accurate, or the metadata endpoint is being blocked by something else (like IMDSv2 requiring a token). The route table has no bearing on IMDS accessibility.

---

### Question 7

An architect needs to connect 4 VPCs using VPC Peering. VPC-A must communicate with VPC-B and VPC-C. VPC-B must communicate with VPC-C and VPC-D. VPC-C must communicate with VPC-D. VPC-A must NOT be able to communicate with VPC-D. Which statement about this topology is TRUE?

A. Transit Gateway can enforce the VPC-A to VPC-D restriction but VPC Peering cannot

B. Exactly 5 VPC Peering connections are required and VPC-A will never be able to reach VPC-D because peering is non-transitive

C. VPC Peering transitivity means VPC-A can reach VPC-D through VPC-B or VPC-C

D. You need only 2 peering connections because Transit Gateway provides the rest

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. VPC Peering is non-transitive by default. If there is no direct peering connection between VPC-A and VPC-D, VPC-A cannot communicate with VPC-D regardless of what other peering connections exist. Transit Gateway is not required to enforce this restriction — the non-transitive nature of peering enforces it inherently.
- B is correct. The required connections are: A-B, A-C, B-C, B-D, C-D — exactly 5. VPC Peering is non-transitive, so VPC-A cannot reach VPC-D through VPC-B (A→B→D is not possible with peering) or VPC-C (A→C→D is not possible). The restriction is naturally enforced by peering's non-transitive nature.
- C is incorrect. This directly contradicts the non-transitive property of VPC Peering. Traffic cannot transit through an intermediate VPC in a peering relationship.
- D is incorrect. Transit Gateway is not involved in this scenario. VPC Peering is the stated connectivity mechanism, and Transit Gateway is a separate service.

---

### Question 8

An application on EC2 needs to make API calls to AWS Systems Manager Parameter Store. The EC2 instance is in a private subnet with no route to the internet and no NAT Gateway. Which solution enables the connection?

A. Assign a public IP to the EC2 instance

B. Create an Interface VPC Endpoint for AWS Systems Manager in the VPC

C. Create a Gateway Endpoint for AWS Systems Manager

D. Add a route to the internet in the private subnet's route table

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. A public IP on an EC2 instance in a private subnet does not create an outbound internet path. Internet-bound traffic requires a route to an Internet Gateway, which the private subnet does not have.
- B is correct. AWS Systems Manager is one of the many AWS services that supports Interface VPC Endpoints powered by PrivateLink. An Interface Endpoint creates an ENI in the private subnet, allowing EC2 to reach SSM Parameter Store through the AWS private network without requiring internet access.
- C is incorrect. Gateway Endpoints are only available for S3 and DynamoDB. AWS Systems Manager does not support Gateway Endpoints. For all other AWS services, Interface Endpoints are required.
- D is incorrect. Adding a route to the internet requires an Internet Gateway, which makes the subnet public. This violates the private subnet requirement and the implicit requirement to avoid public internet exposure.

---

### Question 9

A company wants to route 10% of traffic to a new version of their application (v2) and 90% to the existing version (v1). After validation, they will shift to 100% v2. Which Route 53 routing policy provides this capability?

A. Failover Routing

B. Latency-Based Routing

C. Weighted Routing

D. Geolocation Routing

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Failover Routing is an active-passive pattern — one endpoint receives all traffic and the other only receives traffic when the primary fails. It cannot split traffic proportionally.
- B is incorrect. Latency-Based Routing routes based on network latency from the user to each endpoint. It does not distribute traffic by percentage.
- C is correct. Weighted Routing assigns numeric weights to DNS records. Setting v1 to weight 90 and v2 to weight 10 sends approximately 10% of queries to v2. To complete the migration, change v1 to weight 0 and v2 to weight 100 (or delete the v1 record).
- D is incorrect. Geolocation Routing distributes traffic based on the user's geographic location. It cannot split traffic percentages between two versions of the same application.

---

### Question 10

An EC2 instance in a private subnet is associated with a security group that allows all outbound traffic. The subnet's Network ACL has an outbound rule 100 that allows ALL TCP traffic. An engineer adds a new NACL rule 50 that denies outbound TCP traffic on port 443. Traffic from the instance to external HTTPS endpoints now fails. What is the cause?

A. The security group outbound allow rule does not override the NACL deny rule

B. NACL rules are evaluated after security group rules, so security groups cannot override NACLs

C. NACL rule 50 has a higher rule number than rule 100, so rule 100 takes precedence

D. NACLs only apply to inbound traffic; this must be a security group issue

**Correct Answer: A**

**Distractor Analysis:**

- A is correct. NACLs are evaluated independently of security groups. A NACL deny rule stops traffic at the subnet boundary regardless of what the security group allows. NACLs are processed in rule number order — rule 50 (deny HTTPS) is evaluated before rule 100 (allow all TCP) because it has a lower number. The NACL deny takes precedence, stopping outbound HTTPS traffic.
- B is incorrect. The statement about evaluation order is backwards in its implication. NACLs operate at the subnet level and are evaluated before traffic reaches the instance security group for inbound traffic, and after it leaves the instance for outbound traffic. Either way, NACLs and security groups are independent layers — a NACL deny blocks regardless of security group rules.
- C is incorrect. NACL rules are evaluated in ascending numeric order and processing stops at the first matching rule. Rule 50 has a LOWER number than rule 100, so it is evaluated FIRST. This means the deny rule at 50 triggers before the allow rule at 100 is ever evaluated.
- D is incorrect. NACLs apply to both inbound and outbound traffic. This is a key difference from security groups (stateful) vs. NACLs (stateless) — both directions must be explicitly allowed in NACLs.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
