# Video Script: Module 03 — Continuous Integration and Security Gates

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–1:30)

[SLIDE: Module 03 title card]

Welcome to Module 03. We've secured our version control system — signed commits, branch protection, secrets scanning. Now the code is in the repository and it's time to build. In this module we focus on the CI pipeline: how it's structured, how to build it as code, and most importantly how to embed security gates that automatically block vulnerable code from advancing.

By the end of this module you'll be able to describe CI pipeline architecture, write pipeline configurations in GitHub Actions and GitLab CI YAML syntax, define build triggers, implement automated test stages, integrate security scanning tools as pipeline jobs, configure quality gates that fail the pipeline on security findings, and explain the concept of pipeline as code.

---

### SEGMENT 2 — CI Pipeline Architecture (1:30–5:00)

[SLIDE: CI pipeline stage diagram — Source, Build, Test, Scan, Report]

A Continuous Integration pipeline is a series of automated steps that execute every time code is pushed to the repository. The fundamental purpose: give developers fast feedback about whether their change broke anything — including security things.

The typical CI pipeline has five layers.

The first layer is Source. The pipeline triggers on a Git event: a push to main, a pull request opened, or a tag created. The pipeline checks out the code.

The second layer is Build. The application is compiled or packaged. For interpreted languages like Python or JavaScript, this stage may install dependencies and verify the project structure.

The third layer is Test. Automated unit tests, integration tests, and code coverage checks run here. A failing test fails the pipeline.

The fourth layer is Scan. This is where DevSecOps security gates live. SAST tools analyze source code. Dependency scanners check for known CVEs in third-party libraries. Container image scanners check the built Docker image.

The fifth layer is Report. Scan results are published to a security dashboard. SARIF files are uploaded to the platform's security tab. Badges and metrics are updated.

Pipeline jobs within each layer can run sequentially or in parallel. Security scans are often parallelized with unit tests to minimize total pipeline duration.

The key principle: if any stage fails — including a security scan — the pipeline is red and the code does not advance to the next stage. A pull request that fails a security gate cannot be merged.

---

### SEGMENT 3 — GitHub Actions Architecture (5:00–9:00)

[SLIDE: GitHub Actions workflow structure diagram]

GitHub Actions is the native CI/CD platform for GitHub repositories. Workflows are defined in YAML files under `.github/workflows/`. Let's look at the key concepts.

A workflow is the top-level unit. A workflow is triggered by one or more events.

A job is a collection of steps that runs on a single runner machine. Jobs in the same workflow can run in parallel or depend on each other using the `needs` keyword.

A step is an individual task — either a shell command or a reference to a reusable action from the GitHub Marketplace.

Here is a complete security-integrated pipeline:

```yaml
name: Secure CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: "3.12"

jobs:
  build-and-test:
    name: Build and Unit Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run unit tests
        run: pytest --tb=short --cov=src

  secrets-scan:
    name: Secrets Detection
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  sast-scan:
    name: SAST — Semgrep
    runs-on: ubuntu-latest
    needs: build-and-test
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
        with:
          config: p/owasp-top-ten

  dependency-scan:
    name: Dependency Vulnerability Scan
    runs-on: ubuntu-latest
    needs: build-and-test
    steps:
      - uses: actions/checkout@v4
      - name: Run OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: myapp
          path: .
          format: SARIF
          out: reports/
      - uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: reports/dependency-check-report.sarif
```

Notice several security-conscious design choices. The `actions/checkout@v4` action is pinned to a version tag. The `GITHUB_TOKEN` is used instead of a personal access token. SARIF output is uploaded to GitHub's Security tab for centralized visibility.

---

### SEGMENT 4 — GitLab CI Architecture (9:00–12:00)

[SLIDE: GitLab CI stage pipeline diagram]

GitLab CI uses a `.gitlab-ci.yml` file at the repository root. The key concepts are similar to GitHub Actions but with different terminology.

In GitLab CI, the stages array defines the order of pipeline stages. Jobs are grouped into stages. All jobs in a stage run in parallel; the next stage begins only after all jobs in the current stage pass.

```yaml
stages:
  - build
  - test
  - scan
  - report

variables:
  DOCKER_DRIVER: overlay2
  SAST_EXCLUDED_PATHS: tests/

include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
  - template: Security/Secret-Detection.gitlab-ci.yml

build-app:
  stage: build
  image: python:3.12-slim
  script:
    - pip install -r requirements.txt
    - python -m build
  artifacts:
    paths:
      - dist/

unit-tests:
  stage: test
  image: python:3.12-slim
  script:
    - pip install -r requirements.txt
    - pytest --tb=short --junitxml=report.xml
  artifacts:
    reports:
      junit: report.xml

semgrep-scan:
  stage: scan
  image: returntocorp/semgrep:latest
  script:
    - semgrep --config=p/owasp-top-ten --sarif > semgrep.sarif
  artifacts:
    reports:
      sast: semgrep.sarif
```

