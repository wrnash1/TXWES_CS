# Video Script: Module 14 — Multi-Cloud Provisioning with Terraform

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Segment 1: Introduction (Lines 1–18)

Welcome back to CIS-4337. This is Module 14: Multi-Cloud Provisioning with Terraform.

One of Terraform's defining advantages over cloud-native tools like CloudFormation or Azure Bicep is that a single tool can provision resources across AWS, Azure, GCP, and dozens of other providers simultaneously. Multi-cloud architectures are increasingly common — not as an ideological preference but because different clouds have genuine strengths. AWS leads in compute variety and ML services. Azure leads in enterprise identity and Microsoft workload integration. GCP leads in data analytics and Kubernetes-native tooling.

In this module we will cover:

- Configuring multiple providers in a single Terraform workspace
- Provider aliasing for multi-region and multi-account scenarios
- Provider version constraints and lock files
- Cross-cloud architecture patterns: active-active, primary-failover, and cloud-native service selection
- Multi-cloud DNS with Terraform
- The trade-offs of multi-cloud complexity

These concepts are tested in the Terraform Associate exam, particularly the understanding of provider configuration and aliasing.

---

## Segment 2: Configuring Multiple Providers (Lines 19–50)

Terraform allows you to configure as many provider instances as your configuration requires. Each provider block declares one connection to one cloud platform or service.

A configuration that uses both AWS and Azure starts with two provider blocks:

```hcl
provider "aws" {
  region = "us-east-2"
}

provider "azurerm" {
  features {}
  subscription_id = var.azure_subscription_id
}
```

You can then write resources for both providers in the same Terraform configuration. Terraform manages the dependency graph across all providers — if an Azure resource needs an output from an AWS resource, Terraform will create the AWS resource first and pass the value forward.

This is a genuinely powerful capability. Consider provisioning an AWS VPC, an Azure Virtual Network, and a site-to-site VPN between them in a single `terraform apply`. Every component is managed together, versioned together, and destroyed together.

The `required_providers` block must list all providers:

```hcl
terraform {
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

Provider version constraints follow semantic versioning. The `~>` operator is the pessimistic constraint — `~> 5.0` allows any version from 5.0 up to but not including 6.0. This is the recommended constraint for production configurations: it allows patch and minor updates but prevents major version upgrades that may contain breaking changes.

---

## Segment 3: Provider Aliasing (Lines 51–80)

Provider aliasing solves two problems: deploying resources to multiple regions of the same cloud, and deploying resources to multiple accounts or subscriptions of the same cloud.

Consider a disaster recovery setup where you provision an S3 bucket in `us-east-2` for primary and a replication destination in `us-west-2` for DR. You need two AWS provider instances. You configure this with aliases:

```hcl
provider "aws" {
  region = "us-east-2"
  alias  = "primary"
}

provider "aws" {
  region = "us-west-2"
  alias  = "dr"
}
```

The first provider block without an alias becomes the default AWS provider. Any provider block with an alias must be explicitly referenced in resources using the `provider` meta-argument:

```hcl
resource "aws_s3_bucket" "primary" {
  bucket   = "my-app-primary"
  provider = aws.primary
}

resource "aws_s3_bucket" "dr_replica" {
  bucket   = "my-app-dr-replica"
  provider = aws.dr
}
```

Aliasing also enables multi-account patterns. If your organization uses AWS Organizations with separate accounts for dev, staging, and production, you can configure provider aliases for each account:

```hcl
provider "aws" {
  alias  = "dev"
  region = "us-east-2"
  assume_role {
    role_arn = "arn:aws:iam::111111111111:role/TerraformExecutor"
  }
}

