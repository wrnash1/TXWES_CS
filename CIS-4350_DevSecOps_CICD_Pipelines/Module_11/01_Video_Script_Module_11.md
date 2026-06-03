# Video Script: Module 11 - Container Image Scanning: Trivy and Grype

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 11 — Container Image Scanning: Trivy and Grype"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. In Module 04 we covered Docker security — secure Dockerfiles, non-root users, minimal base images. That was about how you build the image. This module is about what you find after you build it.

Container images bundle your application code, its runtime, and the operating system packages that support it. Any of those layers can contain CVEs. An nginx base image from six months ago might have dozens of unpatched OS vulnerabilities. A Python package installed during build might have a critical CVE discovered last week. Container image scanning is the control that catches these. By the end of this video you will understand how Trivy and Grype work as container image scanners, how to integrate them into your CI/CD pipeline with exit code gating, and how to triage image scan findings effectively."

---

### [01:30 - 06:00] What Container Image Scanning Finds

**Visual:** Diagram showing image layers — OS base, language runtime, application packages

**Audio:**

"Container images are composed of layers. At the bottom is the OS base image — Alpine, Debian slim, UBI — which includes the OS kernel libraries and package manager. On top of that is the language runtime — Python 3.11, Node.js 20, the JDK. On top of that are the application dependencies installed by pip, npm, or Maven. On top of that are your application source files.

CVEs can exist at any of these layers. An old Alpine base image might have CVEs in musl libc. A Python 3.9 runtime might have CVEs in the standard library's ssl module. A Flask version from two years ago has known CVEs. Container image scanners build a complete inventory of every OS package and language package in every layer of the image and check each against vulnerability databases.

This is distinct from what SAST and SCA do. SAST scans your first-party source code. SCA scans your declared dependencies in `requirements.txt` or `package.json`. Container image scanning scans the full runtime artifact — every binary, library, and package that will actually execute in production. This includes packages that were installed as transitive dependencies of transitive dependencies and OS packages that came with the base image that you never explicitly chose.

The two primary container image scanners are Trivy (from Aqua Security) and Grype (from Anchore). Both are open-source, both are fast, and both have excellent GitHub Actions integrations."

---

### [06:00 - 12:00] Trivy

**Visual:** Trivy scan output against a Docker image

**Audio:**

"Trivy is a comprehensive vulnerability scanner from Aqua Security. It scans container images, filesystems, Git repositories, and Kubernetes clusters. For container images, it checks OS packages (Alpine apk, Debian apt, RHEL rpm) and language packages (Python pip, Node.js npm, Java Maven/Gradle, Ruby gems, Go modules, Rust crates).

**[SHOW CODE]**

```bash
# Install Trivy
brew install trivy

# Scan a local image
trivy image python:3.9-slim

# Scan a specific severity
trivy image --severity HIGH,CRITICAL python:3.9-slim

# Fail if HIGH or CRITICAL CVEs found (exit code 1)
trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest

# Output as SARIF
trivy image --format sarif --output trivy-results.sarif myapp:latest

# Scan and ignore unfixed vulnerabilities
trivy image --ignore-unfixed --exit-code 1 --severity HIGH,CRITICAL myapp:latest
```

The `--exit-code 1` flag is the pipeline gate: Trivy exits with code 1 if any CVE matching the severity filter is found. A non-zero exit code fails the GitHub Actions job.

`--ignore-unfixed` is an important flag for reducing noise. Many CVEs in OS packages do not have a patch available yet. These unfixed CVEs cannot be remediated by upgrading; they can only be addressed by switching to a different base image. `--ignore-unfixed` filters them out so the scan focuses on actionable findings.

Here is a complete GitHub Actions container scanning job:

```yaml
container-scan:
  name: Container Image Scan
  runs-on: ubuntu-latest
  needs: build
  steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Build container image
      run: docker build -t myapp:${{ github.sha }} .

    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: myapp:${{ github.sha }}
        format: sarif
        output: trivy-results.sarif
        exit-code: '1'
        severity: HIGH,CRITICAL
        ignore-unfixed: true

    - name: Upload Trivy results to GitHub Code Scanning
      uses: github/codeql-action/upload-sarif@v3
      if: always()
      with:
        sarif_file: trivy-results.sarif
```

