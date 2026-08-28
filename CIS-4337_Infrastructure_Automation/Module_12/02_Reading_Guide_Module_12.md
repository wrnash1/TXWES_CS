# Reading Guide: Module 12 — Terraform and CI/CD Pipelines

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4337 &BULL; INFRASTRUCTURE AUTOMATION & CONFIGURATION MANAGEMENT</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Overview

This reading guide accompanies Module 12 and provides the conceptual foundation for integrating Terraform into automated pipelines. By the end of this module you will understand the architecture of a production-grade CI/CD Terraform pipeline, the tools used to enforce quality and security gates, and the strategies for detecting and responding to infrastructure drift.

**Estimated reading time:** 60–75 minutes

---

## Section 1: The Case for Pipeline-Driven Infrastructure

### 1.1 Problems with Manual Terraform Workflows

Manual workflows are the starting point for most Terraform practitioners, but they do not scale. The core problems are reproducibility, accountability, and safety.

Reproducibility fails when different engineers use different Terraform versions or different provider plugin caches. A configuration that plans cleanly on one machine may behave differently on another due to version mismatches.

Accountability fails because there is no automatic record of who ran what plan, what the plan showed, and when apply was executed. In regulated environments, this gap is a compliance finding.

Safety fails most severely when apply runs without a reviewed plan. Even experienced engineers make configuration errors. The plan output is the safety net — it shows exactly what Terraform intends to change before any changes occur. Without a formal review step, that safety net is optional rather than mandatory.

### 1.2 GitOps for Infrastructure

GitOps is the practice of using Git as the single source of truth for both application and infrastructure state. All changes to infrastructure flow through pull requests. Merging a PR to the main branch is the approved change process. Rollback means reverting a commit, not running a manual command.

For Terraform, GitOps means:

- No one runs `terraform apply` from a local workstation against production
- All plans are reviewed as PR comments before merge
- All applies are automated and logged by the CI system
- The Git history is the complete audit trail of infrastructure changes

This model aligns directly with change management frameworks used in SOC 2 Type II audits, ISO 27001, and FedRAMP authorization.

---

## Section 2: GitHub Actions Pipeline Architecture

### 2.1 Workflow File Structure

A GitHub Actions workflow is defined in YAML at `.github/workflows/terraform.yml`. The file specifies:

- **Triggers** (`on:`): which events start the workflow
- **Jobs**: the units of work, each running on a GitHub-hosted runner
- **Steps**: the individual commands within each job

For Terraform, the standard triggers are `pull_request` (for plan and validation) and `push` to the main branch (for apply).

### 2.2 The Validate Job

The validate job runs two commands:

- `terraform fmt -check` — verifies all files are formatted per Terraform's canonical style. This is a style gate, not a functional one, but consistent formatting reduces review friction.
- `terraform validate` — checks that the configuration is syntactically valid and internally consistent. It does not contact cloud providers; it only validates the HCL structure.

Both commands should be required status checks in your GitHub branch protection rules. If either fails, the PR cannot merge.

### 2.3 The Plan Job

The plan job is the most important job in the pipeline. Its steps are:

1. Check out the repository code
2. Set up Terraform using `hashicorp/setup-terraform@v3`
3. Configure backend credentials via environment variables from GitHub Secrets
4. Run `terraform init` to initialize providers and backend
5. Run `terraform plan -out=tfplan -no-color` to generate and save the plan
6. Upload `tfplan` as a workflow artifact
7. Post the plan output as a PR comment

Saving the plan as an artifact is the critical step. It creates a binding between the reviewed plan and the subsequent apply. When the apply job runs after merge, it downloads this exact artifact and applies it. This ensures the reviewer saw exactly what will be applied.

### 2.4 The Apply Job

The apply job runs on push to main (after PR merge). Its steps are:

1. Check out the repository
2. Set up Terraform
3. Configure credentials
4. Run `terraform init`
5. Download the `tfplan` artifact from the plan job
6. Run `terraform apply tfplan`

