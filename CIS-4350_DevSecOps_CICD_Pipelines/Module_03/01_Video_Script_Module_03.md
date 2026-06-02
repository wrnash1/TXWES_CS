# Video Script: Module 03 - CI/CD Concepts: Jenkins, GitHub Actions, GitLab CI

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 03 — CI/CD Concepts: Jenkins, GitHub Actions, GitLab CI"

**Audio:**

"Welcome back. I'm Professor Nash. In Module 02 we worked hands-on with Git and wrote our first GitHub Actions workflow. In this module we're going to zoom out and look at the CI/CD landscape more broadly — comparing GitHub Actions with Jenkins and GitLab CI, understanding the security characteristics of each, and writing a complete multi-stage pipeline with security gates built in.

By the end of this video you'll be able to compare the architecture of Jenkins, GitHub Actions, and GitLab CI, identify the security advantages and risks specific to each platform, and write a complete CI/CD pipeline YAML that includes build, test, security scan, and deploy stages. This entire module is exam-relevant — the DevSecOps Professional certification tests your ability to design and evaluate pipelines across multiple CI/CD platforms."

---

### [01:30 - 06:00] Jenkins: Architecture and Security Considerations

**Visual:** Jenkins architecture diagram — controller node, agent nodes, plugin ecosystem

**Audio:**

"Let's start with Jenkins — the most widely deployed open-source CI/CD system in the world, introduced in 2011. Understanding Jenkins is critical for the exam because the majority of enterprise CI/CD environments still run Jenkins, and many DevSecOps pipeline security questions are Jenkins-focused.

Jenkins uses a controller-agent architecture. The controller is the central server that manages jobs, plugins, configuration, and the web UI. Agents — sometimes called nodes or workers — are the machines where actual job steps execute. A Jenkins controller can manage hundreds of agents.

From a security perspective, Jenkins has several critical configuration points you must know for the exam.

**Authentication and authorization.** Jenkins ships with minimal security by default. In production, you configure an authentication provider — typically LDAP or SAML — and use the Role-Based Authorization Strategy plugin to enforce least privilege. The exam tests whether you know that Jenkins' 'Matrix-based security' allows granular permission assignment at the job, agent, and system level.

**Credentials management.** Jenkins has a built-in Credentials Manager for storing secrets. Credentials are stored encrypted and injected into pipeline steps via the `withCredentials()` block. Never use environment variables in Jenkinsfile to pass plaintext passwords — use the credentials() binding.

**Pipeline types.** Jenkins supports two pipeline models: Declarative (recommended, structured syntax starting with `pipeline {}`) and Scripted (Groovy-based, more flexible but harder to audit). For DevSecOps, declarative pipelines are preferred because their structured syntax is easier to review for security misconfigurations.

**Plugin risk.** Jenkins' extensibility through plugins is also its biggest attack surface. Every plugin is potential supply chain risk. The exam tests the principle of minimizing installed plugins to reduce attack surface and regularly updating plugins to remediate CVEs."

---

### [06:00 - 11:00] GitHub Actions vs. GitLab CI: Architecture Comparison

**Visual:** Side-by-side comparison table — GitHub Actions, GitLab CI, Jenkins

**Audio:**

"Now let's compare GitHub Actions and GitLab CI — the two platform-native CI/CD systems that have largely replaced Jenkins for new projects.

GitHub Actions, which we covered in Module 02, defines pipelines as YAML workflow files in `.github/workflows/`. Jobs run on GitHub-hosted runners or self-hosted runners. The Actions Marketplace provides thousands of community-built actions — which is both a convenience and a supply chain security risk.

GitLab CI defines pipelines in a single `.gitlab-ci.yml` file at the repository root. Jobs are organized into stages (build, test, deploy). GitLab Runners execute jobs — you can use GitLab-shared runners or register your own. GitLab's integrated security scanning features — SAST, DAST, dependency scanning, container scanning — are built directly into GitLab Ultimate and can be enabled by including pre-built templates.

**[SHOW CODE]**

Here is the same three-step workflow expressed in both GitHub Actions and GitLab CI format, so you can see the structural differences:

GitHub Actions format:

```yaml
name: Build and Test

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: pytest tests/
```

GitLab CI format:

```yaml
stages:
  - build
  - test

build-job:
  stage: build
  image: python:3.11-slim
  script:
    - pip install -r requirements.txt

test-job:
  stage: test
  image: python:3.11-slim
  script:
    - pip install -r requirements.txt
    - pytest tests/
```

Key structural difference: GitHub Actions organizes automation into jobs within a workflow file. GitLab CI organizes automation into jobs assigned to stages within a single pipeline file. Both support parallel execution within a stage and sequential progression between stages."

---

### [11:00 - 17:00] Writing a Complete Multi-Stage Security Pipeline

**Visual:** Complete pipeline YAML in code editor, stages labeled

**Audio:**

"Now let's build the most important pipeline of this module — a complete CI/CD pipeline that includes build, test, security scan, and deploy stages. This is the required lab pattern for this module, and this structure is what the exam expects you to understand.

**[SHOW CODE]**

Here is a complete GitHub Actions pipeline with all four stages:

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
    name: Build
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build application artifact
        run: python setup.py build

  test:
    name: Unit Tests
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run unit tests with coverage
        run: pytest tests/ --cov=src --cov-report=xml

  security-scan:
    name: Security Gates
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Secrets detection
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: SAST with Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/owasp-top-ten

      - name: Dependency vulnerability scan
        uses: snyk/actions/python@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  deploy:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: [test, security-scan]
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Deploy to staging environment
        run: ./scripts/deploy.sh staging
        env:
          DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
```

Let me walk through the critical design decisions.

The `needs:` keyword creates a dependency graph. `test` and `security-scan` both need `build` — so they run in parallel after build completes. `deploy` needs both `test` and `security-scan` — so it waits for both to pass before running. This means the security scan is on the critical path to deployment: if it fails, deployment is blocked.

The `if:` condition on the deploy job means deployment only runs on pushes to main, not on pull requests. This prevents every PR from deploying to staging — only merged, passing code deploys.

The `security-scan` job chains three security controls: secrets detection, SAST, and dependency scanning. All three must pass. If any fails, the job fails and the deploy job's `needs` dependency is not satisfied.

This is the DevSecOps pipeline pattern you must be able to explain and reconstruct on the exam."

---

### [17:00 - 20:30] Jenkins Declarative Pipeline with Security Stages

**Visual:** Jenkinsfile YAML/Groovy in code editor

**Audio:**

"Let's also see the equivalent pipeline in Jenkins Declarative syntax, because the exam tests both formats.

**[SHOW CODE]**

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python setup.py build'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/ --cov=src'
            }
        }

        stage('Security Scan') {
            parallel {
                stage('Secrets Detection') {
                    steps {
                        sh 'gitleaks detect --source . --exit-code 1'
                    }
                }
                stage('SAST') {
                    steps {
                        sh 'semgrep --config p/owasp-top-ten --error .'
                    }
                }
                stage('Dependency Check') {
                    steps {
                        dependencyCheck additionalArguments: '--scan ./', odcInstallation: 'OWASP-DC'
                        dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([string(credentialsId: 'deploy-key', variable: 'DEPLOY_KEY')]) {
                    sh './scripts/deploy.sh staging'
                }
            }
        }
    }

    post {
        failure {
            mail to: 'security@example.com',
                 subject: "Pipeline FAILED: ${env.JOB_NAME}",
                 body: "Security gate failure in build ${env.BUILD_URL}"
        }
    }
}
```

Notice the `parallel {}` block in the Security Scan stage — Jenkins can run the secrets detection, SAST, and dependency check simultaneously, reducing pipeline duration. Notice `withCredentials` — this is how Jenkins securely injects secrets into a step without exposing them in the log. The `post { failure {} }` block sends an alert on pipeline failure — important for security gate failures that need human attention."

---

### [20:30 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know the three CI/CD platforms, their file locations — `.github/workflows/` for GitHub Actions, `.gitlab-ci.yml` for GitLab CI, and `Jenkinsfile` for Jenkins — and their structural differences. Know that `needs:` in GitHub Actions and `stages:` in GitLab CI both control execution order. Know that security scan jobs should block the deploy job via the dependency graph. Know `withCredentials` in Jenkins and `${{ secrets.SECRET_NAME }}` in GitHub Actions as the correct credential injection patterns.

Complete the lab, which requires writing a full four-stage pipeline YAML. See you in Module 04."
