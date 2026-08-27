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

---

### Question 11 (5 points)

A company runs a stateful web application on EC2 instances behind an ALB. Users report being logged out when requests route to different instances. Which ALB feature should the architect enable?

A. Path-based routing rules to pin each user to a dedicated target group

B. Sticky sessions using a duration-based ALB-generated cookie on the target group

C. AWS Global Accelerator endpoint weights to route each user to a fixed instance

D. Network Load Balancer with a static IP to maintain TCP session persistence

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Path-based routing directs traffic based on URL path patterns, not individual user identity. It cannot bind a specific user to a specific instance.
- B is correct. ALB sticky sessions use a load balancer-generated cookie to bind a user's session to a specific target instance for the stickiness duration. This preserves server-side session state across requests from the same user.
- C is incorrect. Global Accelerator routes traffic to the nearest healthy endpoint at the ALB or EC2 level using Anycast IPs. It does not provide per-user instance affinity within an ALB target group.
- D is incorrect. NLBs operate at Layer 4 (TCP/UDP) and do not support HTTP-layer session stickiness. Switching from ALB to NLB would lose HTTP routing capabilities needed for a web application.

---

### Question 12 (5 points)

A company wants to pre-provision EC2 capacity 45 minutes before a known daily peak traffic event at 9 AM. Reactive scaling policies add capacity too slowly. Which Auto Scaling feature directly addresses this requirement?

A. Target Tracking scaling based on RequestCountPerTarget

B. Step Scaling with multiple CloudWatch alarms at increasing CPU thresholds

C. Scheduled Scaling with a scheduled action set to increase desired capacity at 8:15 AM daily

D. Predictive Scaling with a 24-hour forecast horizon

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Target Tracking is reactive — it responds to observed metric values. It cannot provision capacity before the actual spike because it only acts after the metric exceeds the target.
- B is incorrect. Step Scaling is reactive. It fires when CloudWatch alarms breach CPU thresholds, meaning it adds capacity during the spike, not before it.
- C is correct. Scheduled Scaling configures Auto Scaling to change the desired capacity at a specific date and time using a cron expression. Setting the action to fire at 8:15 AM daily ensures capacity is available 45 minutes before the 9 AM peak event.
- D is incorrect. Predictive Scaling uses machine learning to forecast load based on historical CloudWatch metrics and pre-scales automatically. For a known fixed-time daily event, Scheduled Scaling is simpler and more deterministic. Predictive Scaling is better for variable workload patterns.

---

### Question 13 (5 points)

An architect is reviewing EC2 purchasing options for a batch analytics workload that runs for 6 hours every Saturday night and can tolerate interruptions with checkpointing. The team has a budget constraint and wants maximum cost reduction. Which purchasing model minimizes cost for this workload?

A. On-Demand Instances

B. 1-year All Upfront Reserved Instances for the weekend batch cluster

C. Spot Instances with checkpointing logic to resume from the last checkpoint on interruption

D. Dedicated Hosts with a 1-year commitment for exclusive hardware

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. On-Demand pricing is the most expensive per-hour option and provides no discount for workloads that can tolerate interruption.
- B is incorrect. Reserved Instances provide a 40% discount for steady-state continuous usage. At 6 hours per week (3.6% utilization), the RI commitment is paid for mostly idle capacity, making On-Demand with stop/start cheaper than an RI.
- C is correct. Spot Instances provide up to 90% discount versus On-Demand. Batch analytics workloads that can checkpoint progress and resume after interruption are the canonical Spot Instance use case. The combination of interrupt-tolerance, checkpointing, and large compute make Spot the maximum cost reduction option.
- D is incorrect. Dedicated Hosts provide exclusive physical server access for per-socket or per-core software licensing. They are the most expensive EC2 option and have no benefit for a batch analytics workload without licensing constraints.

---

### Question 14 (5 points)

An EC2 instance family comparison is needed. A workload runs intensive video transcoding that is heavily CPU-bound with medium memory requirements. The job runs for 2-4 hours continuously. Which EC2 instance family is MOST appropriate?

A. R6i — memory optimized

B. I3 — storage optimized

C. C6i — compute optimized

D. T3 — burstable general purpose

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. R-family instances are memory-optimized with high memory-to-vCPU ratios. Video transcoding is a CPU-intensive workload, not memory-intensive. R-family instances are over-provisioned on memory and under-optimized for sustained CPU.
- B is incorrect. I3 instances are storage-optimized with locally attached NVMe SSDs for high-IOPS workloads. Video transcoding performance is bounded by CPU, not disk IOPS.
- C is correct. C-family (Compute Optimized) instances provide the highest CPU-to-memory ratio and are specifically designed for compute-intensive workloads such as video encoding, scientific modeling, and high-performance batch processing. C6i instances offer Intel Ice Lake processors with up to 3.5 GHz sustained turbo frequency.
- D is incorrect. T3 instances use a CPU credit model and are designed for workloads with low-to-moderate average CPU utilization with occasional spikes. A 2-4 hour sustained CPU-intensive transcoding job will exhaust T3 CPU credits quickly and throttle to baseline performance.

