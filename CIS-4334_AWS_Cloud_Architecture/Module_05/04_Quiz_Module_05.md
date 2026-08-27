# Quiz: Module 05 - VPC: Subnets, Route Tables, Security Groups, NACLs

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Questions:** 10

---

## Question 1

A solutions architect is designing a VPC with a CIDR block of 10.0.0.0/16. They create a subnet with the CIDR 10.0.1.0/24. How many IP addresses are available for EC2 instances in this subnet?

- A) 256
- B) 254
- C) 251
- D) 248

### Answer 1

Correct Answer: C

### Explanation 1

- A is incorrect: 256 is the total number of IP addresses in a /24 block, but AWS reserves 5 of them.
- B is incorrect: 254 would be the number of usable addresses if only 2 were reserved (network and broadcast). AWS reserves 5 addresses.
- C is correct: AWS reserves 5 IP addresses in every subnet: the network address (.0), the VPC router (.1), the Amazon DNS resolver (.2), a reserved future-use address (.3), and the broadcast address (.255). 256 minus 5 equals 251 usable addresses.
- D is incorrect: 248 does not correspond to any standard IP reservation calculation for AWS subnets.

---

## Question 2

An EC2 instance in a private subnet needs to download software updates from the internet. The instance has no public IP address. Which resource enables outbound internet connectivity for this instance while preventing unsolicited inbound connections from the internet?

- A) Internet Gateway attached to the private subnet's route table
- B) VPC Peering connection to a public VPC
- C) NAT Gateway deployed in a public subnet, with a route in the private subnet's route table pointing to it
- D) An Elastic IP address assigned directly to the private EC2 instance

### Answer 2

Correct Answer: C

### Explanation 2

- A is incorrect: An Internet Gateway in a private subnet's route table would require the instance to have a public IP to receive return traffic. More importantly, it would also allow inbound connections from the internet, violating the requirement.
- B is incorrect: VPC Peering enables private communication between two VPCs. It does not provide internet access for private subnet resources.
- C is correct: A NAT Gateway in a public subnet performs network address translation — it sends outbound requests to the internet using its own Elastic IP and forwards responses back to the originating private instance. Unsolicited inbound connections from the internet cannot reach the private instance because NAT Gateway does not forward inbound traffic.
- D is incorrect: Assigning an Elastic IP to an instance in a private subnet does not work — the subnet must have a route to an Internet Gateway for the Elastic IP to be usable, which would also expose the instance to inbound internet connections.

---

## Question 3

A security team needs to block all traffic from a specific malicious IP address range (198.51.100.0/24) from reaching any instance in a public subnet. Which resource is the correct tool for this requirement?

- A) Security Group — add a deny rule for 198.51.100.0/24
- B) Network ACL — add a deny rule with a rule number lower than existing allow rules
- C) IAM policy with a source IP condition
- D) Route table — add a route for 198.51.100.0/24 pointing to a blackhole

### Answer 3

Correct Answer: B

### Explanation 3

- A is incorrect: Security Groups only support Allow rules. There is no mechanism to add an explicit Deny rule to a security group. Any traffic not explicitly allowed is implicitly denied, but you cannot create a rule that explicitly blocks a specific source IP.
- B is correct: Network ACLs support both Allow and Deny rules. Adding a Deny rule with a rule number lower than 100 (the typical first allow rule) ensures traffic from 198.51.100.0/24 is blocked before any allow rule matches. NACLs apply at the subnet level, so all instances in the public subnet are protected.
- C is incorrect: IAM policies with source IP conditions control access to AWS API calls (like the AWS Management Console or S3), not VPC network-level traffic to EC2 instances.
- D is incorrect: A blackhole route would need to specifically match 198.51.100.0/24 as a destination — meaning traffic FROM 198.51.100.0/24 would route normally (the route table controls outbound destinations from within the VPC, not inbound sources). Route tables do not filter traffic based on source IP.

---

## Question 4

A developer notices that after adding an inbound rule to a security group allowing TCP port 443 from the internet, the HTTPS connections succeed. But after adding an equivalent inbound NACL rule, HTTPS connections from the internet time out. What is the most likely cause?

- A) NACLs cannot allow HTTPS traffic — only security groups can permit port 443
- B) The NACL is stateless and requires a corresponding outbound rule allowing the ephemeral port range (1024-65535) for response traffic
- C) NACLs only take effect after a 15-minute propagation delay
- D) The NACL inbound rule must reference the security group ID instead of a CIDR range

