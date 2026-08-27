# Quiz: Module 03 - EC2: Instance Types, Auto Scaling, and Load Balancing

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Questions:** 10

---

## Question 1

A solutions architect needs to choose an EC2 instance type for an in-memory database that must hold 300 GB of active data in RAM with consistent, sustained performance throughout the day. Which instance family is most appropriate?

- A) C5 — compute optimized
- B) T3 — burstable general purpose
- C) R6i — memory optimized
- D) I3 — storage optimized

### Answer 1

Correct Answer: C

### Explanation 1

- A is incorrect: C5 instances are compute optimized with a high CPU-to-memory ratio. They are not designed for workloads that require very large amounts of RAM.
- B is incorrect: T3 instances are burstable and provide only moderate amounts of memory. They are inappropriate for 300 GB in-memory requirements, and their CPU performance degrades under sustained load.
- C is correct: R-family (memory optimized) instances provide the largest memory-to-CPU ratios in the general-purpose memory category. R6i instances offer up to terabytes of RAM and are specifically designed for in-memory databases, real-time analytics, and SAP HANA workloads.
- D is incorrect: I3 instances are storage optimized for high-IOPS local NVMe storage. They are appropriate for NoSQL databases requiring fast local I/O, not for in-memory data platforms.

---

## Question 2

A company runs a web application with steady, predictable traffic 24 hours a day, 7 days a week. The architecture uses 10 M5.xlarge instances continuously. The company wants to reduce costs with the lowest commitment that guarantees this capacity. Which purchasing option provides the maximum discount?

- A) Spot Instances
- B) On-Demand Instances
- C) Standard Reserved Instances with a 3-year term
- D) Savings Plans with a 1-year Compute commitment

### Answer 2

Correct Answer: C

### Explanation 2

- A is incorrect: Spot Instances offer the highest discount (up to 90%) but can be interrupted with only 2 minutes notice. A 24/7 production web application cannot tolerate arbitrary interruptions.
- B is incorrect: On-Demand is the most expensive option with no discount. It is appropriate for unpredictable or short-term workloads, not steady-state 24/7 production systems.
- C is correct: Standard Reserved Instances with a 3-year term offer up to 72% discount over On-Demand for a specific instance type in a specific Region. For a steady 24/7 workload that will use the same instance type for years, this provides the maximum discount.
- D is incorrect: Savings Plans also provide significant discounts (up to 66% for Compute Savings Plans) but slightly less than Standard Reserved Instances for a specific committed type and Region. The question asks for maximum discount on a fixed, known instance type.

---

## Question 3

An Auto Scaling Group is configured with a target tracking scaling policy targeting 60% average CPU utilization. The application experiences a sudden traffic spike and CPU rises to 90% across all instances. The ASG is currently at minimum capacity of 2 and maximum capacity of 10. What is the correct expected behavior?

- A) The ASG terminates instances to reduce load on the CPU
- B) The ASG immediately launches 10 new instances to reach maximum capacity
- C) The ASG calculates the number of instances needed to bring average CPU toward 60% and launches that number, subject to the maximum capacity limit
- D) Nothing happens until a CloudWatch alarm is manually created for the CPU metric

### Answer 3

Correct Answer: C

### Explanation 3

- A is incorrect: When CPU is above the target threshold, the ASG scales out (adds instances), not in. Scale-in occurs when CPU drops below the target.
- B is incorrect: Target tracking scaling calculates the number of additional instances needed to move the metric toward the target value. It does not jump directly to maximum capacity unless the calculation determines that many instances are needed.
- C is correct: Target tracking automatically calculates the required capacity change to move the average CPU toward the 60% target. If scaling to 5 instances would bring average CPU to approximately 60%, the ASG launches 3 additional instances (from 2 to 5). The max capacity of 10 is the upper bound.
- D is incorrect: Target tracking scaling creates and manages the required CloudWatch alarms automatically. No manual alarm creation is needed.

---

## Question 4

A company needs a load balancer for a new microservices application. Different URL paths must be routed to different backend services — requests to `/api/orders` go to the Orders service, requests to `/api/inventory` go to the Inventory service. Which load balancer type supports this requirement?

