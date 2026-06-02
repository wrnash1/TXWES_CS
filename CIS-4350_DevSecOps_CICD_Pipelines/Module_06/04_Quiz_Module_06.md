# Quiz: Module 06 - SAST: Static Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

What is the fundamental difference between SAST and DAST?

- A) SAST runs on the production environment while DAST runs on the development environment
- B) SAST analyzes source code without executing the application, while DAST sends requests to a running application to find runtime vulnerabilities
- C) SAST detects vulnerabilities in third-party dependencies, while DAST detects vulnerabilities in first-party application code
- D) SAST requires a live database connection to perform analysis, while DAST runs entirely in memory

#### Q1 Correct Answer

B — SAST (Static Analysis) analyzes source code without execution — it finds vulnerability patterns at the code level. DAST (Dynamic Analysis) sends crafted HTTP requests to a running application and observes responses to find runtime vulnerabilities. SAST runs at PR/commit; DAST runs at staging.

#### Q1 Distractor Analysis

- *Why A is incorrect:* SAST runs at the earliest pipeline stages (commit, PR). DAST runs at staging after deployment. Neither runs exclusively in production or development.
- *Why C is incorrect:* Detecting third-party dependency vulnerabilities is SCA, not SAST or DAST.
- *Why D is incorrect:* SAST reads source code files from the filesystem. It does not require a database connection.

---

### Question 2

A Semgrep scan flags the following line of Python code. What vulnerability type does this finding represent?

```python
query = "SELECT * FROM accounts WHERE user = '" + request.args.get('user') + "'"
cursor.execute(query)
```

- A) Cross-Site Scripting (XSS) — user-controlled input is written to the HTML response
- B) SQL Injection — untrusted user input is concatenated directly into a SQL query string without parameterization
- C) Path Traversal — the user-controlled input is used to construct a filesystem path
- D) Command Injection — the user-controlled input is passed to an OS shell command

#### Q2 Correct Answer

B — The `request.args.get('user')` value is an HTTP query parameter (untrusted user input). It is concatenated directly into the SQL query string using the `+` operator. The database executes whatever SQL the attacker injects through the `user` parameter.

#### Q2 Distractor Analysis

- *Why A is incorrect:* XSS involves writing untrusted data to an HTML response. This code executes a SQL query, not an HTML response.
- *Why C is incorrect:* Path traversal involves constructing filesystem paths from user input. This code constructs a SQL query.
- *Why D is incorrect:* Command injection involves passing user input to OS shell functions like `os.system()`. This code passes to a SQL cursor's execute method.

---

### Question 3

Which remediation correctly fixes the SQL injection vulnerability from Question 2?

- A) Wrapping the query in a try/except block to catch SQL errors before they reach the user
- B) Using a parameterized query with a `?` placeholder and passing user input as a separate parameter tuple
- C) Converting the user input to uppercase before concatenating it into the query
- D) Checking that the user input is not empty before executing the query

#### Q3 Correct Answer

B — A parameterized query separates the SQL structure from the data. The database driver handles the user input as a data value, not as SQL syntax. An attacker cannot inject SQL commands through a parameterized parameter.

#### Q3 Distractor Analysis

- *Why A is incorrect:* A try/except block catches errors after the injection has already been attempted. It does not prevent SQL injection from occurring.
- *Why C is incorrect:* Converting to uppercase does not prevent SQL injection. SQL is case-insensitive and an attacker can construct effective injection payloads in any case.
- *Why D is incorrect:* Checking for empty input prevents a null value error but does not prevent injection. An attacker will provide a non-empty, malicious input.

---

### Question 4

A SAST tool is integrated into a pull request pipeline with `continue-on-error: true`. How does this affect the pipeline's behavior when the SAST tool finds a critical vulnerability?

- A) The pipeline fails immediately and the PR cannot be merged until the vulnerability is fixed
- B) The pipeline job reports the findings but exits successfully, allowing the PR to proceed and merge
- C) The pipeline pauses and waits for a security engineer to manually approve before continuing
- D) The SAST tool automatically applies the fix and recommits the corrected code

