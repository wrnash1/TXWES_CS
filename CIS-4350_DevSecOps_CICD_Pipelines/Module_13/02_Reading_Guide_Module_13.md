# Reading Guide: Module 13 — Compliance as Code

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

This reading guide supports Module 13: Compliance as Code. The module covers Open Policy Agent (OPA), the Rego policy language, Kubernetes Gatekeeper as an admission controller, and Conftest for pipeline policy enforcement. By the end of this module you should be able to write Rego policies, deploy Gatekeeper, and integrate compliance checks into CI/CD pipelines with traceability to specific SOC 2 and PCI-DSS controls.

---

### Section 1 — Glossary of Key Terms

**Compliance as Code** — The practice of expressing organizational security and compliance requirements as executable, version-controlled policy code rather than static documents. Policy violations are detected and blocked automatically without human review.

**Open Policy Agent (OPA)** — A CNCF-graduated, general-purpose policy engine that evaluates structured input (JSON) against policies written in Rego and returns a structured decision. OPA is not Kubernetes-specific and can enforce policy across CI/CD, Terraform, API authorization, and Kubernetes admission.

**Rego** — OPA's declarative, logic-based policy language, influenced by Datalog. Rego policies define rules that evaluate conditions against input data and produce output decisions.

**Package** — A Rego namespace declaration (`package k8s.security`) that organizes policies into logical groups. Packages correspond to OPA evaluation paths.

**Rule** — A Rego construct that defines conditions under which a policy fires. Incremental rules like `deny[msg]` build a set — each binding of variables that satisfies the conditions adds an element to the set.

**Incremental rule** — A Rego rule of the form `rule[element]` that builds a set. Used for `deny`, `violation`, and `warn` rules in policy enforcement contexts.

**Input** — The reserved Rego variable that always refers to the document being evaluated. In Kubernetes admission control, `input` is the AdmissionReview request body. In Conftest, `input` is the structured representation of the file being tested.

**Wildcard iterator (`_`)** — A Rego syntax element that matches every element in an array without binding to a named variable. `input.spec.containers[_]` iterates over every container in the pod spec.

**Negation (`not`)** — A Rego keyword that evaluates to true when the expression that follows it is not satisfied. Used to detect missing fields: `not container.securityContext.runAsNonRoot` fires when the field is absent.

**Gatekeeper** — The official Kubernetes admission controller for OPA. It intercepts every Kubernetes API request and evaluates policies against resources before they are admitted to the cluster.

**ConstraintTemplate** — A Gatekeeper custom resource that defines the Rego policy logic and the parameter schema for a policy type. It creates a new custom resource definition (CRD) in the cluster.

**Constraint** — A Gatekeeper custom resource that is an instance of a ConstraintTemplate. It specifies which resource types and namespaces the policy applies to and what `enforcementAction` to take.

**enforcementAction** — A Constraint field that controls how Gatekeeper handles violations. Values: `deny` (block the resource), `warn` (allow but return a warning), `dryrun` (audit only, record in violation status but do not block).

**Admission controller** — A Kubernetes component that intercepts API server requests after authentication and authorization but before persistence. Admission controllers can mutate or validate resources. Gatekeeper is a validating admission webhook.

**Conftest** — A tool that evaluates structured data files (YAML, JSON, HCL, Dockerfile, Terraform plans) against OPA Rego policies at the command line without a Kubernetes cluster. Used for CI/CD pipeline policy gates.

**Policy-as-code lifecycle** — The discipline of managing Rego policies with the same rigor as application code: version control, peer review, automated testing, and staged rollout.

**OPA Playground** — A browser-based tool at `play.openpolicyagent.org` for evaluating Rego policies interactively. Useful for learning and debugging Rego before deployment.

**SOC 2 Trust Services Criteria** — A framework of five categories (Security, Availability, Processing Integrity, Confidentiality, Privacy) with specific criteria codes. Common compliance-as-code targets include CC6.1 (logical access), CC6.6 (network access), CC6.7 (data in transit), and CC7.2 (monitoring).

**PCI-DSS Requirement 6** — PCI-DSS section covering secure systems development. Relevant sub-requirements for DevSecOps: 6.2.4 (prevent common vulnerabilities), 6.3.3 (protect against known vulnerabilities), 6.4.1 (protect public-facing applications).

---

### Section 2 — Core Concepts

#### 2.1 The OPA Evaluation Model

OPA uses a three-component evaluation model:

1. **Input** — the document being evaluated (JSON). In Kubernetes admission, this is the AdmissionReview object. In Conftest, this is the parsed YAML or JSON file.

2. **Policy** — Rego rules that express what is and is not allowed. Policies declare conditions; when conditions are satisfied, rules fire.

