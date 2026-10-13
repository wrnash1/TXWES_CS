# Discussion Forum: Module 03 - EC2: Instance Types, Auto Scaling, and Load Balancing

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Instructions

Read all three scenarios below and select one to address in your initial post. Your initial post must be 175-225 words, technically precise, and reference specific EC2, Auto Scaling, or load balancing concepts from this module. Respond to at least two classmates who chose different scenarios from yours.

Initial post due: Wednesday at 11:59 PM
Peer responses due: Sunday at 11:59 PM

---

## Scenario A - Scaling Policy Failure Post-Mortem

A SaaS company experienced a major outage during a product launch event. Their Auto Scaling Group was configured with a target tracking policy at 80% CPU, EC2 health checks only, and a minimum capacity of 1 instance. When the launch generated 100x normal traffic, the single instance became completely unresponsive. New instances were being launched but took 8 minutes to reach InService state, during which users saw errors. Analyze the architectural failures in this configuration. For each failure, identify the specific configuration element, explain how it contributed to the outage, and recommend a specific corrective action. Your response should address at least three separate failures and propose a post-launch architecture that would handle this scenario without user-visible errors.

---

## Scenario B - Load Balancer Architecture Decision

A financial services company is building two new systems simultaneously. System 1 is a customer-facing REST API that routes requests to different microservices based on URL path. System 2 is a real-time trading platform that processes 500,000 TCP connections per second, requires sub-millisecond latency, and must expose a static IP address that client firms can whitelist through their firewalls. The team lead proposes using a single Application Load Balancer for both systems to simplify the infrastructure. Evaluate this proposal. Explain why one load balancer type cannot satisfy both requirements, identify which load balancer type is correct for each system and why, and describe any additional architectural consideration for the trading platform related to IP addressing.

---

## Scenario C - Purchasing Model Optimization

A retail company currently runs 100% of their workload on On-Demand EC2 instances. Their workload profile is: 40 M5.xlarge web servers running continuously 24/7 all year, 20 C5.2xlarge batch processing servers that run nightly jobs from 11 PM to 5 AM, and a variable fleet of up to 60 R5.4xlarge analytics instances that process end-of-quarter reports for 5 days per quarter. Design a purchasing strategy that minimizes cost while meeting availability requirements. For each fleet, specify the purchasing model you recommend, justify it based on the usage pattern, and explain the risk or tradeoff. Your response should reference at least two different purchasing models.

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — technical accuracy | 3 | Correctly identifies failure modes, load balancer capabilities, or purchasing model tradeoffs; no factual errors |
| Initial post — depth and completeness | 2 | Addresses all parts of the chosen scenario; 175-225 words; uses specific AWS service names and configuration parameters |
| Initial post — clarity | 1 | Well-organized, professional tone, correct technical terminology |
| Peer response 1 — substantive engagement | 2 | Adds alternative solution, identifies a gap in the peer's analysis, or extends the scenario; minimum 50 words |
| Peer response 2 — substantive engagement | 2 | Adds alternative solution, identifies a gap in the peer's analysis, or extends the scenario; minimum 50 words |
| **Total** | **10** | |

---

## Professor Nash Note

Strong posts in this module will include specific numbers and configuration values — not just "increase the minimum capacity" but "increase minimum capacity to 2, one per Availability Zone, to survive a single AZ failure." Vague architectural advice is not sufficient. Peer responses that simply agree are not sufficient. Challenge or extend the thinking in the post you are responding to.
