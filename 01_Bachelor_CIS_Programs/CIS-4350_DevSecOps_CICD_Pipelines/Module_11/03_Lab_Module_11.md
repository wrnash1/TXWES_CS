# Lab Activity: Module 11 - Container Image Scanning: Trivy and Grype

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Total Points: 100

---

## Objectives

By completing this lab you will be able to:

- Run Trivy against a container image and interpret CVE findings by layer type.
- Configure Trivy with `--exit-code 1` and `--ignore-unfixed` to create a meaningful pipeline gate.
- Run Grype and compare its output and CLI semantics to Trivy.
- Integrate container image scanning into a GitHub Actions pipeline.
- Triage findings and distinguish between OS package CVEs and language package CVEs.

---

## Prerequisites

Before beginning this lab, confirm the following:

- Docker is installed and running.
- Trivy is installed (`trivy --version`). Install with `brew install trivy` or from the Aqua Security GitHub releases.
- Grype is installed (`grype version`). Install with `brew install grype` or from the Anchore GitHub releases.
- You have a GitHub repository from earlier modules.
- You have completed the Module 11 video and reading guide.

---

## Part 1: Trivy Image Scan (30 points)

### Part 1 Background

Trivy scans all layers of a container image — base OS packages, language runtime packages, and application packages — against its vulnerability database. This part covers the core Trivy workflow including severity filtering and unfixed CVE handling.

### Part 1 Instructions

**Step 1: Scan a known-vulnerable Python base image.**

```bash
trivy image python:3.9-slim
```

This image is intentionally chosen for its age. Record the total finding count, the count by severity (CRITICAL, HIGH, MEDIUM, LOW), and the count of findings with a fixed version available.

**Step 2: Filter to HIGH and CRITICAL only.**

```bash
trivy image --severity HIGH,CRITICAL python:3.9-slim
```

Record the output. Note how many findings remain.

**Step 3: Apply the unfixed filter.**

```bash
trivy image --severity HIGH,CRITICAL --ignore-unfixed python:3.9-slim
```

Compare the finding count from Step 2 to Step 3. In 2-3 sentences, explain what `--ignore-unfixed` removed and why filtering unfixed CVEs is useful in a pipeline context.

**Step 4: Test the pipeline gate.**

```bash
trivy image --exit-code 1 --severity HIGH,CRITICAL --ignore-unfixed python:3.9-slim
echo "Exit code: $?"
```

Record the exit code and explain what a non-zero exit code means for a GitHub Actions pipeline job.

**Step 5: Scan your own application image.**

Build a simple `python:3.11-slim`-based image and scan it:

```bash
docker build -t myapp:lab11 .
trivy image --severity HIGH,CRITICAL --ignore-unfixed myapp:lab11
```

Compare the finding count against `python:3.9-slim`. Record whether using a more current base image reduced the finding count.

### Part 1 Deliverable

Submit: the full Trivy output tables from Steps 1-4, the written explanation of `--ignore-unfixed`, the exit code record with explanation, and the base image comparison from Step 5.

### Part 1 Rubric

| Criterion | Points |
|---|---|
| Trivy output tables are complete and accurate | 10 |
| `--ignore-unfixed` explanation is technically correct | 8 |
| Exit code record and explanation are accurate | 6 |
| Base image comparison analysis is accurate | 6 |

---

## Part 2: Grype Comparison (20 points)

### Part 2 Background

Grype provides similar scanning capabilities to Trivy with different CLI semantics. Understanding both tools is required for the DevSecOps Professional exam.

### Part 2 Instructions

**Step 1: Scan the same image with Grype.**

```bash
grype python:3.9-slim
```

Record the finding count and compare it to Trivy's output for the same image. Note any differences in the packages flagged or the CVE IDs reported.

**Step 2: Apply the severity filter and fixed-only flag.**

```bash
grype --only-fixed --fail-on high python:3.9-slim
echo "Exit code: $?"
```

Record the exit code and compare the finding count to Trivy's `--ignore-unfixed` output.

**Step 3: Write the Trivy vs. Grype comparison.**

Create a comparison table with these rows: CLI pipeline gate flag, unfixed CVE filter flag, output format, SARIF support. Fill in the correct value for each tool in each row.

Then write 2-3 sentences explaining which tool you would choose for a new project and why.

### Part 2 Deliverable

Submit: the Grype output table, exit code record, the comparison table, and the written tool recommendation with justification.

### Part 2 Rubric

| Criterion | Points |
|---|---|
| Grype output is recorded accurately | 6 |
| Comparison table is complete and technically accurate | 8 |
| Tool recommendation is justified with specific technical reasoning | 6 |

---

## Part 3: GitHub Actions Container Scan Integration (30 points)

### Part 3 Background

Container image scanning must run in the CI/CD pipeline automatically after each image build. This part integrates Trivy as a required pipeline gate before image push.

### Part 3 Instructions

**Step 1: Create a Dockerfile with a vulnerable base image.**

Create a simple `Dockerfile` using `python:3.9-slim`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

**Step 2: Add a container-scan job to your GitHub Actions pipeline.**

In your `full-pipeline.yml`, add a `container-scan` job after the `build` job. The job must:

- Declare `needs: build` to run only after the build succeeds.
- Check out code with `actions/checkout@v4`.
- Build the image with `docker build -t myapp:${{ github.sha }} .`.
- Run `aquasecurity/trivy-action@master` with `image-ref: myapp:${{ github.sha }}`, `format: sarif`, `output: trivy-results.sarif`, `exit-code: '1'`, `severity: HIGH,CRITICAL`, and `ignore-unfixed: true`.
- Upload the SARIF file using `github/codeql-action/upload-sarif@v3` with `if: always()`.

