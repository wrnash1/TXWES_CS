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

### Question 11 (5 points)

An application running on EC2 in a private subnet must access Amazon S3 without sending traffic over the internet and without using a NAT Gateway. Which solution achieves private S3 access at the lowest cost?

A. Configure an S3 Interface Endpoint (PrivateLink) in the private subnet

B. Configure an S3 Gateway Endpoint and add the endpoint to the private subnet's route table

C. Configure a NAT Instance in a public subnet and route S3 traffic through it

D. Enable S3 Transfer Acceleration to route traffic over the AWS backbone

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. S3 supports both Gateway Endpoints (free) and Interface Endpoints (hourly + data processing charges). The Gateway Endpoint is the more cost-effective option for S3 access from within a VPC. Interface Endpoints are appropriate when you need to access S3 from on-premises via Direct Connect or VPN.
- B is correct. S3 Gateway Endpoints route S3 API traffic through the AWS private network at no additional charge. Adding the endpoint route to the private subnet's route table directs S3 traffic to the endpoint instead of the NAT Gateway, eliminating NAT data processing charges and internet routing.
- C is incorrect. A NAT Instance is a self-managed alternative to NAT Gateway that still processes data and routes it over the internet. It does not keep S3 traffic within the AWS network and requires OS patching and HA configuration.
- D is incorrect. S3 Transfer Acceleration routes uploads through CloudFront edge locations over the internet, improving throughput for geographically distant clients. It does not prevent traffic from traversing the internet and does not provide private network access.

---

### Question 12 (5 points)

A company uses AWS Direct Connect with a 1 Gbps dedicated connection to connect its on-premises data center to AWS. They need to ensure that if the Direct Connect connection fails, applications can continue accessing AWS using an encrypted backup path. Which architecture provides this resilience?

A. Add a second Direct Connect connection from a different Direct Connect location

B. Configure an AWS Site-to-Site VPN as a backup to the Direct Connect connection, with BGP routing that prefers Direct Connect

C. Enable Direct Connect resiliency mode in the AWS console to automatically create a backup path

D. Use AWS Global Accelerator as a failover path for Direct Connect traffic

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. A second Direct Connect connection provides redundancy against single-connection failures, but if both connections use the same Direct Connect location, a facility outage could take both down. Additionally, a second Direct Connect connection takes weeks to provision and may not be cost-justified as a backup.
- B is correct. An AWS Site-to-Site VPN uses the public internet with IPSec encryption, providing an always-available backup path even when Direct Connect is down. BGP route preferences (lower MED/higher LOCAL_PREF for Direct Connect) ensure Direct Connect is preferred when available, with automatic failover to VPN. This is the AWS-recommended pattern for Direct Connect failover.
- C is incorrect. There is no "Direct Connect resiliency mode" that automatically creates a backup path. Direct Connect resiliency is achieved through redundant connections, not a console toggle.
- D is incorrect. AWS Global Accelerator is a networking service that routes application traffic over the AWS global backbone to the nearest healthy endpoint. It is designed for global application traffic optimization, not for Direct Connect failover.

---

### Question 13 (5 points)

A company has a production VPC (10.0.0.0/16) and a development VPC (10.0.0.0/16) in the same Region. A developer wants to establish VPC Peering between them. What is the issue?

A. VPC Peering is not supported between VPCs in the same Region

B. VPC Peering cannot be established between VPCs with overlapping CIDR blocks

C. Both VPCs must have an Internet Gateway attached to support VPC Peering

D. VPC Peering requires both VPCs to use the same route table

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. VPC Peering is fully supported between VPCs in the same Region (same-Region peering) and between VPCs in different Regions (inter-region peering), and even between different AWS accounts.
- B is correct. VPC Peering requires non-overlapping CIDR blocks. Both VPCs use 10.0.0.0/16, which is identical — the routing would be ambiguous. When VPCs have overlapping CIDRs, AWS rejects the peering connection. The solution is to re-CIDR one of the VPCs before establishing peering.
- C is incorrect. Internet Gateways are not required for VPC Peering. Peering enables private communication between VPCs using their private IP addresses. Internet Gateways are for public internet connectivity.
- D is incorrect. Each VPC manages its own route tables independently. VPC Peering does not require shared route tables — each VPC adds a route pointing to the peering connection for the peer VPC's CIDR.

---

### Question 14 (5 points)

An architect is designing a hub-and-spoke network topology connecting a central security VPC (hub) with 50 spoke VPCs across multiple AWS accounts. All inter-spoke traffic must be inspected by firewall appliances in the hub VPC. Which networking service enables this topology at scale?

A. VPC Peering between each spoke and the hub, with VPC Peering between all spokes

B. AWS Transit Gateway with a centralized inspection routing architecture using Gateway Load Balancer

C. AWS PrivateLink endpoints in every spoke VPC pointing to the hub

