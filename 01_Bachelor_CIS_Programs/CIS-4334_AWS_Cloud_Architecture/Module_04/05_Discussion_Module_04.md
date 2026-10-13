# Discussion Forum: Module 04 - S3: Storage Classes, Lifecycle Policies, and Security

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Instructions

Read all three scenarios below and select one to address in your initial post. Your initial post must be 175-225 words, technically precise, and reference specific S3 features, storage classes, or security controls from this module. Respond to at least two classmates who chose different scenarios from yours.

Initial post due: Wednesday at 11:59 PM
Peer responses due: Sunday at 11:59 PM

---

## Scenario A - Data Retention Cost Optimization

A healthcare company stores patient imaging files in S3 Standard. Each study is 500 MB on average. The radiology team accesses studies frequently during the first 90 days post-scan for diagnosis and follow-up. After 90 days, studies are accessed roughly once a year for reference. After 7 years, studies must be retained but are almost never accessed. The company currently pays for all storage at Standard rates and wants to reduce their annual S3 bill significantly. Design a lifecycle policy strategy for this use case. Specify which storage classes you would use, when transitions occur, the minimum storage duration implications, and what retrieval SLA the company should expect at each stage. Quantify approximately how much storage cost could be saved on a per-study basis compared to storing everything in Standard.

---

## Scenario B - S3 Security Incident Response

A DevOps engineer at a fintech startup receives a notification from AWS Trusted Advisor that two S3 buckets containing customer payment data are publicly accessible. Investigation reveals that Block Public Access was never configured and a bucket policy was added six months ago that unintentionally grants s3:GetObject to all principals. Describe the immediate remediation steps, the specific S3 controls you would configure to prevent recurrence, and the AWS services you would enable to detect future misconfigurations proactively. Your response should address at least three distinct security controls and explain what threat each one mitigates.

---

## Scenario C - Compliance Archive Design

A legal services firm must retain client correspondence files for 10 years under state bar association rules. The files cannot be modified or deleted during the retention period under any circumstances, including by IT administrators. After 10 years, files should be automatically deleted. The firm processes approximately 50,000 new files per year averaging 2 MB each. Cost must be minimized. Design the complete S3 architecture for this requirement. Specify the storage class or classes, the Object Lock configuration, any lifecycle policy needed, and explain why the chosen Object Lock mode satisfies the "cannot be deleted under any circumstances" requirement better than the alternative mode.

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — technical accuracy | 3 | Correctly applies S3 storage classes, lifecycle mechanics, security controls, or Object Lock; no factual errors |
| Initial post — depth and completeness | 2 | Addresses all parts of the chosen scenario; 175-225 words; uses specific S3 class names, policy elements, and service names |
| Initial post — clarity | 1 | Well-organized, professional tone, correct AWS terminology |
| Peer response 1 — substantive engagement | 2 | Adds alternative configuration, identifies a gap in the design, or extends the scenario with an edge case; minimum 50 words |
| Peer response 2 — substantive engagement | 2 | Adds alternative configuration, identifies a gap in the design, or extends the scenario with an edge case; minimum 50 words |
| **Total** | **10** | |

---

## Professor Nash Note

Scenario A rewards precision — if you propose Glacier for data that needs immediate access, that is a design flaw. Scenario B rewards completeness — if you only fix the bucket that is already exposed without preventing future exposures, you have missed the point. Scenario C rewards understanding the difference between Governance and Compliance mode. In all cases, peer responses should engage with the design, not just affirm it.
