# Video Script: Module 07 — Amazon EC2 and Auto Scaling

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

---

### SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4334. I'm Professor Nash, and today we are covering Amazon EC2 and Auto Scaling — two services that are absolutely central to the AWS Solutions Architect Associate exam and to real-world AWS architecture.

EC2 is the foundational compute service in AWS. But understanding EC2 at an architect level means knowing far more than how to launch an instance. You need to know which instance family fits which workload, how to price your compute intelligently, where to physically place instances for performance or fault isolation, and how to automate scaling so your application handles demand without manual intervention.

By the end of this module you will be able to select the correct EC2 instance family for a given workload scenario, explain all four pricing models and identify the right model per use case, describe the three placement group types and when to use each, configure an Auto Scaling group using a launch template with the appropriate scaling policy, and explain how lifecycle hooks enable custom automation during scale-out and scale-in events.

Let's get into it.

---

### SEGMENT 2 — Instance Types and Families (1:30–5:30)

[SHOW DIAGRAM: Grid of EC2 instance family icons organized by workload category — General Purpose, Compute Optimized, Memory Optimized, Storage Optimized, Accelerated Computing — each with representative instance names and icons]

AWS organizes EC2 instances into families based on the type of workload they target. Understanding these families is not optional for the SAA-C03 — scenario questions will ask you to identify the right family. Let me walk through each one.

**General Purpose** — the default starting point for most workloads. The T-family — T3, T3a, T4g — uses a burstable CPU model. Instances accumulate CPU credits during idle periods and spend them during bursts. This is ideal for web servers, development environments, and low-traffic applications that have occasional spikes. The M-family — M5, M6i, M7g — provides a balanced ratio of CPU, memory, and network without burstable behavior. Use M-family for steady production workloads where consistent performance matters.

**Compute Optimized** — the C-family. C5, C6g, C7i. These provide the highest CPU-to-memory ratio in EC2. Target workloads: batch processing jobs, high-performance web servers, scientific modeling, game servers, and media transcoding. On the exam, if a scenario says "CPU-intensive with low memory requirements," the answer is C-family.

**Memory Optimized** — built for workloads that process large datasets entirely in RAM. The R-family — R5, R6g, R7i — is the general memory-optimized choice for in-memory databases, real-time analytics, and large caches. The X-family — X1e, X2idn — goes further with up to 24 TB of memory, designed for SAP HANA and other enterprise in-memory databases. If you see a scenario mentioning SAP HANA or "the largest possible memory configuration," think X-family.

**Storage Optimized** — the I-family, D-family, and H-family. I3 and I4i instances provide NVMe SSD-backed instance storage for extremely low-latency, high-throughput random I/O. These are designed for NoSQL databases, data warehouses needing fast local storage, and high-frequency OLTP. The D-family uses HDD storage optimized for sequential reads — distributed file systems and data processing frameworks like Hadoop. On the exam: "high IOPS, low latency, sequential workload" → I-family or D-family respectively.

**Accelerated Computing** — P-family and G-family instances provide GPU-backed compute for machine learning training, deep learning, and graphics rendering. The Inf family uses AWS-designed Inferentia chips optimized for ML inference at lower cost per inference than GPU instances.

[SHOW DIAGRAM: EC2 instance name breakdown — "m6g.2xlarge" labeled with arrows: m=family, 6=generation, g=processor variant (Graviton), .=separator, 2xlarge=size]

The naming convention encodes important information. "m6g.2xlarge" means M-family, sixth generation, Graviton ARM processor, double-extra-large size. Processor suffixes matter: no suffix means Intel Xeon, "a" means AMD EPYC, "g" means AWS Graviton (ARM). Graviton instances typically provide 20–40% better price-performance than equivalent x86 instances for compatible workloads.

---

### SEGMENT 3 — Amazon Machine Images (5:30–7:30)

[SHOW DIAGRAM: AMI creation and launch flow — Running EC2 instance with software installed → Create Image action → AMI artifact (consisting of EBS snapshot + metadata + permissions) → Launch new instances in multiple AZs from the AMI]

