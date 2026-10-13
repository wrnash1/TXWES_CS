# Discussion Forum: Module 12 — Kubernetes Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

This week's discussion explores Kubernetes security through three scenarios drawn from real-world cluster incidents, RBAC misconfigurations, and Network Policy deployment failures. Initial posts are due Wednesday at 11:59 PM Central. Peer responses are due Sunday at 11:59 PM Central.

---

### Scenario 1 — The Compromised CI/CD Pipeline

A fintech company's GitHub Actions pipeline uses a Kubernetes service account named `deploy-sa` to push application updates to the `payments-prod` namespace. An incident investigation reveals that an attacker who compromised a pull request workflow used the pipeline's credentials to enumerate all Secrets in the cluster, discover database passwords, and exfiltrate payment processing credentials. The root cause: `deploy-sa` was bound to the `cluster-admin` ClusterRole via a ClusterRoleBinding because "it was the easiest way to make the pipeline work."

In 175–225 words, analyze this incident and design the remediation from an RBAC perspective. Address:

- What specific RBAC objects should replace the `cluster-admin` ClusterRoleBinding — be precise about Role versus ClusterRole, the namespace scope, and the minimum verbs and resources required for a deployment-only service account
- Why the attacker was able to read Secrets in namespaces outside `payments-prod`, and what the correct RBAC design would have prevented — use the `kubectl auth can-i` command syntax in your explanation to show how the team could have validated the permissions before deployment
- What additional Kubernetes control (beyond RBAC) would prevent the pipeline service account's pods from making network connections to Secrets store endpoints or cross-namespace database services even if RBAC were misconfigured again

---

### Scenario 2 — The Network Policy Migration Failure

A startup deploys a default-deny-all NetworkPolicy to their `app-prod` namespace as the first step in a micro-segmentation initiative. Within 90 seconds, all 12 microservices in the namespace are reporting DNS resolution failures, health check timeouts, and database connection errors. The on-call engineer rolls back the NetworkPolicy and opens a ticket: "Network Policies break everything — we should not use them."

In 175–225 words, write a technical post-mortem explaining what went wrong and how to implement Network Policies correctly. Address:

- The specific traffic flows that the default-deny-all policy blocked that caused DNS failures — name the protocol, port number, and destination namespace, and write the NetworkPolicy `egress` rule snippet that would have prevented this failure
- The correct implementation sequence for rolling out Network Policies to a namespace that already has running workloads — explain how to use the `warn` mode of PodSecurity as an analogy for how you would test Network Policy behavior with a dry-run or logging approach before applying enforcement
- Why the engineer's conclusion ("Network Policies break everything") demonstrates a misunderstanding of the technology, and what the correct DevSecOps posture is when a security control causes application failures on first deployment

---

### Scenario 3 — The Privileged Container Escape

A security audit of a production Kubernetes cluster finds that 8 out of 14 application Deployments have containers running with the default Security Context — no `runAsNonRoot`, no `allowPrivilegeEscalation: false`, no `readOnlyRootFilesystem`. One container is running as root. During a penetration test, the tester exploits a Remote Code Execution vulnerability in one of the root-running containers and demonstrates a container escape to the Kubernetes node. The CISO asks: "How do we prevent this class of attack systematically — not just fix these 8 deployments?"

In 175–225 words, respond to the CISO with a systematic hardening plan that addresses:

- The three specific Security Context fields that, if properly set, would have made the container escape significantly harder or impossible — explain the security mechanism of each field (`runAsNonRoot`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`) in terms a CISO can understand, and name the specific Linux kernel feature that `allowPrivilegeEscalation: false` controls
- How the PodSecurity admission controller with the `restricted` profile and `enforce` mode would prevent these misconfigurations from being deployed in the future — name the specific namespace label syntax required and explain what happens at `kubectl apply` time when a pod violates the profile
- How Checkov with `--framework kubernetes` and `soft_fail: false` in the CI pipeline would have caught these misconfigurations before they ever reached the cluster — name at least two specific CKV_K8S_* check IDs that would have fired on these Deployments

---

### Peer Response Requirements

After your initial post, write substantive replies to at least two classmates (minimum 60 words each). Your peer responses should:

- Add a specific technical detail the original post did not mention
- Challenge an assumption or offer a more precise solution
- Connect the scenario to an adjacent DevSecOps control covered in a previous module

Simple agreement or restatement of the original post does not satisfy the substantive requirement.

---

### Discussion Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post addresses all required elements with technical precision — names specific RBAC objects, NetworkPolicy fields, and Security Context fields | 4 |
| Initial post demonstrates understanding of Kubernetes security layers (RBAC, Network Policy, Security Context, PodSecurity) | 2 |
| Initial post meets the 175–225 word count requirement | 1 |
| First peer response is substantive — adds new technical content or a precise alternative | 1.5 |
| Second peer response is substantive — adds new technical content or a precise alternative | 1.5 |
| **Total** | **10** |

---

### Grading Notes

- Posts must name specific Kubernetes objects (Role, RoleBinding, ClusterRole, NetworkPolicy, podSelector) to receive full technical precision credit.
- Answers to Scenario 1 that say "use least privilege" without specifying which verbs and resources the Role should contain receive partial credit only.
- Answers to Scenario 3 that do not name specific CKV_K8S_* check IDs receive partial credit only.

---

### Professor Nash Note

The three scenarios here represent the three most common Kubernetes security failures I see in real production environments: over-permissive CI/CD credentials, Network Policy rollout without DNS egress planning, and containers running with default (insecure) Security Contexts. The pattern across all three is the same: security controls were either skipped because they seemed difficult, or applied without understanding their dependencies. Your posts should demonstrate that you understand not just the controls themselves but the failure modes that occur when they are applied incorrectly.
