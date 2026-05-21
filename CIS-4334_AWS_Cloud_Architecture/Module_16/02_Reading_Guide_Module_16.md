# Reading Guide: Module 16 - Final Exam Prep & AWS Solutions Architect Associate
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 16 - Final Exam Prep & AWS Solutions Architect Associate (SAA-C03)**! This module is your comprehensive review and exam readiness assessment for the AWS Certified Solutions Architect – Associate certification. You will consolidate knowledge across all 15 prior modules, practice high-difficulty scenario-based questions, refine exam time management strategies, and walk through the full exam registration and preparation process. The SAA-C03 exam is 65 questions over 130 minutes — this module ensures you are ready.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. These represent the highest-priority cross-domain concepts for the SAA-C03 exam:

*   **SAA-C03 Exam Domain Weightings**: The SAA-C03 exam is divided into four domains: Domain 1 – Design Secure Architectures (30%), Domain 2 – Design Resilient Architectures (26%), Domain 3 – Design High-Performing Architectures (24%), Domain 4 – Design Cost-Optimized Architectures (20%). Security is the most heavily weighted domain. Knowing the domain percentages helps prioritize study time — spend 30% of prep on security, 26% on resilience, etc.

*   **Cross-Service Integration Patterns**: The SAA-C03 exam heavily tests how multiple AWS services work together. Critical patterns include: S3 + CloudFront + OAC (secure static site delivery), SQS + Lambda (decoupled event processing), SNS + SQS fan-out (parallel processing), API Gateway + Lambda + DynamoDB (serverless CRUD API), EC2 + ALB + ASG + Multi-AZ RDS (multi-tier HA web app), VPC + NAT Gateway + Private Subnets (secure compute). Practice drawing these architectures from memory.

*   **Service Comparison Decision Trees**: Many SAA-C03 questions require choosing between similar services. Key comparisons: ECS vs. EKS (AWS-native simplicity vs. Kubernetes portability), ALB vs. NLB (Layer 7 content routing vs. Layer 4 extreme performance), RDS vs. DynamoDB (relational SQL vs. NoSQL at scale), CloudFront vs. Global Accelerator (cacheable content vs. dynamic/non-cacheable traffic), S3 Standard vs. S3 Glacier (active access vs. archival), SQS vs. SNS (pull queue for one consumer vs. push fan-out to many).

*   **High-Availability Design Principles**: AWS HA architecture always involves: deploying across multiple AZs, using managed services with built-in redundancy (ALB, RDS Multi-AZ, DynamoDB), eliminating single points of failure, designing for automatic recovery (ASG health checks, RDS failover, Route 53 health checks), and decoupling components (SQS buffers, Lambda event-driven processing). Any architecture with a single instance, single AZ, or synchronous tight coupling is likely an anti-pattern in exam answers.

*   **Cost Optimization Decision Framework**: Exam cost optimization questions follow a pattern. For compute: Spot (interruptible batch) > Reserved (steady baseline) > Savings Plans (flexible committed usage) > On-Demand (unpredictable). For storage: Glacier Deep Archive (rarely accessed archival) < Glacier Flexible Retrieval < Standard-IA (monthly access) < Standard (frequent access). For databases: Aurora Serverless (variable traffic) vs. RDS Reserved (steady-state). For delivery: Lambda (per-invocation) vs. EC2 (running instances) vs. Fargate (per-second containers).

---

### 2. Certification Exam Tips

*   **SAA-C03 Exam Format**: 65 questions (multiple choice and multiple response), 130 minutes, passing score approximately 720/1000. 15 of the 65 questions are unscored pilot questions that do not count toward your score but cannot be identified. Budget approximately 2 minutes per question. Flag and skip questions you are uncertain about — return to them after answering the questions you know.

*   **Highest-Priority Topics by Domain Frequency:** Security (30%): IAM roles/policies, KMS SSE-KMS, WAF, Security Groups vs. NACLs, Shared Responsibility Model. Resilient (26%): Multi-AZ, ASG health checks, RDS Multi-AZ vs. Read Replicas, Route 53 Failover routing, SQS for decoupling. High-Performing (24%): ALB path routing, ElastiCache, CloudFront, DynamoDB On-Demand, Fargate right-sizing. Cost-Optimized (20%): Reserved vs. Spot vs. On-Demand, S3 Lifecycle policies, Lambda vs. EC2, right-sizing.

