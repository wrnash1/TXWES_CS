# Quiz: Module 03 - CI/CD Concepts: Jenkins, GitHub Actions, GitLab CI

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

In a GitHub Actions workflow, a `deploy` job is configured with `needs: [test, security-scan]`. What is the security significance of this dependency configuration?

- A) It ensures the deploy job runs at the same time as the test and security-scan jobs, reducing total pipeline duration
- B) It prevents the deploy job from running unless both the test and security-scan jobs complete successfully, making security checks mandatory on the critical path to deployment
- C) It causes the deploy job to skip if either the test or security-scan job fails, but the workflow still reports an overall success
- D) It copies the artifacts produced by the test and security-scan jobs into the deploy job's workspace automatically

#### Q1 Correct Answer

B — `needs:` in GitHub Actions creates a dependency requiring that listed jobs complete successfully. If `security-scan` fails, the `deploy` job is skipped and the workflow fails, preventing deployment of insecure code.

#### Q1 Distractor Analysis

- *Why A is incorrect:* `needs:` creates sequential dependencies, not parallelism. Jobs listed in `needs:` must complete before the dependent job starts.
- *Why C is incorrect:* When a job in `needs:` fails, the dependent job is not merely skipped — the workflow run reports a failure status, which blocks PR merges if the workflow is a required status check.
- *Why D is incorrect:* Artifact sharing between jobs requires explicit `actions/upload-artifact` and `actions/download-artifact` steps. `needs:` alone does not transfer artifacts.

---

### Question 2

Where is a GitLab CI pipeline definition file stored in a repository?

- A) `.github/workflows/pipeline.yml` at any path in the repository
- B) `Jenkinsfile` in the root of the repository
- C) `.gitlab-ci.yml` in the root of the repository
- D) `pipeline/ci-config.yaml` in a dedicated subdirectory

#### Q2 Correct Answer

C — GitLab CI always reads `.gitlab-ci.yml` from the repository root by default. This is a fixed location, unlike GitHub Actions where workflow files can be any `.yml` file under `.github/workflows/`.

#### Q2 Distractor Analysis

- *Why A is incorrect:* `.github/workflows/` is the GitHub Actions convention. GitLab CI uses a different file path.
- *Why B is incorrect:* `Jenkinsfile` is the Jenkins pipeline definition file, not GitLab CI.
- *Why D is incorrect:* GitLab CI does not look in a `pipeline/` subdirectory by default. The file must be at the repository root (though the path is configurable in project settings).

---

### Question 3

In a GitLab CI pipeline, two jobs are assigned to the same stage. How do they execute relative to each other?

- A) They execute sequentially in alphabetical order by job name
- B) They execute in parallel, and both must succeed before the next stage begins
- C) The first job defined in the YAML file runs, and the second job runs only if the first fails
- D) GitLab CI does not support multiple jobs in the same stage

#### Q3 Correct Answer

B — Jobs within the same GitLab CI stage run in parallel. All jobs in a stage must succeed before GitLab advances to the next stage. This allows multiple security scans (SAST, SCA, secrets detection) to run simultaneously within a `security` stage.

#### Q3 Distractor Analysis

- *Why A is incorrect:* GitLab CI does not execute same-stage jobs sequentially by name. Parallelism is the default.
- *Why C is incorrect:* There is no fallback-on-failure sequencing between jobs in the same stage. Both run simultaneously.
- *Why D is incorrect:* Multiple jobs in the same stage is a core GitLab CI feature used extensively for parallel security scans.

---

### Question 4

A Jenkins Declarative pipeline stores a database password directly in the `environment {}` block as a plaintext string. What is the primary security risk of this configuration?

- A) The password will be printed in plaintext to the Jenkins build log, making it visible to anyone with log access
- B) Jenkins will refuse to start the pipeline because plaintext values in environment blocks are blocked by default
- C) The password will be automatically rotated by Jenkins every 24 hours, causing authentication failures
- D) The password will only be accessible to the first stage in the pipeline and unavailable to subsequent stages

