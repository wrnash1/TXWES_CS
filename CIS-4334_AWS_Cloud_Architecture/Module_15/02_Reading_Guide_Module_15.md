# Reading Guide: Module 15 — AWS Migration and Hybrid Architectures

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Select the appropriate migration strategy (7 Rs) for a given workload and business requirement
2. Explain how AWS Application Migration Service performs continuous block-level replication
3. Configure AWS DMS for homogeneous and heterogeneous database migrations using CDC
4. Compare Direct Connect and Site-to-Site VPN and select the correct connectivity option
5. Design a multi-VPC Transit Gateway topology for hub-and-spoke network architectures
6. Explain when AWS Outposts is appropriate and how it differs from a standard cloud deployment
7. Configure Route 53 Resolver endpoints to enable bidirectional hybrid DNS resolution

---

## Section 1: Migration Strategies — The 7 Rs

### 1.1 Strategy Selection Guide

| Strategy | Effort | Cloud Benefit | When to Use |
|---|---|---|---|
| Retire | None | Cost savings | No longer needed |
| Retain | None | None yet | Compliance, dependency, not ready |
| Rehost | Low | Moderate | Fast migration; optimize later |
| Replatform | Medium | Medium | Minor optimizations without code changes |
| Repurchase | Low | High | Better SaaS option exists |
| Refactor | High | Very High | Strategic workloads needing cloud-native redesign |
| Relocate | Low | Moderate | VMware-based environments |

### 1.2 Rehost in Practice

Rehost (lift-and-shift) is the dominant strategy for large-scale migrations where speed is the primary concern. Applications are moved to EC2 with the same OS, same runtime, same configuration. No code changes. The benefit is speed and risk reduction — once in AWS, teams can optimize later. AWS Application Migration Service automates the rehost process.

### 1.3 Replatform Examples

Replatform makes targeted improvements without full re-architecture:

- Self-managed MySQL on-premises → Amazon RDS MySQL (eliminate OS patching, backup management)
- Java application on Tomcat on EC2 → same application on Elastic Beanstalk (eliminate infrastructure management)
- Self-managed Redis on-premises → Amazon ElastiCache Redis (eliminate cluster management)

### 1.4 Migration Assessment Tools

**AWS Migration Evaluator** (formerly TSO Logic) analyzes on-premises server utilization data to project the cost of running the same workloads on AWS. Provides a business case with cost comparisons before migration begins.

**AWS Application Discovery Service** discovers on-premises servers, collects performance and configuration data, and maps application-to-server dependencies. Two modes: Discovery Agent (installed on servers, collects detailed data) and Agentless Collector (VMware vCenter integration, agentless).

---

## Section 2: AWS Application Migration Service

### 2.1 Architecture

MGN operates in three phases:

**Replication phase** — the AWS Replication Agent is installed on source servers. The agent continuously replicates block-level changes to a staging area in AWS (low-cost EBS volumes). Replication is ongoing — the staging area always reflects the near-current state of the source.

**Testing phase** — launch test instances from the staging area without disrupting the source server. Run application tests, validate behavior, and iterate.

**Cutover phase** — trigger a final sync, launch the production instance, redirect traffic. Downtime is limited to the final sync and DNS/load balancer update — typically 10–30 minutes.

### 2.2 Post-Launch Actions

MGN supports post-launch action scripts — automation that runs after instance launch. Examples: domain join, software agent installation, configuration management tool execution. Integrate with AWS Systems Manager Run Command or CloudFormation for post-migration configuration.

### 2.3 MGN vs. EC2 AMI-based Migration

Creating an AMI from an on-premises VMware VM (using VM Import/Export) is an alternative but requires a full snapshot rather than continuous replication. VM Import/Export is appropriate for one-time migrations of small fleets. MGN is preferred for large fleets requiring minimal downtime.

---

## Section 3: AWS Database Migration Service

### 3.1 Migration Task Types

| Task Type | When to Use |
|---|---|
| Full load | Initial bulk migration; source can go down during migration |
| Full load + CDC | Migrate data while source remains in production; enables near-zero downtime |
| CDC only | Source data already exists in target; replicate ongoing changes only |

### 3.2 AWS Schema Conversion Tool

SCT is required for heterogeneous migrations (different database engines). It converts:

- Database schemas (tables, views, indexes, sequences)
- Stored procedures and functions — partial automation; complex PL/SQL may require manual conversion
- Triggers and packages

SCT provides an assessment report showing what can be automatically converted and what requires manual effort. Use the assessment report to estimate migration complexity before committing.

### 3.3 DMS Replication Instance Sizing

