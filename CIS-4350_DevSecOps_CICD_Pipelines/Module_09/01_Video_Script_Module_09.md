# Video Script: Module 09 - Secrets Management: HashiCorp Vault and AWS Secrets Manager

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 09 — Secrets Management: HashiCorp Vault and AWS Secrets Manager"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. We have covered scanning tools — SAST, DAST, and SCA — and the controls around containers and dependencies. Now we're going to cover a control area that cuts across every part of your pipeline: secrets management.

A secret is any credential that grants access to a system — API keys, database passwords, TLS certificates, SSH keys, tokens. If a secret is exposed in your source code, your pipeline logs, your container image, or your environment variables in plaintext, any attacker who can read those locations now has access to whatever that secret unlocks. By the end of this video you will understand what constitutes a secret, why secrets leak, how secrets scanners detect them, how HashiCorp Vault and AWS Secrets Manager work as solutions, and how to integrate secrets management correctly into your CI/CD pipeline."

---

### [01:30 - 06:00] The Secrets Leakage Problem

**Visual:** Slide showing secrets found in GitHub repositories with lines redacted

**Audio:**

"Let's start with why secrets management is such a persistent problem in software engineering. Developers are under time pressure. When a database connection needs a password, the fastest path is to hardcode it in the source file. When a CI job needs an API key, the fastest path is to paste it into the shell script. These patterns work immediately and do not require understanding any secrets management system. They also create catastrophic exposure risk.

Here is a concrete example. A developer commits this file:

**[SHOW CODE]**

```python
DB_PASSWORD = 'Sup3rS3cr3t!'
API_KEY = 'sk-proj-aaaaabbbbccccdddd'
AWS_SECRET_ACCESS_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
```

Even if the developer realizes the mistake immediately and removes it in the next commit, the secret is now permanently in the Git history. Anyone with repository access — or anyone who finds the public repository — can run `git log` and recover the secret from any prior commit.

The second failure mode is secrets in environment variables that are printed to pipeline logs. A developer debugging a failing build adds `env` or `printenv` to their pipeline job to see what is set. That command dumps every environment variable — including secrets injected into the build environment — to the pipeline log. If pipeline logs are accessible to all team members, all secrets are now readable by all team members.

The third failure mode is secrets baked into container images. A Dockerfile that runs `RUN pip install --extra-index-url https://user:password@internal.registry.example.com/pypi` includes the credential in the image layer history. Even if the final image does not have the credential in an obvious file, `docker history` and layer inspection tools reveal it.

Secrets management solutions address all three failure modes: secrets never enter source code, never appear in pipeline logs, and never are baked into container images."

---

### [06:00 - 12:00] Secrets Scanning: Gitleaks and GitHub Secret Scanning

**Visual:** Gitleaks output showing a detected API key

**Audio:**

"Before covering the solutions, let's cover the detective control: secrets scanning. Secrets scanners analyze repository history and new commits to detect credential-shaped strings using pattern libraries for known secret formats — AWS access keys follow a specific regex pattern, GitHub personal access tokens have a specific prefix, Stripe API keys have a specific format.

**Gitleaks** is an open-source secrets scanner commonly used in pre-commit hooks and CI pipelines. It scans the full Git history for known secret patterns, not just the current working tree.

**[SHOW CODE]**

```bash
# Install Gitleaks
brew install gitleaks

# Scan the current repository including full history
gitleaks detect --source . --verbose

# Scan only staged changes (pre-commit hook usage)
gitleaks protect --staged
```

To integrate Gitleaks in a pre-commit hook, add it to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks:
      - id: gitleaks
```

GitHub also provides built-in secret scanning at the repository level, which scans every push for known secret patterns from over 100 providers — AWS, Stripe, GitHub tokens, and others. When a match is found, GitHub alerts the repository owner and, for public repositories, notifies the secret's issuing partner so they can revoke the token automatically.

**[SHOW CODE]**

Here is a GitHub Actions secrets scanning job:

```yaml
secrets-scan:
  name: Secrets Scanning
  runs-on: ubuntu-latest
  steps:
    - name: Checkout code
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Run Gitleaks scan
      uses: gitleaks/gitleaks-action@v2
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

The `fetch-depth: 0` is critical here — without it, the shallow clone only checks recent commits and misses secrets committed earlier in the repository history."

---

### [12:00 - 17:30] HashiCorp Vault