GitLab's built-in templates — `Security/SAST.gitlab-ci.yml`, `Security/Dependency-Scanning.gitlab-ci.yml`, `Security/Secret-Detection.gitlab-ci.yml` — automatically configure popular security tools with sensible defaults. Using these templates is the fastest way to add security scanning to a GitLab pipeline.

---

### SEGMENT 5 — Build Triggers and Security Implications (12:00–14:00)

[SLIDE: Build trigger types and when to use each]

Not all builds are equal. The trigger determines what security checks are appropriate.

Push to feature branch: Run fast checks — secrets scan, unit tests, SAST on changed files only. Feedback in under 5 minutes.

Pull request to main: Run the full security suite — secrets, SAST, dependency scan, license check. This is the critical gate before code enters main. Feedback in under 15 minutes.

Push to main: Full build plus container image build and scan. This is the production candidate.

Tag (release): Full build, all scans, SBOM generation, sign the artifact. This produces the deployable release.

Scheduled (nightly): Run more expensive checks — full DAST against staging, supply chain scanning, license compliance audit.

A common mistake is running the full security suite on every feature branch push. This creates a slow feedback loop that discourages developers. Use fast incremental scans on feature branches and reserve the full suite for pull requests to main.

---

### SEGMENT 6 — Security Quality Gates (14:00–17:30)

[SLIDE: Quality gate pass/fail flowchart]

A quality gate is a policy-enforced threshold that blocks pipeline progression when security standards are not met. Configuring quality gates correctly is one of the most important practical skills in DevSecOps.

For SAST quality gates, the standard configuration fails the pipeline on any Critical or High severity finding. Medium findings generate warnings but do not fail. Low and Informational findings are reported but do not block.

```yaml
# Semgrep quality gate — fail on critical/high
- name: Semgrep scan with quality gate
  run: |
    semgrep --config=p/owasp-top-ten \
      --severity ERROR \
      --error \
      --json > semgrep-results.json
    CRITICAL=$(jq '[.results[] | select(.extra.severity == "ERROR")] | length' semgrep-results.json)
    if [ "$CRITICAL" -gt 0 ]; then
      echo "FAILED: $CRITICAL critical findings"
      exit 1
    fi
```

For dependency scanning, use CVSS score thresholds. The OWASP Dependency-Check tool allows configuring a failure threshold:

```yaml
- name: Dependency-Check with CVSS gate
  uses: dependency-check/Dependency-Check_Action@main
  with:
    project: myapp
    path: .
    format: HTML
    args: >-
      --failOnCVSS 7
      --enableRetired
```

The `--failOnCVSS 7` argument fails the build if any dependency has a CVSS score of 7.0 or higher (High or Critical).

Quality gates must be tuned. Starting at CVSS 10 (Critical only) and progressively lowering the threshold over time as technical security debt is paid down is a practical adoption strategy.

---

### SEGMENT 7 — Pipeline as Code and Security of the Pipeline (17:30–20:30)

[SLIDE: Pipeline security — who can modify the pipeline?]

Pipeline as code means your CI/CD configuration lives in version control alongside the application code. This is good for auditability and reproducibility. But it creates a security question: who can modify the pipeline?

If any developer can edit `.github/workflows/` and merge it to main without review, they can effectively bypass security gates by editing the pipeline configuration. The solution is to protect pipeline configuration files using CODEOWNERS:

```gitignore
# CODEOWNERS
.github/workflows/   @org/devops-security-team
.gitlab-ci.yml       @org/devops-security-team
```

Additionally, use reusable workflows in GitHub Actions to centralize security scan jobs. Teams consume the central workflow rather than defining their own, preventing security gate bypasses:

```yaml
# Reusable workflow called by all teams
jobs:
  security-scan:
    uses: org/security-workflows/.github/workflows/security-gates.yml@main
    secrets: inherit
```

Pipeline secrets — API keys for scanning tools, registry credentials — must never be hardcoded in YAML. Use GitHub Secrets or GitLab CI/CD variables, and apply least-privilege scoping: secrets available only to specific jobs and branches.

---

### SEGMENT 8 — Module Summary and Looking Ahead (20:30–22:00)

[SLIDE: Module 03 key takeaways]

Let's recap Module 03.

CI pipelines are five layers: Source, Build, Test, Scan, Report. Security gates live in the Scan layer and must be configured to fail the pipeline on findings above a severity threshold.

GitHub Actions uses workflow YAML files in `.github/workflows/`. GitLab CI uses `.gitlab-ci.yml` with built-in security scan templates.

Build triggers should be tiered — fast incremental scans on feature branches, full security suites on pull requests to main.

Quality gates use CVSS thresholds and severity levels to block pipeline advancement. Start strict on Critical, progressively include High as your codebase matures.

Pipeline as code requires its own access controls — protect `.github/workflows/` with CODEOWNERS. Use reusable workflows for centralized security enforcement.

In Module 04 we move into container security — Dockerfile best practices, image scanning with Trivy, Docker Content Trust, and container registry security. See you there.

---

*[END OF SCRIPT — Module 03]*
