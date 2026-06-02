# Reading Guide: Module 03 - CI/CD Concepts: Jenkins, GitHub Actions, GitLab CI

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 03 broadens the CI/CD perspective from GitHub Actions alone to the three most widely used pipeline platforms in enterprise DevSecOps: Jenkins, GitHub Actions, and GitLab CI. Understanding the architectural differences, security characteristics, and pipeline syntax of each platform is a high-weight topic on the DevSecOps Professional exam. This reading guide provides the comparison tables, configuration references, and exam tips needed to answer scenario-based questions about pipeline design across platforms.

---

## Section 1: High-Yield Glossary

**Continuous Integration (CI)** — The practice of automatically building and testing every code commit, providing rapid feedback on whether the change integrates correctly with the existing codebase.

**Continuous Delivery (CD)** — An extension of CI where every passing build is automatically prepared for deployment to a production-like environment. A human approval step precedes actual production deployment.

**Continuous Deployment** — An extension of CD where every passing build is automatically deployed to production without manual approval. Requires high confidence in automated testing and security gates.

**Pipeline** — The ordered sequence of automated stages (build, test, scan, deploy) that a code change passes through from commit to deployment.

**Stage** — A logical grouping of pipeline jobs. In GitLab CI and Jenkins, stages execute sequentially while jobs within a stage run in parallel. In GitHub Actions, stages are approximated with `needs:` dependencies between jobs.

**Job** — The unit of work in a CI/CD pipeline. A job runs on a specific runner or agent and contains one or more steps or script commands.

**Agent (Jenkins) / Runner (GitHub Actions, GitLab CI)** — The compute environment that executes pipeline jobs. May be shared (hosted by the platform) or self-hosted (managed by the organization).

**Jenkinsfile** — A text file defining a Jenkins pipeline, stored in the root of the source code repository. Supports Declarative (structured, recommended) and Scripted (Groovy-based, flexible) syntax.

**Declarative Pipeline** — The recommended Jenkins pipeline syntax. Uses a structured `pipeline {}` block with predefined sections: agent, stages, stage, steps, post. More readable and auditable than Scripted Pipelines.

**Scripted Pipeline** — The original Jenkins pipeline syntax. Written in Groovy, more flexible but harder to review for security misconfigurations due to arbitrary code execution capability.

**GitLab Runner** — The process that executes GitLab CI jobs. Can run as a shared runner (managed by GitLab.com), group runner, or project-specific runner. Supports Docker, shell, Kubernetes, and other executors.

**GitLab CI template** — A reusable pipeline definition that can be included in `.gitlab-ci.yml` using the `include:` keyword. GitLab provides pre-built security scanning templates (SAST, DAST, dependency scanning) that add security jobs to any pipeline with a single line.

**`needs:` keyword (GitHub Actions)** — Defines explicit job dependencies in a GitHub Actions workflow. A job with `needs: [job-a, job-b]` will not start until both job-a and job-b complete successfully.

**`parallel {}` block (Jenkins)** — Executes multiple Jenkins stages simultaneously within a single parent stage, reducing total pipeline duration.

**`withCredentials` (Jenkins)** — A Jenkins pipeline step that securely injects stored credentials into a block of steps as environment variables. Credentials are masked in build logs.

**SAST template (GitLab)** — A built-in GitLab CI template that adds SAST scanning to a pipeline by including `template: Security/SAST.gitlab-ci.yml`. Available in GitLab Ultimate.

**Supply chain attack (CI/CD context)** — An attack that compromises the pipeline by injecting malicious code into a shared action, plugin, or dependency used by the pipeline itself. Mitigated by pinning actions to commit SHAs and auditing third-party plugins.

---

## Section 2: CI/CD Platform Comparison

