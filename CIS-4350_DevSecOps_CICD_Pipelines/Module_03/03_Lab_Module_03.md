# Lab Activity: Module 03 - CI/CD Concepts: Jenkins, GitHub Actions, GitLab CI

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Write a complete multi-stage CI/CD pipeline YAML with build, test, security-scan, and deploy stages.
- Explain the job dependency graph that ensures security gates block deployment on failure.
- Compare the same pipeline logic expressed in GitHub Actions and GitLab CI syntax.
- Analyze a Jenkins Declarative pipeline for security misconfigurations.

---

## Prerequisites

Before beginning this lab, confirm the following:

- You have completed the Module 03 video and reading guide.
- You have a GitHub account and the repository from Module 02 available.
- You are familiar with the GitHub Actions workflow syntax from Module 02.

---

## Part 1: Write a Complete CI/CD Pipeline YAML (40 points)

### Part 1 Background

This part requires you to write the complete four-stage pipeline that is the core deliverable of Module 03. The pipeline must include build, test, security-scan, and deploy stages. The security-scan job must be on the critical path to deployment — if any security check fails, the deploy job must not run.

### Part 1 Instructions

**Step 1: Write the complete GitHub Actions pipeline.**

Create `.github/workflows/full-pipeline.yml` in your lab repository. The pipeline must satisfy all requirements below:

Requirements:

- Triggers on both `pull_request` to main and `push` to main.
- Sets `permissions: contents: read` and `security-events: write` at the workflow level.
- Has four jobs: `build`, `test`, `security-scan`, and `deploy`.
- The `test` job has `needs: build`.
- The `security-scan` job has `needs: build` (runs in parallel with test).
- The `deploy` job has `needs: [test, security-scan]`.
- The `deploy` job only runs on pushes to main (not on pull requests) using an `if:` condition.
- The `security-scan` job includes at minimum: a secrets detection step and a SAST step.
- All steps have descriptive `name:` values.
- No plaintext credentials appear anywhere in the YAML — all secrets use `${{ secrets.NAME }}` syntax.

The pipeline must follow this structure:

```yaml
name: Full CI/CD Pipeline with Security Gates

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read
  security-events: write

jobs:
  build:
    # Complete this job

  test:
    needs: build
    # Complete this job

  security-scan:
    needs: build
    # Complete this job with at least 2 security steps

  deploy:
    needs: [test, security-scan]
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    # Complete this job
```

**Step 2: Push the workflow to GitHub and verify it runs on a pull request.**

Create a feature branch, push the workflow file, and open a pull request to main. Navigate to the Actions tab and confirm that build, test, and security-scan jobs run on the PR. Confirm that deploy does NOT run on the PR.

**Step 3: Merge the PR and verify deploy runs on push to main.**

After all PR checks pass, merge the pull request. In the Actions tab, confirm that the push-to-main trigger fires and the deploy job runs this time.

### Part 1 Deliverable

Submit: your complete `full-pipeline.yml` file, a screenshot of the PR check run showing build/test/security-scan passing and deploy not running, and a screenshot of the post-merge run showing all four jobs including deploy.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Pipeline YAML is syntactically correct and complete | 10 |
| All four jobs present with correct `needs:` dependencies | 10 |
| Security-scan has at least two distinct security steps | 8 |
| Deploy `if:` condition correctly limits to main push only | 6 |
| PR screenshot shows deploy not running | 3 |
| Post-merge screenshot shows all four jobs running | 3 |

---

## Part 2: GitLab CI Equivalent Pipeline (25 points)

### Part 2 Background

The DevSecOps Professional exam tests your ability to work across CI/CD platforms. This part requires translating your GitHub Actions pipeline into GitLab CI syntax.

### Part 2 Instructions

**Step 1: Write the equivalent pipeline in GitLab CI syntax.**

Create a file named `gitlab-ci-equivalent.yml` (you do not need to run this — submit the file). The pipeline must define the same four stages and security controls as your GitHub Actions pipeline in Part 1, expressed in GitLab CI syntax.

Requirements:

- Define `stages:` array with four stages: `build`, `test`, `security`, `deploy`.
- Build job runs `pip install -r requirements.txt`.
- Test job runs `pytest tests/`.
- Security stage includes two separate jobs: one for secrets detection, one for SAST.
- Deploy job uses `rules:` to restrict deployment to the main branch only.
- All jobs specify a Docker image using the `image:` keyword.
- Credentials use environment variable syntax (`$VARIABLE_NAME`), not plaintext.

**Step 2: Write a comparison table.**

Create a table with two columns — GitHub Actions syntax element and GitLab CI equivalent — covering these items:

- Job dependencies (ordering between stages)
- Parallel job execution within a stage
- Credential injection
- Branch-conditional execution
- Runner/executor specification

### Part 2 Deliverable

Submit your `gitlab-ci-equivalent.yml` file and the comparison table.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Stages array is correctly defined | 4 |
| All four stage jobs are present with correct stage assignment | 8 |
| Security stage has two parallel jobs in the same stage | 5 |
| Deploy job uses `rules:` to restrict to main branch | 4 |
| Comparison table covers all five required items accurately | 4 |

---

## Part 3: Jenkins Pipeline Security Analysis (20 points)

### Part 3 Background

The Jenkins Declarative pipeline below contains several security misconfigurations. Analyze it and provide a detailed remediation plan.

### Part 3 Scenario

Review the following Jenkinsfile:

```groovy
pipeline {
    agent any

    environment {
        DB_PASSWORD = "MyP@ssw0rd123"
        AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        DEPLOY_ENV = "production"
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Deploy') {
            steps {
                sh './scripts/deploy.sh ${DEPLOY_ENV}'
            }
        }
    }
}
```

### Part 3 Instructions

**Step 1: Identify all security problems.**

List every security misconfiguration in the Jenkinsfile above. For each problem, state: what the misconfiguration is, what the risk is, and which DevSecOps principle it violates.

You must identify at least four distinct problems.

**Step 2: Write the corrected Jenkinsfile.**

Rewrite the complete Jenkinsfile with all security problems fixed. Use `withCredentials()` for secrets. Add a Security Scan stage between Build and Deploy. Restrict deployment to the main branch using a `when` condition.

**Step 3: Explain the withCredentials pattern.**

In 3-4 sentences, explain how `withCredentials()` protects secrets compared to environment variables in the `environment {}` block. Specifically explain what happens to the secret value in the Jenkins build log.

### Part 3 Deliverable

Submit: your list of security problems with analysis, your corrected Jenkinsfile, and your `withCredentials()` explanation.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| At least 4 security problems identified with accurate risk analysis | 10 |
| Corrected Jenkinsfile uses withCredentials and adds Security Scan stage | 6 |
| withCredentials explanation is technically accurate | 4 |

---

## Part 4: Pipeline Design Justification (15 points)

### Part 4 Instructions

Write a 200-250 word technical justification for the following pipeline design decision:

"The security-scan job is placed in parallel with the test job rather than sequentially after it, and both are required by the deploy job."

Your justification must address:

1. The performance benefit of running security-scan and test in parallel rather than sequentially.
2. Why both must be required by the deploy job rather than having deploy depend only on test.
3. A scenario where this design catches a security issue that would have been missed if security-scan ran after deploy.

### Part 4 Deliverable

Submit your written justification (200-250 words) as part of your combined submission document.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Performance benefit of parallelism is accurately explained | 5 |
| Necessity of both jobs blocking deploy is correctly justified | 5 |
| Scenario correctly illustrates why sequential post-deploy scanning is insufficient | 5 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (03) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.
