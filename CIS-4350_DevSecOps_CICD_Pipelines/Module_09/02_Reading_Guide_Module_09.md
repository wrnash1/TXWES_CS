# Reading Guide: Module 09 - Secrets Management: HashiCorp Vault and AWS Secrets Manager

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4350 &BULL; DEVSECOPS & CI/CD SECURITY AUTOMATION</text>
    
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


## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 09 covers secrets management — the DevSecOps control that prevents credentials from being exposed in source code, pipeline logs, and container images. Secrets are the keys to your systems: database passwords, API tokens, TLS private keys, SSH keys, and cloud credentials. Every modern application has them. The question is whether they are managed securely or scattered across repositories and build artifacts. This module covers secrets scanning, HashiCorp Vault, and AWS Secrets Manager as the three primary controls.

---

## Section 1: High-Yield Glossary

**Secret** — Any credential that grants access to a system or service: API keys, database passwords, TLS private keys, SSH keys, OAuth tokens, cloud access credentials. Secrets must never appear in source code, pipeline logs, or container images.

**Secrets management** — The set of practices and tools for storing, rotating, auditing, and distributing secrets to applications and pipelines. Centralized secrets management replaces hardcoded and environment-variable-based secrets with dynamic, access-controlled secret retrieval.

**Secrets scanning** — Automated scanning of Git history and new commits for credential-shaped strings using pattern libraries for known secret formats (AWS access keys, GitHub tokens, Stripe keys, etc.). Detective control that identifies already-committed secrets.

**Gitleaks** — An open-source secrets scanner that scans Git repository history and staged changes for known secret patterns. Commonly run as a pre-commit hook and in CI pipelines. Supports `detect` (repository scan) and `protect` (staged changes).

**HashiCorp Vault** — An open-source secrets management platform providing centralized secret storage, dynamic secret generation, access control via policies, and audit logging. Supports multiple auth methods (AppRole, Kubernetes, GitHub) and multiple secret engines (KV, database, PKI, AWS).

**AppRole** — A HashiCorp Vault authentication method designed for machine-to-machine authentication. The client presents a role ID and secret ID to authenticate. Used by CI/CD pipelines to retrieve secrets from Vault.

**Dynamic secrets** — Vault-generated credentials that are created on demand, time-limited, and unique per request. A database secret engine creates a new database user with a password valid for a configurable lease duration. After expiry, the credential is automatically revoked.

**AWS Secrets Manager** — AWS managed service for storing, rotating, and retrieving secrets. Integrates natively with IAM for access control, RDS for automatic database credential rotation, and Lambda for custom rotation logic.

**Secret rotation** — Automatic or scheduled replacement of a secret with a new value, updating both the secrets store and the target system. Limits the exposure window if a secret is compromised. AWS Secrets Manager supports built-in rotation for RDS, Redshift, and DocumentDB.

**OIDC federation** — OpenID Connect-based trust relationship between a CI/CD platform (GitHub, GitLab) and a cloud provider (AWS, GCP, Azure). The pipeline authenticates using a short-lived JWT token issued by the CI provider, receiving temporary cloud credentials without storing long-lived keys in CI secrets.

**Layer persistence** — The Docker image layer model permanently records each `RUN` command layer. Secrets passed as `ARG` or `RUN` commands are recoverable from image layer history even if deleted in a subsequent layer.

**BuildKit secret mount** — Docker BuildKit's `--mount=type=secret` syntax for passing secrets to `RUN` commands without storing them in any image layer. The preferred method for using secrets during image builds.

**KV secret engine** — HashiCorp Vault's Key-Value secret engine for storing static secrets. KV v2 supports versioning, allowing retrieval of previous secret versions and automated rotation workflows.

**Vault policy** — An HCL document that defines what paths and operations an authenticated Vault entity can access. Implements least-privilege access control for secrets.

---

## Section 2: Secrets Failure Mode Reference

