# Reading Guide: Module 11 — Infrastructure as Code on GCP

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4329 &BULL; GOOGLE CLOUD PLATFORM (GCP) CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Google Cloud &bull; CIS-4329 Module 11</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=UGRDM86MBIQ" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/UGRDM86MBIQ" title="Google Cloud Associate Cloud Engineer (ACE) Official Prep" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Google Cloud Associate Cloud Engineer (ACE) Official Prep</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This reading guide accompanies the Module 11 video lectures on Infrastructure as Code.
It covers Cloud Deployment Manager, Terraform with the GCP provider, state management,
and infrastructure versioning patterns.

**Estimated reading time**: 60–75 minutes

---

### Learning Objectives

After completing this module's readings you will be able to:

- Explain the purpose and benefits of Infrastructure as Code
- Write and deploy Cloud Deployment Manager configurations
- Use Deployment Manager Jinja2 templates for reusable resource definitions
- Initialize, plan, apply, and destroy infrastructure with Terraform
- Configure Terraform remote state in Cloud Storage
- Compare Deployment Manager and Terraform for GCP use cases
- Describe infrastructure versioning best practices using Git

---

### Required Reading 1: Cloud Deployment Manager

**Source**: Google Cloud Documentation — Deployment Manager Overview

**URL**: `https://cloud.google.com/deployment-manager/docs/fundamentals`

#### Deployment Manager Key Terms

- **Deployment**: A named collection of GCP resources defined and managed as a unit;
  creating, updating, and deleting a deployment affects all its resources together
- **Configuration file**: A YAML file listing resources with their types and properties;
  the primary input to Deployment Manager
- **Template**: A reusable Jinja2 or Python file that generates resource definitions;
  imported by configuration files and parameterized with `properties`
- **Type**: Specifies the GCP resource type, such as `compute.v1.instance` or
  `storage.v1.bucket`
- **Manifest**: An immutable record of a deployment at a specific point in time;
  Deployment Manager retains a manifest history for each deployment
- **Preview**: A dry-run mode that shows what changes will be made without applying them;
  enabled with `--preview` flag

#### Deployment Manager CLI Reference

| Command | Purpose |
|---|---|
| `gcloud deployment-manager deployments create NAME --config=FILE` | Create a new deployment |
| `gcloud deployment-manager deployments update NAME --config=FILE` | Update an existing deployment |
| `gcloud deployment-manager deployments update NAME --config=FILE --preview` | Preview changes before applying |
| `gcloud deployment-manager deployments cancel-preview NAME` | Revert a preview without applying |
| `gcloud deployment-manager deployments delete NAME` | Delete deployment and all its resources |
| `gcloud deployment-manager deployments describe NAME` | Show deployment status and resources |
| `gcloud deployment-manager deployments list` | List all deployments in the project |
| `gcloud deployment-manager manifests list --deployment=NAME` | List deployment history |

#### Deployment Manager ACE Exam Focus Points

- Deployment Manager manages resources as a unit — deleting a deployment deletes all
  its resources unless you explicitly exclude them
- The `$(ref.RESOURCE.PROPERTY)` syntax creates implicit dependencies; Deployment Manager
  creates referenced resources before dependents
- Jinja2 templates use `{{ properties["key"] }}` to access parameters passed from the
  configuration file
- Deployment Manager does not require a local state file — state is managed entirely
  by the GCP service
- Python templates are also supported but Jinja2 is more common in documentation

#### Deployment Manager Review Questions

1. What is the difference between a configuration file and a template in Deployment
   Manager?
2. What does the `--preview` flag do, and how do you apply or cancel a preview?
3. What happens to the resources in a deployment when you run `deployments delete`?

---

### Required Reading 2: Terraform with GCP Provider

**Source**: Terraform Documentation — Google Cloud Provider

**URL**: `https://registry.terraform.io/providers/hashicorp/google/latest/docs`

#### Terraform Key Terms

- **HCL (HashiCorp Configuration Language)**: The declarative language used to write
  Terraform configurations; human-readable JSON-compatible syntax
- **Provider**: A plugin that implements CRUD operations for a specific platform; the
  `google` provider manages GCP resources
- **Resource block**: The primary unit of a Terraform configuration; defines one GCP
  resource and its desired state
- **State file**: `terraform.tfstate` — a JSON file tracking every resource Terraform
  manages; must not be deleted or modified manually
- **Backend**: Configures where the state file is stored; local by default; GCS backend
  for team environments
- **Plan**: `terraform plan` output showing what will be created, updated, or destroyed;
  no changes are applied
- **Module**: A directory of `.tf` files that can be called from other configurations;
  supports parameterization via `variable` blocks

#### Terraform Workflow Steps

1. `terraform init` — downloads provider plugins and initializes the backend
2. `terraform validate` — checks configuration syntax without connecting to GCP
3. `terraform plan` — shows what changes will be made; compare to the state file
4. `terraform apply` — executes the plan; prompts for confirmation
5. `terraform destroy` — destroys all resources tracked in the state file

#### Terraform GCP Provider Authentication

Terraform authenticates to GCP using Application Default Credentials (ADC). In Cloud
Shell or on a GCE VM with the correct service account, ADC works automatically. For
local development:

```bash
# Authenticate using your user account
gcloud auth application-default login

# Or specify a service account key file
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

#### Terraform Remote State in GCS

```hcl
terraform {
  backend "gcs" {
    bucket  = "my-tf-state"
    prefix  = "env/prod"
  }
}
```

The GCS bucket must exist before running `terraform init`. Enable object versioning on
the bucket to allow state file rollback.

#### Terraform ACE Exam Focus Points

- Terraform state is the source of truth — if a resource is deleted outside of Terraform,
  the next `terraform plan` shows it as needing recreation
- `terraform import` brings existing resources under Terraform management; the resource
  block must be written manually after import
- The `google` provider version is pinned in the `terraform` block to prevent breaking
  changes from provider updates
- Remote state in GCS allows multiple team members to work with the same infrastructure
  without state conflicts
- `terraform plan` should always be reviewed before `terraform apply` in production

#### Terraform Review Questions

1. What is the purpose of the Terraform state file, and why should it never be deleted
   manually?
2. What are the five steps of the Terraform workflow in order?
3. What backend configuration stores Terraform state in Cloud Storage?

---

### Required Reading 3: Deployment Manager vs Terraform

**Source**: Google Cloud Blog — Choosing IaC Tools on GCP

#### Comparison Table

| Dimension | Cloud Deployment Manager | Terraform |
|---|---|---|
| Language | YAML + Jinja2 or Python | HCL |
| GCP scope | GCP only | Multi-cloud |
| State management | GCP-managed | Local or remote .tfstate file |
| Module ecosystem | Limited | Extensive (Terraform Registry) |
| Community size | Small | Very large |
| CI/CD integration | Via Cloud Build | Via Cloud Build, GitHub Actions, etc. |
| Drift detection | Via manifest comparison | Via `terraform plan` vs state |
| Exam coverage | ACE tested | ACE tested |

#### When to Use Each

Use Deployment Manager when:

- Your team is GCP-only and wants zero state file management
- You are working in an environment where third-party tools are restricted
- You need deep integration with GCP-specific APIs not yet in the Terraform provider

Use Terraform when:

- Your infrastructure spans multiple cloud providers
- You want access to the large Terraform module registry
- Your team prefers HCL over YAML
- You need advanced features like workspaces, moved blocks, and conditional resources

#### IaC Comparison ACE Exam Focus Points

- Both tools create GCP resources; the ACE exam tests whether you know the basic commands
  and concepts for each
- Deployment Manager is GCP-native and requires no state file management
- Terraform requires explicit state management; remote state is required for teams
- Neither tool locks you in — you can migrate between them if needed

---

### Required Reading 4: Infrastructure Versioning Patterns

**Source**: Google Cloud Architecture Center — Infrastructure as Code best practices

**URL**: `https://cloud.google.com/docs/terraform/best-practices-for-terraform`

#### Infrastructure Versioning Key Terms

- **GitOps**: The practice of using Git as the single source of truth for both
  application code and infrastructure; all changes go through pull requests
- **Branch protection**: Prevents direct commits to the main branch; all changes must
  go through reviewed pull requests
- **Environment isolation**: Separate state backends for dev, staging, and production
  to prevent accidental cross-environment changes
- **State locking**: Prevents two users or CI/CD pipelines from running `terraform apply`
  simultaneously; GCS backend supports locking via Cloud Storage object conditions

#### Infrastructure Versioning Best Practices

- Store all IaC configuration in a Git repository alongside application code or in a
  dedicated infrastructure repository
- Never apply Terraform from a local machine in production — always use CI/CD
- Run `terraform plan` as a required check on every pull request
- Tag the infrastructure repository at each production deployment (e.g., `prod-2024-01-15`)
- Use separate `.tfvars` files per environment rather than hardcoded values
- Enable state bucket versioning so corrupted state files can be rolled back

#### Infrastructure Versioning ACE Exam Focus Points

- The ACE exam does not test deep Git knowledge, but may ask about Deployment Manager
  update strategies (preview before apply) and Terraform state isolation patterns
- Multiple Terraform workspaces or separate state files per environment are both valid
  isolation patterns

---

### Pre-Lab Checklist

Before starting Lab 11, confirm you can answer yes to each item:

- I can write a Deployment Manager YAML configuration defining at least 2 resources
- I know the gcloud commands to create, update, describe, and delete a deployment
- I understand what `$(ref.RESOURCE.PROPERTY)` does in a Deployment Manager config
- I can describe the 5-step Terraform workflow
- I know how to configure a GCS backend for Terraform remote state

---

#
---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 11 — Infrastructure as Code on GCP** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 11 — Infrastructure as Code on GCP**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 11 — Infrastructure as Code on GCP**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 11 — Infrastructure as Code on GCP**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


## Additional Resources

- Deployment Manager documentation:
  `https://cloud.google.com/deployment-manager/docs`
- Terraform GCP provider documentation:
  `https://registry.terraform.io/providers/hashicorp/google/latest/docs`
- Terraform best practices on GCP:
  `https://cloud.google.com/docs/terraform/best-practices-for-terraform`
- ACE exam guide:
  `https://cloud.google.com/certification/guides/cloud-engineer`

---

## 9. Supplemental Resources

**1. Google Cloud Documentation — Terraform on Google Cloud**
<https://cloud.google.com/docs/terraform>
Official GCP guide to using Terraform covering provider configuration, GCS remote state setup, best practices for module structure, and how to store and manage Terraform configurations for GCP projects — directly applicable to the lab and ACE exam.

**2. HashiCorp Learn — Get Started with Terraform on GCP**
<https://developer.hashicorp.com/terraform/tutorials/gcp-get-started>
Step-by-step tutorial series from HashiCorp covering Terraform installation, writing the first GCP configuration, running the five-step workflow (init/plan/apply/destroy), and using variables and outputs.

**3. Google Cloud Documentation — Cloud Deployment Manager Fundamentals**
<https://cloud.google.com/deployment-manager/docs/fundamentals>
Comprehensive reference for Deployment Manager covering YAML configuration syntax, Jinja2 and Python templates, the `$(ref.RESOURCE.PROPERTY)` dependency syntax, preview mode, and deployment lifecycle management.