D. VPN connections from each spoke VPC to the hub using Virtual Private Gateway

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. With 50 spokes, peering requires 50 connections to the hub plus 1,225 connections between all spokes (50×49/2) for full mesh — operationally unmanageable. VPC Peering is also non-transitive, so inter-spoke inspection through the hub is not achievable with peering alone.
- B is correct. AWS Transit Gateway connects up to 5,000 VPCs and on-premises networks through a single managed hub, supporting centralized routing and inspection architectures. With Gateway Load Balancer and Transit Gateway together, all inter-VPC traffic can be directed through firewall appliances in the inspection VPC. This is the AWS-recommended architecture for enterprise hub-and-spoke with centralized security.
- C is incorrect. AWS PrivateLink creates Interface Endpoints that expose specific services from a provider VPC to consumer VPCs. It is designed for service-to-service connectivity, not for a general-purpose hub-and-spoke network topology with centralized inspection.
- D is incorrect. VPN connections from 50 spoke VPCs to a hub are operationally complex and limited by Virtual Private Gateway bandwidth. Transit Gateway supports higher aggregate bandwidth and simpler management for large-scale hub-and-spoke deployments.

---

### Question 15 (5 points)

An EC2 instance in a private subnet in a VPC is experiencing intermittent connectivity failures to an external API endpoint. VPC Flow Logs are enabled. What steps allow the architect to determine whether the failure is a network-level block (REJECT) or if the traffic is leaving the VPC but failing beyond the VPC boundary?

A. Check CloudTrail for API call failures from the EC2 instance

B. Query VPC Flow Logs for the instance's ENI, filtering for records with the destination IP and Action=REJECT; if ACCEPT appears, the failure is outside the VPC boundary

C. Run ping from the instance to the external IP and check the response time

D. Check the EC2 Instance Console Output for network error messages

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. CloudTrail logs AWS API calls made by IAM principals. It does not capture TCP/IP network traffic between an EC2 instance and an external API endpoint. External HTTP failures would not appear in CloudTrail.
- B is correct. VPC Flow Logs record individual network flows with an Action field that is either ACCEPT or REJECT. If logs show Action=REJECT for the destination IP, the traffic is being blocked within the VPC (by a security group or NACL). If logs show Action=ACCEPT, the traffic is leaving the VPC successfully, and the failure is at the external endpoint or at an intermediate network layer outside the VPC.
- C is incorrect. ICMP ping may be blocked by the remote API endpoint's firewall even when HTTP/HTTPS is working. Ping response is not a reliable indicator of HTTP connectivity, and no ping to a production API endpoint should be used in isolation for network troubleshooting.
- D is incorrect. EC2 Instance Console Output captures the OS boot log and kernel messages. Application-level network failures to external endpoints would not normally appear in the console output unless the OS itself is logging them.

---

### Question 16 (5 points)

A company wants to restrict all outbound internet access from EC2 instances in private subnets, except to a list of approved HTTPS endpoints. Which solution implements this with the LEAST operational overhead?

A. Use a Network ACL with explicit Deny rules for all IP ranges except the approved endpoints

B. Deploy an AWS Network Firewall with domain-based filtering rules that allow only approved HTTPS domains

C. Create security group outbound rules allowing HTTPS only to the specific IP ranges of each approved endpoint

D. Deploy a third-party proxy on EC2 instances with an allow-list of approved URLs

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. NACL rules are IP-based only — you cannot filter by domain name. Cloud services like SaaS APIs often use dynamic IP addresses that change without notice. Maintaining a NACL with approved IP ranges requires ongoing updates every time endpoint IPs change.
- B is correct. AWS Network Firewall supports stateful domain-based filtering rules. An allow rule for specific FQDN patterns (e.g., `*.example.com`) matches any IP that those domains resolve to, without requiring IP address maintenance. Network Firewall is a managed service requiring no EC2 instances to operate.
- C is incorrect. Security group rules are also IP-based. For cloud APIs with dynamic or CDN-distributed IPs, maintaining accurate IP-based security group rules requires constant updates. This has high operational overhead for approved endpoint lists.
- D is incorrect. A proxy running on EC2 instances requires patching, scaling, high-availability configuration, and ongoing maintenance. This has the highest operational overhead of all options.

---

### Question 17 (5 points)

A company uses a VPN connection between their on-premises network (192.168.0.0/16) and their AWS VPC (10.0.0.0/16). The on-premises network can reach the VPC, but EC2 instances in the VPC cannot initiate connections to on-premises servers. What is the most likely cause?

A. VPN connections are unidirectional — traffic can only flow from on-premises to AWS, not the reverse

B. The VPC route table for the private subnets does not have a route for 192.168.0.0/16 pointing to the Virtual Private Gateway

C. The on-premises firewall is blocking inbound VPN traffic on port 4500

D. The EC2 instances need Elastic IP addresses to route traffic through the VPN

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. AWS Site-to-Site VPN connections are bidirectional. Traffic can flow in both directions once the VPN tunnel is established and routing is configured on both sides.
- B is correct. For EC2 instances to route traffic to on-premises networks, the VPC route table for the instances' subnets must have an entry for the on-premises CIDR (192.168.0.0/16) with the Virtual Private Gateway as the target. Without this route, packets destined for 192.168.0.0/16 addresses have no path and are dropped.
- C is incorrect. If the on-premises firewall were blocking VPN traffic on port 4500 (IPSec NAT-T), the VPN tunnel itself would not be established and neither direction would work. The question states on-premises can reach the VPC, implying the tunnel is up.
- D is incorrect. VPN traffic uses private IP addresses — it routes through the VPN tunnel, not through the Internet Gateway. Elastic IPs are for direct internet connectivity and are not required for or involved in VPN routing.

