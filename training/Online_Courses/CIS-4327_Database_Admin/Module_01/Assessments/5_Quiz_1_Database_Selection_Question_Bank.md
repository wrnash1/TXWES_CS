### 5. Quiz 1: Database Selection (Question Bank)
**Question 1**
Your company is developing a multiplayer mobile game that requires user profiles to be stored as JSON documents. The app needs to support offline synchronization for mobile clients. Which Google Cloud database service is the most appropriate choice?
A) Cloud SQL
B) Cloud Spanner
C) Cloud Bigtable
D) Firestore
*   **Correct Answer:** D) Firestore
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud SQL is a relational SQL database, not designed for native JSON document storage or mobile offline sync.
    *   *Why B is incorrect:* Cloud Spanner is a global relational database, overkill and the wrong paradigm for simple mobile document syncing.
    *   *Why C is incorrect:* Bigtable is for massive analytical workloads and time-series data, not for mobile app backends with offline sync.

**Question 2**
You are migrating an on-premises PostgreSQL database to Google Cloud. The application serves users in a single geographic region and requires strong ACID consistency. Which service minimizes migration effort while meeting requirements?
A) Cloud SQL
B) Cloud Spanner
C) BigQuery
D) Firestore
*   **Correct Answer:** A) Cloud SQL
*   **Distractor Analysis:**
    *   *Why B is incorrect:* While Spanner supports PostgreSQL dialects, migrating to it requires architectural changes. Cloud SQL is a direct "lift and shift" for regional PostgreSQL.
    *   *Why C is incorrect:* BigQuery is an enterprise data warehouse for analytics, not an operational transactional (OLTP) database.
    *   *Why D is incorrect:* Firestore is a NoSQL document database, completely incompatible with a direct PostgreSQL migration.
