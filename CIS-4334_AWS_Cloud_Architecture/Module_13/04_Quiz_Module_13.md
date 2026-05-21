# Quiz: Module 13 - AWS Security – KMS, WAF, Shield, GuardDuty
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A company's web application running behind an Application Load Balancer is receiving HTTP requests that include SQL injection payloads in query parameters. The security team needs to block these malicious requests without modifying the application code. Which AWS service provides this protection?
*   A) AWS Shield Advanced — enables application-layer DDoS protection against the SQL injection attack.
*   B) Amazon GuardDuty — detects SQL injection attempts in VPC Flow Logs and blocks the source IP automatically.
*   C) AWS WAF (Web Application Firewall) — attach a Web ACL to the ALB with rules that detect and block SQL injection patterns at Layer 7.
*   D) AWS Network Firewall — deploy in the VPC to inspect and block HTTP packets containing SQL injection strings.
*   **Correct Answer:** C) AWS WAF is the Layer 7 firewall that can inspect HTTP request bodies, headers, and query strings for SQL injection patterns and block them before they reach the application.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* AWS Shield protects against volumetric DDoS attacks at Layers 3, 4, and 7. Shield Advanced does include application-layer protections, but it is not designed or managed for blocking specific HTTP request content patterns like SQL injection. WAF is purpose-built for application-layer content filtering.
    *   *Why B is incorrect:* GuardDuty analyzes CloudTrail, VPC Flow Logs, and DNS logs for behavioral threat patterns. VPC Flow Logs contain IP/port metadata, not HTTP payload content. GuardDuty cannot inspect or block HTTP query parameter content, and it does not take blocking actions — it generates findings for human review.
    *   *Why C is correct:* WAF Web ACLs can be attached directly to an ALB. AWS Managed Rules include a SQLi rule group that inspects all request components for SQL injection syntax. WAF blocks matching requests with a 403 Forbidden response before they reach the backend — no application code changes required.
    *   *Why D is incorrect:* AWS Network Firewall operates at the network/transport layer with stateful inspection capabilities. While it can perform deep packet inspection, it is primarily designed for network-level threats (ports, protocols, IP ranges, domain-based filtering). WAF with ALB integration is the more targeted, lower-complexity solution for HTTP application-layer content filtering.

---

**Question 2**
Which of the following is the most accurate description of **Amazon GuardDuty**?
*   A) A vulnerability scanner that periodically scans EC2 instances for missing OS patches and software CVEs, generating remediation reports.
*   B) A managed threat detection service that analyzes CloudTrail API logs, VPC Flow Logs, and DNS logs using machine learning to detect malicious or unauthorized behavior — such as cryptomining, credential compromise, and command-and-control communication.
*   C) A data classification service that uses machine learning to discover and protect sensitive data (PII, financial data) stored in S3 buckets.
*   D) A network-level DDoS mitigation service that absorbs volumetric attacks before they reach AWS infrastructure.
*   **Correct Answer:** B) GuardDuty is a behavioral threat detection service that continuously analyzes multiple AWS log sources using ML and threat intelligence to detect active threats across the AWS environment.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Amazon Inspector, which performs vulnerability assessments on EC2 instances (OS packages, container images) and Lambda function code. Inspector finds known CVEs; GuardDuty detects active behavioral threats.
    *   *Why B is correct:* GuardDuty is the runtime threat detection layer for AWS. It requires no agents, no log routing configuration changes, and no additional infrastructure. Enabling it provides immediate detection coverage across CloudTrail API events, VPC Flow Logs, and DNS logs. Key finding categories include reconnaissance, privilege escalation, persistence, and exfiltration.
    *   *Why C is incorrect:* This describes Amazon Macie, which uses ML to discover sensitive data (PII, credit card numbers, SSNs) in S3 buckets. Macie is for data loss prevention; GuardDuty is for threat detection.
    *   *Why D is incorrect:* This describes AWS Shield (Standard or Advanced), which is the DDoS protection layer. Shield operates at the network edge; GuardDuty operates by analyzing control plane and network flow logs.

---

**Question 3**
A compliance requirement mandates that all encryption keys for an application's S3 data must support annual automated rotation, and all key usage must be logged in an auditable trail. Which S3 encryption configuration satisfies these requirements?
*   A) SSE-S3 (Server-Side Encryption with Amazon S3-managed keys) — AWS manages key rotation automatically with no customer configuration needed.
*   B) SSE-KMS with a Customer Managed Key (CMK) configured with annual automatic rotation enabled; all KMS API calls are automatically logged to CloudTrail.
*   C) SSE-C (Server-Side Encryption with Customer-Provided Keys) — the customer provides keys on each request, maintaining full key audit control outside of AWS.
*   D) Client-side encryption using the AWS Encryption SDK — encrypt data before upload so no AWS service has access to the plaintext or key metadata.
*   **Correct Answer:** B) SSE-KMS with a CMK provides both automatic annual key rotation and comprehensive CloudTrail audit logging of every Encrypt/Decrypt API call — satisfying both compliance requirements.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SSE-S3 uses AWS-managed keys that do auto-rotate, but key usage is NOT logged to CloudTrail. There is no audit trail showing which IAM principal accessed which S3 object via decryption. This fails the "auditable trail" requirement.
    *   *Why B is correct:* KMS CMKs can be configured with automatic annual rotation. Every KMS API call (GenerateDataKey, Decrypt) is logged to CloudTrail with the caller's identity, timestamp, and resource. This provides both rotation and auditability — the combination required by compliance mandates like PCI DSS and HIPAA.
    *   *Why C is incorrect:* SSE-C requires the customer to provide the encryption key with every PUT and GET request. AWS never stores the key, and key usage is not logged to CloudTrail (the key is only in the HTTP header). This satisfies key control but fails the "auditable trail" requirement through AWS-native logging.
    *   *Why D is incorrect:* Client-side encryption keeps all key management external to AWS, which can satisfy some compliance requirements but removes the auditability provided by KMS CloudTrail integration. The key usage trail is not in CloudTrail — it is managed entirely outside AWS, adding operational complexity.

