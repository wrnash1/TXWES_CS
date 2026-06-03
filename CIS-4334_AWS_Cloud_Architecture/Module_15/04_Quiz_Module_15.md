# Quiz: Module 15 — AWS Migration and Hybrid Architectures

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Answer key and distractor analysis follow each question.

---

## Question 1

A company wants to migrate 200 on-premises servers to AWS as quickly as possible with minimal changes. Applications must remain available during migration. Which AWS service BEST supports this requirement?

- A. AWS Database Migration Service (DMS)
- B. AWS Application Migration Service (MGN)
- C. AWS Server Migration Service (SMS)
- D. AWS VM Import/Export

### Q1 Answer: B

### Q1 Analysis

A is incorrect. DMS is designed for database migrations, not server workload migrations. It replicates database content, not entire server operating systems and applications.

B is correct. MGN performs continuous block-level replication of on-premises servers to AWS. Servers remain fully operational during replication. When ready, a cutover launches EC2 instances from the replicated data, typically with only 10–30 minutes of downtime. MGN replaced SMS as the recommended server migration service.

C is incorrect. SMS was the previous-generation service that MGN replaced. AWS recommends MGN for new migrations.

D is incorrect. VM Import/Export requires taking a snapshot of the VM, which causes downtime and requires a one-time bulk transfer — not continuous replication. It is not suited for large-scale migrations requiring minimal downtime.

---

## Question 2

A company needs to migrate a 5 TB Oracle database to Amazon Aurora PostgreSQL with minimal downtime. The database must remain available during migration and the schema must be converted. Which combination of AWS services accomplishes this?

- A. AWS Application Migration Service to replicate the Oracle server, then manually export/import data
- B. AWS Schema Conversion Tool (SCT) for schema conversion, then AWS DMS with CDC for data migration
- C. AWS Database Migration Service in full-load mode only, with a maintenance window for downtime
- D. AWS DataSync to synchronize Oracle data files to S3, then load into Aurora

### Q2 Answer: B

### Q2 Analysis

A is incorrect. MGN migrates entire servers, not databases at the schema and data level. It would create an EC2 instance running Oracle, not an Aurora PostgreSQL database.

B is correct. For a heterogeneous migration (Oracle to PostgreSQL), SCT converts the database schema, stored procedures, and functions. DMS with CDC mode then performs an initial full load and continuously replicates changes, keeping the source Oracle database operational. At cutover, applications are redirected to Aurora.

C is incorrect. Full-load mode requires taking the source database offline or accepting data loss during migration. The question requires minimal downtime, which demands CDC.

D is incorrect. AWS DataSync replicates files and objects between storage systems. Oracle database files are not directly importable into Aurora PostgreSQL — the schema and data must be properly migrated at the database level.

---

## Question 3

A financial services company requires a dedicated private network connection to AWS with consistent 10 Gbps throughput and compliance requirements prohibiting data from traversing the public internet. Which connectivity option satisfies BOTH requirements?

- A. AWS Site-to-Site VPN with two redundant tunnels
- B. AWS Direct Connect with a 10 Gbps dedicated connection
- C. AWS Direct Connect with a hosted connection from a partner
- D. AWS Client VPN with split-tunnel mode

### Q3 Answer: B

### Q3 Analysis

A is incorrect. Site-to-Site VPN transmits data over the public internet (encrypted via IPsec). The compliance requirement prohibits public internet transit regardless of encryption.

B is correct. Direct Connect 10 Gbps dedicated connection provides exactly 10 Gbps of dedicated private bandwidth. Traffic flows entirely through the AWS private network and the Direct Connect facility — never traversing the public internet. This satisfies both the throughput and compliance requirements.

C is incorrect. A hosted connection provides sub-10 Gbps to 10 Gbps options, but the question specifies 10 Gbps is required. A dedicated connection at exactly 10 Gbps is more appropriate for a stated 10 Gbps requirement.

D is incorrect. Client VPN provides user-to-VPC connectivity for remote users over the internet. It does not provide dedicated 10 Gbps bandwidth and does not satisfy the internet-transit prohibition.

---

## Question 4

A company has an AWS Direct Connect connection for primary connectivity to AWS. They want to ensure that if the Direct Connect connection fails, traffic automatically fails over to an encrypted alternative path. Which architecture provides automatic failover with encryption?

- A. A second Direct Connect connection from the same provider
- B. AWS Site-to-Site VPN configured on the same Virtual Private Gateway as the Direct Connect connection
- C. A Transit Gateway peering connection to a second region
- D. AWS CloudFront with origin failover configuration

