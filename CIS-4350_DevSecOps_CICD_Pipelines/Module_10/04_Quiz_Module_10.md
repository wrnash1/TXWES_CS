# Quiz: Module 10 — Cloud Security Posture Management (CSPM)

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

**Instructions:** Select the single best answer for each question. Review the distractor analysis after completing the quiz.

---

### Question 1

A security engineer is evaluating CSPM tools for a company that uses AWS, Azure, and GCP simultaneously. Which tool is best suited for this multi-cloud environment and provides a graph-based cloud attack path analysis capability?

- A) AWS Security Hub — evaluates AWS accounts against CIS Benchmarks and the AWS Foundational Security Standard
- B) Microsoft Defender for Cloud — provides Secure Score and Azure-native posture management
- C) Wiz — constructs a security graph across all cloud environments and surfaces toxic combinations of misconfigurations as attack paths
- D) Checkov — performs static analysis of Terraform configuration files before cloud resources are provisioned

- **Correct Answer:** C) Wiz. It provides multi-cloud coverage AND a unique graph-based attack path model that identifies dangerous combinations of misconfigurations — not just individual findings.
- **Distractor Analysis:**
  - *Why C is correct:* Wiz covers AWS, Azure, GCP, and other cloud platforms. Its distinguishing capability is the security graph that links identities, workloads, network paths, and data stores to identify "toxic combinations" — situations where individual low-severity misconfigurations combine into a critical attack path.
  - *Why A is incorrect:* AWS Security Hub is native to AWS only. It does not provide graph-based attack path analysis and does not cover Azure or GCP environments.
  - *Why B is incorrect:* Microsoft Defender for Cloud is Azure-native. While it has some multi-cloud capabilities, it is primarily an Azure posture tool and does not provide graph-based attack path analysis.
  - *Why D is incorrect:* Checkov is an IaC scanner — it analyzes Terraform and other IaC files before deployment. It does not scan live cloud environments and does not provide attack path analysis.

---

### Question 2

A DevSecOps team wants to catch S3 bucket misconfigurations before Terraform deploys them to AWS. At which stage of the CI/CD pipeline should they add a Checkov scan?

- A) After `terraform apply` completes, to scan the live AWS resources using Checkov's cloud scanning mode
- B) After `terraform plan`, to use the plan JSON file as Checkov's input for more accurate analysis
- C) At the pull-request stage, before any Terraform commands run, to scan the static .tf files
- D) After merging to the main branch but before deploying to production, to catch misconfigurations in the final merged code

- **Correct Answer:** C) The pull-request stage. Checkov performs static analysis of .tf files and does not require Terraform plan or apply to have run. Running at the PR stage applies the shift-left principle — catching misconfigurations before any infrastructure is provisioned.
- **Distractor Analysis:**
  - *Why C is correct:* Checkov analyzes Terraform .tf files statically and can run immediately after checkout. Running it at the PR stage means a misconfigured S3 bucket is caught in code review, not after it has been deployed and potentially exposed data.
  - *Why A is incorrect:* Scanning after apply means the misconfigured infrastructure has already been provisioned and may have been accessible to external parties. This is reactive, not proactive, and violates the shift-left principle.
  - *Why B is incorrect:* While Checkov supports scanning terraform plan JSON output, this is not its primary use case. Scanning static .tf files at the PR stage is earlier and catches misconfigurations before any Terraform command runs.
  - *Why D is incorrect:* Waiting until after merge to the main branch is too late. Misconfigurations in main can be immediately applied to production infrastructure. The PR stage is the appropriate gate.

---

### Question 3

An organization implements an AWS Service Control Policy that denies `cloudtrail:StopLogging`, `cloudtrail:DeleteTrail`, and `cloudtrail:UpdateTrail` for all accounts in the organization. Which CSPM control type does this SCP represent?

- A) Detective control — it identifies CloudTrail changes that have already occurred
- B) Preventive control — it prevents CloudTrail from being disabled regardless of individual IAM permissions
- C) Reactive control — it automatically re-enables CloudTrail when it is stopped
- D) Corrective control — it creates an audit log of all attempts to modify CloudTrail

