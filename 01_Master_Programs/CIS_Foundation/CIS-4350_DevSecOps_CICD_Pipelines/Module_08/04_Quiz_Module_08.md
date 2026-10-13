# Quiz: Module 08 - SCA: Software Composition Analysis and Dependency Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

At which CI/CD pipeline stage should SCA scanning run?

- A) At the code commit stage, before any tests run, to catch vulnerable packages as early as possible
- B) At the build stage, after the package manager has resolved and downloaded dependencies, giving the tool the full dependency graph
- C) After deployment to staging, because dependencies are only fully resolved in a deployed environment
- D) After deployment to production, because the production runtime reveals all loaded libraries

#### Q1 Correct Answer

B — SCA tools need the fully resolved dependency graph to scan accurately. The package manager resolves and downloads all transitive dependencies during the build stage. This is when the complete dependency tree is available for analysis.

#### Q1 Distractor Analysis

- *Why A is incorrect:* At the commit stage, the dependency graph has not been resolved. SCA cannot scan packages that have not yet been downloaded by the package manager.
- *Why C is incorrect:* The build stage resolves dependencies before deployment. Waiting until staging deployment delays the feedback loop unnecessarily.
- *Why D is incorrect:* Running SCA against production introduces unnecessary risk and delays finding vulnerabilities until after deployment. SCA should gate the build, not production.

---

### Question 2

What is a transitive dependency?

- A) A dependency that is imported in multiple source files within the same project
- B) A package that your direct dependency requires, which you did not explicitly declare in your manifest
- C) A dependency that has been deprecated but continues to function in the current runtime
- D) A package that is only loaded conditionally based on environment variables at runtime

#### Q2 Correct Answer

B — A transitive dependency is a package pulled in by your direct dependencies, not one you explicitly chose. Because you never declared it, you may not know it exists in your application, making it a common source of hidden CVE exposure.

#### Q2 Distractor Analysis

- *Why A is incorrect:* Importing a package in multiple files is a code organization pattern, not a dependency classification. Direct vs. transitive refers to how the dependency was introduced, not how often it is referenced.
- *Why C is incorrect:* Deprecated packages are a separate category. A deprecated package may be direct or transitive, and being deprecated is not the definition of a transitive dependency.
- *Why D is incorrect:* Conditional loading at runtime describes optional or lazy-loaded dependencies. Whether a dependency is transitive is determined by the dependency graph, not by whether it is conditionally loaded.

---

### Question 3

A `snyk test` command exits with a non-zero code in a GitHub Actions pipeline. What is the correct interpretation?

- A) The Snyk authentication token has expired and must be renewed before the scan can complete
- B) The scan found vulnerabilities at or above the configured severity threshold, indicating a pipeline gate failure
- C) The `requirements.txt` file is malformed and Snyk cannot parse the dependency manifest
- D) The scan completed successfully but found zero vulnerabilities, using non-zero to indicate a clean result

#### Q3 Correct Answer

B — `snyk test` exits non-zero when it finds vulnerabilities meeting the threshold set by `--severity-threshold`. This non-zero exit code is the mechanism that fails the CI/CD pipeline job, acting as a security gate that prevents the build from proceeding.

#### Q3 Distractor Analysis

- *Why A is incorrect:* An authentication failure produces a specific error message and a distinct exit code. A non-zero exit from a completed scan means findings were detected, not an auth failure.
- *Why C is incorrect:* A manifest parsing error would also fail the scan, but the typical non-zero exit in a properly configured scan means vulnerabilities were found, not a parse error.
- *Why D is incorrect:* A clean scan with zero findings exits with code 0, indicating success. Non-zero specifically signals a failure condition — vulnerable dependencies detected.

---

### Question 4

Which command would you use in a CI/CD pipeline to fail the build when any HIGH or CRITICAL severity CVEs are found in Python dependencies?

- A) `snyk test --file=requirements.txt --package-manager=pip --severity-threshold=medium`
- B) `snyk test --file=requirements.txt --package-manager=pip --severity-threshold=high`
- C) `snyk test --file=requirements.txt --package-manager=pip --severity-threshold=critical`
- D) `snyk test --file=requirements.txt --package-manager=pip --fail-on=all`

#### Q4 Correct Answer

B — `--severity-threshold=high` causes `snyk test` to exit non-zero when any HIGH or CRITICAL severity CVE is found. CVSS High is 7.0-8.9 and Critical is 9.0-10.0. Using `high` as the threshold catches both tiers.

