# Discussion Forum: Module 05 — Kubernetes Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Discussion Overview

Post your original response to one scenario below (minimum 175 words). Then reply substantively to at least two classmates' posts (minimum 75 words each). Original posts due Sunday 11:59 PM; peer replies due Tuesday 11:59 PM.

Professor Nash note: Kubernetes security is where theory and practice diverge most dramatically. Textbook configurations often break real applications in ways that require careful tuning. I want to see responses that acknowledge the operational reality of migrating production workloads to restrictive security profiles — not just the security ideal.

---

## Scenario 1 — The PSA Migration Crisis

Your organization is migrating 200 microservices from a Kubernetes 1.20 cluster (with PodSecurityPolicies) to Kubernetes 1.26 (PSP removed, using Pod Security Admission). The security team wants to enable the Restricted profile on all production namespaces. The platform team has run a compatibility scan and discovered that 67 of the 200 services fail the Restricted profile for one of three reasons: running as root, using host path volumes, or needing specific Linux capabilities for networking operations.

Design a migration strategy. How do you use the PSA `warn` and `audit` labels before `enforce`? How do you prioritize which of the 67 non-compliant services to fix first? For the services that legitimately need capabilities or host path access, what is the correct long-term pattern? What is your go-live timeline and what rollback plan do you have if enforcing Restricted causes production outages? Reference specific PSA label configurations and compliant pod spec patterns from this module.

### Scenario 1 — Peer Response Prompt

Your classmate proposed a migration timeline. Is their timeline realistic for 67 non-compliant services? What risk does rushing this migration introduce, and what risk does delaying it introduce?

---

## Scenario 2 — RBAC Privilege Escalation Incident

During a security incident investigation, your team discovers that an attacker who compromised a single pod in the `payments` namespace was able to escalate to full `cluster-admin` access. Your investigation reveals the pod's ServiceAccount had a RoleBinding that allowed `create` on `clusterrolebindings` in the `kube-system` namespace. The attacker used this to bind `cluster-admin` to a new ServiceAccount they created.

Analyze this incident. What RBAC misconfiguration enabled the privilege escalation? What RBAC design principle was violated? How would you audit your cluster to discover similar over-permissioned service accounts? Reference the `kubectl auth can-i --list` commands from this module. What is the broader lesson about which Kubernetes verbs are considered "escalation verbs" and should never be granted to application service accounts? Propose a post-incident RBAC policy that would prevent this class of attack.

### Scenario 2 — Peer Response Prompt

Your classmate proposed a post-incident RBAC policy. Does their policy close the specific escalation vector described? What residual risk remains after their proposed controls are implemented?

---

## Scenario 3 — Network Policy and Service Mesh Trade-offs

Your security team has implemented default-deny Network Policies across all namespaces. Three weeks later, a critical incident reveals that network policy debugging is causing significant operational pain: inter-service communication is regularly broken by misconfigured policies, and on-call engineers spend hours tracing which Network Policy is blocking traffic during incidents. The platform team proposes replacing Network Policies with a service mesh (Istio or Linkerd) to handle both network security and observability.

Evaluate this trade-off. What does a service mesh provide that Network Policies do not? What do Network Policies provide that a service mesh does not? Are they complementary or competing solutions? What is the operational cost of each approach for a team of 10 engineers managing 50 microservices? If you were advising this team, would you recommend keeping Network Policies, migrating to a service mesh, or using both? Be specific about which capabilities of Istio or Linkerd are relevant to this security problem and what the implementation complexity looks like.

### Scenario 3 — Peer Response Prompt

Your classmate recommended a specific approach. What is the single biggest risk of their recommended approach that they may have underweighted in their analysis?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Original post addresses all parts of the chosen scenario | 3 |
| Specific Kubernetes resources, commands, or configurations cited | 2 |
| Operational trade-offs and migration realities acknowledged | 2 |
| Peer reply 1 — substantive challenge or extension | 1.5 |
| Peer reply 2 — substantive challenge or extension | 1.5 |
| Total | 10 |

---

Discussion — Module 05 | CIS-4350 | Texas Wesleyan University | Professor Nash
