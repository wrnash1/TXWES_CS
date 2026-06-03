# Discussion Forum: Module 08 — Amazon S3 and Storage Services

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to the scenario. Then write a substantive reply (75–100 words) to at least one classmate who chose a different scenario. Use specific AWS service names and feature names in your response.

---

## Scenario A — The Storage Class Cost Audit

A retail company's CTO receives an S3 cost report showing $40,000 per month in storage. An audit reveals the bucket contains four types of data: (1) product images accessed constantly by the website, (2) daily sales reports accessed frequently for the first 30 days then monthly for a year, (3) 5-year-old order history required by regulators but never accessed, and (4) nightly automated database backups where only last week's backup is ever needed.

Design a storage class strategy for each data type. For each type, identify the appropriate storage class, whether a lifecycle policy transition is needed, and whether any data can be expired to reduce cost. Estimate the relative cost impact of your recommendations. Consider whether S3 Intelligent-Tiering is the right answer for any of the four types or whether explicit lifecycle rules are more appropriate.

---

## Scenario B — The Shared Storage Debate

A startup is building a content management platform with 10 EC2 web servers running Amazon Linux across three Availability Zones. A developer proposes storing all uploaded user content on an EBS gp3 volume attached to the "primary" web server, with the other 9 servers reading content via NFS mounted from that instance. The lead architect pushes back and says this design is wrong at the fundamental level.

Explain why the developer's approach is architecturally flawed. Describe the correct AWS storage solution for this use case and why it is superior. Address: availability (what happens if the primary instance goes down), scalability (what happens when the fleet grows to 50 instances), and durability (how the correct solution protects against data loss). Be specific about which AWS storage service and configuration you would use.

---

## Scenario C — Compliance and Immutability

A publicly traded company is implementing an S3-based document archive for SEC filings and financial records. Legal has specified three requirements: records must be retained for exactly 7 years, records cannot be modified or deleted during the retention period by anyone including IT administrators, and the company must be able to provide an audit trail to regulators demonstrating that the retention policy was enforced.

Design the complete S3 architecture to meet these requirements. Your response should address the specific S3 features and configurations that enforce immutability, explain the difference between the two retention modes available and which applies here, describe how lifecycle expiration interacts with immutability, and explain how the company would demonstrate compliance to auditors.

---

## Peer Response Instructions

After posting your initial response, read your classmates' posts and reply to at least one person who chose a different scenario than you. Your reply should:

- Identify one point in their response you agree with and explain why
- Identify one consideration they may have missed or could strengthen
- Ask a follow-up question that extends the discussion

---

## 10-Point Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical Accuracy | 3 | AWS service names, storage classes, and feature behaviors described correctly |
| Depth of Analysis | 2 | Response addresses the specific requirements rather than generic storage advice |
| Word Count (Initial) | 1 | Initial post is between 175 and 225 words |
| Use of Module Concepts | 2 | Response references concepts from Module 08 video and reading guide |
| Peer Reply Quality | 2 | Reply is substantive (75–100 words), identifies a specific point, and asks a meaningful follow-up question |
| **Total** | **10** | |

---

**Professor Nash Note:** Scenario B is the one I want you to think hardest about. In my experience consulting and in interviews, the "shared EBS via NFS from a primary instance" anti-pattern comes up repeatedly from developers who are comfortable with on-premises NAS storage. Understanding why EFS is architecturally correct — not just "better" — requires you to think about availability zones, instance failure, and what happens at scale. If you choose Scenario B, push yourself to explain the failure modes, not just the solution.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