#### Q4 Distractor Analysis

- *Why A is incorrect:* `--severity-threshold=medium` would fail the build on MEDIUM, HIGH, and CRITICAL findings. This is a lower threshold that would likely produce too many failures for teams with older dependencies.
- *Why C is incorrect:* `--severity-threshold=critical` would only fail on CRITICAL (CVSS 9.0+) findings, allowing HIGH severity CVEs (CVSS 7.0-8.9) to pass. HIGH severity CVEs represent significant risk and should also gate the build.
- *Why D is incorrect:* `--fail-on=all` is not the correct Snyk flag syntax for severity threshold gating. The correct parameter is `--severity-threshold`.

---

### Question 5

Log4Shell (CVE-2021-44228) became the canonical example of why SCA tooling is essential. Which specific characteristic of Log4j's presence in enterprise applications made it so difficult to identify exposure without SCA?

- A) Log4j was a direct dependency explicitly declared in every affected application's `pom.xml`
- B) Log4j was primarily included as a transitive dependency by frameworks like Spring and Elasticsearch, making it invisible without an SBOM
- C) Log4j was a commercial library with restricted license terms that prevented it from appearing in open-source manifests
- D) Log4j was bundled inside compiled JAR artifacts at the operating system level, bypassing application-level dependency management

#### Q5 Correct Answer

B — Log4j was widely used as a transitive dependency — pulled in automatically by frameworks, application servers, and middleware. Application developers often had no idea Log4j was in their runtime. Without SCA tooling that inventories transitive dependencies, organizations could not quickly determine which applications were affected.

#### Q5 Distractor Analysis

- *Why A is incorrect:* If Log4j had been a direct dependency explicitly declared in every manifest, it would have been visible in package files. The crisis arose precisely because it was hidden as a transitive dependency.
- *Why C is incorrect:* Log4j is an open-source Apache project under the Apache License. License restrictions played no role in its widespread use or the difficulty of identifying exposure.
- *Why D is incorrect:* While some JARs do shade (embed) Log4j, the primary exposure vector was through the standard Maven/Gradle dependency resolution process, not OS-level bundling.

---

### Question 6

What is the difference between `snyk test` and `snyk monitor`?

- A) `snyk test` scans Python projects; `snyk monitor` scans Node.js projects
- B) `snyk test` is a one-time CI pipeline scan that exits with a code indicating findings; `snyk monitor` sends a dependency snapshot to Snyk for continuous monitoring that alerts on new CVEs published after the scan
- C) `snyk test` runs in the developer's local environment; `snyk monitor` runs only inside GitHub Actions workflows
- D) `snyk test` fails the build on any finding; `snyk monitor` only fails the build on CRITICAL findings

#### Q6 Correct Answer

B — `snyk test` performs a point-in-time scan and exits non-zero on findings — the CI gate. `snyk monitor` sends the dependency snapshot to Snyk's platform. When new CVEs are subsequently published that affect a recorded snapshot, Snyk sends alerts even without a new pipeline run. `snyk monitor` addresses the window between deployments.

#### Q6 Distractor Analysis

- *Why A is incorrect:* Both commands support multiple ecosystems. The language is determined by the project type, not by which Snyk command is used.
- *Why C is incorrect:* Both commands can run in any environment — local development or CI. The distinction is what each command does, not where it runs.
- *Why D is incorrect:* The threshold behavior is controlled by `--severity-threshold`, not by the choice between `test` and `monitor`. `snyk monitor` does not perform build gating — it enables continuous monitoring.

---

### Question 7

The OWASP Dependency-Check GitHub Action is configured with `--failOnCVSS 7`. A scan finds three CVEs: one with CVSS 6.5, one with CVSS 7.8, and one with CVSS 9.1. What is the pipeline outcome?

- A) The pipeline passes because the majority of findings (two out of three) are below the threshold
- B) The pipeline fails because the CVEs with scores of 7.8 and 9.1 meet or exceed the threshold of 7.0
- C) The pipeline passes because CVSS 7.8 is below the CRITICAL threshold of 9.0
- D) The pipeline fails on the CVSS 9.1 finding only, because `--failOnCVSS 7` requires a score strictly greater than 7

#### Q7 Correct Answer

B — `--failOnCVSS 7` causes OWASP Dependency-Check to exit non-zero when any CVE with a CVSS score of 7.0 or higher is found. This threshold covers both HIGH (7.0-8.9) and CRITICAL (9.0-10.0) severities. Two of the three findings (7.8 and 9.1) meet or exceed this threshold, so the pipeline fails.

