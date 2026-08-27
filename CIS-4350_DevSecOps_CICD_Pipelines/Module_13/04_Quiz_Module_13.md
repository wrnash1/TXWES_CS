# Quiz: Module 13 — Compliance as Code

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

Instructions: Select the single best answer for each question. Review the distractor analysis after completing the quiz.

---

### Question 1

What is the OPA evaluation model, and what are its three core components?

- A) OPA is a Kubernetes-specific admission controller that evaluates pod manifests against CIS Benchmark rules stored in etcd
- B) OPA is a general-purpose policy engine that evaluates structured input (JSON) against policies written in Rego and returns a structured decision (JSON) — the three components are input, policy, and decision
- C) OPA is a SIEM integration layer that receives security events from Falco and translates them into Kubernetes NetworkPolicy rules
- D) OPA is a code scanning tool that evaluates Python and JavaScript source files against OWASP Top 10 rules and returns a SARIF report

Correct Answer: B — OPA's evaluation model is intentionally simple and general-purpose: any JSON document can be evaluated as input, Rego policies express conditions, and the output is a JSON decision. OPA itself does not enforce — it only evaluates. Enforcement is the responsibility of the system calling OPA (Gatekeeper, Conftest, an API gateway). This is why OPA can be used across Kubernetes, Terraform, CI/CD pipelines, and microservice authorization with the same policy engine.

Distractor Analysis:

- Why A is incorrect: OPA is not Kubernetes-specific — it is a general-purpose policy engine that predates its Kubernetes use. CIS Benchmarks are implemented as policy rules in Rego, not stored in etcd.
- Why C is incorrect: OPA does not receive events or generate NetworkPolicy rules. Event correlation is a SIEM function. OPA is a request-time policy evaluator, not an event-driven system.
- Why D is incorrect: OPA evaluates structured data (JSON/YAML), not source code. Source code scanning is the domain of SAST tools like Semgrep and SonarQube. OPA does not produce SARIF output natively.

---

### Question 2

In Rego, what does the `deny[msg]` rule syntax define, and when is a Kubernetes resource denied?

- A) `deny[msg]` defines a boolean variable that is set to `true` when the first violation is found; the resource is denied when `deny == true`
- B) `deny[msg]` defines an incremental rule that builds a set; the resource is denied when the `deny` set is non-empty after evaluating all rules
- C) `deny[msg]` defines a function that is called by Gatekeeper for each container in the pod spec; the resource is denied when the function returns a non-null string
- D) `deny[msg]` defines a complete rule that short-circuits evaluation after the first match; only the first violation message is returned

Correct Answer: B — In Rego, `deny[msg]` is an incremental rule. Every time the rule's conditions are satisfied for a given binding of variables, a new element (the `msg` string) is added to the `deny` set. If two containers in the same pod each violate a policy, both messages are added. The resource is denied when the `deny` set is non-empty. This is fundamentally different from a boolean `deny = true` complete rule, which cannot return multiple messages.

Distractor Analysis:

- Why A is incorrect: `deny[msg]` is not a boolean variable. It is a set-building incremental rule. `deny == true` is a complete rule pattern — a different construct that cannot return violation messages.
- Why C is incorrect: `deny[msg]` is not a function. In Rego, functions are defined with `f(args) { ... }` syntax. `deny[msg]` is a rule that produces a set. Gatekeeper does not call it as a function — it queries the `deny` set after OPA evaluates all rules.
- Why D is incorrect: Incremental rules do not short-circuit. All bindings of variables that satisfy the conditions are evaluated, and all resulting values are added to the set. Complete rules (`allow = true`) can short-circuit, but incremental rules accumulate all results.

---

### Question 3

What is the purpose of the wildcard operator `_` in the Rego expression `input.spec.containers[_]`?

- A) The `_` operator selects only the first container in the array, providing a safe default when the array might be empty
- B) The `_` operator is a wildcard iterator that matches every element in the array; if any element satisfies the rule's conditions, the rule fires
- C) The `_` operator is a null-safety check that prevents the rule from throwing an error when the `containers` field is missing from the input
- D) The `_` operator filters out containers whose name starts with an underscore, which is the convention for system containers in Kubernetes