The apply job should have a `needs:` dependency on the plan job so it never runs without a valid plan artifact.

### 2.5 OIDC Authentication

Storing long-lived AWS, Azure, or GCP credentials as GitHub Secrets is a security risk — if those secrets are compromised, an attacker has persistent cloud access. OIDC eliminates this risk.

With OIDC:

- GitHub Actions requests a short-lived token from GitHub's OIDC provider
- AWS, Azure, or GCP verifies the token against a pre-configured trust relationship
- The cloud provider issues temporary credentials scoped to a specific IAM role
- Those credentials expire when the job ends

There are no stored secrets. The attack surface is dramatically reduced. OIDC is the recommended authentication method for any production CI/CD pipeline interacting with cloud APIs.

---

## Section 3: GitLab CI Pipeline Architecture

### 3.1 Pipeline Stages

GitLab CI defines pipelines in `.gitlab-ci.yml`. Stages run sequentially; jobs within a stage run in parallel. A standard Terraform pipeline uses:

- **validate** — fmt check and validate
- **plan** — generate and store the plan
- **apply** — apply the plan (manual trigger on main branch only)

### 3.2 Manual Gates

A manual gate in GitLab CI is a job with `when: manual`. The pipeline pauses and waits for a human to click the play button. This is the standard approach for production apply jobs. Combined with GitLab's protected environment feature, you can require that only specific users can trigger the apply job on the production environment.

### 3.3 GitLab Managed State

GitLab offers a built-in Terraform state backend. You configure it in your Terraform `backend` block with the GitLab HTTP backend URL and a personal access token or CI job token. GitLab stores the state file with full encryption and provides a locking mechanism backed by its database. This is a convenient option for teams already using GitLab who do not want to manage a separate S3 bucket or Terraform Cloud workspace.

---

## Section 4: Drift Detection

### 4.1 What Is Drift?

Infrastructure drift occurs when the actual state of cloud resources differs from the state recorded in `terraform.tfstate`. Common causes include:

- Manual changes made through the cloud console or CLI
- Changes applied by other automation tools (Ansible, Chef, cloud-init scripts)
- Cloud provider automatic updates to managed service configurations
- Expired or deleted resources that Terraform still believes exist

### 4.2 Detecting Drift with Scheduled Pipelines

The `--detailed-exitcode` flag makes `terraform plan` return:

- Exit code 0 — no changes needed
- Exit code 1 — error occurred
- Exit code 2 — changes are present (drift detected)

A nightly scheduled pipeline runs `terraform plan -detailed-exitcode` and checks this exit code. Exit code 2 causes the pipeline to fail, which triggers notifications via email, Slack, or PagerDuty depending on your alerting configuration.

### 4.3 Responding to Drift

When drift is detected, the response depends on the nature of the change:

- **Intended drift (hotfix)**: The manual change was intentional. Update the Terraform configuration to match the current state and commit the change through the normal PR process.
- **Unintended drift (unauthorized change)**: The change must be investigated. Determine who made it and why. Decide whether to revert it (by running terraform apply) or accept it.
- **Cloud provider drift**: The cloud provider automatically changed a configuration (e.g., updated a TLS policy on a load balancer). Use `terraform apply -refresh-only` to update the state file without changing any resources, then codify the provider change in your configuration.

### 4.4 Preventing Drift

The most effective prevention strategy is removing the ability to make manual changes. Use:

- AWS Service Control Policies (SCPs) to deny console/CLI modifications to production resources
- Azure Policies with DeployIfNotExists and Deny effects
- GCP Organization Policies to restrict resource modifications

When the CI pipeline is the only permitted path for infrastructure changes, drift through manual action becomes impossible.

---

## Section 5: Automated Testing with Terratest

### 5.1 Why Test Infrastructure Code?

