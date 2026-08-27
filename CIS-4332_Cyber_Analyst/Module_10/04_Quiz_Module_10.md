# Quiz: Module 10 — Cloud Security Analysis

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Instructions

Answer all 10 questions. Each question is worth 10 points. Select the single best answer.

---

## Question 1

A developer at a cloud-hosted company commits code to a public GitHub repository. The commit includes AWS access keys belonging to an IAM user with the policy `"Action": "*", "Resource": "*"` attached. A threat actor discovers the keys within four hours and uses them to enumerate S3 buckets, read customer data, create a new IAM user, and disable CloudTrail. Which aspect of the shared responsibility model best explains why this incident resulted in full account-level impact?

- A) AWS failed to secure the exposed IAM user's credentials because access key protection is a cloud provider responsibility under the IaaS model
- B) The customer bears responsibility for IAM configuration and access key management — the overly permissive policy and absence of key rotation controls are customer-side failures that amplified the incident's scope
- C) The incident demonstrates that IaaS is inherently less secure than SaaS because the customer must manage the underlying operating system
- D) AWS should have automatically revoked the access key when it detected enumeration activity, making this a shared provider-customer failure

Correct Answer: B

Distractor Analysis:

- A is incorrect. Access key management and IAM policy configuration are explicitly customer responsibilities under the AWS shared responsibility model. AWS provides the IAM service and the controls; the customer is responsible for using them correctly — including not committing access keys to public repositories and not granting wildcard permissions.
- B is correct. The shared responsibility model places IAM configuration, access key lifecycle management, and permission scoping entirely within the customer's responsibility domain. The wildcard policy gave the attacker unrestricted access to all AWS services. Key rotation controls (or automatic revocation on exposure) were absent. Both failures are customer-side responsibilities that directly determined the incident's blast radius.
- C is incorrect. The IaaS vs. SaaS comparison is not the relevant analysis here. The incident was caused by a specific IAM misconfiguration and credential management failure — not by the service model category.
- D is incorrect. While AWS does offer services like IAM Access Analyzer and GuardDuty that can detect anomalous activity, the primary obligation to prevent credential exposure and configure least-privilege policies belongs to the customer. AWS does not automatically revoke keys based on detected misuse — this would disrupt legitimate operations that look anomalous.

---

## Question 2

A security analyst reviewing AWS CloudTrail logs finds the following event: `eventName: DeleteTrail`, `userIdentity.userName: temp-analyst`, `sourceIPAddress: 198.51.100.22`. The analyst has confirmed that `temp-analyst` is a legitimate IAM user but has no documented authorization to modify CloudTrail configuration. Which MITRE ATT&CK tactic does this event represent, and what is the immediate investigative priority?

- A) Exfiltration — the analyst should search VPC Flow Logs for large outbound data transfers from the same IP address
- B) Defense Evasion — the analyst should determine what activity occurred in the CloudTrail logs immediately before the deletion event, since the attacker's goal is to prevent logging of subsequent activity
- C) Persistence — the analyst should check whether new IAM users or access keys were created by the same identity before the trail was deleted
- D) Initial Access — the analyst should investigate how the `temp-analyst` account was created and whether it represents unauthorized account creation

Correct Answer: B

Distractor Analysis:

- A is incorrect. While exfiltration is a concern in a broader investigation, `DeleteTrail` is a Defense Evasion technique — its purpose is to blind the logging system so subsequent attacker activity is not recorded. Investigating exfiltration is appropriate as a follow-on step but not the immediate priority.
- B is correct. `DeleteTrail` maps to ATT&CK T1562 — Impair Defenses. When an attacker deletes a CloudTrail trail, their goal is to ensure that actions taken after the deletion are not logged. The analyst's immediate priority is to review all events captured before the deletion to understand what the attacker has already done and to re-enable logging immediately to restore visibility.
- C is incorrect. Persistence (creating IAM users or access keys) is a relevant concern, but the `DeleteTrail` event itself is Defense Evasion. Persistence investigation is appropriate as a parallel investigation, not the primary classification of this specific event.
- D is incorrect. `DeleteTrail` is not an Initial Access technique — Initial Access describes how the attacker first entered the environment. The `temp-analyst` account may already represent a persistence mechanism, but the deletion of the CloudTrail trail is Defense Evasion.

---

## Question 3

An AWS EC2 instance running a customer-facing web application has an IAM role attached with the `AdministratorAccess` policy. A penetration tester discovers that the application has a Server-Side Request Forgery (SSRF) vulnerability. Why does this specific combination of vulnerability and IAM configuration represent a critical severity finding?

