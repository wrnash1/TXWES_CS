# Reading Guide: Module 07 — Amazon EC2 and Auto Scaling

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4334 &BULL; AMAZON WEB SERVICES (AWS) CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

---

## Introduction

Amazon EC2 is the most widely tested service on the AWS SAA-C03 exam. This reading guide provides the reference tables, decision frameworks, and architectural patterns you need to answer EC2 and Auto Scaling scenario questions correctly. Work through each section in order and complete the checklist before attempting the module quiz.

---

## Section 1: EC2 Instance Families

### 1.1 Instance Family Reference Table

| Family | Class | vCPU:Memory Ratio | Primary Use Cases | Exam Trigger Words |
|--------|-------|-------------------|-------------------|--------------------|
| T3 / T4g | General Purpose (Burstable) | Variable | Dev/test, low-traffic web servers | "burst," "low-cost," "variable CPU" |
| M5 / M6i / M7g | General Purpose (Balanced) | 1:4 | App servers, mid-tier databases | "balanced," "general workload" |
| C5 / C6g / C7i | Compute Optimized | 1:2 | Batch, HPC, media transcoding | "CPU-intensive," "high performance compute" |
| R5 / R6g / R7i | Memory Optimized | 1:8 | In-memory DBs, real-time analytics | "large in-memory," "Redis at scale" |
| X1e / X2idn | Memory Optimized (Large) | 1:32+ | SAP HANA, largest in-memory | "SAP HANA," "terabytes of RAM" |
| I3 / I4i | Storage Optimized (NVMe) | Varies | NoSQL, high IOPS, low-latency I/O | "NVMe," "high IOPS," "low-latency storage" |
| D3 / H1 | Storage Optimized (HDD) | Varies | Hadoop, sequential throughput | "sequential I/O," "data warehouse local" |
| P3 / P4 | Accelerated (GPU) | Varies | ML training, deep learning | "GPU," "machine learning training" |
| G4 / G5 | Accelerated (GPU Graphics) | Varies | Graphics rendering, game streaming | "graphics," "GPU rendering" |
| Inf1 / Inf2 | Accelerated (Inferentia) | Varies | ML inference at low cost | "inference," "Inferentia" |

### 1.2 Processor Suffix Reference

| Suffix | Processor | Key Benefit |
|--------|-----------|-------------|
| (none) | Intel Xeon | Broad software compatibility |
| a | AMD EPYC | ~10% cost reduction vs. Intel equivalent |
| g | AWS Graviton (ARM) | 20–40% better price-performance for compatible workloads |
| i | Intel Ice Lake / Sapphire Rapids | Latest Intel generation |

### 1.3 Instance Sizing

Sizes follow a consistent doubling pattern within a family and generation: nano, micro, small, medium, large, xlarge, 2xlarge, 4xlarge, 8xlarge, 12xlarge, 16xlarge, 24xlarge, 32xlarge, 48xlarge, metal. Each size step approximately doubles vCPU and memory. Metal instances provide dedicated hardware with no hypervisor overhead.

---

## Section 2: Amazon Machine Images

### 2.1 AMI Concepts

An AMI is a snapshot-based template containing:

- A root volume snapshot (the operating system and pre-installed software)
- Launch permissions specifying which AWS accounts can use the AMI
- Block device mappings specifying volumes to attach on launch

AMIs are registered in a specific AWS Region. The AMI ID format is `ami-` followed by 17 hex characters (e.g., `ami-0abcdef1234567890`). AMI IDs differ across regions even for the same underlying OS version.

### 2.2 AMI Types by Source

| AMI Source | Description | Trust Level | Best Use |
|------------|-------------|-------------|----------|
| AWS-provided | Maintained by Amazon, regularly patched | Highest | Starting point for all new instances |
| AWS Marketplace | Vendor-provided, includes licensed software | High (vetted by AWS) | Licensed products (Cisco, Palo Alto, etc.) |
| Community | Shared by third-party users | Low (not vetted) | Evaluate carefully before production use |
| Custom (self-created) | Built from your own instance | Highest (you own it) | Golden image pattern, standardized fleets |

### 2.3 Golden Image Pattern

The golden image workflow is the standard enterprise practice for consistent EC2 deployments:

1. Launch a base instance from an AWS-provided AMI
2. Install OS patches and hardening configurations
3. Install and configure application dependencies
4. Create an AMI from the running instance (this creates EBS snapshots of all attached volumes)
5. Store the AMI ID in SSM Parameter Store for automated reference
6. Reference the AMI in launch templates for Auto Scaling groups
7. Periodically rebuild the golden image to incorporate new patches

