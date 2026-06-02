# Lab Activity: Module 06 - SAST: Static Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Run Semgrep SAST against vulnerable Python code and interpret the output.
- Analyze a SAST finding using the structured framework from the reading guide.
- Write remediated code that eliminates the vulnerability identified by the scanner.
- Integrate Semgrep into a GitHub Actions pipeline as a required security gate.

---

## Prerequisites

Before beginning this lab, confirm the following:

- Python 3.8 or later is installed (`python --version`).
- You have access to the GitHub repository from previous modules.
- Semgrep can be installed locally for Parts 1 and 2.

Install Semgrep locally:

```bash
pip install semgrep
semgrep --version
```

---

## Part 1: Analyze SAST Findings — SQL Injection (30 points)

### Part 1 Background

This is the core deliverable of Module 06. Given a vulnerable Python code sample and its Semgrep output, analyze the finding using the structured framework from the reading guide, then write the remediated code.

### Part 1 Vulnerable Code Sample

The following Python Flask application has a critical SQL injection vulnerability. Read it carefully.

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('app.db')
    return conn

@app.route('/products')
def search_products():
    category = request.args.get('category', '')
    conn = get_db()
    cursor = conn.cursor()
    query = "SELECT id, name, price FROM products WHERE category = '" + category + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)

@app.route('/admin/user')
def get_user():
    username = request.args.get('name')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    row = cursor.fetchone()
    conn.close()
    return jsonify(row)
```

### Part 1 SAST Finding Output

Semgrep produces the following findings when scanning this code:

```text
Finding 1:
/app/routes.py
  python.flask.security.injection.sql-injection.sql-injection
  Detected SQL injection. User-controlled data flows into a SQL query
  without sanitization.

  14 |  query = "SELECT id, name, price FROM products WHERE category = '" + category + "'"
      |  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Severity: ERROR
  CWE: CWE-89 (Improper Neutralization of Special Elements in SQL Commands)
  OWASP: A03:2021 - Injection

Finding 2:
/app/routes.py
  python.flask.security.injection.sql-injection.sql-injection
  Detected SQL injection. User-controlled data flows into a SQL query
  without sanitization.

  22 |  cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
      |  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Severity: ERROR
  CWE: CWE-89 (Improper Neutralization of Special Elements in SQL Commands)
  OWASP: A03:2021 - Injection
