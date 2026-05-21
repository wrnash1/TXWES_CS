# Reading Guide: Module 13 - AWS Security – KMS, WAF, Shield, GuardDuty
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 13 - AWS Security – KMS, WAF, Shield, and GuardDuty**! Security is the highest-weighted domain on the SAA-C03 exam at 30% of all questions. This module covers the AWS services dedicated to encryption key management, web application firewall protection, DDoS mitigation, and threat detection. Knowing how to layer these services for defense in depth — and which service solves which type of security problem — is essential for both the exam and real-world AWS security architecture.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AWS KMS (Key Management Service)**: A managed service for creating and controlling cryptographic keys used to encrypt data across AWS services (S3 SSE-KMS, EBS, RDS, Secrets Manager, etc.). KMS supports Customer Managed Keys (CMKs) — where the customer controls key creation, rotation policy, and key policy — and AWS Managed Keys — where AWS manages the key lifecycle automatically. All KMS key usage is logged to CloudTrail. KMS integrates with virtually every AWS service that offers encryption at rest, making it the central control plane for data protection compliance.

*   **AWS WAF (Web Application Firewall)**: A Layer 7 (HTTP/HTTPS) firewall that filters web requests based on configurable rules — blocking SQL injection, cross-site scripting (XSS), known bad bot signatures, IP block lists, and custom regex patterns. WAF is deployed on Amazon CloudFront, Application Load Balancers, API Gateway, and AppSync. WAF rules are organized into Web ACLs (Access Control Lists). AWS Managed Rules provide pre-built rule groups (e.g., OWASP Top 10, AWS IP Reputation List) for common threat categories.

*   **AWS Shield**: A managed DDoS protection service. Shield Standard is automatically enabled for all AWS customers at no extra cost, protecting against the most common network (Layer 3/4) DDoS attacks. Shield Advanced is a paid subscription offering enhanced DDoS protection for high-risk applications (CloudFront, Route 53, ALB, Elastic IPs), 24/7 access to the AWS DDoS Response Team (DRT), near real-time visibility into DDoS events, and financial protection against scaling cost spikes during attacks.

*   **Amazon GuardDuty**: A managed threat detection service that continuously analyzes AWS CloudTrail events, VPC Flow Logs, and DNS logs using machine learning and threat intelligence feeds to identify malicious or unauthorized behavior. GuardDuty detects threats such as compromised EC2 instances communicating with known malware command-and-control servers, credential exfiltration, unusual API calls from unexpected locations, and cryptomining activity. GuardDuty requires no agents and no changes to existing infrastructure — enabling it takes two clicks.

*   **AWS Secrets Manager**: A service that stores, rotates, and retrieves application secrets (database passwords, API keys, OAuth tokens) securely. Secrets Manager can automatically rotate RDS, Redshift, and DocumentDB credentials on a configurable schedule by invoking a Lambda function. Applications retrieve the current secret value via API call rather than reading hardcoded configuration files. Secrets Manager is preferable to SSM Parameter Store (which also stores secrets) when automatic rotation is required.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Coverage:** Security is the largest exam domain at 30%. Expect 19–20 questions directly testing security services, IAM, encryption, and compliance. Security knowledge appears in almost every other domain question as well.

*   **KMS CMK vs. SSE-S3 Exam Selection:** SSE-S3 uses AWS-managed keys with no customer visibility into key usage. SSE-KMS uses KMS keys with full CloudTrail audit of every Decrypt/Encrypt call. If a question mentions compliance, key rotation control, or auditing of key usage → SSE-KMS. If the question just needs "encryption at rest" with no compliance context → SSE-S3 is simpler and cheaper.

*   **WAF vs. Shield vs. GuardDuty:** WAF = Layer 7 web request filtering (SQL injection, XSS, bad bots). Shield = DDoS protection at Layers 3, 4, and 7. GuardDuty = behavioral threat detection using log analysis. These are complementary, not competing. The exam presents a specific threat type and expects you to select the right service.

*   **GuardDuty vs. Inspector vs. Macie:** GuardDuty = runtime threat detection (is someone attacking me now?). Amazon Inspector = vulnerability scanning of EC2 OS and container images (am I patched?). Amazon Macie = sensitive data discovery in S3 (do I have unprotected PII?). Know these distinctions — the exam tests all three.

*   **Secrets Manager vs. SSM Parameter Store:** Both store secrets. Secrets Manager = automatic rotation built in, higher cost per secret. SSM Parameter Store SecureString = lower cost, manual rotation with Lambda. The exam answer for "automatic database credential rotation" is always Secrets Manager.

*   **Study Resource:** The KMS and WAF developer guides provide comprehensive service documentation: [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/) and [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/). The [AWS Security Best Practices whitepaper](https://aws.amazon.com/whitepapers/) covers defense-in-depth architecture.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the KMS, WAF, Shield, and GuardDuty chapters in the AWS Solutions Architect study materials. Review the [AWS Security Hub documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) to understand how it aggregates findings from GuardDuty, Inspector, and Macie. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "AWS Security Best Practices" and "AWS Best Practices for DDoS Resiliency" whitepapers.

*   **Required Video:** Watch the security services module in the official course playlist, paying close attention to the layered defense architecture (WAF → Shield → GuardDuty → KMS) and the exam-differentiating scenarios for each service: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create a KMS Customer Managed Key and encrypt an S3 bucket:** Create a CMK with a key policy restricting usage to specific IAM Roles. Enable SSE-KMS on an S3 bucket using the CMK ARN. Upload an object and verify in CloudTrail that a `kms:Decrypt` event is logged when the object is downloaded.

*   **Create a WAF Web ACL and attach it to an ALB:** Create a Web ACL with an AWS Managed Rule (e.g., AWS-AWSManagedRulesCommonRuleSet). Attach the Web ACL to an Application Load Balancer. Use a test tool (e.g., curl with a SQL injection string in a query parameter) and verify the WAF blocks the request with a 403 response.

*   **Enable GuardDuty and review findings:** Enable GuardDuty in the AWS Console (one click). Review the sample findings by generating GuardDuty sample findings (`aws guardduty create-sample-findings`). Observe the finding types (e.g., `UnauthorizedAccess:EC2/SSHBruteForce`) and their severity levels.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Review the KMS key policy model at [https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html).
- [ ] Understand WAF rule groups and Web ACLs at [https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html).
- [ ] Watch the AWS Security video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab with KMS encryption, WAF rule creation, and GuardDuty findings.
- [ ] Proceed to the weekly quiz.
