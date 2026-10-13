# Lab: Module 14 — Multi-Cloud Provisioning with Terraform

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will configure Terraform with multiple provider instances to deploy resources across two AWS regions simultaneously using provider aliasing. You will then add a DNS-based failover routing policy in Route 53, observe cross-provider dependency resolution, and work with version constraints and the lock file.

**Estimated time:** 90–120 minutes

**Prerequisites:**

- Terraform CLI v1.5+ installed
- AWS Free Tier account
- Registered domain name in Route 53 (or use a subdomain of an existing hosted zone)
- Completed Module 12 lab (S3 backend available for state storage)

**Note:** This lab uses two AWS regions to simulate multi-cloud provider aliasing. The concepts — aliased provider blocks, module providers map, cross-provider dependencies — apply identically when the two providers are AWS and Azure rather than two AWS regions. Using two AWS regions avoids the need for a second cloud account while demonstrating all the same Terraform mechanics.

---

## Part 1: Multi-Region Provider Configuration (20 minutes)

### Step 1.1 — Create the Project Structure

```text
module14-lab/
  main.tf
  variables.tf
  outputs.tf
  backend.tf
  modules/
    app_bucket/
      main.tf
      variables.tf
      outputs.tf
```

### Step 1.2 — Configure the Root Module Providers

Create `main.tf` in the root:

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "aws" {
  region = var.primary_region
}

provider "aws" {
  alias  = "secondary"
  region = var.secondary_region
}
```

Create `variables.tf`:

```hcl
variable "primary_region" {
  type    = string
  default = "us-east-2"
}

variable "secondary_region" {
  type    = string
  default = "us-west-2"
}

variable "app_name" {
  type    = string
  default = "module14-lab"
}

variable "owner_tag" {
  type = string
}

variable "hosted_zone_id" {
  description = "Route 53 hosted zone ID for DNS failover records"
  type        = string
  default     = ""
}

variable "primary_domain" {
  description = "Primary application hostname"
  type        = string
  default     = "primary.lab.example.com"
}
```

### Step 1.3 — Write the Child Module

Create `modules/app_bucket/variables.tf`:

```hcl
variable "bucket_name" {
  type = string
}

variable "region_label" {
  type = string
}

