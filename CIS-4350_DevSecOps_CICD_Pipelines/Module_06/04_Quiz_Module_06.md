# Quiz: Module 06 - SAST – Static Application Security Testing

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
What is the characteristic behavior of a SAST (Static Application Security Testing) tool?

* A) It scans code by executing the application in an isolated test sandbox and probing its endpoints
* B) It analyzes source code, bytecode, or binaries for vulnerabilities without running the application
* C) It monitors production CPU and memory usage to detect anomalous behavior indicative of exploitation
* D) It intercepts network traffic between a browser and a web application to identify insecure HTTP responses
* **Correct Answer:** B) SAST scanners evaluate source files against known vulnerability patterns (e.g., hardcoded keys, SQL concatenation) without requiring a running application.
* **Distractor Analysis:**
  * *Why B is correct:* SAST is a white-box, code-analysis technique that reads and parses source or binary files; because it does not execute the code, it can run at the earliest pipeline stage (commit/pull request) before a build even exists.
  * *Why A is incorrect:* Executing the application in a sandbox and probing endpoints describes DAST (Dynamic Application Security Testing), not SAST.
  * *Why C is incorrect:* Monitoring production CPU/memory for anomalies describes runtime application self-protection (RASP) or behavioral anomaly detection, not static analysis.
  * *Why D is incorrect:* Intercepting traffic between a browser and a web application describes a DAST proxy tool (such as OWASP ZAP or Burp Suite), not a SAST tool.

---

**Question 2**
Which of the following most accurately describes pattern matching as used in SAST tooling?

* A) A machine learning technique that compares runtime behavior of an application against a baseline model to detect anomalies
* B) A SAST analysis method that compares code against a library of known vulnerability signatures or insecure code constructs, such as detecting user input passed directly to a `exec()` call
* C) A penetration testing method where an assessor manually searches for specific vulnerability patterns in a deployed application
* D) A Git feature that selectively applies commit changes to a specific branch using a cherry-pick operation
* **Correct Answer:** B) Pattern matching in SAST tools uses rule sets (like Semgrep YAML rules) to detect specific code constructs that match known vulnerability patterns — fast, deterministic, and easy to customize.
* **Distractor Analysis:**
  * *Why B is correct:* Tools like Semgrep use declarative pattern rules (e.g., match `sink(source)` where source is user-controlled) to systematically find classes of vulnerabilities across entire codebases in seconds.
  * *Why A is incorrect:* Machine learning-based anomaly detection is a runtime security or SIEM technique; SAST pattern matching is rule-based, not ML-based.
  * *Why C is incorrect:* Manual penetration testing searches for vulnerabilities in a running application, not in source code. Pattern matching in SAST is automated and code-analysis based.
  * *Why D is incorrect:* Git cherry-pick is a version control operation for applying specific commits to a branch; it has no relationship to SAST analysis techniques.

---

**Question 3**
A SAST scanner reports 47 findings in a pull request, but after manual review the team determines that 40 of them are false positives. What is the most appropriate DevSecOps response to prevent recurring false positive alert fatigue?

* A) Disable the SAST scanner entirely to prevent the false positives from blocking future deployments
* B) Tune the SAST rule configuration by adjusting severity thresholds, disabling rules with high false-positive rates for this codebase, and adding inline suppression comments with documented justifications for accepted risks
* C) Automatically approve and suppress all findings without manual review to keep the pipeline moving
* D) Switch to a DAST-only approach, since DAST produces fewer false positives by testing running code
* **Correct Answer:** B) SAST tools should be tuned to the specific codebase — disabling inapplicable rules, adjusting thresholds, and documenting suppressed findings — so the scanner produces actionable signal without overwhelming developers.
* **Distractor Analysis:**
  * *Why B is correct:* Tuning reduces false positives while preserving true positive detection. Documented suppression comments (`# nosec BXXX -- justification`) create an audit trail, and periodic reviews ensure suppressed findings are reconsidered as the codebase evolves.
  * *Why A is incorrect:* Disabling the scanner eliminates false positives but also eliminates true positive detection, removing a critical security gate from the pipeline.
  * *Why C is incorrect:* Auto-approving all findings without review defeats the purpose of scanning; true positives (real vulnerabilities) would be silently suppressed along with false positives.
  * *Why D is incorrect:* DAST tests running applications and finds runtime vulnerabilities that SAST cannot; it does not replace SAST's ability to catch code-level issues at the earliest pipeline stage. Both are needed in a complete DevSecOps pipeline.