#### Q7 Distractor Analysis

- *Why A is incorrect:* Pipeline gate decisions are not made by majority vote among findings. Any single finding at or above the threshold triggers failure.
- *Why C is incorrect:* `--failOnCVSS 7` is not limited to CRITICAL findings. A CVSS score of 7.8 is HIGH severity and meets the `--failOnCVSS 7` threshold.
- *Why D is incorrect:* `--failOnCVSS 7` triggers on scores greater than or equal to 7.0, not strictly greater than 7. A score of exactly 7.0 would also trigger the failure.

---

### Question 8

What is an SBOM, and which two standard formats are recognized for regulatory and government compliance?

- A) A Software Build Order Map, used to document the sequence of compilation steps; standard formats are YAML and TOML
- B) A Software Bill of Materials, a machine-readable inventory of all components in a software artifact; standard formats are CycloneDX and SPDX
- C) A Software Baseline Optimization Model, used for performance profiling; standard formats are JSON and XML
- D) A Software Binary Object Manifest, used for container image layer tracking; standard formats are OCI and Docker Hub

#### Q8 Correct Answer

B — An SBOM (Software Bill of Materials) is a machine-readable inventory of all components in an application: package names, versions, suppliers, and licenses. CycloneDX (OWASP-maintained) and SPDX (Linux Foundation) are the two recognized standard formats. SBOMs are increasingly required by government procurement regulations and compliance frameworks.

#### Q8 Distractor Analysis

- *Why A is incorrect:* SBOM stands for Software Bill of Materials, not Build Order Map. The formats YAML and TOML are generic configuration serialization formats, not SBOM standards.
- *Why C is incorrect:* SBOM is not related to performance profiling. The described meaning and formats are fabricated.
- *Why D is incorrect:* Container image layer tracking uses OCI manifests and Docker image specs, which are separate from SBOM standards. SBOM tracks software component inventory, not binary layer structure.

---

### Question 9

What is reachability analysis in the context of SCA, and how does it affect CVE triage decisions?

- A) Reachability analysis determines whether a vulnerable package can be downloaded from the internet, affecting whether it can be installed in air-gapped environments
- B) Reachability analysis determines whether the vulnerable code path in a flagged dependency is actually invoked by the application, reducing false positives by filtering CVEs in code paths that are never called
- C) Reachability analysis measures network connectivity between the CI server and the vulnerability database, ensuring scan results are current
- D) Reachability analysis identifies whether a CVE affects the production environment or only the development environment based on dependency scope

#### Q9 Correct Answer

B — Reachability analysis examines whether the application actually calls the vulnerable function in a flagged dependency. A library may contain a CVE in its RSA cryptography code, but if the application only uses the library's AES functions and never calls the RSA functions, the vulnerable code path is unreachable. Reachability analysis reduces triage noise by deprioritizing CVEs in unreachable code paths.

#### Q9 Distractor Analysis

- *Why A is incorrect:* Network accessibility of package repositories is unrelated to reachability analysis. Reachability analysis is about application code paths, not network connectivity to registries.
- *Why C is incorrect:* Connectivity to the vulnerability database is a tool configuration concern. Reachability analysis is a static and dynamic analysis technique for determining code path execution.
- *Why D is incorrect:* Development vs. production scope is controlled by dependency scope flags (`devDependencies`, `--dev`). Reachability analysis is about whether vulnerable code paths are executed, not about which environment a package belongs to.

---

### Question 10

A development team runs `snyk test` in their GitHub Actions pipeline on every PR. A new critical CVE is published in a library used by their application at 2:00 AM on a Tuesday. Their next PR is submitted at 11:00 AM on Thursday. What is the earliest the team will be alerted to the new CVE if they are using only `snyk test`?

- A) Immediately at 2:00 AM Tuesday, because Snyk monitors the repository in real time
- B) At 11:00 AM Thursday when the next PR triggers the pipeline and `snyk test` runs against the current dependency manifest
- C) At 2:00 AM Tuesday plus 24 hours, because Snyk caches scan results for 24 hours before flagging new CVEs
- D) Never, because `snyk test` only detects CVEs that existed when the dependency was first declared

#### Q10 Correct Answer

