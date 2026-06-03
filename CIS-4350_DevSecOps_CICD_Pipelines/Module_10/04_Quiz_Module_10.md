# Quiz: Module 10 — Cloud Security Posture Management (CSPM)

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

**Instructions:** Select the single best answer for each question. Review the distractor analysis after completing the quiz.

---

**Question 1**

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

**Question 2**

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

**Question 3**

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

**Question 4**

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

**Question 5**

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

**Question 6**

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

**Question 7**

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

**Question 8**

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

**Question 9**

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

**Question 10**

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
