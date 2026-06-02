# Video Script: Module 01 - DevOps Fundamentals and the DevSecOps Mindset

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 01 — DevOps Fundamentals and the DevSecOps Mindset"

**Audio:**

"Welcome to CIS-4350, DevSecOps and CI/CD Pipelines. I'm Professor Nash, and in this opening module we're going to build the conceptual foundation that every subsequent module depends on.

By the end of this video you'll be able to explain what DevSecOps is and why it exists, describe the evolution from waterfall development through DevOps to DevSecOps, define shift-left security with concrete examples, and identify where each class of security tool belongs in the software delivery lifecycle.

These concepts are directly tested on the DevSecOps Professional certification exam, so let's get into it."

---

### [01:30 - 05:00] The Evolution: Waterfall to DevOps to DevSecOps

**Visual:** Timeline diagram — Waterfall (1970s) to Agile (2001) to DevOps (2009) to DevSecOps (2012-present)

**Audio:**

"To understand DevSecOps, we need to understand the problem it solves. Let's go back to traditional software development.

In the waterfall model — which dominated from the 1970s through the 1990s — development happened in strict sequential phases: requirements, design, implementation, testing, deployment. Security was positioned near the end, typically a 'security review' or 'penetration test' before go-live. The problem? By the time you found a SQL injection vulnerability in the security review, the code had already been written, tested, integrated, and was sitting in a release candidate. Fixing it was expensive. Research from that era showed that fixing a defect in production could cost 100 times more than fixing it during design.

Then Agile emerged — shorter iterations, faster feedback, continuous stakeholder collaboration. Better, but security still lagged. The Agile Manifesto said nothing about security.

DevOps — popularized around 2009 — broke down the wall between Development and Operations. Suddenly teams were releasing code multiple times per day using CI/CD pipelines, Infrastructure as Code, and automated testing. The velocity was remarkable.

But here is the problem that DevSecOps addresses: when you are deploying dozens of times per day, a manual security review every six weeks does not work. Security became the bottleneck. The security team was perpetually behind. Vulnerabilities were shipping to production faster than they could be reviewed.

DevSecOps — sometimes called Rugged DevOps — emerged around 2012 to solve this. The core idea: embed security controls directly into the CI/CD pipeline so that security checking happens automatically on every single commit, every single deployment, without human bottlenecks."

---

### [05:00 - 09:00] The Three Pillars of DevSecOps

**Visual:** Three-column diagram — People, Process, Technology

**Audio:**

"The DevSecOps model rests on three pillars: People, Process, and Technology. Let's walk through each.

**People.** DevSecOps requires a cultural shift. Developers are no longer just responsible for making features work — they are co-owners of security. This is sometimes implemented through 'security champions' — developers within each team who receive extra security training and serve as liaisons to the dedicated security team. Operations engineers are responsible for secure infrastructure configuration. Security professionals shift from gatekeepers to enablers: they build the tools, write the policies, and train the teams rather than reviewing everything manually.

**Process.** The key process change is integrating security activities into existing development workflows rather than adding separate security phases. Code review now includes security checklists. Pull requests trigger automated scans. Sprint planning includes threat modeling for new features. Incident response includes post-mortems that feed back into pipeline policy.

**Technology.** This is where the CI/CD pipeline tools come in. Automated Static Application Security Testing — SAST — scans source code at commit time. Software Composition Analysis — SCA — checks dependencies for known vulnerabilities at build time. Dynamic Application Security Testing — DAST — tests running applications in staging. Container scanning checks Docker images before deployment. Infrastructure as Code scanning checks Terraform configurations before provisioning.

Each of these we will cover in depth in later modules. Today we are establishing why they exist and where they fit."

---

### [09:00 - 13:00] Shift-Left Security: The Core Concept

**Visual:** SDLC cost curve — exponentially increasing cost from Design to Code to Test to Staging to Production

**Audio:**

"The single most important conceptual term in DevSecOps — and on the certification exam — is 'shift left.' Let me explain it precisely.

Imagine a timeline of the software development lifecycle laid out horizontally. On the left side: design and coding. On the right side: staging, production, post-deployment. Shifting left means moving security activities toward the left side of that timeline — earlier in the process.

Why does this matter economically? The cost of fixing a vulnerability increases dramatically the later it is found. A hardcoded credential found by a developer before they commit costs minutes to fix. The same credential found in a production security audit six months later means potential data breach, incident response, credential rotation across all environments, a security advisory, and possible regulatory notification. The cost difference is orders of magnitude.

Shift-left security means: put the controls where the cost of detection is lowest. That is as early as possible in the developer's workflow.

**[SHOW CODE]**

Here is a concrete example. A pre-commit hook is the earliest possible shift-left control. When a developer runs `git commit`, this hook fires before the commit is finalized:

```bash
#!/bin/sh
# .git/hooks/pre-commit
# Run Gitleaks to detect secrets before commit is created
gitleaks detect --source . --no-git --exit-code 1
if [ $? -ne 0 ]; then
  echo "BLOCKED: Secret detected. Remove credentials before committing."
  exit 1
fi
```