### Answer 4

Correct Answer: B

### Explanation 4

- A is incorrect: NACLs can permit any traffic including HTTPS. There is no protocol restriction on NACLs.
- B is correct: NACLs are stateless. When a client connects to the EC2 instance on port 443, the response is sent from the instance back to the client on an ephemeral port (1024-65535) that the client OS assigned. The NACL outbound rules must explicitly allow this ephemeral port range. Without the outbound ephemeral port rule, response packets are blocked and connections time out.
- C is incorrect: NACL rule changes take effect immediately with no propagation delay.
- D is incorrect: NACLs do not support security group references as sources. They only support CIDR blocks. This is one of the key differences between NACLs and security groups.

---

## Question 5

A company has three VPCs: VPC-A, VPC-B, and VPC-C. VPC-A is peered with VPC-B. VPC-B is peered with VPC-C. An engineer configures a route in VPC-A's route table to reach VPC-C's CIDR through VPC-B. Resources in VPC-A still cannot reach resources in VPC-C. What is the cause?

- A) VPC peering does not support IPv4 routing
- B) VPC peering is non-transitive; VPC-A needs a direct peering connection with VPC-C to communicate with it
- C) The VPC peering connection requires an Internet Gateway to route between non-adjacent VPCs
- D) The CIDR blocks of VPC-A and VPC-C must be identical for peering to work

### Answer 5

Correct Answer: B

### Explanation 5

- A is incorrect: VPC peering fully supports IPv4 routing. IPv6 peering is also supported.
- B is correct: VPC peering is explicitly non-transitive. Even if a route is configured in VPC-A pointing to VPC-C's CIDR through VPC-B, AWS does not forward that traffic through the peering connection. A direct peering connection between VPC-A and VPC-C is required for them to communicate. This is a fundamental limitation of VPC peering — for scalable multi-VPC connectivity, use Transit Gateway.
- C is incorrect: Internet Gateways are for internet connectivity, not inter-VPC routing. VPC peering provides direct private connectivity.
- D is incorrect: CIDR blocks must be different (non-overlapping) for VPC peering to work. Identical CIDRs would make peering impossible due to routing ambiguity.

---

## Question 6

A company has 15 VPCs that all need to communicate with each other for internal services. The network team is evaluating whether to use VPC peering or Transit Gateway. Which factor most strongly favors Transit Gateway in this scenario?

- A) VPC peering does not support cross-account connectivity
- B) Transit Gateway is free while VPC peering has per-GB data transfer charges
- C) Establishing full connectivity between 15 VPCs with peering would require 105 separate peering connections, while Transit Gateway requires only 15 attachments with transitive routing
- D) VPC peering cannot be used in the same Region as Transit Gateway

### Answer 6

Correct Answer: C

### Explanation 6

- A is incorrect: VPC peering fully supports cross-account connectivity. The accepting VPC's account accepts the peering request.
- B is incorrect: Transit Gateway has both an hourly attachment fee and per-GB data processing charges. VPC peering has no hourly fee — only data transfer charges (free within the same AZ). Transit Gateway is not cheaper for small-scale deployments.
- C is correct: Full mesh connectivity between N VPCs requires N(N-1)/2 peering connections. For 15 VPCs, that is 15×14/2 = 105 connections to manage. Each connection requires route table entries in both VPCs. Transit Gateway requires one attachment per VPC (15 total) and supports transitive routing, eliminating the management overhead.
- D is incorrect: VPC peering and Transit Gateway can coexist in the same Region. They serve different connectivity scenarios and are not mutually exclusive.

---

## Question 7

An EC2 instance in a private subnet needs to send API calls to Amazon S3. The application team wants to ensure that S3 traffic never traverses the public internet and incurs no NAT Gateway data processing charges. Which solution achieves both requirements?

- A) Enable S3 Transfer Acceleration on the bucket
- B) Create an S3 Gateway VPC Endpoint and add a route to the private subnet's route table
- C) Deploy a NAT Gateway in each AZ for the private subnets
- D) Assign an Elastic IP address to the EC2 instance

### Answer 7

Correct Answer: B

### Explanation 7