*   **Common Exam Traps to Remember:** (1) Multi-AZ standby CANNOT serve read traffic — only Read Replicas can. (2) Security Groups are STATEFUL (allow-only); NACLs are STATELESS (allow + deny). (3) Lambda max timeout is 15 minutes — anything longer needs EC2, ECS, or Batch. (4) CloudFront does not cache POST/PUT requests by default — only GET/HEAD are cached. (5) S3 Transfer Acceleration speeds uploads, not downloads. (6) Enabling "detailed monitoring" on EC2 only increases metric frequency to 1-minute intervals — it does NOT add memory metrics (need CloudWatch Agent).

*   **Exam Registration and Scheduling:** The SAA-C03 exam is administered through Pearson VUE. Register at [aws.amazon.com/certification](https://aws.amazon.com/certification/). The exam fee is $150 USD. AWS provides a free Official Practice Exam (not a full mock exam) after scheduling. AWS Skill Builder offers an Official Practice Question Set (20 questions) for free, and a full 65-question Official Practice Exam for $29. After passing, your certification is valid for 3 years.

*   **Final Week Preparation Strategy:** Days 7–4 before exam: complete full practice exams (Tutorials Dojo, Whizlabs, or AWS Official) and review every incorrect answer. Days 3–2: focus only on your weakest domain (review pillar, re-read AWS FAQ pages for the services you miss). Day 1: light review of the decision trees and high-priority topics above. Day 0 (exam day): no cramming — trust your preparation.

*   **Study Resources:** The most comprehensive free resource is the AWS documentation and FAQs for each service. The AWS Certified Solutions Architect – Associate Exam Guide is available at [https://aws.amazon.com/certification/certified-solutions-architect-associate/](https://aws.amazon.com/certification/certified-solutions-architect-associate/). Practice exams from Tutorials Dojo are highly recommended by the community as the closest to actual exam difficulty. AWS re:Invent session videos on YouTube provide deep technical context for difficult topics.

---

### Required Readings & Videos
To prepare for this module's exam readiness review, you must complete the following:

*   **Required Reading:** Download and read the official SAA-C03 Exam Guide at [https://aws.amazon.com/certification/certified-solutions-architect-associate/](https://aws.amazon.com/certification/certified-solutions-architect-associate/). Review the sample questions provided in the Exam Guide. Re-read the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) to connect services to pillars. Review the [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) for the "Disaster Recovery of Workloads on AWS" and "AWS Security Best Practices" whitepapers.

*   **Required Video:** Watch the SAA-C03 final review / exam tips video in the official course playlist, focusing on the service comparison sections and the most common exam traps called out by the instructor: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's final review activities, you will complete the following:

*   **Complete a timed full-length practice exam:** Take a 65-question, 130-minute practice exam from Tutorials Dojo or the AWS Official Practice Exam. Grade yourself and identify your weakest domain by counting incorrect answers per domain.

*   **Architecture whiteboard review:** Without references, draw the complete architecture for a three-tier web application on AWS: ALB in public subnets → EC2 instances in private subnets (ASG across 2 AZs) → RDS Multi-AZ in isolated subnets. Add security controls (Security Groups, NACLs, IAM Role on EC2, KMS-encrypted RDS), monitoring (CloudWatch Alarms → SNS), and a CloudFront distribution with WAF. Verify your diagram against the course materials.

*   **Register for the certification exam:** If you have not already done so, register for the SAA-C03 exam through Pearson VUE at [https://home.pearsonvue.com/aws](https://home.pearsonvue.com/aws). Choose a test date 1–2 weeks after completing this module to allow time for final review.

---

### 3. Study Checklist
- [ ] Review all five glossary entries and be able to recall the SAA-C03 domain percentages from memory.
- [ ] Complete at least one full 65-question practice exam and score each domain separately.
- [ ] Review the official SAA-C03 Exam Guide at [https://aws.amazon.com/certification/certified-solutions-architect-associate/](https://aws.amazon.com/certification/certified-solutions-architect-associate/).
- [ ] Watch the final review video in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the architecture whiteboard exercise without references.
- [ ] Register for and schedule the SAA-C03 exam.
- [ ] Complete the final course exam.
