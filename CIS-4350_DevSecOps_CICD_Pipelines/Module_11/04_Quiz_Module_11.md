# Quiz: Module 11 - Container Image Scanning: Trivy and Grype

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

What does container image scanning check that SCA (Software Composition Analysis) scanning does not?

- A) Container image scanning checks application source code for insecure coding patterns that SCA misses
- B) Container image scanning checks all OS packages in the base image layers in addition to language packages — SCA only scans declared application dependencies in manifest files
- C) Container image scanning checks for secrets and API keys embedded in environment variables, which SCA cannot detect
- D) Container image scanning checks the container runtime configuration (Dockerfile instructions) for security misconfigurations that SCA tools ignore

#### Q1 Correct Answer

B — SCA tools (Snyk, OWASP Dependency-Check) scan dependency manifests (`requirements.txt`, `package.json`) for application package CVEs. Container image scanning scans the complete image filesystem — every OS package installed by the base image and every language package present in any layer. OS packages from Alpine, Debian, or Ubuntu base images are invisible to SCA tools because they are not declared in application manifests.

#### Q1 Distractor Analysis

- *Why A is incorrect:* Container image scanning does not analyze source code for insecure patterns. SAST is the control for source code analysis. Image scanners check package versions against CVE databases.
- *Why C is incorrect:* Secrets scanning (Gitleaks, GitHub Secret Scanning) is the control for detecting credentials. Container image scanners detect package CVEs, not secrets.
- *Why D is incorrect:* Dockerfile instruction analysis is performed by Hadolint, a Dockerfile linter. Container image scanners examine the built artifact's package inventory, not the Dockerfile instructions.

---

### Question 2

Which Trivy CLI flag causes the pipeline to fail when HIGH or CRITICAL CVEs are found?

- A) `--fail-on HIGH,CRITICAL`
- B) `--severity HIGH,CRITICAL` alone, which automatically exits non-zero when matching CVEs are found
- C) `--exit-code 1` combined with `--severity HIGH,CRITICAL`
- D) `--block-on-severity HIGH,CRITICAL`

#### Q2 Correct Answer

C — `--exit-code 1` tells Trivy to exit with code 1 (non-zero) when vulnerabilities are found. Combined with `--severity HIGH,CRITICAL`, this limits the gate to only HIGH and CRITICAL findings. Without `--exit-code 1`, Trivy reports findings but exits with code 0, which does not fail the pipeline job.

#### Q2 Distractor Analysis

- *Why A is incorrect:* `--fail-on` is Grype's flag, not Trivy's. Trivy uses `--exit-code 1` for pipeline gating.
- *Why B is incorrect:* `--severity` alone only filters which severity levels appear in the output. It does not change the exit code behavior. Trivy still exits 0 unless `--exit-code 1` is explicitly set.
- *Why D is incorrect:* `--block-on-severity` is not a valid Trivy flag. The correct Trivy flag for pipeline gating is `--exit-code`.

---

### Question 3

What does `trivy image --ignore-unfixed` do, and why is it useful in a CI/CD pipeline?

- A) It ignores CVEs in packages that are not imported by the application source code, applying a form of reachability filtering
- B) It excludes CVEs for which no patched package version exists — these cannot be remediated by upgrading, so excluding them focuses the pipeline gate on actionable findings
- C) It ignores CVEs discovered in the last 30 days, giving the vendor time to release a patch before failing the build
- D) It ignores CVEs that are rated informational or LOW severity, equivalent to `--severity HIGH,CRITICAL`

#### Q3 Correct Answer

B — Many OS packages in base images have known CVEs that the OS vendor has not yet patched. These unfixed CVEs appear in scan output but cannot be remediated by upgrading the package — the only options are switching base images, accepting the risk, or waiting for a future patch. `--ignore-unfixed` removes these from the output and the exit code evaluation, focusing the pipeline gate on CVEs that can actually be fixed.

#### Q3 Distractor Analysis

- *Why A is incorrect:* `--ignore-unfixed` filters based on whether a fix exists in the vulnerability database, not based on code reachability. Reachability analysis is an SCA capability (Snyk paid tiers), not a Trivy container scanning feature.
- *Why C is incorrect:* `--ignore-unfixed` is not based on CVE publication date. It is based on whether a patched version of the affected package exists in the package repository.
- *Why D is incorrect:* `--ignore-unfixed` and `--severity` are independent filters. `--ignore-unfixed` can apply at any severity level — it filters based on fix availability, not severity.

---

### Question 4

Which Grype flag is the equivalent of Trivy's `--ignore-unfixed`?

- A) `--skip-unfixed`
- B) `--no-fix`
- C) `--only-fixed`
- D) `--fixable-only`

#### Q4 Correct Answer

C — `grype --only-fixed` limits output to CVEs for which a fixed package version is available. This is the Grype equivalent of `trivy --ignore-unfixed`. Both flags serve the same purpose: reducing pipeline noise by focusing the gate on actionable, remediable findings.

#### Q4 Distractor Analysis

