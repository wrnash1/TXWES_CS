# Quiz: Module 08 - SCA – Software Composition Analysis and Dependency Scanning

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the primary function of a Software Composition Analysis (SCA) tool?

* A) To analyze the application's UI design for accessibility compliance issues
* B) To identify open-source and third-party dependencies with known security vulnerabilities (CVEs) in both direct and transitive packages
* C) To optimize network throughput between microservices in a Kubernetes cluster
* D) To compile Python packages from source into optimized bytecode for faster runtime execution
* **Correct Answer:** B) SCA scans dependency definition files (e.g., `package.json`, `requirements.txt`) against vulnerability databases and reports which component versions have known CVEs.
* **Distractor Analysis:**
  * *Why B is correct:* SCA tools inventory all packages — direct and transitive — and cross-reference each version against the NVD, GitHub Advisory Database, and other CVE sources, producing a prioritized list of vulnerabilities to remediate.
  * *Why A is incorrect:* UI accessibility compliance is evaluated by tools like axe or Lighthouse, not SCA scanners. SCA focuses on software component security, not user interface design.
  * *Why C is incorrect:* Network throughput optimization between microservices is a Kubernetes networking and service mesh concern (Istio, Linkerd). SCA operates at the dependency inventory layer, not the runtime network layer.
  * *Why D is incorrect:* Compiling Python packages to bytecode is a Python runtime optimization performed by the interpreter. SCA analyzes installed package versions for CVEs and does not perform compilation.

---

**Question 2**
Which of the following most accurately describes license compliance in the context of Software Composition Analysis?

* A) The process of verifying that all CI/CD pipeline job execution licenses are within the paid tier limits of the CI platform
* B) The SCA practice of inventorying the open-source licenses of all dependencies — identifying copyleft licenses (GPL, AGPL) that may impose legal requirements on the application's distribution model
* C) A Kubernetes resource policy that limits the number of pod replicas a deployment is licensed to run in a given namespace
* D) A cryptographic certificate chain validation step that verifies the authenticity of package signatures before installation
* **Correct Answer:** B) License compliance in SCA ensures that open-source components with copyleft or restrictive licenses are identified before they impose unexpected legal obligations on the product.
* **Distractor Analysis:**
  * *Why B is correct:* Copyleft licenses like GPL require that derivative works also be open-sourced. SCA tools generate license inventories and flag components whose licenses conflict with the organization's usage model, enabling legal review before those packages are shipped to customers.
  * *Why A is incorrect:* CI platform billing tiers are a commercial and operational concern. License compliance in SCA refers to software licensing of open-source components, not CI platform subscription tiers.
  * *Why C is incorrect:* Kubernetes resource policies (LimitRange, ResourceQuota) control CPU, memory, and replica counts in namespaces. These are operational controls unrelated to software license auditing.
  * *Why D is incorrect:* Package signature verification (e.g., `pip` hash checking, `npm` integrity fields) is a supply chain integrity control. While related to supply chain security, it is distinct from open-source license compliance analysis.

---

**Question 3**
A Node.js application's `package.json` lists `express@4.17.1` as a direct dependency. An SCA scan reports a CRITICAL CVE in `lodash@4.17.4` — a package that `express` depends on but is not listed in `package.json`. What concept does this illustrate, and what is the correct response?

* A) This is a false positive because `lodash` is not a direct dependency; the team should suppress the finding and continue development
* B) This illustrates transitive (indirect) dependency vulnerability exposure; the correct response is to upgrade `express` to a version that depends on a patched `lodash` version, or add a direct `lodash` override to the project's dependency resolution
* C) This finding indicates that the SCA scanner is misconfigured; only direct dependencies should be scanned for CVEs
* D) This is a SAST finding, not an SCA finding; switch to a SAST tool to properly remediate the lodash issue
* **Correct Answer:** B) Transitive dependency vulnerabilities are real and exploitable regardless of whether the package is directly listed in the manifest; the application ships the vulnerable `lodash` code and must be remediated by upgrading the dependency chain.
* **Distractor Analysis:**
  * *Why B is correct:* The Log4Shell vulnerability (CVE-2021-44228) demonstrated the catastrophic risk of transitive dependencies. A transitive CVE means the vulnerable code is present in the deployed application and is reachable — it must be treated with the same urgency as a direct dependency vulnerability.
  * *Why A is incorrect:* Suppressing a CRITICAL transitive CVE because the package is not directly listed ignores a real, exploitable vulnerability. Transitive dependencies are shipped in the application's `node_modules` and are fully present at runtime.
  * *Why C is incorrect:* SCA tools are specifically designed to scan the full dependency tree including transitive dependencies. Limiting SCA to direct dependencies only would miss a large and historically significant category of vulnerability.
  * *Why D is incorrect:* SCA is the correct tool for dependency CVE analysis. SAST analyzes source code for coding vulnerabilities; it does not track package versions against CVE databases.

