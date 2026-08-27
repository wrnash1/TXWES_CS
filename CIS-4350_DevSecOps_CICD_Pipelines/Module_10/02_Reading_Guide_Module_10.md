# Reading Guide: Module 10 - Infrastructure as Code Security: Terraform Security Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 10 covers IaC security — the DevSecOps control that prevents cloud infrastructure misconfigurations from reaching production. Infrastructure as Code means your cloud resources are defined in version-controlled configuration files. IaC security scanning tools analyze those files statically — before any infrastructure is provisioned — to identify misconfigurations against security benchmarks. This module covers Terraform as the primary IaC language and Checkov, tfsec, and Terrascan as the primary scanning tools.

---

## Section 1: High-Yield Glossary

**IaC (Infrastructure as Code)** — The practice of defining cloud infrastructure resources (compute, storage, networking, IAM) in version-controlled configuration files rather than through manual console operations. Primary languages: Terraform (HCL), CloudFormation (JSON/YAML), Pulumi (Python/TypeScript), Bicep (Azure).

**Terraform** — HashiCorp's open-source IaC tool that uses HCL (HashiCorp Configuration Language) to define cloud resources. Resources are declared in `.tf` files and applied via `terraform plan` / `terraform apply`.

**HCL (HashiCorp Configuration Language)** — The configuration language used by Terraform. Human-readable, supports variables, modules, outputs, and data sources.

**IaC security scanning** — Static analysis of IaC configuration files to detect security misconfigurations before infrastructure is provisioned. Equivalent to SAST for infrastructure code.

**Checkov** — An open-source IaC security scanner from Bridgecrew/Palo Alto Networks. Supports the broadest framework set: Terraform, CloudFormation, Kubernetes manifests, Dockerfiles, ARM templates, Bicep, Helm charts. Maps checks to CIS benchmarks, NIST, and SOC2.

**tfsec** — An open-source Terraform-focused static analysis tool from Aqua Security. Optimized for HCL analysis with detailed Terraform-specific context in findings.

**Terrascan** — An open-source IaC scanner from Tenable. Uses Rego (the Open Policy Agent policy language) for defining security policies, enabling custom policy reuse across IaC scanning and Kubernetes admission control.

**CIS Benchmarks** — Configuration security standards published by the Center for Internet Security. CIS AWS Foundations Benchmark defines secure configurations for S3, IAM, VPC, RDS, and other AWS services. Checkov maps its checks to CIS controls.

**IMDSv2 (Instance Metadata Service v2)** — An AWS EC2 security improvement that requires session-oriented authentication for metadata API requests, preventing SSRF attacks from accessing instance credentials. Checkov check `CKV_AWS_79`.

**Terraform state** — A file or remote backend that records the current state of provisioned infrastructure. State files can contain sensitive values (database passwords, private IPs). State should be stored in encrypted remote backends (S3 + DynamoDB), not in version control.

**`terraform plan`** — A dry run that shows what changes `terraform apply` would make without provisioning anything. IaC scanners run before `terraform plan` to catch misconfigurations at the source code level.

**Rego** — The policy language used by Open Policy Agent (OPA) and Terrascan. Declarative, logic-based language for expressing policy as code. Used in Kubernetes admission controllers and IaC policy enforcement.

**Misconfiguration** — A cloud resource configuration that violates a security best practice — for example, an S3 bucket with public access enabled, a security group allowing inbound traffic from 0.0.0.0/0, or an RDS instance with encryption disabled.

**SARIF (Static Analysis Results Interchange Format)** — A JSON-based standard format for security tool findings. Supported by GitHub Code Scanning for unified display of SAST, IaC, and container scan results in the Security tab.

---

## Section 2: IaC Scanner Comparison

