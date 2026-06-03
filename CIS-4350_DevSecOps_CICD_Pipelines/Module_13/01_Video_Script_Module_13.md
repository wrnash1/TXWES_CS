# Video Script: Module 13 — Compliance as Code

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### SEGMENT 1 — Introduction (0:00–2:00)

Welcome back to CIS-4350. I'm Professor Nash. In previous modules we covered CSPM for cloud posture, Falco for runtime security, and SIEM for event correlation. All of those are about detection. In this module we flip to prevention and enforcement: how do you express your organization's compliance requirements as executable code that automatically rejects policy violations before they ever reach production?

This is the domain of Compliance as Code — using Open Policy Agent, the Rego policy language, and Kubernetes Gatekeeper to make compliance requirements first-class citizens in your software delivery pipeline. Instead of a PDF document that says "all containers must run as non-root," you have a Rego policy that is evaluated at every pull request and every Kubernetes API call, automatically enforcing that requirement with no human review required.

By the end of this module you will understand what OPA is and how it works, how to write Rego policies, how to deploy Gatekeeper as a Kubernetes admission controller, how to implement automated compliance checks for SOC 2 and PCI-DSS controls, and how to manage a policy-as-code lifecycle in a DevSecOps program.

---

### SEGMENT 2 — Open Policy Agent Architecture (2:00–6:00)

Open Policy Agent — OPA — is a CNCF-graduated general-purpose policy engine. It evaluates structured input (JSON) against policies written in Rego, and produces a structured output decision (also JSON). OPA is not Kubernetes-specific. It can enforce policy for CI/CD pipelines, Terraform plans, API authorization, microservice access control, and Kubernetes admission control.

The OPA evaluation model is simple:

1. You have data — the resource being evaluated (a Kubernetes manifest, a Terraform plan, an API request body)
2. You have policy — Rego rules that define what is and is not allowed
3. OPA evaluates the data against the policy and returns a decision

OPA is typically embedded in or called by the system making authorization decisions. For Kubernetes, this is done through Gatekeeper. For Terraform, this can be done through Conftest. For CI/CD pipelines, this can be done through OPA's built-in evaluation CLI or through framework-specific tooling.

Rego is OPA's policy language. It is a declarative, logic-based language influenced by Datalog. Rego policies are composed of rules that define sets of conditions. When all conditions in a rule are true, the rule is satisfied.

Here is a minimal Rego policy that checks whether a Kubernetes Pod runs as non-root:

```rego
package k8s.security

# Deny pods that run as root
deny[msg] {
  input.spec.containers[_].securityContext.runAsNonRoot == false
  msg := "Container must set runAsNonRoot to true"
}

deny[msg] {
  not input.spec.containers[_].securityContext.runAsNonRoot
  msg := "Container must explicitly set runAsNonRoot"
}
```

Let me unpack the Rego syntax. `package k8s.security` declares the policy namespace. `deny[msg]` defines a rule that populates a `deny` set — each element in the set is a denial message. The `{...}` block contains the conditions; if all conditions are true, the rule fires and adds `msg` to the `deny` set. The `input` variable always refers to the document being evaluated — in Kubernetes admission, this is the AdmissionReview request body.

---

### SEGMENT 3 — Rego Language Deep Dive (6:00–10:00)

Rego looks unusual if you are coming from procedural languages like Python or JavaScript. Let me walk through the key concepts.

**Rules and sets.** In Rego, `deny[msg]` defines an incremental rule that builds a set. Every time the rule's conditions are met for some binding of variables, a new element is added to the set. If the `deny` set is non-empty after evaluating all rules, the request is denied.

**Iteration with underscore.** The `_` in `input.spec.containers[_]` is a wildcard iterator — it matches every element of the array. If any container satisfies the condition, the rule fires. This is how you check "any container that runs as root" rather than a specific container.

**Negation with not.** `not expr` is true when `expr` is not satisfied. This is used to detect missing fields — `not input.spec.containers[_].securityContext.runAsNonRoot` fires when `runAsNonRoot` is absent entirely.

