# Quiz: Module 10 - Infrastructure as Code Security – Terraform Security Scanning

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Which deployment strategy maintains two identical environments, routing traffic to one while updating and testing the other?

* A) Direct Cutover — traffic is immediately switched from old to new with no parallel environment
* B) Blue-Green Deployment — two identical environments exist; traffic routes to the stable one while the new version is deployed and tested in the other
* C) Rolling Update — instances are replaced gradually, a few at a time, until all instances run the new version
* D) Shadow Deployment — live traffic is duplicated to a new environment for testing without serving user responses from the new version
* **Correct Answer:** B) Blue-green deployment maintains two complete environments; if the green (new) environment fails health checks, traffic routing is switched back to blue (stable) with no downtime.
* **Distractor Analysis:**
  * *Why B is correct:* Blue-green uses a load balancer or DNS switch to control which environment receives traffic. This enables instant rollback, zero-downtime deployments, and a clean separation between the current and new versions during validation.
  * *Why A is incorrect:* Direct cutover replaces the old environment immediately with no fallback; if the new version fails, a full rollback deployment is required, resulting in downtime.
  * *Why C is incorrect:* Rolling updates replace instances incrementally — at any point both old and new versions are running simultaneously, which can cause request inconsistencies if the versions are incompatible.
  * *Why D is incorrect:* Shadow deployment mirrors traffic to a new environment without serving responses to users; it is used for testing traffic patterns and performance, not for production deployments with rollback capability.

---

**Question 2**
Which of the following most accurately describes what tools like Checkov and tfsec scan for in a DevSecOps IaC pipeline?

* A) Syntax errors in Python application source code that prevent the Terraform CLI from executing
* B) Misconfigured cloud resources and security policy violations in Terraform and other IaC template files, such as publicly accessible S3 buckets or unencrypted database instances
* C) Runtime crashes in deployed cloud services caused by insufficient memory or CPU allocation
* D) Hard drive block size misalignments in the CI/CD runner's storage configuration that affect build performance
* **Correct Answer:** B) IaC scanners flag security misconfigurations (such as open S3 buckets or unencrypted disks) in Terraform code before the cloud resources are provisioned, applying the shift-left principle to infrastructure security.
* **Distractor Analysis:**
  * *Why B is correct:* Checkov and tfsec analyze Terraform HCL files against libraries of cloud security rules (CIS Benchmarks, NIST controls, provider best practices) and report misconfigurations that would result in insecure cloud resources if `terraform apply` ran.
  * *Why A is incorrect:* Python source code syntax errors are detected by Python linters (Flake8, Pylint) or the Python interpreter. Checkov and tfsec specifically analyze IaC template files (`.tf`, `.yaml`, `.json` CloudFormation), not application source code.
  * *Why C is incorrect:* Runtime crashes from resource exhaustion are operational monitoring concerns detected by tools like Prometheus or CloudWatch after deployment. IaC scanners operate on configuration files before provisioning.
  * *Why D is incorrect:* CI/CD runner storage configuration is an infrastructure operations concern. IaC security scanners analyze cloud resource definitions, not the runner environment.

---

**Question 3**
A Terraform configuration defines an AWS S3 bucket with the following setting: `acl = "public-read"`. A Checkov scan flags this as a CRITICAL security violation. What is the security risk, and what is the correct Terraform fix?

* A) The `public-read` ACL uses more bandwidth than necessary; fix by setting `acl = "private"` to reduce AWS data transfer costs
* B) The `public-read` ACL makes all objects in the bucket readable by any anonymous internet user, potentially exposing sensitive data; fix by setting `acl = "private"` and enabling S3 Block Public Access settings
* C) The `public-read` ACL causes the bucket to fail compliance checks for HIPAA encryption requirements; fix by enabling server-side encryption on the bucket
* D) The `public-read` ACL prevents the CI/CD pipeline from writing build artifacts to the bucket; fix by adding an IAM policy granting the pipeline write access
* **Correct Answer:** B) A `public-read` S3 ACL exposes all bucket objects to anonymous internet users — any file in the bucket can be downloaded without authentication. The fix is to set `acl = "private"` and enable `block_public_acls = true` in an `aws_s3_bucket_public_access_block` resource.
* **Distractor Analysis:**
  * *Why B is correct:* Public S3 buckets are one of the most common cloud data breach causes. Setting `private` ACL and enabling Block Public Access prevents both accidental and intentional exposure of bucket contents. Checkov check `CKV_AWS_20` flags this exact misconfiguration.
  * *Why A is incorrect:* While public access may increase bandwidth usage, the primary risk is data exposure and unauthorized access, not bandwidth cost. The ACL setting controls access permissions, not data transfer efficiency.
  * *Why C is incorrect:* HIPAA encryption requirements are addressed by enabling S3 server-side encryption (`aws_s3_bucket_server_side_encryption_configuration`), which is a separate Terraform resource configuration from the ACL setting.
  * *Why D is incorrect:* Pipeline write access is controlled by IAM policies, not by the bucket ACL. The `public-read` ACL grants anonymous read access to everyone on the internet, which is independent of the pipeline's write permissions.

