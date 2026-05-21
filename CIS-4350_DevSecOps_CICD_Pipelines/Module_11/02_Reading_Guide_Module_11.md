# Reading Guide: Module 11 - Container Image Scanning – Trivy and Grype

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 11 - Container Image Scanning – Trivy and Grype**! This module covers container image vulnerability scanning as the pipeline security gate that checks built Docker images for known CVEs in OS packages and application dependencies before they are pushed to a registry or deployed. Unlike SCA (which scans source dependency manifests), container image scanners analyze the actual filesystem layers of a built image — finding vulnerabilities in system libraries, language runtimes, and application packages as they exist inside the container. Trivy and Grype are the two dominant open-source tools in this space and are heavily tested on the CDP exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Secret scanning**: In the context of container image scanning, the automated detection of secrets (API keys, certificates, passwords) that may have been inadvertently embedded in image layers during the build process. Trivy includes a secret scanning mode that checks image layer contents for credential patterns, complementing the source-level secret scanning covered in Module 09.

* **Git leaks prevention**: The pre-image-build controls (pre-commit hooks, SAST secret scanning, `.dockerignore` configuration) that prevent secrets from entering a container image in the first place. If a secret appears in a `COPY . .` layer because it was present in the build context, git leaks prevention at the source stage is the upstream fix.

* **HashiCorp Vault (in container context)**: The secrets management platform used to inject runtime secrets into containers without embedding them in image layers. In Kubernetes deployments, Vault Agent Injector or the Vault CSI provider injects secrets as in-memory files or environment variables at pod startup — ensuring the container image itself never contains secrets.

* **Encrypted environment variables**: Secrets injected into container runtime environments (Kubernetes Secrets, Docker environment flags, CI/CD secrets) rather than baked into image layers. Encrypted at rest in Kubernetes etcd (with envelope encryption enabled), these variables provide runtime credential access without image-layer exposure.

---

### 2. Certification Exam Tips

* **SCA vs. Image Scanning**: The CDP exam distinguishes between SCA (scans dependency manifest files in source code) and container image scanning (scans the actual installed packages inside a built image layer). An image may contain packages not listed in `requirements.txt` — OS-level libraries, language runtimes, indirect pip installs — that SCA would miss. Both tools are needed.
* **Trivy Scan Targets**: Trivy can scan container images (`trivy image myapp:latest`), filesystem directories (`trivy fs .`), Git repositories (`trivy repo`), Kubernetes clusters (`trivy k8s`), and IaC files (`trivy config .`). The CDP exam tests which scan target to use in a given scenario.
* **CRITICAL Severity Gate**: Standard DevSecOps pipeline configuration fails the image push job on CRITICAL severity CVEs (`trivy image --exit-code 1 --severity CRITICAL myapp:latest`). Know the Trivy exit code behavior and how it integrates with pipeline pass/fail logic.
* **Study Resource**: The [Trivy documentation](https://aquasecurity.github.io/trivy/) covers all scan targets, severity filtering, output formats (JSON, SARIF, table), and CI/CD integration examples — review the "Integrations" section for CDP pipeline configuration questions.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [Trivy documentation Getting Started guide](https://aquasecurity.github.io/trivy/latest/getting-started/overview/) — covers Trivy installation, scanning container images and filesystems, severity filtering, output format options, and GitHub Actions integration. Focus on image scanning and the `--exit-code` and `--severity` options used to configure pipeline gates.
* **Required Video**: Watch the container image scanning segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates building a Docker image in a CI pipeline, running Trivy against it, interpreting vulnerability output, and configuring the scan as a blocking pipeline gate before the image push step.

---

### Lab & Command Integration

In this week's hands-on lab, you will integrate container image scanning into a CI/CD pipeline by:

* **Configure GitHub Actions secrets variables**: Configure registry authentication credentials (GitHub Container Registry token or Docker Hub credentials) as GitHub Actions secrets, referenced in the workflow as `${{ secrets.REGISTRY_TOKEN }}` to authenticate the image push step that follows a successful scan.
* **Run a git leak scan detecting exposed tokens**: Run `trivy image --scanners secret myapp:latest` against a locally built image to detect any secrets inadvertently embedded in image layers, validating that `.dockerignore` properly excludes credential files from the build context.
* **Verify secrets masking in logs**: Add `trivy image --exit-code 1 --severity HIGH,CRITICAL --format sarif --output trivy-results.sarif myapp:latest` as a pipeline step and confirm that: (a) the step fails when HIGH/CRITICAL CVEs are present, (b) SARIF output is uploaded as a GitHub Code Scanning result, and (c) the image push step only executes when the Trivy step passes.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand the difference between SCA (source dependency scanning) and container image scanning (installed package scanning).
* [ ] Read the Trivy documentation at [https://aquasecurity.github.io/trivy/](https://aquasecurity.github.io/trivy/).
* [ ] Watch the container image scanning segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the Trivy pipeline integration and severity-gated image push in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