| Dimension | Checkov | tfsec | Terrascan |
|---|---|---|---|
| Maintainer | Bridgecrew / Palo Alto Networks | Aqua Security | Tenable |
| License | Open-source (Apache 2.0) | Open-source (MIT) | Open-source (Apache 2.0) |
| Framework support | Terraform, CloudFormation, K8s, Dockerfile, ARM, Bicep, Helm | Terraform (primary), some others | Terraform, CloudFormation, K8s, Helm |
| Policy language | Python (built-in) | Go (built-in) | Rego (OPA) |
| Custom policies | Python or YAML | YAML | Rego |
| CIS benchmark mapping | Yes | Yes | Yes |
| SARIF output | Yes | Yes | Yes |
| GitHub Action | `bridgecrewio/checkov-action` | `aquasecurity/tfsec-action` | `tenable/terrascan-action` |
| Pipeline exit code | `soft_fail: false` | `--minimum-severity` | `--severity` |

---

## Section 3: Common Terraform Misconfigurations and Checkov Checks

| Misconfiguration | Checkov Check ID | Risk | Remediation |
|---|---|---|---|
| S3 public access enabled | CKV_AWS_20, CKV_AWS_57 | Data exposure | Set all `block_public_*` to `true` |
| S3 encryption disabled | CKV_AWS_19 | Data at rest exposure | Enable `server_side_encryption_configuration` |
| S3 access logging disabled | CKV_AWS_18 | No audit trail | Enable `logging` block |
| Security group ingress 0.0.0.0/0 | CKV_AWS_25 | Network exposure | Restrict `cidr_blocks` to known ranges |
| RDS encryption disabled | CKV_AWS_17 | Data at rest exposure | Set `storage_encrypted = true` |
| EC2 IMDSv2 not enforced | CKV_AWS_79 | SSRF to credential theft | Set `http_tokens = "required"` |
| IAM wildcard permissions | CKV_AWS_40 | Excessive privilege | Replace `*` actions with specific permissions |
| CloudTrail logging disabled | CKV_AWS_67 | No audit trail | Enable `enable_log_file_validation = true` |

---

## Section 4: IaC Security Pipeline Integration

| Stage | Action | Tool |
|---|---|---|
| Pre-commit | Scan staged `.tf` files before commit | Checkov pre-commit hook |
| Pull request | Run full IaC scan as PR status check | Checkov/tfsec GitHub Actions |
| Merge to main | Block merge if HIGH/CRITICAL findings present | Branch protection + required status checks |
| `terraform plan` | Review plan output for unexpected changes | `terraform plan` + policy check |
| `terraform apply` | Automated apply gated by plan approval | Environment protection rules |

---

## Section 5: Terraform State Security

Terraform state files record the current state of all provisioned resources and can contain sensitive values. Key security practices:

- Store state in a remote backend with encryption at rest (S3 with SSE-KMS + DynamoDB state locking).
- Never commit `terraform.tfstate` or `terraform.tfstate.backup` to version control.
- Add `*.tfstate` and `*.tfstate.backup` to `.gitignore`.
- Use IAM policies to restrict who can read the state backend.
- Enable state versioning on S3 to allow rollback.

---

## Section 6: SAST vs. IaC Scanning Comparison

| Dimension | SAST | IaC Security Scanning |
|---|---|---|
| Target | Application source code | Infrastructure configuration files |
| Language | Python, Java, JavaScript, etc. | Terraform HCL, CloudFormation YAML, etc. |
| Finds | CWEs, injection flaws, hardcoded secrets | Cloud misconfigurations, over-permissive policies |
| Pipeline stage | Commit / PR | PR (before provisioning) |
| Tools | Semgrep, SonarQube, Checkmarx | Checkov, tfsec, Terrascan |
| Benchmark alignment | OWASP Top 10, CWE | CIS Benchmarks, NIST, SOC2 |

---

## Section 7: Kubernetes RBAC Model Reference

The principle of least privilege in IaC mirrors RBAC least privilege.

- Avoid wildcard IAM permissions in Terraform — `"Action": "*"` grants all AWS permissions.
- Scope security group ingress rules to the minimum required CIDR ranges.
- Use resource-level encryption for all data stores.
- Apply the `CKV_AWS_*` checks as a minimum security baseline.

