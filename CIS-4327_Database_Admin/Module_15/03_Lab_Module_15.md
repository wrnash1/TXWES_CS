# Lab Activity: Module 15 — Database Automation and Monitoring

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Lab Overview

**Title**: Cloud SQL Monitoring, Alerting, and Terraform Provisioning

**Estimated Time**: 90 minutes

**Difficulty**: Intermediate

In this lab you will provision a Cloud SQL for PostgreSQL instance using Terraform,
configure Cloud Monitoring alerts for key metrics, generate load to trigger alerts,
test HA failover, and measure recovery time. This lab simulates the operational tasks
of a database reliability engineer.

---

## Prerequisites

- Active GCP project with billing enabled
- Cloud SQL Admin API, Cloud Monitoring API, and Compute Engine API enabled
- Cloud Shell access
- Terraform 1.5+ installed (available in Cloud Shell by default)
- Owner or Cloud SQL Admin + Monitoring Admin roles

---

## Lab Objectives

By the end of this lab, you will be able to:

1. Provision a Cloud SQL HA instance using Terraform
2. Create CPU and connection count alerting policies in Cloud Monitoring
3. Use Cloud SQL Insights to identify a slow query
4. Trigger and measure a Cloud SQL HA failover
5. Demonstrate Terraform state management with GCS backend

---

## Part 1 — Terraform Setup and State Backend

### Step 1.1 — Create a GCS Bucket for Terraform State

```bash
export PROJECT_ID=$(gcloud config get-value project)
export STATE_BUCKET="${PROJECT_ID}-tf-state"

gsutil mb -l us-central1 gs://${STATE_BUCKET}
gsutil versioning set on gs://${STATE_BUCKET}
```

### Step 1.2 — Create Terraform Configuration

Create a working directory and write the Terraform files:

```bash
mkdir -p ~/lab15-terraform && cd ~/lab15-terraform
```

Create `backend.tf`:

```hcl
terraform {
  backend "gcs" {
    bucket = "PROJECT_ID-tf-state"
    prefix = "lab15"
  }
}
```

Create `main.tf`:

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

resource "google_sql_database_instance" "lab15" {
  name                = "lab15-pg-instance"
  database_version    = "POSTGRES_15"
  region              = var.region
  deletion_protection = false

  settings {
    tier              = "db-g1-small"
    availability_type = "REGIONAL"

    backup_configuration {
      enabled                        = true
      start_time                     = "03:00"
      point_in_time_recovery_enabled = true
      transaction_log_retention_days = 3
      retained_backups               = 7
    }

    database_flags {
      name  = "cloudsql.iam_authentication"
      value = "on"
    }

    insights_config {
      query_insights_enabled  = true
      query_string_length     = 512
      record_application_tags = false
    }

    ip_configuration {
      ipv4_enabled = true
      authorized_networks {
        name  = "cloud-shell"
        value = "0.0.0.0/0"
      }
    }
  }
}

resource "google_sql_database" "lab15_db" {
  name     = "lab15db"
  instance = google_sql_database_instance.lab15.name
}

resource "google_sql_user" "lab15_user" {
  name     = "lab15_admin"
  instance = google_sql_database_instance.lab15.name
  password = var.db_password
}

output "instance_connection_name" {
  value = google_sql_database_instance.lab15.connection_name
}

output "instance_ip" {
  value = google_sql_database_instance.lab15.public_ip_address
}
```

Create `variables.tf`:

```hcl
variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "db_password" {
  description = "Database admin password"
  type        = string
  sensitive   = true
}
```

Create `terraform.tfvars` (replace PROJECT_ID with your actual project):

```hcl
project_id  = "YOUR_PROJECT_ID"
region      = "us-central1"
db_password = "Lab15Str0ng!Pass"
```

### Step 1.3 — Initialize and Apply Terraform

Replace `PROJECT_ID` in `backend.tf` with your actual project ID, then:

```bash
cd ~/lab15-terraform

# Replace placeholder in backend.tf
sed -i "s/PROJECT_ID/${PROJECT_ID}/g" backend.tf