#### Q4 Correct Answer

A — Jenkins environment block variables are echoed to the build log during step execution. Anyone with access to the build log — which may include all Jenkins users — can see the plaintext credential. The correct pattern is `withCredentials()`, which masks the value in logs.

#### Q4 Distractor Analysis

- *Why B is incorrect:* Jenkins does not block plaintext values in environment blocks. It will run the pipeline without error, creating the security exposure.
- *Why C is incorrect:* Jenkins does not perform credential rotation. Rotation must be configured through an external secrets management system.
- *Why D is incorrect:* Environment block variables are available to all stages in the pipeline. The problem is visibility in logs, not scope.

---

### Question 5

A DevSecOps engineer wants to add SAST scanning to an existing GitLab CI pipeline with minimal configuration. Which approach requires the least custom code?

- A) Write a custom Docker-based job that installs Semgrep and runs it against the source code in every pipeline
- B) Include the GitLab-provided SAST template using `include: template: Security/SAST.gitlab-ci.yml` in the pipeline file
- C) Add a shell script to the repository that runs SAST locally and commit the results as an artifact
- D) Configure a GitHub Actions workflow to run SAST and post results to the GitLab merge request

#### Q5 Correct Answer

B — GitLab provides pre-built security scanning templates that can be included with a single line. The SAST template automatically adds language-appropriate SAST scanning to the pipeline without custom job definitions.

#### Q5 Distractor Analysis

- *Why A is incorrect:* Writing a custom Docker-based SAST job is valid but requires significantly more configuration than using the built-in template. The question asks for minimal configuration.
- *Why C is incorrect:* Running SAST locally and committing results as an artifact is not a pipeline integration — it does not block merges on finding vulnerabilities.
- *Why D is incorrect:* Using GitHub Actions to scan a GitLab repository is an architecturally complex cross-platform integration, not the minimal approach.

---

### Question 6

Which GitHub Actions `if:` condition correctly restricts a deploy job to run only when a commit is pushed to the main branch, and not when a pull request is opened?

- A) `if: github.event_name == 'pull_request'`
- B) `if: github.ref == 'refs/heads/main' && github.event_name == 'push'`
- C) `if: github.branch == 'main'`
- D) `if: github.event.action == 'deploy'`

#### Q6 Correct Answer

B — This condition checks both the ref (the branch must be main) and the event type (must be a push, not a pull_request). Both conditions together ensure deployment happens only on direct merges to main.

#### Q6 Distractor Analysis

- *Why A is incorrect:* This condition is true when the event IS a pull request — the opposite of the intended restriction.
- *Why C is incorrect:* `github.branch` is not a valid GitHub Actions expression context. The correct property is `github.ref`, which contains `refs/heads/main` for main branch pushes.
- *Why D is incorrect:* `github.event.action == 'deploy'` is not a valid GitHub event type for code push pipelines. Deploy is not a standard GitHub event action name.

---

### Question 7

A security team discovers that a malicious GitHub Actions action in the Actions Marketplace was updated by its maintainer to exfiltrate repository secrets. The team's pipeline uses this action pinned to a version tag `@v2`. What remediation best prevents this attack vector going forward?

- A) Stop using GitHub Actions entirely and migrate to Jenkins, which does not use third-party actions
- B) Pin all third-party actions to a specific commit SHA instead of a mutable version tag
- C) Disable GitHub Secrets and use environment variables to store credentials instead
- D) Set the workflow trigger to `on: schedule` so it runs at night when fewer attackers are active

#### Q7 Correct Answer

B — Version tags like `@v2` are mutable — a malicious maintainer can update what the tag points to. Commit SHAs are immutable — once pinned to a specific SHA, the action code cannot be changed without changing the SHA. Pinning to a SHA prevents a tag update from delivering malicious code.

#### Q7 Distractor Analysis