#### Q4 Correct Answer

B — `continue-on-error: true` makes the GitHub Actions step succeed regardless of the tool's exit code. SAST findings are reported in the log and any connected dashboard, but they do not cause the pipeline job to fail. The PR can merge despite findings. This is non-breaking mode.

#### Q4 Distractor Analysis

- *Why A is incorrect:* That describes breaking mode. `continue-on-error: true` is specifically the configuration that prevents the job from failing.
- *Why C is incorrect:* There is no built-in GitHub Actions "pause for approval" mechanism in this context. That would require an environment protection rule, not `continue-on-error`.
- *Why D is incorrect:* SAST tools are read-only analysis tools. They report findings but do not modify source code.

---

### Question 5

Which SAST tool is most appropriate for a highly regulated financial institution that needs deep interprocedural taint analysis across a large Java monolith with complex method call chains?

- A) Semgrep Community — because it has the largest community rule registry and free licensing
- B) Hadolint — because it integrates directly with Java build tools like Maven and Gradle
- C) Checkmarx — because it performs deep interprocedural taint analysis suited for complex enterprise codebases
- D) Grype — because it scans Java JAR files for CVEs in compiled bytecode

#### Q5 Correct Answer

C — Checkmarx is designed for enterprise environments with complex codebases. Its deep interprocedural taint analysis traces data flow across method calls, class boundaries, and module imports — essential for finding injection vulnerabilities in large Java monoliths where taint sources and sinks may be in different modules.

#### Q5 Distractor Analysis

- *Why A is incorrect:* Semgrep is excellent for most use cases but uses pattern matching with lighter taint analysis. For deep interprocedural analysis in a complex enterprise codebase, Checkmarx provides more thorough coverage.
- *Why B is incorrect:* Hadolint is a Dockerfile linter, not a Java source code SAST tool. It does not analyze Java code.
- *Why D is incorrect:* Grype scans artifacts for known CVEs in dependencies. It does not perform source code vulnerability analysis or taint analysis.

---

### Question 6

A developer finds a Semgrep finding that flags a line of code as a potential security issue. After careful review, they determine with certainty that the flagged code pattern cannot be exploited in this application's context. What is the correct way to handle this finding?

- A) Delete the code entirely since any flagged code should be removed
- B) Disable the Semgrep rule globally across the entire repository to prevent recurrence of this finding type
- C) Add a `# nosemgrep: rule-id` comment on the flagged line with a comment explaining why the finding is a false positive
- D) Ignore the finding permanently and instruct the team to filter it out of dashboard views

#### Q6 Correct Answer

C — A line-level suppression comment with the specific rule ID suppresses only that finding at that line. The rule remains active for all other code. A justification comment documents why the finding was reviewed and confirmed as a false positive, creating an audit trail.

#### Q6 Distractor Analysis

- *Why A is incorrect:* Code that is functionally correct and confirmed not exploitable should not be deleted. The SAST tool's judgment about exploitability is not infallible.
- *Why B is incorrect:* Disabling a rule globally removes protection for all other locations where the same vulnerability pattern might genuinely exist.
- *Why D is incorrect:* Silently ignoring findings without documentation creates no audit trail and allows future team members to be unaware that the finding was reviewed.

---

### Question 7

A SonarQube quality gate is configured with the rule: "No new Critical vulnerabilities." A pull request adds three new files with two new Critical SAST findings. What happens when the PR is analyzed?

- A) The PR can be merged because new findings only count against the next sprint's quality metrics
- B) The quality gate fails, blocking the PR from merging until the two Critical findings are remediated
- C) The quality gate sends a warning email but does not block the merge
- D) SonarQube automatically increases the severity threshold to accommodate the new findings

#### Q7 Correct Answer

B — SonarQube quality gates evaluate the current code change against configured thresholds. Two new Critical findings violate the "no new Critical vulnerabilities" rule. The quality gate fails, and SonarQube reports a failure status to the CI/CD pipeline, blocking the PR merge through the branch protection required status check.

