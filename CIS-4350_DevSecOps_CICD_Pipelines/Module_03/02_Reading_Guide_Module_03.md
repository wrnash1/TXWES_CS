# Reading Guide: Module 03 — Continuous Integration and Security Gates

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Describe the five-layer CI pipeline architecture and the role of each layer
- Write GitHub Actions and GitLab CI pipeline configurations with security stages
- Differentiate build trigger strategies for feature branches vs. pull requests vs. releases
- Configure SAST and dependency scanning quality gates with CVSS thresholds
- Protect pipeline configuration files using CODEOWNERS and reusable workflows
- Explain the security risks of unprotected pipeline-as-code files

---

## Section 1 — CI Pipeline Architecture

### 1.1 The Five Pipeline Layers

| Layer | Jobs | Failure Impact |
|---|---|---|
| Source | Checkout, credential validation | Pipeline does not start |
| Build | Compile, package, install deps | Downstream layers cannot run |
| Test | Unit tests, integration tests | Code logic errors caught |
| Scan | SAST, dependency scan, secrets scan, container scan | Security gate — blocks on findings |
| Report | SARIF upload, badge update, metrics | Non-blocking — informational |

### 1.2 Job Parallelism Design

Security scans can run in parallel with tests to minimize total pipeline time:

```text
checkout
    ├── unit-tests          (parallel)
    ├── sast-scan           (parallel)
    ├── secrets-scan        (parallel)
    └── dependency-scan     (parallel)
        └── container-build (needs: unit-tests)
            └── image-scan  (needs: container-build)
```

### 1.3 Pipeline Failure Semantics

When any job in a required path fails, all downstream jobs that `need` it are automatically skipped or cancelled. This is the enforcement mechanism for security gates — a SAST failure prevents the container from being built and pushed.

---

## Section 2 — GitHub Actions Deep Dive

### 2.1 Workflow Syntax Reference

| Element | Purpose | Example |
|---|---|---|
| `on` | Trigger events | `push`, `pull_request`, `schedule` |
| `jobs` | Parallel execution units | `build:`, `scan:` |
| `needs` | Job dependency chain | `needs: [build, test]` |
| `runs-on` | Runner OS | `ubuntu-latest`, `windows-latest` |
| `uses` | Reference a reusable action or workflow | `actions/checkout@v4` |
| `run` | Shell command | `pip install -r requirements.txt` |
| `env` | Job-level environment variables | `PYTHON_VERSION: "3.12"` |
| `secrets` | Reference GitHub Secrets | `${{ secrets.SNYK_TOKEN }}` |
| `if` | Conditional job execution | `if: github.ref == 'refs/heads/main'` |
| `continue-on-error` | Allow job to fail without failing workflow | `continue-on-error: true` |
| `permissions` | Restrict GITHUB_TOKEN scope | `contents: read` |

### 2.2 Security-Hardened Workflow Template

```yaml
name: Secure CI — Hardened

on:
  pull_request:
    branches: [main]

# Minimal permissions by default
permissions:
  contents: read
  security-events: write

jobs:
  sast:
    name: SAST — Semgrep
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - name: Checkout at PR head (not merge commit)
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}

      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/owasp-top-ten
            p/python
          generateSarif: "1"

      - name: Upload SARIF to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: semgrep.sarif
```

### 2.3 Pinning Action Versions

Always pin actions to a specific commit SHA for supply chain security, not just a version tag (tags are mutable):

```yaml
# Insecure — tag is mutable
- uses: actions/checkout@v4

# Secure — pinned to immutable SHA
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
```

For audit purposes, use a tool like `pin-github-action` or Dependabot's `github-actions` ecosystem to automate SHA pinning and updates.

### 2.4 Reusable Workflows for Centralized Security Gates

```yaml
# .github/workflows/security-gates.yml (in org/security-workflows repo)
on:
  workflow_call:
    inputs:
      fail-on-severity:
        required: false
        type: string
        default: "HIGH,CRITICAL"

jobs:
  semgrep:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
        with:
          config: p/owasp-top-ten

  dependency-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dependency-check/Dependency-Check_Action@main
        with:
          project: app
          path: .
          format: SARIF
          args: --failOnCVSS 7
```