B — `snyk test` is a point-in-time scan that runs when the pipeline is triggered. If the pipeline only runs on PR submission, the team will not discover the new CVE until the next PR triggers the pipeline. This gap — from CVE publication to next pipeline run — is the window that `snyk monitor` addresses by enabling alerting outside the pipeline run schedule.

#### Q10 Distractor Analysis

- *Why A is incorrect:* `snyk test` does not monitor the repository in real time. It is a CLI command that runs when explicitly invoked. Real-time alerting is the function of `snyk monitor`.
- *Why C is incorrect:* Snyk does not delay CVE flagging by 24 hours. A caching delay of this type is not how Snyk operates; `snyk test` checks against Snyk's current vulnerability database at scan time.
- *Why D is incorrect:* `snyk test` checks the current package versions against the vulnerability database at the time of the scan. It will catch CVEs published after the dependency was declared, as long as the scan runs after the CVE was published.

---

### Question 11 (5 points)

A dependency confusion attack succeeds when a build system pulls a malicious public package instead of a legitimate private internal package with the same name. Which control most directly prevents this attack?

- A) Enabling `snyk monitor` to watch for new CVEs in private packages
- B) Configuring the package manager to use an internal proxy registry that blocks direct public registry access for private package namespaces
- C) Running `cosign verify` on all pulled packages before installation
- D) Pinning all package versions to exact version numbers in the manifest

#### Q11 Correct Answer

B — The most direct defense against dependency confusion is an internal proxy/nexus registry (such as Artifactory or Nexus) that controls name resolution. When a package name matches an internal namespace, the proxy serves the internal version and blocks the public registry version from being fetched. Scope prefixes (e.g., `@company/`) and verified registries also mitigate this attack.

#### Q11 Distractor Analysis

- *Why A is incorrect:* `snyk monitor` detects CVEs in known packages — it does not prevent the build system from pulling from the wrong registry.
- *Why C is incorrect:* `cosign verify` verifies that an artifact was signed by a trusted key — but the malicious public package in a dependency confusion attack is likely unsigned or signed with a different key. The prevention is registry control, not post-download verification.
- *Why D is incorrect:* Exact version pinning prevents unexpected version upgrades but does not address which registry the package is pulled from — a dependency confusion attack can supply the exact pinned version from the public registry.

---

### Question 12 (5 points)

What does SLSA (Supply-chain Levels for Software Artifacts) Level 2 require that Level 1 does not?

- A) Every build must be hermetic — no network access allowed during compilation
- B) The build must use a hosted, version-controlled build service that generates authenticated provenance
- C) Two-person approval is required for every code change before building
- D) All dependencies must be locked to commit SHA rather than version tags

#### Q12 Correct Answer

B — SLSA Level 1 requires provenance to exist (any form). SLSA Level 2 adds the requirement that builds use a hosted CI/CD service (not a local developer machine) and that the service generates authenticated, unforgeable provenance attestations. This prevents a compromised developer workstation from producing undetected tampered artifacts.

#### Q12 Distractor Analysis

- *Why A is incorrect:* Hermetic builds are required at SLSA Level 4, not Level 2.
- *Why C is incorrect:* Two-person review is a code review governance requirement, not a specific SLSA level requirement. SLSA focuses on build process integrity.
- *Why D is incorrect:* Dependency pinning to commit SHAs is a best practice related to SLSA but is not the defining difference between Level 1 and Level 2.

---

### Question 13 (5 points)

`npm audit` is run against a Node.js project and reports a vulnerability in `lodash@4.17.20` with severity "moderate". The team decides to suppress it. Which command correctly suppresses a specific npm audit advisory without modifying package versions?

- A) `npm audit fix --force`
- B) Add an `overrides` block to `package.json` pinning lodash to a patched version
- C) Add the advisory ID to the `auditIgnore` array in an `.nsprc` file or use `npm audit --omit=moderate`
- D) Remove `lodash` from `package.json` and use a different library

#### Q13 Correct Answer

C — For npm, suppressing specific advisories can be done with an `.nsprc` or `audit-resolve.json` file that lists advisory IDs to ignore, or by using `--omit` flags to exclude severity levels from results. This creates an auditable record of accepted risk.

#### Q13 Distractor Analysis

- *Why A is incorrect:* `npm audit fix --force` attempts to upgrade packages to fixed versions, potentially making breaking changes — it is not a suppression mechanism.
- *Why B is incorrect:* `overrides` in `package.json` forces a specific version across the dependency tree — this is a remediation approach, not a suppression. It is effective but modifies the dependency, unlike a documented suppression.
- *Why D is incorrect:* Replacing a library is a remediation action, not a suppression. The question asks specifically about suppression.