Correct Answer: B — In Rego, `[_]` is an anonymous wildcard iterator. It binds to each element of the array in turn. If any binding satisfies all the conditions in the rule body, the rule fires and adds a message to the `deny` set. The rule does not need to specify which container to check — it checks all of them. This is why a single Rego rule can detect a violation in any container in a multi-container pod.

Distractor Analysis:

- Why A is incorrect: `[_]` does not select only the first element — that would be `[0]`. The wildcard iterates over every element.
- Why C is incorrect: `[_]` is not a null-safety operator. If the `containers` field is missing from the input, the expression is simply undefined and the rule does not fire — but that is a property of Rego's evaluation model, not a function of the `_` operator specifically.
- Why D is incorrect: `_` has no relationship to underscores in container names. It is standard Rego syntax for an anonymous variable, equivalent to a throwaway variable in other languages.

---

### Question 4

What is the difference between a Gatekeeper ConstraintTemplate and a Constraint?

- A) A ConstraintTemplate is the running Gatekeeper pod; a Constraint is the configuration file that tells Gatekeeper which namespaces to monitor
- B) A ConstraintTemplate defines the Rego policy logic and creates a new custom resource definition; a Constraint is an instance of that template applied to specific resource types and namespaces with a configured enforcementAction
- C) A ConstraintTemplate is a read-only audit report of policy violations; a Constraint is the active enforcement rule that blocks non-compliant resources
- D) A ConstraintTemplate stores historical policy evaluations in etcd; a Constraint is the live query that Gatekeeper executes against those stored evaluations

Correct Answer: B — ConstraintTemplate and Constraint have a class-instance relationship. The ConstraintTemplate defines the policy logic (Rego) and parameter schema, and creates a new CRD kind in the cluster. The Constraint is an instance of that template — it specifies which resource types (`spec.match.kinds`), namespaces (`spec.match.namespaces`), and `enforcementAction` (deny/warn/dryrun) apply. One ConstraintTemplate can have multiple Constraints with different scopes — for example, `deny` in production and `warn` in staging.

Distractor Analysis:

- Why A is incorrect: A ConstraintTemplate is a Kubernetes custom resource, not a pod. Gatekeeper runs as a Deployment. The ConstraintTemplate is a policy definition, not infrastructure configuration.
- Why C is incorrect: Audit reports are part of the Constraint's `.status.violations` field — populated by Gatekeeper's audit controller. ConstraintTemplates define logic; they do not contain reports.
- Why D is incorrect: Gatekeeper does not store historical evaluations in etcd. Each API request triggers a fresh evaluation. The `.status.violations` field records current violations, not historical evaluations.

---

### Question 5

A Gatekeeper Constraint is deployed with `enforcementAction: dryrun`. A developer submits a Deployment with a privileged container. What happens?

- A) The Deployment is blocked and the developer receives an error: `admission webhook denied the request`
- B) The Deployment is admitted, a warning is returned in the kubectl output, and the violation is recorded in the cluster audit log
- C) The Deployment is admitted, no warning is returned to the developer, but the violation is recorded in the Constraint's `.status.violations` field
- D) The Deployment is admitted and silently allowed with no record of the violation anywhere in the cluster

Correct Answer: C — `dryrun` is the audit-only enforcement action. Resources that violate the policy are admitted — no blocking, no warning to the developer. The violation is recorded in the Constraint's `.status.violations` field, which can be queried with `kubectl describe constraint <name>`. This mode is used to audit existing resources and quantify the violation backlog before moving to `warn` or `deny`. It is the correct first phase of a policy rollout.

Distractor Analysis:

- Why A is incorrect: `deny` is the enforcement action that blocks resources and returns an admission webhook error. `dryrun` does not block.
- Why B is incorrect: `warn` is the enforcement action that admits the resource and returns a warning in the kubectl output. `dryrun` does not surface a warning to the developer — it only records in `.status.violations`.
- Why D is incorrect: `dryrun` does record violations — in the Constraint's `.status.violations` field. It is not silent. The distinction from `warn` is that the violation is recorded cluster-side only, with no signal to the developer at deployment time.

