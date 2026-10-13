# Discussion Forum: Module 13 — Compliance as Code

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

This week's discussion explores compliance as code through three scenarios covering Rego policy design, Gatekeeper adoption in production, and organizational policy governance. Initial posts are due Wednesday at 11:59 PM Central. Peer responses are due Sunday at 11:59 PM Central.

---

### Scenario 1 — The Developer Objection to Policy Gates

A senior engineer at a payments company pushes back against adding Conftest to the CI/CD pipeline. The team already has a manual security review checklist that engineers fill out before merging any change that modifies Kubernetes manifests. The engineer argues: "We already have a process — the checklist catches the same issues Conftest would. Adding an automated gate is just distrust of the engineering team, and it will slow down our deployment pipeline." Two weeks later, a P1 incident occurs when a new engineer, unfamiliar with the checklist, deploys a pod with `privileged: true` and `hostNetwork: true` to the production namespace. A penetration tester later demonstrates that the configuration would have allowed a container breakout.

In 175–225 words, analyze this incident and the engineer's objection. Address:

- The specific failure mode of a manual checklist versus automated policy gates, using the term "policy drift" to describe what happens when compliance documentation and actual deployed configurations diverge over time
- Why compliance as code provides an audit trail that a manual checklist cannot — specifically, what artifact is created when a Conftest violation fires in a GitHub Actions workflow and how that artifact supports a SOC 2 or PCI-DSS audit
- What the correct Gatekeeper `enforcementAction` migration strategy would have been for this team, naming all three phases in order and explaining what the `dryrun` phase would have revealed before any enforcement was applied

---

### Scenario 2 — The Overly Restrictive Policy Incident

A platform team deploys Gatekeeper with a ConstraintTemplate that enforces SOC 2 CC6.1 resource limits across all namespaces with `enforcementAction: deny`. Within four hours, the on-call engineer receives alerts: the cluster autoscaler cannot create new nodes because the Kubernetes system components in `kube-system` — including CoreDNS and the metrics-server — do not have explicit resource limits in their managed manifests and are being blocked by the Constraint. The cluster is degraded. The team disables Gatekeeper entirely to restore service.

In 175–225 words, design a remediation plan that prevents this scenario from recurring. Address:

- The specific Constraint field that should have been used to exclude `kube-system` and other system namespaces from the policy scope — provide the exact YAML field path and the value that would exclude `kube-system`
- Why deploying a policy directly with `enforcementAction: deny` without a `dryrun` phase represents a governance failure, and what the `dryrun` audit output would have shown about existing violations in `kube-system` before enforcement
- The correct namespace label strategy using the PodSecurity admission controller's `privileged` profile as a precedent, explaining how the same separation-of-concerns pattern applies to Gatekeeper Constraint scope

---

### Scenario 3 — The Compliance Evidence Gap

A DevSecOps team at a healthcare company is preparing for their SOC 2 Type II audit. The auditors request evidence that all containers in the production Kubernetes environment are running as non-root at all times and that this control has been consistently enforced over the 12-month audit period. The team has Gatekeeper deployed with `K8sRequireNonRoot` Constraints set to `deny` in the production namespace. However, the audit team's evidence request asks for: (1) the policy definition, (2) proof that the policy was enforced throughout the audit period, and (3) evidence of what happened when a violation was attempted.

In 175–225 words, describe a complete compliance evidence package. Address:

- How the Rego policy stored in a Git repository with commit history satisfies the policy definition requirement — specifically, what git metadata (beyond the file content itself) demonstrates that the policy was reviewed, approved, and has not been modified without review
- How the Gatekeeper audit controller's `.status.violations` field in combination with a SIEM or log aggregation system provides continuous enforcement evidence — name the specific Kubernetes API object field path and explain how periodic scraping of that field over 12 months creates an audit trail
- What a denied admission event looks like in the Kubernetes audit log, including which audit log field contains the policy violation message and how that field maps to a specific compliance control reference in your Rego deny message

---

### Peer Response Requirements

After your initial post, write substantive replies to at least two classmates (minimum 60 words each). Your peer responses should:

- Add a technical detail the original post omitted or a more precise implementation of the proposed solution
- Identify a potential weakness in the proposed approach and suggest how to address it
- Connect the compliance-as-code scenario to a DevSecOps control from an earlier module (CSPM, runtime security, SIEM)

Simple agreement or restatement of the original post does not meet the substantive requirement.

---

### Discussion Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post addresses all required elements with technical specificity — names Gatekeeper fields, Rego constructs, and compliance control references | 4 |
| Initial post demonstrates understanding of the compliance evidence use case for policy-as-code, not just the technical implementation | 2 |
| Initial post meets the 175–225 word count requirement | 1 |
| First peer response is substantive — adds technical content or a specific alternative | 1.5 |
| Second peer response is substantive — adds technical content or a specific alternative | 1.5 |
| **Total** | **10** |

---

### Grading Notes

- Scenario 1 posts that describe the Gatekeeper migration phases without naming all three (`dryrun`, `warn`, `deny`) receive partial credit only.
- Scenario 2 posts that say "exclude system namespaces" without providing the specific Constraint field path (`spec.match.excludedNamespaces`) receive partial credit only.
- Scenario 3 posts that describe compliance evidence in general terms without referencing the Kubernetes audit log or the `.status.violations` field receive partial credit only.

---

### Professor Nash Note

The three scenarios in this module's discussion are deliberately focused on the organizational and audit dimensions of compliance as code — not just the technical implementation. Writing a Rego policy is the easy part. Deploying it safely, maintaining it over time, and generating the evidence that auditors require are the skills that differentiate a DevSecOps engineer who can implement a tool from one who can operate a compliance program. Your responses should reflect both technical precision and the judgment to explain these requirements to a compliance officer who does not read YAML.
