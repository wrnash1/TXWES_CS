# Reading Guide: Module 07 - DAST – Dynamic Application Security Testing

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 07 - DAST – Dynamic Application Security Testing**! This module covers DAST as the pipeline security gate that tests a running application from the outside, simulating real attacker behavior against deployed endpoints. You will learn how DAST tools like OWASP ZAP interact with a live web application to probe for vulnerabilities that only manifest at runtime — such as authentication flaws, session management issues, and server-side injection — and how DAST is integrated into staging-environment pipelines. Understanding the distinction between SAST and DAST, and knowing when each is appropriate, is a core CDP exam topic.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **DAST scanners**: Security tools that test a running application by sending crafted HTTP requests and analyzing responses to detect vulnerabilities. Unlike SAST, DAST requires no access to source code and tests the application from an external attacker's perspective. Common DAST tools include OWASP ZAP, Burp Suite Professional, and Nikto. In a DevSecOps pipeline, DAST typically runs against a staging environment after a successful build and deploy step.

* **OWASP ZAP**: The OWASP Zed Attack Proxy, a free and open-source DAST scanner maintained by the Open Web Application Security Project. ZAP can run in both interactive (GUI) and headless (daemon) modes, making it suitable for CI/CD pipeline integration. ZAP's automated scan action is available as a GitHub Actions step, enabling teams to add DAST to their pipeline with minimal configuration.

* **Active scanning**: A DAST mode in which the scanner actively sends attack payloads — such as SQL injection strings, XSS vectors, and path traversal sequences — to application endpoints to elicit vulnerable responses. Active scanning is more thorough than passive scanning but generates significant traffic and should only run against isolated test or staging environments, never directly against production.

* **Sandbox testing**: The practice of running DAST against an isolated, ephemeral environment that mirrors production configuration but contains no real user data. Pipeline-integrated DAST typically spins up a Docker Compose or Kubernetes namespace environment as part of the workflow, runs the DAST scan, and tears down the environment after results are collected.

* **Network responses**: The HTTP status codes, headers, and body content returned by an application in response to DAST probe requests. DAST scanners analyze response characteristics (e.g., error messages containing stack traces, unexpected 200 responses to injection payloads, missing security headers) to identify vulnerabilities. Response analysis is fundamentally what distinguishes DAST from SAST.

---

### 2. Certification Exam Tips

* **SAST vs. DAST — Which Finds What**: The CDP exam tests which tool category detects specific vulnerability types. SAST finds: hardcoded secrets, injection patterns in source code, insecure function calls. DAST finds: authentication bypass in live sessions, missing security headers, server-side injection confirmed by actual responses, business logic flaws that only manifest at runtime.
* **Pipeline Stage for DAST**: DAST runs after deployment to a staging environment — it cannot run without a live application. The correct pipeline order is: SAST (code commit) → build → SCA (build) → deploy to staging → DAST (staging) → deploy to production.
* **Passive vs. Active Scanning**: Passive scanning (ZAP spider/crawl) observes traffic without sending attack payloads — lower risk but lower coverage. Active scanning sends crafted payloads — higher coverage but must be scoped to avoid testing production. The CDP exam tests this distinction.
* **Study Resource**: The [OWASP ZAP documentation](https://www.zaproxy.org/docs/) provides the full reference for ZAP scan modes, automation framework configuration, and GitHub Actions integration — review the "Automate" section for CDP exam pipeline integration questions.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [OWASP ZAP Automation Framework documentation](https://www.zaproxy.org/docs/automate/) — covers how to run ZAP in headless mode within a CI/CD pipeline, configure scan policies, and interpret JSON/HTML reports. Focus on the GitHub Actions integration section for CDP exam pipeline design questions.
* **Required Video**: Watch the DAST pipeline integration segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates deploying a test web application in a pipeline, running OWASP ZAP against it, and evaluating DAST findings as a pipeline gate.

---

### Lab & Command Integration

In this week's hands-on lab, you will integrate DAST into a staging pipeline by:

* **Setup web app in a pipeline container**: Add a Docker Compose or GitHub Actions service container step that starts a vulnerable web application (e.g., DVWA or Juice Shop) on a local port within the CI runner environment.
* **Run a DAST scanner against web endpoint**: Add an OWASP ZAP GitHub Actions step (using `zaproxy/action-full-scan@v0.10.0` or equivalent) pointing to the local application URL, configured to perform a baseline or full active scan.
* **Verify vulnerability detections**: Review the ZAP HTML report generated as a pipeline artifact — identify at least two confirmed findings, their risk level, the CWE reference, and the recommended fix.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand the difference between active and passive DAST scanning.
* [ ] Read the OWASP ZAP Automation Framework docs at [https://www.zaproxy.org/docs/automate/](https://www.zaproxy.org/docs/automate/).
* [ ] Watch the DAST segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the DAST pipeline integration and report review in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
