# Quiz: Module 08 — Managed Databases on GCP

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

Your team needs a relational database for a retail application. The application currently
runs in a single US region and serves around 500 concurrent users. The team is familiar
with PostgreSQL. Which GCP service is the most appropriate choice?

- A) Cloud Spanner
- B) Cloud SQL for PostgreSQL
- C) Cloud Bigtable
- D) Cloud Firestore

Correct answer: B — Cloud SQL for PostgreSQL is the right choice for a single-region
relational workload with existing PostgreSQL expertise. Cloud Spanner is global and
significantly more expensive — overkill for a single-region application. Bigtable and
Firestore are NoSQL, not relational.

---

### Question 2

A global financial services company needs a relational database that supports ACID
transactions, scales horizontally across multiple continents, and provides a 99.999% SLA.
Which service should they use?

- A) Cloud SQL with read replicas in multiple regions
- B) Cloud Bigtable with multi-cluster replication
- C) Cloud Spanner with a multi-region configuration
- D) Cloud Firestore with multi-region replication

Correct answer: C — Cloud Spanner multi-region provides globally distributed ACID
transactions, horizontal scaling, and a 99.999% SLA. Cloud SQL is regional only and
cannot provide global strong consistency. Bigtable does not support ACID transactions.
Firestore is a document store, not a relational database.

---

### Question 3

You are building a mobile application that needs to synchronize data in real time between
the server and mobile clients, support offline operation, and scale automatically without
provisioning servers. Which database service best fits these requirements?

- A) Cloud SQL
- B) Cloud Spanner
- C) Cloud Bigtable
- D) Cloud Firestore in Native mode

Correct answer: D — Firestore Native mode provides real-time listeners that push updates
to connected clients, built-in offline support in the mobile SDKs, and fully serverless
automatic scaling. No other GCP database provides native real-time sync and offline
support.

---

### Question 4

Your company collects IoT sensor readings from 10 million devices at a rate of 2 million
writes per second. Each reading includes a device ID, timestamp, and sensor value. The
data must be retained for 2 years and queried by device ID and time range. Which service
is designed for this workload?

- A) Cloud SQL
- B) Cloud Spanner
- C) Cloud Bigtable
- D) Memorystore

Correct answer: C — Bigtable is designed for high-throughput, low-latency wide-column
workloads at petabyte scale. IoT time-series data with high write rates and row-key-based
queries is the canonical Bigtable use case. Cloud SQL and Spanner cannot handle millions
of writes per second at this scale. Memorystore is an in-memory cache, not persistent
storage.

---

### Question 5

A team wants to reduce the number of repeated database queries hitting their Cloud SQL
instance. Many API responses are identical for several minutes. Which service should they
add to the architecture to cache these responses?

- A) Cloud Bigtable
- B) Memorystore for Redis
- C) Cloud Spanner
- D) Cloud Firestore

Correct answer: B — Memorystore for Redis is the correct caching layer. It provides
sub-millisecond key-value reads, supports TTL-based expiration, and is accessible via
private IP from the same VPC as the Cloud SQL instance. The other options are primary
databases, not caching layers.

---

### Question 6

A developer is creating a Cloud SQL instance for a production application and needs
automatic failover to a standby in a different availability zone. Which availability type
must be selected?

- A) ZONAL
- B) REGIONAL
- C) MULTI-REGION
- D) HIGH\_AVAILABILITY

Correct answer: B — `REGIONAL` availability type creates a Cloud SQL HA configuration
with a standby instance in a different zone within the same region and enables automatic
failover. `ZONAL` is single-zone with no automatic failover. `MULTI-REGION` and
`HIGH_AVAILABILITY` are not valid Cloud SQL availability type values.

---

### Question 7

Which statement about Cloud SQL shared-core tiers (db-f1-micro, db-g1-small) is correct?

- A) They support high availability with automatic failover
- B) They are excluded from the Cloud SQL SLA
- C) They are recommended for production read replicas
- D) They support up to 64 TB of SSD storage

Correct answer: B — Shared-core Cloud SQL tiers are excluded from the Cloud SQL SLA and
are intended for development and testing only. They do not support high availability
configurations. Production workloads must use dedicated-core tiers to be covered by the
SLA.

---

### Question 8

You need to connect an application running on a Compute Engine VM to a Cloud SQL instance
securely without using a public IP address on the database. Which connection method(s)
should you use?

- A) Authorized networks with the VM's external IP
- B) Cloud SQL Auth Proxy on the VM connecting over the internal network
- C) Cloud SQL direct private IP via VPC peering
- D) Both B and C are valid secure private connection methods

Correct answer: D — Both the Cloud SQL Auth Proxy (which uses IAM authentication and
encrypts the connection over the internal network) and a private IP connection via VPC
peering are valid secure methods that avoid a public IP on the Cloud SQL instance. The
Auth Proxy is the most commonly tested method on the ACE exam.