- A) SSRF vulnerabilities are always critical severity regardless of IAM configuration because they allow the attacker to access any internal IP address on the VPC network
- B) The SSRF vulnerability allows the attacker to retrieve temporary AWS credentials from the instance metadata service, and the AdministratorAccess policy means those credentials grant full control of the entire AWS account
- C) The IAM role with AdministratorAccess is the critical finding; the SSRF vulnerability is informational because SSRF cannot be exploited without direct network access to the instance
- D) The SSRF vulnerability allows the attacker to bypass the EC2 security group rules, making the instance's network exposure the critical risk rather than the IAM permissions

Correct Answer: B

Distractor Analysis:

- A is incorrect. SSRF severity depends heavily on what is accessible from the server. While SSRF allows access to internal services, not all internal services contain critical data. The critical severity in this scenario comes specifically from the combination of SSRF and the high-permission IAM role — the SSRF is the mechanism and the IAM role is the blast radius multiplier.
- B is correct. The EC2 Instance Metadata Service at `http://169.254.169.254` is accessible from the instance itself. An SSRF vulnerability allows an external attacker to make the server retrieve that URL and return the contents — including the IAM role's temporary access key, secret key, and session token. With `AdministratorAccess`, those credentials grant full unrestricted access to every AWS service in the account. This converts a web application vulnerability into full cloud account compromise.
- C is incorrect. The SSRF vulnerability is the exploitation mechanism — without it, the IAM role's permissiveness affects only someone who already has legitimate access to the instance. The combination creates the critical risk. SSRF does not require direct network access from the attacker's perspective — it exploits the server's ability to make outbound requests.
- D is incorrect. SSRF does not bypass security group rules. The security group controls inbound traffic from the internet. The SSRF exploits the server's ability to make requests from inside the VPC, which is not controlled by inbound security group rules. The risk is the metadata service access, not security group bypass.

---

## Question 4

A cloud security analyst uses the AWS CLI to generate a credential report and finds the following entry for an IAM user: `access_key_1_last_used_date: N/A`, `access_key_1_last_rotated: 2021-06-15`, `mfa_active: false`. Today's date is 2024-03-15. Which two security findings does this credential report entry reveal?

- A) The access key has never been used and is 1,004 days old without rotation; MFA is not configured on this account — both represent least-privilege and identity hygiene violations
- B) The account's MFA being disabled means it cannot be used for console login; the old access key indicates the user has been deprovisioned
- C) The access key age exceeds the 90-day rotation requirement, but MFA is optional for programmatic-access-only IAM users and is not a finding
- D) The `N/A` last used date means the key has been rotated recently and does not represent a finding; only the missing MFA is a security concern

Correct Answer: A

Distractor Analysis:

- A is correct. In the AWS credential report, `last_used_date: N/A` means the access key has never been used since it was created. An access key created on 2021-06-15 and never used means it is an orphaned credential that has been sitting untouched for nearly three years — a prime candidate for theft and use without detection, since there is no baseline of normal activity to deviate from. Combined with no MFA on the account (which protects console access), this represents two distinct IAM hygiene findings that should be remediated: rotate or delete the stale access key, and enforce MFA.
- B is incorrect. MFA being disabled does not prevent console login — it removes the second authentication factor, making the account more vulnerable to password-based compromise. A missing MFA is a security finding, not a functional limitation. The old access key with `N/A` last used indicates a potentially orphaned credential, not confirmed deprovisioning.
- C is incorrect. MFA is not optional for IAM users in a security-hardened environment, even programmatic users. The CIS AWS Foundations Benchmark requires MFA for all IAM users. Programmatic users with both console access and access keys are particularly at risk without MFA.
- D is incorrect. `N/A` for `last_used_date` in an AWS credential report explicitly means the key has never been used — it is not an indicator of recent rotation. Recent rotation would show a recent date in `last_rotated`. An access key with a 2021 rotation date and no usage history is a stale credential, not a recently rotated one.

---

## Question 5

A GuardDuty finding appears with the type `UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B` for an IAM user that normally operates from company IP addresses in the United States. The finding shows a console login from an IP address geolocated to Eastern Europe at 3:00 AM local time, followed immediately by API calls to `DescribeInstances`, `ListBuckets`, and `GetSecretValue`. Which initial response action is highest priority and why?

- A) Disable the IAM user account immediately to prevent further API calls, then investigate the authentication event in Azure AD to determine if the same credentials were used across cloud platforms
- B) Disable or deactivate the IAM user's console access and access keys immediately to stop the active session, then review CloudTrail for all API calls made during and after the anomalous login to determine what data was accessed
- C) Rotate the IAM user's password and leave the session active to observe what the attacker accesses next, collecting intelligence before containment
- D) File a report with GuardDuty suppression rules to prevent future false positive alerts for this user, then investigate during business hours when the security team is fully staffed