---

## Section 8: DevSecOps Professional Exam Tips

1. **IaC scanning pipeline stage** — IaC security scanning runs at the PR stage, before `terraform plan` or `terraform apply`. This is the IaC equivalent of SAST — static analysis of configuration code before execution.

2. **Checkov framework support** — Know that Checkov has the broadest framework support: Terraform, CloudFormation, Kubernetes manifests, Dockerfiles, ARM templates, Bicep, and Helm charts. This makes it the most versatile option for multi-cloud, multi-framework environments.

3. **Terrascan and Rego** — Know that Terrascan uses Rego for policy definitions, the same language as OPA and Kubernetes admission controllers. This enables policy reuse between IaC scanning and admission control.

4. **Three canonical misconfigurations** — Memorize: S3 public access (`block_public_acls = false`), security group `0.0.0.0/0` ingress, and RDS `storage_encrypted = false`. Know the Checkov check IDs for S3 public access (CKV_AWS_20) and RDS encryption (CKV_AWS_17).

5. **`soft_fail: false`** — Know that `soft_fail: false` in the Checkov GitHub Action causes the job to exit non-zero on any FAILED check, acting as a pipeline gate. `soft_fail: true` allows the pipeline to continue despite findings.

6. **Terraform state security** — Know that `terraform.tfstate` can contain sensitive values and must never be committed to version control. Know that the secure pattern is an S3 remote backend with encryption and DynamoDB state locking.

7. **SARIF output** — All three IaC scanners (Checkov, tfsec, Terrascan) support SARIF output. Know that SARIF files are uploaded to GitHub Code Scanning using the `github/codeql-action/upload-sarif@v3` action.

8. **Shift-left for infrastructure** — The core DevSecOps value of IaC scanning is catching misconfigurations before they reach production. A publicly exposed S3 bucket found in a PR is infinitely cheaper to fix than one found after a data breach.

---

## Section 9: Required Reading

- Review the OWASP Infrastructure as Code Security Cheat Sheet at [https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html).

---

## Section 10: Study Checklist

- [ ] Explain what IaC security scanning is and at which pipeline stage it runs.
- [ ] Name the three primary Terraform security scanning tools and one distinguishing characteristic of each.
- [ ] Identify the three canonical Terraform misconfigurations and their remediations.
- [ ] Explain what `soft_fail: false` does in the Checkov GitHub Action.
- [ ] Explain why Terraform state files must not be committed to version control.
- [ ] Describe what Rego is and which IaC scanner uses it.
- [ ] Explain what SARIF is and how IaC scan results are integrated into GitHub Code Scanning.
- [ ] Review the OWASP IaC Security Cheat Sheet at [https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html).
- [ ] Complete the Module 10 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.

---

## 9. Supplemental Resources

**1. [AWS Security Hub documentation and standards reference](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)**
Official AWS documentation covering Security Hub's supported security standards (CIS AWS Foundations, AWS Foundational Security Best Practices, PCI-DSS), finding aggregation, custom insights, and integration with GuardDuty, Inspector, and Macie.

**2. [Prowler open-source AWS security tool](https://docs.prowler.com/)**
Documentation for Prowler, the open-source CLI tool for AWS, Azure, and GCP security assessments. Covers all supported compliance frameworks (CIS, SOC 2, PCI-DSS, HIPAA), output formats (HTML, JSON, SARIF), and CI/CD integration patterns.

**3. [Wiz cloud security graph — research blog and attack path examples](https://www.wiz.io/blog/announcing-wiz-research)**
Wiz's research blog covers real-world cloud attack paths, toxic combination analysis, and case studies of how graph-based CSPM detects risks that rule-based tools miss. Provides concrete examples of the graph security model described in this module.

---

Reading Guide — Module 10 | CIS-4350 | Texas Wesleyan University | Professor Nash
