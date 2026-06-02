# Discussion Forum: Module 05 - Container Orchestration Security: Kubernetes

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 05 concepts — Kubernetes RBAC, Security Contexts, Network Policies, and API server security — to realistic operational scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Over-Privileged Deployment Pipeline

A startup's DevOps engineer sets up a CI/CD pipeline that deploys to Kubernetes. To avoid permission errors during initial setup, they give the pipeline's service account the built-in `cluster-admin` ClusterRole. The pipeline works perfectly and they never revisit the configuration. Eighteen months later, a supply chain attack compromises one of the GitHub Actions used in the pipeline, and the malicious action exfiltrates the service account token. The attacker now has `cluster-admin` on the production cluster.

In 175-225 words, address the following: Identify what an attacker with `cluster-admin` can do in this cluster — be specific about at least three distinct high-impact actions. Describe the RBAC configuration that should have been in place from the beginning: which specific RBAC objects would you create, what verbs on what resources would you grant, and what scope (namespace vs. cluster) would you use for a pipeline that only needs to update deployments in the `production` namespace? Finally, explain how this incident illustrates the principle of least privilege applied to CI/CD credentials.

---

## Scenario B: The Flat Network Incident

A financial services company runs a Kubernetes cluster with 15 microservices. One service handles payment processing and stores card data. Another service handles marketing email campaigns. A security researcher performing an authorized penetration test compromises the marketing email service through a vulnerability in its Node.js dependencies. From the compromised marketing pod, the researcher is able to reach and query the payment service's database directly using standard network tools, exfiltrating test card data. The cluster has no Network Policies.

In 175-225 words, address the following: Explain precisely why the researcher was able to reach the payment database from the marketing pod — what Kubernetes default behavior enabled this? Describe the Network Policy implementation that would have prevented lateral movement from the marketing namespace to the payment namespace, including the specific policy types (Ingress, Egress) and selectors needed. Explain how the defense-in-depth principle applies here — what other controls (beyond Network Policies) would reduce the risk of data exfiltration even if a pod is compromised?

---

## Scenario C: The Kubernetes Secret Exposure

A DevSecOps engineer audits a Kubernetes cluster and discovers that the team has been treating Kubernetes Secrets as secure storage for database credentials. The team believes that because they used `kubectl create secret`, the credentials are encrypted. Another engineer argues that all Secrets should be stored in HashiCorp Vault instead, but the team lead dismisses this as "over-engineering."

In 175-225 words, address the following: Explain what the team misunderstands about Kubernetes Secret storage — specifically, how Secrets are stored in etcd by default and what "base64 encoding" means versus encryption. Identify two scenarios where an attacker could retrieve the Secret value despite the team's belief that it is protected. Evaluate the engineer's Vault proposal — is it over-engineering or appropriate security hardening? Describe the middle-ground solution (encryption at rest via EncryptionConfiguration) that would significantly improve security without requiring a Vault deployment.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise Kubernetes and DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario elements with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most elements but lacks technical depth in one or more areas.
- 0-2 pts: Incomplete, missing, or does not substantively address the scenario.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios.

- 4 pts: Two substantive responses (at least 50 words each) that add technical content, propose an alternative approach, or cite a specific reading guide concept.
- 2 pts: Only one substantive response, or both are superficial.
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

Scenario A connects directly to a real attack pattern: over-privileged CI/CD service accounts are one of the most common Kubernetes security findings in enterprise security audits. When writing your RBAC configuration in your response, use the actual RBAC verb names (`update`, `patch`, `get`, `list`) rather than vague descriptions. Precision matters — "read access" is not the same as "get + list + watch", and the exam will test whether you know the difference.
