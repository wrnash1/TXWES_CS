# Video Script: Module 12 — Terraform and CI/CD Pipelines

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Segment 1: Introduction (Lines 1–20)

Welcome back to CIS-4337. I am Professor Nash, and this is Module 12: Terraform and CI/CD Pipelines.

If Terraform is the engine that provisions infrastructure, CI/CD pipelines are the transmission that puts it into motion safely. When teams grow and multiple engineers contribute Terraform code, you cannot rely on individuals running `terraform apply` manually from their laptops. That workflow breaks down quickly. It creates drift, inconsistency, and security gaps.

In this module we will cover:

- Why Terraform belongs in a CI/CD pipeline
- GitHub Actions workflow structure for Terraform
- GitLab CI pipeline configuration
- Running plan and apply safely in automation
- Drift detection strategies
- Automated infrastructure testing with Terratest
- Security scanning with tfsec and Checkov

These skills map directly to Terraform Associate Objective 9: understanding Terraform workflows and automation. Let us get started.

---

## Segment 2: Why Automate Terraform? (Lines 21–45)

Manual Terraform workflows have three fundamental problems.

The first is the snowflake workstation. Every engineer's laptop has a different Terraform version, different provider credentials, and different environment variables. What works on one machine may silently fail on another.

The second is the missing plan review. When someone runs `terraform apply` without a team reviewing the plan first, risky changes can slip through. A CI pipeline enforces plan-before-apply as a mandatory gate.

The third is drift blindness. If someone modifies infrastructure manually in the cloud console, Terraform does not know about it unless you run `terraform plan`. A scheduled pipeline catches that drift automatically.

CI/CD solves all three problems by centralizing execution. The pipeline always uses a known Terraform version from the container image. It always runs `plan` first and surfaces the output in a pull request comment. And it can run on a schedule to detect drift before it causes incidents.

The GitOps principle applies here: infrastructure changes flow through source control. The repository is the single source of truth. Merging a pull request is the only approved way to change production infrastructure.

This is not just good engineering practice. It is increasingly a compliance requirement. SOC 2, PCI-DSS, and FedRAMP all require documented change management. A CI/CD pipeline creates that audit trail automatically.

---

## Segment 3: GitHub Actions for Terraform (Lines 46–80)

GitHub Actions is the most common CI platform for teams already using GitHub. Let me walk through a complete Terraform workflow structure.

A workflow file lives at `.github/workflows/terraform.yml`. It triggers on pull requests to main and on direct pushes to main.

On pull request events, the workflow runs three jobs: validate, plan, and security-scan. These run in parallel where possible. The validate job runs `terraform fmt -check` and `terraform validate`. If either fails, the PR cannot merge.

The plan job does the real work. It checks out the code, sets up Terraform using the `hashicorp/setup-terraform` action, initializes with `terraform init`, and then runs `terraform plan -out=tfplan`. The plan output is saved as an artifact and also posted as a comment on the pull request.

Why save the plan as an artifact? Because on the merge event — when apply actually runs — we want to apply exactly the plan that was reviewed, not a new plan generated at apply time. Using `terraform apply tfplan` ensures no surprises.

On push to main — meaning after the PR merges — a separate apply job downloads the saved plan artifact and runs `terraform apply tfplan`. This is the only time apply runs. No human runs apply manually.

The key security consideration is credentials. You never put AWS access keys or Azure client secrets in the workflow YAML. You store them as GitHub Actions secrets and reference them as environment variables. GitHub masks these in logs automatically.

For AWS, the preferred approach is OpenID Connect. GitHub Actions can assume an IAM role via OIDC without needing long-lived credentials at all. You configure an OIDC provider in AWS IAM, create a role that trusts GitHub's OIDC provider, and reference that role ARN in your workflow. The workflow gets temporary credentials that expire when the job ends.

---

## Segment 4: GitLab CI Configuration (Lines 81–110)

GitLab CI uses a `.gitlab-ci.yml` file at the repository root. The concepts are the same but the syntax differs.

GitLab pipelines use stages. For Terraform you typically define four stages: validate, plan, apply, and cleanup.

The validate stage runs `terraform fmt -check` and `terraform validate`. These must pass before any subsequent stage begins.

The plan stage runs `terraform plan -out=tfplan -lock=false`. Notice the `-lock=false` flag. In a CI environment, locking the state file during a plan can block other pipeline runs. Many teams skip the lock on plan and only lock during apply. This is a design tradeoff you must document for your team.

The apply stage runs only on the main branch and requires a manual trigger in GitLab's pipeline UI. This manual gate means a human must click play before infrastructure changes are applied. GitLab calls this a manual job. It gives teams the automation benefit while preserving human approval for production changes.

GitLab has a native Terraform integration. You can configure the pipeline to post plan output directly to merge request comments using the `gitlab-terraform` helper script. GitLab also offers a managed Terraform state backend.

Environment protection rules in GitLab let you restrict which branches can deploy to production environments. Only the main branch with a specific set of approvers can trigger the production apply job. This is a powerful access control layer that complements Terraform's own state locking.

---

## Segment 5: Drift Detection (Lines 111–135)

Drift is what happens when your actual infrastructure diverges from your Terraform state. It can happen when someone makes a manual change in the console, when a resource is modified by another automation tool, or when a cloud provider upgrades a managed service configuration.