- *Why A is incorrect:* Jenkins has its own supply chain risks through plugins. Migrating platforms does not eliminate supply chain risk; it shifts it to a different attack surface.
- *Why C is incorrect:* Using environment variables instead of GitHub Secrets reduces security by making credentials visible in workflow logs. It does not address the third-party action supply chain risk.
- *Why D is incorrect:* Scheduled execution time has no effect on what code runs when the action executes. The malicious action runs regardless of when the workflow is triggered.

---

### Question 8

In a Jenkins pipeline, what does the `parallel {}` block accomplish within a stage?

- A) It runs the stage on multiple Jenkins agents simultaneously, distributing the load across the cluster
- B) It executes multiple nested stages at the same time within the parent stage, reducing total pipeline duration
- C) It runs the same stage multiple times with different parameter sets for matrix testing
- D) It creates a backup execution path that runs if the primary stage step fails

#### Q8 Correct Answer

B — The `parallel {}` block in a Jenkins Declarative pipeline creates nested stages that execute concurrently. This is commonly used to run multiple security scans (SAST, SCA, secrets detection) at the same time within a single Security Scan stage.

#### Q8 Distractor Analysis

- *Why A is incorrect:* Running on multiple agents requires the `agent` directive within each parallel stage. `parallel {}` alone defines concurrent execution within one stage but uses the declared agent.
- *Why C is incorrect:* Matrix builds in Jenkins use the `matrix {}` directive, not `parallel {}`.
- *Why D is incorrect:* Fallback execution on failure uses the `post { failure {} }` block, not `parallel {}`.

---

### Question 9

A GitHub Actions workflow has the following structure. What is the execution order of the jobs?

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
  test:
    needs: build
    runs-on: ubuntu-latest
  security-scan:
    needs: build
    runs-on: ubuntu-latest
  deploy:
    needs: [test, security-scan]
    runs-on: ubuntu-latest
```

- A) build, then test, then security-scan, then deploy — all sequential
- B) build runs first; then test and security-scan run in parallel; then deploy runs after both complete
- C) All four jobs run simultaneously in parallel
- D) build and security-scan run in parallel first, then test runs, then deploy runs last

#### Q9 Correct Answer

B — `build` has no `needs:` so it runs first. Both `test` and `security-scan` need only `build`, so they both start as soon as `build` succeeds and run in parallel. `deploy` needs both `test` and `security-scan`, so it waits until both complete.

#### Q9 Distractor Analysis

- *Why A is incorrect:* `test` and `security-scan` both depend only on `build`, not on each other. There is no sequential dependency between them — they run in parallel.
- *Why C is incorrect:* `build` must complete before `test` and `security-scan` can start, and both must complete before `deploy` can start. All four cannot run simultaneously.
- *Why D is incorrect:* `build` and `security-scan` do not share a parallel relationship. `security-scan` depends on `build`, so it runs after `build`, alongside `test`.

---

### Question 10

A team is migrating from a scripted Jenkins pipeline to a declarative Jenkins pipeline. What is the primary security advantage of the declarative format?

- A) Declarative pipelines execute faster because they skip the Groovy compilation step
- B) Declarative pipelines cannot access Jenkins environment variables, reducing the risk of credential leakage
- C) Declarative pipelines use a constrained, auditable structure that limits arbitrary Groovy code execution, reducing the attack surface for malicious pipeline modifications
- D) Declarative pipelines automatically encrypt all credential values stored in the environment block

#### Q10 Correct Answer

C — Declarative pipelines enforce a structured schema (`pipeline {}`, `stages {}`, `steps {}`). Arbitrary Groovy code execution is sandboxed or requires explicit approval. Scripted pipelines allow unrestricted Groovy execution, which can be exploited to exfiltrate credentials or modify pipeline behavior.

#### Q10 Distractor Analysis

- *Why A is incorrect:* Both pipeline types ultimately compile to Groovy internally. There is no meaningful execution speed difference from format choice.
- *Why B is incorrect:* Declarative pipelines can access environment variables. The difference is in code execution restrictions, not variable access.
- *Why D is incorrect:* Declarative pipelines do not automatically encrypt environment block values. Encryption requires using `withCredentials()` or the Jenkins Credentials Manager — regardless of pipeline type.
