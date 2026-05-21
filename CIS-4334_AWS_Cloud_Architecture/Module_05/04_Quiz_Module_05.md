# Quiz: Module 05 - VPC – Subnets, Route Tables, Security Groups, NACLs
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
What VPC component is required to enable two-way communication between resources in a public subnet and the public internet?
*   A) NAT Gateway
*   B) Internet Gateway (IGW)
*   C) VPC Peering Connection
*   D) AWS Direct Connect Gateway
*   **Correct Answer:** B) An Internet Gateway attached to the VPC and referenced in the subnet's route table enables bidirectional communication between public subnet resources and the internet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A NAT Gateway allows private subnet resources to make outbound-only connections to the internet. It does not permit inbound connections from the internet, making it inappropriate for resources that need to be publicly reachable.
    *   *Why B is correct:* The Internet Gateway is the gateway that makes a subnet "public." It allows bidirectional internet traffic when combined with a route table entry pointing 0.0.0.0/0 → IGW and a public IP assigned to the instance.
    *   *Why C is incorrect:* VPC Peering connects two VPCs together for private routing between them. It has no role in connecting a VPC to the public internet.
    *   *Why D is incorrect:* AWS Direct Connect establishes a dedicated private network connection between an on-premises data center and AWS. It is a hybrid connectivity solution, not a public internet gateway.

---

**Question 2**
Which of the following is the most accurate description of the difference between a **Security Group** and a **Network ACL (NACL)** in AWS VPC?
*   A) Security Groups are applied at the subnet level and are stateless; NACLs are applied at the instance level and are stateful.
*   B) Security Groups are stateful instance-level firewalls that automatically allow return traffic; NACLs are stateless subnet-level firewalls that require explicit rules for both inbound and outbound traffic, including deny rules.
*   C) Security Groups and NACLs are identical in function but differ only in where they are configured in the AWS Console.
*   D) Security Groups support both Allow and Deny rules; NACLs only support Allow rules.
*   **Correct Answer:** B) Security Groups are stateful (return traffic automatically allowed) and operate at the instance level; NACLs are stateless (both directions require explicit rules) and operate at the subnet level, supporting both Allow and Deny.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the definitions. Security Groups are instance-level and stateful; NACLs are subnet-level and stateless.
    *   *Why B is correct:* This is a high-frequency SAA-C03 exam distinction. Stateful (SG) vs. stateless (NACL) is critical for troubleshooting questions. NACLs require return traffic rules (including ephemeral ports 1024–65535) because they do not track connection state. Only NACLs can explicitly deny specific IP addresses.
    *   *Why C is incorrect:* Security Groups and NACLs have fundamentally different behavior (stateful vs. stateless, instance vs. subnet scope, allow-only vs. allow+deny) that directly affects network connectivity.
    *   *Why D is incorrect:* This is the reverse of the actual behavior. Security Groups are allow-only (you cannot write an explicit Deny rule). NACLs support both Allow and Deny rules evaluated in numeric order.

---

**Question 3**
A solutions architect needs to ensure that EC2 instances in a private subnet can download software updates from the internet but cannot be directly accessed from the internet. Which component provides this capability?
*   A) Attach an Internet Gateway to the private subnet's route table pointing 0.0.0.0/0 → IGW.
*   B) Place a NAT Gateway in the public subnet and add a route in the private subnet route table pointing 0.0.0.0/0 → NAT Gateway.
*   C) Enable VPC Flow Logs and configure a CloudWatch alarm to block inbound traffic automatically.
*   D) Create a VPC Endpoint for the software repository to allow private connectivity without internet access.
*   **Correct Answer:** B) A NAT Gateway in the public subnet provides outbound-only internet access for private subnet resources while blocking all unsolicited inbound connections from the internet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Adding an IGW route to a private subnet makes it a public subnet. Resources would then be reachable from the internet (if they have public IPs), which violates the "cannot be directly accessed" requirement.
    *   *Why B is correct:* This is the canonical private subnet internet access pattern. The NAT Gateway translates outbound requests using its own Elastic IP, allowing private instances to reach the internet. Return traffic is allowed because NAT tracks the connection state. New inbound connections from the internet cannot initiate because the private instances have no public IP and the NAT Gateway does not forward unsolicited inbound traffic.
    *   *Why C is incorrect:* VPC Flow Logs capture network traffic metadata for analysis but cannot actively block traffic. Flow Logs combined with CloudWatch alarms can trigger notifications or Lambda functions, but this is not a native traffic-blocking mechanism.
    *   *Why D is incorrect:* VPC Endpoints provide private connectivity to specific AWS services (e.g., S3, DynamoDB) without internet traversal. They are appropriate for AWS service access but cannot provide general internet connectivity for arbitrary software repositories.

