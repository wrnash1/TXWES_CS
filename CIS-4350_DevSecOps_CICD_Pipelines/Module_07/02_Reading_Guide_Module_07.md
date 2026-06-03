# Reading Guide: Module 07 — Application Security Testing in CI/CD

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Learning Objectives

After completing this reading guide, you will be able to:

- Explain the difference between SAST and DAST and describe what each finds
- Configure SonarQube Quality Gates and Semgrep rule sets in CI pipelines
- Run OWASP ZAP baseline and API scans in GitHub Actions against a staging environment
- Configure OWASP Dependency-Check with CVSS quality gates
- Generate SBOMs using Syft in CycloneDX and SPDX formats
- Design a complete application security testing pipeline integrating all four types

---

## Section 1 — SAST vs. DAST vs. SCA: What Each Finds

### 1.1 Testing Type Comparison

| Attribute | SAST | DAST | SCA / Dependency Scan |
|---|---|---|---|
| What is analyzed | Source code, bytecode | Running application | Dependency manifests and lock files |
| Application running? | No | Yes (required) | No |
| Pipeline timing | Early — before build | Late — after deploy to staging | Early — with or before build |
| Vulnerabilities found | Code logic flaws | Runtime behavior flaws | Known CVEs in libraries |
| False positive rate | Medium-high | Low-medium | Low |
| Language dependency | Yes — language-specific rules | No | Yes — ecosystem-specific |
| Example tool | Semgrep, SonarQube | OWASP ZAP | OWASP Dependency-Check |
| Finding example | SQL injection in db.py:42 | XSS via /search?q= parameter | requests==2.18.0 → CVE-2023-32681 |

### 1.2 Complementary Coverage

No single testing type finds all vulnerabilities:

- SAST finds the SQL injection but cannot tell if the parameterization bypass is exploitable through the running app's middleware
- DAST finds that `/login` is vulnerable to brute force but cannot trace it to the source code line
- SCA finds that PyYAML 5.3.1 has a code execution CVE but does not know if the vulnerable function is called

Use all three for defense in depth.

---

## Section 2 — SAST: SonarQube

### 2.1 SonarQube Architecture

| Component | Description |
|---|---|
| SonarQube Server | Web UI and backend for storing results, rules, and Quality Gates |
| Scanner | CLI tool that analyzes code and sends results to the server |
| Quality Gate | Policy defining conditions that must pass for a scan to succeed |
| Security Hotspot | Code pattern that may be a vulnerability — requires human review |
| Vulnerability | Confirmed security weakness with CVSS rating |

### 2.2 Quality Gate Configuration

```text
SonarQube Quality Gate: Default DevSecOps Gate

Condition 1: New Blocker Issues = 0
Condition 2: New Critical Issues = 0
Condition 3: New Security Hotspots Reviewed = 100%
Condition 4: Coverage on New Code >= 80%
Condition 5: New Duplications <= 3%
```

### 2.3 sonar-project.properties

```properties
sonar.projectKey=org_myapp
sonar.projectName=My Application
sonar.sources=src/
sonar.tests=tests/
sonar.python.coverage.reportPaths=coverage.xml
sonar.python.version=3.12
sonar.exclusions=**/migrations/**,**/fixtures/**
sonar.security.sources.jaas.loginConfig=
```

### 2.4 GitHub Actions Integration

