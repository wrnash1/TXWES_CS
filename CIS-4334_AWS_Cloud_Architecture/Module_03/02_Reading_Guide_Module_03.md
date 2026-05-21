# Reading Guide: Module 03 - EC2 – Instance Types, Auto Scaling, and Load Balancing
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 03 - EC2 – Instance Types, Auto Scaling, and Load Balancing**! Amazon Elastic Compute Cloud (EC2) is the core compute service of AWS and is heavily tested on the SAA-C03 exam. This module covers how to select the right instance type for a workload, how to configure Auto Scaling Groups to maintain availability and optimize cost, and how Elastic Load Balancers distribute traffic across instances. Mastering these concepts enables you to design systems that are both highly available and cost-efficient.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **EC2 Instance Types**: Virtual machines with predefined combinations of CPU, memory, storage, and network capacity, grouped into families by use case. General Purpose (M, T families) balance CPU and memory for web servers. Compute Optimized (C family) prioritize CPU for batch processing and gaming. Memory Optimized (R, X families) suit in-memory databases and big data analytics. Storage Optimized (I, D families) deliver high IOPS for transactional workloads. Choosing the wrong family is a common exam distractor.

*   **Amazon Machine Images (AMIs)**: Pre-configured templates containing the operating system, application server, and applications used to launch EC2 instances. AMIs can be AWS-provided, AWS Marketplace offerings, or custom images created from running instances. AMIs are Region-specific but can be copied across Regions to support multi-Region deployments.

*   **EC2 Purchase Options**: The billing model under which an EC2 instance runs. On-Demand instances are billed per second with no commitment, ideal for unpredictable workloads. Reserved Instances (1- or 3-year terms) offer up to 72% savings for steady-state workloads. Spot Instances use spare AWS capacity at up to 90% discount but can be interrupted. Dedicated Hosts provide physical server control for licensing compliance.

*   **Auto Scaling Groups (ASGs)**: A collection of EC2 instances managed as a fleet, governed by minimum, desired, and maximum capacity settings. ASGs use Launch Templates (or legacy Launch Configurations) to define how new instances are launched. Scaling policies — Simple, Step, and Target Tracking — determine when to add or remove instances based on CloudWatch metrics such as CPU utilization or requests per target.

*   **Elastic Load Balancers (ELBs)**: Managed load balancers that distribute incoming traffic across healthy targets (EC2 instances, containers, Lambda functions, IP addresses). Application Load Balancers (ALB) operate at Layer 7 and support path-based and host-based routing, ideal for microservices and HTTP/HTTPS. Network Load Balancers (NLB) operate at Layer 4 for extreme performance and static IP requirements. Gateway Load Balancers (GWLB) insert third-party virtual appliances transparently.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** EC2, ASG, and ELB content spans all four SAA-C03 domains but is heaviest in Design Resilient Architectures (26%) and Design Cost-Optimized Architectures (20%).

*   **Instance Type Selection Trap:** The exam describes a workload (e.g., "in-memory analytics requiring 512 GB RAM") and asks which instance type is most appropriate. Always match the workload characteristic to the instance family: memory-intensive → R/X family; compute-intensive → C family; general web → T/M family.

*   **Spot vs. Reserved vs. On-Demand:** The exam tests cost optimization scenarios. Spot = cheapest for interruptible, fault-tolerant batch jobs. Reserved = best for steady-state baseline workloads. On-Demand = right for unpredictable spikes. Savings Plans are a flexible alternative to Reserved Instances for compute and Lambda.

*   **ALB vs. NLB Exam Trap:** ALB is the answer for HTTP/HTTPS routing, path-based routing (`/api/*` → service A), host-based routing, and WebSocket connections. NLB is the answer for TCP/UDP ultra-low latency, static IP, or PrivateLink. Do not confuse them.

*   **ASG Health Checks:** By default, ASGs use EC2 status checks. When behind an ELB, enable ELB health checks so the ASG terminates instances that pass EC2 checks but fail application-level health checks. This is a common exam scenario.

*   **Study Resource:** The official EC2 documentation includes instance type comparison tables and the Auto Scaling Developer Guide: [Amazon EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html). Review the "Best practices for Amazon EC2" and "Auto Scaling group" sections specifically.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the EC2 chapters in the AWS Solutions Architect study materials. Focus on the [Amazon EC2 Instance Types page](https://aws.amazon.com/ec2/instance-types/) for the family-to-use-case mapping, and the [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) portal for the "Cost Optimization with AWS" whitepaper covering Reserved Instances and Savings Plans.

*   **Required Video:** Watch the EC2, Auto Scaling, and Elastic Load Balancing modules in the official course playlist, paying close attention to the ALB vs. NLB comparison and the mechanics of Target Tracking scaling policies: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Launch an EC2 instance with a custom AMI and instance profile:** Use the AWS CLI to launch a t3.micro instance: `aws ec2 run-instances --image-id ami-XXXXXX --instance-type t3.micro --iam-instance-profile Name=MyRole`. Connect via EC2 Instance Connect.

*   **Create an Auto Scaling Group with a Target Tracking policy:** Configure a Launch Template, create an ASG with min=1/desired=2/max=4, and attach a Target Tracking policy targeting 50% average CPU utilization. Use a stress-testing tool to trigger scale-out.

*   **Attach an Application Load Balancer and observe routing:** Create an ALB with two target groups, configure path-based routing rules (e.g., `/api/*` → Target Group 1, `/static/*` → Target Group 2), and verify that requests are routed to the correct instances.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Review EC2 instance type families at [https://aws.amazon.com/ec2/instance-types/](https://aws.amazon.com/ec2/instance-types/).
- [ ] Review Auto Scaling pricing and purchase options at [https://aws.amazon.com/ec2/pricing/](https://aws.amazon.com/ec2/pricing/).
- [ ] Watch the EC2/ALB/ASG video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab launching instances, configuring ASG, and routing with ALB.
- [ ] Proceed to the weekly quiz.
