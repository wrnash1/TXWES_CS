# Reading Guide: Module 03 - EC2: Instance Types, Auto Scaling, and Load Balancing

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Introduction

Amazon EC2 is the foundational compute service in AWS and one of the highest-weight topics on the SAA-C03 exam. This module covers the three decisions every solutions architect must make when designing an EC2-based workload: selecting the right instance type and purchasing model, configuring Auto Scaling to match capacity to demand, and choosing the right load balancer to distribute traffic. Each of these decisions directly maps to SAA-C03 exam questions in the cost optimization, performance, and resilience domains.

---

## Section 1: EC2 Instance Families Reference

### 1.1 Instance Family Comparison Table

| Family | Category | Optimized For | Representative Types | Exam Use Case |
|---|---|---|---|---|
| M | General Purpose | Balanced CPU/memory/network | M5, M6i, M6g | Web servers, app servers, dev environments |
| T | General Purpose (burstable) | Variable CPU with burst credits | T3, T3a, T4g | Dev boxes, low-traffic sites, microservices |
| C | Compute Optimized | High CPU-to-memory ratio | C5, C6i, C6g | Batch, video encoding, HPC, web servers under load |
| R | Memory Optimized | Large RAM for in-memory workloads | R5, R6i, R6g | In-memory DB, real-time analytics, SAP |
| X | Memory Optimized (extreme) | Largest available RAM | X1e, X2idn | SAP HANA, largest in-memory databases |
| I | Storage Optimized | High IOPS local NVMe storage | I3, I3en, I4i | NoSQL DBs, transactional workloads, low-latency I/O |
| D | Storage Optimized | Dense HDD storage | D3, D3en | Hadoop, HDFS, data lakes, distributed storage |
| P | Accelerated Computing | GPU for ML training | P3, P4d | Deep learning training, HPC |
| G | Accelerated Computing | GPU for graphics/inference | G4dn, G5 | ML inference, video transcoding, game streaming |
| Inf | Accelerated Computing | ML inference (Inferentia) | Inf1, Inf2 | High-throughput inference at low cost |
| Trn | Accelerated Computing | ML training (Trainium) | Trn1 | Cost-efficient ML model training |
| Hpc | High Performance Compute | Tightly coupled HPC | Hpc6a | CFD, weather modeling, genomics |

### 1.2 Instance Naming Convention

Instance type names follow a consistent format: `[family][generation][attributes].[size]`

For example, `r6gd.4xlarge` breaks down as:

- `r` — memory optimized family
- `6` — sixth generation
- `g` — Graviton (ARM-based) processor
- `d` — NVMe local storage included
- `4xlarge` — size (4x the baseline of xlarge in this family)

Common attribute codes:

| Code | Meaning |
|---|---|
| a | AMD EPYC processor |
| g | AWS Graviton ARM processor |
| i | Intel processor (sometimes used for clarification) |
| n | Enhanced networking, higher network bandwidth |
| d | NVMe local instance storage |
| e | Extra storage or memory (varies by family) |
| z | High frequency processor |
| b | Block storage optimized |

### 1.3 T-Series Burstable Instances

T-series instances accumulate CPU credits when running below the baseline CPU utilization level and spend credits when bursting above baseline. Each instance size has a defined baseline CPU percentage and credit accrual rate.

Key exam point: if a workload requires sustained, consistently high CPU utilization, T-series instances will exhaust their CPU credit balance and throttle back to baseline, causing performance degradation. For sustained CPU-intensive workloads, use C, M, or R family instances instead.

T-series instances support two modes:

- Standard mode: CPU performance is capped if credits are exhausted
- Unlimited mode: instance can burst beyond credits; excess burst usage is charged at a per-vCPU-hour rate

---

## Section 2: EC2 Purchasing Options

### 2.1 Purchasing Model Comparison Table

