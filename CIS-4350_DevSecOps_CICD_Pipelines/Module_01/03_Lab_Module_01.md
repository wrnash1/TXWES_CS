# Lab Activity: Module 01 - DevOps Fundamentals and the DevSecOps Mindset

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Construct a complete DevSecOps pipeline security map that places each tool class at the correct SDLC stage.
- Analyze a sample GitHub Actions workflow and identify where security gates are missing.
- Calculate the relative cost impact of late-stage vulnerability discovery.
- Explain the shared responsibility model for a described organizational scenario.

---

## Prerequisites

Before beginning this lab, confirm the following:

- You have access to a text editor or word processor for written deliverables.
- You have a GitHub account (free tier is sufficient) for Part 3.
- You have completed the Module 01 video and reading guide.
- You have read the OWASP DevSecOps Guideline introduction at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).

---

## Part 1: DevSecOps Pipeline Security Map (30 points)

### Part 1 Background

A DevSecOps pipeline is only as strong as the security controls embedded within it. Your first task is to construct a complete security map for a standard CI/CD pipeline, justifying each control placement using shift-left principles.

### Part 1 Instructions

**Step 1: Fill in the pipeline security map.**

Using the template below, complete the Security Activity, Tool Examples, and Shift-Left Justification columns for each stage. Submit this as a completed table in a document or a filled-in Markdown table.

| Pipeline Stage | Security Activity | Tool Examples | Shift-Left Justification |
|---|---|---|---|
| Developer workstation (pre-commit) | | | |
| Code commit / Pull request | | | |
| Build (dependency download) | | | |
| Container image build | | | |
| Staging environment (deployed app) | | | |
| IaC provisioning | | | |
| Production runtime | | | |

**Step 2: Annotate the cost curve.**

On a separate page or section, sketch or describe the SDLC vulnerability cost curve. Mark where each security activity from your table intercepts the curve. Write 2-3 sentences explaining why catching a vulnerability at the pre-commit stage is less expensive than catching it at the staging or production stage.

**Step 3: Identify two non-automated security activities.**

Name two DevSecOps security activities that are not automated pipeline scans — such as threat modeling or manual penetration testing. For each, state: (a) where in the SDLC it belongs, (b) why it cannot be fully automated, and (c) how it complements the automated controls in your pipeline map.

### Part 1 Deliverable

Submit your completed pipeline map table, cost curve annotation, and non-automated activity analysis as a single document (PDF, Word, or Markdown).

### Part 1 Rubric

| Criterion | Points |
|---|---|
| All 7 pipeline stages have a correct security activity and tool example | 14 |
| Shift-left justification is technically accurate for each stage | 7 |
| Cost curve annotation is correct and written explanation is clear | 5 |
| Two non-automated activities are correctly identified and explained | 4 |

---

## Part 2: Vulnerability Cost Analysis (25 points)

### Part 2 Background

The economic case for shift-left security is a frequently tested topic on the DevSecOps Professional exam. This exercise reinforces the cost multiplier concept with a realistic scenario.

### Part 2 Scenario

Your team ships a web application using a Python Flask backend. A developer accidentally commits a hardcoded AWS access key to the GitHub repository. The timeline below describes discovery at three different pipeline stages:

- **Stage A — Pre-commit hook:** Developer notices immediately, removes the key from the staged file before the commit is finalized. Cost: 10 minutes of developer time.
- **Stage B — CI pipeline SAST scan on pull request:** Scan flags the hardcoded credential. Developer must fix, recommit, and re-run the pipeline. Cost: 45 minutes of developer time plus 10 minutes of pipeline runtime.
- **Stage C — Production security audit six months later:** Auditor finds the key in Git history. The key has been active and potentially exposed for 6 months. Required response: revoke and rotate the key in all environments, search CloudTrail logs for unauthorized API calls, file a security incident report, notify management, conduct a lessons-learned meeting. Cost: 3 days of developer time + 1 day of security team time + 1 day of operations team time.

### Part 2 Instructions

**Step 1: Calculate dollar cost per stage.**

