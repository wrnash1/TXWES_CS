# Lab Activity: Module 06 — PostgreSQL Administration

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Lab Overview

In this lab you will administer a PostgreSQL instance from installation through production-ready configuration. You will create roles with appropriate privileges, configure host-based authentication, analyze table health using pg_stat views, run VACUUM operations, and configure PgBouncer connection pooling.

**Estimated Time:** 90 minutes

**Prerequisites:**

- Ubuntu 22.04 LTS VM (Google Cloud Compute Engine e2-medium or equivalent)
- sudo privileges
- Basic familiarity with psql from Module 05

---

## Part 1 — Install and Initialize PostgreSQL

### Step 1.1 — Install PostgreSQL 15

```bash
sudo apt-get update
sudo apt-get install -y postgresql-15 postgresql-contrib-15

# Verify installation
psql --version
sudo systemctl status postgresql
```

### Step 1.2 — Explore the Data Directory

```bash
sudo -u postgres ls /var/lib/postgresql/15/main/
sudo -u postgres ls /var/lib/postgresql/15/main/pg_wal/
```

Identify the following directories and record their purpose in your lab notebook:

- `base/` — per-database object files
- `pg_wal/` — Write-Ahead Log segments
- `global/` — cluster-wide system catalogs
- `pg_tblspc/` — symlinks to tablespace directories

### Step 1.3 — Connect as the postgres Superuser

```bash
sudo -u postgres psql
```

Run a quick sanity check:

```sql
SELECT version();
SELECT current_user;
\l
\q
```

---

## Part 2 — Configure postgresql.conf

### Step 2.1 — Edit Configuration

```bash
sudo nano /etc/postgresql/15/main/postgresql.conf
```

Change or add the following parameters:

```ini
listen_addresses = 'localhost'
max_connections = 50
shared_buffers = 128MB
work_mem = 8MB
maintenance_work_mem = 64MB
effective_cache_size = 512MB
random_page_cost = 1.1
checkpoint_completion_target = 0.9
wal_level = replica
log_min_duration_statement = 500
log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '
```

### Step 2.2 — Reload and Verify

```bash
sudo systemctl reload postgresql
```

```sql
sudo -u postgres psql -c "SELECT name, setting, unit FROM pg_settings WHERE name IN ('max_connections','shared_buffers','work_mem','random_page_cost');"
```

**Lab Question 2.1:** What is the unit for `shared_buffers` as reported by pg_settings? Why does this differ from the value you set in postgresql.conf?

---

## Part 3 — Configure pg_hba.conf

### Step 3.1 — Edit the HBA File

```bash
sudo nano /etc/postgresql/15/main/pg_hba.conf
```

Replace the default content below the comments with:

```text
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             postgres                                peer
local   all             all                                     scram-sha-256
host    labdb           labapp          127.0.0.1/32            scram-sha-256
host    all             all             0.0.0.0/0               reject
```

### Step 3.2 — Reload and Test

```bash
sudo systemctl reload postgresql
```

```sql
sudo -u postgres psql -c "SELECT pg_reload_conf();"
```

**Lab Question 3.1:** Why does the `local all postgres peer` rule need to appear before the `local all all scram-sha-256` rule?

---

## Part 4 — Create Roles and a Lab Database

### Step 4.1 — Create the Database and Roles

```bash
sudo -u postgres psql
```

```sql
-- Create the lab database
CREATE DATABASE labdb;

-- Create group roles
CREATE ROLE lab_readonly;
CREATE ROLE lab_readwrite;

-- Create login users
CREATE ROLE labapp WITH LOGIN PASSWORD 'AppPass2024!';
CREATE ROLE labreport WITH LOGIN PASSWORD 'ReportPass2024!';

-- Assign to groups
GRANT lab_readwrite TO labapp;
GRANT lab_readonly TO labreport;

\c labdb
```

### Step 4.2 — Create Tables and Grant Privileges

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2),
    stock_qty INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE order_events (
    event_id BIGSERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    event_type VARCHAR(20),
    event_ts TIMESTAMPTZ DEFAULT now()
);

-- Grant schema usage
GRANT USAGE ON SCHEMA public TO lab_readonly, lab_readwrite;

-- Grant to read-only group
GRANT SELECT ON ALL TABLES IN SCHEMA public TO lab_readonly;

-- Grant to read-write group
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO lab_readwrite;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO lab_readwrite;

-- Apply to future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO lab_readonly;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO lab_readwrite;
```

### Step 4.3 — Test Role Access

```bash
# Test labapp (read-write)
psql -h 127.0.0.1 -U labapp -d labdb -c "INSERT INTO products (product_name, price, stock_qty) VALUES ('Widget A', 9.99, 100);"