| Model | Commitment | Max Discount vs On-Demand | Best Use Case | Risk |
|---|---|---|---|---|
| On-Demand | None | None (baseline price) | Unpredictable workloads, testing, new apps | Highest cost |
| Standard Reserved | 1 or 3 years, specific type/Region | Up to 72% | Steady-state 24/7 production workloads | No flexibility; unused capacity is wasted |
| Convertible Reserved | 1 or 3 years, flexible type | Up to 54% | Steady-state workloads that may evolve | Lower discount than Standard |
| Savings Plans (Compute) | 1 or 3 years, $/hour commitment | Up to 66% | Mixed EC2/Lambda/Fargate across Regions | Requires accurate usage forecasting |
| Savings Plans (EC2 Instance) | 1 or 3 years, specific family/Region | Up to 72% | Steady-state single-family EC2 | Less flexible than Compute SP |
| Spot | None | Up to 90% | Fault-tolerant batch, stateless, interruptible | 2-minute termination notice |
| Dedicated Hosts | On-Demand or Reserved | Varies | Licensing compliance (per-socket/per-core) | Highest per-unit cost |
| Dedicated Instances | On-Demand or Reserved | Small premium | Compliance requiring single-tenant hardware | Higher cost than shared |

### 2.2 Combining Purchasing Models

Production architectures typically combine models. A common pattern:

- Reserved Instances or Savings Plans for the baseline (always-on) capacity
- On-Demand for predictable short-term spikes
- Spot for fault-tolerant overflow and batch workloads

The Auto Scaling Group Mixed Instance Policy supports combining On-Demand and Spot instances in a single ASG, with the On-Demand portion maintaining the baseline.

---

## Section 3: EC2 Auto Scaling Deep Dive

### 3.1 Auto Scaling Components

| Component | Purpose | Key Configuration |
|---|---|---|
| Launch Template | Defines what instance to launch | AMI, instance type, key pair, SG, IAM profile, user data |
| Auto Scaling Group | Defines where and how many | VPC subnets, min/desired/max capacity, health check type |
| Target Group | Routes ALB traffic to ASG instances | Health check path, port, protocol |
| Scaling Policy | Defines when to scale | Target tracking, step scaling, scheduled, predictive |
| Lifecycle Hooks | Pause launch/terminate for custom actions | Run scripts before instance enters or leaves service |

### 3.2 Scaling Policy Comparison

| Policy Type | How It Works | Best Use Case |
|---|---|---|
| Target Tracking | Adds/removes instances to maintain a target metric value | Most web applications; easiest to configure |
| Step Scaling | Scales in discrete steps based on CloudWatch alarm thresholds | Fine-grained control; different scaling amounts for different alarm levels |
| Scheduled Scaling | Changes capacity at specific times | Predictable scheduled events (weekly sale, end-of-month processing) |
| Predictive Scaling | ML-based forecast of future load; pre-scales proactively | Cyclical workloads with consistent daily/weekly patterns |
| Simple Scaling | Legacy; adds/removes fixed count on single alarm | Avoid in new architectures; replaced by target tracking |

### 3.3 Health Check Types

Auto Scaling Groups support two health check sources:

- EC2 health checks: checks that the underlying EC2 instance is running and passes system status checks. This is the default.
- ELB health checks: checks that the load balancer's health check for the instance passes. More meaningful for application availability — an instance can be running (passes EC2 check) but serving 500 errors (fails ELB check).

Best practice: always enable ELB health checks when an ASG is attached to a load balancer. This ensures Auto Scaling replaces instances that are unhealthy from the application's perspective, not just from the EC2 infrastructure perspective.

### 3.4 Lifecycle Hooks

Lifecycle hooks allow you to pause an instance at a specific point in its launch or termination lifecycle to perform custom actions:

- Launch lifecycle hook: instance enters pending:wait state before becoming InService. Use to install software, configure agents, run validation tests.
- Terminate lifecycle hook: instance enters terminating:wait state before being terminated. Use to drain connections, copy logs, deregister from service discovery.

The hook must complete within a configurable heartbeat timeout (default 1 hour). If the action completes, call CompleteLifecycleAction to proceed. If it times out, the default result (CONTINUE or ABANDON) applies.

---

## Section 4: Elastic Load Balancing

### 4.1 Load Balancer Type Comparison