Correct Answer: B

Distractor Analysis:

- A is incorrect. The first sentence (disable the IAM user) is the correct immediate action, but AWS IAM is not integrated with Azure AD — these are separate identity systems. The investigation should focus on CloudTrail in the AWS account where the anomalous login occurred, not Azure AD.
- B is correct. An active unauthorized console session in progress — accessing secrets and enumerating resources — must be stopped immediately. Disabling the IAM user's console access and revoking or deactivating access keys terminates the attacker's ability to take further action. Concurrent CloudTrail review establishes what the attacker already accessed (scope assessment) and what may have been exfiltrated or modified. This sequence mirrors the incident response triage process: contain active access, then assess impact.
- C is incorrect. Leaving an active attacker session running to collect intelligence creates ongoing risk of data exfiltration, resource modification, or persistence establishment. The intelligence value does not justify the continued exposure. Real incident response does not allow attackers to continue operating to gather information.
- D is incorrect. This is a high-confidence GuardDuty finding based on geolocation anomaly combined with sensitive API calls. Suppressing it and delaying investigation until business hours allows the attacker to continue operating for potentially many hours. Active security incidents require immediate response regardless of time of day.

---

## Question 6

A CSPM scan of an AWS account identifies that an S3 bucket named `company-hr-records` has the following configuration: `BlockPublicAcls: false`, `BlockPublicPolicy: false`, `IgnorePublicAcls: false`, `RestrictPublicBuckets: false`. Additionally, the bucket ACL has a grant for `AllUsers` with `READ` permission. What is the correct immediate remediation, and why is this a critical severity finding?

- A) Enable S3 versioning on the bucket to prevent data modification; this is a medium severity finding because read-only access does not allow attackers to delete data
- B) Enable server-side encryption on the bucket; this is a high severity finding because unencrypted data is more easily exfiltrated if the bucket is accessed
- C) Enable all four S3 Block Public Access settings at the bucket level and remove the `AllUsers READ` ACL grant; this is a critical severity finding because any unauthenticated internet user can read all objects in the bucket
- D) Move the HR records to an encrypted EBS volume instead of S3; this is a high severity finding because S3 is not appropriate for sensitive HR data

Correct Answer: C

Distractor Analysis:

- A is incorrect. Versioning prevents data loss and enables recovery from deletion or modification attacks — it does not address unauthorized access. The critical finding is that the bucket is publicly readable, not that its contents could be deleted. Severity is critical, not medium: read access to HR records exposes PII and may trigger breach notification obligations.
- B is incorrect. Server-side encryption at rest protects data from physical media theft and some insider threats — it does not prevent an authenticated (or in this case, unauthenticated public) request from reading the objects. If the bucket is publicly accessible, encryption at rest does not prevent the attacker from reading the plaintext data via normal S3 API calls.
- C is correct. The four S3 Block Public Access settings are the definitive control for preventing public access: they block public ACLs, public bucket policies, and restrict public access regardless of bucket-level configuration. The `AllUsers READ` ACL grant is the specific misconfiguration that makes the bucket publicly readable. Removing the ACL grant and enabling all four Block Public Access settings closes the exposure. This is critical severity because HR records contain PII (names, SSNs, compensation, health information) and public exposure may trigger GDPR, state breach notification, and potentially HIPAA obligations.
- D is incorrect. EBS volumes are attached to specific EC2 instances and are not a general-purpose object storage replacement for S3. S3 is an appropriate storage service for HR records when configured correctly with access controls and encryption. The finding is a misconfiguration — not a wrong service choice.

---

## Question 7

A cloud security analyst is reviewing IAM policies for a Lambda function that processes payment transactions. The function's execution role has the following policy attached: `"Action": "s3:*", "Resource": "*"`. The function's actual documented requirement is to write transaction logs to a single specific S3 bucket named `payments-audit-logs`. Which principle is violated and what is the minimum-permission replacement policy for the `Action` and `Resource` fields?

- A) Defense in depth is violated; replace with `"Action": "s3:PutObject", "Resource": "arn:aws:s3:::payments-audit-logs/*"` to restrict writes to the specific bucket
- B) Separation of duties is violated; the Lambda function should not have any S3 access — all file writes should be handled by a separate IAM user account
- C) Least privilege is violated; replace with `"Action": "s3:PutObject", "Resource": "arn:aws:s3:::payments-audit-logs/*"` to grant only the write action needed on only the target bucket's objects
- D) Least privilege is violated; replace with `"Action": ["s3:PutObject", "s3:GetObject"], "Resource": "arn:aws:s3:::payments-audit-logs/*"` because Lambda functions always need read access in addition to write access