```

### Part 1 Instructions

**Step 1: Analyze Finding 1 using the structured framework.**

Write a structured analysis covering all six framework elements:

1. Finding description — what did the tool flag?
2. Vulnerability type — name the vulnerability class.
3. CWE and OWASP classification — cite the numbers.
4. Attack scenario — describe a specific attack an adversary would execute against the `/products` endpoint using this vulnerability. Include an example malicious input string.
5. Why SAST caught it — explain which analysis technique detected this finding.
6. Remediation — write the corrected `search_products()` function using parameterized queries.

**Step 2: Analyze Finding 2 using the structured framework.**

Write a structured analysis covering all six framework elements for the `/admin/user` endpoint finding. Note whether the attack surface differs from Finding 1 given the endpoint name.

**Step 3: Write the complete remediated version of the vulnerable file.**

Replace all vulnerable SQL patterns with parameterized queries. Your remediated file must pass Semgrep scanning with zero SQL injection findings.

### Part 1 Deliverable

Submit: your structured analysis for Finding 1 (covering all six elements), your structured analysis for Finding 2, and your complete remediated Python file.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Finding 1 analysis covers all six framework elements accurately | 12 |
| Finding 2 analysis covers all six framework elements accurately | 8 |
| Remediated file correctly uses parameterized queries for both routes | 8 |
| Remediated file would pass Semgrep scanning (no SQL injection patterns) | 2 |

---

## Part 2: Run Semgrep and Interpret Results (25 points)

### Part 2 Background

Running a SAST tool locally against provided vulnerable code and interpreting the output is a hands-on DevSecOps skill.

### Part 2 Instructions

**Step 1: Create the vulnerable code file.**

Save the vulnerable code from Part 1 as `vulnerable_routes.py` in your lab directory.

**Step 2: Run Semgrep with the OWASP Top 10 rule pack.**

```bash
semgrep --config p/owasp-top-ten vulnerable_routes.py
```

Record the complete output.

**Step 3: Run Semgrep with JSON output for pipeline integration simulation.**

```bash
semgrep --config p/owasp-top-ten --json vulnerable_routes.py > semgrep-results.json
```

Open `semgrep-results.json` and record the values of the following fields for Finding 1: `path`, `check_id`, `severity`, `message`, `line`.

**Step 4: Run Semgrep against your remediated file.**

```bash
semgrep --config p/owasp-top-ten remediated_routes.py
```

Record the output confirming zero SQL injection findings.

**Step 5: Explain the exit code significance.**

In 2-3 sentences, explain what happens to the Semgrep process exit code when findings are detected vs. when no findings are detected, and why this matters for CI/CD pipeline integration.

### Part 2 Deliverable

Submit: the full Semgrep output for the vulnerable file, the five JSON fields from the results file, the Semgrep output for the remediated file confirming zero findings, and your exit code explanation.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Semgrep output for vulnerable file is shown and correct | 8 |
| Five JSON fields are correctly extracted and recorded | 7 |
| Semgrep output for remediated file confirms zero findings | 6 |
| Exit code explanation is technically accurate | 4 |

---

## Part 3: GitHub Actions SAST Pipeline Integration (25 points)

### Part 3 Background

SAST is most valuable as a required CI/CD pipeline gate — not just a local tool.

### Part 3 Instructions

**Step 1: Add a SAST job to your GitHub Actions pipeline.**

Update your `full-pipeline.yml` from Module 03 to add a dedicated SAST step within the `security-scan` job. The step must:

- Use `returntocorp/semgrep-action@v1`.
- Configure the `config:` parameter to include `p/owasp-top-ten` and `p/python`.
- Run on every pull request.

**Step 2: Commit the vulnerable code to a feature branch and open a pull request.**

Add the `vulnerable_routes.py` file to your repository on a feature branch. Open a pull request to main. Observe the pipeline results in the GitHub Actions tab.

**Step 3: Document the pipeline gate behavior.**

Take a screenshot of the failed SAST step in GitHub Actions showing the SQL injection findings. Take a screenshot of the PR checks section showing the security-scan job as failing.

**Step 4: Replace the vulnerable file with the remediated version.**

Commit the `remediated_routes.py` to the same branch. Observe the pipeline results.

**Step 5: Document the passing pipeline.**

Take a screenshot of the passing SAST step and the passing PR checks.

### Part 3 Deliverable

Submit: your updated pipeline YAML with the SAST step, screenshots of the failed run (with SQL injection findings), and screenshots of the passing run.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| Pipeline YAML correctly adds Semgrep to the security-scan job | 8 |
| Screenshot shows failed SAST step with SQL injection findings | 7 |
| Screenshot shows passing SAST step after remediation | 6 |
| PR check screenshots show the security-scan job status in both states | 4 |

---

## Part 4: SAST Operational Concepts (20 points)

### Part 4 Instructions

Answer each question in 3-5 sentences using precise SAST and DevSecOps terminology.

**Question A:** A team introduces Semgrep to a production codebase that has 847 existing findings. The team lead proposes using `continue-on-error: true` in the GitHub Actions step for the first two weeks. Explain what this configuration does, why it is appropriate as an initial rollout strategy, and what the team should do after those two weeks.

**Question B:** A developer receives a Semgrep finding flagging a line of code as a potential path traversal vulnerability, but after reviewing the code they determine the input is validated by an earlier function call that Semgrep cannot see. Describe the correct way to handle this confirmed false positive, including the syntax needed in the code and what documentation is required to justify the suppression.

**Question C:** Explain the difference between SAST and DAST using a specific example: a cross-site scripting (XSS) vulnerability in a web application. Describe what each tool sees, what information each needs to run, and what stage of the CI/CD pipeline each belongs at.

### Part 4 Deliverable

Submit written answers to all three questions (3-5 sentences each). Label each answer with the question letter.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Question A correctly explains continue-on-error and the rollout strategy | 7 |
| Question B correctly describes suppression syntax and documentation requirement | 7 |
| Question C accurately distinguishes SAST and DAST with XSS example | 6 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (06) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
