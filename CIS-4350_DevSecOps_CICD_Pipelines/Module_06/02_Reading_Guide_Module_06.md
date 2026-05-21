# Reading Guide: Module 06 - SAST – Static Application Security Testing

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 06 - SAST – Static Application Security Testing**! This module covers SAST as the primary shift-left security gate in a DevSecOps pipeline. You will learn how SAST tools analyze source code without executing it — using pattern matching, data flow analysis, and taint tracking — to detect vulnerabilities such as SQL injection, hardcoded credentials, insecure deserialization, and path traversal. You will also learn how to manage false positives effectively and integrate SAST results as blocking pipeline gates. These skills are essential for the CDP exam and for building security into the development workflow.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **SAST scanners**: Security tools that analyze application source code, bytecode, or compiled binaries for vulnerabilities without executing the code. Common SAST tools include Semgrep, SonarQube, Checkmarx, Veracode, and CodeQL. In a DevSecOps pipeline, SAST scanners run as a pipeline job triggered at the pull request stage, blocking merges when high-severity findings are detected.

* **Static analysis**: The process of examining code structure, data flow, and control flow to identify security vulnerabilities, bugs, and policy violations without running the program. Static analysis can detect entire classes of vulnerabilities (e.g., all uses of `eval()` on user input) systematically across a codebase — something human code review cannot do consistently at scale.

* **Pattern matching**: A SAST technique that compares code against a library of known vulnerability signatures or anti-patterns (e.g., detecting `String query = "SELECT * FROM users WHERE id = " + userId` as a SQL injection risk). Pattern-matching SAST is fast and produces low false-positive rates but may miss vulnerabilities that require cross-function data flow analysis.

* **False positives management**: The process of reviewing, validating, and suppressing SAST findings that are incorrectly flagged as vulnerabilities. Effective false positive management is critical for maintaining developer trust in SAST tooling — too many false positives cause alert fatigue and lead teams to ignore scanner output. Suppression comments (e.g., `# nosec`) should be tracked and reviewed regularly to prevent legitimate findings from being hidden.

---

### 2. Certification Exam Tips

* **SAST vs. DAST Distinction**: The CDP exam heavily tests the SAST/DAST distinction. SAST analyzes source code without execution (can run without a deployed application, catches issues at code review time). DAST tests a running application from the outside (requires deployment, finds runtime and configuration issues SAST cannot see). Know both the differences and why you need both.
* **Pipeline Gate Failure Modes**: Know the difference between SAST configured as a blocking gate (pipeline fails and merge is prevented on HIGH/CRITICAL findings) versus advisory mode (findings are reported but the pipeline continues). The CDP exam expects you to know when each mode is appropriate and what the security tradeoffs are.
* **Semgrep vs. CodeQL**: Semgrep uses YAML rules for pattern matching and is fast and developer-friendly; CodeQL performs deep semantic analysis and data flow tracing for more complex vulnerability patterns. The exam may ask you to select the appropriate tool for a given scenario.
* **Study Resource**: The [OWASP Source Code Analysis Tools page](https://owasp.org/www-community/Source_Code_Analysis_Tools) provides a comprehensive comparison of SAST tools by language support, analysis depth, and license — essential reference for CDP tool selection questions.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [OWASP Source Code Analysis Tools reference](https://owasp.org/www-community/Source_Code_Analysis_Tools) — OWASP's curated comparison of SAST tools covering commercial and open-source options, analysis techniques, and language coverage. This resource directly supports CDP exam tool selection and pipeline design questions.
* **Required Video**: Watch the SAST integration segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates configuring a SAST scanner (Semgrep or CodeQL) as a GitHub Actions step, interpreting scan output, and configuring severity thresholds for pipeline gates.

---

### Lab & Command Integration

In this week's hands-on lab, you will configure and run a SAST pipeline gate by:

* **Configure a SAST scanner tool in pipeline**: Add a Semgrep or CodeQL scanning step to a GitHub Actions workflow, configuring it to run on `pull_request` events and to fail the build on HIGH or CRITICAL severity findings.
* **Scan a repository containing security issues**: Use a deliberately vulnerable sample application (such as WebGoat or DVWA) as a scan target, running the configured SAST tool against its source code.
* **Review scan reports**: Interpret the scanner's output — identify the finding severity, the vulnerable code location, the CWE classification, and the recommended remediation — and document one true positive and one false positive finding.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand the difference between pattern matching and data flow analysis in SAST.
* [ ] Read the OWASP Source Code Analysis Tools reference at [https://owasp.org/www-community/Source_Code_Analysis_Tools](https://owasp.org/www-community/Source_Code_Analysis_Tools).
* [ ] Watch the SAST segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the SAST pipeline integration and scan review in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