- **Correct Answer:** B) Preventive control. An SCP enforced at the AWS Organizations level prevents the specified API actions from executing, regardless of what individual IAM policies allow. This stops misconfigurations before they occur.
- **Distractor Analysis:**
  - *Why B is correct:* SCPs operate at the organization level and set the maximum permissions boundary for all accounts and roles. Even if an administrator has full IAM permissions, a Deny in an SCP prevents the action. This is a preventive control — it blocks the misconfiguration from occurring.
  - *Why A is incorrect:* Detective controls identify misconfigurations that already exist. An SCP does not detect or report — it prevents. AWS Config Rules and Security Hub findings are examples of detective controls.
  - *Why C is incorrect:* Reactive controls (auto-remediation) fix misconfigurations after they occur. An SCP cannot observe that CloudTrail was stopped and re-enable it — that would require a Config Rule with an auto-remediation SSM document.
  - *Why D is incorrect:* Creating audit logs is a logging or monitoring control. CloudTrail itself is the audit log service. The SCP described here prevents modification of CloudTrail, not the creation of logs.

---

### Question 4

During a Prowler CIS compliance assessment of an AWS account, a finding is generated with severity CRITICAL: `cloudtrail-logging-enabled — Ensure CloudTrail is enabled in all regions`. The organization has decided this region is low-risk and will not remediate within the standard SLA. What is the correct process according to CSPM exception management best practices?

- A) Permanently suppress the finding in Prowler using the `--skip-check` flag so it does not appear in future reports
- B) Document the finding in a formal exceptions register with business justification, a named risk owner, compensating controls, and an expiry date of no more than 12 months
- C) Reduce the finding severity to Low in Prowler's configuration so it does not trigger the CRITICAL SLA
- D) Close the finding in the CSPM console as a false positive since the region is considered low-risk

- **Correct Answer:** B) A formal exceptions register entry with documented justification, risk owner, compensating controls, and a maximum 12-month expiry date. This is the auditable risk acceptance process required for SOC 2 and PCI-DSS compliance.
- **Distractor Analysis:**
  - *Why B is correct:* Formal exception management requires documentation of the accepted risk, business justification, a named individual who accepts responsibility, compensating controls that reduce risk in lieu of remediation, and an expiry date that forces periodic review. This creates an audit trail for compliance assessments.
  - *Why A is incorrect:* Permanently suppressing a finding removes it from visibility entirely with no documentation of why the risk was accepted. This is an audit failure — assessors reviewing SOC 2 or PCI-DSS controls will find no evidence that the finding was ever considered.
  - *Why C is incorrect:* Changing the severity in tool configuration to avoid SLA triggers is a form of data manipulation. It obscures the true risk posture and violates audit integrity requirements.
  - *Why D is incorrect:* Closing findings as false positives when they are true positives (CloudTrail is genuinely not enabled) is incorrect. A false positive is when the tool incorrectly flags a compliant configuration. This is a real misconfiguration being accepted as a risk, which requires proper exception documentation.

---

### Question 5

A Checkov scan of a Terraform file produces the following finding: `CKV_AWS_20: Ensure the S3 bucket does not have public ACLs`. The Terraform resource has `acl = "public-read"` on an `aws_s3_bucket_acl` resource. What is the correct remediation and why?

- A) Add a bucket policy that grants only specific IAM roles read access, which overrides the public-read ACL
- B) Change `acl = "public-read"` to `acl = "private"` and add an `aws_s3_bucket_public_access_block` resource with all four block settings set to true
- C) Enable S3 server-side encryption on the bucket, which automatically removes the public-read ACL
- D) Move the bucket to a VPC endpoint, which restricts access to the VPC and disables the public-read ACL

- **Correct Answer:** B) Change the ACL to private and add a public access block resource. The ACL change removes the immediate public grant; the public access block prevents any future public ACL or policy from being applied, creating defense in depth.
- **Distractor Analysis:**
  - *Why B is correct:* Setting `acl = "private"` removes the explicit AllUsers read grant. Adding `aws_s3_bucket_public_access_block` with all four booleans set to true provides a persistent guard that blocks future attempts to re-enable public access through ACLs or bucket policies. This is the recommended defense-in-depth pattern.
  - *Why A is incorrect:* A bucket policy restricting access to specific IAM roles does not remove the public-read ACL. ACLs and bucket policies are evaluated separately; a public-read ACL grants access to anonymous users regardless of what the bucket policy says.
  - *Why C is incorrect:* S3 server-side encryption controls data confidentiality at rest — it does not modify access control settings. Enabling encryption does not remove or change ACLs.
  - *Why D is incorrect:* VPC endpoints control network-level access from within a VPC but do not disable public S3 ACLs. An S3 bucket with a public-read ACL is still accessible from the internet regardless of VPC endpoint configuration.

