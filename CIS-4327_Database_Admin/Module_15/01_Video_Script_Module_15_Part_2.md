# Video Script: Module 15 — Database Automation and Monitoring (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Part 2 Introduction

Welcome back to Module 15. In Part 1 we covered Cloud Monitoring metrics, dashboards,
alerting policies, Cloud SQL Insights, Spanner and BigQuery monitoring, maintenance
windows, and automated backups.

In Part 2 we cover Infrastructure as Code with Terraform for database provisioning,
and automated failover testing to validate your high-availability configuration.

---

## SLIDE 2 — Why Infrastructure as Code for Databases?

Manually creating and configuring databases through the GCP console works for
learning and experimentation. In production, it creates problems:

- **Drift**: Configuration changes applied manually are not tracked. Over time the
  actual configuration diverges from what was documented.
- **Reproducibility**: If an instance is lost, recreating it from memory or
  documentation is slow and error-prone.
- **Auditability**: Who changed which setting and when? Manual changes leave no
  audit trail by default.
- **Environment consistency**: Development, staging, and production instances must
  have consistent configurations. Manual management leads to "it works in dev" bugs
  caused by configuration differences.

Infrastructure as Code (IaC) solves all of these problems. Terraform is the most
widely adopted IaC tool for GCP, and it is the primary IaC tool referenced on the
Professional Database Engineer exam.

---

## SLIDE 3 — Terraform Basics for GCP Databases

Terraform uses the **HashiCorp Configuration Language (HCL)** to declare infrastructure.
For GCP, you use the `google` Terraform provider.

Basic structure of a Terraform project:

```text
project/
  main.tf         # Resource definitions
  variables.tf    # Input variable declarations
  outputs.tf      # Output value declarations
  terraform.tfvars  # Variable values (not committed to git)
```

Provider configuration:

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}
```

Core Terraform commands:

- `terraform init` — Initialize the working directory and download providers
- `terraform plan` — Preview changes without applying them
- `terraform apply` — Apply the planned changes
- `terraform destroy` — Delete all resources managed by this configuration

---

## SLIDE 4 — Terraform Resource: Cloud SQL Instance

A complete Cloud SQL for PostgreSQL instance with high availability:

```hcl
resource "google_sql_database_instance" "primary" {
  name             = "prod-pg-instance"
  database_version = "POSTGRES_15"
  region           = var.region
  deletion_protection = true

  settings {
    tier              = "db-n1-standard-4"
    availability_type = "REGIONAL"   # High availability

    backup_configuration {
      enabled                        = true
      start_time                     = "02:00"
      point_in_time_recovery_enabled = true
      transaction_log_retention_days = 7
      retained_backups               = 30
    }

    ip_configuration {
      ipv4_enabled    = false
      private_network = var.vpc_network
    }

    maintenance_window {
      day          = 7    # Sunday
      hour         = 3    # 3 AM
      update_track = "stable"
    }

    database_flags {
      name  = "cloudsql.iam_authentication"
      value = "on"
    }

    insights_config {
      query_insights_enabled  = true
      query_string_length     = 1024
      record_application_tags = true
    }
  }
}
```

The `deletion_protection = true` flag prevents Terraform (and the GCP console)
from deleting the instance accidentally. This is essential for production databases.

---

## SLIDE 5 — Terraform Resource: Cloud SQL Read Replica

```hcl
resource "google_sql_database_instance" "read_replica" {
  name                 = "prod-pg-replica"
  master_instance_name = google_sql_database_instance.primary.name
  database_version     = "POSTGRES_15"
  region               = "us-east1"   # Cross-region replica
  deletion_protection  = true

  settings {
    tier              = "db-n1-standard-2"
    availability_type = "ZONAL"

    ip_configuration {
      ipv4_enabled    = false
      private_network = var.vpc_network_east
    }
  }

  depends_on = [google_sql_database_instance.primary]
}
```

Notice the `depends_on` declaration — Terraform must create the primary instance
before attempting to create the replica. Terraform's dependency graph handles most
ordering automatically via resource references, but explicit `depends_on` is
sometimes needed.

---

## SLIDE 6 — Terraform Resource: BigQuery Dataset and Table

```hcl
resource "google_bigquery_dataset" "analytics" {
  dataset_id    = "analytics_prod"
  location      = "US"
  friendly_name = "Production Analytics"

  access {
    role          = "OWNER"
    user_by_email = var.owner_email
  }

  access {
    role          = "READER"
    special_group = "projectReaders"
  }
}