**Step 3: Trigger the pipeline with the vulnerable Dockerfile.**

Push to a feature branch and observe the container-scan job failing in the Actions tab.

**Step 4: Screenshot the failed scan.**

Capture the Trivy job output showing the CVE findings.

**Step 5: Update the Dockerfile to use a more current base image.**

Change `FROM python:3.9-slim` to `FROM python:3.11-slim` in the Dockerfile. Push and observe the pipeline re-run.

**Step 6: Screenshot the passing pipeline.**

Capture the passing container-scan job.

### Part 3 Deliverable

Submit: the updated pipeline YAML, screenshots of the failed and passing pipeline runs, and a one-paragraph explanation of why `if: always()` is required on the SARIF upload step.

### Part 3 Rubric

| Criterion | Points |
|---|---|
| Pipeline YAML correctly adds container-scan job with all required parameters | 12 |
| Screenshot shows failed pipeline with Trivy CVE findings | 8 |
| Screenshot shows passing pipeline after base image update | 7 |
| Explanation of `if: always()` is technically accurate | 3 |

---

## Part 4: Triage and Remediation Concepts (20 points)

### Part 4 Instructions

Answer each question in 3-5 sentences using precise container security and DevSecOps terminology.

**Question A:** A Trivy scan finds a CRITICAL CVE (CVSS 9.1) in the `libssl1.1` package in the base image. The CVE has no fixed version available in the current Alpine release. Your application is deployed to production. Explain what `--ignore-unfixed` would do to this finding in the pipeline, what alternative remediation paths exist when no fix is available, and what documentation should be produced.

**Question B:** A developer argues that since they already run SCA with Snyk on every PR, adding Trivy in the pipeline is redundant — "Snyk already catches dependency CVEs." Explain the specific class of vulnerabilities that container image scanning finds that Snyk SCA does not, using the concept of OS package layers vs. application package layers to make the distinction precise.

**Question C:** Your container scan pipeline is configured to fail on HIGH and CRITICAL CVEs. A new release of your application's base image (`node:20-alpine`) is published that patches 14 HIGH CVEs. Describe the DevSecOps process for updating to the new base image: what triggers the update, how is it implemented safely, and how does the pipeline confirm the update resolved the CVEs. Name the GitHub feature that can automate the base image update PR.

### Part 4 Deliverable

Submit written answers to all three questions. Label each answer with the question letter.

### Part 4 Rubric

| Criterion | Points |
|---|---|
| Question A correctly explains `--ignore-unfixed` and alternative remediation paths | 7 |
| Question B precisely distinguishes OS layer CVEs from application layer CVEs | 6 |
| Question C describes a correct update process and names the correct GitHub feature | 7 |

---

## Submission Instructions

Combine all four parts into a single document. Label each part clearly. Include your name, date, course number (CIS-4350), and module number (11) at the top. Submit via the Canvas LMS assignment portal before the due date shown in Canvas.

---

## Part 9 — Challenge Exercise

### Challenge 1: Trivy Operator Continuous Scanning in Kubernetes

Deploy the Trivy operator to a local Kubernetes cluster and observe continuous vulnerability reporting on running workloads.

1. Start a local cluster and install the Trivy operator via Helm:

```bash
helm repo add aqua https://aquasecurity.github.io/helm-charts/
helm repo update
helm install trivy-operator aqua/trivy-operator \
  --namespace trivy-system \
  --create-namespace \
  --set="trivy.ignoreUnfixed=true"
```

1. Deploy a vulnerable image to trigger a scan: `kubectl run vuln-app --image=nginx:1.18 --restart=Never`
2. Wait 60-90 seconds and then retrieve the VulnerabilityReport: `kubectl get vulnerabilityreports -A` and `kubectl describe vulnerabilityreport <report-name> -n default`
3. Record the VulnerabilityReport output. Note which CVEs are listed, their severities, and whether fixed versions are shown.
4. Update the pod to use `nginx:latest` (`kubectl delete pod vuln-app && kubectl run vuln-app --image=nginx:latest`) and observe the operator generating a new VulnerabilityReport for the updated image. Compare the finding counts.

### Challenge 2: Cosign Image Signing and Verification Gate

Sign a container image with cosign and configure a policy that requires a valid signature before deployment.

1. Install cosign (`brew install cosign` or download from GitHub releases) and generate a key pair: `cosign generate-key-pair`
2. Build and push a test image, then sign it:

```bash
docker build -t ttl.sh/lab11-signed:1h .
docker push ttl.sh/lab11-signed:1h
cosign sign --key cosign.key ttl.sh/lab11-signed:1h
```

1. Verify the signature: `cosign verify --key cosign.pub ttl.sh/lab11-signed:1h`
2. Attempt to verify an unsigned image (such as `nginx:latest`) with the same key and record the error output.
3. Write a GitHub Actions step that runs `cosign verify --key ${{ secrets.COSIGN_PUBLIC_KEY }} $IMAGE` before any deployment step, so unsigned or tampered images fail the pipeline.

### Reflection Questions

1. The Trivy operator generates VulnerabilityReports for running workloads independently of the CI pipeline. A developer argues this creates duplicate work since CI already scans images at build time. Explain two scenarios in which the Trivy operator would detect a CVE that the CI pipeline scan would not, and describe what operational response each scenario requires.
2. Cosign image signing creates a verifiable chain of custody from build to deployment. However, signing an image does not mean the image is free of vulnerabilities — it only means the image has not been tampered with since it was signed. Describe a complete supply chain security posture that combines cosign signing, SBOM generation, and Trivy scanning, and explain at which pipeline stage each control provides value.

---

Lab 11 | CIS-4350 | Texas Wesleyan University | Professor Nash