---

**Question 4**
A DevSecOps team generates a Software Bill of Materials (SBOM) as part of their pipeline. A new critical CVE is published for `openssl@1.1.1`. How does the SBOM help the team respond?

* A) The SBOM automatically patches all affected systems by downloading and applying the new OpenSSL version
* B) The SBOM provides an immediate inventory of which applications include OpenSSL and which version, allowing the team to quickly identify all affected services without manually inspecting every codebase
* C) The SBOM notifies the OpenSSL maintainers of the team's affected deployment, triggering an automated patch release
* D) The SBOM generates a pull request in each affected repository to update the OpenSSL dependency automatically
* **Correct Answer:** B) An SBOM is a structured inventory of all software components and versions in each application; when a new CVE is disclosed, the SBOM enables rapid triage — identifying affected applications in minutes rather than hours of manual review.
* **Distractor Analysis:**
  * *Why B is correct:* SBOM formats (CycloneDX, SPDX) list every component with its version and license; querying `openssl@1.1.1` across all SBOMs immediately surfaces every application that ships the vulnerable version, enabling prioritized incident response.
  * *Why A is incorrect:* SBOMs are read-only inventory documents; they do not perform automated patching. Patching requires developer action or automated PR tooling (like Dependabot) separate from SBOM generation.
  * *Why C is incorrect:* SBOMs are internal organizational artifacts; they are not shared with upstream maintainers as part of their generation. Upstream notifications happen through CVE disclosure processes, not SBOM generation.
  * *Why D is incorrect:* Automated dependency update PRs are generated by tools like Dependabot or Renovate, not by SBOMs. An SBOM is an inventory document, not an automation trigger.

---

**Question 5**
An SCA scan of a Python application identifies the following vulnerable dependency: `Pillow==9.0.0` with CVE-2023-44271 (CRITICAL, image processing denial of service). The latest patched version is `Pillow==10.0.1`. Which remediation steps correctly address this vulnerability within a DevSecOps pipeline?

* A) Add a suppression entry for CVE-2023-44271 in the SCA configuration file so future scans no longer report it as a finding
* B) Upgrade `requirements.txt` to specify `Pillow>=10.0.1`, run the SCA scan again to verify no CRITICAL findings remain, and merge the fix through the normal PR process so the pipeline validates the remediation
* C) Remove Pillow from the application entirely and replace all image processing functionality with custom-written code
* D) Deploy a web application firewall rule that blocks all HTTP requests containing image files so the Pillow vulnerability cannot be triggered
* **Correct Answer:** B) Upgrading the dependency to the patched version and re-running the SCA scan confirms the remediation — the pipeline gate validates the fix before the change is merged and deployed.
* **Distractor Analysis:**
  * *Why B is correct:* Dependency version upgrades are the canonical SCA remediation. Specifying `>=10.0.1` in the requirements file, rebuilding the environment, and verifying the scan passes is the complete, correct DevSecOps workflow for a dependency CVE.
  * *Why A is incorrect:* Suppressing the CVE removes the finding from reports without fixing the vulnerability. The application continues to ship the vulnerable Pillow version, leaving users exposed.
  * *Why C is incorrect:* Replacing a well-tested library with custom-written image processing code introduces significant new risk — custom code is far more likely to contain vulnerabilities than a patched, widely reviewed open-source library.
  * *Why D is incorrect:* A WAF rule blocking image file uploads is an overly broad compensating control that breaks application functionality. It also does not address all attack vectors for an image processing CVE; some vulnerabilities can be triggered through non-obvious image payloads.
