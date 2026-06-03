# Lab: Module 08 — Managed Databases on GCP

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Lab Overview

In this lab you will provision and interact with two managed database services: Cloud SQL
(PostgreSQL) and Cloud Firestore. You will create instances, load sample data, run queries,
configure backups, and clean up resources to avoid ongoing charges.

**Estimated time**: 60–75 minutes

**Cost estimate**: Under $1.00 USD if completed and cleaned up within the session

---

### Prerequisites

- A GCP project with billing enabled
- Cloud Shell or gcloud CLI installed and authenticated
- The following APIs enabled: Cloud SQL Admin API, Cloud Firestore API

Enable APIs:

```bash
gcloud services enable sqladmin.googleapis.com
gcloud services enable firestore.googleapis.com
```

---

### Part 1: Cloud SQL — PostgreSQL Instance

#### Task 1.1: Create a Cloud SQL Instance

Create a small PostgreSQL instance for this lab. Use the shared-core tier to minimize cost.

```bash
# Set your project (replace with your actual project ID)
gcloud config set project YOUR_PROJECT_ID

# Create a PostgreSQL 15 instance (shared-core for lab use)
gcloud sql instances create lab08-postgres \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=us-central1 \
  --storage-size=10GB \
  --storage-type=SSD \
  --backup-start-time=03:00

# Verify the instance is RUNNABLE
gcloud sql instances describe lab08-postgres \
  --format="value(state)"
```

Expected output: `RUNNABLE`

#### Task 1.2: Create a Database and User

```bash
# Create a database named "inventory"
gcloud sql databases create inventory \
  --instance=lab08-postgres

# Set the root postgres user password
gcloud sql users set-password postgres \
  --instance=lab08-postgres \
  --password=Lab08Password!

# Create an application user
gcloud sql users create appuser \
  --instance=lab08-postgres \
  --password=AppUser123!

# List databases
gcloud sql databases list --instance=lab08-postgres
```

#### Task 1.3: Connect and Create a Table

Use Cloud SQL Auth Proxy to connect securely. In Cloud Shell, the gcloud CLI can also
open a direct connection:

```bash
# Connect directly using gcloud (Cloud Shell only)
gcloud sql connect lab08-postgres \
  --user=postgres \
  --database=inventory
```

Once connected to the psql prompt, run these SQL commands:

```sql
-- Create a products table
CREATE TABLE products (
  product_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  category VARCHAR(50),
  price NUMERIC(10,2),
  stock_qty INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Insert sample data
INSERT INTO products (name, category, price, stock_qty) VALUES
  ('Laptop Pro 15', 'Electronics', 1299.99, 45),
  ('Wireless Mouse', 'Electronics', 29.99, 200),
  ('Office Chair', 'Furniture', 349.00, 30),
  ('USB-C Hub', 'Electronics', 49.99, 150),
  ('Standing Desk', 'Furniture', 599.00, 20);

-- Query the data
SELECT name, category, price
FROM products
ORDER BY price DESC;

-- Exit psql
\q
```

#### Task 1.4: Create a Manual Backup

```bash
# Create an on-demand backup
gcloud sql backups create \
  --instance=lab08-postgres \
  --description="Lab 08 manual backup"

# List backups
gcloud sql backups list --instance=lab08-postgres
```

#### Task 1.5: Export to Cloud Storage

```bash
# Create a Cloud Storage bucket for the export
gsutil mb -l us-central1 gs://YOUR_PROJECT_ID-lab08-exports/

# Export the inventory database to Cloud Storage
gcloud sql export sql lab08-postgres \
  gs://YOUR_PROJECT_ID-lab08-exports/inventory-backup.sql \
  --database=inventory

# Verify the export file exists
gsutil ls gs://YOUR_PROJECT_ID-lab08-exports/
```

---

### Part 2: Cloud Firestore — Document Database

#### Task 2.1: Create a Firestore Database

