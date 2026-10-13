# Video Script: Module 10 - Infrastructure as Code Security: Terraform Security Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 10 — Infrastructure as Code Security: Terraform Security Scanning"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. We have covered application-layer security controls — SAST, DAST, SCA, and secrets management. Now we're shifting to the infrastructure layer: Infrastructure as Code, or IaC. If your application is deployed on cloud infrastructure defined in Terraform, CloudFormation, or Ansible, those infrastructure definitions are code — and code can have security vulnerabilities.

An S3 bucket with public access enabled, a security group open to 0.0.0.0/0 on port 22, an RDS instance with encryption disabled: these are not application code vulnerabilities, but they create the same kind of exploitable exposure. By the end of this video you will understand what IaC security scanning is, why it belongs in the CI/CD pipeline, how to use Checkov, tfsec, and Terrascan against Terraform configurations, and how to integrate IaC scanning as a pipeline gate."

---

### [01:30 - 06:00] What Is IaC Security and Why Does It Matter

**Visual:** Side-by-side: Terraform resource block and the AWS console showing the resulting misconfigured resource

**Audio:**

"Infrastructure as Code means your cloud resources — virtual machines, databases, object storage, network configuration, IAM roles — are defined in configuration files checked into version control. This is a security improvement over manual console configuration because IaC is auditable, repeatable, and reviewable. But it also means that security misconfigurations are codified and reproduced consistently across every deployment.

Consider this Terraform resource:

**[SHOW CODE]**

```hcl
resource "aws_s3_bucket" "data" {
  bucket = "company-customer-data"
}

resource "aws_s3_bucket_acl" "data" {
  bucket = aws_s3_bucket.data.id
  acl    = "public-read"
}
```

This configuration creates an S3 bucket with public read access. Every `terraform apply` in every environment will create this publicly accessible bucket. Without IaC security scanning, this configuration passes through code review, gets applied to staging, gets applied to production, and exposes customer data.

IaC security scanners analyze your Terraform configuration files statically — before `terraform plan` or `terraform apply` runs — and flag resources that violate security best practices. The three primary tools are Checkov, tfsec, and Terrascan. All three support Terraform, with varying support for CloudFormation, Kubernetes manifests, Dockerfiles, and Helm charts.

The pipeline placement for IaC scanning is the same principle as SAST: scan early, gate early. IaC scanning runs in the PR pipeline check on the Terraform configuration files, failing the PR if high-severity misconfigurations are detected, before any infrastructure is provisioned."

---

### [06:00 - 12:00] Checkov

**Visual:** Checkov scan output showing FAILED and PASSED checks

**Audio:**

"Checkov is an open-source IaC security scanner from Bridgecrew (acquired by Palo Alto Networks). It has the broadest framework support — Terraform, CloudFormation, Kubernetes manifests, Dockerfiles, ARM templates, Bicep, Helm charts, and more. Checkov maps its checks to CIS benchmarks, NIST standards, and SOC2 controls.

**[SHOW CODE]**

Running Checkov against a Terraform directory:

```bash
# Install Checkov
pip install checkov

# Scan a Terraform directory
checkov -d ./terraform

# Scan a specific file
checkov -f ./terraform/main.tf

# Output as SARIF for GitHub Code Scanning
checkov -d ./terraform --output sarif --output-file checkov-results.sarif

# Fail only on HIGH and CRITICAL findings
checkov -d ./terraform --check HIGH,CRITICAL
```

Checkov's output shows each check with its check ID, resource, result (PASSED or FAILED), file path, and line number. FAILED checks include a remediation guide with the corrected HCL.

Here is a GitHub Actions job for Checkov:

```yaml
iac-scan:
  name: IaC Security Scan
  runs-on: ubuntu-latest
  steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Run Checkov IaC scan
      uses: bridgecrewio/checkov-action@master
      with:
        directory: terraform/
        framework: terraform
        output_format: sarif
        output_file_path: checkov-results.sarif
        soft_fail: false

    - name: Upload Checkov results to GitHub Code Scanning
      uses: github/codeql-action/upload-sarif@v3
      if: always()
      with:
        sarif_file: checkov-results.sarif
```

`soft_fail: false` means the job exits non-zero when any FAILED check is found. Setting it to `true` would allow the pipeline to continue despite findings — useful during initial adoption when you want visibility without blocking.

