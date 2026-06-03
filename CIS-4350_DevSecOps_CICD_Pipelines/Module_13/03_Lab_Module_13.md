# Lab Activity: Module 13 — Compliance as Code with OPA and Conftest

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 90–120 minutes

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

In this lab you will write OPA Rego policies that enforce PCI-DSS and SOC 2 compliance controls, test those policies using the OPA test framework, and integrate them into a simulated CI/CD pipeline using Conftest. You will evaluate intentionally non-compliant Kubernetes manifests against your policies, observe violations, remediate the manifests, and confirm clean policy evaluations.

---

### Learning Objectives

By completing this lab you will be able to:

- Write Rego `deny[msg]` rules that check Kubernetes pod spec fields
- Use the OPA CLI to evaluate policies interactively
- Run the OPA test framework to validate policy logic
- Use Conftest to evaluate Kubernetes YAML manifests against policies
- Interpret Conftest output and trace violations to compliance controls
- Remediate non-compliant manifests and confirm resolution

---

### Prerequisites

- Docker Desktop installed and running (for OPA container)
- OR OPA binary installed locally (`brew install opa` on macOS, or download from GitHub releases)
- Conftest installed (`brew install conftest` on macOS, or download from GitHub releases)
- A text editor
- Basic familiarity with Kubernetes YAML structure (Deployments, Pods, securityContext)

#### Verify tool availability

```bash
opa version
conftest --version
```

Expected output examples:

```text
OPA 0.58.0 (commit ..., built ...)
Version: 0.46.0
```

---

### Lab Structure

This lab has four parts:

- Part 1: Write and test Rego policies using the OPA CLI
- Part 2: Write OPA policy unit tests
- Part 3: Evaluate non-compliant Kubernetes manifests with Conftest
- Part 4: Remediate and re-evaluate

---

### Part 1 — Write and Test Rego Policies

#### Step 1.1 — Create the policy directory structure

```bash
mkdir -p compliance-lab/policies
mkdir -p compliance-lab/manifests
cd compliance-lab
```

#### Step 1.2 — Write the PCI-DSS Rego policy

Create `policies/k8s_pci.rego` with the following content:

```rego
package k8s.pci

# PCI-DSS 6.3.3: Deny images with latest tag — requires version pinning
deny[msg] {
  container := input.spec.containers[_]
  endswith(container.image, ":latest")
  msg := sprintf("PCI-DSS 6.3.3: Container image %v uses ':latest' tag. Pin to a specific version.", [container.image])
}

# PCI-DSS 7.2.1: Deny privileged containers — least privilege violation
deny[msg] {
  container := input.spec.containers[_]
  container.securityContext.privileged == true
  msg := sprintf("PCI-DSS 7.2.1: Container %v is privileged. Privileged containers violate least privilege.", [container.name])
}

# PCI-DSS 6.4.1: Deny hostNetwork — exposes host network stack
deny[msg] {
  input.spec.hostNetwork == true
  msg := "PCI-DSS 6.4.1: hostNetwork: true exposes the host network stack. Prohibited in PCI scope."
}

# PCI-DSS 7.2.1: Deny allowPrivilegeEscalation
deny[msg] {
  container := input.spec.containers[_]
  container.securityContext.allowPrivilegeEscalation == true
  msg := sprintf("PCI-DSS 7.2.1: Container %v sets allowPrivilegeEscalation: true. Set to false.", [container.name])
}
```

#### Step 1.3 — Write the SOC 2 Rego policy

Create `policies/k8s_soc2.rego` with the following content:

```rego
package k8s.soc2

# SOC 2 CC6.1: Require memory limits — resource constraint is a logical access control
deny[msg] {
  container := input.spec.containers[_]
  not container.resources.limits.memory
  msg := sprintf("SOC 2 CC6.1: Container %v has no memory limit. Resource limits are required.", [container.name])
}

# SOC 2 CC6.1: Require CPU limits
deny[msg] {
  container := input.spec.containers[_]
  not container.resources.limits.cpu
  msg := sprintf("SOC 2 CC6.1: Container %v has no CPU limit. Resource limits are required.", [container.name])
}

# SOC 2 CC6.6: Prohibit hostNetwork — network access controls
deny[msg] {
  input.spec.hostNetwork == true
  msg := "SOC 2 CC6.6: hostNetwork: true violates network access controls. Prohibited."
}

# SOC 2 CC6.1: Require runAsNonRoot
deny[msg] {
  container := input.spec.containers[_]
  container.securityContext.runAsNonRoot != true
  msg := sprintf("SOC 2 CC6.1: Container %v must set runAsNonRoot: true.", [container.name])
}

# SOC 2 CC6.1: Require runAsNonRoot when field is absent
deny[msg] {
  container := input.spec.containers[_]
  not container.securityContext.runAsNonRoot
  msg := sprintf("SOC 2 CC6.1: Container %v must explicitly set runAsNonRoot: true.", [container.name])
}
```