This pattern ensures every instance is identical from birth and eliminates configuration drift.

---

## Section 3: Placement Groups

### 3.1 Placement Group Comparison

| Feature | Cluster | Spread | Partition |
|---------|---------|--------|-----------|
| Goal | Low latency, high throughput | Fault isolation for individual instances | Fault isolation for groups of instances |
| Scope | Single AZ | Multi-AZ capable | Multi-AZ capable |
| Max instances | No hard limit | 7 per AZ | Hundreds per partition; up to 7 partitions per AZ |
| Hardware sharing | Shared rack (intentional) | No rack sharing | Per-partition rack isolation |
| Failure blast radius | Entire group if rack fails | Single instance | Single partition |
| Best for | HPC, MPI, tightly-coupled parallel | Small sets of critical independent instances | Hadoop, Cassandra, Kafka |

### 3.2 Placement Group Decision Tree

```
Is the workload tightly-coupled requiring max network performance?
  Yes → Cluster Placement Group

Is the workload a small set (<= 7 per AZ) of critical, isolated instances?
  Yes → Spread Placement Group

Is the workload a large distributed system needing rack-level fault isolation?
  Yes → Partition Placement Group

No performance or isolation requirements?
  → No placement group needed
```

---

## Section 4: EC2 Pricing Models

### 4.1 Pricing Model Comparison

| Model | Discount vs. On-Demand | Commitment | Interruption Risk | Best For |
|-------|----------------------|------------|-------------------|----------|
| On-Demand | None (baseline) | None | None | Unpredictable, short-term, dev/test |
| Savings Plans (Compute) | Up to 66% | 1 or 3 years ($/hr) | None | Flexible steady-state across EC2/Lambda/Fargate |
| Savings Plans (EC2 Instance) | Up to 72% | 1 or 3 years ($/hr) | None | Steady-state, single instance family in a region |
| Reserved (Standard) | Up to 72% | 1 or 3 years | None | Fixed instance type, region, predictable usage |
| Reserved (Convertible) | Up to 54% | 1 or 3 years | None | Steady-state with flexibility to change instance family |
| Spot | Up to 90% | None | 2-minute notice | Fault-tolerant, interruptible, batch |

### 4.2 Reserved Instance Payment Options

| Payment Option | Upfront Cost | Monthly Cost | Total Discount |
|----------------|-------------|--------------|----------------|
| All Upfront | Highest | None | Highest |
| Partial Upfront | Medium | Lower than No Upfront | Medium |
| No Upfront | None | Highest (of RI options) | Lowest (still a discount vs. On-Demand) |

All three options are cheaper than On-Demand for equivalent usage over the commitment period.

### 4.3 Spot Instance Architecture Patterns

Spot Instances are only appropriate for workloads designed to tolerate sudden interruption. Architectural patterns that enable Spot use:

- **Checkpointing**: Write progress to S3 or DynamoDB periodically so work can resume from the last checkpoint after interruption
- **Spot Fleet**: Launch a mix of instance types and Spot pools to reduce interruption probability
- **Mixed instance groups**: Configure Auto Scaling groups with a blend of On-Demand (baseline) and Spot (burst) capacity
- **Graceful shutdown**: Use the 2-minute interruption notice to save state and deregister from load balancers

### 4.4 SAA-C03 Pricing Scenarios

| Scenario | Correct Pricing Model |
|----------|----------------------|
| Nightly batch job, 6 hours, can be restarted | Spot Instances |
| 24/7 production web app, predictable traffic | Savings Plans or Standard Reserved |
| New application with unknown traffic pattern | On-Demand initially, move to Savings Plans after 3 months of data |
| Development environment used business hours only | On-Demand (or Reserved if usage is high enough) |
| Short-term project lasting 2 months | On-Demand |
| Large HPC cluster running monthly 48-hour simulations | Spot Fleet |
| Mission-critical database with no interruption tolerance | On-Demand or Reserved (NOT Spot) |

---

## Section 5: Auto Scaling Groups

### 5.1 Launch Template vs. Launch Configuration

| Feature | Launch Template | Launch Configuration |
|---------|----------------|---------------------|
| Versioning | Yes (multiple named versions) | No |
| Spot instance diversification | Yes | No |
| T-instance CPU credit specification | Yes | No |
| Dedicated host configuration | Yes | No |
| AWS recommendation | Preferred — use for all new ASGs | Deprecated |
| Can be modified after creation | Yes (create new version) | No (immutable) |

Always use launch templates. Launch configurations are a legacy feature and do not support new EC2 capabilities.

### 5.2 Scaling Policy Comparison

