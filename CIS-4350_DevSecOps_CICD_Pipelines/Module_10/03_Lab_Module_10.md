# Lab Activity: Module 10 - Infrastructure as Code Security: Terraform Security Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Write intentionally misconfigured Terraform and interpret IaC scanner findings.
- Run Checkov against a Terraform directory and read its output.
- Remediate HIGH and CRITICAL Checkov findings and verify the scan passes.
- Integrate Checkov into a GitHub Actions pipeline as a required status check.
- Explain the security risk of Terraform state files in version control.

---

## Prerequisites

Before beginning this lab, confirm the following:

- Python 3.8 or later is installed.
- Checkov is installed (`pip install checkov` then `checkov --version`).
- You have a GitHub repository from earlier modules where you can add pipeline YAML.
- You have completed the Module 10 video and reading guide.

---

## Part 1: Identify Misconfigurations with Checkov (30 points)

### Part 1 Background

Checkov analyzes Terraform configuration files and maps findings to CIS benchmarks and NIST controls. This part walks through scanning a deliberately misconfigured Terraform module and interpreting the output.

### Part 1 Instructions

**Step 1: Create a misconfigured Terraform configuration.**

Create a directory `lab10/terraform` and add the following `main.tf`:

```hcl
resource "aws_s3_bucket" "data" {
  bucket = "lab10-vulnerable-data-bucket"
}

resource "aws_s3_bucket_acl" "data" {
  bucket = aws_s3_bucket.data.id
  acl    = "public-read"
}

resource "aws_s3_bucket_public_access_block" "data" {
  bucket                  = aws_s3_bucket.data.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_db_instance" "app" {
  identifier          = "lab10-app-db"
  engine              = "postgres"
  engine_version      = "14"
  instance_class      = "db.t3.micro"
  username            = "admin"
  password            = "insecure-hardcoded-password"
  storage_encrypted   = false
  publicly_accessible = true
}

resource "aws_security_group" "web" {
  name        = "lab10-web-sg"
  description = "Web server security group"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t3.micro"

  metadata_options {
    http_tokens = "optional"
  }
}
```

**Step 2: Run Checkov and record findings.**

```bash
checkov -d lab10/terraform --compact
```

Create a table with these columns: Check ID, Resource, Severity, Description, Line Number.

Record every FAILED check. Note: do not remediate yet.

**Step 3: Run Checkov with SARIF output.**

```bash
checkov -d lab10/terraform --output sarif --output-file lab10-results.sarif
```

Open `lab10-results.sarif` and identify the structure: locate the `runs[0].results` array and describe in 1-2 sentences what each result object contains.

**Step 4: Interpret two findings in detail.**

Choose two FAILED checks from your table. For each, write 2-3 sentences explaining: what the misconfiguration is, what the attacker impact would be if this configuration were deployed to production, and what the Checkov check ID is.

### Part 1 Deliverable

Submit: the complete Checkov output table, the SARIF structure description, and the two detailed finding interpretations.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Findings table is complete and accurate with correct check IDs and severities | 12 |
| SARIF structure description is technically accurate | 6 |
| Two finding interpretations correctly explain the misconfiguration and attacker impact | 12 |

---

## Part 2: Remediate and Verify (25 points)

### Part 2 Background

Remediation closes the gap between the vulnerable configuration and the security baseline. After remediation, a clean Checkov scan confirms the configuration is correct before Terraform applies it.

### Part 2 Instructions

**Step 1: Remediate all HIGH and CRITICAL findings.**

Update `main.tf` to fix each finding from Part 1. The remediated configuration must:

- Set all four `block_public_*` attributes to `true` on the S3 bucket public access block.
- Remove the `acl = "public-read"` from the S3 bucket ACL resource.
- Set `storage_encrypted = true` on the RDS instance and remove the hardcoded password (replace with a reference to a variable: `var.db_password`).
- Set `publicly_accessible = false` on the RDS instance.
- Restrict the SSH security group ingress rule to `cidr_blocks = ["10.0.0.0/8"]` or remove it entirely.
- Set `http_tokens = "required"` on the EC2 instance metadata options.