Here is a more comprehensive policy for PCI-DSS compliance:

```rego
package k8s.pci

# PCI-DSS 6.3.3: All software components are protected from known vulnerabilities
# Deny images with "latest" tag — requires specific version pinning
deny[msg] {
  container := input.spec.containers[_]
  endswith(container.image, ":latest")
  msg := sprintf("PCI-DSS 6.3.3: Container image %v uses 'latest' tag. Pin to a specific version.", [container.image])
}

# PCI-DSS 7.2.1: Least privilege access — no privileged containers
deny[msg] {
  container := input.spec.containers[_]
  container.securityContext.privileged == true
  msg := sprintf("PCI-DSS 7.2.1: Container %v is privileged. Privileged containers violate least privilege.", [container.name])
}

# PCI-DSS 6.4.1: Protect public-facing applications — deny hostNetwork
deny[msg] {
  input.spec.hostNetwork == true
  msg := "PCI-DSS 6.4.1: hostNetwork: true exposes host network stack. Prohibited in PCI scope."
}

# SOC 2 CC6.1: Logical access controls — require explicit resource limits
deny[msg] {
  container := input.spec.containers[_]
  not container.resources.limits.memory
  msg := sprintf("SOC 2 CC6.1: Container %v has no memory limit. Resource limits are required.", [container.name])
}
```

Each `deny` rule includes a compliance reference in its message — the PCI-DSS control number or SOC 2 criteria reference. This makes every policy violation traceable to a specific compliance requirement, transforming YAML rejections into compliance evidence.

---

### SEGMENT 4 — Kubernetes Gatekeeper (10:00–14:00)

Gatekeeper is the official Kubernetes admission controller for OPA. It runs as a set of pods in your Kubernetes cluster and intercepts every API server request. When a pod, deployment, or other resource is created or updated, the API server calls Gatekeeper before admitting the resource. If Gatekeeper's policies deny the resource, the API server returns an error and the resource is not created.

Gatekeeper introduces two custom resource types:

**ConstraintTemplate** — defines the Rego policy logic and the schema for the constraint parameters.

**Constraint** — an instance of a ConstraintTemplate applied to specific resource types and namespaces, with optional parameter values.

Here is a ConstraintTemplate for requiring non-root containers:

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequirenonroot
spec:
  crd:
    spec:
      names:
        kind: K8sRequireNonRoot
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequirenonroot

        violation[{"msg": msg}] {
          container := input.review.object.spec.containers[_]
          container.securityContext.runAsNonRoot != true
          msg := sprintf("Container %v must set runAsNonRoot: true", [container.name])
        }
```

And the corresponding Constraint that applies this policy to all pods in the production namespace:

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequireNonRoot
metadata:
  name: require-non-root-production
spec:
  match:
    kinds:
      - apiGroups: ["*"]
        kinds: ["Pod"]
    namespaces:
      - production
  enforcementAction: deny
```

The `enforcementAction` can be `deny` (block the resource), `warn` (allow but return a warning), or `dryrun` (audit only, record in violation status). This mirrors the PodSecurity admission controller's enforce/warn/audit labels and enables the same migration strategy: start with `dryrun` to discover violations, switch to `warn` when ready to notify teams, then switch to `deny` for full enforcement.

---

### SEGMENT 5 — Conftest for Pipeline Policy Gates (14:00–17:30)

Gatekeeper enforces policy at the Kubernetes API level. But you want to catch policy violations earlier — at the pull request stage when developers can fix them with immediate feedback. This is where Conftest comes in.

Conftest is a tool that evaluates structured data (YAML, JSON, HCL, Dockerfile, Terraform plans) against OPA Rego policies in the command line — no Kubernetes cluster required. You use the same Rego policies for both Conftest in CI and Gatekeeper in the cluster, creating policy-as-code consistency from code to production.

