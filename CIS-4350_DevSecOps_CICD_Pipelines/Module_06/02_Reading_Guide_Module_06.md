# Reading Guide: Module 06 — Infrastructure as Code Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Explain why IaC misconfigurations are a leading cause of cloud data breaches
- Scan Terraform configurations with tfsec and checkov and interpret findings
- Write OPA Rego policies for Terraform plan validation with Conftest
- Describe HashiCorp Sentinel's three enforcement levels
- Explain drift detection and the immutable infrastructure principle
- Build a complete IaC security pipeline in GitHub Actions

---

## Section 1 — IaC Misconfiguration Risk Landscape

### 1.1 Common IaC Misconfigurations

| Misconfiguration | Cloud Service | Risk |
|---|---|---|
| Public read ACL | AWS S3 | Data exposure |
| `0.0.0.0/0` ingress on port 22 | Security Groups | SSH brute force |
| Encryption at rest disabled | RDS, S3, EBS | Data exposure if storage accessed |
| Logging disabled | S3, CloudTrail, LB | No audit trail for incident response |
| MFA delete disabled | S3 versioning | Objects deleted without second factor |
| Public IP on database | RDS | Direct internet access to DB |
| Wildcard IAM permissions (`"Action": "*"`) | IAM Policy | Privilege escalation |
| Root account API keys | IAM | Full AWS account compromise |
| Security group with all egress allowed | Security Groups | Data exfiltration |
| Secrets in Terraform variables (plaintext) | Any | Credential exposure in state file |

### 1.2 Why Automation is Required

Manual review of IaC files fails because:

- Infrastructure engineers rarely have cloud-specific security training
- Reviews happen under time pressure
- Cloud service APIs add new security parameters — legacy configs miss new best practices
- Copy-paste from public examples propagates insecure defaults
- State files (Terraform .tfstate) often contain plaintext secrets and are stored insecurely

---

## Section 2 — tfsec

### 2.1 tfsec Rule Severity and Coverage

| Severity | Example Rule | Description |
|---|---|---|
| CRITICAL | `aws-s3-no-public-buckets` | S3 bucket is publicly accessible |
| CRITICAL | `aws-iam-no-policy-wildcards` | IAM policy contains wildcard actions |
| HIGH | `aws-rds-enable-iam-authentication` | RDS not using IAM auth |
| HIGH | `aws-ec2-no-public-ip-subnet` | Subnet assigns public IPs automatically |
| MEDIUM | `aws-s3-enable-bucket-logging` | S3 access logging not enabled |
| LOW | `aws-s3-enable-versioning` | S3 versioning not enabled |

### 2.2 tfsec Configuration File

```yaml
# .tfsec/config.yml
minimum_severity: MEDIUM
exclude:
  - aws-s3-enable-versioning  # Not required for ephemeral build artifacts
custom_checks:
  - code: CUS001
    description: S3 bucket must have a name starting with 'company-'
    impact: Naming convention enforces ownership tracking
    resolution: Prefix bucket name with 'company-'
    requiredTypes:
      - resource
    requiredLabels:
      - aws_s3_bucket
    errorMessage: S3 bucket name must start with 'company-'
    matchSpec:
      name: bucket
      action: startsWith
      value: "company-"
```

### 2.3 tfsec in CI

```yaml
# GitHub Actions tfsec job
- name: Run tfsec
  uses: aquasecurity/tfsec-action@v1.0.0
  with:
    working_directory: infra/
    soft_fail: false
    format: sarif
    sarif_file: tfsec-results.sarif
    additional_args: --minimum-severity MEDIUM
```

---

## Section 3 — checkov

### 3.1 Framework Coverage

| Framework | checkov Flag | Example Resources Scanned |
|---|---|---|
| Terraform | `--framework terraform` | aws_s3_bucket, aws_security_group |
| CloudFormation | `--framework cloudformation` | AWS::S3::Bucket, AWS::EC2::SecurityGroup |
| Kubernetes | `--framework kubernetes` | Deployment, Pod, NetworkPolicy |
| Dockerfile | `--framework dockerfile` | FROM, USER, RUN, COPY |
| GitHub Actions | `--framework github_actions` | Workflow permissions, action pinning |
| Helm | `--framework helm` | Chart values, templates |
| ARM (Azure) | `--framework arm` | Azure Resource Manager templates |

