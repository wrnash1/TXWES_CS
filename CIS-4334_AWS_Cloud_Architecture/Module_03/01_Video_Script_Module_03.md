# Video Script: Module 03 - EC2: Instance Types, Auto Scaling, and Load Balancing

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome back. I am Professor Nash and this is Module 03: EC2 — Instance Types, Auto Scaling, and Load Balancing.

EC2 is AWS's primary compute service and a major focus of the SAA-C03 exam. Whether you are designing for cost, performance, availability, or resilience, EC2 decision-making appears in every domain. By the end of this module you will be able to:

- Select the right EC2 instance type for compute, memory, storage, and GPU workloads
- Explain the EC2 purchasing options (On-Demand, Reserved, Spot, Savings Plans) and their cost tradeoffs
- Design an Auto Scaling Group with the correct scaling policy for a given performance requirement
- Choose between Application, Network, and Gateway Load Balancers for a given traffic pattern
- Architect a multi-AZ, load-balanced, auto-scaled deployment for high availability

---

## [01:30 - 07:00] EC2 Instance Types and Families

[SHOW DIAGRAM]

EC2 instances come in families, each optimized for a different workload type. The SAA-C03 exam presents scenario questions where you must match the workload description to the correct instance family. Let me walk through each family.

**General Purpose (M and T families)** — balanced CPU, memory, and networking. M5 and M6i are workhorses for web servers, application servers, and development environments. T3 and T4g are burstable — they accumulate CPU credits during low-utilization periods and spend them during bursts. T-series instances are ideal for workloads with variable CPU requirements like small databases, microservices, or development boxes. The exam trap: T-series instances can underperform under sustained CPU load because they exhaust credits. If the workload description mentions consistent, sustained high CPU, T-series is wrong.

**Compute Optimized (C family)** — high-performance processors with high CPU-to-memory ratio. C5, C6i, C6g. Use cases: high-performance web servers, batch processing, video encoding, scientific modeling, dedicated gaming servers. Any scenario that mentions CPU-intensive workloads without a memory requirement points to C-family.

**Memory Optimized (R, X, and z families)** — large amounts of RAM for memory-intensive workloads. R5, R6i: in-memory databases like Redis or SAP HANA, real-time big data analytics, high-performance databases. X1e, X2i: the largest memory instances — ideal for SAP HANA and large in-memory databases. The exam pattern: if the scenario mentions in-memory database, memory-intensive analytics, or workloads that need to hold large datasets in RAM, choose R or X family.

**Storage Optimized (I, D, and H families)** — high sequential read/write access to very large datasets on local NVMe storage. I3, I4i: NoSQL databases requiring low-latency direct-attached storage, data warehousing, distributed file systems. D3: dense storage for Hadoop, HDFS, data processing. H1: MapReduce. The exam pattern: if the scenario mentions low-latency local storage, sequential I/O, or distributed storage workloads, choose I or D family.

**Accelerated Computing (P, G, Inf, and Trn families)** — hardware accelerators for GPU compute and machine learning. P4d, P3: ML model training, high-performance computing, graphics rendering. G4dn, G5: ML inference, video transcoding, game streaming. Inf1, Inf2: high-throughput, low-latency ML inference using AWS Inferentia chips. Trn1: ML training using AWS Trainium. The exam pattern: GPU, machine learning, graphics, or deep learning workloads.

[SHOW DIAGRAM]