The replication instance runs the DMS replication software. Size based on:

- Volume of data (larger datasets benefit from larger instances)
- Number of concurrent migration tasks
- LOB (Large Object) handling — LOBs are migrated in limited LOB mode or full LOB mode; full LOB mode requires more memory

Start with `dms.r5.large` or `dms.r5.xlarge` for most production migrations.

### 3.4 Validation

DMS supports data validation — after migration, DMS compares row counts and key values between source and target. Validation results are published to CloudWatch Logs. Enable validation for all production migrations to confirm data fidelity.

---

## Section 4: AWS Direct Connect

### 4.1 Connection Types

**Dedicated connections** — physical 1 Gbps, 10 Gbps, or 100 Gbps port at a Direct Connect location. Requested from AWS; provisioned by an AWS Direct Connect Partner.

**Hosted connections** — sub-1-Gbps to 10 Gbps connections provisioned by an AWS Direct Connect Partner. More flexible sizing, faster provisioning, no dedicated physical port management.

### 4.2 Virtual Interface Types

| VIF Type | Connects To | Use Case |
|---|---|---|
| Private VIF | VGW or Direct Connect Gateway | Access VPC private resources |
| Public VIF | AWS public endpoints | Access S3, CloudFront, DynamoDB without internet |
| Transit VIF | Transit Gateway | Access multiple VPCs via Transit Gateway |

### 4.3 Direct Connect Resilience Models

AWS defines four resilience models:

- **Maximum Resiliency** — multiple dedicated connections from multiple Direct Connect locations with redundant on-premises routers. Survives a full Direct Connect location failure.
- **High Resiliency** — two dedicated connections from the same Direct Connect location. Survives device failure but not location failure.
- **Development and Test** — single connection, no redundancy. For non-production use only.
- **Classic** — legacy single-connection model. Avoid for new deployments.

### 4.4 MACsec Encryption

MACsec provides Layer 2 encryption between your on-premises router and the AWS Direct Connect device. Only available on dedicated connections (10 Gbps and 100 Gbps). Encrypts all traffic at the Ethernet frame level before it enters the Direct Connect facility.

---

## Section 5: Site-to-Site VPN Architecture

### 5.1 VPN Tunnel Redundancy

Every AWS Site-to-Site VPN connection creates two IPsec tunnels, each terminating at a different AWS endpoint in different Availability Zones. Both tunnels should be configured on your on-premises VPN device. If one tunnel fails, the other maintains connectivity. Ensure your on-premises device is configured to use both tunnels.

### 5.2 AWS VPN CloudHub

VPN CloudHub enables multiple remote sites (each with a Customer Gateway) to communicate with each other through the AWS VGW — the VGW acts as a hub. Useful when remote branch offices need site-to-site connectivity and you can leverage AWS as the transit hub. Each site requires a VPN connection to the same VGW.

### 5.3 Client VPN

AWS Client VPN is a managed OpenVPN service for individual user-to-VPC connectivity (remote workers). Different from Site-to-Site VPN, which connects entire networks. Client VPN authenticates users via Active Directory, SAML-based IdP, or mutual certificate authentication.

### 5.4 VPN + Direct Connect HA Pattern

The recommended hybrid connectivity HA pattern:

1. Primary path: Direct Connect Private VIF for dedicated, low-latency connectivity
2. Backup path: Site-to-Site VPN over the internet, using the same VGW

Configure BGP route preferences so Direct Connect routes are preferred. If Direct Connect fails, BGP automatically shifts traffic to the VPN backup. Recovery is automatic, typically within seconds to a few minutes depending on BGP timers.

---

## Section 6: AWS Transit Gateway

### 6.1 Attachments

Transit Gateway supports these attachment types:

- VPC attachments — connect a VPC to the Transit Gateway
- VPN attachments — connect a Site-to-Site VPN
- Direct Connect Gateway attachment (Transit VIF) — connect a Direct Connect circuit
- Transit Gateway peering — connect two Transit Gateways in the same or different regions
- Connect attachments — connect third-party SD-WAN appliances using GRE tunnels

### 6.2 Route Tables and Route Propagation

Each attachment can associate with a route table and propagate its routes into a route table. Use multiple route tables to implement routing policies:

- **Shared services VPC** — all VPCs can reach the shared services VPC, but VPCs cannot reach each other (spoke isolation)
- **Full mesh** — all VPCs can reach each other (single route table, all attachments associated)
- **Security segmentation** — route internet-bound traffic from all VPCs to a centralized inspection VPC containing a firewall before routing to the internet gateway

### 6.3 ECMP for VPN Throughput

