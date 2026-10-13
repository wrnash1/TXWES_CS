# Video Script: Module 06 — PostgreSQL Administration (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back to CIS-4327. I am Professor Nash, and this is Module 06: PostgreSQL Administration.

PostgreSQL is the engine behind Cloud SQL for PostgreSQL on Google Cloud. If you are preparing for the Google Cloud Professional Database Engineer exam, you need to be comfortable with how Postgres is installed, configured, secured, and maintained. This module covers exactly that.

We split this module into two parts. In Part 1 we cover concepts and architecture — what PostgreSQL is, how its configuration files control the server, how roles and privileges work, and what tablespaces are. In Part 2 we get hands-on with VACUUM, pg_stat monitoring views, and PgBouncer connection pooling.

Let's start with the big picture.

---

## Section 1 — What Is PostgreSQL?

PostgreSQL is an open-source object-relational database system that has been in active development since 1986. It is ACID-compliant, standards-compliant with SQL:2016, and extensible — you can add custom data types, operators, and even procedural languages.

Here are the key architectural components you need to know.

**The postmaster process** is the parent process that starts when you launch PostgreSQL. It listens for incoming connections and forks a new backend process for each client connection. This is called the process-per-connection model.

**Backend processes** execute queries on behalf of clients. Each connection gets its own dedicated backend process, which is why connection count management matters so much.

**Shared memory** — specifically the shared buffer pool — is where PostgreSQL caches data pages. This is controlled by the `shared_buffers` parameter. For a dedicated database server, set shared_buffers to 25% of total RAM.

**The Write-Ahead Log, or WAL** — WAL is fundamental to PostgreSQL durability and replication. Every change is first written to the WAL before it is applied to the actual data files. This guarantees that even if the server crashes, the database can replay the WAL to recover to a consistent state.

**Background processes** — PostgreSQL has several background workers you should know:

- The **checkpointer** flushes dirty pages from shared_buffers to disk at regular intervals.
- The **background writer** proactively writes dirty pages to reduce checkpoint spikes.
- The **autovacuum launcher** manages table bloat by reclaiming dead tuple space.
- The **WAL writer** flushes WAL buffers to disk.
- The **stats collector** gathers query and object statistics used by the query planner.

Understanding these processes is critical because they map directly to performance parameters you will tune in postgresql.conf.

---

## Section 2 — Installation Overview

On a Linux system — and the Google Cloud Certification exam assumes Linux — PostgreSQL installation typically looks like this.

For Ubuntu or Debian-based systems:

```bash
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
```

After installation, the postgres system user is created automatically. The PostgreSQL data directory — called PGDATA — is located at `/var/lib/postgresql/<version>/main` on Debian-based systems.

The **initdb** utility initializes the data cluster. On most package installations, initdb runs automatically. It creates the PGDATA directory structure, generates the initial system catalogs, and creates the default postgres superuser role.

**Service management** on systemd-based systems:

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql
```

On Google Cloud, when you use Cloud SQL with PostgreSQL, you do not manage these processes directly — Google handles the operating system layer. But the configuration parameters inside postgresql.conf still apply, and you set them through the Cloud SQL console or gcloud CLI. That is why understanding the parameters themselves is so important.

---

## Section 3 — postgresql.conf Deep Dive

The `postgresql.conf` file is the primary configuration file for a PostgreSQL instance. Every major behavioral parameter lives here. Let me walk through the most important categories.

### Connection Parameters

```ini
listen_addresses = '*'
port = 5432
max_connections = 100
```

`listen_addresses` controls which network interfaces PostgreSQL accepts connections on. Setting it to `'*'` means all interfaces. In production, bind only to specific IPs.

`max_connections` is one of the most consequential settings. Every connection consumes memory — roughly 5 to 10 MB per backend process. If you set max_connections too high and all connections run queries simultaneously, you can exhaust RAM. This is exactly why PgBouncer connection pooling exists.

### Memory Parameters

```ini
shared_buffers = 256MB
work_mem = 4MB
maintenance_work_mem = 64MB
effective_cache_size = 4GB
```

`shared_buffers` is the size of PostgreSQL's in-memory page cache. Increasing this reduces disk I/O. Start at 25% of RAM.

`work_mem` is the memory allocated per sort or hash operation per query node. A complex query can have many sort nodes, so a single connection can use many multiples of work_mem. Be conservative here to avoid out-of-memory conditions under concurrent load.

`maintenance_work_mem` is used by VACUUM, CREATE INDEX, and REINDEX. You can set it higher temporarily for maintenance operations.

`effective_cache_size` tells the query planner how much memory it can expect for caching, including OS file system cache. This does not allocate memory — it is a planner hint. Set it to about 75% of total RAM.

### WAL Parameters

```ini
wal_level = replica
max_wal_senders = 10
wal_keep_size = 1GB
```

`wal_level` determines how much information is written to the WAL. For streaming replication you need at least `replica`. For logical replication or Change Data Capture, you need `logical`.

`max_wal_senders` is the number of simultaneous WAL streaming connections — one per standby server plus any backup tools.

### Checkpoint Parameters

```ini
checkpoint_completion_target = 0.9
checkpoint_timeout = 5min
```

`checkpoint_completion_target` spreads the checkpoint write work across 90% of the checkpoint interval, reducing I/O spikes.

---

## Section 4 — pg_hba.conf — Host-Based Authentication

`pg_hba.conf` is the access control file for PostgreSQL. HBA stands for host-based authentication. Every incoming connection attempt is matched against entries in this file from top to bottom, and the first matching rule applies.

The format of each line is:

```text
TYPE  DATABASE  USER  ADDRESS  METHOD
```

Here are examples:

```text
# Allow local OS-user connections without password
local   all             all                                     peer