3. **Decision** — the output JSON produced by OPA after evaluating the input against the policy. For admission control, the decision is whether to allow or deny the resource.

This model makes OPA context-independent: the same Rego policy can be evaluated by Conftest in a CI pipeline, by Gatekeeper in a Kubernetes cluster, or by an OPA sidecar in a microservice — using the same policy file.

#### 2.2 Rego Rule Types

Rego supports several rule types relevant to policy enforcement:

**Complete rules** — Define a single value: `default allow = false`. If no other rule sets `allow` to `true`, it remains `false`.

**Incremental rules** — Build a set by firing multiple times: `deny[msg]`. Each time the conditions are satisfied for a different binding of variables, a new message is added to the `deny` set. The resource is denied if the `deny` set is non-empty.

**Function rules** — Named functions: `is_latest(image) { endswith(image, ":latest") }`. Reusable logic that other rules can call.

**Default rules** — Provide fallback values: `default allow = true`. If no incremental rule fires, the default applies.

#### 2.3 Rego Syntax Reference

| Construct | Syntax | Purpose |
|---|---|---|
| Package | `package k8s.pci` | Namespace declaration |
| Incremental rule | `deny[msg] { ... }` | Build denial set |
| Input reference | `input.spec.containers[_]` | Access evaluated document |
| Variable binding | `container := input.spec.containers[_]` | Name a value for reuse |
| Wildcard iterator | `[_]` | Match every array element |
| Negation | `not expr` | True when expr unsatisfied |
| String function | `endswith(s, suffix)` | String test |
| Formatted message | `sprintf("text %v", [value])` | Dynamic message |
| Equality check | `x == value` | Comparison |
| Inequality | `x != value` | Not-equal comparison |

#### 2.4 Gatekeeper Architecture

Gatekeeper runs as a Kubernetes Deployment (typically 3 replicas for HA) and registers itself as a ValidatingWebhookConfiguration. The Kubernetes API server sends every create/update request to Gatekeeper before admitting the resource.

The Gatekeeper workflow:

1. Developer or CI/CD pipeline submits a resource manifest via `kubectl apply`
2. Kubernetes API server authenticates and authorizes the request
3. API server calls Gatekeeper's validating webhook with the AdmissionReview object
4. Gatekeeper evaluates the resource against all active Constraints
5. If any Constraint's Rego policy fires a violation, Gatekeeper returns a denial with the violation message
6. If no violations, Gatekeeper allows the resource and the API server persists it to etcd

Gatekeeper also runs an **audit controller** that periodically scans existing resources against all Constraints and records violations in the Constraint's `.status.violations` field. This enables compliance reporting on resources that predate a policy.

#### 2.5 ConstraintTemplate and Constraint Relationship

A ConstraintTemplate is the policy class. It:

- Defines the Rego logic in the `spec.targets[].rego` field
- Declares the parameter schema (CRD spec) that Constraints can pass to the policy
- Creates a new custom resource kind (e.g., `K8sRequireNonRoot`)

A Constraint is a policy instance. It:

- Specifies which resource kinds (`spec.match.kinds`) and namespaces (`spec.match.namespaces`) the policy applies to
- Sets the `enforcementAction` (deny/warn/dryrun)
- Can pass parameters to the ConstraintTemplate's Rego (e.g., allowed registry prefixes)

Multiple Constraints can reference the same ConstraintTemplate with different scopes. For example, one Constraint applies the non-root policy to the `production` namespace with `deny`, and another applies it to `staging` with `warn`.

#### 2.6 The enforcementAction Migration Strategy

The `enforcementAction` field enables a three-phase compliance rollout:

**Phase 1 — dryrun** — Deploy Constraints with `enforcementAction: dryrun`. Violations are recorded in `.status.violations` but resources are not blocked. Use this phase to audit existing resources and quantify the violation backlog.

**Phase 2 — warn** — Switch to `enforcementAction: warn`. New resources that violate the policy receive a warning in the API server response but are still admitted. Developers see warnings in their `kubectl apply` output. Use this phase to notify teams and drive remediation without blocking deployment.

**Phase 3 — deny** — Switch to `enforcementAction: deny`. Non-compliant resources are rejected at admission. Teams must remediate before deploying. Use this phase after the violation backlog is cleared.

This mirrors the PodSecurity admission controller's audit/warn/enforce label progression.

#### 2.7 Conftest and CI/CD Integration

Conftest evaluates the same Rego policies used by Gatekeeper — but at the command line before any Kubernetes cluster is involved. This enables **shift-left compliance**: policy violations caught at pull request time when developers can fix them with immediate feedback.

Key Conftest CLI flags:

