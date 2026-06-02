# Quiz: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis is provided to reinforce exam-level reasoning.

---

### Question 1

Your team is deploying a Python application on Google Kubernetes Engine that needs to connect to a Cloud SQL for PostgreSQL instance. The security team requires that no database passwords be stored in application environment variables. Which connection approach best meets this requirement?

- A) Use the Cloud SQL Auth Proxy with IAM database authentication via the GKE workload identity.
- B) Use a Public IP connection with an authorized networks entry for the GKE cluster IP range.
- C) Store the database password in a Kubernetes Secret and mount it as an environment variable.
- D) Use Private IP connectivity and hard-code the database password in a config file on the container image.

Correct Answer: A — The Cloud SQL Auth Proxy combined with IAM database authentication (using GKE Workload Identity) allows the application to authenticate to Cloud SQL using its GCP service account identity rather than a password. No password needs to be stored anywhere. This is the documented GCP best practice for Kubernetes-based applications connecting to Cloud SQL.

Distractor analysis: B is incorrect because Public IP with authorized networks still requires a database password; it only controls which source IPs can attempt a connection. C is incorrect because it uses a Kubernetes Secret to store a password — the password still exists in the cluster's secrets store, which violates the requirement. D is incorrect because hard-coding a password in a container image is a critical security vulnerability that violates credential management best practices.

---

### Question 2

A Cloud SQL for MySQL instance is running out of disk space and causing application errors. Automated storage auto-increase was not enabled. What is the fastest way to restore availability?

- A) Patch the instance to enable storage auto-increase; Cloud SQL will immediately allocate additional storage.
- B) Create a new larger instance, export data from the current instance, and import into the new instance.
- C) Delete the oldest backup files from the instance to free up storage space.
- D) Increase the machine type to a higher tier, which also increases available storage.

Correct Answer: A — Enabling storage auto-increase on a running Cloud SQL instance via `gcloud sql instances patch` triggers an immediate storage expansion. This is the fastest path to restoring availability without data migration or downtime. The storage increase is applied online.

Distractor analysis: B is incorrect as the fastest option; export and import is a multi-hour process depending on data volume and would extend the outage significantly. C is incorrect because backup files in Cloud SQL are managed by GCP and are stored in separate GCP-managed storage, not on the instance's own disk; deleting them does not free instance storage. D is incorrect because changing the machine tier does not increase storage; storage and machine type are independently configured.

---

### Question 3

A Cloud SQL for PostgreSQL production instance loses its primary zone due to an infrastructure failure. Approximately how long should the application team expect the database to be unavailable before automatic failover completes, assuming high availability is enabled?

- A) Approximately 60 seconds
- B) Approximately 5 minutes
- C) Less than 1 second (transparent, no interruption)
- D) The database does not recover automatically; manual promotion is required

Correct Answer: A — Cloud SQL HA automatic failover takes approximately 60 seconds. The standby instance in the secondary zone is promoted to primary and the DNS entry is updated. Applications must handle the brief connection interruption with retry logic.

Distractor analysis: B is incorrect because 5 minutes significantly overstates the failover duration for Cloud SQL HA. C is incorrect because Cloud SQL HA does have a brief outage during failover — sub-second transparent failover is a characteristic of Cloud Spanner, not Cloud SQL. D is incorrect because Cloud SQL HA failover is fully automatic when `--availability-type=REGIONAL` is configured; manual intervention is not required.

---

### Question 4

You need to restore a Cloud SQL for PostgreSQL database to its exact state at 3:14:27 PM yesterday after a developer accidentally executed `DELETE FROM orders WHERE 1=1;`. Point-in-time recovery is available. What must have been configured before this event for PITR to be possible?

- A) WAL archiving must have been enabled on the instance before the deletion occurred.
- B) A manual on-demand backup must have been triggered within 15 minutes before the deletion.
- C) The instance must have been running Cloud SQL Enterprise Plus edition.
- D) The database schema must have been exported to Cloud Storage before the deletion.