Correct Answer: C

Distractor Analysis:

- A is incorrect. The remediation in option A is technically identical to option C, but the principle violation is least privilege — not defense in depth. Defense in depth describes a layered security architecture; least privilege describes the principle of granting minimal required permissions. The distinction matters for the exam.
- B is incorrect. Separation of duties is a principle that prevents a single entity from having end-to-end control of a sensitive process — for example, preventing the same person from both initiating and approving a financial transaction. A Lambda function writing to S3 does not raise a separation of duties concern. Using IAM roles for Lambda execution is the correct approach, not delegating to a separate IAM user.
- C is correct. Least privilege requires granting only the permissions required for the intended function. The Lambda function needs to write objects to one specific bucket. The correct policy grants `s3:PutObject` (not `s3:*`) and restricts the resource to the specific bucket ARN and its objects (`arn:aws:s3:::payments-audit-logs/*`). This prevents the function from reading, deleting, or listing objects in any bucket — including the audit bucket itself.
- D is incorrect. The Lambda function's documented requirement is to write transaction logs. Read access (`s3:GetObject`) is not part of the documented requirement and should not be granted unless specifically needed. Adding permissions that exceed the documented requirement violates least privilege, even if those permissions might be convenient.

---

## Question 8

An organization runs its web application on EC2 instances behind a load balancer. The security team is implementing controls to prevent future SSRF attacks that could reach the instance metadata service. Which two controls, implemented together, provide the strongest mitigation against SSRF-based credential theft?

- A) Enable CloudTrail in all regions and configure GuardDuty to alert on anomalous API calls from EC2 instance roles
- B) Require IMDSv2 on all EC2 instances (enforcing session token requirement for all metadata requests) and remove the high-permission IAM role from instances that do not require AWS API access
- C) Deploy a Web Application Firewall to block all outbound HTTP requests from the application server to internal IP addresses
- D) Enable VPC Flow Logs and alert on any traffic from the application server to the `169.254.254.0/24` subnet

Correct Answer: B

Distractor Analysis:

- A is incorrect. CloudTrail and GuardDuty are detective controls — they detect anomalous use of credentials after the fact. They do not prevent the SSRF attack from succeeding or prevent the metadata service credentials from being retrieved. Detective controls are valuable but do not address the prevention requirement.
- B is correct. IMDSv2 requires a PUT request to obtain a session token before any GET request to the metadata endpoint. SSRF vulnerabilities typically can only make GET requests (following a redirect) and cannot perform the required PUT-then-GET sequence, blocking metadata access. Additionally, removing the high-permission IAM role from instances that do not need AWS API access eliminates the valuable credential that SSRF would expose — even if SSRF succeeds, there are no useful credentials to steal. Together, these controls address both the exploitation mechanism and the blast radius.
- C is incorrect. WAFs can block certain SSRF patterns in HTTP requests, but the metadata service address `169.254.169.254` is a link-local address accessed by the server internally — it is not an outbound internet request that a perimeter WAF would see. A WAF positioned between internet users and the application cannot block the server's own outbound requests to the link-local metadata address.
- D is incorrect. VPC Flow Logs capture network metadata (IP, port, protocol, bytes) but the metadata service is accessed via link-local addressing within the instance — this traffic may not appear in VPC Flow Logs as standard inter-host network traffic. Even if it did, this is a detective control (alerting after the fact), not a preventive control. The question asks for the strongest mitigation, which requires prevention.

---

## Question 9

An organization's AWS Security Hub dashboard shows a finding: `CIS AWS Foundations Benchmark v1.4.0 — Control 1.4: Ensure no root user account access key exists — FAILED`. The finding shows that the root account has an active access key with `last_used: 847 days ago`. What is the correct remediation and why is this a critical severity finding regardless of the key's age and inactivity?

- A) Rotate the root access key to a new value immediately; an old but not recently used key poses low risk because attackers typically exploit recently active credentials
- B) Delete the root access key entirely — root accounts should never have programmatic access keys; even an unused key represents a persistent critical exposure because root account compromise grants unrestricted access to every AWS service and cannot be limited by IAM policies
- C) Reduce the root access key's permissions by attaching a restrictive IAM policy to the root account; this limits the damage if the key is compromised while preserving programmatic access for legacy integrations
- D) Enable MFA on the root account, which provides sufficient protection for the existing access key; the CIS benchmark finding will clear once MFA is active

Correct Answer: B

Distractor Analysis:

- A is incorrect. Rotating the root access key to a new value is better than leaving the old key active, but it does not address the fundamental problem: root accounts should have no access keys whatsoever. The root account in AWS has unrestricted access to all services and cannot be limited by IAM policies — a compromised root access key is a full account takeover regardless of what policies are attached.
- B is correct. AWS best practice and the CIS Benchmark explicitly state that the root account should not have access keys. The root account bypasses all IAM permission boundaries — no IAM policy can restrict what the root account can do. An access key for the root account, even one that has not been used recently, remains a catastrophic exposure: if the key is discovered, the attacker has unlimited access to all AWS services, all regions, all data, and the ability to modify billing and account settings. Delete the key. If automated processes historically used root keys, they must be migrated to appropriately permissioned IAM roles.
- C is incorrect. IAM policies cannot be attached to or used to restrict the root account. This is a fundamental AWS behavior — root account permissions are not managed through IAM. The root account has unrestricted access regardless of any IAM policy configuration.
- D is incorrect. MFA on the root account is a required separate control (CIS Control 1.5), but enabling MFA does not satisfy Control 1.4 (no root access keys). MFA protects console login; it does not apply to access key authentication. The access key would still be usable for programmatic API calls without MFA. Both controls are required independently.

---

## Question 10

A security analyst is building a detection rule for AWS environments to identify a common cloud persistence technique. The analyst wants to alert on activity that indicates an attacker is creating backdoor access after initial compromise. Which combination of CloudTrail events, occurring in sequence from the same source IP within a 10-minute window, provides the highest-confidence indicator of attacker persistence establishment?

- A) `ListBuckets` followed by `GetObject` followed by `PutObject` — indicating the attacker is staging exfiltration via S3
- B) `DescribeInstances` followed by `RunInstances` followed by `TerminateInstances` — indicating the attacker is testing instance launch capabilities
- C) `CreateUser` followed by `CreateLoginProfile` followed by `CreateAccessKey` — indicating the attacker is creating a new IAM identity with both console and programmatic access for persistent re-entry
- D) `GetCallerIdentity` followed by `ListRoles` followed by `AssumeRole` — indicating the attacker is performing identity reconnaissance before lateral movement

Correct Answer: C

Distractor Analysis:

- A is incorrect. `ListBuckets` → `GetObject` → `PutObject` is a pattern consistent with data staging or exfiltration — an ATT&CK Exfiltration technique. While concerning, this sequence does not represent persistence establishment. Persistence means the attacker is creating a mechanism to return after the initial access vector is closed.
- B is incorrect. `DescribeInstances` → `RunInstances` → `TerminateInstances` could represent resource abuse (cryptomining instance launch and termination after testing) or authorized operational activity. It does not directly represent persistence establishment in the identity domain.
- C is correct. This three-event sequence is the canonical cloud persistence pattern: `CreateUser` creates a new IAM identity the attacker controls; `CreateLoginProfile` enables that identity to log into the AWS console with a password (not just programmatic access); `CreateAccessKey` provides a permanent programmatic credential for that identity. Together, these three actions create a fully functional backdoor account. Even if the originally compromised `dev-jenkins` access key is revoked, the attacker retains access via the new `backup-svc-user` account. This sequence in sequence from the same IP over a short window is high-confidence malicious.
- D is incorrect. `GetCallerIdentity` → `ListRoles` → `AssumeRole` represents identity reconnaissance followed by lateral movement via role assumption — an ATT&CK Discovery then Lateral Movement sequence. While this is a serious finding, it describes an attacker moving laterally or escalating privileges within the existing session, not creating a persistent backdoor that survives credential revocation.

---

## Question 11 (5 points)

A cloud security analyst reviewing Azure Active Directory audit logs finds that a user account has been added to the Global Administrator role by an account that was itself created 48 hours ago. Neither the role assignment nor the new account creation appears in any approved change management tickets. Which cloud attack technique does this sequence most likely represent?

- A) SQL injection against the Azure management API
- B) Privilege escalation via unauthorized role assignment — potentially indicating a compromised account being used to establish privileged persistence before the original compromise is detected
- C) A DDoS attack targeting the Azure identity management service
- D) Legitimate Microsoft Entra ID behavior that creates administrative accounts during tenant provisioning

Correct Answer: B

Distractor Analysis:

- A is incorrect. SQL injection targets database query inputs in web applications. Azure AD role assignment is an identity management operation performed through APIs and portals, not SQL queries.
- B is correct. Creating a new account and immediately elevating it to Global Administrator (or equivalent privileged role) within 48 hours without change management approval is a high-confidence cloud privilege escalation and persistence indicator. This sequence (account creation → privileged role assignment → no ticket) indicates an attacker using a compromised identity to establish a persistent privileged foothold before the original breach is detected.
- C is incorrect. A DDoS attack aims to overwhelm services with traffic, causing unavailability. Account creation and role assignment are identity management events, not traffic-based attacks.
- D is incorrect. Azure tenant provisioning creates specific service accounts with documented, predictable behavior. Untracked Global Administrator role assignments to newly created accounts are not part of normal provisioning and should always be investigated.

---

## Question 12 (5 points)

Which AWS service provides continuous monitoring and threat detection for AWS accounts by analyzing CloudTrail logs, VPC Flow Logs, and DNS logs using machine learning and threat intelligence?

- A) AWS Config
- B) Amazon Inspector
- C) Amazon GuardDuty
- D) AWS Trusted Advisor

Correct Answer: C

Distractor Analysis:

- A is incorrect. AWS Config tracks configuration changes and compliance state of AWS resources. It does not analyze logs for threat detection patterns using machine learning.
- B is incorrect. Amazon Inspector performs automated security assessments of EC2 instances and container images for known vulnerabilities and misconfigurations. It is a vulnerability assessment tool, not a threat detection platform.
- C is correct. Amazon GuardDuty is the AWS managed threat detection service. It continuously analyzes CloudTrail management events, S3 data events, VPC Flow Logs, and DNS logs to identify threats such as compromised credentials, reconnaissance activity, data exfiltration, and cryptomining — applying ML-based anomaly detection and threat intelligence.
- D is incorrect. AWS Trusted Advisor provides cost optimization, performance, security, fault tolerance, and service quota recommendations. Its security checks cover basic hygiene items (open S3 buckets, unrestricted security groups) but it does not perform continuous threat detection or log analysis.

---

## Question 13 (5 points)

An analyst is reviewing GCP (Google Cloud Platform) Cloud Audit Logs and finds that a service account key was created, an IAM policy was modified to grant the service account `roles/owner` on the project, and then a VM instance was created — all within 7 minutes. The service account was not previously documented. What cloud attack phase does this most likely represent?

- A) Initial access via spearphishing
- B) Post-compromise resource abuse — the attacker, having already gained a foothold, is creating privileged infrastructure for cryptomining, data exfiltration, or C2 staging
- C) Normal GCP DevOps automation for continuous deployment pipelines
- D) A GCP billing optimization activity that creates temporary instances to balance workloads

Correct Answer: B

Distractor Analysis:

- A is incorrect. Initial access via spearphishing involves sending a malicious email to gain an initial foothold. The log events described occur after access is already established — they are post-compromise infrastructure actions, not the initial entry vector.
- B is correct. Creating a service account key, granting it owner-level IAM permissions, and then launching VM instances in rapid succession without documentation is a textbook post-compromise cloud resource abuse pattern. Attackers use this sequence to establish persistent access and create compute resources for cryptomining, proxying, or data exfiltration. The speed and undocumented nature are the key indicators.
- C is incorrect. Legitimate CI/CD automation creates predictable, documented resources with tracked service accounts. Undocumented service accounts with owner-level permissions created manually in 7 minutes are not consistent with normal DevOps pipeline behavior.
- D is incorrect. GCP billing optimization does not involve creating new service accounts with owner-level IAM roles. Workload balancing is handled by autoscaling and managed instance groups.

---

## Question 14 (5 points)

Which of the following best describes the cloud security concept of "misconfiguration as the primary attack surface"?

- A) Cloud providers introduce new vulnerabilities faster than they can patch them, making cloud environments inherently less secure than on-premises systems
- B) The most common and impactful cloud security incidents result from customer-controlled configuration errors — such as overly permissive IAM policies, publicly accessible storage buckets, and missing logging — rather than from exploitation of unpatched CVEs in cloud infrastructure
- C) Cloud misconfigurations can only be identified through manual security audits performed by cloud vendor support teams
- D) Misconfigurations in cloud environments are automatically remediated by the cloud provider under the shared responsibility model

Correct Answer: B

Distractor Analysis:

- A is incorrect. Cloud providers have dedicated security teams and patch cloud infrastructure rapidly. The most common cloud breaches are not caused by unpatched cloud infrastructure CVEs — they result from customer IAM and configuration errors.
- B is correct. The industry consensus from Gartner, CSA, and major cloud providers is that misconfiguration is the leading cause of cloud security incidents. Publicly exposed S3 buckets, wildcard IAM policies, disabled CloudTrail, unrestricted security groups, and missing MFA on cloud console accounts are all customer-configurable settings that, when incorrectly set, create the most impactful exposures.
- C is incorrect. Cloud Security Posture Management (CSPM) tools, native cloud security services (AWS Security Hub, Azure Defender for Cloud, GCP Security Command Center), and automated CIS Benchmark scanning can all identify misconfigurations programmatically without vendor support involvement.
- D is incorrect. Under the shared responsibility model, customer-controlled configurations (IAM, storage access policies, logging settings) are entirely the customer's responsibility to configure and maintain. The cloud provider does not automatically correct customer misconfiguration.