```bash
# Install conftest
brew install conftest

# Test a Kubernetes manifest
conftest test k8s/deployment.yaml \
  --policy policies/ \
  --namespace k8s.pci

# Output
FAIL - k8s/deployment.yaml - k8s.pci - PCI-DSS 6.3.3: Container image myapp:latest uses 'latest' tag.
FAIL - k8s/deployment.yaml - k8s.pci - SOC 2 CC6.1: Container api has no memory limit.
2 tests, 0 passed, 0 warnings, 2 failures
```

GitHub Actions integration for Conftest:

```yaml
compliance-check:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    - name: Install Conftest
      run: |
        curl -L https://github.com/open-policy-agent/conftest/releases/download/v0.46.0/conftest_0.46.0_Linux_x86_64.tar.gz \
          | tar xzf - conftest
        sudo mv conftest /usr/local/bin/

    - name: Run Compliance Policy Checks
      run: |
        conftest test k8s/ \
          --policy policies/ \
          --output github \
          --namespace k8s.pci \
          --all-namespaces
```

The `--output github` flag formats output as GitHub annotations, making policy failures appear directly in the pull request diff view.

---

### SEGMENT 6 — Policy Lifecycle and Regulatory Frameworks (17:30–20:30)

Compliance as Code is not a one-time setup. Policies must be maintained as a living codebase with the same discipline as application code.

**Policy versioning.** Store your Rego policies in a Git repository. Every policy change goes through pull request review. Policy reviews should include a security engineer and a compliance officer.

**SOC 2 mapping.** SOC 2 Trust Services Criteria map to specific technical controls. Compliance as Code can enforce:

- CC6.1 (Logical access): RBAC constraints, no cluster-admin in application namespaces
- CC6.6 (Network access): Network Policy presence required, hostNetwork prohibited
- CC6.7 (Data in transit): TLS required on service endpoints, no unencrypted connections
- CC7.2 (Monitoring): Logging sidecars required, falco deployed in namespace

**PCI-DSS mapping.** PCI-DSS Requirement 6 (Develop and Maintain Secure Systems) maps directly to DevSecOps pipeline controls:

- 6.2.4: Software development practices prevent common vulnerabilities — SAST + SCA gates
- 6.3.3: Software components protected from known vulnerabilities — container scan gates
- 6.4.1: Public-facing application security — no hostNetwork, no privileged containers

**Policy testing.** Rego policies must be tested. OPA includes a built-in test framework: `opa test policies/`. Tests use the same `package` declarations as policies but in files named `*_test.rego`.

```rego
package k8s.pci_test

import data.k8s.pci

test_deny_latest_tag {
  deny["PCI-DSS 6.3.3"] with input as {
    "spec": {"containers": [{"image": "myapp:latest"}]}
  }
}

test_allow_pinned_tag {
  not deny with input as {
    "spec": {"containers": [{"image": "myapp:1.2.3"}]}
  }
}
```

---

### SEGMENT 7 — Wrap-Up (20:30–22:00)

Compliance as Code transforms your organization's security and compliance requirements from static documents into executable, automatically enforced policies. OPA and Rego provide the policy engine. Conftest brings policy enforcement into your CI/CD pipeline at pull-request time. Gatekeeper enforces those same policies at the Kubernetes API level as a runtime admission controller.

The consistency of using the same Rego policies in both Conftest and Gatekeeper is the key architectural advantage — developers get early feedback in CI, and the cluster enforces the same rules as a final gate. Nothing non-compliant can be deployed.

In the next module we cover Threat Modeling in DevSecOps — using the STRIDE framework and tools like OWASP Threat Dragon to systematically identify threats before you write a line of code.

See you there.

---

### PRODUCTION NOTES

- Screen share: OPA playground at play.openpolicyagent.org with Rego evaluation
- Demo: Conftest scan on a Kubernetes YAML with PCI-DSS policy violations
- Demo: Gatekeeper ConstraintTemplate deployment and admission webhook test
- Slide: OPA evaluation model diagram (input + policy = decision)
- Slide: SOC 2 / PCI-DSS control-to-Rego mapping table