---

### Question 6

An organization enables AWS Config auto-remediation for the `s3-bucket-server-side-encryption-enabled` rule with `Automatic: true` and `MaximumAutomaticAttempts: 3`. During testing, the SSM Automation document for this remediation incorrectly enables encryption with a key that has no permissions for the application's IAM role, breaking the application. What process failure led to this outcome?

- A) The Config rule was not mapped to the correct CIS Benchmark control before enabling auto-remediation
- B) The SSM Automation document was not tested in a non-production environment before enabling automatic remediation in production
- C) The auto-remediation was configured with too many maximum attempts, allowing the SSM document to run three times
- D) The Prowler scan that identified the original finding did not include sufficient context for the SSM document to select the correct KMS key

- **Correct Answer:** B) The SSM Automation document was not tested in a non-production environment before being enabled in production with automatic execution.
- **Distractor Analysis:**
  - *Why B is correct:* Auto-remediation that modifies production resources must be validated in sandbox or staging environments before enabling the Automatic flag. The SSM document should be run manually, reviewed for side effects, and confirmed to use appropriate KMS keys before automation is enabled. This is a standard CSPM auto-remediation best practice.
  - *Why A is incorrect:* CIS Benchmark mapping is for compliance reporting, not for determining the correctness of an SSM Automation document. The misconfiguration of the KMS key is unrelated to which benchmark control is mapped.
  - *Why C is incorrect:* Three maximum attempts is a conservative limit. The problem is not how many times the document ran — the problem is that the document itself had an incorrect configuration (wrong KMS key). Reducing attempts would not have prevented the breakage on the first run.
  - *Why D is incorrect:* Prowler findings identify misconfigurations but do not provide input to SSM Automation documents. SSM documents have their own parameter configuration. The KMS key selection is a configuration issue in the SSM document, not a gap in the Prowler finding.

---

### Question 7

What is the primary difference between Prisma Cloud's RQL (Resource Query Language) approach to CSPM and Wiz's graph-based approach?

- A) RQL evaluates each cloud resource configuration individually against policy rules, while Wiz analyzes relationships and combinations of configurations across the entire cloud environment to identify attack paths
- B) RQL is an open-source tool while Wiz is a commercial platform with enterprise licensing requirements
- C) RQL scans IaC files in CI/CD pipelines while Wiz scans only live cloud environments after deployment
- D) RQL requires an agent installed on each cloud resource while Wiz is agentless

- **Correct Answer:** A) RQL evaluates individual resource configurations against defined rules. Wiz builds a security graph linking resources, identities, and network paths, and identifies dangerous combinations (toxic combos) that create attack paths even when each individual misconfiguration is low severity.
- **Distractor Analysis:**
  - *Why A is correct:* This is the fundamental architectural difference between rule-based CSPM (Prisma Cloud RQL) and graph-based CSPM (Wiz). RQL policies ask "is this resource configured correctly?" Wiz asks "given how all resources are connected, what attack paths exist?" The graph approach catches risks that individual resource evaluation misses.
  - *Why B is incorrect:* Both Prisma Cloud and Wiz are commercial platforms. Neither is open-source in their primary form.
  - *Why C is incorrect:* Both Prisma Cloud and Wiz primarily scan live cloud environments for posture management. Prisma Cloud also has IaC scanning capabilities (formerly Bridgecrew), but the distinction between them is not about IaC vs. live scanning.
  - *Why D is incorrect:* Both Prisma Cloud and Wiz support agentless scanning for cloud resource posture assessment. Agentlessness is not the primary differentiator between them.

---

### Question 8

A Prowler scan generates 3,000 findings in a single AWS account. The security team is overwhelmed. Which approach best addresses finding volume management while maintaining security governance?