---

### Question 6

What is the key architectural advantage of using Conftest in a CI/CD pipeline alongside Gatekeeper in a Kubernetes cluster?

- A) Conftest replaces Gatekeeper in environments that cannot run Kubernetes, providing an equivalent admission controller for Docker Compose deployments
- B) Conftest evaluates the same Rego policies as Gatekeeper but at the pull request stage — developers get early feedback in CI while Gatekeeper enforces the same rules as a final gate at the cluster level, ensuring nothing non-compliant can be deployed
- C) Conftest provides a graphical policy editor that generates Rego code automatically, reducing the need for security engineers to write policy logic manually
- D) Conftest integrates with OPA's cloud service to download pre-built compliance policy packs for SOC 2 and PCI-DSS, eliminating the need to write custom policies

Correct Answer: B — The key advantage is policy consistency across the pipeline. Conftest and Gatekeeper both evaluate the same Rego policy files from the same Git repository. Developers who fix a Conftest failure in their PR know the same fix will satisfy Gatekeeper in the cluster. There is no policy drift between the CI gate and the runtime gate. This shift-left approach gives immediate developer feedback while maintaining a cluster-level safety net.

Distractor Analysis:

- Why A is incorrect: Conftest does not replace Gatekeeper — it is a complementary tool for a different layer of the pipeline. Conftest runs at CI time before any cluster is involved. It cannot function as an admission controller.
- Why C is incorrect: Conftest does not include a graphical policy editor. It is a CLI tool. Rego policies must be written by engineers. The OPA Playground provides interactive Rego evaluation but is not a code generator.
- Why D is incorrect: Conftest does not connect to a cloud service for policy downloads. Policies are loaded from a local directory specified with `--policy`. The Gatekeeper Policy Library on GitHub provides community policies, but they must be downloaded and reviewed manually.

---

### Question 7

A Rego policy contains this rule:

```rego
deny[msg] {
  container := input.spec.containers[_]
  not container.securityContext.runAsNonRoot
  msg := sprintf("Container %v must set runAsNonRoot: true", [container.name])
}
```

What specific case does this rule detect that `container.securityContext.runAsNonRoot != true` would NOT detect?

- A) Containers where `runAsNonRoot` is explicitly set to `false`
- B) Containers where the `securityContext.runAsNonRoot` field is entirely absent from the manifest
- C) Containers where `runAsNonRoot` is set to a string value instead of a boolean
- D) Containers where the `securityContext` field itself is missing from the container spec

Correct Answer: B — In Rego, `x != true` is only satisfied when `x` exists and has a value that is not `true`. If `runAsNonRoot` is absent from the securityContext entirely, `x != true` is undefined — and an undefined condition does not fire. `not container.securityContext.runAsNonRoot` fires when the field is absent (undefined) because `not undefined` evaluates to `true` in Rego. The two rules together cover both cases: explicitly `false` and completely absent.

Distractor Analysis:

- Why A is incorrect: `container.securityContext.runAsNonRoot != true` already handles the case where `runAsNonRoot` is explicitly `false`. Both `false != true` is `true` (so the rule fires), and `not false` is also `true`. For explicit `false`, both rules would fire.
- Why C is incorrect: If `runAsNonRoot` is set to a string, `string != true` is true (strings are not booleans), so the `!= true` rule would fire. Both rules handle type mismatches.
- Why D is incorrect: If `securityContext` itself is absent, both `container.securityContext.runAsNonRoot != true` and `not container.securityContext.runAsNonRoot` would handle the absence — but only through undefined propagation. The key distinction is about the `runAsNonRoot` field within an existing `securityContext`.

---

### Question 8

Which SOC 2 Trust Services Criteria is most directly addressed by a Rego policy that denies containers without explicit memory and CPU resource limits?

- A) CC7.2 — System monitoring: require logging sidecars in all production namespaces
- B) CC6.6 — Network access: restrict logical access from networks outside the organization
- C) CC6.1 — Logical access: use logical access security measures to protect against threats from sources outside the system boundaries
- D) CC6.7 — Data in transit: use encryption to protect data transmitted over public networks