- A) Network Load Balancer
- B) Gateway Load Balancer
- C) Application Load Balancer
- D) Classic Load Balancer

### Answer 4

Correct Answer: C

### Explanation 4

- A is incorrect: Network Load Balancer operates at Layer 4 (TCP/UDP). It routes based on port numbers, not URL paths. It cannot inspect HTTP path content.
- B is incorrect: Gateway Load Balancer is used to route traffic through third-party virtual appliances such as firewalls and intrusion detection systems. It does not support HTTP path-based routing for application microservices.
- C is correct: Application Load Balancer operates at Layer 7 and natively supports path-based routing rules. You create listener rules that match specific path patterns (e.g., `/api/orders/*`) and route matching requests to specific target groups.
- D is incorrect: Classic Load Balancer supports only simple round-robin routing without content-based rules. It is a legacy service and does not support path-based routing.

---

## Question 5

A gaming company needs a load balancer for their game server backend. The requirements are: handle millions of UDP connections per second with sub-millisecond latency, preserve the original client IP address for server-side logging, and provide a static IP address per Availability Zone that mobile game clients can hardcode in their firewall rules. Which load balancer is correct?

- A) Application Load Balancer with cross-zone load balancing enabled
- B) Network Load Balancer
- C) Gateway Load Balancer
- D) Application Load Balancer with Lambda target group

### Answer 5

Correct Answer: B

### Explanation 5

- A is incorrect: ALB does not support UDP traffic (only HTTP/HTTPS). ALB does not preserve source IP (it uses X-Forwarded-For). ALB does not provide static IP addresses per AZ.
- B is correct: NLB operates at Layer 4, supports UDP and TCP with millions of connections per second at sub-millisecond latency, preserves the source IP of clients, and provides one static IP per Availability Zone that can be assigned as Elastic IPs for client whitelisting.
- C is incorrect: GWLB is for inline traffic inspection through virtual appliances. It is not a user-facing application load balancer and does not serve game client connections.
- D is incorrect: ALB with Lambda targets routes HTTP requests to Lambda functions — not applicable to UDP gaming traffic.

---

## Question 6

An Auto Scaling Group has EC2 health checks configured. An application bug causes all instances to return HTTP 500 errors for all requests, but the EC2 instances themselves are running normally (passing EC2 status checks). What happens to the unhealthy instances?

- A) The ASG detects the HTTP 500 errors and terminates the unhealthy instances
- B) Nothing — the ASG only evaluates EC2 instance status, not application-level HTTP responses
- C) CloudWatch automatically creates an alarm and notifies the ASG to replace the instances
- D) The Application Load Balancer terminates the instances and requests the ASG to launch replacements

### Answer 6

Correct Answer: B

### Explanation 6

- A is incorrect: With only EC2 health checks configured, the ASG does not evaluate HTTP response codes. It only checks whether the EC2 instance is in a running state and passing system status checks.
- B is correct: EC2 health checks only verify that the instance is running and passing infrastructure-level status checks. Application-level failures (HTTP 500 errors) are invisible to the ASG when only EC2 health checks are enabled. This is why ELB health checks should always be enabled on ASGs attached to load balancers.
- C is incorrect: CloudWatch alarms require explicit configuration and do not automatically trigger ASG instance replacement based on HTTP error rates by default.
- D is incorrect: Load balancers stop routing traffic to unhealthy targets but do not have the authority to terminate EC2 instances or communicate instance replacement requests to the ASG.

---

## Question 7

A data processing company runs large batch jobs that process scientific simulation data. Each job takes 2-6 hours to complete and can be checkpointed and resumed from the last save point if interrupted. The jobs run continuously and the company wants the lowest possible cost. Which EC2 purchasing option should they use?

- A) On-Demand instances with Reserved Instances for the baseline
- B) Spot instances
- C) Dedicated Hosts with a 3-year reservation
- D) Standard Reserved Instances with partial upfront payment

### Answer 7

Correct Answer: B