- A) Disable Prowler scanning and rely solely on GuardDuty for threat detection
- B) Implement severity-based SLAs, establish a formal exceptions register for accepted risks, and focus remediation resources on Critical and High findings first
- C) Run Prowler only once per quarter instead of daily to reduce the volume of new findings
- D) Configure Prowler to suppress all Medium and Low findings permanently so only Critical and High findings are reported

- **Correct Answer:** B) Severity-based SLAs, formal exception management, and prioritized remediation. This is the standard CSPM governance model for managing large finding volumes.
- **Distractor Analysis:**
  - *Why B is correct:* High finding volumes are a normal outcome of CSPM at scale. The correct response is triage by severity, establish SLAs (Critical: 24 hours, High: 7 days, Medium: 30 days), formally document accepted risks with expiry dates, and focus engineering capacity on the highest-severity findings. This maintains governance without overwhelming the team.
  - *Why A is incorrect:* GuardDuty detects active threats and suspicious behavior — it does not detect misconfigurations. Disabling CSPM leaves the configuration attack surface unaddressed. CSPM and GuardDuty are complementary, not substitutes.
  - *Why C is incorrect:* Running CSPM infrequently means new misconfigurations introduced between scans go undetected for extended periods. Daily scans are appropriate for catching drift quickly. The volume problem is managed through triage, not scan frequency reduction.
  - *Why D is incorrect:* Permanently suppressing an entire severity tier removes visibility into those findings. Medium and Low findings accumulate and may combine with High findings to create exploitable attack chains. Suppression without documentation also fails audit requirements.

---

### Question 9

An organization wants to prevent any IAM role in their AWS organization from being created with `"Action": "*"` wildcard permissions. Which CSPM control should they implement?

- A) An AWS Config Rule that evaluates IAM roles after creation and generates findings for roles with wildcard policies
- B) An AWS SCP that denies `iam:CreateRole` and `iam:PutRolePolicy` when the policy document contains `"Action": "*"`
- C) A Checkov scan in the CI/CD pipeline that flags Terraform code containing wildcard IAM policies
- D) A Prowler compliance check that reports wildcard IAM policies as HIGH severity findings in the nightly scan

- **Correct Answer:** B) An SCP with conditions that deny role and policy creation when the policy contains wildcard actions. This is a preventive control that blocks the creation before it occurs.
- **Distractor Analysis:**
  - *Why B is correct:* SCPs are preventive controls applied at the organization level. They can use conditions and resource-based constraints to prevent IAM policies with specific dangerous patterns from being created. This stops the misconfiguration at the source, not after the fact.
  - *Why A is incorrect:* An AWS Config Rule is a detective control — it evaluates resources after they exist and generates findings. This means the wildcard IAM role will be created and may be used before the finding is remediated.
  - *Why C is incorrect:* Checkov in the CI/CD pipeline is a preventive control for IaC-provisioned resources. However, if IAM roles are created through the console or CLI outside the pipeline, Checkov will not catch them. SCPs provide broader coverage across all provisioning methods.
  - *Why D is incorrect:* Prowler is a detective control that reports findings after misconfigurations exist. Like Config Rules, Prowler findings still mean the wildcard role was created and potentially used. Preventive controls are preferred when the risk is high.

---

### Question 10

Which combination of CSPM controls implements the most complete defense-in-depth posture for preventing and detecting cloud misconfigurations?

- A) Run Checkov in the CI/CD pipeline only, relying on pull request reviews to catch any Checkov findings before deployment
- B) Use Prowler nightly scans only, reviewing the HTML report manually each morning and assigning remediation tickets
- C) Implement Checkov in CI/CD pipelines (preventive, IaC layer), AWS Config Rules with auto-remediation (detective and reactive, runtime layer), and Prowler nightly scans (detective, compliance reporting layer)
- D) Deploy AWS Security Hub with GuardDuty integration only, relying on GuardDuty to detect configuration changes that introduce risk