---

### Question 14 (5 points)

A GitHub Actions workflow runs `snyk test --severity-threshold=high` on every push to `main`. A developer pushes a commit that introduces `requests==2.6.0` (a Python library with a known HIGH CVE). What is the expected pipeline behavior?

- A) The pipeline passes because `snyk test` only runs on pull requests, not direct pushes to main
- B) The pipeline fails with a non-zero exit code because a HIGH severity CVE was found
- C) The pipeline passes because `requests` is a well-known library and Snyk trusts it by default
- D) The pipeline produces a warning but does not fail — `--severity-threshold=high` only generates reports

#### Q14 Correct Answer

B — `snyk test --severity-threshold=high` exits non-zero when any HIGH or CRITICAL CVE is found. `requests==2.6.0` contains known CVEs above the HIGH threshold. The GitHub Actions job fails, blocking the commit from being used in subsequent deployment stages.

#### Q14 Distractor Analysis

- *Why A is incorrect:* The workflow trigger is `push` to `main` — it runs on direct pushes, not only on pull requests.
- *Why C is incorrect:* Snyk does not apply trust levels to well-known libraries — it scans all dependencies against the CVE database regardless of library popularity.
- *Why D is incorrect:* `--severity-threshold=high` is a gate flag that causes a non-zero exit code — it does not produce reports only.

---

### Question 15 (5 points)

Which Sigstore component provides a tamper-evident, publicly auditable log of all artifact signatures, preventing a signer from secretly signing an artifact without it being publicly recorded?

- A) Fulcio
- B) Cosign
- C) Rekor
- D) OIDC

#### Q15 Correct Answer

C — Rekor is Sigstore's transparency log. Every signature produced by cosign is written to Rekor, creating an immutable, publicly auditable record. This prevents silent signing of backdoored artifacts — any signature can be independently verified against the Rekor log.

#### Q15 Distractor Analysis

- *Why A is incorrect:* Fulcio is Sigstore's certificate authority — it issues short-lived code-signing certificates bound to an OIDC identity. It does not serve as the transparency log.
- *Why B is incorrect:* cosign is the client tool for signing and verifying — it writes to Rekor but is not the log itself.
- *Why D is incorrect:* OIDC is the identity protocol used to authenticate signers to Fulcio — it is not a Sigstore component and is not a transparency log.

---

### Question 16 (5 points)

A team uses `pip-audit` to scan Python dependencies. The tool reports a vulnerability in `Pillow==8.2.0`. The fix requires upgrading to `Pillow==9.3.0`, which introduced a breaking API change. What is the correct DevSecOps process for handling this situation?

- A) Add `Pillow==8.2.0` to a permanent exception list and never upgrade
- B) Document the accepted risk with a suppression annotation, set a remediation deadline, and create a tracking ticket for the API migration work
- C) Immediately force-upgrade to `Pillow==9.3.0` in the same commit that introduces the vulnerability finding
- D) Disable pip-audit in the pipeline until the team has time to upgrade Pillow

#### Q16 Correct Answer

B — When a fix requires breaking API changes, the appropriate response is to document the accepted risk formally, set a remediation deadline aligned with the CVE severity, and schedule the migration work as a tracked engineering task. This balances security urgency with engineering reality while maintaining visibility and accountability.

#### Q16 Distractor Analysis

- *Why A is incorrect:* A permanent exception with no deadline or remediation plan is a security debt anti-pattern that allows risk to accumulate indefinitely.
- *Why C is incorrect:* Force-upgrading in the same commit without testing the API changes can break the application — remediation must go through normal development and testing processes.
- *Why D is incorrect:* Disabling the security tool removes visibility for all findings, not just this one — it is the highest-risk response.

---

### Question 17 (5 points)

What is the purpose of a "lockfile" (e.g., `package-lock.json`, `poetry.lock`, `requirements.txt` with pinned versions) in the context of supply chain security?

- A) Lockfiles prevent any new dependencies from being added to a project without a security review
- B) Lockfiles record exact dependency versions and hashes, ensuring reproducible builds and detecting unexpected dependency substitution
- C) Lockfiles are used by Snyk to authenticate with the package registry
- D) Lockfiles are required by GitHub Actions to enable dependency caching

#### Q17 Correct Answer

