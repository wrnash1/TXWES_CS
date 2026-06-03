# Discussion: Module 03 — Compute Engine

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This discussion asks you to apply Compute Engine concepts to realistic
infrastructure design problems. The scenarios below represent the kind of
architectural decisions cloud engineers make daily and that appear in ACE
exam scenario questions.

**Due:** See course calendar for deadlines.

**Grading:** Initial post (60 points) + two peer responses (20 points each) = 100 points

---

## Prompt A — Infrastructure Design for High Availability (Choose One)

A regional e-commerce company runs its web storefront on a single Compute
Engine VM in `us-central1-a`. The VM uses a pd-standard boot disk and has no
backups. Traffic spikes during sales events — sometimes to 10x the baseline
load — and the site has gone down during two major sales in the past year.

In your post, design a Compute Engine architecture that addresses these problems:

1. Describe your complete Compute Engine configuration, including:
   - Machine family and type you would choose and why
   - Disk type(s) and why
   - Instance group type (zonal vs. regional MIG) and zone placement
2. Design an autoscaling policy. Specify:
   - Minimum and maximum instance counts and your reasoning
   - Which autoscaling signal you would use and the target value
   - Cool-down period and why it matters during traffic spikes
3. Explain how you would create a backup and recovery strategy using
   Compute Engine features. Include snapshot policy recommendations.
4. Describe how startup scripts fit into the new architecture. What would
   your startup script do, and how would it be delivered to instances?

---

## Prompt B — Cost Optimization Analysis (Choose One)

Your company runs a mixed compute workload on GCP with the following components:

- 8 web servers running 24/7 serving production traffic
- A machine learning training job that runs 3 hours per day
- A nightly data pipeline that processes files for 5 hours; retries on failure
- A development environment used 8 hours per day, Monday–Friday only
- A database server that must never be interrupted

Analyze the cost-optimization strategy for each workload:

1. For each workload, recommend the appropriate VM pricing model
   (on-demand, committed use discount, sustained use discount, Spot VM, or
   preemptible VM). Justify each choice.
2. For the development environment, describe how autoscaling and scheduled
   scaling could reduce costs. Include specific parameters in your answer.
3. Explain the risk/reward trade-off of using Spot VMs for the data pipeline.
   What design patterns would you implement to make it production-safe?
4. Calculate the approximate monthly cost impact of your recommendations
   compared to running all workloads on on-demand e2-standard-4 VMs. Use
   the GCP Pricing Calculator at cloud.google.com/products/calculator and
   document your assumptions.

---

## Response Requirements

Your initial post must be at least 300 words and include:

- Specific GCP machine types or families by name (e.g., `e2-medium`, `n2-standard-4`)
- Quantitative reasoning where applicable (instance counts, percentages, costs)
- At least one trade-off you considered and rejected, with explanation

Your two peer responses must each be at least 100 words and do one of the
following:

- Identify a workload requirement the original post may have overlooked
- Propose a different configuration and explain the trade-off
- Challenge a cost or availability assumption with evidence or reasoning

---

## Discussion Tips

- The GCP pricing calculator is your friend. Use it to get real numbers
  before making cost-based arguments.
- The ACE exam often presents scenarios with two plausible answers. Practice
  articulating why one is better than the other in a specific context.
- Think about failure modes. For every design choice, ask: what happens when
  this component fails?

---

## Reflection Question (Optional — Extra Credit)

Compare a managed instance group with autoscaling to a Kubernetes deployment
with the Horizontal Pod Autoscaler. In what scenarios would you choose one
over the other, and what are the operational trade-offs? Minimum 150 words.

---

End of Discussion — Module 03

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