- **Correct Answer:** C) Layered controls combining IaC scanning (preventive), Config Rules with auto-remediation (detective and reactive), and periodic compliance assessments (reporting). This implements all three CSPM control types across both the pipeline and runtime layers.
- **Distractor Analysis:**
  - *Why C is correct:* Defense-in-depth requires multiple complementary control layers. Checkov in CI/CD prevents misconfigurations in IaC-provisioned resources. Config Rules detect drift in live resources. Auto-remediation closes the loop on common misconfigurations without human toil. Prowler generates compliance evidence for audits. No single tool covers all scenarios.
  - *Why A is incorrect:* Checkov only scans IaC code. Resources provisioned outside the pipeline (via console, CLI, or other tools) are not covered. Pull request reviews are human and can miss complex misconfigurations that automated tools would catch.
  - *Why B is incorrect:* Nightly scans plus manual review introduces a 24-hour detection window and relies on human capacity to process reports. Manual ticket assignment does not scale and has no enforcement mechanism for SLA compliance.
  - *Why D is incorrect:* AWS Security Hub aggregates findings but focuses on threats (GuardDuty) and vulnerability assessments, not primarily on configuration misconfigurations. GuardDuty detects active threats, not misconfigurations. Security Hub alone does not provide IaC scanning or auto-remediation capabilities.

---

**Question 11** (5 points)

An AWS Config Rule evaluates all S3 buckets and marks any bucket without versioning enabled as NON_COMPLIANT. A developer creates a temporary scratch bucket without versioning for a one-time data transfer. The Config Rule immediately flags it. What is the most appropriate CSPM response?

- A) Disable the Config Rule for the account to prevent false positives on temporary buckets
- B) Document a time-boxed exception in the exceptions register with a justification and a named risk owner, and set the exception to expire when the scratch bucket is deleted
- C) Lower the Config Rule's severity to Informational so it does not count against compliance metrics
- D) Ignore the finding since scratch buckets are not subject to the same controls as production resources

- **Correct Answer:** B) A time-boxed exception with documented justification and an expiry aligned to the bucket's expected lifetime.
- **Distractor Analysis:**
  - *Why B is correct:* Exceptions are a legitimate part of CSPM governance for justified deviations. The key requirement is documentation — why the exception is accepted, who owns it, when it expires — so auditors can review it.
  - *Why A is incorrect:* Disabling the rule removes detection for all S3 buckets in the account, not just the scratch bucket. This eliminates governance coverage for potentially important resources.
  - *Why C is incorrect:* Changing severity in tool configuration to avoid compliance metrics is a data integrity violation that misrepresents the actual security posture to auditors.
  - *Why D is incorrect:* Ignoring findings without documentation creates an audit gap — there is no evidence the finding was considered, evaluated, and accepted.

---

**Question 12** (5 points)

Prisma Cloud generates a finding: "AWS EC2 instance with public IP in a subnet without Network ACL restrictions — HIGH." The EC2 instance is a legitimate internet-facing web server. Which RQL query would help the security team verify whether this is a true positive?

- A) `config from cloud.resource where api.name = 'aws-ec2-describe-instances' AND json.rule = publicIpAddress exists AND json.rule = subnetId exists`
- B) A query that also joins the Security Group and Network ACL rules to verify whether inbound access is actually unrestricted
- C) A query that checks whether GuardDuty has active findings for the instance
- D) A query that checks the instance's CloudTrail API call history for the last 30 days

- **Correct Answer:** B) A query combining the EC2 instance, Security Group rules, and Network ACL rules to determine whether the unrestricted access is genuine or mitigated by network controls.
- **Distractor Analysis:**
  - *Why B is correct:* A public IP alone does not mean the instance is exposed — Security Groups and Network ACLs may restrict inbound access to specific ports or IPs. True-positive validation requires checking all network control layers.
  - *Why A is incorrect:* This query confirms the instance has a public IP but does not assess whether the traffic is actually unrestricted. It would produce the same result for a tightly-controlled web server and an exposed instance.
  - *Why C is incorrect:* GuardDuty findings indicate active threats, not configuration validation. The absence of GuardDuty findings does not mean the configuration is correct.
  - *Why D is incorrect:* CloudTrail history shows API calls made to AWS — it does not describe the network exposure of the instance.

---

**Question 13** (5 points)

An organization deploys AWS GuardDuty and AWS Security Hub together. What is the division of responsibility between these two services?

- A) GuardDuty scans IaC files before deployment; Security Hub monitors live resources after deployment
- B) GuardDuty performs behavioral threat detection (anomalous API calls, network activity, credential misuse); Security Hub aggregates findings from GuardDuty, Config, Inspector, and third-party tools into a unified compliance and findings dashboard
- C) GuardDuty manages IAM permissions; Security Hub manages network security group rules
- D) GuardDuty is for detective controls; Security Hub replaces the need for IaC scanning in CI/CD pipelines

