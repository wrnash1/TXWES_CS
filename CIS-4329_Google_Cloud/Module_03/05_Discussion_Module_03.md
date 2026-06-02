# Discussion — Module 03

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Compute Engine Architecture and VM Design Decisions

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. In your peer responses, you may respond to classmates who chose any scenario.

Initial Post due: Wednesday at 11:59 PM Central

Peer Responses due: Sunday at 11:59 PM Central

---

## Scenario A — The Lift-and-Shift Migration

A mid-size logistics company is migrating its on-premises application server fleet to Google Cloud. The fleet consists of 30 Windows Server 2019 VMs and 20 Linux (CentOS 7) VMs. Each VM has been manually configured with company-specific software, security baselines, and monitoring agents installed over the past three years. The IT team wants to minimize reboot time, maintain configuration consistency across all VMs, and reduce the manual effort of re-configuring each VM after migration. They have a three-month timeline.

In 175–225 words, address the following:

- Which Compute Engine feature would you use to preserve the current VM configurations and deploy them consistently to GCP? Explain your choice.
- Would you use startup scripts, custom images, or both? Justify your approach.
- What machine families would you evaluate for the Windows and Linux workloads, and what information would you need to select the right machine type for each?

---

## Scenario B — The Cost-Optimized Analytics Platform

A university research department runs a genomics data processing pipeline that executes 8-hour batch jobs twice per week. Each job spawns 200 worker VMs that process data in parallel and write results to Cloud Storage. The jobs are fully fault-tolerant — if a VM fails mid-job, the pipeline detects it and retries that segment on a new VM. The department has a tight annual budget and needs to minimize per-job compute costs.

In 175–225 words, address the following:

- Which Compute Engine pricing model should the department use for the worker VMs and why?
- What machine family is most appropriate for CPU-intensive genomics computation?
- The department runs these jobs only twice per week for 8 hours each. Would committed use discounts make sense here? Show your reasoning.
- What architecture would you use to automatically provision 200 VMs at job start and tear them down when the job completes?

---

## Scenario C — The High-Availability Web Application

A startup is deploying its first production web application on GCP. The application must remain available even if a single data center (zone) experiences a hardware failure. The startup expects to handle 1,000 to 10,000 simultaneous users during peak hours, with low traffic overnight. The team has no dedicated infrastructure staff and wants to minimize manual scaling operations.

In 175–225 words, address the following:

- Which Compute Engine feature would you use to automatically scale the VM fleet up and down based on user demand? Name the specific feature and explain how it works.
- How would you deploy the web servers across multiple zones to survive a zone failure? Name the specific architecture.
- The startup's developers have a custom Nginx configuration with their application baked in. How would they ensure all auto-scaled VMs start with the exact same configuration?
- What disk type would you use for the application VMs, and would you use local SSDs for the application data?

---

## Peer Response Guidelines

Your peer responses must be at least 50 words each. A strong peer response does at least one of the following:

- Identifies a trade-off the classmate did not mention in their design
- Suggests a specific gcloud command or Console workflow the classmate could use to implement part of their solution
- Questions an assumption in the classmate's machine type or pricing choice and proposes an alternative
- Connects the scenario to something learned in the lab exercise

Responses that consist only of agreement without substantive technical content receive no credit.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all sub-questions with accurate Compute Engine terminology, names specific GCP features (custom images, MIGs, Spot VMs, etc.), and provides justified reasoning for each choice. 175–225 words.
- 3–4 pts: Addresses most sub-questions but uses vague terminology or lacks justification for design choices.
- 1–2 pts: Addresses only one sub-question or contains significant factual errors about Compute Engine.
- 0 pts: Initial post not submitted by the Wednesday deadline.

Peer Responses — 4 Points:

- 4 pts: Two responses submitted by Sunday, each at least 50 words, each contributing specific technical additions.
- 2 pts: Only one qualifying response, or both are superficial.
- 0 pts: No peer responses submitted.

---

Professor Nash note: Compute Engine architecture decisions involve real trade-offs between cost, availability, maintainability, and performance. In your posts, go beyond naming features — explain why you chose each feature over alternatives. "I would use a Managed Instance Group because it provides autoscaling" is a start, but "I would use a regional MIG because it spans three zones and will automatically redistribute traffic if zone us-central1-a fails" shows you understand the actual resilience benefit.

---

End of Discussion — Module 03

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