Teams consume it:

```yaml
# In each team's repo
jobs:
  security:
    uses: org/security-workflows/.github/workflows/security-gates.yml@main
    secrets: inherit
```

---

## Section 3 — GitLab CI Deep Dive

### 3.1 GitLab CI Syntax Reference

| Element | Purpose |
|---|---|
| `stages` | Ordered list of pipeline stages |
| `image` | Docker image for the job |
| `script` | Shell commands to execute |
| `only` / `rules` | Conditions for job execution |
| `artifacts` | Files persisted between stages |
| `cache` | Files cached between pipeline runs |
| `include` | Import external YAML templates |
| `needs` | DAG-style job dependencies (bypass stage ordering) |
| `variables` | CI/CD variables |
| `environment` | Deployment target |

### 3.2 Built-in Security Templates

GitLab provides pre-built security templates in the Auto DevOps template library:

| Template | Tools Included |
|---|---|
| `Security/SAST.gitlab-ci.yml` | Bandit (Python), Brakeman (Ruby), ESLint Security (JS), Semgrep |
| `Security/Dependency-Scanning.gitlab-ci.yml` | Gemnasium, retire.js, bundler-audit |
| `Security/Secret-Detection.gitlab-ci.yml` | Gitleaks |
| `Security/Container-Scanning.gitlab-ci.yml` | Trivy |
| `Security/DAST.gitlab-ci.yml` | OWASP ZAP |

### 3.3 GitLab Security Dashboard

GitLab Ultimate includes a Security Dashboard that aggregates findings from all pipeline scans across projects. It supports:

- Vulnerability management workflows (triage, dismiss, create issue)
- Compliance dashboards for audit evidence
- Merge request security widget showing new findings introduced by the branch

---

## Section 4 — Build Triggers and Their Security Implications

### 4.1 Trigger Strategy by Branch Type

| Trigger | Scan Scope | Target Duration | Gate Strictness |
|---|---|---|---|
| Push to feature branch | Secrets scan, fast SAST (changed files) | < 5 min | Warn on Medium, fail on Critical |
| Pull request to main | Full SAST, dep scan, secrets, license | < 15 min | Fail on High+Critical |
| Push to main | Full scan + container build/scan | < 20 min | Fail on High+Critical |
| Release tag | All scans + SBOM + signing | < 30 min | Fail on any severity |
| Scheduled (nightly) | DAST, supply chain, license audit | No limit | Report only |

### 4.2 Pull Request Security Event

The most important trigger is the pull request. GitHub Actions supports:

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
    branches: [main, develop]
