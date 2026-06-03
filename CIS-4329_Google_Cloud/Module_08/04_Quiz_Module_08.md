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