---

### Question 9

What unit is used to measure compute capacity in Cloud Spanner, and how many of these
units equal one node?

- A) Virtual CPUs (vCPUs); 4 vCPUs = 1 node
- B) Processing Units (PUs); 1000 PUs = 1 node
- C) Capacity Units (CUs); 100 CUs = 1 node
- D) Instance Units (IUs); 500 IUs = 1 node

Correct answer: B — Cloud Spanner uses Processing Units (PUs) to measure compute
capacity. 1000 PUs equals 1 node. You can provision in 100 PU increments for
single-region configurations, starting at 100 PUs.

---

### Question 10

A Memorystore for Redis instance must be accessed by an application running on a Compute
Engine VM. Which statement correctly describes how the application connects?

- A) The application connects to a public IP address assigned to the Redis instance
- B) The application connects via private IP within the same authorized VPC network
- C) The application uses Cloud SQL Auth Proxy to connect to Memorystore
- D) The application connects via Cloud Interconnect to the Redis endpoint

Correct answer: B — Memorystore instances have no public IP. They are only accessible
via private IP within an authorized VPC network. The Compute Engine VM must be in the
same VPC (or a peered network) as the Memorystore instance. Cloud SQL Auth Proxy is
specific to Cloud SQL and does not apply to Memorystore.

---

### Question 11 (5 points)

You need to perform a point-in-time recovery on a Cloud SQL for PostgreSQL
instance, restoring it to a state from 3 hours ago. Which Cloud SQL feature
enables this?

- A) On-demand backup taken 3 hours ago
- B) Automated backup combined with binary logging / write-ahead log replay
   (point-in-time recovery)
- C) Read replica promotion to the state it had 3 hours ago
- D) Exporting the database to Cloud Storage every 3 hours

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) On-demand backups capture a full snapshot at a specific moment; restoring to a point between two backups requires transaction log replay, not just a backup.
  - C) Read replicas are continuously synchronized with the primary and do not retain historical states; they cannot be rolled back to a past point in time.
  - D) Exporting to Cloud Storage creates a logical dump file; it does not support sub-minute point-in-time recovery and requires manual import to restore.

---

### Question 12 (5 points)

A Cloud Spanner instance is configured in a single region. The SLA for a
single-region Spanner configuration is 99.99%. What configuration provides
a 99.999% SLA?

- A) Increase the number of processing units from 1000 to 3000
- B) Enable Spanner's high-availability mode via the `--ha` flag
- C) Configure a multi-region Spanner instance spanning multiple continents
- D) Add a read replica in a second region

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Increasing processing units scales compute capacity but does not change the SLA tier; the SLA improvement requires geographic distribution of replicas.
  - B) There is no `--ha` flag for Cloud Spanner; high availability is determined by the instance configuration (single-region vs. multi-region).
  - D) Cloud Spanner read replicas are a feature of multi-region configurations, not an add-on to a single-region instance; the full multi-region configuration is required for the 99.999% SLA.

---

### Question 13 (5 points)

What is the Firestore Native mode feature that distinguishes it from
Datastore mode?

- A) Native mode supports SQL queries; Datastore mode does not
- B) Native mode provides real-time listeners that push document updates
   to connected clients; Datastore mode does not support real-time updates
- C) Native mode supports larger document sizes (10 MB vs. 1 MB in Datastore)
- D) Native mode stores data in JSON format; Datastore mode uses binary
   encoding

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Neither Firestore mode supports SQL; both use the Firestore query API with structured filters and indexes.
  - C) Both Firestore modes have the same 1 MB document size limit; document size is not the distinguishing feature.
  - D) Both modes use the same underlying Firestore storage format; the encoding is not user-visible and is not the distinguishing feature.

---

### Question 14 (5 points)

A developer configures a Cloud Bigtable cluster with 3 nodes. The workload
unexpectedly increases and latency rises. What is the fastest way to reduce
latency?

- A) Redesign the row key schema to reduce hotspotting
- B) Add more nodes to the cluster — Bigtable scales linearly with node count
- C) Enable Bigtable's automatic caching tier
- D) Migrate to Cloud Spanner for better horizontal scaling

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Redesigning the row key schema is the right fix for hotspotting-induced latency, but it requires application changes and is not the fastest approach to reduce latency for a general throughput increase.
  - C) Bigtable does not have a separate automatic caching tier as a configuration option; caching is handled internally.
  - D) Migrating to Cloud Spanner is a major architectural change that takes significant time; adding nodes to an existing Bigtable cluster takes effect in minutes.

---

### Question 15 (5 points)