---

**Question 4**
A DevSecOps team adds a Checkov scan step to their Terraform CI/CD pipeline. The scan runs after `terraform plan` but before `terraform apply`. Is this the correct pipeline placement, and why?

* A) Yes, running after `terraform plan` is correct because the plan output shows exactly which resources will be modified, giving Checkov more context for its analysis
* B) No, Checkov should run before `terraform plan` — it analyzes the static `.tf` source files and does not require a plan. Running it earlier (at the pull request stage) catches misconfigurations before any Terraform commands execute
* C) Yes, running before `terraform apply` is correct because applying the infrastructure first and then scanning the live cloud resources is the most accurate approach
* D) No, Checkov should only run in production environments after deployment so it can scan actual cloud resource configurations rather than Terraform source files
* **Correct Answer:** B) Checkov analyzes Terraform `.tf` source files statically and does not require `terraform plan` or `apply` to have run. It should run at the pull request stage — before any Terraform commands — to catch misconfigurations at the earliest possible point.
* **Distractor Analysis:**
  * *Why B is correct:* Checkov performs static analysis of `.tf` files and can run immediately after checkout, before `terraform init` or `plan`. Moving it earlier to the pull request stage aligns with shift-left principles and prevents misconfigured code from ever being planned or applied.
  * *Why A is incorrect:* While `terraform plan` output can be scanned (Checkov supports `--file tfplan.json`), Checkov's primary use case is static `.tf` file analysis that does not require plan execution. Running it after plan adds unnecessary pipeline execution time.
  * *Why C is incorrect:* Scanning live cloud resources after `apply` means the misconfigured infrastructure has already been provisioned and may have been accessible to attackers during the window between apply and scan. This is the opposite of shift-left.
  * *Why D is incorrect:* Running IaC scanning only in production after deployment defeats the entire purpose of IaC security gates. Misconfigurations discovered in production require teardown and reprovisioning, which is expensive and disruptive.

---

**Question 5**
A Checkov scan of a Terraform file reports the following finding: `CKV_AWS_8: Ensure all data stored in the Launch configuration EBS is securely encrypted`. The affected resource is an `aws_launch_configuration` with `encrypted = false` on the EBS block device. Which Terraform configuration change resolves this finding?

* A) Add `deletion_protection = true` to the `aws_launch_configuration` resource to prevent accidental deletion of the EBS volume
* B) Set `encrypted = true` in the `ebs_block_device` block of the `aws_launch_configuration` resource so EBS volumes are encrypted at rest using the default AWS KMS key
* C) Add an `aws_security_group` resource restricting network access to the EC2 instances launched by this configuration
* D) Move the `aws_launch_configuration` resource to a private subnet by adding `associate_public_ip_address = false`
* **Correct Answer:** B) Setting `encrypted = true` on the EBS block device configuration enables AES-256 encryption at rest for all volumes launched from this configuration, directly addressing the Checkov CKV_AWS_8 check.
* **Distractor Analysis:**
  * *Why B is correct:* The Terraform `ebs_block_device` block accepts an `encrypted` boolean parameter. Setting it to `true` instructs AWS to encrypt the EBS volume with the default AWS managed KMS key (or a custom KMS key ARN if specified), satisfying the check and protecting data at rest if the physical storage is compromised.
  * *Why A is incorrect:* `deletion_protection` prevents accidental API-level deletion of an RDS instance; it is not a valid attribute for `aws_launch_configuration` and does not address encryption at rest.
  * *Why C is incorrect:* Adding a security group restricts network access to the instance but does not address data-at-rest encryption of the EBS volume. These are separate security controls addressing different threat vectors.
  * *Why D is incorrect:* `associate_public_ip_address = false` prevents the instance from receiving a public IP address, which is a network exposure control. It does not address EBS encryption and does not resolve the Checkov CKV_AWS_8 finding.