---

### Question 15 (5 points)

An architect is designing EC2 placement for 100 instances running a distributed Kafka cluster. Kafka partitions data across brokers, and the primary concern is that a single hardware failure should not take down more than a few brokers simultaneously. Which placement group type is MOST appropriate?

A. Cluster placement group

B. Spread placement group

C. Partition placement group

D. No placement group with Enhanced Networking enabled

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Cluster placement groups pack instances onto the same hardware for the lowest inter-node latency. This maximizes performance but concentrates instances — a single hardware failure could take down many Kafka brokers simultaneously.
- B is incorrect. Spread placement groups place each individual instance on separate hardware, providing maximum fault isolation per instance. However, Spread groups are limited to 7 instances per AZ per placement group — insufficient for 100 instances.
- C is correct. Partition placement groups divide instances into logical partitions, where each partition runs on separate hardware racks with separate power and network. Kafka is designed to distribute partition replicas across brokers, and placement group partitions map directly to Kafka's failure isolation requirement. Partition groups support hundreds of instances per group.
- D is incorrect. Without a placement group, instances are placed by AWS based on capacity availability. There is no guarantee that instances are distributed across separate failure domains. For a large distributed system like Kafka, partition placement groups provide the needed fault isolation guarantee.

---

### Question 16 (5 points)

A solutions architect needs to choose between EC2 Instance Savings Plans and Compute Savings Plans for a company that has committed to 3 years of steady EC2 usage but expects to change instance families and Regions over that period. Which plan provides greater flexibility?

A. EC2 Instance Savings Plans because they provide the highest possible EC2 discount

B. Compute Savings Plans because they apply across any EC2 instance family, size, OS, Region, Lambda, and Fargate

C. Reserved Instances because they can be exchanged for different instance types using the Convertible RI option

D. There is no difference in flexibility between the two Savings Plan types

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. EC2 Instance Savings Plans provide a higher discount (up to 72%) but are locked to a specific instance family in a specific Region. If the team changes instance families or Regions, the plan does not automatically apply. Maximum discount at the cost of flexibility.
- B is correct. Compute Savings Plans apply to any EC2 usage (any family, size, OS, tenancy) and also cover Lambda and Fargate, across all Regions. They provide up to 66% discount with maximum flexibility — the team can migrate workloads to new instance families or Regions without losing the commitment discount.
- C is incorrect. Convertible RIs can be exchanged for different instance types, but the exchange process requires manual action and involves specific size/region constraints. Compute Savings Plans are more flexible and require no management of exchanges.
- D is incorrect. The two Savings Plan types differ significantly in flexibility and discount level. EC2 Instance Savings Plans are locked to an instance family and Region; Compute Savings Plans are flexible across all EC2 parameters.

---

### Question 17 (5 points)

An Auto Scaling group uses ELB health checks. An EC2 instance passes the EC2 status check (shows "ok") but fails the ALB health check for 3 consecutive periods. What action does Auto Scaling take?

A. Marks the instance as Unhealthy and terminates it, launching a replacement

B. Removes the instance from the ALB target group but keeps it running in the ASG

C. Sends a CloudWatch metric alert but takes no automated action without a CloudWatch Alarm

D. Waits for the EC2 status check to also fail before marking the instance as Unhealthy

**Correct Answer: A**

**Distractor Analysis:**

- A is correct. When ELB health checks are enabled on an Auto Scaling group, ASG uses the ALB health check result as the instance health status. An instance failing the ALB health check for the unhealthy threshold number of consecutive periods is marked Unhealthy by Auto Scaling, which then terminates the instance and launches a replacement — even if EC2 status checks pass.
- B is incorrect. ALB automatically deregisters unhealthy instances from routing (stops sending traffic), but Auto Scaling with ELB health checks enabled will also terminate the unhealthy instance, not just deregister it.
- C is incorrect. Auto Scaling with ELB health checks enabled acts automatically based on the ALB health check result. No additional CloudWatch Alarm is required for ASG to take the replacement action.
- D is incorrect. When ELB health check type is configured on the ASG, the ELB health check result is authoritative. A failed ELB health check triggers replacement regardless of whether the EC2 system status check is passing.

---

### Question 18 (5 points)