provider "aws" {
  alias  = "prod"
  region = "us-east-2"
  assume_role {
    role_arn = "arn:aws:iam::999999999999:role/TerraformExecutor"
  }
}
```

This pattern is extremely common in enterprise AWS environments. A single Terraform workspace can manage resources across multiple accounts by assuming the appropriate role in each account.

---

## Segment 4: Provider Version Constraints and Lock Files (Lines 81–105)

When you run `terraform init`, Terraform creates a `.terraform.lock.hcl` file. This lock file records the exact provider versions installed and their checksums. It is the Terraform equivalent of `package-lock.json` in Node.js or `Gemfile.lock` in Ruby.

The lock file should be committed to version control. This ensures that every team member and every CI pipeline runner uses exactly the same provider versions. Without the lock file, two engineers might get different provider versions depending on when they run `terraform init`, leading to plan differences.

To upgrade a provider version, run `terraform init -upgrade`. This downloads the newest version that satisfies the version constraint and updates the lock file. Always review the provider's changelog before upgrading in production — provider major versions often include breaking changes that require configuration updates.

Version constraint operators:

- `= 5.0.0` — exact version only. Too restrictive for most cases.
- `>= 5.0.0` — any version 5.0.0 or higher. Too permissive — allows major version bumps.
- `~> 5.0` — any 5.x release. Recommended for production.
- `~> 5.12.3` — any 5.12.x patch release. Maximum control.

For multi-cloud configurations, always pin all provider versions. Version drift between providers can cause subtle incompatibilities, especially when providers share resources (for example, a DNS provider that creates records in both AWS Route 53 and GCP Cloud DNS).

---

## Segment 5: Cross-Cloud Architecture Patterns (Lines 106–135)

Let me describe three common multi-cloud architecture patterns and how Terraform implements each.

The first pattern is active-active multi-cloud. Both clouds serve production traffic simultaneously. Load is distributed across clouds by a global load balancer or DNS-based routing. This provides maximum resilience — if one entire cloud provider has an outage, the other continues serving traffic.

In Terraform, you provision identical application infrastructure in each cloud using module composition. A single Terraform module defines the application tier, and you call it twice: once with AWS provider configuration and once with Azure provider configuration. This is the "write once, deploy anywhere" ideal, though in practice cloud-specific services require cloud-specific resource types.

The second pattern is primary-failover. One cloud is primary and the other is a warm standby. Traffic normally routes to the primary. If the primary fails health checks, DNS or a global load balancer switches to the failover cloud. This is cheaper than active-active but has a failover delay.

The third pattern is cloud-native service selection. You use each cloud for what it does best. Your primary application runs on AWS EC2. Your data analytics pipeline runs on GCP BigQuery. Your identity management uses Azure Active Directory. Terraform provisions all three and manages the cross-cloud networking and data transfer.

All three patterns require cross-cloud networking — usually site-to-site VPNs or direct interconnects between cloud networks. Terraform can provision AWS Virtual Private Gateway, Azure VPN Gateway, and GCP Cloud VPN and configure the peering between them, all in a single configuration.

---

## Segment 6: Multi-Cloud DNS with Terraform (Lines 136–158)

DNS is the connective tissue of multi-cloud architectures. It is what allows a client to find your application regardless of which cloud is serving it at any given moment.

Terraform can manage DNS records in multiple DNS providers simultaneously. A common setup uses AWS Route 53 as the primary authoritative DNS with latency-based routing records pointing to both AWS and Azure endpoints.

You configure weighted or latency-based routing policies in Route 53 using `aws_route53_record` with routing policy blocks. When the primary endpoint is healthy, 100% of traffic routes there. When the health check fails, Route 53 automatically routes to the secondary endpoint in the other cloud.

For global traffic management across multiple cloud regions, AWS Global Accelerator, Azure Front Door, and GCP Cloud Load Balancing all offer their own multi-cloud routing capabilities. Terraform supports all three through their respective provider resources.

The key insight for exam purposes is this: DNS records are Terraform resources like any other. You can create an `aws_route53_record` that points to an Azure Load Balancer IP address. Terraform does not care that the record in one provider points to a resource in another — it manages each resource through its own provider.

---

## Segment 7: Multi-Cloud Complexity Trade-offs (Lines 159–185)

Multi-cloud is not free. Every capability you gain in resilience and vendor independence comes with a corresponding increase in operational complexity.

Engineering complexity is the first cost. Engineers must understand multiple cloud platforms, multiple CLIs, multiple IAM models, and multiple billing structures. Skills that transfer from AWS to Azure are not as portable as the vendor marketing suggests. Security models differ significantly — AWS IAM, Azure RBAC, and GCP IAM have fundamentally different designs.

Cost management is the second challenge. Data egress fees accumulate rapidly when data flows between clouds. A multi-cloud active-active setup may have lower application downtime but higher monthly cost due to cross-cloud traffic.

Observability complexity is the third challenge. Distributed tracing, metrics, and logs span multiple cloud-native observability stacks. You need a unified observability platform — Datadog, Grafana Cloud, or OpenTelemetry — that aggregates data from all clouds.

Terraform itself adds a layer of complexity. When providers have incompatible resource models, abstraction breaks down and you must write cloud-specific code rather than reusable modules.

My recommendation for practitioners: start with multi-region on a single cloud before attempting multi-cloud. The resilience benefits of multi-region single-cloud capture most of the value at a fraction of the complexity. Move to multi-cloud when you have a specific business requirement that cannot be satisfied with a single cloud provider.

In the next module we will explore advanced Terraform patterns — dynamic blocks, for_each, conditional expressions, and refactoring techniques.

See you there.

---

End of Module 14 Video Script