- A is incorrect: S3 Transfer Acceleration routes traffic through CloudFront Edge Locations, which are on the public internet. It increases cost and does not keep traffic private.
- B is correct: An S3 Gateway VPC Endpoint routes S3 traffic through the AWS private network, bypassing the internet completely. It is added to the VPC route table as a route destination for S3 service endpoints. There is no charge for the endpoint or for data transferred through it — eliminating NAT Gateway processing fees for S3 traffic.
- C is incorrect: A NAT Gateway routes traffic to the public internet, which violates the first requirement. It also charges per-GB of data processed, which violates the cost requirement.
- D is incorrect: Assigning an Elastic IP to a private subnet instance does not make it reachable without a route to an Internet Gateway (which would also expose it to inbound connections and still route traffic over the internet).

---

## Question 8

A company is setting up connectivity between their on-premises data center and their AWS VPC. The requirements are: dedicated network bandwidth of 10 Gbps, consistent latency, and traffic must not traverse the public internet. Which connectivity option meets all three requirements?

- A) AWS Site-to-Site VPN with multiple tunnels for aggregated bandwidth
- B) AWS Direct Connect with a 10 Gbps port
- C) VPC Peering to an AWS-managed transit VPC
- D) Internet Gateway with Elastic IPs for all private instances

### Answer 8

Correct Answer: B

### Explanation 8

- A is incorrect: AWS Site-to-Site VPN tunnels use the public internet (encrypted via IPsec). Each tunnel supports up to 1.25 Gbps. Multiple tunnels can be aggregated, but VPN traffic still traverses the public internet, which violates the third requirement.
- B is correct: AWS Direct Connect provides a dedicated private network connection between on-premises and AWS. A 10 Gbps port provides consistent, dedicated bandwidth. Traffic routes through the AWS network and does not traverse the public internet.
- C is incorrect: VPC Peering connects two VPCs within AWS. It does not connect on-premises networks to AWS and has no concept of a transit VPC for on-premises connectivity.
- D is incorrect: An Internet Gateway with public IPs routes traffic over the public internet and provides no dedicated bandwidth or latency guarantees.

---

## Question 9

A company enables VPC Flow Logs on their production VPC. The security team reports that they cannot find log entries for DHCP traffic or DNS queries made through the Amazon-provided DNS resolver (169.254.169.253). Is this a configuration error?

- A) Yes — VPC Flow Logs should capture all traffic including DHCP and DNS; the flow log configuration must be incorrect
- B) No — VPC Flow Logs do not capture DHCP traffic, traffic to/from the Amazon DNS resolver, or traffic to the instance metadata service endpoint
- C) Yes — DHCP and DNS traffic must be captured by enabling Enhanced Networking on the EC2 instances
- D) No — DHCP and DNS traffic are captured only in S3-based Flow Logs, not CloudWatch-based Flow Logs

### Answer 9

Correct Answer: B

### Explanation 9

- A is incorrect: This is expected behavior, not a misconfiguration.
- B is correct: VPC Flow Logs explicitly exclude certain types of traffic regardless of configuration: DHCP traffic, traffic to/from the Amazon DNS server (169.254.169.253), traffic to/from the instance metadata service (169.254.169.254), and Amazon Windows license activation traffic. For DNS query visibility, use Route 53 Resolver Query Logs separately.
- C is incorrect: Enhanced Networking is a performance feature that enables higher network bandwidth and lower CPU utilization on EC2 instances. It does not affect what VPC Flow Logs capture.
- D is incorrect: The exclusions apply regardless of whether Flow Logs are published to CloudWatch Logs or S3. The destination does not affect which traffic is included.

---

## Question 10

A network architect is designing a new AWS environment with a hub-and-spoke architecture. There is a central Network Services VPC containing shared services (DNS, Active Directory, firewall appliances) and 12 spoke VPCs for different business units. All spoke VPCs must be able to reach the Network Services VPC, and traffic between spoke VPCs must pass through the firewall appliances in the Network Services VPC for inspection. Which architecture supports this design?

- A) VPC Peering between each spoke VPC and the Network Services VPC, with VPC Peering between all spoke VPCs for direct communication
- B) Transit Gateway connecting all VPCs, with a Transit Gateway route table that sends inter-spoke traffic through the Network Services VPC for inspection
- C) Internet Gateway in the Network Services VPC with all spoke VPCs routing through the internet for connectivity
- D) VPC Peering from each spoke to the Network Services VPC, relying on transitive routing through the Network Services VPC

### Answer 10

Correct Answer: B

### Explanation 10

