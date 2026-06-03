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