### Explanation 7

- A is incorrect: On-Demand instances are the highest per-unit cost option. Adding Reserved Instances helps with steady-state baseline but does not maximize savings for interruptible batch jobs.
- B is correct: Spot Instances offer up to 90% discount over On-Demand. The batch jobs are fault-tolerant (they can be checkpointed and resumed), making them the ideal Spot workload. Interruptions simply cause the job to resume from the last checkpoint, and the massive cost savings justify this design.
- C is incorrect: Dedicated Hosts are for compliance and BYOL licensing scenarios. They are the most expensive option and are not appropriate for cost-driven batch processing.
- D is incorrect: Standard Reserved Instances provide commitment discounts for predictable steady-state workloads. They still pay for unused capacity if the batch jobs do not run continuously at full capacity, and they cost significantly more than Spot.

---

## Question 8

A solutions architect is configuring an Auto Scaling Group for a web application. The application experiences predictable traffic spikes every Monday morning at 9 AM when employees start work, and traffic drops on Friday evenings. Which scaling policy type is most appropriate for this pattern?

- A) Target tracking scaling with CPU utilization as the metric
- B) Step scaling with CloudWatch alarms for CPU thresholds at 60% and 80%
- C) Scheduled scaling to increase capacity before 9 AM on Monday and decrease it on Friday evening
- D) Predictive scaling using ML-based traffic forecasting

### Answer 8

Correct Answer: C

### Explanation 8

- A is incorrect: Target tracking scaling reacts to metrics after they change. On Monday morning, the application would experience degraded performance during the ramp-up while the ASG adds capacity reactively. It does not pre-scale before the known event.
- B is incorrect: Step scaling is also reactive — it adds capacity after CPU thresholds are breached. Like target tracking, it cannot pre-scale for a known scheduled event.
- C is correct: Scheduled scaling is designed exactly for predictable, time-based traffic patterns. You configure the ASG to increase minimum and desired capacity before 9 AM on Mondays and reduce it Friday evening. Capacity is ready before the spike arrives.
- D is incorrect: Predictive scaling uses ML to forecast load based on historical patterns. While it would eventually learn the Monday pattern, scheduled scaling is more precise, simpler to configure, and takes effect immediately without a training period.

---

## Question 9

A company is choosing between Standard Reserved Instances and Compute Savings Plans for their AWS workload. Their architecture uses EC2 M5 instances in us-east-1 for web servers, Lambda functions for data processing, and AWS Fargate for container workloads. They want the best discount while retaining flexibility. Which option is most appropriate?

- A) Standard Reserved Instances for M5 instances in us-east-1, and separate On-Demand pricing for Lambda and Fargate
- B) Compute Savings Plans covering EC2, Lambda, and Fargate with flexibility across instance families and Regions
- C) EC2 Instance Savings Plans for the M5 family in us-east-1 combined with Lambda Reserved Concurrency for Lambda
- D) Convertible Reserved Instances for EC2 plus Spot Instances for Lambda and Fargate

### Answer 9

Correct Answer: B

### Explanation 9

- A is incorrect: Standard Reserved Instances only cover the specific EC2 instance type they are purchased for. Lambda and Fargate are not covered, resulting in full On-Demand pricing for those services.
- B is correct: Compute Savings Plans apply a committed spend level across EC2 (any family, size, OS, tenancy), Lambda, and Fargate across all Regions. This provides up to 66% discount with maximum flexibility — the company can change instance families, move workloads between EC2 and Lambda, or change Regions without losing the discount.
- C is incorrect: EC2 Instance Savings Plans are more restrictive than Compute Savings Plans — they apply to a specific instance family in a specific Region. Lambda Reserved Concurrency is a concurrency limit, not a pricing commitment — it does not provide any cost discount.
- D is incorrect: Convertible Reserved Instances only cover EC2. Lambda and Fargate do not have Spot pricing — they are always On-Demand or Savings Plans eligible.

---

## Question 10

An application running on EC2 requires lifecycle management — specifically, when new instances are launched, a software agent must be installed and validated before the instance begins serving production traffic. Which Auto Scaling feature enables this behavior?

