# Quiz: Module 15 - Well-Architected Framework – 6 Pillars
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which pillar of the AWS Well-Architected Framework focuses on the workload's ability to recover from infrastructure or service disruptions and to automatically scale to meet demand?
*   A) Performance Efficiency
*   B) Cost Optimization
*   C) Reliability
*   D) Operational Excellence
*   **Correct Answer:** C) The Reliability Pillar covers automatic recovery from failure, horizontal scaling, testing recovery procedures, and managing change to avoid unexpected impacts on workload availability.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Performance Efficiency focuses on using computing resources efficiently — selecting right-sized instances, using managed services, and achieving performance as demand changes. It is about efficiency, not failure recovery.
    *   *Why B is incorrect:* Cost Optimization focuses on eliminating unnecessary spending and running workloads at the optimal price point. While cost and reliability can be in tension, Cost Optimization does not address failure recovery or availability.
    *   *Why C is correct:* The Reliability Pillar explicitly covers: foundations (service limits, network topology), workload architecture (distributed systems, loose coupling), change management, and failure management (backup, DR, chaos engineering). Multi-AZ deployment, Auto Scaling, and Route 53 failover all serve this pillar.
    *   *Why D is incorrect:* Operational Excellence focuses on running and monitoring systems to deliver business value and continuously improve processes. It addresses operations as code, small reversible changes, and learning from events — not infrastructure failure recovery.

---

**Question 2**
Which of the following is the most accurate description of the **Performance Efficiency Pillar** of the AWS Well-Architected Framework?
*   A) The practice of running and monitoring systems to deliver business value, using operations as code and making frequent small reversible changes.
*   B) The approach of using computing resources efficiently to meet system requirements while maintaining that efficiency as demand grows and technologies evolve — including right-sizing, using managed services, and leveraging serverless architectures.
*   C) The process of protecting data, systems, and assets while delivering business value by applying security at every layer and implementing a strong identity foundation.
*   D) The practice of minimizing the environmental impact of cloud workloads by maximizing utilization, choosing energy-efficient hardware, and reducing unnecessary data transfer.
*   **Correct Answer:** B) The Performance Efficiency Pillar focuses on selecting the right resources, using the latest technology efficiently, going global in minutes, using serverless architectures, and experimenting more often.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes the Operational Excellence Pillar — "operations as code," "small reversible changes," and "learning from operations events" are the Operational Excellence design principles.
    *   *Why B is correct:* Performance Efficiency is about matching resources to requirements and continuously optimizing as the workload and available AWS technology evolve. Key AWS services include EC2 right-sizing, ElastiCache for caching, CloudFront for global content delivery, and Lambda for event-driven compute — all reducing latency and improving throughput per dollar.
    *   *Why C is incorrect:* This describes the Security Pillar — "protecting data, systems, and assets," "security at every layer," and "strong identity foundation" are Security Pillar design principles.
    *   *Why D is incorrect:* This describes the Sustainability Pillar (the sixth pillar, added in 2021) — minimizing environmental impact through efficient resource use and renewable energy.

---

**Question 3**
A company needs to design a disaster recovery architecture for a critical application. Their RTO is 4 hours and RPO is 1 hour. Cost must be minimized. Which Well-Architected disaster recovery strategy best meets these requirements?
*   A) Multi-Site Active/Active — run identical production workloads in two Regions simultaneously for zero RTO and near-zero RPO.
*   B) Warm Standby — maintain a scaled-down but fully functional version of the production environment in a secondary Region, scaling it up during a failover event.
*   C) Pilot Light — keep core data replicated to a secondary Region with minimal compute pre-provisioned; scale out compute during a disaster event.
*   D) Backup and Restore — take automated snapshots and backups, restore from them in a new environment during a disaster event.
*   **Correct Answer:** C) Pilot Light keeps critical data (e.g., database replication) running in the secondary Region with minimal compute cost, meeting the 1-hour RPO (continuous replication) and 4-hour RTO (scale out compute from the pre-configured base).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Multi-Site Active/Active provides the lowest RTO and RPO possible but at the highest cost — you pay for full production capacity in both Regions continuously. The question specifies "cost must be minimized," making this the most expensive option without proportional benefit for the stated RTO/RPO.
    *   *Why B is incorrect:* Warm Standby maintains a scaled-down but fully running environment, which has lower RTO than Pilot Light but higher ongoing cost. For a 4-hour RTO, Pilot Light is sufficient and cheaper than Warm Standby.
    *   *Why C is correct:* Pilot Light pre-provisions only the core elements that are slowest to restore (data replication, pre-built AMIs, networking infrastructure). During a disaster, compute scales out from the "pilot light" base. For a 4-hour RTO with a 1-hour RPO, Pilot Light provides the right balance — better recovery speed than Backup & Restore with much lower ongoing cost than Warm Standby or Active/Active.
    *   *Why D is incorrect:* Backup and Restore typically achieves RTO measured in hours to days depending on data volume — it involves restoring from S3 snapshots to new instances, which may exceed the 4-hour RTO for large databases. The 1-hour RPO also requires very frequent backups or continuous replication, making this approach operationally complex and potentially unreliable for the stated requirements.

