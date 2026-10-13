# Reading Guide: Module 11 - Container Image Scanning: Trivy and Grype

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

Module 11 covers container image scanning — the DevSecOps control that identifies CVEs in OS packages and language packages bundled inside container images. While SCA scans your declared dependency manifest, container image scanning scans the full runtime artifact: every binary and library present in every layer of the image. This module covers Trivy (Aqua Security) and Grype (Anchore) as the two primary tools, and pipeline integration patterns for gating builds on vulnerability findings.

---

## Section 1: High-Yield Glossary

**Container image scanning** — Automated scanning of a container image's OS packages and language packages against vulnerability databases. Scans the complete runtime artifact, including packages from the base image and every layer added during the build.

**Trivy** — An open-source vulnerability scanner from Aqua Security. Scans container images, filesystems, Git repositories, and Kubernetes clusters. Checks OS packages (apk, apt, rpm) and language packages (pip, npm, Maven, gems, Go modules). The most widely deployed container scanner.

**Grype** — An open-source container image and filesystem scanner from Anchore. Produces a clean tabular output showing package, installed version, fixed version, and severity. Supports `--only-fixed` to filter unfixable findings.

**`--exit-code 1`** — Trivy CLI flag that causes the process to exit with code 1 when any CVE matching the severity filter is found. This non-zero exit code fails the CI/CD pipeline job.

**`--fail-on`** — Grype CLI flag equivalent to Trivy's `--exit-code 1`. `grype --fail-on high` exits non-zero when any HIGH or CRITICAL CVE is found.

**`--ignore-unfixed`** — Trivy CLI flag that excludes CVEs for which no patched version is available. Reduces pipeline noise by focusing on actionable, remediable findings.

**`--only-fixed`** — Grype CLI flag equivalent to Trivy's `--ignore-unfixed`. Filters the output to show only CVEs with an available fix version.

**OS package CVE** — A vulnerability in a package provided by the container's operating system base image (Alpine apk packages, Debian apt packages, RHEL rpm packages). Remediated by updating the base image to a newer version.

**Language package CVE** — A vulnerability in an application dependency installed via a package manager (pip, npm, Maven). Remediated by updating the dependency version in the manifest.

**Base image currency** — The practice of regularly updating the `FROM` base image in a Dockerfile to include OS security patches. Critical because base images receive OS CVE fixes as patches are released by the OS maintainer.

**Image digest pinning** — Using `FROM python:3.11-slim@sha256:abc...` instead of `FROM python:3.11-slim` to lock to a specific immutable image version. Provides reproducibility but requires explicit update PRs when base images are patched.

**SBOM from image** — Trivy can generate an SBOM in CycloneDX format from a container image, producing a complete machine-readable inventory of every package in the image.

**Anchore** — The company that maintains Grype and Syft (an SBOM generation tool). The Anchore suite provides image scanning (Grype), SBOM generation (Syft), and enterprise policy enforcement.

**Syft** — Anchore's open-source SBOM generation tool. Generates CycloneDX and SPDX SBOMs from container images and filesystems. Works alongside Grype: Syft generates the package inventory, Grype checks the inventory against vulnerability databases.

---

## Section 2: Trivy vs. Grype Comparison

| Dimension | Trivy | Grype |
|---|---|---|
| Maintainer | Aqua Security | Anchore |
| License | Apache 2.0 | Apache 2.0 |
| Scanning targets | Container images, filesystems, Git repos, K8s clusters | Container images, filesystems, directories, OCI layouts |
| OS package support | Alpine, Debian, Ubuntu, RHEL, CentOS, Amazon Linux, SUSE | Alpine, Debian, Ubuntu, RHEL, CentOS, Amazon Linux |
| Language package support | Python, Node, Java, Ruby, Go, Rust | Python, Node, Java, Ruby, Go, .NET |
| Pipeline exit code flag | `--exit-code 1` | `--fail-on high` |
| Unfixed CVE filter | `--ignore-unfixed` | `--only-fixed` |
| SARIF output | Yes | Yes |
| SBOM generation | Yes (CycloneDX) | Via Syft |
| GitHub Action | `aquasecurity/trivy-action` | `anchore/scan-action` |
| Kubernetes cluster scan | Yes | No |

---

## Section 3: Container Scanning Pipeline Placement

| Stage | Scan Target | Tool | Gate |
|---|---|---|---|
| Build | Newly built image before push | Trivy / Grype | Fail on HIGH/CRITICAL |
| Registry push | Images on push to ECR/GCR | ECR scan-on-push, GCR Artifact Registry | Alert on new CVEs |
| Continuous monitoring | Running images in Kubernetes | Trivy operator, Anchore Enterprise | Alert, optional admission block |
| Pre-deployment | Image pulled for staging | Trivy / Grype in deploy job | Block deploy if new CVEs found |

---

## Section 4: CVE Triage Decision Framework

| Finding Type | Remediation Path | Pipeline Gate Behavior |
|---|---|---|
| CRITICAL with fix available | Upgrade package or base image immediately | Fail build |
| HIGH with fix available | Upgrade in current sprint | Fail build |
| CRITICAL/HIGH with no fix | Accept risk, document in risk register | Report, do not fail (use `--ignore-unfixed`) |
| MEDIUM with fix available | Track in backlog, fix in next sprint | Report only |
| LOW | Track in backlog | Report only |

---

## Section 5: Base Image Security Practices