# Test labreport (read-only) -- should succeed
psql -h 127.0.0.1 -U labreport -d labdb -c "SELECT * FROM products;"

# Test labreport INSERT -- should fail with permission denied
psql -h 127.0.0.1 -U labreport -d labdb -c "INSERT INTO products (product_name, price) VALUES ('Unauthorized', 1.00);"
```

**Lab Question 4.1:** What error message do you receive when labreport attempts the INSERT? Record the exact SQLSTATE code.

---

## Part 5 — VACUUM and Table Statistics

### Step 5.1 — Generate Dead Tuples

Insert and update rows to create dead tuple bloat:

```sql
\c labdb

-- Insert seed data
INSERT INTO products (product_name, price, stock_qty)
SELECT 'Product ' || i, round((random() * 100)::numeric, 2), (random() * 1000)::int
FROM generate_series(1, 10000) AS s(i);

-- Update all rows multiple times to create dead tuples
UPDATE products SET stock_qty = stock_qty + 1;
UPDATE products SET stock_qty = stock_qty + 1;
UPDATE products SET stock_qty = stock_qty + 1;
```

### Step 5.2 — Check Dead Tuple Count Before VACUUM

```sql
SELECT relname, n_live_tup, n_dead_tup,
       round(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 1) AS dead_pct,
       last_autovacuum, last_vacuum
FROM pg_stat_user_tables
WHERE relname = 'products';
```

Record the `n_dead_tup` value.

### Step 5.3 — Run VACUUM ANALYZE

```sql
VACUUM ANALYZE products;

-- Check again
SELECT relname, n_live_tup, n_dead_tup,
       last_vacuum
FROM pg_stat_user_tables
WHERE relname = 'products';
```

**Lab Question 5.1:** What happened to `n_dead_tup` after running VACUUM? Did the table size change on disk? Why or why not?

### Step 5.4 — Monitor Transaction ID Age

```sql
SELECT datname, age(datfrozenxid) AS xid_age
FROM pg_database
ORDER BY xid_age DESC;
```

**Lab Question 5.2:** What is the current XID age for `labdb`? At what age should you begin to be concerned?

---

## Part 6 — pg_stat Monitoring

### Step 6.1 — Simulate Active Sessions

Open a second terminal and run a long query:

```bash
sudo -u postgres psql -d labdb -c "SELECT pg_sleep(60);" &
```

In the first terminal, monitor from psql:

```sql
SELECT pid, usename, state, now() - query_start AS runtime, query
FROM pg_stat_activity
WHERE state != 'idle';
```

### Step 6.2 — Install pg_stat_statements

```sql
\c labdb

-- The extension was included with postgresql-contrib
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

Then add to postgresql.conf and restart:

```bash
sudo bash -c "echo \"shared_preload_libraries = 'pg_stat_statements'\" >> /etc/postgresql/15/main/postgresql.conf"
sudo systemctl restart postgresql
```

Run some queries and check statistics:

```sql
\c labdb

SELECT * FROM products WHERE product_id < 100;
SELECT product_name, price FROM products ORDER BY price DESC LIMIT 10;

SELECT query, calls, total_exec_time, mean_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 5;
```

---

## Part 7 — PgBouncer Setup

### Step 7.1 — Install PgBouncer

```bash
sudo apt-get install -y pgbouncer
```

### Step 7.2 — Configure PgBouncer

```bash
sudo nano /etc/pgbouncer/pgbouncer.ini
```

Replace the content with:

```ini
[databases]
labdb = host=127.0.0.1 port=5432 dbname=labdb

[pgbouncer]
listen_port = 6432
listen_addr = 127.0.0.1
auth_type = scram-sha-256
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction
max_client_conn = 100
default_pool_size = 5
min_pool_size = 1
reserve_pool_size = 2
log_connections = 1
log_disconnections = 1
stats_period = 60
```

### Step 7.3 — Create the User List

```bash
# Generate scram-sha-256 hash for the application user
sudo -u postgres psql -d labdb -t -c "SELECT concat('\"labapp\" \"', passwd, '\"') FROM pg_shadow WHERE usename='labapp';" | sudo tee /etc/pgbouncer/userlist.txt
```

### Step 7.4 — Start and Test PgBouncer

```bash
sudo systemctl enable pgbouncer
sudo systemctl start pgbouncer
sudo systemctl status pgbouncer

# Connect through PgBouncer instead of directly to PostgreSQL
psql -h 127.0.0.1 -p 6432 -U labapp -d labdb -c "SELECT count(*) FROM products;"
```

### Step 7.5 — Check Pool Statistics