---

**Question 4**
An AWS account shows unexpected EC2 instances launched in Regions the company does not normally use, and CloudTrail logs show API calls from unusual IP addresses in Eastern Europe. The security team suspects a compromised IAM credential. Which AWS service would have generated an automated finding alerting the team to this behavior before manual review?
*   A) AWS Config — detects and alerts on resource configuration changes including EC2 instance launches in unexpected Regions.
*   B) Amazon GuardDuty — analyzes CloudTrail logs using ML-based anomaly detection to generate findings for unusual API call patterns, unexpected Region activity, and credentials being used from unexpected locations.
*   C) AWS Trusted Advisor — flags account-level security vulnerabilities including suspicious IAM activity patterns.
*   D) AWS Security Hub — correlates findings from multiple services and generates a consolidated security score that alerts the team to anomalous activity.
*   **Correct Answer:** B) GuardDuty would generate findings for both the unusual Region API activity and the credential use from an unexpected geographic location — both are behavioral anomaly patterns in GuardDuty's threat detection model.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* AWS Config tracks resource configuration changes and can alert on EC2 instances being launched in specific Regions (via Config Rules), but it does not analyze behavioral anomalies in CloudTrail API calls or use ML to detect threat patterns. Config is a configuration compliance tool, not a threat detection tool.
    *   *Why B is correct:* GuardDuty findings like `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration` and `PenTest:IAMUser/KaliLinux` are generated by analyzing CloudTrail logs for anomalous behaviors. Credential use from geographically unusual locations is a core GuardDuty detection capability, triggered before manual review could catch it.
    *   *Why C is incorrect:* AWS Trusted Advisor provides recommendations across cost, performance, security, and reliability based on account-level best practices (e.g., "MFA not enabled on root account"). It does not perform behavioral analysis of CloudTrail API calls or generate real-time threat findings.
    *   *Why D is incorrect:* AWS Security Hub aggregates and normalizes findings from GuardDuty, Inspector, Macie, and other services — it is a central findings aggregation layer. However, Security Hub does not perform its own threat detection; it relies on services like GuardDuty to generate the findings it aggregates.

---

**Question 5**
A company runs a public-facing API on CloudFront + API Gateway. They experience a large-scale DDoS attack generating millions of requests per second targeting their API Gateway endpoint. The attack is causing legitimate user requests to time out. Which two AWS services should be deployed together to protect against both volumetric (Layer 3/4) and application-layer (Layer 7) DDoS attacks while also filtering malicious HTTP requests?
*   A) Amazon GuardDuty and AWS Config
*   B) AWS Shield Advanced and AWS WAF
*   C) AWS KMS and Amazon Inspector
*   D) AWS Shield Standard and Amazon Macie
*   **Correct Answer:** B) Shield Advanced provides enhanced DDoS mitigation at Layers 3, 4, and 7 with 24/7 DRT support and cost protection; WAF provides Layer 7 HTTP request filtering to block malicious traffic patterns.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GuardDuty provides threat detection from log analysis but does not actively block or mitigate attack traffic. AWS Config monitors resource configurations for compliance. Neither service provides active DDoS mitigation or request blocking capabilities.
    *   *Why B is correct:* This is the canonical AWS DDoS protection architecture for public-facing applications. Shield Advanced mitigates volumetric attacks (SYN floods, UDP reflection, etc.) and provides application-layer DDoS protection with the DRT during active attacks. WAF filters malicious HTTP requests (rate-based rules block request floods, WAF rules block bad bots and attack signatures) at Layer 7. Together they provide defense in depth for the described attack scenario.
    *   *Why C is incorrect:* AWS KMS is an encryption key management service — it has no role in DDoS mitigation or traffic filtering. Amazon Inspector is a vulnerability scanner for EC2 and container images. Neither addresses the described attack.
    *   *Why D is incorrect:* Shield Standard is automatically enabled and provides basic Layer 3/4 protection, but it does not include the enhanced application-layer protection, DRT access, or cost protection that Shield Advanced provides for high-risk public APIs. Amazon Macie is a data classification service for S3 — it has no role in DDoS protection.