A Cloud SQL for MySQL instance has automated backups enabled with a 7-day
retention period. Today is day 8. Are backups from day 1 available for
restoration?

- A) Yes — automated backups are retained indefinitely
- B) No — the day 1 backup is automatically deleted after 7 days
- C) Yes — backups are retained for 7 days plus a 30-day grace period
- D) No — Cloud SQL only retains the single most recent backup

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Automated backups are deleted after the configured retention period; "indefinitely" would require on-demand backups, which are not automatically deleted.
  - C) There is no 30-day grace period for automated backups; the retention period is fixed as configured (7 days in this scenario).
  - D) Cloud SQL retains multiple automated backups up to the configured retention count (typically 7); it is not limited to a single backup.

---

### Question 16 (5 points)

You need to connect an on-premises application to Cloud SQL without
exposing the database over the public internet. The on-premises environment
connects to GCP via Cloud Interconnect. What is the recommended connection
approach?

- A) Use the Cloud SQL Auth Proxy running on-premises connecting via the
   Cloud Interconnect private IP
- B) Enable a public IP on Cloud SQL and use SSL certificates for encryption
- C) Use a VPN tunnel directly from the on-premises application to Cloud SQL
- D) Export Cloud SQL data to Cloud Storage and have the on-premises app
   read from there

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Enabling a public IP exposes the database to the internet, violating the requirement for no public internet exposure; this approach also requires managing authorized network IP ranges.
  - C) Cloud Interconnect already provides a private dedicated connection; adding a VPN tunnel on top is redundant and adds unnecessary complexity.
  - D) Reading from Cloud Storage does not provide the live query capability a connected database application requires; this is a data export pattern, not a connectivity solution.

---

### Question 17 (5 points)

Cloud Bigtable row keys should NOT start with a monotonically increasing
timestamp. Why?

- A) Timestamps are not valid row key characters in Bigtable
- B) Monotonically increasing keys cause sequential writes to route to the
   same tablet server, creating a hotspot that limits throughput
- C) Bigtable automatically reverses timestamps, making lookups incorrect
- D) Timestamps exceeding 64 bits cause row key overflow errors

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Timestamps are valid row key values; they can be used as part of a row key if ordered appropriately (e.g., reversed timestamp to achieve descending time order).
  - C) Bigtable does not automatically reverse timestamps; the developer must reverse them explicitly if descending time order is desired to avoid hotspotting.
  - D) There is no 64-bit overflow concern for row keys; row keys are arbitrary byte strings up to 4 KB in length.

---

### Question 18 (5 points)

What is the maximum number of databases allowed per Cloud SQL instance?

- A) 1 — each Cloud SQL instance can contain only one database
- B) Unlimited — Cloud SQL supports any number of databases per instance
- C) 100 databases per instance for MySQL; varies by edition for PostgreSQL
- D) The limit depends on the instance tier (machine type)

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud SQL instances support multiple databases (equivalent to schemas); a single instance can host many databases for different applications.
  - C) While there are practical performance considerations for many databases on one instance, there is no hard documented limit of 100 for MySQL in Cloud SQL.
  - D) The number of databases is not limited by the machine tier; performance and storage are tier-dependent, but the database count limit is not.

---

### Question 19 (5 points)

A team uses Cloud Firestore in Native mode. They need to query all documents
in the `orders` collection where `status == "pending"` AND
`order_date < [30 days ago]`. After deploying this query, it fails with an
index error. What must be created?

- A) A single-field index on the `status` field
- B) A single-field index on the `order_date` field
- C) A composite index on `(status, order_date)` for the `orders` collection
- D) A manual index on the entire `orders` collection

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) A single-field index on `status` supports queries that filter on `status` alone but not compound queries combining `status` with `order_date` range filters.
  - B) A single-field index on `order_date` supports range queries on that field alone; the compound filter across two different fields requires a composite index.
  - D) "Manual index on the entire collection" is not a Firestore concept; Firestore uses per-query composite indexes defined by field path and query direction.

---

### Question 20 (5 points)

Memorystore for Redis supports two service tiers: Basic and Standard. What
is the key operational difference?

- A) Basic tier supports Redis cluster mode; Standard tier is single-node only
- B) Standard tier includes high availability with automatic failover to a
   replica; Basic tier is single-node with no replication
- C) Basic tier supports Redis 7.x; Standard tier is limited to Redis 6.x
- D) Standard tier stores data on persistent disk; Basic tier stores only
   in memory

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The Redis cluster mode (sharded) description is reversed; Basic is single-node and Standard adds HA with a replica, not cluster sharding.
  - C) Both Basic and Standard tiers support the same Redis version options; the tier choice does not determine Redis version.
  - D) Both tiers store data in memory (that is the nature of Redis); Standard tier adds an in-memory replica for high availability, not persistent disk storage.