---

**Question 4**
A security team wants to block all traffic from a specific external IP address (203.0.113.50) from reaching any resource in a VPC subnet. Which VPC component can enforce this deny rule?
*   A) Security Group — add an inbound deny rule for source 203.0.113.50/32.
*   B) Network ACL — add a numbered inbound Deny rule for source 203.0.113.50/32 with a lower rule number than the Allow rules.
*   C) IAM policy — add a Deny condition for requests originating from 203.0.113.50.
*   D) VPC Route Table — add a route for 203.0.113.50/32 with a target of "blackhole."
*   **Correct Answer:** B) Network ACLs support explicit Deny rules and are evaluated in rule number order; adding an inbound Deny rule with a lower number than existing Allow rules blocks traffic from that IP before it reaches any instance in the subnet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Security Groups are allow-only. There is no mechanism to add an explicit Deny rule to a Security Group. You can only remove Allow rules, which then results in an implicit Deny — but you cannot target a specific source IP for an explicit Deny.
    *   *Why B is correct:* NACLs are the only standard VPC component that supports explicit Deny rules for specific IP addresses. Rules are evaluated in ascending numeric order; the first matching rule applies. Adding a low-numbered Deny rule for 203.0.113.50/32 before higher-numbered Allow rules blocks that IP entirely.
    *   *Why C is incorrect:* IAM policies control API-level access to AWS services, not network-level traffic flowing into a VPC subnet. An IAM policy cannot block TCP/IP packets at the network layer.
    *   *Why D is incorrect:* Route table "blackhole" routes (pointing to a deleted gateway) prevent the VPC from routing traffic toward a destination. They are used to block traffic to destinations, not from sources. You cannot use a route table to block traffic from a specific source IP.

---

**Question 5**
A company is designing a three-tier web application on AWS. The web tier (load balancer) must be publicly accessible, the application tier (EC2 instances) must only receive traffic from the web tier, and the database tier (RDS) must only accept connections from the application tier. Which security configuration enforces this architecture with the principle of least privilege?
*   A) Place all three tiers in public subnets and use a single Security Group allowing all ports between all tiers.
*   B) Place the web tier in a public subnet and the application and database tiers in private subnets; configure Security Groups so each tier's SG only allows inbound traffic from the SG of the tier directly above it.
*   C) Place all three tiers in private subnets and use NACLs to control all inter-tier traffic based on IP ranges.
*   D) Place all three tiers in separate VPCs and use VPC Peering to connect them, with no Security Group restrictions.
*   **Correct Answer:** B) Public subnet for the web tier with Security Group chaining (referencing the upstream tier's SG as the inbound source) ensures each tier only accepts traffic from the intended upstream tier.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Placing all tiers in public subnets exposes the database and application servers directly to the internet. Allowing all ports between all tiers violates the principle of least privilege and creates a large attack surface.
    *   *Why B is correct:* This is the textbook AWS three-tier architecture pattern. SG chaining (specifying another SG as the source, not a CIDR) means the app tier SG only allows inbound from the load balancer's SG, and the DB SG only allows inbound from the app tier's SG. This is both least privilege and operationally clean — no IP management required.
    *   *Why C is incorrect:* NACLs work on CIDR ranges, not SG IDs, making them harder to maintain as instances scale. Placing the web tier in a private subnet makes it unreachable from the internet, which breaks the requirement for public accessibility.
    *   *Why D is incorrect:* Separate VPCs with peering adds architectural complexity without security benefit. VPC Peering without Security Group restrictions would be less secure than a properly designed single-VPC architecture. VPC Peering is also non-transitive, complicating three-tier connectivity.