```

The `synchronize` type triggers on every new commit pushed to the PR branch, ensuring re-scanning when code changes.

---

## Section 5 — Security Quality Gates

### 5.1 CVSS Score Reference

| CVSS Score | Severity | Typical Gate Action |
|---|---|---|
| 9.0–10.0 | Critical | Always fail pipeline |
| 7.0–8.9 | High | Fail pipeline (mature orgs) |
| 4.0–6.9 | Medium | Warn; fail after grace period |
| 0.1–3.9 | Low | Informational only |
| 0.0 | None | No action |

### 5.2 Phased Quality Gate Adoption

Start with Critical only to establish the gate without overwhelming teams:

- Phase 1 (Month 1–2): Fail on CVSS 9.0+ (Critical only)
- Phase 2 (Month 3–4): Fail on CVSS 7.0+ (High and Critical)
- Phase 3 (Month 5–6): Warn on CVSS 4.0+ (Medium), fail on 7.0+
- Phase 4 (Month 7+): Full compliance — fail on any unexcepted finding

### 5.3 SARIF — Standard Output Format

Static Analysis Results Interchange Format (SARIF) is the JSON schema standard for security tool output. GitHub and GitLab both consume SARIF files to populate their Security tabs.

```json
{
  "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
  "version": "2.1.0",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "Semgrep",
          "version": "1.x"
        }
      },
      "results": [
        {
          "ruleId": "python.flask.security.injection.tainted-sql-string",
          "level": "error",
          "message": { "text": "Possible SQL injection via string concatenation" },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": { "uri": "app/db.py" },
                "region": { "startLine": 42 }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Section 6 — Pipeline Security

### 6.1 Protecting Pipeline Configuration

| Risk | Control |
|---|---|
| Developer edits pipeline to disable security gates | CODEOWNERS + required review for `.github/workflows/` |
| Malicious pull request executes arbitrary code | Use `pull_request_target` only with care; restrict `secrets` access |
| Third-party action supply chain attack | Pin actions to commit SHA; audit new actions |
| Exposed secrets in pipeline logs | Never `echo` secrets; use `::add-mask::` for dynamic values |
| Overly permissive GITHUB_TOKEN | Set `permissions: contents: read` at workflow level; override per-job |

### 6.2 Secrets in Pipelines

```yaml
# Never do this
- run: snyk test --token=abc123def456

# Correct — reference from secrets store
- run: snyk test
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

### 6.3 Environment Protection Rules

For deployment jobs, use GitHub Environments with protection rules:

- Required reviewers: one or more people must approve the deployment
- Wait timer: minimum delay before deployment runs
- Deployment branches: restrict which branches can deploy

---

## Exam Tips for DSOE Certification

- Know the five pipeline layers and what security activities belong in each.
- GitHub Actions jobs run in parallel by default within a workflow; use `needs` for sequencing.
- GitLab CI stages are sequential; jobs within a stage are parallel.
- SARIF is the standard output format for security tools — know what it is and why it matters.
- Quality gates: fail on CVSS 9.0+ Critical minimum; mature orgs extend to 7.0+ High.
- Action version pinning to SHA prevents supply chain attacks on CI pipelines.
- Reusable workflows centralize security enforcement and prevent gate bypass.
- `GITHUB_TOKEN` permissions should follow least-privilege — set `permissions: contents: read` by default.
- CODEOWNERS + branch protection prevents developers from disabling security gates in pipeline YAML.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| CI Pipeline | Automated sequence of jobs triggered by code changes |
| Quality Gate | Policy-enforced threshold that blocks pipeline on failing checks |
| SARIF | Static Analysis Results Interchange Format — JSON standard for tool output |
| GitHub Actions | Native CI/CD platform for GitHub; workflows in `.github/workflows/` |
| GitLab CI | Native CI/CD for GitLab; configuration in `.gitlab-ci.yml` |
| Reusable Workflow | GitHub Actions workflow callable from other repositories |
| GITHUB_TOKEN | Auto-generated short-lived token scoped to the current repository |
| Build Trigger | Event that initiates a pipeline run |
| CVSS | Common Vulnerability Scoring System — 0–10 severity scale |
| Pipeline as Code | CI/CD configuration stored in version control |

---

## 9. Supplemental Resources

**1. [GitHub Actions security hardening guide](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)**
Official GitHub documentation on hardening CI workflows, covering GITHUB_TOKEN scoping, SHA pinning, `pull_request_target` risks, environment protection rules, and reusable workflow security. Essential reference for the pipeline security section of this module.

**2. [OWASP Dependency-Check documentation](https://jeremylong.github.io/DependencyCheck/)**
Comprehensive documentation for the OWASP Dependency-Check tool, including Maven/Gradle plugins, CLI usage, CVSS threshold configuration, suppression files, and report format options (HTML, JSON, SARIF).

**3. [SARIF specification and tooling — Microsoft SARIF SDK](https://github.com/microsoft/sarif-sdk)**
The SARIF (Static Analysis Results Interchange Format) specification and reference implementation. Explains the JSON schema used by all major security scanning tools to produce standardized output consumed by GitHub, GitLab, and Azure DevOps security dashboards.

---

Reading Guide — Module 03 | CIS-4350 | Texas Wesleyan University | Professor Nash