- **Correct Answer:** B) GuardDuty detects active threats via behavioral analysis; Security Hub aggregates and normalizes findings from multiple AWS security services into a single pane of glass.
- **Distractor Analysis:**
  - *Why B is correct:* These services are complementary. GuardDuty uses machine learning to detect suspicious behavior in CloudTrail, VPC Flow Logs, and DNS logs. Security Hub consumes findings from GuardDuty, AWS Config, Inspector, Macie, and third-party integrations, normalizing them into ASFF (Amazon Security Finding Format) for unified triage.
  - *Why A is incorrect:* Neither GuardDuty nor Security Hub scans IaC files — that is the role of checkov or tfsec in a CI/CD pipeline.
  - *Why C is incorrect:* Neither service manages IAM permissions or security group rules — those are configuration resources managed by IAM and EC2 respectively.
  - *Why D is incorrect:* Security Hub does not replace IaC scanning — it aggregates runtime findings. IaC scanning catches misconfigurations before deployment; Security Hub addresses runtime posture.

---

**Question 14** (5 points)

A Prowler finding reports that CloudTrail multi-region logging is disabled. The remediation command is: `aws cloudtrail update-trail --name mytrail --is-multi-region-trail`. Before running this in production, what should the DevSecOps engineer verify?

- A) That the AWS account has a CloudTrail lake configured to receive the new multi-region events
- B) That enabling multi-region logging will not exceed S3 storage limits and that the S3 bucket policy allows CloudTrail to write from all regions
- C) That all EC2 instances in all regions are running the CloudWatch agent before enabling multi-region logging
- D) That the AWS account's Service Control Policy allows CloudTrail to be enabled in all regions

- **Correct Answer:** B) Verify S3 storage and bucket policy before enabling multi-region logging to avoid write failures or unexpected costs.
- **Distractor Analysis:**
  - *Why B is correct:* Enabling multi-region CloudTrail increases log volume proportionally to the number of active regions. The S3 bucket must have a bucket policy that permits CloudTrail write access (`cloudtrail.amazonaws.com`) from all regions, and storage costs should be estimated.
  - *Why A is incorrect:* CloudTrail Lake is an optional managed event data store — it is separate from standard CloudTrail S3 delivery. Multi-region logging writes to S3, not necessarily to CloudTrail Lake.
  - *Why C is incorrect:* The CloudWatch agent is for metric and log collection from EC2 instances — it is unrelated to CloudTrail's ability to log API calls across regions.
  - *Why D is incorrect:* If an SCP denied CloudTrail operations, Prowler would have flagged that separately. The current finding is about multi-region being disabled, not about SCPs preventing enablement.

---

**Question 15** (5 points)

A CSPM tool identifies that an S3 bucket hosting a public static website has `BlockPublicPolicy: false`. The security team argues this is intentional for the website. Which explanation correctly describes why `BlockPublicPolicy: false` may still be a finding even for an intentional public website?

- A) S3 static websites should use CloudFront, not direct bucket access, so the bucket itself should still have public access blocked
- B) `BlockPublicPolicy: false` allows any future bucket policy change to make the bucket public, including accidental or malicious changes — the public website should be served through a controlled mechanism such as a specific bucket policy, not by disabling the block
- C) Static website hosting does not work unless `BlockPublicPolicy` is set to true
- D) `BlockPublicPolicy: false` is only a finding for buckets in the us-east-1 region

- **Correct Answer:** A) The recommended pattern is to serve the website through CloudFront with the bucket remaining private, so the public access block can remain enabled without breaking the website.
- **Distractor Analysis:**
  - *Why A is correct:* Using CloudFront as a CDN in front of an S3 bucket allows the bucket to remain private (with public access block enabled) while the website is still publicly accessible through CloudFront. This eliminates direct public S3 access and allows applying WAF rules, access logging, and HTTPS enforcement at the CloudFront layer.
  - *Why B is also partially correct:* But the question asks for the "best explanation" — the architectural recommendation (CloudFront) is more actionable than the general risk argument.
  - *Why C is incorrect:* S3 static website hosting does work with `BlockPublicPolicy: false` combined with a public bucket policy — it is not required to set it to true for the website to function.
  - *Why D is incorrect:* S3 public access block settings apply globally, not by region.

