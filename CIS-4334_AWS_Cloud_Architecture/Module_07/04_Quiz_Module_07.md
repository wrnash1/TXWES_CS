# Quiz: Module 07 — Amazon EC2 and Auto Scaling

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A genomics company needs to run large-scale protein folding simulations. Each simulation requires 64 vCPUs with intensive parallel computation and low latency between compute nodes. The simulation runs for 12–24 hours. Which EC2 configuration is MOST appropriate?

A. R6g.16xlarge instances in a Spread placement group

B. C6g.16xlarge instances in a Cluster placement group

C. M6i.16xlarge instances with no placement group

D. I3.16xlarge instances in a Partition placement group

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. R-family is memory-optimized; protein folding simulations are CPU-intensive, not memory-heavy. Spread groups maximize fault isolation but add latency, not reduce it.
- B is correct. C-family (Compute Optimized) provides the highest CPU-to-memory ratio. Cluster placement group delivers the lowest inter-node network latency required for parallel HPC workloads. Graviton processors provide price-performance advantage.
- C is incorrect. M-family is balanced general purpose, not optimized for compute-intensive workloads. No placement group wastes the potential for low-latency inter-node communication.
- D is incorrect. I3 is Storage Optimized for high-IOPS workloads. Partition groups are for large distributed systems, not tightly-coupled HPC.

---

### Question 2

A company's Auto Scaling group is configured with minimum 2, maximum 10, and desired 4 instances. A Target Tracking policy is set to maintain average CPU at 60%. CPU climbs to 85% for 5 minutes. What action does Auto Scaling take?

A. Terminates instances to reduce CPU load

B. Launches additional instances until average CPU returns to approximately 60%

C. Does nothing because the desired capacity is already set to 4

D. Sends a notification but does not change instance count until manually approved

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Scaling in (terminating instances) would increase CPU per instance, making the problem worse. Auto Scaling scales out when CPU exceeds the target.
- B is correct. Target Tracking scaling automatically calculates how many instances to add to bring the average CPU back to the target value of 60%. The ASG increases desired capacity and launches new instances up to the maximum of 10.
- C is incorrect. Target Tracking overrides the static desired capacity by adjusting it dynamically in response to metric changes.
- D is incorrect. Target Tracking scaling policies act automatically without manual approval.

---

### Question 3

A company runs a content rendering farm. Render jobs take 2–4 hours each and can be re-submitted if an instance is lost. The farm runs hundreds of instances simultaneously only during business hours on weekdays. Which EC2 pricing model minimizes cost?

A. On-Demand Instances

B. Standard Reserved Instances with 3-year No Upfront

C. Spot Instances

D. Compute Savings Plans

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. On-Demand provides no discount and is the most expensive option for this volume of compute.
- B is incorrect. Reserved Instances commit to continuous usage. A workload that only runs during business hours on weekdays has very low utilization relative to a 3-year commitment, making it inefficient.
- C is correct. The workload is fault-tolerant (jobs can be re-submitted), runs in large batches, and is a textbook Spot use case. Spot provides up to 90% discount for interruptible workloads.
- D is incorrect. Savings Plans are for continuous steady-state workloads. They provide continuous discounts, not batch discounts. Spot remains cheaper for fault-tolerant workloads.

---

### Question 4

An engineer needs to ensure a new EC2 instance installs application monitoring agents and verifies connectivity to a configuration database before it begins receiving traffic from the load balancer. Which feature enables this?

A. EC2 User Data script executed at boot

B. Auto Scaling warm pool

C. Auto Scaling launch lifecycle hook (EC2_INSTANCE_LAUNCHING)

D. Load balancer health check grace period

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. User Data scripts run at boot but the instance still enters InService after the health check grace period regardless of script completion. There is no mechanism to hold the instance in Pending:Wait based on script success or failure.
- B is incorrect. Warm pools pre-initialize instances to reduce launch latency but do not provide a mechanism to gate InService entry on application-level verification.
- C is correct. A launch lifecycle hook puts the instance in Pending:Wait state, allowing automation via Lambda triggered by EventBridge to run the monitoring agent installation and connectivity verification. Only after CompleteLifecycleAction(CONTINUE) does the instance enter InService.
- D is incorrect. The grace period delays health check evaluation, not InService entry. It does not gate on custom script execution.

---

### Question 5

An architect is designing an EC2 deployment for three critical components: a primary RDS database proxy, a secondary standby database proxy, and a bastion host. The requirement is that a single hardware failure must never affect more than one component. All three instances must be in the same AWS Region. Which placement group is MOST appropriate?

A. Cluster placement group

B. Partition placement group with three partitions

C. Spread placement group

D. No placement group required

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Cluster groups intentionally pack instances on the same hardware for low latency, maximizing the blast radius of any hardware failure.
- B is incorrect. Partition groups are designed for large distributed systems. Three instances is below the minimum where partitions add value over spread groups. Spread is simpler and more appropriate for this small set.
- C is correct. Spread placement groups place each instance on completely separate hardware (separate rack, power, and network). Three instances is well within the 7-per-AZ limit. A single hardware failure can only affect one of the three instances.
- D is incorrect. Without a placement group, AWS may place multiple instances on the same underlying hardware, violating the isolation requirement.

---

### Question 6