Correct Answer: C — SOC 2 CC6.1 covers logical access controls and resource constraints. Requiring memory and CPU limits is a logical access control in the resource consumption domain: it prevents a misbehaving or compromised container from consuming unbounded cluster resources, which could deny service to other applications. The compliance mapping rationale is that CC6.1 requires the system to protect itself from unauthorized resource consumption, and resource limits implement that protection.

Distractor Analysis:

- Why A is incorrect: CC7.2 covers security monitoring — requiring Falco, logging agents, and audit logging. Resource limits are not monitoring controls.
- Why B is incorrect: CC6.6 covers network access controls — requiring NetworkPolicy presence and prohibiting `hostNetwork`. Resource limits do not control network access.
- Why D is incorrect: CC6.7 covers encryption of data in transit — requiring TLS on service endpoints. Resource limits are not encryption controls.

---

### Question 9

A security engineer wants to write a Rego policy test that verifies a compliant manifest passes without violations. Which test structure is correct?

- A) `test_allow_compliant { deny[_] with input as { "spec": { "containers": [{"image": "app:1.0"}] } } }`
- B) `test_allow_compliant { count(deny) == 0 with input as { "spec": { "containers": [{"image": "app:1.0", "securityContext": {"runAsNonRoot": true}}] } } }`
- C) `test_allow_compliant { not deny with input as { "spec": { "containers": [{"image": "app:1.0"}] } } }`
- D) `test_allow_compliant { deny == false with input as { "spec": { "containers": [{"image": "app:1.0"}] } } }`

Correct Answer: B — `count(deny) == 0` asserts that the `deny` set contains zero elements after evaluating the input. This is the correct way to assert that a compliant input produces no violations. Using `count` makes the assertion explicit and readable. The `with input as {...}` construct provides the synthetic test input.

Distractor Analysis:

- Why A is incorrect: `deny[_]` asserts that the `deny` set is non-empty (at least one element exists). This is the opposite of what a "compliant manifest should pass" test should assert — it would fail if the manifest is compliant.
- Why C is incorrect: `not deny` in Rego means "the `deny` set is empty or undefined." While this is technically equivalent to `count(deny) == 0`, the `not deny` form is less explicit and can be confusing because it reads as "deny is false." The `count(deny) == 0` form is the recommended style for clarity.
- Why D is incorrect: `deny == false` would attempt to compare a set to a boolean `false`. `deny` is a set, not a boolean. This comparison would never be true and the test would fail regardless of input.

---

### Question 11

A Rego policy uses the rule `deny[msg] { container := input.spec.containers[_]; not container.securityContext; msg := "Container must have a securityContext" }`. A manifest has a container with `securityContext: {}` (an empty object). Does this rule fire?

- A) Yes — `not container.securityContext` is true when `securityContext` is an empty object because empty objects are falsy in Rego
- B) No — `not container.securityContext` is false when `securityContext` is present as a key, even if the value is an empty object `{}`
- C) Yes — `not container.securityContext` only fires when the key is absent; since the key is present, it evaluates to true
- D) The rule causes an OPA evaluation error because it cannot evaluate `not` on an object

Correct Answer: B — In Rego, `not expr` is true only when `expr` is undefined or false. An empty object `{}` is a defined value and evaluates as truthy — it is not undefined. Therefore `not container.securityContext` is false when the key exists with an empty object value. The rule would only fire if the `securityContext` key is entirely absent from the container spec.

Distractor Analysis:

- Why A is incorrect: Rego does not have the concept of "falsy" empty objects as JavaScript does. In Rego, any defined value — including `{}`, `[]`, `0`, `""` — is truthy. Undefinedness is the only condition that makes `not` evaluate to true.
- Why C is incorrect: This answer contradicts itself. The correct behavior is that when the key is present, `not container.securityContext` is false — not true. The key's presence makes the expression defined and therefore truthy.
- Why D is incorrect: OPA evaluates `not` on object-valued expressions without error. `not obj` is simply false when `obj` is a defined non-null value. No evaluation error occurs.

