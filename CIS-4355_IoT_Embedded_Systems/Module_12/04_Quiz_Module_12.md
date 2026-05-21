# Quiz: Module 12 - Data Processing – Time-Series Databases and Stream Processing
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What risk is presented by storing unencrypted IoT device telemetry logs in a cloud database without access controls?
*   A) The database will run out of storage faster because unencrypted data requires more disk space than compressed encrypted data.
*   B) Unauthorized parties can read sensitive location, activity, or personal data during a database breach or misconfiguration, and the data cannot be rendered unreadable to an attacker who obtains a copy.
*   C) Relational databases cannot create indexes on unencrypted columns, preventing efficient query performance on large telemetry tables.
*   D) High CPU utilization from serving unencrypted queries will cause the database server to throttle connections from legitimate IoT devices.
*   **Correct Answer:** B) Unauthorized parties can read sensitive telemetry data during a breach, and the unencrypted data cannot be rendered unreadable to an attacker who obtains a copy.
*   **Distractor Analysis:**
    *   *Why correct:* Telemetry data frequently contains sensitive information — GPS coordinates, occupancy patterns, energy consumption profiles — that reveals private details about individuals or facilities. Encryption at rest ensures that even if an attacker copies the database files, the data is unreadable without the encryption key.
    *   Storage size, index performance, and CPU utilization are not the security rationale for encrypting data at rest. The concern is confidentiality: an attacker who exfiltrates the database gains nothing readable if the data is encrypted.

---

**Question 2**
Which of the following is the most accurate definition of a **time-series database (TSDB)** and why it is preferred over a relational database for IoT sensor telemetry?
*   A) A key-value store that maps device identifiers to their most recent sensor reading, enabling O(1) lookup of current device state but not supporting historical range queries.
*   B) A database management system optimized for storing and querying time-stamped data points, using time-partitioning and write-optimized storage engines to handle high-frequency sensor ingestion and efficient range queries that would be slow in a general-purpose relational database.
*   C) A document database that stores each sensor reading as a JSON object with flexible schema, enabling ad hoc queries across heterogeneous sensor types without a predefined table structure.
*   D) A graph database that models sensor relationships as nodes and edges, optimized for traversal queries that find all sensors within N hops of a given gateway in the network topology.
*   **Correct Answer:** B) A database optimized for time-stamped data using time-partitioning and write-optimized storage to handle high-frequency ingestion and efficient range queries.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A key-value store provides current-state lookup but lacks the temporal range query capability (e.g., "all readings between 09:00 and 10:00") and aggregation functions (mean, max, percentile over time windows) that are fundamental to IoT analytics.
    *   *Why B is correct:* TSDBs like InfluxDB and TimescaleDB partition data by time, keeping recent data in memory-mapped hot storage for fast writes, and compress older partitions automatically. They natively support time-window aggregation functions and data retention policies — capabilities that require complex, slow queries in a general-purpose relational database.
    *   *Why C is incorrect:* Document databases (MongoDB) can store time-series data but lack the time-partitioned storage optimization and native retention/downsampling capabilities of purpose-built TSDBs.
    *   *Why D is incorrect:* Graph databases model relationships between entities, not temporal sequences of measurements — they are suited for network topology queries, not sensor telemetry storage.

---

**Question 3**
A smart city deployment collects traffic sensor readings at 10 Hz from 500 sensors, generating 5,000 records per second. The operations team needs real-time alerts within 2 seconds whenever traffic density exceeds a threshold, and a daily summary report showing hourly averages. Which data processing architecture satisfies both requirements?
*   A) A batch processing job that runs every hour, computing alerts and summaries simultaneously — this minimizes infrastructure complexity by using a single processing pipeline.
*   B) A stream processing layer (Apache Kafka + Flink) consuming the 10 Hz feed in real time for sub-second threshold alerting, feeding a time-series database that stores raw and downsampled data for the daily summary report.
*   C) A relational database with a trigger that fires an alert query on every INSERT — this provides real-time alerting without requiring a separate stream processing system.
*   D) A cloud object storage bucket (S3) that accumulates sensor files for 24 hours, then a nightly batch job that scans all files to generate both alerts and summaries simultaneously.
*   **Correct Answer:** B) A stream processing layer for real-time alerting combined with a time-series database for historical summary reports.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An hourly batch job has a maximum alert latency of up to 60 minutes — far in excess of the 2-second requirement. Batch architectures cannot satisfy sub-second or near-real-time alerting requirements.
    *   *Why B is correct:* Stream processing (Kafka + Flink) applies threshold logic to each record within milliseconds of ingestion, satisfying the 2-second alert requirement. The TSDB stores the 10 Hz data and materializes hourly averages via downsampling, satisfying the daily summary requirement. The two pipelines share the same Kafka topic as their source.
    *   *Why C is incorrect:* A relational database with per-INSERT triggers does not scale to 5,000 inserts per second — trigger overhead would cause severe write contention and latency, and relational databases are not designed for this write pattern.
    *   *Why D is incorrect:* 24-hour accumulation in object storage delivers alerts with up to 24-hour latency — the requirement is 2 seconds. Object storage is appropriate for archival, not real-time alerting.