A single VPN tunnel provides up to 1.25 Gbps. To exceed this, connect multiple VPN connections to Transit Gateway and enable ECMP. Traffic is distributed across all tunnels. AWS supports up to 50 VPN connections per Transit Gateway — up to 62.5 Gbps aggregate throughput with ECMP.

---

## Section 7: AWS Outposts

### 7.1 Form Factors

- **Outposts Rack** — full 42U rack of AWS infrastructure for large deployments
- **Outposts Server** — 1U or 2U form factor for space-constrained deployments (branch offices, factory floors)

### 7.2 Connectivity Requirements

Outposts must connect to the parent AWS region via a reliable network (Direct Connect or internet). The Service Link connection carries control-plane traffic (management API calls, AMI downloads, metrics). If the Service Link is interrupted, Outposts continues to run existing workloads but cannot launch new instances or make API changes.

### 7.3 Local Gateway

Each Outpost has a Local Gateway (LGW) that routes traffic between the Outpost and your on-premises local network. Instances on the Outpost can communicate directly with on-premises systems through the LGW without hairpinning through the AWS region.

### 7.4 S3 on Outposts

S3 on Outposts stores objects locally on the Outpost hardware. Used for data residency requirements where data must not leave the physical location. Objects on S3 on Outposts cannot be directly accessed from the AWS region — they are locally accessible only.

---

## Section 8: Route 53 Resolver Hybrid DNS

### 8.1 The Hybrid DNS Problem

Private hosted zones in Route 53 are not natively resolvable from on-premises DNS servers. On-premises DNS servers are not natively resolvable from within a VPC. To enable hybrid name resolution, you need DNS forwarders at both ends.

### 8.2 Inbound Endpoint

A Route 53 Resolver Inbound Endpoint creates one or more IP addresses in your VPC subnets. On-premises DNS servers can be configured to forward specific AWS domains (e.g., `*.internal.aws`) to these IP addresses. Route 53 Resolver resolves the query using VPC DNS and private hosted zones.

### 8.3 Outbound Endpoint

A Route 53 Resolver Outbound Endpoint creates IP addresses in your VPC subnets from which DNS queries can be forwarded. Resolver Rules define which domain names trigger forwarding and which on-premises DNS server IP addresses receive the forwarded queries.

### 8.4 Resolver Rule Types

- **Forward rule** — forward queries for a specific domain to specified DNS servers
- **System rule** — override AWS default resolution for specific domains (e.g., `amazonaws.com` stays on AWS)

Rules can be shared with other accounts using AWS Resource Access Manager, enabling centralized DNS management across an AWS Organization.

---

## Key Terms

- **7 Rs** — seven migration strategies: Retire, Retain, Rehost, Replatform, Repurchase, Refactor, Relocate
- **MGN** — AWS Application Migration Service; continuous block-level replication for server migrations
- **DMS** — AWS Database Migration Service; minimal-downtime database migration with CDC
- **SCT** — AWS Schema Conversion Tool; converts schema for heterogeneous database migrations
- **Direct Connect** — dedicated private network connection to AWS at 1/10/100 Gbps
- **Virtual Private Gateway (VGW)** — AWS-side endpoint for VPN and Direct Connect Private VIF
- **Transit Gateway** — network hub connecting VPCs and on-premises networks at scale
- **Outposts** — AWS infrastructure deployed in your on-premises data center
- **Inbound Endpoint** — Route 53 Resolver IP in a VPC; accepts DNS queries from on-premises
- **Outbound Endpoint** — Route 53 Resolver IP in a VPC; forwards queries to on-premises DNS

---

## SAA-C03 Exam Tips

- Rehost = fastest migration; Refactor = best cloud optimization; Replatform = middle ground
- DMS + SCT is required for heterogeneous migrations (Oracle → PostgreSQL, SQL Server → Aurora)
- Direct Connect does NOT encrypt traffic by default — add VPN over Direct Connect or MACsec for encryption
- Site-to-Site VPN is quick to set up and encrypted by default; Direct Connect provides dedicated bandwidth
- Transit Gateway is the answer when connecting more than a few VPCs — peering mesh does not scale
- Route 53 Resolver Inbound Endpoint answers on-premises DNS queries about AWS private names
- Route 53 Resolver Outbound Endpoint forwards VPC DNS queries to on-premises DNS servers
- Outposts is the answer when workloads require ultra-low latency or data residency on-premises
- VPN CloudHub uses a single VGW to connect multiple remote sites together through AWS
- Direct Connect Gateway allows one Direct Connect connection to reach VPCs in multiple regions