---

### Question 12

A ConstraintTemplate named `K8sRequireLabels` has been deployed to a cluster. A developer creates a Constraint resource with `enforcementAction: warn` that requires a `team` label on all Deployments. A new Deployment is submitted without the `team` label. What is the admission outcome?

- A) The Deployment is rejected with an admission error listing the missing label
- B) The Deployment is admitted and a warning is returned to the `kubectl apply` caller indicating the label is missing
- C) The Deployment is admitted silently — warnings are only recorded in the audit log
- D) The Constraint is ignored because `enforcementAction: warn` requires OPA Gatekeeper v3.9 or later

Correct Answer: B — `enforcementAction: warn` causes Gatekeeper to admit the resource but return a warning message to the submitter. The warning appears in the output of `kubectl apply` (or equivalent tooling). Unlike `deny`, the resource is not rejected — it is created despite the policy violation. Warnings are also recorded in the audit log.

Distractor Analysis:

- Why A is incorrect: Rejection only occurs with `enforcementAction: deny`. With `warn`, the admission webhook returns a non-blocking warning that allows the resource to be created.
- Why C is incorrect: In Kubernetes admission webhook responses, warnings are returned to the caller (the kubectl client or CI tool), not silently to the audit log only. The submitter sees the warning in their terminal output.
- Why D is incorrect: `enforcementAction: warn` has been available in OPA Gatekeeper since version 3.4. Version constraints are not a factor for any Gatekeeper release in current use.

---

### Question 13

A security engineer wants to write a Rego policy that requires every container in a Kubernetes pod to have both `memory` and `cpu` limits defined. Which Rego expression correctly checks that a CPU limit is missing?

- A) `container.resources.limits.cpu == null`
- B) `not container.resources.limits.cpu`
- C) `container.resources.limits.cpu != ""`
- D) `container.resources.limits.cpu == false`

Correct Answer: B — In Rego, `not container.resources.limits.cpu` evaluates to true when the `cpu` field is undefined — which happens when the field is absent from the manifest. Missing resource limits appear as absent keys in the JSON input document, not as `null` or `false`. The `not` operator tests for undefinedness, which is the correct test for absent optional fields.

Distractor Analysis:

- Why A is incorrect: `cpu == null` would only match if the field is explicitly set to the JSON `null` value. An absent field is not the same as a `null` field in Rego — absent fields are undefined, not null. This comparison would not fire when the limit is simply not specified.
- Why C is incorrect: `cpu != ""` tests whether the cpu value is not an empty string. A missing field is undefined, not an empty string. This expression would cause an OPA evaluation to produce no result (undefined) rather than true.
- Why D is incorrect: `cpu == false` tests whether the cpu value is the boolean false. Resource limit values are strings (like `"500m"`) or absent. Comparing to boolean false will never match a real manifest.

---

### Question 14

Which of the following best describes the difference between OPA Gatekeeper and Conftest in a DevSecOps pipeline?

- A) Gatekeeper uses Rego; Conftest uses YAML configuration files — they enforce the same policies in different syntax
- B) Gatekeeper enforces policy at the Kubernetes admission layer (runtime), blocking non-compliant resources from being created; Conftest enforces the same Rego policies in CI pipelines (pre-deployment), blocking non-compliant manifests before they reach the cluster
- C) Gatekeeper is only for Kubernetes resources; Conftest can only test Terraform and Dockerfile configurations
- D) Conftest is the open-source version of Gatekeeper — they are the same tool with different licensing

Correct Answer: B — Gatekeeper and Conftest use the same Rego policy language, which is the key architectural advantage. Gatekeeper runs as a Kubernetes admission webhook and enforces at the API server level when resources are submitted to the cluster. Conftest runs in CI pipelines as a command-line tool and evaluates manifests before deployment. The same Rego file can be used in both contexts, providing consistent enforcement across development and runtime.

Distractor Analysis:

- Why A is incorrect: Both Gatekeeper and Conftest use Rego for policy definitions. They are not differentiated by policy language syntax.
- Why C is incorrect: Conftest is not limited to Terraform and Dockerfiles — it evaluates any structured data format (YAML, JSON, HCL, Dockerfile, etc.) against Rego policies. It is commonly used for Kubernetes manifests.
- Why D is incorrect: Gatekeeper and Conftest are distinct tools with different purposes and different maintainers. Conftest is maintained by the Conftest project (originally Thoughtworks); Gatekeeper is maintained by the OPA project under CNCF. Neither is a "version" of the other.

---

### Question 15

A Gatekeeper `dryrun` Constraint has been deployed to a production cluster with a policy requiring all pods to have resource limits. After one week, the team inspects the `.status.violations` field of the Constraint object. What does this field contain?

- A) A list of all resources that were admitted despite violating the policy — because `dryrun` does not block admission, all violations since deployment are recorded here
- B) An empty list — `dryrun` mode does not record any violations; it only prevents false positives
- C) A list of only the most recent violation, because the violations field is overwritten on each evaluation cycle
- D) A count of violations by resource type, not the specific violating resources

Correct Answer: A — In Gatekeeper `dryrun` mode, non-compliant resources are admitted without rejection, but the admission controller records all violations in the `.status.violations` field of the Constraint object. This allows teams to audit the backlog of non-compliant existing resources before switching to `warn` or `deny`. The violations list includes the namespace, name, and kind of each violating resource.

Distractor Analysis:

- Why B is incorrect: `dryrun` mode specifically exists to surface violations without blocking admission. Recording violations is its primary value. An empty violations list would make `dryrun` useless as a migration assessment tool.
- Why C is incorrect: Gatekeeper accumulates violations in `.status.violations` across evaluation cycles, not just the most recent. The list reflects all currently non-compliant resources in the cluster, up to the configured violation limit.
- Why D is incorrect: The `.status.violations` field contains an array of violation objects, each with `kind`, `name`, `namespace`, and `message`. It provides specific resource identities, not aggregated counts.

---

### Question 16

A Rego policy contains the following rule:

```rego
deny[msg] {
  input.spec.hostNetwork == true
  msg := "SOC 2 CC6.6: hostNetwork must be false"
}
```

A manifest has `spec.hostNetwork: false`. Does this rule fire?

- A) Yes — the rule fires for all pods because the `hostNetwork` field is present
- B) No — `input.spec.hostNetwork == true` is false when the value is `false`, so the rule body does not evaluate to true and no denial is produced
- C) Yes — Rego treats `false` values as undefined, so the rule fires when the field exists with any value
- D) The rule causes an error because a Rego rule cannot compare boolean values with `==`

Correct Answer: B — In Rego, a rule body is a conjunction of conditions. All conditions must be true for the rule to produce a result. `input.spec.hostNetwork == true` evaluates to `false` when `hostNetwork` is `false`. Since this condition is false, the rule body fails to evaluate and no denial message is added to the `deny` set. The pod is admitted without a violation.

Distractor Analysis:

- Why A is incorrect: The rule only fires when `input.spec.hostNetwork == true`. The presence of the `hostNetwork` field alone is not sufficient — the value must equal `true`.
- Why C is incorrect: Rego does not treat `false` values as undefined. The boolean value `false` is a defined value that evaluates as false in a boolean context. Undefinedness in Rego is when a key is absent entirely, not when it has the value `false`.
- Why D is incorrect: Rego fully supports equality comparisons (`==`) on boolean values. Boolean comparison is a standard operation in Rego policy conditions.

---

### Question 17

A team has written Rego policies and corresponding `_test.rego` files. Running `opa test policies/` reports `FAIL: 1/5`. What is the correct next step?

- A) Delete the failing test — a failing test indicates the test was written incorrectly and should be removed
- B) Run `opa eval --data policies/ --input <test-input.json> "data.k8s.pci.deny"` to inspect what the `deny` set actually contains for the failing test's input, then fix either the policy logic or the test assertion based on findings
- C) Add `soft_fail: true` to the Conftest command to allow the pipeline to continue despite the failing test
- D) Switch from `opa test` to running Conftest directly — Conftest does not report test failures