B — Lockfiles record the exact resolved version and integrity hash of every dependency (direct and transitive) at the time of `install`. This ensures every build uses the same dependency versions and allows the package manager to verify that downloaded packages match the expected hashes, detecting tampering or substitution attacks.

#### Q17 Distractor Analysis

- *Why A is incorrect:* Lockfiles do not enforce a security review requirement — they record resolved versions. Adding new dependencies is controlled by team process, not lockfiles.
- *Why C is incorrect:* Lockfiles are not authentication credentials — they are dependency manifests with version and hash data.
- *Why D is incorrect:* GitHub Actions caching uses the lockfile as a cache key input, but the security value of lockfiles is reproducibility and integrity verification, not enabling caching.

---

### Question 18 (5 points)

`snyk test --json` outputs a JSON report from a CI pipeline run. A developer notices a CVE in `cryptography==38.0.1` is marked as `"isPatched": false` and `"isIgnored": false`. What action is required?

- A) The finding is informational only — `snyk test` flags that do not produce a non-zero exit code require no action
- B) The team must update `cryptography` to a version without the CVE, or formally accept and document the risk with a suppression
- C) The developer should re-run `snyk test` without `--json` to get the actionable output
- D) `isIgnored: false` means Snyk has already reported the CVE to the library maintainer on the team's behalf

#### Q18 Correct Answer

B — `isPatched: false` means no Snyk patch is available; `isIgnored: false` means the team has not explicitly accepted this risk. The required response is either to upgrade the dependency to a fixed version or to formally add it to the Snyk ignore list with a documented justification and expiration date.

#### Q18 Distractor Analysis

- *Why A is incorrect:* Whether the finding is informational depends on the exit code — if `--severity-threshold` was set and the CVE meets it, the exit code will be non-zero. Regardless, an unpatched, unignored finding requires a decision.
- *Why C is incorrect:* The JSON output contains the same information as the text output — the format does not affect what action is required.
- *Why D is incorrect:* Snyk does not report CVEs to maintainers on a team's behalf — vulnerability disclosure is a manual process separate from scanning.

---

### Question 19 (5 points)

The `--all-projects` flag in `snyk test` is useful in which scenario?

- A) Scanning a monorepo that contains multiple projects with different package managers (Node.js, Python, Java) in subdirectories
- B) Scanning all public repositories in a GitHub organization simultaneously
- C) Running SAST analysis on all source files, not just dependency manifests
- D) Enabling reachability analysis for all dependencies in a single package manifest

#### Q19 Correct Answer

A — `--all-projects` instructs Snyk to auto-detect and scan all supported project manifests in the current directory tree. This is essential for monorepos that contain multiple services with different languages and package managers, ensuring no project is missed.

#### Q19 Distractor Analysis

- *Why B is incorrect:* Scanning multiple GitHub organization repositories requires the Snyk GitHub integration or the Snyk CLI with repository iteration — `--all-projects` operates on the local directory.
- *Why C is incorrect:* `--all-projects` is a dependency scanning flag — Snyk SAST (Code) analysis is a separate product and is not enabled by this flag.
- *Why D is incorrect:* Reachability analysis is enabled separately (via Snyk's platform settings) — `--all-projects` only controls which project manifests are scanned.

---

### Question 20 (5 points)

US Executive Order 14028 (2021) created a federal requirement for SBOMs in software sold to the US government. What practical implication does this have for software vendors?

- A) All software sold to the US government must be open source so SBOMs can be generated
- B) Vendors must provide a machine-readable SBOM for any software sold to federal agencies, documenting all components and dependencies
- C) SBOMs must be filed with NIST before software can be licensed for government use
- D) The executive order requires SBOMs only for software running on classified government networks

#### Q20 Correct Answer

B — EO 14028 requires software vendors selling to the federal government to provide SBOMs so agencies can understand the software supply chain, identify exposure to CVEs, and make informed procurement decisions. This has driven broad industry adoption of SBOM tooling even outside the government sector.

#### Q20 Distractor Analysis

- *Why A is incorrect:* EO 14028 does not require open-source software — it requires transparency through SBOMs, which can be generated for proprietary software as well.
- *Why C is incorrect:* There is no NIST SBOM filing requirement — SBOMs are provided to customers/agencies, not submitted to a registry.
- *Why D is incorrect:* The requirement applies to all software sold to federal agencies, not specifically classified network environments.

---

Quiz — Module 08 | CIS-4350 | Texas Wesleyan University | Professor Nash
