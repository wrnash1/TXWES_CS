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

---

#### Q11

A pipeline runs `trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest` and finds three HIGH CVEs in the `libssl` OS package. The security team determines that all three CVEs require a kernel module not present in the container's runtime environment. What is the appropriate next action?

- A) Ignore the findings permanently — OS package CVEs are never exploitable in containers
- B) Add `--ignore-unfixed` to the Trivy command to remove all unfixed findings from future scans
- C) Create a `.trivyignore` file listing the three CVE IDs with a justification comment, and document the risk acceptance decision
- D) Downgrade the severity filter to `--severity CRITICAL` so the pipeline no longer fails on HIGH findings

#### Q11 Correct Answer

C — A `.trivyignore` file suppresses specific CVE IDs while leaving all other HIGH/CRITICAL findings as pipeline gates. The suppression should be accompanied by a documented risk acceptance decision explaining why the CVE is not exploitable in this specific runtime context. This is the correct targeted suppression approach.

#### Q11 Distractor Analysis

- *Why A is incorrect:* OS package CVEs can be exploitable in containers when the exploitable component is reachable. Blanket dismissal of OS package CVEs is not a valid security posture and would fail a security audit.
- *Why B is incorrect:* `--ignore-unfixed` removes all findings without available fixes, not findings that are not exploitable in a specific context. It is a broader filter that would hide other legitimate unfixed CVEs.
- *Why D is incorrect:* Dropping the severity threshold to CRITICAL-only would hide all HIGH findings across the entire image, not just the three accepted risks. This degrades the overall security gate without justification for the other HIGH findings.

---

#### Q12

You are building a container image for a Go application. The final image is `FROM scratch` with only the compiled binary. A Trivy scan of this image returns zero findings. A developer argues the scan proves the image is secure. What is the most accurate limitation of this conclusion?

- A) Trivy cannot scan images built `FROM scratch` — the scan must have returned a false negative
- B) The scan only checked OS package CVEs; since `FROM scratch` has no OS layer, application-level vulnerabilities in the Go binary itself (logic flaws, injection, insecure deserialization) are outside the scope of a CVE scanner
- C) The Go binary packages are not scanned by Trivy because Go uses static linking
- D) Trivy requires a running container to scan for vulnerabilities — scanning an image at rest is not meaningful

#### Q12 Correct Answer

B — Container image scanners check packages against CVE databases. A `FROM scratch` image with a statically compiled Go binary has no OS packages to scan, and Go module CVEs can still be detected if Go module data is embedded. However, application logic vulnerabilities — injection flaws, business logic errors, insecure handling of inputs — are never detected by CVE scanning. A zero-finding scan does not mean the application is secure, only that no known CVEs in scanned packages were found.

#### Q12 Distractor Analysis

- *Why A is incorrect:* Trivy can scan `FROM scratch` images. It would scan Go module metadata if present. A zero-finding result is valid — it means no CVEs were found, not that the scan failed.
- *Why C is incorrect:* Trivy does scan Go module dependencies using go.sum and module metadata embedded in the binary. Static linking does not prevent CVE detection for Go modules.
- *Why D is incorrect:* Container image scanners operate on the image filesystem at rest — they do not need a running container. Trivy extracts layers and scans package metadata without executing the container.

---

#### Q13

A team's container scan pipeline uses `grype myapp:latest --fail-on high`. The pipeline has been failing for two weeks because a transitive dependency of a logging library has a HIGH CVE with no available fix. The developers want to unblock the pipeline. What is the recommended approach?

- A) Switch the fail threshold to `--fail-on critical` to stop failing on HIGH findings permanently
- B) Remove the container scan job from the pipeline until the upstream library publishes a fix
- C) Use `grype myapp:latest --fail-on high --only-fixed` so the gate only fails on HIGH/CRITICAL CVEs that have an available remediation
- D) Pin the logging library to an older version that does not have the transitive dependency

#### Q13 Correct Answer

C — `--only-fixed` (Grype) filters findings to those with an available fixed version. This means unfixable CVEs no longer block the pipeline while still gating on HIGH/CRITICAL findings that the team can actually remediate. This is the standard pattern for reducing noise without permanently lowering the security bar.

