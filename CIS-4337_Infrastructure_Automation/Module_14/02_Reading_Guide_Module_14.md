# Reading Guide: Module 14 — Multi-Cloud Provisioning with Terraform

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Overview

This reading guide covers Terraform's multi-provider and multi-cloud capabilities. You will understand how to configure multiple providers, use provider aliasing for multi-region and multi-account scenarios, manage provider version constraints, and evaluate the architectural patterns and trade-offs of multi-cloud infrastructure.

**Estimated reading time:** 55–70 minutes

---

## Section 1: Provider Configuration Fundamentals

### 1.1 The Provider Block

Every Terraform provider requires a `provider` block that configures how Terraform connects to that service. The provider block specifies authentication, region or location, and any provider-specific settings.

```hcl
provider "aws" {
  region = "us-east-2"
}

provider "azurerm" {
  features {}
  subscription_id = var.azure_subscription_id
  tenant_id       = var.azure_tenant_id
}

provider "google" {
  project = var.gcp_project_id
  region  = "us-central1"
}
```

The `features {}` block in the Azure provider is required even if empty — it was introduced to allow future feature flags without breaking existing configurations.

### 1.2 The required_providers Block

All providers used in a configuration must be declared in the `terraform` block's `required_providers` section:

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}
```

The `source` field uses the format `<registry>/<namespace>/<type>`. For official providers hosted on the Terraform Registry, the format is `hashicorp/<type>`. Community providers follow `<namespace>/<type>`. Third-party providers may be hosted on private registries with a full hostname prefix.

### 1.3 Multi-Provider Dependency Management

Terraform's dependency graph operates across all providers. When an Azure resource needs the output of an AWS resource — for example, an Azure Private Link endpoint pointing to an AWS service IP address — Terraform automatically determines the creation order. The AWS resource is created first, its output is captured, and that value flows into the Azure resource creation.

This cross-provider dependency tracking is one of the most powerful features of Terraform's declarative model. You declare the desired state and Terraform figures out the execution order regardless of which cloud each resource lives in.

---

## Section 2: Provider Aliasing

### 2.1 Default and Aliased Providers

When a Terraform configuration contains only one `provider` block for a given provider type, that block is the default provider for all resources of that type. When a configuration needs multiple instances of the same provider — different regions or different accounts — provider aliasing is required.

A provider block with no `alias` attribute is the default. All resource blocks that do not specify a `provider` meta-argument use the default provider. A provider block with an `alias` attribute must be explicitly referenced in each resource that uses it.

```hcl
provider "aws" {
  region = "us-east-2"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_vpc" "east" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_vpc" "west" {
  cidr_block = "10.1.0.0/16"
  provider   = aws.west
}
```

The `aws_vpc.east` resource uses the default (us-east-2) provider. The `aws_vpc.west` resource uses the aliased (us-west-2) provider.

### 2.2 Passing Aliases to Modules

When a child module needs to use an aliased provider from its parent, you pass the provider using the `providers` map in the module block:

```hcl
module "east_app" {
  source = "./modules/app"

  providers = {
    aws = aws.primary
  }
}

module "west_app" {
  source = "./modules/app"

  providers = {
    aws = aws.west
  }
}
```

This allows you to deploy the same module configuration in two different regions or accounts by simply changing which provider alias the module receives. The module itself does not need to know about aliasing — it just uses `provider "aws"` normally, and the parent configuration controls which provider instance it gets.

### 2.3 Multi-Account Cross-Cloud Aliasing

In enterprise environments, Terraform configurations often span multiple AWS accounts and multiple Azure subscriptions. The full pattern uses `assume_role` in AWS and `subscription_id` in Azure:

```hcl
provider "aws" {
  alias  = "networking"
  region = "us-east-2"
  assume_role {
    role_arn = "arn:aws:iam::111111111111:role/TerraformExecutor"
  }
}

provider "aws" {
  alias  = "workloads"
  region = "us-east-2"
  assume_role {
    role_arn = "arn:aws:iam::222222222222:role/TerraformExecutor"
  }
}

provider "azurerm" {
  alias           = "prod_subscription"
  features        {}
  subscription_id = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
}
```

Each provider instance authenticates independently with its own credentials or assumed role. The CI pipeline runner needs permission to assume all roles used in the configuration.

---

## Section 3: Provider Version Constraints

### 3.1 Semantic Versioning

Terraform providers follow semantic versioning: `MAJOR.MINOR.PATCH`. The conventions are:

- MAJOR version changes introduce breaking changes — resources or arguments may be renamed, removed, or change behavior
- MINOR version changes add new resources or arguments without breaking existing configurations
- PATCH version changes fix bugs without adding or removing functionality

Understanding this convention is essential for choosing version constraints.

### 3.2 Constraint Operators

| Operator | Example | Meaning |
|----------|---------|---------|
| `=` | `= 5.12.3` | Exactly this version only |
| `!=` | `!= 5.0.0` | Any version except this one |
| `>` | `> 5.0.0` | Greater than this version |
| `>=` | `>= 5.0.0` | This version or newer |
| `<` | `< 6.0.0` | Older than this version |
| `<=` | `<= 5.12.3` | This version or older |
| `~>` | `~> 5.0` | Pessimistic constraint — 5.x only |

The `~>` operator is the most important. `~> 5.0` allows `5.0.0`, `5.1.0`, `5.12.3` but not `6.0.0`. `~> 5.12.3` allows `5.12.3`, `5.12.4`, `5.12.10` but not `5.13.0`.

Using `~> MAJOR.MINOR` is the recommended production practice — it allows patch updates for bug fixes while preventing minor and major version jumps.

### 3.3 The Lock File

The `.terraform.lock.hcl` file records the resolved provider versions and their content hashes. Example entry:

```hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "5.12.0"
  constraints = "~> 5.0"
  hashes = [
    "h1:...",
    "zh:...",
  ]
}
```

The `h1:` hash is a hash of the zip archive. The `zh:` hashes are per-platform hashes for the specific binary. When another engineer runs `terraform init`, Terraform downloads the same version and verifies it matches the recorded hashes — preventing supply chain attacks where a provider binary is tampered with.

The lock file must be committed to version control. Running `terraform init -upgrade` updates the lock file to the newest version satisfying the constraints.

---

## Section 4: Cross-Cloud Architecture Patterns

### 4.1 Active-Active Multi-Cloud

In active-active multi-cloud, both providers simultaneously serve production traffic. This is the most resilient and most expensive pattern.

Implementation with Terraform uses module composition:

- A shared `app_tier` module defines the application infrastructure in provider-agnostic terms where possible
- The root module calls `app_tier` twice with different provider aliases
- A global load balancer (AWS Global Accelerator, Azure Front Door, or Cloudflare) distributes traffic between both cloud deployments
- Terraform manages all components including the global load balancer configuration

The challenge of active-active is data consistency. Application databases cannot usually be active-active across clouds without a globally distributed database service (CockroachDB, Azure Cosmos DB, or Spanner). Terraform provisions the database cluster, but the application architecture must be designed for multi-master replication.

### 4.2 Primary-Failover

Primary-failover is the most practical starting point for multi-cloud resilience. The primary cloud runs the production workload. The failover cloud runs a warm standby — provisioned and ready but not serving traffic.

DNS-based failover uses health checks on the primary endpoint. When health checks fail, the DNS routing policy automatically switches traffic to the failover endpoint. AWS Route 53, Azure Traffic Manager, and GCP Cloud DNS all support health-check-based failover.

Terraform provisions the health checks and routing policies alongside the infrastructure. This ensures the failover mechanism is always configured correctly and not subject to manual error.

### 4.3 Best-of-Breed Service Selection

The pragmatic multi-cloud pattern selects each cloud provider for specific workloads where it offers a genuine advantage:

- AWS for compute-intensive workloads, Lambda serverless, and the broadest service catalog
- Azure for Microsoft 365 integration, Azure Active Directory SSO, and Windows Server workloads
- GCP for BigQuery data warehousing, Vertex AI, and Anthos multi-cloud Kubernetes

Terraform provisions all resources across all three clouds and manages the cross-cloud networking. The operational challenge is team expertise — someone must understand each cloud deeply.

---

## Section 5: Multi-Cloud DNS

### 5.1 DNS as the Multi-Cloud Routing Layer

DNS is the universally available routing mechanism that works across cloud boundaries. A DNS record can point to any IP address regardless of which cloud hosts it. Health-check-based DNS routing allows automatic failover without changing the application.

### 5.2 Route 53 with Multi-Cloud Endpoints

AWS Route 53 health checks can monitor any TCP or HTTP endpoint, including endpoints in Azure or GCP. The routing policy determines traffic distribution:

- **Simple routing**: a single record pointing to one endpoint — no failover
- **Weighted routing**: distribute traffic by percentage across multiple endpoints
- **Latency-based routing**: route each request to the endpoint with the lowest latency for that client
- **Failover routing**: primary and secondary designation with automatic failover on health check failure

Terraform manages Route 53 records with routing policies through `aws_route53_record` with the appropriate routing policy block. A health check targeting an Azure endpoint uses `aws_route53_health_check` with the Azure IP address or hostname.

### 5.3 Third-Party DNS Providers

Teams already using Cloudflare, NS1, or another DNS provider can use the corresponding Terraform provider instead of Route 53. The `cloudflare` provider manages DNS records, load balancing pools, and health checks. The multi-cloud DNS configuration looks the same from a Terraform perspective — resource blocks and provider references — regardless of which DNS service backs it.

---

## Section 6: Multi-Cloud Trade-offs

### 6.1 Complexity Costs

Multi-cloud infrastructure multiplies operational complexity. Engineers must be proficient in multiple cloud platforms. Security policies must be implemented consistently across platforms with different IAM models. Incident response must span multiple cloud consoles and CLIs.

### 6.2 Cost Considerations

Data transfer costs between cloud providers are significant. AWS charges for data leaving its network (egress). Azure and GCP do the same. An active-active multi-cloud setup with continuous data replication can have substantial egress costs that eliminate the cost savings from cloud competition.

Accurately modeling the total cost of a multi-cloud architecture requires including:

- Compute costs in each cloud
- Storage costs in each cloud
- Egress/ingress costs between clouds
- Additional operational tooling costs (unified observability, multi-cloud management platforms)

### 6.3 When to Use Multi-Cloud

Multi-cloud is justified when:

- Regulatory requirements mandate no single cloud provider dependency
- A specific cloud service has a capability not available anywhere else (e.g., Azure OpenAI for specific enterprise contract terms)
- Business continuity requirements mandate survival of a complete cloud provider outage
- An acquisition brought an existing cloud footprint that must be integrated

Multi-cloud is not justified when the primary motivation is "avoiding vendor lock-in" as an abstract goal. Every Terraform module for cloud-specific resources is already cloud-specific — true cloud portability requires using only the lowest common denominator services, which sacrifices the very capabilities that make each cloud valuable.

---

## Key Terms

- **Provider alias**: a named instance of a provider allowing multiple regions, accounts, or subscriptions
- **required_providers**: block in the `terraform` configuration declaring all providers and version constraints
- **Pessimistic constraint (`~>`)**: allows patch and minor updates within a major version
- **Lock file (`.terraform.lock.hcl`)**: records resolved provider versions and content hashes
- **assume_role**: AWS provider configuration that causes Terraform to assume a specific IAM role before making API calls
- **Active-active multi-cloud**: both clouds simultaneously serving production traffic
- **Primary-failover**: one cloud serves production; the other is a warm standby with automatic DNS failover
- **Egress cost**: charges for data leaving a cloud provider's network to the internet or another provider

---

## Review Questions

1. What is the difference between a default provider and an aliased provider? How do resources reference each?

2. What does the `~>` version constraint operator mean, and why is it the recommended choice for production configurations?

3. Explain how the `.terraform.lock.hcl` file prevents supply chain attacks on provider binaries.

4. Describe the primary-failover multi-cloud pattern and how DNS-based routing enables automatic failover.

5. What are the `providers` map argument on a module block and when is it required?

6. List two genuine business justifications for multi-cloud architecture and two scenarios where it adds complexity without proportional benefit.

---

## Supplemental Resources

**1. Terraform Provider Configuration and Aliasing**
<https://developer.hashicorp.com/terraform/language/providers/configuration>
The official HashiCorp documentation for provider configuration, covering the `provider` block syntax, authentication methods, and the `alias` meta-argument used to define multiple configurations of the same provider. Includes concrete examples of multi-region and multi-account aliasing and explains how module `providers` maps pass aliased providers to child modules.

**2. Dependency Lock File (.terraform.lock.hcl)**
<https://developer.hashicorp.com/terraform/language/files/dependency-lock>
Detailed reference for the `.terraform.lock.hcl` file, including how Terraform records selected provider versions and hashes, how the lock file interacts with version constraints in `required_providers`, and when to use `terraform init -upgrade` to intentionally move to a newer allowed version. Essential reading for understanding why the lock file must be committed to version control.

**3. HashiCorp Terraform Multi-Cloud Architecture Guide**
<https://developer.hashicorp.com/terraform/tutorials/aws/provider-use>
A HashiCorp tutorial demonstrating practical multi-provider configurations, covering how to manage state for resources spanning multiple providers and accounts, how to use `assume_role` inside a provider block for cross-account AWS deployments, and the provider version constraint operators (`~>`, `>=`, `=`) with worked examples of how the lock file changes after each `init` or `init -upgrade` invocation.

---

End of Module 14 Reading Guide