- A is incorrect: Peering between all 12 spoke VPCs would require 66 peering connections (12×11/2) plus 12 more to the Network Services VPC. More critically, VPC peering is non-transitive — traffic between spoke VPCs cannot be forced through the Network Services VPC firewall via peering alone.
- B is correct: Transit Gateway supports centralized inspection architectures. A TGW route table can direct inter-spoke traffic to the Network Services VPC attachment before routing to the destination spoke. This implements a hub-and-spoke with centralized firewall inspection — a common enterprise architecture pattern on the SAA-C03 exam.
- C is incorrect: Routing through the internet introduces latency, security risks, and bandwidth costs. Enterprise spoke-to-hub traffic should never traverse the public internet.
- D is incorrect: VPC peering is non-transitive. Traffic from Spoke VPC A destined for Spoke VPC B cannot be routed through the Network Services VPC via peering — the traffic would be dropped. Only Transit Gateway supports this transitive inspection pattern.

---

## Question 11

An EC2 instance in a private subnet needs to download software packages from the internet. The instance has no public IP address. The VPC has an Internet Gateway attached. What additional component must be deployed and how must routing be configured?

- A) Assign an Elastic IP address to the instance and add a 0.0.0.0/0 route in the private route table pointing to the Internet Gateway
- B) Deploy a NAT Gateway in a public subnet; add a 0.0.0.0/0 route in the private subnet route table pointing to the NAT Gateway ID
- C) Enable VPC Flow Logs and configure them to route internet-bound traffic through the AWS backbone
- D) Create a VPC Gateway Endpoint for the internet to allow outbound traffic from private subnets

### Answer 11

Correct Answer: B

### Explanation 11

- A is incorrect: Assigning an Elastic IP to a private instance would make it reachable from the internet (unless security groups block inbound access), which defeats the purpose of a private subnet. Additionally, a 0.0.0.0/0 route to the Internet Gateway in the private route table would make the subnet public in behavior.
- B is correct: A NAT Gateway must be deployed in a public subnet (where a 0.0.0.0/0 route to the Internet Gateway already exists). The private route table must have a 0.0.0.0/0 route pointing to the NAT Gateway. Traffic flows: private instance → NAT Gateway (public subnet) → Internet Gateway → internet. Return traffic reverses this path. The private instance's private IP is never exposed to the internet.
- C is incorrect: VPC Flow Logs capture metadata about network traffic for monitoring and troubleshooting. They do not route traffic or provide internet connectivity.
- D is incorrect: VPC Gateway Endpoints exist for S3 and DynamoDB only. There is no "internet" VPC Gateway Endpoint. Gateway Endpoints route traffic to specific AWS services through the AWS private network, not to the public internet.

---

## Question 12

A security engineer is reviewing a VPC configuration and wants to prevent all instances in a specific subnet from initiating outbound connections to the internet, regardless of their security group rules. Which control achieves this at the subnet level?

- A) Create a security group rule denying all outbound traffic and attach it to all instances in the subnet
- B) Remove the 0.0.0.0/0 outbound route from the subnet's route table and do not add a NAT Gateway route
- C) Apply a NACL rule on the subnet with an explicit Deny for outbound traffic to 0.0.0.0/0
- D) Both B and C are correct, but B is the simpler and more complete control

### Answer 12

Correct Answer: D

### Explanation 12

- A is incorrect: Security groups are stateful and apply at the instance level, not the subnet level. Additionally, security groups cannot contain explicit Deny rules — they use implicit deny. Removing outbound rules from a security group blocks outbound traffic from those specific instances, but this requires updating every instance's security group and is not a subnet-level control.
- B is correct: Removing the internet-bound route from the route table is the simplest and most effective subnet-level control. Without a route, traffic destined for the internet has no path and is dropped by the VPC router.
- C is correct: A NACL Deny rule on outbound traffic to 0.0.0.0/0 blocks internet-bound traffic at the subnet boundary. NACLs apply to all traffic entering or leaving the subnet, regardless of instance security group rules.
- D is correct: Both B and C achieve the goal. Removing the route is simpler and sufficient by itself because without a route, traffic cannot be forwarded. Using both provides defense in depth — the route table controls forwarding, and the NACL provides an explicit block even if a route is accidentally added later.

---

## Question 13

A company has two VPCs in the same AWS Region: VPC-A (10.0.0.0/16) and VPC-B (10.1.0.0/16). A VPC peering connection is established between them. An EC2 instance in VPC-A cannot reach an EC2 instance in VPC-B. Both security groups allow traffic on the required port. What is the most likely cause?

