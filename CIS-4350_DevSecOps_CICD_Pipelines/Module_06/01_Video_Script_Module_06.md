# Video Script: Module 06 — Infrastructure as Code Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–1:30)

[SLIDE: Module 06 title card]

Welcome to Module 06. We've secured our code, our containers, and our Kubernetes clusters. Now let's address the infrastructure that runs all of it. Infrastructure as Code — IaC — is the practice of managing cloud resources through version-controlled configuration files. Terraform, AWS CloudFormation, Azure Bicep, Pulumi — these tools provision servers, databases, networks, and security groups programmatically.

The security problem: IaC files frequently contain misconfigurations — open S3 buckets, public security group rules, disabled encryption — that would be caught in an application code review but are often overlooked because infrastructure engineers may not have security training for cloud-specific risks.

In this module we'll cover Terraform security scanning with tfsec and checkov, CloudFormation security, policy as code with OPA and HashiCorp Sentinel, drift detection, and the immutable infrastructure principle.

---

### SEGMENT 2 — IaC and the Security Problem (1:30–4:30)

[SLIDE: Timeline — IaC misconfiguration to breach]

Infrastructure misconfigurations are one of the most common causes of cloud data breaches. The Verizon Data Breach Investigations Report and the IBM Cost of a Data Breach Report both consistently list misconfiguration as a top breach cause alongside phishing and stolen credentials.

Why are IaC misconfigurations so common?

First, cloud APIs change rapidly. A Terraform resource that was secure when written may have new security options available a year later that are not enabled in the original configuration.

Second, infrastructure developers often copy and paste from Stack Overflow or GitHub examples. Those examples prioritize "getting it working" over security. The `0.0.0.0/0` CIDR range in a security group is a classic example — it opens all traffic but is everywhere in examples.

Third, IaC files are code reviewed less rigorously than application code. Security engineers rarely participate in infrastructure pull request reviews unless there is a specific process requirement.

The solution is the same pattern we've applied throughout this course: automate the security check and embed it in the pipeline. IaC scanners analyze Terraform, CloudFormation, Kubernetes manifests, and other configuration formats for known-bad patterns before the infrastructure is ever provisioned.

---

### SEGMENT 3 — Terraform Security with tfsec (4:30–8:00)

[SLIDE: tfsec scan output on a Terraform file]

tfsec is an open-source static analysis tool for Terraform code. It scans `.tf` files for security issues using a library of built-in rules covering AWS, Azure, GCP, and general Terraform practices.

Consider this Terraform configuration for an S3 bucket:

```hcl
# Insecure S3 bucket
resource "aws_s3_bucket" "data" {
  bucket = "my-app-data"
}

resource "aws_s3_bucket_acl" "data_acl" {
  bucket = aws_s3_bucket.data.id
  acl    = "public-read"
}
```

Running tfsec against this configuration:

```bash
tfsec .
```

tfsec will report multiple findings:

```text
CRITICAL  aws-s3-no-public-buckets
          Bucket has public access enabled via ACL
          /main.tf:7

HIGH      aws-s3-enable-versioning
          Bucket does not have versioning enabled
          /main.tf:1

HIGH      aws-s3-enable-bucket-encryption
          Bucket does not have encryption enabled
          /main.tf:1

MEDIUM    aws-s3-enable-bucket-logging
          Bucket does not have logging enabled
          /main.tf:1
```

The remediated configuration:

```hcl
resource "aws_s3_bucket" "data" {
  bucket = "my-app-data"
}

resource "aws_s3_bucket_public_access_block" "data" {
  bucket                  = aws_s3_bucket.data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}
```

tfsec can be integrated into GitHub Actions:

```yaml
- name: Run tfsec
  uses: aquasecurity/tfsec-action@v1.0.0
  with:
    soft_fail: false
    working_directory: infra/
```

---

### SEGMENT 4 — Terraform Security with checkov (8:00–11:00)

[SLIDE: checkov multi-framework scan output]

checkov, developed by Bridgecrew (now part of Palo Alto Prisma Cloud), supports a wider range of IaC frameworks than tfsec and includes both built-in checks and custom Python-based checks.

```bash
# Install checkov
pip install checkov

# Scan Terraform files
checkov -d infra/ --framework terraform

# Scan CloudFormation templates
checkov -d templates/ --framework cloudformation

# Scan Kubernetes manifests
checkov -d k8s/ --framework kubernetes

# Scan Dockerfile
checkov -f Dockerfile --framework dockerfile

# Output in SARIF for GitHub Security tab
checkov -d infra/ --output sarif --output-file-path results/
```

checkov supports suppressing specific checks when there is a documented business reason:

```hcl
resource "aws_security_group_rule" "allow_http" {
  type        = "ingress"
  from_port   = 80
  to_port     = 80
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  #checkov:skip=CKV_AWS_25: Public HTTP access required for load balancer health checks
}
```

The suppression comment is tracked in code review, providing an auditable record of accepted risk.

---

### SEGMENT 5 — Policy as Code with OPA and Sentinel (11:00–14:30)

[SLIDE: OPA policy evaluation flow]

Built-in scanner rules cover known patterns, but organizations need custom policies. Policy as Code tools allow security teams to write organization-specific rules in a machine-executable language.

Open Policy Agent (OPA) with Conftest tests IaC files against Rego policies:

```rego
# policies/terraform/deny_public_s3.rego
package main

deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  resource.bucket_acl == "public-read"
  msg := sprintf("S3 bucket '%s' must not be publicly readable", [name])
}

deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  not resource.server_side_encryption_configuration
  msg := sprintf("S3 bucket '%s' must have encryption enabled", [name])
}
```

Running Conftest against a Terraform plan:

```bash
# Convert Terraform plan to JSON
terraform init
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary > tfplan.json

# Run Conftest against the plan
conftest test tfplan.json --policy policies/terraform/
```

HashiCorp Sentinel is an enterprise-grade policy as code framework integrated natively into Terraform Cloud and Terraform Enterprise. Sentinel policies run as part of the Terraform run workflow:

```python
# sentinel/restrict_instance_types.sentinel
import "tfplan/v2" as tfplan

allowed_types = ["t3.micro", "t3.small", "t3.medium"]

instances = filter tfplan.resource_changes as _, rc {
  rc.type is "aws_instance"
  rc.mode is "managed"
  (rc.change.actions contains "create") or (rc.change.actions contains "update")
}

violations = filter instances as _, instance {
  not (instance.change.after.instance_type in allowed_types)
}

main = rule {
  length(violations) is 0
}
```

Sentinel has three enforcement levels: advisory (log only), soft mandatory (can be overridden with approval), and hard mandatory (cannot be overridden — the plan is rejected).

---

### SEGMENT 6 — Drift Detection and Immutable Infrastructure (14:30–17:00)

[SLIDE: Drift detection timeline diagram]

Configuration drift occurs when the actual state of deployed infrastructure diverges from the IaC-defined desired state. This happens when engineers make manual changes in the cloud console ("ClickOps") or when automated systems modify resources outside of IaC workflows.

Drift is a security problem because manually applied changes bypass the security scanning and code review process. A security group opened manually in the AWS console is invisible to your IaC security gates.

Terraform Cloud detects drift through continuous workspace runs:

```hcl
# Terraform Cloud workspace configuration
resource "tfe_workspace" "production" {
  name              = "production"
  organization      = "my-org"
  auto_apply        = false
  speculative_plans = true

  vcs_repo {
    identifier = "org/infra-repo"
    branch     = "main"
  }
}
```

When drift is detected, Terraform Cloud can alert the team and optionally auto-remediate by applying the IaC-defined state.

Immutable infrastructure takes drift prevention further: instead of patching deployed instances, you replace them entirely with newly provisioned instances from updated IaC. No manual changes are ever made to running infrastructure. This eliminates drift by design.

The immutable infrastructure workflow:

1. Update IaC configuration
2. CI pipeline scans and validates the change
3. New infrastructure is provisioned from the updated config
4. Traffic is shifted to the new infrastructure
5. Old infrastructure is destroyed

---

### SEGMENT 7 — IaC Security in the Pipeline (17:00–20:00)

[SLIDE: IaC security pipeline stages]

A complete IaC security pipeline integrates scanning at multiple stages:

```yaml
name: Terraform Security Pipeline

on:
  pull_request:
    paths: [infra/**]

jobs:
  terraform-validate:
    name: Terraform Validate and Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.7.0
      - run: terraform -chdir=infra/ init -backend=false
      - run: terraform -chdir=infra/ validate
      - run: terraform -chdir=infra/ fmt -check -recursive

  tfsec-scan:
    name: tfsec Security Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aquasecurity/tfsec-action@v1.0.0
        with:
          working_directory: infra/
          format: sarif
          sarif_file: tfsec-results.sarif
      - uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: tfsec-results.sarif

  checkov-scan:
    name: checkov Multi-Framework Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: infra/
          framework: terraform
          output_format: sarif
          output_file_path: checkov-results.sarif
          soft_fail: false
      - uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: checkov-results.sarif

  conftest-policy:
    name: OPA Policy Validation
    runs-on: ubuntu-latest
    needs: terraform-validate
    steps:
      - uses: actions/checkout@v4
      - name: Install conftest
        run: |
          wget https://github.com/open-policy-agent/conftest/releases/download/v0.50.0/conftest_0.50.0_linux_amd64.tar.gz
          tar xzf conftest_*.tar.gz && mv conftest /usr/local/bin/
      - name: Run Conftest policy checks
        run: conftest test infra/ --policy policies/terraform/
```

---

### SEGMENT 8 — Module Summary and Looking Ahead (20:00–22:00)

[SLIDE: Module 06 key takeaways]

Module 06 summary.

Infrastructure as Code misconfigurations are a leading cause of cloud data breaches. IaC scanning automates detection before infrastructure is provisioned.

tfsec is a fast, opinionated Terraform scanner. checkov supports multiple frameworks including Terraform, CloudFormation, Kubernetes, and Dockerfiles.

Policy as Code with OPA Conftest and HashiCorp Sentinel enables organization-specific rules beyond built-in checks. Sentinel's enforcement levels — advisory, soft mandatory, hard mandatory — provide graduated policy enforcement.

Drift detection identifies when deployed infrastructure diverges from IaC definitions. Immutable infrastructure eliminates drift by replacing rather than patching.

The IaC security pipeline validates, lints, scans, and policy-checks every change before it reaches the cloud.

In Module 07 we go deep on Application Security Testing — SAST with SonarQube and Semgrep, DAST integration with OWASP ZAP, dependency scanning with OWASP Dependency-Check, and SBOM generation. See you there.

---

*[END OF SCRIPT — Module 06]*