Assume developer time costs $75/hour, security team time costs $100/hour, and operations team time costs $90/hour. Calculate the total dollar cost for Stage A, Stage B, and Stage C. Show your arithmetic.

**Step 2: Compute the cost multipliers.**

Calculate how many times more expensive Stage C is compared to Stage A. Then calculate how many times more expensive Stage C is compared to Stage B.

**Step 3: Write a recommendation memo.**

In 100-150 words, write a memo addressed to a development team manager explaining why investing in pre-commit and CI pipeline secret scanning is economically justified based on your calculations. Use the specific dollar figures from Step 1.

### Part 2 Deliverable

Submit a document containing your Stage A/B/C cost calculations with arithmetic shown, the cost multiplier calculations, and the recommendation memo.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Stage A, B, and C costs calculated correctly with arithmetic shown | 9 |
| Cost multipliers calculated correctly | 6 |
| Recommendation memo is technically accurate and uses calculated figures | 7 |
| Memo is professional in tone and within the 100-150 word target | 3 |

---

## Part 3: Analyze a GitHub Actions Workflow (30 points)

### Part 3 Background

The following GitHub Actions workflow is used by a small development team. It runs on every push to `main`. Read the workflow carefully and answer the questions that follow.

**[SHOW CODE]**

```yaml
name: Build and Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run unit tests
        run: pytest tests/

      - name: Build Docker image
        run: docker build -t myapp:latest .

      - name: Push to registry
        run: |
          docker login -u ${{ secrets.DOCKER_USER }} -p ${{ secrets.DOCKER_PASS }}
          docker push myapp:latest

      - name: Deploy to production
        run: ./scripts/deploy.sh production
```

### Part 3 Instructions

**Step 1: Identify missing security gates.**

List all DevSecOps security controls that are absent from this workflow. For each missing control, state: the control type (SAST, SCA, secrets scan, container scan, etc.), where in the workflow it should be inserted (before or after which step), and why its absence represents a risk. You must identify at least five missing controls.

**Step 2: Write the improved workflow.**

Rewrite the complete workflow YAML adding the missing security gates you identified in Step 1. Add a comment above each new security step explaining its purpose.

```yaml
# Write your improved workflow here
```

**Step 3: Explain the trigger gap.**

The workflow runs only on `push` to `main`. Explain why this trigger design is a DevSecOps problem. Describe the better trigger strategy and what additional protection it provides.

### Part 3 Deliverable

Submit your list of missing controls, improved workflow YAML, and trigger gap explanation as a single document.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| At least 5 missing controls correctly identified with accurate risk explanation | 15 |
| Improved YAML is syntactically correct with controls at the right stages | 10 |
| Trigger gap explanation is technically accurate | 5 |

---

## Part 4: Shared Responsibility Scenario (15 points)

### Part 4 Scenario

A mid-size SaaS company has three teams: Development (builds features), Operations (manages infrastructure), and Security (conducts audits and pen tests). They currently have no CI/CD pipeline security automation. After a production data breach caused by a SQL injection vulnerability, the CTO asks: "Whose fault is this, and what should each team do differently?"

### Part 4 Instructions

Write a structured response of 200-250 words that addresses all five points below:

1. Explain why assigning blame to a single team misunderstands the DevSecOps shared responsibility model.
2. Identify what the Development team should have done differently, specifying one concrete technical control.
3. Identify what the Operations team should have done differently, specifying one concrete technical control.
4. Identify what the Security team should have done differently, specifying one concrete change to their process or tooling.
5. Describe how a feedback loop improvement would prevent the same class of vulnerability from recurring.

### Part 4 Deliverable

Submit your structured response addressing all five numbered points. Include your name, date, course number, and module number at the top of the document.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Correctly reframes blame using the shared responsibility model | 3 |
| Development team recommendation is technically specific and correct | 3 |
| Operations team recommendation is technically specific and correct | 3 |
| Security team recommendation is technically specific and correct | 3 |
| Feedback loop improvement is accurately described | 3 |

---

## Submission Instructions

Combine all four parts into a single submission document. Label each part clearly. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