```bash
psql -h 127.0.0.1 -p 6432 -U labapp pgbouncer -c "SHOW POOLS;"
psql -h 127.0.0.1 -p 6432 -U labapp pgbouncer -c "SHOW STATS;"
```

**Lab Question 7.1:** In the SHOW POOLS output, what do the `cl_active`, `sv_active`, and `sv_idle` columns represent?

---

## Lab Deliverables

Submit a PDF containing:

1. Screenshots of each step's output (pg_stat_user_tables before/after VACUUM, pg_stat_activity output, SHOW POOLS output).

2. Written answers to all five Lab Questions.

3. A copy of your final `pgbouncer.ini` and `pg_hba.conf` files.

4. A brief paragraph (5–8 sentences) explaining why PgBouncer transaction pooling is incompatible with `LISTEN/NOTIFY` and what you would use instead if your application requires notifications.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1–2: Installation and configuration correct | 15 |
| Part 3: pg_hba.conf with correct methods | 15 |
| Part 4: Roles and privileges working as expected | 20 |
| Part 5: VACUUM demonstration with before/after data | 20 |
| Part 6: pg_stat_statements query results captured | 15 |
| Part 7: PgBouncer running with SHOW POOLS output | 15 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Row-Level Security for a Multi-Tenant Schema

Implement a multi-tenant data isolation policy using PostgreSQL Row-Level Security.

```sql
-- Create a multi-tenant orders table
CREATE TABLE tenant_orders (
    order_id   SERIAL PRIMARY KEY,
    tenant_id  INTEGER NOT NULL,
    item_name  VARCHAR(200) NOT NULL,
    amount     NUMERIC(10,2) NOT NULL
);

-- Insert sample data for two tenants
INSERT INTO tenant_orders (tenant_id, item_name, amount) VALUES
    (1, 'Widget A', 49.99),
    (1, 'Widget B', 19.99),
    (2, 'Gadget X', 99.99),
    (2, 'Gadget Y', 149.99);

-- Create two tenant application roles
CREATE ROLE tenant1_app WITH LOGIN PASSWORD 'T1pass!';
CREATE ROLE tenant2_app WITH LOGIN PASSWORD 'T2pass!';

GRANT SELECT ON tenant_orders TO tenant1_app, tenant2_app;
```

Then complete the following steps:

1. Enable RLS and create a policy that uses `current_setting('app.tenant_id')::INTEGER` to restrict each role to its own tenant rows. Apply the policy and verify that connecting as `tenant1_app` with `SET app.tenant_id = '1'` returns only tenant 1 rows while `SELECT COUNT(*)` as `tenant2_app` with `SET app.tenant_id = '2'` returns only tenant 2 rows.
2. Attempt to query `tenant_orders` as `tenant1_app` without setting `app.tenant_id` first. Record the result and explain whether RLS silently returns zero rows or raises an error.
3. Write a paragraph explaining the security implication if a developer accidentally calls `SET app.tenant_id = '0'` and what additional application-layer guard should be implemented.

### Challenge 2: Autovacuum Tuning for a High-Churn Table

Simulate a high-churn workload and measure its effect on dead tuple accumulation, then tune autovacuum to respond faster.

Run the following to create churn:

```sql
CREATE TABLE churn_test (id SERIAL PRIMARY KEY, val TEXT);
INSERT INTO churn_test (val) SELECT md5(random()::text) FROM generate_series(1, 100000);

-- Simulate repeated updates creating dead tuples
UPDATE churn_test SET val = md5(random()::text);
UPDATE churn_test SET val = md5(random()::text);
UPDATE churn_test SET val = md5(random()::text);
```

Then complete the following steps:

1. Query `pg_stat_user_tables` to record `n_dead_tup` for `churn_test` immediately after the updates. Note whether autovacuum has already run.
2. Override the autovacuum settings to trigger more aggressively, then wait 60–90 seconds for autovacuum to respond:

```sql
ALTER TABLE churn_test SET (
    autovacuum_vacuum_scale_factor = 0.01,
    autovacuum_vacuum_threshold    = 50
);
```

3. Re-query `pg_stat_user_tables` to check `last_autovacuum` and the new `n_dead_tup` value. Capture the before and after values and write a paragraph explaining how `autovacuum_vacuum_scale_factor` and `autovacuum_vacuum_threshold` combine to determine when autovacuum triggers.

### Reflection Questions

1. In Challenge 1, what is the difference between a permissive and a restrictive RLS policy, and in what scenario would you use a restrictive policy in addition to a permissive one on the same table?
2. In Challenge 2, if autovacuum is disabled entirely on a production table to reduce I/O overhead during a bulk load, what operational steps must the DBA take immediately after the load completes to prevent transaction ID wraparound and query plan degradation?
