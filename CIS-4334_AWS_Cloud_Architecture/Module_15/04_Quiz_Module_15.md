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

---

### Question 11 (5 points)

A company is migrating a large Oracle database to Amazon Aurora PostgreSQL. The schema uses Oracle-specific PL/SQL stored procedures and data types that are not compatible with PostgreSQL. Which AWS tool converts the schema and code automatically before migration?

A. AWS Database Migration Service (DMS) with Full Load mode

B. AWS Schema Conversion Tool (SCT) followed by DMS for ongoing replication

C. AWS DataSync with Oracle agent configuration

D. AWS Snowball Edge with the Oracle database export feature

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. DMS handles data migration (rows) but does not convert schemas or stored procedures. Oracle-specific PL/SQL code cannot be migrated to Aurora PostgreSQL by DMS alone — schema conversion must happen first.
- B is correct. AWS SCT analyzes the Oracle schema and automatically converts compatible objects (tables, views, indexes) to PostgreSQL syntax and flags objects (PL/SQL procedures, Oracle-specific functions) that require manual review. After SCT converts the schema, DMS migrates the data with ongoing replication to minimize downtime during cutover.
- C is incorrect. AWS DataSync is a file transfer service that moves data between on-premises file storage and AWS storage services (S3, EFS, FSx). It does not handle database schema conversion or relational data migration.
- D is incorrect. Snowball Edge is a physical data transport device for large-scale offline data transfer. It is used when network bandwidth is insufficient to transfer data online — it does not perform schema conversion.

---

### Question 12 (5 points)

A company has a Direct Connect connection to AWS but wants to ensure encrypted connectivity for sensitive financial data traveling between on-premises and their VPC. Direct Connect does not encrypt traffic by default. What is the MOST cost-effective solution that adds encryption without replacing the Direct Connect connection?

A. Replace the Direct Connect connection with an IPsec Site-to-Site VPN

B. Configure MACsec encryption on the Direct Connect connection (requires a dedicated connection)

C. Establish a Site-to-Site VPN over the existing Direct Connect connection using a Private Virtual Interface and a Virtual Private Gateway

D. Enable TLS on all application traffic — transport-layer encryption eliminates the need for network-layer encryption

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Replacing Direct Connect with a VPN loses the dedicated bandwidth, consistent latency, and higher throughput that Direct Connect provides. It is not the most cost-effective solution when Direct Connect is already in place.
- B is incorrect. MACsec provides Layer 2 encryption on Direct Connect but requires a dedicated Direct Connect connection (not a hosted connection) and supported hardware at the customer premises. It is not universally available and adds cost and hardware requirements.
- C is correct. Running an IPsec VPN tunnel over a Direct Connect Private VIF combines Direct Connect's reliable dedicated bandwidth with VPN's encryption. The VPN tunnel uses the Direct Connect path rather than the public internet, providing both performance and encryption at minimal additional cost.
- D is incorrect. TLS encrypts application-layer traffic between specific endpoints, but it does not encrypt all traffic at the network level. Non-TLS protocols, management traffic, and database replication streams may traverse the connection unencrypted. Network-layer encryption provides defense in depth that application-layer TLS alone cannot.

---

### Question 13 (5 points)

A company completed a Rehost migration of 200 servers to EC2 using AWS Application Migration Service (MGN). Six months later, the cloud team is asked to reduce costs and improve performance. Which migration strategy should they apply next?

A. Retire — decommission servers that are no longer needed after the rehost

B. Replatform — move databases from EC2 to RDS and application servers to Elastic Beanstalk without changing core logic

C. Repurchase — replace the existing applications with SaaS alternatives

