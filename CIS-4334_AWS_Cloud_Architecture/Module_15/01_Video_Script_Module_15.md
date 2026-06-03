# Video Script: Module 15 — AWS Migration and Hybrid Architectures

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Segment 1: Introduction to Migration and Hybrid

Welcome to Module 15. This module covers two interrelated topics tested on SAA-C03: migrating workloads to AWS and designing hybrid architectures that connect on-premises environments to AWS.

The two topics are often inseparable in practice. Most enterprise migrations are not lift-and-shift all at once — they take months or years, and during that transition period the on-premises environment and AWS must coexist and communicate reliably. Designing that coexistence is hybrid architecture.

For the SAA-C03 exam, the key services and patterns are:

- AWS Migration Hub — centralized migration tracking
- AWS Application Migration Service — lift-and-shift server replication
- AWS Database Migration Service — database migrations with minimal downtime
- AWS Direct Connect — dedicated private network connection to AWS
- AWS Site-to-Site VPN — encrypted tunnel over the internet
- AWS Transit Gateway — hub-and-spoke network architecture at scale
- AWS Outposts — AWS infrastructure in your data center
- Hybrid DNS patterns — resolving on-premises and AWS hostnames across the connection

---

## Segment 2: AWS Migration Strategies — The 7 Rs

Migration strategy selection is the foundation of any cloud migration project. AWS defines seven strategies:

**Retire** — decommission the application. No migration needed.

**Retain** — keep the application on-premises for now. May migrate later.

**Rehost** — "lift and shift." Move the application to EC2 without changes. Fastest migration path, minimal cloud optimization.

**Replatform** — "lift, tinker, and shift." Make minor optimizations — for example, migrate from self-managed MySQL on-premises to Amazon RDS MySQL. The application code does not change.

**Repurchase** — move to a different product, typically a SaaS solution. Example: replace on-premises CRM with Salesforce.

**Refactor / Re-architect** — redesign the application to take full advantage of cloud-native capabilities. Example: break a monolith into microservices on Lambda and DynamoDB. Highest ROI long-term, highest effort upfront.

**Relocate** — move VMware infrastructure to VMware Cloud on AWS without changing the hypervisor layer. Fastest for VMware-heavy environments.

For the exam: Rehost = fastest. Refactor = best long-term cloud optimization. Replatform = middle ground.

---

## Segment 3: AWS Application Migration Service

AWS Application Migration Service (MGN) replicates on-premises servers to AWS continuously using block-level replication. The replication agent is installed on source servers and continuously replicates data to AWS. When you are ready to cut over, you launch test or production instances from the replicated data.

Key features:

- Continuous block-level replication — minimizes downtime during cutover
- Supports any OS and application without changes (true lift-and-shift)
- Automatic conversion to AWS EC2 (converts BIOS/UEFI, storage drivers, network drivers)
- Test cutovers before committing to production
- Cutover window is typically 10–30 minutes

MGN replaced the older Server Migration Service (SMS) and is now the recommended service for server replication migrations.

---

## Segment 4: AWS Database Migration Service

AWS Database Migration Service (DMS) migrates databases with minimal downtime. The source database remains fully operational during migration. DMS continuously replicates changes from the source to the target using Change Data Capture (CDC).

**Supported source databases:** Oracle, SQL Server, MySQL, PostgreSQL, MariaDB, MongoDB, Amazon RDS, Amazon Aurora, SAP ASE, and more.

**Supported target databases:** Any of the above, plus Redshift, DynamoDB, Kinesis Data Streams, DocumentDB, and Elasticsearch.

**Homogeneous migrations** (e.g., MySQL → RDS MySQL) are straightforward — DMS handles the replication directly.

**Heterogeneous migrations** (e.g., Oracle → PostgreSQL) require the AWS Schema Conversion Tool (SCT) to convert the schema and stored procedures before DMS replicates the data.

**DMS Replication Instance** — a managed EC2 instance that runs the DMS replication process. Size the replication instance based on the volume of data and the number of concurrent tasks.

Migration phases:

1. Full load — initial bulk copy of all existing data from source to target
2. CDC — ongoing replication of changes while the source remains in production
3. Cutover — switch application connections from source to target; stop CDC

---

## Segment 5: AWS Direct Connect

Direct Connect establishes a dedicated private network connection between your on-premises network and AWS. Traffic flows through a Direct Connect location (a co-location facility) rather than the public internet.

**Benefits:**

- Consistent, predictable bandwidth (1 Gbps, 10 Gbps, 100 Gbps hosted or dedicated connections)
- Lower latency than internet-based VPN
- Reduced data transfer costs for high-volume workloads (Direct Connect egress pricing is lower than internet egress)
- Required for workloads with strict compliance requirements prohibiting internet-transit data

**Virtual Interfaces (VIFs):**

- **Private VIF** — connects to resources in a VPC via a Virtual Private Gateway or Direct Connect Gateway
- **Public VIF** — connects to AWS public endpoints (S3, CloudFront, DynamoDB) without traversing the internet
- **Transit VIF** — connects to multiple VPCs through AWS Transit Gateway

**Direct Connect Gateway** — connects a single Direct Connect connection to VPCs in multiple AWS regions. One connection, multi-region access.

**Resilience.** A single Direct Connect connection is a single point of failure. For production resilience, provision two Direct Connect connections from different Direct Connect locations with different providers. Use Site-to-Site VPN as a backup path over the internet.