```bash
# Create a Firestore database in Native mode
gcloud firestore databases create \
  --location=us-central1 \
  --type=firestore-native

# Verify creation
gcloud firestore databases list
```

#### Task 2.2: Add Documents Using gcloud

The gcloud CLI provides basic Firestore document management. Use the Cloud Console for
richer interaction, but practice the CLI commands for the ACE exam.

```bash
# Navigate to the Firestore Console to add documents interactively
# URL: https://console.cloud.google.com/firestore

# Use gcloud to export an existing collection (after populating via console)
gcloud firestore export \
  gs://YOUR_PROJECT_ID-lab08-exports/firestore-backup
```

#### Task 2.3: Explore Firestore in the Console

1. Open the Cloud Console and navigate to **Firestore**.
2. Click **+ Start Collection** and name it `customers`.
3. Add a document with the following fields:

```text
Document ID: cust_001 (auto or manual)
Fields:
  name: "Alice Johnson"  (string)
  email: "alice@example.com"  (string)
  tier: "premium"  (string)
  account_balance: 1500.00  (number)
  active: true  (boolean)
```

4. Add a second document `cust_002` for "Bob Smith".
5. Click on `cust_001` and add a subcollection named `orders`.
6. Add one order document inside the `orders` subcollection:

```text
Fields:
  order_id: "ord_101"  (string)
  amount: 249.99  (number)
  status: "shipped"  (string)
  order_date: (timestamp — use current time)
```

#### Task 2.4: Run Queries in the Firestore Console

1. In the Firestore Console, use the **Query builder** panel.
2. Filter the `customers` collection where `tier == "premium"`.
3. Observe that only `cust_001` (Alice) appears.
4. Add a second filter: `account_balance > 1000`.
5. Note the composite index warning.

Firestore requires a composite index for multi-field queries on different fields.

---

### Part 3: Lab Reflection Questions

Answer these questions in your lab submission document:

1. What availability type did you use for the Cloud SQL instance, and what does that mean
   for failover behavior?
2. Why does Cloud SQL Auth Proxy improve security compared to connecting over public IP
   with authorized networks?
3. What is the difference between the Cloud SQL export you created and a Cloud SQL backup?
4. What Firestore mode did you create, and what feature does it unlock that Datastore mode
   does not provide?
5. Why does a multi-field Firestore query require a composite index?
6. If this inventory system needed to scale globally with 99.999% availability, which GCP
   database service would you recommend instead of Cloud SQL? Justify your answer.

---

### Part 4: Cleanup — Delete All Resources

Always delete lab resources to avoid unexpected charges.

```bash
# Delete the Cloud SQL instance (this also deletes all databases and backups)
gcloud sql instances delete lab08-postgres --quiet

# Delete the Cloud Storage bucket and all contents
gsutil rm -r gs://YOUR_PROJECT_ID-lab08-exports/

# Firestore databases cannot be deleted via gcloud in all configurations
# Use the Console: Firestore > Settings > Delete Database
# Or use the REST API for full deletion
```

---

### Submission Checklist

Before submitting, confirm you have completed all items:

- Cloud SQL PostgreSQL instance created and verified RUNNABLE
- Database and application user created
- Products table created with 5 rows of sample data
- Manual backup created
- Export to Cloud Storage completed
- Firestore database created in Native mode
- At least 2 customer documents created in Firestore
- Subcollection with one order document added
- All 6 reflection questions answered in your submission document
- All resources deleted (Cloud SQL instance, GCS bucket)

---

### Grading Rubric

| Task | Points |
|---|---|
| Cloud SQL instance created with correct settings | 15 |
| Database, user, and table created with sample data | 20 |
| Manual backup and GCS export completed | 15 |
| Firestore database in Native mode created | 10 |
| Firestore documents and subcollection created | 15 |
| Reflection questions answered completely | 20 |
| All resources cleaned up | 5 |
| **Total** | **100** |