resource "google_bigquery_table" "orders" {
  dataset_id          = google_bigquery_dataset.analytics.dataset_id
  table_id            = "orders"
  deletion_protection = true

  time_partitioning {
    type  = "DAY"
    field = "order_date"
  }

  clustering = ["region", "category"]

  schema = jsonencode([
    { name = "order_id",    type = "INT64",   mode = "REQUIRED" },
    { name = "customer_id", type = "INT64",   mode = "NULLABLE" },
    { name = "order_date",  type = "DATE",    mode = "NULLABLE" },
    { name = "revenue",     type = "NUMERIC", mode = "NULLABLE" },
    { name = "region",      type = "STRING",  mode = "NULLABLE" },
    { name = "category",    type = "STRING",  mode = "NULLABLE" }
  ])
}
```

---

## SLIDE 7 — Terraform State Management

Terraform tracks the actual deployed state of resources in a **state file**
(`terraform.tfstate`). For teams, the state file must be stored remotely so all
team members and CI/CD pipelines share the same view.

Configuring a GCS backend for Terraform state:

```hcl
terraform {
  backend "gcs" {
    bucket = "my-terraform-state-bucket"
    prefix = "database/prod"
  }
}
```

Best practices:

- Never commit `terraform.tfstate` to git — it may contain sensitive data
- Enable object versioning on the GCS bucket to keep state history
- Use `terraform state lock` (handled automatically with GCS backend) to prevent
  concurrent applies from corrupting state
- Use separate state files per environment (dev, staging, prod)

**Workspaces**: Terraform workspaces allow multiple state files within one
configuration directory — useful for managing dev/staging/prod variants.

```bash
terraform workspace new staging
terraform workspace select prod
terraform apply
```

---

## SLIDE 8 — Automated Failover Testing

High availability configuration on Cloud SQL uses a standby instance in a
different zone. When the primary fails, Cloud SQL automatically fails over to
the standby. But how do you know this works?

You test it. Regularly.

**Why test failover?**

- Failover behavior may have changed after a maintenance event or configuration change
- Application connection poolers may not handle reconnection correctly
- DNS TTL or connection string caching may delay recovery beyond acceptable RPO/RTO
- Failover may surface bugs in application error handling that only appear during
  a reconnection event

**How to trigger failover on Cloud SQL**:

```bash
gcloud sql instances failover prod-pg-instance
```

This command forces an immediate failover from the primary to the standby replica.
Cloud SQL promotes the standby to primary. The original primary becomes the new standby.

**What to measure during failover**:

- **Time to failover**: How long from `gcloud sql instances failover` until the new
  primary accepts connections. Typically 30–120 seconds.
- **Application recovery time**: How long from failover initiation until the application
  resumes normal operation (the true RTO from the user's perspective).
- **Connection errors**: How many errors did users experience? What error codes?
- **Data loss**: Were any committed transactions lost? (Should be zero for Cloud SQL HA.)

---

## SLIDE 9 — Automated Failover Testing Pipeline

In mature organizations, failover testing is automated and run on a schedule.
Here is a simple automated failover test pipeline using Cloud Build:

```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/gcloud'
    id: 'pre-failover-health'
    args:
      - sql
      - instances
      - describe
      - prod-pg-instance
      - --format=json

  - name: 'gcr.io/cloud-builders/gcloud'
    id: 'trigger-failover'
    args:
      - sql
      - instances
      - failover
      - prod-pg-instance

  - name: 'gcr.io/cloud-builders/gcloud'
    id: 'wait-for-recovery'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        for i in $(seq 1 30); do
          STATUS=$(gcloud sql instances describe prod-pg-instance \
            --format="value(state)")
          if [ "$$STATUS" = "RUNNABLE" ]; then
            echo "Instance recovered after $$((i * 10)) seconds"
            exit 0
          fi
          sleep 10
        done
        echo "Failover did not complete within 300 seconds"
        exit 1

  - name: 'gcr.io/cloud-builders/gcloud'
    id: 'post-failover-health'
    args:
      - sql
      - instances
      - describe
      - prod-pg-instance
      - --format=json
```

Schedule this Cloud Build trigger to run monthly using Cloud Scheduler.

---

## SLIDE 10 — Database Health Dashboard

A well-designed monitoring dashboard shows at a glance whether a database is healthy.
For Cloud SQL, a standard dashboard includes:

**Row 1 — Instance Overview**:

- CPU utilization (gauge + time series)
- Memory utilization (gauge + time series)
- Active connections vs. max connections

**Row 2 — Storage and I/O**:

- Disk utilization
- Read IOPS and Write IOPS
- Network bytes in/out

**Row 3 — Query Performance** (Cloud SQL Insights data):

- Top 5 queries by CPU time
- P95 query latency trend
- Error rate (failed queries per minute)

**Row 4 — Replication** (if replicas exist):

- Replication lag per replica
- Replica state (RUNNING / STOPPED / ERROR)

Creating dashboards as code using Terraform:

```hcl
resource "google_monitoring_dashboard" "cloud_sql_health" {
  dashboard_json = file("dashboards/cloud_sql_health.json")
}
```

Store dashboard JSON in your IaC repository so dashboards are version-controlled
and reproducible.

---

## SLIDE 11 — Module 15 Summary

Key takeaways for Part 2:

**Terraform**: Use HCL to declare Cloud SQL instances, BigQuery datasets, and
all database configuration. Store state remotely in GCS. Use `deletion_protection = true`
on production databases. Version-control all Terraform configurations.

**Failover testing**: Test HA failover regularly using `gcloud sql instances failover`.
Measure time-to-failover and application recovery time. Automate tests with Cloud Build
and Cloud Scheduler.

**Dashboards**: Build dashboards in Terraform using `google_monitoring_dashboard` so
they are reproducible and version-controlled.

**CI/CD for databases**: Use Terraform in CI/CD pipelines (Cloud Build, GitHub Actions)
to validate (`terraform plan`) and apply database configuration changes automatically.

Combined with Part 1's monitoring and alerting concepts, you now have a complete
operational framework for managing GCP databases in production.

Complete the lab, quiz, and discussion. Module 16 is our exam preparation and capstone.

---

*End of Part 2 Script*