| Policy Type | How It Works | Best For | Configuration Effort |
|-------------|-------------|----------|---------------------|
| Target Tracking | Maintains a metric at a target value (e.g., CPU at 50%) | Most workloads — recommended default | Low |
| Step Scaling | Different actions at different alarm threshold breaches | When granular control over scaling steps is needed | Medium |
| Scheduled Scaling | Pre-defined capacity changes at specified times | Known recurring traffic patterns | Low |
| Predictive Scaling | ML-based forecast of future demand, proactive scaling | Cyclical workloads with consistent patterns | Low (setup), ML-managed |
| Simple Scaling | Single action when alarm fires, then cooldown | Legacy — superseded by Target Tracking | Low |

### 5.3 Auto Scaling Health Checks

Auto Scaling can use two sources for health checks:

- **EC2 health check**: Considers an instance unhealthy if it is stopped, terminated, or its status check fails. This is the default.
- **ELB health check**: Also considers the Elastic Load Balancer's health check result. If the load balancer marks the instance as unhealthy (application-level failure), Auto Scaling will replace it. This is recommended for web-tier ASGs behind a load balancer.

Always enable ELB health checks for Auto Scaling groups behind load balancers. EC2-only health checks will not detect application failures that the load balancer can detect.

### 5.4 ASG Termination Policy

The default termination policy when scaling in:

1. Select the AZ with the most instances
2. Within that AZ, select the instance with the oldest launch template or launch configuration
3. If a tie, select the instance closest to the next billing hour

This behavior helps balance AZs and ensures the fleet runs the most current launch template version.

---

## Section 6: Lifecycle Hooks

### 6.1 Lifecycle States

| State | Trigger | Wait Duration | Action |
|-------|---------|---------------|--------|
| Pending:Wait | Instance is launched, before InService | Up to 48 hours (default 1 hour) | Run pre-launch automation |
| Pending:Proceed | CompleteLifecycleAction called with CONTINUE | Immediate | Instance moves to InService |
| Terminating:Wait | Instance selected for termination, before actual termination | Up to 48 hours (default 1 hour) | Run pre-termination automation |
| Terminating:Proceed | CompleteLifecycleAction called with CONTINUE | Immediate | Instance proceeds to Terminated |

If the lifecycle hook times out without receiving a CompleteLifecycleAction signal, the default action is ABANDON (instance is terminated during launch) or CONTINUE (instance proceeds to termination). Configure the default action based on your requirements.

### 6.2 Lifecycle Hook Integration Patterns

```
Pattern 1 — Launch Hook with Lambda:
  ASG launches instance
    → Instance enters Pending:Wait
    → EventBridge rule matches lifecycle event
    → Lambda function triggered
    → Lambda: installs agents, pulls config from Parameter Store
    → Lambda calls CompleteLifecycleAction (CONTINUE)
    → Instance enters InService

Pattern 2 — Termination Hook with Lambda:
  ASG selects instance for termination
    → Instance enters Terminating:Wait
    → EventBridge rule matches lifecycle event
    → Lambda function triggered
    → Lambda: ships logs to S3, deregisters from service discovery
    → Lambda calls CompleteLifecycleAction (CONTINUE)
    → Instance is terminated
```

---

## Section 7: SAA-C03 Exam Tips for Module 07

**Exam Tip 1 — Instance family triggers:**
Match workload keywords to instance families. "CPU-intensive" → C-family. "Large in-memory" → R-family. "SAP HANA" → X-family. "High IOPS low latency local storage" → I-family. "GPU machine learning training" → P-family. "Burst workload, variable CPU" → T-family.

**Exam Tip 2 — Spot never for stateful critical workloads:**
Spot is only correct when the scenario explicitly states the workload is fault-tolerant, interruptible, or can be restarted. If the scenario mentions "critical," "stateful," "cannot be interrupted," or "production database," Spot is the wrong answer.

**Exam Tip 3 — Savings Plans vs. Reserved:**
Savings Plans are more flexible than Reserved Instances. If the scenario involves multiple instance types, regions, or also includes Lambda or Fargate, Compute Savings Plans is the better answer. If the scenario is a fixed single instance type in a single region with maximum discount, Standard Reserved is the answer.

**Exam Tip 4 — Launch templates, not launch configurations:**
Any question that asks about Auto Scaling configuration should reference launch templates. If a distractor answer offers "launch configuration," it is likely wrong for any scenario involving modern EC2 features.

**Exam Tip 5 — Lifecycle hooks for pre-launch and pre-termination automation:**
If a scenario describes running a script before an instance accepts traffic or before an instance is destroyed, the answer involves lifecycle hooks. Keywords: "before termination," "before InService," "drain connections," "upload logs before shutdown."