# Allow password connections from the application server subnet
host    appdb           appuser         10.0.1.0/24            scram-sha-256

# Allow replication connections from standby servers
host    replication     replicator      10.0.2.10/32           scram-sha-256
```

**Authentication methods you must know:**

- `trust` — accepts connection with no authentication. Use only for local Unix socket connections in tightly controlled environments.
- `peer` — uses the OS username. The database user must match the OS user. Only works for local connections.
- `md5` — MD5-hashed password. Supported widely but considered weaker.
- `scram-sha-256` — modern strong password hashing. Recommended for all network connections.
- `reject` — explicitly denies the connection.

After editing pg_hba.conf, reload configuration without restarting:

```bash
sudo systemctl reload postgresql
```

Or from inside a psql session:

```sql
SELECT pg_reload_conf();
```

---

## Section 5 — Roles and Privileges

PostgreSQL uses a unified concept called **roles** for both users and groups. A role that can log in is essentially a user. A role without login is essentially a group.

### Creating Roles

```sql
-- Create a login role (user)
CREATE ROLE appuser WITH LOGIN PASSWORD 'SecurePass123!';

-- Create a group role (no login)
CREATE ROLE readonly_group;

-- Grant group membership
GRANT readonly_group TO appuser;
```

### System-Level Role Attributes

```sql
-- Superuser
CREATE ROLE dba_admin WITH SUPERUSER LOGIN PASSWORD 'StrongPass!';

-- Create database privilege
CREATE ROLE dev_user WITH CREATEDB LOGIN PASSWORD 'DevPass!';

-- Replication role
CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'ReplPass!';
```

**Superuser bypasses all privilege checks.** Use it sparingly. On Google Cloud SQL, the default postgres user has limited superuser capabilities — some system-level operations are blocked for security.

### Object Privileges

```sql
-- Grant SELECT on a table
GRANT SELECT ON TABLE orders TO readonly_group;

-- Grant all DML privileges
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE orders TO appuser;

-- Grant privileges on all tables in a schema
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_group;

-- Grant future tables automatically
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO readonly_group;
```

The principle of least privilege applies here. Application users should never be superusers. Read-only reporting users should only have SELECT.

### Schema-Level Control

```sql
-- Create a schema and grant usage
CREATE SCHEMA analytics;
GRANT USAGE ON SCHEMA analytics TO reporting_role;
GRANT SELECT ON ALL TABLES IN SCHEMA analytics TO reporting_role;
```

Schemas provide a namespace boundary — they are the first line of defense for data isolation within a single database.

---

## Section 6 — Tablespaces

A **tablespace** in PostgreSQL maps a logical name to a physical directory on disk. By default, all objects are stored in the `pg_default` tablespace. There is also `pg_global` for system catalog objects shared across the cluster.

Why create custom tablespaces?

- **Separate fast and slow storage**: Put frequently accessed tables on SSD-backed storage and archives on cheaper spinning disk.
- **Isolate large objects**: Move large tables or indexes to a separate mount point to prevent filling the OS disk.

```sql
-- Create a tablespace pointing to a separate disk
CREATE TABLESPACE fast_storage LOCATION '/mnt/ssd_data';

-- Create a table in a specific tablespace
CREATE TABLE events (
    event_id BIGSERIAL PRIMARY KEY,
    event_ts TIMESTAMPTZ NOT NULL,
    payload JSONB
) TABLESPACE fast_storage;

-- Move an existing table to a different tablespace
ALTER TABLE events SET TABLESPACE fast_storage;
```

On Cloud SQL, tablespace management is abstracted — Cloud SQL does not expose the underlying filesystem. But the concept is tested on the certification exam in the context of understanding Postgres internals.

---

## Section 7 — Exam Relevance and Summary

Let me close Part 1 with what the Google Cloud Database Engineer exam tests about PostgreSQL.

**High-frequency exam topics from this section:**

- The role of WAL in durability and replication
- What `wal_level = logical` enables versus `replica`
- pg_hba.conf authentication methods — especially `scram-sha-256` vs `trust`
- Role attribute differences: SUPERUSER, CREATEDB, REPLICATION
- What `shared_buffers` controls and how to size it

**Common exam trap:** The exam may ask which pg_hba.conf method is most secure for network connections. The answer is `scram-sha-256`, not `md5`.

**Another common trap:** `effective_cache_size` does not allocate memory — it is a planner hint. Students frequently confuse it with `shared_buffers`.

---

## Closing

That wraps up Part 1 of Module 06. You now understand PostgreSQL's architecture, its two main configuration files, role-based access control, and tablespaces.

In Part 2, we shift to hands-on content — VACUUM, ANALYZE, pg_stat monitoring views, and PgBouncer connection pooling. Those topics appear heavily in both the lab and the certification exam.

See you in Part 2.