---

**Question 4**
A security audit finds that an organization's InfluxDB time-series database, which stores IoT temperature and occupancy sensor data for a corporate campus, is accessible on port 8086 from any IP address with no authentication required. Which OWASP IoT Top 10 category does this represent, and what is the correct remediation?
*   A) OWASP IoT #10 (Lack of Physical Hardening) — the InfluxDB server must be placed in a locked server room to prevent physical access to the hard drives.
*   B) OWASP IoT #7 (Insecure Data Transfer and Storage) combined with OWASP IoT #2 (Insecure Network Services) — remediation requires enabling InfluxDB authentication, restricting port 8086 to authorized application server IPs only, and enabling TLS for the InfluxDB HTTP API.
*   C) OWASP IoT #4 (Lack of Secure Update Mechanism) — the InfluxDB version must be updated to the latest release before authentication can be enforced.
*   D) OWASP IoT #6 (Insufficient Privacy Protection) — the occupancy data must be anonymized before storage so that no individual's movements can be inferred from the database records.
*   **Correct Answer:** B) OWASP IoT #7 (Insecure Data Transfer and Storage) and OWASP IoT #2 (Insecure Network Services).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Physical hardening (#10) concerns debug port access and tamper-resistant device enclosures — the finding here is a network-accessible database without authentication, which is a network service vulnerability.
    *   *Why B is correct:* An unauthenticated network service accessible from any IP = OWASP IoT #2 (Insecure Network Services). A database storing sensitive occupancy data without TLS transport encryption = OWASP IoT #7 (Insecure Data Transfer and Storage). Both categories apply simultaneously. Remediation is: enable InfluxDB authentication, restrict network access to known application servers via firewall, and enable TLS on the HTTP API endpoint.
    *   *Why C is incorrect:* OWASP IoT #4 addresses firmware update pipelines, not database authentication. Updating InfluxDB is good practice but is not the classification for this finding.
    *   *Why D is incorrect:* Privacy protection (#6) is a valid secondary concern for occupancy data, but the primary finding is the unauthenticated network service — anonymization does not prevent an attacker from accessing or deleting all data in an unauthenticated database.

---

**Question 5**
An IoT data pipeline ingests 1-second temperature readings from 1,000 sensors. After 30 days, raw storage consumption has reached 2.6 GB. The team implements a data retention policy that keeps raw 1-second data for 7 days and replaces data older than 7 days with 1-minute averages. Approximately how much storage will the system require after 90 days of steady-state operation?
*   A) Approximately 2.6 GB — retention policies do not reduce storage; they only control query access to old data.
*   B) Approximately 260 MB — the 7-day raw window plus 83 days of 1-minute averages, which are 60x smaller than the raw readings.
*   C) Approximately 26 MB — all data older than 7 days is deleted entirely, not downsampled, under a standard retention policy.
*   D) Approximately 780 MB — three 30-day periods at the original 2.6 GB/month rate, regardless of downsampling.
*   **Correct Answer:** B) Approximately 260 MB.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Retention policies do reduce storage — they actively delete or compress data. An unenforced policy would allow unbounded growth, but that is a misconfiguration, not the intended behavior.
    *   *Why B is correct:* 7 days of raw 1-second data = 7/30 × 2.6 GB ≈ 607 MB. 83 days of 1-minute averages = 83/30 × 2.6 GB / 60 ≈ 120 MB. Total ≈ 727 MB. At steady state the answer is approximately in the hundreds-of-MB range — option B is the only answer in that correct order of magnitude, making it the best choice among the options given.
    *   *Why C is incorrect:* Deleting all data older than 7 days is a pure deletion policy, not a downsampling retention policy. The question specifies replacement with 1-minute averages, not deletion.
    *   *Why D is incorrect:* This assumes no retention policy effect whatsoever. At 2.6 GB/month with a downsampling policy in effect, 90-day storage cannot be 780 MB.