| Failure Mode | Example | Consequence | Prevention |
|---|---|---|---|
| Hardcoded in source | `password = 'abc123'` in Python file | Permanent exposure in Git history even after removal | Pre-commit secrets scanning, secrets manager |
| Environment variable leak | `printenv` in pipeline job logs | All env vars including secrets dumped to log | Log masking, avoid debug env dumps |
| Docker image layer | `RUN pip install --index-url https://user:pass@registry/` | Credential in image layer history | BuildKit `--mount=type=secret`, multi-stage builds |
| CI/CD variable misconfiguration | Secret stored in plaintext CI variable instead of masked variable | Visible in pipeline UI and logs | Use masked/protected CI variables |
| Secrets in pipeline YAML | `password: mysecret` hardcoded in workflow file | Committed to repository, visible to all team members | Reference secrets from secrets store by name only |

---

## Section 3: Secrets Scanning Tools

| Tool | Type | Scanning Scope | Integration Points |
|---|---|---|---|
| Gitleaks | Open-source | Full Git history, staged changes | Pre-commit hook, GitHub Actions |
| GitHub Secret Scanning | Built-in (GitHub) | Push, PR, repository history | Automatic for public repos, configured for private |
| GitLab Secret Detection | Built-in (GitLab) | MR, repository | SAST template inclusion |
| truffleHog | Open-source | Git history, live filesystem | Pre-commit, CI pipeline |
| detect-secrets | Open-source | File-level, baseline management | Pre-commit hook |

---

## Section 4: HashiCorp Vault Architecture Reference

| Component | Purpose | Exam Key Point |
|---|---|---|
| Secret engine | Stores or generates secrets (KV, database, PKI, AWS) | Dynamic secrets require a secret engine, not just KV |
| Auth method | Authenticates clients to Vault (AppRole, Kubernetes, GitHub) | AppRole used for CI/CD machine auth |
| Policy | HCL rules defining path-level read/write permissions | Implements least privilege in Vault |
| Lease | Time-limited access grant for dynamic secrets | Lease duration bounds exposure window |
| Audit log | Append-only log of all Vault reads/writes | Required for compliance — every secret access recorded |
| Agent | Sidecar/daemon that handles Vault auth and token renewal | Used for application-level secret injection |

---

## Section 5: Vault vs. AWS Secrets Manager Comparison

| Dimension | HashiCorp Vault | AWS Secrets Manager |
|---|---|---|
| Deployment | Self-hosted or HCP Vault (managed) | AWS managed service |
| Cloud portability | Cloud-agnostic, on-premises capable | AWS-native |
| Dynamic secrets | Yes — database, AWS, PKI engines | No — stores static secrets with rotation |
| Auth methods | AppRole, Kubernetes, GitHub, LDAP, JWT | IAM roles, resource policies |
| Rotation | Manual or via Vault agent | Built-in for RDS, Redshift, DocumentDB; custom Lambda |
| Audit log | Built-in, append-only | CloudTrail integration |
| Cost | Open-source (self-hosted); HCP Vault is paid | $0.40/secret/month + $0.05/10,000 API calls |
| Kubernetes native | Yes — Vault Agent Injector, CSI driver | AWS EKS integration via IAM roles for service accounts |
| OIDC / JWT auth | Yes — JWT/OIDC auth method | Yes — via IAM OIDC identity provider |

---

## Section 6: CI/CD Secrets Integration Patterns

| Pattern | Security Level | Use Case |
|---|---|---|
| Hardcoded in YAML | None — do not use | No acceptable use case |
| CI/CD platform secrets (GitHub Secrets, GitLab CI Variables) | Medium — encrypted at rest, masked in logs | Short-lived secrets, non-rotating credentials |
| Vault AppRole in pipeline | High — audit logged, policy-controlled | Enterprise pipelines, rotating secrets |
| OIDC federation + AWS Secrets Manager | High — no long-lived credentials | AWS-hosted workloads |
| Dynamic secrets via Vault | Highest — time-limited, unique per run | Database credentials, cloud credentials |

---

## Section 7: Kubernetes RBAC Model Reference

The principle of least privilege in secrets management mirrors RBAC least privilege.