| Feature | ALB | NLB | GWLB | CLB |
|---|---|---|---|---|
| OSI Layer | Layer 7 | Layer 4 | Layer 3 | Layer 4 and 7 |
| Protocols | HTTP, HTTPS, gRPC, WebSocket | TCP, UDP, TLS | IP (GENEVE) | HTTP, HTTPS, TCP |
| Routing | Path, host, header, query string | Port-based | Flow-based | Round-robin |
| Target types | EC2, IP, Lambda, containers | EC2, IP, ALB | Virtual appliances | EC2 only |
| Static IP | No (use NLB in front) | Yes (1 per AZ) | No | No |
| Source IP preservation | No (X-Forwarded-For header) | Yes | Yes | No |
| WAF integration | Yes | No | No | No |
| SSL/TLS termination | Yes | Yes (passthrough or termination) | No | Yes |
| Use case | Web apps, microservices, APIs | High performance, gaming, IoT | Virtual firewalls, IDS/IPS | Legacy (avoid for new) |

### 4.2 ALB Routing Rules

ALB supports content-based routing with listener rules evaluated in priority order. Rule types:

- Path-based: route `/api/*` to one target group, `/static/*` to another
- Host-based: route `api.example.com` differently than `www.example.com`
- HTTP header: route based on custom request headers
- HTTP method: route GET vs. POST to different backends
- Query string: route `?version=2` to a new backend for A/B testing
- Source IP: route traffic from specific CIDR ranges to internal backends

### 4.3 Connection Draining and Deregistration Delay

When a target is deregistered from a target group (due to scale-in, health check failure, or manual deregistration), the load balancer stops sending new requests to that target. Deregistration delay keeps the target registered long enough for in-flight requests to complete:

- ALB and NLB: configurable from 0 to 3600 seconds (default 300)
- Set lower for stateless short-lived connections (decrease scale-in time)
- Set higher for long-lived connections (API calls, downloads)

### 4.4 Cross-Zone Load Balancing

By default, each load balancer node distributes traffic only to targets registered in its Availability Zone. With cross-zone load balancing enabled, each node distributes traffic evenly across all registered targets in all AZs. Cross-zone load balancing is enabled by default for ALB and disabled by default for NLB and GWLB. Enable it when your Auto Scaling Group has uneven instance distribution across AZs.

---

## Section 5: Architecture Pattern — Auto-Scaled Multi-AZ Web Application

[SHOW DIAGRAM]

```text
Internet
    |
[Route 53] --> [ALB in us-east-1a and us-east-1b] (public subnets)
                    |
       [Target Group: port 80, health check /health]
                    |
    [Auto Scaling Group spanning private subnets]
    [AZ: us-east-1a]         [AZ: us-east-1b]
    EC2 (t3.medium)          EC2 (t3.medium)
    EC2 (t3.medium)          EC2 (t3.medium)
                    |
    [RDS Multi-AZ: primary us-east-1a, standby us-east-1b]
    [ElastiCache (optional): session caching layer]
```

Design decisions in this architecture:

- ALB spans two AZs for load balancer redundancy
- ASG minimum capacity = 2 (one per AZ) ensures availability during a single AZ failure
- Private subnets for compute and database tiers; public subnets only for ALB
- ELB health checks configured on ASG to replace application-unhealthy instances
- Target tracking scaling policy targeting 60% average CPU utilization

---

## Section 6: SAA-C03 Exam Tips for Module 03

**Exam Tip 1 — Instance family selection by workload keyword:**
Memory database or in-memory analytics = R or X family. CPU-intensive batch or encoding = C family. GPU or ML = P, G, or Inf family. Local NVMe low-latency I/O = I family. Balanced general web/app = M family. Burstable variable CPU = T family.

**Exam Tip 2 — Spot instance limitations:**
Spot instances are never correct for databases, stateful applications, or any workload the scenario describes as critical or requiring high availability. The 2-minute termination notice makes them unsuitable for these workloads. Spot is only correct when the scenario explicitly mentions fault-tolerant, stateless, or interruptible workloads.

**Exam Tip 3 — Reserved vs. Savings Plans:**
When a scenario mentions commitment across multiple instance families, multiple Regions, or a mix of EC2 and Lambda/Fargate, Savings Plans is the answer. When a scenario mentions a single, specific, locked-in instance type for a long-running steady workload, Standard Reserved Instances may offer a slightly higher discount.