A company has used Standard Reserved Instances for their EC2 fleet for three years. Their architecture is shifting from a fixed instance type to a mix of instance families and will also start using AWS Lambda functions. Which option provides the MOST flexible discount going forward?

A. Convertible Reserved Instances

B. Compute Savings Plans

C. EC2 Instance Savings Plans

D. Scheduled Reserved Instances

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Convertible Reserved Instances allow exchanging for different EC2 instance types but do not apply to Lambda or Fargate. They also require manual exchange actions.
- B is correct. Compute Savings Plans apply automatically across all EC2 instance types, sizes, regions, and operating systems, as well as AWS Lambda and AWS Fargate. They provide the broadest coverage for a mixed and evolving architecture.
- C is incorrect. EC2 Instance Savings Plans are scoped to a specific instance family in a specific region. They offer the same maximum discount as Standard Reserved but without cross-family flexibility and without Lambda coverage.
- D is incorrect. Scheduled Reserved Instances are a legacy feature for known recurring schedules and do not address the flexibility or Lambda coverage requirements.

---

### Question 7

An Auto Scaling group is configured with EC2 health checks only. An application bug causes an instance to return HTTP 500 errors for all requests while the EC2 instance itself remains running and passes its system status check. What happens?

A. Auto Scaling immediately replaces the unhealthy instance

B. Auto Scaling does not replace the instance because the EC2 health check passes

C. The load balancer terminates the instance directly

D. CloudWatch automatically triggers a scale-in event

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Auto Scaling can only replace the instance automatically if it is configured with ELB health checks. EC2-only health checks cannot detect application-level failures.
- B is correct. The EC2 health check only evaluates whether the underlying EC2 instance hardware and operating system are functional. An application returning HTTP 500 does not fail the EC2 status check. With EC2-only health checks, Auto Scaling considers this instance healthy.
- C is incorrect. Load balancers stop sending traffic to unhealthy targets but cannot terminate EC2 instances directly.
- D is incorrect. CloudWatch alarms can trigger scaling policies but will not automatically identify and replace individual unhealthy instances based on application response codes.

---

### Question 8

A company creates a custom AMI from a configured EC2 instance in us-east-1. They want to launch identical instances in eu-west-1. What step is required?

A. Share the AMI with the eu-west-1 region using AMI permissions

B. Copy the AMI to eu-west-1 using the CopyImage API

C. Export the AMI to an S3 bucket and import it in eu-west-1

D. Use the same AMI ID in eu-west-1 because AMI IDs are globally unique

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. AMI sharing (making an AMI public or sharing with another account) does not make it available in a different region. Sharing controls access, not region availability.
- B is correct. AMIs are regional resources. The CopyImage API replicates the AMI and its underlying EBS snapshots to the target region. The copied AMI receives a new region-specific AMI ID.
- C is incorrect. VM Import/Export exists for migrating on-premises VMs to AWS. It is not the correct method for copying an existing AWS AMI between regions. CopyImage is the purpose-built operation.
- D is incorrect. AMI IDs are region-specific, not globally unique. The same AMI ID does not exist in a different region.

---

### Question 9

An Auto Scaling group has a scheduled scaling policy that sets desired capacity to 8 at 8:00 AM and back to 2 at 6:00 PM every weekday. The business also wants to handle unexpected traffic spikes above the 8-instance level. Which combination BEST meets this requirement?

A. Two Scheduled Scaling policies only

B. Two Scheduled Scaling policies and one Target Tracking policy

C. One Predictive Scaling policy only

D. Two Step Scaling policies triggered by CloudWatch alarms

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Scheduled scaling handles the known pattern but provides no mechanism to scale beyond 8 instances if demand unexpectedly spikes above what 8 instances can handle.
- B is correct. Scheduled scaling manages the predictable daily pattern. Target Tracking adds a dynamic layer that can scale beyond 8 instances if unexpected demand exceeds the target metric value. Multiple scaling policy types can coexist on the same ASG.
- C is incorrect. Predictive Scaling uses historical patterns to forecast and pre-scale. It requires historical data and may not respond well to truly unexpected spikes. It also does not give the clean time-based 8-instance floor.
- D is incorrect. Step Scaling alone could handle spikes but does not provide the clean time-based capacity changes that Scheduled Scaling provides for the known daily pattern.

---

### Question 10

A developer asks why they should use a launch template instead of a launch configuration when creating a new Auto Scaling group. Which TWO reasons are MOST accurate? (Select TWO)

A. Launch templates support versioning; launch configurations are immutable

B. Launch configurations support Spot instance diversification; launch templates do not

C. Launch templates can specify T-instance CPU credit options; launch configurations cannot

D. Launch configurations are required for ELB integration; launch templates are not

**Correct Answer: A and C**

**Distractor Analysis:**

- A is correct. Launch templates support multiple named versions, allowing configuration updates and rollbacks. Launch configurations cannot be modified after creation.
- B is incorrect. This is backwards. Launch templates support Spot instance diversification. Launch configurations do not support this feature.
- C is correct. Launch templates support T-instance CPU credit specification (standard vs. unlimited mode). Launch configurations do not expose this option.
- D is incorrect. Both launch templates and launch configurations can be used with Elastic Load Balancing. ELB integration is configured at the ASG level.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
