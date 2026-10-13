# Discussion Forum: Module 11 — Container Image Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

This week's discussion explores container image scanning through three scenarios drawn from real-world DevSecOps pipeline decisions, vulnerability triage challenges, and base image management. Initial posts are due Wednesday at 11:59 PM Central. Peer responses are due Sunday at 11:59 PM Central.

---

### Scenario 1 — The SCA-Only Argument

A senior developer at a fintech company pushes back against adding Trivy to the CI/CD pipeline. The team already runs Snyk SCA on every pull request, and the developer argues: "We are already scanning dependencies with Snyk — adding Trivy is just duplication. We will end up with two tools screaming about the same CVEs, and our pipeline is already slow enough." The team lead escalates to you as the DevSecOps engineer.

In 175–225 words, write a technical response to the developer that addresses:

- The specific class of vulnerabilities that container image scanning finds that Snyk SCA cannot detect, using the concept of OS package layers versus application package layers to make the distinction precise and cite a concrete example (name a specific OS package type such as `libssl`, `glibc`, or `openssl` from a Debian or Alpine base image)
- Why SCA scanning of `requirements.txt` or `package.json` would be completely blind to a CRITICAL CVE in the container's base image OS packages, explaining what those files contain versus what the built container image contains
- What the correct pipeline placement is for SCA (before image build) versus container image scanning (after image build) and why running them at different stages makes them complementary rather than redundant

---

### Scenario 2 — The Unfixable CVE Pipeline Block

A platform engineering team deploys a new container scan job with `--exit-code 1 --severity HIGH,CRITICAL` and no `--ignore-unfixed` flag. Within 24 hours, every pipeline across the organization is failing. Investigation reveals that 34 of the 41 blocking CVEs have no fixed version available — they are CVEs in Debian base image packages for which upstream patches have not yet been released. The development teams are furious and demanding the scan job be disabled.

In 175–225 words, design a remediation plan that addresses:

- The immediate configuration change to apply to the Trivy command to restore pipeline functionality while maintaining a meaningful security gate — be specific about the exact flag to add and explain precisely what it filters
- The correct Grype equivalent flag for teams using Grype instead of Trivy, demonstrating you understand both tools' CLI semantics
- Why disabling the scan job entirely is the wrong response, and what the correct DevSecOps posture is: how unfixable CVEs should be tracked, documented, and revisited (name a specific artifact such as a risk register entry or `.trivyignore` file)

---

### Scenario 3 — Base Image Negligence and the Dependabot Gap

A security audit of a production Kubernetes workload reveals the application container is running `python:3.9-slim` as its base image. Trivy reports 47 findings including 8 CRITICAL CVEs. The most recent image build was 14 months ago. The team's Dockerfile pins the base image as `FROM python:3.9-slim` without a digest. When asked why the base image was never updated, the engineer responds: "We have Dependabot enabled — if there were vulnerabilities it would have opened a PR."

In 175–225 words, correct the engineer's misunderstanding and propose a complete base image currency solution by addressing:

- Why Dependabot's default behavior would not have flagged the outdated `python:3.9-slim` base image — explain the difference between what Dependabot monitors (dependency manifests) versus what requires image digest pinning with scheduled rebuild pipelines
- The two-part technical solution: how image digest pinning (`FROM python:3.9-slim@sha256:...`) combined with Dependabot's `docker` ecosystem configuration actually enables automated base image PRs, and why a tag-only reference (`FROM python:3.9-slim`) defeats this mechanism
- What a scheduled nightly rebuild pipeline job (using `on: schedule: cron:`) adds as a defense layer even when Dependabot is correctly configured, and what it would have caught in this scenario

---

### Peer Response Requirements

After your initial post, write substantive replies to at least two classmates (minimum 60 words each). Your peer responses should:

- Add a specific technical detail the original post did not mention
- Challenge an assumption or offer a more precise solution
- Connect the scenario to an adjacent DevSecOps control covered in a previous module

Simple agreement or restatement of the original post does not satisfy the substantive requirement.

---

### Discussion Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post addresses all required elements with technical precision — names specific tools, flags, and package types | 4 |
| Initial post demonstrates understanding of the distinction between SCA and container image scanning scopes | 2 |
| Initial post meets the 175–225 word count requirement | 1 |
| First peer response is substantive — adds new technical content or a precise alternative | 1.5 |
| Second peer response is substantive — adds new technical content or a precise alternative | 1.5 |
| **Total** | **10** |

---

### Grading Notes

- Posts must name specific Trivy or Grype flags (`--ignore-unfixed`, `--only-fixed`, `--exit-code 1`, `--fail-on`) to receive full technical precision credit.
- Answers to Scenario 2 that say "adjust the scan configuration" without naming the exact flag receive partial credit only.
- Answers to Scenario 3 that do not explain the digest pinning mechanism or the Dependabot `docker` ecosystem configuration receive partial credit only.

---

### Professor Nash Note

The three scenarios in this discussion are chosen to surface the most common real-world friction points in container scanning adoption: the "we already have SCA" objection, the unfixable CVE pipeline paralysis problem, and the false confidence in Dependabot without digest pinning. Each of these has caused production security incidents. Your posts should reflect not just technical knowledge but the judgment to explain these tradeoffs to engineers who are skeptical or frustrated — that communication skill is central to the DevSecOps role.