Correct Answer: B — The `opa eval` command with explicit input and a query against the policy's `deny` set reveals what the policy actually produces for a given input. This allows the engineer to determine whether the policy has a logic error (producing the wrong output) or the test has an incorrect assertion (expecting the wrong output). Fix the root cause — either policy or test — based on what `opa eval` reveals.

Distractor Analysis:

- Why A is incorrect: Deleting a failing test removes a quality assurance signal. A failing test means there is a discrepancy between the policy's actual behavior and the expected behavior. The correct response is to investigate and resolve the discrepancy, not suppress it.
- Why C is incorrect: `soft_fail` is a Checkov flag, not an OPA or Conftest flag. More importantly, `opa test` runs unit tests of the Rego logic — bypassing a failing unit test would mean deploying a policy with unverified or incorrect behavior.
- Why D is incorrect: Conftest evaluates structured input files against Rego policies; it does not run Rego unit test files (`_test.rego`). The `opa test` command is the correct tool for running Rego unit tests.

---

### Question 18

A SOC 2 audit requires evidence that the organization's Kubernetes admission controls are enforced and that violations are logged with traceability to specific compliance criteria. How does embedding the compliance reference in the Rego `deny` message satisfy this requirement?

- A) It does not satisfy the requirement — Rego deny messages are only visible to engineers running `kubectl apply` and are not stored in any audit trail
- B) The deny message text is included in the Kubernetes audit log entry for the rejected admission request and in the Gatekeeper audit violation list, providing a searchable, attributable record linking the specific resource to the specific compliance control
- C) It satisfies the requirement only if the Gatekeeper audit log is exported to a SIEM — without SIEM integration, the evidence is not admissible
- D) The compliance reference in the message is cosmetic — SOC 2 auditors require separate documentation; the Rego message content has no evidentiary value

Correct Answer: B — When Gatekeeper rejects an admission request, the denial message is recorded in the Kubernetes API server audit log as part of the admission webhook response. The `.status.violations` field of the Constraint object also records violations with the full message text. Embedding the SOC 2 criteria ID (e.g., `CC6.6`) in the message makes these log entries directly traceable to the compliance control during an audit, without requiring separate manual documentation.

Distractor Analysis:

- Why A is incorrect: Kubernetes admission webhook responses — including denial messages — are captured in the API server audit log when audit logging is enabled. Gatekeeper also maintains its own violation records. The messages are not ephemeral.
- Why C is incorrect: SIEM integration enhances searchability and alerting but is not a prerequisite for the audit log evidence to be valid. The Kubernetes audit log and Gatekeeper violation records are themselves evidence-grade records for a SOC 2 audit.
- Why D is incorrect: SOC 2 auditors do accept system-generated logs as evidence of control operation. A Kubernetes audit log entry showing a rejected admission with a message referencing `SOC 2 CC6.6` directly demonstrates that the control is operational and enforced. This is stronger evidence than static documentation.

---

### Question 19

A developer wants to test a Rego policy locally before committing it. They run `conftest test deployment.yaml --policy policies/` and receive the output `PASS - deployment.yaml - data.k8s.pci - No failures`. The same manifest is later rejected by Gatekeeper in the staging cluster. What is the most likely explanation for the discrepancy?

- A) Conftest and Gatekeeper use different versions of the Rego language and the policy evaluates differently in each runtime
- B) The Conftest policy bundle in `policies/` is out of date and does not include the policy that Gatekeeper is enforcing in the cluster
- C) Conftest evaluated a cached version of the manifest — the actual submitted manifest has different field values
- D) `conftest test` only checks the `data.main` package by default and does not evaluate packages namespaced under `data.k8s.pci` unless the `--all-namespaces` flag is used, causing Conftest to miss violations that Gatekeeper's deployed policy catches

Correct Answer: D — Conftest evaluates the `main` package by default. Rego policies in namespaced packages (like `package k8s.pci`) are not evaluated unless `--all-namespaces` is passed or the package is explicitly referenced. If the developer ran Conftest without `--all-namespaces`, it would report no failures because it did not evaluate the PCI policy at all — not because the manifest is compliant.