#### Q13 Distractor Analysis

- *Why A is incorrect:* Permanently lowering the threshold to CRITICAL-only removes the HIGH severity gate for the entire image and all future findings, not just the specific unfixable CVE. This is a broad scope reduction not warranted by a single unfixable finding.
- *Why B is incorrect:* Removing the container scan job eliminates all vulnerability detection for this image. The security gate provides value beyond this single CVE; removing it entirely is not proportionate.
- *Why D is incorrect:* Pinning to an older version may introduce other vulnerabilities in the older version and does not guarantee the transitive dependency vulnerability is absent. It also creates technical debt and conflicts with receiving bug fixes in the logging library.

---

#### Q14

A GitHub Actions workflow scans a container image and uploads the results to GitHub Code Scanning using `github/codeql-action/upload-sarif@v3` with `if: always()`. Why is `if: always()` required on the SARIF upload step?

- A) Without `if: always()`, the SARIF file is deleted from the runner before the upload step executes
- B) Without `if: always()`, a failing scan step (exit code 1) causes all subsequent steps to be skipped by default, which would prevent the SARIF results from being uploaded when the scan finds vulnerabilities
- C) `if: always()` grants the upload step elevated permissions to write to the GitHub Security tab
- D) `if: always()` is required only when the scan produces zero findings — it has no effect when the scan fails

#### Q14 Correct Answer

B — In GitHub Actions, when a step exits with a non-zero exit code, all subsequent steps in the job are skipped unless explicitly configured otherwise. Since the scan step uses `--exit-code 1` or `--fail-on`, it will exit non-zero when vulnerabilities are found. Without `if: always()`, the SARIF upload would be skipped precisely when it is most needed — when the scan has found real findings to report.

#### Q14 Distractor Analysis

- *Why A is incorrect:* SARIF files written to the runner filesystem persist until the job completes. File persistence is not the issue — step execution control is.
- *Why C is incorrect:* `if: always()` is a step execution condition, not a permissions modifier. SARIF upload permissions are controlled by the `permissions: security-events: write` job-level setting.
- *Why D is incorrect:* `if: always()` applies regardless of whether the scan found zero or many findings. Its purpose is to ensure the step runs even after a previous step failure, not to handle the zero-findings case specifically.

---

#### Q15

Which of the following best describes the difference between what Trivy detects in `--scanners vuln` mode versus `--scanners secret` mode?

- A) `vuln` mode scans the running container; `secret` mode scans the Dockerfile source code
- B) `vuln` mode detects CVEs in OS and language packages; `secret` mode detects hardcoded credentials, API keys, and tokens baked into image layers
- C) `vuln` mode detects application logic flaws; `secret` mode detects dependency version mismatches
- D) Both modes produce the same findings — the flag only controls the output format

#### Q15 Correct Answer

B — Trivy's `--scanners vuln` mode queries vulnerability databases for CVEs in packages. `--scanners secret` mode uses pattern matching to detect hardcoded credentials, API keys, tokens, and other secrets baked into image layers or filesystem files. These are two distinct risk categories: known CVEs in software supply chain versus sensitive data exposure baked into the artifact.

#### Q15 Distractor Analysis

- *Why A is incorrect:* Both scanner modes operate on the container image at rest, not on a running container or on the Dockerfile source. Trivy extracts and analyzes image layers regardless of the scan mode.
- *Why C is incorrect:* Neither mode detects application logic flaws — that is the domain of SAST and DAST tools. Dependency version mismatches are a version management concern, not a separate scanner mode.
- *Why D is incorrect:* The two modes produce different types of findings from different detection engines. They can be combined (`--scanners vuln,secret`) to run both in a single scan.

---

#### Q16

A security engineer wants to enforce that no container image with a CRITICAL CVE can be deployed to the production Kubernetes cluster, regardless of what passed the CI scan at build time. Which control enforces this at the admission stage?