- A) Auto Scaling cooldown periods
- B) Launch Template user data scripts only
- C) Auto Scaling lifecycle hooks with a launch transition hook
- D) EC2 instance warm-up settings

### Answer 10

Correct Answer: C

### Explanation 10

- A is incorrect: Cooldown periods prevent Auto Scaling from launching or terminating additional instances for a specified time after a scaling activity. They do not pause an instance in a pre-service state for custom initialization.
- B is incorrect: User data scripts run at instance launch, but the instance enters InService status as soon as it passes health checks, regardless of whether the user data script has completed. There is no guarantee the agent is installed and validated before traffic arrives.
- C is correct: A lifecycle hook with the launch transition (autoscaling:EC2_INSTANCE_LAUNCHING) pauses the instance in a pending:wait state after launch. Custom automation can install and validate the agent, then call CompleteLifecycleAction with CONTINUE to move the instance to InService. Until that call is made, the ALB does not route traffic to the instance.
- D is incorrect: EC2 instance warm-up is a setting that tells Auto Scaling to wait a specified period before including a newly launched instance's metrics in target tracking calculations. It does not pause the instance in a pre-service state — the instance enters InService and begins receiving traffic as soon as health checks pass.

---

## Question 11

A company runs a stateful web application on EC2 instances behind an Application Load Balancer. Users report that they are being logged out when their requests are routed to different instances during peak traffic. Which ALB feature resolves this issue?

- A) ALB path-based routing rules that direct each user to a dedicated instance
- B) ALB sticky sessions (session affinity) using a load balancer-generated cookie
- C) EC2 Auto Scaling predictive scaling to prevent new instances from being added
- D) AWS Global Accelerator with endpoint weights to pin users to specific instances

### Answer 11

Correct Answer: B

### Explanation 11