- A) VPC peering connections between VPCs in the same Region are not supported
- B) The route tables in VPC-A and/or VPC-B have not been updated with routes for the peer VPC's CIDR block
- C) VPC peering connections require a NAT Gateway to route traffic between the two VPCs
- D) The security group in VPC-B cannot reference a security group from VPC-A as a source for cross-VPC traffic

### Answer 13

Correct Answer: B

### Explanation 13

- A is incorrect: VPC peering within the same Region is fully supported and is the original VPC peering use case. Cross-region VPC peering is also supported.
- B is correct: Creating a VPC peering connection does not automatically add routes to the VPC route tables. After establishing the peering connection, each VPC's route table must have a route for the peer VPC's CIDR block pointing to the peering connection ID (pcx-xxxxxxxxx). Without these routes, traffic cannot flow between the VPCs even though the peering connection exists.
- C is incorrect: NAT Gateways are not required for VPC peering. VPC peering establishes a direct private network connection between the two VPCs. NAT Gateways are used for outbound internet access from private subnets.
- D is incorrect: VPC peering does support cross-VPC security group references within the same Region. You can specify the peer VPC's security group ID as the source in a security group rule. However, the question states security groups are already correctly configured.

---

## Question 14

An architect is designing subnet CIDR allocation for a VPC with CIDR 10.0.0.0/16 deployed across three Availability Zones. The design requires a public subnet, a private subnet, and a database subnet in each AZ. What is the minimum subnet size that provides at least 200 usable IP addresses per subnet while fitting all nine subnets within the /16 VPC?

- A) /24 subnets providing 251 usable IPs each
- B) /25 subnets providing 123 usable IPs each
- C) /27 subnets providing 27 usable IPs each
- D) /20 subnets providing 4,091 usable IPs each

### Answer 14

Correct Answer: A

### Explanation 14

- A is correct: A /24 subnet contains 256 IP addresses; AWS reserves 5 (network address, VPC router, DNS, future use, broadcast), leaving 251 usable IPs — exceeding the 200 IP requirement. Nine /24 subnets consume 9 × 256 = 2,304 IP addresses out of the 65,536 available in a /16 VPC, leaving over 60,000 IP addresses unallocated for future growth.
- B is incorrect: A /25 subnet contains 128 IP addresses; after AWS reserves 5, only 123 are usable. This does not meet the 200 usable IP requirement.
- C is incorrect: A /27 subnet contains 32 IP addresses; after AWS reserves 5, only 27 are usable. This is far below the 200 IP requirement.
- D is incorrect: A /20 subnet provides 4,091 usable IPs, which exceeds the requirement, but it is 16 times larger than necessary. Nine /20 subnets would consume 9 × 4,096 = 36,864 IPs, leaving limited address space for future expansion. /24 satisfies the requirement more efficiently.

---

## Question 15

A developer deploys an EC2 instance in a public subnet with a public IP address. The instance has a security group that allows SSH inbound on port 22 from the developer's IP address (1.2.3.4/32). The developer cannot SSH to the instance. VPC Flow Logs show inbound SSH traffic arriving at the instance with an ACCEPT result, but the connection times out. What is the most likely cause?

- A) The Internet Gateway is not attached to the VPC
- B) The NACL on the public subnet is blocking inbound SSH or outbound ephemeral port responses
- C) The security group is blocking outbound traffic on the ephemeral port range because security groups require explicit outbound rules for return traffic
- D) The instance's operating system firewall (iptables) is blocking the connection

### Answer 15

Correct Answer: B

### Explanation 15

- A is incorrect: If the Internet Gateway were not attached, VPC Flow Logs would show the traffic not reaching the instance at all. The question states Flow Logs show ACCEPT on inbound — meaning traffic reached the instance and the security group allowed it. The IGW is working.
- B is correct: VPC Flow Logs showing ACCEPT for inbound SSH means the security group allowed the traffic. The connection timeout despite an ACCEPT result typically means the return traffic (outbound ephemeral ports 1024-65535) is being blocked by a stateless NACL. The developer's response packets cannot leave the subnet because the NACL outbound rules do not include the ephemeral port range. Security groups are stateful and automatically allow return traffic, but NACLs are stateless and require explicit outbound ephemeral port rules.
- C is incorrect: Security groups are stateful — they automatically allow return traffic without requiring an explicit outbound rule. No outbound security group rule is needed for established inbound connections.
- D is incorrect: While OS-level firewalls can cause connectivity issues, the question is specifically testing VPC networking concepts. The combination of Flow Log ACCEPT result and timeout is the classic indicator of a NACL stateless return traffic issue.