An AMI — Amazon Machine Image — is a template containing the complete configuration needed to launch an EC2 instance: the operating system, pre-installed software, application configuration, and storage volume mappings. AMIs are the cornerstone of repeatable, consistent EC2 deployments.

AMIs are regional resources. An AMI created in us-east-1 cannot be directly used to launch instances in eu-west-1. You must copy the AMI to the target region first. This is an important exam fact — if a question mentions multi-region deployment from a single golden image, the workflow involves AMI copy operations.

There are three sources for AMIs. First, AWS-provided AMIs — maintained by Amazon and include Amazon Linux 2023, Ubuntu, Windows Server, Red Hat Enterprise Linux, and others. These receive security patches and are the safest starting point. Second, AWS Marketplace AMIs — provided by software vendors, pre-configured with licensed software such as Cisco network appliances, Palo Alto firewalls, or commercial database engines. Third, community AMIs — shared by other AWS users. Use these cautiously because they are not vetted or supported by AWS.

The most important AMI concept for architects is the golden image pattern. You launch a base instance from an AWS-provided AMI, install and configure your application stack, harden the OS, and then create a custom AMI from that running instance. All future instances launched from that AMI start in an identical, pre-configured state. This pattern is combined with launch templates and Auto Scaling groups to ensure every instance in your fleet is identical.

For dynamic deployments, use AWS Systems Manager Parameter Store to store the latest AMI ID. CloudFormation and Terraform can reference the SSM parameter dynamically rather than hardcoding region-specific AMI IDs.

---

### SEGMENT 4 — Placement Groups (7:30–9:30)

[SHOW DIAGRAM: Three side-by-side diagrams — Left: Cluster group showing instances packed together on a single rack in one AZ. Center: Spread group showing individual instances each on separate hardware across AZs. Right: Partition group showing a set of partitions, each partition containing multiple instances on dedicated racks]

Placement groups control the physical placement of EC2 instances within AWS infrastructure. The three types serve fundamentally different goals.

**Cluster placement groups** pack instances together on the same underlying hardware within a single Availability Zone. This delivers the lowest possible network latency and highest throughput — up to 10 Gbps of bandwidth between instances in a cluster group. The trade-off is reduced fault tolerance: if the underlying hardware experiences an issue, all instances in the group are affected. Use cluster groups for HPC workloads, tightly-coupled parallel computing, and applications where node-to-node latency directly impacts performance.

**Spread placement groups** place each individual instance on a separate physical rack, with independent power and network. You are limited to 7 instances per Availability Zone in a spread group, but you can span multiple AZs. Use spread groups for a small number of critical instances that must not share failure domains. The classic example: a primary database, a secondary database, and an application server — each on separate hardware so a single hardware failure cannot affect more than one component.

**Partition placement groups** divide instances into logical partitions. Each partition occupies its own set of hardware (rack) with dedicated power and networking, providing partition-level fault isolation. Unlike spread groups, you can run hundreds or thousands of instances in a partition group across up to 7 partitions per AZ. This is designed for large distributed systems — Hadoop clusters, Apache Cassandra rings, Apache Kafka brokers — where you want rack-level fault isolation while still scaling to large instance counts.

The exam decision is direct: low latency for HPC equals Cluster. Small number of critical isolated instances equals Spread. Large distributed systems needing rack-level isolation equals Partition.

---

### SEGMENT 5 — EC2 Pricing Models (9:30–13:00)

[SHOW DIAGRAM: Bar chart comparing pricing of On-Demand at 100%, Compute Savings Plan at approximately 66%, Standard Reserved 1-year All Upfront at approximately 40%, and Spot at approximately 10–30% of On-Demand baseline, with workload characteristics noted under each bar]

AWS provides four main pricing models for EC2. Selecting the right model is one of the highest-ROI architectural decisions you can make, and it is tested heavily on the SAA-C03.

**On-Demand** pricing means you pay for compute by the hour or second with no commitments or upfront costs. This is the highest per-unit cost but gives you maximum flexibility. On-Demand is the right choice for workloads with unpredictable or short-duration compute needs, for new applications being evaluated before committing, and for development and test environments that run intermittently. Think of On-Demand as the baseline from which all other models provide discounts.

