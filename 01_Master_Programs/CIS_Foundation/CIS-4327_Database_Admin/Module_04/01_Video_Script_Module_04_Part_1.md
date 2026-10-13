# Video Script: Module 04 — Cloud Spanner: Globally Distributed Databases (Part 1)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 13–15 minutes

---

### Opening

**[SHOW SLIDE: Module 04 — Cloud Spanner: Globally Distributed Databases]**

Hello, and welcome back to CIS-4327. I am Professor Nash. This is Module 04: Cloud Spanner.

Cloud Spanner is one of the most distinctive database technologies in the world. It is the only commercially available database that provides both full ACID transactions and horizontal scalability across a globally distributed infrastructure. Understanding what makes Spanner different — and when to use it versus Cloud SQL — is one of the most heavily tested topics on the GCP Database Engineer exam.

In Part 1 we cover Spanner's architecture, its consistency model, schema design, and the DDL syntax that differs from standard SQL. In Part 2 we cover DML, interleaved tables, secondary indexes, the Spanner query plan, and exam scenarios.

---

### Section 1 — Why Cloud Spanner Exists

**[SHOW SLIDE: The CAP theorem triangle — Consistency, Availability, Partition Tolerance]**

The traditional database engineering constraint is the CAP theorem: in a distributed system, you can have at most two of three properties — Consistency, Availability, and Partition Tolerance. Most distributed NoSQL databases choose availability and partition tolerance over strong consistency.

Cloud Spanner breaks this conventional trade-off using a combination of two innovations: TrueTime and Paxos consensus replication.

TrueTime is Google's globally synchronized clock infrastructure. It uses atomic clocks and GPS receivers in every Google data center to provide timestamps accurate to within a few milliseconds. By knowing the precise global time, Spanner can order transactions across regions without a central coordinator.

Paxos consensus replication means that every write to Spanner is replicated to a majority of nodes in the replica set before it is acknowledged as committed. This guarantees that even if a node fails, the committed data is safe and consistent.

Together, TrueTime and Paxos allow Spanner to offer what Google calls external consistency — a guarantee stronger than serializable isolation. Spanner transactions behave as if they execute on a single machine, even when spanning multiple continents.

---

### Section 2 — Cloud Spanner Architecture

**[SHOW SLIDE: Spanner instance hierarchy — instance, databases, tables, rows]**

A Cloud Spanner deployment has three layers.

An instance is the compute and storage resource allocation for Spanner. You configure the number of processing units (PUs) or nodes. One node provides approximately 2,000 QPS of reads and 1,000 QPS of writes.

A database lives within an instance. You can have multiple databases per instance.

Tables and rows are the standard relational constructs inside a database.

**[SHOW SLIDE: Single-region vs. multi-region Spanner configurations]**

Spanner offers two configuration types.

Regional configurations replicate data within a single GCP region across three zones. They provide 99.999% availability (five nines). This is appropriate for applications that need high availability without the latency of global replication.

Multi-region configurations replicate data across two or more regions. They provide 99.999% availability with geographic redundancy. They have slightly higher write latency because writes must achieve Paxos consensus across regions. Multi-region configurations are appropriate for truly global applications.

---

### Section 3 — Creating a Cloud Spanner Instance and Database

**[SHOW CONSOLE: Cloud Spanner Create Instance form]**

**[SHOW CODE]**

```bash
# Create a Spanner instance
gcloud spanner instances create txwes-spanner \
    --config=regional-us-central1 \
    --description="TXWES Lab Instance" \
    --processing-units=100

# Create a database within the instance
gcloud spanner databases create university_db \
    --instance=txwes-spanner
```

**[END CODE]**

Processing units (PUs) are the compute unit for Cloud Spanner. 1000 PUs equals one node. The minimum for testing is 100 PUs. For production workloads, scale based on your QPS requirements.

---

### Section 4 — Spanner DDL

**[SHOW SLIDE: Spanner DDL — similar to standard SQL with key differences]**

Spanner uses a SQL-like DDL for schema definition, but there are important differences from standard PostgreSQL or MySQL.

**[SHOW CODE]**

