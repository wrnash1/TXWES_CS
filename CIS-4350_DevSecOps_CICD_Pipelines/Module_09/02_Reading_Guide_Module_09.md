# Reading Guide: Module 09 - Secrets Management – HashiCorp Vault and AWS Secrets Manager

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 09 - Secrets Management – HashiCorp Vault and AWS Secrets Manager**! This module covers secrets management as one of the most critical security controls in a DevSecOps pipeline. Hardcoded credentials in source code and CI/CD configuration files are among the most common causes of cloud security breaches. You will learn how secrets management platforms like HashiCorp Vault and AWS Secrets Manager securely store, rotate, and deliver secrets to pipelines and applications at runtime — replacing the dangerous pattern of hardcoded or environment-variable-embedded credentials. These concepts are directly tested on the CDP exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Secret scanning**: The automated process of scanning Git commits, repository history, and CI/CD configuration files for credential patterns — API keys, private keys, database passwords, OAuth tokens, and high-entropy strings. Tools like Gitleaks, TruffleHog, and GitHub's native secret scanning detect these patterns before or after they enter version control. In a DevSecOps pipeline, secret scanning runs as a pre-commit hook and a CI pipeline stage.

* **Git leaks prevention**: The combination of pre-commit hooks, branch protection rules, and CI pipeline secret scanners that collectively prevent credentials from entering the Git repository history. Once a secret is committed to Git, it is extremely difficult to fully remove — it persists in branch histories, forks, and cached clones. Prevention at the pre-commit stage is the most effective control.

* **HashiCorp Vault**: An open-source secrets management platform that provides centralized, audited, and access-controlled storage for secrets. Vault issues short-lived dynamic credentials (e.g., generating a time-limited database password on demand), eliminates long-lived static credentials, and integrates with CI/CD pipelines via JWT authentication and the Vault API. The CDP exam tests Vault's dynamic secrets, authentication methods, and pipeline integration patterns.

* **Encrypted environment variables**: Secrets stored as encrypted values in CI/CD platform settings (GitHub Actions Secrets, GitLab CI Variables, Jenkins Credentials) that are injected as environment variables into pipeline jobs at runtime. They are masked in pipeline logs so they never appear in plain text in build output. This is the standard pattern for providing pipeline jobs access to registry credentials, cloud provider keys, and API tokens.

---

### 2. Certification Exam Tips

* **Dynamic vs. Static Secrets**: The CDP exam tests the difference between static secrets (a fixed password stored in a vault, valid indefinitely) and dynamic secrets (Vault generates a credential on demand that expires after a configured TTL). Dynamic secrets dramatically reduce the blast radius of a credential compromise because they expire automatically.
* **Secret Injection Patterns**: Know three patterns: (1) CI platform secrets injected as `${{ secrets.MY_SECRET }}` in workflow YAML; (2) Vault JWT auth from a pipeline job that exchanges an OIDC token for a short-lived Vault token; (3) `docker --secret` mount at build time for secrets needed only during image build. The CDP exam tests which pattern is appropriate in a given scenario.
* **Git History Cannot Be Cleaned Easily**: Even `git filter-repo` and force pushes cannot remove secrets from forks, cached clones, or CI/CD system copies of the repository. Prevention (pre-commit hooks + secret scanning) is orders of magnitude more effective than remediation.
* **Study Resource**: The [HashiCorp Vault documentation](https://developer.hashicorp.com/vault/docs) covers authentication methods, secret engines, dynamic credentials, and CI/CD integration patterns — review the "Auth Methods" and "Dynamic Secrets" sections for CDP exam scenarios.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [HashiCorp Vault Getting Started guide](https://developer.hashicorp.com/vault/tutorials/getting-started) — covers Vault's core concepts (secrets engines, policies, authentication methods, token TTLs), how to store and retrieve secrets, and how CI/CD jobs authenticate to Vault using JWT/OIDC. Focus on the dynamic secrets and CI/CD integration tutorials.
* **Required Video**: Watch the secrets management segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates configuring GitHub Actions secrets, running a secret scanner to detect exposed tokens in commits, and verifying that secrets are masked in pipeline logs.

---

### Lab & Command Integration

In this week's hands-on lab, you will implement secrets management practices by:

* **Configure GitHub Actions secrets variables**: Add a repository secret in GitHub Settings → Secrets and Variables, reference it in a workflow using `${{ secrets.MY_API_KEY }}`, and verify it is masked in the pipeline run logs.
* **Run a git leak scan detecting exposed tokens**: Run Gitleaks against a sample repository containing a deliberately embedded API key pattern using `gitleaks detect --source=.`, and confirm the scan identifies the exposed credential and exits with a non-zero code.
* **Verify secrets masking in logs**: In a GitHub Actions workflow, intentionally log the value of a secret using `echo ${{ secrets.MY_SECRET }}` and observe that GitHub replaces the output with `***`, confirming masking works even when accidentally exposed in log commands.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand the difference between static and dynamic secrets, and between pre-commit prevention and post-commit remediation.
* [ ] Read the HashiCorp Vault Getting Started guide at [https://developer.hashicorp.com/vault/tutorials/getting-started](https://developer.hashicorp.com/vault/tutorials/getting-started).
* [ ] Watch the secrets management segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the GitHub Actions secrets configuration and Gitleaks scan in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