- A) GitHub branch protection rules requiring the container scan job to pass before merge
- B) A Kubernetes admission controller (such as Kyverno or OPA Gatekeeper) that checks an image attestation or admission webhook that verifies the image has a clean scan report before scheduling
- C) Setting `imagePullPolicy: Never` on all production pods to prevent unscanned images from being pulled
- D) Configuring Trivy in the CI pipeline with `--severity CRITICAL --exit-code 1` on the build job

#### Q16 Correct Answer

B — Admission controllers enforce policy at the point where a resource is submitted to the Kubernetes API server, before the pod is scheduled. An admission webhook can verify that the image carries a valid attestation (for example, a cosign signature or SBOM attestation from a trusted scanner) confirming it passed the required scan. This is a runtime enforcement layer independent of the CI pipeline.

#### Q16 Distractor Analysis

- *Why A is incorrect:* Branch protection prevents merging code that fails CI scans, but it does not prevent a direct deployment from a developer's local environment or an out-of-band kubectl apply that bypasses the PR workflow.
- *Why C is incorrect:* `imagePullPolicy: Never` prevents pulling images from a registry but does not enforce scan compliance — it simply blocks all pulls. It would prevent legitimate deployments as well as unscanned ones.
- *Why D is incorrect:* CI pipeline gates enforce scan requirements at build time. They do not enforce anything at deployment time. An image built and scanned months ago could be deployed without a re-scan.

---

#### Q17

A Trivy scan of `python:3.9-slim` returns 47 HIGH/CRITICAL CVEs. The same application scanned in a `python:3.9-alpine` base image returns 8. What explains the difference?

- A) Alpine-based images use a different CVE database that has fewer entries, making the scan appear to find fewer vulnerabilities
- B) Alpine Linux uses musl libc and BusyBox instead of glibc and the full Debian package set, resulting in a significantly smaller OS package footprint that has fewer packages and therefore fewer CVEs
- C) Trivy skips Alpine images by default because Alpine uses apk, which is not supported by Trivy's OS scanner
- D) The `slim` variant includes development tools that introduce CVEs; `alpine` removes them

#### Q17 Correct Answer

B — Alpine Linux has a minimal OS package set built on musl libc and BusyBox rather than the Debian/Ubuntu package ecosystem. The smaller surface area means fewer installed packages, and therefore fewer packages that can have associated CVEs. Debian-based images include many more system libraries and utilities that accumulate CVE findings even when not needed by the application.

#### Q17 Distractor Analysis

- *Why A is incorrect:* Trivy uses the same CVE databases (NVD, OSV, vendor advisories) regardless of the base image OS. The difference in findings reflects actual package differences, not database differences.
- *Why C is incorrect:* Trivy fully supports Alpine/apk package scanning. Alpine is one of the most commonly scanned base images.
- *Why D is incorrect:* The `slim` variant removes development tools and documentation compared to the full image — it is already a reduced surface area. The difference between `slim` and `alpine` is the underlying OS package ecosystem, not the presence of dev tools.

---

#### Q18

What is the purpose of generating a Software Bill of Materials (SBOM) for a container image, and which Trivy flag produces a CycloneDX-format SBOM?

- A) An SBOM lists the CVEs found in the image; `--format cyclonedx` generates the CVE report in CycloneDX format
- B) An SBOM is an inventory of all packages and dependencies in the image; `trivy image --format cyclonedx --output sbom.json myapp:latest` generates a CycloneDX SBOM
- C) An SBOM is only required for images published to public registries; `--sbom` flag generates it for private registries
- D) An SBOM replaces the vulnerability scan — once an SBOM is generated, no further scanning is needed

#### Q18 Correct Answer

B — An SBOM is a structured inventory of every package, library, and component in a container image. CycloneDX is one of the two standard SBOM formats (alongside SPDX). The `--format cyclonedx` flag with `--output sbom.json` produces a CycloneDX SBOM that can be used for vulnerability correlation, compliance attestation, and supply chain auditing.

#### Q18 Distractor Analysis