---

**Question 16** (5 points)

Which AWS service acts as a preventive guardrail at the AWS Organizations level, and what is a key limitation compared to IAM policies on individual roles?

- A) AWS Organizations SCPs; a limitation is that SCPs cannot use IAM condition keys such as `aws:RequestedRegion` or `aws:SourceIp`
- B) AWS Organizations SCPs; a key limitation is that SCPs do not apply to the management (master) account of the organization
- C) AWS Config Rules; a limitation is that they only evaluate resources in the account where the rule is deployed, not across the organization
- D) AWS Control Tower guardrails; a limitation is that they only apply to accounts created after Control Tower was enabled

- **Correct Answer:** B) SCPs do not apply to the management account — the management account retains all IAM permissions regardless of SCPs, making it a critical security boundary that must be managed separately.
- **Distractor Analysis:**
  - *Why B is correct:* This is a significant and exam-relevant limitation of SCPs. AWS explicitly excludes the management account from SCP enforcement. Any SCP that denies a dangerous action (like disabling CloudTrail) does not protect the management account itself, which is why the management account should have no workloads and be strictly access-controlled.
  - *Why A is incorrect:* SCPs do support condition keys including `aws:RequestedRegion`, `aws:SourceIp`, and others. Condition-based SCPs are a common pattern for restricting to approved regions.
  - *Why C is incorrect:* AWS Config Rules can be deployed as organizational rules that apply across all member accounts. This is a feature, not a limitation.
  - *Why D is incorrect:* Control Tower guardrails apply to all accounts enrolled in Control Tower, including accounts that were enrolled after setup. The enrollment process applies guardrails at enrollment time.

---

**Question 17** (5 points)

What does the CIS AWS Foundations Benchmark level 1 vs. level 2 distinction mean for an organization adopting Prowler for compliance assessment?

- A) Level 1 checks are automated; Level 2 checks require manual audit procedures
- B) Level 1 checks represent basic security hygiene applicable to all organizations; Level 2 checks are more stringent requirements suitable for high-security environments that can tolerate reduced usability
- C) Level 1 covers AWS accounts; Level 2 covers multi-cloud environments including Azure and GCP
- D) Level 1 findings have a 30-day SLA; Level 2 findings have a 7-day SLA by default

- **Correct Answer:** B) Level 1 is baseline security applicable to all organizations; Level 2 is more stringent and appropriate for highly sensitive environments.
- **Distractor Analysis:**
  - *Why B is correct:* CIS Benchmarks define two implementation groups. Level 1 items are considered essential security configurations that all organizations should implement — they have minimal impact on usability. Level 2 items add more restrictive controls appropriate for environments that require higher security assurance, potentially with higher operational overhead.
  - *Why A is incorrect:* Both Level 1 and Level 2 CIS checks can be automated with Prowler — the distinction is about security stringency, not automation feasibility.
  - *Why C is incorrect:* CIS AWS Foundations Benchmark is AWS-specific at all levels — it does not extend to Azure or GCP in Level 2.
  - *Why D is incorrect:* The CIS Benchmark defines control importance, not SLAs — SLAs are set by the organization's security policy, not by the benchmark itself.

---

**Question 18** (5 points)

An organization uses Terraform to provision AWS resources and Checkov in CI/CD to scan IaC. A developer manually creates an S3 bucket with public access through the AWS console. Checkov does not flag this bucket. What control would detect this configuration drift?

- A) Adding more Checkov rules that scan the AWS console directly
- B) An AWS Config Rule that evaluates all S3 buckets in the account (regardless of how they were created) and reports NON_COMPLIANT for any bucket with public access enabled
- C) A pre-commit hook that intercepts AWS CLI commands before they execute
- D) A Terraform import of the manually-created bucket so Checkov can scan it