D. Retain — keep the applications running as-is on EC2 indefinitely

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Retiring applies to servers that are no longer needed — this is appropriate for some servers post-migration but does not improve performance or reduce costs for the servers that must remain.
- B is correct. Replatforming is the logical next step after Rehost. Moving databases from self-managed EC2 to RDS eliminates patching, backup management, and Multi-AZ complexity. Moving application tiers to managed services reduces operational overhead and often reduces cost compared to always-on EC2 instances. Core application logic remains unchanged.
- C is incorrect. Repurchase (replace with SaaS) is appropriate when a commercial off-the-shelf SaaS application can replace a custom-built workload. It requires vendor evaluation, data migration, and user retraining — a much larger effort than replatforming.
- D is incorrect. Retaining applications as-is on EC2 after a Rehost provides no cost reduction or performance improvement beyond the initial lift-and-shift. It is appropriate only for applications that cannot be changed for technical or compliance reasons.

---

### Question 14 (5 points)

A company's on-premises DNS server resolves `app.internal.corp` for on-premises clients. After migrating the application to AWS, EC2 instances in a VPC also need to resolve `app.internal.corp` using the same on-premises DNS server. What must be configured in AWS?

A. A Route 53 private hosted zone for `internal.corp` with an A record pointing to the EC2 instance

B. A Route 53 Resolver Outbound Endpoint with a forwarding rule that routes queries for `internal.corp` to the on-premises DNS server IP

C. A Route 53 Resolver Inbound Endpoint with a forwarding rule that routes queries from on-premises to Route 53

D. A DHCP Option Set on the VPC pointing the DNS server to the on-premises DNS server IP

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Creating a Route 53 private hosted zone duplicates DNS records in AWS but does not leverage the authoritative on-premises DNS server. Any changes on-premises would require manual updates in Route 53, creating a synchronization problem.
- B is correct. A Route 53 Resolver Outbound Endpoint provides Route 53 Resolver with ENIs in the VPC. A forwarding rule directs DNS queries for `internal.corp` from VPC resources to the specified on-premises DNS server IP. This allows EC2 instances to resolve on-premises domain names through the existing authoritative DNS server.
- C is incorrect. Inbound Endpoints accept DNS queries from on-premises clients directed at AWS private hosted zones — they solve the opposite problem (on-premises resolving AWS names), not VPC instances resolving on-premises names.
- D is incorrect. Setting the VPC DHCP Option Set DNS server to the on-premises IP would route all DNS queries (including AWS internal names like EC2 instance hostnames and S3 endpoints) to the on-premises DNS server. This breaks AWS service discovery and is not recommended.

---

### Question 15 (5 points)

A financial services company must keep all primary data processing within their on-premises data center due to regulatory requirements, but wants to burst compute capacity to AWS during month-end processing peaks. Which hybrid architecture pattern enables this?

A. AWS Storage Gateway File Gateway — cache on-premises files and process them in S3

B. AWS Outposts — deploy AWS infrastructure in the on-premises data center for consistent hybrid compute

C. VMware Cloud on AWS — migrate on-premises VMs to AWS-hosted VMware infrastructure

D. AWS Wavelength — deploy compute at carrier network edges close to the data center

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Storage Gateway File Gateway provides cloud-backed file storage for on-premises applications — it enables access to S3 from on-premises but does not provide compute burst capacity and moves data to AWS storage, potentially violating the data residency requirement.
- B is correct. AWS Outposts deploys genuine AWS infrastructure (servers, networking) physically inside the on-premises data center. Applications running on Outposts use AWS APIs and services but data never leaves the premises. During peaks, workloads can seamlessly burst to AWS Region capacity using the same APIs, fulfilling the regulatory residency requirement while enabling elastic scale.
- C is incorrect. VMware Cloud on AWS migrates VMs to AWS-hosted VMware infrastructure — the compute runs in an AWS Region, not on-premises. This does not satisfy the requirement to keep primary data processing within the on-premises data center.
- D is incorrect. AWS Wavelength deploys compute at telecom carrier network edges (5G) to reduce latency for mobile and edge applications. It is not designed for on-premises data center compute bursting or regulatory data residency scenarios.

---

