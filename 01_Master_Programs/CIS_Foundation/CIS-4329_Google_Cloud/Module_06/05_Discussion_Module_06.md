# Discussion: Module 06 — Google Kubernetes Engine (GKE)

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This discussion asks you to apply GKE architecture principles to realistic
production scenarios. Kubernetes is the dominant container orchestration
platform in enterprise environments, and the ability to design GKE deployments
correctly is a highly valued cloud engineering skill.

**Due:** See course calendar for deadlines.

**Grading:** Initial post (60 points) + two peer responses (20 points each) = 100 points

---

## Prompt A — GKE Architecture Design (Choose One)

A startup is building a multi-tenant SaaS platform. Their application has
three components:

- A high-traffic HTTP API serving thousands of requests per second
- A machine learning inference service that requires GPU acceleration
- A nightly batch job that processes large datasets for 2–4 hours, fault-tolerant

The engineering team is three people and does not want to spend time managing
Kubernetes infrastructure. They expect traffic to be variable — low overnight,
peak during business hours.

Design a GKE architecture for this platform:

1. Choose Standard or Autopilot for this scenario and justify your choice.
   If Standard, describe the node pool structure.
2. Describe the Kubernetes objects you would deploy for each component
   (Deployment vs. StatefulSet vs. Job, Service type, HPA settings).
3. Explain how you would handle the GPU inference service on a shared cluster.
   Include node pool configuration and pod scheduling constraints.
4. Describe the autoscaling strategy for the HTTP API, including what signals
   you would use for the HPA and how the Cluster Autoscaler fits in.
5. Explain how you would expose the HTTP API externally while keeping the
   inference service internal.

---

## Prompt B — GKE Migration Analysis (Choose One)

A financial services firm currently runs a 20-service microservices application
on bare-metal servers in their own data center. They are evaluating migration
to GKE. The application has these characteristics:

- Services communicate over HTTP/2 and gRPC
- Two services require stateful storage with guaranteed IOPS
- One service processes payments and must meet PCI-DSS compliance requirements
- The team currently uses Ansible and shell scripts for deployment; they have
  no Kubernetes experience
- The application must maintain 99.9% uptime with zero planned downtime windows

Analyze the migration path and produce recommendations:

1. Should they use Standard or Autopilot? Discuss the trade-offs given their
   experience level and compliance requirements.
2. Describe the Kubernetes service types and Ingress configuration needed for
   gRPC and HTTP/2 traffic.
3. Explain how to address the stateful storage requirement. What Kubernetes
   and GCP storage objects are involved?
4. Describe the cluster configuration (zonal vs. regional, node pool design)
   needed to meet the 99.9% uptime requirement.
5. Propose a phased migration approach that minimizes risk for a team new to
   Kubernetes.

---

## Response Requirements

Your initial post must be at least 300 words and include:

- Specific Kubernetes object types and GKE features by name
- Explicit reasoning for architecture decisions, including trade-offs considered
- At least one decision where you explain why you chose one option over another

Your two peer responses must each be at least 100 words and do one of the
following:

- Identify a failure scenario the original architecture does not handle
- Challenge a specific design choice with a concrete alternative
- Add a security or compliance consideration the post did not address

---

## Discussion Tips

- The Kubernetes documentation at kubernetes.io/docs is the authoritative
  reference for object types and their configuration options.
- Think about the "day 2" operational experience, not just the initial
  deployment. Who will maintain this cluster? How will upgrades work?
- The ACE exam frequently presents scenario questions with two plausible
  cluster configurations. Practice articulating why one fits better.

---

## Reflection Question (Optional — Extra Credit)

Compare running workloads on GKE (with Cluster Autoscaler) to running the same
workloads on Compute Engine managed instance groups (with autoscaling). Describe
two scenarios where you would clearly prefer GKE and two scenarios where a MIG
would be the better choice. Minimum 150 words.

---

End of Discussion — Module 06

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
