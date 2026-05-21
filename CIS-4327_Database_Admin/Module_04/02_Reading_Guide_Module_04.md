# Reading Guide: Module 04 - Cloud Spanner – Globally Distributed Databases
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 04 - Cloud Spanner – Globally Distributed Databases**! This week you will study Google Cloud Spanner, a service that is unique in the industry: a fully managed, globally distributed, relational database that provides both horizontal scalability and strong external consistency (ACID compliance across regions). Understanding when and why to choose Spanner over Cloud SQL is one of the most important decision points on the GCP Professional Cloud Database Engineer exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud Spanner**: A fully managed, globally distributed relational database service that delivers >99.999% availability and horizontal scalability while maintaining strong ACID consistency. Unlike Cloud SQL, which is limited to a single region, Spanner replicates data across multiple regions simultaneously, making it appropriate for global applications that cannot tolerate regional failure.
*   **TrueTime**: Google's globally synchronized clock infrastructure that uses GPS receivers and atomic clocks in every data center. TrueTime gives Spanner an upper bound on clock uncertainty across nodes worldwide, which is the mechanism that enables Spanner to guarantee externally consistent (serializable) transactions across geographically distributed replicas without a central lock manager.
*   **Interleaved Tables**: A Spanner-specific physical schema design where child table rows are stored on the same storage split as their parent row. Declared using `INTERLEAVE IN PARENT table_name ON DELETE CASCADE`, interleaving dramatically reduces the cost of parent-child JOIN queries by eliminating cross-split remote reads. This concept is a frequent exam topic.
*   **Processing Units (PUs) and Nodes**: Spanner compute capacity is measured in Processing Units (100 PUs = 0.1 Node; 1,000 PUs = 1 Node). You scale read and write throughput by adding Processing Units, not by resizing an instance. The exam may ask you to calculate how many nodes are needed for a given throughput requirement.
*   **Stale Reads**: Spanner offers the option to read data that may be up to a specified number of seconds old (bounded staleness) or as of an exact timestamp. Stale reads avoid acquiring read locks and are significantly faster and cheaper than strong reads. They are appropriate for analytics and reporting that do not need real-time consistency.

---

### 2. Certification Exam Tips
*   **Cloud SQL vs. Cloud Spanner Decision**: This is the most common Spanner exam question type. Choose Cloud SQL for: single-region workloads, lift-and-shift migrations, and cost-sensitive applications. Choose Cloud Spanner for: global users, >99.999% availability SLAs, horizontal write scaling beyond what a single Cloud SQL instance can support, and multi-region ACID transactions.
*   **Interleaving vs. Indexing**: Know that Spanner secondary indexes are global by default (stored across all splits) and that interleaving is the performance technique for hierarchical parent-child data. The exam distinguishes between creating an index and interleaving a table — they solve different access patterns.
*   **TrueTime and Consistency**: Expect at least one question about how Spanner achieves external consistency across regions. The answer always involves TrueTime — not traditional 2-phase locking or a primary-replica topology.
*   **Hotspot Prevention**: Spanner splits data across servers by key range. Sequential (monotonically increasing) primary keys like auto-increment IDs cause all new writes to land on the same split (a hotspot). Use UUIDs, bit-reversed sequences, or hash prefixes to distribute writes evenly.
*   **Study Resource:** The official Google Cloud Spanner documentation is the authoritative exam resource: [Cloud Spanner Documentation – Google Cloud](https://cloud.google.com/spanner/docs). The freeCodeCamp SQL course reinforces the relational and SQL fundamentals that Spanner builds on: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to solidify the relational concepts (schemas, keys, joins) that Spanner extends to a globally distributed context: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This free lecture reinforces the SQL and relational fundamentals that you will apply when working with Cloud Spanner's SQL interface: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will create a Cloud Spanner instance, define a schema with an interleaved parent-child table relationship, insert data, run queries using both strong reads and bounded-staleness stale reads, and observe the performance difference.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the relevant chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the SQL fundamentals lecture in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the Cloud Spanner schema design steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