Application developers have unit tests, integration tests, and end-to-end tests. Infrastructure code deserves the same rigor. A Terraform module that deploys an EC2 instance correctly is not sufficient — you need to verify that the instance is accessible, running the correct AMI, in the correct security group, and responding to health checks.

Static validation (`terraform validate`) only checks syntax. Plan checks only verify intent. Only deploying the infrastructure and testing it confirms that it actually works.

### 5.2 Terratest Architecture

Terratest tests are written in Go and use the `testing` package from the Go standard library. A test file imports `github.com/gruntwork-io/terratest/modules/terraform` and optionally cloud-specific packages like `github.com/gruntwork-io/terratest/modules/aws`.

A standard Terratest flow:

1. Set options including the Terraform directory and any input variables
2. Call `terraform.InitAndApply()` — this runs `terraform init` and `terraform apply`
3. Use `defer terraform.Destroy()` to ensure cleanup even if assertions fail
4. Make assertions using the standard Go `testing` package or the `assert` package
5. Optionally call cloud SDK functions to verify resource properties beyond Terraform outputs

### 5.3 Test Isolation

Test isolation prevents tests from interfering with each other. Key practices:

- Append a random 6-character suffix to all resource names using `random.UniqueId()`
- Use dedicated test AWS accounts or GCP projects where possible
- Set short retention periods and TTL-based cleanup for test resources

### 5.4 Cost and Speed Tradeoffs

Terratest tests are slow — a typical test deploys real resources, which may take minutes. They also cost money. Best practices for managing this:

- Run Terratest only on schedule (nightly) or on manual trigger
- Use `terraform-compliance` or OPA-based policy checks for fast PR feedback
- Maintain a test environment with pre-deployed base infrastructure to reduce test setup time

---

## Section 6: Security Scanning

### 6.1 tfsec

tfsec performs static analysis on Terraform HCL files. It reads your configuration and identifies patterns that match known insecure configurations without contacting any cloud APIs.

Common tfsec findings:

- `aws-s3-no-public-buckets` — S3 bucket allows public access
- `aws-ec2-no-public-ip` — EC2 instance gets a public IP by default
- `aws-iam-no-policy-wildcards` — IAM policy uses `*` for actions or resources
- `azure-storage-use-secure-tls-policy` — storage account accepts TLS 1.0 or 1.1
- `google-compute-no-public-ip` — GCE instance has an external IP

tfsec produces output with severity levels (CRITICAL, HIGH, MEDIUM, LOW) and links to remediation documentation. In CI, run tfsec with `--minimum-severity HIGH` to fail only on high-severity and above.

### 6.2 Checkov

Checkov is a multi-framework policy scanner. For Terraform, it scans both HCL files and plan JSON output. It includes over 1,000 built-in checks organized by cloud provider and compliance framework.

Checkov check IDs follow the pattern `CKV_AWS_*`, `CKV_AZURE_*`, `CKV_GCP_*`. You can skip specific checks with `#checkov:skip=CKV_AWS_18:Reason` inline comments in your Terraform files, creating documented exceptions with justifications.

Checkov produces a SARIF output format that integrates with GitHub's security alerts feature. When you upload Checkov's SARIF output as a code scanning artifact, findings appear in the Security tab of your GitHub repository.

### 6.3 Custom Policies

Both tfsec and Checkov support custom policy definitions. This allows organizations to enforce internal standards that go beyond vendor-supplied checks.

Examples of custom organizational policies:

- All EC2 instances must have a `CostCenter` tag
- All S3 buckets must use the organization's centralized KMS key ARN
- All security groups must have a `Owner` tag
- No resources may be deployed to the `us-east-1` region (if your policy requires `us-east-2`)

Custom policies are version-controlled alongside your Terraform code and applied consistently across all pipelines.

---

## Section 7: Pipeline Integration Summary

### 7.1 Recommended Job Ordering

A production Terraform CI/CD pipeline should run jobs in this sequence:

1. **security-scan** — tfsec and Checkov (fast, blocks further runs if critical issues found)
2. **validate** — fmt check and validate (fast, no cloud credentials needed)
3. **plan** — terraform init and plan (requires cloud credentials, saves plan artifact)
4. **review** — human approval step (PR review or manual gate)
5. **apply** — terraform apply with saved plan artifact

### 7.2 Notification Strategy

Successful applies should notify the team in a shared channel. Failed applies require immediate attention — they should page the on-call engineer. Drift detection failures should create tracking tickets automatically rather than paging, since drift is typically not an emergency but needs resolution within the sprint.

### 7.3 Artifact Retention

Pipeline artifacts (plan files, scan reports, apply logs) should be retained for at least 90 days to support audit requests. Some compliance frameworks require one year. Configure artifact expiration policies in your CI platform accordingly.

---

## Key Terms

- **CI/CD**: Continuous Integration / Continuous Delivery — automated build, test, and deploy workflows
- **GitOps**: using Git as the single source of truth for infrastructure state
- **Drift**: divergence between actual infrastructure and Terraform state
- **OIDC**: OpenID Connect — federated identity protocol used for keyless cloud authentication
- **tfsec**: static security analysis tool for Terraform HCL
- **Checkov**: multi-framework policy-as-code scanner
- **Terratest**: Go-based integration testing framework for Terraform modules
- **terraform plan -detailed-exitcode**: returns exit code 2 when changes are present, enabling drift detection
- **Manual gate**: a CI job that waits for human approval before proceeding
- **SARIF**: Static Analysis Results Interchange Format — standard output format for security scan results

---

## Review Questions

1. What are the three exit codes returned by `terraform plan -detailed-exitcode`, and what does each mean?

2. Why is saving a `tfplan` artifact before apply safer than generating a new plan at apply time?

3. What is the primary security advantage of OIDC authentication over storing cloud credentials as CI secrets?

4. Explain the difference between tfsec and Checkov in terms of scope and use case.

5. In a GitLab CI pipeline, what does a `when: manual` job configuration accomplish, and why is it used for production apply jobs?

6. What causes infrastructure drift, and what are two strategies for preventing it?

7. Why are Terratest tests typically not run on every pull request?

---

## Further Reading

- HashiCorp: Automate Terraform (official documentation)
- GitHub Actions: `hashicorp/setup-terraform` action documentation
- Aqua Security: tfsec documentation at aquasecurity.github.io/tfsec
- Bridgecrew: Checkov documentation at checkov.io
- Gruntwork: Terratest documentation at terratest.gruntwork.io
- CNCF: OpenGitOps principles at opengitops.dev

---

## Supplemental Resources

**1. Automate Terraform with GitHub Actions**
<https://developer.hashicorp.com/terraform/tutorials/automation/github-actions>
The official HashiCorp tutorial walking through the complete GitHub Actions workflow for Terraform: format check, validate, plan with PR comment posting, and apply on merge. Covers `hashicorp/setup-terraform` action configuration, backend credential injection via GitHub Secrets, and the plan artifact upload-and-download pattern used to guarantee the reviewed plan is applied.

**2. tfsec Documentation**
<https://aquasecurity.github.io/tfsec/latest>
Complete reference for tfsec including all built-in check IDs organized by cloud provider, the `--minimum-severity` and `--soft-fail` flags used in CI integration, the inline `#tfsec:ignore` comment syntax for documented suppressions, and instructions for writing custom YAML-based checks for organization-specific policies.

**3. Checkov Documentation — Terraform Scanning**
<https://www.checkov.io/5.Policy%20Index/terraform.html>
The Checkov policy index for Terraform covering all `CKV_AWS_*`, `CKV_AZURE_*`, and `CKV_GCP_*` built-in check IDs with descriptions, severity levels, and remediation guidance. Also covers SARIF output format for GitHub Security tab integration, the `#checkov:skip=` inline suppression syntax, and custom policy authoring in Python.

---

End of Module 12 Reading Guide
