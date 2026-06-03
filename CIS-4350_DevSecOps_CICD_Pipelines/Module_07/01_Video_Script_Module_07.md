# Video Script: Module 07 — Application Security Testing in CI/CD

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–1:30)

[SLIDE: Module 07 title card]

Welcome to Module 07. This module is where shift-left security becomes most concrete: we're testing the application itself — its source code, its running behavior, and its dependencies. We'll cover four major disciplines: Static Application Security Testing with SonarQube and Semgrep, Dynamic Application Security Testing with OWASP ZAP in pipelines, dependency scanning with OWASP Dependency-Check, and SBOM generation.

By the end of this module you'll understand the difference between SAST and DAST, be able to configure both in a CI pipeline, run dependency scans with quality gates, and generate a Software Bill of Materials for your application.

---

### SEGMENT 2 — SAST: Static Application Security Testing (1:30–6:30)

[SLIDE: SAST tool flow diagram — source code in, findings out]

SAST analyzes source code, bytecode, or binary code without executing it. The tool reads the code and looks for patterns that match known vulnerability signatures. Because SAST doesn't run the application, it can be integrated very early — before the application can even be built.

Two leading open-source SAST tools:

SonarQube is a full-featured code quality and security platform. It runs as a server with a web UI, stores historical scan results, tracks vulnerability trends over time, and enforces Quality Gates — policies that must pass before code can be merged.

```bash
# Run SonarQube scanner
sonar-scanner \
  -Dsonar.projectKey=myapp \
  -Dsonar.sources=src/ \
  -Dsonar.host.url=http://sonarqube:9000 \
  -Dsonar.token=$SONAR_TOKEN
```

In GitHub Actions:

```yaml
- name: SonarQube Scan
  uses: SonarSource/sonarqube-scan-action@master
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
```

SonarQube's Quality Gate is what makes it a blocking gate in CI. When the Quality Gate condition fails — for example, when a new Critical vulnerability is introduced — the pipeline fails. The default Quality Gate fails on any new Security Hotspot or Vulnerability with severity Blocker or Critical.

Semgrep is a lightweight, fast SAST engine that uses pattern-based rules written in a simple YAML format. It's extremely developer-friendly because rules are easy to read and write.

```yaml
# Custom Semgrep rule: detect SQL string concatenation
rules:
  - id: sql-string-concat
    patterns:
      - pattern: $QUERY = "..." + $INPUT
      - pattern: cursor.execute($QUERY)
    message: Possible SQL injection via string concatenation in $QUERY
    languages: [python]
    severity: ERROR
    metadata:
      cwe: "CWE-89"
      owasp: "A03:2021"
```

```bash
# Run Semgrep with OWASP Top 10 rule set
semgrep --config p/owasp-top-ten --sarif > semgrep.sarif

# Run with auto-detect language rules
semgrep --config auto --error .
```

The key difference between SonarQube and Semgrep: SonarQube is a platform that tracks trends and enforces gates across many projects over time. Semgrep is a scanning engine optimized for fast, per-commit feedback. They complement each other — many organizations use both.

---

### SEGMENT 3 — DAST: Dynamic Application Security Testing (6:30–11:00)

[SLIDE: DAST scan flow — running app, scanner, findings]

DAST tests a running application by sending HTTP requests and analyzing responses. Unlike SAST, DAST detects runtime vulnerabilities — issues that only appear when the application is actually processing input, such as reflected XSS, CSRF token bypass, or authentication flaws.

OWASP ZAP (Zed Attack Proxy) is the most widely used open-source DAST tool. It acts as an intercepting proxy and scanner. In a DevSecOps pipeline, ZAP runs in three modes:

Baseline scan: A quick passive scan that flags obvious issues without active attack. Runs in about 2 minutes. Safe for production-adjacent environments.

Full scan: Active scanning with attack payloads. Finds deeper vulnerabilities but takes longer and is not safe for production (it sends attack traffic).

API scan: Scans REST or GraphQL APIs using an OpenAPI/Swagger specification.

```yaml
# GitHub Actions — OWASP ZAP baseline scan
- name: ZAP Baseline Scan
  uses: zaproxy/action-baseline@v0.12.0
  with:
    target: https://staging.myapp.com
    rules_file_name: zap-rules.tsv
    cmd_options: '-a'
    fail_action: true
```

The `fail_action: true` flag makes the pipeline fail when ZAP finds MEDIUM or higher severity issues.

For API scanning with an OpenAPI spec:

```yaml
- name: ZAP API Scan
  uses: zaproxy/action-api-scan@v0.7.0
  with:
    target: https://staging.myapp.com/api/v1/openapi.json
    format: openapi
    fail_action: true
    cmd_options: '-a -j'
```

Important consideration: DAST requires a running application. This means DAST runs later in the pipeline than SAST — typically against a deployed staging environment. The pipeline pattern is:

```text
Code push → SAST (fast, no running app) → Build → Deploy to staging → DAST → Results
```

DAST also requires careful scoping. Attack payloads sent by ZAP should never reach production databases. Always point DAST at an isolated staging environment with disposable test data.

---

### SEGMENT 4 — Dependency Scanning with OWASP Dependency-Check (11:00–14:30)

[SLIDE: Dependency tree with CVE annotations]

Modern applications use dozens or hundreds of open-source libraries. Each library is a potential vulnerability surface. Dependency scanning tools compare the libraries your application uses against known CVE databases — primarily the NVD (National Vulnerability Database) — and report which libraries have known vulnerabilities.