#### Step 1.4 — Test a policy interactively with the OPA CLI

Create a test input file `manifests/test_input.json`:

```json
{
  "spec": {
    "containers": [
      {
        "name": "api",
        "image": "myapp:latest",
        "securityContext": {
          "privileged": false,
          "runAsNonRoot": false,
          "allowPrivilegeEscalation": true
        },
        "resources": {
          "limits": {}
        }
      }
    ],
    "hostNetwork": false
  }
}
```

Evaluate the PCI policy against this input:

```bash
opa eval \
  --data policies/k8s_pci.rego \
  --input manifests/test_input.json \
  "data.k8s.pci.deny"
```

Expected output — you should see denial messages for the latest tag and allowPrivilegeEscalation violations:

```json
{
  "result": [
    {
      "expressions": [
        {
          "value": [
            "PCI-DSS 6.3.3: Container image myapp:latest uses ':latest' tag. Pin to a specific version.",
            "PCI-DSS 7.2.1: Container api sets allowPrivilegeEscalation: true. Set to false."
          ],
          ...
        }
      ]
    }
  ]
}
```

#### Step 1.5 — Evaluate the SOC 2 policy

```bash
opa eval \
  --data policies/k8s_soc2.rego \
  --input manifests/test_input.json \
  "data.k8s.soc2.deny"
```

Record all denial messages in your lab report.

---

### Part 2 — Write OPA Policy Unit Tests

#### Step 2.1 — Create the PCI test file

Create `policies/k8s_pci_test.rego`:

```rego
package k8s.pci_test

import data.k8s.pci

# Test: latest tag should be denied
test_deny_latest_tag {
  count(pci.deny) > 0 with input as {
    "spec": {
      "containers": [{"name": "api", "image": "myapp:latest", "securityContext": {}}]
    }
  }
}

# Test: pinned tag should pass the version check
test_allow_pinned_tag {
  violations := pci.deny with input as {
    "spec": {
      "containers": [{"name": "api", "image": "myapp:1.2.3", "securityContext": {}}]
    }
  }
  not violations["PCI-DSS 6.3.3: Container image myapp:1.2.3 uses ':latest' tag. Pin to a specific version."]
}

# Test: privileged container should be denied
test_deny_privileged {
  count(pci.deny) > 0 with input as {
    "spec": {
      "containers": [{
        "name": "api",
        "image": "myapp:1.0.0",
        "securityContext": {"privileged": true}
      }]
    }
  }
}

# Test: hostNetwork true should be denied
test_deny_host_network {
  count(pci.deny) > 0 with input as {
    "spec": {
      "containers": [{"name": "api", "image": "myapp:1.0.0", "securityContext": {}}],
      "hostNetwork": true
    }
  }
}
```

#### Step 2.2 — Run the tests

```bash
opa test policies/ -v
```

Expected output:

```text
data.k8s.pci_test.test_deny_latest_tag: PASS (...)
data.k8s.pci_test.test_allow_pinned_tag: PASS (...)
data.k8s.pci_test.test_deny_privileged: PASS (...)
data.k8s.pci_test.test_deny_host_network: PASS (...)
--------------------------------------------------------------------------------
PASS: 4/4
```

If any test fails, debug the Rego logic before proceeding. A failing test means either the policy has a logic error or the test has an incorrect assertion.

---

### Part 3 — Evaluate Non-Compliant Kubernetes Manifests with Conftest

#### Step 3.1 — Create the non-compliant Deployment manifest

Create `manifests/deployment_noncompliant.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service
  namespace: production
spec:
  replicas: 2
  selector:
    matchLabels:
      app: payment-service
  template:
    metadata:
      labels:
        app: payment-service
    spec:
      hostNetwork: true
      containers:
        - name: payment-api
          image: payment-api:latest
          securityContext:
            privileged: true
            runAsNonRoot: false
            allowPrivilegeEscalation: true
          resources: {}
```

#### Step 3.2 — Run Conftest against the non-compliant manifest

```bash
conftest test manifests/deployment_noncompliant.yaml \
  --policy policies/ \
  --all-namespaces
```

Expected output — you should see multiple failures:

```text
FAIL - manifests/deployment_noncompliant.yaml - k8s.pci - PCI-DSS 6.3.3: Container image payment-api:latest uses ':latest' tag.
FAIL - manifests/deployment_noncompliant.yaml - k8s.pci - PCI-DSS 7.2.1: Container payment-api is privileged.
FAIL - manifests/deployment_noncompliant.yaml - k8s.pci - PCI-DSS 6.4.1: hostNetwork: true exposes the host network stack.
FAIL - manifests/deployment_noncompliant.yaml - k8s.pci - PCI-DSS 7.2.1: Container payment-api sets allowPrivilegeEscalation: true.
FAIL - manifests/deployment_noncompliant.yaml - k8s.soc2 - SOC 2 CC6.1: Container payment-api has no memory limit.
FAIL - manifests/deployment_noncompliant.yaml - k8s.soc2 - SOC 2 CC6.6: hostNetwork: true violates network access controls.
FAIL - manifests/deployment_noncompliant.yaml - k8s.soc2 - SOC 2 CC6.1: Container payment-api must set runAsNonRoot: true.
7 tests, 0 passed, 0 warnings, 7 failures
```

Record the exact violation count and each violation message in your lab report.

#### Step 3.3 — Test Conftest with JSON output for CI integration

```bash
conftest test manifests/deployment_noncompliant.yaml \
  --policy policies/ \
  --all-namespaces \
  --output json
```

Review the JSON output structure. In a CI pipeline this output could be parsed and posted as a pull request comment or stored as a compliance artifact.

---

### Part 4 — Remediate and Re-Evaluate

#### Step 4.1 — Create the remediated Deployment manifest

Create `manifests/deployment_compliant.yaml` that corrects all violations identified in Part 3:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service
  namespace: production
spec:
  replicas: 2
  selector:
    matchLabels:
      app: payment-service
  template:
    metadata:
      labels:
        app: payment-service
    spec:
      hostNetwork: false
      containers:
        - name: payment-api
          image: payment-api:2.1.4
          securityContext:
            privileged: false
            runAsNonRoot: true
            runAsUser: 1000
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
          resources:
            limits:
              memory: "256Mi"
              cpu: "500m"
            requests:
              memory: "128Mi"
              cpu: "250m"
```

#### Step 4.2 — Run Conftest against the compliant manifest

```bash
conftest test manifests/deployment_compliant.yaml \
  --policy policies/ \
  --all-namespaces
```

Expected output:

```text
6 tests, 6 passed, 0 warnings, 0 failures
```

If any tests still fail, review the violation messages and adjust `deployment_compliant.yaml` until all pass.

#### Step 4.3 — Write a reflection

In your lab report, answer the following questions (2–3 sentences each):

1. The compliant manifest includes `readOnlyRootFilesystem: true` and `capabilities.drop: [ALL]` even though no Rego policy explicitly checks for them. Why is this considered best practice even without a policy enforcement requirement?

2. The SOC 2 CC6.1 policy fires two separate `deny` rules for `runAsNonRoot`: one that checks `!= true` and one that checks `not container.securityContext.runAsNonRoot`. Why are both rules needed? What case does each handle?

3. If you were deploying Gatekeeper in a production cluster and adopting this policy set for the first time, which `enforcementAction` would you start with and why?

---

### Deliverables

Submit the following in your lab report document:

1. The complete content of `policies/k8s_pci.rego`
2. The complete content of `policies/k8s_soc2.rego`
3. The complete content of `policies/k8s_pci_test.rego`
4. Screenshot or copy of `opa test policies/ -v` output showing all tests passing
5. Screenshot or copy of Conftest output for `deployment_noncompliant.yaml` showing all violations
6. Screenshot or copy of Conftest output for `deployment_compliant.yaml` showing 0 failures
7. Answers to the three reflection questions in Step 4.3

---

### Grading Rubric

| Criterion | Points |
|---|---|
| `k8s_pci.rego` contains all four required deny rules with correct Rego syntax | 20 |
| `k8s_soc2.rego` contains all five required deny rules with correct Rego syntax | 20 |
| `k8s_pci_test.rego` contains all four test functions; `opa test` passes all tests | 20 |
| Conftest output for non-compliant manifest shows all expected violations | 15 |
| Conftest output for compliant manifest shows 0 failures | 15 |
| Reflection questions answered with technical depth and accuracy | 10 |
| **Total** | **100** |

---

### Common Errors and Troubleshooting

**Conftest reports no failures on the non-compliant manifest**: Verify the `--all-namespaces` flag is present. Without it, Conftest defaults to the `main` package and may not find `k8s.pci` or `k8s.soc2`.

**OPA eval returns empty result set**: The Rego condition may not match the input structure. Use `opa eval --data policies/k8s_pci.rego --input manifests/test_input.json "input"` to inspect the input document as OPA sees it. Compare field paths carefully — YAML keys become JSON object keys.

**Test fails with "undefined"**: The `import data.k8s.pci` statement is required in the test file to reference the policy package. Without it, `pci.deny` is undefined.

**`endswith` function error**: `endswith` is a built-in OPA function that takes exactly two string arguments. If the image field is missing from the input, the rule simply does not fire — it does not cause an error.

---

*CIS-4350 DevSecOps and CI/CD Pipelines | Texas Wesleyan University | Professor Nash*