**Encryption.** Direct Connect does not encrypt traffic in transit by default. For encryption over Direct Connect, establish a VPN connection over the Direct Connect connection (VPN over DX), or use MACsec for physical-layer encryption.

---

## Segment 6: AWS Site-to-Site VPN

Site-to-Site VPN creates an encrypted IPsec tunnel between your on-premises network and an AWS VPC over the public internet.

**Components:**

- **Virtual Private Gateway (VGW)** — the AWS-side VPN endpoint, attached to a VPC
- **Customer Gateway (CGW)** — a resource representing your on-premises VPN device
- **VPN Connection** — two IPsec tunnels between the VGW and the customer gateway IP address for redundancy

AWS manages the VGW. You configure your on-premises VPN appliance with the provided configuration.

**Bandwidth:** Up to 1.25 Gbps per tunnel. Multiple VPN connections can be used for additional throughput but ECMP (Equal Cost Multi-Path) routing requires Transit Gateway.

**Cost:** Hourly charge per VPN connection plus data transfer charges. Much less expensive than Direct Connect to provision, but unpredictable latency and bandwidth.

**Accelerated Site-to-Site VPN** — routes VPN traffic through AWS Global Accelerator edge locations to improve performance for geographically dispersed remote sites.

**VPN vs. Direct Connect comparison for the exam:**

- Need dedicated bandwidth, low consistent latency, or compliance? → Direct Connect
- Need quick setup, lower cost, or acceptable internet latency? → Site-to-Site VPN
- Need both reliability and redundancy? → Direct Connect primary + VPN backup

---

## Segment 7: AWS Transit Gateway

Transit Gateway is a network transit hub that connects VPCs and on-premises networks through a central gateway. Without Transit Gateway, connecting N VPCs requires N*(N-1)/2 VPC peering connections — a mesh that becomes unmanageable at scale.

With Transit Gateway, each VPC and each VPN/Direct Connect connection attaches to the Transit Gateway once. Transit Gateway routes between all attachments using route tables.

**Key features:**

- Connect hundreds of VPCs and on-premises networks
- Supports VPC attachments, VPN attachments, Direct Connect (Transit VIF) attachments, and peering with other Transit Gateways (including inter-region peering)
- Route isolation — create multiple route tables to separate environments (production, dev, shared services)
- Multicast support for one-to-many IP multicast traffic
- Equal Cost Multi-Path (ECMP) for multiple VPN tunnels to increase aggregate bandwidth

**Transit Gateway vs. VPC Peering:**

- Peering: Direct, encrypted, no bandwidth limit, no single point of failure. Use for small numbers of VPCs.
- Transit Gateway: Centralized, adds slight latency, supports large-scale hub-and-spoke topologies with route table policies.

---

## Segment 8: AWS Outposts and Hybrid DNS

**AWS Outposts** brings native AWS infrastructure, services, and APIs to your on-premises data center. AWS delivers and installs physical rack hardware running the same AWS software. You manage Outposts through the AWS console exactly like cloud resources.

Use cases:

- Ultra-low latency applications that cannot tolerate WAN round-trip time (manufacturing automation, financial trading)
- Data residency requirements mandating data not leave a physical location
- Applications that require local processing with cloud integration

Outposts support EC2, EBS, RDS, EKS, ECS, S3 on Outposts, and EMR. Full outpost networking connects back to the parent AWS region over Direct Connect or internet.

**Hybrid DNS.** When on-premises applications need to resolve AWS private DNS names (e.g., `mydb.cluster-xxxx.rds.amazonaws.com`) and AWS Lambda functions need to resolve on-premises DNS names, a DNS forwarding architecture is needed.

The AWS pattern:

- **Route 53 Resolver Inbound Endpoint** — an IP address in your VPC that on-premises DNS servers forward AWS-domain queries to. Route 53 resolves them.
- **Route 53 Resolver Outbound Endpoint** — forwards queries for on-premises domains from AWS to your on-premises DNS servers via rules.
- **Resolver Rules** — define which domains to forward outbound and to which DNS server IPs.

This bidirectional DNS resolution is the foundation of seamless hybrid name resolution.

---

## Segment 9: Migration Hub and Migration Orchestration

**AWS Migration Hub** is the central tracking service for all migration activities. It aggregates status from DMS, MGN, and partner tools into a single dashboard. Migration Hub does not perform migrations itself — it provides visibility.

**Migration Hub Orchestrator** creates and executes migration workflows as step-by-step templates. Built-in templates exist for SAP, SQL Server, and rehost/replatform patterns. Track each step, view dependencies, and automate handoffs between migration phases.

**AWS Application Discovery Service** automatically discovers on-premises servers, collects configuration and performance data, and maps application dependencies. Use the Discovery Agent for detailed data or Agentless Connector for VMware-based environments. Discovery data feeds into Migration Hub to inform migration planning.

---

## Closing Summary

Module 15 equipped you to design and discuss migrations and hybrid architectures. You know the seven R migration strategies, how MGN and DMS handle server and database migrations with minimal downtime, and how Direct Connect and Site-to-Site VPN connect on-premises networks to AWS. Transit Gateway scales connectivity to hundreds of VPCs. Outposts extends AWS to your data center. Route 53 Resolver enables hybrid DNS resolution across the connection.

Your lab this week uses the AWS console to configure a simulated hybrid DNS architecture using Route 53 Resolver endpoints and forward rules. See you in the lab.