| Flag | Purpose |
|---|---|
| `--policy <dir>` | Directory containing Rego policy files |
| `--namespace <pkg>` | Rego package to evaluate (e.g., `k8s.pci`) |
| `--all-namespaces` | Evaluate all packages in all `.rego` files |
| `--output github` | Format failures as GitHub PR annotations |
| `--output json` | Machine-readable JSON output |
| `--combine` | Pass all input files as a single array (for multi-file policies) |

The `--output github` flag is particularly important for GitHub Actions integration: violations appear directly in the pull request diff view as inline annotations on the affected YAML lines.

#### 2.8 Policy Testing with OPA

OPA includes a built-in test framework. Policy tests live in files named `*_test.rego` in the same directory as the policy. Test syntax:

- Test functions are named `test_*`
- The `with input as {...}` construct provides a synthetic input document
- The `deny[...]` set notation asserts that a specific denial message exists
- `not deny with input as {...}` asserts that a specific input should pass

Run all tests: `opa test policies/`

Policy testing is a critical governance requirement: untested policies can contain logic errors that silently allow violations (false negatives) or block valid resources (false positives).

---

### Section 3 — SOC 2 and PCI-DSS Control Mapping

#### 3.1 SOC 2 Trust Services Criteria

| SOC 2 Criteria | Description | Rego Enforcement |
|---|---|---|
| CC6.1 | Logical access controls — restrict access to authorized users only | RBAC constraints; no cluster-admin in app namespaces; require resource limits |
| CC6.6 | Network access — restrict logical access from untrusted networks | Require NetworkPolicy presence; prohibit `hostNetwork: true` |
| CC6.7 | Data in transit — protect data with encryption | Require TLS on service endpoints; prohibit unencrypted connections |
| CC7.2 | Monitoring — deploy and operate security monitoring tools | Require logging sidecars in production namespaces; require Falco DaemonSet |

#### 3.2 PCI-DSS Requirement 6 Mapping

| PCI-DSS Control | Description | Rego Enforcement |
|---|---|---|
| 6.2.4 | Prevent common vulnerabilities in bespoke and custom software | SAST gates in CI; OWASP dependency checks |
| 6.3.3 | Protect software components from known vulnerabilities | Deny `latest` tag (unpinned versions); container scan gates |
| 6.4.1 | Protect public-facing applications | Deny `hostNetwork: true`; deny `privileged: true`; require resource limits |
| 7.2.1 | Least privilege access | Deny `privileged: true`; deny `allowPrivilegeEscalation: true`; drop ALL capabilities |

Embedding compliance control references directly in Rego `deny` messages transforms policy violations into compliance evidence. A denied admission with message `PCI-DSS 6.3.3: Container image myapp:latest uses 'latest' tag` is directly traceable in audit logs.

---

### Section 4 — Policy Lifecycle Governance

#### 4.1 Policy Repository Structure

Organize Rego policies in a dedicated repository (or subdirectory of the application repository):

```text
policies/
  k8s/
    pci.rego
    pci_test.rego
    soc2.rego
    soc2_test.rego
    security_baseline.rego
    security_baseline_test.rego
  terraform/
    aws_baseline.rego
    aws_baseline_test.rego
  CHANGELOG.md
```

Every policy file has a corresponding `_test.rego` file. New policies require passing tests before merging.

#### 4.2 Policy Review Requirements

Policy changes should require review from:

- A security engineer (validates Rego logic correctness and absence of false positives/negatives)
- A compliance officer (validates that the policy accurately implements the compliance control)

Changes to `enforcementAction` from `warn` to `deny` should require an additional review gate confirming the violation backlog is cleared.

#### 4.3 Policy Change Management

| Stage | Action | Stakeholder |
|---|---|---|
| Draft | Write Rego + tests; `opa test` must pass | Security engineer |
| Review | PR review by security + compliance | Both |
| Deploy dryrun | Deploy Constraint with `dryrun` | Platform team |
| Audit | Review `.status.violations` for 2 weeks | Compliance officer |
| Deploy warn | Switch to `warn`; notify affected teams | Platform team |
| Remediate | Teams fix violations | Development teams |
| Deploy deny | Switch to `deny` after backlog cleared | Platform team |

---

### Section 5 — Exam Tips and High-Yield Facts

The DSOE certification exam tests practical understanding of OPA, Rego, and Gatekeeper. Focus on these patterns:

**OPA evaluation model**: Three components — input (JSON), policy (Rego), decision (JSON). OPA does not enforce; it only evaluates. Enforcement is the responsibility of the system calling OPA (Gatekeeper, Conftest, a custom API gateway).

**Rego incremental rules**: `deny[msg]` builds a set. The resource is denied when the set is non-empty. This is different from a boolean `deny = true` rule. Know the difference between incremental and complete rules.