| Practice | Description | Tool |
|---|---|---|
| Use minimal base images | Alpine, Debian slim, distroless — fewer packages means fewer CVE surface | Dockerfile linter (Hadolint) |
| Pin base image versions | Specify minor version (`python:3.11-slim`), not just major (`python:3`) | Dependabot |
| Rebuild regularly | Even with pinned tags, rebuild periodically to pick up OS patch updates | Scheduled pipeline |
| Update base images via PR | Dependabot automatically opens PRs when base image digest changes | Dependabot |
| Multi-stage builds | Final image contains only runtime artifacts, not build tools | Dockerfile review |

---

## Section 6: SCA vs. Container Image Scanning Comparison

| Dimension | SCA | Container Image Scanning |
|---|---|---|
| What is scanned | Dependency manifest (`requirements.txt`, `package.json`) | Complete image filesystem — all packages in all layers |
| Stage | Build (before image build) | After image build, before push |
| Finds | CVEs in declared application dependencies | CVEs in OS packages, runtime packages, AND application packages |
| Scope | Application packages only | OS + language runtime + application |
| Tools | Snyk, OWASP Dependency-Check | Trivy, Grype |
| Remediation | Update manifest | Update manifest or base image |

---

## Section 7: Kubernetes RBAC Model Reference

Container image scanning principles connect to Kubernetes security.

- Trivy can scan running Kubernetes clusters: `trivy k8s --report summary cluster`.
- Admission controllers can block deployment of images with unresolved HIGH/CRITICAL CVEs.
- Image digest pinning in Kubernetes manifests ensures the scanned image version is the deployed image version.

---

## Section 8: DevSecOps Professional Exam Tips

1. **Trivy `--exit-code 1`** — Know that `--exit-code 1` is the Trivy pipeline gate flag. Without it, Trivy reports findings but exits with code 0, which does not fail the pipeline.

2. **Grype `--fail-on`** — Know that `grype --fail-on high` is the Grype equivalent of `trivy --exit-code 1 --severity HIGH,CRITICAL`. Both cause non-zero exit on HIGH or CRITICAL findings.

3. **`--ignore-unfixed` vs. `--only-fixed`** — Know that these flags filter out CVEs with no available patch. This is important for avoiding pipeline paralysis caused by unfixable OS CVEs in base images.

4. **OS packages vs. language packages** — Know that container image scanning checks both. OS CVEs come from the base image; language CVEs come from pip/npm/Maven. Remediation path differs: OS CVEs require a base image update, language CVEs require a dependency version update.

5. **`needs: build` ordering** — Know that the container scan job must declare `needs: build` to ensure the image exists before the scanner runs. Scanning before build would fail because there is no image to scan.

6. **Trivy scope** — Know that Trivy scans more than just containers. It also scans filesystems, Git repositories, and Kubernetes clusters. This broader scope distinguishes it from Grype.

7. **SBOM from images** — Know that both Trivy and Grype/Syft can generate CycloneDX SBOMs from container images. This provides a machine-readable inventory of all packages present in the deployed container.

8. **SCA and image scanning are complementary** — SCA scans the manifest before the image is built; image scanning scans the full artifact after the image is built. They can find different packages because the image may contain packages installed by the base image that are not in any manifest.

---

## Section 9: Required Reading

- Review the Aqua Security Trivy documentation at [https://aquasecurity.github.io/trivy/](https://aquasecurity.github.io/trivy/).

---

## Section 10: Study Checklist

- [ ] Explain what container image scanning finds that SCA does not.
- [ ] Name the two primary container image scanners and one distinguishing CLI flag for each.
- [ ] Explain what `--ignore-unfixed` does and when to use it.
- [ ] Describe the pipeline placement for container image scanning relative to the build and push steps.
- [ ] Explain the CVE triage decision: when does a finding fail the build vs. when is it reported only.
- [ ] Explain why base image currency matters and how Dependabot addresses it.
- [ ] Identify two SARIF upload steps in a container scan pipeline and explain why `if: always()` is needed.
- [ ] Review the Trivy documentation at [https://aquasecurity.github.io/trivy/](https://aquasecurity.github.io/trivy/).
- [ ] Complete the Module 11 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.

---

## 9. Supplemental Resources

**1. [Aqua Security Trivy documentation](https://aquasecurity.github.io/trivy/)**
The official Trivy documentation covering all scan targets (container images, filesystems, Git repos, Kubernetes clusters), scanner modes (vuln, secret, config, sbom), output formats (table, JSON, SARIF, CycloneDX), CLI flags (`--ignore-unfixed`, `--exit-code`, `.trivyignore`), and CI/CD integration patterns.

**2. [Anchore Grype GitHub repository and documentation](https://github.com/anchore/grype)**
The official Grype repository covering installation, CLI usage (`--fail-on`, `--only-fixed`, `--output`), supported ecosystems, SBOM input scanning, and integration with Anchore's Syft SBOM generator. Includes worked examples for container image and filesystem scanning.

**3. [GitHub — Storing workflow data as artifacts and uploading SARIF results](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)**
GitHub's official guide to uploading SARIF files from container scanners and other security tools to GitHub Code Scanning. Covers the `github/codeql-action/upload-sarif@v3` action, `if: always()` pattern, SARIF file size limits, and how findings appear in the Security tab and pull request annotations.

---

Reading Guide — Module 11 | CIS-4350 | Texas Wesleyan University | Professor Nash