### Question 16 (5 points)

A company uses AWS DataSync to migrate 500 TB from an on-premises NAS to Amazon S3. Their internet connection is 1 Gbps. The migration must complete within 10 days. Is DataSync over the existing internet connection feasible?

A. Yes — DataSync saturates a 1 Gbps connection and can transfer approximately 10.8 TB per day, completing the migration in under 50 days

B. No — 500 TB over 1 Gbps takes approximately 46 days at maximum theoretical throughput; AWS Snowball Edge should be used instead

C. Yes — DataSync compresses data before transfer and can achieve 10x compression, effectively transferring 500 TB in under 5 days

D. No — DataSync cannot transfer more than 100 TB in a single task; multiple tasks would be required

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The calculation is accurate (1 Gbps = 10.8 TB/day theoretical maximum at 100% utilization), but the conclusion is wrong. At 10.8 TB/day, 500 TB takes approximately 46 days — far exceeding the 10-day requirement.
- B is correct. At 1 Gbps theoretical maximum (never achieved in practice due to protocol overhead, latency, and competing traffic), transferring 500 TB takes approximately 46 days. AWS Snowball Edge devices can transfer 80 TB each — 7 devices would complete the physical transfer within the 10-day window, with DataSync handling the final delta sync.
- C is incorrect. DataSync does not apply general-purpose compression to all data. Compression ratios vary by data type and are not a reliable planning assumption. Binary files, encrypted data, and already-compressed formats achieve little to no compression.
- D is incorrect. DataSync tasks do not have a 100 TB limit. A single DataSync task can transfer petabyte-scale datasets. Multiple tasks can be used for parallelism, but the limitation here is network bandwidth, not DataSync task size.

---

### Question 17 (5 points)

A company runs a Transit Gateway in `us-east-1` with 10 VPCs attached. They want VPCs in `eu-west-1` to communicate with the `us-east-1` VPCs without routing through the public internet. What is the correct solution?

A. Create VPC peering connections between each `eu-west-1` VPC and each `us-east-1` VPC

B. Deploy a Transit Gateway in `eu-west-1`, attach the `eu-west-1` VPCs, and create a Transit Gateway inter-region peering connection between the two Transit Gateways

C. Configure a Direct Connect connection between the two regions

D. Use AWS Global Accelerator to route traffic between the VPCs across regions

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Creating individual VPC peering connections between every `eu-west-1` VPC and every `us-east-1` VPC creates a mesh that scales as O(n×m) — in this case up to 10 × (number of eu-west-1 VPCs) peering connections. VPC peering does not support transitive routing, so each pair requires its own connection.
- B is correct. Transit Gateway inter-region peering connects two Transit Gateways across regions over the AWS global backbone network (not the public internet). All VPCs attached to each TGW can reach each other through the peered TGWs with a single inter-region peering connection, providing scalable transitive routing across regions.
- C is incorrect. Direct Connect connects on-premises data centers to AWS regions — it does not connect AWS regions to each other. Inter-region connectivity between VPCs uses the AWS backbone, not Direct Connect.
- D is incorrect. AWS Global Accelerator routes end-user traffic to optimal AWS endpoints over the AWS global network to improve application performance. It is not designed for private VPC-to-VPC inter-region routing.

---

### Question 18 (5 points)

A company's application requires sub-millisecond latency to a large on-premises data store that cannot be migrated to AWS. The application logic must run in AWS to use managed services. Which AWS feature minimizes latency between the AWS compute and the on-premises data store?

A. AWS Direct Connect with a 10 Gbps dedicated connection

B. Amazon ElastiCache deployed in the same VPC as the application to cache on-premises data locally

C. AWS Outposts deployed in the same on-premises facility as the data store, running the application compute on AWS infrastructure co-located with the data