### 3.2 Inline Suppressions

```hcl
resource "aws_security_group_rule" "alb_http" {
  type        = "ingress"
  from_port   = 80
  to_port     = 80
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]

  # checkov:skip=CKV_AWS_25: Public HTTP required for ALB; protected by WAF
  # Approved by: SecurityTeam, 2024-03-15, ticket INC-4521
}
```

Suppression comments are tracked in Git history, providing an audit trail of accepted risk decisions.

### 3.3 Custom Python Checks

```python
# checks/custom/s3_lifecycle_policy.py
from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class S3LifecyclePolicy(BaseResourceCheck):
    def __init__(self):
        name = "S3 bucket should have a lifecycle policy"
        id = "CKV_CUSTOM_S3_LIFECYCLE"
        supported_resources = ["aws_s3_bucket_lifecycle_configuration"]
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id,
                         categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        rules = conf.get("rule", [])
        if rules:
            return CheckResult.PASSED
        return CheckResult.FAILED

check = S3LifecyclePolicy()
```

---

## Section 4 — Policy as Code

### 4.1 OPA Conftest Workflow

```bash
# Step 1: Initialize Terraform and generate plan JSON
terraform init -backend=false
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary > tfplan.json

# Step 2: Run Conftest with policy directory
conftest test tfplan.json \
  --policy policies/terraform/ \
  --namespace main

# Step 3: Combine with namespace
conftest test tfplan.json \
  --policy policies/ \
  --all-namespaces
```

### 4.2 Rego Policy Patterns

```rego
# policies/terraform/no_public_security_groups.rego
package main

import future.keywords.in

# Collect all security group ingress rules allowing 0.0.0.0/0
public_sg_rules[name] {
  resource := input.resource_changes[_]
  resource.type == "aws_security_group_rule"
  resource.change.actions[_] in {"create", "update"}
  "0.0.0.0/0" in resource.change.after.cidr_blocks
  resource.change.after.type == "ingress"
  name := resource.address
}

deny[msg] {
  some name in public_sg_rules
  msg := sprintf(
    "Security group rule '%s' allows unrestricted ingress from 0.0.0.0/0",
    [name]
  )
}
```

### 4.3 HashiCorp Sentinel Enforcement Levels

| Level | Behavior | Use Case |
|---|---|---|
| Advisory | Policy checked; violation logged but plan proceeds | New policy rollout; awareness phase |
| Soft Mandatory | Plan blocked on violation; can be overridden with approver permission | Standard policy; security team can grant exceptions |
| Hard Mandatory | Plan blocked on violation; cannot be overridden by anyone | Absolute requirements (encryption, no public databases) |

```python
# sentinel/no_public_rds.sentinel
import "tfplan/v2" as tfplan

rds_instances = filter tfplan.resource_changes as _, rc {
  rc.type is "aws_db_instance"
  rc.mode is "managed"
  (rc.change.actions contains "create") or (rc.change.actions contains "update")
}

violations = filter rds_instances as _, rds {
  rds.change.after.publicly_accessible is true
}

main = rule {
  length(violations) is 0
}
```

---

## Section 5 — Drift Detection and Immutable Infrastructure

### 5.1 Drift Sources

| Source | Example | Detection Method |
|---|---|---|
| Manual console change | Engineer opens port 22 in AWS console | Terraform plan shows difference |
| Auto-scaling modification | ASG changes instance count | Continuous plan monitoring |
| Cloud provider maintenance | AWS changes default parameter group | Drift notification |
| Misconfigured automation | Deployment script modifies security group | Audit log analysis |

### 5.2 Terraform Drift Detection Commands

```bash
# Plan against live state — shows what Terraform would change
terraform plan -refresh-only

# If drift detected, output will show:
# ~ resource "aws_security_group_rule" "ssh" {
#     ~ cidr_blocks = [
#         - "10.0.0.0/8",
#         + "0.0.0.0/0",   # <-- manually changed
#       ]
# }

# Apply the refresh to sync state without changing resources
terraform apply -refresh-only

# Or remediate by re-applying the desired state
terraform apply
```

### 5.3 Immutable Infrastructure Principles