### Q4 Answer: B

### Q4 Analysis

A is incorrect. A second Direct Connect connection from the same provider would fail if the provider has an outage. Additionally, Direct Connect itself does not provide internet-based failover — both connections share the same failure domain risk.

B is correct. Configuring a Site-to-Site VPN on the same VGW creates an automatic BGP failover. Direct Connect routes are preferred by BGP metric. If Direct Connect fails, BGP removes those routes and traffic automatically shifts to the VPN path. The VPN provides IPsec encryption, satisfying the encryption requirement.

C is incorrect. Transit Gateway peering provides inter-region VPC connectivity but does not create failover for an on-premises Direct Connect outage.

D is incorrect. CloudFront is a CDN for content delivery. It does not provide network-level failover between Direct Connect and VPN.

---

## Question 5

A company has 50 VPCs across three AWS regions and an on-premises data center connected via Direct Connect. They need all VPCs to communicate with each other and with on-premises. The networking team wants to minimize management overhead. Which architecture is MOST appropriate?

- A. Create VPC peering connections between every pair of VPCs (peering mesh)
- B. Deploy a Transit Gateway in each region with inter-region Transit Gateway peering and a Direct Connect Gateway
- C. Configure a single Virtual Private Gateway shared across all VPCs in all regions
- D. Use VPC sharing via AWS Resource Access Manager to combine all subnets into one VPC

### Q5 Answer: B

### Q5 Analysis

A is incorrect. 50 VPCs across 3 regions would require 50*(50-1)/2 = 1,225 VPC peering connections. This is unmanageable and VPC peering also does not support transitive routing — traffic cannot flow through a peering connection to reach a third VPC.

B is correct. One Transit Gateway per region with inter-region TGW peering provides full mesh connectivity with centralized routing management. A Direct Connect Gateway with a Transit VIF connects the on-premises Direct Connect circuit to all regions through the TGW. This scales to hundreds of VPCs with minimal management overhead.

C is incorrect. A VGW attaches to a single VPC. It cannot be shared across multiple VPCs. There is no concept of a shared VGW.

D is incorrect. VPC sharing via RAM shares subnets with other accounts within the same VPC — it does not enable routing between separate VPCs in multiple regions.

---

## Question 6

A company needs to resolve on-premises hostnames (e.g., `appserver01.corp.local`) from within an AWS VPC. The VPC and on-premises network are connected via Direct Connect. Which Route 53 Resolver configuration is required?

- A. Create a Public Hosted Zone for `corp.local` in Route 53
- B. Create an Outbound Endpoint and a Forward Rule sending `corp.local` queries to the on-premises DNS server
- C. Create an Inbound Endpoint and configure the on-premises DNS server to forward AWS queries to it
- D. Enable VPC DNS hostnames and DNS resolution settings on the VPC

### Q6 Answer: B

### Q6 Analysis

A is incorrect. Creating a public hosted zone for `corp.local` would make these names publicly resolvable on the internet — a security problem. It also would not forward to the actual on-premises DNS server.

B is correct. When VPC instances need to resolve on-premises hostnames, Route 53 Resolver uses an Outbound Endpoint to forward those queries to the on-premises DNS server. A Forward Rule specifies the domain (`corp.local`) and the target DNS server IP. The on-premises DNS server answers with the correct IP.

C is incorrect. An Inbound Endpoint solves the opposite problem — on-premises resolving AWS names. The question asks about AWS resolving on-premises names.

D is incorrect. VPC DNS settings enable DNS hostnames for EC2 instances and resolution of AWS-provided DNS names. They do not forward on-premises domain queries to external DNS servers.

---

## Question 7

A retail company is migrating its e-commerce application to AWS. The application is currently a Java monolith on-premises. Due to time constraints, the team must complete the migration in 3 weeks with no code changes. Six months later, they plan to redesign the application as microservices. Which migration strategies apply to each phase respectively?

- A. Phase 1: Replatform; Phase 2: Refactor
- B. Phase 1: Rehost; Phase 2: Refactor
- C. Phase 1: Repurchase; Phase 2: Replatform
- D. Phase 1: Retain; Phase 2: Rehost

### Q7 Answer: B

### Q7 Analysis

A is incorrect. Replatform involves making targeted improvements (e.g., moving to a managed service) — it is not "no code changes." The time constraint and no-code-change requirement rule out replatform for Phase 1.