Common Checkov checks you should know: `CKV_AWS_18` (S3 access logging), `CKV_AWS_19` (S3 encryption), `CKV_AWS_20` (S3 bucket not public), `CKV_AWS_57` (S3 bucket policy not public), `CKV_AWS_8` (EC2 instance metadata service IMDSv2), `CKV_AWS_79` (IMDSv2 enforcement)."

---

### [12:00 - 17:00] tfsec and Terrascan

**Visual:** tfsec output, then Terrascan output side-by-side

**Audio:**

"**tfsec** is a Terraform-focused static analysis tool from Aqua Security. While Checkov is broader in framework support, tfsec is optimized specifically for Terraform and HCL and provides detailed context about each finding.

**[SHOW CODE]**

```bash
# Install tfsec
brew install tfsec

# Scan a Terraform directory
tfsec ./terraform

# Fail on HIGH severity and above
tfsec ./terraform --minimum-severity HIGH

# Output as SARIF
tfsec ./terraform --format sarif --out tfsec-results.sarif
```

tfsec findings include the severity, a description, a link to documentation, and the specific HCL block causing the issue. It also shows the `terraform plan` impact — what would be created or changed.

**Terrascan** is an open-source IaC scanner from Tenable. It is notable for its policy-as-code model: policies are written in Rego (the same language used by OPA and Open Policy Agent). This allows organizations to write custom security policies in the same language they use for admission control in Kubernetes.

**[SHOW CODE]**

```bash
# Install Terrascan
brew install terrascan

# Scan Terraform files
terrascan scan -i terraform -d ./terraform

# Scan with specific ruleset
terrascan scan -i terraform -d ./terraform --policy-type aws

# Output as SARIF
terrascan scan -i terraform -d ./terraform --output sarif
```

For the exam, know that all three tools — Checkov, tfsec, and Terrascan — scan Terraform statically, support SARIF output for GitHub Code Scanning integration, and can be configured to fail the pipeline on HIGH and CRITICAL findings. Checkov has the broadest framework support. Terrascan uses Rego for custom policies."

---

### [17:00 - 21:30] Common IaC Misconfigurations and Remediation

**Visual:** Vulnerable Terraform, Checkov FAILED check, then remediated Terraform

**Audio:**

"Let's walk through three canonical IaC misconfigurations and their remediations.

**[SHOW CODE]**

#### Misconfiguration 1: S3 Bucket with Public Access

```hcl
# Vulnerable
resource "aws_s3_bucket_public_access_block" "example" {
  bucket                  = aws_s3_bucket.example.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Remediated
resource "aws_s3_bucket_public_access_block" "example" {
  bucket                  = aws_s3_bucket.example.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

#### Misconfiguration 2: Security Group Open to the World

```hcl
# Vulnerable
resource "aws_security_group_rule" "ssh" {
  type        = "ingress"
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

# Remediated — restrict to known CIDRs
resource "aws_security_group_rule" "ssh" {
  type        = "ingress"
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"
  cidr_blocks = ["10.0.0.0/8"]
}
```

#### Misconfiguration 3: RDS with Encryption Disabled

```hcl
# Vulnerable
resource "aws_db_instance" "app" {
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  storage_encrypted = false
}

# Remediated
resource "aws_db_instance" "app" {
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  storage_encrypted = true
  kms_key_id        = aws_kms_key.rds.arn
}
```

Each of these misconfigurations is caught by Checkov and tfsec before `terraform apply` runs. The key DevSecOps principle here is shift-left: finding a misconfiguration in a PR is far cheaper than finding it after it has been running in production for six months."

---

### [21:30 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know that IaC security scanning tools — Checkov, tfsec, and Terrascan — analyze Terraform configuration statically before infrastructure is provisioned. Know that Checkov has the broadest framework support (Terraform, CloudFormation, Kubernetes, Dockerfiles), tfsec is Terraform-focused, and Terrascan uses Rego for custom policies. Know the three canonical misconfigurations: S3 public access, security groups open to 0.0.0.0/0, and unencrypted databases. Know that all three tools support SARIF output for GitHub Code Scanning integration and can fail the pipeline on HIGH or CRITICAL findings. Know that IaC scanning runs at the PR stage — before any infrastructure is provisioned — following the shift-left principle. See you in Module 11."
