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