```sql
-- Create a parent table
CREATE TABLE Students (
    StudentId   INT64  NOT NULL,
    FullName    STRING(100) NOT NULL,
    Email       STRING(255) NOT NULL,
    EnrolledYear INT64  NOT NULL
) PRIMARY KEY (StudentId);

-- Create a child table interleaved in the parent
CREATE TABLE Courses (
    CourseId    INT64  NOT NULL,
    CourseCode  STRING(20) NOT NULL,
    CourseName  STRING(200) NOT NULL,
    Credits     INT64  NOT NULL
) PRIMARY KEY (CourseId);

-- Create an interleaved table (child physically co-located with parent)
CREATE TABLE Enrollments (
    StudentId   INT64  NOT NULL,
    CourseId    INT64  NOT NULL,
    EnrolledAt  TIMESTAMP NOT NULL,
    Grade       STRING(2)
) PRIMARY KEY (StudentId, CourseId),
  INTERLEAVE IN PARENT Students ON DELETE CASCADE;
```

**[END CODE]**

Key differences from standard SQL:

Data types: Spanner uses INT64, STRING(N), FLOAT64, BOOL, DATE, TIMESTAMP, BYTES(N), and JSON. There is no INTEGER or VARCHAR — these are Spanner-specific type names.

AUTO_INCREMENT does not exist in Spanner. You must manage primary key generation yourself, typically using UUID or a client-generated value. Auto-incrementing sequential integers are actively discouraged in Spanner because they create write hotspots — all new rows are written to the same tablet (storage shard), eliminating the benefit of horizontal scaling.

INTERLEAVE IN PARENT physically co-locates child table rows with their parent row in the same storage node. When Enrollments is interleaved in Students, all enrollment rows for StudentId 42 are stored on the same physical server as the Student 42 row. Queries that read a student and all their enrollments require no cross-server network hops.

---

### Section 5 — Primary Key Design in Spanner

**[SHOW SLIDE: Hot-spotting diagram — sequential keys all going to one tablet; UUID keys distributed across tablets]**

Primary key design is critical in Cloud Spanner. Poor key choice creates write hotspots that negate the scaling benefits of Spanner's distributed architecture.

A hotspot occurs when new rows are consistently written to the same Spanner tablet because their keys are sequential. If you use an auto-incrementing integer as a primary key, every INSERT goes to the tablet holding the highest-valued key range. That one tablet becomes a bottleneck regardless of how many nodes you have.

The recommended approaches to avoid hotspots:

Use UUID (random) primary keys. Rows are distributed randomly across tablets.

Use bit-reversed sequential IDs. Reverse the bits of a sequential number to distribute the write pattern while maintaining approximate ordering.

Use a hash prefix. Prepend a hash of the natural key to the primary key to distribute writes.

Use composite keys that distribute naturally. (region, timestamp) distributes writes by region before timestamp, spreading load across tablets.

---

### Section 6 — Spanner vs. Cloud SQL — When to Use Each

**[SHOW SLIDE: Decision criteria table — Cloud SQL vs. Cloud Spanner]**

This is the most important decision framework for the GCP exam.

| Criterion | Cloud SQL | Cloud Spanner |
|---|---|---|
| Geographic scope | Single region | Single region or global |
| Scaling | Vertical (bigger machine) | Horizontal (add nodes) |
| ACID transactions | Full ACID | Full ACID, globally |
| Maximum storage per instance | 64 TB | Unlimited |
| Failover time | ~60 seconds | Near-zero |
| Cost | Lower | Significantly higher |
| SQL compatibility | Standard MySQL/PostgreSQL | Spanner SQL (ANSI SQL with extensions) |
| Best for | Regional OLTP, lift-and-shift | Global OLTP, financial systems, gaming |

The decision rule for the exam: if the scenario requires global consistency and horizontal scaling, the answer is Cloud Spanner. If the scenario describes a regional workload with existing MySQL or PostgreSQL code, the answer is Cloud SQL.

---

### Closing — Part 1 Summary

**[SHOW SLIDE: Module 04 Part 1 key concepts]**

In Part 1 we covered Cloud Spanner's architecture: TrueTime for global timestamp ordering, Paxos replication for consistency, and the instance-database-table hierarchy.

We covered Spanner DDL: Spanner-specific data types, the absence of AUTO_INCREMENT, and the INTERLEAVE IN PARENT directive for physical co-location.

We covered primary key design: why sequential keys create hotspots and the four strategies to avoid them.

In Part 2 we cover Spanner DML, secondary indexes, reading with staleness bounds, and the exam scenarios that test Cloud SQL vs. Cloud Spanner selection.

See you in Part 2.

---

Reference: cloud.google.com/learn