Instance naming convention breakdown — let me decode this. Take `m6g.2xlarge`: `m` is the family (general purpose), `6` is the generation (higher = newer), `g` is the attribute (in this case, Graviton — AWS's ARM-based processor), `2xlarge` is the size within the family. Common attribute letters: `a` = AMD processor, `g` = AWS Graviton ARM processor, `i` = Intel processor, `n` = enhanced networking, `d` = NVMe local storage, `e` = extra storage or memory.

---

## [07:00 - 11:00] EC2 Purchasing Options

[SHOW DIAGRAM]

Choosing the right purchasing option is as important as choosing the right instance type for cost optimization — which is 20% of the SAA-C03 exam. There are four main options.

**On-Demand Instances** — pay per second (Linux) or per hour (Windows) with no commitment. Full flexibility, highest per-unit price. Use case: workloads with unpredictable traffic, development and testing, first-time deployments before usage patterns are understood.

**Reserved Instances** — commit to a specific instance type in a specific Region for 1 or 3 years. Discounts up to 72% compared to On-Demand. Standard Reserved Instances lock you into a specific instance type. Convertible Reserved Instances allow you to change instance family, OS, or tenancy but offer a smaller discount (up to 54%). Scheduled Reserved Instances are for workloads that run on a predictable recurring schedule. Use case: steady-state production workloads with predictable, consistent usage.

**Savings Plans** — flexible commitment model with discounts similar to Reserved Instances. Compute Savings Plans apply to EC2, Fargate, and Lambda regardless of instance family, size, or Region. EC2 Instance Savings Plans apply to a specific instance family in a Region but allow size and OS flexibility. Savings Plans offer up to 66% savings with more flexibility than Reserved Instances. For the exam: if the scenario mentions flexibility across multiple services or Regions combined with significant savings, Savings Plans is often the answer.

**Spot Instances** — use spare AWS capacity at up to 90% discount compared to On-Demand. The catch: AWS can reclaim Spot instances with a 2-minute interruption notice when capacity is needed. Use case: fault-tolerant, stateless workloads — batch processing, data analysis, rendering, HPC workloads that can be checkpointed and resumed. Never use Spot for databases, critical web servers, or any workload that cannot tolerate interruption.

Exam pattern: match the workload description to the purchasing model. Consistent 24/7 workload = Reserved or Savings Plans. Variable burst workload = On-Demand. Fault-tolerant batch = Spot. Mixed architecture = combine On-Demand (baseline) with Spot (variable overflow).

---

## [11:00 - 15:30] EC2 Auto Scaling

[SHOW DIAGRAM]

EC2 Auto Scaling automatically adjusts the number of instances in a fleet based on demand. It consists of three components: the Launch Template (or Launch Configuration), the Auto Scaling Group, and the scaling policies.

A **Launch Template** defines what type of instance to launch — AMI ID, instance type, key pair, security groups, IAM instance profile, user data script, and EBS volume configuration. Launch Templates are versioned and are the preferred over the older Launch Configurations. Always use Launch Templates on the exam.

An **Auto Scaling Group** defines where instances run — the VPC subnets (typically multiple AZs for high availability), the minimum number of instances, the desired capacity, and the maximum number of instances. The ASG monitors instance health and replaces unhealthy instances automatically.

**Scaling Policies** determine when and how to scale.

Target Tracking Scaling is the simplest and most recommended approach. You specify a metric and a target value — for example, keep average CPU utilization at 50%. The ASG automatically adds or removes instances to maintain that target. Use target tracking for most web application scaling scenarios.

Step Scaling responds to CloudWatch alarms with discrete scaling steps. When CPU exceeds 70%, add 2 instances. When CPU exceeds 90%, add 5 instances. More precise control than target tracking but requires more configuration.

Scheduled Scaling adds or removes capacity at a specific time. Use this when you know traffic will spike — for example, every Friday at 6 PM before a weekend sale event.

Predictive Scaling uses machine learning to forecast future load based on historical patterns and pre-scales capacity before the load arrives. Use this for workloads with predictable daily or weekly traffic cycles.

[SHOW DIAGRAM]

The SAA-C03 exam frequently asks about the relationship between Auto Scaling and load balancers. When you attach an Auto Scaling Group to an Application Load Balancer, the ALB automatically registers new instances as targets when they are launched and deregisters them when they are terminated. Health checks flow in both directions — the ASG uses EC2 health checks AND ALB health checks to determine instance health.

Connection draining (called deregistration delay on ALB) ensures that when an instance is being terminated, the load balancer stops sending new requests to it while allowing in-flight requests to complete. The default is 300 seconds. For long-running requests, increase this value. For short-lived connections, decrease it to speed up scale-in.

---

## [15:30 - 19:30] Elastic Load Balancing

[SHOW DIAGRAM]

AWS offers four types of load balancers. Choosing the right one is a frequent SAA-C03 exam question.

**Application Load Balancer (ALB)** operates at Layer 7 — the HTTP/HTTPS application layer. It supports path-based routing, host-based routing, HTTP header-based routing, and query string routing. It supports WebSocket, HTTP/2, and gRPC. ALB integrates with AWS WAF, AWS Cognito, and Lambda targets. Target types: EC2 instances, IP addresses, Lambda functions, or containers. Use ALB for: web applications, microservices with different URL paths routed to different backend services, REST APIs.

**Network Load Balancer (NLB)** operates at Layer 4 — TCP, UDP, and TLS. It handles millions of requests per second with ultra-low latency (sub-millisecond). NLB preserves the source IP address of clients, which ALB does not without X-Forwarded-For headers. NLB supports static IP addresses (one per AZ) and Elastic IPs — useful when clients need to whitelist specific IP addresses. Use NLB for: high-throughput low-latency applications, gaming, IoT, real-time communications, when source IP preservation is required, and when clients need static IPs to whitelist.

**Gateway Load Balancer (GWLB)** is for deploying, scaling, and managing third-party virtual network appliances — firewalls, intrusion detection systems, deep packet inspection appliances. It operates at Layer 3 and uses GENEVE protocol encapsulation to pass traffic through appliances transparently. Use GWLB when a scenario mentions inline traffic inspection or a virtual firewall appliance.

**Classic Load Balancer (CLB)** is the legacy option — it supports both Layer 4 and Layer 7 but with fewer features than ALB or NLB. The exam may reference it for backward compatibility questions. For new architectures, always choose ALB or NLB.

Exam pattern for load balancer selection:

- HTTP/HTTPS web traffic, path routing, host-based routing, Lambda targets: ALB
- TCP/UDP, high performance, static IP, source IP preservation: NLB
- Virtual firewalls, intrusion detection, inline inspection: GWLB

---

## [19:30 - 22:00] Putting It Together — Multi-AZ Scalable Architecture

[SHOW DIAGRAM]

Let me describe the canonical multi-AZ, load-balanced, auto-scaled architecture you will design on the SAA-C03 exam:

An Application Load Balancer is deployed with nodes in at least two Availability Zones. The ALB is configured with a target group pointing to an Auto Scaling Group. The ASG uses a Launch Template specifying the AMI, instance type, IAM instance profile, and user data. The ASG spans at least two private subnets in different AZs. The minimum capacity is 2 (one per AZ) to ensure availability even if one AZ fails. Target tracking scaling keeps CPU at 60%. RDS Multi-AZ sits behind the application tier. CloudWatch alarms trigger scale-out when the queue depth or CPU target is breached.

This pattern achieves:

- High availability: if one AZ fails, instances in the other AZ continue serving traffic
- Elasticity: Auto Scaling adds capacity when load increases and removes it when load decreases
- Cost efficiency: you pay only for the capacity you need at any given time

---

## [22:00 - 24:00] Module Summary and Exam Preview

Instance families: General Purpose (M, T) for balanced; Compute Optimized (C) for CPU-intensive; Memory Optimized (R, X) for in-memory; Storage Optimized (I, D) for local I/O; Accelerated Computing (P, G, Inf) for GPU and ML.

Purchasing: On-Demand for unpredictable; Reserved or Savings Plans for steady-state; Spot for fault-tolerant batch.

Auto Scaling: Launch Template defines what, ASG defines where and how many, scaling policies define when. Target tracking for most scenarios.

Load balancers: ALB for Layer 7 web traffic; NLB for Layer 4 high performance and static IP; GWLB for virtual appliances.

In the lab this week, you will work through EC2 instance selection scenarios, configure Auto Scaling Group parameters, and design a load balancing architecture. In the Reading Guide you have a complete instance family reference table, purchasing model comparison, and scaling policy decision framework.

For your certification study: aws.amazon.com/certification.

---

End of Module 03 Video Script