---

**Question 4**
In a GitHub Actions SAST workflow using CodeQL, which configuration ensures that only HIGH and CRITICAL severity findings block the pull request merge while LOW and MEDIUM findings are reported but non-blocking?

* A) Set `on: push` instead of `on: pull_request` so the scan runs after merge and cannot block it
* B) Configure the CodeQL action with a severity threshold of `high` in the action inputs, and set the GitHub required status check only on the SAST job, not the reporting job
* C) Run CodeQL on a scheduled weekly basis rather than on every pull request to reduce pipeline execution time
* D) Use a `.gitignore` file to exclude security-sensitive source directories from CodeQL analysis
* **Correct Answer:** B) Setting a severity threshold in the SAST action configuration allows the pipeline step to fail (blocking the merge) only on findings at or above the defined severity level, while lower-severity findings appear in the security advisory tab without blocking merges.
* **Distractor Analysis:**
  * *Why B is correct:* Most SAST tools and GitHub Actions integrations support severity threshold arguments that control exit codes; an exit code of 0 (pass) for LOW/MEDIUM findings and non-zero (fail) for HIGH/CRITICAL findings triggers the branch protection status check accordingly.
  * *Why A is incorrect:* Running the scan on `push` after merge means the scan cannot block the merge — the code is already merged when the scan runs. This defeats the purpose of a security gate.
  * *Why C is incorrect:* Weekly scheduled scans cannot serve as merge gates because they are not triggered by pull request events and run independently of the merge workflow.
  * *Why D is incorrect:* Excluding source directories from analysis reduces coverage, potentially hiding real vulnerabilities. The purpose of the severity threshold is to tune alert routing, not to reduce scan scope.

---

**Question 5**
A SAST scan of a Python web application flags the following code as a SQL injection vulnerability: `cursor.execute("SELECT * FROM orders WHERE user_id = " + user_id)`. Which remediation correctly addresses the root cause?

* A) Add input validation to ensure `user_id` contains only numeric characters before passing it to the query
* B) Replace the string concatenation with a parameterized query: `cursor.execute("SELECT * FROM orders WHERE user_id = %s", (user_id,))`
* C) Hash the `user_id` value with SHA-256 before concatenating it into the SQL string
* D) Move the SQL query to a stored procedure in the database so the application does not handle raw SQL
* **Correct Answer:** B) Parameterized queries (also called prepared statements) separate SQL code from user-supplied data, making it structurally impossible for user input to alter the query's logic regardless of its content.
* **Distractor Analysis:**
  * *Why B is correct:* Parameterized queries pass user input as a bound parameter, not as part of the SQL text. The database driver handles escaping and type enforcement, completely eliminating SQL injection as an attack vector.
  * *Why A is incorrect:* Input validation (allow-listing numeric input) is a useful defense-in-depth measure but is not the root-cause fix. Validation can be bypassed or inconsistently applied; parameterized queries are structural and cannot be bypassed.
  * *Why C is incorrect:* Hashing the user ID would produce a hash string that is still concatenated into the SQL statement. If the attacker controls input that produces a specific hash (impractical but conceptually), the injection remains possible. More practically, a valid user_id hash would still be concatenated unsafely.
  * *Why D is incorrect:* Stored procedures can reduce exposure but do not eliminate SQL injection if the stored procedure itself concatenates user input into dynamic SQL. Parameterized queries within the application are the canonical fix.
