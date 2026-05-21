# Reading Guide: Module 01 - DevOps Fundamentals and the DevSecOps Mindset

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 01 - DevOps Fundamentals and the DevSecOps Mindset**! This module establishes the cultural and technical foundations of DevSecOps: what it means to embed security into every stage of the software delivery lifecycle rather than treating it as a final checkpoint. You will explore the evolution from traditional waterfall development through DevOps and into DevSecOps, understanding why integrating security earlier — "shifting left" — dramatically reduces the cost and risk of vulnerabilities. These foundational concepts underpin every subsequent module and are heavily weighted on the CDP certification exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **DevSecOps**: A software engineering culture and practice that integrates security controls, testing, and responsibilities into every phase of the DevOps CI/CD pipeline. Rather than a separate security review at the end of development, DevSecOps makes security a shared responsibility among developers, operations engineers, and security professionals from the first commit onward.

* **Shift-left security**: The practice of moving security activities — such as code analysis, dependency scanning, and threat modeling — earlier in the software development lifecycle (SDLC). By catching vulnerabilities during development rather than post-deployment, teams reduce remediation cost and prevent security debt from accumulating.

* **Pipeline automation**: The use of CI/CD tooling (GitHub Actions, Jenkins, GitLab CI) to automatically trigger build, test, and security-gate steps upon each code commit. Automating security checks within the pipeline ensures consistent, repeatable enforcement without relying on manual human review for every change.

* **Feedback loops**: Rapid, automated signals returned to the developer about the security and quality state of their code — such as a failed SAST scan blocking a pull request. Short feedback loops are central to DevSecOps: the faster a developer learns their commit introduced a vulnerability, the cheaper and easier it is to fix.

---

### 2. Certification Exam Tips

* **Shift-Left Scenario**: The CDP exam frequently presents scenarios where a vulnerability is discovered late in the pipeline or in production and asks what process change would have prevented it. The answer almost always involves shifting the relevant security check (SAST, SCA, IaC scan) earlier — into the developer commit stage or pull request gate.
* **Culture vs. Tools**: Distinguish between DevSecOps as a cultural shift (shared security ownership) and the tools that enable it. Exam questions may ask which statement best describes the DevSecOps mindset — prioritize answers about shared responsibility and continuous security over answers that focus only on tooling.
* **SDLC Phase Knowledge**: Know which security activity belongs at each SDLC phase: threat modeling (design), SAST (code commit), SCA (build), DAST (staging), container scan (pre-deploy). The exam tests whether you can place the right tool at the right phase.
* **Study Resource**: The [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/) is the authoritative open-source reference for integrating security into DevOps pipelines. Review the introductory sections for foundational principles tested on the CDP exam.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the OWASP DevSecOps Guideline at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/) — an open-source reference maintained by the Open Web Application Security Project that maps security practices (SAST, DAST, SCA, secrets management) to each pipeline stage. Focus on the introduction and pipeline integration sections.
* **Required Video**: Watch the DevSecOps culture segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — a comprehensive free course covering DevSecOps culture through hands-on pipeline examples.

---

### Lab & Command Integration

In this week's hands-on lab, you will apply foundational DevSecOps concepts by:

* **Map security gate checks in the development lifecycle**: Diagram where SAST, SCA, DAST, and container scanning checkpoints belong within a typical CI/CD pipeline, justifying each placement using shift-left principles.
* **Analyze cost differences of finding bugs early vs. late**: Review published defect cost multiplier data and annotate a lifecycle diagram showing the relative cost of fixing a vulnerability at each SDLC phase.
* **Document pipeline structures**: Using the freeCodeCamp course example pipelines as a reference, document a sample GitHub Actions workflow structure — identify trigger events, jobs, steps, and where security steps would be inserted.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand their definitions in the context of pipeline security.
* [ ] Read the OWASP DevSecOps Guideline introduction at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
* [ ] Watch the DevSecOps culture segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the lifecycle diagram and cost analysis in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