- Grant pipelines only the Vault policies or IAM roles required for the specific deployment.
- Rotate secrets regularly — the longer a secret lives, the larger the exposure window if compromised.
- Use dynamic secrets wherever possible — a credential that expires in 1 hour has a bounded exposure window.
- Audit all secret access — Vault's audit log and AWS CloudTrail record every secret retrieval.

---

## Section 8: DevSecOps Professional Exam Tips

1. **Three secrets failure modes** — The exam tests all three: hardcoded in source code (permanent Git history exposure), secrets in logs (from debug commands), and secrets baked into Docker image layers. Know each failure mode and its prevention.

2. **Gitleaks `fetch-depth: 0`** — Know that secrets scanning must use `fetch-depth: 0` in the checkout step to scan full Git history. A shallow clone misses secrets committed in earlier history.

3. **AppRole authentication** — Know that AppRole is Vault's CI/CD authentication method. The pipeline authenticates with a role ID and secret ID to receive a Vault token, which is then used to retrieve actual secrets.

4. **Dynamic secrets** — Know what dynamic secrets are: Vault generates unique, time-limited credentials per request. Know that this limits exposure because each credential expires automatically and is never reused.

5. **OIDC federation** — Know that OIDC federation lets CI/CD pipelines authenticate to cloud providers (AWS, GCP, Azure) without storing long-lived credentials. GitHub Actions uses `permissions: id-token: write` to enable OIDC token issuance.

6. **AWS Secrets Manager rotation** — Know that AWS Secrets Manager supports automatic rotation for RDS, Redshift, and DocumentDB using built-in rotation Lambda functions. Custom rotation is via your own Lambda.

7. **Layer persistence** — Know that secrets passed to Docker `RUN` commands are permanently in the image layer even if deleted. The fix is BuildKit `--mount=type=secret`, which provides the secret to the build step without storing it in any layer.

8. **Masked CI variables** — Know that CI/CD platform secrets (GitHub Secrets, GitLab masked variables) are encrypted at rest and masked in logs, but they are static — they do not rotate automatically and do not provide audit logging per access.

---

## Section 9: Required Reading

- Review the OWASP Secrets Management Cheat Sheet at [https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).

---

## Section 10: Study Checklist

- [ ] Name and explain the three primary secrets failure modes.
- [ ] Explain what Gitleaks does and why `fetch-depth: 0` is required.
- [ ] Describe Vault AppRole authentication: what is the role ID, what is the secret ID, and what does the pipeline do with them.
- [ ] Explain what dynamic secrets are and why they reduce exposure risk compared to static secrets.
- [ ] Explain what OIDC federation is and why it eliminates long-lived credentials in CI pipelines.
- [ ] Identify two differences between HashiCorp Vault and AWS Secrets Manager.
- [ ] Explain why secrets in Docker image layers persist even after deletion in a subsequent layer.
- [ ] Describe the BuildKit `--mount=type=secret` pattern and when to use it.
- [ ] Review the OWASP Secrets Management Cheat Sheet at [https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).
- [ ] Complete the Module 09 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.

---

## 9. Supplemental Resources

**1. [HashiCorp Vault documentation — getting started and secrets engines](https://developer.hashicorp.com/vault/docs)**
The official Vault documentation covering all authentication methods, secrets engines (KV, database, AWS, PKI), policies, audit logging, and dynamic secrets. Essential reference for all hands-on Vault configuration tasks in this module.

**2. [AWS Secrets Manager developer guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)**
Official AWS documentation covering secret creation, automatic rotation with Lambda, OIDC-based IAM role access, cross-account access, and cost model. Includes worked examples for RDS credential rotation and ECS task role integration.

**3. [GitHub Actions — using secrets and OIDC with cloud providers](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)**
GitHub's guide to secrets management in Actions, covering secret scoping (repository, environment, organization), OIDC federation setup for AWS and Azure, secret masking in logs, and security hardening recommendations.

---

Reading Guide — Module 09 | CIS-4350 | Texas Wesleyan University | Professor Nash