terraform init
terraform plan
terraform apply -auto-approve
```

Wait 5–8 minutes for the Cloud SQL instance to be created.

**Lab Question 1**: What did `terraform plan` show before `apply`? How many
resources were created?

---

## Part 2 — Cloud Monitoring Alerts

### Step 2.1 — Create a CPU Utilization Alert

In the GCP Console, navigate to Monitoring → Alerting → Create Policy.

Configure the following alert:

- **Metric**: `cloudsql.googleapis.com/database/cpu/utilization`
- **Filter**: `database_id = "PROJECT:lab15-pg-instance"`
- **Condition threshold**: > 0.60 (60%) for 2 minutes
- **Notification channel**: Your email address
- **Alert name**: "Lab15 — Cloud SQL CPU High"
- **Documentation**: "CPU exceeded 60%. Check for long-running queries."

### Step 2.2 — Create a Connections Alert

Create a second alert:

- **Metric**: `cloudsql.googleapis.com/database/postgresql/num_backends`
- **Filter**: `database_id = "PROJECT:lab15-pg-instance"`
- **Condition threshold**: > 20 backends for 1 minute
- **Alert name**: "Lab15 — Cloud SQL Connections High"

### Step 2.3 — Generate Load to Trigger CPU Alert

Install pgbench (PostgreSQL benchmarking tool) in Cloud Shell:

```bash
sudo apt-get install -y postgresql-client postgresql
```

Get the instance IP from Terraform output:

```bash
cd ~/lab15-terraform
export DB_IP=$(terraform output -raw instance_ip)
```

Initialize pgbench:

```bash
PGPASSWORD="Lab15Str0ng!Pass" pgbench \
  -h $DB_IP -U lab15_admin -d lab15db \
  --initialize --scale=10
```

Run a load test for 3 minutes:

```bash
PGPASSWORD="Lab15Str0ng!Pass" pgbench \
  -h $DB_IP -U lab15_admin -d lab15db \
  --time=180 --client=10 --jobs=4 \
  --report-latency
```

Monitor the CPU metric in Cloud Monitoring during the load test.

**Lab Question 2**: Did the CPU alert fire? What was the peak CPU utilization?
How long after crossing the threshold did you receive the alert notification?

---

## Part 3 — Cloud SQL Insights

### Step 3.1 — Create a Slow Query

Connect to the database and run a deliberately slow query:

```bash
PGPASSWORD="Lab15Str0ng!Pass" psql \
  -h $DB_IP -U lab15_admin -d lab15db
```

Inside psql, run:

```sql
-- Create a table with a missing index to produce a slow query
CREATE TABLE IF NOT EXISTS slow_test AS
SELECT
  generate_series(1, 1000000) AS id,
  md5(random()::text)         AS data,
  (random() * 100)::int       AS category;

-- Run a slow query (sequential scan on a large table)
EXPLAIN ANALYZE
SELECT category, COUNT(*), AVG(LENGTH(data))
FROM slow_test
WHERE data LIKE 'a%'
GROUP BY category
ORDER BY category;

\q
```

### Step 3.2 — View the Query in Cloud SQL Insights

In the GCP Console, navigate to Cloud SQL → lab15-pg-instance → Insights.

Under "Top queries by CPU time," find the slow query you just ran.

**Lab Question 3**: What does Insights show as the query's average execution time?
What does the execution plan analysis reveal about why it is slow?
What index would you create to speed it up?

---

## Part 4 — HA Failover Test

### Step 4.1 — Record Pre-Failover Metrics

In Cloud Monitoring, note the current baseline:

- CPU utilization: ____________________
- Number of backends: ____________________

### Step 4.2 — Trigger Failover

```bash
cd ~/lab15-terraform

echo "Failover started at: $(date)"
gcloud sql instances failover lab15-pg-instance

echo "Failover command issued at: $(date)"
```

### Step 4.3 — Measure Recovery Time

Poll the instance status until it returns to RUNNABLE:

```bash
start_time=$(date +%s)
while true; do
  STATUS=$(gcloud sql instances describe lab15-pg-instance \
    --format="value(state)")
  echo "$(date): Status = $STATUS"
  if [ "$STATUS" = "RUNNABLE" ]; then
    end_time=$(date +%s)
    echo "Instance recovered. Total time: $((end_time - start_time)) seconds"
    break
  fi
  sleep 5