**Visual:** Vault architecture diagram — agent, auth methods, secret engines

**Audio:**

"HashiCorp Vault is an open-source secrets management platform that provides a centralized store for secrets with access control, audit logging, and automatic rotation.

The key Vault concepts you need to understand are: secret engines, auth methods, policies, and dynamic secrets.

**Secret engines** are the storage and generation backends. The KV (Key-Value) secret engine stores static secrets as key-value pairs. The database secret engine dynamically generates database credentials on demand. The PKI secret engine generates X.509 certificates. The AWS secret engine generates temporary AWS IAM credentials.

**Auth methods** are how Vault verifies the identity of clients requesting secrets. GitHub auth validates GitHub personal access tokens. AppRole is used for CI/CD pipelines — the pipeline has a role ID and secret ID that together authenticate to Vault. Kubernetes auth lets pods authenticate using their service account JWT tokens.

**Policies** control which secrets an authenticated entity can read or write. This is Vault's RBAC system.

**[SHOW CODE]**

Here is how a CI/CD pipeline retrieves a secret from Vault:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Import secrets from Vault
        uses: hashicorp/vault-action@v3
        with:
          url: https://vault.company.internal:8200
          method: approle
          roleId: ${{ secrets.VAULT_ROLE_ID }}
          secretId: ${{ secrets.VAULT_SECRET_ID }}
          secrets: |
            secret/data/myapp/production db_password | DB_PASSWORD ;
            secret/data/myapp/production api_key | API_KEY

      - name: Deploy application
        run: ./deploy.sh
        env:
          DB_PASSWORD: ${{ env.DB_PASSWORD }}
          API_KEY: ${{ env.API_KEY }}
```

The secrets are fetched at runtime from Vault and injected as environment variables. They never appear in the pipeline YAML. The `VAULT_ROLE_ID` and `VAULT_SECRET_ID` stored in GitHub Secrets are not the actual application secrets — they are authentication credentials that Vault uses to issue the actual secrets.

**Dynamic secrets** are Vault's most powerful capability. Rather than storing a database password that any authorized client can retrieve indefinitely, Vault generates a unique, time-limited database credential for each request. The pipeline gets a credential valid for 1 hour. After the deployment, the credential expires and becomes unusable. If the credential is leaked, its exposure window is bounded."

---

### [17:30 - 21:00] AWS Secrets Manager

**Visual:** AWS Secrets Manager console with rotation diagram

**Audio:**

"AWS Secrets Manager is the managed secrets service in the AWS ecosystem. If your workloads run on AWS, Secrets Manager integrates natively with IAM, RDS, Lambda, and ECS.

The key features are: centralized secret storage, automatic rotation via Lambda functions, and fine-grained IAM access policies.

**[SHOW CODE]**

Retrieving a secret from AWS Secrets Manager in a Python application:

```python
import boto3
import json

def get_secret(secret_name: str, region: str = 'us-east-1') -> dict:
    client = boto3.client('secretsmanager', region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

db_creds = get_secret('myapp/production/database')
db_password = db_creds['password']
```

In GitHub Actions, AWS Secrets Manager integrates through the `aws-actions/aws-secretsmanager-get-secrets` action or directly through the AWS CLI after assuming an IAM role via OIDC federation:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - name: Configure AWS credentials via OIDC
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: us-east-1

      - name: Retrieve secrets
        uses: aws-actions/aws-secretsmanager-get-secrets@v2
        with:
          secret-ids: myapp/production/database

      - name: Deploy
        run: ./deploy.sh
```

OIDC federation means the pipeline authenticates to AWS using a short-lived JWT token issued by GitHub — no long-lived AWS access key credentials stored in GitHub Secrets at all. This is the recommended pattern for CI/CD systems running in cloud environments."

---

### [21:00 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know the three secrets failure modes — hardcoded in source, exposed in logs, baked into container images. Know Gitleaks as the secrets scanning tool and `fetch-depth: 0` as the required Git checkout option for full history scanning. Know that HashiCorp Vault uses AppRole authentication for CI/CD pipelines and that dynamic secrets generate time-limited credentials per request. Know that AWS Secrets Manager integrates with IAM and supports automatic rotation via Lambda. Know that OIDC federation eliminates the need for long-lived cloud credentials in CI pipelines. Know that secrets should never be in pipeline YAML files — they are injected at runtime from a secrets management system. See you in Module 10."