**Reserved Instances** provide up to 72% discount in exchange for committing to a specific instance type in a specific region for 1 or 3 years. Payment options are All Upfront, Partial Upfront, and No Upfront — more upfront payment means a larger discount. Standard Reserved Instances are locked to a specific instance type and cannot be changed. Convertible Reserved Instances allow you to exchange them for a different instance type family, operating system, or tenancy but offer a smaller discount of up to 54%. Reserved Instances are applied automatically to matching On-Demand usage in your account — there is no separate configuration needed.

**Savings Plans** are the modern evolution of Reserved Instances. Instead of committing to a specific instance type, you commit to a specific dollar amount of compute spend per hour. Compute Savings Plans apply across EC2, Lambda, and AWS Fargate regardless of instance family, region, or OS — maximum flexibility, up to 66% discount. EC2 Instance Savings Plans are scoped to a specific instance family in a region but offer up to 72% discount. Savings Plans are generally preferred for new workloads because they automatically apply savings across the broadest set of usage.

**Spot Instances** let you use spare AWS EC2 capacity at up to 90% discount compared to On-Demand. The critical caveat: AWS can reclaim Spot instances with only a 2-minute warning when the underlying capacity is needed elsewhere. This means Spot is exclusively appropriate for fault-tolerant, stateless, and interruptible workloads: nightly batch data processing, CI/CD pipeline build agents, image rendering farms, and stateless application tier instances running behind a load balancer where any individual instance can be replaced without data loss.

[SHOW DIAGRAM: Pricing decision tree — "Is the workload steady-state and running continuously?" → Yes → Savings Plans or Reserved. "Can the workload be interrupted and restarted?" → Yes → Spot. "Is duration short or unpredictable?" → Yes → On-Demand.]

Classic exam scenario: a company runs a 4-hour data transformation job every night that can be restarted from a checkpoint if interrupted. The answer is Spot Instances. Another scenario: a company runs a production e-commerce website 24/7 with predictable traffic. The answer is Compute Savings Plans or Standard Reserved Instances.

---

### SEGMENT 6 — Auto Scaling Groups (13:00–17:00)

[SHOW DIAGRAM: Auto Scaling group visual spanning 3 AZs. CloudWatch alarm at top. Arrows show instances being added when CPU alarm fires and removed when CPU drops. Min/Desired/Max labels on the side with example values 2/4/10.]

Auto Scaling allows your EC2 fleet to grow and shrink automatically in response to real demand. An Auto Scaling group — ASG — is the core resource. It maintains a desired number of instances, automatically replaces unhealthy instances by checking health checks, and adjusts capacity based on scaling policies you define.

Every ASG has three capacity settings. **Minimum** is the floor — the ASG will never have fewer instances than this value. **Maximum** is the ceiling — the ASG will never exceed this. **Desired** is the target count the ASG actively tries to maintain. When a scaling policy fires, it adjusts the desired count, and the ASG either launches new instances or terminates existing ones to reach the new target.

Auto Scaling uses a **launch template** to define what to launch. A launch template specifies the AMI ID, instance type, key pair, security groups, IAM instance profile, user data bootstrap script, and optional Spot configuration. Launch templates support versioning — you can create new versions and roll back if needed. Always use launch templates over the older launch configurations, which are deprecated and do not support all modern EC2 features including T-instance CPU credit options, Spot instance diversification, and dedicated hosts.

[SHOW DIAGRAM: Scaling policy comparison — four rows: Target Tracking with a thermostat icon, Step Scaling with tiered alarm levels, Scheduled Scaling with a calendar icon, Predictive Scaling with an ML forecast curve]

AWS provides four scaling policy types. **Target Tracking Scaling** is the recommended default. You specify a target value for a metric — "keep average CPU utilization at 50%" — and Auto Scaling adds or removes instances to maintain that target value. The ASG calculates the required capacity change automatically. This is analogous to a thermostat — set the target temperature and let the system manage it.