| Dimension | Jenkins | GitHub Actions | GitLab CI |
|---|---|---|---|
| Pipeline file | Jenkinsfile | `.github/workflows/*.yml` | `.gitlab-ci.yml` |
| Pipeline syntax | Declarative (Groovy DSL) or Scripted Groovy | YAML | YAML |
| Hosted runners | Self-hosted only | GitHub-hosted or self-hosted | GitLab-shared or self-hosted |
| Plugin ecosystem | 1,800+ plugins (attack surface) | Actions Marketplace | GitLab built-in + community |
| Built-in security scanning | Via plugins (OWASP DC, SonarQube) | Via Actions Marketplace | Built-in SAST/DAST templates (Ultimate) |
| Credentials storage | Jenkins Credentials Manager | GitHub Secrets | GitLab CI/CD Variables |
| Credential injection | `withCredentials()` block | `${{ secrets.NAME }}` | `$VARIABLE_NAME` in script |
| Stage parallelism | `parallel {}` block | `needs:` dependency graph | Jobs in same stage run in parallel |
| Pipeline-as-Code | Yes (Jenkinsfile in repo) | Yes (YAML in repo) | Yes (YAML in repo) |
| Deployment gates | `when { branch 'main' }` | `if:` condition on job | `only:` / `rules:` on job |
| Supply chain risk | Plugin vulnerabilities | Malicious Marketplace Actions | Included templates, dependencies |

---

## Section 3: Pipeline Stage Comparison — Security Gate Placement

The following table shows how security gates map to pipeline stages across the three platforms. The gate placement is identical conceptually; only the syntax differs.

| Security Gate | Jenkins Stage | GitHub Actions Job | GitLab CI Job |
|---|---|---|---|
| Secrets detection | Security Scan stage, parallel | `security-scan` job, pre-deploy | `secret-detection` job, test stage |
| SAST | Security Scan stage, parallel | `security-scan` job | `sast` job, test stage |
| SCA / dependency check | Security Scan stage, parallel | `security-scan` job | `dependency-scanning` job, test stage |
| Container image scan | Deploy Prep stage | Separate `container-scan` job | `container-scanning` job |
| DAST | Post-deploy stage (staging) | Separate `dast` job | `dast` job, staging stage |
| IaC scan | Pre-deploy stage | `iac-scan` job | `iac-security` job |

---

## Section 4: GitHub Actions Multi-Job Pipeline Structure Reference

A multi-stage pipeline in GitHub Actions uses job dependencies via `needs:` to enforce sequential execution between stages while allowing parallel execution within a stage. The security-critical rule: the deploy job must `needs:` both the test job and the security-scan job. If either fails, deployment is blocked.

```yaml
jobs:
  build:
    # runs first, no dependencies
  test:
    needs: build
    # runs after build
  security-scan:
    needs: build
    # runs in parallel with test, after build
  deploy:
    needs: [test, security-scan]
    # runs only after BOTH test and security-scan pass
    if: github.ref == 'refs/heads/main'
```

---

## Section 5: Jenkins Declarative Pipeline Structure Reference

A Jenkins Declarative pipeline organizes work into sequential stages. Security stages should appear before deploy stages. The `parallel {}` block allows multiple security scans to run simultaneously within one stage.

```groovy
pipeline {
    agent any
    stages {
        stage('Build')   { steps { /* build commands */ } }
        stage('Test')    { steps { /* test commands */ } }
        stage('Security Scan') {
            parallel {
                stage('Secrets') { steps { /* gitleaks */ } }
                stage('SAST')    { steps { /* semgrep  */ } }
                stage('SCA')     { steps { /* snyk     */ } }
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps { /* deploy commands */ }
        }
    }
    post {
        failure { /* notify security team */ }
    }
}
```

---

## Section 6: GitLab CI Pipeline Structure Reference

GitLab CI uses stages defined at the top of `.gitlab-ci.yml`. Jobs assigned to the same stage run in parallel; stages execute sequentially.