This runs on the developer's local machine before the commit even exists in Git history. If it finds an API key, the commit is blocked. The secret never enters the repository. That is shift-left in its purest form — detection at the earliest possible moment, on the developer's own workstation.

Compare that to scanning the running production application — same security check, but now the secret has been in production for however long the application has been running. The risk exposure is vastly different."

---

### [13:00 - 17:00] The DevSecOps Pipeline: Security Gates Overview

**Visual:** CI/CD pipeline diagram with labeled security stages — Pre-commit, Build, Test, Staging, Deploy, Monitor

**Audio:**

"Let's map the security tools to the pipeline stages. This mapping is critical for the exam and for designing real DevSecOps pipelines.

**Pre-commit stage:** Secrets scanning with tools like Gitleaks or truffleHog. Pre-commit hooks run on the developer's machine before code is pushed. This is the earliest possible gate.

**Code commit and pull request:** SAST — Static Application Security Testing. Tools like Semgrep, Checkmarx, or SonarQube analyze source code without executing it, looking for vulnerability patterns: SQL injection, cross-site scripting, insecure deserialization, and hardcoded credentials.

**Build stage:** SCA — Software Composition Analysis. When your build process downloads dependencies — npm packages, Maven jars, Python pip packages — SCA tools like Snyk, OWASP Dependency-Check, or Grype scan those dependencies against vulnerability databases like the NVD. A dependency with a known critical CVE fails the build.

**Container build:** Container image scanning. When you build a Docker image, tools like Trivy scan the base image layers and installed packages for CVEs before the image is pushed to a registry.

**Staging deployment:** DAST — Dynamic Application Security Testing. Tools like OWASP ZAP send actual HTTP requests to the running application looking for runtime vulnerabilities that SAST cannot find because they only appear during execution.

**Infrastructure provisioning:** IaC scanning. When Terraform configurations are being applied, tools like Checkov or tfsec scan the .tf files for misconfigurations: publicly exposed S3 buckets, security groups with overly permissive ingress rules, missing encryption settings.

**Production monitoring:** Runtime security monitoring with tools like Falco for container runtime anomaly detection.

Each of these stages has its own module in this course. Right now, what you need to understand is the architecture: security is not a single gate at the end. It is a series of automated checks at every stage, each catching the class of vulnerability most efficiently detectable at that point."

---

### [17:00 - 20:00] Feedback Loops and Why They Matter

**Visual:** Diagram showing short feedback loop vs. long feedback loop with cost annotations

**Audio:**

"The second critical concept after shift-left is the feedback loop. In DevSecOps, a feedback loop is the time between when a developer introduces a vulnerability and when they are notified about it.

In traditional security models, the feedback loop could be measured in weeks or months — a developer writes vulnerable code, it ships, a penetration test happens six weeks later, a ticket is filed, the developer is contacted. By then they have moved on to three other features and have zero context on the original code.

In DevSecOps, the goal is to make feedback loops as short as possible. Ideally, a developer gets a failed security check notification within minutes of pushing code. At that point they still have the code open in their editor, they understand what they just wrote, and the fix takes minutes.

This is why pipeline integration matters. A SAST scan that runs as a GitHub Actions job on every pull request and posts its results as a PR comment achieves a tight feedback loop. The developer sees the issue immediately, in context, while fixing it is cheap.

The feedback loop concept also applies at the organizational level: when a production security incident occurs, the lessons learned need to feed back into pipeline policy changes — new SAST rules, updated dependency blocklists, new IaC scan checks — so the same class of vulnerability is automatically prevented in the future."

---

### [20:00 - 22:30] DevSecOps Professional Exam Alignment

**Visual:** Exam objective checklist on screen

**Audio:**

"Let me connect everything we have covered to the DevSecOps Professional certification objectives.

The exam tests your ability to explain the DevSecOps philosophy and distinguish it from traditional security models. Know the three pillars: People, Process, Technology. Know that DevSecOps is a culture and set of practices, not just a collection of tools.

The exam will present scenario questions where you must identify which security activity should be added at which pipeline stage. Use this mental model: SAST at commit, SCA at build, DAST at staging, container scan at image build, IaC scan at provisioning.

The exam tests the business case for shift-left: the cost multiplier for late-stage vulnerability discovery. Know that earlier detection costs less to remediate.

Finally, the exam tests understanding of the shared responsibility model: developers own secure code, operations owns secure infrastructure, security teams own tooling and policy and training. No single role owns security in DevSecOps — it is a shared responsibility.

In the next module, we will get hands-on with version control and Git — the foundation everything else is built on. For this module's lab, you will create a shift-left security map documenting which tools and controls belong at each stage of a sample CI/CD pipeline. Complete the reading guide and quiz before moving on."

---

### [22:30 - End] Closing

**Visual:** Instructor on camera

**Audio:**

"That wraps up Module 01. The key takeaways: DevSecOps embeds security at every CI/CD pipeline stage rather than treating it as a final gate. Shift-left means detecting vulnerabilities earlier when they are cheapest to fix. Feedback loops should be as short as possible. Security is a shared responsibility across developers, operations, and security teams.

See you in Module 02."