- *Why A is incorrect:* `--skip-unfixed` is not a valid Grype flag. The correct Grype flag is `--only-fixed`.
- *Why B is incorrect:* `--no-fix` is not a valid Grype flag. Trivy and Grype use different naming conventions for this functionality.
- *Why D is incorrect:* `--fixable-only` is not a valid Grype flag. The correct flag is `--only-fixed`.

---

### Question 5

A GitHub Actions pipeline has the following container scan job structure. What is the security purpose of the `if: always()` condition on the SARIF upload step?

```yaml
- name: Run Trivy scan
  uses: aquasecurity/trivy-action@master
  with:
    exit-code: '1'
    severity: HIGH,CRITICAL

- name: Upload Trivy results to GitHub Code Scanning
  uses: github/codeql-action/upload-sarif@v3
  if: always()
  with:
    sarif_file: trivy-results.sarif
```

- A) `if: always()` prevents GitHub from marking the SARIF upload step as skipped when the workflow is cancelled
- B) `if: always()` ensures the SARIF results are uploaded to GitHub Code Scanning even when the Trivy step fails due to finding HIGH/CRITICAL CVEs — making findings visible in the PR Security tab regardless of build outcome
- C) `if: always()` makes the SARIF upload run before the Trivy scan to pre-register the report location with GitHub
- D) `if: always()` configures the SARIF upload to run on every branch, not just pull requests

#### Q5 Correct Answer

B — When Trivy exits with code 1 (due to `--exit-code 1` and finding HIGH/CRITICAL CVEs), GitHub Actions skips all subsequent steps in the job by default. `if: always()` overrides this behavior, ensuring the SARIF upload runs regardless of whether the Trivy step succeeded or failed. This is critical: if the scan fails, you still want the findings uploaded to GitHub Code Scanning so engineers can see them in the PR Security tab.

#### Q5 Distractor Analysis

- *Why A is incorrect:* While `if: always()` does run on cancellation, the primary security purpose here is ensuring findings are uploaded even when the scan step exits non-zero due to vulnerabilities.
- *Why C is incorrect:* `if: always()` controls when a step runs relative to prior step outcomes. It does not change the execution order — steps always run in declaration order.
- *Why D is incorrect:* `if: always()` controls execution based on prior step status, not based on branch name. Branch filtering is handled by `on:` trigger conditions.

---

### Question 6

A Trivy scan of a production container image reports this finding:

```text
CRITICAL  CVE-2023-44487  libssl1.1  1.1.1n-0+deb11u4  1.1.1w-0+deb11u1
```

What does this output tell you, and what is the remediation?

- A) The `libssl1.1` package has CRITICAL CVE-2023-44487; installed version is 1.1.1n-0+deb11u4; fixed in version 1.1.1w-0+deb11u1; remediate by updating the base image to one that ships 1.1.1w-0+deb11u1 or later
- B) The `libssl1.1` package has CRITICAL CVE-2023-44487; both versions shown are vulnerable; the fix requires a source code change in the application
- C) The `libssl1.1` package has CRITICAL CVE-2023-44487; the fixed version 1.1.1w-0+deb11u1 is the installed version; no remediation is needed
- D) The `libssl1.1` package has CRITICAL CVE-2023-44487; the version shown is from a custom package layer, not the base image; remediate by updating the Dockerfile

#### Q6 Correct Answer

A — The Trivy output columns are: severity, CVE ID, package name, installed version, fixed version. `libssl1.1` at version `1.1.1n-0+deb11u4` has CRITICAL CVE-2023-44487, and a fix is available in version `1.1.1w-0+deb11u1`. Since `libssl1.1` is an OS package from the Debian base image, the remediation is to rebuild the image using a base image version that ships the patched `libssl1.1`.

#### Q6 Distractor Analysis

- *Why B is incorrect:* The output shows a fixed version is available. Both versions shown are the installed version and the fixed version, not two vulnerable versions. A fixed version in the Trivy output means upgrading resolves the CVE.
- *Why C is incorrect:* The output columns are installed version then fixed version. `1.1.1n-0+deb11u4` is the installed (vulnerable) version; `1.1.1w-0+deb11u1` is the fixed version. The installed version is still vulnerable.
- *Why D is incorrect:* Trivy does not identify which Dockerfile instruction installed a package. `libssl1.1` is a Debian standard library — it comes from the base image, not a custom Dockerfile layer.

---

### Question 7

Why must a container scan GitHub Actions job declare `needs: build` (or equivalent)?

- A) `needs: build` ensures the build job's environment variables are available to the scanner
- B) The container scan job must run after the image is built because the scanner needs the image artifact to exist before it can scan it — without `needs: build`, the scan job might run before the image is built
- C) `needs: build` is required for SARIF upload permissions to be inherited from the build job
- D) `needs: build` configures GitHub Actions to cache the base image layers between the build and scan jobs for faster scan execution

#### Q7 Correct Answer

B — Container image scanners scan a built image artifact. If the scan job runs in parallel with or before the build job, the image does not yet exist and the scanner has nothing to scan. `needs: build` creates an explicit dependency that prevents the scan job from starting until the build job completes successfully and the image is available.