---

## Question 15 (5 points)

An analyst investigating an AWS incident finds that `AssumeRole` was called on a role named `OrganizationAccountAccessRole` from an external AWS account ID not belonging to the organization. The role's trust policy contains `"Principal": {"AWS": "*"}`. What does this finding indicate and what is the immediate remediation?

- A) This is normal cross-account federation behavior and requires no action
- B) The role's trust policy allows any AWS account to assume the role — this is a critical misconfiguration that may have enabled unauthorized cross-account access; restrict the trust policy to specific, authorized account IDs immediately
- C) The wildcard principal is required for AWS Organizations integration and cannot be modified
- D) The external AWS account assumption is blocked by default SCPs and requires no remediation

Correct Answer: B

Distractor Analysis:

- A is incorrect. A trust policy with `"Principal": {"AWS": "*"}` grants permission for any entity in any AWS account to assume the role. This is almost never intentional and represents a critical misconfiguration that should be investigated immediately.
- B is correct. An IAM role with a wildcard principal in its trust policy can be assumed by any authenticated AWS principal in any account. If an external account ID successfully called `AssumeRole` on this role, unauthorized cross-account access occurred. The immediate action is to update the trust policy to restrict the principal to specific authorized account IDs or ARNs.
- C is incorrect. AWS Organizations cross-account access uses specific trust policies with the organization's master account ID or an organization unit condition — not a wildcard. The wildcard is never a required or recommended configuration for Organizations integration.
- D is incorrect. SCPs (Service Control Policies) can restrict what services a member account can use but do not block `AssumeRole` calls from external accounts by default. Trust policy restrictions are the correct control for cross-account role access.

---

## Question 16 (5 points)

In a containerized environment running Kubernetes, an attacker exploits a vulnerability in a pod and gains container escape to the underlying node. Which Kubernetes security control, if properly configured, would have most limited the blast radius of this container escape?

- A) Network policies restricting inbound traffic to the pod on specific ports
- B) Pod Security Admission enforcing restricted security contexts — preventing containers from running as root, disabling privilege escalation, and requiring read-only root filesystems
- C) Resource quotas limiting CPU and memory usage per namespace
- D) Horizontal Pod Autoscaler configuration

Correct Answer: B

Distractor Analysis:

- A is incorrect. Network policies restrict network communication to and from pods. They reduce the attack surface for network-based exploits but do not prevent container escape techniques that exploit kernel vulnerabilities or privileged container configurations.
- B is correct. Pod Security Admission (PSA) with the restricted security context prevents containers from running with root privileges, disables Linux capability additions, requires read-only root filesystems, and prevents privilege escalation. These constraints significantly limit the techniques available for container escape — a container running without root privileges and with a read-only filesystem has far fewer escape paths than a privileged container.
- C is incorrect. Resource quotas limit computational resources per namespace. They prevent resource exhaustion but have no effect on privilege-based container escape techniques.
- D is incorrect. Horizontal Pod Autoscaler manages scaling of pods based on metrics. It has no security function related to container escape prevention.

---

## Question 17 (5 points)

A cloud security analyst discovers that an S3 bucket containing application logs has been configured with `Block Public Access: Off` and the bucket policy includes `"Principal": "*", "Action": "s3:GetObject"`. The bucket contains 14 months of application logs. What is the immediate risk and remediation action?

- A) The bucket is accessible only to authenticated AWS users; no immediate action is required
- B) The bucket is publicly readable by anyone on the internet — any person with the bucket URL can download all 14 months of application logs; immediately enable S3 Block Public Access and remove the public-read bucket policy
- C) The bucket policy with wildcard principal only applies to AWS service accounts, not external internet users
- D) Application logs cannot contain sensitive data so the public accessibility presents no meaningful risk

Correct Answer: B

Distractor Analysis:

- A is incorrect. `"Principal": "*"` in an S3 bucket policy means any principal — including unauthenticated requests from the public internet — can perform the allowed actions. This is not limited to authenticated users.
- B is correct. An S3 bucket with Block Public Access disabled and a bucket policy allowing `s3:GetObject` for `Principal: *` is fully publicly readable without any authentication. Any person with the bucket URL (which can be enumerated or exposed) can download all objects. Application logs frequently contain sensitive data including IP addresses, user identifiers, authentication events, and application errors. Immediate remediation is to enable S3 Block Public Access and remove or restrict the bucket policy.
- C is incorrect. `"Principal": "*"` means all principals, including anonymous (unauthenticated) internet users. It is not limited to AWS service accounts.
- D is incorrect. Application logs routinely contain PII, authentication tokens, session identifiers, IP addresses, and business logic information that can be exploited by attackers for reconnaissance and further attacks.

---

## Question 18 (5 points)

Which cloud security framework provides a hierarchical set of security controls mapped to cloud service provider services and organized into 17 domains including Identity and Access Management, Infrastructure Security, and Data Security?

- A) NIST Cybersecurity Framework (CSF)
- B) Cloud Security Alliance (CSA) Cloud Controls Matrix (CCM)
- C) CIS Benchmarks
- D) ISO 27001

Correct Answer: B

Distractor Analysis:

- A is incorrect. The NIST CSF is a general cybersecurity risk framework with five functions (Identify, Protect, Detect, Respond, Recover). It is not cloud-specific and does not organize controls into cloud-oriented domains.
- B is correct. The CSA Cloud Controls Matrix (CCM) is the cloud industry's most widely referenced control framework. It organizes 197 control objectives into 17 domains specifically addressing cloud security concerns, with mappings to major compliance frameworks (ISO 27001, SOC 2, NIST SP 800-53) and cloud provider services.
- C is incorrect. CIS Benchmarks are hardening guides providing specific technical configuration recommendations for operating systems, cloud platforms, databases, and applications. They are implementation-level guides, not a control framework with domain structure.
- D is incorrect. ISO 27001 is a general information security management system standard. While applicable to cloud environments, it is not cloud-specific and does not map controls to cloud provider services in the CCM's domain structure.

---

## Question 19 (5 points)

An analyst wants to verify whether any EC2 instances in an AWS account are publicly accessible via SSH (port 22) from the internet. Which AWS native tool provides an automated compliance check for this condition?

- A) AWS CloudTrail — query for `AuthorizeSecurityGroupIngress` events with port 22
- B) AWS Security Hub — CIS AWS Foundations Benchmark control for unrestricted SSH access
- C) Amazon VPC Flow Logs — filter for inbound port 22 traffic
- D) AWS Cost Explorer — review resource usage for all EC2 instances

Correct Answer: B

Distractor Analysis:

- A is incorrect. CloudTrail logging `AuthorizeSecurityGroupIngress` events would show when SSH rules were created but does not provide an ongoing compliance assessment of current security group state. Historical event analysis does not tell you current configuration state.
- B is correct. AWS Security Hub includes the CIS AWS Foundations Benchmark as a built-in security standard. Control 4.1 specifically checks for security groups that allow unrestricted (0.0.0.0/0) inbound access on port 22. This provides a continuous, automated compliance check with findings for non-compliant security groups.
- C is incorrect. VPC Flow Logs capture actual network traffic — they would show if SSH connections are being made but do not assess whether the security group configuration allows unrestricted access. You would see traffic after the fact, not the misconfiguration itself.
- D is incorrect. AWS Cost Explorer is a billing and cost management tool. It provides no security configuration assessment capability.

---

## Question 20 (5 points)

Under the cloud shared responsibility model for SaaS (Software as a Service), which security control remains the customer's responsibility?

- A) Patching the underlying operating system on which the SaaS application runs
- B) Managing the physical security of the data center hosting the SaaS application
- C) Managing user identity and access controls — including which users are provisioned, their privilege levels, and offboarding processes when users leave the organization
- D) Encrypting data at the storage layer within the SaaS provider's infrastructure

Correct Answer: C

Distractor Analysis:

- A is incorrect. In a SaaS model, the cloud provider is responsible for all infrastructure including OS patching. The customer has no access to or responsibility for the underlying operating system.
- B is incorrect. Physical data center security is always the cloud provider's responsibility under all service models (IaaS, PaaS, SaaS). Customers have no physical access to the provider's facilities.
- C is correct. Identity and access management is explicitly the customer's responsibility even in a SaaS model. The customer controls which users are provisioned, what roles and permissions they have, and whether access is revoked when employees leave. Failure to offboard departing employees promptly from SaaS applications is a common cloud access control gap.
- D is incorrect. In a SaaS model, the cloud provider manages all data storage infrastructure including at-rest encryption at the storage layer. Customers may have the ability to provide their own encryption keys (customer-managed keys) in some SaaS offerings, but base storage encryption is a provider responsibility.
