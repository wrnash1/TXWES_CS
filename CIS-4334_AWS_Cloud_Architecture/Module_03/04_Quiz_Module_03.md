# Quiz: Module 03 - EC2 – Instance Types, Auto Scaling, and Load Balancing
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A data engineering team needs an EC2 instance to run an in-memory Apache Spark analytics job that requires approximately 384 GB of RAM. Which EC2 instance family is most appropriate?
*   A) C5 (Compute Optimized)
*   B) T3 (General Purpose – Burstable)
*   C) R6i (Memory Optimized)
*   D) I3 (Storage Optimized)
*   **Correct Answer:** C) R6i is a Memory Optimized instance family designed for workloads requiring large amounts of RAM, such as in-memory analytics, large caches, and high-performance databases.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* C5 is Compute Optimized, designed for CPU-intensive batch and media processing. It offers high CPU-to-memory ratios, not high memory-to-CPU ratios.
    *   *Why B is incorrect:* T3 instances are burstable general-purpose instances with modest memory; they are designed for variable workloads like small web servers, not 384 GB RAM analytics jobs.
    *   *Why C is correct:* Memory Optimized families (R, X, z1d) are designed specifically for memory-intensive workloads. R6i instances provide up to 768 GB RAM with a balanced CPU complement, making them the correct family for Spark in-memory processing.
    *   *Why D is incorrect:* I3 is Storage Optimized, designed for high IOPS NVMe storage workloads like NoSQL databases. It does not offer the large RAM footprint needed for in-memory analytics.

---

**Question 2**
Which of the following is the most accurate definition of an **EC2 Auto Scaling Group (ASG)**?
*   A) A billing construct that reserves EC2 capacity for a 1- or 3-year term at a discounted hourly rate.
*   B) A managed fleet of EC2 instances with defined minimum, desired, and maximum capacity limits, automatically launching or terminating instances in response to demand or health check failures.
*   C) A pre-configured template containing an OS image, launch parameters, and application software used to launch EC2 instances identically at scale.
*   D) A virtual firewall that controls inbound and outbound traffic to and from EC2 instances at the instance level.
*   **Correct Answer:** B) An Auto Scaling Group manages a fleet of EC2 instances, maintaining desired capacity and scaling in or out based on policies, health checks, and schedules.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a Reserved Instance — a pricing model, not a scaling mechanism.
    *   *Why B is correct:* An ASG is the EC2 fleet management construct. It enforces min/max/desired counts, replaces unhealthy instances automatically, and applies scaling policies (Target Tracking, Step Scaling, Scheduled) to adjust capacity dynamically.
    *   *Why C is incorrect:* This describes a Launch Template (or AMI), which defines what instances look like. An ASG uses Launch Templates but is itself the fleet management layer, not the template.
    *   *Why D is incorrect:* This describes a Security Group, which is a stateful network firewall at the instance level, not a scaling mechanism.

---

**Question 3**
A company runs a microservices application on EC2 instances. Service A handles API requests at the path `/api/*` and Service B serves static content at `/static/*`. Both services must be accessible through a single DNS endpoint. Which load balancer and configuration best meets this requirement?
*   A) Network Load Balancer with TCP listeners on port 80 routing to a single target group.
*   B) Application Load Balancer with path-based routing rules directing `/api/*` to one target group and `/static/*` to a second target group.
*   C) Classic Load Balancer with two listeners on different ports routing to separate instance sets.
*   D) Network Load Balancer with two static IPs, one per service, registered in Route 53.
*   **Correct Answer:** B) An Application Load Balancer with path-based routing rules on a single listener cleanly splits traffic between the two services under one DNS name.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An NLB operates at Layer 4 (TCP/UDP) and cannot inspect HTTP paths. It has no concept of URL path-based routing.
    *   *Why B is correct:* ALB operates at Layer 7 and supports path-based routing natively. A single ALB DNS name with listener rules matching `/api/*` and `/static/*` routes to independent target groups — the canonical microservices pattern on SAA-C03.
    *   *Why C is incorrect:* Classic Load Balancers are legacy and do not support path-based routing. Using different ports for each service also breaks the "single endpoint" requirement for HTTP traffic on port 80.
    *   *Why D is incorrect:* Two separate NLBs with separate IPs do not meet the requirement of a single DNS endpoint for both services.

---

**Question 4**
A company has a steady baseline EC2 workload of 20 instances running continuously, plus variable demand that spikes to 50 instances for unpredictable short periods. Which combination of purchase options minimizes cost while maintaining availability?
*   A) Run all 50 instances as On-Demand to handle peak demand at any time.
*   B) Purchase 20 Reserved Instances for the steady baseline and use On-Demand or Spot for the variable spike capacity.
*   C) Purchase 50 Reserved Instances to cover both baseline and peak demand with the maximum discount.
*   D) Run all 50 instances as Spot Instances to get the lowest possible price.
*   **Correct Answer:** B) Reserve the 20 steady-state instances for maximum savings and use On-Demand (or Spot if the workload is fault-tolerant) for variable spike capacity.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running 50 On-Demand instances at all times pays full price for the steady 20, missing the opportunity for Reserved Instance savings on that predictable baseline.
    *   *Why B is correct:* This is the canonical cost optimization pattern for the SAA-C03 exam. Reserved Instances save up to 72% on committed baseline capacity. Variable/spiky overflow uses On-Demand (guaranteed availability) or Spot (cheapest for fault-tolerant spikes).
    *   *Why C is incorrect:* Buying 50 Reserved Instances commits you to paying for 30 instances that sit unused during non-peak periods, generating wasted Reserved Instance spend.
    *   *Why D is incorrect:* Spot Instances can be interrupted with 2-minute notice. Running the steady 20 critical instances as Spot exposes the baseline workload to availability risk — an unacceptable trade-off for a continuously running baseline.

---

**Question 5**
An Auto Scaling Group is configured with EC2 health checks only. An EC2 instance passes the EC2 status check (the OS is running) but fails the Application Load Balancer health check (the application is returning HTTP 503). What happens in this scenario, and what change should be made to ensure unhealthy application instances are automatically replaced?
*   A) The ASG replaces the instance because ALB health check failures are automatically detected without any configuration change.
*   B) Nothing happens; the ASG continues to count the instance as healthy. Enable ELB health checks on the ASG to allow ALB health check failures to trigger instance replacement.
*   C) AWS Route 53 detects the HTTP 503 response and redirects traffic to a healthy Region automatically.
*   D) The ALB deregisters the instance from the target group and the ASG automatically terminates and replaces it without any configuration change.
*   **Correct Answer:** B) With EC2-only health checks, the ASG treats the instance as healthy even when the application fails. Enabling ELB health checks on the ASG propagates ALB health check results so that application-level failures trigger instance termination and replacement.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ALB health check failures do not automatically propagate to the ASG unless ELB health checks are explicitly enabled on the ASG. The default is EC2 health checks only.
    *   *Why B is correct:* This is a classic SAA-C03 exam trap. The ALB can deregister the unhealthy instance from its target group (stopping new traffic), but the ASG will not replace the instance unless you explicitly enable ELB health check mode on the ASG so that ALB health failures trigger termination.
    *   *Why C is incorrect:* Route 53 health checks and routing policies operate at the DNS level; they cannot detect HTTP 503 responses at the individual instance level within a single ALB target group.
    *   *Why D is incorrect:* The ALB does deregister the instance (stopping it from receiving new requests), but without ELB health checks enabled on the ASG, the ASG does not terminate and replace the instance.