OWASP Dependency-Check is a free, widely-used tool maintained by OWASP. It analyzes your project's dependency manifests (package.json, requirements.txt, pom.xml, etc.) and generates a report.

```bash
# Run Dependency-Check locally
dependency-check.sh \
  --project myapp \
  --scan . \
  --format HTML \
  --format JSON \
  --failOnCVSS 7 \
  --out reports/

# In Docker
docker run --rm \
  -v "$(pwd):/src" \
  -v "$(pwd)/reports:/report" \
  owasp/dependency-check:latest \
  --project myapp \
  --scan /src \
  --format HTML JSON SARIF \
  --failOnCVSS 7 \
  --out /report
```

In GitHub Actions:

```yaml
- name: OWASP Dependency-Check
  uses: dependency-check/Dependency-Check_Action@main
  with:
    project: myapp
    path: .
    format: SARIF
    out: reports/
    args: --failOnCVSS 7 --enableRetired

- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v3
  if: always()
  with:
    sarif_file: reports/dependency-check-report.sarif
```

The `--failOnCVSS 7` flag causes Dependency-Check to exit with a non-zero code if any dependency has a CVSS score of 7.0 or higher, failing the pipeline.

The `--enableRetired` flag also flags dependencies that have been officially retired — no longer maintained — even if they don't have an active CVE. An unmaintained library is a latent risk.

---

### SEGMENT 5 — SBOM Generation (14:30–17:00)

[SLIDE: SBOM format comparison — SPDX vs. CycloneDX]

A Software Bill of Materials (SBOM) is a structured, machine-readable inventory of all software components in an application — including direct dependencies, transitive dependencies, OS packages, and their versions and licenses. The SBOM is the security equivalent of an ingredient label on food packaging.

SBOMs became a regulatory requirement in the United States following Executive Order 14028 (2021) which directed federal agencies and their software suppliers to provide SBOMs.

Two standard SBOM formats:

SPDX (Software Package Data Exchange) — developed by the Linux Foundation, widely supported, JSON or tag-value format.

CycloneDX — developed by OWASP, optimized for security use cases, JSON or XML format.

Syft is the leading open-source SBOM generation tool:

```bash
# Generate SBOM for a container image
syft myapp:v1.2.3 -o cyclonedx-json > sbom.json

# Generate SBOM for a directory
syft dir:. -o spdx-json > sbom-spdx.json

# Generate SBOM and scan immediately with Grype (vulnerability scanner)
syft myapp:v1.2.3 -o cyclonedx-json | \
  grype --add-cpes-if-none

# In GitHub Actions
- name: Generate SBOM with Syft
  uses: anchore/sbom-action@v0
  with:
    image: myapp:${{ github.sha }}
    format: cyclonedx-json
    output-file: sbom.json

- name: Upload SBOM as artifact
  uses: actions/upload-artifact@v4
  with:
    name: sbom-${{ github.sha }}
    path: sbom.json
```

SBOMs should be generated and stored for every release. When a new CVE is published, you can query your SBOM archive to immediately determine which of your releases are affected without re-scanning every build.

---

### SEGMENT 6 — Integrating All Four Testing Types (17:00–20:00)

[SLIDE: Complete AppSec pipeline diagram]

A complete application security testing pipeline integrates all four types:

```yaml
name: Complete AppSec Pipeline

on:
  pull_request:
    branches: [main]

jobs:
  sast-semgrep:
    name: SAST — Semgrep
    runs-on: ubuntu-latest

  sast-sonarqube:
    name: SAST — SonarQube
    runs-on: ubuntu-latest

  dependency-scan:
    name: Dependency Scan — OWASP DC
    runs-on: ubuntu-latest

  build-and-push:
    name: Build Image
    runs-on: ubuntu-latest
    needs: [sast-semgrep, dependency-scan]

  dast-scan:
    name: DAST — OWASP ZAP
    runs-on: ubuntu-latest
    needs: build-and-push
    # Deploy to staging first, then scan

  sbom-generate:
    name: SBOM Generation — Syft
    runs-on: ubuntu-latest
    needs: build-and-push
```

Each type finds different classes of vulnerabilities:

- SAST finds code-level flaws: SQL injection, XSS in templates, insecure deserialization
- DAST finds runtime flaws: authentication bypass, session fixation, actual XSS in rendered output
- Dependency scan finds vulnerable libraries: Log4Shell, Spring4Shell, PyYAML code execution
- SBOM generation provides compliance evidence and enables future CVE triage

---

### SEGMENT 7 — Module Summary and Looking Ahead (20:00–22:00)

[SLIDE: Module 07 key takeaways]

Module 07 summary.

SAST analyzes source code without execution. SonarQube provides platform-level tracking and Quality Gates. Semgrep provides fast, pattern-based scanning with custom rule support.

DAST tests running applications. OWASP ZAP runs baseline (passive) and full (active) scans. In CI, always scan a staging environment, never production. Use `fail_action: true` to enforce the gate.

OWASP Dependency-Check scans library manifests against the NVD. Use `--failOnCVSS 7` for a High+ quality gate and `--enableRetired` to flag unmaintained libraries.

Syft generates SBOMs in CycloneDX or SPDX format. Store SBOMs with every release for future CVE triage.

In Module 08 we go deeper on the supply chain — SCA tools, SBOM formats, dependency confusion attacks, code signing, and the SLSA framework. See you there.

---

*[END OF SCRIPT — Module 07]*
