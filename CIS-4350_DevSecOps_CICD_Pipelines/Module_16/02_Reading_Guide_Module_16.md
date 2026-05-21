# Reading Guide: Module 16 - Final Exam Prep & DevSecOps Professional Certification

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 16 - Final Exam Prep & DevSecOps Professional Certification**! This final module consolidates all concepts from Modules 01–15 into a structured review framework aligned with the Certified DevSecOps Professional (CDP) exam objectives. You will review the complete DevSecOps pipeline from culture and version control through container security, policy enforcement, and compliance metrics. This module also provides exam-day strategy: how to approach scenario-based questions, how to distinguish between similar tools and concepts, and how to apply shift-left reasoning to novel situations. Complete the review checklist and practice questions before sitting for the CDP exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. This module's glossary consolidates the most exam-critical terms from the entire course:

* **Core Operations (CDP Exam Scope)**: The complete set of DevSecOps pipeline security operations — SAST at commit, SCA at build, container image scanning before push, DAST at staging, IaC scanning before apply, secrets scanning at pre-commit, compliance policy enforcement at Kubernetes admission — that together implement a defense-in-depth security posture across the full CI/CD lifecycle.

* **Best Practices (DevSecOps)**: The consensus-recognized implementation patterns for DevSecOps security: shift-left security placement, defense in depth using multiple scan types, least privilege for all service accounts and IAM roles, immutable infrastructure with pipeline-built images, secrets stored in dedicated vaults never in source code, policy as code for continuous compliance, and audit trails for every production deployment.

* **System Configuration (DevSecOps Pipeline)**: The complete set of technical settings across the CI/CD platform (GitHub Actions workflow YAML, branch protection rules, required status checks), container registry (push access controls, image signing requirements), Kubernetes cluster (RBAC, NetworkPolicies, Pod Security Standards, admission webhooks), and secrets management (Vault policies, dynamic secret TTLs) that together enforce the organization's security requirements.

---

### 2. Certification Exam Tips

* **CDP Exam Format**: The CDP exam consists of scenario-based multiple choice questions. The exam presents realistic DevSecOps situations and asks you to identify the correct tool, pipeline placement, security control, or policy configuration. Memorizing definitions alone is insufficient — practice applying concepts to novel scenarios.
* **Most Common Wrong Answer Patterns**: Watch for answer choices that (a) use the correct tool but at the wrong pipeline stage, (b) address the symptom rather than the root cause, (c) are administrative controls when a technical control is needed, or (d) are correct in isolation but weaken security in context (e.g., `imagePullPolicy: IfNotPresent` is operationally valid but reduces security compared to `Always`).
* **Cross-Module Integration**: The CDP exam tests whether you understand how tools and stages interconnect. Be prepared for questions like: "A SAST scan passes, an SCA scan passes, but a Trivy image scan fails CRITICAL. What is the most likely cause?" (Answer: The base image contains OS-level CVEs that SCA, which scans application-level manifests, would not detect.)
* **Study Resource**: Complete the [Practical DevSecOps CDP Practice Tests](https://www.practical-devsecops.com/certified-devsecops-professional/) — the official Practical DevSecOps practice exam materials aligned directly with the CDP certification objectives are the most targeted preparation resource available.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Review all 15 module reading guides and their glossary terms — focus on the terms you found most challenging and ensure you can apply each definition in a pipeline scenario context. Create a one-page summary of the complete pipeline security gate sequence with the tool and trigger stage for each gate.
* **Required Video**: Re-watch any segments of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) that cover tools or concepts you are least confident about. The freeCodeCamp course covers SAST, DAST, SCA, container scanning, secrets management, IaC scanning, and compliance — a complete CDP exam topic survey.

---

### Lab & Command Integration

In this final module's review activity, you will consolidate your practical skills by:

* **Review the complete pipeline sequence**: Document a complete end-to-end GitHub Actions workflow that incorporates every security gate from this course — linting, SAST, SCA, Docker build, Trivy image scan, IaC scan (if applicable), staging deployment, DAST, and production deployment with compliance gate — with the correct trigger event and failure behavior for each step.
* **Practice scenario-based questions**: Work through the Module 16 quiz and review each distractor analysis carefully — for each incorrect answer, articulate why it is wrong using course concepts.
* **Prepare exam documentation checklist**: List the key tool-to-pipeline-stage mappings, the STRIDE categories and their mitigations, the three Kubernetes Pod Security Standard profiles, and the five most important Dockerfile security practices — as a personal reference sheet for exam day.

---

### 3. Study Checklist

* [ ] Review all glossary terms from Modules 01–15 and test yourself on each definition in a scenario context.
* [ ] Re-read all 15 module Certification Exam Tips sections — these highlight the highest-yield CDP exam topics.
* [ ] Complete the final review video segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the full-pipeline documentation exercise in the lab activity.
* [ ] Attempt the Module 16 practice quiz and review all distractor analyses for questions you missed.
* [ ] Visit [https://www.practical-devsecops.com/certified-devsecops-professional/](https://www.practical-devsecops.com/certified-devsecops-professional/) to review the official CDP exam objectives and register for the certification exam.