```yaml
- name: SonarQube scan and Quality Gate check
  uses: SonarSource/sonarqube-scan-action@master
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}

- name: SonarQube Quality Gate check
  uses: SonarSource/sonarqube-quality-gate-action@master
  timeout-minutes: 5
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

The Quality Gate action polls SonarQube until the analysis is complete and then fails the pipeline if the gate fails.

---

## Section 3 — SAST: Semgrep

### 3.1 Semgrep Rule Sets

| Rule Set | Content | Use Case |
|---|---|---|
| `p/owasp-top-ten` | Rules covering all OWASP Top 10 categories | Baseline for all projects |
| `p/python` | Python-specific security and quality rules | Python projects |
| `p/flask` | Flask framework security rules | Flask web apps |
| `p/django` | Django-specific rules | Django apps |
| `p/javascript` | JavaScript security rules | Node.js, React |
| `p/java` | Java security rules | Spring Boot, Jakarta |
| `p/secrets` | Secret pattern detection | Any project |
| `auto` | Automatically selects rules for detected languages | Quick start |

### 3.2 Custom Semgrep Rules

```yaml
# .semgrep/custom_rules.yml
rules:
  - id: flask-debug-mode
    pattern: app.run(debug=True)
    message: Flask application is running with debug=True. Disable in production.
    languages: [python]
    severity: ERROR
    metadata:
      cwe: "CWE-94"
      owasp: "A05:2021"

  - id: hardcoded-secret-pattern
    patterns:
      - pattern: |
          $SECRET = "..."
      - metavariable-regex:
          metavariable: $SECRET
          regex: (?i)(password|secret|token|key|api_key)
    message: Possible hardcoded secret in variable $SECRET
    languages: [python, javascript, java]
    severity: WARNING
```

### 3.3 Semgrep with Inline Suppression

```python
def dangerous_function(user_input):
    query = "SELECT * FROM users WHERE id = " + user_input  # nosemgrep: sql-string-concat
    # nosemgrep is tracked in code review — document why it's acceptable
    cursor.execute(query)
```

---

## Section 4 — DAST: OWASP ZAP

### 4.1 ZAP Scan Modes Comparison

| Mode | Scan Type | Duration | Safe for Staging? | Safe for Production? |
|---|---|---|---|---|
| Baseline | Passive only | ~2 min | Yes | Yes (no attack traffic) |
| Full | Active attacks | 10–60 min | Yes | Never |
| API | Active against OpenAPI spec | 5–30 min | Yes | Never |

### 4.2 ZAP Rules File

The rules file customizes which alerts are treated as failures:

```text
# zap-rules.tsv
# Rule ID  Threshold (IGNORE/INFO/LOW/MEDIUM/HIGH)
10202       IGNORE    # Absence of Anti-CSRF Tokens (false positive in API)
10027       IGNORE    # Information Disclosure - Suspicious Comments
40029       HIGH      # CSRF
40018       HIGH      # SQL Injection
40012       HIGH      # Cross-Site Scripting (Reflected)
```

### 4.3 ZAP Context File for Authenticated Scanning

ZAP can scan authenticated pages by providing a session token:

```yaml
# zap-context.yml
contexts:
  - name: myapp-auth
    urls:
      - https://staging.myapp.com
    authentication:
      method: "bearer"
      parameters:
        loginUrl: "https://staging.myapp.com/api/auth/token"
        loginRequestBody: '{"username":"test@example.com","password":"testpass"}'
        tokenPath: "$.access_token"
    sessionTokens:
      - "Authorization"
```

---

## Section 5 — Dependency Scanning: OWASP Dependency-Check

### 5.1 Supported Ecosystems

| Ecosystem | File Analyzed |
|---|---|
| Python | requirements.txt, Pipfile.lock, setup.py |
| Node.js | package.json, package-lock.json, yarn.lock |
| Java | pom.xml, build.gradle, *.jar |
| Ruby | Gemfile.lock |
| .NET | .csproj, packages.config |
| Go | go.sum, go.mod |
| PHP | composer.lock |

### 5.2 Suppression File for False Positives

```xml
<!-- dependency-check-suppression.xml -->
<suppressions>
  <suppress>
    <notes>CVE-2021-44228 (Log4Shell) suppressed - we use logback, not log4j</notes>
    <cve>CVE-2021-44228</cve>
  </suppress>
  <suppress>
    <notes>False positive - this jaxb library version does not contain the vuln</notes>
    <packageUrl regex="true">^pkg:maven/com\.sun\.xml\.bind/.*$</packageUrl>
    <cve>CVE-2022-40152</cve>
  </suppress>