Notice `needs: build` — the image must be built before it can be scanned. The `if: always()` on the SARIF upload ensures findings are uploaded to GitHub Code Scanning even when the scan fails the pipeline."

---

### [12:00 - 17:00] Grype

**Visual:** Grype scan output side-by-side with Trivy

**Audio:**

"Grype is Anchore's open-source container image and filesystem vulnerability scanner. Its strength is a clearly formatted output that shows the vulnerability, affected package, installed version, fixed version, and severity in a clean table.

**[SHOW CODE]**

```bash
# Install Grype
brew install grype

# Scan an image
grype python:3.9-slim

# Scan with severity threshold — fail on HIGH+
grype --fail-on high python:3.9-slim

# Scan a local tarball
grype docker-archive:myapp.tar

# Output as JSON
grype --output json --file grype-results.json myapp:latest

# Scan only fixed vulnerabilities
grype --only-fixed --fail-on high myapp:latest
```

The `--fail-on high` flag is Grype's equivalent of Trivy's `--exit-code 1 --severity HIGH,CRITICAL`. It exits with code 1 if any HIGH or CRITICAL CVE is found.

Grype also scans filesystem artifacts — not just Docker images. You can point it at a directory, a tarball, or even an OCI layout directory. This is useful for scanning build artifacts before they are containerized.

Here is a GitHub Actions job using Grype:

```yaml
grype-scan:
  name: Grype Container Scan
  runs-on: ubuntu-latest
  needs: build
  steps:
    - name: Build image
      run: docker build -t myapp:${{ github.sha }} .

    - name: Run Grype scan
      uses: anchore/scan-action@v3
      id: scan
      with:
        image: myapp:${{ github.sha }}
        fail-build: true
        severity-cutoff: high
        output-format: sarif

    - name: Upload Grype SARIF results
      uses: github/codeql-action/upload-sarif@v3
      if: always()
      with:
        sarif_file: ${{ steps.scan.outputs.sarif }}
```

For the exam, know both tools. Trivy is the more widely deployed, with broader ecosystem scanning beyond just containers. Grype is noted for its clear output format and `--only-fixed` filtering capability."

---

### [17:00 - 21:00] Triage and Remediation Strategy

**Visual:** CVE triage decision tree

**Audio:**

"When a container image scan produces findings, you need a triage process. Not all findings require the same response.

The first triage question: is there a fixed version available? If no fixed version exists for a CVE, you cannot remediate it by upgrading the package. `--ignore-unfixed` and `--only-fixed` filter these out.

If a fix exists, the next question is: what layer is the vulnerable package in? If the CVE is in an OS package from the base image, updating the base image tag resolves it. If the CVE is in an application dependency, updating the dependency version resolves it.

Base image currency is one of the most important container security practices. Using `FROM python:3.11-slim` pins to a specific minor version but gets the latest patch releases. Pinning to a specific digest is more reproducible but requires explicit updates. The DevSecOps pattern is to use Dependabot or a similar tool to automatically open PRs when base image updates are available.

For the CI/CD pipeline, the typical configuration is: fail the build on any CRITICAL finding. Fail the build on HIGH findings with a fixed version available. Report but do not fail on HIGH findings with no fix available — these go into the risk register. Report but do not fail on MEDIUM and LOW findings — track these in the next sprint's backlog.

This tiered approach prevents the pipeline from becoming blocked by findings that cannot be remediated, while still gating on findings that can and should be fixed."

---

### [21:00 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know Trivy and Grype as the two primary container image scanners. Know that Trivy uses `--exit-code 1` to gate the pipeline, and Grype uses `--fail-on high`. Know that `--ignore-unfixed` (Trivy) and `--only-fixed` (Grype) filter out CVEs with no available patch, reducing noise for actionable remediation. Know that container image scanning checks both OS packages and language packages in all image layers. Know that `needs: build` in GitHub Actions ensures the image is built before scanning. Know that Trivy has broader scanning beyond containers — it also scans filesystems, Git repositories, and Kubernetes clusters. See you in Module 12."