#### Q7 Distractor Analysis

- *Why A is incorrect:* SonarQube quality gates are evaluated on each analysis run. Findings do not carry over to future sprints — they must be remediated in the current change or the gate fails.
- *Why C is incorrect:* A quality gate failure blocks merging when properly integrated with branch protection required status checks. It is not merely advisory.
- *Why D is incorrect:* SonarQube does not automatically adjust quality gate thresholds. Thresholds are configured by the team and remain fixed until deliberately changed.

---

### Question 8

Which CWE number corresponds to SQL Injection vulnerabilities?

- A) CWE-79
- B) CWE-22
- C) CWE-89
- D) CWE-798

#### Q8 Correct Answer

C — CWE-89 is "Improper Neutralization of Special Elements used in an SQL Command (SQL Injection)." This is one of the most common and highest-priority vulnerabilities detected by SAST tools.

#### Q8 Distractor Analysis

- *Why A is incorrect:* CWE-79 is Cross-Site Scripting (XSS) — improper neutralization of input during web page generation.
- *Why B is incorrect:* CWE-22 is Path Traversal — improper limitation of a pathname to a restricted directory.
- *Why D is incorrect:* CWE-798 is Use of Hard-coded Credentials — embedding passwords or cryptographic keys directly in source code.

---

### Question 9

A security team wants to ensure that SAST covers the OWASP Top 10 vulnerability categories. Which Semgrep configuration parameter addresses this requirement most directly?

- A) `config: p/secrets` — scans for hardcoded credentials and API keys
- B) `config: p/owasp-top-ten` — uses the community rule pack mapped to OWASP Top 10 categories
- C) `config: auto` — automatically selects rules based on the detected programming language
- D) `config: p/python` — uses all Python-specific rules regardless of vulnerability category

#### Q9 Correct Answer

B — The `p/owasp-top-ten` Semgrep rule pack is specifically curated to cover the OWASP Top 10 web application security risk categories: Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, and others.

#### Q9 Distractor Analysis

- *Why A is incorrect:* `p/secrets` specifically targets hardcoded credentials and API keys. It covers OWASP A07 (authentication failures) but not the full Top 10.
- *Why C is incorrect:* `auto` selects rules based on language detection, not vulnerability category coverage. It may not cover all OWASP Top 10 categories for a given language.
- *Why D is incorrect:* `p/python` covers Python-specific coding patterns, but is not organized around OWASP Top 10 categories.

---

### Question 10

A developer is performing taint analysis mentally before running a SAST tool. They identify this code path. What is the taint source, the sink, and the missing control?

```python
filename = request.form.get('document_name')
with open(f'/app/documents/{filename}', 'rb') as f:
    return f.read()
```

- A) Source: `/app/documents/` path string. Sink: `open()` call. Missing control: directory existence check
- B) Source: `request.form.get('document_name')`. Sink: `open()` call with constructed path. Missing control: path validation to prevent traversal outside `/app/documents/`
- C) Source: `f.read()` return value. Sink: the HTTP response. Missing control: response encryption
- D) Source: `/app/documents/` directory. Sink: `request.form`. Missing control: CSRF token verification

#### Q10 Correct Answer

B — The taint source is the HTTP form parameter `document_name` (untrusted user input). It flows into an f-string that constructs a filesystem path. The sink is the `open()` call. Without path validation, an attacker can provide `../../etc/passwd` as the filename, traversing out of the intended directory. This is a Path Traversal vulnerability (CWE-22).

#### Q10 Distractor Analysis

- *Why A is incorrect:* The static path string `/app/documents/` is not tainted — it is hardcoded. The taint comes from the form input, not the path prefix.
- *Why C is incorrect:* `f.read()` reads file content — it is not a taint source in this context. The taint source is the user-controlled `filename` parameter.
- *Why D is incorrect:* The taint flow runs from the request form input to the file open call, not in the reverse direction. CSRF token verification addresses a different vulnerability class.