**Wildcard iteration vs. named variable**: `input.spec.containers[_]` is an anonymous iterator. `container := input.spec.containers[_]` binds the iterator to a named variable so you can reference `container.name`, `container.image`, etc. multiple times within the rule.

**Gatekeeper vs. Conftest**: Gatekeeper enforces at the Kubernetes API layer (runtime). Conftest enforces at the CI pipeline layer (pre-deployment). Both use the same Rego policies — this consistency is the key architectural advantage of the compliance-as-code approach.

**enforcementAction values**: Know all three — `deny`, `warn`, `dryrun`. Know when to use each in a migration strategy. Exam questions often test the correct order: dryrun → warn → deny.

**Gatekeeper object types**: Two types — ConstraintTemplate (defines the policy, creates a CRD) and Constraint (applies the policy to specific resources/namespaces). Know which is the class and which is the instance.

**Policy testing**: `opa test policies/` runs all `*_test.rego` files. The `with input as {}` construct is for providing synthetic test input. This is required for DSOE governance questions about policy quality assurance.

**SOC 2 and PCI-DSS mapping**: Know that CC6.1 maps to resource limits and RBAC; CC6.6 maps to NetworkPolicy and hostNetwork prohibition; PCI-DSS 6.3.3 maps to version pinning (deny `:latest`); PCI-DSS 7.2.1 maps to least privilege (`privileged: false`, drop ALL capabilities).

**Common exam distractor**: OPA does not replace Kubernetes RBAC. OPA/Gatekeeper enforces policy on resource content and structure; RBAC enforces who can perform which API operations. They are complementary, not redundant.

---

### Section 6 — Study Checklist

Before attempting the Module 13 quiz, confirm you can do the following without reference materials:

- [ ] Explain the OPA evaluation model (three components: input, policy, decision)
- [ ] Write a Rego `deny[msg]` rule that checks a single condition on a Kubernetes pod spec
- [ ] Explain what `input.spec.containers[_]` does using the term "wildcard iterator"
- [ ] Explain when `not expr` evaluates to true in Rego
- [ ] Describe the difference between ConstraintTemplate and Constraint in Gatekeeper
- [ ] List the three `enforcementAction` values and the correct migration order
- [ ] Explain what Conftest does and how it differs from Gatekeeper
- [ ] Name the Conftest flag that formats output as GitHub PR annotations (`--output github`)
- [ ] Identify the SOC 2 criteria that maps to requiring NetworkPolicy (`CC6.6`)
- [ ] Identify the PCI-DSS control that maps to denying the `:latest` tag (`6.3.3`)
- [ ] Describe the OPA test framework file naming convention (`*_test.rego`) and the command to run tests (`opa test`)
- [ ] Explain why embedding compliance control references in `deny` messages creates compliance evidence

---

### Section 7 — Further Reading

- OPA Documentation: `https://www.openpolicyagent.org/docs/latest/`
- Rego Playground: `https://play.openpolicyagent.org/`
- Gatekeeper Documentation: `https://open-policy-agent.github.io/gatekeeper/`
- Conftest Documentation: `https://www.conftest.dev/`
- OPA Rego Style Guide: `https://github.com/StyraInc/rego-style-guide`
- Gatekeeper Policy Library: `https://github.com/open-policy-agent/gatekeeper-library`
- CNCF Security Whitepaper: Cloud Native Security controls mapping

---

## 9. Supplemental Resources

**1. [Open Policy Agent documentation — Rego language reference](https://www.openpolicyagent.org/docs/latest/policy-language/)**
The official OPA documentation for the Rego policy language, covering rule types (complete, incremental, partial), the `input` document, `with` keyword for test mocking, built-in functions (`contains`, `endswith`, `sprintf`, `count`), and the `not` operator. The definitive reference for writing and debugging Rego policies.

**2. [OPA Gatekeeper policy library](https://github.com/open-policy-agent/gatekeeper-library)**
The community-maintained library of pre-built Gatekeeper ConstraintTemplates and Constraints covering Kubernetes security baselines, PSA equivalence, PCI-DSS controls, and resource governance. Provides working examples of ConstraintTemplate structure, Rego constraint logic, and Constraint resource format that can be used as starting points for custom organizational policies.

**3. [Conftest documentation and examples](https://www.conftest.dev/)**
The official Conftest documentation covering installation, `conftest test` usage, `--policy` and `--all-namespaces` flags, supported input formats (YAML, JSON, HCL, Dockerfile, CUE), `--output github` for PR annotations, and how to share policies using OPA bundles. Includes worked examples for Kubernetes manifest validation, Terraform plan evaluation, and Dockerfile compliance checking.

---

*CIS-4350 DevSecOps and CI/CD Pipelines | Texas Wesleyan University | Professor Nash*