Correct Answer: A — Point-in-time recovery for PostgreSQL requires WAL (Write-Ahead Log) archiving to be enabled. WAL archiving continuously captures transaction log records that enable recovery to any point within the retention window. This must be enabled before the data loss event — you cannot retroactively enable PITR to recover past a point where logs were not being captured.

Distractor analysis: B is incorrect because a manual backup captures a point-in-time snapshot but does not enable recovery to an arbitrary second; without WAL logs, you can only restore to backup checkpoint times. C is incorrect because PITR is available on both Cloud SQL Enterprise and Enterprise Plus editions; edition tier does not determine PITR availability. D is incorrect because a schema export to Cloud Storage does not capture data; it would not allow row-level recovery.

---

### Question 5

Your organization requires that the Cloud SQL instance for a financial application never be reachable from the public internet. Which configuration achieves this?

- A) Configure the Cloud SQL instance with Private IP only, using Private Services Access on the application's VPC.
- B) Enable the Cloud SQL Auth Proxy on all connecting applications and disable all authorized networks entries.
- C) Set the instance firewall rules to block all inbound traffic from 0.0.0.0/0.
- D) Enable Cloud Armor on the Cloud SQL instance to filter incoming connection attempts.

Correct Answer: A — Configuring Cloud SQL with Private IP only and no public IP address means the instance has no internet-routable endpoint. It is only reachable through the VPC network using Private Services Access peering. This is the documented architecture for isolating Cloud SQL from the public internet.

Distractor analysis: B is incorrect because the Auth Proxy manages authentication and encryption but does not remove the public IP endpoint if one is assigned; the instance would still be reachable from the internet. C is incorrect because Cloud SQL instances are not directly configured with VPC firewall rules; instance-level network access is controlled through Private IP vs. Public IP configuration and authorized networks, not VPC firewall rules. D is incorrect because Cloud Armor is a DDoS protection and WAF service for HTTP(S) Load Balancers; it does not apply to Cloud SQL TCP connections.

---

### Question 6

An application runs batch analytics reports every evening that generate heavy read load on the production Cloud SQL instance. Application transaction response times degrade significantly during the report window. What is the most cost-effective solution?

- A) Create a read replica and direct reporting queries to the replica connection string.
- B) Upgrade the primary instance to a higher machine type with more CPU and RAM.
- C) Enable Cloud SQL Enterprise Plus edition to access the data cache feature.
- D) Export the data to BigQuery every evening and run reports there instead.

Correct Answer: A — A read replica offloads read-heavy reporting queries from the primary instance without requiring a primary instance upgrade. The replica is asynchronously updated and accepts read-only connections. Directing reporting queries to the replica connection string eliminates read contention on the primary.

Distractor analysis: B is incorrect because upgrading the primary machine type is more expensive than a replica and requires a restart, causing downtime. A replica can be added without touching the primary. C is incorrect because the data cache in Enterprise Plus improves in-memory performance for all queries but does not eliminate the I/O contention problem from analytics queries competing with transactional ones. D is incorrect because exporting to BigQuery every evening adds operational complexity and latency; it is the right solution for truly analytical workloads but is disproportionate for a nightly reporting window that can be addressed with a replica.

---

### Question 7

Which Cloud SQL storage configuration change requires creating a new instance rather than patching the existing one?

- A) Decreasing the storage allocation from 500 GB to 200 GB
- B) Increasing the storage allocation from 200 GB to 500 GB
- C) Switching from SSD to HDD storage type on a running instance
- D) Enabling storage auto-increase on a running instance

Correct Answer: A — Cloud SQL storage auto-increase is one-directional. Once storage is expanded, it cannot be reduced on the same instance. Decreasing storage requires creating a new smaller instance, exporting data from the current instance, and importing it into the new one.

Distractor analysis: B is incorrect because increasing storage can be done via `gcloud sql instances patch --storage-size`; no new instance is required. C is incorrect because switching storage type between SSD and HDD can be done by patching the instance, though it requires a restart. D is incorrect because enabling storage auto-increase is a patch operation on the existing instance and takes effect immediately.