</suppressions>
```

---

## Section 6 — SBOM Generation and Use Cases

### 6.1 SBOM Format Comparison

| Attribute | SPDX | CycloneDX |
|---|---|---|
| Maintained by | Linux Foundation | OWASP |
| File formats | JSON, RDF, Tag-Value, YAML | JSON, XML, Protobuf |
| Security focus | Moderate — compliance origin | High — security use cases primary |
| License tracking | Excellent | Good |
| VEX support | Limited | Yes — Vulnerability Exploitability Exchange |
| Tool support | Broad | Broad + security-tool integrations |
| EO 14028 compliance | Yes | Yes |

### 6.2 Syft SBOM Generation

```bash
# Generate CycloneDX SBOM for a container image
syft myapp:v1.2.3 -o cyclonedx-json=sbom-cyclonedx.json

# Generate SPDX SBOM for source code
syft dir:. -o spdx-json=sbom-spdx.json

# Include license information
syft myapp:v1.2.3 -o cyclonedx-json --source-name myapp --source-version v1.2.3

# Scan SBOM for vulnerabilities immediately with Grype
grype sbom:sbom-cyclonedx.json
```

### 6.3 SBOM in the Release Workflow

```yaml
release-with-sbom:
  name: Release Artifact with SBOM
  runs-on: ubuntu-latest
  needs: [all-security-gates-passed]
  steps:
    - uses: actions/checkout@v4

    - name: Build and push image
      run: |
        docker build -t myapp:${{ github.ref_name }} .
        docker push myregistry.io/myapp:${{ github.ref_name }}

    - name: Generate SBOM
      uses: anchore/sbom-action@v0
      with:
        image: myregistry.io/myapp:${{ github.ref_name }}
        format: cyclonedx-json
        output-file: sbom-${{ github.ref_name }}.json

    - name: Attach SBOM to GitHub Release
      uses: softprops/action-gh-release@v2
      with:
        files: sbom-${{ github.ref_name }}.json
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## Exam Tips for DSOE Certification

- SAST does not require a running application; DAST does — this is the most tested distinction.
- SonarQube Quality Gate: the gate fails when conditions are violated; pipeline blocks on gate failure.
- Semgrep `nosemgrep` comment suppresses a finding — it must be documented and is tracked in Git history.
- OWASP ZAP baseline scan is passive (safe for production); full scan sends attack payloads (never run against production).
- OWASP Dependency-Check `--failOnCVSS 7` exits with non-zero code when CVSS >= 7.0 — required for CI gate.
- Syft generates SBOMs; Grype scans SBOMs for vulnerabilities. They are complementary tools from Anchore.
- SPDX is from Linux Foundation; CycloneDX is from OWASP — both satisfy EO 14028 requirements.
- CycloneDX supports VEX (Vulnerability Exploitability Exchange) — documents whether a vulnerability is actually exploitable.
- SBOM use case: when a new CVE is published, query stored SBOMs to find affected releases without re-scanning.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| SAST | Static Application Security Testing — analyzes source code without execution |
| DAST | Dynamic Application Security Testing — tests a running application |
| SonarQube | SAST platform with Quality Gates, vulnerability tracking, and code metrics |
| Semgrep | Pattern-based SAST engine with YAML rule format |
| Quality Gate | SonarQube policy that must pass for a build to be considered clean |
| OWASP ZAP | Open-source DAST tool; baseline and full scan modes |
| Baseline Scan | ZAP passive scan — no attack payloads; safe for production-adjacent environments |
| Full Scan | ZAP active scan — sends attack payloads; staging environments only |
| OWASP Dependency-Check | Free tool scanning dependency manifests against the NVD |
| SBOM | Software Bill of Materials — machine-readable inventory of all software components |
| Syft | Open-source SBOM generation tool supporting CycloneDX and SPDX |
| Grype | Open-source vulnerability scanner that consumes SBOMs |
| VEX | Vulnerability Exploitability Exchange — documents exploitability of CVEs in an SBOM |
| NVD | National Vulnerability Database — NIST-maintained CVE database |

---

Reading Guide — Module 07 | CIS-4350 | Texas Wesleyan University | Professor Nash