**Exam Tip 4 — Target tracking is the default scaling answer:**
For most web application Auto Scaling scenarios, target tracking scaling is the correct answer. The exam will describe a need to "automatically scale based on CPU" or "maintain consistent response times" — target tracking handles this. Step scaling is correct only when the scenario requires different scaling amounts at different thresholds.

**Exam Tip 5 — ALB vs. NLB selection:**
If the scenario mentions HTTP, HTTPS, path-based routing, microservices, REST API, or Lambda targets: ALB. If the scenario mentions TCP, UDP, static IP, source IP preservation, very high throughput, or gaming: NLB. If the scenario mentions virtual firewall or inline traffic inspection: GWLB.

**Exam Tip 6 — ELB health checks on ASG:**
Always enable ELB health checks on an Auto Scaling Group that is attached to a load balancer. EC2 health checks alone will not catch application-level failures — an instance can pass EC2 health checks while returning HTTP 500 errors to clients.

**Exam Tip 7 — Dedicated Hosts vs. Dedicated Instances:**
Dedicated Hosts give you visibility into and control over the physical server, which is required for some BYOL (Bring Your Own License) software licensing models (per-socket, per-core). Dedicated Instances run on single-tenant hardware but you do not control which physical server. The exam distinguishes these when a question mentions software licensing compliance.

**Exam Tip 8 — Launch Templates over Launch Configurations:**
The SAA-C03 exam and AWS best practices both prefer Launch Templates over Launch Configurations. Launch Templates support versioning, mixed instance policies, and newer EC2 features. If given a choice in an exam question, Launch Template is always correct.

---

## Section 7: Key CLI Commands for Module 03

Describe available instance types with filter:

```bash
aws ec2 describe-instance-types \
  --filters Name=instance-type,Values=m5.* \
  --query "InstanceTypes[*].{Type:InstanceType,vCPU:VCpuInfo.DefaultVCpus,MemGiB:MemoryInfo.SizeInMiB}" \
  --output table
```

Describe an Auto Scaling Group:

```bash
aws autoscaling describe-auto-scaling-groups \
  --auto-scaling-group-names MyWebAppASG \
  --output json
```

List target groups for a load balancer:

```bash
aws elbv2 describe-target-groups \
  --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-alb/abc123 \
  --output table
```

Check target health:

```bash
aws elbv2 describe-target-health \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-tg/xyz789
```

---

## Section 8: Study Checklist

- [ ] Name all major instance families and their primary use case from memory
- [ ] Decode an instance type name (e.g., r6gd.2xlarge) into its components without referencing notes
- [ ] Explain T-series CPU credit mechanics and identify when T-series is inappropriate
- [ ] Compare all four purchasing models (On-Demand, Reserved, Savings Plans, Spot) on commitment, discount, and use case
- [ ] Describe the three components of an Auto Scaling Group and what each configures
- [ ] Explain the difference between EC2 health checks and ELB health checks on an ASG
- [ ] Select the correct load balancer type (ALB, NLB, GWLB) for at least five different scenario descriptions
- [ ] Describe connection draining and explain when to increase vs. decrease the deregistration delay
- [ ] Run the CLI commands in Section 7 and record the output
- [ ] Complete the Module 03 quiz with a score of at least 80 percent
- [ ] Post your initial response in the Module 03 discussion forum by the Wednesday deadline

---

## References

All certification study materials and exam registration: <aws.amazon.com/certification>

---

## 9. Supplemental Resources

**1. AWS Documentation — Amazon EC2 Auto Scaling User Guide**
https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
Comprehensive guide covering Auto Scaling groups, launch templates, scaling policies (target tracking, step, scheduled), lifecycle hooks, and health check integration with ELB.

**2. AWS Skill Builder — Amazon EC2 Basics (Free Digital Course)**
https://skillbuilder.aws/learn/course/external/view/elearning/479/amazon-ec2-basics
Free course covering EC2 instance types, purchasing options, EBS volumes, and the fundamentals of compute on AWS — directly supporting Module 03 exam preparation.

**3. AWS Documentation — Elastic Load Balancing Features Comparison**
https://aws.amazon.com/elasticloadbalancing/features/
Official feature comparison page for ALB, NLB, GWLB, and CLB — essential reference for the SAA-C03 load balancer selection questions covered in this module.