B is correct. Rehost (lift-and-shift) moves the application to EC2 without code changes — achievable in a tight timeframe. Refactor (re-architect) redesigns the application as microservices on cloud-native services — appropriate for Phase 2 after the initial migration.

C is incorrect. Repurchase means switching to a SaaS product. The company is keeping their application, not replacing it with a commercial product.

D is incorrect. Retain means leaving the application on-premises. The question requires migrating in Phase 1.

---

## Question 8

A company uses AWS Outposts in its manufacturing facility because the production control systems require sub-5ms latency to AWS-managed compute. Internet connectivity at the facility is unreliable. What happens to running workloads on the Outpost if the connection to the AWS region is interrupted?

- A. All running instances are immediately terminated and must be restarted after connectivity is restored
- B. Running workloads continue to operate; new instance launches and API changes are unavailable until connectivity is restored
- C. The Outpost automatically fails over to a secondary Outpost in a nearby facility
- D. Running workloads pause and resume automatically when connectivity is restored with no data loss

### Q8 Answer: B

### Q8 Analysis

A is incorrect. Running instances are not terminated during a connectivity disruption. Terminating running instances would make Outposts useless for the stated low-latency manufacturing use case where connectivity is unreliable.

B is correct. The Outpost Service Link carries control-plane traffic (API calls, AMI management). When it is interrupted, existing running workloads continue operating normally. However, you cannot launch new instances, make API changes, or access the AWS console for the Outpost until connectivity is restored.

C is incorrect. Outposts does not have a built-in automatic failover to a secondary Outpost. High availability for Outposts workloads requires explicit application-level redundancy design.

D is incorrect. Running workloads do not pause — they continue. "Pause and resume" describes a different kind of behavior, such as EC2 hibernation, which is unrelated to Service Link interruption.

---

## Question 9

An organization wants to migrate its VMware vSphere on-premises infrastructure to AWS. The virtual machines run specialized legacy operating systems that cannot easily be re-engineered. The team wants to avoid re-installing operating systems and applications. Which migration strategy and service combination is MOST appropriate?

- A. Refactor using AWS Lambda and containers; rewrite all applications
- B. Rehost using AWS Application Migration Service to lift VMs to EC2
- C. Relocate using VMware Cloud on AWS; move VMs without changing the hypervisor
- D. Replatform using AWS Elastic Beanstalk; deploy application code directly

### Q9 Answer: C

### Q9 Analysis

A is incorrect. Refactoring legacy specialized OS applications is high-effort and may not be feasible for legacy systems. The question specifically states the team wants to avoid re-engineering.

B is incorrect. MGN can migrate VMs to EC2, but the OS and application stack must be compatible with AWS virtualization drivers. Specialized legacy OSes may require conversion work.

C is correct. Relocate (the 7th R) is specifically designed for VMware environments. VMware Cloud on AWS runs the same VMware software stack (vSphere, NSX, vSAN) on AWS-dedicated hardware. VMs move without OS reinstallation or application changes, and the same VMware management tools continue to work.

D is incorrect. Elastic Beanstalk deploys application code to managed compute environments. It does not migrate entire VMs or handle legacy OS-dependent applications.

---

## Question 10

A company needs to connect its on-premises network to 15 VPCs in a single AWS region. They also need encryption for all traffic between on-premises and AWS. Direct Connect is not in the budget. Which solution provides connectivity with encryption at the lowest cost?

- A. Create 15 separate Site-to-Site VPN connections, one per VPC
- B. Create a Transit Gateway, attach all 15 VPCs, configure a single Site-to-Site VPN to the Transit Gateway, and enable route propagation
- C. Create a Direct Connect hosted connection and use MACsec for encryption
- D. Use AWS PrivateLink endpoints in each VPC to accept on-premises traffic

### Q10 Answer: B

### Q10 Analysis

A is incorrect. Creating 15 separate VPN connections is costly (each has an hourly charge), operationally complex to manage, and requires 15 separate Customer Gateway configurations. Each VPN connection provides only one path — no transitive routing between VPCs.

B is correct. A single Transit Gateway VPN connection ($0.05/hour for the VPN + $0.02/GB attachment fee) connects all 15 VPCs through the TGW's routing. Site-to-Site VPN provides IPsec encryption by default. This is the most cost-effective and scalable solution.

C is incorrect. Direct Connect is explicitly excluded by the budget constraint. MACsec on Direct Connect would also not apply without the Direct Connect circuit.

D is incorrect. AWS PrivateLink exposes specific services from within a VPC to consumers over private network connectivity. It does not provide general network connectivity for an on-premises network to reach multiple VPCs.