---

### Question 8

A development team is testing a new feature on a copy of the production Cloud SQL database. They want an exact snapshot copy as quickly as possible without affecting the production instance. Which Cloud SQL feature is most appropriate?

- A) Clone the production instance using the Cloud SQL clone operation.
- B) Create a read replica and promote it to a standalone instance.
- C) Run `pg_dump` on the production instance and restore it to a new instance.
- D) Use Database Migration Service to copy the production schema to a new instance.

Correct Answer: A — Cloud SQL instance cloning creates an exact copy of the source instance at a specific point in time. The clone is created quickly without generating load on the source instance because it uses a copy-on-write snapshot of the underlying storage. It is the fastest way to get a development copy of a production database.

Distractor analysis: B is incorrect because creating and promoting a replica requires waiting for full replication synchronization and the promotion step; it is slower than cloning and also temporarily affects the replica count. C is incorrect because pg_dump generates a logical backup that must be fully transferred and restored, which is slow for large databases and generates read load on the production instance during the dump. D is incorrect because Database Migration Service is designed for heterogeneous migrations between different database engines or environments; it is not the appropriate tool for creating a quick development copy within the same project.

---

### Question 9

You need to compare Cloud SQL Enterprise and Cloud SQL Enterprise Plus to determine which edition meets a contractual SLA requirement of 99.99% uptime. Which statement is accurate?

- A) Cloud SQL Enterprise Plus provides a 99.99% SLA; Cloud SQL Enterprise provides 99.95% for HA instances.
- B) Both editions provide a 99.99% SLA when high availability is enabled.
- C) Cloud SQL Enterprise provides 99.99% SLA; Enterprise Plus is only relevant for performance, not availability.
- D) Neither edition provides a 99.99% SLA; Cloud Spanner is required for 99.999% availability.

Correct Answer: A — Cloud SQL Enterprise Plus provides a 99.99% SLA for HA instances along with near-zero downtime maintenance windows. Cloud SQL Enterprise provides 99.95% SLA for HA instances. For contractual requirements above 99.95%, Enterprise Plus is required.

Distractor analysis: B is incorrect because Enterprise edition offers 99.95%, not 99.99%, even with HA enabled. C is incorrect because Enterprise Plus provides both higher availability (99.99% SLA) and better I/O performance; it is not relevant only for performance. D is incorrect because Cloud SQL Enterprise Plus does achieve 99.99% SLA; Cloud Spanner provides 99.999% (five nines), which is a separate and higher tier.

---

### Question 10

An application connects to Cloud SQL using the Public IP method with an authorized networks entry of `203.0.113.0/24`. The security team audits the configuration and classifies it as a risk. Which two changes would reduce the attack surface while maintaining application connectivity?

- A) Switch to Private IP connectivity and replace the authorized networks entry with the VPC internal IP range.
- B) Remove the authorized networks entry and require all connections to use the Cloud SQL Auth Proxy with IAM authentication.
- C) Change the authorized networks entry from `/24` to `/32` to restrict to a single IP address.
- D) Enable SSL certificate verification for all connections to the Public IP endpoint.

Correct Answer: A — Switching to Private IP removes the public internet endpoint entirely, eliminating the exposure of the database to internet-based attacks. This is the most comprehensive reduction of attack surface. Option B is also a valid improvement but still leaves the public IP accessible to anyone who can attempt an IAM-authenticated connection.

Distractor analysis: The question asks for the changes that most reduce attack surface. A is the best single answer because Private IP eliminates the public endpoint entirely. B is a valid answer but technically the Auth Proxy still uses the public endpoint unless Private IP is also configured. C is incorrect because narrowing the authorized network to /32 reduces the allowed source IP range but does not remove the public endpoint. D is incorrect because SSL verification protects data in transit but does not reduce network-level attack surface; the endpoint remains publicly accessible.

---

Reference: cloud.google.com/learn