done
```

**Lab Question 4**: How many seconds did it take for the instance to return to
RUNNABLE state after the failover command was issued?

### Step 4.4 — Verify Reconnection

After the instance recovers, reconnect to verify connectivity:

```bash
PGPASSWORD="Lab15Str0ng!Pass" psql \
  -h $DB_IP -U lab15_admin -d lab15db \
  -c "SELECT NOW(), 'Post-failover connection successful';"
```

---

## Part 5 — Terraform Destroy and State Inspection

### Step 5.1 — Inspect Terraform State

```bash
cd ~/lab15-terraform
terraform state list
terraform state show google_sql_database_instance.lab15
```

**Lab Question 5**: What fields are stored in the Terraform state for the Cloud SQL
instance? Where is this state stored, and why is that location important?

### Step 5.2 — Destroy Lab Resources

```bash
terraform destroy -auto-approve
```

Verify the instance is deleted:

```bash
gcloud sql instances list
```

Also delete the state bucket:

```bash
gsutil rm -r gs://${STATE_BUCKET}
```

---

## Lab Deliverables

Submit a document containing:

1. Screenshot of the `terraform apply` output showing resources created
2. Screenshot of the CPU alert firing (or monitoring graph showing CPU spike)
3. Screenshot of the Cloud SQL Insights query detail for the slow query
4. Failover recovery time measurement from Step 4.3
5. Answers to Lab Questions 1 through 5

---

## Grading Rubric

| Component | Points |
|---|---|
| Terraform configuration correct and applied successfully | 25 |
| CPU and connections alerts created in Cloud Monitoring | 20 |
| Load test run and CPU metrics captured | 15 |
| Slow query created and analyzed in Insights | 15 |
| Failover triggered and recovery time measured | 15 |
| Lab Questions 1–5 answered | 10 |
| **Total** | **100** |

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Log-Based Metric for Long-Running Transactions

1. In Cloud Logging, create a log-based metric that counts PostgreSQL log entries matching long-running transaction warnings. First, generate a long transaction on your Cloud SQL instance:

   ```sql
   BEGIN;
   SELECT pg_sleep(120);
   -- Leave this transaction open for 2 minutes without committing
   ```

2. In Cloud Logging, filter for logs from your Cloud SQL instance and find the lock/transaction warning log entries. Note the log entry format and the relevant field.

3. Create a log-based metric named `cloudsql_long_transactions` using the following filter pattern (adjust the resource labels to match your instance):

   ```
   resource.type="cloudsql_database"
   resource.labels.database_id="YOUR_PROJECT:YOUR_INSTANCE"
   textPayload=~"duration:.*ms"
   ```

4. Create a Cloud Monitoring alerting policy that fires when `cloudsql_long_transactions` exceeds 5 occurrences in 5 minutes, and send a notification to your email.

### Challenge 2: Terraform Drift Detection and Remediation

1. Using your existing Terraform-managed Cloud SQL instance, manually add a database flag through the Cloud Console: set `log_min_duration_statement = 1000` (log queries slower than 1 second).

2. Run `terraform plan` and capture the output showing the planned change. Confirm Terraform detects the drift and plans to revert the manually added flag.

3. Add `log_min_duration_statement = 1000` to your Terraform `database_flags` block:

   ```hcl
   database_flags {
     name  = "log_min_duration_statement"
     value = "1000"
   }
   ```

4. Run `terraform apply` and confirm the flag is now managed by Terraform. Then run `terraform plan` again and confirm the output shows `No changes` — the configuration is now in sync.

### Reflection Questions

1. In Challenge 1, you built a log-based metric from PostgreSQL log entries. Explain the architectural difference between this approach and using `pg_stat_statements` for detecting long-running queries. Which approach would you choose for a production alerting system and why?
2. In Challenge 2, you experienced configuration drift where a manual change conflicted with Terraform-managed state. In a team environment where multiple DBAs have console access, what policy and technical controls would you implement to prevent unauthorized manual changes from creating drift in Terraform-managed infrastructure?

---

Module 15 Lab — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