**Exam Tip 6 — ELB health checks for web tiers:**
For ASGs behind a load balancer, always enable ELB health checks in addition to EC2 health checks. EC2 health checks alone cannot detect application-level failures.

**Exam Tip 7 — Spread placement group limit:**
The maximum is 7 instances per Availability Zone for spread placement groups. If a scenario requires more than 7 isolated instances per AZ, spread groups cannot meet the requirement — consider Partition instead.

**Exam Tip 8 — AMIs are regional:**
AMIs must be copied to each target region before they can be used to launch instances in that region. Cross-region AMI copy is always required for multi-region deployments based on a single golden image.

---

## Section 8: Key CLI Commands

Describe all EC2 instance types in a region:

```bash
aws ec2 describe-instance-types \
  --filters "Name=instance-type,Values=m6g.*" \
  --query "InstanceTypes[*].{Type:InstanceType,vCPU:VCpuInfo.DefaultVCpus,Memory:MemoryInfo.SizeInMiB}" \
  --output table
```

Create a launch template:

```bash
aws ec2 create-launch-template \
  --launch-template-name MyAppTemplate \
  --version-description "v1" \
  --launch-template-data '{
    "ImageId": "ami-0abcdef1234567890",
    "InstanceType": "m6g.large",
    "SecurityGroupIds": ["sg-0123456789abcdef0"],
    "IamInstanceProfile": {"Name": "MyInstanceProfile"},
    "UserData": "IyEvYmluL2Jhc2g="
  }'
```

Create an Auto Scaling group:

```bash
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name MyASG \
  --launch-template "LaunchTemplateName=MyAppTemplate,Version=1" \
  --min-size 2 \
  --max-size 10 \
  --desired-capacity 4 \
  --availability-zones us-east-1a us-east-1b us-east-1c \
  --health-check-type ELB \
  --health-check-grace-period 300
```

Put a scaling policy (Target Tracking):

```bash
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name MyASG \
  --policy-name TargetTrackingCPU50 \
  --policy-type TargetTrackingScaling \
  --target-tracking-configuration '{
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    },
    "TargetValue": 50.0
  }'
```

Create a lifecycle hook:

```bash
aws autoscaling put-lifecycle-hook \
  --auto-scaling-group-name MyASG \
  --lifecycle-hook-name MyTerminationHook \
  --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING \
  --heartbeat-timeout 300 \
  --default-result CONTINUE
```

---

## Section 9: Study Checklist

- [ ] Name the EC2 instance family for each workload type: web server, SAP HANA, Hadoop, ML training, batch processing
- [ ] Explain the CPU credit mechanism for T-family instances and when credits are earned vs. spent
- [ ] Describe the golden image AMI workflow in sequence from base instance to Auto Scaling group deployment
- [ ] Compare Cluster, Spread, and Partition placement groups on goal, instance limit, and blast radius
- [ ] Explain the difference between Compute Savings Plans and EC2 Instance Savings Plans
- [ ] Describe when Spot Instances are and are not appropriate, with an architectural pattern that enables Spot use
- [ ] Compare launch templates and launch configurations; explain why launch templates are preferred
- [ ] Describe the four Auto Scaling scaling policy types and identify the recommended default
- [ ] Explain Auto Scaling health check types and when to enable ELB health checks
- [ ] Describe lifecycle hooks: which states they intercept, common use cases, and how to signal completion
- [ ] Run the CLI commands in Section 8 and record the output in your lab notes
- [ ] Complete the Module 07 quiz with a score of at least 80 percent

---

## References

All AWS certification study materials and exam registration: <aws.amazon.com/certification>

---

## 9. Supplemental Resources

**1. AWS Documentation — Amazon EC2 Auto Scaling Lifecycle Hooks**
https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html
Detailed guide on Auto Scaling lifecycle hooks covering launch and termination transitions, heartbeat timeouts, default results, and integration with Lambda and SNS for custom automation.

**2. AWS Skill Builder — Amazon EC2 Auto Scaling Deep Dive**
https://skillbuilder.aws/learn/course/external/view/elearning/656/amazon-ec2-auto-scaling-deep-dive
Free course covering Auto Scaling scaling policies (Target Tracking, Step, Scheduled, Predictive), launch templates, instance refresh, and warm pools — directly aligned to Module 07 advanced topics.

**3. AWS Documentation — EC2 Instance Types Overview**
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html
Official reference for all EC2 instance families including compute, memory, storage, accelerated computing, and network-optimized types — with vCPU counts, memory, and use case descriptions for SAA-C03 instance selection questions.

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