Distractor Analysis:

- Why A is incorrect: Both Conftest and Gatekeeper use the same OPA Rego evaluation engine. There are no language version differences between them when using the same policy source.
- Why B is incorrect: This is a plausible scenario, but it describes a policy version mismatch rather than the more common mistake of missing the `--all-namespaces` flag. The question's phrasing points to a configuration oversight rather than a drift scenario.
- Why C is incorrect: Conftest reads the manifest file directly from disk — it does not cache manifest content. If the file contents differ between the local test and the cluster submission, that is a source control issue, not a Conftest caching issue.

---

### Question 20

A Rego policy file contains `package k8s.security_baseline`. A test file for this policy begins with `package k8s.security_baseline_test`. The test file references `security_baseline.deny`. When running `opa test policies/`, the test fails with `undefined`. What is missing?

- A) The test file must be in a separate directory from the policy file
- B) The test file is missing `import data.k8s.security_baseline` — without this import, the reference to `security_baseline.deny` is undefined
- C) The policy file must be named `security_baseline_test.rego` for OPA to automatically discover the test file
- D) `opa test` requires the `--bundle` flag to load multiple Rego files together

Correct Answer: B — In Rego test files, policies from other packages must be explicitly imported using `import data.<package.path>`. Without `import data.k8s.security_baseline`, the reference `security_baseline.deny` is an undefined identifier because the test file has no declaration that brings the policy's package into scope.

Distractor Analysis:

- Why A is incorrect: OPA test files can be in the same directory as the policy files they test. OPA discovers all `*_test.rego` files under the specified directory regardless of subdirectory organization.
- Why C is incorrect: OPA discovers test files by the `_test` suffix in the package name, not by the filename convention. The filename does not need to match the package path for test discovery.
- Why D is incorrect: `opa test policies/` loads all Rego files in the `policies/` directory without requiring the `--bundle` flag. The `--bundle` flag is used when policies are packaged as OPA bundles (tar archives), not for simple directory evaluation.

---

Quiz — Module 13 | CIS-4350 | Texas Wesleyan University | Professor Nash

---

### Question 10

A DevSecOps team wants to add a Rego policy that enforces PCI-DSS 6.3.3 by requiring container images to be pinned to a specific digest rather than a mutable tag. Which Rego rule correctly implements this requirement?

- A) `deny[msg] { container := input.spec.containers[_]; contains(container.image, ":"); msg := "Image must use digest pinning" }`
- B) `deny[msg] { container := input.spec.containers[_]; not contains(container.image, "@sha256:"); msg := sprintf("PCI-DSS 6.3.3: Container %v must be pinned to a digest (e.g., image:tag@sha256:...)", [container.name]) }`
- C) `deny[msg] { container := input.spec.containers[_]; container.image == "latest"; msg := "Image must not be latest" }`
- D) `deny[msg] { container := input.spec.containers[_]; not container.image; msg := "Container must have an image field" }`

Correct Answer: B — Digest pinning requires the image reference to include a `@sha256:` content-addressable digest. A tag alone (`:1.2.3`) is mutable — the registry can push a different image to the same tag. Only a digest reference is immutable. `not contains(container.image, "@sha256:")` fires when the digest is absent, which covers images with no tag, a mutable tag, or even a version tag without a digest. The message includes the compliance reference and a concrete example of the required format.

Distractor Analysis:

- Why A is incorrect: `contains(container.image, ":")` would fire on all images that have any colon — including properly tagged images like `app:1.2.3`. A colon is present in any image with a tag or port, so this rule would incorrectly deny all tagged images.
- Why C is incorrect: `container.image == "latest"` only matches images where the full image string is exactly the string "latest" — not `app:latest`. The correct check for the latest tag is `endswith(container.image, ":latest")`. But even that only catches one specific mutable tag — digest pinning is a stronger requirement.
- Why D is incorrect: `not container.image` fires when the image field is missing entirely. A missing image field is a different (and arguably more serious) misconfiguration than a missing digest. This rule does not address the PCI-DSS 6.3.3 requirement for version pinning.