variable "owner_tag" {
  type = string
}
```

Create `modules/app_bucket/main.tf`:

```hcl
resource "aws_s3_bucket" "app" {
  bucket = var.bucket_name

  tags = {
    Region    = var.region_label
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}

resource "aws_s3_bucket_versioning" "app" {
  bucket = aws_s3_bucket.app.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "app" {
  bucket = aws_s3_bucket.app.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "app" {
  bucket                  = aws_s3_bucket.app.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

Create `modules/app_bucket/outputs.tf`:

```hcl
output "bucket_name" {
  value = aws_s3_bucket.app.id
}

output "bucket_arn" {
  value = aws_s3_bucket.app.arn
}

output "bucket_region" {
  value = aws_s3_bucket.app.region
}
```

---

## Part 2: Module Instantiation with Provider Aliases (25 minutes)

### Step 2.1 — Call the Module Twice with Different Providers

Add to the root `main.tf`:

```hcl
resource "random_id" "suffix" {
  byte_length = 4
}

module "primary_bucket" {
  source = "./modules/app_bucket"

  providers = {
    aws = aws
  }

  bucket_name  = "${var.app_name}-primary-${random_id.suffix.hex}"
  region_label = var.primary_region
  owner_tag    = var.owner_tag
}

module "secondary_bucket" {
  source = "./modules/app_bucket"

  providers = {
    aws = aws.secondary
  }

  bucket_name  = "${var.app_name}-secondary-${random_id.suffix.hex}"
  region_label = var.secondary_region
  owner_tag    = var.owner_tag
}
```

Create `outputs.tf`:

```hcl
output "primary_bucket_name" {
  value = module.primary_bucket.bucket_name
}

output "primary_bucket_region" {
  value = module.primary_bucket.bucket_region
}

output "secondary_bucket_name" {
  value = module.secondary_bucket.bucket_name
}

output "secondary_bucket_region" {
  value = module.secondary_bucket.bucket_region
}
```

### Step 2.2 — Initialize and Plan

```bash
terraform init
terraform plan -var="owner_tag=your-name"
```

Observe in the plan output that resources are being created in both `us-east-2` and `us-west-2`. The plan shows the provider associated with each resource in the resource address format.

### Step 2.3 — Apply

```bash
terraform apply -var="owner_tag=your-name" -auto-approve
```

Verify in the AWS console that buckets were created in both regions. Verify the region of each bucket matches the expected provider.

---

## Part 3: Cross-Provider Dependencies (20 minutes)

### Step 3.1 — Add a Cross-Region S3 Replication Rule

In the root `main.tf`, add an IAM role for replication and configure primary-to-secondary replication:

```hcl
data "aws_iam_policy_document" "replication_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["s3.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "replication" {
  name               = "${var.app_name}-s3-replication-${random_id.suffix.hex}"
  assume_role_policy = data.aws_iam_policy_document.replication_assume_role.json

  tags = {
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}

resource "aws_s3_bucket_replication_configuration" "primary_to_secondary" {
  role   = aws_iam_role.replication.arn
  bucket = module.primary_bucket.bucket_name

  rule {
    id     = "replicate-all"
    status = "Enabled"

    destination {
      bucket        = module.secondary_bucket.bucket_arn
      storage_class = "STANDARD"
    }
  }

  depends_on = [
    module.primary_bucket,
    module.secondary_bucket,
  ]
}
```

### Step 3.2 — Observe Dependency Resolution

Run `terraform plan`. Observe that Terraform correctly orders the operations:

1. `random_id.suffix` — no dependencies
2. `aws_iam_role.replication` — depends on the policy document data source
3. Both module buckets — independent, can run in parallel
4. `aws_s3_bucket_replication_configuration` — depends on both buckets and the IAM role

Terraform identifies the cross-module dependency and creates the replication configuration only after both buckets are ready.

---

## Part 4: Version Constraints and Lock File (15 minutes)

### Step 4.1 — Inspect the Lock File

After running `terraform init`, open `.terraform.lock.hcl`:

```bash
cat .terraform.lock.hcl
```

Identify:

- The resolved AWS provider version
- The constraints line showing `~> 5.0`
- The `h1:` hash and `zh:` platform-specific hashes

### Step 4.2 — Attempt a Version Downgrade

Temporarily change the AWS provider constraint to `= 4.0.0` in `required_providers`. Run:

```bash
terraform init
```

Observe the error. The lock file records `5.x` and the new constraint conflicts with the installed version. Restore `~> 5.0` and run `terraform init` again to confirm it resolves cleanly.

### Step 4.3 — Simulate Lock File Absence

Delete `.terraform.lock.hcl` and run `terraform init`. Terraform downloads the newest version satisfying `~> 5.0` and regenerates the lock file. Compare the new lock file version to the previous one.

Document: did the version change? This demonstrates why the lock file must be committed to version control.

---

## Part 5: Optional Route 53 Failover DNS (20 minutes)

This part requires a registered domain in Route 53. Skip if you do not have one.

### Step 5.1 — Add Failover DNS Records

Add to `main.tf`:

```hcl
resource "aws_route53_health_check" "primary" {
  count = var.hosted_zone_id != "" ? 1 : 0

  fqdn              = "s3.${var.primary_region}.amazonaws.com"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/"
  failure_threshold = 3
  request_interval  = 30

  tags = {
    Name      = "primary-region-check"
    ManagedBy = "Terraform"
  }
}

resource "aws_route53_record" "primary" {
  count = var.hosted_zone_id != "" ? 1 : 0

  zone_id = var.hosted_zone_id
  name    = var.primary_domain
  type    = "CNAME"
  ttl     = 60

  records = [module.primary_bucket.bucket_name]

  failover_routing_policy {
    type = "PRIMARY"
  }

  health_check_id = aws_route53_health_check.primary[0].id
  set_identifier  = "primary"
}

resource "aws_route53_record" "secondary" {
  count = var.hosted_zone_id != "" ? 1 : 0

  zone_id = var.hosted_zone_id
  name    = var.primary_domain
  type    = "CNAME"
  ttl     = 60

  records = [module.secondary_bucket.bucket_name]

  failover_routing_policy {
    type = "SECONDARY"
  }

  set_identifier = "secondary"
}
```

Apply with your hosted zone ID and verify the DNS records in the Route 53 console.

---

## Lab Submission Requirements

Include in your submission document:

1. Screenshot of the `terraform plan` output showing resources being created in both `us-east-2` and `us-west-2`
2. Screenshot of the AWS console S3 bucket list showing both buckets in their respective regions
3. The contents of your `.terraform.lock.hcl` file (copy the text)
4. The error message produced when you attempted to use `= 4.0.0` as the version constraint
5. Answer: In what scenario would you use the `providers` map on a module block, and what happens if you omit it when a module uses aliased providers? (2–3 sentences)

---

## Cleanup

```bash
terraform destroy -var="owner_tag=your-name" -auto-approve
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Cross-Account Provider Aliasing with AssumeRole

Simulate a multi-account deployment by configuring two `aws` provider aliases that use different IAM role assumptions to represent a dev account and a staging account. In a real organization these would be separate AWS accounts; in this lab you will use two IAM roles within the same account to practice the configuration pattern.

**Step A.** Create two IAM roles in your AWS account using the AWS console or CLI:

```bash
# Create a dev role (using your own account ID as the trusted principal for simplicity)
aws iam create-role --role-name tf-lab-dev-role \
  --assume-role-policy-document '{
    "Version":"2012-10-17",
    "Statement":[{
      "Effect":"Allow",
      "Principal":{"AWS":"arn:aws:iam::ACCOUNT_ID:root"},
      "Action":"sts:AssumeRole"
    }]
  }'
aws iam attach-role-policy --role-name tf-lab-dev-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# Repeat for staging role
aws iam create-role --role-name tf-lab-staging-role \
  --assume-role-policy-document '{
    "Version":"2012-10-17",
    "Statement":[{
      "Effect":"Allow",
      "Principal":{"AWS":"arn:aws:iam::ACCOUNT_ID:root"},
      "Action":"sts:AssumeRole"
    }]
  }'
aws iam attach-role-policy --role-name tf-lab-staging-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```

**Step B.** Create `challenge1/main.tf` with two aliased provider configurations using `assume_role`:

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  alias  = "dev"
  region = "us-east-2"

  assume_role {
    role_arn     = "arn:aws:iam::ACCOUNT_ID:role/tf-lab-dev-role"
    session_name = "terraform-dev"
  }
}

provider "aws" {
  alias  = "staging"
  region = "us-east-2"

  assume_role {
    role_arn     = "arn:aws:iam::ACCOUNT_ID:role/tf-lab-staging-role"
    session_name = "terraform-staging"
  }
}

resource "aws_s3_bucket" "dev_artifacts" {
  provider = aws.dev
  bucket   = "tf-lab-dev-artifacts-${var.suffix}"

  tags = {
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}

resource "aws_s3_bucket" "staging_artifacts" {
  provider = aws.staging
  bucket   = "tf-lab-staging-artifacts-${var.suffix}"

  tags = {
    Environment = "staging"
    ManagedBy   = "Terraform"
  }
}

variable "suffix" {
  type = string
}

output "dev_bucket" {
  value = aws_s3_bucket.dev_artifacts.id
}

output "staging_bucket" {
  value = aws_s3_bucket.staging_artifacts.id
}
```

1. Run `terraform init` and `terraform plan -var="suffix=your-name"`. Observe that the plan creates two S3 buckets and that both are attributed to their respective aliased providers in the plan output.
2. Inspect `.terraform.lock.hcl` after init. Record the version selected and the h1 hash for the AWS provider. Note that a single lock file entry covers both aliased provider instances because they share the same source.
3. Run `terraform apply -var="suffix=your-name"` and verify both buckets exist in the AWS console.
4. Record in `lab_notes.txt`: when Terraform assumes a role, the temporary credentials last 1 hour by default. What `assume_role` argument would you add to set a custom session duration of 30 minutes, and why might a shorter session duration be preferable for a CI pipeline that runs for only a few minutes?

### Challenge 2: Provider Version Constraint Pinning and Lock File Upgrade

Explore the interaction between version constraints and the lock file by intentionally creating and then resolving a constraint conflict.

**Step A.** In a new directory `challenge2/`, create `main.tf` with a deliberately older version constraint:

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "= 5.0.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

resource "random_id" "tag_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "pinned" {
  bucket = "tf-lab-pinned-${random_id.tag_suffix.hex}"
}
```

**Step B.** Run `terraform init` to install the exact pinned version, then examine the lock file:

```bash
terraform init
cat .terraform.lock.hcl
```

1. Note the exact version recorded for `hashicorp/aws` and `hashicorp/random`. Record both in `lab_notes.txt`.
2. Update the constraint in `main.tf` to `version = "~> 5.0"` to allow any `5.x` release, then run `terraform init` again (without `-upgrade`). Observe whether Terraform upgrades or keeps the existing lock file version and explain why in `lab_notes.txt`.
3. Now run `terraform init -upgrade`. Observe that Terraform selects the latest `5.x` version, updates `.terraform.lock.hcl`, and reports the version change. Record the before and after versions.
4. Change the constraint back to `version = "= 5.0.0"` and run `terraform init` without `-upgrade`. Observe the error Terraform produces when the lock file version conflicts with the updated constraint, and record the exact error message.
5. Document in `lab_notes.txt`: what is the correct workflow for deliberately upgrading a provider in a team environment so that the lock file update is reviewed and approved through the same process as code changes?

### Reflection Questions

1. The lab used explicit `provider = aws.primary` and `provider = aws.secondary` meta-arguments on resources to assign them to the correct provider alias. Explain what would happen if you omitted the `provider` argument on a resource in a configuration that has two `aws` provider instances — one with an alias and one without. Which provider instance would Terraform use, and what rule determines this? Describe a scenario where forgetting a `provider` assignment would cause a resource to be created in the wrong region or account without a plan-time error.
2. The `.terraform.lock.hcl` file records both the selected version and h1 cryptographic hashes for each provider. Explain the security purpose of the hash entries. What attack does hash verification prevent, and under what specific circumstance would you need to run `terraform providers lock -platform=` to add additional hash entries to the lock file?

---

End of Module 14 Lab