---

## Question 16

A company needs to ensure that EC2 instances in private subnets can access Amazon DynamoDB without internet connectivity, and that all DynamoDB API traffic stays within the AWS network. Which solution accomplishes this without requiring a NAT Gateway for DynamoDB traffic?

- A) Deploy a NAT Gateway in a public subnet and route all private subnet traffic through it
- B) Create a VPC Interface Endpoint for DynamoDB in each private subnet
- C) Create a VPC Gateway Endpoint for DynamoDB and update the private subnet route tables to route DynamoDB traffic to the endpoint
- D) Enable DynamoDB global tables in the same Region to create a local copy of the table

### Answer 16

Correct Answer: C

### Explanation 16

- A is incorrect: A NAT Gateway allows private instances to access DynamoDB through the internet. This sends DynamoDB API traffic over the public internet and incurs NAT Gateway data processing charges per GB. The question specifically requires staying within the AWS network without a NAT Gateway for DynamoDB traffic.
- B is incorrect: DynamoDB is available as a Gateway VPC Endpoint, not an Interface Endpoint. Interface Endpoints use AWS PrivateLink and have hourly charges, while Gateway Endpoints for DynamoDB and S3 are free. The correct endpoint type for DynamoDB is the Gateway Endpoint.
- C is correct: DynamoDB supports a VPC Gateway Endpoint. Creating the Gateway Endpoint and adding a route entry in the private subnet route table directs DynamoDB API traffic through the AWS private network. There are no data processing charges for Gateway Endpoint traffic, and no NAT Gateway is required.
- D is incorrect: DynamoDB global tables replicate a table across multiple AWS Regions for multi-region active-active access. This is a different feature entirely and does not eliminate the need for a NAT Gateway for API access from private subnets.

---

## Question 17

A solutions architect is designing a multi-tier application with these security requirements: the web tier must accept HTTPS from the internet; the application tier must only accept traffic from the web tier; the database tier must only accept traffic from the application tier. Which approach correctly implements these isolation requirements using security groups?

- A) Use Network ACLs to block direct access between tiers and use security groups with port ranges only
- B) Create separate security groups for each tier; reference the web tier security group as the source in the app tier security group; reference the app tier security group as the source in the database tier security group
- C) Use a single security group for all three tiers with broad port ranges to allow internal communication
- D) Assign Elastic IPs to each tier and use IP-based source restrictions in each security group

### Answer 17

Correct Answer: B

### Explanation 17

- A is incorrect: Using NACLs for east-west tier isolation requires knowing the CIDR ranges of each subnet and maintaining NACL rule order. Security group references are more dynamic, easier to maintain, and more precise than CIDR-based NACL rules for east-west tier isolation.
- B is correct: Referencing a security group ID as the source (rather than a CIDR block) means the rule applies to any instance that has that security group attached. This is the AWS best practice for east-west tier isolation in multi-tier architectures. The app tier security group rule specifies the web tier SG ID as source, and the database tier SG rule specifies the app tier SG ID as source.
- C is incorrect: A single security group for all tiers with broad port ranges eliminates tier isolation entirely. Any instance in any tier could communicate with any other instance on the allowed ports, defeating the security architecture.
- D is incorrect: Elastic IPs are public IP addresses. Using Elastic IPs for internal east-west traffic forces the traffic to exit to the internet and return, which is expensive, slower, and exposes private traffic to the internet.

---

## Question 18

An architect is auditing a VPC configuration and notices that VPC Flow Logs are enabled but a security team member says they cannot see DNS queries in the flow log records. What is the reason?

- A) VPC Flow Logs only capture TCP traffic; UDP (which DNS uses) is not captured
- B) VPC Flow Logs capture IP-level network traffic but do not capture DNS query content, hostname lookups, or application-layer metadata
- C) VPC Flow Logs must be enabled on the individual EC2 instances to capture DNS traffic, not at the VPC or subnet level
- D) DNS traffic is encrypted and cannot be captured by VPC Flow Logs

### Answer 18

Correct Answer: B

### Explanation 18

