# Quiz: Module 03 - CI/CD Concepts – Jenkins, GitHub Actions, GitLab CI

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
Which file format is used to configure GitHub Actions workflow pipeline scripts?

* A) JSON — JavaScript Object Notation, used for API payloads and package manifests
* B) XML — Extensible Markup Language, used in Maven and Ant build configurations
* C) YAML — Yet Another Markup Language, used for human-readable configuration files
* D) TOML — Tom's Obvious Minimal Language, used in Rust and Python packaging configs
* **Correct Answer:** C) GitHub Actions workflows are declared in YAML files located inside the `.github/workflows/` directory.
* **Distractor Analysis:**
  * *Why C is correct:* GitHub Actions, GitLab CI, and Kubernetes all use YAML for pipeline and configuration definitions because its indentation-based hierarchy is readable and tool-parseable.
  * *Why A is incorrect:* JSON is used for GitHub API responses and `package.json` manifests but is not the format for GitHub Actions workflow files.
  * *Why B is incorrect:* XML is used by Maven (`pom.xml`) and older Jenkins configurations but is not the format for GitHub Actions.
  * *Why D is incorrect:* TOML is used in `pyproject.toml` and Cargo manifests but is not supported as a GitHub Actions workflow format.

---

**Question 2**
Which of the following most accurately describes a "job" in a GitHub Actions workflow?

* A) A single shell command that runs within a larger sequence of pipeline tasks
* B) A logical grouping of sequential steps that execute on a single runner, which can run in parallel with other jobs in the same workflow
* C) The YAML file that defines the entire pipeline, stored in `.github/workflows/`
* D) A GitHub repository setting that controls which branches are protected from direct pushes
* **Correct Answer:** B) Jobs are the top-level execution units in a workflow — each job runs on its own runner, and multiple jobs can execute in parallel unless dependencies are specified with `needs:`.
* **Distractor Analysis:**
  * *Why B is correct:* In GitHub Actions YAML, `jobs:` contains named job blocks; each job specifies a `runs-on` runner and a list of `steps`. Multiple jobs default to parallel execution, enabling simultaneous SAST and linting checks.
  * *Why A is incorrect:* A single shell command is a `step` within a job, not a job itself. Jobs contain multiple steps.
  * *Why C is incorrect:* The YAML file is the workflow file; a job is a subdivision within that file, not the file itself.
  * *Why D is incorrect:* Branch protection is a GitHub repository configuration feature, not a concept within the workflow YAML structure.

---

**Question 3**
A DevSecOps engineer wants security scans in a GitHub Actions workflow to run only when a developer opens or updates a pull request targeting the `main` branch. Which trigger configuration achieves this?

* A) `on: push` — fires on every push to any branch in the repository
* B) `on: schedule` with a cron expression — fires at a defined time interval
* C) `on: pull_request` with `branches: [main]` — fires only when a PR targets the `main` branch
* D) `on: release` — fires only when a GitHub Release is published
* **Correct Answer:** C) The `on: pull_request` trigger with a branch filter ensures security scans gate every proposed merge to `main` without running on unrelated branches.
* **Distractor Analysis:**
  * *Why C is correct:* `on: pull_request` fires on PR open, synchronize, and reopen events; adding `branches: [main]` limits it to PRs targeting `main`, making it the standard gate for protecting the primary branch.
  * *Why A is incorrect:* `on: push` fires on direct pushes to branches, not on pull request events, and applies to all branches without a filter.
  * *Why B is incorrect:* A scheduled trigger runs at fixed time intervals regardless of code changes — it cannot enforce a merge gate.
  * *Why D is incorrect:* `on: release` fires after a release is published, which is too late to gate code quality before merge.

---

**Question 4**
In a Jenkins declarative pipeline, which block defines the sequence of stages (Build, Test, Security Scan) and the steps within each stage?

* A) The `Jenkinsfile` `environment {}` block, which sets pipeline-wide environment variables
* B) The `pipeline { stages { stage('Name') { steps { ... } } } }` structure in the `Jenkinsfile`
* C) The Jenkins global configuration page under "Manage Jenkins > Configure System"
* D) The `triggers {}` block, which defines when the pipeline runs automatically
* **Correct Answer:** B) Jenkins declarative pipelines use a nested `pipeline > stages > stage > steps` structure in the `Jenkinsfile` to define what executes at each phase.
* **Distractor Analysis:**
  * *Why B is correct:* The declarative `pipeline` block contains a `stages` section; each `stage` has a name and a `steps` block with shell commands or plugin calls — this is where SAST scans, builds, and tests are defined.
  * *Why A is incorrect:* The `environment {}` block declares key-value environment variables available to all steps; it does not define execution stages or steps.
  * *Why C is incorrect:* The Jenkins global configuration controls system-level settings like JDK installations and credentials; pipeline logic lives in the `Jenkinsfile`.
  * *Why D is incorrect:* The `triggers {}` block defines scheduling (like a cron) or SCM polling; it controls when the pipeline runs, not what it does when it runs.

---

**Question 5**
A team using GitLab CI wants to ensure that a DAST scan runs only after the application has been successfully deployed to a staging environment. Which GitLab CI feature enforces this sequencing?

* A) Define both jobs with the same `stage:` name so they run in parallel
* B) Use the `needs:` keyword to create a direct dependency from the DAST job to the staging deploy job
* C) Set the DAST job's `when: manual` so a human must trigger it after deployment
* D) Place both jobs in `.gitlab-ci.yml` and rely on alphabetical execution order
* **Correct Answer:** B) The `needs:` keyword in GitLab CI creates an explicit dependency — the DAST job will not start until all jobs listed in its `needs:` array have completed successfully.
* **Distractor Analysis:**
  * *Why B is correct:* `needs:` allows DAG (directed acyclic graph) ordering in GitLab CI pipelines, ensuring the DAST job waits for a successful staging deploy before probing live endpoints.
  * *Why A is incorrect:* Jobs sharing the same `stage:` name run in parallel, not sequentially — a DAST scan would attempt to run at the same time as the deploy, before the environment is ready.
  * *Why C is incorrect:* `when: manual` requires a human to click "Run" in the GitLab UI; while this ensures the deploy happened, it breaks the automated pipeline and is not a recommended DevSecOps pattern.
  * *Why D is incorrect:* GitLab CI does not execute jobs in alphabetical order; execution order is determined by `stage:` and `needs:` configuration.