- **Correct Answer:** B) An AWS Config Rule that evaluates all S3 buckets regardless of provisioning method.
- **Distractor Analysis:**
  - *Why B is correct:* AWS Config evaluates all resources in the account, not just those created through Terraform. This covers console-created, CLI-created, and SDK-created resources — providing comprehensive detection regardless of how the misconfiguration was introduced.
  - *Why A is incorrect:* Checkov is a static analysis tool for IaC files — it cannot scan live AWS resources created through the console.
  - *Why C is incorrect:* Pre-commit hooks run on the developer's local machine — they intercept Git operations, not AWS API calls. AWS console actions bypass both Git and pre-commit hooks entirely.
  - *Why D is incorrect:* Running `terraform import` for every console-created resource is operationally impractical and still would not trigger Checkov in the CI pipeline unless a PR was opened with the imported resource definition.

---

**Question 19** (5 points)

A CSPM finding reports "EC2 instance has IMDSv1 enabled (instance metadata service version 1)." Why is IMDSv2 preferred from a security perspective?

- A) IMDSv2 encrypts instance metadata at rest, preventing unauthorized access to instance configuration
- B) IMDSv2 requires a session-oriented PUT request to get a token before metadata can be accessed, preventing Server-Side Request Forgery (SSRF) attacks from reading instance metadata without the PUT step
- C) IMDSv2 limits metadata access to IAM roles with the `ec2:DescribeInstances` permission
- D) IMDSv2 disables the metadata endpoint entirely for instances that do not require it

- **Correct Answer:** B) IMDSv2 requires a session token obtained via PUT, which SSRF vulnerabilities cannot easily perform — preventing the attack pattern used in the Capital One breach.
- **Distractor Analysis:**
  - *Why B is correct:* The SSRF attack pattern that exposed the Capital One breach exploited IMDSv1's GET-based metadata endpoint — any service-side request could reach it. IMDSv2 requires a PUT request with a TTL header to obtain a session token before metadata can be read. SSRF vulnerabilities typically only allow GET requests, making IMDSv2 resistant to this attack.
  - *Why A is incorrect:* IMDSv2 does not encrypt metadata at rest — the data is the same. The security improvement is in the authentication requirement for access.
  - *Why C is incorrect:* Instance metadata is accessible from within the instance without IAM authentication — it is a network endpoint on `169.254.169.254`. IAM permissions control AWS API calls, not direct metadata endpoint access.
  - *Why D is incorrect:* IMDSv2 does not disable the endpoint — it adds a session token requirement. Disabling the endpoint is a separate option (`HttpEndpoint: disabled`).

---

**Question 20** (5 points)

A Wiz security graph identifies the following "toxic combination": EC2 instance with an IAM role that has `s3:GetObject *` on all buckets + the instance is in a public subnet with port 80 open to 0.0.0.0/0 + the instance runs a web application with an unpatched CVE-2023-XXXX (SSRF). What makes this a "toxic combination" rather than three separate findings?

- A) Each finding independently triggers a Critical severity alert — the combination increases the alert count
- B) Individually, each finding might be Medium or Low severity, but the combination creates a complete attack chain: an attacker exploits SSRF to reach the metadata endpoint and steal IAM credentials with broad S3 access
- C) The SSRF CVE makes the other two findings irrelevant — patching the CVE resolves all three
- D) Wiz's graph combines findings only when they are in the same AWS region and availability zone

- **Correct Answer:** B) The combination creates a complete, exploitable attack chain that no individual finding fully represents.
- **Distractor Analysis:**
  - *Why B is correct:* This is the core value of graph-based CSPM. The public exposure alone might be acceptable for a web server. The broad S3 permissions alone might be Low severity in isolation. The SSRF CVE might be Medium. But combined: an external attacker reaches the public web app, exploits SSRF to call `169.254.169.254/latest/meta-data/iam/security-credentials/`, obtains the EC2 role's temporary credentials, and uses them to exfiltrate all S3 data. Each finding enables the next step.
  - *Why A is incorrect:* "Toxic combination" is not about alert count multiplication — it is about attack path completion that the individual findings do not individually represent.
  - *Why C is incorrect:* Patching the SSRF removes one link in the attack chain but the other vulnerabilities remain. Defense in depth requires fixing all three.
  - *Why D is incorrect:* Wiz's graph operates across regions, accounts, and cloud providers — it is not constrained to same-region or same-AZ resources.

---

Quiz — Module 10 | CIS-4350 | Texas Wesleyan University | Professor Nash