- A is incorrect: VPC Flow Logs capture both TCP and UDP traffic. DNS typically uses UDP port 53. UDP traffic does appear in VPC Flow Logs as individual packet records.
- B is correct: VPC Flow Logs capture IP-level metadata: source IP, destination IP, source port, destination port, protocol, bytes, packets, action (ACCEPT/REJECT), and flow direction. They do not capture DNS query names, hostname resolution details, application payload content, or HTTP request content. To capture DNS query content, use Route 53 Resolver Query Logs.
- C is incorrect: VPC Flow Logs can be enabled at three levels: VPC, subnet, or individual network interface (ENI). All three capture the same metadata. DNS traffic from EC2 instances appears in subnet-level or VPC-level flow logs as UDP packets to port 53.
- D is incorrect: Standard DNS queries over UDP port 53 are not encrypted. DNS over HTTPS (DoH) or DNS over TLS (DoT) are encrypted, but standard VPC DNS traffic to the Route 53 Resolver at the VPC+2 address (169.254.169.253) is unencrypted UDP. The limitation is about application-layer content capture, not encryption.

---

## Question 19

A company wants to connect its on-premises data center (192.168.0.0/16) to an AWS VPC (10.0.0.0/16) using AWS Direct Connect. They also have a second VPC (10.1.0.0/16) in the same Region that needs to communicate with on-premises systems. Which AWS networking component allows a single Direct Connect connection to reach both VPCs?

- A) VPC Peering between the two VPCs with routes propagated to the on-premises router
- B) A Direct Connect Gateway attached to the Direct Connect connection, with a Transit Gateway or Virtual Private Gateway for each VPC
- C) Two separate Direct Connect connections — one per VPC — from the same Direct Connect location
- D) AWS Site-to-Site VPN over the Direct Connect connection with split tunneling to each VPC

### Answer 19

Correct Answer: B

### Explanation 19

- A is incorrect: VPC Peering does not propagate routes to on-premises networks. VPC peering is non-transitive — routing learned from Direct Connect in one VPC does not extend through peering to the second VPC.
- B is correct: A Direct Connect Gateway enables a single Direct Connect connection to access multiple VPCs across Regions (with some restrictions). The Direct Connect Gateway connects to a Transit Gateway (for scalable multi-VPC connectivity) or Virtual Private Gateways in each VPC. This is the standard AWS architecture for sharing a Direct Connect connection across multiple VPCs.
- C is incorrect: Establishing a second Direct Connect connection per VPC doubles the Direct Connect port and data transfer costs unnecessarily. Direct Connect Gateways exist specifically to solve this multi-VPC sharing requirement.
- D is incorrect: VPN over Direct Connect (also called hosted VPN) is used to encrypt Direct Connect traffic for compliance requirements. It does not address the multi-VPC connectivity challenge and does not replace the need for a Direct Connect Gateway or Transit Gateway.

---

## Question 20

A startup deploys a three-tier application in a VPC. After launch, the operations team realizes that the VPC CIDR (10.0.0.0/24) is too small — they need to add more subnets for a new service tier. What is the correct approach to expand the VPC's address space?

- A) Delete all existing subnets and recreate the VPC with a larger CIDR block
- B) Associate a secondary CIDR block to the existing VPC from a non-overlapping range
- C) Enable VPC CIDR auto-expansion, which adds address space automatically when subnets run out
- D) Create a new VPC with a larger CIDR and migrate all resources using AWS Server Migration Service

### Answer 20

Correct Answer: B

### Explanation 20

- A is incorrect: Deleting all subnets to recreate the VPC requires terminating all running EC2 instances, deleting all subnet-dependent resources (RDS, ELB, NAT Gateways), and rebuilding the entire network layer. This causes extensive downtime and is not the correct approach.
- B is correct: AWS allows you to associate up to four secondary IPv4 CIDR blocks to an existing VPC. The secondary CIDR must not overlap with the primary CIDR, existing secondary CIDRs, or the on-premises network. Additional subnets can be created from the secondary CIDR and used immediately without affecting existing resources.
- C is incorrect: VPC CIDR auto-expansion does not exist as an AWS feature. VPC CIDR blocks must be explicitly defined and secondary CIDRs must be manually associated.
- D is incorrect: Migrating all resources to a new VPC is operationally complex, causes service disruption, and requires reconfiguring all network-dependent resources. Adding a secondary CIDR block to the existing VPC is the non-disruptive solution.