**Step Scaling** defines different scaling actions for different alarm severity thresholds. If CPU is between 60–80%, add 1 instance. If CPU exceeds 80%, add 3 instances. This gives more granular control but requires more manual configuration than Target Tracking.

**Scheduled Scaling** adjusts capacity on a defined schedule. If your application consistently experiences heavy load on Monday mornings, configure a scheduled action to increase desired capacity at 7:45 AM before the load arrives. Scheduled scaling can be combined with other policy types.

**Predictive Scaling** uses machine learning trained on your historical CloudWatch metrics to forecast future demand and proactively adjust capacity before demand arrives. It works well for workloads with recurring, cyclical patterns.

Auto Scaling groups distribute instances across the Availability Zones you specify. The ASG balances the instance count as evenly as possible across AZs. When a scale-in termination occurs, the default termination policy selects the AZ with the most instances and within that AZ terminates the instance with the oldest launch template version, helping keep the fleet on current configurations.

---

### SEGMENT 7 — Lifecycle Hooks (17:00–19:30)

[SHOW DIAGRAM: EC2 instance lifecycle state machine — boxes for: Pending → Pending:Wait (hook fires here, Lambda runs) → Pending:Proceed → InService → Terminating → Terminating:Wait (hook fires here, Lambda runs) → Terminating:Proceed → Terminated. Arrows show CompleteLifecycleAction signals returning to the ASG.]

Lifecycle hooks are one of those features that separate intermediate AWS users from architects. They pause EC2 instances at specific transition points in the Auto Scaling lifecycle so you can run custom actions before the instance enters or leaves the InService state.

When you configure a scale-out lifecycle hook, newly launched instances enter a **Pending:Wait** state instead of immediately becoming InService and receiving traffic. During this wait window — configurable up to 48 hours — you can run automation via EventBridge rules triggering Lambda functions or SSM Run Command. Common use cases: installing monitoring agents, configuring application settings from Parameter Store or Secrets Manager, running smoke tests, or registering the instance with a service discovery system. When your automation completes successfully, it calls the CompleteLifecycleAction API to signal the ASG, and the instance transitions to InService.

The same mechanism works on scale-in. When an instance is selected for termination, it enters **Terminating:Wait** before the actual termination. Your hook automation can drain open connections, flush an in-memory cache to a database, deregister from service discovery, or archive logs to S3. This prevents data loss during scale-in events.

This is a critical exam pattern. "A company needs to ensure logs are uploaded to S3 before an EC2 instance is terminated by Auto Scaling." The solution is a lifecycle hook on the termination transition that invokes a Lambda function to collect and upload logs, then signals completion.

Another pattern: "A company needs to run a configuration script before new instances accept traffic." The solution is a launch lifecycle hook that pauses instances in Pending:Wait while an SSM document runs the configuration script.

---

### SEGMENT 8 — Summary and Exam Tips (19:30–21:30)

Let me close with the high-priority exam takeaways for Module 07.

Instance families: T-family for burstable low-cost workloads, C-family for CPU-intensive tasks, R and X-family for large in-memory datasets including SAP HANA, I-family for NVMe SSD high-IOPS storage workloads, P and G-family for GPU-based ML and graphics.

Pricing models: Spot for interruptible fault-tolerant batch jobs at maximum savings. Savings Plans for flexible commitment discounts across EC2, Lambda, and Fargate. Standard Reserved for fixed steady-state workloads with maximum EC2 discount. On-Demand for short-term, unpredictable, and development usage.

Placement groups: Cluster for HPC low-latency networking, Spread for critical isolated instances with a 7-per-AZ limit, Partition for large distributed systems like Hadoop and Cassandra.

Auto Scaling: always use launch templates not launch configurations. Target Tracking is the recommended default policy. ASGs auto-balance across AZs. Default termination policy favors the oldest launch template.

Lifecycle hooks: Pending:Wait for custom actions before an instance goes InService. Terminating:Wait for custom actions before an instance is destroyed. They are the correct answer any time a scenario involves doing something before an instance comes online or before it is terminated.

In Module 08 we shift to storage — S3 and the full AWS storage services family. I'll see you there.

---

*End of Module 07 Video Script*

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
