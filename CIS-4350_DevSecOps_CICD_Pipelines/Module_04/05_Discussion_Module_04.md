# Discussion Forum: Module 04 - Containerization: Docker Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 04 concepts — Dockerfile security, container image scanning, non-root execution, multi-stage builds, and runtime hardening — to realistic engineering scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Privileged Production Container

A DevOps engineer at a healthcare company deploys a containerized application to production using the following `docker run` command: `docker run --privileged -u root -p 80:80 patient-data-api:latest`. The application processes protected health information. A security auditor flags this configuration during an annual review and states it violates HIPAA's minimum necessary access standard.

In 175-225 words, address the following: Explain specifically what attack capability `--privileged` grants an attacker who achieves code execution inside the container, and why `-u root` compounds this risk. Identify the correct runtime flags that should replace `--privileged` and `-u root` to implement least privilege for a web application that needs to bind to port 80. Explain how the principle of least privilege in container runtime configuration relates to the DevSecOps shared responsibility model — specifically, which team is responsible for setting these runtime flags and how this should be enforced systematically rather than relying on individual engineer knowledge.

---

## Scenario B: The Exposed Secret in the Registry

A development team pushes a Docker image to Docker Hub. Two weeks later, a security researcher contacts them to report that running `docker history their-image:latest` reveals a layer with the instruction `ENV STRIPE_SECRET_KEY=sk_live_xyz123...` — a plaintext production payment API key. The key has been publicly accessible for two weeks in the image that was pushed to a public registry.

In 175-225 words, address the following: Explain the technical reason why the key is visible in the image history even if a subsequent Dockerfile revision removed the ENV instruction. Identify the two immediate remediation actions that must occur in the correct order and explain why the ordering matters. Then describe two specific technical controls — one at the Dockerfile authoring stage and one at the CI/CD pipeline stage — that would prevent this class of exposure in the future. Use precise Docker and DevSecOps terminology in your response.

---

## Scenario C: The CVE Triage Problem

A DevSecOps engineer integrates Trivy into the CI/CD pipeline with `--exit-code 1 --severity CRITICAL,HIGH`. On the first run, Trivy reports 47 CRITICAL and 312 HIGH CVEs in the base image `ubuntu:22.04`. The engineering manager panics and asks the team to disable the scan because it is blocking all deployments. The DevSecOps engineer argues that disabling the scan is the wrong response.

In 175-225 words, address the following: Explain to the engineering manager why 47 CRITICAL CVEs in a base image does not necessarily mean the application is exploitable in production — introduce the concept of reachability in vulnerability triage. Propose a realistic remediation path that does not involve disabling the scanner: what base image change would reduce the CVE count dramatically and why? Finally, describe how a vulnerability acceptance policy (sometimes called a .trivyignore file or scanner exception) can be used for CVEs that are genuinely not exploitable in the application's context, while preserving the value of the scan for new critical vulnerabilities.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise Docker and DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario elements with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most elements but lacks technical depth or correct terminology in one or more areas.
- 0-2 pts: Incomplete, missing, or does not substantively address the scenario.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios.

- 4 pts: Two substantive responses (at least 50 words each) that add technical depth, propose an alternative approach, or cite a specific concept from the reading guide or lab.
- 2 pts: Only one substantive response, or both are superficial.
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

Scenario B involves a real pattern that has affected production systems at multiple organizations. When discussing the remediation order, note that "remove the key from the Dockerfile" is not the first action — it is the second. The first is always to revoke the exposed credential. A key that has been publicly visible for two weeks must be treated as compromised regardless of whether the image is still accessible. The exam tests this sequencing explicitly.