---

**Question 4**
A solutions architect reviews a company's architecture and identifies that their application runs on a single oversized r5.8xlarge EC2 instance to handle peak holiday traffic, but sits at 5% CPU utilization for 10 months of the year. Which Well-Architected pillar improvement directly addresses this situation?
*   A) Security Pillar — the single instance creates a single point of attack; distribute workloads across multiple instances.
*   B) Cost Optimization Pillar — right-size the instance to match normal load and use Auto Scaling to add capacity for holiday peaks rather than permanently over-provisioning.
*   C) Reliability Pillar — a single instance is a single point of failure; deploy in multiple AZs with an Auto Scaling Group.
*   D) Performance Efficiency Pillar — the r5.8xlarge is a Memory Optimized instance; switch to a Compute Optimized (C5) instance family for better performance.
*   **Correct Answer:** B) The Cost Optimization Pillar addresses over-provisioning waste. The correct fix is to right-size the instance for normal load and use Auto Scaling to provision additional capacity only when demand requires it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While a single instance is a larger attack surface than a distributed deployment, the Security Pillar concerns protecting data and systems from unauthorized access — not from over-provisioning. Security improvements are orthogonal to instance sizing.
    *   *Why B is correct:* Running an r5.8xlarge at 5% CPU for 10 months is a classic Cost Optimization anti-pattern. The Cost Optimization Pillar explicitly calls out "right-sizing" (matching instance types to actual workload requirements) and "matching supply to demand" (using Auto Scaling rather than permanent over-provisioning) as key practices.
    *   *Why C is incorrect:* The Reliability Pillar concern about single AZ deployment is valid and should also be addressed, but it is not the primary issue identified — the question focuses on the 5% utilization waste, which is a cost problem. Reliability and Cost Optimization are different pillars with different improvement recommendations for this scenario.
    *   *Why D is incorrect:* The r5 family is Memory Optimized. Switching to C5 (Compute Optimized) would change the workload characteristics, potentially degrading performance if the application has memory-intensive components. The primary issue is not the instance family but the size — an r5.large or r5.xlarge (right-sized) with Auto Scaling would address both cost and the holiday scaling requirement.

---

**Question 5**
A company implements the following changes: enables AWS CloudTrail in all Regions, configures all API calls to be logged, enables AWS Config with a library of compliance rules, and sets up automated alerting when non-compliant resources are detected. Which pillar of the Well-Architected Framework do these changes primarily support?
*   A) Cost Optimization — CloudTrail and Config help identify unused resources to eliminate waste.
*   B) Reliability — monitoring all API calls and resource configurations enables faster incident detection and recovery.
*   C) Security — enabling traceability through comprehensive audit logging (CloudTrail) and continuous compliance monitoring (Config) are Security Pillar design principles.
*   D) Performance Efficiency — logging API calls allows architects to identify performance bottlenecks in service call patterns.
*   **Correct Answer:** C) The Security Pillar design principle "Enable traceability" is implemented through CloudTrail (audit who did what) and Config (audit resource compliance state) — both directly called out in the Security Pillar's best practices.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While AWS Cost Explorer and Trusted Advisor can help identify cost waste, CloudTrail and Config are security and compliance tools, not cost management tools. Their primary function in this scenario is audit trail and compliance monitoring, not cost optimization.
    *   *Why B is incorrect:* CloudTrail and Config do contribute to faster incident detection (which supports Reliability), but the Security Pillar is the explicit home for "enable traceability" (CloudTrail) and "automate security best practices" (Config automated compliance rules with remediation). The described changes align more directly with Security than Reliability.
    *   *Why C is correct:* The Well-Architected Security Pillar's design principle #2 is "Enable traceability: Monitor, alert, and audit actions and changes to your environment in real time." CloudTrail is the audit log for API traceability; Config is the compliance monitoring system. This is textbook Security Pillar implementation.
    *   *Why D is incorrect:* Performance Efficiency focuses on compute resource selection, caching, and latency optimization. While API call patterns can reveal performance issues, that is not the primary purpose of CloudTrail and Config. Using these services to analyze performance bottlenecks would be a secondary, incidental use case.