#### Q7 Distractor Analysis

- *Why A is incorrect:* Environment variables in GitHub Actions are passed via `env:` sections or secrets, not via `needs:` job dependencies. `needs:` controls execution order and job output passing, not environment variable inheritance.
- *Why C is incorrect:* SARIF upload permissions are controlled by `permissions: security-events: write` in the workflow, not by `needs:` job dependencies.
- *Why D is incorrect:* Docker layer caching in GitHub Actions is configured via `cache-from` and `cache-to` in the build step. `needs:` job dependencies do not control layer caching.

---

### Question 8

A platform team is evaluating whether to use Trivy or Grype for their container scanning pipeline. Their requirements include scanning Kubernetes clusters for vulnerable images in addition to scanning images during CI builds. Which tool meets this requirement?

- A) Grype — because its Anchore Enterprise integration provides native Kubernetes scanning
- B) Trivy — because it includes a native Kubernetes cluster scanning mode (`trivy k8s`)
- C) Both tools support Kubernetes cluster scanning equally, so either would meet the requirement
- D) Neither tool supports Kubernetes cluster scanning — a dedicated Kubernetes security tool like Falco is required

#### Q8 Correct Answer

B — Trivy includes native Kubernetes cluster scanning with `trivy k8s --report summary cluster`, which scans all running workloads in a cluster for vulnerable images. Grype scans individual images and filesystems but does not have a built-in Kubernetes cluster scanning mode.

#### Q8 Distractor Analysis

- *Why A is incorrect:* Anchore Enterprise provides Kubernetes integration, but Grype (the open-source tool) does not include a native `grype k8s` command. The question specifies the scanner tool, not the enterprise platform.
- *Why C is incorrect:* Trivy and Grype have different scanning scopes. Trivy has broader scanning capabilities including Kubernetes. They are not equivalent in this dimension.
- *Why D is incorrect:* Trivy supports Kubernetes cluster scanning. Falco is a runtime security tool that detects behavioral anomalies — it is a different control than image scanning.

---

### Question 9

A developer rebuilds a container image using `FROM python:3.11-slim` instead of `FROM python:3.9-slim`. The Trivy scan finding count drops from 47 to 3. What is the most likely explanation?

- A) Python 3.11 has fewer installed packages than Python 3.9, producing a smaller attack surface with fewer scannable packages
- B) Python 3.11-slim uses Alpine Linux instead of Debian, and Alpine has fewer CVEs in its package database
- C) The `python:3.11-slim` base image was built more recently and includes OS security patches that address many CVEs that were present in the older `python:3.9-slim` image
- D) Trivy applies different scanning rules to Python 3.11 images, reducing the number of checks it performs

#### Q9 Correct Answer

C — Base image versions track OS package patch levels. A newer `python:3.11-slim` image incorporates Debian slim packages that have received security updates applied after the `python:3.9-slim` image was published. Many CVEs present in the older image's OS packages have been patched in newer Debian package releases. This demonstrates why base image currency is a critical container security practice.

#### Q9 Distractor Analysis

- *Why A is incorrect:* Python 3.9 and 3.11 slim images are both Debian-based with similar package sets. The difference in CVE count is not primarily driven by package count differences.
- *Why B is incorrect:* Both `python:3.9-slim` and `python:3.11-slim` are based on Debian slim. Neither uses Alpine Linux. The vulnerability reduction is from OS patch currency, not a Linux distribution change.
- *Why D is incorrect:* Trivy applies the same scanning rules to all images. The finding count difference reflects actual package version differences, not different rule sets.

---

### Question 10

A security team wants to ensure that container images running in production are re-scanned when new CVEs are published — not just when images are built in CI. What combination of capabilities provides this continuous monitoring?

- A) Running `trivy image` manually on a weekly schedule by a security engineer
- B) Using the Trivy operator deployed in the Kubernetes cluster, which continuously scans running workloads, combined with ECR scan-on-push in the container registry
- C) Configuring GitHub Dependabot to monitor container image CVEs and open PRs automatically
- D) Running the container-scan GitHub Actions job nightly on a schedule against the production image tag

#### Q10 Correct Answer

B — The Trivy operator runs as a Kubernetes controller and continuously scans all running workloads, generating VulnerabilityReport custom resources that surface new CVEs in running images without requiring a new CI build. ECR scan-on-push re-scans images each time they are pushed to the registry. Together, these provide continuous monitoring of the production environment independent of the CI build pipeline.

#### Q10 Distractor Analysis

- *Why A is incorrect:* Manual weekly scanning introduces human dependency and a 7-day window where newly published CVEs in running production images go undetected. Continuous monitoring should be automated.
- *Why C is incorrect:* Dependabot monitors dependency manifests and opens PRs to update them. It does not scan running production container workloads for CVEs in OS packages.
- *Why D is incorrect:* Nightly CI pipeline scans provide better coverage than weekly manual scans, but a running production workload using an image that was not recently rebuilt would not be re-scanned unless the image is re-pushed to trigger the job.