D. AWS Local Zones deployed in the nearest city to the on-premises facility

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Direct Connect provides dedicated, consistent bandwidth between on-premises and AWS regions, reducing latency compared to internet VPN. However, even a 10 Gbps Direct Connect connection has 1–10ms latency depending on physical distance — insufficient for sub-millisecond requirements.
- B is incorrect. ElastiCache caches data locally in the VPC, which would serve cache hits at low latency — but cache misses still require round-trips to the on-premises data store over the network. For workloads requiring consistent sub-millisecond access to the full dataset, caching does not solve the problem.
- C is correct. AWS Outposts places AWS compute infrastructure physically inside the on-premises facility, co-located with the data store. Traffic between Outposts compute and the on-premises data store travels over the local data center network at sub-millisecond speeds, while the application still uses AWS managed services APIs.
- D is incorrect. AWS Local Zones extend AWS compute closer to specific metropolitan areas to reduce latency for end users. They do not deploy inside a specific on-premises facility and still have network hops between the Local Zone and any on-premises data store.

---

### Question 19 (5 points)

A company uses AWS VPN CloudHub. They have a central VGW in `us-east-1` with three Customer Gateways configured — one at their New York office, one in London, and one in Tokyo. Which traffic flows are supported by this architecture?

A. New York → AWS VPC only; office-to-office traffic is not supported by VPN CloudHub

B. New York → AWS VPC, and New York → London → Tokyo hub-and-spoke traffic through the VGW

C. New York → London directly, bypassing the VGW for lower latency

D. The architecture is invalid — a VGW can only have one Customer Gateway attached at a time

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. VPN CloudHub specifically enables site-to-site traffic between Customer Gateways through the central VGW — this is the defining feature of CloudHub that distinguishes it from a standard VPN connection.
- B is correct. VPN CloudHub allows each Customer Gateway to communicate with the VPC and with each other through the hub VGW. New York, London, and Tokyo offices can all reach the AWS VPC and exchange traffic with each other by routing through the VGW in `us-east-1`. This hub-and-spoke model is the core CloudHub architecture.
- C is incorrect. Traffic between Customer Gateways in CloudHub always transits through the VGW — there is no direct Customer Gateway-to-Customer Gateway path that bypasses the hub.
- D is incorrect. A VGW supports multiple Customer Gateway connections simultaneously — this is fundamental to both standard multi-site VPN configurations and VPN CloudHub. There is no single-CGW limit on a VGW.

---

### Question 20 (5 points)

A company is performing a migration assessment using the 7 Rs framework. They have identified a legacy monolithic application with tightly coupled components that would significantly benefit from being decomposed into microservices. Business leadership wants maximum long-term cloud benefit and is willing to invest significant development effort. Which strategy applies?

A. Rehost — migrate the monolith as-is to EC2

B. Replatform — move the monolith to Elastic Beanstalk without changing the architecture

C. Refactor (Re-architect) — redesign the application as microservices using Lambda, ECS, and API Gateway

D. Retain — keep the monolith on-premises until a full rewrite is complete

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Rehosting (lift-and-shift) moves the monolith to EC2 unchanged. It achieves the fastest migration with the least effort but provides no architectural improvement and does not decompose the tightly coupled components. It does not deliver maximum long-term cloud benefit.
- B is incorrect. Replatforming moves to a managed platform (Elastic Beanstalk) with minor optimizations but does not redesign the architecture. The monolith remains tightly coupled — the core architectural problem is unaddressed.
- C is correct. Refactoring (Re-architecting) is the highest-effort, highest-reward strategy. Decomposing a monolith into microservices using Lambda (serverless functions), ECS (containers), and API Gateway (managed routing) provides independent scaling, fault isolation, faster deployment cycles, and optimized cloud cost per service. This is the strategy when maximum long-term benefit justifies the development investment.
- D is incorrect. Retaining on-premises delays cloud benefits entirely and provides no value during the retention period. Retaining is appropriate for applications with hard regulatory or technical constraints, not for applications where leadership is actively willing to invest in modernization.

---
