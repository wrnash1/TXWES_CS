# Video Script: Module 08 - SCA: Software Composition Analysis and Dependency Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 08 — SCA: Software Composition Analysis and Dependency Scanning"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. We have covered SAST and DAST for first-party application code. Now we're going to cover SCA — Software Composition Analysis — which addresses a different but equally critical risk: the open-source dependencies your application depends on.

Modern applications are largely assembled from open-source components. A Python web service might import 200 packages. A Node.js app might have 1,000 transitive dependencies. Every one of those packages is a potential vulnerability source. By the end of this video you will understand what SCA is, how dependency graphs and transitive dependencies work, how to use Snyk and OWASP Dependency-Check in pipelines, and how to interpret and remediate CVE findings in dependencies."

---

### [01:30 - 06:00] The Dependency Risk Landscape

**Visual:** npm dependency tree visualization — 5 direct dependencies, 127 transitive

**Audio:**

"Let's start with why dependencies are a major security concern. When you `pip install flask` or `npm install express`, you get not just Flask or Express — you get their entire dependency trees. Flask depends on Jinja2, which depends on MarkupSafe. Express depends on dozens of packages, which depend on dozens more. These transitive dependencies — packages your dependencies depend on — are ones you never explicitly chose and may not even know exist in your project.

The Log4Shell vulnerability in December 2021 — CVE-2021-44228 — is the canonical example of why this matters. Log4j was a Java logging library used as a transitive dependency by thousands of enterprise applications. Most application developers had no idea they were running Log4j. When the vulnerability was announced, organizations scrambled to audit millions of applications to determine exposure. Many could not answer the question 'do we use Log4j?' quickly because they had no SCA tooling.

SCA solves this. SCA tools build a complete Software Bill of Materials (SBOM) — an inventory of every direct and transitive dependency in your application — and check each component against vulnerability databases like the National Vulnerability Database (NVD), the GitHub Advisory Database, and vendor-specific advisories. When a new CVE is published, the SCA tool can immediately identify which of your applications are affected."

---

### [06:00 - 12:00] SCA Tools: Snyk and OWASP Dependency-Check

**Visual:** Snyk scan output showing a CRITICAL CVE finding

**Audio:**

"The two SCA tools you need to know for the DevSecOps Professional exam are Snyk and OWASP Dependency-Check.

**Snyk** is a commercial SCA platform (with a free tier) that scans package manifests (`package.json`, `requirements.txt`, `pom.xml`, `Gemfile.lock`) against its vulnerability database. Snyk provides remediation guidance — not just 'this package has a CVE' but 'upgrade from version 2.1.3 to 2.1.4 to remediate this CVE, and here are the patch notes.' Snyk integrates with GitHub as a pull request check, automatically opening PRs to update vulnerable dependencies.

**[SHOW CODE]**

Installing and running Snyk:

```bash
# Install Snyk CLI
npm install -g snyk

# Authenticate
snyk auth

# Test for vulnerabilities in current project
snyk test

# Test and fail if any HIGH or CRITICAL issues found
snyk test --severity-threshold=high

# Monitor the project for new vulnerabilities
snyk monitor
```

`snyk test` exits non-zero when vulnerabilities at or above the threshold are found — making it a pipeline gate.

`snyk monitor` sends the current dependency snapshot to Snyk's platform, enabling continuous monitoring: when a new CVE is published that affects one of your snapshots, Snyk sends an alert even without a new deployment.

**OWASP Dependency-Check** is a free, open-source tool that scans a project's build artifacts and dependency manifests against the NVD. It is configured via the `dependency-check-maven` plugin, `dependency-check-gradle` plugin, or as a standalone CLI.

**[SHOW CODE]**

Running OWASP Dependency-Check via the standalone script:

```bash
dependency-check.sh \
  --project myapp \
  --scan ./lib \
  --format HTML \
  --format JSON \
  --out ./reports \
  --failOnCVSS 7
```

`--failOnCVSS 7` causes the tool to exit non-zero if any CVE with a CVSS score of 7.0 or higher is found — this covers HIGH and CRITICAL severity CVEs."

---

### [12:00 - 17:00] Integrating SCA into the CI/CD Pipeline

**Visual:** GitHub Actions pipeline YAML with SCA job highlighted

**Audio:**

"SCA runs at the build stage — after the package manager downloads dependencies, but before the artifact is built. This is the right placement because dependencies are fully resolved at this stage, giving SCA the complete dependency graph to scan.

**[SHOW CODE]**

Here is a GitHub Actions SCA job using Snyk:

```yaml
sca-scan:
  name: Dependency Vulnerability Scan
  runs-on: ubuntu-latest
  needs: build
  steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run Snyk SCA scan
      uses: snyk/actions/python@master
      continue-on-error: true
      env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      with:
        args: --severity-threshold=high

    - name: Upload Snyk results to GitHub Code Scanning
      uses: github/codeql-action/upload-sarif@v3
      with:
        sarif_file: snyk.sarif
```

And here is the equivalent using OWASP Dependency-Check:

```yaml
sca-owasp:
  name: OWASP Dependency Check
  runs-on: ubuntu-latest
  needs: build
  steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Run OWASP Dependency-Check
      uses: dependency-check/Dependency-Check_Action@main
      with:
        project: 'myapp'
        path: '.'
        format: 'SARIF'
        out: 'reports'
        args: >
          --failOnCVSS 7
          --enableRetired

    - name: Upload Dependency-Check results
      uses: github/codeql-action/upload-sarif@v3
      with:
        sarif_file: reports/dependency-check-report.sarif
```

A few notes on the design. `--enableRetired` flags deprecated packages that may not have CVEs yet but are no longer receiving security updates — important for proactive dependency hygiene. SARIF upload to GitHub Code Scanning integrates findings into the Security tab alongside SAST results."

---

### [17:00 - 20:30] CVE Triage and SBOM

**Visual:** CVSS score breakdown diagram and SBOM excerpt

**Audio:**

"When SCA finds vulnerabilities, you need a process for triaging them. Not every CVE requires immediate action.

CVSS — Common Vulnerability Scoring System — provides a 0-10 severity score. CVEs with CVSS 9.0+ are Critical; 7.0-8.9 are High; 4.0-6.9 are Medium; 0-3.9 are Low. Critical and High findings should be remediated within defined SLAs — typically 24-72 hours for Critical, 7-14 days for High.

The key triage question for each finding: is this vulnerability actually reachable? A CVE in a library you depend on may be in a code path you never call. If you use only the email-sending function of a package and the CVE is in its image-processing code, the vulnerability may not be reachable in your application. Snyk and some other tools provide reachability analysis to help with this.

SBOM — Software Bill of Materials — is a machine-readable inventory of every component in your application, including name, version, license, and known vulnerabilities. CycloneDX and SPDX are the two standard SBOM formats. Generating an SBOM is increasingly required for regulated industries and government software procurement. Snyk and OWASP Dependency-Check both support CycloneDX SBOM generation."

---

### [20:30 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know that SCA scans third-party dependencies at the build stage. Know Snyk and OWASP Dependency-Check as the primary SCA tools. Know that `snyk test --severity-threshold=high` and `--failOnCVSS 7` are the pipeline gate configurations. Know what transitive dependencies are and why they are a risk. Know SBOM as the machine-readable dependency inventory and CycloneDX as a standard format. Know that Log4Shell is the canonical example of why SCA matters. See you in Module 09."