```yaml
stages:
  - build
  - test
  - security
  - deploy

build-job:
  stage: build
  script: [pip install -r requirements.txt]

test-job:
  stage: test
  script: [pytest tests/]

sast:
  stage: security
  include:
    - template: Security/SAST.gitlab-ci.yml

dependency-scan:
  stage: security
  include:
    - template: Security/Dependency-Scanning.gitlab-ci.yml

deploy-staging:
  stage: deploy
  script: [./scripts/deploy.sh staging]
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

---

## Section 7: SAST vs. DAST vs. SCA Comparison

| Dimension | SAST | DAST | SCA |
|---|---|---|---|
| Full name | Static Application Security Testing | Dynamic Application Security Testing | Software Composition Analysis |
| Requires running application | No | Yes | No |
| Primary target | First-party source code | Running application endpoints | Third-party dependencies |
| Pipeline stage | Commit / Pull request | Staging | Build |
| Finds | Insecure code patterns | Runtime flaws, auth issues | Known CVEs in libraries |
| Representative tools | Semgrep, SonarQube, Checkmarx | OWASP ZAP, Burp Suite Enterprise | Snyk, OWASP Dependency-Check |

---

## Section 8: Jenkins Security Configuration Reference

Jenkins requires explicit security hardening after installation. Key settings for the exam:

- Enable security on first launch — configure an admin account immediately.
- Use LDAP or SAML for authentication in enterprise environments.
- Install Role-Based Authorization Strategy plugin for fine-grained permissions.
- Disable Script Console access for non-admin users (Groovy execution risk).
- Use Credentials Manager with `withCredentials()` — never store secrets as plaintext environment variables.
- Restrict Groovy sandbox execution for untrusted Scripted Pipelines.
- Update all plugins regularly — Jenkins CVEs are frequently published.
- Minimize installed plugins — every plugin is potential attack surface.

---

## Section 9: Supply Chain Risk in CI/CD Pipelines

Supply chain attacks targeting CI/CD pipelines are a growing threat. Key exam topics:

- **GitHub Actions pinning** — Pin third-party actions to a commit SHA (e.g., `uses: actions/checkout@a5ac7e5`) rather than a mutable tag (`@v4`) to prevent a compromised tag from delivering malicious code.
- **Jenkins plugin vetting** — Only install plugins from the official Jenkins update center. Review plugin source code for sensitive API access before installation.
- **GitLab template verification** — Community-contributed templates should be reviewed before inclusion. GitLab's official security templates (under `Security/`) are maintained by GitLab and are safe to include.
- **Poisoned pipeline execution** — An attacker with write access to a branch can modify the pipeline YAML to exfiltrate secrets or deploy malicious artifacts. Restrict who can modify pipeline files.

---

## Section 10: DevSecOps Professional Exam Tips

1. **Pipeline file locations** — Know the exact file path for each platform: `.github/workflows/*.yml`, `.gitlab-ci.yml`, `Jenkinsfile`. The exam tests this directly.

2. **Stage execution order** — In GitLab CI, stages defined in the `stages:` array execute sequentially. Jobs within the same stage execute in parallel. In GitHub Actions, parallelism is controlled by `needs:` dependencies.

3. **Deploy gate pattern** — Know that the deploy job must depend on both test and security-scan jobs. If security-scan is not in the `needs:` list, failing security scans do not block deployment.

4. **`withCredentials` vs. environment variables** — In Jenkins, `withCredentials()` is the secure pattern. Plaintext env vars in Jenkinsfiles are a security misconfiguration. The exam tests this distinction.

5. **GitLab include templates** — Know that `include: template: Security/SAST.gitlab-ci.yml` adds SAST to a GitLab pipeline with one line. This is a common correct answer for "how do you add SAST to a GitLab pipeline" questions.

6. **Declarative vs. Scripted** — Know that Declarative Jenkins pipelines are preferred for DevSecOps because their structured syntax is auditable. Scripted pipelines allow arbitrary Groovy execution, which is a security risk.

7. **`if:` condition on GitHub Actions deploy job** — Know that `if: github.ref == 'refs/heads/main' && github.event_name == 'push'` restricts deployment to main-branch pushes only, preventing PR-triggered deployments.

8. **Supply chain pin pattern** — Know that pinning to a commit SHA is more secure than pinning to a tag. Tags are mutable; commit SHAs are immutable.

---

## Section 11: Study Checklist

- [ ] Explain the structural difference between GitHub Actions workflow jobs and GitLab CI stages.
- [ ] List the Jenkins Declarative pipeline sections in order: pipeline, agent, stages, stage, steps, post.
- [ ] Explain why `needs: [test, security-scan]` on the deploy job makes security scanning mandatory.
- [ ] Describe the `withCredentials()` pattern and why it is preferred over plaintext env vars in Jenkins.
- [ ] Explain what a supply chain attack on a CI/CD pipeline looks like and how action pinning mitigates it.
- [ ] Reconstruct the GitLab CI `stages:` pattern for a four-stage pipeline from memory.
- [ ] Read the OWASP DevSecOps Guideline CI/CD integration section at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
- [ ] Complete the Module 03 lab activity (full four-stage pipeline YAML).
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