| Principle | Description |
|---|---|
| No SSH / no patch in place | Servers are never modified after provisioning |
| Replace, don't repair | When a fix is needed, build a new image and redeploy |
| Golden AMI / image pipeline | A base image is hardened, tested, and promoted |
| Blue/green deployment | New infrastructure runs alongside old; traffic shifts after validation |
| State in external store | Databases, caches are external to compute — compute is disposable |

---

## Section 6 — IaC Security Pipeline Design

### 6.1 Complete IaC Pipeline Stages

| Stage | Tool | Gate Condition |
|---|---|---|
| Validate | `terraform validate` | Syntax and configuration validity |
| Format | `terraform fmt -check` | Consistent formatting enforced |
| tfsec | tfsec | CRITICAL/HIGH findings block |
| checkov | checkov | Configurable severity threshold |
| Conftest | OPA/Conftest | Custom org policies pass |
| Plan | `terraform plan` | Plan generated and inspected |
| Sentinel | HashiCorp Sentinel | Enterprise policy enforcement |
| Cost estimate | Infracost | Optional: cost within budget |

### 6.2 Terraform State Security

The Terraform state file (`.tfstate`) frequently contains secrets — database passwords, private keys, API tokens — in plaintext. Never:

- Commit `.tfstate` to Git (add to `.gitignore`)
- Store state in a local file in shared environments
- Give all developers read access to the production state bucket

Always use a remote backend with encryption and access control:

```hcl
terraform {
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "arn:aws:kms:us-east-1:123456789:key/abc-123"
    dynamodb_table = "terraform-state-lock"

    # Access controlled via IAM role assumed by CI/CD only
  }
}
```

---

## Exam Tips for DSOE Certification

- tfsec is Terraform-specific; checkov supports multiple frameworks including Terraform, CloudFormation, and Kubernetes.
- OPA Conftest validates configuration files against Rego policies — the same Rego used in Kubernetes OPA Gatekeeper.
- Sentinel has three enforcement levels: advisory, soft mandatory, hard mandatory — know what each does.
- Drift occurs when manually applied changes diverge from IaC state. `terraform plan -refresh-only` detects it.
- Immutable infrastructure replaces servers rather than patching them — eliminates drift by design.
- Terraform state files may contain plaintext secrets — encrypt and restrict access to the state backend.
- checkov inline suppression comments require a documented reason — this creates an audit trail of accepted risk.
- IaC security scanning in CI should block on CRITICAL/HIGH by default, same as application security scanning.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| IaC | Infrastructure as Code — managing infrastructure via version-controlled configuration files |
| tfsec | Open-source static analysis tool for Terraform |
| checkov | Multi-framework IaC scanner by Bridgecrew/Palo Alto |
| OPA | Open Policy Agent — general-purpose policy engine using Rego |
| Conftest | CLI tool for testing configurations against OPA Rego policies |
| Sentinel | HashiCorp enterprise policy-as-code framework for Terraform |
| Drift | Divergence between deployed infrastructure state and IaC-defined desired state |
| Immutable Infrastructure | Pattern where servers are replaced rather than modified after deployment |
| Terraform State | JSON file tracking which real-world resources correspond to IaC definitions |
| Remote Backend | Cloud-hosted Terraform state storage with encryption and locking |

---

## 9. Supplemental Resources

**1. [checkov documentation — supported frameworks and checks](https://www.checkov.io/5.Policy%20Index/terraform.html)**
The full checkov policy index lists every built-in check by ID, provider, resource type, and description. Use this reference to understand what each CKV check tests and to find the correct skip annotation for justified exceptions.

**2. [tfsec documentation and check library](https://aquasecurity.github.io/tfsec/)**
Official tfsec documentation covering all built-in rules, custom check authoring, configuration options, and CI integration. Includes SARIF output configuration and per-check severity overrides.

**3. [HashiCorp Sentinel policy language documentation](https://developer.hashicorp.com/sentinel/docs)**
Reference documentation for the Sentinel policy-as-code language used with Terraform Cloud and Terraform Enterprise. Covers enforcement levels (advisory, soft-mandatory, hard-mandatory), policy sets, and example policies for common IaC security controls.

---

Reading Guide — Module 06 | CIS-4350 | Texas Wesleyan University | Professor Nash
