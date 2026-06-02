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