The detection mechanism is simple: run `terraform plan` and check whether the exit code indicates changes. Terraform exits with code 0 for no changes, 1 for errors, and 2 for changes present. A CI pipeline can treat exit code 2 as an alert condition.

You configure a scheduled pipeline — nightly in most teams — that runs `terraform plan -detailed-exitcode`. If the exit code is 2, the pipeline fails, which triggers a notification to the team. This tells you that something changed outside of Terraform.

Responding to drift requires judgment. Sometimes drift is intentional — a hotfix was applied manually and needs to be codified in Terraform. Sometimes it is accidental and needs to be reverted. Your runbook should document the response procedure.

For proactive drift prevention, use cloud provider SCPs or Azure Policies to prevent manual console changes to production resources. When only the CI pipeline can make changes, drift cannot occur through the UI.

The `terraform apply -refresh-only` workflow, added in Terraform 1.1, lets you update the state file to match reality without making configuration changes. This is useful when you need to accept a vendor-initiated change before Terraform will plan cleanly again.

---

## Segment 6: Automated Testing with Terratest (Lines 136–165)

Terratest is a Go testing framework from the Terraform community. It lets you write real integration tests for your Terraform modules.

A Terratest test does three things: deploy infrastructure with `terraform apply`, assert that the infrastructure behaves correctly by making HTTP requests or calling cloud APIs, and then destroy the infrastructure with `terraform destroy`.

Why write tests in Go? Because Terratest uses the Go testing standard library and the AWS, Azure, and GCP SDKs directly. You can make API calls to verify your infrastructure is genuinely working, not just that it was provisioned.

A simple test for an AWS EC2 module might use `terraform.InitAndApply()` to deploy the module, then use the aws package to describe the instance and assert it has the correct instance type, is in the running state, and has the correct tags. Finally `terraform.Destroy()` cleans up.

Test isolation is critical. Each test run should use unique resource names, typically by appending a random suffix. This prevents tests from conflicting when multiple engineers run them simultaneously.

Terratest tests are expensive — they create and destroy real cloud resources. This means they should not run on every commit. Run them nightly or on release branches only. Use `terraform validate` and policy checks for faster feedback on every PR.

The `terraform-compliance` tool offers a lighter-weight alternative. It uses Gherkin-style BDD syntax to write policy rules that run against `terraform plan` output without deploying anything.

---

## Segment 7: Security Scanning with tfsec and Checkov (Lines 166–200)

Security scanning should be the first gate in your pipeline, running before plan or apply. If your Terraform code has obvious security misconfigurations, there is no point paying for cloud resources to test them.

tfsec is a static analysis tool from Aqua Security. It scans your Terraform files for known security issues. It checks things like S3 buckets with public access enabled, security groups open to 0.0.0.0/0 on dangerous ports, unencrypted storage volumes, missing logging configurations, and hundreds of other checks.

You run tfsec with `tfsec .` from your Terraform directory. It produces output showing each finding with a severity level, the file and line number, and a remediation suggestion. In a CI pipeline, you run it with `--soft-fail` for warnings and without that flag to hard-fail on CRITICAL and HIGH severity issues.

Checkov is a broader policy-as-code tool from Prisma Cloud. It supports not just Terraform but also CloudFormation, Kubernetes manifests, Dockerfile, and other IaC formats. This makes it useful in polyglot environments.

Checkov checks map directly to CIS Benchmarks, NIST 800-53, PCI-DSS, and SOC 2 control families. When you run Checkov in your pipeline and it passes, you have documented evidence of controls for your compliance auditors.

Both tools support custom policies. You can write your own checks in Python for Checkov or YAML for tfsec to enforce organization-specific rules. For example, you might require that all EC2 instances have a specific cost allocation tag, or that all S3 buckets use a specific KMS key ARN.

Integrating both tfsec and Checkov gives you defense in depth. tfsec is faster and simpler. Checkov is more comprehensive. Running both catches the maximum number of issues before code reaches production.

---

## Segment 8: The Complete Pipeline Mental Model (Lines 201–230)

Let me describe the complete CI/CD pipeline as a mental model.

A developer opens a pull request. The pipeline triggers immediately. In parallel: tfsec runs security scanning, Checkov runs compliance scanning, and the validate job runs `terraform fmt -check` and `terraform validate`. If any of these fail, the PR shows red status checks and cannot merge.

If all checks pass, the plan job runs. It generates a plan, posts the plan output as a PR comment, and saves the plan file as a pipeline artifact. A human reviewer reads the plan output in the PR comment, reviews the code changes, and approves the PR.

On merge to main, the apply job runs. It downloads the saved plan artifact and runs `terraform apply` with that exact plan. The apply output is logged. On success, a notification goes to the team channel. On failure, the pipeline alerts and any partial changes are tracked for remediation.

Nightly, a separate scheduled pipeline runs `terraform plan -detailed-exitcode` against all environments to check for drift. If drift is detected, a ticket is created automatically via the CI platform's API integration.

This pipeline is the gold standard for production Terraform. It enforces code review, documents every change, prevents manual drift, and scans for security issues before anything reaches production.

In the next module we will go deeper on security — specifically secrets management, state file encryption, and least-privilege IAM design.

See you there.

---

End of Module 12 Video Script