- A is incorrect: Path-based routing rules direct requests based on URL path patterns (e.g., /api/* vs /static/*), not based on individual user identity. They cannot bind a specific user to a specific instance.
- B is correct: ALB sticky sessions use a load-balancer-generated cookie to bind a user's session to a specific target instance. Once bound, all subsequent requests from that user within the stickiness duration are routed to the same instance, preserving session state.
- C is incorrect: Preventing Auto Scaling from adding instances does not solve the root problem — users can still be routed to different existing instances on subsequent requests. Disabling scaling removes a key availability and performance feature.
- D is incorrect: AWS Global Accelerator routes traffic to the nearest healthy endpoint at the ALB or EC2 level, but it does not provide per-user instance affinity. It is not designed for session stickiness within an ALB target group.

---

## Question 12

An e-commerce company wants to handle a 10x traffic spike during an annual sale event. They want EC2 capacity to be available before the spike begins, not after Auto Scaling detects increased CPU utilization. Which Auto Scaling scaling policy type achieves this?

- A) Target Tracking scaling based on CPU utilization
- B) Simple Scaling policy triggered by a CloudWatch alarm at 70% CPU
- C) Scheduled Scaling with a scheduled action set to increase capacity 30 minutes before the sale starts
- D) Step Scaling policy with multiple CloudWatch alarms at 50%, 70%, and 90% CPU

### Answer 12

Correct Answer: C

### Explanation 12

- A is incorrect: Target Tracking is reactive — it monitors the current metric value and scales after the metric exceeds the target. It cannot provision capacity before a predicted spike because it relies on observed utilization data.
- B is incorrect: Simple Scaling is reactive. It fires after the CloudWatch alarm breaches a threshold, meaning capacity is being added during or after the traffic spike, not before it begins.
- C is correct: Scheduled Scaling configures Auto Scaling to change the desired capacity at a specific date and time. By setting a scheduled action 30 minutes before the anticipated sale traffic, the company proactively provisions capacity before any actual demand spike occurs.
- D is incorrect: Step Scaling is reactive, responding to increasing alarm thresholds as load rises. Like all metric-driven policies, it cannot add capacity before the metric actually increases due to real traffic.

---

## Question 13

A solutions architect needs to deploy a web application that serves users globally. The architecture requires the load balancer to inspect HTTP headers, route requests based on URL path and hostname, and redirect HTTP requests to HTTPS. Which AWS load balancer type supports all of these capabilities?

- A) Network Load Balancer (NLB)
- B) Classic Load Balancer (CLB)
- C) Application Load Balancer (ALB)
- D) Gateway Load Balancer (GWLB)

### Answer 13

Correct Answer: C

### Explanation 13

- A is incorrect: The NLB operates at Layer 4 (TCP/UDP). It does not inspect HTTP headers, does not support URL path-based routing, and does not perform HTTP-to-HTTPS redirects. NLB is optimized for ultra-low latency and high throughput TCP/UDP traffic.
- B is incorrect: The Classic Load Balancer is a legacy load balancer that supports both Layer 4 and basic Layer 7 features, but it does not support content-based routing rules or advanced redirect actions. AWS recommends migrating from CLB to ALB or NLB.
- C is correct: The ALB operates at Layer 7 (HTTP/HTTPS). It supports listener rules based on URL path (`/api/*`), hostname (`api.example.com`), HTTP headers, query strings, and source IP. It also supports redirect actions, including HTTP-to-HTTPS redirect, and fixed response actions.
- D is incorrect: The GWLB operates at Layer 3 and is designed to route traffic through third-party virtual network appliances (firewalls, intrusion detection systems). It does not perform application-layer routing or HTTP redirects.

---

## Question 14

An Auto Scaling group is configured with a minimum of 2, desired of 4, and maximum of 8 instances. The group has a Target Tracking policy set to 60% average CPU utilization. Current CPU is at 30% with 4 instances running. What action does Auto Scaling take?

- A) Auto Scaling adds instances to bring CPU utilization up to 60%
- B) Auto Scaling terminates instances until CPU reaches 60% or minimum of 2 is reached
- C) Auto Scaling maintains 4 instances because the cooldown period prevents scaling in
- D) Auto Scaling terminates all excess instances immediately to minimize cost

### Answer 14

Correct Answer: B

### Explanation 14

- A is incorrect: Auto Scaling does not add instances when CPU is below the target. Adding instances would further reduce per-instance CPU, moving further from the target.
- B is correct: When CPU utilization is below the target (30% vs 60% target), Target Tracking scales in (terminates instances) to bring CPU toward the target utilization. It will scale in until the average CPU approaches 60% or the minimum capacity of 2 is reached — whichever comes first.
- C is incorrect: While Auto Scaling does have scale-in cooldown settings, the question describes steady-state below target, which is the condition that drives scale-in. Cooldown periods prevent back-to-back scaling activities, not the initial scale-in response.
- D is incorrect: Target Tracking does not terminate all excess instances at once. It calculates the number of instances needed to achieve the target and terminates them incrementally according to its calculation.

---

## Question 15

A company needs to deploy an application that handles real-time financial transaction processing requiring guaranteed network performance with less than 1 millisecond latency between EC2 nodes. The workload requires 8 EC2 instances operating in tight coordination. Which EC2 placement group type is most appropriate?

- A) Partition placement group
- B) Spread placement group
- C) Cluster placement group
- D) No placement group with Enhanced Networking enabled

### Answer 15

Correct Answer: C

### Explanation 15

- A is incorrect: Partition placement groups spread instances across logical partitions on separate hardware racks, designed for large distributed workloads like Hadoop and Kafka where fault isolation between node groups is more important than inter-node latency.
- B is incorrect: Spread placement groups place each instance on separate underlying hardware, maximizing fault isolation. Each instance is on a different rack with a different power source. This maximizes availability but creates higher inter-instance latency compared to Cluster placement groups.
- C is correct: Cluster placement groups pack instances into a single AZ on the same or nearby hardware connected by high-bandwidth, low-latency networking. This configuration provides the lowest inter-instance network latency (sub-millisecond), which is required for the financial transaction processing workload described.
- D is incorrect: Enhanced Networking (ENA) reduces network latency and increases bandwidth for a single instance, but without a Cluster placement group, instances are distributed across the Availability Zone on hardware that may be physically distant from each other. Enhanced Networking alone does not guarantee sub-millisecond inter-instance latency.

---

## Question 16

An engineering team is reviewing EC2 purchasing options for a new application. The application is expected to run continuously for three years with predictable, steady-state compute requirements. The team wants the maximum possible discount compared to On-Demand pricing. Which EC2 purchasing option provides the highest discount?

- A) 1-year All Upfront Reserved Instance
- B) 3-year All Upfront Reserved Instance
- C) 3-year Compute Savings Plan
- D) Spot Instances with Spot Fleet

### Answer 16

Correct Answer: B

### Explanation 16

- A is incorrect: 1-year Reserved Instances provide up to 40% discount versus On-Demand. This is less than the 3-year commitment discount.
- B is correct: 3-year All Upfront Reserved Instances provide the highest EC2 discount available — up to 72% off On-Demand prices. The combination of maximum commitment duration (3 years) and maximum upfront payment (All Upfront) yields the greatest discount of any purchasing option for predictable, continuous workloads.
- C is incorrect: 3-year Compute Savings Plans provide up to 66% discount — slightly less than the 72% available with 3-year All Upfront Reserved Instances. However, Compute Savings Plans provide more flexibility (applying across instance families, Regions, Lambda, and Fargate), which comes at a slightly lower discount ceiling.
- D is incorrect: Spot Instances can provide up to 90% discount, but they can be interrupted at any time with a 2-minute warning. A continuously running, steady-state application cannot tolerate interruptions. Spot Instances are not appropriate for this workload.

---

## Question 17

A company runs an Auto Scaling group behind an ALB. When instances are terminated during scale-in, users experience request errors because in-flight requests are dropped. Which setting prevents this?

- A) Increase the ALB idle timeout to allow connections to complete before the ALB closes them
- B) Enable connection draining (deregistration delay) on the ALB target group so the load balancer completes in-flight requests before deregistering the instance
- C) Configure the Auto Scaling group with a scale-in protection policy on all instances
- D) Set the Auto Scaling minimum capacity to match the current desired capacity to prevent scale-in

### Answer 17

Correct Answer: B

### Explanation 17

- A is incorrect: The ALB idle timeout closes idle connections, not in-flight requests. Increasing it does not specifically address the race condition between instance deregistration and in-flight requests completing.
- B is correct: Connection draining (ALB target group deregistration delay, default 300 seconds) causes the ALB to stop sending new requests to an instance being deregistered while waiting for existing in-flight requests to complete. Only after all in-flight requests are done (or the deregistration delay expires) does the ALB complete deregistration. This prevents request errors during scale-in.
- C is incorrect: Scale-in protection prevents Auto Scaling from terminating a specific instance. It is useful for protecting instances running long-running jobs, but it does not solve the general in-flight request problem for all instances during scale-in events.
- D is incorrect: Setting minimum equal to desired prevents any scale-in from occurring, eliminating the cost benefits of Auto Scaling. This is not an appropriate solution for a production application that needs elastic capacity.

---

## Question 18

An architect is designing a highly available three-tier web application. The web tier uses EC2 instances in an Auto Scaling group. Which EC2 health check configuration ensures that the ASG replaces instances that are passing EC2 health checks but are failing to respond to application HTTP requests?

- A) EC2 status check monitoring only, with CloudWatch alarms for HTTP response codes
- B) ELB health checks enabled on the Auto Scaling group, with the ALB health check configured to test the application's health endpoint
- C) Custom scripts running on each instance that terminate the EC2 process on HTTP failure
- D) EC2 instance health check with detailed monitoring enabled at 1-minute intervals

### Answer 18

Correct Answer: B

### Explanation 18

- A is incorrect: EC2 status checks verify the health of the underlying hardware and the instance's ability to run (power, network, software). They do not test whether the application is responding to HTTP requests. An application crash passes EC2 status checks but fails application health.
- B is correct: When ELB health checks are enabled on the ASG, the Auto Scaling group uses the ALB's health check result as the instance health status. The ALB's health check can be configured to make HTTP requests to a specific path (e.g., `/health`) on the application. If the application is not responding correctly, the ALB marks the instance as unhealthy, and the ASG replaces it.
- C is incorrect: Writing custom scripts to terminate processes is fragile, error-prone, and not a supported AWS-native mechanism for ASG health management. It also terminates the EC2 process but does not necessarily trigger ASG replacement.
- D is incorrect: Detailed monitoring increases the CloudWatch metric reporting frequency from 5 minutes to 1 minute. It does not change the nature of EC2 health checks from infrastructure-level to application-level.

---

## Question 19

A company runs a three-tier application on EC2 with an ALB and an RDS database. During a load test, the team discovers that the ALB returns 503 Service Unavailable errors at high traffic volumes. CloudWatch shows EC2 CPU utilization is at 30% across all instances. What is the most likely cause of the 503 errors?

- A) The RDS instance is out of storage space and rejecting new database connections
- B) The ALB target group health check is failing because the application's health check endpoint URL is misconfigured
- C) The EC2 instances are healthy but the ALB has hit its registered listener rules limit
- D) The application's maximum thread pool or connection pool is exhausted, causing health check failures on some instances

### Answer 19

Correct Answer: D

### Explanation 19

- A is incorrect: RDS storage exhaustion causes database connection errors at the application layer, which would result in 500-series errors from the application — but the question states CPU is low, suggesting the bottleneck is not at the compute layer. RDS storage would not directly cause ALB 503 errors.
- B is incorrect: A misconfigured health check URL would cause all or most instances to be marked unhealthy consistently, resulting in 503 errors even at low traffic. The symptom described (errors appearing at high traffic with low CPU) points to an application-level resource exhaustion, not a health check misconfiguration.
- C is incorrect: ALB listener rule limits are a configuration limit (100 rules per listener by default) that would cause errors when new rules cannot be added, not when traffic volume increases. This is not a runtime behavior.
- D is correct: Low CPU with 503 errors under high traffic is a classic symptom of application-level resource exhaustion — typically thread pool saturation, connection pool limits, or file descriptor limits. Instances are not computationally overloaded but cannot accept new connections because the application's internal concurrency limits are reached. The health checks fail for instances that are connection-saturated, causing the ALB to return 503.

---

## Question 20

A solutions architect is selecting an EC2 instance type for a new real-time data analytics engine that processes streaming data. The workload requires very fast storage I/O with hundreds of thousands of random read and write IOPS, and the analytics results are regenerated from the data stream if the instance is lost. Which EC2 instance type best fits this requirement?

- A) R6g memory-optimized instance with an attached gp3 EBS volume
- B) M5 general purpose instance with io2 EBS volume provisioned at 100,000 IOPS
- C) I3 or I4i storage-optimized instance with locally attached NVMe SSD instance store
- D) C6g compute-optimized instance with an EFS file system attached for shared storage

### Answer 20

Correct Answer: C

### Explanation 20

- A is incorrect: R6g instances are memory-optimized and suitable for large in-memory datasets. gp3 EBS volumes provide up to 16,000 IOPS — far below the hundreds of thousands of IOPS required.
- B is incorrect: While io2 EBS volumes can be provisioned up to 64,000 IOPS (or higher with io2 Block Express), EBS storage is network-attached and adds latency compared to locally attached NVMe. For extremely high IOPS streaming workloads where data is regeneratable, instance store provides better performance at lower cost.
- C is correct: I3 and I4i instances are storage-optimized and include high-performance locally attached NVMe SSD instance store volumes capable of millions of IOPS with microsecond latency. Since the analytics results can be regenerated from the data stream, the ephemeral nature of instance store is acceptable. This combination provides the best IOPS performance at the lowest per-IOPS cost for this use case.
- D is incorrect: EFS is a network file system designed for shared, concurrent access by multiple instances. It does not provide the high-IOPS, low-latency performance required for a real-time analytics engine processing hundreds of thousands of IOPS.