- *Why A is incorrect:* An SBOM is a component inventory, not a CVE report. The `--format cyclonedx` flag changes the SBOM output format, but when used in vulnerability scan mode, it produces vulnerability findings in CycloneDX VEX format — not just an inventory. The description conflates the two outputs.
- *Why C is incorrect:* SBOMs are useful for both public and private images and are increasingly required by US federal procurement regulations (EO 14028) for any software delivered to government customers, regardless of registry visibility.
- *Why D is incorrect:* An SBOM and a vulnerability scan serve complementary purposes. The SBOM provides the component inventory; the vulnerability scan correlates that inventory against CVE databases. An SBOM does not replace scanning.

---

#### Q19

A container image scan finds CVE-2023-XXXXX (CRITICAL) in `openssl 3.0.7`. The fixed version is `openssl 3.0.8`. The image uses `FROM debian:bookworm-slim`. What is the correct remediation action?

- A) Add `openssl` to the `.trivyignore` file since the fix is available and will be applied automatically by the OS
- B) Rebuild the image using `docker build --no-cache` to force a fresh base image pull, which will include the patched `openssl` version if Debian has published the update to its package repositories
- C) Remove OpenSSL from the image using `RUN apt-get remove openssl` in the Dockerfile
- D) Pin the OpenSSL version to `3.0.7` in the Dockerfile to prevent Trivy from detecting the version mismatch

#### Q19 Correct Answer

B — OS package CVEs in Debian-based images are remediated by pulling a fresh base image layer that includes the patched package version. Using `--no-cache` forces Docker to re-pull the base image and re-run all `RUN apt-get install` layers, picking up security updates published to the Debian security repositories. This is the standard OS-layer CVE remediation path.

#### Q19 Distractor Analysis

- *Why A is incorrect:* `.trivyignore` suppresses a CVE finding in the scan output but does not remediate the vulnerability. The vulnerable version of OpenSSL remains in the running container. Suppressing a finding with an available fix defeats the purpose of the security gate.
- *Why C is incorrect:* Removing OpenSSL is only viable if nothing in the application or base image depends on it. Debian packages have complex dependency trees; removing a core library will likely break the image or require removing large portions of the base image package set.
- *Why D is incorrect:* Pinning a package to a known-vulnerable version is the wrong direction — it ensures the vulnerability persists. Trivy detects the installed version; pinning to the vulnerable version does not hide it.

---

#### Q20

A development team scans their production image weekly in CI and updates the base image monthly. A new CRITICAL CVE in the base image's `libc` package is published on a Tuesday. Under this schedule, when is the earliest the team's pipeline would detect the new CVE?

- A) Immediately — container registries push CVE alerts in real time to all images that contain the affected package
- B) The next weekly CI scan run — Trivy downloads updated vulnerability databases each time it runs, so the CVE would be detected at the next scheduled scan
- C) The next monthly base image update — CVEs are only detectable after a new base image version is published
- D) Never — `libc` CVEs cannot be detected by container image scanners because libc is a system library, not a package

#### Q20 Correct Answer

B — Trivy downloads the latest vulnerability database from GitHub releases each time it runs (or from a cache that is refreshed on a configurable schedule). When a new CVE is published and added to the NVD or OS vendor advisory database, the next Trivy scan run will detect the CVE in the currently installed package version. A weekly scan schedule means the detection gap is up to 7 days.

#### Q20 Distractor Analysis

- *Why A is incorrect:* Container registries do not push CVE alerts in real time to images stored in the registry. ECR scan-on-push re-scans when images are pushed; it does not automatically re-scan existing stored images without an explicit re-scan trigger (unless using ECR enhanced scanning with Inspector integration).
- *Why C is incorrect:* CVEs are detected against the installed package version in the current image, not against a new base image version. A scan run with an updated vulnerability database will detect the CVE in the currently deployed image regardless of whether the base image has been updated.
- *Why D is incorrect:* libc is a standard OS package tracked by OS vendor advisory databases (Debian Security Advisories, Ubuntu USN, etc.). Trivy and Grype both detect CVEs in libc and other core system libraries.

---

Quiz — Module 11 | CIS-4350 | Texas Wesleyan University | Professor Nash