**Step 2: Run Checkov on the remediated configuration.**

```bash
checkov -d lab10/terraform --compact
```

Confirm that all previously FAILED checks now PASS. Record the new output.

**Step 3: Write the remediation summary.**

Create a table with columns: Check ID, Original Configuration, Remediated Configuration, Resolved (Y/N).

### Part 2 Deliverable

Submit: the remediated `main.tf`, the clean Checkov output showing all checks passed, and the remediation summary table.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Remediated `main.tf` correctly addresses all HIGH and CRITICAL findings | 10 |
| Clean Checkov output shows all previously FAILED checks now PASS | 8 |
| Remediation summary table is accurate and complete | 7 |

---

## Part 3: GitHub Actions IaC Pipeline Integration (25 points)

### Part 3 Background

IaC scanning must run automatically on every pull request that modifies Terraform configuration. This prevents misconfigurations from reaching the main branch and being applied to production infrastructure.

### Part 3 Instructions

**Step 1: Add an IaC scan job to your GitHub Actions pipeline.**

Update your `full-pipeline.yml` to add an `iac-scan` job triggered on PRs that modify files in `terraform/**`. The job must:

- Run on `ubuntu-latest`.
- Check out the code with `actions/checkout@v4`.
- Use the `bridgecrewio/checkov-action@master` action with `directory: terraform/`, `framework: terraform`, `output_format: sarif`, `output_file_path: checkov-results.sarif`, and `soft_fail: false`.
- Upload the SARIF results to GitHub Code Scanning using `github/codeql-action/upload-sarif@v3` with `if: always()` to upload even on failure.

**Step 2: Commit the vulnerable `main.tf` from Part 1 to a feature branch and open a PR.**

Push and observe the IaC scan job failing in the Actions tab.

**Step 3: Screenshot the failed IaC scan.**

Capture the failing Checkov job output showing the specific failed checks.

**Step 4: Commit the remediated `main.tf` from Part 2.**

Push the update and observe the pipeline re-run passing.

**Step 5: Screenshot the passing pipeline.**

Capture the passing Checkov job and the green PR status checks.

### Part 3 Deliverable

Submit: the updated pipeline YAML, screenshots of the failed and passing pipeline runs, and a one-paragraph explanation of why `if: always()` is used on the SARIF upload step.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| Pipeline YAML correctly adds the iac-scan job with all required parameters | 10 |
| Screenshot shows failed pipeline with Checkov findings | 7 |
| Screenshot shows passing pipeline after remediation | 5 |
| Explanation of `if: always()` is technically accurate | 3 |

---

## Part 4: IaC Security Concepts (20 points)

### Part 4 Instructions

Answer each question in 3-5 sentences using precise IaC and DevSecOps terminology.

**Question A:** Your team stores `terraform.tfstate` in the repository alongside the Terraform configuration files for simplicity. A security engineer requests that the state file be moved to an S3 remote backend. Explain what a Terraform state file contains, why it must not be stored in version control, and what the recommended AWS remote backend configuration includes (name the specific AWS services involved and their security roles).

**Question B:** A developer argues: "Checkov is slowing down our PR pipeline and flagging things that don't matter for our specific use case. We should just disable it." Propose a specific configuration change to Checkov that allows the pipeline to continue collecting findings without blocking PRs, and explain the DevSecOps tradeoff this creates. Then explain under what conditions re-enabling the gate would be appropriate.

**Question C:** Terrascan uses Rego for its policy definitions. Explain what Rego is, which other DevSecOps tool ecosystem uses Rego for policy enforcement, and what advantage reusing Rego policies between IaC scanning and that other ecosystem provides to a DevSecOps team managing both Terraform infrastructure and Kubernetes deployments.

### Part 4 Deliverable

Submit written answers to all three questions. Label each answer with the question letter.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Question A correctly explains state file contents and names the correct AWS services | 7 |
| Question B correctly identifies the Checkov parameter and articulates the tradeoff accurately | 6 |
| Question C correctly explains Rego, names the other ecosystem, and explains the reuse advantage | 7 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (10) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