A company runs a three-tier web application with an ALB and an Auto Scaling group. The operations team wants to deploy an application update with zero downtime and the ability to immediately roll back if the new version causes errors. Which deployment strategy accomplishes this?

A. Rolling update: terminate and replace instances one by one in the same Auto Scaling group

B. Blue/Green deployment: launch a new Auto Scaling group with the new version and shift ALB traffic gradually from the old target group to the new one

C. In-place update: use EC2 Systems Manager Run Command to update all instances simultaneously

D. Canary deployment using a single instance with the new version placed directly in the production target group

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Rolling updates replace instances gradually, but the old and new versions run in the same target group simultaneously. If the new version has critical bugs, rollback requires re-deploying the old version — not an immediate switch. The old instances are already terminated.
- B is correct. Blue/Green deployment maintains two complete environments — the old (blue) and new (green). ALB weighted target group routing shifts traffic from blue to green incrementally. If the new version fails, 100% traffic is immediately shifted back to the blue target group. The old environment remains intact until the new version is fully verified.
- C is incorrect. In-place updates on all instances simultaneously create downtime during the update window and have no rollback mechanism other than re-running the update with the old version. This does not meet the zero-downtime requirement.
- D is incorrect. A single canary instance in production sends a small percentage of real user traffic to the new version, which can detect issues early. However, immediate full rollback is not instant — it requires removing the canary instance. B/G is better for immediate rollback capability.

---

### Question 19 (5 points)

A company uses an Auto Scaling group and notices that instances are frequently cycling — new instances are launched, then terminated shortly after, then launched again. The Target Tracking policy is set to 50% CPU. What is the MOST LIKELY cause of this scaling churn?

A. The Auto Scaling group minimum and maximum are set to the same value

B. The cooldown period is set too short, allowing new scaling activities to trigger before metrics stabilize after a previous scaling event

C. The EC2 instances are using T3 burstable performance, which causes erratic CPU metrics

D. The Target Tracking policy is configured with a PredefinedMetricType that is incompatible with the instance type

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. If minimum equals maximum, the ASG cannot change instance count at all — there would be no scaling activity, not scaling churn.
- B is correct. The cooldown period prevents Auto Scaling from launching or terminating additional instances for a specified time after a scaling activity completes. If the cooldown is too short, the ASG may respond to metric values measured immediately after the last scale-out (when the new instances have not yet received their share of traffic and CPU appears artificially high), triggering another scale-out followed by scale-in once load redistributes — creating a churn cycle.
- C is incorrect. T3 instances do have variable CPU behavior due to credit-based performance, but the question describes a churn pattern specifically linked to scaling activity, which points to cooldown configuration rather than instance type.
- D is incorrect. Target Tracking with ASGAverageCPUUtilization is compatible with all EC2 instance types. There is no incompatibility between PredefinedMetricType and instance type.

---

### Question 20 (5 points)

An architect is designing an EC2-based application that requires the operating system and application to be pre-configured before any instance enters service in the Auto Scaling group. The configuration process involves installing agents, running compliance checks, and registering with a service discovery system — taking up to 8 minutes total. Which approach BEST ensures no traffic reaches an instance before configuration is complete?

A. Set the EC2 instance warm-up period to 8 minutes in the Auto Scaling group settings

B. Configure a lifecycle hook on the autoscaling:EC2_INSTANCE_LAUNCHING transition; the hook holds the instance in pending:wait state until the configuration script completes and calls CompleteLifecycleAction

C. Use a longer UserData script that sleeps for 8 minutes before completing to delay instance readiness

D. Set the ALB health check grace period to 8 minutes so the ALB does not check the instance until configuration completes

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The EC2 instance warm-up period delays the inclusion of the instance's metrics in target tracking calculations, but the instance enters InService status and can receive traffic as soon as it passes health checks. The warm-up does not hold the instance out of the InService state.
- B is correct. A lifecycle hook with the EC2_INSTANCE_LAUNCHING transition holds the instance in the pending:wait state after launch. The configuration script runs, performs all required setup, and then calls the CompleteLifecycleAction API with CONTINUE. Only after this call does the instance transition to InService and begin receiving ALB traffic. This guarantees no traffic reaches the instance before configuration is complete.
- C is incorrect. A UserData sleep does delay script completion but the instance still enters InService status when health checks pass — which may occur before the sleep completes if the application port is already listening. This is not a reliable mechanism for sequencing configuration completion with traffic routing.
- D is incorrect. The ALB health check grace period delays when the ALB begins health-checking a new instance, preventing premature unhealthy marking during startup. It does not hold the instance out of InService status or prevent all traffic routing. Traffic can still be sent to the instance by the ALB before the grace period expires if the health check finds the instance healthy.

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