---

### Question 18 (5 points)

A company's application sends events to an Amazon SQS queue. The consuming Lambda function processes one message at a time. During peak hours, the queue depth grows to 100,000 messages and messages take 4 hours to process. The business requires processing to complete within 30 minutes. Which solution resolves this?

A. Increase the SQS visibility timeout to 4 hours to prevent message redelivery during processing

B. Increase the Lambda concurrency limit and configure Lambda event source mapping to process larger batches from the queue

C. Switch from SQS Standard to SQS FIFO queue to improve processing throughput

D. Enable SQS long polling to reduce the time between message arrivals to Lambda

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Increasing the visibility timeout prevents duplicate processing of in-flight messages, but it does not increase throughput. Messages are still processed one at a time.
- B is correct. The bottleneck is throughput — 100,000 messages cannot be processed in 30 minutes at a rate of one-at-a-time. Increasing Lambda concurrency allows multiple Lambda invocations to process messages in parallel. Increasing the batch size in the event source mapping allows each Lambda invocation to process multiple messages simultaneously. Together, these changes scale the consumer to match the queue depth.
- C is incorrect. SQS FIFO queues provide ordering and exactly-once processing guarantees, but they do not improve throughput for high-volume scenarios — FIFO queues actually have lower throughput limits per message group than Standard queues.
- D is incorrect. Long polling reduces the number of empty ReceiveMessage API calls and the latency between message arrival and Lambda invocation. It improves efficiency but does not directly increase the number of messages processed per second.

---

### Question 19 (5 points)

An architect is designing an event-driven architecture. Multiple downstream services (notifications, inventory, analytics) must receive a copy of every order event published by the order service. If any downstream service is temporarily unavailable, its events must not be lost. Which architecture is MOST resilient?

A. The order service publishes directly to each downstream service's API endpoint

B. The order service publishes to an SNS topic; each downstream service has its own SQS queue subscribed to the topic

C. The order service publishes to a single SQS queue that all downstream services poll

D. The order service stores events in DynamoDB and each downstream service queries for new items on a polling schedule

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Direct API calls from the order service to each downstream service creates tight coupling. If any downstream service is unavailable during the API call, the order service must handle the failure and retry — potentially blocking order processing. This is the synchronous, tightly-coupled anti-pattern.
- B is correct. This is the SNS fan-out with SQS buffering pattern. SNS delivers the event to all subscribed SQS queues simultaneously. If a downstream service is unavailable, its SQS queue retains the message (up to 14 days) until the service resumes and processes it. Each service's queue is independent — one service's slowness does not affect others.
- C is incorrect. A single SQS queue shared by all consumers creates competing consumers — each message is delivered to only one consumer (whichever polls first). This does not fan out the event to all three services.
- D is incorrect. Polling DynamoDB for new records introduces latency between event publication and processing. It also requires each service to maintain state about the last processed record and handle concurrent polling coordination. This is complex and brittle compared to the SNS/SQS pattern.

---

### Question 20 (5 points)

An application in AWS VPC needs to communicate with on-premises Microsoft Active Directory servers. The on-premises network is connected to the VPC via AWS Direct Connect. The AD servers are at 192.168.10.5 and 192.168.10.6. DNS queries for the corporate domain (corp.example.com) must resolve to on-premises AD servers. Which Route 53 configuration enables this?

A. Create a public hosted zone for corp.example.com with A records pointing to the on-premises AD servers' IP addresses

B. Create a Route 53 Resolver Outbound Endpoint and a Resolver rule forwarding corp.example.com queries to 192.168.10.5 and 192.168.10.6

C. Create a Route 53 Resolver Inbound Endpoint to receive DNS queries from on-premises and forward them to the VPC

D. Enable Route 53 Resolver DNS Firewall to block external DNS queries and allow only corporate domain resolution

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. A public hosted zone for corp.example.com would make internal corporate AD DNS records publicly visible on the internet. This is a security risk and not the correct mechanism for hybrid DNS resolution from within a VPC.
- B is correct. Route 53 Resolver Outbound Endpoints allow DNS queries from EC2 instances in the VPC to be forwarded to on-premises DNS servers. The Resolver rule specifies that queries for `corp.example.com` are forwarded to the specified IP addresses (192.168.10.5 and 192.168.10.6) via the Direct Connect connection. This enables VPC resources to resolve on-premises hostnames.
- C is incorrect. Route 53 Resolver Inbound Endpoints allow on-premises systems to query Route 53 for private hosted zone records in the VPC. This is the reverse direction — enabling on-premises-to-VPC DNS resolution, not VPC-to-on-premises DNS resolution.
- D is incorrect. Route 53 Resolver DNS Firewall blocks DNS queries to specific domains for security filtering (blocking malware domains, etc.). It does not forward DNS queries to on-premises DNS servers.

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
